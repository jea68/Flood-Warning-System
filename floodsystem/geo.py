# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
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
        