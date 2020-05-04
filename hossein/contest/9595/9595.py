# https://quera.ir/problemset/contest/9595/

n = int(input())
lines = [input() for i in range(2 * n)]
cnt = 0
for i in range(0, 2 * n, 2):
    if lines[i].replace(' ', '') == lines[i + 1].replace(' ', ''):
        continue
    cnt += 1
print(cnt)
