# question : https://quera.ir/problemset/university/618

# print("Hello there!", end = '')

diameter = int(input())
diameter += 1
STAR="*"
SPACE=" "
for i in range(diameter):
    print(SPACE*(diameter-i-1),end='')
    print(STAR * (i*2 + 1),end='')
    print()
for i in reversed(range(diameter - 1)):
    print(SPACE*(diameter-i-1),end='')
    print(STAR*(i*2+1),end='')
    print()
