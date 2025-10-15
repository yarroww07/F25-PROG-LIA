# Imports
import pandas as pd
import matplotlib.pyplot as plt

Sleep_Data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

# Variables
condition_count_male = 0
condition_count_female = 0

# Assigning variables to each row
for index, row in Sleep_Data.iterrows():
    gender = row['Gender']
    condition = row['Sleep Disorder']
    
    # Checking if a condition is applied to male or female
    if condition != 'None':
        if gender == 'Male':
            condition_count_male += 1
        elif gender == 'Female':
            condition_count_female += 1

# TEST (keep as comment)
# print(condition_count_female)
# print(condition_count_male)

# Creating a bar graph 
# Variables
categories = ['Male', 'Female']
values = [condition_count_male, condition_count_female]

plt.bar(categories, values, color=['blue','pink'])
plt.title('Test')
plt.xlabel('Gender')
plt.ylabel('Number of People with Sleep Disorders')
plt.grid()
plt.show()