import logging
from dataclasses import dataclass
from typing import Final
from collections import Counter
from functools import cmp_to_key


def setup_logging():
    level: int = logging.INFO
    fmt: str = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)


RANKED_POSSIBLE_CARDS: Final[tuple[str, ...]] = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
RANKED_POSSIBLE_WILD_CARDS: Final[tuple[str, ...]] = ('J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A')
RANKED_POSSIBLE_HANDS: Final[tuple[str, ...]] = ('High Card', 'One Pair', 'Two Pair', 'Three of a Kind', 'Full House'
                                                 , 'Four of a Kind', 'Five of a Kind')
j_is_joker: bool = False


@dataclass(slots=True, kw_only=True) # slots implemented in 3.10 and later
class Game:
    hand: str
    no_joker: str
    bid: int
    hand_type: RANKED_POSSIBLE_HANDS = None
    absolute_rank: int = 0


def determine_hand_type(game: Game) -> None:
    global j_is_joker
    # solution to this found via Reddit
    # https://github.com/mgtezak/Advent_of_Code/blob/master/2023/Day_07.py
    # You-Tube video for explanation: https://www.youtube.com/watch?v=ZZIsVVJTyBk

    joker_count: int = 0
    if j_is_joker:
        joker_count = game.hand.count('J')
        logging.debug(f"pre removal: {game.hand}")
        game.no_joker = [x for x in game.hand if x != 'J']
        logging.debug(f"hand: {game.no_joker} + {joker_count} jokers")
        counts: list[int] = sorted(Counter(game.no_joker).values(), reverse=True)
    else:
        counts: list[int] = sorted(Counter(game.hand).values(), reverse=True)
    logging.debug(f"counts: {counts}")
    if not counts:
        counts = [0]
    if counts[0] + joker_count == 5:
        game.hand_type = 'Five of a Kind'
    elif counts[0] + joker_count == 4:
        game.hand_type = 'Four of a Kind'
    elif counts[0] + joker_count == 3 and counts[1] == 2:
        game.hand_type = 'Full House'
    elif counts[0] + joker_count == 3:
        game.hand_type = 'Three of a Kind'
    elif counts[0] + joker_count == 2 and counts[1] == 2:
        game.hand_type = 'Two Pair'
    elif counts[0] + joker_count == 2:
        game.hand_type = 'One Pair'
    else:
        game.hand_type = 'High Card'
    logging.debug(f"hand type: {game.hand_type}")


def compare(a: Game, b: Game) -> int:
    global j_is_joker
    determine_hand_type(a)
    determine_hand_type(b)
    logging.debug("1")
    if RANKED_POSSIBLE_HANDS.index(a.hand_type) > RANKED_POSSIBLE_HANDS.index(b.hand_type):
        logging.debug("bigger")
        return 1
    elif RANKED_POSSIBLE_HANDS.index(a.hand_type) < RANKED_POSSIBLE_HANDS.index(b.hand_type):
        logging.debug("smaller")
        return -1
    else:
        if j_is_joker:
            for i, j in zip(a.hand, b.hand):
                if RANKED_POSSIBLE_WILD_CARDS.index(i) == RANKED_POSSIBLE_WILD_CARDS.index(j):
                    continue
                if RANKED_POSSIBLE_WILD_CARDS.index(i) > RANKED_POSSIBLE_WILD_CARDS.index(j):
                    return 1
                elif RANKED_POSSIBLE_WILD_CARDS.index(i) < RANKED_POSSIBLE_WILD_CARDS.index(j):
                    return -1
        else:
            logging.debug("zipping")
            logging.debug(f"a:{a}")
            logging.debug(f"b:{b}")

            for i, j in zip(a.hand, b.hand):
                if RANKED_POSSIBLE_CARDS.index(i) == RANKED_POSSIBLE_CARDS.index(j):
                    logging.debug("equal")
                    continue
                if RANKED_POSSIBLE_CARDS.index(i) > RANKED_POSSIBLE_CARDS.index(j):
                    logging.debug("bigger")
                    return 1
                elif RANKED_POSSIBLE_CARDS.index(i) < RANKED_POSSIBLE_CARDS.index(j):
                    logging.debug("smaller")
                    return -1


def main() -> None:
    global j_is_joker
    total_winnings: int = 0
    setup_logging()
    logging.info("Advent of Code 2023 - Day 07")
    logging.info("https://adventofcode.com/2023/day/7")
    logging.info("Puzzle 07 Part I - Camel Cards")
    games: list[Game] = load_games()
    logging.debug("Games loaded - time to sort:")
    games.sort(key=cmp_to_key(compare))

    for count, game in enumerate(games, start=1):
        game.absolute_rank = count
        total_winnings += game.bid * count

    logging.debug("Games all sorted")
    logging.debug(games)

    logging.info(f"Total Winnings: {total_winnings}")
    logging.info("End Day 07 Part I")

    logging.info("Puzzle 07 - Part II - Camel Cards")
    logging.info("Jacks replaced by Jokers - Wild")
    j_is_joker = True
    total_winnings = 0
    games = []
    games = load_games()

    games.sort(key=cmp_to_key(compare))

    for count, game in enumerate(games, start=1):
        game.absolute_rank = count
        total_winnings += game.bid * count
    logging.debug(games)
    logging.info(f"Total Winnings: {total_winnings}")
    logging.info("End Day 07 Part II")


def load_games() -> list[Game]:
    games: list[Game] = []
    logging.debug("Loading input...")
    with open("input.txt", "r") as input_file:
        for input_line in input_file.readlines():
            split_input: list[str] = list(input_line.split(' '))
            game: Game = Game(hand=split_input[0], no_joker=split_input[0], bid=int(split_input[1]))
            games.append(game)
    # close the file
    return games


if __name__ == '__main__':
    main()
