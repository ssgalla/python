##### import panda, matplotlib.pyplot and numpy modules #####
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

##### read csv file containing data #####
df = pd.read_csv("Plots.csv")

##### create seperate variable for first part of analysis
data_plotstatus = df

##### How many terrorist attacks were executed in comparison to how many were prevented? #####
# data clean up required for this analysis 
# remove records where no details are recorded on whether attacks was prevented or not prevented
data_plotstatus.dropna(subset = ["plot_status"])

# drop unnecessary information for this question
data_plotstatus.drop(['plot_ID'], axis=1)
data_plotstatus.drop(['plot_ideology'], axis=1)
data_plotstatus.drop(['prevention_method'], axis=1)
data_plotstatus.drop(['attack_date'], axis=1)
data_plotstatus.drop(['victims_wounded'], axis=1)
data_plotstatus.drop(['victims_killed'], axis=1)
data_plotstatus.drop(['plot_name'], axis=1)

# find how many plots were prevented
prevented_plots = data_plotstatus[data_plotstatus['plot_status'] == "Prevented"]
prevented_plots = len(prevented_plots)

# find how many plots were not prevented
notprevented_plots = data_plotstatus[data_plotstatus['plot_status'] == 'NotPrevented']
notprevented_plots = len(notprevented_plots)

print(prevented_plots)
print(notprevented_plots)