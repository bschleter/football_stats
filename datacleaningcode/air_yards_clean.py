import pandas as pd
import os

# Get the absolute path to the file
file_path = os.path.abspath('stat_csv/air_yards.csv')
# Load the data
df_air_yards = pd.read_csv(file_path)

# Remove the row that is a repeat of the column headers
df_air_yards = df_air_yards[df_air_yards['Unnamed: 0_level_0'] != 'Tm']

# Remove rows where the 'Unnamed: 1_level_0' field is NaN
df_air_yards = df_air_yards.dropna(subset=['Unnamed: 1_level_0'])

# Convert numerical columns to appropriate data types
numeric_cols = df_air_yards.columns[2:]  # All columns from 'Cmp' onwards are numeric
df_air_yards[numeric_cols] = df_air_yards[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Rename the columns
df_air_yards.columns = ['Team', 'Games', 'Completions', 'Attempts', 'Yards', 'Average Intended Air Yards', 'Average Intended Air Yards per Attempt', 'Completed Air Yards', 'Completed Air Yards per Completion', 'Completed Air Yards per Attempt', 'Yards After Catch', 'Yards After Catch per Completion']

# Display the first few rows of the cleaned dataframe
df_air_yards.head()

print(df_air_yards.head(4))
df_air_yards.to_csv('air_yards.csv', index=False)
