import matplotlib.pyplot as plt

y = norm.rvs(loc=42, scale=5, size=10000)

from scipy.stats import norm
import numpy as np
import seaborn as sns

#if you want to maintain reproducibility
np.random.seed(111)

# mean of zero and std. deviation of 2
population = norm.rvs(loc=42, scale=5, size=10000)

sns.distplot(population, color='#20c997', kde=True,
             hist_kws=dict(edgecolor="brown"))
plt.show()


from statistics import mean
from random import sample

means = []

for _i in range(100):
    m = mean(sample(sorted(population), 400))
    means.append(m)

sns.distplot(means, bins=25, color='#20c997', kde=True,
             hist_kws=dict(edgecolor="brown"))

# calculate the mean of the means
mn_of_mns = round(mean(means), 3)
plt.annotate(mn_of_mns, xy=(43, 0.9), color='#20c997')
plt.title('Distribution of sample means \n'
          '(sample size n = 400)')
plt.show()