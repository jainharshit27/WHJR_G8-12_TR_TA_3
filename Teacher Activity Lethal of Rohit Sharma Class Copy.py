import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
%matplotlib inline

df = pd.read_csv("https://raw.githubusercontent.com/jainharshit27/datasets/main/Rohit_truncated_ball_by_ball.csv")
 
df.head()
 
df_Rohit = df[df["player_dismissed"] == "RG Sharma"]
 
'''
Code here for df_Rohit_dismissed
which is equal to df_Rohit.groupby("ball").count()
and show the output
'''
 
plt.bar(df_Rohit_dismissed.index, df_Rohit_dismissed["player_dismissed"])
plt.title("Number of times the player was dismissed on each ball of over")
''' Code here to plot the bar graph '''
plt.xlabel("Ball of the over")
plt.ylabel("Dismissals")
plt.show()


'''
Code here for df_runs_per_ball 
which is equal to df.groupby("ball").sum()
and show the output
'''
 
plt.title("Runs scored for each ball of over")
''' Code here to plot the bar graph '''
plt.xlabel("Ball of the over")
plt.ylabel("Runs Scored")
plt.show()