# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 14:59:19 2021

@author: taufiqlibrary
"""

# load an example dataset
from vega_datasets import data
cars = data.cars()

# plot the dataset, referencing dataframe column names
import altair as alt
alt.Chart(cars).mark_bar().encode(
    x='mean(Miles_per_Gallon)',
    y='Origin',
    color='Origin'
    )