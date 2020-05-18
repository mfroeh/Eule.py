import keyboard
from Macros import *
from kthread import KThread


class Listener:
    def __init__(self, settings, handle):
        self.handle = handle
        self.paused = False
        self.set_listeners(settings)

        self.thread = KThread(target=lambda: keyboard.wait('k+i+l+l'))
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
                        v, port_a1, args=(self.handle,)
                    )
                elif k == 'lower_diff':
                    self.listeners[k] = keyboard.add_hotkey(
                        v, lower_diff, args=(self.handle,)
                    )
                elif k == 'pause':
                    self.listeners[k] = keyboard.add_hotkey(
                        v, self.pause, args=(settings,)
                    )

    def renew_listeners(self, settings):
        keyboard.remove_all_hotkeys()
        self.set_listeners(settings)

    def renew_handle(self, new_handle):
        print(new_handle)
        self.handle = new_handle

    def pause(self, settings):
        if self.paused:
            self.renew_listeners(settings)
            self.paused = False
            print('continuing')
        else:
            keyboard.remove_all_hotkeys()
            keyboard.add_hotkey(settings.hotkeys['pause'], self.pause, args=(settings,))
            self.paused = True
            print('paused')
