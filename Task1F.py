#Function that returns false if the first value is bigger than second + a function that shows all stations which are wrong

from floodsystem.stationdata import build_station_list
stations = build_station_list()


def typical_range_consistent(self):
    for station in self:
        typical_range = station.typical_range
        if typical_range == None:
            print(False)
        else:
            difference = typical_range[0] - typical_range[1]
            print(difference < 0)


def inconsistent_typical_range__stations(stations):
    y = []
    for station in stations:
        typical_range = station.typical_range
        if typical_range == None:
            z = ["{}".format(station.name)]
            y = y + z
        else:
            difference = typical_range[0] - typical_range[1]
            if difference > 0:
                x = ["{}".format(station.name)]
                y = y + x
    
    false_stations = sorted(y)
    return false_stations

print(inconsistent_typical_range__stations(stations))
print(typical_range_consistent(self=stations))