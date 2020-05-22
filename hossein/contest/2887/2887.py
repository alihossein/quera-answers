# https://quera.ir/problemset/contest/2887/

n = int(input())
A_str = input().split(' ')
A = list(map(lambda x: int(x), A_str))


def find_gcd(my_list):
    def gcd(first, second):
        while second:
            first, second = second, first % second
        return first

    result = my_list[0]
    for val in my_list:
        result = gcd(result, val)
        if result == 1:
            return 1
    return result

addiction_level = find_gcd(A)
result = 0
for val in A:
    temp = int(val) / addiction_level
    result += temp

print(int(result))
