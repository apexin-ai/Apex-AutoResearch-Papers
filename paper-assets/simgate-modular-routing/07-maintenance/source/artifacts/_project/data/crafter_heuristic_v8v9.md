## Heuristic Agent v8→v9 Comparison

| Metric | Random | Heuristic v8 | Heuristic v9 |
|--------|--------|-------------|-------------|
| Avg steps | 151 | ~353 | 293 |
| Death rate | 100% | 100% | 100% |
| Avg achievements | 2.4 | N/A | 5.8 |

### v9 Death Cause: Sleep Starvation
- 92% of actions are movement (constant fleeing)
- Only 7 sleeps in 1466 total steps (0.5%)
- energy→0 with no recovery → health never regenerates
- ~1 zombie hit every 43 steps, cumulative damage → death

### v10 Priorities
1. Restore emergency sleep (radius 5-6 not 12)
2. Conditional flee (only when unarmed OR low HP OR multiple monsters)
3. Active monster clearing when armed + healthy
4. Tighter water-camp + food strategy