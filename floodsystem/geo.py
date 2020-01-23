# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

from floodsystem.stationdata import build_station_list
import haversine

print(tuple(haversine.Unit))

def stations_within_radius(stations, centre, r):
    for station in stations:
        x = 52.2053
        y = 0.1218
        centre = (x,y)
        