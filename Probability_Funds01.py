# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:05:30 2022

@author: Aaron
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

#Produce Normal Distribution w/ Mean and STDEV
mu,sigma = 75,10 
randValue = np.random.default_rng()
norm = randValue.normal(mu,sigma,100)

# Probability Density Function
plt.hist(norm)



# Convert to Standard Distribution Z-Score value
# Z = xi-mu/stdev
zscore = (norm - mu)/sigma
plt.hist(zscore)

#Cumulative Density Function
#print(zscore)
display(scipy.stats.norm.sf(abs(zscore)))
display(scipy.stats.norm.sf(abs(zscore))[1])






zscore = (60 - mu)/sigma



