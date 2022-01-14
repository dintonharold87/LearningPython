import pandas as pd

# Read data from the data file(csv file)
#  use the pd.read_csv() function to read the data into a DataFrame
data=pd.read_csv('IMDB-Movie-Data.csv')
print(data.head())

# Read data with specific explicit index

#This means we include the title of the file as we read the data
"""  For example, you can see in this dataset that the CSV file has a built-in index, which pandas did not pick up on automatically. To make pandas use that column for the index (instead of creating a new one from scratch), we can specify an index_col. """
indexed_data=pd.read_csv('IMDB-Movie-Data.csv',index_col='Title')

# view data from the source
# head method gives you the first five rows of the data
print(indexed_data.head())

# tail method gives you the last five rows of the data
print(data.tail())

# View the information about the datatypes

print(data.info())

# view the structure of the file
# We can use the shape attribute to check how large the resulting DataFrame is:
# Tells you how many records we have and the number of columns
# print(data.shape)

# view the statistical summary of the data in the filename
print(data.describe())

# Getting a data serie from the data frame
# print(data["Rating"])

#Getting more than one column from the data frame
# print(data[['Rating','Year','Votes','Metascore','Rank']])

""" STEP 6------Indexing, Selecting & Assigning """
""" HOW TO ACCESS ROWS / SPECIFIC ROWS WE WANT FROM OUR DATA
We use loc and iloc methods to achieve this.
Selection by Label
Rows can be selected by passing row label to a loc function.
Selection by index-based location
Rows can be selected by passing index location to an iloc function. """
# We are focusing on the row Suicide squad, to get it's genre,rating, year of release and revenue.

# loc- we are accessing the row using the actual title of the row
""" Label-based selection
The second paradigm for attribute selection is the one followed by the loc operator: label-based selection. In this paradigm, it's the data index value, not its position, which matters. """
suicideSquadRow=indexed_data.loc[["Suicide Squad"]][["Genre",'Rating','Year','Revenue (Millions)']]
print(suicideSquadRow)

# iloc(index location)
# Both loc and iloc are row-first, column-second. This is the opposite of what we do in native Python, which is column-first, row-second.
data.iloc[10:15][['Title','Director','Rating','Year','Revenue (Millions)']]


""" STEP 7---DATA SELECTION 
How we can filter our data """

# Getting data from the year between 2010 and 2011 with a rating less than 6
yearBetween=data[((data['Year']>=2010)&(data['Year']<=2011)&(data['Rating']< 6.0))]
print(yearBetween)

# GROUP BY OPERATION ON THE DATA
""" Any groupby operation involves one of the following operations on the original object. They are −

Splitting the Object

Applying a function

Combining the results

In many situations, we split the data into sets and we apply some functionality on each subset. In the apply functionality, we can perform the following operations −

Aggregation − computing a summary statistic

Transformation − perform some group-specific operation

Filtration − discarding the data with some condition

Split Data into Groups
Pandas object can be split into any of their objects. There are multiple ways to split an object like −

obj.groupby('key')
obj.groupby(['key1','key2'])
obj.groupby(key,axis=1) """
# first five rows but not in ord
directorData=data.groupby('Director')[['Rating']].mean().head()
print(directorData)

# min average(rating) of each director{last five rows}
averageData=data.groupby('Director')[['Rating']].min().tail()
print(averageData)

# SORTING OPERATIONS ON OUR DATA
""" There are two kinds of sorting available in Pandas. They are −

By label
By Actual Value
By LABEL
Using the sort_index() method, by passing the axis arguments and the order of sorting, DataFrame can be sorted. By default, sorting is done on row labels in ascending order. 

Order of Sorting
By passing the Boolean value to ascending parameter, the order of the sorting can be controlled.

Sort the Columns
By passing the axis argument with a value 0 or 1, the sorting can be done on the column labels. By default, axis=0, sort by row. Let us consider the following example to understand the same."""
# sorted data of the last five rows of the directors with the least rating in descending order
sorted_data=data.groupby('Director')[['Rating']].mean().sort_values(['Rating'],ascending=False).tail()
print(sorted_data)

""" DEALING WITH MISSING VALUES IN YOUR DATASET """

# Finding out which columns have some missing values 
""" sum()
Returns the sum of the values for the requested axis. By default, axis is index (axis=0) """
print(data.isnull().sum())

""" STEP-8 DROPPING ROWS WITH NULL VALUES 
This can be achieved using two methods
first method:drop method
this ignores the column,inplace=True deletes the column temporarily

second method:dropna method"""

# dropping the Metascore column
# DataFrame − “index” (axis=0, default), “columns” (axis=1)
print(data.drop('Metascore',axis=1).head())

#  This deletes all columns with missing values and null values
# print(data.dropna('Metascore',axis=1))

# To delete rows with missing values and null values
# data.dropna()


meanRevenue=indexed_data['Revenue (Millions)'].mean()
print("The mean revenue is:",meanRevenue)

""" step 9-handle missing values in the revenue coulumn.
The fillna function can “fill in” NA values """
indexed_data['Revenue (Millions)'].fillna(meanRevenue,inplace=True)

# Pandas provides the isnull() and notnull() functions, which are also methods on Series and DataFrame objects to Check for Missing Values 
print(indexed_data.isnull().sum())
