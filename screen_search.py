import win32gui
from utils import transform_coordinates
from sends import send_mouse
import macros
from time import sleep


def start_game(ahk, handle):
    x1, y1, x2, y2 = win32gui.GetWindowRect(handle)
    image_path = f'./images/start_game_{x2 - x1}_{y2 - y1}.png'
    x1, y1 = transform_coordinates(handle, 160, 500)
    x2, y2 = transform_coordinates(handle, 320, 540)
    found = ahk.image_search(image_path, (x1, y1), (x2, y2), 30)
    if found:
        print('FOUND START GAME!')
        send_mouse(handle, 'LM', x1, y1)


def open_rift(ahk, handle, rift_type):
    x1, y1, x2, y2 = win32gui.GetWindowRect(handle)
    image_path = f'./images/obelisk_{x2 - x1}_{y2 - y1}.png'
    x1, y1 = transform_coordinates(handle, 220, 30)
    x2, y2 = transform_coordinates(handle, 300, 100)
    found = ahk.image_search(image_path, (x1, y1), (x2, y2), 30)
    if found:
        print('FOUND OPEN RIFT!')
        if rift_type == 'grift':
            macros.open_gr()
        else:
            macros.open_rift()


def gamble(ahk, handle, item):
    x1, y1, x2, y2 = win32gui.GetWindowRect(handle)
    image_path = f'./images/kadala_{x2 - x1}_{y2 - y1}.png'
    x1, y1 = transform_coordinates(handle, 220, 30)
    x2, y2 = transform_coordinates(handle, 300, 100)
    found = ahk.image_search(image_path, (x1, y1), (x2, y2), 30)
    if found:
        print('FOUND Kadala!')
        macros.gamble(item)


def accept_gr(ahk, handle):
    x1, y1, x2, y2 = win32gui.GetWindowRect(handle)
    image_path = f'./images/keystone_{x2 - x1}_{y2 - y1}.png'
    x1, y1 = transform_coordinates(handle, 705, 755)
    x2, y2 = transform_coordinates(handle, 790, 815)
    found = ahk.image_search(image_path, (x1, y1), (x2, y2), 30)
    if found:
        print('FOUND accept GR')
        accept = transform_coordinates(handle, 800, 900)
        send_mouse(handle, 'LM', accept[0], accept[1])
