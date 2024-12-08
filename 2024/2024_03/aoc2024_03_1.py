from aoc2024_03_utils import get_input
import re

def main():
    pattern = r"mul\(\d+,\d+\)"
    input_data = get_input()

    result = 0

    for line in input_data:
        mults = re.findall(pattern, line)

        for mult in mults:
            # extract the numbers by stripping the mul() and , then multiply the numbers
            num1, num2 = map(int, re.findall(r"\d+", mult))
            result += num1 * num2
    print(result)

if __name__ == "__main__":
    main()