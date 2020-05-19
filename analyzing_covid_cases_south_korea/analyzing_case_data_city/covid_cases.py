##### import panda, matplotlib.pyplot and numpy modules #####
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

##### read csv file containing data #####
df = pd.read_csv("Case.csv")

##### clean up data to use for further analysis #####
# drop columns with insufficient data
df.drop(df[df['city'] == "-"].index, inplace=True)
df.drop(df[df['longitude'] == "-"].index, inplace=True)

# drop information not required for analysis
df.drop(['group'], axis=1, inplace=True)
df.drop(['infection_case'], axis=1, inplace=True)
df.drop(['latitude'], axis=1, inplace=True)
df.drop(['longitude'], axis=1, inplace=True)

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

# slicing data: Sejong
df_sejong = df[-2:]
total_sejong = df_sejong['confirmed'].sum()

###### create seperate dataframe for final results containing confirmed cases grouped by province #####
# initialise data for dataframe
data_province = {'province':['Seoul', 'Busan', 'Daegu', 'Daejeon', 'Sejong'], 'confirmed':[total_seoul, total_busan, total_daegu, total_daejeon, total_sejong]} 
provinces = data_province['province']
confirmed_cases = data_province['confirmed']


# df for province group results
df = pd.DataFrame(data_province)
print("Confirmed cases grouped by province:")
print(df)

##### matplotlib to build analysis data
# building horizontal bar chart to depict most affected province?
provinces_bar = provinces
y_pos = np.arange(len(provinces_bar))
confirmed = confirmed_cases

plt.barh(y_pos, confirmed, align='center', alpha=0.5)
plt.yticks(y_pos, provinces_bar)
plt.xlabel('Confirmed Cases')
plt.ylabel('Provinces (S. Korea)')

plt.show()