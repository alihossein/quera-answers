# https://quera.ir/problemset/contest/52544

CORNER_ONE = {(0, 0), (0, 1), (0, 2), (0, 6), (0, 7), (0, 8),
              (1, 0), (1, 2), (1, 6), (1, 8),
              (2, 0), (2, 1), (2, 2), (2, 6), (2, 7), (2, 8),
              (6, 0), (6, 1), (6, 2), (6, 6), (6, 7), (6, 8),
              (7, 0), (7, 2), (7, 6), (7, 8),
              (8, 0), (8, 1), (8, 2), (8, 6), (8, 7), (8, 8)}
CORNER_ZERO = {(1, 1), (1, 7),
               (7, 1), (7, 7)}
result = 1
mat = [input() for i in range(9)]
result_mat = []
for line in mat:
    result_mat.append([int(val) for val in line])

mat = result_mat

for line in enumerate(mat):
    for in_line in enumerate(line[1]):
        if (line[0], in_line[0]) in CORNER_ONE:
            if in_line[1] == 0:
                print(0)
                exit(0)
            continue
        if (line[0], in_line[0]) in CORNER_ZERO:
            if in_line[1] == 1:
                print(0)
                exit(0)
            continue
        if in_line[1] == 2:
            result *= 2
print(result)
