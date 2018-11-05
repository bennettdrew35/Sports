import pandas as pd
from scipy.spatial.distance import pdist, squareform
import numpy as np
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
full_dum = pd.get_dummies(full_df3['diff_From_Mean'])
full_df_com = pd.concat([df['teamAbbr'], full_dum], axis=1)
full_grp = full_df_com.groupby('teamAbbr').sum()
full_s_dist = squareform(pdist(full_grp, metric="jaccard"))
np.fill_diagonal(full_s_dist, np.nan)
full_sim = np.subtract(1, full_s_dist)
full_df_sim = pd.DataFrame(full_sim, columns=full_grp.index, index=full_grp.index)
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
full_dum = pd.get_dummies(full_df3['diff_From_Mean'])
full_df_com = pd.concat([df['teamAbbr'], full_dum], axis=1)
full_grp = full_df_com.groupby('teamAbbr').sum()
full_s_dist = squareform(pdist(full_grp, metric="jaccard"))
np.fill_diagonal(full_s_dist, np.nan)
full_sim = np.subtract(1, full_s_dist)
full_df_sim = pd.DataFrame(full_sim, columns=full_grp.index, index=full_grp.index)
"""
Regulation Time
"""
reg_col = ['game_Time', 'teamAbbr', 'teamLoc','teamMin']
reg_df = df2[reg_col]
reg_std = reg_df.groupby(['teamAbbr'])['teamMin'].std().reset_index().rename(columns={'teamMin':'teamMin_Std'})
reg_mean = reg_df.groupby(['teamAbbr'])['teamMin'].mean().reset_index().rename(columns={'teamMin':'teamMin_Mean'})
reg_df2 = reg_df.merge(reg_std, on='teamAbbr')
reg_df3 = reg_df2.merge(reg_mean, on='teamAbbr')
reg_df3['diff_From_Mean'] = (reg_df3['teamMin'] - reg_df3['teamMin_Mean']).abs().round(0)
reg_dum = pd.get_dummies(reg_df3['diff_From_Mean'])
reg_df_com = pd.concat([df['teamAbbr'], reg_dum], axis=1)
reg_grp = reg_df_com.groupby('teamAbbr').sum()
reg_s_dist = squareform(pdist(reg_grp, metric="jaccard"))
np.fill_diagonal(reg_s_dist, np.nan)
reg_sim = np.subtract(1, reg_s_dist)
reg_df_sim = pd.DataFrame(reg_sim, columns=reg_grp.index, index=reg_grp.index)

"""
Save Excel File
"""
writer = pd.ExcelWriter("NBA_Relationship_Info.xlsx", engine='xlsxwriter')
df2.to_excel(writer, sheet_name='Games_Info', index=False)
first_df_sim.to_excel(writer, sheet_name='First_Half_Dist')
sec_df_sim.to_excel(writer, sheet_name='Second_Half_Dist')
full_df_sim.to_excel(writer, sheet_name='Full_Game_Dist')
reg_df_sim.to_excel(writer, sheet_name='Regulation_Time_Dist')
writer.save()