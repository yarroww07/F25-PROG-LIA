# Imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Variables
Sleep_Data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
duration = Sleep_Data['Sleep Duration']
quality = Sleep_Data['Quality of Sleep']

# Trendline
m, b = np.polyfit(duration, quality, 1)
plt.plot(duration, m*duration + b, color='red', linestyle='dotted')

# Graph
plt.title('Relationship Between Sleep Duration and Sleep Quality')
plt.xlabel('Sleep Duration')
plt.ylabel('Sleep Quality')
plt.scatter(duration, quality, color='purple')
plt.show()