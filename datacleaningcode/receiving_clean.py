import pandas as pd
import os

# Get the absolute path to the file
file_path = os.path.abspath('stat_csv/receiving.csv')

# Load the data
receiving_df = pd.read_csv(file_path)

# Removing extra header rows
receiving_df = receiving_df[receiving_df["Rk"] != "Rk"]

# Converting numerical columns to their appropriate data types
num_cols = ['Age', 'G', 'GS', 'Tgt', 'Rec', 'Yds', 'TD', '1D', 'Lng', 'R/G', 'Y/G', 'Fmb']
receiving_df[num_cols] = receiving_df[num_cols].apply(pd.to_numeric, errors='coerce')

# Filling missing values in 'Pos' column with 'Unknown'
receiving_df['Pos'] = receiving_df['Pos'].fillna('N/A')

# Filling missing values in 'Y/R' column with 0
receiving_df['Y/R'] = receiving_df['Y/R'].fillna(0)

# Renaming columns
receiving_df = receiving_df.rename(columns={'Tm': 'Team','G':'Games', 'GS': 'Games Started', 'Tgt': 'Targets', 'Rec':'Receptions','Ctch%':'Catch Percentage', 
                                            'Yds':'Yards','Y/R':'Yards per Reception','TD':'Touchdowns',
                                            '1D': 'First Down Receiving', 'Lng': 'Longest Reception', 'Y/Tgt': 'Yards per Target',
                                            'R/G': 'Receptions per Game', 'Y/G': 'Yards per Game', 'Fmb': 'Fumbles'})

receiving_df.head()

print(receiving_df.head(4))#save to path 
receiving_df.to_csv('cleanstats/receiving.csv', index=False)
