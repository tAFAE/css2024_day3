# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:41:34 2024

@author: ptmab
"""

import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv("C:/Users/ptmab/css2024_day2/data_02/time_series_data.csv")
file["class"]= file["class"].str.replace("Iris-","")
#plt.scatter(file["sepal_length"], file["sepal_width"])
#plt.xlabel("sepal_length (cm)")
#plt.ylabel("sepal_width (cm)")
#plt.title("Species with their sepal length")
#plt.show()

#import seaborn as sns
#sns.pairplot(file,hue="class")
#plt.show()

class_count = file["class"].value_counts()
plt.pie(class_count, labels= class_count.index)
plt.show