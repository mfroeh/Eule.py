class PoolSpotList:
    def __init__(self, poolspots):
        self.spots = []

        for poolspot in poolspots:
            act_coords = map_act_coords_by_wp(poolspot)
            wp_coords = map_wp_coords_by_wp(poolspot)
            self.spots.append((act_coords, wp_coords))

        self.last_index = -1

    def next_spot(self):
        next_index = self.last_index + 1
        if next_index < len(self.spots):
            self.last_index = next_index
            return self.spots[next_index]
        elif self.spots:
            self.last_index = 0
            return self.spots[0]


def map_act_coords_by_wp(wp):
    switcher = {
        **dict.fromkeys(
            [
                'cemetry_of_the_forsaken',
                'the_weeping_hollow',
                'southern_highlands',
                'leorics_manor_courtyard',
                'fields_of_misery',
                'drowned_temple',
            ],
            (740, 620),
        ),
        **dict.fromkeys(['howling_plateau', 'road_to_alcarnus'], (1090, 525)),
        **dict.fromkeys(
            [
                'the_battlefields',
                'bridge_of_korsikk',
                'rakkis_crossing',
                'tower_of_the_dammned_level_1',
                'tower_of_the_cursed_level_1',
            ],
            (710, 400),
        ),
        **dict.fromkeys(
            ['lower_realm_of_infernal_fate', 'realm_of_fractured_fate'], (1450, 370)
        ),
        **dict.fromkeys(['pandemonium_fortress_level_1'], (590, 550)),
    }
    return switcher.get(wp, (0, 0))


def map_wp_coords_by_wp(wp):
    switcher = {
        # 'new_tristram': (740, 620),
        # 'hidden_camp': (1040, 780),
        # 'bastions_keep_stronghold': (510, 485),  # Ist von a3
        # 'the_survivors_enclave': (1170, 630),
        'cemetry_of_the_forsaken': (630, 370),
        'the_weeping_hollow': (690, 485),
        'southern_highlands': (810, 795),
        'leorics_manor_courtyard': (580, 585),
        'fields_of_misery': (450, 320),
        'drowned_temple': (580, 250),
        'howling_plateau': (880, 560),
        'road_to_alcarnus': (1290, 600),
        'the_battlefields': (630, 330),
        'bridge_of_korsikk': (800, 460),
        'rakkis_crossing': (870, 300),
        'tower_of_the_dammned_level_1': (1320, 340),
        'tower_of_the_cursed_level_1': (1320, 610),
        'lower_realm_of_infernal_fate': (1480, 300),
        'realm_of_fractured_fate': (560, 510),
        'pandemonium_fortress_level_1': (800, 325),
    }
    return switcher.get(wp, (0, 0))
