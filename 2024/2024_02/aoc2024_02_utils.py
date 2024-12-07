def get_input():

    with open("input.txt") as f:
        reports = []
        for line in f:
            report = list(int(level) for level in line.strip().split())
            reports.append(report)

    return reports