from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName('Employees 2').getOrCreate()

df = spark.read.csv('data/Employees2.csv', inferSchema=True, header=True)

df.show()

df.groupBy('Name').sum().show()
df.groupBy('Departments').sum().show()
df.agg({'Salary': 'sum'})
df.groupBy('Departments').mean().show()
df.groupBy('Departments').avg().show()
df.groupBy('Name').min().show()
df.groupBy('Name').max().show()
