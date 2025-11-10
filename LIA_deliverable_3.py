import pandas as pd
import matplotlib.pyplot as plt

Sleep_Data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")


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
print(Sleep_Data.isnull())