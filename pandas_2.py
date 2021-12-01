
import pandas as pd

lst = ["John", "James", "Scott", "Robert", "Liam", "Sammy"]

my_series = pd.Series(lst)

print(type(my_series))



import pandas as pd

dictionary = {'A' : 100, 'B' : 200, 'C' : 300}

my_series = pd.Series(dictionary)

print(my_series)




import pandas as pd

data = [['tom', 20], ['scott', 35], ['juli', 44]]

df = pd.DataFrame(data, columns = ['Name', 'Age'])

print(df)


data = {
    "student": ["john", "tom", "felix", "mike"],
    'books': [3, 2, 9, 1],
    'pens': [5, 3, 7, 2]
}

import pandas as pd

columns = ["first_name", "last_name", "gender", "language", "age", "salary"]

data = [("Krishna", "Popplestone", "Non-binary", "German", 30, 52000),
        ("Wilbert", "Gavaran", "Male", "Thai", 70, 43000),
        ("Anthe", "Klulisek", "Male", "Persian", 40, 89000),
        ("Filbert",	"Roebuck", "Male", "Maltese", 20, 35000),
        ("Lisetta",	"Cohan", "Non-binary", "English", 55, 75000),
        ("Shellie",	"Blackston", "Female", "Maltese", 23, 44000),
        ("Tani", "Clayton",	 "Female", "English", 42, 37000),
        ("Fern", "Beckerleg", "Non-binary", "Thai", 25, 60000),
        ("Garth", "Kegg", "Female", "German", 29, 25000)]

df = pd.DataFrame(data, columns=columns)
print(df)

df.first_name

# select all females
df[(df["gender"] == "Female") & (df["age"] > 25)]

df[]

data = [{'a': 10, 'b': 20, 'c':30},
		{'a':100, 'b': 200, 'c': 300}]

df = pd.DataFrame(data)
print(df)

Name = ["john", "tom", "felix", "mike"]
Age = [25, 30, 26, 22]
Marks = [20, 21, 17, 19]

list_of_tuples = list(zip(Name, Age, Marks))

df = pd.DataFrame(list_of_tuples,
                  columns = ['Name', 'Age', "Marks"])

print(df)

# select single row, single column
df.loc[6, "age"]

# select multiple rows and multiple columns
df.loc[[2,4,7], ["first_name", "gender"]]

# select all rows and multiple columns
df.loc[:, ["language", "salary"]]


# select single row
df.iloc[0]

# all rows, single column
df.iloc[:, 0]

# some rows, some columns within a range
df.iloc[1:5, 2:4]

# some rows, some columns not within a range
df.iloc[[2, 3, 7], [0, 2, 4]]

subset_df = df.loc[df["age"]> 30]
print(subset_df)

print(subset_df.reset_index())

new_index = df.set_index('first_name')
print(new_index)

df["city"] = "Berlin"
df["language"] = "German"
print(df)