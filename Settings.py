import json


class Settings:
    def __init__(self):
        try:
            with open('./settings.json') as f:
                self.json = json.load(f)
        except FileNotFoundError:
            self.json = {
                "paths": {"Fiddler": "", "TurboHUD": "", "pHelper": ""},
                "hotkeys": {
                    "cube_conv_sm": "5+strg",
                    "cube_conv_lg": "6+strg",
                    "reforge": "4+strg",
                    "open_gr": "",
                    "upgrade_gem": "",
                    "leave_game": "",
                    "salvage": "",
                    "gamble": "alt",
                    "drop_inventory": "f+strg",
                    "port_a1": "",
                    "port_a2": "",
                    "port_a3": "",
                    "port_a5": "",
                    "port_pool": "",
                    "right_click": "",
                    "left_click": "",
                    "lower_difficulty": "",
                    "swap_armor": "",
                    "pause": "",
                },
                "poolspots": [
                    "cemetry_of_the_forsaken",
                    "the_weeping_hollow",
                    "the_battlefields",
                    "southern_highlands",
                    "leorics_manor_courtyard",
                    "howling_plateau",
                    "road_to_alcarnus",
                    "bridge_of_korsikk",
                    "rakkis_crossing",
                    "tower_of_the_dammned_level_1",
                    "tower_of_the_cursed_level_1",
                ],
                "special": {
                    "empowered": False,
                    "fast_convert": False,
                    "armor_swap_amount": 3,
                    "spare_columns": 1,
                    "gamble_item": "ring",
                    "auto_start": False,
                },
            }
        self.paths = self.json['paths']
        self.hotkeys = self.json['hotkeys']
        self.poolspots = self.json['poolspots']
        self.special = self.json['special']

    def save(self):
        with open('./settings.json', 'w') as f:
            d = {
                'paths': self.paths,
                'hotkeys': self.hotkeys,
                'poolspots': self.poolspots,
                'special': self.special,
            }
            json.dump(d, f)
