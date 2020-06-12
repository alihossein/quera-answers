# https://quera.ir/problemset/contest/52549

result = []
while True:
    n = int(input())
    if n == 0:
        break
    test_list = [list(map(int, input().split(' '))) for i in range(n)]
    players = {}
    for j in range(len(test_list)):
        rank = 3
        for selected in test_list[j][1:]:
            players[selected] = players.get(selected, 0) + rank
            rank -= 1
    winner = set()
    max_score = max(players.values())
    for player in players.keys():
        if players[player] == max_score:
            winner.add(player)
    result.append(winner)

for line in result:
    print(*sorted(line))
