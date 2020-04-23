# question : https://quera.ir/problemset/university/595/
n = int(input())

temp = {}

for i in range(1, n + 1):
    string = ''
    aa = {}
    temp[i] = {}
    for j in range(0, i):
        if j in [0, i - 1]:
            aa[j] = 1
            string = string + ' ' + str(temp.get(0, 1))
        else:
            previous_line = i - 1
            sum_two_numbers = temp.get(previous_line).get(j, 0) + temp.get(previous_line).get(j - 1, 0)
            aa[j] = sum_two_numbers
            string = string + ' ' + str(sum_two_numbers)
    temp[i] = aa
    print(string.strip())
