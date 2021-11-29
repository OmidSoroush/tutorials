from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DecimalType
from pyspark.sql import SparkSession

data = [("John", "Lenon", 33, 19, "student"),
        ("Liam", "James", 43, 16, "engineer"),
        ("Scott", "King", 56, 21, "cook"),
        ("Robert", "Black", 19, 17, "athlete")]

# Create a schema for the dataframe
schema = StructType([
    StructField('first_name', StringType(), True),
    StructField('last_name', StringType(), True),
    StructField('age', IntegerType(), True),
    StructField('Marks', IntegerType(), True),
    StructField('occupation', StringType(), True),
])

spark = SparkSession.builder.appName('withColumn()').getOrCreate()

# Create data frame
df = spark.createDataFrame(data,schema)
df.show()



from pyspark.sql.functions import col

# change value of the Marks column (5 times higher)
df.withColumn("Marks",col("Marks")*5).show()


from pyspark.sql.functions import col

# change Marks to DecimalType
df.withColumn("Marks",col("Marks").cast("Float")).show()



from pyspark.sql.functions import col

#create new column from existing column
df.withColumn("age_in_decade",(col("age")/ 10)).show()


from pyspark.sql.functions import lit

df.withColumn("salary", lit(50000)).show()

# adding multiple columns
df.withColumn("country", lit("Germany")) \
  .withColumn("city",lit("Berlin")) \
  .show()



df.withColumnRenamed("occupation","job").show()

df.drop("Marks").show()
