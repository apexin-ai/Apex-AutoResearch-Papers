## Crafter Random Agent Demo Results

Seed=42, 5 episodes, determinism patch applied, PYTHONHASHSEED=0

| Episode | Steps | Reward | Death | Achievements |
|---------|-------|--------|-------|-------------|
| 0 | 180 | 3.10 | Yes | collect_sapling, collect_wood, place_plant, place_table, wake_up |
| 1 | 40 | -0.90 | Yes | (none) |
| 2 | 135 | 2.10 | Yes | collect_sapling, place_plant, wake_up |
| 3 | 254 | 2.10 | Yes | collect_sapling, place_plant, wake_up |
| 4 | 148 | 0.10 | Yes | wake_up |

**Determinism verification**: PASSED (two runs with same seed produce identical JSON output)

**Critical requirement**: Must set `PYTHONHASHSEED=0` because `crafter.Env.reset()` uses `hash((seed, episode))` for per-episode seed derivation, and Python 3 `hash()` is randomized by default.