
from pyspark.sql import SparkSession

columns = ["first_name", "last_name", "gender", "language", "age", "salary"]

data = [("Krishna", "Popplestone", "Non-binary", "German", 85, 52000),
        ("Wilbert", "Gavaran", "Male", "Thai", 47, 43000),
        ("Anthe", "Klulisek", "Male", "Persian", 37, 89000),
        ("Filbert",	"Roebuck", "Male", "Maltese", 43, 35000),
        ("Lisetta",	"Cohan", "Non-binary", "English", 32, 75000),
        ("Shellie",	"Blackston", "Female", "Maltese", 30, 44000),
        ("Tani", "Clayton",	 "Female", "English", 87, 37000),
        ("Fern", "Beckerleg", "Non-binary", "Thai", 78, 60000),
        ("Garth", "Kegg", "Female", "German", 82, 25000)]

spark = SparkSession.builder \
    .appName("DataFrame Bascis") \
    .getOrCreate()

df = spark.createDataFrame(data, columns)
df.show()

# summary statistics
df.describe().show()

# print the schema
df.printSchema()


# the rest comes here
df.columns


from pyspark.sql.types import (StructType, StructField,
                                StringType, IntegerType)

data_schema = StructType([StructField("first_name", StringType(), True),
                          StructField("last_name", StringType(), True),
                          StructField("gender", StringType(), True),
                          StructField("language", StringType(), True),
                          StructField("age", IntegerType(), True),
                          StructField("salary", IntegerType(), True)])

df = spark.createDataFrame(data, schema=data_schema)
df.printSchema()

type(df["age"])

df["age"]

df.select("age").show(3)

df.head(2)[0]

df.select(["first_name", "age"]).show(3)

df.withColumn("new_salary", df["salary"] + 100).show(4)

df.show()

df.withColumnRenamed("salary", "my_new_salary").show(4)

df.createOrReplaceTempView("employees")

results = spark.sql("SELECT * FROM employees WHERE age > 40")

results.show(3)