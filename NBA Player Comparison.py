# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 16:02:36 2017

@author: Nadeem Choudhury
"""

import pandas as pd
stats=pd.read_csv("Seasons_Stats.csv",index_col=2)
stats["PPG"]=stats["PTS"]/stats["G"]
stats["APG"]=stats["AST"]/stats["G"]
stats["FG%"]*=100
     
Player1=str(input("Enter full name of Player1: "))
Player2=str(input("Enter full name of Player2: "))

P1=stats.loc[Player1]
P2=stats.loc[Player2]

import matplotlib.pyplot as plt
plt.figure(figsize=(10,7))
plt.plot(P1["Year"],P1["PPG"])
plt.plot(P2["Year"],P2["PPG"])
plt.plot(P1["Year"],P1["APG"])
plt.plot(P2["Year"],P2["APG"])
plt.plot(P1["Year"],P1["FG%"])
plt.plot(P2["Year"],P2["FG%"])

plt.xlabel("Year",fontsize=18)
plt.ylabel("PPG/APG/FG%",fontsize=18)
plt.title(Player1 +'/'+ Player2 +' ' + "Comparison",fontsize=24)
plt.legend([Player1+' PPG',Player2+' PPG',Player1+' APG',Player2+' APG',Player1+' FG%',Player2+' FG%'],loc=6,bbox_to_anchor=(-0.5,0.75),fontsize='x-large')

plt.show()

