# question : https://quera.ir/problemset/contest/3414/
inputs = input()
inputs = inputs.split(' ')

if inputs[0] == inputs[2]:
    print('Vertical')
elif inputs[1] == inputs[3]:
    print('Horizontal')
else:
    print('Try again')
