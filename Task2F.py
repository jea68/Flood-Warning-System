import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level



stations = build_station_list()
five_highest_water_levels = stations_highest_rel_level(stations, N = 5 )
print(five_highest_water_levels)

for values in five_highest_water_levels:
    station_name = values[0]
    print(station_name)
    for station in stations:
        if station.name == station_name:
            task_dates, water_level = fetch_measure_levels(measure_id=station.measure_id, dt= datetime.timedelta(days=10))
            print(plot_water_level_with_fit(station = station, dates = task_dates, levels = water_level, p = 4))

