# question : https://quera.ir/problemset/university/618
n = int(input())
my_string = '*'
total_string_length = 2 * n + 1
for i in range(0, int(total_string_length / 2)):
    j = 2 * i + 1
    star_string = my_string * j
    string_length = total_string_length - len(star_string)
    string_revised = star_string.center(total_string_length)
    print(string_revised)

for i in range(int(total_string_length / 2), -1, -1):
    j = 2 * i + 1
    star_string = my_string * j
    string_length = total_string_length - len(star_string)
    string_revised = star_string.center(total_string_length)
    print(string_revised)
