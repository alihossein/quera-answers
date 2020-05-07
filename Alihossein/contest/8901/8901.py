x_n = input().split(' ')
x = x_n[1]
n = int(x_n[0])
default_value = {
    'L': 0,
    'M': 0,
    'R': 0,
}
movements = []
for one_input in range(n):
    movements.append(input().split(' '))

default_value[x] = 1
for one_movement in movements:
    temp = default_value.get(one_movement[0])
    default_value[one_movement[0]] = default_value.get(one_movement[1])
    default_value[one_movement[1]] = temp

for index in default_value:
    if default_value.get(index) == 1:
        print(index)
        break
