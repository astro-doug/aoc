import logging
from re import Match
import re


def setup_logging():
    level: int = logging.INFO
    fmt: str = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)


def main() -> None:
    setup_logging()
    logging.info("Advent of Code 2024 - Day 03")
    logging.info("https://adventofcode.com/2024/day/3")
    logging.info("Puzzle 03 Part I - Mull It Over")
    memory: str = load_memory()
    logging.info(f"Loaded memory:  {memory}")
    commands: list[str] = parse_memory(memory)
    total: int = perform_calc(commands)
    logging.info(f"Total: {total}")
    logging.info("Puzzle 03 Part II - Mull It Over")


def perform_calc(commands: list[str]) -> int:
    total: int = 0
    val1: int
    val2: int
    multiplier_enabled: bool = True

    for x, instruction in enumerate(commands):
        flag: Match = re.match("(do\(\)|don\'t\(\))", instruction)
        logging.info(f"Flag: {flag}")
        if flag:
            if flag[1] == "do()":
                logging.info("Enabling multiplier")
                multiplier_enabled = True
            elif flag[1] == "don't()":
                logging.info("Disabling multiplier")
                multiplier_enabled = False
        if multiplier_enabled:
            m: Match = re.match("(\w+)\((\d+),(\d+)\)", instruction)
            if m:
                val1 = int(m.group(2))
                val2 = int(m.group(3))
                logging.info(f"Instruction: {instruction} - val1: {val1} - val2: {val2}")
                total = total + (val1 * val2)
    return total


def parse_memory(memory: str) -> list[str]:
    commands: list[str] = re.findall(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)", memory)
    logging.info(f"commands: {commands}")
    return commands


def load_memory() -> str:
    loaded_mem: str = ""
    logging.debug("Loading input...")
    with open("input.txt", "r") as input_file:
        for input_line in input_file.readlines():
            loaded_mem = loaded_mem + input_line
    return loaded_mem


if __name__ == '__main__':
    main()
