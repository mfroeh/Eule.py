import keyboard
from Macros import *
from kthread import KThread
from PoolSpot import PoolSpotList


class Listener:
    def __init__(self, settings, handle):
        self.handle = handle
        self.paused = False
        self.set_listeners(settings)

        self.thread = KThread(target=lambda: keyboard.wait('a+r+b+i+t+r+a+r+y'))
        self.thread.start()

    def set_listeners(self, settings):
        self.listeners = {}
        for k, v in settings.hotkeys.items():
            if v:
                if k == 'right_click':
                    self.listeners[k] = keyboard.add_hotkey(
                        v, right_click, args=(self.handle,)
                    )
                elif k == 'left_click':
                    self.listeners[k] = keyboard.add_hotkey(
                        v, left_click, args=(self.handle,)
                    )
                elif k == 'salvage':
                    self.listeners[k] = keyboard.add_hotkey(
                        v, salvage, args=(self.handle,)
                    )
                elif k == 'drop_inventory':
                    self.listeners[k] = keyboard.add_hotkey(
                        v, drop_inventory, args=(self.handle,)
                    )
                elif k == 'gem_up':
                    self.listeners[k] = keyboard.add_hotkey(
                        v, gem_up, args=(self.handle, settings.special['empowered'])
                    )
                elif k == 'cube_conv_sm':
                    self.listeners[k] = keyboard.add_hotkey(
                        v,
                        cube_conv_sm,
                        args=(self.handle, settings.special['fast_convert']),
                    )
                elif k == 'cube_conv_lg':
                    self.listeners[k] = keyboard.add_hotkey(
                        v,
                        cube_conv_lg,
                        args=(self.handle, settings.special['fast_convert']),
                    )
                elif k == 'reforge':
                    self.listeners[k] = keyboard.add_hotkey(
                        v, reforge, args=(self.handle,)
                    )
                elif k == 'open_gr':
                    self.listeners[k] = keyboard.add_hotkey(
                        v, open_gr, args=(self.handle,)
                    )
                elif k == 'leave_game':
                    self.listeners[k] = keyboard.add_hotkey(
                        v, leave_game, args=(self.handle,)
                    )
                elif k == 'port_a1':
                    self.listeners[k] = keyboard.add_hotkey(
                        v, port_town, args=(self.handle, 1)
                    )
                elif k == 'port_a2':
                    self.listeners[k] = keyboard.add_hotkey(
                        v, port_town, args=(self.handle, 2)
                    )
                elif k == 'port_a3':
                    self.listeners[k] = keyboard.add_hotkey(
                        v, port_town, args=(self.handle, 3)
                    )
                elif k == 'port_a5':
                    self.listeners[k] = keyboard.add_hotkey(
                        v, port_town, args=(self.handle, 5)
                    )
                elif k == 'lower_diff':
                    self.listeners[k] = keyboard.add_hotkey(
                        v, lower_diff, args=(self.handle,)
                    )
                elif k == 'armor_swap':
                    self.listeners[k] = keyboard.add_hotkey(
                        v,
                        armor_swap,
                        args=(self.handle, settings.special['armor_swap']),
                    )
                elif k == 'pool_tp':
                    self.listeners[k] = keyboard.add_hotkey(
                        v,
                        pool_tp,
                        args=(self.handle, PoolSpotList(settings.poolspots)),
                    )
                elif k == 'pause':
                    self.listeners[k] = keyboard.add_hotkey(
                        v, self.pause, args=(settings,)
                    )

    def renew_listeners(self, settings):
        keyboard.remove_all_hotkeys()
        self.set_listeners(settings)

    def renew_handle(self, new_handle):
        self.handle = new_handle

    def pause(self, settings):
        if self.paused:
            self.paused = False
            self.renew_listeners(settings)
        else:
            self.paused = True
            keyboard.remove_all_hotkeys()
            keyboard.add_hotkey(settings.hotkeys['pause'], self.pause, args=(settings,))
