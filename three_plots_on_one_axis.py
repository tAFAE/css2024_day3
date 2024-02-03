# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:54:51 2024

@author: ptmab
"""

import pandas as pd
import matplotlib.pyplot as plt
df =pd.read_csv("C:/Users/ptmab/css2024_day3/poker_2016_09_27.csv", names=["Time", "NUN", "x", "y", "z"])
df["Time"]=pd.to_datetime(df["Time"]), format="%H-%M-%S").dt.time
#plt.plot(df["Time"], df["x"], label="x")
#plt.plot(df["Time"], df["y"], label="y")
#plt.plot(df["Time"], df["z"], label="z")

#plt.plot(df["Time"], df["x"], df["y"], df["z"])
plt.plot(df["Time"], y=["x","y","z")
                        