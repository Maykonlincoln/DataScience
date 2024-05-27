import pandas as pd


notas = pd.read_csv('ratings.csv')
notas

import matplotlib as plt

notas["nota"].plot()
plt.show()


notas["nota"].plot(kind='hist')
plt.show()
