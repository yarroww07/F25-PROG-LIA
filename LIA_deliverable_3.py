import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")


                                    ### Prelimenary steps ###
## a ##                                    
#print(Sleep_Data.head())

#print(Sleep_Data.shape)

#print(Sleep_Data.info())

#print(Sleep_Data.describe())


## b ##
#Duplicates = Sleep_Data.duplicated()
#print(Duplicates.value_counts())


## c ##
#print(df.isnull())





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
                              
