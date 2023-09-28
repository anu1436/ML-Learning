# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv('House_Price.csv')

# Explore Data
print(df.info())
print(df.describe())

# Handle Missing Values
df.dropna(inplace=True)

# Feature Engineering
df['Age'] = 2023 - df['YearBuilt']

# Data Normalization
df['Price'] = (df['Price'] - df['Price'].min()) / (df['Price'].max() - df['Price'].min())

# Data Visualization
plt.scatter(df['SquareFeet'], df['Price'])
plt.xlabel('Square Feet')
plt.ylabel('Normalized Price')
plt.show()
