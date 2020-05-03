# question : https://quera.ir/problemset/university/283
a = int(input())
b = int(input())

STAR = "* "
SPACE = "  "
if (a <= b):
    print('Wrong order!')
    exit(0)
elif (a - b) % 2 != 0:
    print('Wrong difference!')
    exit(0)

diff = int((a - b) / 2)
for i in range(a):
    between_char = (i < diff or i >= b + diff)
    print(STAR * diff, ((1 - between_char) * SPACE + (between_char) * STAR) * b, STAR * diff, sep='')
