# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 14:12:27 2016

@author: qcpt
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fpath = '/home/qcpt/PBPK-workshop/Day2_PM/Model/rpt_mc_human_600.simdat'
df = pd.read_csv(fpath, sep='\t')

marker = ['CPL_R_mgL', 'CPL_D_mgL']
fig, ax = plt.subplots(1,2, figsize=(8,6))
time = np.arange(0, 72+0.25, 0.25)
for i,m in enumerate(marker):
    template = '%s_1.%s'
    temp_df = df.ix[:, template%(m,1):template%(m,289)]
    quant = temp_df.quantile([0.025, 0.5, 0.975], axis=0)
    ax[i].plot(time, quant.ix[0.025,:], 'k--')
    ax[i].plot(time, quant.ix[0.500,:], 'k-')
    ax[i].plot(time, quant.ix[0.975,:], 'k--')

ax[1].set_xlabel('Time [hrs]', fontsize=16)
ax[0].set_ylabel('Plasma RPT Concentration (mg/L)', fontsize=16)
ax[1].set_ylabel('Plasma dRPR Concentration (mg/L)', fontsize=16)
ax[0].errorbar([0,2,4,6,8,10,12,18,24, 48, 72],
                [0,7.52E+00, 1.13E+01, 1.18E+01, 1.18E+01, 1.05E+01, 1.00E+01, 6.80E+00, 6.02E+00, 2.28E+00, 1.12E+00],
                yerr=[0.01, 1.21, 1.1, 1.3, 1.1, 0.84, 1.75, 0.93, 1.17, 0.58, 0.343], fmt='o')
ax[1].errorbar([0,2,4,6,8,10,12,18,24,48,72],
                [0,1.64E+00, 2.85E+00, 4.16E+00, 5.21E+00, 5.42E+00, 5.69E+00, 5.83E+00, 5.42E+00, 2.34E+00, 1.41E+00],
                yerr=[0.01, 0.1, 0.58, 1.04, 0.97, 0.81, 0.98, 1.24, 0.98, 0.55, 0.484], fmt='o'
                )
plt.tight_layout()