# import panda, matplotlib.pyplot and numpy modules
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

# read the csv file containing data 
data = pd.ExcelFile("TimeAge.xls")

# clean up data to use for further analysis
# parse data to use only one days data 2020-03-02
data_date = data.parse(u'TimeAge', skipfooter=655)
#print(data_date)

# drop any empty rows just to take precaution as it is a larger dataset
data_date.dropna(inplace=True)

# print data
print("after clean up:")
print(data_date)

# plot data - age with confirmed and deceased through all data 
data_date['confirmed'].plot(label="Confirmed")
data_date['deceased'].plot(label="Deceased")
plt.legend(loc="upper right")
plt.show()