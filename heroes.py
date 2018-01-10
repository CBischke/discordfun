from opendota.connection import Connection
import collections
import json

class Heroes:
    def __init__(self):
        self.conn = Connection()

    def determineMatchUp(self, localname):
        id = str(self.conn.localToId(localname))
        myfile = open('miner/data.json', 'r')
        rows = json.loads(myfile.read())
        myfile.close()

        winrate = rows[id]['win_ratio']
        worksBestWith = rows[id]['best_with']
        bestAgainst = rows[id]['best_against']
        worstAgainst = rows[id]['worst_against']

        finalString = localname + " has a winrate of: " + winrate + "\n"
        finalString = finalString + "BEST WITH: \n"
        for hero in worksBestWith:
            name = self.conn.idToLocalName(hero['hero_id'])
            ratio = hero['win_ratio']
            games_played = hero['games_played']
            games_won = hero['games_won']
            finalString = finalString + "    " + name + ": " + str(ratio) + "(" + str(games_won) + "/" + str(games_played) + ")" + "\n"

        finalString = finalString + "BEST AGAINST: \n"
        for hero in bestAgainst:
            name = self.conn.idToLocalName(hero['hero_id'])
            ratio = hero['win_ratio']
            games_played = hero['games_played']
            games_won = hero['games_won']
            finalString = finalString + "    " + name + ": " + str(ratio) + "(" + str(games_won) + "/" + str(games_played) + ")" + "\n"

        finalString = finalString + "WORST AGAINST: \n"
        for hero in worstAgainst:
            name = self.conn.idToLocalName(hero['hero_id'])
            ratio = hero['loss_ratio']
            games_played = hero['games_played']
            games_lost = hero['games_lost']
            finalString = finalString + "    " + name + ": " + str(ratio) + "(" + str(games_lost) + "/" + str(games_played) + ")" + "\n"

        return finalString