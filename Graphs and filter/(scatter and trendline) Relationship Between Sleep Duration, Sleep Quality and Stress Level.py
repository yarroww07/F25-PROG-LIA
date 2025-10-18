#CORRELATION BETWEEN BMI CATEGORIES, SLEEP DURATION AND SLEEP QUALITY
#AUTHOR: SARAH MEGHDIR
#SCATTER PLOT WITH TWO DEPENDANT VARAIBLES (SLEEP DURATION AND SLEEP QUALITY) AND TRENDLINES

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Sleep_Data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
 
#DEFINING MY VARIABLES
x = Sleep_Data["Stress Level"]
y = Sleep_Data["Quality of Sleep"]
z = Sleep_Data["Sleep Duration"]

#TRENDLINE FORMAT (y=mx+b)
#DEFINING m AND b
m_y, b_y = np.polyfit(x, y, 1)
m_z, b_z = np.polyfit(x, z, 1)

#GRAPHING

#SCATTER PLOT
plt.scatter(x, y, color='darkmagenta', label = 'Quality of Sleep')
plt.scatter(x, z, color='indigo', label = 'Sleep Duration')

#TRENDLINES
plt.plot(x, m_y*x + b_y, color='darkmagenta', linestyle='dotted')
plt.plot(x, m_z*x + b_z, color='indigo', linestyle='dotted')

#TITLES
plt.title('Relationship Between Sleep Duration, Sleep Quality and Stress Level')
plt.xlabel('Stress Level')
plt.ylabel('Sleep Quality and Sleep Duration')

#LEGEND
plt.legend(title = 'Variables', loc = 'upper right')
