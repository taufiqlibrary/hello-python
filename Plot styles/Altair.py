# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 14:33:38 2021

@author: taufiqlibrary
"""

import altair as alt
from vega_datasets import data
cars = data.cars()

alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
    ).interactive()