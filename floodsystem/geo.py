# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
p = (52.2053, 0.1218)
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit
import python_utils
stations = build_station_list()
global ordered
def sorted_by_key(x, i, reverse=False):
    def key(element):
        return element[i]
    return sorted(x, key=key, reverse=reverse)

def stations_by_distance(stations, p):
    stat_town_dist = []
    global ordered
    ordered = []
    for station in stations:
        distance = haversine(p, station.coord)
        stat_town_dist.append((station.name, distance, station.town))
    ordered = sorted_by_key(stat_town_dist, 1, reverse=False)
    print("")
    print("the 10 closest stations are: (", ordered[:10], ")")
    print("")
    print("the 10 furthest stations are: (", ordered[-10:], ")")
    return(ordered)

stations_by_distance(stations, p)


def stations_within_radius(stations, centre, r):
    y = []
    for station in stations:
        r2 = haversine(centre, station.coord)
        
        if r2 <= r:
            x = ["{}".format(station.name)]
            y = y + x
        
    stations_within_radius = sorted(y)
    return stations_within_radius

stations = build_station_list()
global station_rivers
global ordered_rivers
def rivers_with_station(stations):
    global station_rivers
    station_rivers = {}
    for station in stations:
        station_rivers[station.river] = station.name
    stations_by_river(stations)
   
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
    return(river_Thames)
rivers_with_station(stations)



def river_by_station_number(stations, N):
    
    rivers = {}
    for station in stations:
        river = station.river
        if river in rivers:
            rivers[river] += 1
        else:
            rivers[river] = 1
            
    total_ordered_rivers = sorted(rivers.items(), key = lambda kv:(kv[1], kv[0]), reverse = True)
    name_1 ={}
    for p, m in total_ordered_rivers:
        name_1[p] = m
    
    
    dictValues = list (name_1.values())
    Value = dictValues[N-1]
    if len(dictValues) > N:
        if dictValues[N] ==  Value:
            N += 1
        else:
            N = N
    else:
        N=N
    ordered_rivers_N = sorted(rivers.items(), key = lambda kv:(kv[1], kv[0]), reverse = True)[:N]
    return ordered_rivers_N
        
