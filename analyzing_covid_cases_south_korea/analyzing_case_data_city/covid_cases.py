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
print(df.head(80))

# slicing data: Seoul records
df_seoul = df[:8]
#print("seoul clean data:")
#print(df_seoul)

# slicing data: Busan
df_busan = df[8:12]
#print("busan clean data:")
#print(df_busan)

# slicing data: Daegu
df_daegu = df[12:17]
#print("daegu clean data:")
#print(df_daegu)

# slicing data: Daejeon
df_daejeon = df.iloc[17]
#print("daejeon clean data:")
#print(df_daejeon)
