import sys
sys.path.insert(0, '../')

import time
import json

from tqdm import tqdm
from opendota.connection import Connection
from hero import Hero

con = Connection()

matches = con.getLatestMatches()

dictOfHeros= {}

for i in tqdm(range(len(matches))):
    matchid = matches[i]['match_id']
    time.sleep(.33)
    
    try:
        match = con.getMatch(matchid)
    except:
        print("problem with: " + str(matchid))
        continue

    players = match['players']

    for player in players:
        heroid = player['hero_id']
        win = player['win']

        if heroid not in dictOfHeros.keys():
            dictOfHeros[heroid] = Hero(heroid)

        dictOfHeros[heroid].addGamePlayed()

        if win == 1:
            dictOfHeros[heroid].addGameWon()

        for p in players:
            otherheroID = p['hero_id']
            if otherheroID == heroid:
                continue

            dictOfHeros[heroid].addGamesPlayedWith(otherheroID)

            otherPlayerWin = p['win']
            if otherPlayerWin == win and win == 1:
                dictOfHeros[heroid].addWonWith(otherheroID)

finalDict = {}
for heroid, hero in dictOfHeros.items():
    heroDict = {}
    heroDict['win_ratio'] = str(hero.getWinRatio())
    heroDict['gamesPlayed'] = str(hero.getGameCount())
    heroDict['localName'] = str(con.idToLocalName(heroid))
    heroDict['id'] = str(heroid)
    heroDict['best_with'] = hero.getWonWithMost()
    finalDict[heroid] = heroDict

myFile = open('data.json', 'w')
myFile.write(str(json.dumps(finalDict)))
myFile.close()