class PoolSpotList:
    def __init__(self, poolspots):
        self.spots = [PoolSpot(wp) for wp in poolspots]
        self.last_spot = -1

    def next_spot(self):
        if self.last_spot + 1 < len(self.spots):
            self.last_spot += 1
        else:
            self.last_spot = 0
        return self.spots[self.last_spot]


class PoolSpot:
    def __init__(self, wp):
        self.wp = wp
        self.act_coords = act_coords(wp)
        self.wp_coords = wp_coords(wp)


def act_coords(wp):
    switcher = {
        **dict.fromkeys(
            [
                'cemetry_of_the_forsaken',
                'the_weeping_hollow',
                'southern_highlands',
                'leorics_manor_courtyard',
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
        4: (1450, 370),
        5: (590, 550),
    }
    return switcher.get(wp, (0, 0))


def wp_coords(wp):
    switcher = {
        'new_tristram': (740, 620),
        'hidden_camp': (1040, 780),
        'bastions_keep_stronghold': (510, 485),  # Ist von a3
        'the_survivors_enclave': (1170, 630),
        'cemetry_of_the_forsaken': (630, 370),
        'the_weeping_hollow': (690, 485),
        'southern_highlands': (810, 795),
        'leorics_manor_courtyard': (580, 585),
        'howling_plateau': (880, 560),
        'road_to_alcarnus': (1290, 600),
        'the_battlefields': (630, 330),
        'bridge_of_korsikk': (800, 460),
        'rakkis_crossing': (870, 300),
        'tower_of_the_dammned_level_1': (1320, 340),
        'tower_of_the_cursed_level_1': (1320, 610),
    }
    return switcher.get(wp, (0, 0))
