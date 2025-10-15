import pandas as pd
import matplotlib.pyplot as plt

Sleep_Data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
 

print(Sleep_Data.columns)
# Create the plot
x = Sleep_Data['Sleep Duration']
y = Sleep_Data['Quality of Sleep']
# plt.scatter(x,y, color = 'blue', label = 'Data points')
plt.plot(x, y, 'o', label='Data Points')
plt.title('Sleep Quality vs Sleep Duration')
plt.xlabel('Sleep Duration')
plt.ylabel('Sleep Quality')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

