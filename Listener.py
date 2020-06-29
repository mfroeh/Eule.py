import keyboard
import macros
from kthread import KThread
from PoolSpot import PoolSpotList
import sys
import os

try:
    wd = sys._MEIPASS
except AttributeError:
    wd = ''


class Listener:
    def __init__(self, settings):
        self.settings = settings

        self.thread = KThread(target=lambda: keyboard.wait('a+r+b+i+t+r+a+r+y'))
        self.thread.start()

        self.start()

    def start(self):
        self.paused = False
        hotkeys = self.settings.hotkeys
        special = self.settings.special
        abbrevations = self.settings.abbrevations

        if hotkeys['right_click']:
            keyboard.add_hotkey(
                hotkeys['right_click'],
                macros.right_click,
                args=(hotkeys['right_click'],),
                suppress=True,
            )
        if hotkeys['left_click']:
            keyboard.add_hotkey(
                hotkeys['left_click'],
                macros.left_click,
                args=(hotkeys['left_click'],),
                suppress=True,
            )
        if hotkeys['lower_difficulty']:
            keyboard.add_hotkey(
                hotkeys['lower_difficulty'], macros.lower_difficulty, suppress=True
            )
        if hotkeys['swap_armor']:
            keyboard.add_hotkey(
                hotkeys['swap_armor'],
                macros.swap_armor,
                args=(special['armor_swap_amount'],),
                suppress=True,
            )
        if hotkeys['pause']:
            keyboard.add_hotkey(hotkeys['pause'], self.pause, suppress=True)
        if hotkeys['port_a1']:
            keyboard.add_hotkey(
                hotkeys['port_a1'], macros.port_town, args=(1,), suppress=True
            )
        if hotkeys['port_a2']:
            keyboard.add_hotkey(
                hotkeys['port_a2'], macros.port_town, args=(2,), suppress=True
            )
        if hotkeys['port_a3']:
            keyboard.add_hotkey(
                hotkeys['port_a3'], macros.port_town, args=(3,), suppress=True
            )
        if hotkeys['port_a4']:
            keyboard.add_hotkey(
                hotkeys['port_a4'], macros.port_town, args=(4,), suppress=True
            )
        if hotkeys['port_a5']:
            keyboard.add_hotkey(
                hotkeys['port_a5'], macros.port_town, args=(5,), suppress=True
            )
        if hotkeys['port_pool']:
            keyboard.add_hotkey(
                hotkeys['port_pool'],
                macros.port_pool,
                args=(PoolSpotList(self.settings.poolspots),),
                suppress=True,
            )
        if hotkeys['open_gr']:
            keyboard.add_hotkey(hotkeys['open_gr'], macros.open_gr, suppress=True)
        if hotkeys['upgrade_gem']:
            keyboard.add_hotkey(
                hotkeys['upgrade_gem'],
                macros.upgrade_gem,
                args=(special['empowered'], special['choose_gem']),
            )
        if hotkeys['leave_game']:
            keyboard.add_hotkey(hotkeys['leave_game'], macros.leave_game, suppress=True)
        if hotkeys['salvage']:
            keyboard.add_hotkey(
                hotkeys['salvage'],
                macros.salvage,
                args=(special['spare_columns'],),
                suppress=True,
            )
        if hotkeys['drop_inventory']:
            keyboard.add_hotkey(
                hotkeys['drop_inventory'],
                macros.drop_inventory,
                args=(special['spare_columns'],),
                suppress=True,
            )
        if hotkeys['gamble']:
            keyboard.add_hotkey(
                hotkeys['gamble'],
                macros.gamble,
                args=(special['gamble_item'],),
                suppress=True,
            )
        if hotkeys['cube_conv_sm']:
            keyboard.add_hotkey(
                hotkeys['cube_conv_sm'],
                macros.cube_conv_sm,
                args=(special['cube_conv_speed'],),
            )
        if hotkeys['cube_conv_lg']:
            keyboard.add_hotkey(
                hotkeys['cube_conv_lg'],
                macros.cube_conv_lg,
                args=(special['cube_conv_speed'],),
            )
        if hotkeys['reforge']:
            keyboard.add_hotkey(hotkeys['reforge'], macros.reforge, suppress=True)
        if hotkeys['skill_macro']:
            active_macro = self.settings.skill_macro['profiles'][
                self.settings.skill_macro['active']
            ]
            print(active_macro['name'])
            keyboard.add_hotkey(
                hotkeys['skill_macro'],
                macros.skill_macro,
                args=(active_macro['hotkeys'], active_macro['delays']),
                suppress=True,
            )

        if self.settings.special['abbrevations_enabled']:
            for abbrevation, msg in abbrevations.items():
                keyboard.add_abbreviation(abbrevation, msg)

    def stop(self):
        keyboard.unhook_all()

    def pause(self):
        if self.paused:
            keyboard.unhook_all()
            self.start()
            self.gui_paused.setChecked(False)
            p = os.path.join(wd, './Compiled/active.png').replace('\\', '/')
            self.status_image.setStyleSheet(
                "background-image: url("
                + p
                + ");"
                + "background-repeat: no-repeat;"
                + "background-position: center;"
            )
        else:
            self.paused = True
            self.stop()
            keyboard.add_hotkey(
                self.settings.hotkeys['pause'], self.pause, suppress=True
            )
            self.gui_paused.setChecked(True)
            p = os.path.join(wd, './Compiled/inactive.png').replace('\\', '/')
            self.status_image.setStyleSheet(
                f"background-image: url("
                + p
                + ");"
                + "background-repeat: no-repeat;"
                + "background-position: center;"
            )
            [t.stop() for t in macros.timers]
            macros.timers = []
            macros.is_running = False
