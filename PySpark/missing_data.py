from pyspark.sql import SparkSession

columns = ["first_name", "last_name", "gender", "language", "age", "salary"]

data = [("Krishna", "Popplestone", "Non-binary", "German", 85, 52000),
        ("Wilbert", "Gavaran", "Male", "Thai", None, 43000),
        (None, None, None, None, 37, None),
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

df.na.drop(subset=["last_name", "salary"]).show(3)

df.na.fill("No Last Name", subset=["last_name"]).show(3)

from pyspark.sql.functions import mean

# calculate the mean
mean_age = df.select(mean(df["age"])).collect()

# get the actual mean value
mean_age = mean_age[0][0]

# fill the missings with the mean
df.na.fill(mean_age, subset=["age"]).show(3)