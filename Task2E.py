#we create a list of dates and times water level is recorded : this becomes the inpiut for the x values
#create list of water levels in same order as the times : becomes y values
#make a graph from them

import matplotlib.pyplot as plt
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels


stations = build_station_list()
five_highest_water_levels = stations_highest_rel_level(stations, N = 5 )
print(five_highest_water_levels)

for values in five_highest_water_levels:
    station_name = values[0]
    print(station_name)
    for station in stations:
        if station.name == station_name:
            task_dates, water_level = fetch_measure_levels(measure_id=station.measure_id, dt= datetime.timedelta(days=10))
            print(plot_water_levels(station = station, dates = task_dates, levels = water_level))