import logging


def setup_logging():
    level: int = logging.DEBUG
    fmt: str = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)


def load_rules(input_line: str) -> list[int]:
    rule: list[int] = list(map(int, input_line.split('|')))
    logging.debug(f"Rule loaded {rule}")
    return rule


def load_input_data(input_line: str) -> list[int]:
    datum: list[int] = list(map(int, input_line.split(',')))
    logging.debug(f"Datum loaded {datum}")
    return datum


def load_data(rules: list[list[int]], data: list[list[int]]) -> None:
    logging.info("Loading input...")
    with open("test_input.txt", "r") as input_file:
        for input_line in input_file.readlines():
            if input_line.__contains__("|"):
                rules.append(load_rules(input_line))
            elif input_line.__contains__(","):
                data.append(load_input_data(input_line))


def main() -> None:
    setup_logging()
    logging.info("Advent of Code 2024 - Day 05")
    logging.info("https://adventofcode.com/2024/day/5")
    logging.info("Puzzle 05 Part I - Print Queue")
    rules: list[list[int]] = []
    data: list[list[int]] = []
    good_data: list[list[int]] = []

    load_data(rules, data)
    logging.debug(f"Data: {data}")
    logging.debug(f"Rules:{rules}")
    for data_block in range(len(data)):
        good_data_block: bool = True
        logging.debug(f"New data block: {data[data_block]}")
        for position in range(len(data[data_block])):
            check_value: int = data[data_block][position]
            logging.debug(f"Value: {check_value}")
            # loop through rules and check if the data block contains both numbers in the rule
            for rule in enumerate(rules):
                logging.debug(f"Rule: {rule[1]}")
                if check_value == rule[1][0]:
                    logging.debug(f"Check value: {check_value} matched")
                    if data[data_block].__contains__(rule[1][1]) > 0:
                        found_position: int = data[data_block].index(rule[1][1])
                        if found_position > -1:
                            logging.debug(f"Data block: {data[data_block]} contains value {rule[1][1]} in position: {found_position}")
                            if found_position > data[data_block].index(check_value):
                                good_data_block = True
                            else:
                                good_data_block = False
                                break

if __name__ == '__main__':
    main()
