import pandas as pd
import os 

# Get the absolute path to the file
file_path = os.path.abspath('stat_csv/kicking.csv')
# Load the data
kicking_df = pd.read_csv(file_path)

# Remove extra header rows
kicking_df = kicking_df[kicking_df["Rk"] != "Rk"]
    
# Remove '%' from 'TB%,FGM, FGA' and convert to float
kicking_df['FGA'] = pd.to_numeric(kicking_df['FGA'], errors='coerce').fillna(0).astype(int)
kicking_df['FGM'] = pd.to_numeric(kicking_df['FGM'], errors='coerce').fillna(0).astype(int)
kicking_df['TB%'] = kicking_df['TB%'].str.rstrip('%').astype('float') / 100.0

# Convert columns to numeric types where applicable, handling errors
num_cols = ['Age', 'G', 'GS', 'FGA', 'FGM', 'FG%', 'XPA', 'XPM', 'XP%', 'KO', 'KOYds', 'TB', 'TB%', 'KOAvg']
for col in num_cols:
    kicking_df[col] = pd.to_numeric(kicking_df[col], errors='coerce')

# Replace missing numeric values with 0
kicking_df[num_cols] = kicking_df[num_cols].fillna(0)

# Replace missing non-numeric values with 'Unknown'
kicking_df.fillna('Unknown', inplace=True)

# Renaming columns
kicking_df = kicking_df.rename(columns={"Rk": "Rank","Tm": "Team","Age": "Age","Pos": "Position","G": "Games","GS": "GamesStarted","FGA": "FieldGoalAttempts","FGM": "FieldGoalsMade",
    "FG%": "FieldGoalPercentage","XPA": "ExtraPointAttempts","XPM": "ExtraPointsMade","XP%": "ExtraPointPercentage","KO": "KickOffs",
    "KOYds": "KickOffYards","TB": "TouchBacks","TB%": "TouchBackPercentage","KOAvg": "KickOffAverage"})
#view 
kicking_df.head()
print(kicking_df.head(4))
#save to path 
kicking_df.to_csv('cleanstats/kicking.csv', index=False)