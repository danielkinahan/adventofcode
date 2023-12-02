input = "2/input.txt"

totalCubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def isPossibleGame(values):
    for draw in values.split("; "):
        for cubes in draw.split(", "):
            count, colour = cubes.split(" ")
            if int(count) > totalCubes[colour.strip()]:
                return False
    return True 

ids = []
with open(input, 'r') as file:
    for line in file:
        game, values = line.split(": ")
        id = int(game.replace("Game ", ""))
        if isPossibleGame(values):
            ids.append(id)
print(sum(ids))