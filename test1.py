# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 10:55:13 2020

@author: z00461cr

""" 
"""This function is used to detect outliers based on statistical approach by forming clusters and finding the distance between clusters """

import pandas as pd
import numpy as np
import hdf5storage
import datetime
from matplotlib import pyplot as plt


import seaborn as sns
sns.set()

matlab_to_python = hdf5storage.loadmat('C:/UserData/Z00461CR/Documents/DataAdlershof/5. DataForAnalysis/LoadedData_20170609T100716_20200109T225953Table.mat')


dictionary_to_array = np.array(matlab_to_python['#subsystem#'])
                                                
number_of_columns = (dictionary_to_array[0][0][0][7][0].shape)[0]

nestedlist_for_columnnames = []
for each_columnname in range(number_of_columns):
    nestedlist_for_columnnames.append(dictionary_to_array[0][0][0][7][0][each_columnname]) # Retrieving column names 
    
nestedlist_to_list =[columnname[0] for eachname in nestedlist_for_columnnames for columnname in eachname]  #Retrieving column names from nested list to list

#Creating a DataFrame

df = pd.DataFrame()

for k in range(number_of_columns):
    each_column_data =[dictionary_to_array[0][0][0][2][0][k][eachdate][0] for eachdate in range((dictionary_to_array[0][0][0][2][0][k].shape)[0])]
    df.insert(k,nestedlist_to_list[k],each_column_data)
    
df['ColumnTime'] = df['ColumnTime'].astype(str)

df['ColumnTime'] = pd.to_datetime(df['ColumnTime'])



plt.hist(df['C_Geb1952_Mtr01_Pwr'], bins = 160)
plt.yscale('log')
plt.xlim([0, 76])
plt.xticks(np.arange(0, 76, 5))
#plt.xticks(range(0, 76, 0.2))
plt.show()

No_of_datapoints_in_each_bin, edges = np.histogram(df['C_Geb1952_Mtr01_Pwr'],bins=160,density=False)
print(No_of_datapoints_in_each_bin)


l=np.where(No_of_datapoints_in_each_bin==0)
clusters_list = []
clusters_list.append(l[0][0]*0.47)  # First Starting Point
for i in range(1,len(l[0])):
    
    if(l[0][i] - l[0][i-1] >1):
        end_point = (l[0][i-1]+1)*0.47
        start_point = (l[0][i]*0.47)
        clusters_list.append(end_point)
        clusters_list.append(start_point)
clusters_list.append(l[0][-1]*0.47)    #Last Ending point
   
print(clusters_list)

difference_between_clusters = []
for each_point in range(0,len(clusters_list)-1, 2):
    difference_between_clusters.append(clusters_list[each_point + 1] - clusters_list[each_point])
    



threshold_value = 0.3917
error_mask = df['C_Geb1952_Mtr01_Pwr']


for i in range(1, len(clusters_list)-1, 2):
    if (clusters_list[i+1] - clusters_list[i]) > threshold_value:
        start_index = clusters_list[i]
        end_index =   clusters_list[i+1]
        error_mask = error_mask.mask(error_mask.between(start_index, end_index), -1)


df[df['C_Geb1952_Mtr01_Pwr'] > 50 ].index.values

print(df['C_Geb1952_Mtr01_Pwr'][2761845])

print(error_mask[2813687])

error_mask = df['C_Geb1952_Mtr01_Pwr']

print(error_mask[2891440])



temp_df = pd.DataFrame()

temp_df['ColumnTime'] = df['ColumnTime']
temp_df['C_Geb1952_Mtr01_Pwr'] = df['C_Geb1952_Mtr01_Pwr']

temp_df['value_grp'] = (temp_df.C_Geb1952_Mtr01_Pwr.diff(1) != 0).astype('int').cumsum()
error_df = pd.DataFrame({'BeginDate' : temp_df.groupby('value_grp').ColumnTime.first(), 
              'EndDate' : temp_df.groupby('value_grp').ColumnTime.last(),
              'Consecutive' : temp_df.groupby('value_grp').size(), 
              'C_Geb1952_Mtr01_Pwr' : temp_df.groupby('value_grp').C_Geb1952_Mtr01_Pwr.first()}).reset_index(drop=True)
    

    
error_df.drop(error_df[error_df.Consecutive == 1].index, inplace = True)
error_df.drop(error_df[error_df.C_Geb1952_Mtr01_Pwr == 0].index, inplace = True)



plt.hist(error_df['C_Geb1952_Mtr01_Pwr'], bins = 160)
plt.show()
hist, edges = np.histogram(error_df['C_Geb1952_Mtr01_Pwr'],bins=160,density=False)
print(hist)