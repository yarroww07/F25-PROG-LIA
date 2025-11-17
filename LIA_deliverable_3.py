import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")


#PRELIMINARY STEPS
#CODED BY SARAH MEGHDIR

#a) INITIAL DATA INSPECTION                                 
print("Head:")
print(df.head())

print("Shape:")
print(df.shape)

print("Info:")
print(df.info())

print("Description:")
print(df.describe())

#b) Handle duplicate entries
print("Number of duplicates:")
Duplicates = df.duplicated()
print(Duplicates.value_counts())
#THERE ARE NO DUPLICATES THEREFORE NO NEED TO DROP ANY ROWS

#c) Identify and manage missing values
print("Number of null values:")
print(df.isnull().sum())
df['Sleep Disorder'] = df['Sleep Disorder'].fillna("No disorder")
print(df.info())
print(df['Sleep Disorder'].value_counts())
#In the column "Sleep disorder", 219 people had no sleep disorder, fitting into the category "None". Using isnull, these values were read as null values. To avoid confusion, I replaced them by a new category: "No disorder".

#d) Correct data types and formats
df['BMI Category'] = df['BMI Category'].replace({'Normal Weight':'Normal'})
#In the BMI category, two categories are used to indicate a BMI in a normal range; Normal and Normal Weight. Since both of them represent the same thing, I merged them into one category: Normal.

                                  ### Univariate Non-graphical EDA ###

numeric_df = df.select_dtypes(include = np.number)

print('Numerical Values')
print('')
print('')
      

for col in numeric_df.columns:
    print(col) 
    print('mean:', df[col].mean())
    print('median:', df[col].median())
    print('mode:', df[col].mode())
    print('standard deviation:', df[col].std())
    print('variance:', df[col].var())
    print('skewness', df[col].skew())
    print('kurtosis:', df[col].kurt())
    print('quartiles',df[col].quantile([0.25, 0.5, 0.75]))
    print('')
    print('')
    
categorical_df = df.select_dtypes(exclude = np.number) 

print('categorical Values')
print('')
print('')  

for col in categorical_df.columns:
    print(col)
    print('frequency count:', df[col].value_counts())
    print('proportion:', df[col].value_counts(normalize = True))
    print('mode:', df[col].mode())
    print('unique values:', df[col].nunique())
    print('')
    print('')
    
    
    


                              ### Univariate Graphical EDA ###
                    
for col in numeric_df:
    if col != 'Age' and col != 'Daily Steps' and col != 'Person ID':
        sns.displot(data = df,
                x= col,
                hue = 'Gender',
                multiple = 'dodge',
                common_norm = False,
                kde = True)  

for col  in numeric_df:
    if col != 'Age' and col != 'Daily Steps' and col != 'Person ID':
        sns.displot(data = df,
              x= col,
              hue = 'Sleep Disorder',
              kind = 'ecdf')  
    
for col in numeric_df:
    if col != 'Age' and col != 'Daily Steps' and col != 'Person ID':
        sns.displot(data = df,
              x= col,
              hue = 'Occupation',
              common_norm = False,
              stat = 'density',
              palette = 'flare',
              multiple = 'stack',
              discrete = True)         
    
    

                           ### Multivariate Non-Graphical EDA ###
                              
# First Relationship: Occupation and Sleep Disorder (with percentages over the total values)
# pd.crosstab(df['Occupation'], df['Sleep Disorder'])
# pd.crosstab(df['Occupation'], df['Sleep Disorder'], normalize=True)

# Second Relationship:
# pd.crosstab(df['BMI Category'], df['Sleep Disorder'])
# pd.crosstab(df['BMI Category'], df['Sleep Disorder'], normalize=True)

# Third Relationship: Gender and Sleep Disorder (with percentages over ROWS and over total values)
# pd.crosstab(df['Gender'], df['Sleep Disorder'])
# pd.crosstab(df['Gender'], df['Sleep Disorder'], normalize='index')
# pd.crosstab(df['Gender'], df['Sleep Disorder'], normalize=True)

# Three-way frequency table; BMI was added at first, but removed because it did not give a clean look
# pd.crosstab(df['Occupation'], [df['Gender'],df['Sleep Disorder']])
# pd.crosstab(df['Occupation'], [df['Gender'],df['Sleep Disorder']], normalize=True)


                         ### Multivariate Graphical EDA ###

# 6.1. Visualizing statistical relationships

# a) Faceted relplot answwering Q1
sns.relplot(data = df, x = "Stress Level", y = "Sleep Duration", col = "Occupation")
plt.figure()

#b) Answers question 5
#sns.relplot(data = df,
#            x = 'Quality of Sleep', 
#            y = 'Physical Activity Level',
#            hue = 'BMI Category',
#            size = 'Daily Steps',
#            col = 'Gender')

#plt.figure() # in order not to merge the two plots

#c) Answers question 4 (age is the continuity variable here)
#sns.lineplot(data = df,
#            x = 'Age',
#             y = 'Sleep Duration',
#             hue = 'Gender')

#plt.figure()

#d) 
# sns.pointplot(
#     data=df,
#     x='Stress Level',
#     y='Quality of Sleep',
#     errorbar='sd',
#     color='Green'
# )

# e) Linear regression plots answering Q1
sns.regplot(data = df, x = "Stress Level", y = "Sleep Duration")
plt.figure()

sns.regplot(data = df, x = "Stress Level", y = "Quality of Sleep")
plt.figure()                       
                         
                         
# 6.2. Visualizing categorical data 

#a) Answers question 4
# sns.catplot(data = df,
#            x = 'Gender',
#            y = 'Sleep Disorder',
#            jitter = True)

#plt.figure()

# b) Categorical scatter WITHOUT jitter answering Q6
sns.stripplot(data = df, x = "Sleep Disorder", y = "Sleep Duration", jitter = False)
plt.figure()

#c) Answers question 4
#sns.catplot(data = df,
#            x = 'Sleep Disorder',
#            y = 'Heart Rate',
#            hue = 'Gender',
#            kind = 'swarm')

#plt.figure()

# d) Box plot with 3 variables answering Q6
sns.boxplot(data = df, x = "Sleep Disorder", y = "Sleep Duration", hue = "Gender")
plt.figure()

#e) 
sns.boxenplot(
    data=df,
    x='BMI Category',
    y='Physical Activity Level',
    palette='Set2'
)
 
#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")


#PRELIMINARY STEPS
#CODED BY SARAH MEGHDIR

#a) INITIAL DATA INSPECTION                                 
print("Head:")
print(df.head())

print("Shape:")
print(df.shape)

print("Info:")
print(df.info())

print("Description:")
print(df.describe())

#b) Handle duplicate entries
print("Number of duplicates:")
Duplicates = df.duplicated()
print(Duplicates.value_counts())
#THERE ARE NO DUPLICATES THEREFORE NO NEED TO DROP ANY ROWS

#c) Identify and manage missing values
print("Number of null values:")
print(df.isnull().sum())
df['Sleep Disorder'] = df['Sleep Disorder'].fillna("No disorder")
print(df.info())
print(df['Sleep Disorder'].value_counts())
#In the column "Sleep disorder", 219 people had no sleep disorder, fitting into the category "None". Using isnull, these values were read as null values. To avoid confusion, I replaced them by a new category: "No disorder".

#d) Correct data types and formats
df['BMI Category'] = df['BMI Category'].replace({'Normal Weight':'Normal'})
#In the BMI category, two categories are used to indicate a BMI in a normal range; Normal and Normal Weight. Since both of them represent the same thing, I merged them into one category: Normal.

#f) 
sns.violinplot(
    data=df,
    x='Quality of Sleep',
    y='Sleep Duration',
    hue='BMI Category',
    split=True,       
    bw=0.3,  
    palette='Set2'
)


#%%
#g) Answers question 5
#g = sns.catplot(data = df,
#                x = 'Physical Activity Level',
#                y = 'Quality of Sleep',
#                kind = 'violin',
#                inner = None)

#sns.swarmplot(data = df,
#             x = 'Physical Activity Level',
 #             y = 'Quality of Sleep',
  #            color = 'k',
   #           size = 3,
    #          ax = g.ax)

#plt.figure()


#h)
# plt.figure(figsize=(15,6))
# sns.barplot(
#     data=df,
#     x='BMI Category',
#     y='Sleep Duration',
#     hue='Gender',
#     errorbar=('ci', 97),
#     palette='magma'
# )
# sns.barplot(
#     data=df,
#     x='BMI Category',
#     y='Physical Activity Level',
#     hue='Gender',
#     errorbar=('ci', 97),
#     palette='mako'
# )


# i) Point plot (3 variables, 90% CI, dashed lines) answering Q6


# sns.pointplot(
#     data=df,
#     x='Physical Activity Level',
#     y='Quality of Sleep',
#     hue='Gender',
#     errorbar=('ci',90),
#     linestyles='dashed'
# )


#j


# sns.countplot(data=df, 
#               x='Sleep Disorder', 
#               hue='Gender',
#               palette='mako'
#               )


#6.3. Visualizing bivariate distributions


#a)
sns.displot(
    data=df,
    x='Physical Activity Level',
    y='Sleep Duration',
    kind='hist',
    bins=(10,10),
    cbar=True
)

#b) distribution plot with 2 variables makign use of bivariate density contours with amount of curves and its lowest level adjusted, kernel dens. estimation

sns.kdeplot(
    data=df,
    x='Sleep Duration',
    y='Quality of Sleep',
    hue='Gender',
    levels=8,
    fill=False
)

#%%

#c) Answers Question 5 # Added gender because it looks better with gender
#sns.displot(data = df, 
 #           y = 'Quality of Sleep',
  #          x = 'Daily Steps',
   #         palette = 'flare',
    #        hue = 'Gender',
     #       kind = 'kde')






                                   
             #Meriem 
# Description: This  code provides a proportion between the diferrent blood levels between all individuals in the dataset.
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
            
                         
                         

# %%
