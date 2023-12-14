import re

_max_length = 0
_max_width = 0


def outside_bounds(y,x):
    if (x < 0 or x >= _max_width-1 or y < 0 or y >= _max_length):
        return True
    return False
    
def is_digit(schematic, y, x):
    if schematic[y][x].isdigit():
        return True
    return False

def is_dot(schematic, y, x):
    if schematic[y][x] == '.':
        return True
    return False

def is_symbol(schematic, y, x):

    if outside_bounds(y,x):
        return False

    if is_digit(schematic, y, x):
        return False
    
    if is_dot(schematic, y, x):
        return False
    
    return True

def symbol_in_boundary(schematic, index_tuple, length):

    y, x = index_tuple #index of first digit of number
    ybound_top = y-1
    ybound_bottom = y+2
    xbound_left = x-1
    xbound_right = x+length+1
    
    gears = []
    symbol_present = False

    for iy in range(ybound_top, ybound_bottom):
        for ix in range(xbound_left, xbound_right):
            # print(f'{schematic[iy][ix]} at row{iy} col{ix}')
            if is_symbol(schematic, iy, ix):
                symbol_present = True
                if schematic[iy][ix] == '*':
                    gears.append((iy, ix))
    
    return symbol_present, gears

def get_number_from_digit(all_numbers, y, x):
    for number in all_numbers:
        end_index = number[1] + number[2]
        if number[0] == y:
            if number[1] <= x < end_index:
                return number
    print(f"Couldn't find number that contains coordinates {y}-{x}")

def get_matching_gear_part(schematic, all_numbers, gear, original_number):
    y, x = gear
    ybound_top = y-1
    ybound_bottom = y+2
    xbound_left = x-1
    xbound_right = x+2

    surrounding_numbers = []
    surround_list = []

    for iy in range(ybound_top, ybound_bottom):
        for ix in range(xbound_left, xbound_right):
            surround_list.append(schematic[iy][ix])
            if is_digit(schematic, iy, ix):
                number = get_number_from_digit(all_numbers, iy, ix) 
                if number not in surrounding_numbers and number != original_number:
                    surrounding_numbers.append(number)

    if len(surrounding_numbers) == 0:
        return None
    elif len(surrounding_numbers) > 1:
        print('Too many matches')
    else:
        return surrounding_numbers[0]

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

        # list of tuples that contain y, x and length of number
        all_numbers = []
        all_gears = []

        # Collect all numbers and their indices
        for i in range(_max_length):
            numbers = re.finditer(r'\b\d+\b', lines[i])
            for match in numbers:
                number = match.group()
                x = match.start()
                all_numbers.append((i, x, len(number)))

        # Check surroundings of collected numbers for symbols
        for number_data in all_numbers:
            symbol_present, gears = symbol_in_boundary(schematic, number_data[:2], number_data[2])
            number = int(lines[number_data[0]][number_data[1]:number_data[1] + number_data[2]])
            print(number)
            if symbol_present:
                # if not gears:
                #     sum += number
                # else:
                for gear in gears:
                    if gear not in all_gears:
                        all_gears.append(gear)
                        matching_gear = get_matching_gear_part(schematic, all_numbers, gear, number_data)
                        if matching_gear:
                            matching_gear_number = int(lines[matching_gear[0]][matching_gear[1]:matching_gear[1] + matching_gear[2]])
                            sum += (number*matching_gear_number)
                            # else:
                            #     sum+= number
                    


    print(sum)

if __name__ == "__main__":
    main()