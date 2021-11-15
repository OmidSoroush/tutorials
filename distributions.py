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



from scipy.stats import binom
print(1-binom.cdf(k=10, n=20, p=0.5))
print(binom.sf(k=10, n=20, p=0.5))
import matplotlib.pyplot as plt
import numpy as np

# creating a array of values between 0 and 20
k = np.arange(0, 20, 0.1)

y = binom.cdf(k=k, n=20, p=0.5)

plt.plot(x, y)
plt.title('Binomial CDF')
plt.show()

from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np

# creating a array of probability from 0 to 1
q = np.arange(0, 1, 0.01)

y = binom.ppf(q=q, n=30, p=0.5)

plt.plot(q, y)
plt.title('Cumulative Probability')
plt.show()
n = 20
p = 0.6

EV = n*p
Var = (n*p) * (1-p)

print('The expected value is:', EV)
print('The variance is:', Var)

from scipy.stats import uniform
import matplotlib.pyplot as plt
import numpy as np

# if you want to maintain reproducibility
np.random.seed(111)


# generate uniformly distributed random numbers
y = uniform.rvs(loc=3, scale=9, size=100000)

plt.hist(y, edgecolor='brown', color='#20c997', bins=26)
plt.title('Random Uniform Distribution')
plt.xlabel('Uniform Values')
plt.ylabel('Frequency')
plt.show()

from scipy.stats import uniform
import matplotlib.pyplot as plt
import numpy as np

# creating a array of values
x = np.arange(-2, 12, 0.1)

y = uniform.pdf(x=x, loc=2, scale=6)

plt.plot(x, y, color='#20c997')
plt.title('Uniform (PDF)')
plt.xlabel('Uniform values')
plt.ylabel('Probabilities')
plt.show()

from scipy.stats import uniform
import matplotlib.pyplot as plt
import numpy as np

# creating a array of values
x = np.arange(-2, 12, 0.1)

y = uniform.cdf(x=x, loc=2, scale=6)

plt.plot(x, y, color='#20c997')
plt.title('Uniform (CDF)')
plt.xlabel('Uniform values')
plt.ylabel('Probabilities')
plt.show()




from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#if you want to maintain reproducibility
np.random.seed(111)

# create random variable with 100000 normally distributed values
# mean of zero and std. deviation of 1
x = norm.rvs(0, 1, 100000)
# mean of zero and std. deviation of 2
y = norm.rvs(0, 2, 100000)

sns.distplot(x, color='#20c997', hist=False, kde=True)
sns.distplot(y, color='brown', hist=False, kde=True)
plt.annotate('-- μ = 0, σ =1', xy=(6, 0.35), color='#20c997')
plt.annotate('-- μ = 0, σ =2', xy=(6, 0.30), color='brown')
plt.show()

from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# creating an array of values
x = np.arange(-5, 5, 0.1)

y = norm.pdf(x, 0, 1)

plt.plot(x, y, color='#20c997')
plt.title('Normal Distribution (PDF)')
plt.xlabel('Values')
plt.ylabel('Probabilities')
plt.show()


from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# creating an array of values
x = np.arange(-5, 5, 0.1)

y = norm.cdf(x, 0, 1)

plt.plot(x, y, color='#20c997')
plt.title('Normal Distribution (CDF)')
plt.xlabel('Values')
plt.ylabel('Probabilities')
plt.show()

from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# creating an array of probabilities
x = np.arange(0, 1, 0.01)

y = norm.ppf(x, 0, 1)

plt.plot(x, y, color='#20c997')
plt.title('Normal Distribution (ppf)')
plt.xlabel('Probabilities')
plt.ylabel('Values')
plt.show()