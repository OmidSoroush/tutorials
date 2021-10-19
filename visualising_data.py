import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data/MOCK_DATA.csv")

pd.crosstab(index=data['country'], columns=data['gender'])

data['country'].value_counts()

from random import sample
gen = pd.Series(np.random.choice(["male", "female", "Non-binary"], 1000, replace=True))

data['gender2'] = gen

tab = pd.DataFrame(pd.crosstab(index=data['country'], columns='values'))

plt.bar(data['country'])


import matplotlib.pyplot as plt

# create the data
dict = {'Belgium': 65, 'Germany':498, 'Spain':437}
countries = list(dict.keys())
values = list(dict.values())

# determine the chart size
fig = plt.figure(figsize = (12, 6))

# create the bar chart
plt.bar(countries, values, color='#2dc997', width=0.4)

plt.xlabel('Country of origin')
plt.ylabel('Number of respondent')
plt.title('Number of people per country')
plt.show()