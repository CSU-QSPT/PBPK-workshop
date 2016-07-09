# -*- coding: utf-8 -*-
"""
First Python script

Visualize RPT data
"""

import numpy as np
import matplotlib.pyplot as plt

time = np.array([1, 2, 4, 8, 24, 48])
mean = np.array([5.53, 7.58, 8.47, 8.44, 5.09, 1.86])
sdev = np.array([0.67, 0.98, 1.19, 0.7, 0.31, 0.31])

plt.errorbar(time, mean, yerr=sdev, fmt='o')