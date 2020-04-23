# question : https://quera.ir/problemset/university/9773
diameter = int(input())
diameter /= 2
diameter = int(diameter) + 1
STAR = "*"
SPACE = " "
for i in range(diameter):
    print(SPACE * (diameter - i - 1), STAR * (i * 2 + 1), SPACE * (2 * (diameter - i) - 2), STAR * (i * 2 + 1), sep='')
for i in range(diameter - 2, -1, -1):
    print(SPACE * (diameter - i - 1), STAR * (i * 2 + 1), SPACE * (2 * (diameter - i - 1)), STAR * (i * 2 + 1), sep='')

