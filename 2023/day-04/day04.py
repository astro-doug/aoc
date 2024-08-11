import logging
import re


def setup_logging():
    level = logging.DEBUG
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)


def main():
    setup_logging()

    logging.info("Advent of Code 2023 - Day 04")
    logging.info("https://adventofcode.com/2023/day/4")
    logging.info("Puzzle 04 Part I - Scratchcards")
    logging.debug("Loading input...")

    total_points = 0
    lottery_cards = []
    # new_lottery_cards = []

    with open("input.txt", "r") as input_file:
        for input_line in input_file.readlines():
            lottery_card = input_line.replace(":", "|").split("|")
            lottery_card.append(1)
            # store away for part II so I don't have to re-read the file
            lottery_cards.append(lottery_card)

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
            logging.info(f"Count of Number Matches: {count_matches}")
            if count_matches > 0:
                total_points += 2**(count_matches-1)
            logging.info(f"Sub-Total Points: {total_points}")

    logging.debug("Done")
    logging.info(f"Total Points: {total_points}")

    logging.info("Puzzle 04 Part II - Scratchcards")
    logging.debug("Looping through Lottery Cards Again...")
    total_cards = 0

    for lottery_card in lottery_cards:
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
        logging.debug(f"Count of Number Matches: {count_matches}")

        if count_matches > 0:
            logging.info(f"Will create {lottery_card[3]} copies of each of the next {count_matches} cards")
            # cards_to_add = []
            for counter in range(count_matches):
                card_to_add = lottery_cards[lottery_cards.index(lottery_card) + counter + 1]
                card_to_add[3] += lottery_card[3]
                logging.debug(f"Card: {card_to_add[0]} now has {card_to_add[3]} occurrences")

    for lottery_card in lottery_cards:
        total_cards += lottery_card[3]
    logging.info(f"There are {total_cards} lottery cards in the stack")


if __name__ == '__main__':
    main()
