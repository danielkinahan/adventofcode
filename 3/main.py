import re

_max_length = 0
_max_width = 0

def is_symbol(schematic, y, x):

    if (x < 0 or x >= _max_width-1 or y < 0 or y >= _max_length):
        return False

    if schematic[y][x].isdigit():
        return False
    if schematic[y][x] == '.':
        return False
    return True


def symbol_in_boundary(schematic, index_tuple, length):

    y, x = index_tuple #index of first digit of number
    ybound_top = y-1
    ybound_bottom = y+2
    xbound_left = x-1
    xbound_right = x+length+1

    for iy in range(ybound_top, ybound_bottom):
        for ix in range(xbound_left, xbound_right):
            # print(f'{schematic[iy][ix]} at row{iy} col{ix}')
            if is_symbol(schematic, iy, ix):
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
            schematic.append(list(line.strip()))

        all_numbers = []

        # Collect all numbers and their indices
        for i in range(_max_length):
            numbers = re.finditer(r'\b\d+\b', lines[i])
            for match in numbers:
                number = match.group()
                x = match.start()
                all_numbers.append((i, x, len(number)))

        # Check surroundings of collected numbers for symbols
        for number_data in all_numbers:
            if symbol_in_boundary(schematic, number_data[:2], number_data[2]):
                sum += int(lines[number_data[0]][number_data[1]:number_data[1] + number_data[2]])


    print(sum)

if __name__ == "__main__":
    main()