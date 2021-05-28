from pyspark.sql import SparkSession 
from pyspark.sql.functions import col, when
from datetime import date

spark = SparkSession.builder.appName("my-spark-app").config("spark.ui.port","5050").getOrCreate()
df = spark.read.format("csv").option("header", "true").load("../../df_matches.csv")
df.printSchema()
df2 = df.withColumnRenamed("X4","match").withColumnRenamed("X6","competition")
df2.printSchema()
df2.select('match', 'competition', 'adversaire', 'score_france', 'score_adversaire', 'penalty_france', 'penalty_adversaire', 'date').show()

def blank_as_zero(x):
    return when(col(x) != "NA", col(x)).otherwise(0)

dfWithEmptyReplaced = df2.withColumn("penalty_france", blank_as_zero("penalty_france")).withColumn("penalty_adversaire", blank_as_zero("penalty_adversaire"))
dfWithEmptyReplaced.show()

today = date.today().strftime("%Y-%m-%d")
dfFiltered = dfWithEmptyReplaced.filter((dfWithEmptyReplaced.date >= '1980-03-01') & (dfWithEmptyReplaced.date <= today))
dfFiltered.show()