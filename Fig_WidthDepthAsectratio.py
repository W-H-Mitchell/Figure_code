import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

channel_data = pd.read_csv('ChannelDimensions.csv')
channel_data.head()

# downstream distance (x axis)
dist = channel_data.Distance_km
# element scale
elem_width = channel_data.Width
elem_height = channel_data.Height
elem_asp = channel_data.AspectRatio
# complex scale
c_width = channel_data.C_Width
c_height = channel_data.C_Height
c_asp = channel_data.C_AspectRatio
# seafloor channel
sea_width = channel_data.Sea_Width
sea_height = channel_data.Sea_Height
sea_asp = channel_data.Sea_AspectRatio

# Creating stacked plots for width, depth and aspect ratio
fig = plt.figure(figsize=(8.0, 10.0))
axes1 = fig.add_subplot(3, 1, 1)
axes2 = fig.add_subplot(3, 1, 2)
axes3 = fig.add_subplot(3, 1, 3)
# width plot
axes1.set_ylabel('Width (m)')
axes1.plot(dist, elem_width, linestyle='solid',color='b', marker='s', markersize=4, linewidth=1) # square marker for channel elements
axes1.plot(dist, c_width, linestyle='solid', color='k', marker='o', markersize=4, linewidth=1) # circle marker for complex scale
axes1.plot(dist, sea_width, linestyle='solid', color='r', marker='D', markersize=4, linewidth=1) # diamond marker for seafloor channels
# depth plot 
axes2.set_ylabel('Thickness or Depth (m)')
axes2.plot(dist, elem_height,linestyle='solid',color='b', marker='s', markersize=4, linewidth=1) # square marker for channel elements
axes2.plot(dist, c_height, linestyle='solid', color='k', marker='o', markersize=4, linewidth=1) # circle marker for complex scale
axes2.plot(dist, sea_height, linestyle='solid', color='r', marker='D', markersize=4, linewidth=1) # diamond marker for seafloor channels
# aspect plot
axes3.set_ylabel('Thickness or Depth (m)')
axes3.set_xlabel('Downstream Distance (km)')
axes3.plot(dist, elem_asp,linestyle='solid',color='b', marker='s', markersize=4, linewidth=1) # square marker for channel elements
axes3.plot(dist, c_asp, linestyle='solid', color='k', marker='o', markersize=4, linewidth=1) # circle marker for complex scale
axes3.plot(dist, sea_asp, linestyle='solid', color='r', marker='D', markersize=4, linewidth=1) # diamond marker for seafloor channels

fig.tight_layout()
plt.savefig("Width_Depth_AspectRatio.pdf", format='pdf')