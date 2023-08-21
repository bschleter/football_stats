import pandas as pd
import os

# Get the absolute path to the file
file_path = os.path.abspath('stat_csv/advanced_air_yards.csv')
# Load the data
df_advanced_air_yards = pd.read_csv(file_path)

# Remove the row that is a repeat of the column headers
df_advanced_air_yards = df_advanced_air_yards[df_advanced_air_yards['Unnamed: 0_level_0'] != 'Rk']

# Remove rows where the 'Player' field is NaN
df_advanced_air_yards = df_advanced_air_yards.dropna(subset=['Unnamed: 1_level_0'])

# Convert numerical columns to appropriate data types
numeric_cols = df_advanced_air_yards.columns[6:]  # All columns from 'Age' onwards are numeric
df_advanced_air_yards[numeric_cols] = df_advanced_air_yards[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Rename the columns
df_advanced_air_yards.columns = ['Rank', 'Player', 'Team', 'Age', 'Position', 'Games', 'Games Started', 'Completions', 'Attempts', 'Yards', 'Average Intended Yards', 'Average Intended Yards per Attempt', 'Completed Air Yards', 'Completed Air Yards per Completion', 'Completed Air Yards per Attempt', 'Seaon Yards After Catch', 'Yards After Catch per Completion']

#in position column replace empty values with NaN
df_advanced_air_yards['Position'] = df_advanced_air_yards['Position'].fillna('N/A')

# Display the first few rows of the cleaned dataframe
df_advanced_air_yards.head()
print(df_advanced_air_yards.head(10))

#save to path 
df_advanced_air_yards.to_csv('advanced_air_yards.csv', index=False)
