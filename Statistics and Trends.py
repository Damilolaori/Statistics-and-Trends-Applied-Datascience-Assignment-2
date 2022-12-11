# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 16:52:38 2022

@author: HI
"""

# importing neccesary libraries for the data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns



#define functions for reading and transposing data
def read_data_excel(excel_url, sheet_name, new_columns, countries):
    data_electricity = pd.read_excel(excel_url, skiprows=3)
    data_electricity = data_electricity[new_columns]
    data_electricity = data_electricity.loc[countries]
    data_electricity = data_electricity.set_index('Country Name', inplace=True)
    
    return data_electricity, data_electricity.transpose()


# parameters for reading data
excel_url = ('https://api.worldbank.org/v2/en/indicator/EG.ELC.ACCS.ZS?downloadformat=excel')
sheet_name = 'Data'
data_electricity = pd.read_excel(excel_url, skiprows=3)
countryFilter = ['Angola', 
                 'United States', 
                 'Nigeria', 
                 'China', 
                 'India', 
                 'Ghana', 
                 'South Africa']
columnFilter = ['Country Name', 
                '2000', 
                '2003', 
                '2006', 
                '2009', 
                '2012', 
                '2015', 
                '2018']
data_electricity = pd.DataFrame(data_electricity[data_electricity['Country Name'].isin(countryFilter)], columns = columnFilter).transpose()
#data_electricity = data_electricity.rename(columns=data_electricity.iloc[0]).drop(data_electricity.index[0])
data_electricity, data_electricity.columns = data_electricity[1:], data_electricity.iloc[0]
print(data_electricity)

# Defining functions for the multiple line plot
def multiple_plot(x_data, y_data, xlabel, title, labels, colors):
    """
    function defines a multiple line plot which attributes are discussed below:
    x_data: states the index which represents the years of the indicators
    y_data: states the countries of the indicators
    x_label: indicates the label of the X_axis
    title: shows the title of the plot
    labels: specific labels of each line plots displayed by the legend function
    colors: color of each line plots
    """    
    
    plt.figure(figsize = (12,9))
    plt.title(title, fontsize=20)
    for i in range(len(y_data)):
        plt.plot(x_data, y_data[i], label = labels[i], color = colors[i])
    plt.xlabel(xlabel, fontsize=20)
    plt.legend(bbox_to_anchor=(1.02, 1))
    plt.show()
    
    
#parameters to produce multiple plots for Access to Electricity (% of Population)
x_data = data_electricity.index
y_data = [data_electricity['South Africa'],
         data_electricity['China'],
         data_electricity['Angola'],
         data_electricity['Ghana'],
         data_electricity['India'],
         data_electricity['Nigeria'],
         data_electricity['United States']]
xlabel = 'Year'
labels = ['South Africa', 
          'China', 
          'Angola', 
          'Ghana', 
          'India', 
          'Nigeria', 
          'United States']
colors = ['red', 'blue', 'green', 'black', 'purple', 'pink', 'orange']
title = 'Access to Electricity (% of Population)'
multiple_plot(x_data, y_data, xlabel, title, labels, colors)  


#define functions for reading and transposing data
def read_data_excel(excel_url, sheet_name, new_columns, countries):
    data_urbanpop = pd.read_excel(excel_url, sheet_name=sheet_name, skiprows=3)
    data_urbanpop = data_urbanpop[new_columns]
    data_urbanpop = data_urbanpop.loc[countries]
    data_urbanpop = data_urbanpop.set_index('Country Name', inplace=True)
    
    return data_urbanpop, data_urbanpop.transpose()

# parameters for reading data
excel_url = ('https://api.worldbank.org/v2/en/indicator/SP.URB.TOTL.IN.ZS?downloadformat=excel')
sheet_name = 'Data'
data_urbanpop = pd.read_excel(excel_url, sheet_name=sheet_name, skiprows=3)
countryFilter = ['Angola', 
                 'United States', 
                 'Nigeria', 
                 'China', 
                 'India', 
                 'Ghana', 
                 'South Africa']
columnFilter = ['Country Name', 
                '2000', 
                '2003', 
                '2006', 
                '2009', 
                '2012', 
                '2015', 
                '2018']
data_urbanpop = pd.DataFrame(data_urbanpop
                             [data_urbanpop['Country Name'].isin(countryFilter)], 
                             columns = columnFilter).transpose()
#data_urbanpop = data_urbanpop.rename(columns=data_urbanpop.iloc[0]).drop(data_urbanpop.index[0])
data_urbanpop, data_urbanpop.columns = data_urbanpop[1:], data_urbanpop.iloc[0]
print(data_urbanpop)


 # Defining functions for the multiple line plot
def multiple_plot(x_data, y_data, xlabel, title, labels, colors):
    """
    function defines a multiple line plot which attributes are discussed below:
    x_data: states the index which represents the years of the indicators
    y_data: states the countries of the indicators
    x_label: indicates the label of the X_axis
    title: shows the title of the plot
    labels: specific labels of each line plots displayed by the legend function
    colors: color of each line plots
    
    """
    
    
    plt.figure(figsize = (12,9))
    plt.title(title, fontsize=20)
    for i in range(len(y_data)):
        plt.plot(x_data, y_data[i], label = labels[i], color = colors[i])
    plt.xlabel(xlabel, fontsize=20)
    plt.legend(bbox_to_anchor=(1.02, 1))
    plt.show()


# parameters to produce multiple plots for Urban Population (% of total Population)
x_data = data_urbanpop.index
y_data = [data_urbanpop['South Africa'],
         data_urbanpop['China'],
         data_urbanpop['Angola'],
         data_urbanpop['Ghana'],
         data_urbanpop['India'],
         data_urbanpop['Nigeria'],
         data_urbanpop['United States']]
xlabel = 'Year'
labels = ['South Africa', 
          'China', 
          'Angola', 
          'Ghana', 
          'India', 
          'Nigeria', 
          'United States']
colors = ['red', 'blue', 'green', 'black', 'purple', 'pink', 'orange']
title = 'Urban Population (% of total Population)'
multiple_plot(x_data, y_data, xlabel, title, labels, colors) 



# define functions for reading and transposing data
def read_data_excel(excel_url, sheet_name, new_columns, countries):
    data_agric = pd.read_excel(excel_url, sheet_name=sheet_name, skiprows=3)
    data_agric = data_agric[new_columns]
    data_agric = data_agric.loc[countries]
    data_agric = data_agric.set_index('Country Name', inplace=True)
    
    return data_agric, data_agric.transpose()

# parameters for reading data
excel_url = ('https://api.worldbank.org/v2/en/indicator/NV.AGR.TOTL.ZS?downloadformat=excel')
sheet_name = 'Data'
data_agric = pd.read_excel(excel_url, sheet_name=sheet_name, skiprows=3)
countryFilter = ['Angola', 
                 'United States', 
                 'Nigeria', 
                 'China', 
                 'India', 
                 'Ghana', 
                 'South Africa']
columnFilter = ['Country Name', 
                '2000', 
                '2003', 
                '2006', 
                '2009', 
                '2012', 
                '2015', 
                '2018']
data_agric = pd.DataFrame(data_agric
                          [data_agric['Country Name'].isin(countryFilter)], 
                          columns = columnFilter).transpose()
#data_agric = data_agric.rename(columns=data_agric.iloc[0]).drop(data_agric.index[0])
data_agric, data_agric.columns = data_agric[1:], data_agric.iloc[0]
print(data_agric)

# parameters to produce grouped barplots for Agriculture, forestry, and fishery, value added (% of GDP)
data_agric.plot(kind='bar')
plt.title('Agriculture, forestry, and fishing, value added (% of GDP)')
plt.xlabel('Years')
plt.ylabel('Agriculture')
plt.rcParams["figure.dpi"] = 1000
plt.legend(loc= "upper right")
plt.figure(figsize=(8, 6))
plt.show()


#define functions for reading and transposing data
def read_data_excel(excel_url, sheet_name, new_columns, countries):
    data_CO2 = pd.read_excel(excel_url, sheet_name=sheet_name, skiprows=3)
    data_CO2 = data_CO2[new_columns]
    data_CO2 = data_CO2.loc[countries]
    data_CO2 = data_CO2.set_index('Country Name', inplace=True)
    
    return data_CO2, data_CO2.transpose()

# parameters for reading
excel_url = ('https://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.KT?downloadformat=excel')
sheet_name = 'Data'
data_CO2 = pd.read_excel(excel_url, sheet_name=sheet_name, skiprows=3)
countryFilter = ['Angola', 'United States', 'Nigeria', 'China', 'India', 'Ghana', 'South Africa']
columnFilter = ['Country Name', '2000', '2003', '2006', '2009', '2012', '2015', '2018']
data_CO2 = pd.DataFrame(data_CO2[data_CO2['Country Name'].isin(countryFilter)], columns = columnFilter).transpose()
#data = data.rename(columns=data.iloc[0]).drop(data.index[0])
data_CO2, data_CO2.columns = data_CO2[1:], data_CO2.iloc[0]
print(data_CO2)

# parameters to produce grouped barplots for CO2 Emissions (kt)
data_CO2.plot(kind='bar')
plt.title('CO2 Emissions (kt)')
plt.xlabel('Years')
plt.ylabel('CO2 Emissions')
plt.rcParams["figure.dpi"] = 1000
plt.legend(loc= "upper left")
plt.figure(figsize=(8, 6))
plt.show()

# creating a dataframe for china to calculate correlation
china = pd.DataFrame(
{'Urban Population': data_urbanpop['China'].astype(float),
'Co2 emission': data_CO2['China'].astype(float),
'Elec. Access': data_electricity['China'].astype(float),
'Agriculture': data_agric['China'].astype(float)})
print(china)

# correlation for china
corr_china= china.corr()
print(corr_china)

# heatmap showing the correlation for china using the indicators
plt.figure(figsize=(8,5))
sns.heatmap(china.corr(),annot=True,cmap='Reds')
plt.title('Correlation heatmap China')
plt.show()

# importing a necessary library to get the p-value
from scipy import stats

corr_china= pd.DataFrame(columns=['r', 'p'])
for col in china:
    if pd.api.types.is_numeric_dtype(china[col]) and not '':
        r, p = stats.pearsonr(china['Urban Population'], china[col])
        corr_china.loc[col] = [round(r,3), round(p,3)]
print(corr_china)

# creating a dataframe for Nigeria to calculate correlation
nigeria = pd.DataFrame(
{'Urban Population': data_urbanpop['Nigeria'].astype(float),
'Co2 emission': data_CO2['Nigeria'].astype(float),
'Elec. Access': data_electricity['Nigeria'].astype(float),
'Agriculture': data_agric['Nigeria'].astype(float)})
print(nigeria)

# correlation for Nigeria
corr_nigeria = nigeria.corr()
print(corr_nigeria)

# heatmap showing the correlation for Nigeria using the indicators
plt.figure(figsize=(8,5))
sns.heatmap(nigeria.corr(),annot=True,cmap='Greens')
plt.title('Correlation heatmap Nigeria')
plt.show()

corr_nigeria= pd.DataFrame(columns=['r', 'p'])
for col in nigeria:
    if pd.api.types.is_numeric_dtype(nigeria[col]) and not '':
        r, p = stats.pearsonr(china['Urban Population'], nigeria[col])
        corr_nigeria.loc[col] = [round(r,3), round(p,3)]
print(corr_nigeria)

