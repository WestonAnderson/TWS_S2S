# Subseasonal to seasonal (S2S) Terrestrial water storage (TWS) Github

- The project document with research questions, methods, and proposed datasts can be found [here](https://docs.google.com/document/d/1zxjAwmp0WKjTjrPXQ_zq9LG_gzlNKSq5iVJmAVhnPvg/edit)

- A list of meeting notes from the project can be found [here](https://docs.google.com/document/d/1qAJKye5W6mPPwAZFzEdG7rBslx4xFyBmhCC6v--O0zc/edit)

- A google slide deck of preliminary findings is [here](https://docs.google.com/presentation/d/1IsyFnAmGQ887-0ufJH2BVsX2p2lxu5W47H4boSAdrtA/edit#slide=id.g290c274fe44_0_12)

## Datasets used in the analysis
Dataset name + variable + units + basin name

- FLDAS Precipitation (mm/day)
- GLEAM Surface and Root Zone Soil Moisture (mm3/mm3)
- GIMMS 4g LAI (m2/m2)
- GRACE-RL06 Liquid Water Equivalent (cm) (CSR_GRACE_GRACE-FO_RL06_Mascons_all-corrections_v02)
- GLWS2 Reanalysis fields for groundwater storage (mm, absolute value), soil moisture storage (mm, absolute value), surface water storage (mm, absolute value), total terrestrial water storage (mm, ANOMALY)
- GRUN-ENS Runoff Reconstruction (mm/day)
- DAHITI water level data (m)
- VODCA X-band VOD
- GRDC polygons for basins

## Methods:

### Data Processing TWS:
- Deaseasonalize the data (anomalies relative to seasonal cycle)
- Linearly detrend

### Basin-scale pre-process:
- variables are trimmed using GRDC polygons
- variables are area-weighted and aggregated to the basin scale at the monthly timestep
- variables are converted to monthly anomalies by subtracting the climatology
- standardized
  
### Missing GRACE data
- Missing data is handled in a few different ways:
    1. Infilled with climatology everywhere, including the nearly year-long gap from July 2017 - May 2018. 

### Basin-scale analysis:
- calculating the autocorrelation and cross-correlation at basin scale for lags up to 9 months
