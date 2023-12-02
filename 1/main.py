input = "1/input.txt"

codes = []
with open(input, 'r') as file:
    for line in file:
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(char)
        if len(digits) == 0:
            code = 0
        elif len(digits) == 1:
            code = digits[0] + digits[0]
        else:
            code = digits[0] + digits[-1]
        codes.append(int(code))

print(sum(codes))