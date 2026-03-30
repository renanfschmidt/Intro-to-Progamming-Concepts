class player_nfl:
 def __init__(self,name,position):
  self.playerName =name
  self.playerPosition= position
class team_nfl:
 def __init__(self,name,teamList):
  self.teamName =name
  self.teamList =teamList
player_1 = player_nfl('Joe Montana', 'QB')
player_2 = player_nfl('Barry Saders', 'RB')
player_3 = player_nfl('Graham Gano', 'K')
player_4 = player_nfl('Jerry Rice', 'WR')
playerlist = [player_1, player_2, player_3, player_4]
Team = team_nfl("NFL Players", playerlist)

print("Team Name:", Team.teamName)
for p in Team.teamList:
  print(p.playerName,p.playerPosition)