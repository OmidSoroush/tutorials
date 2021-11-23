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
                .load('/Users/omidsoroush/Downloads/example_data.csv')
df.show()
type(df)
print(f'Record count is: {df.count()}')



data = [('Berlin',35,56,67,41), ('Paris',85,76,87,91), ("London", 85,78,96,92), ("Madrid", 92,76,89,96)]

rdd = spark.sparkContext.parallelize(data, 4)

