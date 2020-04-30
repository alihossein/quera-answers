# question : https://quera.ir/problemset/contest/3561/
n = 2
my_char = '*'
line_length = 9


def draw(space_ratio, start_loop, shape_count=1):
    for i in range(start_loop, 5):
        line = ''
        for j in range(shape_count):
            star_string = ''
            if i == 0:
                star_string += '*'
            elif 0 < i < 4:
                star_string += '**'
                space_inside_string = ' ' * (2 * i - 1)
                star_string = space_inside_string.join(star_string)
            elif i == 4:
                if j == 0:
                    star_string += '*' * 9
                elif j > 0:
                    star_string += '*' * 8

                space_inside_string = ''
                star_string = space_inside_string.join(star_string)

            left_space_around = (9 - len(star_string))/2
            left_space_around+=i
            left_space_around *= space_ratio
            left_space_around=int(left_space_around)

            right_space_around = (9 - len(star_string))/2
            right_space_around+=i
            right_space_around *= space_ratio
            right_space_around=int(right_space_around)

            line += ' ' * left_space_around + star_string + ' '* right_space_around
        print(line)


for level_number in range(0, n):
    if level_number == 0:
        draw(space_ratio=n - level_number, start_loop=0, shape_count=level_number + 1)
    else:
        draw(space_ratio=n - level_number, start_loop=1, shape_count=level_number + 1)
