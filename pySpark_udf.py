from pyspark.sql import SparkSession

spark = SparkSession.builder \
        .appName("UDF").getOrCreate()

columns = ["full_name", "age", "salary"]

data = [("Krishna Cohan", 85, 52000),
        ("Wilbert Blackston", 47, 43000),
        ("Anthe Clayton", 37, 89000),
        ("Filbert Roebuck", 43, 35000)]

df = spark.createDataFrame(data, columns)
df.show()

@udf(returnType=StringType())
def get_first_name(name):
       lst = name.split()
       return lst[0]



from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

split_udf = udf(lambda x: get_first_name(x), StringType())

from pyspark.sql.functions import col

df.withColumn("first_name", split_udf(col("full_name"))) \
  .show()
