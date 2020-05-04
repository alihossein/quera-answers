# question: https://quera.ir/problemset/contest/34081
tmp = input()
n, k = tmp.split(' ')
k = int(k)
n = int(n)
start = 1
cnt = 0
while True:
    next_step = (start + k) % n
    cnt += 1
    if next_step == 1: print(cnt); break
    start = next_step
