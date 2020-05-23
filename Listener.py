import keyboard
from macros import *
from kthread import KThread
from PoolSpot import PoolSpotList


class Listener:
    def __init__(self, settings):
        self.settings = settings
        self.start()

        self.thread = KThread(target=lambda: keyboard.wait('a+r+b+i+t+r+a+r+y'))
        self.thread.start()

    def start(self):
        self.paused = False
        self.listeners = {}
        for k, v in self.settings.hotkeys.items():
            if v:
                if k == 'right_click':
                    self.listeners[k] = keyboard.add_hotkey(v, right_click)
                elif k == 'left_click':
                    self.listeners[k] = keyboard.add_hotkey(v, left_click)
                elif k == 'salvage':
                    self.listeners[k] = keyboard.add_hotkey(
                        v, salvage, args=(self.settings.special['spare_columns'],)
                    )
                elif k == 'drop_inventory':
                    self.listeners[k] = keyboard.add_hotkey(
                        v,
                        drop_inventory,
                        args=(self.settings.special['spare_columns'],),
                    )
                elif k == 'gamble':
                    self.listeners[k] = keyboard.add_hotkey(
                        v, gamble, args=(self.settings.special['gamble_item'],),
                    )
                elif k == 'gem_up':
                    self.listeners[k] = keyboard.add_hotkey(
                        v, gem_up, args=(self.settings.special['empowered'],)
                    )
                elif k == 'cube_conv_sm':
                    self.listeners[k] = keyboard.add_hotkey(
                        v, cube_conv_sm, args=(self.settings.special['fast_convert'],),
                    )
                elif k == 'cube_conv_lg':
                    self.listeners[k] = keyboard.add_hotkey(
                        v, cube_conv_lg, args=(self.settings.special['fast_convert'],),
                    )
                elif k == 'reforge':
                    self.listeners[k] = keyboard.add_hotkey(v, reforge)
                elif k == 'open_gr':
                    self.listeners[k] = keyboard.add_hotkey(v, open_gr)
                elif k == 'leave_game':
                    self.listeners[k] = keyboard.add_hotkey(v, leave_game)
                elif k == 'port_a1':
                    self.listeners[k] = keyboard.add_hotkey(v, port_town, args=(1,))
                elif k == 'port_a2':
                    self.listeners[k] = keyboard.add_hotkey(v, port_town, args=(2,))
                elif k == 'port_a3':
                    self.listeners[k] = keyboard.add_hotkey(v, port_town, args=(3,))
                elif k == 'port_a5':
                    self.listeners[k] = keyboard.add_hotkey(v, port_town, args=(5,))
                elif k == 'lower_diff':
                    self.listeners[k] = keyboard.add_hotkey(v, lower_diff)
                elif k == 'armor_swap':
                    self.listeners[k] = keyboard.add_hotkey(
                        v, armor_swap, args=(self.settings.special['armor_swap'],),
                    )
                elif k == 'port_pool':
                    self.listeners[k] = keyboard.add_hotkey(
                        v, port_pool, args=(PoolSpotList(self.settings.poolspots),),
                    )
                elif k == 'pause':
                    self.listeners[k] = keyboard.add_hotkey(v, self.pause)

    def stop(self):
        keyboard.remove_all_hotkeys()

    def pause(self):
        if self.paused:
            keyboard.remove_all_hotkeys()
            self.start()
        else:
            self.paused = True
            self.stop()
            keyboard.add_hotkey(self.settings.hotkeys['pause'], self.pause)
