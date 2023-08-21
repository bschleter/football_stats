import pandas as pd
import os

# Get the absolute path to the file
file_path = os.path.abspath('stat_csv/fantasy.csv')

# Load the data
fantasy_df = pd.read_csv((file_path), header=1)

# Handle missing values
# For numeric columns, fill missing values with 0
# For non-numeric columns, fill missing values with 'Nan'
for col in fantasy_df.columns:
    if fantasy_df[col].dtype == 'object':
        fantasy_df[col] = fantasy_df[col].fillna(0)

# Convert string columns to numeric where possible
for col in fantasy_df.columns:
    fantasy_df[col] = pd.to_numeric(fantasy_df[col], errors='ignore')

# Rename columns
# Rename more columns
fantasy_df = fantasy_df.rename(columns={
    "Tm": "Team",
    "FantPos": "Fantasy Position ;)",
    "G": "Games",
    "GS": "Games Started",
    "Cmp": "Completions",
    "Att": "Passing Attempts",
    "Yds": "Passing Yards",
    "TD": "Passing Touchdowns",
    "Int": "Interceptions",
    "Att.1": "Rushing Attempts",
    "Yds.1": "Rushing Yards",
    "Y/A": "Yards Per Attempt",
    "TD.1": "Rushing Touchdowns",
    "Tgt": "Pass Targets",
    "Rec": "Receptions",
    "Yds.2": "Receiving Yards",
    "Y/R": "Yards Per Reception",
    "TD.2": "Receiving Touchdowns",
    "Fmb": "Fumbles",
    "FL": "Fumbles Lost",
    "TD.3": "Touchdowns Of All Types",
    "2PM": "Two Point Conversion Made",
    "2PP": "Two Point Conversion Passes",
    "FantPt": "Fantasy Points",
    "PPR": "PPR Scoring Points",
    "DKPt": "Draft Kings Scoring Points",
    "FDPt": "FanDuelScoring Points",
    "VBD": "Baseline Fantasy Points Score",
    "PosRank": "Position Rank",
    "OvRank": "Overall Rank"

})

# Display the first few rows to verify changes
fantasy_df.head()
print(fantasy_df.head(10))
fantasy_df.to_csv('cleanstats/fantasy.csv', index=False)
