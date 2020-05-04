# this answer not currect
count = int(input())
numbers = []
for i in range(count):
    numbers.append(int(input()))


#################################################################
def numbers_sum(one_number):
    # to convert number to list of integers
    one_number_array = [int(x) for x in str(one_number)]
    result = 0
    for j in one_number_array:
        result += j
    return result


#################################################################

for num in numbers:

    start_number = num - ((len(str(num))) * 9)
    end_number = num

    flag = False
    for number in range(start_number, end_number):
        res = numbers_sum(one_number=number)
        if res + number == num:
            flag = True
            break

    if flag:
        print('Yes')
    else:
        print('No')
