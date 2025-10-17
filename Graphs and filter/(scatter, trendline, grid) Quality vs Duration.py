# SUMMARY OF THE FILE
# Author: Rania Bouladraf
# Contains: Scatter plot with a trendline



# Imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
Sleep_Data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

# Variables
duration = Sleep_Data['Sleep Duration']
quality = Sleep_Data['Quality of Sleep']

# Trendline
m, b = np.polyfit(duration, quality, 1)
plt.plot(duration, m*duration + b, color='burlywood', linestyle='dotted')

# Graph
plt.title('Relationship Between Sleep Duration and Sleep Quality')
plt.xlabel('Sleep Duration')
plt.ylabel('Sleep Quality')
plt.scatter(duration, quality, color='seagreen')
plt.grid()
plt.show()