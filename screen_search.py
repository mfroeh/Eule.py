import win32gui
from utils import transform_coordinates
from sends import send_mouse, send_key
import macros
import os
import sys
from numpy import array
import win32ui
from ctypes import windll
from PIL import Image
from cv2 import (
    cvtColor,
    imread,
    minMaxLoc,
    matchTemplate,
    TM_CCOEFF_NORMED,
    COLOR_BGR2GRAY,
)


try:
    wd = sys._MEIPASS
except AttributeError:
    wd = ''


def crop_image(image, *rect):
    return image.crop(x for x in rect)


def get_image(handle):
    # left, top, right, bot = win32gui.GetClientRect(hwnd)
    left, top, right, bot = win32gui.GetClientRect(handle)
    w = right - left
    h = bot - top

    hwndDC = win32gui.GetWindowDC(handle)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    saveDC.SelectObject(saveBitMap)

    windll.user32.PrintWindow(handle, saveDC.GetSafeHdc(), 0)

    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)

    im = Image.frombuffer(
        'RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1
    )
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(handle, hwndDC)

    return im


# Searches for an image inside of a source image
def image_search(image, src_img, precision=0.8):
    img_rgb = array(src_img)
    img_gray = cvtColor(img_rgb, COLOR_BGR2GRAY)
    template = imread(image, 0)

    res = matchTemplate(img_gray, template, TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = minMaxLoc(res)
    if max_val < precision:
        return False
    return True


########################################################################################


def start_game(screenshot, handle):
    x1, y1, x2, y2 = win32gui.GetClientRect(handle)
    img_to_find = os.path.join(wd, f'./images/{x2 - x1}_{y2 - y1}/start_game.png')
    x1, y1 = transform_coordinates(handle, 160, 500)
    x2, y2 = transform_coordinates(handle, 320, 540)
    img = crop_image(screenshot, x1, y1, x2, y2)
    if image_search(img_to_find, img, precision=0.8):
        print('FOUND START GAME!')
        send_mouse(handle, 'LM', x1, y1)


def open_rift(screenshot, handle, rift_type):
    x1, y1, x2, y2 = win32gui.GetClientRect(handle)
    img_to_find = os.path.join(wd, f'./images/{x2 - x1}_{y2 - y1}/obelisk.png')
    x1, y1 = transform_coordinates(handle, 220, 30)
    x2, y2 = transform_coordinates(handle, 300, 100)
    img = crop_image(screenshot, x1, y1, x2, y2)
    if image_search(img_to_find, img, precision=0.8):
        print('FOUND OPEN RIFT!')
        if rift_type == 'grift':
            macros.open_gr()
        else:
            macros.open_rift()


def gamble(screenshot, handle, item):
    x1, y1, x2, y2 = win32gui.GetClientRect(handle)
    img_to_find = os.path.join(wd, f'./images/{x2 - x1}_{y2 - y1}/kadala.png')
    x1, y1 = transform_coordinates(handle, 220, 30)
    x2, y2 = transform_coordinates(handle, 300, 100)
    img = crop_image(screenshot, x1, y1, x2, y2)
    if image_search(img_to_find, img, precision=0.8):
        print('FOUND Kadala!')
        macros.gamble(item)


# Probably wont work on none 16:9!
def accept_gr(screenshot, handle):
    x1, y1, x2, y2 = win32gui.GetClientRect(handle)
    img_to_find = os.path.join(wd, f'./images/{x2 - x1}_{y2 - y1}/keystone.png')
    x1, y1 = transform_coordinates(handle, 705, 755)
    x2, y2 = transform_coordinates(handle, 790, 815)
    accept = transform_coordinates(handle, 800, 900)
    img = crop_image(screenshot, x1, y1, x2, y2)
    if image_search(img_to_find, img, precision=0.8):
        print('FOUND accept GR')
        send_mouse(handle, 'LM', accept[0], accept[1])


def upgrade_gem(screenshot, handle):
    x1, y1, x2, y2 = win32gui.GetClientRect(handle)
    uhrsi = os.path.join(wd, f'./images/{x2 - x1}_{y2 - y1}/urhsi.png')
    x1, y1 = transform_coordinates(handle, 220, 30)
    x2, y2 = transform_coordinates(handle, 300, 100)
    img = crop_image(screenshot, x1, y1, x2, y2)
    if image_search(uhrsi, img, precision=0.8):
        x1, y1, x2, y2 = win32gui.GetClientRect(handle)
        images_to_find = [
            os.path.join(wd, f'./images/{x2 - x1}_{y2 - y1}/urhsi_upgrade_{i}.png')
            for i in range(1, 6)
        ]
        x1, y1 = transform_coordinates(handle, 270, 530)
        x2, y2 = transform_coordinates(handle, 355, 560)
        upgrade = transform_coordinates(handle, 280, 550)

        upgrade_img = crop_image(screenshot, x1, y1, x2, y2)

        if image_search(images_to_find[4], upgrade_img, precision=0.95):
            send_mouse(handle, 'LM', upgrade[0], upgrade[1])
            print('Found 5 Upgrades left!')
        elif image_search(images_to_find[3], upgrade_img, precision=0.95):
            send_mouse(handle, 'LM', upgrade[0], upgrade[1])
            print('Found 4 Upgrades Left!')
        elif image_search(images_to_find[2], upgrade_img, precision=0.95):
            send_mouse(handle, 'LM', upgrade[0], upgrade[1])
            send_key(handle, 't')
            print('Found 3 Upgrades Left!')
        elif image_search(images_to_find[1], upgrade_img, precision=0.95):
            send_mouse(handle, 'LM', upgrade[0], upgrade[1])
            send_key(handle, 't')
            print('Found 2 Upgrades Left!')
        elif image_search(images_to_find[0], upgrade_img, precision=0.95):
            send_mouse(handle, 'LM', upgrade[0], upgrade[1])
            send_key(handle, 't')
            print('Found 1 Upgrades Left!')
