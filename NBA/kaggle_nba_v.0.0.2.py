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

df2 = df2.groupby(['game_Time', 'teamAbbr', 'teamLoc', 'teamRslt']).mean().reset_index()

"""
First Half
"""

first_col = ['game_Time', 'teamAbbr', 'teamLoc', 'teamRslt',
             'teamPTS1', 'teamPTS2']
first_df = df2[first_col]
first_sum = [col for col in first_df if col.startswith('teamPTS')]
first_df['first_HalfPTS'] = first_df[first_sum].sum(axis=1)
print(first_df.head())
"""
Second Half
"""

sec_col = ['game_Time', 'teamAbbr', 'teamLoc', 'teamRslt',
           'teamPTS3', 'teamPTS4', 'teamPTS5', 'teamPTS6', 'teamPTS7', 'teamPTS8']
sec_df = df2[sec_col]
sec_sum = [col for col in sec_df if col.startswith('teamPTS')]
sec_df['second_HalfPTS'] = sec_df[sec_sum].sum(axis=1)
print(sec_df.head())
"""
Full Game
"""

full_col = ['game_Time', 'teamAbbr', 'teamLoc', 'teamRslt',
            'teamPTS1', 'teamPTS2', 'teamPTS3', 'teamPTS4', 'teamPTS5', 'teamPTS6', 'teamPTS7', 'teamPTS8']
full_df = df2[full_col]
full_sum = [col for col in full_df if col.startswith('teamPTS')]
full_df['full_GamePTS'] = full_df[full_sum].sum(axis=1)
print(full_df.head())

"""
Regulation Time
"""
reg_col = ['game_Time', 'teamAbbr', 'teamLoc', 'teamRslt','teamMin']
reg_df = df2[reg_col]
print(reg_df.head())