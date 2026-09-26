import pandas as pd

def merge_data(teams_df, schedule_df):
    key_columns = ["season", "week", "team", "season_type", "game_id", "opponent_team"]

    rename_map = {}
    for col in teams_df.columns:
        if col not in key_columns:
            rename_map[col] = f"home_{col}"

    home_stats = teams_df.rename(columns=rename_map)
    home_stats = home_stats[["game_id", "team"] + list(rename_map.values())]

    rename_map = {}
    for col in teams_df.columns:
        if col not in key_columns:
            rename_map[col] = f"away_{col}"
    
    away_stats = teams_df.rename(columns=rename_map)
    away_stats = away_stats[["game_id", "team"] + list(rename_map.values())]

    ultimate_df = schedule_df.merge(
        home_stats,
        left_on=["game_id", "home_team"],
        right_on=["game_id", "team"],
        how="left"
    )

    ultimate_df = ultimate_df.merge(
        away_stats,
        left_on=["game_id", "away_team"],
        right_on=["game_id", "team"],
        how="left"
    )

    return ultimate_df