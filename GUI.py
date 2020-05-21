import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
from tkinter.ttk import *
import win32gui
from Settings import Settings
from Listener import Listener
from utils import start_thirdparty
import keyboard
import tkinter as tk
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import askokcancel
import keyboard
from threading import Thread
from utils import start_thirdparty
from ressources import pool_wps

# import Tkinter as tk     # python 2
# import tkFont as tkfont  # python 2


class App(tk.Tk):
    def __init__(self, settings, listener):
        tk.Tk.__init__(self)
        self.title('Eule.py')
        self.settings = settings
        self.listener = listener

        tab_parent = Notebook(self)
        self.main_frame = MainFrame(self)
        self.settings_frame = SettingsFrame(self)

        tab_parent.add(self.main_frame, text='Main')
        tab_parent.add(self.settings_frame, text='Settings')
        tab_parent.grid()


class MainFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.DACTIVE = tk.BooleanVar(self, True)
        self.HKS = {}

        self.EMP = tk.BooleanVar(self, parent.settings.special['empowered'])
        self.FASTCONV = tk.BooleanVar(self, parent.settings.special['fast_convert'])
        self.ARMORSWAP = tk.IntVar(self, parent.settings.special['armor_swap'])

        frames = {
            'cube': LabelFrame(self, text='Cube Hotkeys'),
            'gr': LabelFrame(self, text='Greater Rift Hotkeys'),
            'general': LabelFrame(self, text='General Hotkeys'),
            'ports': LabelFrame(self, text='Porting Hotkeys'),
            'town': LabelFrame(self, text='Town Hotkeys'),
            'info': LabelFrame(self, text='Info'),
        }

        for i, (name, hotkey) in enumerate(parent.settings.hotkeys.items()):
            self.HKS[name] = tk.StringVar(self, hotkey)
            frame = frames['general']
            if i <= 2:
                frame = frames['cube']
            elif 3 <= i <= 5:
                frame = frames['gr']
            elif 6 <= i <= 7:
                frame = frames['town']
            elif 8 <= i <= 12:
                frame = frames['ports']

            Label(frame, text=nice_name(name)).grid(column=0, row=i, sticky='W')
            Button(
                frame,
                textvariable=self.HKS[name],
                command=lambda x=name: self.set_hotkey(x),
            ).grid(column=1, row=i)

        Checkbutton(
            frames['info'],
            text='Diablo hooked',
            onvalue=True,
            offvalue=False,
            variable=self.DACTIVE,
            state=tk.DISABLED,
        ).grid(column=0, row=0)

        Checkbutton(
            frames['gr'],
            text='Empowered',
            variable=self.EMP,
            onvalue=True,
            offvalue=False,
            command=lambda x='emp': self.button_clicked(x),
        ).grid()

        Checkbutton(
            frames['cube'],
            text='SoL Converting',
            variable=self.FASTCONV,
            onvalue=True,
            offvalue=False,
            command=lambda x='conv': self.button_clicked(x),
        ).grid()

        Radiobutton(
            frames['general'],
            text='Cains',
            variable=self.ARMORSWAP,
            value=3,
            command=lambda x='armor_swap': self.button_clicked(x),
        ).grid()

        Radiobutton(
            frames['general'],
            text='Bounty DH',
            variable=self.ARMORSWAP,
            value=2,
            command=lambda x='armor_swap': self.button_clicked(x),
        ).grid()

        Button(
            frames['info'],
            text='Start Third Party',
            command=lambda: Thread(
                target=lambda: start_thirdparty(parent.settings.paths)
            ).start(),
        ).grid(column=0, row=1)

        for i, v in enumerate(frames.values()):
            v.grid(
                row=int(0.5 * i),
                column=i % 2,
                sticky='NW',
                pady=5,
                padx=5,
                ipadx=5,
                ipady=5,
            )

    def set_hotkey(self, hotkey):
        settings = self.parent.settings
        listener = self.parent.listener
        keyboard.remove_all_hotkeys()
        input = keyboard.read_hotkey(suppress=False)
        if input != 'esc' and not hotkey_delete_request(input):
            if askokcancel(message=f'New Hotkey: {input}. Save?'):
                for k, v in settings.hotkeys.items():
                    if v == input:
                        settings.hotkeys[k] = ''
                        self.HKS[k].set('')
                settings.hotkeys[hotkey] = input
                self.HKS[hotkey].set(input)
        elif hotkey_delete_request(input):
            settings.hotkeys[hotkey] = ''
            self.HKS[hotkey].set('')
        listener.renew_listeners(settings)

    def button_clicked(self, cb):
        settings = self.parent.settings
        listener = self.parent.listener
        if cb == 'emp':
            settings.special['empowered'] = self.EMP.get()
            listener.renew_listeners(settings)
        elif cb == 'conv':
            settings.special['fast_convert'] = self.FASTCONV.get()
            listener.renew_listeners(settings)
        elif cb == 'armor_swap':
            settings.special['armor_swap'] = self.ARMORSWAP.get()
            listener.renew_listeners(settings)


class SettingsFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.PATHS = {}
        frame = LabelFrame(self, text='Third Party Paths')  # Need frames for pools etc.
        for i, (name, path) in enumerate(parent.settings.paths.items()):
            self.PATHS[name] = tk.StringVar(self, path)
            Label(frame, text=name).grid(column=0, row=i, sticky='W')
            entry = Entry(frame, textvariable=self.PATHS[name])
            entry.grid(column=1, row=i, ipady=2, pady=2)
            entry.bind('<1>', lambda event, x=name: self.set_path(event, x))

        Button(
            self, text='Choose Poolspots', command=lambda: PopupPoolspots(self.parent),
        ).grid()

        frame.grid(
            row=int(0.5 * i),
            column=i % 2,
            sticky='NW',
            pady=5,
            padx=5,
            ipadx=5,
            ipady=5,
        )

    def set_path(self, event, name):
        path = askopenfilename(initialdir='./')
        if path:
            self.parent.settings.paths[name] = path
            self.PATHS[name].set(path)


class PopupPoolspots(tk.Toplevel):
    def __init__(self, elder):  # XD
        tk.Toplevel.__init__(self)
        self.wm_title('Choose Poolspots')
        self.elder = elder

        self.poolspots = []
        for wp in pool_wps():
            if wp in self.elder.settings.poolspots:
                var = tk.StringVar(value=wp)
            else:
                var = tk.StringVar('')
            self.poolspots.append(var)
            Checkbutton(self, var=var, text=wp, onvalue=wp).grid(
                sticky='NW', padx=5, ipadx=5
            )

        Button(self, text="Save", command=lambda: self.update_poolspots()).grid()
        Button(self, text="Cancel", command=self.destroy).grid()

    def update_poolspots(self):
        settings = self.elder.settings
        listener = self.elder.listener
        settings.poolspots = [
            p.get() for p in self.poolspots if p.get() not in ['', '0']
        ]
        listener.renew_listeners(settings)
        self.destroy()


def hotkey_delete_request(hotkey):
    try:
        scan_codes = keyboard.key_to_scan_codes(hotkey)
        return scan_codes[0] == 83
    except:
        return False


def nice_name(name):
    switcher = {
        'cube_conv_sm': 'Cube Conv (Single Slot)',
        'cube_conv_lg': 'Cube Conv (Dual Slot)',
        'reforge': 'Reforge / Conv Set',
        'open_gr': 'Open Grift',
        'gem_up': 'Upgrade Gem',
        'leave_game': 'Leave Game',
        'salvage': 'Salvage',
        'drop_inventory': 'Drop Inventory',
        'right_click': 'Spam Right Click',
        'left_click': 'Spam Left Click',
        'port_a1': 'Port to A1 Town',
        'port_a2': 'Port to A2 Town',
        'port_a3': 'Port to A3 / A4 Town',
        'port_a5': 'Port to A5 Town',
        'lower_diff': 'Normalize Difficulty',
        'armor_swap': 'Swap Armor',
        'pool_tp': 'Port to next Pool Spot',
        'pause': 'Pause Eule.py',
    }
    return switcher.get(name, 'Key not found!')


if __name__ == "__main__":
    handle = win32gui.FindWindow('D3 Main Window Class', 'Diablo III')
    print(handle)
    settings = Settings()
    listener = Listener(settings, handle)
    app = App(settings, listener)
    app.mainloop()
