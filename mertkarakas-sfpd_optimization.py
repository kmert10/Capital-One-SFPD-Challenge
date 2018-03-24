# -*- coding: utf-8 -*-
"""
Capital One Challenge: Can you optimize and predict emergency calls?

Mert Karakas
UVA 2020
"""

import pandas as pd
import numpy as np
from  matplotlib import pyplot
import seaborn
import plotly.plotly as py
import plotly.graph_objs as go
seaborn.set(style='ticks')


data = pd.read_csv('sfpd_dispatch_data_subset.csv') # read in .csv into a pd.Dataframe
schema = pd.read_csv('sfpd_dispatch_schema.csv') # read in .csv into a pd.Dataframe

# 1. Data Visuals: Display or graph 3 metrics or trends from the data set that are interesting to you.


# 2. Given an address and time, what is the most likely dispatch to be required?
hours = []
for time in range(len(data['dispatch_timestamp'])):
    hours.append(int(data['dispatch_timestamp'].loc[time].split()[1].split(':')[0]))
hour = pd.Series(hours)
d = {'Time (Hour)':hour, 'Zip Codes':data['zipcode_of_incident'], 'unit_type':data['unit_type']}
ut = pd.DataFrame(data=d)
units = np.unique(ut['unit_type'])
fg = seaborn.FacetGrid(data=ut[0:5000], hue='unit_type', hue_order=units,size=10, aspect=1.61)
fg.map(pyplot.scatter, 'Time (Hour)', 'Zip Codes').add_legend()

days = []
for time in range(len(data['call_date'])):
    days.append(int(data['call_date'].loc[time].split('-')[2]))
day = pd.Series(days)

d = {'Days in January':day, 'Zip Codes':data['zipcode_of_incident'], 'unit_type':data['unit_type']}
ut = pd.DataFrame(data=d)
x = np.linspace(1, 10, len(ut['Zip Codes']))
dt = [
    go.Bar(
        x=ut['Zip Codes'], # assign x as the dataframe column 'x'
        y=ut['unit_type']
    ),
    go.Bar(
        x=ut['Zip Codes'], # assign x as the dataframe column 'x',
        y=ut['unit_type']
    ),
    go.Bar(
        x=ut['Zip Codes'], # assign x as the dataframe column 'x',
        y=ut['unit_type']
    ),
    go.Bar(
        x=ut['Zip Codes'], # assign x as the dataframe column 'x',
        y=ut['unit_type']
    )
]
layout = go.Layout(
    barmode='stack',
    title='Stacked Bar with Pandas'
)

fig = go.Figure(data=dt, layout=layout)

iris = seaborn.load_dataset('sfpd_dispatch_data_subset.csv')
g = seaborn.PairGrid(iris)
g.map(pyplot.scatter);
# 3. Which areas take the longest time to dispatch to on average? How can this be reduced?