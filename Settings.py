import json


class Settings:
    def __init__(self):
        try:
            with open('./settings.json') as f:
                self.json = json.load(f)
        except:
            self.json = {
                "paths": {"Fiddler": "", "TurboHUD": "", "pHelper": ""},
                "hotkeys": {
                    "cube_conv_sm": "5+ctrl",
                    "cube_conv_lg": "6+ctrl",
                    "reforge": "4+ctrl",
                    "open_gr": "",
                    "upgrade_gem": "",
                    "leave_game": "x+ctrl",
                    "salvage": "alt+v",
                    "gamble": "",
                    "drop_inventory": "f+strg",
                    "port_a1": "ctrl+1",
                    "port_a2": "",
                    "port_a3": "",
                    "port_a5": "",
                    "port_pool": "",
                    "right_click": "",
                    "left_click": "",
                    "lower_difficulty": "",
                    "swap_armor": "",
                    "pause": "f10",
                },
                "abbrevations": {
                    'pool': 'There is a pool on me please TP!',
                    'take': 'Take the Pylon!',
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
                    "abbrevations_enabled": True,
                    "auto_start": False,
                    "auto_open": False,
                    "auto_open_option": "rift",
                    "auto_accept_gr": False,
                    "auto_upgrade_gem": False,
                    "auto_gamble": False,
                },
            }
        self.paths = self.json['paths']
        self.hotkeys = self.json['hotkeys']
        self.abbrevations = self.json['abbrevations']
        self.poolspots = self.json['poolspots']
        self.special = self.json['special']

    def save(self):
        with open('./settings.json', 'w') as f:
            d = {
                'paths': self.paths,
                'hotkeys': self.hotkeys,
                'abbrevations': self.abbrevations,
                'poolspots': self.poolspots,
                'special': self.special,
            }
            json.dump(d, f)
