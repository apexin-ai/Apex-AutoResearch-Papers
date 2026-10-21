# Crafter Heuristic Agent v10 — Final Results

## Best Version: v10.4 (sapling farming)

### 5-Episode Comparison (seed=42)
| Agent | Avg Steps | Avg Achievements | Death Rate |
|-------|-----------|-----------------|------------|
| Heuristic v10 | **377** | **8.4** | 100% |
| Random | 151 | 2.4 | 100% |
| Ratio | **2.5x** | **3.5x** | same |

### 20-Episode Test (seed=100)
| Metric | v10 | v9 |
|--------|-----|-----|
| Avg steps | **328** | 286 |
| Avg achievements | **7.2** | 5.8 |
| Max steps | 772 | 760 |

### Death Causes
- ~60% monster cluster damage (-7hp single step from 3+ mobs)
- ~40% starvation (food=0, slow health decay)

### Iteration History
| Version | Change | Avg Steps | Result |
|---------|--------|-----------|--------|
| v10 | emergency sleep + conditional flee + clear mobs | 286 | baseline |
| v10.4 | + sapling farming | **326** | **best** |
| v10.6 | + aggressive hunting | 218 | worse |
| v10.7 | + danger-aware movement | 225 | worse |

### Implication for Crafter Pilot
100% death rate for BOTH agents means no death rate asymmetry.
Options: (1) use survival-time as signal, (2) max_steps cutoff, (3) shelter/armor strategy, (4) trained RL agent