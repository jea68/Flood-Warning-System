#we create a list of dates and times water level is recorded : this becomes the inpiut for the x values
#create list of water levels in same order as the times : becomes y values
#make a graph from them

import matplotlib.pyplot as plt
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list

def plot_water_levels(station, dates, levels):

    X = [station.typical_range[0]] * (len(dates))
    Y = [station.typical_range[1]] * (len(dates))

    plt.plot(dates, levels, label= "$\water _ level$", color = "blue")
    plt.plot(dates, X, label = "$\ typical_ Low_value$", color = "red" )
    plt.plot(dates, Y, label = "$\ typical_High_value$", color = "red")

    plt.legend()


    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title("{}".format(station.name))
    plt.tight_layout() 

    return plt.show()