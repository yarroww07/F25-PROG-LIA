#PRELIMINARY STEPS
#CODED BY SARAH MEGHDIR

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

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
print("Number of dupilcates:")
Duplicates = df.duplicated()
print(Duplicates.value_counts())


#c) Identify and manage missing values
print("Number of null values:")
print(df.isnull().sum())
df['Sleep Disorder'] = df['Sleep Disorder'].fillna("No disorder")
print(df.info())
print(df['Sleep Disorder'].value_counts())




#d) Correct data types and formats
print()