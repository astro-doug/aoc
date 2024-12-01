import logging

def setup_logging():
    level: int = logging.INFO
    fmt: str = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)


def main() -> None:
    setup_logging()
    logging.info("Advent of Code 2024 - Day 01")
    logging.info("https://adventofcode.com/2024/day/1")
    logging.info("Puzzle 01 Part I - Historian Hysteria")
    values: list = load_cords()
    logging.info(values)
    distances: list[int] = determine_distances(values[0], values[1])
    total_distance: int = determine_total(distances)
    logging.info(f"Total Distance: {total_distance}")


def determine_total(distances: list[int]) -> int:
    total_distance: int = 0
    for x, distance in enumerate(distances):
        logging.info(f"Distance: {distances[x]}")
        total_distance += distances[x]
    return total_distance


def determine_distances(left: list[int], right: list[int]) -> list[int]:
    distances: list[int] = []
    logging.info(f"Size of Left list: {len(left)}")
    logging.info(f"Size of Right list: {len(right)}")
    for count, left_cord in enumerate(left):
        distances.append(abs(int(left[count]) - int(right[count])))
        logging.info(f"Distance between {left[count]} and {right[count]} is {abs(int(left[count]) - int(right[count]))}")
    return distances


def sort_list(input_list: list[int]) -> None:
    input_list.sort()


def load_cords() -> list:
    left: list[int] = []
    right: list[int] = []
    values: list[list] = []
    logging.debug("Loading input...")
    with open("input.txt", "r") as input_file:
        for input_line in input_file.readlines():
            split_input: list[int] = list(input_line.split('   '))
            left.append(split_input[0])
            sort_list(left)
            #logging.info(f"Left: {left}")
            right.append(int(str(split_input[1]).strip()))
            sort_list(right)
            #logging.info(f"Right: {right}")
    # close the file
    values.append(left)
    values.append(right)
    return values


if __name__ == '__main__':
    main()
