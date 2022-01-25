import pandas as pd
from matplotlib import pyplot as plt

# Reading data from the csv file into a dataframe
# avocado_data = pd.read_csv('avocado.csv')
# print(avocado_data)

# Using the shape attribute to  check how large the resulting DataFrame is
# print(avocado_data.shape)

indexed_avocado_data =pd.read_csv('avocado.csv',index_col=0)
print(indexed_avocado_data)

# View the information about the datatypes

print(indexed_avocado_data.info())
print(indexed_avocado_data.index)
# Finding out which columns have some missing values 
print(indexed_avocado_data.isnull().sum())

#Year with the smallest average revenue
least_average_revenue=indexed_avocado_data.groupby('year')[['Total Volume']].mean().sort_values(['Total Volume'])

print(least_average_revenue)

# Year with highest average price 
highest_average_price=indexed_avocado_data.groupby('year')[['AveragePrice']].max().sort_values(['AveragePrice'],ascending=False)
print(highest_average_price)

# least consumed avocado type
least_consumed_type=indexed_avocado_data.groupby('type')[['Total Bags']].sum().sort_values(['Total Bags'])
print(least_consumed_type)

# least consuming region
least_consuming_region=indexed_avocado_data.groupby(['region'])[['Total Bags']].sum().sort_values(['Total Bags'])
print(least_consuming_region)

#pie chart represent the  avocado category interms of price

#setting the data to start with date as its index
# indexed_avocado_data = indexed_avocado_data.set_index('type')
# data_frame=indexed_avocado_data['AveragePrice']
# print(my_data)
# The figure() function in pyplot module of matplotlib library is used to create a new figure.
# figsize(float, float): These parameter are the width, height in inches.
# fig = plt.figure(figsize =(10, 7))
# plt.pie(data_frame,explode=None)
# plt.show()

# indexed_avocado_data = indexed_avocado_data.set_index('region')
data_frame=indexed_avocado_data[['Small Bags', 'Large Bags','XLarge Bags','region','type','year','Total Volume']]
# scatter plot

data_frame.plot(kind='scatter',x='type',y='Small Bags')
# line plot
data_frame.plot(kind='line',x='region',y='Large Bags')
# bar plot
data_frame.plot(kind='bar',x='year',y='XLarge Bags')
# Area plot
data_frame.plot(kind='area',x='region',y='Total Volume')
plt.show()