import nflreadpy as nfl

def import_team_data(seasons: list[int]):
    print(f"Fetching team stats from season(s): {seasons}")
    teams_data = nfl.load_team_stats(seasons)
    teams_data = teams_data.to_pandas()

    return teams_data