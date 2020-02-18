#create a function in thr flood submodule that prints a list in DESCENDING order of the N stations with highest water level relative to typical range

#for stations find relative to typical range
# make list of name and relative water level
#sort into descending order
# return the first N stations


from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold

def stations_highest_rel_level(stations, N):
    update_water_levels(stations)

    for station in stations:
