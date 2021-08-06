# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 09:50:25 2021

@author: taufiqlibrary
"""

#import matplotlib.pyplot as plt
#import numpy as np
#import seaborn as sns

# Generate some random data
#num_points = 20
# x will be 5, 6, 7 ... but also twiddled randomly
#x = 5 + np.arange(num_points) + np.random.randn(num_points)
# y will be 10, 11, 12 ... but twiddled even more randomly
#y = 10 + np.arange(num_points) + 5 * np.random.randn(num_points)
#sns.regplot(x, y)
#plt.show()

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(color_codes=True)
tips = sns.load_dataset("tips")

sns.regplot(x="total_bill", y="tip", data=tips);

#import seaborn as sns
#df = sns.load_dataset("penguins")
#sns.pairplot(df, hue="species")

#import numpy as np
#import seaborn as sns
#%matplotlib inline
#import matplotlib.pyplot as plt

#import seaborn as sns
#df = sns.load_dataset("penguins")
#sns.pairplot(df, hue="species")