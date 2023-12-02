input = "1/input.txt"

nums = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def get_code(line):
    digits = []
    printBool = False
    newLine = line
    for key, value in nums.items():
        indices = [index for index in range(len(newLine)) if newLine.startswith(key, index)]
        if len(indices) > 0:
            printBool = True
        indices.reverse()
        for index in indices:
            newLine = newLine[:index+1] + value + newLine[index:]
    for char in newLine:
        if char.isdigit():
            digits.append(char)
    if len(digits) == 0:
        code = 0
    elif len(digits) == 1:
        code = digits[0] + digits[0]
    else:
        code = digits[0] + digits[-1]

    if printBool:
        print(line + newLine + code)
        print('\n')
    return int(code)

codes = []
with open(input, 'r') as file:
    for line in file:
        codes.append(get_code(line))

print(sum(codes))

# line = "jsgtwonefvmcdsnqfp4fivefivesevenhkbkqcb1vgkshfnxfc\n"
# print(get_code(line))