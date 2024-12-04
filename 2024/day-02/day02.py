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
    # logging.info(f"Reports: {reports}")
    good_reports = check_reports(reports, dampener_engaged=False)
    logging.info(f"Number of good reports: {good_reports}")
    logging.info("Puzzle 02 Part II - Red-Nosed Reports")
    # new_reports: list[list[int]] = load_reports()
    # good_reports = check_reports(new_reports, dampener_engaged=True)
    # logging.info(f"Number of good reports: {good_reports}")


def check_reports(reports: list[list[int]], dampener_engaged: bool = False) -> int:
    good_reports: int = 0
    for x, report in enumerate(reports):
        if check_report_safe(report, False, dampener_engaged):
            good_reports += 1
            logging.info(f"Good report ascending. tally: {good_reports}")
        else:
            report.reverse()
            if check_report_safe(report, True, dampener_engaged):
                good_reports += 1
                logging.info(f"Good report descending. tally: {good_reports}")
    return good_reports


# Need to refactor since it's no longer a binary condition because of phase II - one fault can be tolerated
# going to keep track of faults, and if that count is 0 or 1, then safe = True, else False
def check_report_safe(report: list[int], backwards: bool = False, dampener_engaged: bool = False) -> bool:
    safe: bool = False
    prev_value: int = 0
    bad_count: int = 0

    for x, value in enumerate(report):
        #  if not backwards:
        safe = True if prev_value == 0 or ((prev_value + 3 >= value > prev_value) and value != prev_value) else False
        # else:
            # safe = True if prev_value == 0 or ((prev_value - 3 <= value < prev_value) and value != prev_value) else False
        if not safe:
            bad_count += 1
        logging.info(f"{backwards} - {report}: value: {value} -- prev_value: {prev_value} dampener: {dampener_engaged} bad_count: {bad_count} --- Safe: {safe}")
        prev_value = value
        if not safe:
            if not dampener_engaged:
                break
    if dampener_engaged:
        return bad_count <= 1
    else:
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
