import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import datetime

df = pd.read_csv(r"/home/drew/PycharmProjects/Sports/NBA/2017-18_officialBoxScore.csv")


df['game_Time'] = pd.to_datetime(df['gmDate'] + ' ' + df['gmTime'])

df2_col = ['game_Time', 'teamAbbr', 'teamLoc', 'teamRslt',
           'teamPTS1', 'teamPTS2', 'teamPTS3', 'teamPTS4', 'teamPTS5', 'teamPTS6', 'teamPTS7', 'teamPTS8']
df2 = df[df2_col]

df2 = df2.groupby(['game_Time', 'teamAbbr', 'teamLoc', 'teamRslt']).mean()

print(df2.head())

first_col = ['game_Time', 'teamAbbr', 'teamLoc', 'teamRslt',
             'teamPTS1', 'teamPTS2']
first_df = df[first_col]

first_df[]