from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.datafetcher import fetch_measure_levels
import datetime
stations = build_station_list()
update_water_levels(stations)
def risks(stations):
    low = []
    high = []
    moderate = []
    severe = []
    level = []
    date = []
    a = 0
    b = 0
    for station in stations:
        date, level = fetch_measure_levels(measure_id=station.measure_id, dt= datetime.timedelta(days=2))
        if len(level) == 0 or level == None or level[0] == None or level[1] == None :
            water_level_change = "unkown water level change"
            a = a + 1
        elif (level[1] - level[0]) < 0 :
            water_level_change = "water level decreased"
            b = b + 1
        elif (level[1] - level[0]) > 0 :
            water_level_change = "water level rising"
            b = b + 1
        elif level[1] == level[0] :
            water_level_change  = "constant water level"
            b = b + 1 
        if station.latest_level == None :
            low = low
            high = high
            moderate = moderate
            severe = severe 
        elif station.latest_level < 0.75 :
            low.append((station.name, station.latest_level, water_level_change))
        elif 0.75 <= station.latest_level <= 1.0 : 
            moderate.append((station.name, station.latest_level, water_level_change))
        elif 1.0 < station.latest_level <= 3 :
            high.append((station.name, station.latest_level, water_level_change))
        elif 3 < station.latest_level : 
            severe.append((station.name, station.latest_level, water_level_change)) 
    print("")
    print("low flood risk rivers: ", low)
    print("")
    print("moderate flood risk rivers: ", moderate)
    print("")
    print("high flood risk rivers: ", high)
    print("")
    print("severe flood risk rivers: ", severe)
    print("")
    return(b + a)

risks(stations)
