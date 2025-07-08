import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.image as mpimg
import plotly.graph_objects as go


RS_Swing_Percentage = 0.491

#read csvs
data = pd.read_csv("RS_LH_IN_PULL.csv")
data2 = pd.read_csv("RS_LH_OUT_PULL.csv")
data3 = pd.read_csv("RS_RH_IN_PULL.csv")
data4 = pd.read_csv("RS_RH_OUT_PULL.csv")
data5 = pd.read_csv("RS_RH_INP.csv")
data6 = pd.read_csv("RS_LH_INP.csv")
data7 = pd.read_csv("RS_RH_BP.csv")
data8 = pd.read_csv("RS_LH_BP.csv")
data9 = pd.read_csv("RS_RH_BIP.csv")
data10 = pd.read_csv("RS_LH_BIP.csv")
data11 = pd.read_csv("RS_RH_TP.csv")
data12 = pd.read_csv("RS_LH_TP.csv")
data13 = pd.read_csv("RS_RH_MIDP.csv")
data14 = pd.read_csv("RS_LH_MIDP.csv")
data15 = pd.read_csv("RS_RH_MID_PULL.csv")
data16 = pd.read_csv("RS_LH_MID_PULL.csv")

#create dataframs
RS_LH_IN_PULL_df = pd.DataFrame(data)
RS_LH_OUT_PULL_df = pd.DataFrame(data2)
RS_RH_IN_PULL_df = pd.DataFrame(data3)
RS_RH_OUT_PULL_df = pd.DataFrame(data4)
RS_RH_INP_df = pd.DataFrame(data5)
RS_LH_INP_df = pd.DataFrame(data6)
RS_RH_BP_df = pd.DataFrame(data7)
RS_LH_BP_df = pd.DataFrame(data8)
RS_RH_BIP_df = pd.DataFrame(data9)
RS_LH_BIP_df = pd.DataFrame(data10)
RS_RH_TP_df = pd.DataFrame(data11)
RS_LH_TP_df = pd.DataFrame(data12)
RS_RH_MIDP_df = pd.DataFrame(data13)
RS_LH_MIDP_df = pd.DataFrame(data14)
RS_RH_MID_PULL_df = pd.DataFrame(data15)
RS_LH_MID_PULL_df = pd.DataFrame(data16)

#drop empty rows
RS_LH_IN_PULL_df = RS_LH_IN_PULL_df.dropna(subset=['ba', 'slg'])
RS_LH_OUT_PULL_df = RS_LH_OUT_PULL_df.dropna(subset=['ba', 'slg'])
RS_RH_IN_PULL_df = RS_RH_IN_PULL_df.dropna(subset=['ba', 'slg'])
RS_RH_OUT_PULL_df = RS_RH_OUT_PULL_df.dropna(subset=['ba', 'slg'])
RS_RH_MID_PULL_df = RS_RH_MID_PULL_df.dropna(subset=['ba', 'slg'])
RS_LH_MID_PULL_df = RS_LH_MID_PULL_df.dropna(subset=['ba', 'slg'])
RS_RH_INP_df = RS_RH_INP_df.dropna(subset=['pitches', 'total_pitches'])
RS_LH_INP_df = RS_LH_INP_df.dropna(subset=['pitches', 'total_pitches'])
RS_RH_BP_df = RS_RH_BP_df.dropna(subset=['pitches'])
RS_LH_BP_df = RS_LH_BP_df.dropna(subset=['pitches'])
RS_RH_BIP_df = RS_RH_BIP_df.dropna(subset=['pitches'])
RS_LH_BIP_df = RS_LH_BIP_df.dropna(subset=['pitches'])
RS_RH_TP_df = RS_RH_TP_df.dropna(subset=['pitches'])
RS_LH_TP_df = RS_LH_TP_df.dropna(subset=['pitches'])
RS_RH_MIDP_df = RS_RH_MIDP_df.dropna(subset=['pitches'])
RS_LH_MIDP_df = RS_LH_MIDP_df.dropna(subset=['pitches'])

#calculate team averages
RS_LH_IN_PULL_BA = np.average(RS_LH_IN_PULL_df['ba'], weights=RS_LH_IN_PULL_df['pitches'])
RS_LH_IN_PULL_SLG = np.average(RS_LH_IN_PULL_df['slg'], weights=RS_LH_IN_PULL_df['pitches'])

RS_LH_OUT_PULL_BA = np.average(RS_LH_OUT_PULL_df['ba'], weights=RS_LH_OUT_PULL_df['pitches'])
RS_LH_OUT_PULL_SLG = np.average(RS_LH_OUT_PULL_df['slg'], weights=RS_LH_OUT_PULL_df['pitches'])

RS_RH_IN_PULL_BA = np.average(RS_RH_IN_PULL_df['ba'], weights=RS_RH_IN_PULL_df['pitches'])
RS_RH_IN_PULL_SLG = np.average(RS_RH_IN_PULL_df['slg'], weights=RS_RH_IN_PULL_df['pitches'])

RS_RH_OUT_PULL_BA = np.average(RS_RH_OUT_PULL_df['ba'], weights=RS_RH_OUT_PULL_df['pitches'])
RS_RH_OUT_PULL_SLG = np.average(RS_RH_OUT_PULL_df['slg'], weights=RS_RH_OUT_PULL_df['pitches'])

RS_RH_MID_PULL_BA = np.average(RS_RH_MID_PULL_df['ba'], weights=RS_RH_MID_PULL_df['pitches'])
RS_RH_MID_PULL_SLG = np.average(RS_RH_MID_PULL_df['slg'], weights=RS_RH_MID_PULL_df['pitches'])

RS_LH_MID_PULL_BA = np.average(RS_LH_MID_PULL_df['ba'], weights=RS_LH_MID_PULL_df['pitches'])
RS_LH_MID_PULL_SLG = np.average(RS_LH_MID_PULL_df['slg'], weights=RS_LH_MID_PULL_df['pitches'])


#clean data frames
RS_LH_IN_PULL_df = RS_LH_IN_PULL_df[['player_name', 'ba', 'slg']]
RS_LH_OUT_PULL_df = RS_LH_OUT_PULL_df[['player_name', 'ba', 'slg']]
RS_RH_IN_PULL_df = RS_RH_IN_PULL_df[['player_name', 'ba', 'slg']]
RS_RH_OUT_PULL_df = RS_RH_OUT_PULL_df[['player_name', 'ba', 'slg']]
RS_RH_MID_PULL_df = RS_RH_MID_PULL_df[['player_name', 'ba', 'slg']]
RS_LH_MID_PULL_df = RS_LH_MID_PULL_df[['player_name', 'ba', 'slg']]

RS_RH_BP_df = RS_RH_BP_df[['player_name', 'pitches']]
RS_LH_BP_df = RS_LH_BP_df[['player_name', 'pitches']]
RS_RH_BIP_df = RS_RH_BIP_df[['player_name', 'pitches']]
RS_LH_BIP_df = RS_LH_BIP_df[['player_name', 'pitches']]
RS_RH_TP_df = RS_RH_TP_df[['player_name', 'pitches']]
RS_LH_TP_df = RS_LH_TP_df[['player_name', 'pitches']]

RS_RH_MIDP_df = RS_RH_MIDP_df[['player_name', 'pitches']]
RS_LH_MIDP_df = RS_LH_MIDP_df[['player_name', 'pitches']]

#rename columns for cleaner merging
RS_LH_IN_PULL_df = RS_LH_IN_PULL_df.rename(columns={
    'ba': 'ba1',
    'slg' : 'slg1'
})

RS_RH_IN_PULL_df = RS_RH_IN_PULL_df.rename(columns={
    'ba': 'ba1',
    'slg' : 'slg1'
})

RS_RH_BP_df = RS_RH_BP_df.rename(columns={
    'pitches': 'BP_pitches'
})
RS_LH_BP_df = RS_LH_BP_df.rename(columns={
    'pitches': 'BP_pitches'
})

RS_RH_TP_df = RS_RH_TP_df.rename(columns={
    'pitches': 'TP_pitches'
})
RS_LH_TP_df = RS_LH_TP_df.rename(columns={
    'pitches': 'TP_pitches'
})

RS_LH_MID_PULL_df = RS_LH_MID_PULL_df.rename(columns={
     'ba': 'ba2',
    'slg' : 'slg2'

})
RS_RH_MID_PULL_df = RS_RH_MID_PULL_df.rename(columns={
     'ba': 'ba2',
    'slg' : 'slg2'

})

RS_LH_MIDP_df = RS_LH_MIDP_df.rename(columns={
    'pitches': 'MID_pitches'
})
RS_RH_MIDP_df = RS_RH_MIDP_df.rename(columns={
    'pitches': 'MID_pitches'
})

RS_LH_TP_df = pd.merge(RS_LH_MIDP_df,RS_LH_TP_df, on=['player_name'] )
RS_RH_TP_df = pd.merge(RS_RH_MIDP_df,RS_RH_TP_df, on=['player_name'] )
RS_LH_INP_df = pd.merge(RS_LH_INP_df,RS_LH_TP_df, on=['player_name'] )
RS_RH_INP_df = pd.merge(RS_RH_INP_df,RS_RH_TP_df, on=['player_name'] )
LH_inside_pitch_percent = (np.sum(RS_LH_INP_df['pitches']))/(np.sum(RS_LH_INP_df['TP_pitches']))
LH_middle_pitch_percent = (np.sum(RS_LH_INP_df['MID_pitches']))/(np.sum(RS_LH_INP_df['TP_pitches']))
LH_outside_pitch_percent = 1 - (LH_inside_pitch_percent + LH_middle_pitch_percent)
RH_inside_pitch_percent = (np.sum(RS_RH_INP_df['pitches']))/(np.sum(RS_RH_INP_df['TP_pitches']))
RH_middle_pitch_percent = (np.sum(RS_RH_INP_df['MID_pitches']))/(np.sum(RS_RH_INP_df['TP_pitches']))
RH_outside_pitch_percent = 1 - (RH_inside_pitch_percent + RH_middle_pitch_percent)
RS_LH_INP_df['Inside Pitch %'] = round(RS_LH_INP_df['pitches'] / RS_LH_INP_df['TP_pitches'],2)
RS_LH_INP_df['Middle Pitch %'] = round(RS_LH_INP_df['MID_pitches'] / RS_LH_INP_df['TP_pitches'],2)
RS_LH_INP_df['Outside Pitch %'] = round(1-(RS_LH_INP_df['Inside Pitch %']+RS_LH_INP_df['Middle Pitch %']),2)
RS_RH_INP_df['Inside Pitch %'] = round(RS_RH_INP_df['pitches'] / RS_RH_INP_df['TP_pitches'],2)
RS_RH_INP_df['Middle Pitch %'] = round(RS_RH_INP_df['MID_pitches'] / RS_RH_INP_df['TP_pitches'],2)
RS_RH_INP_df['Outside Pitch %'] = round(1-(RS_RH_INP_df['Inside Pitch %']+RS_RH_INP_df['Middle Pitch %']),2)

RS_RH_INP_df = RS_RH_INP_df[['player_name', 'Inside Pitch %', 'Middle Pitch %', 'Outside Pitch %']]
RS_LH_INP_df = RS_LH_INP_df[['player_name', 'Inside Pitch %', 'Middle Pitch %', 'Outside Pitch %']]

LH_merged_df = pd.merge(RS_LH_IN_PULL_df, RS_LH_OUT_PULL_df, on=['player_name'])
LH_merged_df = pd.merge(LH_merged_df, RS_LH_MID_PULL_df, on=['player_name'])
RH_merged_df = pd.merge(RS_RH_IN_PULL_df, RS_RH_OUT_PULL_df, on=['player_name'])
RH_merged_df = pd.merge(RH_merged_df, RS_RH_MID_PULL_df, on=['player_name'])
RH_PULL_merged_df = pd.merge(RS_RH_BP_df,RS_RH_BIP_df, on=['player_name'])
LH_PULL_merged_df = pd.merge(RS_LH_BP_df,RS_LH_BIP_df, on=['player_name'])

LH_PULL_percent = (np.sum(LH_PULL_merged_df['BP_pitches']))/(np.sum(LH_PULL_merged_df['pitches']))
RH_PULL_percent = (np.sum(RH_PULL_merged_df['BP_pitches']))/(np.sum(RH_PULL_merged_df['pitches']))
RH_PULL_merged_df['Pull %'] = round(RH_PULL_merged_df['BP_pitches']/RH_PULL_merged_df['pitches'],2)
LH_PULL_merged_df['Pull %'] = round(LH_PULL_merged_df['BP_pitches']/LH_PULL_merged_df['pitches'],2)

RH_PULL_merged_df = RH_PULL_merged_df[['player_name', 'Pull %']]
LH_PULL_merged_df = LH_PULL_merged_df[['player_name', 'Pull %']]

LH_merged_df = pd.merge(LH_merged_df, LH_PULL_merged_df, on=['player_name'])
RH_merged_df = pd.merge(RH_merged_df, RH_PULL_merged_df, on=['player_name'])
LH_merged_df = pd.merge(LH_merged_df, RS_LH_INP_df, on=['player_name'])
RH_merged_df = pd.merge(RH_merged_df, RS_RH_INP_df, on=['player_name'])


#rename columns to final presentation names
LH_merged_df = LH_merged_df.rename(columns={
    'player_name':'Player Name',
    'ba1': 'BA (Inside Pitches)',
    'ba': 'BA (Outside Pitches)',
    'slg1': 'SLG (Inside Pitches)',
    'slg': 'SLG (Outside Pitches)',
    'ba2' : 'BA (Middle Pitches)',
    'slg2' : 'SLG (Middle Pitches)'
})

RH_merged_df = RH_merged_df.rename(columns={
    'player_name':'Player Name',
    'ba1': 'BA (Inside Pitches)',
    'ba': 'BA (Outside Pitches)',
    'slg1': 'SLG (Inside Pitches)',
    'slg': 'SLG (Outside Pitches)',
    'ba2' : 'BA (Middle Pitches)',
    'slg2' : 'SLG (Middle Pitches)'
})

#reorder data frame
LH_merged_df = LH_merged_df[['Player Name', 'BA (Inside Pitches)', 'BA (Middle Pitches)','BA (Outside Pitches)',  'SLG (Inside Pitches)', 'SLG (Middle Pitches)', 'SLG (Outside Pitches)','Inside Pitch %','Middle Pitch %', 'Outside Pitch %', 'Pull %']]
RH_merged_df = RH_merged_df[['Player Name', 'BA (Inside Pitches)', 'BA (Middle Pitches)', 'BA (Outside Pitches)', 'SLG (Inside Pitches)', 'SLG (Middle Pitches)', 'SLG (Outside Pitches)', 'Inside Pitch %', 'Middle Pitch %', 'Outside Pitch %', 'Pull %']]

#create team average data frames to merge
LH_team_avg_row = {
    'Player Name': 'Team Stats',
    'BA (Inside Pitches)': round(RS_LH_IN_PULL_BA,3), 
    'BA (Middle Pitches)' : round(RS_LH_MID_PULL_BA,3),   
    'BA (Outside Pitches)': round(RS_LH_OUT_PULL_BA,3),
    'SLG (Inside Pitches)': round(RS_LH_IN_PULL_SLG,3), 
    'SLG (Middle Pitches)' : round(RS_LH_MID_PULL_SLG,3), 
    'SLG (Outside Pitches)': round(RS_LH_OUT_PULL_SLG,3), 
    'Inside Pitch %': round(LH_inside_pitch_percent,2),
    'Middle Pitch %': round(LH_middle_pitch_percent,2),
    'Outside Pitch %': round(LH_outside_pitch_percent,2),
    'Pull %': round(LH_PULL_percent,2)
}

RH_team_avg_row = {
    'Player Name': 'Team Stats',
    'BA (Inside Pitches)': round(RS_RH_IN_PULL_BA,3), 
    'BA (Middle Pitches)' : round(RS_RH_MID_PULL_BA,3),      
    'BA (Outside Pitches)': round(RS_RH_OUT_PULL_BA,3), 
    'SLG (Inside Pitches)': round(RS_RH_IN_PULL_SLG,3),
    'SLG (Middle Pitches)' : round(RS_RH_MID_PULL_SLG,3), 
    'SLG (Outside Pitches)': round(RS_LH_OUT_PULL_SLG,3),
    'Inside Pitch %': round(RH_inside_pitch_percent,2),
    'Middle Pitch %': round(RH_middle_pitch_percent,2),
    'Outside Pitch %': round(RH_outside_pitch_percent,2),
    'Pull %': round(RH_PULL_percent ,2) 
}

#add team average rows onto data frame

LH_merged_df = pd.concat([LH_merged_df, pd.DataFrame([LH_team_avg_row])], ignore_index=True)
RH_merged_df = pd.concat([RH_merged_df, pd.DataFrame([RH_team_avg_row])], ignore_index=True)


#create and display table of player's BA and SLG
def plotTable(name, df):
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns),
                    fill_color='paleturquoise',
                    align='center'),
        cells=dict(values=[df[col] for col in df.columns],
                   fill_color='lavender',
                   align='center'))
    ])

    fig.update_layout(
        title_text=f"{name}<br>Red Sox Team Swing Percentage: {RS_Swing_Percentage:.3f}",
        title_x=0.5,
        width=1000,
        height=600
    )

    fig.show()

# function calls
plotTable("Red Sox LHH Pulled Pitches", LH_merged_df)
plotTable("Red Sox RHH Pulled Pitches", RH_merged_df)



