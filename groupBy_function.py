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
        .appName("filter()").getOrCreate()

df = spark.createDataFrame(data, columns)
df.show()

# sum
df.groupBy("gender").sum("salary").show()

# count
df.groupBy("gender").count().show()

# min
df.groupBy("gender").min("salary").show()

# max
df.groupBy("gender").max("salary").show()

# avg
df.groupBy("gender").avg("salary").show()





df.groupBy("gender","language") \
    .sum("salary","age") \
    .show()

df.printSchema()


from pyspark.sql.functions import max,min,mean,count

df.groupBy("language") \
    .agg(mean("salary").alias("mean_salary"), \
         min("salary").alias("min_salary"), \
         max("salary").alias("max_salary"), \
         mean("age").alias("mean_age") \
     ).show()

