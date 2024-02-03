# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:08:38 2024

@author: ptmab
"""
import numpy as np

#conventional python - for loop
for i in range(1,11):
    print (i)
#This only works for intergers so to do decimales you need to do this
#numpy-range
for i in np.range(1, 11, 0.5):
    print(i)

#let us square the numbers from 1 to 5
squares=[]
for i in range(1,6):
    squares.append(i**2)
print(squares)

squares = np.arange(1,6)**2
print(squares)

import matplotlib.pyplot as plt
x = np.arange (1.6)
y = x**2
print("shape of x:")
print(x.shape)
print("shape of y:")
print(y.shape)
print(x+y)
print(x*y)
print("calculating dot product")
print(x.dot(y))
print("calculating cross product")
print(np.matmul(x,y))
plt.plot(x,y,"r*")
plt.show()
#You can use python and numpy to have the same effect as Mathlab
alist = [1,2,5,6,15,22]
data = np.array(alist)
print(data)
