# Contents
# 1. Creating a Panda dataframe (Line 26)
# 2. Retrieving Labels and Data (Line 144)
# 3. Accessing and Modifying data (Line 192)
# 4. Inserting and Deleting data (Line 254)
# 5. Applying Arithmetic Operations (Line 303)
# 6. Applying NumPy and SciPy Functions (Line 322)
# 7. Sorting a Panda Dataframe (Line 344)
# 8. Filtering Data (Line 359)
# 9. Determining Data Statistics (Line 384)
# 10. Handling Missing Data (Line 406)
# 11. Iterating Over a Panda Dataframe (Line 449)
# 12. Working with Time Series (Line 466)
# 13. Plotting with Panda Dataframes (Line 506)


# import panda module as abbreviation pd
import pandas as pd

# import numpy module as abbreviation np
import numpy as np

# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

########## 1.CREATING PANDA DATAFRAMES ##########
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

##### creating a pandas datafram with numpy arrays
##### using this method gives you the option to be able to use the parameter copy - keeping this off allows you to save significant amount of time and processing power when working with large data sets
#
arr = np.array([[1, 2, 100],
               [2, 4, 100],
               [3, 8, 100]])
df_ = pd.DataFrame(arr, columns=['x', 'y', 'z'])
#print(df_)
#####


##### example of parameter copy being False
##### in this example you can see if we change the array the dataframe also changes whereas if copy is True then it will simply copy the array values rather than using the actual available values
#
arr[0, 0] = 1000
#print(df_)
#####


##### creating a pandas dataframe from files
#
#df.to_csv('data.csv')
#####


##### reading external csv files to panda dataframe
#
read_csv = pd.read_csv('data.csv', index_col=0)
#print(read_csv)

########## 2.RETRIEVING LABELS AND DATA ##########
##### retrieve dataframes row labels with .index and column labels with .columns - lastly find column name of single column by index
#
#print(df.index)
#print(df.columns)
#print(df.columns[1])
#####


##### iterate through labels - you may not need this as you can iterate over entire dateframes in pandas 
#
#df.index = np.arrange(10, 17)
#df.index
#print(df)
#####


##### gathering data as a numpy array
##### sometimes you want to extract data from  dataframes without its label you can do this by using .to_numpy() or .values:
#
#df.to_numpy()
#####


##### how to find the data type of each column
#
#print(df.dtypes)
#print(df.dtypes[1])
#####


##### how to modify data type of individual columns
#
df_ = df.astype(dtype={'age': np.int32, 'py-score': np.float32})
#print(df_.dtypes)
#####


##### finding dataframe size
##### using the .ndim, .size and .shape functions we can return the number of dimensions, number of data values across each dimension and total number of data values (we can also check memory usage by column .memory_usage())
#
#print(df_.ndim)
#print(df_.size)
#print(df_.shape)
#print(df_.memory_usage())
#####


########## 3.ACCESSING AND MODIFYING DATA ##########
##### accessing data by using its column name as a key and secondly by using its row as a label 
#
#print(df['name'])
#print(df.loc[101])
# instead of using .loc() we can also use .iloc() this will return results by its integer index instead both are acceptable 
#print(df.iloc[0])
#####


##### accessors available in panda
##### in total four accessors are available these are .loc[], .iloc[], .at[], .iat[] out of these he first two are particularly powerful which support slicing and numpy style indexing
# you can use this slicing method to access a column in panda
#
#print(df.loc[:, 'city'])
#print(df.iloc[:, 1])
#####


##### using accessors to access specific data using slicing
##### when using slicing on a piece of data do not use tuples as these are reserved for representing multiple dimensions in numpy and pandas aswell as hierarchial, multi-level and indexing pandas
#
#print(df.loc[11:15, ['name', 'city']])
#print(df.iloc[1:6, [0, 1]])
# this can be used to get a collection of data and skipping specific columns if necessary
#print(df.iloc[1:6:2, 0])
#####


##### alternative method to use slicing in panda & numpy
##### instead of using the built in slicing contstruct we can also use slice(), numpy.s[] or pd.IndexSlice[]
#
#print(df.iloc[slice(1, 6, 2), 0])
#print(df.iloc[np.s_[1:6:2], 0])
#print(df.iloc[pd.IndexSlice[1:6:2], 0])
#####


##### accessing single items
##### when you only require a single item panda recommends using .at[] or .iat[]
#
#print(df.at[1, 'name'])
#print(df.iat[2, 0])
#####


##### using accessors to modify parts of a panda dataframe by passing it a python sequence, numpy array or single value
#
#print(df.loc[:, 'py-score'])
#df.loc[:104, ' py-score'] = [40, 50, 60, 70]
#df.loc[105:, 'py-score'] = 0
#print(df['py-score'])
#####


##### using negative indices with .iloc[] to access or modify data
#
df.iloc[:, -1] = np.array([88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0])
#print(df['py-score'])
#####


########## 4. INSERTING AND DELETING ROWS ##########
##### inserting and deleting rows of a list
##### after creating the object john we can add it to our df using .append() we can then remove it with a single call .drop()
#
john = pd.Series(data=['John', 'Boston', 34, 79], index=df.columns, name=17)
john
#print(john.name)
df = df.append(john)
#print(df)
df = df.drop(labels=[17])
#print(df)
#####


##### inserting columns generic method
#
insert = df['js-score'] = np.array([71.0, 95.0, 88.0, 79.0, 91.0, 91.0, 80.0])
insert
#print(df)
total = df['total-score'] = 0
total
#print(df)
#####


##### inserting columns using .insert()
##### using this function allows you to tell the dataframe where to place your new column
#
insert = df.insert(loc=4, column='django-score', value=np.array([86.0, 81.0, 78.0, 88.0, 74.0, 70.0, 81.0]))
insert
#print(df)
#####


##### deleting columns and data generic method
#
del df['total-score']
# you can also use .pop() to remove a column
#df.pop('total-score)
#print(df)
#####


##### removing columns 2 using .drop()
df = df.drop(labels='age', axis=1)
#print(df)
#####


########## 5. APPLYING ARITHMETIC OPERATIONS ##########
##### applying basic arithmetic operators
#
# addition
addition = df['py-score'] + df['js-score']
# divison
division = df['py-score'] / 100
#print(addition)
#print(division)
#####


##### using linear combination on df
df['total'] =\
     0.4 * df['py-score'] + 0.3 * df['django-score'] + 0.3 * df['js-score']
#print(df)
#####


########## 6. APPLYING NUMPY AND SCIPY FUNCTIONS ##########
##### using series or df objects as arguments instead of arrays example using numpy.average()
#
score = df.iloc[:, 2:5]
#print(score)
# work out the average of the selection
averagedf = np.average(score, axis=1, weights=[0.4, 0.3, 0.3])
#print(averagedf)
#####


##### append new column to df using .average()
#
# delete current total column so we can insert new one
del df['total']
#print(df)
# appending new column using .average()
df['total'] = np.average(df.iloc[:, 2:5], axis=1, weights=[0.4, 0.3, 0.3])
#print(df)
#####


########## 7. SORTING A PANDA DATAFRAME ##########
##### sorting a panda df using sort_values()
#
# sort by single column
sort = df.sort_values(by='js-score', ascending=False)
sort
#print(df)

# sort by multiple columns
sortmultiple = df.sort_values(by=['total', 'py-score'], ascending=[False, False])
sortmultiple
#print(df)
#####


########## 8. FILTERING DATA ##########
##### using booleans to filter data with operators
#
filter_ = df['django-score'] >= 80
#print(filter_)
# by using filter_ as a parameter for df we can view the data
#print(df[filter_])
#####


##### creating powerful expressions by combining logical operators
##### the following operators are available (NOT ~, AND &, OR | and XOR ^)
#
logexpression = df[(df['py-score'] >= 80) & (df['js-score'] >= 80)]
#print(logexpression)
#####


##### using numpy logical routines
##### .where() can be used to filter data and or replace values in the positions where the provided condition isn't satisfied
#
#df['django-score'].where(cond=df['django-score'] >= 80, other=0.0)
#####


########## 9. DETERMINING DATA STATISTICS ##########
##### get basic statistice for numerical columns of a panda df with .describe()
#
num_stats = df.describe()
#print(num_stats)
#####


##### getting other statistical data using functions on df
#
overall_mean = df.mean()
pyscore_mean = df['py-score'].mean()
overall_standard_deviation = df.std()
pyscore_standard_deviation = df['py-score'].std()

#print(overall_mean)
#print(pyscore_mean)
#print(overall_standard_deviation)
#print(pyscore_standard_deviation)
#####


########## 10. HANDLING MISSING DATA ##########
##### example of a dataframe with a missing value or nan
#
df_ = pd.DataFrame({'x': [1, 2, np.nan, 4]})
#print(df_)
#####


##### calculating with missing data
##### many panda methods will omit nan values when performing calculations unless they are explicitly instructed not to
##### in the below example the first one will omit the nan value automatically but see the second example outputs nan because we included the missing value with the skipna parameter
#
notwithnan = df_.mean()
withnan = df_.mean(skipna=False)
#print(notwithnan)
#print(withnan)
#####


##### filling missing data 
#
# fill missing value with 0 
df_.fillna(value=0)
# fill missing value with value directly above it
#df_.fillna(method='ffill')
# fill missing value with value directly below it
#df_.fillna(method='bfill')
#####


##### using interpolate on missing values
#
#interpolate = df_.interpolate()
#interpolate
#####


##### in some cases you may want to delete rows and columns with missing data
#
#df_.dropna()
#####


########## 11. ITERATING OVER A PANDAS DATAFRAME ##########
##### how to iterate over a dataframe using .items(), .iteritems(), .iterrows() and .itertuples()
#
# .items() and .iteritems()
#for col_label, col in df.iteritems():
#     print(col_label, col, sep='\n', end='\n\n')
#
# .iterrows()
#for row_labels, row in df.iterrows():
#     print(row_labels, row, sep='\n', end='\n\n')
#
# .itertuples()
#for row in df.loc[;, ["name", "city", "total"]].itertuples():
#     print(row)
#####


########## 12. WORKING WITH TIME SERIES ##########
##### creating dataframes with time-series labels
##### hourly temperatures for a 24 hour time period time-series example
#
temp_c = [ 8.0,  7.1,  6.8,  6.4,  6.0,  5.4,  4.8,  5.0,
           9.1, 12.8, 15.3, 19.1, 21.2, 22.1, 22.4, 23.1,
           21.0, 17.9, 15.5, 14.4, 11.9, 11.0, 10.2,  9.1]

# create hourly date and time range to match temperature
dt = pd.date_range(start='2019-10-27 00:00:00.0', periods = 24, freq='H')
#print(dt)

# create dataframe combining temperature and date time stamps
temp = pd.DataFrame(data={'temp_c': temp_c}, index=dt)
#print(temp)
#####


##### indexing and slicking time-series
#
slicing_temp_data = temp['2019-10-27 05':'2019-10-27 14']
#print(slicing_temp_data)
#####


##### resampling and rolling 
##### example we shall split a hourly interval day in six hour intervals and get the mean temp for each interval using the .resample() and .mean() func
#
conversion = temp.resample(rule='6h').mean()
#####
#print(conversion)


##### rolling-window analysis
#
rolling = temp.rolling(window=3).mean()
#print(rolling)
#####


########## 13. PLOTTING WITH PANDAS DATAFRAMES ##########
##### how to plot with matplotlib.pyplot
#
temp.plot()
#plt.show()
#
# you can chain multiple methods to save the plot figure
#temp.plot().get_figure().savefig('temperatures.png')
#####

##### histogram
# create a histogram from data we passed for job candidates
#
df.loc[:, ['py-score', 'total']].plot.hist(bins=5, alpha=0.4)
#plt.show()