ghotr = int(input())
ghotr /= 2
ghotr=int(ghotr)+1
output = ""


def star(input):
    result = ""
    for i in range(input):
        result += "*"
    return result


def space(input):
    result = ""
    for i in range(input):
        result += " "
    return result


for i in range(ghotr):
    for j in range(ghotr - i - 1):
        output += " "
    for k in range((i * 2) + 1):
        output += "*"
    for l in range((2 * (ghotr - i)) - 2):
        output += " "
    for k in range((i * 2) + 1):
        output += "*"
    output += "\n"
for i in reversed(range(ghotr - 1)):
    for j in range(ghotr - i - 1):
        output += " "
    for k in range((i * 2) + 1):
        output += "*"
    for l in range(2 * (ghotr - i) -2):
        output += " "
    for k in range((i * 2) + 1):
        output += "*"
    output += "\n"
else:
    output = output[0: len(output) - 1]
print(output)
