#CORRELATION BETWEEN BMI CATEGORIES, SLEEP DURATION AND SLEEP QUALITY
#BY SARAH MEGHDIR
#SCATTER PLOT WITH TWO DEPENDANT VARAIBLES, 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Sleep_Data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
 
#DEFINING MY VARIABLES

x = Sleep_Data["Stress Level"]
y = Sleep_Data["Quality of Sleep"]
z = Sleep_Data["Sleep Duration"]


#GRAPHING

plt.scatter(x, y, color='darkmagenta', label = 'Quality of Sleep')
plt.scatter(x, z, color='indigo', label = 'Sleep Duration')
m_y, b_y = np.polyfit(x, y, 1)
m_z, b_z = np.polyfit(x, z, 1)
plt.title('Relationship Between Sleep Duration, Sleep Quality and Stress Level')
plt.xlabel('Stress Level')
plt.ylabel('Sleep Quality and Sleep Duration')

plt.plot(x, m_y*x + b_y, color='darkmagenta', linestyle='dotted')
plt.plot(x, m_z*x + b_z, color='indigo', linestyle='dotted')

plt.legend(title = 'Variables', loc = 'upper right')

