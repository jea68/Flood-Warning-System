#how to find distance between two coordinates

import haversine
lyon = (45.7597, 4.8422) # (lat, lon)
paris = (48.8567, 2.3508)
from haversine import haversine, Unit
haversine(lyon, paris)

point_1 = (100, 10)
point_2 = (50,5)
centre = (30,15)
print(haversine(centre,point_1))
print(haversine(centre,point_2))