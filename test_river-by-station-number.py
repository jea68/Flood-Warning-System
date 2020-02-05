from floodsystem.stationdata import build_station_list
from floodsystem.geo import river_by_station_number
from floodsystem.station import MonitoringStation

def test_rivers_with_station():
    # Create a station 1
    s_id = "Test Station id"
    m_id = "Test-m-id"
    label = "Test station"
    coord = (-1.0, 2.0)
    trange = (-2.0, 3.0)
    river = "River X" # 1st station with river X
    town = "Test Town"
    A = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station 2
    s_id = "Test Station id"
    m_id = "Test-m-id"
    label = "Test station"
    coord = (-1.0, 2.0)
    trange = (-2.0, 3.0)
    river = "River X" #2nd station with river X
    town = "Test Town"
    B = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station 3
    s_id = "Test Station id"
    m_id = "Test-m-id"
    label = "Test station"
    coord = (-1.0, 2.0)
    trange = (-2.0, 3.0)
    river = "River Y" #1st station with river Y
    town = "Test Town"
    C = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station 4
    s_id = "Test Station id"
    m_id = "Test-m-id"
    label = "Test station"
    coord = (-1.0, 2.0)
    trange = (-2.0, 3.0)
    river = "River Y" # 2nd station with river Y
    town = "Test Town"
    D = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station 5
    s_id = "Test Station id"
    m_id = "Test-m-id"
    label = "Test station"
    coord = (-1.0, 2.0)
    trange = (-2.0, 3.0)
    river = "River Z" # 1st station with river Z
    town = "Test Town"
    E = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station 6
    s_id = "Test Station id"
    m_id = "Test-m-id"
    label = "Test station"
    coord = (-1.0, 2.0)
    trange = (-2.0, 3.0)
    river = "River A"  #1st station with river A
    town = "Test Town"
    F = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station 7
    s_id = "Test Station id"
    m_id = "Test-m-id"
    label = "Test station"
    coord = (-1.0, 2.0)
    trange = (-2.0, 3.0)
    river = "River X" # 3rd station with River X
    town = "Test Town"
    G = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station 8
    s_id = "Test Station id"
    m_id = "Test-m-id"
    label = "Test station"
    coord = (-1.0, 2.0)
    trange = (-2.0, 3.0)
    river = "River B" # 1st station with river B
    town = "Test Town"
    H = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station 9
    s_id = "Test Station id"
    m_id = "Test-m-id"
    label = "Test station"
    coord = (-1.0, 2.0)
    trange = (-2.0, 3.0)
    river = "River X" #4th station with river X
    town = "Test Town"
    I = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station 10
    s_id = "Test Station id"
    m_id = "Test-m-id"
    label = "Test station"
    coord = (-1.0, 2.0)
    trange = (-2.0, 3.0)
    river = "River Y" #3rd station with River Y
    town = "Test Town"
    J = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station 11
    s_id = "Test Station id"
    m_id = "Test-m-id"
    label = "Test station"
    coord = (-1.0, 2.0)
    trange = (-2.0, 3.0)
    river = "River Z" #2nd station with river Z
    town = "Test Town"
    K = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station 12
    s_id = "Test Station id"
    m_id = "Test-m-id"
    label = "Test station"
    coord = (-1.0, 2.0)
    trange = (-2.0, 3.0)
    river = "River A" # 2nd station with river A
    town = "Test Town"
    L = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    


    test_stations = [A, B, C, D, E, F, G, H, I, J, K, L]
    assert river_by_station_number(test_stations, N=2) == [('River X', 4), ('River Y', 3)]
    assert river_by_station_number(test_stations, N=4) == [('River X', 4), ('River Y', 3), ('River Z', 2), ('River A', 2)]
    assert river_by_station_number(test_stations, N=3) == river_by_station_number(test_stations, N=4) # tests that it includes rivers with same number of stations
    assert river_by_station_number(test_stations, N=5) == [('River X', 4), ('River Y', 3), ('River Z', 2), ('River A', 2), ('River B', 1)]