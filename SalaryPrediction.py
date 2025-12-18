from pyspark.sql import SparkSession


spark =SparkSession.builder.appName("Salary Prediction").getOrCreate()

training = spark.read.csv('data/test1.csv', inferSchema=True, header=True)

training.show()
training.printSchema()
print(training.columns)


# What's a vector assembler ?
# [Age, Experience] ---> New Feature ---> Independent Feature
from pyspark.ml.feature import VectorAssembler


feature_assembler = VectorAssembler( \
    inputCols=["Age", "Experience"], \
    outputCol="Independent Feature")

output = feature_assembler.transform(training)

output.show()
print(output.columns)

finalized_data = output.select(["Independent Feature", "Salary"])
finalized_data.show()
# What is linear regression and random split

from pyspark.ml.regression import LinearRegression

train_data, test_data = finalized_data.randomSplit([0.8, 0.5])
regressor = LinearRegression(featuresCol="Independent Feature", labelCol='Salary')
regressor = regressor.fit(train_data)

print(regressor.coefficients)
print(regressor.intercept)

prediction_results = regressor.evaluate(test_data)

prediction_results.predictions.show()
print(prediction_results.meanAbsoluteError, prediction_results.meanSquaredError)
