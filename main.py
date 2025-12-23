# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("livwell135.csv")

# Print out the number of rows and columns
print(lwd.shape)

#  basic colors:
# 'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white'

# create a scatter plot
plt.scatter(lwd["year"],lwd["ED_litt_p"],color="red")

# add a title to the plot
plt.title("Percent of Women Who are Literate over Time")

#Label the x-axis
plt.xlabel("Year")

# label the y-axis
plt.ylabel("Women who are literate (%)")

# set the range for the y-axis
plt.ylim(0,14)

# show the plot
plt.show()
