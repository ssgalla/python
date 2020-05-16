# import panda module as abbreviation pd
import pandas as pd

# import numpy module as abbreviation np
import numpy as np

##### dictionary containing data
#
data = {
    "name": ["Xavier", "Ann", "Jana", "Yi", "Robin", "Amal", "Nori"],
    "city": ["Mexico City", "Toronto", "Prague", "Shanghai", "Manchester", "Cairo", "Osaka"],
    "age": [41, 28, 33, 34, 38, 31, 37],
    "py-score": [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
}
#####


##### row_labels assigns each row in the dictionary a label
#
row_labels = [101, 102, 103, 104, 105, 106, 107]
#####


##### create a panda dataframe from the data within the dictionary then print it with the variable df
#
df = pd.DataFrame(data=data, index=row_labels)
#print(df)
#####


##### we can use the .head() function to show the first few items and .tail() to show the last few items
##### the n parameter allows you to adjust how many rows are shown respective to the order they are in 
#
#print(df.head(n=2))
#print(df.tail(n=2))
##### 


##### assign specific column to a variable to be called upon
#
name = df["name"]
age = df["age"]
cities = df["city"]
py = df["py-score"]

#print(cities)
#####


##### we can also call print data based on the row label
#
#print(cities[102])
#print(cities[104])
#####


##### you can also access a whole individual row using the accessor.loc() function as exampled below
#
ann_toronto = df.loc[102]
nori_osaka = df.loc[107]
#
#print(ann_toronto)
#print(nori_osaka)
#####


##### creating a panda dataframe using dictionaries and numpy
#
d = {'x': [1, 2, 3], 'y': np.array([2, 4, 8]), 'z': 100}
d_py = pd.DataFrame(d, index=[100, 200, 300], columns=['z', 'y', 'x'])
#print(d_py)
#####


##### creating a panda dataframe with lists
#
l = [{'x': 1, 'y': 2, 'z': 100},
     {'x': 1, 'y': 2, 'z': 100},
     {'x': 1, 'y': 2, 'z': 100}]
l_py = pd.DataFrame(l)
#print(l_py)
#####


##### making panda dataframe with a nested list (same structure is used for tuples)
#
n = [[1, 2, 100],
     [2, 4, 100],
     [3, 8, 100]]
n_py = pd.DataFrame(n, columns=['x', 'y', 'z'])
#print(n_py)
#####