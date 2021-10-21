
# do the imports
import seaborn as sns
import statistics

# load the dataset
tips = sns.load_dataset('data/tips')

# calculate the mean
print('mean of total_bill:', statistics.mean(tips['total_bill']))
print('mean of tip:', statistics.mean(tips['tip']))


# define ownMean
def average(x):
    return sum(x) / len(x)

print(average(tips['total_bill']))

# median
print('median of total_bill:', statistics.median(tips['total_bill']))
print('median of tip:', statistics.median(tips['tip']))

def median(x):
    """finds the median"""
    # get the length of variable
    n = len(x)

    # sort the variable
    x_sorted = sorted(x)

    # find the midpoint
    midpoint = n // 2

    if n % 2 == 1:
        # if odd, return the middle value
        return x_sorted[midpoint]
    else:
        # if even, return the average of the two middle values
        low_mid = midpoint - 1
        high_mid = midpoint
        return (x_sorted[low_mid] + x_sorted[high_mid]) / 2

# use the function
print(median(tips['total_bill']))
print(median(tips['tip']))



# mode
print('mode of total_bill:', statistics.mode(tips['total_bill']))
print('mode of tip:', statistics.mode(tips['tip']))

from collections import Counter

# own mode
def mode(x):
    """finds the most occuring value"""

    # Count each value occurence
    count_dict = Counter(x)

    # find the max value
    maximum = max(count_dict.values())

    # return the key with highest value
    return [k for k, v in count_dict.iteritems()
        if v == maximum]



def mode(x):
    """finds the most occuring value"""

    # empy dictionary
    counts = dict()

    for i in x:
        counts[i] = counts.get(i, 0) + 1
    return max(counts, key=counts.get)
    return counts
print(mode(tips['total_bill']))
print(mode(tips['tip']))