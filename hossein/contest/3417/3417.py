# https://quera.ir/problemset/contest/3417/
t = int(input())

x_list = [input() for i in range(t)]


# def add_value(num):       #It leads to run time error!
#     result = 0
#     for digit in str(num):
#         result += int(digit)
#     return result

def add_value(num):
    result = 0
    while num != 0:
        result += num % 10
        num = int(num / 10)
    return result

for x in x_list:
    max_diff = len(x) * 9 if int(x) > 9 else int(x)
    x = int(x)
    for i in range(x - max_diff, x):
        temp = i + add_value(i)
        if temp == x: print("Yes");break
    else:
        print("No")