def get_input():
    with open("input.txt") as f:
        grid = []
        for line in f:
            grid.append(line.strip('\n'))
            
        return grid