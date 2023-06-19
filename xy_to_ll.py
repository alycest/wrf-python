###compute dianostic variables

from __future__ import print_function
from netCDF4 import Dataset
from wrf import getvar, interpline, CoordPair, xy_to_ll, ll_to_xy

ncfile = Dataset("wrfinput_d03")

# Get the wind vector
lat_lon = xy_to_ll(ncfile, 100, 50)

print(lat_lon)

x_y = ll_to_xy(ncfile, lat_lon[0], lat_lon[1])

print(x_y)


#### example with multiple coordinates
lat_lon = xy_to_ll(ncfile, [50,50], [100,100])

print(lat_lon)

x_y = ll_to_xy(ncfile, lat_lon[0,:], lat_lon[1,:])

print (x_y)
