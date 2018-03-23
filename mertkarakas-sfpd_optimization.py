# -*- coding: utf-8 -*-
"""
Capital One Challenge: Can you optimize and predict emergency calls?

Mert Karakas
UVA 2020
"""
import pandas as pd
import numpy as np


data = pd.read_csv('sfpd_dispatch_data_subset.csv') # read in .csv into a pd.Dataframe
schema = pd.read_csv('sfpd_dispatch_schema.csv') # read in .csv into a pd.Dataframe

# 1. Data Visuals: Display or graph 3 metrics or trends from the data set that are interesting to you.


# 2. Given an address and time, what is the most likely dispatch to be required?
ut = pd.concat([data['unit_type'], data['']

# 3. Which areas take the longest time to dispatch to on average? How can this be reduced?