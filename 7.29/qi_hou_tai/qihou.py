import numpy as np    
import pandas as pd    
import matplotlib.pyplot as plt  
import os  
import cartopy.crs as ccrs  
import cartopy.feature as cfeature  
import matplotlib.ticker as mticker  
from matplotlib.ticker import MultipleLocator, FuncFormatter
import xarray as xr  

df = xr.open_dataset(r'G:\data\2000\cmems_mod_glo_bgc_my_0.25deg_P1M-m_1721905744350.nc')
df = df.sel(depth=2000, method = 'nearest')
# df = df.sel(time=df['time.season'] == 'MAM') # 季节选取
df = df.mean(dim='time') # 季节平均
print(df)
