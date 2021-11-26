from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .master("local[1]") \
    .appName("Creating RDD using parallelize()")\
    .getOrCreate()



rdd = spark.sparkContext.parallelize([1,2,3,4,5,6,7])
type(rdd)
print(rdd.take(3))


# Convert list to data frame
df = spark.read.format('csv') \
                .option('header',True) \
                .option('inferschema', True) \
                .load('/user/Downloads/example_data.csv')
df.show(5)
type(df)
print(f'Record count is: {df.count()}')



data = [('Berlin',35,56,67,41), ('Paris',85,76,87,91), ("London", 85,78,96,92), ("Madrid", 92,76,89,96)]

rdd = spark.sparkContext.parallelize(data, 4)

df = rdd.toDF()
print(type(df))
df.printSchema()


col_names = ['city', 'paid', 'received', 'amount', 'visits']
df = rdd.toDF(col_names)
df.printSchema()

df.show()




df2 = spark.createDataFrame(rdd).toDF(*col_names)
df2.show()


dfFromList = spark.createDataFrame(data).toDF(*col_names)
dfFromList.show()

from pyspark.sql.types import StructType, StructField, IntegerType, StringType

schema = StructType([ \
    StructField("city", StringType(), True), \
    StructField("paid", IntegerType(), True), \
    StructField("received", IntegerType(), True), \
    StructField("amount", IntegerType(), True), \
    StructField("visits", IntegerType(), True) \
    ])

df = spark.createDataFrame(data=data, schema=schema)
df.printSchema()
df.show(truncate=False)

# read CSV into DataFrame
CSV = spark.read.csv("/path/to/data/example_data.csv")

# read Text into DataFrame
Text = spark.read.text("/path/to/data/example_data.txt")

# read JSON into DataFrame
JSON = spark.read.json("/path/to/data/example_data.json")
type(df2)


df = spark.read
  .format("csv")
  .option("header", true)
  .option("inferSchema", true)
  .load(".csv")