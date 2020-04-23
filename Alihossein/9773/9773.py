# question : https://quera.ir/problemset/university/9773
n = int(input())
my_string = '*'
total_string_length = n + 1
for i in range(0, int(n / 2)):
    j = 2 * i + 1
    star_string = my_string * j
    string_length = n - len(star_string)
    string_revised = star_string.center(n)
    print(string_revised + string_revised)

for i in range(int(total_string_length / 2), -1, -1):
    j = 2 * i - 1
    star_string = my_string * j
    string_length = n - len(star_string)
    string_revised = star_string.center(n)
    print(string_revised + string_revised)
