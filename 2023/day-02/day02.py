print("Advent of Code 2023 - Day 02")
print("Puzzle 02 Part I - Cube Conundrum")
print("Loading input...")
input_file = open("input.txt", "r")

game_num = 0
invalid_game = False
sum_possible_games = 0

for input_line in input_file.readlines():

    line_split = input_line.split(":")
    game_num = int(line_split[0].replace("Game ", ""))
    print(input_line)
    # print(str(game_num))
    invalid_game = False
    games_split = line_split[1].strip().split(";")
    for game in games_split:
        each_game_dice = game.strip().split(",")
        # print(each_game_dice)
        for game_die in each_game_dice:
            result = game_die.strip().split(" ")
            # print (result)
            match result[1]:
                case "red":
                    if int(result[0]) > 12:
                        invalid_game = True
                case "green":
                    if int(result[0]) > 13:
                        invalid_game = True
                case "blue":
                    if int(result[0]) > 14:
                        invalid_game = True
                case _:
                    print("Unknown die: " + result[1] + "with value of" + result[0])
        print(invalid_game)
    if invalid_game == False:
            sum_possible_games += game_num
    print(str(sum_possible_games))
input_file.close()
print("Sum of possible games: " + str(sum_possible_games))