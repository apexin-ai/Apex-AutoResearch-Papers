# a050_fp32 3-Seed Metrics Summary

**Date**: 2026-05-19
**Server**: westd-17855
**Base path**: `/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/`

---

## Part 1: cuda:2 Orphan Process Cleanup

GPU 2 on westd-17855 was already clean at time of check (0 MiB, 0% util). No orphan process found.

Current GPU state:
| GPU | Memory Usage | Process |
|-----|-------------|---------|
| 0 | 14503 MiB / 97887 MiB | python (PID 109870) |
| 1 | 34801 MiB / 97887 MiB | python (PID 74460) |
| 2 | 0 MiB / 97887 MiB | (none) |
| 3 | 0 MiB / 97887 MiB | (none) |
| 4 | 0 MiB / 97887 MiB | (none) |
| 5 | 0 MiB / 97887 MiB | (none) |

---

## Part 2: all_metrics.json Status

| Experiment | Generations | all_metrics.json |
|-----------|------------|-----------------|
| a050_s42_fp32 | 11 (gen_0 to gen_10) | present |
| a050_s43_fp32 | 11 (gen_0 to gen_10) | present |
| a050_s44_fp32 | 11 (gen_0 to gen_10) | present |

All three seeds already had `all_metrics.json` aggregated. No re-aggregation needed.

---

## Part 3: gen_0 vs gen_10 Drift Summary

### Key Metrics at gen_0 and gen_10

| Metric | Seed | gen_0 | gen_10 | Delta | Delta % |
|--------|------|-------|--------|-------|---------|
| **token_entropy** | s42 | 3.234 | 2.707 | -0.527 | -16.3% |
| | s43 | 3.234 | 2.723 | -0.512 | -15.8% |
| | s44 | 3.234 | 2.697 | -0.537 | -16.6% |
| **distinct_1** | s42 | 0.0916 | 0.0649 | -0.0267 | -29.2% |
| | s43 | 0.0929 | 0.0660 | -0.0269 | -29.0% |
| | s44 | 0.0915 | 0.0660 | -0.0256 | -27.9% |
| **distinct_2** | s42 | 0.5038 | 0.3159 | -0.1879 | -37.3% |
| | s43 | 0.5074 | 0.3235 | -0.1840 | -36.3% |
| | s44 | 0.4997 | 0.3266 | -0.1731 | -34.6% |
| **distinct_3** | s42 | 0.8318 | 0.5583 | -0.2735 | -32.9% |
| | s43 | 0.8350 | 0.5647 | -0.2704 | -32.4% |
| | s44 | 0.8286 | 0.5751 | -0.2535 | -30.6% |
| **ece** | s42 | 0.0108 | 0.0868 | +0.0760 | +703% |
| | s43 | 0.0108 | 0.0842 | +0.0734 | +679% |
| | s44 | 0.0108 | 0.0874 | +0.0766 | +709% |
| **perplexity** | s42 | 26.949 | 31.462 | +4.513 | +16.7% |
| | s43 | 26.949 | 31.576 | +4.627 | +17.2% |
| | s44 | 26.949 | 31.424 | +4.475 | +16.6% |

### Cross-Seed Consistency

| Metric | mean(Delta %) | std(Delta %) |
|--------|--------------|-------------|
| token_entropy | -16.2% | 0.3% |
| distinct_1 | -28.7% | 0.6% |
| distinct_2 | -36.1% | 1.1% |
| distinct_3 | -32.0% | 1.0% |
| ece | +697% | 12.9% |
| perplexity | +16.8% | 0.3% |

All metrics show consistent drift across 3 seeds with very low cross-seed variance, confirming reproducibility at alpha=0.50.
