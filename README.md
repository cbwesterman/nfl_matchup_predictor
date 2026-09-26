# NFL Matchup Predictor

A machine learning project that predicts NFL game outcomes — both win probability and
a point estimate for each team's score — using team-level performance data pulled from
the nflverse project via `nflreadpy`. Built as a follow-up to my MLB hit predictor, aimed
at going deeper: richer data, more advanced modeling (including combining multiple models
together), and a fuller pipeline with proper experiment tracking.

**Status: early in progress.** Raw data ingestion and the core home/away merge are
working end-to-end. Feature engineering, modeling, and tracking haven't been started yet.

## Overview

The goal is to predict, for a given NFL matchup: which team wins (a probability) and
each team's expected score. Rather than relying on a single model, part of the plan is
to eventually combine multiple models' predictions together (an ensemble) for a more
robust final answer — though that's still well down the road.

## Approach

**Data source:** [nflreadpy](https://github.com/nflverse/nflreadpy), pulling:
- `load_team_stats()` — team-level box score stats (passing/rushing yards, turnovers,
  etc.), one row per team per game.
- `load_schedules()` — one row per game, with home/away teams, final scores, and rest days.

**Pipeline so far:**
1. `import_team_data.py` — pulls team stats for a given range of seasons.
2. `import_schedule_data.py` — pulls schedule data for the same season range.
3. `merge_data.py` — combines both sources into one row per game. Since `load_team_stats`
   returns two rows per game (one per team), the merge attaches each team's stats to the
   correct side of the matchup by merging twice: once matching a game's `home_team`,
   once matching `away_team`, with columns renamed `home_*`/`away_*` beforehand to avoid
   collisions.
4. `main.py` — owns the season range configuration and orchestrates the pipeline stages
   in order.

**Key design decisions:**
- **One row per game** is the final modeling unit (not one row per team), so the target
  and both teams' features live together on a single row.
- **Left join off schedule data**, not inner — future, not-yet-played games stay in the
  pipeline rather than getting dropped at merge time, deferring "is this row usable" to
  right before modeling (the same way my MLB project's `dropna(subset=model_features)`
  filtered late rather than early), and keeping the door open for eventually generating
  live predictions on upcoming games.
- **8-12 season lookback**, not the full ~25 years available, to balance training volume
  against staying within a reasonably consistent NFL rules/scoring era.
- **Home/away splits, opponent-specific history, and ensembling are deliberately
  deferred** until a simple v1 pipeline is working end-to-end — added complexity should
  be justified by evidence, not assumed upfront.

## Known issues / Next steps

- [ ] **Team abbreviation mismatch**: `load_schedules` uses each team's historical-era
      abbreviation, but `load_team_stats` uses current abbreviations even for old
      seasons — breaks merges for relocated/rebranded franchises (Rams, Chargers, etc.).
      Likely fix: `nflreadpy`'s built-in `team_abbr_mapping`/`team_abbr_mapping_norelocate`.
- [ ] Reshape team stats into leakage-free rolling features (trailing N-game averages
      per team, using `.shift(1)` before `.rolling()`)
- [ ] Build v1 feature set: points scored/allowed, passing yards, rushing yards,
      turnovers committed/forced
- [ ] Prep table for modeling
- [ ] Baseline win-probability and score-prediction models, checked against a naive
      baseline
- [ ] Explore combining multiple models (ensemble/stacking) for a final prediction
- [ ] Experiment tracking and backtesting across seasons
- [ ] Generate live predictions for an upcoming week's games

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install nflreadpy pandas pyarrow
python main.py