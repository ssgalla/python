# import panda, matplotlib.pyplot and numpy modules
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

# read the xls file containing data
df = pd.read_csv("Case.csv")

# clean up data to use for further analysis
# drop columns with insufficient data
df.drop(df[df['city'] == "-"].index, inplace=True)
df.drop(df[df['longitude'] == "-"].index, inplace=True)
#print(df.head(50))

