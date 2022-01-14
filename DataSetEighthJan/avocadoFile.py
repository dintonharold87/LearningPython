import pandas as pd

# Reading data from the csv file into a dataframe
avocado_data = pd.read_csv('avocado.csv')
print(avocado_data)

# Using the shape attribute to  check how large the resulting DataFrame is
print(avocado_data.shape)

# To make pandas use that column for the index (instead of creating a new one from scratch), we can specify an index_col.
indexed_avocado_data =pd.read_csv('avocado.csv',index_col=0)
print(indexed_avocado_data)

# view the summary of statistics pertaining to the DataFrame columns.
""" 'include' is the argument which is used to pass necessary information regarding what columns need to be considered for summarizing. Takes the list of values; by default, 'number'.

object − Summarizes String columns
number − Summarizes Numeric columns
all − Summarizes all columns together (Should not pass it as a list value) """
print(indexed_avocado_data.describe(include='all'))

# View the information about the datatypes

print(indexed_avocado_data.info())

# view information from only Total bags of avocado(one column)
print(indexed_avocado_data['Total Bags'])

#view information of Total bags of avocado, small bags and large bags Only(more than one column)
print(indexed_avocado_data[['Total Bags','Small Bags','Large Bags']])

# View information of a specific row using Index-based selection
# in this case we are interested in the the row with index of 3 and column of index 6
print(indexed_avocado_data.iloc[3,6])
print(indexed_avocado_data.iloc[3]['Total Bags'])

""" View information of specific rows in a specific column """
print(indexed_avocado_data.iloc[3:12,6])
print(indexed_avocado_data.iloc[3:12]['Total Bags'])

""" View information of specific rows in  specific columns """
print(indexed_avocado_data.iloc[3:12][['Total Bags','Small Bags','Large Bags','XLarge Bags']])

"""  View information of a specific row using Label-based selection """
# viewing information of the first five rows with an index of 3 and 4

print(indexed_avocado_data.loc[[3,4]][['Total Bags','Small Bags','Large Bags','XLarge Bags']].head())

# view information of the last five rows with an index of 12
print(indexed_avocado_data.loc[[12]][['Total Bags','Small Bags','Large Bags','XLarge Bags']].tail())

""" DATA SELECTION """

# Getting data about avocados in small bags less than 4000 and avocados in large bags less than 100 and they have a type of organic
print(indexed_avocado_data[((indexed_avocado_data['Small Bags']>8000)&(indexed_avocado_data['Large Bags']<100)&(indexed_avocado_data['type']=='organic'))])

# Getting data about avocados in the region HartfordSpringfield of conventional type and in large bags greater than 100
print(indexed_avocado_data[((indexed_avocado_data['region']=="HartfordSpringfield")&(indexed_avocado_data['Large Bags']<100)&(indexed_avocado_data['type']=='conventional'))])

""" GROUP BY OPERATION """
# Getting the data about average number of avocados in large bags in each region
print(indexed_avocado_data.groupby('region')['Large Bags'].mean())

# Getting data about maximum total bags of avocados collected in each region in each year

print(indexed_avocado_data.groupby(['region','year'])['Total Bags'].max())

# print(indexed_avocado_data.loc[indexed_avocado_data['Large Bags'].isnull()])

# Finding out which columns have some missing values 
# print(indexed_avocado_data.isnull().sum())