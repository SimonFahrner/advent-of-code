from aoc2024_02_utils import get_input

def check_safety(reports):
    number_of_safe_levels = 0
    for report in reports:
        if report == sorted(report) or report == sorted(report, reverse=True):
            for i in range(0, len(report) - 1):
                if not 1 <= abs(report[i] - report[i + 1]) <= 3:
                    break
            else:
                number_of_safe_levels += 1
            
    return number_of_safe_levels


def main():
    reports = get_input()
    number_of_safe_levels = check_safety(reports)
    print(number_of_safe_levels)


if __name__ == "__main__":
    main()
