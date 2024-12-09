from aoc2024_03_utils import get_input
import re

def main():
    pattern = r"(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))"
    input_data = get_input()

    do = True
    result = 0

    for line in input_data:
        for match in re.finditer(pattern, line):
            if match.group(4):  # do()
                do = True
            elif match.group(5):  # don't()
                do = False
            elif match.group(1):  # mul()
                if do:
                    num1, num2 = map(int, re.findall(r"\d+", match.group(1)))
                    result += num1 * num2

    print(result)

if __name__ == "__main__":
    main()