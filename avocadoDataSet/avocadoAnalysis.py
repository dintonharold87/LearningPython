import pandas as pd
from matplotlib import pyplot as plt

# Reading data from the csv file into a dataframe
avocado_data = pd.read_csv('avocado.csv')
# print(avocado_data)

# Using the shape attribute to  check how large the resulting DataFrame is
# print(avocado_data.shape)

indexed_avocado_data =pd.read_csv('avocado.csv',index_col='region')
print(indexed_avocado_data)

# View the information about the datatypes

print(indexed_avocado_data.info())
# print(indexed_avocado_data.index)
# Finding out which columns have some missing values 
print(indexed_avocado_data.isnull().sum())

#Year with the smallest average revenue
indexed_avocado_data['Average Revenue']=indexed_avocado_data['AveragePrice']/ indexed_avocado_data['Total Bags']

least_average_revenue=indexed_avocado_data.groupby('year')[['Average Revenue']].min().sort_values(by='Average Revenue')
# least_average_revenue=indexed_avocado_data.groupby('year')[['Total Volume']].mean().sort_values(by='Total Volume')

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


data_frame=indexed_avocado_data[['AveragePrice','type']]

# The figure() function in pyplot module of matplotlib library is used to create a new figure.
#figsize(float, float): These parameter are the width, height in inches.
#fig = plt.figure(figsize =(5,5))
avocado_type_data=data_frame.groupby('type')
#print(organic_data)
labels=['conventional','organic']
values=avocado_type_data['AveragePrice'].mean()
explode=[0.05,0.0]
colors = [ "orange", "green"]
plt.pie(values,labels=labels,autopct='%.1f%%',explode=explode,colors=colors)
plt.show()


# # indexed_avocado_data = indexed_avocado_data.set_index('region')
data_frame=avocado_data[['Small Bags', 'Large Bags','XLarge Bags','region','type','year','Total Volume']]
# # scatter plot

#data_frame.plot(kind='scatter',x='type',y='Small Bags')
# # line plot to show the large bag
#data_frame.plot(kind='line',x='year',y='Large Bags')
# # bar plot to show the total volume of avocados produced each year
data_frame.plot(kind='bar',x='year',y='Total Volume')
# # Area plot to show total volume produced by each region
#data_frame.plot(kind='area',x='region',y='Total Volume')
plt.show()