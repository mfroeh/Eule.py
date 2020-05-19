import win32api
from time import sleep
from sends import send_mouse, send_key, send_mousemove
import keyboard
import time
from utils import transform_coordinates, act_coords, town_wp_coords


def right_click(handle):
    x, y = win32api.GetCursorPos()
    send_mouse(handle, 'RM', x, y)
    sleep(0.001)


def left_click(handle):
    x, y = win32api.GetCursorPos()
    send_mouse(handle, 'LM', x, y)
    sleep(0.001)


def cube_conv_sm(handle, fast):
    item = transform_coordinates(handle, 1425, 580)
    step = transform_coordinates(handle, 50, 0)[0]
    fill = transform_coordinates(handle, 710, 840)
    transmute = transform_coordinates(handle, 250, 830)
    bw = transform_coordinates(handle, 580, 850)
    fw = transform_coordinates(handle, 850, 850)

    start = time.time()
    if not fast:
        try:
            for i in range(6):
                for j in range(10):
                    send_mouse(handle, 'RM', item[0] + j * step, item[1] + i * step)
                    macro_sleep(0.1)
                    send_mouse(handle, 'LM', fill[0], fill[1])  # Fill
                    send_mouse(handle, 'LM', transmute[0], transmute[1])  # Transmute
                    macro_sleep(0.1)
                    send_mouse(handle, 'LM', bw[0], bw[1])  # Backwards
                    send_mouse(handle, 'LM', fw[0], fw[1])  # Forwards
        except StopMacro:
            pass
    else:
        try:
            for _ in range(2):
                for i in range(6):
                    for j in range(10):
                        send_mouse(handle, 'RM', item[0] + j * step, item[1] + i * step)
                        macro_sleep(0.03)  # 0.025
                        send_mouse(handle, 'LM', fill[0], fill[1])  # Fill
                        send_mouse(
                            handle, 'LM', transmute[0], transmute[1]
                        )  # Transmute
                        macro_sleep(0.03)  # 0.025
                        send_mouse(handle, 'LM', bw[0], bw[1])  # Backwards
                        send_mouse(handle, 'LM', fw[0], fw[1])  # Forwards
        except StopMacro:
            pass
    print(time.time() - start)


def cube_conv_lg(handle, fast):
    item = transform_coordinates(handle, 1425, 580)
    step = transform_coordinates(handle, 50, 0)[0]
    fill = transform_coordinates(handle, 710, 840)
    transmute = transform_coordinates(handle, 250, 830)
    bw = transform_coordinates(handle, 580, 850)
    fw = transform_coordinates(handle, 850, 850)

    if not fast:
        try:
            for i in range(3):
                for j in range(10):
                    send_mouse(handle, 'RM', item[0] + j * step, item[1] + i * step * 2)
                    macro_sleep(0.1)
                    send_mouse(handle, 'LM', fill[0], fill[1])  # Fill
                    send_mouse(handle, 'LM', transmute[0], transmute[1])  # Transmute
                    macro_sleep(0.1)
                    send_mouse(handle, 'LM', bw[0], bw[1])  # Backwards
                    send_mouse(handle, 'LM', fw[0], fw[1])  # Forwards
        except StopMacro:
            pass
    else:
        try:
            for _ in range(2):
                for i in range(3):
                    for j in range(10):
                        send_mouse(
                            handle, 'RM', item[0] + j * step, item[1] + i * step * 2,
                        )
                        macro_sleep(0.03)  # 0.025
                        send_mouse(handle, 'LM', fill[0], fill[1])  # Fill
                        send_mouse(
                            handle, 'LM', transmute[0], transmute[1]
                        )  # Transmute
                        macro_sleep(0.03)  # 0.025
                        send_mouse(handle, 'LM', bw[0], bw[1])  # Backwards
                        send_mouse(handle, 'LM', fw[0], fw[1])  # Forwards
        except StopMacro:
            pass


def reforge(handle):
    item = transform_coordinates(handle, 1425, 580)
    fill = transform_coordinates(handle, 710, 840)
    transmute = transform_coordinates(handle, 250, 830)
    bw = transform_coordinates(handle, 580, 850)
    fw = transform_coordinates(handle, 850, 850)

    send_mouse(handle, 'RM', item[0], item[1])  # Item
    sleep(0.1)
    send_mouse(handle, 'LM', fill[0], fill[1])  # Fill
    send_mouse(handle, 'LM', transmute[0], transmute[1])  # Transmute
    sleep(0.1)
    send_mouse(handle, 'LM', bw[0], bw[1])  # Backwards
    send_mouse(handle, 'LM', fw[0], fw[1])  # Forth
    send_mousemove(handle, item[0], item[1])


def gem_up(handle, empowered):
    gem = transform_coordinates(handle, 100, 640)
    upgrade = transform_coordinates(handle, 280, 550)

    send_mouse(handle, 'LM', gem[0], gem[1])
    sleep(0.1)
    if not empowered:
        try:
            for i in range(4):
                if i == 1:
                    send_key(handle, 't')
                send_mouse(handle, 'LM', upgrade[0], upgrade[1])
                macro_sleep(1.75)
        except StopMacro:
            pass
    else:
        try:
            for i in range(5):
                if i == 2:
                    send_key(handle, 't')
                send_mouse(handle, 'LM', upgrade[0], upgrade[1])
                macro_sleep(1.75)
        except StopMacro:
            pass


def salvage(handle):
    slvg_menu = transform_coordinates(handle, 517, 480)
    slvg_btn = transform_coordinates(handle, 165, 295)
    item = transform_coordinates(handle, 1475, 585)
    step = transform_coordinates(handle, 50, 0)[0]

    send_mouse(handle, 'LM', slvg_menu[0], slvg_menu[1])  # Salvage Menu
    send_mouse(handle, 'LM', slvg_btn[0], slvg_btn[1])  # Click Salvage Button

    for i in range(6):
        for j in range(9):
            send_mouse(handle, 'LM', item[0] + j * step, item[1] + i * step)
            send_key(handle, 'enter')
            send_key(handle, 'enter')
    send_key(handle, 'esc')


def drop_inventory(handle):
    item = transform_coordinates(handle, 1475, 585)
    step = transform_coordinates(handle, 50, 0)[0]

    x, y = win32api.GetCursorPos()
    send_key(handle, 'c')
    for i in range(6):
        for j in range(9):
            send_mouse(handle, 'LM', item[0] + j * step, item[1] + i * step)
            send_mouse(handle, 'LM', x, y)
    send_key(handle, 'c')


def open_gr(handle):
    grift = transform_coordinates(handle, 270, 480)
    accept = transform_coordinates(handle, 260, 850)
    send_mouse(handle, 'LM', grift[0], grift[1])
    send_mouse(handle, 'LM', accept[0], accept[1])


def leave_game(handle):
    leave = transform_coordinates(handle, 230, 475)
    send_key(handle, 'esc')
    send_mouse(handle, 'LM', leave[0], leave[1])


def port_town(handle, act):
    a_coords = act_coords(act)
    t_coords = town_wp_coords(act)
    bw_map = transform_coordinates(handle, 895, 125)
    act = transform_coordinates(handle, a_coords[0], a_coords[1])
    town = transform_coordinates(handle, t_coords[0], t_coords[1])
    print(act)
    print(town)
    send_key(handle, 'm')
    send_mouse(handle, 'LM', bw_map[0], bw_map[1])
    send_mouse(handle, 'LM', act[0], act[1])
    send_mouse(handle, 'LM', town[0], town[1])


def pool_tp(handle, poolspotlist):
    bw_map = transform_coordinates(handle, 895, 125)
    poolspot = poolspotlist.next_spot()
    act = transform_coordinates(handle, poolspot.act_coords[0], poolspot.act_coords[1])
    wp = transform_coordinates(handle, poolspot.wp_coords[0], poolspot.wp_coords[1])

    send_key(handle, 'm')
    send_mouse(handle, 'LM', bw_map[0], bw_map[1])
    send_mouse(handle, 'LM', act[0], act[1])
    send_mouse(handle, 'LM', wp[0], wp[1])


def lower_diff(handle):
    lower = transform_coordinates(handle, 1700, 400)
    send_key(handle, 'esc')
    for i in range(19):
        send_mouse(handle, 'LM', lower[0], lower[1])
        send_key(handle, 'enter')
    send_key(handle, 'esc')


def armor_swap(handle):
    item_1 = transform_coordinates(handle, 1425, 610)
    item_2 = transform_coordinates(handle, 1425, 710)
    item_3 = transform_coordinates(handle, 1425, 810)
    send_key(handle, 'c')
    send_mouse(handle, 'RM', item_1[0], item_1[1])
    send_mouse(handle, 'RM', item_2[0], item_2[1])
    send_mouse(handle, 'RM', item_3[0], item_3[1])
    send_key(handle, 'c')


class StopMacro(Exception):
    pass


def macro_sleep(time):
    for i in range(int(time * 100)):
        if keyboard.is_pressed('esc'):
            raise StopMacro
        else:
            sleep(0.008)
