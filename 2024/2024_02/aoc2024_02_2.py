from aoc2024_02_utils import get_input

def check_safety(reports):
    number_of_safe_levels = 0
    for report in reports:
        for i in range(len(report)):
            report_copy = report[:i] + report[i + 1:]
            if report_copy == sorted(report_copy) or report_copy == sorted(report_copy, reverse=True):
                for i in range(0, len(report_copy) - 1):
                    if not 1 <= abs(report_copy[i] - report_copy[i + 1]) <= 3:
                        break
                else:
                    number_of_safe_levels += 1
                    break
            
    return number_of_safe_levels


def main():
    reports = get_input()
    number_of_safe_levels = check_safety(reports)
    print(number_of_safe_levels)


if __name__ == "__main__":
    main()
