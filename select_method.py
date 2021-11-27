from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .master("local[1]") \
    .appName("select")\
    .getOrCreate()

columns = ["car_make", "car_model", "year", "color"]

data = [("Honda", "Prelude", 2000, "white"),
        ("Ford", "Mustang", 2008, "black"),
        ("Opel", "Astra", 2016, "red"),
        ("Volkswagen", "Polo", 2005, "blue")]

df = spark.createDataFrame(data, columns)

df.show()



df.select("car_make","color").show()
df.select(df.car_make,df.color).show()
df.select(df["car_make"],df["color"]).show()

#By using col() function
from pyspark.sql.functions import col
df.select(col("car_make"),col("color")).show()

# select columns using regular expression
df.select(df.colRegex("`(car)+.+`")).show()

df.columns

# select using index
df.select(df.columns[3]).show(3)
df.select(df.columns[0:3]).show(3)

type(df.columns)