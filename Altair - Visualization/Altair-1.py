# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 14:42:09 2021

@author: taufiqlibrary
"""

# Load an example dataset
from vega_datasets import data
cars = data.cars()

# plot the dataset, referencing dataframe column names
import altair as alt
alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin'
    ).interactive()