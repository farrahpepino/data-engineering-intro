import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/car_details.csv', sep=',')
df.head()
df.info()

df = df.dropna()

# Goal: To identify patterns and associations between car specifications and their resale prices, highlighting which features tend to correspond to higher prices.

df['fuel']= df['fuel'].astype('category')
df["seller_type"] = df["seller_type"].astype("category")
df["transmission"] = df["transmission"].astype("category")
df["owner"] = df["owner"].astype("category")

plt.scatter(df["year"], df["selling_price"])
plt.xlabel("Year of Manufacture")
plt.ylabel("Selling Price")
plt.title("Selling Price vs Year")
plt.show()

plt.scatter(df["km_driven"], df["selling_price"])
plt.xlabel("KM Driven")
plt.ylabel("Selling Price")
plt.title("Selling Price vs Mileage")
plt.show()

df.groupby("fuel")["selling_price"].mean().plot(kind="bar")
plt.ylabel("Average Selling Price")
plt.title("Average Selling Price by Fuel Type")
plt.show()

df.groupby("transmission")["selling_price"].mean().plot(kind="bar")
plt.ylabel("Average Selling Price")
plt.title("Average Selling Price by Transmission Type")
plt.show()

df.groupby("seller_type")["selling_price"].mean().plot(kind="bar")
plt.ylabel("Average Selling Price")
plt.title("Average Selling Price by Seller Type")
plt.show()

