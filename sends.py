import win32api
import win32con
from ressources import key_to_hex


def send_key(handle, key):
    win32api.PostMessage(handle, win32con.WM_KEYDOWN, key_to_hex(key), 0)
    win32api.PostMessage(handle, win32con.WM_KEYUP, key_to_hex(key), 0)


def send_mouse(handle, key, x, y):
    lParam = y << 16 | x
    if key == 'LM':
        win32api.PostMessage(
            handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam
        )
        win32api.PostMessage(handle, win32con.WM_LBUTTONUP, 0, lParam)
    elif key == 'RM':
        win32api.PostMessage(
            handle, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, lParam
        )
        win32api.PostMessage(handle, win32con.WM_RBUTTONUP, 0, lParam)


def send_mouse_shift(handle, key, x, y):
    send_key_down(handle, 'shift')
    send_mouse(handle, key, x, y)
    send_key_up(handle, 'shift')


def send_mousemove(handle, x, y):
    lParam = y << 16 | x
    win32api.PostMessage(handle, win32con.WM_MOUSEMOVE, 0, lParam)


def send_key_down(handle, key):
    win32api.PostMessage(handle, win32con.WM_KEYDOWN, key_to_hex(key), 0)


def send_key_up(handle, key):
    win32api.PostMessage(handle, win32con.WM_KEYUP, key_to_hex(key), 0)


# Sends text to a Window
def send_message(handle, message):
    for c in message:
        win32api.PostMessage(handle, win32con.WM_KEYUP, key_to_hex(c), 0)
