# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:11:49 2024

@author: ptmab
"""
#Check the rest of this code on the recordings
import pandas as pd
from ydata_profiling import ProfileReport
#use absolute path if the file is not from the same directory and relative path if they are form the same directory or folder.
df =pd.read_csv("absolute path")
profile = ProfileReport(df, title="Profiling Report")
profile.to_file("your_report.html")
