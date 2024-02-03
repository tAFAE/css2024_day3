# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:31:02 2024

@author: ptmab
"""

import numpy as np
import matplotlib.pyplot as plt
data=np.loadtxt("noisydata.csv", skiprows=1, delimiter=",")
data_avg=np.mean(data,1)
print("average of columns:")
print(data_avg[1])
pressure=data[:,0]
flowrate=data[:,1]
#the value at the end of the upcoming line determines whether u get a straight line or polynomial fit
#This is done for fitting 
fit =np.polyfit(pressure, flowrate,2)
flowfit=np.polyval(fit,pressure)
plt.plot(pressure,flowrate,"go")
plt.plot(pressure,flowrate,"k-")
plt.xlabel("pressure (Pa)")
plt.ylabel("flow rate ($m3/s$)")
plt.show()