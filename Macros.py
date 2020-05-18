import win32api
from time import sleep
from sends import send_mouse, send_key, send_mousemove
import keyboard
import time


def right_click(handle):
    x, y = win32api.GetCursorPos()
    send_mouse(handle, 'RM', x, y)
    sleep(0.001)


def left_click(handle):
    x, y = win32api.GetCursorPos()
    send_mouse(handle, 'LM', x, y)
    sleep(0.001)


def cube_conv_sm(handle, fast):
    start = time.time()
    if not fast:
        try:
            for i in range(6):
                for j in range(10):
                    send_mouse(handle, 'RM', 1425 + j * 50, 580 + i * 50)  # Item
                    macro_sleep(0.1)
                    send_mouse(handle, 'LM', 710, 840)  # Fill
                    send_mouse(handle, 'LM', 250, 830)  # Transmute
                    macro_sleep(0.1)
                    send_mouse(handle, 'LM', 580, 850)  # Backwards
                    send_mouse(handle, 'LM', 850, 850)  # Forth
        except StopMacro:
            pass
    else:
        try:
            for _ in range(2):
                for i in range(6):
                    for j in range(10):
                        send_mouse(handle, 'RM', 1425 + j * 50, 580 + i * 50)  # Item
                        macro_sleep(0.03)  # 0.025
                        send_mouse(handle, 'LM', 710, 840)  # Fill
                        send_mouse(handle, 'LM', 250, 830)  # Transmute
                        macro_sleep(0.03)  # 0.025
                        send_mouse(handle, 'LM', 580, 850)  # Backwards
                        send_mouse(handle, 'LM', 850, 850)  # Forth
        except StopMacro:
            pass
    print(time.time() - start)


def cube_conv_lg(handle, fast):
    if not fast:
        try:
            for i in range(3):
                for j in range(10):
                    send_mouse(handle, 'RM', 1425 + j * 50, 580 + i * 2 * 50)  # Item
                    macro_sleep(0.1)  # 0.025
                    send_mouse(handle, 'LM', 710, 840)  # Fill
                    send_mouse(handle, 'LM', 250, 830)  # Transmute
                    macro_sleep(0.1)  # 0.025
                    send_mouse(handle, 'LM', 580, 850)  # Backwards
                    send_mouse(handle, 'LM', 850, 850)  # Forth
        except StopMacro:
            pass
    else:
        try:
            for _ in range(2):
                for i in range(3):
                    for j in range(10):
                        send_mouse(
                            handle, 'RM', 1425 + j * 50, 580 + i * 2 * 50
                        )  # Item
                        macro_sleep(0.03)  # 0.025
                        send_mouse(handle, 'LM', 710, 840)  # Fill
                        send_mouse(handle, 'LM', 250, 830)  # Transmute
                        macro_sleep(0.03)  # 0.025
                        send_mouse(handle, 'LM', 580, 850)  # Backwards
                        send_mouse(handle, 'LM', 850, 850)  # Forth
        except StopMacro:
            pass


def reforge(handle):
    send_mouse(handle, 'RM', 1425, 580)  # Item
    sleep(0.1)
    send_mouse(handle, 'LM', 710, 840)  # Fill
    send_mouse(handle, 'LM', 250, 830)  # Transmute
    sleep(0.1)
    send_mouse(handle, 'LM', 580, 850)  # Backwards
    send_mouse(handle, 'LM', 850, 850)  # Forth
    send_mousemove(handle, 1425, 580)


def gem_up(handle, empowered):
    send_mouse(handle, 'LM', 100, 640)
    sleep(0.1)
    if not empowered:
        try:
            for i in range(4):
                if i == 1:
                    send_key(handle, 't')
                send_mouse(handle, 'LM', 280, 550)
                macro_sleep(1.75)
        except StopMacro:
            pass
    else:
        try:
            for i in range(5):
                if i == 2:
                    send_key(handle, 't')
                send_mouse(handle, 'LM', 280, 550)
                macro_sleep(1.75)
        except StopMacro:
            pass


def salvage(handle):
    send_mouse(handle, 'LM', 517, 480)  # Salvage Menu
    send_mouse(handle, 'LM', 165, 295)  # Click Salvage Button

    for i in range(6):
        for j in range(9):
            send_mouse(handle, 'LM', 1477 + 50 * j, 585 + 50 * i)
            send_key(handle, 'enter')
            send_key(handle, 'enter')
    send_key(handle, 'esc')


def drop_inventory(handle):
    x, y = win32api.GetCursorPos()
    send_key(handle, 'c')
    for i in range(6):
        for j in range(9):
            send_mouse(handle, 'LM', 1477 + 50 * j, 585 + 50 * i)
            send_mouse(handle, 'LM', x, y)
    send_key(handle, 'c')


def open_gr(handle):
    send_mouse(handle, 'LM', 270, 480)
    send_mouse(handle, 'LM', 260, 850)


def leave_game(handle):
    send_key(handle, 'esc')
    send_mouse(handle, 'LM', 230, 475)


def port_a1(handle):
    send_key(handle, 'm')
    send_mouse(handle, 'LM', 895, 125)
    send_mouse(handle, 'LM', 740, 620)
    send_mouse(handle, 'LM', 1020, 485)


def lower_diff(handle):
    send_key(handle, 'esc')
    for i in range(19):
        send_mouse(handle, 'LM', 1700, 400)
        send_key(handle, 'enter')
    send_key(handle, 'esc')


class StopMacro(Exception):
    pass


def macro_sleep(time):
    for i in range(int(time * 100)):
        if keyboard.is_pressed('esc'):
            raise StopMacro
        else:
            sleep(0.008)
