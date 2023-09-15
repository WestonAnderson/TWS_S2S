#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 09:01:23 2023

@author: wanders7
"""

import cartopy.io.shapereader as shpreader
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
import xarray as xr
import regionmask

#select the basin to read in. You can use the "bsnNames" object further down to get a list of all the named basins
basin = 'LIMPOPO'

#read lat lon from whatever file you want to rasterize to match
cDF = xr.open_dataset('/Volumes/Svalbard/LargeDatasets/Crop_mapping/GEOGLAM/NetCDF/allCrops_05deg.nc')
lon,lat = np.meshgrid(cDF.longitude,cDF.latitude)

#read in the river basin files
grdcPath = '/Users/wanders7/Downloads/mrb_shp_zip/mrb_basins.shp'
reader = shpreader.Reader(grdcPath)
basinShps = list(reader.geometries())
bsns = cfeature.ShapelyFeature(basinShps, ccrs.PlateCarree())
bsnNames = [shape_dict.attributes['RIVER_BASI'] for shape_dict in list(reader.records())] #write all shapefile basin

loc = np.where(np.isin(bsnNames,basin))[0][0] #find the location of the shape in the shapefile
seg = basinShps[loc] #this is the geometry object of the basin
adm = cfeature.ShapelyFeature([seg], ccrs.PlateCarree())#if you're looking to plot it you have to project it into the appropriate space for cartopy

#this converts the selected shapefile to a mask on the resolution of lon and lat
msk = np.array(regionmask.Regions([basinShps[loc]]).mask(lon,lat)) #find the location mask
msk[msk==0]=1


