players = []
Patrick_Mahomes = {
'name': 'Patrick Mahomes',
'position': '四分卫',
'jersey number': 15}
Travis_Kelce = {
'name': 'Travis Kelce',
'position': '近端锋',
'jersey number': 87}
Isiah_Pacheco = {
'name': 'Isiah Pacheco',
'position': '跑卫',
'jersey number': 10}
players.append(Patrick_Mahomes)
players.append(Travis_Kelce)
players.append(Isiah_Pacheco)
for player in players:
    print(player['name'], player['position'])
players[0]['name'] = 'ikun'
print(players[0]['name'])
