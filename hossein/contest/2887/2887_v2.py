# https://quera.ir/problemset/contest/2887/
import numpy as np

n = int(input())
A_str = input().split(' ')
A = list(map(int, A_str))

addiction_level = np.gcd.reduce(A)
result = 0
for val in A:
    temp = val / addiction_level
    result += temp

print(int(result))
