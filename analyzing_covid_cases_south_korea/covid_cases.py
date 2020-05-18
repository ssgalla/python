# import panda, matplotlib.pyplot and numpy modules
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

# read the csv file containing data 
data = pd.ExcelFile("TimeAge.xls")

# clean up data to use for further analysis
data_date = data.parse(u'TimeAge')

# drop any empty rows just to take precaution as it is a larger dataset
data_date.dropna(inplace=True)

# change index to date 
