# question : https://quera.ir/problemset/contest/3561
STAR = "*"
SPACE = " "
floors = ['    *   ', '   * *  ', '  *   * ', ' *     *', '********']
pad = lambda count, n: SPACE * (n - count) * 4
repeat = lambda rep, count: rep * (count)

n = int(input())
count = 0
for i in range(0, (n * 4) + 1):
    if i % 4 == 0:
        print(pad(count, n) + repeat(floors[4], count) + STAR)
        count = int(i / 4) + 1
    else:
        print((pad(count, n) + repeat(floors[i % 4], count)).rstrip())