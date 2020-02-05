#Function that returns false if the first value is bigger than second + a function that shows all stations which are wrong

from floodsystem.stationdata import build_station_list
stations = build_station_list()




def typical_range_consistent(self):
    typical_range = self.typical_range
    if typical_range == None:
        return False
    else:
        difference = typical_range[0] - typical_range[1]
        if difference < 0:
            return True
        else:
            return False

def inconsistent_typical_range__stations(stations):
    y = []
    for station in stations:
        typical_range = station.typical_range_consistent()
        if typical_range == False:
            z = ["{}".format(station.name)]
            y = y + z    
    false_stations = sorted(y)
    return false_stations

print(inconsistent_typical_range__stations(stations))