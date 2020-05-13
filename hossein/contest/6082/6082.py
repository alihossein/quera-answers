# https://quera.ir/problemset/contest/6082/

n, m = input().split(' ')
in_list = [input() for i in range(int(n))]
cnt = 0
for line in in_list:
    for char in line:
        if char == '*':
            cnt += 1
print(cnt)
