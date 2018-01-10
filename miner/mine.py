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
    try:
        matchid = matches[i]['match_id']
        time.sleep(.33)
        
        match = con.getMatch(matchid)

        players = match['players']

        for player in players:
            heroid = player['hero_id']
            win = player['win']

            if heroid not in dictOfHeros.keys():
                dictOfHeros[heroid] = Hero(heroid)

            hero = dictOfHeros[heroid]
            hero.addGamePlayed()

            if win == 1:
                hero.addGameWon()

            for p in players:
                otherheroID = p['hero_id']
                if otherheroID == heroid:
                    continue

                otherPlayerWin = p['win']

                #same team
                if otherPlayerWin == win:
                    hero.addGamesPlayedWith(otherheroID)
                    #win
                    if win == 1:
                        hero.addWonWith(otherheroID)
                #other team
                elif otherPlayerWin != win:
                    hero.addGamesPlayedAgainst(otherheroID)
                    #loss
                    if win == 0:
                        hero.addLostAgainst(otherheroID)
                    else:
                        hero.addWonAgainst(otherheroID)
    except:
        print("error")
        continue
                    

finalDict = {}
for heroid, hero in dictOfHeros.items():
    heroDict = {}
    heroDict['win_ratio'] = str(hero.getWinRatio())
    heroDict['gamesPlayed'] = str(hero.getGameCount())
    heroDict['localName'] = str(con.idToLocalName(heroid))
    heroDict['id'] = str(heroid)
    heroDict['best_with'] = hero.getWonWithMost()
    heroDict['best_against'] = hero.getBestAgainst()
    heroDict['worst_against'] = hero.getWorstAgainst()
    finalDict[heroid] = heroDict

myFile = open('data.json', 'w')
myFile.write(str(json.dumps(finalDict)))
myFile.close()