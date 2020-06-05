import os
import psutil
from time import sleep
import win32gui
import ctypes
from PyQt5.QtWidgets import QMessageBox
import keyboard


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


def start_thirdparty(paths):
    process_names = [p.name() for p in psutil.process_iter()]
    try:
        if 'Diablo III64.exe' in process_names:
            if paths['Fiddler'] and 'Fiddler.exe' not in process_names:
                start_Fiddler(paths['Fiddler'])
            if paths['TurboHUD'] and 'TurboHUD.exe' not in process_names:
                start_TurboHUD(paths['TurboHUD'])
            if paths['pHelper'] and 'pHelper.exe' not in process_names:
                start_pHelper(paths['pHelper'])
        else:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.setWindowTitle('Diablo III isnt running')
            error_dialog.setText('Please start Diablo III.')
            error_dialog.exec_()
    except OSError:
        print('User interrupted starting Programms')
    print('Done')


def start_Fiddler(path):
    os.startfile(path)
    while not process_active('Fiddler.exe'):
        sleep(0.5)


def start_TurboHUD(path):
    os.startfile(path)
    if not user_is_admin():
        # While TurboHUD hasnt started
        while not win32gui.FindWindow(None, 'TurboHUD'):
            sleep(0.2)
            print('THUD wasnt started yet')
    sleep(2)
    # While TurboHUD hasnt fully loaded
    while win32gui.FindWindow(None, 'TurboHUD'):
        sleep(0.2)
        print('THUD is loading')
    print('THUD has loaded!')


def start_pHelper(path):
    os.startfile(path)
    while not process_active('pHelper.exe'):
        sleep(0.5)


def set_status(diablo_hooked, eule_paused, listener):
    while True:
        diablo_hooked.setChecked(
            win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
        )
        print(listener.paused)
        eule_paused.setChecked(listener.paused)
        sleep(0.5)


# Transforms from 1920x1080 Base
# Works for all 16 / 9 Resolutions
def transform_coordinates(handle, x, y, rel='left'):
    x1, y1, x2, y2 = win32gui.GetClientRect(handle)  # win32gui.GetWindowRect(handle)
    w = x2 - x1
    h = y2 - y1

    if rel == 'left':
        new_x = int((h / 1080) * x)
    elif rel == 'right':
        new_x = int(w - (1920 - x) * h / 1080)
    else:
        new_x = int(x * h / 1080 + (w - 1920 * h / 1080) / 2)
    new_y = int((h / 1080) * y)

    return (new_x, new_y)


class AdminStateUnknownError(Exception):
    pass


def user_is_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        pass
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() == 1
    except AttributeError:
        raise AdminStateUnknownError


def hotkey_delete_request(hotkey):
    try:
        scan_codes = keyboard.key_to_scan_codes(hotkey)
        return scan_codes[0] == 83
    except:
        return False


def hotkey_is_numlock(hotkey):
    try:
        scan_code = keyboard.key_to_scan_codes(hotkey)[1]
        return scan_code in [71, 72, 73, 75, 76, 77, 79, 80, 81, 82]
    except:
        return False


def nicer_text(hotkey):
    switcher = {
        82: 'Num0',
        79: 'Num1',
        80: 'Num2',
        81: 'Num3',
        75: 'Num4',
        76: 'Num5',
        77: 'Num6',
        71: 'Num7',
        72: 'Num8',
        73: 'Num9',
    }
    return switcher.get(hotkey, hotkey)
