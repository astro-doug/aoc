import logging

def setup_logging():
    level = logging.DEBUG
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level = level, format=fmt)

def main():
    setup_logging()
    logging.info("Advent of Code 2023 - Day 03")
    logging.info("https://adventofcode.com/2023/day/3")
    logging.info("Puzzle 03 Part I - Gear Ratios")
    logging.debug("Loading input...")
    with open("input.txt", "r") as input_file:
        for input_line in input_file.readlines():
            logging.debug(input_line)
    logging.debug("Done")

if __name__ == '__main__':
    main()
