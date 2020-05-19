import tkinter as tk
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import askokcancel
import keyboard
from threading import Thread
from utils import start_thirdparty


class GUI:
    def __init__(self, settings, listener):
        self.root = tk.Tk()
        self.root.title('Eule.py')
        # self.root.iconbitmap('C:\\Users\\Arbeit\\Desktop\\Macro.py\\Compile\\owl.ico')
        self.root.style = Style()
        self.root.style.configure('TLabelFrame', font=30)

        self.frames = {
            'path': LabelFrame(self.root, text='Third Party Paths'),
            'cube': LabelFrame(self.root, text='Cube Hotkeys'),
            'gr': LabelFrame(self.root, text='Greater Rift Hotkeys'),
            'town': LabelFrame(self.root, text='Town Hotkeys'),
            'general': LabelFrame(self.root, text='General Hotkeys'),
            'info': LabelFrame(self.root, text='Info'),
        }

        self.DACTIVE = tk.IntVar(self.root, True)
        self.EMP = tk.BooleanVar(self.root, settings.special['empowered'])
        self.FASTCONV = tk.BooleanVar(self.root, settings.special['fast_convert'])
        self.ARMORSWAP = tk.IntVar(self.root, settings.special['armor_swap'])
        self.PATHS = {}
        self.HKS = {}

        for i, (name, path) in enumerate(settings.paths.items()):
            self.PATHS[name] = tk.StringVar(self.root, path)
            Label(self.frames['path'], text=name).grid(column=0, row=i, sticky='W')
            entry = Entry(self.frames['path'], textvariable=self.PATHS[name])
            entry.grid(column=1, row=i, ipady=2, pady=2)
            entry.bind(
                '<1>', lambda event, x=name: self.select_path(event, x, settings)
            )

        for i, (name, hk) in enumerate(settings.hotkeys.items()):
            self.HKS[name] = tk.StringVar(self.root, hk)
            frame = self.frames['general']
            if i <= 2:
                frame = self.frames['cube']
            elif 3 <= i <= 5:
                frame = self.frames['gr']
            elif 6 <= i <= 7:
                frame = self.frames['town']

            Label(frame, text=nice_name(name)).grid(column=0, row=i)
            Button(
                frame,
                textvariable=self.HKS[name],
                command=lambda x=name: self.set_hotkey(x, settings, listener),
            ).grid(column=1, row=i)

        Checkbutton(
            self.frames['info'],
            text='Diablo hooked',
            onvalue=True,
            offvalue=False,
            variable=self.DACTIVE,
            state=tk.DISABLED,
        ).grid(column=0, row=0)

        Button(
            self.frames['info'],
            text='Start Third Party',
            command=lambda: Thread(
                target=lambda: start_thirdparty(settings.paths)
            ).start(),
        ).grid(column=0, row=1)

        Checkbutton(
            self.frames['gr'],
            text='Empowered',
            variable=self.EMP,
            onvalue=True,
            offvalue=False,
            command=lambda x='emp': self.checkbox_clicked(x, settings, listener),
        ).grid()

        Checkbutton(
            self.frames['cube'],
            text='SoL Converting',
            variable=self.FASTCONV,
            onvalue=True,
            offvalue=False,
            command=lambda x='conv': self.checkbox_clicked(x, settings, listener),
        ).grid()

        Radiobutton(
            self.frames['general'],
            text='Cains',
            variable=self.ARMORSWAP,
            value=3,
            command=lambda x='armor_swap': self.checkbox_clicked(x, settings, listener),
        ).grid()

        Radiobutton(
            self.frames['general'],
            text='Bounty DH',
            variable=self.ARMORSWAP,
            value=2,
            command=lambda x='armor_swap': self.checkbox_clicked(x, settings, listener),
        ).grid()

        for i, v in enumerate(self.frames.values()):
            v.grid(
                row=int(0.5 * i),
                column=i % 2,
                sticky='NW',
                pady=5,
                padx=5,
                ipadx=5,
                ipady=5,
            )

        self.root.grid()

    def mainloop(self):
        self.root.mainloop()

    def select_path(self, event, name, settings):
        path = askopenfilename(initialdir='./')
        if path:
            settings.paths[name] = path
            self.PATHS[name].set(path)

    def set_hotkey(self, hotkey, settings, listener):
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

    def checkbox_clicked(self, cb, settings, listener):
        if cb == 'emp':
            settings.special['empowered'] = self.EMP.get()
            listener.renew_listeners(settings)
        elif cb == 'conv':
            settings.special['fast_convert'] = self.FASTCONV.get()
            listener.renew_listeners(settings)
        elif cb == 'armor_swap':
            settings.special['armor_swap'] = self.ARMORSWAP.get()
            listener.renew_listeners(settings)


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
        'armor_swap': 'Swap Armor Cain',
        'pool_tp': 'Teleport to next PoolSpot',
        'pause': 'Pause Eule.py',
    }
    return switcher.get(name, 'Key not found!')


def hotkey_delete_request(hotkey):
    try:
        scan_codes = keyboard.key_to_scan_codes(hotkey)
        return scan_codes[0] == 83
    except:
        return False
