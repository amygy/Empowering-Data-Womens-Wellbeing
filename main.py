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

oneCountryBooleanList = lwd["country_name"] == "India"

oneCountryData = lwd.loc[oneCountryBooleanList]

# Print out the number of rows and columns
print(oneCountryData.shape)

#  basic colors:
# 'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white'

# create a scatter plot
# ER_elec_rural_p = Households in rural areas with access to electricity (%)
plt.scatter(oneCountryData["year"],oneCountryData["ER_elec_rural_p"],color="red")

# add a title to the plot
plt.title("Percent of Households in Rural Areas with Access to Electricity")

#Label the x-axis
plt.xlabel("Year")

# label the y-axis
plt.ylabel("Households in rural areas with access to electricity (%)")

# set the range for the y-axis
plt.ylim(0,100)

# show the plot
plt.show()
