from pyspark.sql import SparkSession 

spark = SparkSession.builder.appName("my-spark-app").config("spark.ui.port","5050").getOrCreate()
df = spark.read.csv("../../df_matches.csv")
df.printSchema()