import pandas as pd
import matplotlib.pyplot as plt

Sleep_Data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
 
#DEFINING MY VARIABLES

x = Sleep_Data["Stress Level"]
y = Sleep_Data["Quality of Sleep"]
z = Sleep_Data["Sleep Duration"]


#GRAPHING

plt.scatter(x, y, color='purple', label = 'Quality of Sleep')
plt.scatter(x, z, color='red', label = 'Sleep Duration')

plt.title('Relationship Between Sleep Duration, Sleep Quality and Stress Level')
plt.xlabel('Stress Level')
plt.ylabel('Sleep Quality' and 'Sleep Duration')

plt.legend(title = 'Variables', loc = 'upper right')

