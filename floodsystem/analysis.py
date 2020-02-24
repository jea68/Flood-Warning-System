import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list

stations = build_station_list()


def polyfit(dates, levels, p):

    x = matplotlib.dates.date2num(dates)
    y = levels
    # Using shifted x values, find coefficient of best-fit
# polynomial f(x) of degree 4
    p_coeff = np.polyfit(x - x[0], y, p)

# Convert coefficient into a polynomial that can be evaluated
# e.g. poly(0.3)
    poly = np.poly1d(p_coeff)
    d0 = x[0]
    return (poly, d0)


