# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:33:46 2024

@author: ptmab
"""

import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv("C:/Users/ptmab/css2024_day2/data_02/iris.csv")
file["class"]= file["class"].str.replace("Iris-","")