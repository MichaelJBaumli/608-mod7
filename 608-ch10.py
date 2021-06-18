#Program Name: 608-ch10.py
#Assignment Module 7
#Class 44680 Block 44599 Section 01
#Michael Baumli
#Date: 20210617

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

c = 5/9 *(f-32)
c = lambda f:5/9*(f-32)
temps = [(f,c(f)) for f in range(0,101,10)]

temps_df = pd.Dataframe(temps, columns=['Fahrenheit', 'Celsius'])

axes = temps_df.plot(x='Fahrenheit',y='Celsius', style='.-')

y_label = axes.set_ylabel('Celsius')

plt.show()