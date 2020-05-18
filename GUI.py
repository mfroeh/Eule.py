import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import askokcancel
import keyboard
from threading import Thread
from utils import start_thirdparty, nice_name


class GUI:
    def __init__(self, settings, listener):
        self.root = tk.Tk()
        self.root.title('Eule.py')
        self.root.iconbitmap('C:\\Users\\Arbeit\\Desktop\\Macro.py\\Compile\\owl.ico')
        self.root.style = ttk.Style()
        self.root.style.configure('TLabelFrame', font=30)

        self.frames = {
            'path': ttk.LabelFrame(self.root, text='Third Party Paths'),
            'cube': ttk.LabelFrame(self.root, text='Cube Hotkeys'),
            'gr': ttk.LabelFrame(self.root, text='Greater Rift Hotkeys'),
            'town': ttk.LabelFrame(self.root, text='Town Hotkeys'),
            'general': ttk.LabelFrame(self.root, text='General Hotkeys'),
            'info': ttk.LabelFrame(self.root, text='Info'),
        }

        self.BV_DACTIVE = tk.IntVar(self.root, True)
        self.BV_EMP = tk.BooleanVar(self.root, settings.special['empowered'])
        self.BV_FASTCONV = tk.BooleanVar(self.root, settings.special['fast_convert'])
        self.SV_PATHS = {}
        self.SV_HKS = {}

        for i, (name, path) in enumerate(settings.paths.items()):
            self.SV_PATHS[name] = tk.StringVar(self.root, path)
            ttk.Label(self.frames['path'], text=name).grid(column=0, row=i, sticky='W')
            entry = ttk.Entry(self.frames['path'], textvariable=self.SV_PATHS[name])
            entry.grid(column=1, row=i, ipady=2, pady=2)
            entry.bind(
                '<1>', lambda event, x=name: self.select_path(event, x, settings)
            )

        for i, (name, hk) in enumerate(settings.hotkeys.items()):
            self.SV_HKS[name] = tk.StringVar(self.root, hk)
            frame = self.frames['general']
            if i <= 2:
                frame = self.frames['cube']
            elif 3 <= i <= 5:
                frame = self.frames['gr']
            elif 6 <= i <= 7:
                frame = self.frames['town']

            ttk.Label(frame, text=nice_name(name)).grid(column=0, row=i)
            ttk.Button(
                frame,
                textvariable=self.SV_HKS[name],
                command=lambda x=name: self.set_hotkey(x, settings, listener),
            ).grid(column=1, row=i)

        ttk.Checkbutton(
            self.frames['info'],
            text='Diablo hooked',
            onvalue=True,
            offvalue=False,
            variable=self.BV_DACTIVE,
            state=tk.DISABLED,
        ).grid(column=0, row=0)

        ttk.Button(
            self.frames['info'],
            text='Start Third Party',
            command=lambda: Thread(target=lambda: start_thirdparty(settings)).start(),
        ).grid(column=0, row=1)

        ttk.Checkbutton(
            self.frames['gr'],
            text='Empowered',
            onvalue=True,
            offvalue=False,
            variable=self.BV_EMP,
            command=lambda x='emp': self.set_cb(x, settings, listener),
        ).grid()

        ttk.Checkbutton(
            self.frames['cube'],
            text='SoL Converting',
            onvalue=True,
            offvalue=False,
            variable=self.BV_FASTCONV,
            command=lambda x='conv': self.set_cb(x, settings, listener),
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
            self.SV_PATHS[name].set(path)

    def set_hotkey(self, hotkey, settings, listener):
        keyboard.remove_all_hotkeys()
        input = keyboard.read_hotkey(suppress=False)
        if input != 'esc':
            if askokcancel(message=f'New Hotkey: {input}. Save?'):
                print(input)
                # if int(input):  # canonical repr von numpad ist jeweils nur die ziffer
                #     input = 'num ' + input

                for k, v in settings.hotkeys.items():
                    if v == input:
                        settings.hotkeys[k] = ''
                        self.SV_HKS[k].set('')
                settings.hotkeys[hotkey] = input
                self.SV_HKS[hotkey].set(input)
        listener.renew_listeners(settings)

    def set_cb(self, cb, settings, listener):
        if cb == 'emp':
            settings.special['empowered'] = self.BV_EMP.get()
            listener.renew_listeners(settings)
        elif cb == 'conv':
            settings.special['fast_convert'] = self.BV_FASTCONV.get()
            listener.renew_listeners(settings)
