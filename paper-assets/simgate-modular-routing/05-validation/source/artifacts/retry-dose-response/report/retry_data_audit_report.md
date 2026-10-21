# Retry Per-Trial Data Audit Report

## Summary: Data confirmed clean. No bugs, no anomalies.

## Per-Trial DR (retry, death-prone 200 eps)
- Trial 0: 93/200 = 46.5%
- Trial 1: 93/185 = 50.3% (denominator = non-early-success episodes)
- Trial 2: 90/184 = 48.9%

## Cumulative DR(N)
- DR(1): 93/200 = 46.5%
- DR(2): 89/200 = 44.5%
- DR(3): 83/200 = 41.5%

## Rescue Rates
- Retry: 1→2: 4.3%, 2→3: 6.7% (low, flat)
- Reflexion: 1→2: 26.1%, 2→3: 21.9% (high, confirms reflection works)

## DR Definition Discrepancy
- Table 4 "Retry (3×): DR = 40.9%" = final_is_death / 220 episodes (all tasks)
- Dose-response DR(3) = 41.5% = all-3-death / 200 episodes (death-prone only)
- 7 episodes differ: had score=0 (non-death) intermediate trial but final trial = death

## Seed/Config
- random.seed(42) set once at main(), no per-trial seed
- LLM randomness from temperature=0.3 (vLLM server-side)
- ScienceWorld env fully reset each trial (new JVM)

## Data Source
- All data from single session (~2.5h window, 2026-05-17 22:01 to 2026-05-18 00:33)
- Same vLLM server throughout