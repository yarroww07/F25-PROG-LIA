# Imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

Sleep_Data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

# Variables
condition_count_male = 0
condition_count_female = 0

# Assigning variables to each row
for index, row in Sleep_Data.iterrows():
    gender = row['Gender']
    condition = row['Sleep Disorder']
    
    # Checking if a condition is applied to male or female
    # print(condition)
    if condition == 'Sleep Apnea' or condition == 'Insomnia':
        if gender == 'Male':
            condition_count_male += 1
        elif gender == 'Female':
            condition_count_female += 1

# MAKING THE PIE CHARTS
# Total counts
count_males = (Sleep_Data['Gender'] == 'Male').sum()
count_females = (Sleep_Data['Gender'] == 'Female').sum()

# Variables
labels_males = ['Males Without Sleep Disorder', 'Males with Sleep Disorder']
values_males = [count_males, condition_count_male]
labels_females = ['Females Without Sleep Disorder', 'Females with Sleep Disorders']
values_females = [count_females, condition_count_female]

# Subplot 1
plt.subplot(1,2,1)
plt.pie(values_males, labels = labels_males, colors = ('paleturquoise','darkslategrey'))
plt.title('Proportion of Men with Sleep Disorders')

# Subplot 2
plt.subplot(1,2,2)
plt.pie(values_females, labels = labels_females, colors = ('firebrick', 'lightcoral'))
plt.title('Proportions of Females with Sleep Disorders')

# Plot Display
plt.tight_layout()
plt.show()
