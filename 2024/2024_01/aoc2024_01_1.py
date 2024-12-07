from aoc2024_01_utils import get_input

def calculate_distance(team1_location_ids, team2_location_ids):
    distance = 0
    for i in range(len(team1_location_ids)):
        distance += abs(team1_location_ids[i] - team2_location_ids[i])

    return distance

def main():
    team1_location_ids, team2_location_ids = get_input()
    team1_location_ids.sort()
    team2_location_ids.sort()
    
    list_distance = calculate_distance(team1_location_ids, team2_location_ids)

    print(list_distance)

if __name__ == "__main__":
    main()