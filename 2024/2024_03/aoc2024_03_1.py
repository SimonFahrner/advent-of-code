import re
from aoc2024_03_utils import calculate_match, get_input

def main():
    pattern = r"mul\(\d+,\d+\)"
    result = sum(calculate_match(mult) for mult in re.findall(pattern, get_input()))
    print(result)

if __name__ == "__main__":
    main()