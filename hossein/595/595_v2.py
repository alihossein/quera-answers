plus = lambda x, y: x + y
current_list = [0, 1]
next_list = []
n = int(input())
if n > 0: print(1)
for i in range(n-1):
    current_list.append(0)
    next_list = list(map(plus, current_list[1:], current_list))
    print(*next_list,sep=' ')
    current_list = next_list
    current_list.insert(0, 0)
    next_list = []