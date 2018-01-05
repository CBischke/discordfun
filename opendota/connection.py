import requests


class Connection:
    def __init__(self):
        self.base = "https://api.opendota.com/api/"
        self.listOfHeroes = None

    def getHeros(self):
        if not self.listOfHeroes:
            r = requests.get(self.base + "heroes/")
            self.listOfHeroes = r.json()
        return self.listOfHeroes

    def idToLocalName(self, id):
        r = self.getHeros()
        for row in r:
            if row['id'] == id:
                return row['localized_name']

    def localToId(self, localname):
        r = self.getHeros()
        for row in r:
            if row['localized_name'].lower() == localname.lower():
                return row['id']

    def getMatchUp(self, id):
        r = requests.get(self.base + "heroes/" + str(id) + "/matchups")
        return r.json()