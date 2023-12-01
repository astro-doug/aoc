print("Advent of Code 2023 - Day 01")
print("Puzzle 1 - Trebuchet?!")
print("Loading input...")
input_file = open("input.txt", "r")
total_calib_value=0
for input_line in input_file.readlines():
    # print(input_line)
    value_count=0
    line_calib_value=0
    for input_char in input_line:
        if input_char.isdigit():
            value_count += 1
            value=int(input_char)
            if value_count == 1:
                line_calib_value = value * 10
            print(line_calib_value)

        total_calib_value += line_calib_value

print("Calibration Value: " + str(total_calib_value))
input_file.close()
