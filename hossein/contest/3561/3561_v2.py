# question : https://quera.ir/problemset/contest/3561
STAR = "*"
SPACE = " "
floors = ['********', '   * *  ', '  *   * ', ' *     *']
pad = lambda count, n: SPACE * (n - count) * 4
repeat = lambda rep, count: rep * (count)

n = int(input())
count = 0
for i in range(0, (n * 4) + 1):
    print((pad(count, n) + repeat(floors[i % 4], count) + (not i % 4) * STAR).rstrip())
    count = int(i / 4) + 1
