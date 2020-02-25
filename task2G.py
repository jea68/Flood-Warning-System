#task2G
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.datafetcher import fetch_measure_levels
import datetime
stations = build_station_list()
def risk(stations):
    update_water_levels(stations)
    low = []
    high = []
    moderate = []
    severe = []
    levels = []
    date = []
    for station in stations:
        date, levels = fetch_measure_levels(measure_id=station.measure_id, dt= datetime.timedelta(days=2))
        if len(levels) == 0 or levels == None or levels[0] == None or levels[1] == None:
            water_level = "unkown water level change"
        elif (levels[1] - levels[0]) < 0 :
            water_level = "water level decreased"
        elif (levels[1] - levels[0]) > 0 :
            water_level = "water level rising"
        elif levels[1] == levels[0] :
            water_level  = "constant water level"
        
        if station.latest_level == None :
            low = low
            high = high
            moderate = moderate
            severe = severe 
        elif station.latest_level < 0.75 :
            low.append((station.name, station.latest_level, water_level))
        elif 0.75 <= station.latest_level <= 1.0 : 
            moderate.append((station.name, station.latest_level, water_level))
        elif 1.0 < station.latest_level <= 3 :
            high.append((station.name, station.latest_level, water_level))
        elif 3 < station.latest_level : 
            severe.append((station.name, station.latest_level, water_level)) 
    print("")
    print("low flood risk rivers: ", low)
    print("")
    print("moderate flood risk rivers: ", moderate)
    print("")
    print("high flood risk rivers: ", high)
    print("")
    print("severe flood risk rivers: ", severe)
    print("")
    return(low, moderate, high, severe)

risk(stations)

