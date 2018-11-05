import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import pdist, squareform
df = pd.read_csv("2017-18_officialBoxScore.csv")
df['game_Time'] = pd.to_datetime(df['gmDate'] + ' ' + df['gmTime'])
df2_col = ['game_Time', 'teamAbbr', 'teamLoc', 'teamRslt', 'teamRslt', 'teamMin',
           'teamPTS1', 'teamPTS2', 'teamPTS3', 'teamPTS4', 'teamPTS5', 'teamPTS6', 'teamPTS7', 'teamPTS8']
df2 = df[df2_col]
df2 = df2.groupby(['game_Time', 'teamAbbr', 'teamLoc',]).mean().reset_index()
df2["Game_Number"] = df2.groupby(['teamAbbr', 'game_Time']).cumcount()+1
#Create excel workbook
writer = pd.ExcelWriter(r"NBA_Distance_Info.xlsx", engine='xlsxwriter')
"""
First Half
"""
first_index = []
for i in range(1,3322):
    first_index.append("D" + str(i))
first_sum = ['teamPTS1', 'teamPTS2']
df2['first_Half_PTS'] = df[first_sum].sum(axis=1)
first_df = df2.groupby('teamAbbr')[['Game_Number', 'first_Half_PTS']].apply(lambda x: pd.Series(pdist(x), index=first_index))
first_df.to_excel(writer, sheet_name='First_Half_Dist')
"""
Second Half
"""
sec_sum = ['teamPTS3', 'teamPTS4', 'teamPTS5', 'teamPTS6', 'teamPTS7', 'teamPTS8']
df2['sec_Half_PTS'] = df[sec_sum].sum(axis=1)
sec_index = []
for i in range(1,3322):
    sec_index.append("D" + str(i))
sec_df = df2.groupby('teamAbbr')[['Game_Number', 'sec_Half_PTS']].apply(lambda x: pd.Series(pdist(x), index=sec_index))
sec_df.to_excel(writer, sheet_name='Second_Half_Dist')
"""
Full Game
"""
full_sum = ['teamPTS1', 'teamPTS2', 'teamPTS3', 'teamPTS4', 'teamPTS5', 'teamPTS6', 'teamPTS7', 'teamPTS8']
df2['full_Game_PTS'] = df[full_sum].sum(axis=1)
full_index = []
for i in range(1,3322):
    full_index.append("D" + str(i))
full_df = df2.groupby('teamAbbr')[['Game_Number', 'full_Game_PTS']].apply(lambda x: pd.Series(pdist(x), index=full_index))
full_df.to_excel(writer, sheet_name='Full_Game_Dist')
"""
Regulation Time
"""
reg_index = []
for i in range(1,3322):
    reg_index.append("D" + str(i))
reg_df = df2.groupby('teamAbbr')[['Game_Number', 'teamMin']].apply(lambda x: pd.Series(pdist(x), index=reg_index))
reg_df.to_excel(writer, sheet_name='Regulation_Time_Dist')
#save excel file
writer.save()