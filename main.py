# Libraries
import pandas as pd

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

    # Test Prints:
    df = pd.read_csv("data/processed/ultimate_df.csv", low_memory=False)

    # See which home_ columns exist, so you can pick a stats one
    print([c for c in df.columns if c.startswith("home_")][:40])
    stat_col = "home_passing_yards"   # replace with a real name from the list above

    missing = df[df[stat_col].isna()].groupby(["season", "home_team"]).size()
    print(missing)
    print(df.groupby("season")[stat_col].apply(lambda s: s.isna().sum()))

if __name__ == "__main__":
    main()