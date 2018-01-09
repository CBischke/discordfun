import collections

class Hero:
    
    def __init__(self, id):
        self.gp = 0
        self.id = -1
        self.gamesWon = 0
        self.gamesPlayedWith = {}
        self.wonAgainst = {}
        self.lostAgainst = {}
        self.wonWith = {}

    def addGamesPlayedWith(self, heroId):
        if heroId not in self.gamesPlayedWith.keys():
            self.gamesPlayedWith[heroId] = 0
        self.gamesPlayedWith[heroId] = self.gamesPlayedWith[heroId] + 1

    def addWonWith(self, heroId):
        if heroId not in self.wonWith.keys():
            self.wonWith[heroId] = 0
        self.wonWith[heroId] = self.wonWith[heroId] + 1

    def wonAgainst(self, heroId):
        if heroId not in self.wonAgainst.keys():
            self.wonAgainst[heroId] = 0
        self.wonAgainst[heroId] = self.wonAgainst[heroId] + 1
    
    def lostAgainst(self, heroId):
        if heroId not in self.lostAgainst.keys():
            self.lostAgainst[heroId] = 0
        self.lostAgainst[heroId] = self.lostAgainst[heroId] + 1

    def addGamePlayed(self):
        self.gp = self.gp + 1

    def addGameWon(self):
        self.gamesWon = self.gamesWon + 1

    def getGameCount(self):
        return self.gp

    def getWinRatio(self):
        return self.gamesWon / self.gp

    def getWonWithMost(self):
        count = collections.Counter(self.wonWith)
        listOfWonTheMost = []
        for k, v in count.most_common(3):
            listOfWonTheMost.append(
                    {
                    'hero_id': k, 
                    'win_ratio': v/self.gamesPlayedWith[k],
                    'games_won': self.wonWith[k],
                    'games_played': self.gamesPlayedWith[k]
                    }
                )
        
        return listOfWonTheMost
