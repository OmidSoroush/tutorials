
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

df.describe().show()