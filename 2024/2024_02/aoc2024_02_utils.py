def get_input():

    with open("input.txt") as f:
        reports = []
        for line in f:
            report = list(int(level) for level in line.strip().split())
            reports.append(report)

    return reports

def is_monotonical(report):
    return report == sorted(report) or report == sorted(report, reverse=True)

def is_slow_changing(report):
    return all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))