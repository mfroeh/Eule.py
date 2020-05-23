def key_to_hex(key):
    switcher = {
        '0': 0x30,
        '1': 0x31,
        '2': 0x32,
        '3': 0x33,
        '4': 0x34,
        '5': 0x35,
        '6': 0x36,
        '7': 0x37,
        '8': 0x38,
        '9': 0x39,
        'a': 0x41,
        'b': 0x42,
        'c': 0x43,
        'd': 0x44,
        'e': 0x45,
        'f': 0x46,
        'g': 0x47,
        'h': 0x48,
        'i': 0x49,
        'j': 0x4A,
        'k': 0x4B,
        'l': 0x4C,
        'm': 0x4D,
        'n': 0x4E,
        'o': 0x4F,
        'p': 0x50,
        'q': 0x51,
        'r': 0x52,
        's': 0x53,
        't': 0x54,
        'u': 0x55,
        'v': 0x56,
        'w': 0x57,
        'x': 0x58,
        'y': 0x59,
        'z': 0x5A,
        'enter': 0x0D,
        'esc': 0x1B,
        'space': 0x20,
        'shift': 0x60,
        'alt': 0x12,
    }
    return switcher.get(key, 0x0)


def map_act_coords_by_act(act):
    switcher = {
        1: (740, 620),
        2: (1090, 525),
        3: (710, 400),
        4: (1450, 370),
        5: (590, 550),
    }
    return switcher.get(act, (0, 0))


def map_town_coords_by_act(act):
    switcher = {
        1: (1020, 490),
        2: (1040, 780),
        3: (510, 485),
        4: (515, 745),
        5: (1170, 625),
    }
    return switcher.get(act, (0, 0))


def poolspots():
    return {
        1: [
            'cemetry_of_the_forsaken',
            'the_weeping_hollow',
            'southern_highlands',
            'leorics_manor_courtyard',
        ],
        2: ['howling_plateau', 'road_to_alcarnus'],
        3: [
            'the_battlefields',
            'bridge_of_korsikk',
            'rakkis_crossing',
            'tower_of_the_dammned_level_1',
            'tower_of_the_cursed_level_1',
        ],
        4: ['lower_realm_of_infernal_fate', 'realm_of_fractured_fate'],
        5: ['pandemonium_fortress_level_1'],
    }
