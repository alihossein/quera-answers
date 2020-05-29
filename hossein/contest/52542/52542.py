# https://quera.ir/problemset/contest/52542

STAR = "*"
n = int(input())
players = list(map(int, input().strip().split(' '))) if n > 0 else exit(0)
for player in players:
    if player <= 3:
        print(player * STAR)
    else:
        print(STAR)
