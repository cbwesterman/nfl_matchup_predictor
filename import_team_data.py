import nflreadpy as nfl
from team_names import TEAM_ABBR_FIX, fix_game_id

def import_team_data(seasons: list[int]):
    print(f"Fetching team stats from season(s): {seasons}")
    teams_data = nfl.load_team_stats(seasons)
    teams_data = teams_data.to_pandas()

    teams_data["game_id"] = teams_data["game_id"].apply(fix_game_id)

    return teams_data