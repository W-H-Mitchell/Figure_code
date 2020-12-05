import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Niger_ChSev.csv')
data1 = pd.read_csv('Niger_ChOne.csv')

# Fig1
# Sinuosity and curvature plot against downstream distance.
dist = data.downstream_distance_km # downstream distance (x axis)
sin = data.sinuosity # sinuosity and curvature (y axis)
data['curvature'] = data.max_curv.map(lambda c:(c**2)**(1/2)) # map a new column with positive curvature
curv = data.curvature

# creating a figure with two y axis for sinuosity and curvature
fig1 = plt.figure(figsize=(10.0, 5.0))
fig1, ax1 = plt.subplots()

# sinuosity plot
ax1.set_xlabel('Downstream Distance (km)')
ax1.set_ylabel('Sinuosity', color='k')
ax1.plot(dist, sin, linestyle='solid', color='k', marker='o', markersize=4, linewidth=1)
ax1.tick_params(axis='y', labelcolor='k')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

# curvature plot
ax2.set_ylabel('Curvature', color= 'b')  # we already handled the x-label with ax1
ax2.plot(dist, curv, linestyle='solid', color='b', marker='d', markersize=4, linewidth=1)
ax2.tick_params(axis='y', labelcolor= 'b')

fig1.tight_layout()  # otherwise the right y-label is slightly clipped
fig1.savefig("ChSev_Sin_Curvature.pdf", format='pdf')



# Fig 2
# Scatter plot of sinuosity curvature for multiple channel systems
df = pd.concat([data, data1], ignore_index='True') # concatenate data from channels
df['curvature'] = df.max_curv.map(lambda c:(c**2)**(1/2)) # map a new column with positive curvature

# Check for missing values
missing_values = df.isnull().sum() 
total_cells = np.product(df.shape) 
percent_missing = (missing_values/total_cells) * 100 # percent of data that is missing
print(percent_missing)
df = df.dropna() # drop missing values

# Added step; remove anomalously high curvature
anomalous_curv = df.loc[df.curvature >= 0.02] 
df = df.drop(df[df.curvature >= 0.02].index)
# df.to_csv(r'/Users/whamitchell/Documents/python/channel_sinuosities/ChC_sin_curv.csv', index = False)
df_sin = df.sinuosity
df_curv = df.curvature 


# split df into unstructured and structured data
structured_data = df.loc[df.structured != False]
unstructured_data = df.loc[df.structured == False]
structured_sinuosity = structured_data.sinuosity
structured_curvature = structured_data.curvature 
unstructured_sinuosity = unstructured_data.sinuosity
unstructured_curvature = unstructured_data.curvature 

# Plots
fig2 = plt.figure(figsize=(12.0, 5.0))
axes1 = fig2.add_subplot(1, 2, 1)
axes2 = fig2.add_subplot(1, 2, 2)

axes1.set_xlabel("Curvature")
axes1.set_ylabel("Sinuosity")
axes1.plot(df_curv, df_sin, c = 'k', marker = '.', linewidth=0)
# calculate the trendline 
m, b = np.polyfit(df_curv, df_sin, 1)
axes1.plot(df_curv, m*df_curv + b, c='r', linewidth=0.5)

axes2.set_xlabel("Curvature")
axes2.set_ylabel("Sinuosity")
axes2.plot(structured_curvature, structured_sinuosity, c = 'tab:red', marker = 'x', linewidth=0)
axes2.plot(unstructured_curvature, unstructured_sinuosity, c = 'tab:blue', marker = '.', markersize=6, linewidth=0)
# calculate the trendline 
m, b = np.polyfit(unstructured_curvature, unstructured_sinuosity, 1)
axes2.plot(unstructured_curvature, m*unstructured_curvature + b, c='r', linewidth=0.5)

fig2.savefig("Sin_Curvature.pdf", format='pdf')