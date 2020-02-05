from floodsystem.station import MonitoringStation
import test_utils
import task1B
from task1B import stations_by_distance
from haversine import haversine, Unit
from task1B import ordered
p =(0,0)
global test_stations

def test_stations_by_distance():
    global test_stations
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
    stations_by_distance(test_stations, (0,0))
    assert ordered == [("the station", 333.5852407005897, "the Town"), ("station", 444.7803209341316, "Town"), ("a station", 555.9754011676645, "a Town")]
    
  


