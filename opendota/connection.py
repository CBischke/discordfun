import requests

"""
select%20%2A%20from%20public_matches%20where%20avg_mmr%20%3E%203000%20and%20game_mode%20%3D%2022%20order%20by%20start_time%20desc%20limit%201000
"""
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

    def getMatch(self, id):
        r = requests.get(self.base + "matches/" + str(id))
        return r.json()

    def getLatestMatches(self):
        q = "select+%2A+from+public_matches+where+avg_mmr+%3E+3000+and+game_mode+%3D+22+order+by+start_time+desc+limit+5000"
        return self.__explorer(q)

    def __explorer(self, q):
        r = requests.get(self.base + "explorer/?sql=" + str(q))
        return r.json()['rows']

