# https://quera.ir/problemset/contest/10231/

MOLANA_HAFEZ = ['MOLANA', 'HAFEZ']
input_text = [input() for i in range(5)]

result = []
for i, line in enumerate(input_text):
    if MOLANA_HAFEZ[0] in line or MOLANA_HAFEZ[1] in line:
        result.append(i + 1)
print(*result) if len(result) > 0 else print('NOT FOUND!')
