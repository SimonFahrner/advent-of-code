from aoc2024_03_utils import calculate_match, get_input
import re

def is_do(match):
    return match.group(4)

def is_dont(match):
    return match.group(5)

def is_mul(match):
    return match.group(1)

def main():
    pattern = r"(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))"
    do = True
    result = 0

    for match in re.finditer(pattern, get_input()):
        if is_do(match):
            do = True
        elif is_dont(match):
            do = False
        elif is_mul(match) and do:
            result += calculate_match(match.group(1))

    print(result)

if __name__ == "__main__":
    main()