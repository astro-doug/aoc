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
    if invalid_game is False:
            sum_possible_games += game_num
    print(str(sum_possible_games))
input_file.close()
print("Sum of possible games: " + str(sum_possible_games))

print("Puzzle 02 Part II - Cube Conundrum")
print("Loading input...")
input_file = open("input.txt", "r")

sum_powers = 0

for input_line in input_file.readlines():
    game_power = 0
    game_num = 0
    max_red = 0
    max_green = 0
    max_blue = 0

    line_split = input_line.split(":")
    game_num = int(line_split[0].replace("Game ", ""))
    print(input_line)
    # print(str(game_num))
    games_split = line_split[1].strip().split(";")
    for game in games_split:
        each_game_dice = game.strip().split(",")
        # print(each_game_dice)
        for game_die in each_game_dice:
            result = game_die.strip().split(" ")
            # print (result)
            match result[1]:
                case "red":
                    if int(result[0]) > max_red:
                        max_red = int(result[0])
                case "green":
                    if int(result[0]) > max_green:
                        max_green = int(result[0])
                case "blue":
                    if int(result[0]) > max_blue:
                        max_blue = int(result[0])
                case _:
                    print("Unknown die: " + result[1] + "with value of" + result[0])

    game_power = max_red * max_green * max_blue
    print("Game Power: " + str(game_power))
    sum_powers += game_power

    print(str(sum_powers))
input_file.close()
print("Sum of powers: " + str(sum_powers))