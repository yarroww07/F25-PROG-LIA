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
# CODED BY: MERIEM HAMZI                                  

numeric_df = df.select_dtypes(include = np.number) # This includes only th enumerival variables

print('Numerical Values')
print('')
print('')
      

for col in numeric_df.columns: # For loop used to not repeat the code multiple time to each variables
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
    print('') # This is used to seperated the lines between the outputs in the Ipython console
    
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
#CODED BY: MERIEM HAMZI

#loops were used to facilitate graph generation
#only 5 of the 7 numerical variables were taken in consideration. Person ID is directly excluded because it is not a variable
#Graphs were made making sure everying asked for was added. This is why there are only three graphs per variable                              
                    
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
# CODED BY: RANIA BOULADRAF     

# First Relationship: Occupation and Sleep Disorder (with percentages over the total values)
pd.crosstab(df['Occupation'], df['Sleep Disorder'])
pd.crosstab(df['Occupation'], df['Sleep Disorder'], normalize=True)

# Second Relationship:
pd.crosstab(df['BMI Category'], df['Sleep Disorder'])
pd.crosstab(df['BMI Category'], df['Sleep Disorder'], normalize=True)

# Third Relationship: Gender and Sleep Disorder (with percentages over ROWS and over total values)
pd.crosstab(df['Gender'], df['Sleep Disorder'])
pd.crosstab(df['Gender'], df['Sleep Disorder'], normalize='index')
pd.crosstab(df['Gender'], df['Sleep Disorder'], normalize=True)

# Three-way frequency table; BMI was added at first, but removed because it did not give a clean look
pd.crosstab(df['Occupation'], [df['Gender'],df['Sleep Disorder']])
pd.crosstab(df['Occupation'], [df['Gender'],df['Sleep Disorder']], normalize=True)


                                ## Multivariate Graphical EDA ###

# 6.1. Visualizing statistical relationships

# a) FACETING PLOT, SARAH
# Faceted relplot, Answering Question 1
sns.relplot(data = df, 
            x = "Stress Level", 
            y = "Sleep Duration", 
            col = "Occupation"
            )
plt.figure()

#b) PLOT REPRESENTING 5 VARIABLES 
# Answers question 5, MERIEM
sns.relplot(data = df,
            x = 'Quality of Sleep', 
            y = 'Physical Activity Level',
            hue = 'BMI Category',
            size = 'Daily Steps',
            col = 'Gender')

plt.figure() # in order not to merge the two plots

#c) PLOT USING LINE INSTEAD OF POINTS, MERIEM
# Answers question 4 (age is the continuity variable here)
sns.lineplot(data = df,
            x = 'Age',
             y = 'Sleep Duration',
             hue = 'Gender')

plt.figure()

#d) PLOT ILLUSTATING STANDARD DEVIATION, RANIA
# Answers question 3
sns.pointplot(
    data=df,
    x='Stress Level',
    y='Quality of Sleep',
    errorbar='sd',
    color='Green'
)

# e) PLOT INCLUDING LINEAR REGRESSION, SARAH
# Answers question 1
sns.regplot(data = df, x = "Stress Level", y = "Sleep Duration")
plt.figure()

sns.regplot(data = df, x = "Stress Level", y = "Quality of Sleep")
plt.figure()                       
                         
                         
# 6.2. Visualizing categorical data 

#a) SCATTER PLOT WITH JITTER ENABLED, MERIEM 
# Answers question 4
sns.catplot(data = df,
           x = 'Gender',
           y = 'Sleep Disorder',
           jitter = True)

plt.figure()

# b) SCATTER PLOT WITHOUT JITTER, SARAH
# Answering Q6
sns.stripplot(data = df, x = "Sleep Disorder", y = "Sleep Duration", jitter = False)
plt.figure()

#c) BEESWARM PLOT REPRESENTING 3 VARIABLES, MERIEM 
# Answers question 4
sns.catplot(data = df,
           x = 'Sleep Disorder',
           y = 'Heart Rate',
           hue = 'Gender',
           kind = 'swarm')

plt.figure()

# d) BOX PLOT WITH 3 VARIABLES, SARAH
# Answering Q6
sns.boxplot(data = df, x = "Sleep Disorder", y = "Sleep Duration", hue = "Gender")
plt.figure()

#e) BOX PLOT SHOWING SHAPE OF DISTRIBUTION, RANIA 
# Answers Q2
sns.boxenplot(
    data=df,
    x='BMI Category',
    y='Physical Activity Level',
    palette='Set2'
)
 
#f) SPLIT VIOLIN PLOT 3 VARIABLES WITH ADJUSTED BANDWIDTH, RANIA
# Answers Q3
sns.violinplot(
    data=df,
    x='Quality of Sleep',
    y='Sleep Duration',
    hue='BMI Category',
    split=True,       
    bw=0.3,  
    palette='Set2'
)

#g) VIOLIN PLOT WITH SCATTER POINTS INSIDE THE VIOLIN SHAPES, MERIEM
# Answers question 5
g = sns.catplot(data = df,
                 x = 'Physical Activity Level',
                 y = 'Quality of Sleep',
                 kind = 'violin',
                 inner = None)

#This would merge  the two factors together

sns.swarmplot(data = df,
           x = 'Physical Activity Level',
           y = 'Quality of Sleep',
           size = 3,
           ax = g.ax)

plt.figure()


#h) BAR PLOT REPRESENTING 3 VARIABLES SHOWING 97% CONFIDENCE INTERVAL, RANIA
#Answers Q2
plt.figure(figsize=(15,6))
sns.barplot(
    data=df,
    x='BMI Category',
    y='Sleep Duration',
    hue='Gender',
    errorbar=('ci', 97),
    palette='magma'
)

# i) POINT PLOT WITH 3 VARIABLES SHOWING 90% CONFIDENCE INTERVAL AND LINES IN DASHED STYLE, SARAH
# Answers Q6
sns.pointplot(
    data=df,
    x='Physical Activity Level',
    y='Quality of Sleep',
    hue='Gender',
    errorbar=('ci',90),
    linestyles='dashed'
)


# j) BAR PLOT SHOWING NUMBER OF OBSERVATIONS IN EACH CATEGORY, RANIA
# Analyzes dataset

sns.countplot(data=df, 
              x='Sleep Disorder', 
              hue='Gender',
              palette='mako'
              )


#6.3. Visualizing bivariate distributions

#a) HEATMAP REPRESENTING 2 VARIABLES WITH COLOR INTENSITY BAR AND ADJUSTED BIN WIDTH, RANIA
# Answers Q2
sns.displot(
    data=df,
    x='Physical Activity Level',
    y='Sleep Duration',
    kind='hist',
    bins=(10,10),
    cbar=True
)

#b) DISTRIBUTION PLOT WITH 2 VARIABLES, BIVARIATE DENSITY CONTOURS, KDE, RANIA
# Answers Q3
sns.kdeplot(
    data=df,
    x='Sleep Duration',
    y='Quality of Sleep',
    hue='Gender',
    levels=8,
    fill=False
)

#c) HEATMAP REPRESENTING THREE VARIABLES, KDE, MERIEM
# Answers Question 5 # Added gender because it looks better with gender, by meriem
sns.displot(data = df, 
             y = 'Quality of Sleep',
             x = 'Daily Steps',
             palette = 'flare',
             hue = 'Gender',
             kind = 'kde')













# Description: This  code provides a proportion between the different blood levels between all individuals in the dataset.
# import pandas as pd
# import matplotlib.pyplot as plt

# Sleep_Data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

# #Variables

# high_blood_pressure = 0
# normal_blood_pressure = 0
# low_blood_pressure = 0

# #Preparing the values for each variable
# for index, row in Sleep_Data.iterrows():
#     blood_pressure = row['Blood Pressure']
    
#     #The value in the column are strings, we have to change them into integers   
#     systolic = int(blood_pressure.split('/')[0]) 
#     diastolic = int(blood_pressure.split('/')[1])
    
#     if systolic == 120 and diastolic == 80:
#         normal_blood_pressure += 1
#     elif systolic > 120 or diastolic > 80:
#         high_blood_pressure += 1
#     else:
#         low_blood_pressure += 1
        
# # Making of pie chart
# labels = ['Low Blood Pressure', 'Normal Blood Pressure', 'High Blood Pressure']
# variables = [low_blood_pressure, normal_blood_pressure, high_blood_pressure]
# colors = ['skyblue', 'lightgreen', 'darkred']

# plt.pie(variables, labels=labels, colors=colors)
# plt.title('Proportions of blood pressure levels in sample')
# plt.show()
