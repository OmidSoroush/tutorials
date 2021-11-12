def pmf(x,p):
    f = p**x*(1-p)**(1-x)
    return f

print(pmf(0, 0.8))

from scipy.stats import bernoulli
print(bernoulli.pmf(0, 0.8))



from scipy.stats import binom

n = 40
p = 0.8

r = list(range(n + 1))
dist = binom.pmf(r, n, p)

import matplotlib.pyplot as plt

plt.bar(r, dist, width=0.9, color='#20c997')
plt.title('Binomial Distribution')
plt.show()


from scipy.stats import binom
import seaborn as sns
sns.distplot(binom.rvs(n=10,p=0.5,size=1000, random_state=111),
             hist=True, kde=False, color='#20c997')


