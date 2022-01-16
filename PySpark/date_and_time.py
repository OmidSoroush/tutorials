
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder \
    .appName("Date and Time") \
    .getOrCreate()


data = [["1"]]
df = spark.createDataFrame(data, ["id"])

#current_date()
df.withColumn("current_date", current_date()).show()

df.select(current_date().alias("current_date")).show()

#df.select(current_date().alias("current_date")).show()


data=[["1","2021-25-01"],["2","2019-13-01"],["3","2021-23-02"]]
df=spark.createDataFrame(data,["id","date"])
df.show()


from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Date and Time") \
    .getOrCreate()

data=[["1","2021-25-01"],["2","2019-13-01"],["3","2021-23-02"]]
df=spark.createDataFrame(data,["id","date"])
df.show()

df.select(col("date"),
    to_date(col("date"), "yyyy-dd-MM").alias("to_date")
  ).show()

df1 = df.withColumn("date", to_date(col("date"), "yyyy-dd-MM"))
df1.show()
df1.select(col("date"),
    datediff(current_date(),to_date(col("date"), format="yyyy-dd-MM")).alias("date_diff")
  ).show()

df1.select(col("date"),
     year(col("date")).alias("year"),
     month(col("date")).alias("month"),
     next_day(col("date"),"Mon").alias("next_day"),
     weekofyear(col("date")).alias("weekofyear")
  ).show()


dayofweek(), dayofmonth(), dayofyear()

df1.select(col("date"),
     dayofweek(col("date")).alias("dayofweek"),
     dayofmonth(col("date")).alias("dayofmonth"),
     dayofyear(col("date")).alias("dayofyear"),
  ).show()

data=[["1","04-14-2012 10 21 39 07"],["2","06-22-2015 09 11 29 333"],["3","07-15-2020 08 12 59 73"]]
df2=spark.createDataFrame(data,["id","timestamp_string"])
df2.show(truncate=False)

df2.select(col("timestamp_string"), current_timestamp().alias("current_timestamp")
  ).show(truncate=False)


df3 = df2.select(col("timestamp_string"),
    to_timestamp(col("timestamp_string"), "MM-dd-yyy HH mm ss SSS").alias("to_timestamp")
  )


df3.select(col("to_timestamp"),
    hour(col("to_timestamp")).alias("hour"),
    minute(col("to_timestamp")).alias("minute"),
    second(col("to_timestamp")).alias("second")
  ).show(truncate=False)

