import pandas as pd
import os

# Get the absolute path to the file
file_path = os.path.abspath('stat_csv/rushing.csv')

# Load the data
df_rushing = pd.read_csv(file_path)

# Remove the row that is a repeat of the column headers
df_rushing = df_rushing[df_rushing['Unnamed: 0_level_0'] != 'Rk']

# Remove rows where the 'Unnamed: 1_level_0' field is NaN
df_rushing = df_rushing.dropna(subset=['Unnamed: 1_level_0'])

# Convert numerical columns to appropriate data types
numeric_cols = df_rushing.columns[6:]  # All columns from 'G' onwards are numeric
df_rushing[numeric_cols] = df_rushing[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Rename the columns
df_rushing.columns = ['Rank', 'Player', 'Team', 'Age', 'Position', 'Games Played', 'Games Started', 'Rushing Attempts', 'Rushing Yards', 'Rushing Touchdowns', 'First Downs', 'Longest Rush', 'Yards per Attempt', 'Yards per Game', 'Fumbles']
# Fill empty values in the 'Position' column with 'N/A'

df_rushing['Position'] = df_rushing['Position'].fillna('N/A')
# Display the first few rows of the cleaned dataframe
df_rushing.head()

#save to path 
df_rushing.to_csv('rushing.csv', index=False)
