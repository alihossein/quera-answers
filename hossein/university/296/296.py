n = int(input())
SHARP = '#'
SPACE = ' '
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n - 1 or j == n - 1 or j == i or (i + j) == n - 1 or (
                (i + j) > (n - 1) and j > i):
            print(SHARP, end='')
        else:
            print(SPACE, end='')
    print()
