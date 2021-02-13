import pandas as pd 
import matplotlib.pyplot as plt

# Creating Dataframe from Excel data
df = pd.read_excel('Livestock.xlsx')

# Defining which data to use
values = df[['Date', 'Total_Cattle', 'Total_Pigs']]
print(values)

# Plotting Chart Axis
ax = values.plot.bar(x='Date',y=['Total_Cattle', 'Total_Pigs'], rot=0)

# Axis Labels
ax.set_xlabel("Date")
ax.set_ylabel("Number in Thousand(s)")

plt.show()

