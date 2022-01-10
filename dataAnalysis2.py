""" A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.

Features of DataFrame
-Potentially columns are of different types
-Size – Mutable(can be changed)
-Labeled axes (rows and columns)
-Can Perform Arithmetic operations on rows and columns 
pandas.DataFrame
A pandas DataFrame can be created using the following constructor −

pandas.DataFrame( data, index, columns, dtype, copy) """
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