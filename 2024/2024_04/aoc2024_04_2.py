from aoc2024_04_utils import get_input

def search_for_all_xmas(grid):
    number_of_rows = len(grid)
    number_of_columns = len(grid[0])
    number_of_xmas = 0

    def in_bounds(x,y):
        return 0<=x<=number_of_rows-1 and 0<=y<=number_of_columns-1

    for row in range(number_of_rows):
        for column in range(number_of_columns):
            if grid[row][column] == 'A':
                if in_bounds(row - 1, column - 1) and in_bounds(row + 1, column + 1)and in_bounds(row - 1, column + 1) and in_bounds(row + 1, column - 1):
                    if (grid[row - 1][column - 1] == 'M' and grid[row + 1][column + 1] == 'S' or grid[row -1][column -1] == 'S' and grid[row +1][column + 1] == 'M' ) and (grid[row - 1][column + 1] == 'M' and grid[row + 1][column - 1] == 'S' or grid[row -1][column + 1] == 'S' and grid[row + 1][column - 1] == 'M' ):
                        number_of_xmas += 1

    return number_of_xmas

def main():
    grid = get_input()
    number_of_xmas = search_for_all_xmas(grid)

    print(number_of_xmas)

if __name__ == "__main__":
    main()