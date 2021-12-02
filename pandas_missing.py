import pandas as pd
import numpy as np

columns = ["first_name", "last_name", "gender", "language", "age", "salary"]

data = [("Krishna", "Popplestone", "Non-binary", "German", 30, 52000),
        ("Wilbert", "Gavaran", "Male", "Thai", 70, 43000),
        ("Anthe", np.nan, "Male", "Persian", np.nan, 89000),
        ("Filbert",	"Roebuck", "Male", "Maltese", 20, 35000),
        ("Lisetta",	np.nan, "Non-binary", "English", 55, np.nan),
        ("Shellie",	"Blackston", "Female", "Maltese", np.nan, 44000),
        ("Tani", "Clayton",	 "Female", "English", 42, 37000),
        ("Fern", "Beckerleg", "Non-binary", "Thai", np.nan, np.nan),
        ("Garth", np.nan, "Female", "German", 29, 25000)]

df = pd.DataFrame(data, columns=columns)
print(df)

df.isnull()
df.isna()

df.notna()
df.notnull()

df.isnull().any()
df.isnull().sum()

df.dropna(subset=['age', 'salary'])

df.dropna(how="all")

df1 = df.dropna(axis="columns", thresh=2)

df.dropna(thresh=2)

# Using median
df['salary'].fillna(df['salary'].median(), inplace=True)

# Using mean
df['salary'].fillna(int(df['salary'].mean()), inplace=True)

# Using mode
df['salary'].fillna(int(df['salary'].mode()), inplace=True)

df.fillna(0, inplace=True)

df.replace(to_replace = np.nan, value =-99, inplace=True)


df['salary'].fillna(method='ffill', inplace=True)

df['salary'].fillna(method='bfill', inplace=True)


df['salary'].interpolate(method='linear')
