from aoc2024_01_utils import get_input

def calculate_simularity_score(team1_location_ids, team2_location_ids):
    simularity = 0
    for location_id  in team1_location_ids:
        simularity += location_id * team2_location_ids.count(location_id)

    return simularity

def main():
    team1_location_ids, team2_location_ids = get_input()
    
    list_simularity = calculate_simularity_score(team1_location_ids, team2_location_ids)

    print(list_simularity)


if __name__ == "__main__":
    main()