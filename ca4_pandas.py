# -*- coding: utf-8 -*-
"""
Created on Sun May 17 12:08:01 2020

@author: pmesquit

This program was created for CA4 of B8IT105

Both csv used for this CA were downloaded from Kaggle's "Uncover Covid-19 Challange"
https://www.kaggle.com/roche-data-science-coalition/uncover/metadata

I'm going to use pandas library to do an analysis of covid data in Ireland and Portugal, aiming to compare number of cases with mobility data.

The two csv files I'm going to use are:
-johns-hopkins-covid-19-daily-dashboard-cases-over-time.csv (contains covid19 data over time)
-regional-mobility.csv (mobility data provided from google)

"""


import matplotlib.pyplot as plt
import pandas as pd

#To strat I'm importing the csv files into data frames
cases = pd.read_csv('johns-hopkins-covid-19-daily-dashboard-cases-over-time.csv')
mobility = pd.read_csv('regional-mobility.csv')

#Next functions were used to analyse the data tables
cases.dtypes
mobility.dtypes

cases.head()
mobility.head()

cases.columns
mobility.columns

#After overlooking data columns, and num rows it is needed to filter the data and reduce the data frame to what we are interested
cases_ir_pt = cases[cases["country_region"].isin(["Ireland","Portugal"])]


mobility_ir_pt = mobility[mobility["country"].isin(["Ireland","Portugal"])]
mobility_ir_pt = mobility_ir_pt[mobility_ir_pt["region"]=="Total"] # To removel county/region level data

pd.set_option('display.max_columns', None)
cases_ir_pt.tail(100) # This allowed me to check some columns have missing data and won't have any use to our analysis. So I will drop them.
mobility_ir_pt.tail(100) #All the columns contain data that can be useful so I won't drop them


cases_ir_pt = cases_ir_pt.dropna(axis='columns') #dropping all columns where values where NaN

#Now let's join the 2 datasets using the country and date as key's.
cases_mob = pd.merge(cases_ir_pt, mobility_ir_pt,
                  left_on = ['country_region', 'last_update'],
                  right_on = ['country', 'date'],
                  how ='left')
#Mobility data is only available from 15/02 until 11/04 inner join could be more useful to compare the two datasets
cases_mob_inner = pd.merge(cases_ir_pt, mobility_ir_pt,
                  left_on = ['country_region', 'last_update'],
                  right_on = ['country', 'date'],
                  how ='inner')

#Creating pivot table to better compare data from two countries
pivot_confirmed = pd.pivot_table(cases_mob, values='confirmed', index=['last_update'], columns = 'country_region') 
pivot_deaths = pd.pivot_table(cases_mob, values='deaths', index=['last_update'], columns = 'country_region')

#I will start to create some plots for visualization of the data starting from the pivot tables
plt.close('all')
pivot_confirmed.plot()
pivot_deaths.plot()

ax = plt.gca()
cases_mob_inner.plot(kind='line', x='last_update', y='delta_confirmed',ax=ax)
