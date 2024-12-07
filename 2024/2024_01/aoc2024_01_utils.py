def get_input():
    with open("input.txt") as file:
        team1_location_ids, team2_location_ids = [], []
        for line in file:
            values = line.strip().split()
            team1_location_ids.append(int(values[0]))
            team2_location_ids.append(int(values[1]))

    return team1_location_ids, team2_location_ids