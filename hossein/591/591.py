n = int(input())

STAR="*"
SPACE=' '
print(n*STAR)
tmp=STAR+(SPACE*(n-2))+STAR
for i in range(n-2):
    print(tmp)
print(n*STAR)