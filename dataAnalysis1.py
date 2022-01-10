""" Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.). The axis labels are collectively called index.

pandas.Series
A pandas Series can be created using the following constructor −
pandas.Series( data, index, dtype, copy)

The parameters of the constructor are as follows −
1
data

data takes various forms like ndarray, list, constants

2	
index

Index values must be unique and hashable, same length as data. Default np.arrange(n) if no index is passed.

3	
dtype

dtype is for data type. If None, data type will be inferred

4	
copy

Copy data. Default False 

A series can be created using various inputs like −

Array
Dict
Scalar value or constant"""
#import the pandas library and aliasing as pd
import pandas as pd
# Converting a list into a data serie
first_list=[10,20,30,40]
first_serie=pd.Series(first_list)
# A data serie is like a 2 dimensional array
print('The series values are :', first_serie.values)
print('The index values of the serie are:',first_serie.index.values)
second_serie=pd.Series(first_list,index=["Uganda",'Kenya','Tanzania','Rwanda'])
print('Drinking competition',second_serie)
serie_copy=second_serie[1:2]
print(serie_copy)
print(second_serie['Kenya'])
# converting a dictionary to a data serie
fruits={'apples':10,'bananas':20,'grapes':30,'pineapples':40,'watermelons':50,'kiwi':60,'pawpaws':70,}
third_series=pd.Series(fruits)
print('Fruits at home \n',third_series)
print('We have',third_series['pineapples'],'pineapples at home')

