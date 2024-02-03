# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:24:14 2024

@author: ptmab
"""
import plotly.express as px
react_conv = [0.5, 0.6, 0.7, 0.7, 0.9]
temp = [180, 200, 220, 240, 260]
fig = px.line(x =temp, y = react_conv)
fig.write_html("plot.html")

#This is used to automatically open the browser of your plot
import webbrowser
webbrowser.open("plot.html")