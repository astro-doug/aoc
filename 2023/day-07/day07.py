import logging
from dataclasses import dataclass


def setup_logging():
    level = logging.DEBUG
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)


possible_cards = ['A'], ['K'], ['Q'], ['J'], ['T'], ['9'], ['8'], ['7'], ['6'], ['5'], ['4'], ['3'], ['2']
possible_hands = (['Five of a Kind'], ['Four of a Kind'], ['Full House'], ['Three of a Kind'], ['Two Pair'],
                  ['One Pair'], ['High Card'])
games = []


@dataclass
class Game:
    hand: str
    bid: int
    hand_type: possible_hands = None
    relative_rank: int = 0
    absolute_rank: int = 0


def determine_hand_type(game):
    cards = list(game.hand)
    if cards[0] == cards[1] == cards[2] == cards[3] == cards[4]:
        game.hand_type = ['Five of a Kind']
        game.absolute_rank = 5
    #elif
    else:
        game.hand_type = ['High Card']
        game.absolute_rank = 1


def main():
    setup_logging()
    logging.info("Advent of Code 2023 - Day 07")
    logging.info("Puzzle 07 Part I - Camel Cards")
    logging.debug("Loading input...")
    with open("input.txt", "r") as input_file:
        for input_line in input_file.readlines():
            # logging.debug(input_line)
            input = list(input_line.split(' '))
            game = Game(hand=input[0], bid=int(input[1]))
            determine_hand_type(game)
            logging.debug(game)
            games.append(game)
    # close the file
    logging.debug("Done")


if __name__ == '__main__':
    main()
