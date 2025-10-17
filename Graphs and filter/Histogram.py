import pandas as pd
import matplotlib.pyplot as plt

Sleep_Data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")


x = Sleep_Data["Daily Steps"]

plt.hist(x, color = "purple")
plt.title('Daily Step distribution')
plt.xlabel('Daily steps ')
plt.show()
 