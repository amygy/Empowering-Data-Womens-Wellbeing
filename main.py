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

# Create a figure with 2 subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# ER_elec_rural_p = Households in rural areas with access to electricity (%)

# SUBPLOT 1: Scatter plot
ax1.scatter(oneCountryData["year"], oneCountryData["ER_elec_rural_p"], color="red", s=50)
ax1.set_title("Households in rural areas with access to electricity (Over Time)")
ax1.set_xlabel("Year")
ax1.set_ylabel("Electricity Access (%)")
ax1.set_ylim(0, 100)
ax1.grid(True, alpha=0.3)

# SUBPLOT 2: Histogram
ax2.hist(oneCountryData["ER_elec_rural_p"], edgecolor='white', bins=8, color='blue', alpha=0.7)
ax2.set_title("Distribution of Electricity Access")
ax2.set_xlabel("Electricity Access (%)")
ax2.set_ylabel("Frequency")
ax2.grid(True, alpha=0.3, axis='y')

# Adjust layout to prevent overlap
plt.tight_layout()

# Save the plot
plt.savefig('electricity_access_plot.png', dpi=100, bbox_inches='tight')
print("Plot saved as electricity_access_plot.png")
plt.show()
