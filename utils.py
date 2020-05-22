import os
import psutil
from time import sleep
from tkinter.messagebox import showwarning, showinfo
import win32gui
import ctypes


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
        if is_user_admin():
            if 'Diablo III64.exe' in process_names:
                if paths['Fiddler'] and 'Fiddler.exe' not in process_names:
                    start_Fiddler(paths['Fiddler'])
                if paths['TurboHUD'] and 'TurboHUD.exe' not in process_names:
                    start_TurboHUD(paths['TurboHUD'])
                if paths['pHelper'] and 'pHelper.exe' not in process_names:
                    sleep(1)
                    start_pHelper(paths['pHelper'])
            else:
                showwarning(
                    'Diablo III not active', 'Please start Diablo III.',
                )
        else:
            showinfo(
                'Administrator Privileges required.',
                'Please start Eule.py with Administrator Privileges to use the Third Party Launcher.',
            )
    except OSError:
        print('User interrupted starting Programms')
    print('Done')


def start_Fiddler(path):
    os.startfile(path)
    while not process_active('Fiddler.exe'):
        sleep(0.5)


def start_TurboHUD(path):
    os.startfile(path)
    sleep(2)
    thud_starting = win32gui.FindWindow(None, 'TurboHUD')
    while thud_starting:
        thud_starting = win32gui.FindWindow(None, 'TurboHUD')
        sleep(0.2)


def start_pHelper(path):
    os.startfile(path)
    while not process_active('pHelper.exe'):
        sleep(0.5)


def watch_handle(DACTIVE):
    while True:
        if win32gui.FindWindow('D3 Main Window Class', 'Diablo III'):
            DACTIVE.set(True)
        else:
            DACTIVE.set(False)
        sleep(1)


# Transforms from 1920x1080 Base
# Works for all 16 / 9 Resolutions
def transform_coordinates(handle, x, y):
    x1, y1, x2, y2 = win32gui.GetWindowRect(handle)
    w = x2 - x1
    h = y2 - y1
    new_x = int((w / 1920) * x)
    new_y = int((h / 1080) * y)
    return (new_x, new_y)


class AdminStateUnknownError(Exception):
    pass


def is_user_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        pass
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() == 1
    except AttributeError:
        raise AdminStateUnknownError
