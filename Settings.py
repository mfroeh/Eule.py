import json


class Settings:
    def __init__(self):
        try:
            with open('./settings.json') as f:
                _json = json.load(f)
                self.json = _json
                self.paths = _json['paths']
                self.hotkeys = _json['hotkeys']
                self.special = _json['special']
        except FileNotFoundError:
            self.json = {
                "paths": {"Fiddler": "", "TurboHUD": "", "pHelper": ""},
                "hotkeys": {
                    "cube_conv_sm": "5+strg",
                    "cube_conv_lg": "6+strg",
                    "reforge": "4+strg",
                    "open_gr": "",
                    "gem_up": "",
                    "leave_game": "",
                    "salvage": "",
                    "drop_inventory": "f+strg",
                    "right_click": "",
                    "left_click": "",
                    "port_a1": "",
                    "lower_diff": "",
                    "pause": "",
                    "armor_swap": "",
                },
                "special": {"empowered": False, "fast_convert": False},
            }
            self.paths = self.json['paths']
            self.hotkeys = self.json['hotkeys']
            self.special = self.json['special']

    def save(self):
        with open('./settings.json', 'w') as f:
            self.json['paths'] = self.paths
            self.json['hotkeys'] = self.hotkeys
            self.json['special'] = self.special
            json.dump(self.json, f)
