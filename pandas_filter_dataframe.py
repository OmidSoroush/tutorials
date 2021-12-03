import pandas as pd

df = pd.read_csv("~/Downloads/customers.csv")

df.head()

filtered = df[(df["gender"] == "Female") & (df["country"] == "France")]

filtered.head()


filtered = df.loc[(df["gender"] == "Female") & (df["country"] == "France")]

filtered.head()


filtered = df.query('gender == "Male" & salary > 45000')

filtered.head()

df.query("country in ('France','Germany')", inplace=True)

values = ["Afghanistan", "Germany"]
filtered = df.loc[df['country'].isin(values)]


filtered = df[df['full_name'].str.startswith('P')]


filtered = df[df['full_name'].str.lower().str.endswith('k')]

filtered = df[df['full_name'].str.len() > 15]


filtered = df[df.apply(lambda x: x["country"] == 'Germany' and x["gender"] == 'Male', axis=1)]