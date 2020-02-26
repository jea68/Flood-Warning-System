from floodsystem.station import MonitoringStation
from floodsystem.geo import river_Thames
from floodsystem.geo import river_Cam
from floodsystem.geo import river_Aire
from floodsystem.geo import ordered_rivers
from floodsystem.geo import rivers_with_station 

def test_rivers_with_station():
    # Create a station
    s_id = "test-id"
    m_id = "test-id"
    label = "station"
    coord = (0.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River Thames"
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
    rivers_with_station(test_stations)
    print(len(test_stations))
    print(len(ordered_rivers))
    assert len(test_stations) == len(ordered_rivers)
