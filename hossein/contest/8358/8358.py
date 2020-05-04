# https://quera.ir/problemset/contest/8358/

n = int(input())
A = list(input().split(' '))
result = [int(i) for i in A if int(i) < 0]
ans = len(result) * (n - 1)
print(ans)
