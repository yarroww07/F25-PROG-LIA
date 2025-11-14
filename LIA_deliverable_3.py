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

                       
for col in ['Sleep Duration', 'Quality of Sleep', 'Age']:
    sns.displot(data = df,
                x= col,
                hue = 'Gender',
                multiple = 'dodge',
                common_norm = False,
                kde = True)  

for col  in ['Daily Steps', 'Physical Activity Level']:
    sns.displot(data = df,
                x= col,
                hue = 'Sleep Disorder',
                kind = 'ecdf')  
    
for col in ['Stress Level', 'Heart Rate']:
    sns.displot(data = df,
                x= col,
                hue = 'Occupation',
                multiple = 'stack',
                discrete = True)         
    
    

                           ### Multivariate Non-Graphical EDA ###
                              

# ASK; Are these three crosstabs enough or should i do three without normalize, then one normalize...

# First Relationship: Occupation and Sleep Disorder (with percentages over the total values)
pd.crosstab(df['Occupation'], df['Sleep Disorder'], normalize=True)

# Second Relationship:
pd.crosstab(df['BMI Category'], df['Sleep Disorder'])

# Third Relationship: Gender and Sleep Disorder (with percentages over ROWS only)
pd.crosstab(df['Gender'], df['Sleep Disorder'], normalize='index')

# Three-way frequency table; BMI was added at first, but removed because it did not give a clean look
pd.crosstab(df['Occupation'], [df['Gender'],df['Sleep Disorder']])


                         ### Multivariate Graphical EDA ###

# 6.1.

#a)

#b) Answers question 5
sns.relplot(data = df,
            x = 'Quality of Sleep', 
            y = 'Physical Activity Level',
            hue = 'BMI Category',
            size = 'Daily Steps',
            col = 'Gender')

plt.figure() # in order not to merge the two plots

#c) Answers question 4 (age is the continuity variable here)
sns.lineplot(data = df,
             x = 'Age',
             y = 'Sleep Duration',
             hue = 'Gender')

plt.figure()

#d)

#e)                         
                         
                         
# 6.2.  

#a) Answers question 4
sns.catplot(data = df,
            x = 'Gender',
            y = 'Quality of Sleep',
            jitter = True)

plt.figure()

#b)

#c) Answers question 4
sns.catplot(data = df,
            x = 'Sleep Disorder',
            y = 'Heart Rate',
            hue = 'Gender',
            kind = 'swarm')
                                   
                         
                         
                         