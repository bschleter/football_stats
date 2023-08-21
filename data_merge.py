import pandas as pd
import os

pd.df = pd.read_csv('cleanstats/passing.csv')
df1 = pd.read_csv('cleanstats/receiving.csv')
df2 = pd.read_csv('cleanstats/advanced_air_yards.csv')
df3 = pd.read_csv('cleanstats/rushing.csv')
df4 = pd.read_csv('cleanstats/fantasy.csv')
df5 = pd.read_csv('cleanstats/fantasy_rz.csv')

# Add more dataframes as needed
merged_df = pd.merge(df1, df2, on=['player name', 'team name', 'games', 'games started'], how='outer')
merged_df = pd.merge(merged_df, df3, on=['player name', 'team name', 'games', 'games started'], how='outer')
# Add more merge operations as needed
