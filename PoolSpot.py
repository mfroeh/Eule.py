from utils import act_coords, wp_coords


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
