#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 11:59:52 2021

@author: whamitchell
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='white', palette="deep", font_scale=1.1, rc={"figure.figsize": [8, 5]})
sns.set_context('talk') # paper or talk 

# Import data
data_chc1 = pd.read_excel('Compiled_dimensions.xlsx', sheet_name=0)
data_chc7 = pd.read_excel('Compiled_dimensions.xlsx', sheet_name=1)
JobeData = pd.read_csv('JobeData.csv')
data_chc1['Width_m'].mean()

columns = ['Width_m', 'Height_m', 'Aspect_Ratio']
# For channel 1
def violin_plt(df, filename):
    """
    df : dataframe
    filename : string
    fileexport name

    """
    fig, ax = plt.subplots(1, 3, figsize=(20, 7))
    for var, subplot in zip(columns, ax.flatten()):
        sns.violinplot(x='Channel', y=var, data=df, ax=subplot)
    plt.show()
    plt.draw()
    fig.savefig(filename)
    
violin_plt(data_chc1, 'ChC1_ViolinPlts.pdf')
violin_plt(data_chc7, 'ChC7_ViolinPlts.pdf')

