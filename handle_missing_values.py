# Handle Missing Values - Veda Technology Day 22
import pandas as pd

# Load dataset
df = pd.read_csv("titanic_missing_values.csv")

print("Original dataset:")
print(df)
print("\nMissing values before treatment:")
print(df.isnull().sum())

# Numerical columns: median is used because it is less affected by outliers.
for col in ["Age", "Fare"]:
    df[col] = df[col].fillna(df[col].median())

# Categorical column: mode is suitable for the small number of missing values.
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

print("\nMissing values after treatment:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("titanic_cleaned.csv", index=False)
print("\nCleaned dataset saved as titanic_cleaned.csv")
