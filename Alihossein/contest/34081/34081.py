# question : https://quera.ir/problemset/contest/34081
numbers = input()
numbers = numbers.split(' ')
# queue length
n = int(numbers[0])

k = int(numbers[1])

turn_number = 1
step = 0
while True:
    if turn_number + k <= n:
        turn_number += k
    else:
        turn_number = (turn_number + k) - n
    step += 1
    if turn_number == 1:
        print(step)
        break
