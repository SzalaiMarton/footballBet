import pandas

class processTeamData:
    fileName = ""
    teamStats:dict = dict()
    data:pandas.DataFrame
    homeTeams:pandas.Series
    awayTeams:pandas.Series
    fthg:pandas.Series
    ftag:pandas.Series
    team:str

    def __init__(self, teamName:str, fileName:str):
        self.team = teamName
        self.fileName = fileName
        self.initializeFile()
            
    def initializeFile(self):
        self.data = pandas.read_csv(self.fileName)
        self.homeTeams = self.data["HomeTeam"]
        self.awayTeams = self.data["AwayTeam"]
        self.fthg = self.data["FTHG"]
        self.ftag = self.data["FTAG"]
        self.team:str = ""
    
    def getAvgByTeam(self, team:str, typeOfSAvg:str, home:bool) -> dict:
        indexes:list = []
        reVaule:int = 0
        teamsArray = self.homeTeams
        if home:
            teamsArray = self.homeTeams
        else:
            teamsArray = self.awayTeams
        for ind in range(len(teamsArray)):
            if teamsArray[ind] == team:
                indexes.append(ind)
        for ind in indexes:
            if typeOfSAvg == "fthg":
                reVaule += int(self.fthg[ind])
            elif typeOfSAvg == "ftag":
                reVaule += int(self.ftag[ind])
        return {team:reVaule / len(indexes)}