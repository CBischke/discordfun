import sys
sys.path.insert(0, '../')

import time
import json

from opendota.connection import Connection
from hero import Hero

con = Connection()

matches = con.getLatestMatches()

dictOfHeros= {}

for row in matches:
    matchid = row['match_id']
    time.sleep(.33)
    match = con.getMatch(matchid)
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


"""for key in dictOfHeros.keys():
    localname = con.idToLocalName(key)
    print(localname + ": " + str(dictOfHeros[key].getGameCount()) + " | " + str(dictOfHeros[key].getWinRatio()))
    print("   won most with:")
    for hero in dictOfHeros[key].getWonWithMost():
        print("    " + con.idToLocalName(hero[0]) + ":" + str(hero[1]))"""

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