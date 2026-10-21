# d066 SciERC Beam Sweep — Final Summary

**Dataset**: SciERC test (551 samples)  
**Model**: Qwen (schema-constrained IE)  
**Server**: westd-21461  
**Configs**: k ∈ {1, 2, 4, 8} × {unconstrained (unc), constrained (con)}

## Full Results Table

| k | Mode | E-P | E-R | E-F1 | R-P | R-R | R-F1 | DR% | CF% | Avg Time (s) | Speedup vs k=8 con |
|---|------|------|------|------|------|------|------|------|------|------|------|
| 1 | unc | 65.01 | 68.86 | **66.88** | 39.82 | 46.61 | 42.95 | 2.11 | 0.0 | 2.494 | 2.03× |
| 1 | con | 65.01 | 68.86 | **66.88** | 39.82 | 46.61 | 42.95 | 0.0 | 0.5 | 2.932 | 1.73× |
| 2 | unc | 66.04 | 69.64 | **67.79** | 41.05 | 49.18 | **44.75** | 1.54 | 0.0 | 2.954 | 1.71× |
| 2 | con | 65.95 | 69.58 | 67.71 | 40.94 | 48.97 | 44.60 | 0.0 | 0.11 | 3.463 | 1.46× |
| 4 | unc | 65.06 | 70.11 | 67.49 | 38.60 | 50.41 | 43.72 | 1.89 | 0.0 | 3.485 | 1.45× |
| 4 | con | 64.82 | 69.81 | 67.22 | 38.53 | 50.21 | 43.60 | **0.0** | **0.0** | 4.069 | 1.24× |
| 8 | unc | 63.75 | 69.28 | 66.40 | 37.81 | 50.31 | 43.17 | 1.77 | 0.0 | 4.194 | 1.21× |
| 8 | con | 63.73 | 69.22 | 66.36 | 38.25 | 50.82 | 43.65 | **0.0** | **0.0** | 5.058 | 1.00× |

**Note**: beam8 con metrics (E-F1, R-F1) extracted from violation report (no eval_beam8_con.json).

## Key Observations

### 1. k=2 is the sweet spot for F1
- **k=2 unc** achieves the best R-F1 (44.75) and E-F1 (67.79) across all configs.
- Beyond k=2, precision drops faster than recall gains → F1 degrades.
- k=8 recall is highest (R-R=50.31–50.82) but precision penalty is severe (R-P drops to ~37.8–38.3).

### 2. Constrained decoding eliminates DR violations at near-zero F1 cost
- DR violations drop from 1.5–2.1% → 0.0% across all k values.
- F1 impact of constraints:
  - k=1: **zero** (identical outputs — greedy decoding has only one beam to select)
  - k=2: E-F1 −0.08, R-F1 −0.15
  - k=4: E-F1 −0.27, R-F1 −0.12
  - k=8: E-F1 −0.04, R-F1 **+0.48** (constraint re-ranking actually improves R-F1)

### 3. CF violations are rare and only appear in constrained mode at low k
- k=1 con: CF=0.5% (9 violations)
- k=2 con: CF=0.11% (2 violations)
- k≥4 con: CF=0.0%
- Likely: constrained filtering of DR-violating triples occasionally shifts output to CF-violating alternatives. At higher k, more beams → better alternatives available.

### 4. Time overhead scales with k
| k | unc→con overhead | k=1 unc→k overhead (unc) |
|---|-----------------|--------------------------|
| 1 | +17.6% | baseline |
| 2 | +17.2% | +18.4% |
| 4 | +16.8% | +39.7% |
| 8 | +20.6% | +68.2% |

Constraint overhead is consistent (~17–21%). Beam width overhead grows sublinearly.

## Pareto Analysis

### Pareto-optimal configurations (R-F1 vs. violation rate)

1. **k=2 unc** — Best raw R-F1 (44.75), DR=1.54%. Best if violations are tolerable.
2. **k=2 con** — R-F1=44.60 (−0.15 from best), DR=0.0%, CF=0.11%. Best cost/benefit tradeoff.
3. **k=4 con** — Zero violations on all axes (DR=0%, CF=0%), R-F1=43.60. Best if strict compliance required.

### Dominated configurations
- k=1 (any): lower F1 than k=2 with no compensating advantage.
- k=8 (any): lower E-F1 than k=2, similar R-F1 to k=4, 40–70% slower.
- k=4 unc: strictly dominated by k=2 unc (lower F1, similar violations).
- k=8 unc: strictly dominated by k=4 con (similar F1 but non-zero violations).

### Recommendation

**k=2 constrained** is the recommended default:
- R-F1 within 0.15 pts of the absolute best (44.60 vs 44.75)
- Eliminates domain-range violations entirely (0.0%)
- Residual CF violations negligible (0.11%, 2 out of 1798 triples)
- Only 39% slower than k=1 unc baseline
- 46% faster than k=8 con

If absolute zero violations are required, **k=4 con** achieves 0%/0% at the cost of −1.15 R-F1 and 1.17× more time vs k=2 con.

## Missing Data
- `eval_beam8_con.json` does not exist. Beam8 con metrics were recovered from:
  - `qwen_scierc_beam8_full_s1_violations.json` → E-F1, R-F1, DR%, CF%
  - `qwen_scierc_beam8_full_s1.jsonl` → avg inference time (computed from per-sample `inference_time_seconds`)
- `d066_summary.json` is empty (`total_configs: 0`), not used.
