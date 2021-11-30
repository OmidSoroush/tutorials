from pyspark.sql import SparkSession

spark = SparkSession.builder \
        .appName("Joins").getOrCreate()

columns = ["first_name", "last_name", "gender", "language", "origin_city_id", "salary"]

data = [("Krishna", "Popplestone", "Non-binary", "German", 50, 52000),
        ("Wilbert", "Gavaran", "Male", "Thai", 70, 43000),
        ("Anthe", "Klulisek", "Male", "Persian", 90, 89000),
        ("Filbert",	"Roebuck", "Male", "Maltese", 50, 35000),
        ("Lisetta",	"Cohan", "Non-binary", "English", 80, 75000),
        ("Shellie",	"Blackston", "Female", "Maltese", 90, 44000),
        ("Tani", "Clayton",	 "Female", "English", 60, 37000),
        ("Fern", "Beckerleg", "Non-binary", "Thai", 100, 60000),
        ("Garth", "Kegg", "Female", "German", 110, 25000)]

emp_df = spark.createDataFrame(data, columns)
emp_df.show()

columns2 = ["city_id", "city"]

data2 = [(50, "Berlin"),
        (60, "London"),
        (70, "Paris"),
        (80, "Rome"),
        (150, "Madrid")]

city_df = spark.createDataFrame(data2, columns2)
city_df.show()



emp_df.join(city_df,emp_df.origin_city_id == city_df.city_id, "inner") \
     .show()


emp_df.join(city_df,emp_df.origin_city_id == city_df.city_id, "full") \
     .show()

emp_df.join(city_df,emp_df.origin_city_id == city_df.city_id, "fullouter") \
     .show()

emp_df.join(city_df,emp_df.origin_city_id == city_df.city_id, "left") \
     .show()

emp_df.join(city_df,emp_df.origin_city_id == city_df.city_id, "leftouter") \
     .show()


emp_df.join(city_df,emp_df.origin_city_id == city_df.city_id, "right") \
     .show()

emp_df.join(city_df,emp_df.origin_city_id == city_df.city_id, "rightouter") \
     .show()


emp_df.join(city_df,emp_df.origin_city_id == city_df.city_id, "anti") \
     .show()


emp_df.createOrReplaceTempView("emp")
city_df.createOrReplaceTempView("city")

joined = spark.sql("SELECT * FROM emp AS e INNER JOIN city AS c ON e.origin_city_id == c.city_id")

joined.show()