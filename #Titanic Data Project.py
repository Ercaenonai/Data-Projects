#Titanic Data Project
import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

titanic_df = pd.read_csv('train.csv')

titanic_df.head()

titanic_df.info()

#number of passengers by gender
sns.catplot('Sex',data=titanic_df,kind='count')

#Passngers by ticket class by gender
sns.catplot('Pclass',data=titanic_df,kind='count',hue='Sex')

#func for dividing male, female, and children
def male_female_child(passenger):
    age,sex = passenger
    if age < 16:
        return 'child'
    else:
        return sex

titanic_df['person'] = titanic_df[['Age','Sex']].apply(male_female_child,axis=1)

titanic_df[0:10]

sns.catplot('Pclass',data=titanic_df,kind='count',hue='person')

#age distribution
titanic_df['Age'].hist(bins=70)

titanic_df['person'].value_counts()


fig = sns.FacetGrid(titanic_df, hue='Sex',aspect=4)

fig.map(sns.kdeplot,'Age',shade = True)

oldest = titanic_df['Age'].max()

fig.set(xlim=(0,oldest))

fig.add_legend()

#seperated including children from created 'person' column
fig = sns.FacetGrid(titanic_df, hue='person',aspect=4)
fig.map(sns.kdeplot,'Age', shade = True)
oldest = titanic_df['Age'].max()
fig.set(xlim=(0,oldest))
fig.add_legend()

#distribution by ticket class
fig = sns.FacetGrid(titanic_df, hue="Pclass",aspect=4)
fig.map(sns.kdeplot,'Age',shade= True)
oldest = titanic_df['Age'].max()
fig.set(xlim=(0,oldest))
fig.add_legend()

#created new deck column with null values dropped
deck = titanic_df['Cabin'].dropna()

deck.head()

#grabs first letter in deck
levels = []

for level in deck:
    levels.append(level[0])
    
cabin_df = DataFrame(levels)
cabin_df.columns = ['Cabin']
sns.catplot('Cabin',data=cabin_df,kind='count',palette = 'winter_d')

#drops extra column T
cabin_df = cabin_df[cabin_df.Cabin != 'T']
sns.catplot('Cabin',data=cabin_df,kind='count',palette = 'summer')

#counts passenger class by location
sns.catplot('Embarked',data = titanic_df, kind='count',hue='Pclass')

#new column called alone
titanic_df['Alone'] = titanic_df.Parch + titanic_df.SibSp
titanic_df['Alone']

#seperates by alone or with family
titanic_df['Alone'].loc[titanic_df['Alone']>0] = 'With Family'
titanic_df['Alone'].loc[titanic_df['Alone']==0] = 'Alone'

sns.catplot('Alone',data = titanic_df, kind='count',palette='Blues')

#filtering for survivors
titanic_df['Survivor'] = titanic_df.Survived.map({0:'no',1: 'yes'})

sns.catplot('Survivor', data=titanic_df,kind='count', palette='Set1')

#survival rate by class
sns.catplot('Pclass','Survived',data=titanic_df, kind='point')

#rate by class and gender
sns.catplot('Pclass','Survived',hue='person',data=titanic_df,kind='point')

#age
sns.lmplot('Age','Survived',data=titanic_df)

#class
sns.lmplot('Age','Survived',hue='Pclass',data=titanic_df, palette='winter_d')

#binned age brackets for cleaner graph
generations=[12,20,30,40,60,80]
sns.lmplot('Age','Survived', hue='Pclass',data=titanic_df,palette='winter',x_bins=generations)

#survivors by age and gender
sns.lmplot('Age','Survived',hue='Sex',data=titanic_df,palette='winter',x_bins=generations)

#adds image from url source, just good to know
from IPython.display import Image
Image(url='http://i.imgur.com/DGNjT.gif')



