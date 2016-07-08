import pandas as pd
import matplotlib.pyplot as plt

fpath = './'
dep_var = '' # Dependent variable
indep_var = '' # Independent variable

df = pd.read_csv(fpath, sep='\t')
plt.plot(df.ix[:,indep_var], df.ix[:, dep_var])
plt.show()
