from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .master("local[1]") \
    .appName("show()")\
    .getOrCreate()


columns = ['id', 'by', 'quote']

data = [(1, "W. Edwards Deming", "In God we trust. All others must bring data."),
        (2, "Sherlock Holmes", "It is a capital mistake to theorize before one has data."),
        (3, "Geoffrey Moore", "Without big data analytics, companies are blind and deaf, wandering out onto the web like deer on a freeway."),
        (4, "Jim Barksdale", "If we have data, let’s look at data. If all we have are opinions, let’s go with mine.")]

df = spark.createDataFrame(data, columns)

df.show(n=2, truncate=40, vertical=True)