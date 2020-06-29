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
                    "cube_conv_sm": "",
                    "cube_conv_lg": "",
                    "reforge": "",
                    "open_gr": "",
                    "upgrade_gem": "",
                    "leave_game": "",
                    "salvage": "",
                    "gamble": "",
                    "drop_inventory": "",
                    "port_a1": "",
                    "port_a2": "",
                    "port_a3": "",
                    "port_a4": "",
                    "port_a5": "",
                    "port_pool": "",
                    "right_click": "",
                    "left_click": "",
                    "lower_difficulty": "",
                    "skill_macro": "",
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
                    "cube_conv_speed": 'normal',
                    "armor_swap_amount": 3,
                    "choose_gem": False,
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
                "skill_macro": {
                    "profiles": {
                        "Profile 1": {
                            "name": "Profile 1",
                            # 1st Skill, 2nd Skill,..., LeftClick Skill, RightClick Skill
                            "hotkeys": [
                                None,
                                None,
                                None,
                                None,
                                'LeftClick',
                                'RightClick',
                            ],
                            "delays": [0, 0, 0, 0, 0, 0],
                        }
                    },
                    "active": "Profile 1",
                },
            }
        self.paths = self.json['paths']
        self.hotkeys = self.json['hotkeys']
        self.abbrevations = self.json['abbrevations']
        self.poolspots = self.json['poolspots']
        self.special = self.json['special']
        self.skill_macro = self.json["skill_macro"]

    def save(self):
        with open('./settings.json', 'w') as f:
            d = {
                'paths': self.paths,
                'hotkeys': self.hotkeys,
                'abbrevations': self.abbrevations,
                'poolspots': self.poolspots,
                'special': self.special,
                'skill_macro': self.skill_macro,
            }
            json.dump(d, f)
