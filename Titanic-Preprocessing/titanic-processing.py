import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv('titanic.csv')

# Data Exploration
print(df.info())
print(df.describe())

# Handling Missing Values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df.dropna(subset=['Embarked'], inplace=True)

# Categorical to Numerical
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df['Embarked'] = df['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})

# Feature Engineering
df['Family_Size'] = df['SibSp'] + df['Parch']

# Data Normalization (Optional)
df['Age'] = (df['Age'] - df['Age'].min()) / (df['Age'].max() - df['Age'].min())
df['Fare'] = (df['Fare'] - df['Fare'].min()) / (df['Fare'].max() - df['Fare'].min())

# Save the cleaned data
df.to_csv('cleaned_titanic.csv', index=False)