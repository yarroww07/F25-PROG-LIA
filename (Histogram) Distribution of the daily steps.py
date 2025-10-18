# Meriem
# Description: Distribution of the daily steps taking by the sampled indivifuals, in order to understand their activity level.
import pandas as pd
import matplotlib.pyplot as plt

Sleep_Data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

#Variables
x = Sleep_Data["Daily Steps"]

#Plotting the histogram
plt.figure(figsize = (12,6))
plt.hist(x, color = "purple")
plt.title('Daily Step distribution')
plt.xlabel('Daily steps ')
plt.ylabel('Count') #Number of individuals who did the daily steps 
plt.tight_layout()
plt.show()
 