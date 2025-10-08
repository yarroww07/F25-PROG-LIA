import numpy as np 
import matplotlib.pyplot as plt

gender, age, occupation, sleep_duration, sleep_quality, physical_activity, stress_level, bmi, blood_pressure, heart_rate, daily_steps, sleep_disorder = np.loadtxt(
    'Sleep_health_and_lifestyle_dataset.csv', skiprows=1, usecols=(1,2,3,4,5,6,7,8,9,10,11,12), unpack=True)

