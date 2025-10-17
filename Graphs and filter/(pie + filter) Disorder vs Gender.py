# SUMMARY OF THE FILE: 
# Author: Rania Bouladraf
# Contains: Filter, one plot with two subplots





# Imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

Sleep_Data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")


# Variables
male_condition_count = 0
female_condition_count = 0
sleep_disorders = [] # List in which we will store the filtered data

# Total counts
male_total_count = (Sleep_Data['Gender'] == 'Male').sum()
female_total_count = (Sleep_Data['Gender'] == 'Female').sum()


# Filtering the dataset → Only keeping columns with sleep conditions (Sleep Apnea or Insomnia)
#   Also counting the amount of males with sleeping disorders, and females with sleeping disorders! 
for index, row in Sleep_Data.iterrows():
    condition = row['Sleep Disorder']
    gender = row['Gender']

    if condition == 'Sleep Apnea' or condition == 'Insomnia': 
        sleep_disorders.append(row)

        if gender == 'Male':
            male_condition_count += 1
        elif gender == 'Female':
            female_condition_count += 1

Filtered_Sleep_Data = pd.DataFrame(sleep_disorders)

# Viewing the filtered data
print(Filtered_Sleep_Data[:4])




# MAKING THE PIE CHARTS

# Variables
labels_males = ['Males Without Sleep Disorders', 'Males with Sleep Disorders']
values_males = [male_total_count, male_condition_count]
labels_females = ['Females Without Sleep Disorders', 'Females with Sleep Disorders']
values_females = [female_total_count, female_condition_count]

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
