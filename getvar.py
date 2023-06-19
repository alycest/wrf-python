###compute dianostic variables

from __future__ import print_function
from netCDF4 import Dataset
from wrf import getvar

ncfile = Dataset("wrfinput_d03")

# Get the wind vector
QVAPOR = getvar(ncfile, "QVAPOR")
QCLOUD = getvar(ncfile, "QCLOUD")

print(QVAPOR, QCLOUD)
