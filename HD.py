import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
import numpy as np

img = mpimg.imread('GenericBaseballField.jpg')

# Read your data
data = pd.read_csv("CSVs\LH_IN_OPP.csv")
data2 = pd.read_csv("CSVs\LH_IN_STR.csv")
data3 = pd.read_csv("CSVs\LH_IN_PULL.csv")
data4 = pd.read_csv("CSVs\LH_MID_OPP.csv")
data5 = pd.read_csv("CSVs\LH_MID_STR.csv")
data6 = pd.read_csv("CSVs\LH_MID_PULL.csv")
data7 = pd.read_csv("CSVs\LH_OUT_OPP.csv")
data8 = pd.read_csv("CSVs\LH_OUT_STR.csv")
data9 = pd.read_csv("CSVs\LH_OUT_PULL.csv")
data10 = pd.read_csv("CSVs\RH_IN_OPP.csv")
data11 = pd.read_csv("CSVs\RH_IN_STR.csv")
data12 = pd.read_csv("CSVs\RH_IN_PULL.csv")
data13 = pd.read_csv("CSVs\RH_MID_OPP.csv")
data14 = pd.read_csv("CSVs\RH_MID_STR.csv")
data15 = pd.read_csv("CSVs\RH_MID_PULL.csv")
data16 = pd.read_csv("CSVs\RH_OUT_OPP.csv")
data17 = pd.read_csv("CSVs\RH_OUT_STR.csv")
data18 = pd.read_csv("CSVs\RH_OUT_PULL.csv")


# create DataFrames
LH_IN_OPP_df = pd.DataFrame(data)
LH_IN_STR_df = pd.DataFrame(data2)
LH_IN_PULL_df = pd.DataFrame(data3)
LH_MID_OPP_df = pd.DataFrame(data4)
LH_MID_STR_df = pd.DataFrame(data5)
LH_MID_PULL_df = pd.DataFrame(data6)
LH_OUT_OPP_df = pd.DataFrame(data7)
LH_OUT_STR_df = pd.DataFrame(data8)
LH_OUT_PULL_df = pd.DataFrame(data9)
RH_IN_OPP_df = pd.DataFrame(data10)
RH_IN_STR_df = pd.DataFrame(data11)
RH_IN_PULL_df = pd.DataFrame(data12)
RH_MID_OPP_df = pd.DataFrame(data13)
RH_MID_STR_df = pd.DataFrame(data14)
RH_MID_PULL_df = pd.DataFrame(data15)
RH_OUT_OPP_df = pd.DataFrame(data16)
RH_OUT_STR_df = pd.DataFrame(data17)
RH_OUT_PULL_df = pd.DataFrame(data18)

#remove empty rows
LH_IN_OPP_df = LH_IN_OPP_df.dropna(subset=['ba', 'slg'])
LH_IN_STR_df = LH_IN_STR_df.dropna(subset=['ba', 'slg'])
LH_IN_PULL_df = LH_IN_PULL_df.dropna(subset=['ba', 'slg'])
LH_MID_OPP_df = LH_MID_OPP_df.dropna(subset=['ba', 'slg'])
LH_MID_STR_df = LH_MID_STR_df.dropna(subset=['ba', 'slg'])
LH_MID_PULL_df = LH_MID_PULL_df.dropna(subset=['ba', 'slg'])
LH_OUT_OPP_df = LH_OUT_OPP_df.dropna(subset=['ba', 'slg'])
LH_OUT_STR_df = LH_OUT_STR_df.dropna(subset=['ba', 'slg'])
LH_OUT_PULL_df = LH_OUT_PULL_df.dropna(subset=['ba', 'slg'])

RH_IN_OPP_df = RH_IN_OPP_df.dropna(subset=['ba', 'slg'])
RH_IN_STR_df = RH_IN_STR_df.dropna(subset=['ba', 'slg'])
RH_IN_PULL_df = RH_IN_PULL_df.dropna(subset=['ba', 'slg'])
RH_MID_OPP_df = RH_MID_OPP_df.dropna(subset=['ba', 'slg'])
RH_MID_STR_df = RH_MID_STR_df.dropna(subset=['ba', 'slg'])
RH_MID_PULL_df = RH_MID_PULL_df.dropna(subset=['ba', 'slg'])
RH_OUT_OPP_df = RH_OUT_OPP_df.dropna(subset=['ba', 'slg'])
RH_OUT_STR_df = RH_OUT_STR_df.dropna(subset=['ba', 'slg'])
RH_OUT_PULL_df = RH_OUT_PULL_df.dropna(subset=['ba', 'slg'])

# Calculate weighted means
LH_IN_OPP_WM_BA = np.average(LH_IN_OPP_df['ba'], weights=LH_IN_OPP_df['pitches'])
LH_IN_STR_WM_BA = np.average(LH_IN_STR_df['ba'], weights=LH_IN_STR_df['pitches'])
LH_IN_PULL_WM_BA = np.average(LH_IN_PULL_df['ba'], weights=LH_IN_PULL_df['pitches'])
LH_IN_OPP_WM_SLG = np.average(LH_IN_OPP_df['slg'], weights=LH_IN_OPP_df['pitches'])
LH_IN_STR_WM_SLG = np.average(LH_IN_STR_df['slg'], weights=LH_IN_STR_df['pitches'])
LH_IN_PULL_WM_SLG = np.average(LH_IN_PULL_df['slg'], weights=LH_IN_PULL_df['pitches'])

LH_MID_OPP_WM_BA = np.average(LH_MID_OPP_df['ba'], weights=LH_MID_OPP_df['pitches'])
LH_MID_STR_WM_BA = np.average(LH_MID_STR_df['ba'], weights=LH_MID_STR_df['pitches'])
LH_MID_PULL_WM_BA = np.average(LH_MID_PULL_df['ba'], weights=LH_MID_PULL_df['pitches'])
LH_MID_OPP_WM_SLG = np.average(LH_MID_OPP_df['slg'], weights=LH_MID_OPP_df['pitches'])
LH_MID_STR_WM_SLG = np.average(LH_MID_STR_df['slg'], weights=LH_MID_STR_df['pitches'])
LH_MID_PULL_WM_SLG = np.average(LH_MID_PULL_df['slg'], weights=LH_MID_PULL_df['pitches'])

LH_OUT_OPP_WM_BA = np.average(LH_OUT_OPP_df['ba'], weights=LH_OUT_OPP_df['pitches'])
LH_OUT_STR_WM_BA = np.average(LH_OUT_STR_df['ba'], weights=LH_OUT_STR_df['pitches'])
LH_OUT_PULL_WM_BA = np.average(LH_OUT_PULL_df['ba'], weights=LH_OUT_PULL_df['pitches'])
LH_OUT_OPP_WM_SLG = np.average(LH_OUT_OPP_df['slg'], weights=LH_OUT_OPP_df['pitches'])
LH_OUT_STR_WM_SLG = np.average(LH_OUT_STR_df['slg'], weights=LH_OUT_STR_df['pitches'])
LH_OUT_PULL_WM_SLG = np.average(LH_OUT_PULL_df['slg'], weights=LH_OUT_PULL_df['pitches'])

RH_IN_OPP_WM_BA = np.average(RH_IN_OPP_df['ba'], weights=RH_IN_OPP_df['pitches'])
RH_IN_STR_WM_BA = np.average(RH_IN_STR_df['ba'], weights=RH_IN_STR_df['pitches'])
RH_IN_PULL_WM_BA = np.average(RH_IN_PULL_df['ba'], weights=RH_IN_PULL_df['pitches'])
RH_IN_OPP_WM_SLG = np.average(RH_IN_OPP_df['slg'], weights=RH_IN_OPP_df['pitches'])
RH_IN_STR_WM_SLG = np.average(RH_IN_STR_df['slg'], weights=RH_IN_STR_df['pitches'])
RH_IN_PULL_WM_SLG = np.average(RH_IN_PULL_df['slg'], weights=RH_IN_PULL_df['pitches'])

RH_MID_OPP_WM_BA = np.average(RH_MID_OPP_df['ba'], weights=RH_MID_OPP_df['pitches'])
RH_MID_STR_WM_BA = np.average(RH_MID_STR_df['ba'], weights=RH_MID_STR_df['pitches'])
RH_MID_PULL_WM_BA = np.average(RH_MID_PULL_df['ba'], weights=RH_MID_PULL_df['pitches'])
RH_MID_OPP_WM_SLG = np.average(RH_MID_OPP_df['slg'], weights=RH_MID_OPP_df['pitches'])
RH_MID_STR_WM_SLG = np.average(RH_MID_STR_df['slg'], weights=RH_MID_STR_df['pitches'])
RH_MID_PULL_WM_SLG = np.average(RH_MID_PULL_df['slg'], weights=RH_MID_PULL_df['pitches'])

RH_OUT_OPP_WM_BA = np.average(RH_OUT_OPP_df['ba'], weights=RH_OUT_OPP_df['pitches'])
RH_OUT_STR_WM_BA = np.average(RH_OUT_STR_df['ba'], weights=RH_OUT_STR_df['pitches'])
RH_OUT_PULL_WM_BA = np.average(RH_OUT_PULL_df['ba'], weights=RH_OUT_PULL_df['pitches'])
RH_OUT_OPP_WM_SLG = np.average(RH_OUT_OPP_df['slg'], weights=RH_OUT_OPP_df['pitches'])
RH_OUT_STR_WM_SLG = np.average(RH_OUT_STR_df['slg'], weights=RH_OUT_STR_df['pitches'])
RH_OUT_PULL_WM_SLG = np.average(RH_OUT_PULL_df['slg'], weights=RH_OUT_PULL_df['pitches'])

#plots the BA & SLG based on what 3rd of the field it was hit on
def plotField(LBA, CBA, RBA, LSLG, CSLG, RSLG, name):
        
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(img)

    img_height, img_width, _ = img.shape

    home_x = img_width / 2
    home_y = img_height * 0.75 

    ax.plot([home_x, home_x - 100], [home_y, home_y - 328], color='red', linestyle='--', linewidth=2)  
    ax.plot([home_x, home_x + 100], [home_y, home_y - 328], color='red', linestyle='--', linewidth=2)  

    ax.text(home_x - 130, home_y - 200, f"BA: {LBA:.3f}\nSLG: {LSLG:.3f}", 
            ha='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.7))

    
    ax.text(home_x, home_y - 225, f"BA: {CBA:.3f}\nSLG: {CSLG:.3f}", 
            ha='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.7))

   
    ax.text(home_x + 130, home_y - 200, f"BA: {RBA:.3f}\nSLG: {RSLG:.3f}", 
            ha='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.7))

    
    ax.axis('off')
    plt.title(name, fontsize=16)
    plt.show()


#function calls
plotField(LH_IN_OPP_WM_BA, LH_IN_STR_WM_BA, LH_IN_PULL_WM_BA, LH_IN_OPP_WM_SLG, LH_IN_STR_WM_SLG, LH_IN_PULL_WM_SLG, "AVG & SLG of LH Inside Pitches")
plotField(LH_MID_OPP_WM_BA, LH_MID_STR_WM_BA, LH_MID_PULL_WM_BA, LH_MID_OPP_WM_SLG, LH_MID_STR_WM_SLG, LH_MID_PULL_WM_SLG, "AVG & SLG of LH Middle Pitches")
plotField(LH_OUT_OPP_WM_BA, LH_OUT_STR_WM_BA, LH_OUT_PULL_WM_BA, LH_OUT_OPP_WM_SLG, LH_OUT_STR_WM_SLG, LH_OUT_PULL_WM_SLG, "AVG & SLG of LH Outside Pitches")

plotField(RH_IN_PULL_WM_BA, RH_IN_STR_WM_BA, RH_IN_OPP_WM_BA, RH_IN_PULL_WM_SLG, RH_IN_STR_WM_SLG, RH_IN_OPP_WM_SLG, "AVG & SLG of RH Inside Pitches")
plotField(RH_MID_PULL_WM_BA, RH_MID_STR_WM_BA, RH_MID_OPP_WM_BA, RH_MID_PULL_WM_SLG, RH_MID_STR_WM_SLG, RH_MID_OPP_WM_SLG, "AVG & SLG of RH Middle Pitches")
plotField(RH_OUT_PULL_WM_BA, RH_OUT_STR_WM_BA, RH_OUT_OPP_WM_BA, RH_OUT_PULL_WM_SLG, RH_OUT_STR_WM_SLG, RH_OUT_OPP_WM_SLG, "AVG & SLG of RH Outside Pitches")

