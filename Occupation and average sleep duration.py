#Meriem
#description: Bar graph representing the various occupation taking in consederation the averag esleep duration.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Sleep_Data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
print(Sleep_Data.columns)
 
#denifing the variables

x = Sleep_Data["Occupation"]
y = Sleep_Data["Sleep Duration"]



#Plotting the bar graph

plt.figure(figsize=(16,6))
plt.title('Average sleep duration per occupation')
sns.barplot(Sleep_Data, x = 'Occupation' , y = 'Sleep Duration' , palette= 'flare')
plt.tight_layout()
plt.show()

