#CORRELATION BETWEEN BMI CATEGORIES AND SLEEP DURATION
#AUTHOR: SARAH MEGHDIR
#BAR GRAPH 

import pandas as pd
import matplotlib.pyplot as plt

Sleep_Data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
 
#DEFINING MY VARIABLES
Sleep_Data['BMI Category'] = Sleep_Data['BMI Category'].replace({'Normal Weight':'Normal'})
x = Sleep_Data["BMI Category"]
y = Sleep_Data["Sleep Duration"]


#GRAPHING

#BARS
plt.bar(x, y, color='darkmagenta')

#TITLES
plt.title ('Correlation Between BMI Category and Sleep Duration')
plt.xlabel('BMI Category')
plt.ylabel('Sleep Duration')
