###compute dianostic variables

from __future__ import print_function
from netCDF4 import Dataset
from wrf import getvar, interpline, CoordPair, xy_to_ll, ll_to_xy

ncfile = Dataset("wrfinput_d03")

# Get the wind vector
QVAPOR = getvar(ncfile, "QVAPOR")

print(QVAPOR)


x_y = ll_to_xy(ncfile, 13.7, 123.5)

print(x_y)

#QVAPOR_LOC = QVAPOR, x_y[0], x_y[1]

#print(QVAPOR_LOC)
