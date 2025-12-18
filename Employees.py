from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.ml.feature import Imputer

spark = SparkSession.builder.appName('Employees').getOrCreate()

df = spark.read.csv('data/Employees.csv', inferSchema=True, header=True)

df.printSchema()
df_drop = df.drop('Experience')
# df_drop = df_drop.na.drop()
# df_drop = df_drop.na.drop(how="any", thresh=2)
# df_drop = df_drop.na.drop(how='any', subset=['Age'])
df_drop.show()
df.describe().show()
#na.fill only works for string values
df_missing = df.na.fill('Missing values', ['name', 'age', 'experience', 'salary']) 
df_missing.show()

# replaces the null values in age, experience and salary with mean of each column
imputer = Imputer(
    inputCols=['age', 'experience', 'salary'],
    outputCols=['{}_imputed'.format(c) for c in ['age', 'experience', 'salary']]
    ).setStrategy('mean')
    
df_imputed = imputer.fit(df_missing).transform(df_missing)
df_imputed.show()
