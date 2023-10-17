#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 13:44:45 2023

@author: wanders7

Code to read in individual water level files and create a pandas dataframe

"""
import numpy as np
import pandas as pd
import os


wlDF= pd.DataFrame(columns=['date','height[m]','error[m]','dataset',
    'ID','name','location','continent','country','longitude','latitude'])

path = '/Users/wanders7/Documents/Code/Project/TWS_S2S/water_level_data/water_level_individual'
files = os.listdir(path)
for file in files:
    df = pd.read_table(path+'/'+file,sep=' ',skiprows=17,names=['date','height[m]','error[m]','dataset'])
    metadata = pd.read_table(path+'/'+file,sep=':',nrows=8,names=['field','value'])
    dID = int(metadata.value[0].strip())
    name = metadata.value[1].lstrip()
    loc =  metadata.value[2].lstrip()
    cont =  metadata.value[3].lstrip()
    country = metadata.value[4].lstrip()
    lon = float(metadata.value[5].strip())
    lat = float(metadata.value[6].strip())
    
    data = pd.DataFrame(data={'date':df['date'].values,'height[m]':df['height[m]'].values,
                      'error[m]':df['error[m]'].values,'dataset':df['dataset'].values,
                    'ID':np.repeat(dID,df.shape[0]),'name':np.repeat(name,df.shape[0]),'location':np.repeat(loc,df.shape[0]),
                    'continent':np.repeat(cont,df.shape[0]),'country':np.repeat(country,df.shape[0]),
                    'longitude':np.repeat(lon,df.shape[0]),'latitude':np.repeat(lat,df.shape[0])})
    wlDF = pd.concat([wlDF,data])

wlDF.to_csv('/Users/wanders7/Documents/Code/Project/TWS_S2S/water_level_data/water_level_df/water_level.csv')

