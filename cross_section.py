###script to produce cross section of a plot
###add library
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from matplotlib.colors import from_levels_and_colors
from cartopy import crs
from cartopy.feature import NaturalEarthFeature, COLORS
from netCDF4 import Dataset 
from wrf import (getvar, to_np, get_cartopy, latlon_coords, vertcross,
		 cartopy_xlim, cartopy_ylim, interpline, CoordPair)

#######Download Data
######specify the location of the data
#path_in
path_out = "/home/aksalatenna/plots/"
ncfile = Dataset("wrfinput_d03")
#ncfile = Dataset("wrfout_d03_2021-06-01_00.nc")


###### take out the variable
cross_start = CoordPair(lat=13.5, lon=123.5)
cross_end =   CoordPair(lat=14.0, lon=124.0)


####Get the WRF Variables 
ht = getvar(ncfile, "z",  timeidx=-1)
#ter = getvar(ncfile, "HGT", timeidx=-1)
ter = getvar(ncfile, "ter", timeidx=-1)
###cloud mixing ratio
QCLOUD = getvar(ncfile, "QCLOUD", timeidx=-1)

z_cross = vertcross(QCLOUD, ht, wrfin=ncfile,
                    start_point=cross_start,
 	   	    end_point=cross_end,
                    latlon=True, 
                    meta=True)

#print the cross section
z_cross.plot()
plt.savefig(path_out + "z_cross.png")
plt.show()

###Make a copy of the z-cross data. Let use regular numpy arrays for this
dbz_cross_filled = np.ma.copy(to_np(z_cross))

###for each cross section column, find the first index with non-missing
##values and copy these to the missing elements below
for i in range(dbz_cross_filled.shape[-1]):
    column_vals = dbz_cross_filled[:,i]
    first_idx = int(np.transpose((column_vals >-10).nonzero())[0])
    dbz_cross_filled[0:first_idx,i] = dbz_cross_filled[first_idx,i]

####get the terrain heights along the cross section line
ter_line = interpline(ter, wrfin=ncfile, start_point= cross_start,
                      end_point=cross_end)

####get the cartopy projection object
cart_proj = get_cartopy(QCLOUD)

#######create the pfigure
fig = plt.figure(figsize=(8,6))
ax_cross = plt.axes()

xs = np.arange(0, z_cross.shape[-1],1)
ys = to_np(z_cross.coords["vertical"])
QCLOUD_contours = ax_cross.contourf(xs, ys,
				   to_np(dbz_cross_filled),
				   cmap="Blues")
####add the color bar
cb_QCLOUD = fig.colorbar(QCLOUD_contours, ax=ax_cross)
cb_QCLOUD.ax.tick_params(labelsize=8)

### fill in the mountain area
ht_fill = ax_cross.fill_between(xs, 0, to_np(ter_line),
				facecolor="saddlebrown")

#####set the x-ticks to use latitude and longitude labels
coord_pairs = to_np(z_cross.coords["xy_loc"])
x_ticks = np.arange(coord_pairs.shape[0])
x_labels = [pair.latlon_str() for pair in to_np(coord_pairs)]

#############set the number of x ticks below
num_ticks = 5 
thin = int((len(x_ticks) / num_ticks) + .5)
ax_cross.set_xticks(x_ticks[::thin])
ax_cross.set_xticklabels(x_labels[::thin], rotation=45, fontsize=8)

####set the x-axis & y-axis labels
ax_cross.set_xlabel("Latitidue, Longitude", fontsize=17)
ax_cross.set_ylabel("Height (m)", fontsize=17)

##########set the range of y-axis
ax_cross.set_ylim(0,5000)

#########set the range of y-axis
ax_cross.set_title("QCLOUD (kg kg-1)", {"fontsize" : 20})
plt.savefig(path_out + "ax_cross_sect.png")
plt.show()
