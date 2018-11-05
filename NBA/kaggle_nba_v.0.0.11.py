import pandas as pd
from scipy.spatial.distance import pdist
df = pd.read_csv("2017-18_officialBoxScore.csv")
df['game_Time'] = pd.to_datetime(df['gmDate'] + ' ' + df['gmTime'])
df_col = ['game_Time', 'teamAbbr', 'teamLoc', 'teamMin',
           'teamPTS1', 'teamPTS2', 'teamPTS3', 'teamPTS4', 'teamPTS5', 'teamPTS6', 'teamPTS7', 'teamPTS8']
df2 = df[df_col]
df2 = df2.groupby(['game_Time', 'teamAbbr', 'teamLoc',]).mean().reset_index()
df2["Game_Number"] = df2.groupby(['teamAbbr']).cumcount()+1
df2_col = ['game_Time', 'teamAbbr', 'teamLoc', 'Game_Number', 'teamMin',
           'teamPTS1', 'teamPTS2', 'teamPTS3', 'teamPTS4', 'teamPTS5', 'teamPTS6', 'teamPTS7', 'teamPTS8']
df2 = df2[df2_col]
#set index
index = ["D" + str(i) for i in range(1,3322)]
"""
First Half
"""
first_sum = ['teamPTS1', 'teamPTS2']
df2['first_Half_PTS'] = df2[first_sum].sum(axis=1)
first_df = df2.groupby('teamAbbr')[['Game_Number', 'first_Half_PTS']].apply(lambda x: pd.Series(pdist(x), index=index))
"""
Second Half
"""
sec_sum = ['teamPTS3', 'teamPTS4', 'teamPTS5', 'teamPTS6', 'teamPTS7', 'teamPTS8']
df2['sec_Half_PTS'] = df2[sec_sum].sum(axis=1)
sec_index = ["D" + str(i) for i in range(1,3322)]
sec_df = df2.groupby('teamAbbr')[['Game_Number', 'sec_Half_PTS']].apply(lambda x: pd.Series(pdist(x), index=index))
"""
Full Game
"""
full_sum = ['teamPTS1', 'teamPTS2', 'teamPTS3', 'teamPTS4', 'teamPTS5', 'teamPTS6', 'teamPTS7', 'teamPTS8']
df2['full_Game_PTS'] = df2[full_sum].sum(axis=1)
full_df = df2.groupby('teamAbbr')[['Game_Number', 'full_Game_PTS']].apply(lambda x: pd.Series(pdist(x), index=index))
"""
Regulation Time
"""
reg_df = df2.groupby('teamAbbr')[['Game_Number', 'teamMin']].apply(lambda x: pd.Series(pdist(x), index=index))
"""
Save Excel File
"""
writer = pd.ExcelWriter("NBA_Distance_Info.xlsx", engine='xlsxwriter')
df2.to_excel(writer, sheet_name='Games_Info', index=False)
first_df.to_excel(writer, sheet_name='First_Half_Dist')
sec_df.to_excel(writer, sheet_name='Second_Half_Dist')
full_df.to_excel(writer, sheet_name='Full_Game_Dist')
reg_df.to_excel(writer, sheet_name='Regulation_Time_Dist')
writer.save()