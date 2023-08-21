import pandas as pd
import os

file_path = os.path.abspath('stat_csv/fantasy_rz.csv')

# Load the data
fantasy_rz_df = pd.read_csv((file_path), header=1)

# Handle missing values
# For numeric columns, fill missing values with 0
# For non-numeric columns, fill missing values with 'Nan'
for col in fantasy_rz_df.columns:
    if fantasy_rz_df[col].dtype == 'object':
        fantasy_rz_df[col] = fantasy_rz_df[col].fillna('Nan')
    else:
        fantasy_rz_df[col] = fantasy_rz_df[col].fillna(0)

# Remove '%' from columns and convert to float
percentage_cols = ['Ctch%', '%Tgt', 'Ctch%.1', '%Tgt.1']
for col in percentage_cols:
    fantasy_rz_df[col] = fantasy_rz_df[col].str.rstrip('%').astype('float') / 100.0

# Convert string columns to numeric where possible
for col in fantasy_rz_df.columns:
    fantasy_rz_df[col] = pd.to_numeric(fantasy_rz_df[col], errors='ignore')

# Rename columns (assume similar naming to previous dataset)
fantasy_rz_df = fantasy_rz_df.rename(columns={
    "Tm": "Team",
    "Tgt": "Red Zone Pass Targets",
    "Rec": "Red Zone Receptions",
    "Yds": "Red Zone Passing Yards",
    "TD": "Red Zone Passing Touchdowns",
    "Tgt.1": "Red Zone Targets",
    "Rec.1": "Red Zone Receptions",
    "Yds.1": "Red Zone Yards",
    "TD.1": "Red Zone Touchdowns",
    "Ctch%": "Red Zone Catch Percentage",
    "Y/Tgt": "Red Zone Yards per Target",
    "%Tgt": "Red Zone Target Percentage",
    "%Tgt.1": "Red Zone Target Percentage",
    "Ctch%.1": "Red Zone Catch Percentage",
    "Link": "Player Link",

})

# Display the first few rows to verify changes
fantasy_rz_df.head()
print(fantasy_rz_df.head(10))
#save to path 
fantasy_rz_df.to_csv('cleanstats/fantasy_rz.csv', index=False)
