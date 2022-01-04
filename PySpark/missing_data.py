from pyspark.sql import SparkSession

columns = ["first_name", "last_name", "gender", "language", "age", "salary"]

data = [("Krishna", "Popplestone", "Non-binary", "German", 85, 52000),
        ("Wilbert", "Gavaran", "Male", "Thai", None, 43000),
        ("Anthe", "Klulisek", None, "Persian", 37, None),
        ("Filbert",	None, "Male", "Maltese", 43, 35000),
        ("Lisetta",	"Cohan", "Non-binary", "English", 32, 75000),
        ("Shellie",	None, "Female", "Maltese", None, 44000),
        ("Tani", "Clayton",	 None, "English", 87, 37000),
        ("Fern", "Beckerleg", "Non-binary", "Thai", 78, None),
        ("Garth", "Kegg", "Female", "German", 82, 25000)]

spark = SparkSession.builder \
    .appName("Handling missing data") \
    .getOrCreate()

df = spark.createDataFrame(data, columns)
df.show(3)