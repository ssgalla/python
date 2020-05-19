# import panda, matplotlib.pyplot and numpy modules
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

# read the xls file containing data
df = pd.read_csv("Case.csv")

# clean up data to use for further analysis
#
# drop columns with insufficient data
df.drop(df[df['city'] == "-"].index, inplace=True)
df.drop(df[df['longitude'] == "-"].index, inplace=True)

# drop information not required for analysis
df.drop(['group'], axis=1, inplace=True)
df.drop(['infection_case'], axis=1, inplace=True)
df.drop(['latitude'], axis=1, inplace=True)
df.drop(['longitude'], axis=1, inplace=True)
#print(df.head(80))

# slicing data and adding to seperate dataframe with total confirmed cases by province
#
# slicing data: Seoul
df_seoul = df[:8]
total_seoul = df_seoul['confirmed'].sum()

# slicing data: Busan
df_busan = df[8:12]
total_busan = df_busan['confirmed'].sum()

# slicing data: Daegu
df_daegu = df[12:17]
total_daegu = df_daegu['confirmed'].sum()

# slicing data: Daejeon
df_daejeon = df.iloc[17]
total_daejeon = df_daejeon['confirmed'].sum()

# slicing data: sejong
df_sejong = df[-2:]
total_sejong = df_sejong['confirmed'].sum()

