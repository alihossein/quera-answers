# question : https://quera.ir/problemset/contest/33023/
# get all inputs
n_m = input().split(' ')
n = int(n_m[0])
m = int(n_m[1])
input_list = []
for i in range(n):
    input_list.append(input().split(' '))

# convert string to int
for row in range(n):
    for column in range(m):
        input_list[row][column] = int(input_list[row][column])

result = 0
for row in range(n):
    if row in [0, n - 1]:
        continue
    for column in range(m):
        if column in [0, m - 1]:
            continue
        if input_list[row][column] > input_list[row - 1][column] and input_list[row][column] > input_list[row + 1][column] and input_list[row][column] < input_list[row][column - 1] and input_list[row][column] < input_list[row][column + 1]:
            result += 1
        if input_list[row][column] < input_list[row - 1][column] and input_list[row][column] < input_list[row + 1][column] and input_list[row][column] > input_list[row][column - 1] and input_list[row][column] > input_list[row][column + 1]:
            result += 1

print(result)
