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
    if i < diff:
        print(a * STAR)
        continue
    if i >= b + diff:
        print(a * STAR)
        continue
    print(STAR * diff, SPACE * b, STAR * diff, sep='')
