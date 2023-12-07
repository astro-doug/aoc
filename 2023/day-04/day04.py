import logging
import re


def setup_logging():
    level = logging.DEBUG
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)


def main():
    setup_logging()

    logging.info("Advent of Code 2023 - Day 04")
    logging.info("Puzzle 04 Part I - Scratchcards")
    logging.debug("Loading input...")

    total_points = 0

    with open("input.txt", "r") as input_file:
        for input_line in input_file.readlines():
            lottery_card = input_line.replace(":", "|").split("|")
            logging.debug(lottery_card)
            card_number = lottery_card[0]
            logging.debug(card_number)

            winning_numbers = list(map(int, re.split(r'\s+', lottery_card[1].strip())))
            winning_numbers.sort()
            logging.debug(f"Winning Numbers: {winning_numbers}")

            card_numbers = list(map(int, re.split(r'\s+', lottery_card[2].strip())))
            card_numbers.sort()
            logging.debug(f"Cards Numbers: {card_numbers}")

            count_matches = 0
            for num_on_card in card_numbers:
                if num_on_card in winning_numbers:
                    count_matches += 1
            logging.debug(f"Card Matches: {count_matches}")
            if count_matches > 0:
                total_points += 2**(count_matches-1)
            logging.info(f"Total Points: {total_points}")

    logging.debug("Done")
    logging.info(f"Total Points: {total_points}")

if __name__ == '__main__':
    main()
