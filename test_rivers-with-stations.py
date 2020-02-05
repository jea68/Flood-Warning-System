from floodsystem.station import MonitoringStation
from task1D import rivers_with_station
from task1D import river_Thames
from task1D import river_Cam
from task1D import river_Aire
from task1D import station_rivers
global test_stations

def test_rivers_with_station():
    global test_stations
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
    assert station_rivers == {'River Thames':'station', 'River y':'a station', 'River X':'the station'}
    assert len(station_rivers) == 3
    assert river_Aire == []
    assert river_Cam == []
    assert river_Thames == ['station']
 