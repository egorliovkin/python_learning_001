lines = int(input())
count = 0
games = {}
while count < lines:
    count += 1
    xs = input().split(';')
    team_1 = xs[0]
    goals_1 = int(xs[1])
    team_2 = xs[2]
    goals_2 = int(xs[3])
    if games.get(team_1) == None:
        games[team_1] = {
            'games': 1,
            'victories': 1 if goals_1 > goals_2 else 0,
            'draw': 1 if goals_1 == goals_2 else 0,
            'loss': 1 if goals_1 < goals_2 else 0,
            'result': 3 if goals_1 > goals_2 else (1 if goals_1 == goals_2 else 0)
        }
    else:
        games[team_1] = {
            'games': games[team_1]['games'] + 1,
            'victories': games[team_1]['victories'] + (1 if goals_1 > goals_2 else 0),
            'draw': games[team_1]['draw'] + (1 if goals_1 == goals_2 else 0),
            'loss': games[team_1]['loss'] + (1 if goals_1 < goals_2 else 0),
            'result': games[team_1]['result'] + (3 if goals_1 > goals_2 else (1 if goals_1 == goals_2 else 0))
        }
    if games.get(team_2) == None:
        games[team_2] = {
            'games': 1,
            'victories': 1 if goals_2 > goals_1 else 0,
            'draw': 1 if goals_2 == goals_1 else 0,
            'loss': 1 if goals_2 < goals_1 else 0,
            'result': 3 if goals_2 > goals_1 else(1 if goals_2 == goals_1 else 0)
        }
    else:
        games[team_2] = {
            'games': games[team_2]['games'] + 1,
            'victories': games[team_2]['victories'] + (1 if goals_2 > goals_1 else 0),
            'draw': games[team_2]['draw'] + (1 if goals_2 == goals_1 else 0),
            'loss': games[team_2]['loss'] + (1 if goals_2 < goals_1 else 0),
            'result': games[team_2]['result'] + (3 if goals_2 > goals_1 else(1 if goals_2 == goals_1 else 0))
        }

for k in games.keys():
    print(f"{k}:{games[k]['games']} {games[k]['victories']} {games[k]['draw']} {games[k]['loss']} {games[k]['result']}")