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