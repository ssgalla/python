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
data_plotstatus.dropna(subset = ["plot_status"], inplace=True)

# drop unnecessary information for this question
data_plotstatus.drop(['plot_ID'], axis=1, inplace=True)
data_plotstatus.drop(['plot_ideology'], axis=1, inplace=True)
data_plotstatus.drop(['prevention_method'], axis=1, inplace=True)
data_plotstatus.drop(['attack_date'], axis=1, inplace=True)
data_plotstatus.drop(['victims_wounded'], axis=1, inplace=True)
data_plotstatus.drop(['victims_killed'], axis=1, inplace=True)
data_plotstatus.drop(['plot_name'], axis=1, inplace=True)

# find how many plots were prevented
prevented_plots = data_plotstatus[data_plotstatus['plot_status'].str.match('Prevented')]
notprevented_plots = data_plotstatus[data_plotstatus['plot_status'].str.match('NotPrevented')]

prevented_total = prevented_plots.len()

print(prevented_total)