def getStates():
  matces=[]
  while (True):
    matchData = input()
    if matchData:
      matces.append(matchData)
    else:
      break
  return matces


def getScoreSet(score):
  p1 = int(score.split("-")[0])
  p2 = int(score.split("-")[1])
  return (p1,p2)


def parseMatchData(match):
  matchData = {}
  stats = match.split(":")
  matchData["player1"] = stats[0]
  matchData["player2"] = stats[1]
  sets = stats[2].split(",")
  matchData["totalSets"] = len(sets)
  matchData["scoreSet"] = list(map(getScoreSet,sets))
  return matchData
  
def getParsedMatchData(stats):
  return list(map(parseMatchData,stats))
  
  
def getAllplayers(matches):
  players = []
  for match in matches:
    p1 = match["player1"]
    p2 = match["player2"]
    if p1 not in players:
      players.append(p1)
    if p2 not in players:
      players.append(p2)
  return players
  

def getPlayerMatches(player,matches):
  playerMatches = []
  for match in matches:
    if match["player1"] == player or match["player2"] == player:
      playerMatches.append(match)
  return playerMatches
  

def iswon(a,b):
  return (a > b)

  
def lostWinStat(isFirstPlayer,scoreSet):
  if isFirstPlayer :
    return 1
  else :
    return 0


def getSetOf5Won(isFirstPlayer,scoreSet):
  if len(scoreSet) < 4 :
    return 0
  else :
    return lostWinStat(isFirstPlayer,scoreSet)
    

def getSetOf3Won(isFirstPlayer,scoreSet):
  if len(scoreSet) > 3 :
    return 0
  else :
    return lostWinStat(isFirstPlayer,scoreSet)
    
    
def getSetsWon(isFirstPlayer,scoreSet):
  setsWon = 0
  if isFirstPlayer:
    for set in scoreSet:
      if iswon(set[0],set[1]):
        setsWon += 1
  else :
    for set in scoreSet:
      if iswon(set[1],set[0]):
        setsWon += 1
  return setsWon


def getGamesWon(isFirstPlayer,scoreSet):
  gameWon = 0
  if isFirstPlayer:
    for set in scoreSet:
        gameWon += set[0]
  else :
    for set in scoreSet:
        gameWon += set[1]
  return gameWon

def getSetsLost(isFirstPlayer,scoreSet):
  setslost = 0
  if isFirstPlayer:
    for set in scoreSet:
      if not iswon(set[0],set[1]):
        setslost += 1
  else :
    for set in scoreSet:
      if not iswon(set[1],set[0]):
        setslost += 1
  return setslost
  
  
def getGamesLost(isFirstPlayer,scoreSet):
  gamelost = 0
  if isFirstPlayer:
    for set in scoreSet:
        gamelost += set[1]
  else :
    for set in scoreSet:
        gamelost += set[0]
  return gamelost
  

def getPlayerStats(player, matches):
  stats =[0] * 6
  for match in matches:
    isFirstPlayer = match["player1"] == player
    stats[0] += getSetOf5Won(isFirstPlayer,match["scoreSet"])
    stats[1] += getSetOf3Won(isFirstPlayer,match["scoreSet"])
    stats[2] += getSetsWon(isFirstPlayer,match["scoreSet"])
    stats[3] += getGamesWon(isFirstPlayer,match["scoreSet"])
    stats[4] += getSetsLost(isFirstPlayer,match["scoreSet"])
    stats[5] += getGamesLost(isFirstPlayer,match["scoreSet"])
    
  return stats
  
  
def getAnalysedData(scores):
  players = getAllplayers(scores)
  playerAnalysedData = []
  for player in players:
    playerScore = {}
    playerMatches = getPlayerMatches(player,scores)
    playerScore["player"] = player
    playerScore["stats"] = getPlayerStats(player,playerMatches)
    playerAnalysedData.append(playerScore)
  return playerAnalysedData
  
def isSmaller(playerA,playerB):
  count = 0
  while(playerA["stats"][count] == playerB["stats"][count]):
    count +=1
  if count == 5 and playerA["stats"][6] == playerB["stats"][6]:
      return playerA["stats"][5] < playerB["stats"][5]
  else:
      return playerA["stats"][6] < playerB["stats"][6]

  return playerA["stats"][count] < playerB["stats"][count]


def getSortedAsRank(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if isSmaller(arr[j] , arr[j+1]):
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr
    

def printData(sortedAsRank):
  for player in sortedAsRank:
    stat = " ".join(map(str, player["stats"]))
    print('{0} {1}'.format(player["player"], stat))


def getAnalysedStats():
    matchesData = getStates()
    parsedData = getParsedMatchData(matchesData)
    analysedData = getAnalysedData(parsedData)
    sortedAsRank = getSortedAsRank(analysedData)
    printData(sortedAsRank)
    # print(sortedAsRank)
    


getAnalysedStats()