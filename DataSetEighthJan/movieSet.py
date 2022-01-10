import pandas as pd

# Read data from the data file(csv file)
data=pd.read_csv('IMDB-Movie-Data.csv')

# Read data with specific explicit index

#This means we include the title of the file as we read the data
indexed_data=pd.read_csv('IMDB-Movie-Data.csv',index_col='Title')

# view data from the source
# head method gives you the first five rows of the data
print(data.head())

# tail method gives you the last five rows of the data
print(data.tail())

# View the information about the datatypes

print(data.info())

# view the structure of the file
print(data.shape)

# view the statistical summary of the data in the filename
print(data.describe())

# Getting a data serie from the data frame
print(data["Rating"])

#Getting more than one column from the data frame
print(data[['Rating','Year','Votes','Metascore','Rank']])