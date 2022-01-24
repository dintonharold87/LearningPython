import pandas as pd

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