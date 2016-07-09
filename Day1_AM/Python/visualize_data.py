# -*- coding: utf-8 -*-
"""
First Python script

Visualize RPT data
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

time = np.array([1, 2, 4, 8, 24, 48])
mean = np.array([5.53, 7.58, 8.47, 8.44, 5.09, 1.86])
sdev = np.array([0.67, 0.98, 1.19, 0.7, 0.31, 0.31])

#plt.errorbar(time, mean, yerr=sdev, fmt='o')

outfile = '/home/qcpt/PBPK-workshop/Day1_AM/Model/one_cmpt_results.out'
df = pd.read_csv(outfile, sep='\t', skiprows=1)
plt.plot(df.Time, df.A1, 'b', label='A1')
plt.plot(df.Time, df.A2, 'k', label='A2')
plt.legend(loc='best')
