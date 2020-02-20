import matplotlib.pyplot as plt
import numpy as np
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list

def water_levels(station, dates):
    stations = build_station_list()
    levels = []
    time = []
    station_name = "Cam"
    for station in stations:
    
        if station.name == station_name:
            time, levels = fetch_measure_levels(measure_id=station.measure_id, dt= datetime.timedelta(days=2))
            X = [station.typical_range[0]] * (len(time))
            Y = [station.typical_range[1]] * (len(time))
    print(X) 
    print(Y)
    print(time)
    print(levels)
    plt.plot(time, levels, label = "$\ water_level$", color = "blue")
    plt.plot(time, X, label = "$\ typical_Low_value$", color = "red" )
    plt.plot(time, Y, label = "$\ typical_High_value$", color = "red")




    
    plt.legend()
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title("{}".format(station_name))
    plt.tight_layout() 

    return plt.show()

print(water_levels(station = 10, dates = 10))