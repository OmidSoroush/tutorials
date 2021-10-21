import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel("data/customer.xlsx")
gen = pd.Series(np.random.choice(["male", "female", "Non-binary"], 1000, replace=True))
data['gender'] = gen
print(data.head())
pd.crosstab(index=data['country'], columns=data['gender'])
data['country'].value_counts()
tab = pd.DataFrame(pd.crosstab(index=data['country'], columns='values'))

# generate random integer values
from numpy.random import seed
from numpy.random import randint
# seed random number generator
seed(1)
# generate some integers
values = randint(20, 150, 1000)

data['purchase'] = values

plt.hist(data['purchase'], bins=[0,10,20,30,40,70,80,90,99], color='#2dc997')
plt.title('Histogram of Purchase')
plt.show()



# pie chart
dict = {'Belgium': 65, 'Germany':498, 'Spain':437}
countries = list(dict.keys())
values = list(dict.values())

# determine the chart size
fig = plt.figure(figsize = (10, 5))

# create the pie chart
plt.pie(values, labels=countries, autopct='%.2f')
plt.show()


import seaborn as sns

sns.set_style("whitegrid")

ax = sns.histplot(
    data,
    x='country',
    hue='gender',
    multiple='stack',
    palette=['#24b1d1', '#ae24d1', '#2dc997'],
    # Add white borders to the bars.
    edgecolor='white',
    # Shrink the bars a bit so they don't touch.
    shrink=0.5
)

ax.set_title('People by country and gender')
# Remove 'Count' ylabel.
ax.set_ylabel(None)


twoway = pd.crosstab(index=data['country'], columns=data['gender'])

twoway.plot(kind='bar', stacked=True, figsize=(8, 4), grid=False)
# Just add a title and rotate the x-axis labels to be horizontal.
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.title('People by country and gender')
plt.xticks(rotation=0, ha='center')







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


import seaborn as sns
tips = sns.load_dataset('tips')
fig = plt.figure(figsize = (10, 4))
ax = plt.subplot(111)
ax.scatter(tips['total_bill'], tips['tip'], color='#2dc997')

# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.xlabel('total bill')
plt.ylabel('tip')

plt.show()

list = ['x', 'y', 3]

for i in list:
    try:
        m = 'a' * i
        break
    except Exception as e:
        print('you are dealing with', e.__class__)
        print('next element')
        print()

print('great! the result is', m)


num = int(input("Enter a number greater than 5:"))
    if num <= 5:
        raise Exception("The number you entered is not greater than 5")