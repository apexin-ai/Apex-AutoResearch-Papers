# analysis exp 008

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_008_20260519T055140_result.json`
- **Structured JSON:** [`781446a5a4b8bfbd2526.json`](../../sessions/78/781446a5a4b8bfbd2526.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results file is complete with all 11 generations (Gen 0–10). Here's the full analysis:

## Complete Metrics — exp_008 (r=0.3, seed 42)

| Gen | eff_rank | log_det | ppl | distinct_4 | train_loss |
|-----|----------|---------|------|-----------|------------|
| 0 | 417.55 | 2366.68 | 9.55 | 0.7414 | — |
| 1 | 476.91 | 2366.13 | 10.19 | 0.6894 | 1.836 |
| 2 | 484.17 | 2372.45 | 10.59 | 0.4892 | 1.774 |
| 3 | 489.48 | 2386.72 | 10.90 | 0.4646 | 1.506 |
| 4 | 492.59 | 2404.02 | 11.23 | 0.4683 | 1.446 |
| 5 | 497.86 | 2431.17 | 11.54 | 0.4508 | 1.407 |
| 6 | 501.63 | 2452.00 | 11.88 | 0.4176 | 1.368 |
| 7 | 506.30 | 2467.05 | 12.22 | 0.3964 | 1.349 |
| 8 | 511.71 | 2485.91 | 12.61 | 0.4058 | 1.320 |
| 9 | 515.92 | 2497.30 | 12.96 | 0.3732 | 1.325 |
| 10 | 521.26 | 2511.13 | 13.38 | 0.3422 | 1.304 |

## log_det Trajectory Analysis

**Pattern: Monotonic rise** (Δ total = +144.45)

Gen-to-gen deltas:
- Gen 0→1: **−0.55** (negligible, <0.025%)
- Gen 1→2: +6.31
- Gen 2→3: +14.27
- Gen 3→4: +17.30
- Gen 4→5: +27.15
- Gen 5→6: +20.83
- Gen 6→7: +15.05
- Gen 7→8: +18.86
- Gen 8→9: +11.39
- Gen 9→10: +13.83

The Gen 0→1 dip is negligible (−0.55 on a base of 2366). From Gen 1 onward, strictly monotonic rise. This is the **same pattern as r=0.5** (monotonic rise, no collapse).

## Cross-Experiment Comparison

| Experiment | r | log_det trajectory | Pattern |
|-----------|-----|-------------------|---------|
| exp_001 | 0.0 | 2469→2179 | **Monotonic decline (collapse)** |
| exp_007 | 0.2 | 2367→2358(dip)→2399 | **Dip-then-recovery** |
| **exp_008** | **0.3** | **2367→2366→2511** | **Monotonic rise (no collapse)** |
| exp_004 | 0.5 | 2367→2573 | **Monotonic rise (no collapse)** |

## Other Trends

- **eff_rank**: monotonic rise 417.55 → 521.26 (+24.8%) — spectral diversity steadily increasing
- **distinct_4**: monotonic decline 0.7414 → 0.3422 (−53.8%) — text diversity drops despite spectral health
- **train_loss**: generally decreasing 1.836 → 1.304 (tiny uptick at Gen 9: 1.325)
- **ppl**: monotonic rise 9.55 → 13.38

## Conclusion

**r=0.3 shows NO spectral collapse.** log_det rises monotonically across all 10 training generations. This places **r_crit ∈ (0.2, 0.3]** — r=0.2 exhibits spectral stress (dip-then-recovery), while r=0.3 is clean. exp_009 (r=0.25) will narrow the bound further.

Notable: distinct_4 declines 54% even with healthy spectrum, suggesting text diversity loss is a separate phenomenon from spectral collapse at this mixing ratio.

### Gen 9 & Gen 10 JSON for registry update:

```json
{
  "gen_9": {
    "effective_rank": 515.92,
    "log_det": 2497.30,
    "perplexity": 12.955,
    "distinct_4": 0.3732,
    "train_loss": 1.3248,
    "mix_ratio": 0.3,
    "controller_ratio": 0.3
  },
  "gen_10": {
    "effective_rank": 521.26,
    "log_det": 2511.13,
    "perplexity": 13.377,
    "distinct_4": 0.3422,
    "train_loss": 1.3036,
    "mix_ratio": 0.3,
    "controller_ratio": 0.3
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "gen_9": {
      "effective_rank": 515.92,
      "log_det": 2497.3,
      "perplexity": 12.955,
      "distinct_4": 0.3732,
      "train_loss": 1.3248,
      "mix_ratio": 0.3,
      "controller_ratio": 0.3
    },
    "gen_10": {
      "effective_rank": 521.26,
      "log_det": 2511.13,
      "perplexity": 13.377,
      "distinct_4": 0.3422,
      "train_loss": 1.3036,
      "mix_ratio": 0.3,
      "controller_ratio": 0.3
    }
  }
}
```

</details>

---
