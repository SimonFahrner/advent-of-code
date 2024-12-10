from aoc2024_02_utils import get_input, is_monotonical, is_slow_changing


def count_safe(reports):
    return sum(1 for report in reports if is_monotonical(report) and is_slow_changing(report))

def main():
    reports = get_input()
    print(count_safe(reports))


if __name__ == "__main__":
    main()
