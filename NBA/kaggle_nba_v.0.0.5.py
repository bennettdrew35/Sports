import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

df = pd.read_csv("2017-18_officialBoxScore.csv")


df['game_Time'] = pd.to_datetime(df['gmDate'] + ' ' + df['gmTime'])

df2_col = ['game_Time', 'teamAbbr', 'teamLoc', 'teamRslt', 'teamMin',
           'teamPTS1', 'teamPTS2', 'teamPTS3', 'teamPTS4', 'teamPTS5', 'teamPTS6', 'teamPTS7', 'teamPTS8']
df2 = df[df2_col]

df2 = df2.groupby(['game_Time', 'teamAbbr', 'teamLoc', 'teamRslt']).mean().reset_index()

#Create excel workbook
writer = pd.ExcelWriter(r"NBA_Info.xlsx", engine='xlsxwriter')

"""
First Half
"""

first_col = ['game_Time', 'teamAbbr', 'teamLoc', 'teamRslt',
             'teamPTS1', 'teamPTS2']
first_df = df2[first_col]
first_sum = [col for col in first_df if col.startswith('teamPTS')]
first_df['first_Half_PTS'] = first_df[first_sum].sum(axis=1)
first_std = first_df.groupby(['teamAbbr'])['first_Half_PTS'].std().reset_index().rename(columns={'first_Half_PTS':'first_Half_PTS_Std'})
first_mean = first_df.groupby(['teamAbbr'])['first_Half_PTS'].mean().reset_index().rename(columns={'first_Half_PTS':'first_Half_PTS_Mean'})
first_df2 = first_df.merge(first_std, on='teamAbbr')
first_df3 = first_df2.merge(first_mean, on='teamAbbr')
first_df3['diff_From_Mean'] = (first_df3['first_Half_PTS'] - first_df3['first_Half_PTS_Mean']).abs()
first_df3.to_excel(writer, sheet_name='First_Half', index=False)
print(first_df3.head())
"""
Second Half
"""

sec_col = ['game_Time', 'teamAbbr', 'teamLoc', 'teamRslt',
           'teamPTS3', 'teamPTS4', 'teamPTS5', 'teamPTS6', 'teamPTS7', 'teamPTS8']
sec_df = df2[sec_col]
sec_sum = [col for col in sec_df if col.startswith('teamPTS')]
sec_df['sec_Half_PTS'] = sec_df[sec_sum].sum(axis=1)
sec_std = sec_df.groupby(['teamAbbr'])['sec_Half_PTS'].std().reset_index().rename(columns={'sec_Half_PTS':'sec_Half_PTS_Std'})
sec_mean = sec_df.groupby(['teamAbbr'])['sec_Half_PTS'].mean().reset_index().rename(columns={'sec_Half_PTS':'sec_Half_PTS_Mean'})
sec_df2 = sec_df.merge(sec_std, on='teamAbbr')
sec_df3 = sec_df2.merge(sec_mean, on='teamAbbr')
sec_df3['diff_From_Mean'] = (sec_df3['sec_Half_PTS'] - sec_df3['sec_Half_PTS_Mean']).abs()
sec_df3.to_excel(writer, sheet_name='Second_Half', index=False)
"""
Full Game
"""
full_col = ['game_Time', 'teamAbbr', 'teamLoc', 'teamRslt',
            'teamPTS1', 'teamPTS2', 'teamPTS3', 'teamPTS4', 'teamPTS5', 'teamPTS6', 'teamPTS7', 'teamPTS8']
full_df = df2[full_col]
full_sum = [col for col in full_df if col.startswith('teamPTS')]
full_df['full_Game_PTS'] = full_df[full_sum].sum(axis=1)
full_std = full_df.groupby(['teamAbbr'])['full_Game_PTS'].std().reset_index().rename(columns={'full_Game_PTS':'full_Game_PTS_Std'})
full_mean = full_df.groupby(['teamAbbr'])['full_Game_PTS'].mean().reset_index().rename(columns={'full_Game_PTS':'full_Game_PTS_Mean'})
full_df2 = full_df.merge(full_std, on='teamAbbr')
full_df3 = full_df2.merge(full_mean, on='teamAbbr')
full_df3['diff_From_Mean'] = (full_df3['full_Game_PTS'] - full_df3['full_Game_PTS_Mean']).abs()
full_df3.to_excel(writer, sheet_name='Full_Game', index=False)
"""
Regulation Time
"""
reg_col = ['game_Time', 'teamAbbr', 'teamLoc', 'teamRslt','teamMin']
reg_df = df2[reg_col]
reg_std = reg_df.groupby(['teamAbbr'])['teamMin'].std().reset_index().rename(columns={'teamMin':'teamMin_Std'})
reg_mean = reg_df.groupby(['teamAbbr'])['teamMin'].mean().reset_index().rename(columns={'teamMin':'teamMin_Mean'})
reg_df2 = reg_df.merge(reg_std, on='teamAbbr')
reg_df3 = reg_df2.merge(reg_mean, on='teamAbbr')
reg_df3['diff_From_Mean'] = (reg_df3['teamMin'] - reg_df3['teamMin_Mean']).abs()
reg_df3.to_excel(writer, sheet_name='Regulation_Time', index=False)
print(reg_df3.head())

#save excel file
writer.save()

