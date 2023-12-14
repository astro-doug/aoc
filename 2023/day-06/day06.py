import logging
import re
from dataclasses import dataclass

def setup_logging():
    level = logging.DEBUG
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level = level, format=fmt)

@dataclass
class Race:
    raceID: int
    race_time: int
    race_distance: int
    ways_to_win: int = 0

def count_race_wins_margin(races=None):
    if races is None:
        races = []
    total_race_wins_margin = 1

    for race in races:
        total_race_wins_margin *= race.ways_to_win

    return total_race_wins_margin

def determine_if_win(current_race):
    for velocity in range(1, current_race.race_time):
        distance_travelled = velocity * (current_race.race_time - velocity)
        # logging.debug(f'Race: {current_race.raceID} - Velocity tested: {velocity} - Distance Travelled: {distance_travelled}')
        if distance_travelled > current_race.race_distance:
            #logging.debug(f'We can win this way')
            current_race.ways_to_win += 1
        else:
            if current_race.ways_to_win > 1:
                break


def main():
    setup_logging()
    logging.info("Advent of Code 2023 - Day 06")
    logging.info("Puzzle 06 Part I - Wait For It")
    logging.debug("Loading input...")
    with open("input.txt", "r") as input_file:
        race_times_line = input_file.readline().replace('Time:', '')
        race_times = list(map(int, re.split(r'\s+', race_times_line.strip())))

        distance_lines = input_file.readline().replace('Distance:', '')
        race_distances = list(map(int, re.split(r'\s+', distance_lines.strip())))
    # close the file
    races = []
    for count, x in enumerate(race_times):
        race = Race(raceID=count, race_time=race_times[count], race_distance=race_distances[count])
        determine_if_win(race)
        races.append(race)

    logging.debug(f'Races: {races}')

    logging.info(f'Margin of Error for {count + 1} races: {count_race_wins_margin(races)}ms')

    logging.info("Puzzle 06 Part II - Wait For It")
    logging.debug("Re-reading input, ignoring kerning...")
    with open("input.txt", "r") as input_file:
        race_times_line = input_file.readline().replace('Time:', '').replace(' ', '')
        long_race_time = int(race_times_line.strip())

        distance_lines = input_file.readline().replace('Distance:', '').replace(' ', '')
        long_race_distance = int(distance_lines.strip())
    # close the file
    races = []
    race = Race(raceID=count, race_time=long_race_time, race_distance=long_race_distance)
    determine_if_win(race)
    races.append(race)

    logging.debug(f'Long Race: {race}')

    logging.info(f'Margin of Error for Long race: {count_race_wins_margin(races)}ms')

    logging.info("Done")

if __name__ == '__main__':
    main()

