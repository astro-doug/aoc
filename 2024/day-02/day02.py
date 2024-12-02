import logging


def setup_logging():
    level: int = logging.INFO
    fmt: str = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)


def main() -> None:
    setup_logging()
    logging.info("Advent of Code 2024 - Day 02")
    logging.info("https://adventofcode.com/2024/day/2")
    logging.info("Puzzle 02 Part I - Red-Nosed Reports")
    reports: list[list[int]] = load_reports()
    logging.info(f"Reports: {reports}")
    good_reports: int = 0
    for x, report in enumerate(reports):
        if check_report_safe(report):
            good_reports += 1
            logging.info(f"Good report ascending. tally: {good_reports}")
        else:
            report.reverse()
            if check_report_safe(report):
                good_reports += 1
                logging.info(f"Good report descending. tally: {good_reports}")
    logging.info(f"Number of good reports: {good_reports}")


def check_report_safe(report: list[int]) -> bool:
    safe: bool = False
    prev_value: int = 0

    for x, value in enumerate(report):
        safe = True if prev_value == 0 or (prev_value + 3 >= value > prev_value and value != prev_value) else False
        logging.info(f"{report}: value: {value} -- prev_value: {prev_value} --- Safe: {safe}")
        prev_value = value
        if not safe:
            break
    return safe


def load_reports() -> list[list[int]]:
    report: list[int] = []
    all_reports: list[report] = []
    logging.debug("Loading input...")
    with open("input.txt", "r") as input_file:
        for input_line in input_file.readlines():
            report = list(map(int, input_line.split(' ')))
            all_reports.append(report)
    return all_reports


if __name__ == '__main__':
    main()
