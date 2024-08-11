print("Advent of Code 2023 - Day 01")
print("https://adventofcode.com/2023/day/1")
print("Puzzle 1 Part I - Trebuchet?!")
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
            # print(line_calib_value)

        # total_calib_value += line_calib_value
    # reverse the input_line and grab the last number (will be the first after reversing the string
    value_count=0
    reversed_line = format(input_line[::-1])
    for rev_input_char in reversed_line:
        if rev_input_char.isdigit():
            value_count += 1
            value=int(rev_input_char)
            if value_count == 1:
                line_calib_value += value
                # print(input_line + "----" + str(line_calib_value))

    total_calib_value += line_calib_value
print("Calibration Value: " + str(total_calib_value))
input_file.close()


print("Puzzle 1 Part II - Trebuchet?!")
print("Loading input...")
input_file = open("input.txt", "r")
total_calib_value=0
text_numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
int_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for input_line in input_file.readlines():
    # value_count = 0
    line_calib_value = 0
    first_int_loc = len(input_line)
    first_text_loc = len(input_line)
    int_value = 0
    text_value = 0

    # print(input_line)

    for number in text_numbers:
        loc = input_line.find(number)
        # print(str(loc) + " : " + str(first_text_loc))
        if loc > -1 and loc < first_text_loc:
            first_text_loc = loc
            text_value = text_numbers.index(number)
            # print("value: " + str(number) + " found with numeric value: " + str(text_value))

    for number in int_numbers:
        loc = input_line.find(str(number))
        # print(str(loc) + " : " + str(first_int_loc))
        if loc > -1 and loc < first_int_loc:
            first_int_loc = loc
            int_value = int_numbers.index(number)
            # print("value: " + str(number) + " found with int value: " + str(int_value))
    if first_text_loc < first_int_loc:
        line_calib_value += (text_value * 10)
    else:
        line_calib_value += (int_value*10)
    # print("Line Calib Value: " + str(line_calib_value))


    # reverse the line and look for the last number
    reversed_line = format(input_line[::-1])
    first_int_loc = len(input_line)
    first_text_loc = len(input_line)
    int_value = 0
    text_value = 0
    # print (reversed_line)
    for number in text_numbers:
        loc = reversed_line.find(format(number[::-1]))
        # print(str(loc) + " : " + str(first_text_loc))
        if loc > -1 and loc < first_text_loc:
            first_text_loc = loc
            text_value = text_numbers.index(number)
            # print("value: " + str(number) + " found with numeric value: " + str(text_value))

    for number in int_numbers:
        loc = reversed_line.find(str(number))
        # print(str(loc) + " : " + str(first_int_loc))
        if loc > -1 and loc < first_int_loc:
            first_int_loc = loc
            int_value = int_numbers.index(number)
            # print("value: " + str(number) + " found with int value: " + str(int_value))
    if first_text_loc < first_int_loc:
        line_calib_value += text_value
    else:
        line_calib_value += int_value
    # print("Line Calib Value: " + str(line_calib_value))

    total_calib_value += line_calib_value

print("Calibration Value: " + str(total_calib_value))
input_file.close()