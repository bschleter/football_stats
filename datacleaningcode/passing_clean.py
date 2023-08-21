import os
import pandas as pd


# Get the absolute path to the file
file_path = os.path.abspath('stat_csv/passing.csv')

# Load the data
df_passing = pd.read_csv(file_path)

# Cleaning the data
df_passing = df_passing[df_passing['Rk'] != 'Rk']  # Remove rows with column headers
df_passing = df_passing.dropna(subset=['Player'])  # Remove rows with missing player names

# Convert numeric columns to appropriate data types
numeric_cols = ['Age', 'G', 'GS', 'Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'Int', '1D', 'Lng', 'Y/A', 'AY/A', 'Y/C', 'Y/G', 'Rate', 'QBR', 'Sk', 'Yds.1', 'NY/A', 'ANY/A', 'Sk%', '4QC', 'GWD']
df_passing[numeric_cols] = df_passing[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Rename the columns
df_passing.columns = ['Rank','Player','Team','Age','Position','Games','Games Started', 'Quarterback Record', 'Completions', 'Attempts', 'Completion Percentage', 'Yards', 'Touchdowns', 'Touchdown Percentage', 'Interceptions','Interception Percentage', 'First Downs Passing', 'Longest Completion', 'Yards per attempt', 'Adjusted Yards per Pass Attempt', 'Yards per Completion', 'Yards per Game', 'Rate', 'QBR', 'Sacks', 'Yards Lost from Sacks','Sack Percentage', 'Net Yards per Pass Attempt', 'Adjusted Net Yards per pass attempt', '4th Quarter Comebacks', 'Game Winning Drives']
# Display the first few rows of the cleaned dataframe

#in position column replace empty values with NaN
df_passing['Position'] = df_passing['Position'].fillna('N/A')
df_passing['Quarterback Record'] = df_passing['Quarterback Record'].fillna('N/A')
df_passing['Yards per Completion'] = df_passing['Yards per Completion'].fillna('N/A')
df_passing['QBR'] = df_passing['QBR'].fillna('N/A')
df_passing['4th Quarter Comebacks'] = df_passing['4th Quarter Comebacks'].fillna('N/A')
df_passing['Game Winning Drives'] = df_passing['Game Winning Drives'].fillna('N/A')

df_passing.head()
# Display the first few rows of the cleaned dataframe
print(df_passing.head(4))
df_passing.to_csv('cleanstats/passing.csv', index=False)
