from opendota.connection import Connection
import collections
import json

class Heroes:
    def __init__(self):
        self.conn = Connection()

    def findWinRate(self, json):
        dictOfValues = {}
        listOfBest = []
        listOfWorst = []
        for row in json:
            wins = row['wins']
            gp = row['games_played']
            if gp < 5:
                continue
            hero = self.conn.idToLocalName(row['hero_id'])
            ratio = wins / gp
            dictOfValues[hero] = ratio
        count = collections.Counter(dictOfValues)

        for k, v in count.most_common(3):
            listOfBest.append((k, v))

        for k, v in count.most_common()[-3:]:
            listOfWorst.append((k, v))

        print(str(listOfBest))
        print(str(listOfWorst))
        return listOfBest, listOfWorst

    def determineMatchUp(self, localname):
        id = self.conn.localToId(localname)
        best, worst = self.findWinRate(self.conn.getMatchUp(id))
        finalString = "Based on professional matches\n"
        finalString = "BEST: \n"

        for row in best:
            finalString = finalString + "   " + str(row[0]) + "|" + str(row[1]) + "\n"

        finalString = finalString + "\nWORST: \n"

        for row in worst:
            finalString = finalString + "   " + str(row[0]) + "|" + str(row[1]) + "\n"

        return finalString


    def findBestWith(self, localname):
        id = str(self.conn.localToId(localname))
        myfile = open('miner/data.json', 'r')
        rows = json.loads(myfile.read())
        myfile.close()

        winrate = rows[id]['win_ratio']
        worksBestWith = rows[id]['best_with']

        finalString = localname + " has a winrate of: " + winrate + "\n"
        finalString = finalString + "works best with: \n"
        for hero in worksBestWith:
            name = self.conn.idToLocalName(hero['hero_id'])
            ratio = hero['win_ratio']
            finalString = finalString + "    " + name + ": " + str(ratio) + "\n"

        return finalString



