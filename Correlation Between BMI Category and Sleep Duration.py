import pandas as pd
import matplotlib.pyplot as plt

Sleep_Data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
 
#DEFINING MY VARIABLES

x = Sleep_Data["BMI Category"]
y = Sleep_Data["Sleep Duration"]


#GRAPHING

plt.bar(x, y, color='purple')

plt.title ('Correlation Between BMI Category and Sleep Duration')
plt.xlabel('BMI Category')
plt.ylabel('Sleep Duration')