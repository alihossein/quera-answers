# question : https://quera.ir/problemset/contest/2887/
n = int(input())
numbers = input().split(' ')


def gcd(x, y):
    x=int(x)
    y=int(y)
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if (x % i == 0) and (y % i == 0):
            gcd = i

    return gcd
    # x = int(x)
    # y = int(y)
    # if y == 0:
    #     return x
    # else:
    #     return gcd(y, x % y)


min_number = int(numbers[0])
gcd_result = 0
result = 0
for index, number in enumerate(numbers):
    if index == len(numbers) - 1:
        continue
    if index == 0:
        gcd_result = gcd(numbers[index], numbers[index + 1])
    else:
        gcd_result = gcd(gcd_result, numbers[index + 1])

for index, number in enumerate(numbers):
    result += int(int(number) / gcd_result)


print(result)