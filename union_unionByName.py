from pyspark.sql import SparkSession

columns = ["first_name", "last_name", "gender", "position", "age", "salary"]

data = [("Krishna", "Popplestone", "Non-binary", "scientist", 85, 52000),
        ("Wilbert", "Gavaran", "Male", "scientist", 47, 43000),
        ("Anthe", "Klulisek", "Male", "scientist", 37, 89000),
        ("Filbert",	"Roebuck", "Male", "scientist", 43, 35000)]

spark = SparkSession.builder \
        .appName("union() - unionByName()").getOrCreate()

scientists = spark.createDataFrame(data, columns)
scientists.show()

data2 = [("Lisetta",	"Cohan", "Non-binary", "engineer", 32, 75000),
        ("Shellie",	"Blackston", "Female", "engineer", 30, 44000),
        ("Tani", "Clayton",	 "Female", "engineer", 87, 37000),
        ("Fern", "Beckerleg", "Non-binary", "engineer", 78, 60000),
        ("Garth", "Kegg", "Female", "engineer", 82, 25000)]

engineers = spark.createDataFrame(data2, columns)
engineers.show()

union_df = scientists.union(engineers).distinct()
union_df.show()




columns = ["first_name", "age", "salary"]

data = [("Krishna", 85, 52000),
        ("Wilbert", 47, 43000),
        ("Anthe", 37, 89000),
        ("Filbert", 43, 35000)]

df1 = spark.createDataFrame(data, columns)
df1.show()

columns2 = ["age", "first_name"]
data2 = [(32, "Lisetta"),
        (45, "Shellie"),
        (22, "Tani"),
        (77, "Fern"),
        (19, "Garth")]

df2 = spark.createDataFrame(data2, columns2)
df2.show()

union_df = df1.unionByName(df2, allowMissingColumns=True)
union_df.show()