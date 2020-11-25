#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:43:29 2020

@author: whamitchell
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def cdf_plt(filename,x_limit, num_bins):
    channel_data = pd.read_csv(filename)
    # channel_data.head()

    data1 = np.array(channel_data.unstructured) # data need to be in np array format
    data2 = np.array(channel_data.structured)

    fig, ax = plt.subplots(figsize=(8, 4))
    n, bins, patches = ax.hist(data1, bins=np.linspace(0, x_limit, num_bins), density=True, histtype='step',
                            cumulative=True, label='Empirical', color ='b')
    n, bins, patches = ax.hist(data2, bins=np.linspace(0, x_limit, num_bins), density=True, histtype='step',
                            cumulative=True, label='Empirical', color ='r')
    plt.xlabel('Width')
    plt.ylabel('CDF')
    plt.savefig("CDF_figure", format='pdf')