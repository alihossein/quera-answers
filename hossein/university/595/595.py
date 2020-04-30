# question : https://quera.ir/problemset/university/595/
n = int(input())


def sum(cur_list, index, max_len):
    if index == 0:
        return 1
    if index >= max_len:
        return cur_list[index - 1]
    elif index < 0:
        return 0
    return cur_list[index - 1] + cur_list[index]


next_list = []
cur_list = [1]
for i in range(n):
    for j in range(i + 1):
        add_val = sum(cur_list, j, i)
        print(add_val,'', end='')
        next_list.append(add_val)
    print()
    cur_list = next_list.copy()
    next_list = []
