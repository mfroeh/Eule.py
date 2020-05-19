from ressources import map_act_coords_by_wp, map_wp_coords_by_wp


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
        self.act_coords = map_act_coords_by_wp(wp)
        self.wp_coords = map_wp_coords_by_wp(wp)
