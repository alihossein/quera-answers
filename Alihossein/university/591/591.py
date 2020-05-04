# question : https://quera.ir/problemset/university/591/
n = int(input())
my_char = '*'
for i in range(n):
    if i in [0, n - 1]:
        print(my_char * n)
    else:
        space_string = " " * (n - 2)
        string_revised = space_string.join('**')
        print(string_revised)
