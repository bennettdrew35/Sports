import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import datetime

df = pd.read_csv(r"/home/drew/PycharmProjects/Sports/NBA/2017-18_officialBoxScore.csv")


df['game_Time'] = pd.to_datetime(df['gmDate'] + ' ' + df['gmTime'])

df2_col = ['game_Time', 'teamAbbr', 'teamLoc', 'teamRslt', 'teamMin',
           'teamPTS1', 'teamPTS2', 'teamPTS3', 'teamPTS4', 'teamPTS5', 'teamPTS6', 'teamPTS7', 'teamPTS8']
df2 = df[df2_col]

df2 = df2.groupby(['game_Time', 'teamAbbr', 'teamLoc', 'teamRslt']).mean()

print(df2.head())

"""
First Half
"""

first_col = ['game_Time', 'teamAbbr', 'teamLoc', 'teamRslt',
             'teamPTS1', 'teamPTS2']
first_df = df[first_col]

first_df['first_HalfPTS'] = first_df['teamPTS1'] + first_df['teamPTS2']

"""
Second Half
"""

sec_col = ['game_Time', 'teamAbbr', 'teamLoc', 'teamRslt',
           'teamPTS3', 'teamPTS4', 'teamPTS5', 'teamPTS6', 'teamPTS7', 'teamPTS8']
sec_df = df[sec_col]

sec_df['second_HalfPTS'] = sec_df['teamPTS3'] + sec_df['teamPTS4'] + sec_df['teamPTS5'] + sec_df['teamPTS6'] + sec_df['teamPTS7'] + sec_df['teamPTS8']

"""
Full Game
"""

full_col = ['game_Time', 'teamAbbr', 'teamLoc', 'teamRslt',
           'teamPTS3', 'teamPTS4', 'teamPTS5', 'teamPTS6', 'teamPTS7', 'teamPTS8']
full_df = df[full_col]

full_df['full_GamePTS'] = first_df['teamPTS1'] + first_df['teamPTS2'] + sec_df['teamPTS3'] + sec_df['teamPTS4'] + sec_df['teamPTS5'] + sec_df['teamPTS6'] + sec_df['teamPTS7'] + sec_df['teamPTS8']
print(full_df)
