import haversine
from haversine import haversine, Unit
from floodsystem.stationdata import build_station_list
stations = build_station_list()

def stations_within_radius(stations, centre, r):
    y = []
    for station in stations:
        r2 = haversine(centre, station.coord)
        
        if r2 <= r:
            x = ["{}".format(station.name)]
            y = y + x
        
    stations_within_radius = sorted(y)
    return stations_within_radius

latitude = 52.2053
longitude = 0.1218
print("List of stations within a 10km radius from coordinates {},{}:".format(latitude,longitude))
print(stations_within_radius(stations, centre = (latitude,longitude), r = 10))