# task to return the rivers with a monitoring station
from floodsystem.stationdata import build_station_list
stations = build_station_list()
global station_rivers
def rivers_with_station(stations):
    global station_rivers
    station_rivers = {}
    for station in stations:
        station_rivers[station.river] = station.name
    return(station_rivers)
   
def stations_by_river(stations):
    global station_rivers
    ordered_rivers = sorted(station_rivers)
    print(ordered_rivers)
    print("the number of stations that has a river near it is ", len(station_rivers))
    river_Aire = []
    river_Cam = []
    river_Thames = []
    for station in stations:    
        if station.river == "River Aire":
            river_Aire.append(station.name)
        elif station.river == "River Cam":
            river_Cam.append(station.name)
        elif station.river == "River Thames":
            river_Thames.append(station.name)
    print("")
    print("the stations near the River Aire is: ", river_Aire)
    print("")
    print("the stations near the River Cam is: ", river_Cam)
    print("")
    print("the stations near the River Thames is: ", river_Thames)
    print("")
    return(river_Aire, river_Cam, river_Thames)
rivers_with_station(stations)
stations_by_river(stations)