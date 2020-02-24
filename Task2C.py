from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
stations = build_station_list()
update_water_levels(stations)
def stations_highest_rel_level(stations, N):
    station_level =[]
    tol = 0.8
    for station in stations:
        if station.latest_level == None:
            station_level = station_level
        elif station.latest_level > tol:
            station_level.append((station.name, station.latest_level))    
    station_level.sort(key=lambda x: float(x[1]), reverse=True)
    highest = station_level[0:N]
    print(highest)
    return(highest)
  
stations_highest_rel_level(stations, 10)
