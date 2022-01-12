import pandas as pd

# Read data from the data file(csv file)
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

""" Indexing, Selecting & Assigning """
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


""" DATA SELECTION 
How we can filter our data """

# Getting data from the year between 2010 and 2011
yearBetween=data[((data['Year']>=2010)&(data['Year']<=2011))]
print(yearBetween)
