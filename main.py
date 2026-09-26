# .py files
from import_team_data import import_team_data
from import_schedule_data import import_schedule_data
from merge_data import merge_data

def main():
    START_SEASON = 2015
    END_SEASON = 2026 # Include current season
    season_span = list(range(START_SEASON, END_SEASON + 1))

    teams_df = import_team_data(season_span)
    teams_df.to_csv("data/raw/teams_data.csv", index=False)
    schedule_df = import_schedule_data(season_span)
    schedule_df.to_csv("data/raw/schedule_data.csv", index=False)

    ultimate_df = merge_data(teams_df, schedule_df)
    ultimate_df.to_csv("data/processed/ultimate_df.csv", index=False)

if __name__ == "__main__":
    main()