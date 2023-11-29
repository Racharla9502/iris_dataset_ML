# importing the data
import numpy as np
import pandas as pd

data = pd.read_csv("C:\\Users\\rvman\\Downloads\\Iris.csv")

print(data.head(5))

print(data.tail(5))

print(data.dtypes)

print(data.describe())

print(data.info())



# data wrangling