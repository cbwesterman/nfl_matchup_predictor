import nflreadpy as nfl
from team_names import TEAM_ABBR_FIX, fix_game_id


def import_schedule_data(seasons: list[int]):
    print(f"Fetching team schedules from season(s): {seasons}")
    schedule_data = nfl.load_schedules(seasons)
    schedule_data = schedule_data.to_pandas()

    schedule_data["home_team"] = schedule_data["home_team"].replace(TEAM_ABBR_FIX)
    schedule_data["away_team"] = schedule_data["away_team"].replace(TEAM_ABBR_FIX)
    schedule_data["game_id"] = schedule_data["game_id"].apply(fix_game_id)

    return schedule_data