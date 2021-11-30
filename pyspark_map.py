from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]") \
    .appName("map()").getOrCreate()

data = ["Shana Weafer", "Nicko Agass", "Mose Lineham",
        "Justino Satyford", "Chick Lansbury", "Nial Twitchett",
        "Bernard Cursey", "Maudie Cantua"]

rdd=spark.sparkContext.parallelize(data)

uppercase_rdd = rdd.map(lambda x: x.upper())
uppercase_rdd.collect()