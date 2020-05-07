# question : https://quera.ir/problemset/contest/3029/

x_y = input().split(' ')
x = int(x_y[0])

x1_y1 = input().split(' ')
x1 = int(x1_y1[0])

if x1 > x:
    print('Right')
else:
    print('Left')
