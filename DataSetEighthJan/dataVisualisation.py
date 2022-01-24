# import os
# os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "D:/anaconda stuff/Library/plugins/platforms"

import pandas as pd
""" Visualization with Matplotlib
Matplotlib is easy to use and an amazing visualizing library in Python. It is built on NumPy arrays and designed to work with the broader SciPy stack and consists of several plots like line, bar, scatter, histogram, etc.  """
""" Pyplot
Pyplot is a Matplotlib module that provides a MATLAB-like interface. Pyplot provides functions that interact with the figure i.e. creates a figure, decorates the plot with labels, creates plotting area in a figure.
 """

# Python program to show pyplot module
import matplotlib.pyplot as plt
  
# Python program to show pyplot module

""" The plot function marks the x-coordinates(1, 2, 3, 4) and y-coordinates(1, 4, 9, 16) in a linear graph with specified scales. [/caption] """
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
""" zero to six on the x axis 
and 0 to 20 on the y axis"""
# plt.axis([0, 6, 0, 20])
"Display the graph"
# plt.show()
""" 
Parameters: This function accepts parameters that enables us to set axes scales and format the graphs. These parameters are mentioned below :-

plot(x, y): plot x and y using default line style and color.
plot.axis([xmin, xmax, ymin, ymax]): scales the x-axis and y-axis from minimum to maximum values
plot.(x, y, color=’green’, marker=’o’, linestyle=’dashed’, linewidth=2, markersize=12): x and y co-ordinates are marked using circular markers of size 12 and green color line with — style of width 2
plot.xlabel(‘X-axis’): names x-axis
plot.ylabel(‘Y-axis’): names y-axis 
plot(x, y, label = ‘Sample line ‘) plotted Sample Line will be displayed as a legend"""
#####################################
movie_data=pd.read_csv('IMDB-Movie-Data.csv')
indexed_data =pd.read_csv('IMDB-Movie-Data.csv',index_col="Title")
print(movie_data[['Revenue (Millions)']])


visualOne=movie_data[['Revenue (Millions)','Title','Rating']]
print(visualOne)

""" We can plot one column versus another using the x and y keywords.

Plotting methods allow a handful of plot styles other than the default line plot. These methods can be provided as the kind keyword argument to plot(). These include −

bar or barh for bar plots
hist for histogram
box for boxplot
'area' for area plots
'scatter' for scatter plots """

visualOne.plot(kind='scatter',x='Title',y='Revenue (Millions)')
# visualOne.plot(kind='line', color= 'Red',y='Rating',ax=ax)
plt.show()
print(movie_data.info())

print(movie_data[['Director']])
slicedSsr=movie_data.iloc[[0]][['Title','Revenue (Millions)']]
print(slicedSsr)

