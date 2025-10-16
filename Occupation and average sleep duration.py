import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Sleep_Data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
print(Sleep_Data.columns)
 
#DEFINING MY VARIABLES

x = Sleep_Data["Occupation"]
y = Sleep_Data["Sleep Duration"]
colors = sns.cubehelix_palette()


#GRAPHING
plt.figure(figsize=(16,6))

sns.barplot(Sleep_Data, x = 'Occupation', y = 'Sleep Duration', palette= 'flare')

