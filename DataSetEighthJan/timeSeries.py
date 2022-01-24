#Time series is a data set where values are measured at different points in time
import pandas as pd
import matplotlib.pyplot as plt

my_data = pd.read_csv("avocado.csv")
print(my_data.head(2))
#prints out the types of data in the columns of the DataFrame 
print(my_data.dtypes) 
""" there are occasions where you’ll need to convert data in a Series to another data type. If you’re planning to print a large number of value to the screen, for instance, it might be helpful to have those values as character strings. Data type conversions is most easily done using the astype() method.

In [21]: print(dataFrame['TEMP'].astype(str)) """

#changing the data type of date from integer to datetime
my_data['Date'] = pd.to_datetime(my_data['Date'])
print(my_data.dtypes)

#setting the data to start with date as its index
my_data = my_data.set_index('Date')
print(my_data)

my_dataframe = my_data[['AveragePrice','type','region']]
print(my_dataframe)

#printing out only values for 2015 december
print(my_dataframe.loc['2015-12'])

#kindly install seaborn using pip install seaborn on your command line - gives styling for graphs

my_dataframe['AveragePrice'].plot()


