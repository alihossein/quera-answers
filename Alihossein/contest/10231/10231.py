# question : https://quera.ir/problemset/contest/10231/

result = ''
inputs = []
for i in range(5):
    inputs.append(input())

for i, one_string in enumerate(inputs):
    if one_string.find('MOLANA') >= 0 or one_string.find('HAFEZ') >= 0:
        result = result + str(i + 1) + ' '

if result == '':
    print('NOT FOUND!')
else:
    print(result.strip())
