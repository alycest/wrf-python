####guna try and write a script that does something

###set your environment
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from wrf import getvar, xy_to_ll, ll_to_xy, vertcross, CoordPair
import numpy as np

###add file
ncfile = Dataset("wrfinput_d03")
#path=("/root/WRF/WRFV4.5/run/BGMP_ideal/")
#ncfile = Dataset(path + "wrfbdy_d01")

####get variable
QVAPOR = getvar(ncfile, "QVAPOR")
#print(QVAPOR[:,20,30])
#print("\n")

x_y = ll_to_xy(ncfile, 13.08656, 123.5965)
print ("X & Y values")
print(x_y)
print("\n")


print("all qvapor")
print(QVAPOR)
print("\n")


print("lat = 13.08656, long = 123.5965")
print(QVAPOR[:, x_y[0], x_y[1]])
print("\n")

print(QVAPOR[:, x_y[0], x_y[1]])
#lat_lon = xy_to_ll(ncfile, 52, -13)

#print("lat,lon values")
#print(lat_lon)
#print("\n")

# Get the qvp attributes
#qvp = ncfile.variables["QVAPOR"]
#qvp_attrs = qvp.__dict__
#print("The attribute dict for QVAPOR")
#print(qvp_attrs)
#print("\n")

#T2 = ncfile.variables['T2'][0,:,:]

#lons= ncfile.variables["XLONG"][0]
#lats = ncfile.variables["XLAT"][0]

###Data bounds
#qvp = ncfile.variables["QVAPOR"][0]

#print(qvp)

#longmax, longmin = 123.5

