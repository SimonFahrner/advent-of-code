from aoc2024_02_utils import get_input, is_monotonical, is_slow_changing

def check_safety(reports):
    number_of_safe_levels = 0
    for report in reports:
        for i in range(len(report)):
            report_copy = report[:i] + report[i + 1:]
            if (is_monotonical(report_copy) and is_slow_changing(report_copy)):
                number_of_safe_levels += 1
                break
            
    return number_of_safe_levels


def main():
    reports = get_input()
    number_of_safe_levels = check_safety(reports)
    print(number_of_safe_levels)


if __name__ == "__main__":
    main()
