import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from numpy import poly1d
from floodsystem.station import MonitoringStation
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
from dateutil.tz import tzutc

def test_polyfit():
    test_dates = [datetime.datetime(2020, 2, 24, 21, 15, tzinfo=tzutc()), datetime.datetime(2020, 2, 24, 21, 0, tzinfo=tzutc()), datetime.datetime(2020, 2, 24, 20, 45, tzinfo=tzutc()), datetime.datetime(2020, 2, 24, 20, 30, tzinfo=tzutc()), datetime.datetime(2020, 2, 24, 20, 15, tzinfo=tzutc())]
    test_levels1 = [3, 3, 3, 3, 3]
    test_levels2 = [0.5, 1, 1.5, 2, 2.5]
    s_id = "Test Station id"
    m_id = "Test-m-id"
    label = "Test station"
    coord = (-1.0, 2.0)
    trange = (-2.0, 3.0)
    river = "River Test"
    town = "Test Town"
    A = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    test_plot1 = plot_water_level_with_fit(station = A, dates = test_dates, levels = test_levels1, p = 4)
    test_plot2 = plot_water_level_with_fit(station = A, dates = test_dates, levels = test_levels2, p = 4)
    return test_plot1, test_plot2
    
    