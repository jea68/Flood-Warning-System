import test_utils
from Task2C import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
stations_highest_rel_level
stations = build_station_list()
update_water_levels(stations)
def test_stations_highest_rel_level():
    stations = build_station_list()
    output_highest = stations_highest_rel_level(stations, 3)
    assert len(output_highest) == 3
test_stations_highest_rel_level()