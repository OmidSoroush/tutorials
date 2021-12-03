import pandas as pd

df = pd.read_csv("~/Downloads/customers.csv")

grouped = df.groupby("country")

for name, records in grouped:
    print(name)
    print(records)

grouped.groups.keys()

group.first()


df.groupby("country")["weight"].count()
# or
df.groupby(["country", "gender"])["weight"].count()





df.groupby(['country', 'gender']).agg(
    {
         'weight': ["mean", "min", "sum"],    # Sum weight per group
         'height': ["max", "count"],  # max height per group
         'salary': ["median", "nunique"]  # median salary per group
    }
)

df.groupby(['country', 'gender']).agg(

    mean_weight=("weight", min),

    max_height=("height", max),

    mean_salary=("salary", lambda x: x.mean())
)


df.groupby('country').agg(
    max_weight=pd.NamedAgg(column='weight', aggfunc=max),
    min_height=pd.NamedAgg(column='height', aggfunc=min),
    total_salary=pd.NamedAgg(column='salary', aggfunc=sum),
    mean_salar=pd.NamedAgg(
        column="salary",
        aggfunc=lambda x: x.mean())
)

import numpy as np

def IQR(data):
    sorted(data)
    Q1,Q3 = np.percentile(data , [25,75])
    IQR = Q3 - Q1
    return IQR

df.groupby(['country', 'gender'])["weight"].apply(lambda x: IQR(x))