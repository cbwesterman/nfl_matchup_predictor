import nflreadpy as nfl

def import_schedule_data(seasons: list[int]):
    print(f"Fetching team schedules from season(s): {seasons}")
    schedule_data = nfl.load_schedules(seasons)
    schedule_data = schedule_data.to_pandas()

    return schedule_data