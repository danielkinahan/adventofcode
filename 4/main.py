import re

def main():

    input = "4/input.txt"
    #sum = 0
    copy_list = [1] * 200

    with open(input, 'r') as file:

        index = 0
        for card in file:
            copies = 0
            game_points = 0
            game = re.sub(r'Card\s+\d+:\s+', "", card)
            winning_numbers, my_numbers = game.split('|')
            for win_number in list(filter(None, winning_numbers.split(" "))):
                for my_number in list(filter(None, my_numbers.strip().split(" "))):
                    if win_number == my_number:
                        copies += 1
                        if game_points == 0:
                            game_points = 1
                        else:
                            game_points *= 2
            for i in range(index+1, index+copies+1):
                copy_list[i] += 1
            #sum += game_points*copy_list[index]
            index += 1
            
    print(sum(copy_list))

if __name__ == "__main__":
    main()