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
    stat_town_dist = []
    global ordered
    ordered = []
    for station in stations:
        distance = haversine(p, station.coord)
        stat_town_dist.append((station.name, distance, station.town))
    ordered = sorted_by_key(stat_town_dist, 1, reverse=False)
    print("")
    print("the 10 closest stations are: (", ordered[:10], ")")
    print("")
    print("the 10 furthest stations are: (", ordered[-10:], ")")
    return(ordered)

stations_by_distance(stations, p)

