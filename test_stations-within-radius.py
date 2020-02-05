from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
from floodsystem.station import MonitoringStation


def test_stations_within_radius():
    # Create a station 1
    s_id = "Test Station id"
    m_id = "Test-m-id"
    label = "Test station A"
    coord = (50, 5.0)       #test co-ordinate A distance from centre = 2376.46km
    trange = (-2.0, 3.0)
    river = "River X" 
    town = "Test Town"
    A = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station 2
    s_id = "Test Station id"
    m_id = "Test-m-id"
    label = "Test station B"
    coord = (100, 10)       #test co-ordinate B distance from centre = 7779.8km
    trange = (-2.0, 3.0)
    river = "River Y" 
    town = "Test Town"
    B = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    test_stations = [A, B]
    test_centre = (30,15)       #test centre
    assert stations_within_radius(test_stations, test_centre, r = 8000) == ['Test station A', 'Test station B']
    assert stations_within_radius(test_stations, test_centre, r = 5000 ) == ['Test station A'] # test to see if it shows station that is not in radius

    