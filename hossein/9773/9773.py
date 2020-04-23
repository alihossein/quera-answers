# question : https://quera.ir/problemset/university/9773
diameter = int(input())
diameter /= 2
diameter = int(diameter) + 1
output = ""
for i in range(diameter):
    for j in range(diameter - i - 1):
        output += " "
    for k in range((i * 2) + 1):
        output += "*"
    for l in range((2 * (diameter - i)) - 2):
        output += " "
    for k in range((i * 2) + 1):
        output += "*"
    output += "\n"
for i in reversed(range(diameter - 1)):
    for j in range(diameter - i - 1):
        output += " "
    for k in range((i * 2) + 1):
        output += "*"
    for l in range(2 * (diameter - i) - 2):
        output += " "
    for k in range((i * 2) + 1):
        output += "*"
    output += "\n"
else:
    output = output[0: len(output) - 1]

print(output)
