import re

def main():

    input = "4/input.txt"
    sum = 0

    with open(input, 'r') as file:
        for card in file:
            game_points = 0
            game = re.sub(r'Card\s+\d+:\s+', "", card)
            winning_numbers, my_numbers = game.split('|')
            for win_number in list(filter(None, winning_numbers.split(" "))):
                for my_number in list(filter(None, my_numbers.strip().split(" "))):
                    if win_number == my_number:
                        if game_points == 0:
                            game_points = 1
                        else:
                            game_points *= 2
            print(game_points)
            sum += game_points
            
    print(sum)

if __name__ == "__main__":
    main()