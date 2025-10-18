#Meriem : This  code provides a proportion between the diferrent blood levels between all individuals in the dataset.
import pandas as pd
import matplotlib.pyplot as plt

Sleep_Data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

#Variables

high_blood_pressure = 0
normal_blood_pressure = 0
low_blood_pressure = 0

#Preparing the values for each variable
for index, row in Sleep_Data.iterrows():
    blood_pressure = row['Blood Pressure']
    
    #The value in the column are strings, we have to change them into integers   
    systolic = int(blood_pressure.split('/')[0]) 
    diastolic = int(blood_pressure.split('/')[1])
    
    if systolic == 120 and diastolic == 80:
        normal_blood_pressure += 1
    elif systolic > 120 or diastolic > 80:
        high_blood_pressure += 1
    else:
        low_blood_pressure += 1
        
# Making of pie chart
labels = ['Low Blood Pressure', 'Normal Blood Pressure', 'High Blood Pressure']
variables = [low_blood_pressure, normal_blood_pressure, high_blood_pressure]
colors = ['skyblue', 'lightgreen', 'darkred']

plt.pie(variables, labels=labels, colors=colors)
plt.title('Proportions of blood pressure levels in sample')
plt.show()
