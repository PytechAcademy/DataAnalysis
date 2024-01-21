import pandas as pd
# importing csv file
df = pd.read_csv("100 Records.csv")
# Data Exploration
print(df.head())  # Display the first five rows
print(df.tail())  # Display the last five rows
print(df.info())  # Get information about the DataFrame
# Subsetting Data works with comparitive and logical operators
young_people_1 = df[df['Age in Yrs.'] < 22]
print(young_people_1)
# Adding a new column
df['Is_30_plus'] = df['Age in Yrs.'] > 30
print(df.columns) # To fetch columns
# Basic Insights
print(df.describe())  # Summary statistics for numerical columns
print(df.describe(include="all")) # summary stats for all columns
print(df['Region'].value_counts())  # Count of unique values in 'Region'


