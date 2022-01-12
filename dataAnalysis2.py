""" A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.

Features of DataFrame
-Potentially columns are of different types
-Size – Mutable(can be changed)
-Labeled axes (rows and columns)
-Can Perform Arithmetic operations on rows and columns 
pandas.DataFrame
A pandas DataFrame can be created using the following constructor −

pandas.DataFrame( data, index, columns, dtype, copy)
1	
data

data takes various forms like ndarray, series, map, lists, dict, constants and also another DataFrame.

2	
index

For the row labels, the Index to be used for the resulting frame is Optional Default np.arange(n) if no index is passed.

3	
columns

For column labels, the optional default syntax is - np.arange(n). This is only true if no index is passed.

4	
dtype

Data type of each column.

5	
copy

This command (or whatever it is) is used for copying of data, if the default is False. """
import pandas as pd
# Saturday 8th Jan

myMarks=pd.Series([78,80,87,80,90],index=['PHY','ECON','MTC','GP','ICT'])
print('Marks obtained by the student are',myMarks)

dtMarks=pd.DataFrame(myMarks,columns=['Student one'])
print('The marks for student one are \n',dtMarks)

heights=pd.Series([5.7,5.1,5.0,5.6],index=['Devin','Dionne','Denise','Dinton'])
weight=pd.Series([65,45,65,65],index=['Devin','Dionne','Denise','Dinton'])
dfPerson=pd.DataFrame({'Height':heights,'Weight':weight})
print('The personal details are: \n',dfPerson)



d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 
   'three' : pd.Series([10,20,30], index=['a','b','c'])}

df = pd.DataFrame(d)
print ("Our dataframe is:")
print (df)
print(d['one'])

# using del function
print ("Deleting the first column using DEL function:")
del df['one']
print (df)

# using pop function
print ("Deleting another column using POP function:")
df.pop('two')
print (df)

""" In the cell below, write code to save this DataFrame to disk as a csv file with the name cows_and_goats.csv """
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
print(animals)
animals.to_csv('cows_and_goats.csv')
      