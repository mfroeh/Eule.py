import os
import psutil
from time import sleep
from tkinter.messagebox import showwarning
import win32gui
import keyboard


def start_thirdparty(settings):
    process_names = [p.name() for p in psutil.process_iter()]
    try:
        if 'Diablo III64.exe' in process_names:
            if 'Fiddler.exe' not in process_names:
                start_fiddler(settings)
            if 'TurboHUD.exe' not in process_names:
                start_turbohud(settings)
            if 'pHelper.exe' not in process_names:
                start_pHelper(settings)
            # kill_process('Fiddler.exe')
        else:
            showwarning(
                'Diablo III not active', 'Please start Diablo III.',
            )
    except OSError:
        print('User interrupt starting Programms')
    print('Done')


def process_active(name):
    for process in psutil.process_iter():
        if process.name() == name:
            return True
    return False


def kill_process(name):
    for process in psutil.process_iter():
        if process.name() == name:
            print(f'{name}-Process found. Terminating it.')
            process.terminate()
            break


def watch_handle(listener, settings, DACTIVE):
    handle_lost = False
    while True:
        handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
        if not handle and not handle_lost:
            keyboard.remove_all_hotkeys()
            # showwarning(
            #     'Diablo III not active',
            #     'Diablo III is not started. Macros dont work outside Diablo.',
            # )
            DACTIVE.set(False)
            handle_lost = True
        elif handle and handle_lost:
            # showinfo('Diablo III active', 'Hook recived! Macros will work now!')
            listener.renew_handle(handle)
            listener.renew_listeners(settings)
            DACTIVE.set(True)
            handle_lost = False
        sleep(1)


def start_fiddler(settings):
    os.startfile(settings.paths['Fiddler'])
    while not process_active('Fiddler.exe'):
        sleep(0.5)


def start_turbohud(settings):
    os.startfile(settings.paths['TurboHUD'])
    sleep(2)
    thud_starting = win32gui.FindWindow(None, 'TurboHUD')
    while thud_starting:
        thud_starting = win32gui.FindWindow(None, 'TurboHUD')
        sleep(0.2)
    print('TurboHUD started!')


def start_pHelper(settings):
    os.startfile(settings.paths['pHelper'])
    while not process_active('pHelper.exe'):
        sleep(0.5)


def nice_name(name):
    switcher = {
        'cube_conv_sm': 'Cube Conv (Single Slot)',
        'cube_conv_lg': 'Cube Conv (Dual Slot)',
        'reforge': 'Reforge / Conv Set',
        'open_gr': 'Open Grift',
        'gem_up': 'Upgrade Gem',
        'leave_game': 'Leave Game',
        'salvage': 'Salvage',
        'drop_inventory': 'Drop Inventory',
        'right_click': 'Spam Right Click',
        'left_click': 'Spam Left Click',
        'port_a1': 'Port to A1',
        'lower_diff': 'Normalize Difficulty',
        'armor_swap': 'Swap Armor Cain',
        'pause': 'Pause Eule.py',
    }
    return switcher.get(name, 'Key not found!')


# Transforms from 1920x1080 Base
def transform_coordinates(handle, x, y):
    x1, y1, x2, y2 = win32gui.GetWindowRect(handle)
    w = x2 - x1
    h = y2 - y1
    new_x = (w / 1920) * x
    new_y = (h / 1080) * y
    return new_x, new_y
