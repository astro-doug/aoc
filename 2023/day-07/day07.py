import logging
from dataclasses import dataclass
from typing import Final
from collections import Counter
from functools import cmp_to_key


def setup_logging():
    level: int = logging.DEBUG
    fmt: str = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)


RANKED_POSSIBLE_CARDS: Final[tuple[str, ...]] = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
RANKED_POSSIBLE_HANDS: Final[tuple[str, ...]] = ('High Card', 'One Pair', 'Two Pair', 'Three of a Kind', 'Full House'
                                                 , 'Four of a Kind', 'Five of a Kind')


@dataclass
class Game:
    hand: str
    bid: int
    hand_type: RANKED_POSSIBLE_HANDS = None
    absolute_rank: int = 0


def determine_hand_type(game: Game) -> None:
    # solution to this found via Reddit
    # https://github.com/mgtezak/Advent_of_Code/blob/master/2023/Day_07.py
    # You-Tube video for explanation: https://www.youtube.com/watch?v=ZZIsVVJTyBk
    counts: list[int] = sorted(Counter(game.hand).values(), reverse=True)
    if counts[0] == 5:
        game.hand_type = 'Five of a Kind'
    elif counts[0] == 4:
        game.hand_type = 'Four of a Kind'
    elif counts[0] == 3:
        if counts[1] == 2:
            game.hand_type = 'Full House'
        else:
            game.hand_type = 'Three of a Kind'
    elif counts[0] == 2:
        if counts[1] == 2:
            game.hand_type = 'Two Pair'
        else:
            game.hand_type = 'One Pair'
    elif counts[0] == 1:
        game.hand_type = 'High Card'


def compare(a: Game, b: Game) -> int:
    determine_hand_type(a)
    determine_hand_type(b)
    if RANKED_POSSIBLE_HANDS.index(a.hand_type) > RANKED_POSSIBLE_HANDS.index(b.hand_type):
        return 1
    elif RANKED_POSSIBLE_HANDS.index(a.hand_type) < RANKED_POSSIBLE_HANDS.index(b.hand_type):
        return -1
    else:
        for i, j in zip(a.hand, b.hand):
            if RANKED_POSSIBLE_CARDS.index(i) == RANKED_POSSIBLE_CARDS.index(j):
                continue
            if RANKED_POSSIBLE_CARDS.index(i) > RANKED_POSSIBLE_CARDS.index(j):
                return 1
            elif RANKED_POSSIBLE_CARDS.index(i) < RANKED_POSSIBLE_CARDS.index(j):
                return -1


def main() -> None:
    games: list[Game] = []
    total_winnings: int = 0
    setup_logging()
    logging.info("Advent of Code 2023 - Day 07")
    logging.info("https://adventofcode.com/2023/day/7")
    logging.info("Puzzle 07 Part I - Camel Cards")
    logging.debug("Loading input...")
    with open("input.txt", "r") as input_file:
        for input_line in input_file.readlines():
            # logging.debug(input_line)
            split_input: list[str] = list(input_line.split(' '))
            game: Game = Game(hand=split_input[0], bid=int(split_input[1]))
            # logging.debug(game)
            games.append(game)
    logging.debug("Games loaded - time to sort:")
    games.sort(key=cmp_to_key(compare))
    # close the file

    for count, game in enumerate(games, start=1):
        game.absolute_rank = count
        total_winnings += game.bid * count

    logging.debug("Games all sorted")
    logging.debug(games)

    logging.debug(f"Total Winnings: {total_winnings}")
    logging.debug("End Day 07 Part I")


if __name__ == '__main__':
    main()
