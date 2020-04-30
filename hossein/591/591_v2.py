# question : https://quera.ir/problemset/university/591/
n = int(input())
STAR = "*"
SPACE = ' '
star_space = [STAR, SPACE]
between_up_down = lambda i, n: star_space[i not in {0, n - 1}] # [0, n-1] or {0, n-1} or (0, n-1)
print(*[(STAR + between_up_down(i, n) * (n - 2) + STAR) for i in range(n)], sep='\n')
