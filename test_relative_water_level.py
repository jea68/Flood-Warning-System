from floodsystem.station import MonitoringStation
import test_utils
from task2B import relative_water_level, stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
stations = build_station_list()
update_water_levels(stations)
def test_stations_level_over_threshold():
    output_level = stations_level_over_threshold(stations, 10000)
    assert output_level == None
test_stations_level_over_threshold()

    
