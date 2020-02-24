import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.analysis import polyfit

def test_polyfit():
    test_dates = []
    test_levels = []
    
    assert polyfit(dates = test_dates, levels = test_levels, p = 4) == x,y
    