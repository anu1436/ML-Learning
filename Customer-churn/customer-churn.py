# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv('Customer_Churn.csv')

# Explore Data
print(df.head())
print(df.info())

# Handle Missing Values
df.dropna(inplace=True)

# Data Transformation
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# Data Normalization
df['MonthlyCharges'] = (df['MonthlyCharges'] - df['MonthlyCharges'].min()) / (df['MonthlyCharges'].max() - df['MonthlyCharges'].min())

# Feature Engineering
df['TotalCharges'] = df['MonthlyCharges'] * df['tenure']

# Data Visualization
plt.hist(df['MonthlyCharges'])
plt.show()