import matplotlib
import matplotlib.pyplot as plt
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
import numpy as np
from floodsystem.analysis import polyfit

stations = build_station_list()

def plot_water_levels(station, dates, levels):

    X = [station.typical_range[0]] * (len(dates))
    Y = [station.typical_range[1]] * (len(dates))

    plt.plot(dates, levels, label = "Water Level",  color = "blue")
    plt.plot(dates, X, label = "Typical Low Value", color = "green")
    plt.plot(dates, Y  , label = "Typical High Value", color = "red")

    plt.legend()


    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title("{}".format(station.name))
    plt.tight_layout() 

    return plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels
    plt.plot(x, y, label = "Relative Water Level Plot", color = "blue")
# Plot polynomial fit at 30 points along interval (note that polynomial
# is evaluated using the shift x)
    p_coeff = np.polyfit(x - x[0], y, p)

# Convert coefficient into a polynomial that can be evaluated
# e.g. poly(0.3)
    poly = np.poly1d(p_coeff)
    d0 = x[0]

    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1 - x[0]), label = "Polynomial Fit", color = "red")

    plt.legend()

    plt.xlabel('date')
    plt.ylabel('relative water level ')
    plt.xticks(rotation=45)
    plt.title("{}".format(station.name))
    plt.tight_layout() 
# Display plot 
    return plt.show()