# import panda, matplotlib.pyplot and numpy modules
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

# read the excel file containing data then print it 
data = pd.ExcelFile("obes-phys-acti-diet-eng-2014-tab.xls")
#print(data.sheet_names)

# we need to cleanup the data within the excel sheet 7.2 
# we only require rows 5 - 18 to analyze the data the rest of the data is not useful to our script
#
# read 2nd section by age
data_age = data.parse(u'7.2', skiprows=4, skipfooter=14)
#print(data_age)

# rename the first header currently unnamed to Year
data_age.rename(columns={u'Unnamed: 0': u'Year'}, inplace=True)

# drop the empty rows filled with NaN
data_age.dropna(inplace=True)

# change the index to year
data_age.set_index('Year', inplace=True)

# print clean data
print("after clean up:")
print(data_age)

# drop total column and plot
data_age_minus_total = data_age.drop('Total', axis=1)

# plot 
#data_age_minus_total.plot()
#plt.show()

# plot: Are Children Getting Fatter? 
# analysis children vs adults obesity rates
data_age['Under 16'].plot(label="Under 16")
data_age['35-44'].plot(label="35-44")
plt.legend(loc="upper right")
#plt.show()

# plot: But What About The Future?
# using curve fitting and polynomial interpolation to try and predict the future obesity rates for children in england
#
print("curve fitting and polynomial interpolation:")
kids_values = data_age['Under 16'].values
x_axis = range(len(kids_values))

poly_degree = 4
curve_fit = np.polyfit(x_axis, kids_values, poly_degree)
poly_interp = np.poly1d(curve_fit)

poly_fit_values = []

for i in range(len(x_axis)):
    poly_fit_values.append(poly_interp(i))

plt.plot(x_axis, poly_fit_values, "-r", label="Fitted")
plt.plot(x_axis, kids_values, "-b", label="Orig")
plt.legend(loc="upper right")

# final plot: But What About The Future?
x_axis2 = range(15)

poly_fit_values = []
for i in range(len(x_axis2)):
    poly_fit_values.append(poly_interp(i))