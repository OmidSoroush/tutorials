from pyspark.sql import SparkSession

columns = ["first_name", "last_name", "gender", "language", "age"]

data = [("Krishna", "Popplestone", "Non-binary", "Japanese", 85),
        ("Wilbert",	"Gavaran", "Male", "Thai", 47),
        ("Anthe", "Klulisek", "Genderqueer", "Persian", 37),
        ("Filbert",	"Roebuck", "Male", "Maltese", 43),
        ("Lisetta",	"Cohan", "Non-binary", "Tsonga",	32),
        ("Shellie",	"Blackston", "Female", "Maltese", 30),
        ("Tani", "Clayton",	 "Female",	"English",	87),
        ("Fern", "Beckerleg", "Non-binary",	"Icelandic", 78),
        ("Garth", "Kegg", "Female",	"German", 82)]

spark = SparkSession.builder \
        .appName("filter()").getOrCreate()

df = spark.createDataFrame(data, columns)
df.show()

from pyspark.sql.functions import col

df.sort("first_name").show()
df.sort(col("first_name")).show()

df.sort("first_name", ascending=False).show()


from pyspark.sql.functions import col

df.sort("gender", "language").show()
df.sort(col("gender"), col("language"), ascending=False).show()


from pyspark.sql.functions import col

df.orderBy("gender", "language", ascending=False).show()
df.orderBy(col("gender"), col("language")).show()


from pyspark.sql.functions import col

df.sort(col("gender").asc(), col("language").desc()).show()
df.orderBy(col("gender").asc(), col("language").desc()).show()