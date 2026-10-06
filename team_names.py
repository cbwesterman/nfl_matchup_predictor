TEAM_ABBR_FIX = {
    "STL": "LA",
    "SD": "LAC",
    "OAK": "LV",
}

def fix_game_id(game_id: str) -> str:
    parts = game_id.split("_")
    parts[2] = TEAM_ABBR_FIX.get(parts[2], parts[2])
    parts[3] = TEAM_ABBR_FIX.get(parts[3], parts[3])
    return "_".join(parts)