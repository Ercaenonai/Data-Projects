#Election Data Analysis
import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from io import StringIO
from datetime import datetime

url = "http://elections.huffingtonpost.com/pollster/2012-general-election-romney-vs-obama.csv"
source = requests.get(url).text
poll_data = StringIO(source)

poll_df = pd.read_csv(poll_data)
poll_df.info()

poll_df.head()

sns.catplot('Affiliation',data=poll_df,kind='count')

sns.catplot('Affiliation',data=poll_df,kind='count', hue='Population')

poll_df = poll_df.drop('Question Text', axis=1)
poll_df = poll_df.drop('Question Iteration',axis=1)
poll_df = poll_df.drop('Other', axis=1)

avg = pd.DataFrame(poll_df.mean())
avg.drop('Number of Observations', axis=0,inplace=True)

std = pd.DataFrame(poll_df.std())
std.drop('Number of Observations',axis=0,inplace=True)

avg.plot(yerr=std,kind ='bar',legend=False)

poll_avg = pd.concat([avg,std],axis=1,sort=False)
poll_avg.columns = ['Average', 'STD']

poll_avg

#sloppy
poll_df.plot(x='End Date', y=['Obama','Romney','Undecided'], marker='o',linestyle='')

#creates new column in dataframe 
poll_df['Difference'] = (poll_df.Obama - poll_df.Romney)/100
poll_df.head()

poll_df = poll_df.groupby(['Start Date'], as_index=False).mean()
poll_df.head()

fig = poll_df.plot('Start Date','Difference', figsize=(12,4), marker='o',linestyle='-',color='olivedrab')

#for loop that finds the debate dates
row_in=0
xlimit = []

for date in poll_df['Start Date']:
    if date[0:7] == '2012-10':
        xlimit.append(row_in)
        row_in +=1
    else:
        row_in +=1
        
print (min(xlimit))
print (max(xlimit))

#plot that shows dif. and debate 
fig = poll_df.plot('Start Date','Difference',figsize=(12,4),marker='o',linestyle='-',color='purple',xlim=(325,352))
plt.axvline(x=325+2, linewidth=4, color='grey')
plt.axvline(x=325+10, linewidth=4, color='grey')
plt.axvline(x=325+21, linewidth=4, color='grey')

