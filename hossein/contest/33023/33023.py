n_m = input().split(' ')
n = int(n_m[0])
m = int(n_m[1])
A = []
int_cast = lambda x: int(x)


def cmp(A, i, j):
    if A[i + 1][j] < A[i][j] < A[i][j - 1] and A[i - 1][j] < A[i][j] < A[i][j + 1]:
        return True
    if A[i][j - 1] < A[i][j] < A[i + 1][j] and A[i][j + 1] < A[i][j] < A[i - 1][j]:
        return True
    return False


for i in range(n):
    A.append(list(map(int_cast, input().strip().split(' '))))

cnt = 0
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if cmp(A, i, j): cnt = cnt + 1

print(cnt)
