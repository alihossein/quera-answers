import math

n = int(input())
for i in range(1, n + 1):
    line = ''
    for j in range(1, n + 1):
        if i in [1, n]:
            line += '#'
        elif j in [1, n]:
            line += '#'
        elif i == j:
            line += '#'
        elif j == n - i + 1:
            line += '#'
        elif j > n-i:
            if i <= int(n/2)+1:
                line += '#'
            else:
                if j > i:
                   line += '#'
                else:
                    line += ' '
        else:
            line += ' '
    print(line)
