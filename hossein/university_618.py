# question : https://quera.ir/problemset/university/618
ghotr = int(input())
ghotr+=1
output = ""
for i in range(ghotr):
    for j in range(ghotr - i - 1):
        output += " "
    for k in range((i * 2) + 1):
        output += "*"
    output += "\n"
for i in reversed(range(ghotr - 1)):
    for j in range(ghotr - i - 1):
        output += " "
    for k in range((i * 2) + 1):
        output += "*"
    output += "\n"
else:
    output = output[0: len(output) - 1]
print(output)
