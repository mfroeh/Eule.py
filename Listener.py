import keyboard
import macros
from kthread import KThread
from PoolSpot import PoolSpotList
from ahk import AHK
import win32gui
import utils
from sends import send_mouse
from time import sleep


class Listener:
    def __init__(self, settings):
        self.settings = settings

        self.thread = KThread(target=lambda: keyboard.wait('a+r+b+i+t+r+a+r+y'))
        self.thread.start()

        self.image_recognition_thread = KThread(target=self.watch_screen)
        self.image_recognition_thread.start()

        self.start()

    def start(self):
        self.paused = False
        hotkeys = self.settings.hotkeys
        special = self.settings.special
        abbrevations = self.settings.abbrevations

        if hotkeys['right_click']:
            keyboard.add_hotkey(hotkeys['right_click'], macros.right_click)
        if hotkeys['left_click']:
            keyboard.add_hotkey(hotkeys['left_click'], macros.left_click)
        if hotkeys['lower_difficulty']:
            keyboard.add_hotkey(hotkeys['lower_difficulty'], macros.lower_difficulty)
        if hotkeys['swap_armor']:
            keyboard.add_hotkey(
                hotkeys['swap_armor'],
                macros.swap_armor,
                args=(special['armor_swap_amount'],),
            )
        if hotkeys['pause']:
            keyboard.add_hotkey(hotkeys['pause'], self.pause)
        if hotkeys['port_a1']:
            keyboard.add_hotkey(hotkeys['port_a1'], macros.port_town, args=(1,))
        if hotkeys['port_a2']:
            keyboard.add_hotkey(hotkeys['port_a2'], macros.port_town, args=(2,))
        if hotkeys['port_a3']:
            keyboard.add_hotkey(hotkeys['port_a3'], macros.port_town, args=(3,))
        if hotkeys['port_a5']:
            keyboard.add_hotkey(hotkeys['port_a5'], macros.port_town, args=(5,))
        if hotkeys['port_pool']:
            keyboard.add_hotkey(
                hotkeys['port_pool'],
                macros.port_pool,
                args=(PoolSpotList(self.settings.poolspots),),
            )
        if hotkeys['open_gr']:
            keyboard.add_hotkey(hotkeys['open_gr'], macros.open_gr)
        if hotkeys['upgrade_gem']:
            keyboard.add_hotkey(
                hotkeys['upgrade_gem'], macros.upgrade_gem, args=(special['empowered'],)
            )
        if hotkeys['leave_game']:
            keyboard.add_hotkey(hotkeys['leave_game'], macros.leave_game)
        if hotkeys['salvage']:
            keyboard.add_hotkey(
                hotkeys['salvage'], macros.salvage, args=(special['spare_columns'],)
            )
        if hotkeys['drop_inventory']:
            keyboard.add_hotkey(
                hotkeys['drop_inventory'],
                macros.drop_inventory,
                args=(special['spare_columns'],),
            )
        if hotkeys['gamble']:
            keyboard.add_hotkey(
                hotkeys['gamble'], macros.gamble, args=(special['gamble_item'],)
            )
        if hotkeys['cube_conv_sm']:
            keyboard.add_hotkey(
                hotkeys['cube_conv_sm'],
                macros.cube_conv_sm,
                args=(special['fast_convert'],),
            )
        if hotkeys['cube_conv_lg']:
            keyboard.add_hotkey(
                hotkeys['cube_conv_lg'],
                macros.cube_conv_lg,
                args=(special['fast_convert'],),
            )
        if hotkeys['reforge']:
            keyboard.add_hotkey(hotkeys['reforge'], macros.reforge)

        if self.settings.special['abbrevations_enabled']:
            for abbrevation, msg in abbrevations.items():
                keyboard.add_abbreviation(abbrevation, msg)

    def stop(self):
        keyboard.unhook_all()

    def pause(self):
        if self.paused:
            self.gui_paused.setChecked(False)
            keyboard.unhook_all()
            self.start()
        else:
            self.paused = True
            self.gui_paused.setChecked(True)
            self.stop()
            keyboard.add_hotkey(self.settings.hotkeys['pause'], self.pause)

    # Regular Version
    def watch_screen(self):
        ahk = AHK()
        while True:
            handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
            if handle and self.settings.special['auto_start'] and not self.paused:
                x1, y1, x2, y2 = win32gui.GetWindowRect(handle)
                image_path = f'./images/start_game_{x2 - x1}_{y2 - y1}.png'
                x1, y1 = utils.transform_coordinates(handle, 160, 500)
                x2, y2 = utils.transform_coordinates(handle, 320, 540)
                found = ahk.image_search(image_path, (x1, y1), (x2, y2), 30)
                if found:
                    print('FOUND!')
                    send_mouse(handle, 'LM', x1, y1)
                else:
                    print('Not found!')
                sleep(0.3)

    """
    # Pyinstaller Version
    def watch_screen(self):
        import sys
        import os

        wd = sys._MEIPASS

        ahk_path = os.path.join(wd, './AutoHotkey/AutoHotkey.exe')
        ahk = AHK(executable_path=ahk_path)
        while True:
            handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
            if handle and self.settings.special['auto_start'] and not self.paused:
                x1, y1, x2, y2 = win32gui.GetWindowRect(handle)
                image_path = os.path.join(
                    wd, f'./images/start_game_{x2 - x1}_{y2 - y1}.png'
                )
                x1, y1 = utils.transform_coordinates(handle, 160, 500)
                x2, y2 = utils.transform_coordinates(handle, 320, 540)
                found = ahk.image_search(image_path, (x1, y1), (x2, y2), 30)
                if found:
                    send_mouse(handle, 'LM', x1, y1)
                sleep(0.3)
    """
