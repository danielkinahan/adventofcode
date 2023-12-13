import re

_max_length = 0
_max_width = 0

def is_digit_or_dot(schematic, y, x):

    if (x < 0 or x >= _max_width or y < 0 or y >= _max_length):
        return True

    if schematic[y][x].isdigit():
        return True
    if schematic[y][x] == '.':
        return True
    return False


def symbol_in_boundary(index_tuple, length, schematic):

    y, x = index_tuple #index of first digit of number
    ybound_top = y-1
    ybound_bottom = y+1
    xbound_left = x-1
    xbound_right = x+length

    for iy in range(ybound_top, ybound_bottom):
        for ix in range(xbound_left, xbound_right):
            if not is_digit_or_dot(schematic, iy, ix):
                return True
    
    return False

def main():

    global _max_length 
    global _max_width

    input = "3/input.txt"
    schematic = []
    sum = 0

    with open(input, 'r') as file:
        lines = file.readlines()

        _max_length = len(lines)
        _max_width = len(lines[0])

        for line in lines:
            schematic.append(list(line))

        for i in range(_max_length):
            numbers = re.sub(r'[^0-9]', ' ', lines[i])
            number_list = list(filter(None, numbers.split(' ')))
            for number in number_list:
                x = lines[i].index(number)
                if symbol_in_boundary((i, x), len(number), schematic):
                    sum += int(number)

    print(sum)

if __name__ == "__main__":
    main()