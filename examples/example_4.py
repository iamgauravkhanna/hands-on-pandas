# Import pandas package
import pandas as pd

df = pd.DataFrame

# Accessing columns
ages = df['Age']

# Filtering data
young_people = df[df['Age'] < 30]

# Adding a new column
df['Salary'] = [50000, 60000, 70000]

# Grouping and aggregating
average_age = df.groupby('City')['Age'].mean()

# Sorting
df_sorted = df.sort_values(by='Age', ascending=False)

# Saving to a CSV file
df.to_csv('output.csv', index=False)