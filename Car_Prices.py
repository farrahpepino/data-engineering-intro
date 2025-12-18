from pyspark.sql import SparkSession
from pyspark.sql.functions import *



spark = SparkSession.builder.appName('Car Price').getOrCreate()

# spark reads all your data as string, with inferschema it follows the actual data type
df = spark.read \
.option('header', True) \
.option('inferSchema', True) \
.csv('data/car_details.csv')
df.printSchema()


# df.select(['name', 'year']).filter(col('year')>2016).show()
df.where(~(df['year']>2018)).select(['name', 'year']).show()
# df.describe().show() 

# df_new = df.withColumn("Price_Times_2", col('selling_price')*2)
# df_new.show()

# df_new = df_new.withColumnRenamed('Price_Times_2', "new_selling_price")
# df_new.show()
# df_drop = df_new.drop('new_selling_price')
# df_drop.show()