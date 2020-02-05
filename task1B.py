# task of finding the stations which are 10 closest and 10 furthest
p = (52.2053, 0.1218)
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit
import python_utils
stations = build_station_list()
global ordered
def sorted_by_key(x, i, reverse=False):
    def key(element):
        return element[i]
    return sorted(x, key=key, reverse=reverse)

def stations_by_distance(stations, p):
    global ordered
    stations = build_station_list()
    stat_town_dist = []
    for station in stations:
        distance = haversine(p, station.coord)
        stat_town_dist.append((station.name, distance, station.town))
    ordered = sorted_by_key(stat_town_dist, 1, reverse=False)
    print("the 10 closest stations are: (", ordered[:10], ")")
    print("")
    print("the 10 furthest stations are: (", ordered[-10:], ")")

stations_by_distance(stations, p)

import my_test_station
p = (4, 5)
stations_by_distance(my_test_station, p)
assert ordered == [("Upton Park", 5 ,"East Ham"), ("Stratford", 13, "Stratford")]

