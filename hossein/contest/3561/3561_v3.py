# question : https://quera.ir/problemset/contest/3561
STAR = "*"
SPACE = " "
floors = [8 * STAR, '   * *  ', '  *   * ', ' *     *']
pad = lambda count, n: SPACE * (n - count) * 4
repeat = lambda rep, count: rep * (count)
count = lambda i: int(i / 4) + 1 - (i%4 == 0 ) * 1

n = int(input())
print(*[((pad(count(i), n) + repeat(floors[i % 4], count(i)) + (not i % 4) * STAR).rstrip()) for i in range(0, (n * 4) + 1)], sep='\n')
