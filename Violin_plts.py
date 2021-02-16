#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 11:59:52 2021

@author: whamitchell
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='ticks', palette="deep", font_scale=1.1, rc={"figure.figsize": [8, 5]})
sns.set_context('talk') # paper or talk 

# Import data
data_chc1 = pd.read_excel('Compiled_dimensions.xlsx', sheet_name=0)
data_chc2 = pd.read_excel('Compiled_dimensions.xlsx', sheet_name=1)
data_chc7 = pd.read_excel('Compiled_dimensions.xlsx', sheet_name=2)
all_comp = pd.read_excel('Compiled_dimensions.xlsx', sheet_name=3)
JobeData = pd.read_csv('JobeData.csv')


columns = ['Width_m', 'Height_m', 'Aspect_Ratio']
col_labels = ["Width (m)", "Height (m)", "Aspect ratio"]
data = [data_chc1, data_chc2, data_chc7]

channel_labels = ['Channel One', 'Channel Two', 'Channel Seven']
for channel, name in zip(data, channel_labels):
    for col, title in zip(columns, titles):
        print(name, title)
        print(f"Mean: \n{channel.groupby('Channel')[col].mean()}")
        print("---------------")
        print(f"StDev: \n{channel.groupby('Channel')[col].std()}")
        print("---------------")
        print(f"Median: \n{channel.groupby('Channel')[col].median()}")
        print("---------------")
        print(f"Max: \n{channel.groupby('Channel')[col].max()}")
        print("---------------")
        print(f"Max: \n{channel.groupby('Channel')[col].min()}")        
        print("---------------")
        print("---------------")
        print("---------------")


# Histogram plot with kernel fitted
def distPlots(df, fname):
    copy = df.drop('Channel', axis=1)
    cols = copy.columns
    col_labels = ["Width (m)", "Height (m)", "Aspect ratio"]
    fig, ax = plt.subplots(1, 3, figsize=(17, 5))
    for var, label, subplot in zip(cols, col_labels, ax.flatten()):
        sns.histplot(x=var, hue="Channel", data=df, kde=True, bins=20, ax=subplot) # add hue='Structured' to include structure
        subplot.set_xlabel(label)
    plt.tight_layout()
    plt.show()
    plt.draw()
    fig.savefig(fname)    
    
distPlots(data_chc1, 'ChC1_distPlots.pdf')
distPlots(data_chc2, 'ChC2_distPlots.pdf')
distPlots(data_chc7, 'ChC7_distPlots.pdf')


def ECDPlots(df, fname):
    copy = df.drop('Channel', axis=1)
    cols = copy.columns
    col_labels = ["Width (m)", "Height (m)", "Aspect ratio"]
    fig, ax = plt.subplots(1, 3, figsize=(17, 5))
    for var, label, subplot in zip(cols, col_labels, ax.flatten()):
        sns.histplot(x=var, hue="Channel", data=df, kde=True, bins=20, 
                     cumulative=True, element="step", fill=False,
                     stat="density", common_norm=False, ax=subplot) 
        subplot.set_xlabel(label)
    plt.tight_layout()
    plt.show()
    plt.draw()
    fig.savefig(fname)    
    
ECDPlots(data_chc1, 'ChC1_EcdfPlots.pdf')
ECDPlots(data_chc2, 'ChC2_EcdfPlots.pdf')
ECDPlots(data_chc7, 'ChC7_EcdfPlots.pdf')


# Violin plot function
def violin_plt(df, filename):
    """
    df : dataframe
    filename : string for file export
    """
    copy = df.drop('Channel', axis=1)
    cols = copy.columns
    col_labels = ["Width (m)", "Height (m)", "Aspect ratio"]
    fig, ax = plt.subplots(1, 3, figsize=(17, 5))
    for var, label, subplot in zip(cols, col_labels, ax.flatten()):
        sns.violinplot(x='Channel', y=var, data=df, cut=0, ax=subplot, inner="stick") # add hue='Structured' to include structure
        subplot.set_xlabel('Channel Style')
        subplot.set_ylabel(label)
    plt.tight_layout()
    plt.show()
    plt.draw()
    fig.savefig(filename)


violin_plt(data_chc1, 'ChC1_ViolinPlts.pdf')
violin_plt(data_chc2, 'ChC2_ViolinPlts.pdf')
violin_plt(data_chc7, 'ChC7_ViolinPlts.pdf')
violin_plt(all_comp, 'ChC_Maturation.pdf')

v_plt(data, 'Comp_ChC')
violin_plt(JobeData, 'ChC_Jobe.pdf')
