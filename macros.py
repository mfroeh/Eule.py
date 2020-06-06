import win32api
import win32gui
from time import sleep
from sends import send_mouse, send_key, send_mousemove, send_key_down, send_key_up
import keyboard
from utils import transform_coordinates
from ressources import (
    map_act_coords_by_act,
    map_town_coords_by_act,
    kadala_tab_by_name,
    kadala_item_by_name,
)

"""
# Works
def right_click(hotkey):
    handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
    if handle:
        x, y = win32gui.ScreenToClient(handle, win32api.GetCursorPos())
        send_mouse(handle, 'LM', x, y)
        keyboard.remove_hotkey(hotkey)
        while keyboard.is_pressed(hotkey):
            x, y = win32gui.ScreenToClient(handle, win32api.GetCursorPos())
            send_mouse(handle, 'RM', x, y)
            sleep(0.01)
    keyboard.add_hotkey(hotkey, right_click, args=(hotkey,))

# Works
def left_click(hotkey):
    handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
    if handle:
        keyboard.remove_hotkey(hotkey)
        while keyboard.is_pressed(hotkey):
            x, y = win32gui.ScreenToClient(handle, win32api.GetCursorPos())
            send_mouse(handle, 'LM', x, y)
            sleep(0.01)
    keyboard.add_hotkey(hotkey, left_click, args=(hotkey,))
"""


def right_click(hotkey):
    handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
    if handle:
        x, y = win32gui.ScreenToClient(handle, win32api.GetCursorPos())
        send_mouse(handle, 'RM', x, y)
        sleep(0.003)


def left_click(hotkey):
    handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
    if handle:
        x, y = win32gui.ScreenToClient(handle, win32api.GetCursorPos())
        send_mouse(handle, 'LM', x, y)
        sleep(0.003)


# Works
def cube_conv_sm(speed):
    handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
    if handle:
        item = transform_coordinates(handle, 1425, 580, rel='right')
        step = transform_coordinates(handle, 50, 50)
        fill = transform_coordinates(handle, 710, 840)
        trans = transform_coordinates(handle, 250, 830)
        bw = transform_coordinates(handle, 580, 850)
        fw = transform_coordinates(handle, 850, 850)

        try:
            if speed == 'normal':
                for i in range(6):
                    for j in range(10):
                        send_mouse(
                            handle, 'RM', item[0] + j * step[0], item[1] + i * step[1]
                        )
                        macro_sleep(0.13)
                        # macro_sleep(0.1)
                        send_mouse(handle, 'LM', fill[0], fill[1])  # Fill
                        send_mouse(handle, 'LM', trans[0], trans[1])  # Transmute
                        macro_sleep(0.13)
                        # macro_sleep(0.1)
                        send_mouse(handle, 'LM', bw[0], bw[1])  # Backwards
                        send_mouse(handle, 'LM', fw[0], fw[1])  # Forwards
            elif speed == 'sol':
                for _ in range(2):
                    for i in range(6):
                        for j in range(10):
                            send_mouse(
                                handle,
                                'RM',
                                item[0] + j * step[0],
                                item[1] + i * step[1],
                            )
                            macro_sleep(0.06)  # 0.025
                            send_mouse(handle, 'LM', fill[0], fill[1])  # Fill
                            send_mouse(handle, 'LM', trans[0], trans[1])  # Transmute
                            macro_sleep(0.06)  # 0.025
                            send_mouse(handle, 'LM', bw[0], bw[1])  # Backwards
                            send_mouse(handle, 'LM', fw[0], fw[1])  # Forwards
            elif speed == 'slow':
                for i in range(6):
                    for j in range(10):
                        send_mouse(
                            handle, 'RM', item[0] + j * step[0], item[1] + i * step[1]
                        )
                        macro_sleep(0.13)
                        send_mouse(handle, 'LM', fill[0], fill[1])  # Fill
                        macro_sleep(0.1)
                        send_mouse(handle, 'LM', trans[0], trans[1])  # Transmute
                        macro_sleep(0.13)
                        send_mouse(handle, 'LM', bw[0], bw[1])  # Backwards
                        macro_sleep(0.1)
                        send_mouse(handle, 'LM', fw[0], fw[1])  # Forwards
        except StopMacro:
            pass


# Works
def cube_conv_lg(speed):
    handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
    if handle:
        item = transform_coordinates(handle, 1425, 580, rel='right')
        step = transform_coordinates(handle, 50, 50)
        fill = transform_coordinates(handle, 710, 840)
        trans = transform_coordinates(handle, 250, 830)
        bw = transform_coordinates(handle, 580, 850)
        fw = transform_coordinates(handle, 850, 850)

        try:
            if speed == 'normal':
                for i in range(3):
                    for j in range(10):
                        send_mouse(
                            handle,
                            'RM',
                            item[0] + j * step[0],
                            item[1] + i * step[1] * 2,
                        )
                        # macro_sleep(0.1)
                        macro_sleep(0.13)
                        send_mouse(handle, 'LM', fill[0], fill[1])  # Fill
                        send_mouse(handle, 'LM', trans[0], trans[1])  # Transmute
                        # macro_sleep(0.1)
                        macro_sleep(0.13)
                        send_mouse(handle, 'LM', bw[0], bw[1])  # Backwards
                        send_mouse(handle, 'LM', fw[0], fw[1])  # Forwards
            elif speed == 'sol':
                for _ in range(2):
                    for i in range(3):
                        for j in range(10):
                            send_mouse(
                                handle,
                                'RM',
                                item[0] + j * step[0],
                                item[1] + i * step[1] * 2,
                            )
                            macro_sleep(0.06)  # 0.025
                            send_mouse(handle, 'LM', fill[0], fill[1])  # Fill
                            send_mouse(handle, 'LM', trans[0], trans[1])  # Transmute
                            macro_sleep(0.06)  # 0.025
                            send_mouse(handle, 'LM', bw[0], bw[1])  # Backwards
                            send_mouse(handle, 'LM', fw[0], fw[1])  # Forwards
            elif speed == 'slow':
                for i in range(3):
                    for j in range(10):
                        send_mouse(
                            handle,
                            'RM',
                            item[0] + j * step[0],
                            item[1] + i * step[1] * 2,
                        )
                        macro_sleep(0.13)
                        send_mouse(handle, 'LM', fill[0], fill[1])  # Fill
                        macro_sleep(0.1)
                        send_mouse(handle, 'LM', trans[0], trans[1])  # Transmute
                        macro_sleep(0.13)
                        send_mouse(handle, 'LM', bw[0], bw[1])  # Backwards
                        macro_sleep(0.1)
                        send_mouse(handle, 'LM', fw[0], fw[1])  # Forwards
        except StopMacro:
            pass


# Works
def reforge():
    handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
    if handle:
        item = transform_coordinates(handle, 1425, 580, rel='right')
        fill = transform_coordinates(handle, 710, 840)
        trans = transform_coordinates(handle, 250, 830)
        bw = transform_coordinates(handle, 580, 850)
        fw = transform_coordinates(handle, 850, 850)

        send_mouse(handle, 'RM', item[0], item[1])  # Item
        sleep(0.1)
        send_mouse(handle, 'LM', fill[0], fill[1])  # Fill
        send_mouse(handle, 'LM', trans[0], trans[1])  # Transmute
        sleep(0.1)
        send_mouse(handle, 'LM', bw[0], bw[1])  # Backwards
        send_mouse(handle, 'LM', fw[0], fw[1])  # Forth
        # send_mousemove(handle, item[0], item[1])
        send_mouse(handle, 'RM', item[0], item[1])  # Item


# Works
def upgrade_gem(empowered):
    handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
    if handle:
        first_gem = transform_coordinates(handle, 100, 640)
        upgrade = transform_coordinates(handle, 280, 550)

        send_mouse(handle, 'LM', first_gem[0], first_gem[1])
        sleep(0.1)
        try:
            if not empowered:
                for i in range(4):
                    if i == 1:
                        send_key(handle, 't')
                    send_mouse(handle, 'LM', upgrade[0], upgrade[1])
                    macro_sleep(1.8)
            else:
                for i in range(5):
                    if i == 2:
                        send_key(handle, 't')
                    send_mouse(handle, 'LM', upgrade[0], upgrade[1])
                    macro_sleep(1.8)
        except StopMacro:
            pass


# Works
def salvage(spare_columns):
    handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
    if handle:
        menu = transform_coordinates(handle, 517, 480)
        anvil = transform_coordinates(handle, 165, 295)
        item = transform_coordinates(handle, 1875, 585, rel='right')
        step = transform_coordinates(handle, 50, 50)

        send_mouse(handle, 'LM', menu[0], menu[1])  # Salvage Menu
        send_mouse(handle, 'LM', anvil[0], anvil[1])  # Click Salvage Button
        for i in range(6):
            for j in range(10 - spare_columns):
                send_mouse(handle, 'LM', item[0] - j * step[0], item[1] + i * step[1])
                send_key(handle, 'enter')
                send_key(handle, 'enter')
        send_key(handle, 'esc')


# Works
def drop_inventory(spare_columns):
    handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
    if handle:
        item = transform_coordinates(handle, 1875, 585, rel='right')
        step = transform_coordinates(handle, 50, 50)
        x, y = win32gui.ScreenToClient(handle, win32api.GetCursorPos())

        send_key(handle, 'c')
        for i in range(6):
            for j in range(10 - spare_columns):
                send_mouse(handle, 'LM', item[0] - j * step[0], item[1] + i * step[1])
                send_mouse(handle, 'LM', x, y)
        send_key(handle, 'c')


# Works
def open_gr():
    handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
    if handle:
        grift = transform_coordinates(handle, 270, 480)
        accept = transform_coordinates(handle, 260, 850)

        send_mouse(handle, 'LM', grift[0], grift[1])
        send_mouse(handle, 'LM', accept[0], accept[1])


def open_rift():
    handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
    if handle:
        rift = transform_coordinates(handle, 270, 300)
        accept = transform_coordinates(handle, 260, 850)

        send_mouse(handle, 'LM', rift[0], rift[1])
        send_mouse(handle, 'LM', accept[0], accept[1])


# Works
def leave_game():
    handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
    if handle:
        leave = transform_coordinates(handle, 230, 475)

        send_key(handle, 'esc')
        send_mouse(handle, 'LM', leave[0], leave[1])


# Works
def port_town(act):
    handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
    if handle:
        act_coords = map_act_coords_by_act(act)
        town_coords = map_town_coords_by_act(act)

        bw_map = transform_coordinates(handle, 895, 125, rel='middle')
        act = transform_coordinates(handle, act_coords[0], act_coords[1], rel='middle')
        town = transform_coordinates(
            handle, town_coords[0], town_coords[1], rel='middle'
        )

        send_key(handle, 'm')
        send_mouse(handle, 'LM', bw_map[0], bw_map[1])
        send_mouse(handle, 'LM', act[0], act[1])
        send_mouse(handle, 'LM', town[0], town[1])


# Works
def port_pool(poolspotlist):
    handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
    if handle:
        poolspot = poolspotlist.next_spot()
        if poolspot:
            bw_map = transform_coordinates(handle, 895, 125, rel='middle')
            act = transform_coordinates(
                handle, poolspot[0][0], poolspot[0][1], rel='middle'
            )
            wp = transform_coordinates(
                handle, poolspot[1][0], poolspot[1][1], rel='middle'
            )

            # send_key(handle, 'm')
            send_mouse(handle, 'LM', bw_map[0], bw_map[1])
            send_mouse(handle, 'LM', act[0], act[1])
            send_mouse(handle, 'LM', wp[0], wp[1])


# Works
def lower_difficulty():
    handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
    if handle:
        lower = transform_coordinates(handle, 1700, 400, rel='right')

        send_key(handle, 'esc')
        for i in range(19):
            send_mouse(handle, 'LM', lower[0], lower[1])
            send_key(handle, 'enter')
        send_key(handle, 'esc')


# Works
def swap_armor(items):
    handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
    if handle:
        item_coords = []
        for i in range(items):
            item_coords.append(
                transform_coordinates(handle, 1425, 580 + i * 100, rel='right')
            )

        send_key(handle, 'c')
        for i, coords in enumerate(item_coords):
            if i == 1:
                send_key_down(handle, 'alt')
                send_mouse(handle, 'RM', coords[0], coords[1])
                send_key_up(handle, 'alt')
            else:
                send_mouse(handle, 'RM', coords[0], coords[1])
        send_key(handle, 'c')


def gamble(item):
    handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
    if handle:
        tab_coords = kadala_tab_by_name(item)
        item_coords = kadala_item_by_name(item)
        tab = transform_coordinates(handle, tab_coords[0], tab_coords[1])
        item = transform_coordinates(handle, item_coords[0], item_coords[1])

        send_mouse(handle, 'LM', tab[0], tab[1])
        for i in range(60):
            send_mouse(handle, 'RM', item[0], item[1])


class StopMacro(Exception):
    pass


def macro_sleep(time):
    for i in range(int(time * 100)):
        if keyboard.is_pressed('esc'):
            raise StopMacro
        else:
            sleep(0.008)
