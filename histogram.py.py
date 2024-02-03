# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:37:58 2024

@author: ptmab
"""


import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv("C:/Users/ptmab/css2024_day2/data_02/time_series_data.csv", index_col=0)
print(df.info())
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%M-%D")
print(df.info())

plt.plot(df["Date"], df["Temperature"])
plt.ylabel("Temperature")
plt.show()

df["Temperature"].plot(kind="hist", bins=20)
title = ("Temperature")
plt.show()