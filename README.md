# Subseasonal to seasonal (S2S) Terrestrial water storage (TWS) Github

The project document with research questions, methods, and proposed datasts can be found [here](https://docs.google.com/document/d/1zxjAwmp0WKjTjrPXQ_zq9LG_gzlNKSq5iVJmAVhnPvg/edit)

A list of meeting notes from the project can be found [here](https://docs.google.com/document/d/1qAJKye5W6mPPwAZFzEdG7rBslx4xFyBmhCC6v--O0zc/edit)


## Datasets used in the analysis
Dataset name + variable + units + basin name

FLDAS Precipitation (mm/day)
GLEAM Surface and Root Zone Soil Moisture (mm3/mm3)
GIMMS 4g LAI (m2/m2)
GRACE-RL06 Liquid Water Equivalent (cm)
GLWS2 Reanalysis fields for groundwater storage (mm, absolute value), soil moisture storage (mm, absolute value), surface water storage (mm, absolute value), total terrestrial water storage (mm, ANOMALY)
GRUN-ENS Runoff Reconstruction (mm/day)
DAHITI water level data (m)
GRDC polygons for basins

## Methods:

Data Processing TWS:
(1) Deaseasonalize the data (anomalies relative to seasonal cycle)
(2) Linearly detrend

Basin-scale analysis:
Variables are trimmed using GRDC polygons, variables are area-weighted and aggregated to the basin scale at the monthly timestep. Variables are converted to monthly anomalies by subtracting the climatology and then standardized before calculating the autocorrelation and cross-correlation. For now, missing TWS data is linearly interpolated if there are fewer than 3 values missing and only data from 2002-2016 is used until we decide how to deal with the gap between GRACE and GRACE FO
