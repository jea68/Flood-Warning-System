from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
stations = build_station_list()
def relative_water_level(self):
    update_water_levels(stations)
    high_low = []
    for station in stations:
        if station.latest_level == None:
            high_low = high_low
        elif station.latest_level >= 0.75:
            high_low.append(station)
        elif station.latest_level <= 0.25:
            high_low.append(station)
    stations_level_over_threshold(high_low, 0.8)

def stations_level_over_threshold(stations, tol):
    station_level =[]
    for station in stations:
        if station.latest_level > tol:
            station_level.append((station.name, station.latest_level))
    station_level.sort(key=lambda x: float(x[1]), reverse=True)
    stations_highest_rel_level(station_level, len(station_level))


def stations_highest_rel_level(stations, N):
    highest = stations[0:10]
    print(highest)
    return(highest)
relative_water_level(stations)
