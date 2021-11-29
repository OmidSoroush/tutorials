from pyspark.sql import SparkSession

data = [("John", "Lennox", 33, 19, "student"),
        ("Liam", "James", 43, 16, "engineer"),
        ("Scott", "King", 56, 21, "cook"),
        ("Robert", "Black", 19, 17, "athlete"),
        ("Ray", "Black", 24, 17, "cook"),
        ("Leo", "Luis", 19, 17, "engineer")]

# Create a schema for the dataframe
schema = StructType([
    StructField('first_name', StringType(), True),
    StructField('last_name', StringType(), True),
    StructField('age', IntegerType(), True),
    StructField('Marks', IntegerType(), True),
    StructField('occupation', StringType(), True),
])

spark = SparkSession.builder \
        .appName("filter()").getOrCreate()

df = spark.createDataFrame(data, schema)
df.show()


df.filter(df.age > 40).show()

df.filter(df.first_name == "Liam").show()

df.filter("last_name == 'James'").show()



df.filter( (df.age  < 20) & (df.occupation  == "athlete") ) \
    .show()


lst=["cook","athlete","student"]
df.filter(df.occupation.isin(lst)).show()

# the opposite using ~
df.filter(~df.occupation.isin(lst)).show()


df.filter(df.first_name.startswith("S")).show()

df.filter(df.last_name.endswith("x")).show()

df.filter(df.occupation.contains("at")).show()


# filter where first name starts with Li and has two more characters
df.filter(df.first_name.like("%Li__")).show()

# filter where occupation contains double "o"
df.filter(df.occupation.rlike("\w?(oo)\w?")).show()


