from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
import test_utils
stations = build_station_list()
def test_stations_by_distance():
    # Create a station
    s_id = "test-id"
    m_id = "test-id"
    label = "station"
    coord = (0.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River "
    town = "Town"
    a = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
  
    s_id = "test"
    m_id = "test"
    label = "a station"
    coord = (5.0, 0.0)
    trange = (-2.3, 3.4445)
    river = "River y"
    town = "a Town"
    b = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    
   
    s_id = "id"
    m_id = "id"
    label = "the station"
    coord = (0.0, 3.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "the Town"
    c = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    test_stations = [a, b, c]
    output = stations_by_distance(test_stations, (0,0))
    assert len(test_stations) == len(output)
    
