from floodsystem.station import MonitoringStation

def test_typical_range_consistent():

    # Create a station
    s_id = "Test Station id"
    m_id = "Test-m-id"
    label = "Test station"
    coord = (-1.0, 2.0)
    trange = (-2.0, 3.0)
    river = "River Test"
    town = "Test Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert s.typical_range_consistent() == True

    trange_inconsistent = (3.0,0.0)
    d = MonitoringStation(s_id, m_id, label, coord, trange_inconsistent, river, town)
    assert d.typical_range_consistent() == False

    trange_none = None

    f = MonitoringStation(s_id, m_id, label, coord, trange_none, river, town)

    assert f.typical_range_consistent() == False

