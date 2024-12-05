import logging
import re
from typing import Final

WORD: Final[str] = "XMAS"
DIRECTIONS: Final[list[list[int]]] = [[-1, -1], [0, -1], [1, -1],
                                      [-1, 0], [1, 0],
                                      [-1, 1], [0, 1], [1, 1]]


def setup_logging():
    level: int = logging.INFO
    fmt: str = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)


def load_puzzle() -> list[list[str]]:
    puzzle: list[list[str]] = []
    logging.debug("Loading input...")
    with open("input.txt", "r") as input_file:
        for input_line in input_file.readlines():
            row:list[str] = re.findall('\w', input_line)
            logging.info(f"Row: {row}")
            puzzle.append(row)
    logging.info(f"Puzzle: {puzzle}")
    return puzzle


def is_in_bounds(x: int, y: int, puzzle_width: int, puzzle_height: int) -> bool:
    in_bounds: bool = 0 <= x < puzzle_width and 0 <= y < puzzle_height
    logging.info(f"Letter found, but ({x}, {y}) is out of bounds - returning False")
    return in_bounds


def find_word_in_direction(puzzle: list[list[str]], x: int, y: int, dir_x: int, dir_y: int, word_location: int):
    if word_location == len(WORD):
        return True

    logging.info(f"Checking spot ({x}, {y}) for character {WORD[word_location]}")

    if is_in_bounds(x, y, len(puzzle), len(puzzle[0])) and WORD[word_location] == puzzle[x][y]:
        logging.info(f"Letter {WORD[word_location]} found")
        return find_word_in_direction(puzzle, x + dir_x, y + dir_y, dir_x, dir_y, word_location + 1)
    return False


def main() -> None:
    setup_logging()
    logging.info("Advent of Code 2024 - Day 04")
    logging.info("https://adventofcode.com/2024/day/4")
    logging.info("Puzzle 04 Part I - Ceres Search")
    puzzle: list[list[str]] = load_puzzle()
    puzzle_width: int = len(puzzle)
    puzzle_height: int = len(puzzle[0])
    logging.info(f"Puzzle dimensions: [{puzzle_width}, {puzzle_height}]")
    times_found: int = 0
    for col in range(puzzle_width):
        for row in range(puzzle_height):
            if puzzle[col][row] == WORD[0]:
                logging.info(f"Found potential start of word at ({col}, {row})")
                for dir_x, dir_y in DIRECTIONS:
                    if find_word_in_direction(puzzle, col, row, dir_x, dir_y, 0):
                        logging.info(f"{WORD} found beginning at ({col}, {row})")
                        times_found += 1
                        # break
            # if word_found(puzzle, 0, 0, col, row, puzzle_width, puzzle_height, 0):
            #    times_found += 1
            #    logging.info(f"{WORD} found beginning at ({col}, {row})")
    logging.info(f"Found {times_found} occurrences of {WORD} in the puzzle")


if __name__ == '__main__':
    main()


# my attempt that doesn't work - I'll revist later maybe :)
def word_found(puzzle: list[list[str]], dir_x: int, dir_y: int, x: int, y: int, puzzle_width: int, puzzle_height: int, word_location: int) -> bool:
    # found: bool = False
    logging.info(f"Checking spot ({x}, {y}) in direction [{dir_x}, {dir_y}] for character {WORD[word_location]}")
    if puzzle[x][y] == WORD[word_location]:
        logging.info(f"Letter {WORD[word_location]} found")
        # if the value of word_location is the same as the length of the word we are searching for, then we found
        # the whole word, return true
        if word_location == len(WORD) - 1:
            logging.info("Full word found - should exit recursive loop")
            return True
        # Letter found, now search in the direction already being searched for the next letter
        # word_location += 1

        for dir_x, dir_y in DIRECTIONS:
            new_x: int = x + dir_x
            new_y: int = y + dir_y
            if is_in_bounds(new_x, new_y, puzzle_width, puzzle_height):
                # legal position to continue to check - recursive call to check that space for the next letter
                logging.info(f"Recursively calling with ({new_x}, {new_y}) in direction [{dir_x},{dir_y}] for character {WORD[word_location + 1]}")
                return word_found(puzzle, dir_x, dir_y, new_x, new_y, puzzle_width, puzzle_height, word_location + 1)
            else:
                logging.info(f"Letter found, but ({new_x}, {new_y}) is out of bounds - returning False")
                return False
                #found = False
    else:
        logging.info(f"Letter {puzzle[x][y]} found instead of {WORD[word_location]}")
        return False
    #return found