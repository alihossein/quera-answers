# https://quera.ir/problemset/contest/2887/


n = int(input())
A_str = input().split(' ')
A = list(map(lambda x: int(x), A_str))

import numpy as np

addiction_level = np.gcd.reduce(A)
result = 0
for val in A:
    temp = int(val) / addiction_level
    result += temp

print(int(result))
