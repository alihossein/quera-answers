# question : https://quera.ir/problemset/contest/8358/
n = int(input())
negative_cunt = 0
fund_list = input().split(' ')

result = 0
for i in fund_list:
    if int(i) < 0:
        negative_cunt += 1

result = (n * negative_cunt) - negative_cunt

print(result)
