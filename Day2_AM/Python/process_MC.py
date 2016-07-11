# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 14:06:44 2016

@author: qcpt
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fpath = '/home/qcpt/PBPK-workshop/Day2_AM/Model/four_cmpt_MC.out'
df = pd.read_csv(fpath, sep='\t')
tfinal = 24
tstep = 0.1
ind_initial = 1
ind_final = int(tfinal/tstep + 1)
markers = ['CBL_mgL', 'CH_mgL']
blood_df = df.ix[:, 'CBL_mgL_1.{0}'.format(ind_initial):'CBL_mgL_1.{0}'.format(ind_final)]

p_interval= blood_df.quantile(q=[0.025, 0.5, 0.975], axis=0)
time = np.arange(0, tfinal+tstep, tstep)

plt.plot(time, p_interval.ix[0.025, :], 'b--')
plt.plot(time, p_interval.ix[0.500, :], 'k')
plt.plot(time, p_interval.ix[0.975, :], 'g--')

