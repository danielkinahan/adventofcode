import numpy as np

input = "2/input.txt"

totalCubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def isPossibleGame(values):
    for draw in values.split("; "):
        for cube in draw.split(", "):
            count, colour = cube.split(" ")
            if int(count) > totalCubes[colour.strip()]:
                return False
    return True

def minimumSetPower(values):
    maxCubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for draw in values.split("; "):
        for cube in draw.split(", "):

            count, colour = cube.split(" ")
            colour = colour.strip()
            count = int(count)
            if count > maxCubes[colour]:
                maxCubes[colour] = count

    return np.product(list(maxCubes.values()))

ids = []
powers = []
with open(input, 'r') as file:
    for line in file:
        game, values = line.split(": ")
        id = int(game.replace("Game ", ""))
        if isPossibleGame(values):
            ids.append(id)
        powers.append(minimumSetPower(values))
print(sum(ids))
print(sum(powers))
