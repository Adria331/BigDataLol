# -*- coding: utf-8 -*-
"""Lolete.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GXJTt9YNOedZlIMIaIukUdeeJTumvHQz
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from pandas.io.json import json_normalize

games = pd.read_json("datas2.json", lines = True, orient="values")

"""#Champion Static content"""

championsDataJson = pd.read_json("champions.json", lines = True, orient="values")

championsDataJson = json.loads(championsDataJson.data.to_json())['0']

"""###Adding champs left"""

#Zoe 142
newdata = {'key':'142', 'tags':['Mage'], 'id':'Zoe'}
championsDataJson['Zoe'] = newdata

#Kayn 141
newdata = {'key':'141', 'tags':['Fighter'], 'id':'Kayn'}
championsDataJson['Kayn'] = newdata

#Neeko 518
newdata = {'key':'518', 'tags':['Mage'], 'id':'Neeko'}
championsDataJson['Neeko'] = newdata

#Xayah 498
newdata = {'key':'498', 'tags':['Marksman'], 'id':'Xayah'}
championsDataJson['Xayah'] = newdata

#Rakan 497
newdata = {'key':'497', 'tags':['Support'], 'id':'Rakan'}
championsDataJson['Rakan'] = newdata

#Kaisa 145
newdata = {'key':'145', 'tags':['Marksman'], 'id':'Kaisa'}
championsDataJson['Kaisa'] = newdata

#Sylas 517
newdata = {'key':'517', 'tags':['Mage'], 'id':'Sylas'}
championsDataJson['Sylas'] = newdata

#Pyke 555
newdata = {'key':'555', 'tags':['Support'], 'id':'Pyke'}
championsDataJson['Pyke'] = newdata

#Ornn 516
newdata = {'key':'516', 'tags':['Tank'], 'id':'Ornn'}
championsDataJson['Ornn'] = newdata

championsDataJson['Pyke']

"""####EXPORT DATA OF CHAMPIONS COMPLETE"""

with open('championsComplete.json', 'w') as f:
    json.dump(championsDataJson, f)

"""#Data management

### Removement of unnecessy columns
"""

#games = games.drop(['gameCreation'], axis=1)
games = games.drop(['gameVersion'], axis=1)
games = games.drop(['platformId'], axis=1)
games = games.drop(['seasonId'], axis=1)
games = games.drop(['queueId'], axis=1)
games = games.drop(['mapId'], axis=1)
games = games.drop(['participantIdentities'], axis=1)
games = games.drop(['gameType'], axis=1)

games.head()

games.columns

"""### Normal or ranked games filter"""

games = games.loc[games['gameMode'] == 'CLASSIC']
#Now that is filtered it's innecessary to maintain the column gamemode
games = games.drop(['gameMode'], axis=1)

"""### Once filtered by games"""

print(games['participants'][0])

print(games['teams'][0])

for key, value in games['participants'][0][0].items() :
    print (key, value)

for key, value in games['participants'][0][0]['stats'].items() :
    print (key, value)

print(games['participants'][9])

len(games)

"""### Check data"""

games.columns

for teams in games['teams']:
  for team in teams:
    print(team['firstTower'])

for teams in games['teams']:
  for team in teams:
    print(team['firstTower'])

with open('game.json', 'w') as f:
    f.write(games.to_json(orient='records', lines=True))

"""##GET MOST PLAYED CHAMP"""

champs = {}

games.participants[0][0]

games['champions'] = games.participants.apply(lambda game: np.array([player['championId'] for player in game]))

games.champions

for x in range(0, max(games['champions'].apply(lambda x: max(x)))+1):
  champs[x] = 0

for champ in np.concatenate(games['champions'].values):
  champs[champ] += 1

champs

maximito = max(champs.values())

maximito

keyMostPlayedChamp = "0"
for keyita, valuito in champs.items():    # for name, age in dictionary.iteritems():  (for Python 2.x)
    if valuito == maximito:
        print(str(keyita))
        keyMostPlayedChamp = str(keyita)

champ = ""
for key, value in championsDataJson.items():
  
  if(value['key'] == keyMostPlayedChamp):
    print(key + " " + value['key'])