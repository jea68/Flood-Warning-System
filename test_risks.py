
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import test_utils
from task2G import risks 
stations = build_station_list()
update_water_levels(stations)

def test_risk():
    output_risk = risks(stations)
    assert output_risk == len(stations)
    

    
