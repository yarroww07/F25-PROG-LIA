import pandas as pd
import matplotlib.pyplot as plt

Sleep_Data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
print(Sleep_Data.head)
 
#DEFINING MY VARIABLES
x = Sleep_Data["Daily Steps"]
y = Sleep_Data["Sleep Quality"]

#GRAPHING
plt.scatter(x, y, color='darkmagenta', label = 'Quality of Sleep')

#TITLES
plt.title('Relationship Between Daily Steps and Sleep Quality')
plt.xlabel('Daily Steps')
plt.ylabel('Sleep Quality')