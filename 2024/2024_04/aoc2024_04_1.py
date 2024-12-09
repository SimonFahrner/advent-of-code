from aoc2024_04_utils import get_input

def search_for_all_xmas(grid):
    number_of_rows = len(grid)
    number_of_columns = len(grid[0])
    number_of_xmas = 0


    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def in_bounds(x,y):
        return 0<=x<=number_of_rows-1 and 0<=y<=number_of_columns-1

    for row in range(number_of_rows):
        for column in range(number_of_columns):
            if grid[row][column] == 'X':
                for direction in directions:
                    if in_bounds(row + direction[0], column + direction[1]):
                        if grid[row + direction[0]][column + direction[1]] == 'M':
                            if in_bounds(row + 2 * direction[0], column + 2 * direction[1]):
                                if grid[row + 2 * direction[0]][column + 2 * direction[1]] == 'A':
                                    if in_bounds(row + 3 * direction[0], column + 3 *direction[1]):
                                        if grid[row + 3 * direction[0]][column + 3 * direction[1]] == 'S':
                                            number_of_xmas += 1

    return number_of_xmas

def main():
    grid = get_input()
    number_of_xmas = search_for_all_xmas(grid)

    print(number_of_xmas)

if __name__ == "__main__":
    main()