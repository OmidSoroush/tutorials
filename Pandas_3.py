pd.set_option('display.max_colwidth', None)

import pandas as pd
df = pd.read_csv("~/Downloads/employees.csv")

mean_age = df.age.mean()

df["dist_mean"] = df.age.map(lambda x: x - mean_age)


def remean_points(row):
    return row.upper()

df.apply(lambda x:x.upper())

df.apply(lambda x : x + 10)



df[["age", "dist_mean"]].head()

df.info()

df.shape

df.first_name.describe()

df = pd.read_csv("~/Downloads/employees.csv", usecols=["first_name", "last_name"])

# set the first row as column names
df = pd.read_csv("~/Downloads/employees.csv", header=1)

# skip the first 3 rows
df = pd.read_csv("~/Downloads/employees.csv", skiprows=3)


import pandas as pd

df = pd.read_excel("~/Downloads/employees.xlsx")

df.head()

import pandas as pd

df = pd.read_json("~/Downloads/employees.json")

df.head()

df.to_csv("~/Downloads/data.csv")
df.to_excel("~/Downloads/data.xlsx")



import pandas as pd
df = pd.read_csv("~/Downloads/employees.csv")

df = df.iloc[:,[1,2]]
df["age"].apply(lambda x : x + 10)
df.apply(lambda x: x.str.upper())


data = [(44, 34, 45),
         (455, 23, 54),
         (775, 34, 25),
         (454, 32, 22),
         (566, 23, 23)]

df = pd.DataFrame(data, columns=list('ABC'))

def double(x):
    return x * 2

df["A"] = df["A"].apply(double)

df[["A", "B"]] = df[["A", "B"]].apply(double)

df = df.apply(double, axis=0)

# One column, lambda function
df["A"] = df["A"].apply(lambda x : x * 2)

# Two columns, lambda function
df[["A", "B"]] = df[["A", "B"]].apply(lambda x : x * 2)

# Entire DataFrame, lambda function
import numpy as np
df = df.apply(sum, axis=0)

df["A"].name


data = [(44, 34, 45),
         (455, 23, 54),
         (775, 34, 25),
         (454, 32, 22),
         (566, 23, 23)]

df = pd.DataFrame(data, columns=list('ABC'))

df = df.apply(lambda x: np.mean(x) if x.name in ['A','B'] else x)



import seaborn as sns

titanic = sns.load_dataset("titanic")

titanic.head()

titanic.survived.duplicated()

titanic.duplicated()

titanic.duplicated(subset=['survived', 'age', 'alive'])


titanic.survived.duplicated().sum()

(~titanic.duplicated()).sum()

titanic.duplicated(subset=['survived', 'age', 'pclass']).sum()


titanic.loc[titanic.duplicated(), :]

titanic.drop_duplicates(inplace=True)

titanic.drop_duplicates(subset=['survived', 'age', 'pclass'])

titanic.duplicated(subset=['survived', 'age', 'pclass'])