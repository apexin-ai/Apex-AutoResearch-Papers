# analyze eval pi05 random k09 spatial seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_k09_spatial_seed42_20260522T012651_result.json`
- **Structured JSON:** [`528fb464a23bdf8586ce.json`](../../sessions/52/528fb464a23bdf8586ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W&B query is having issues, but the log data is complete and sufficient. Here's the analysis:

---

## Experiment Result: `eval_pi05_random_k09_spatial_seed42`

### Configuration
- **Model**: π0.5 (4143.4M params)
- **Prune mode**: random, keep_ratio=0.9 (230/256 tokens per image, 690/768 total)
- **Suite**: libero_spatial, 10 tasks × 50 episodes
- **Runtime**: 115.1 min
- **Log**: `~/runs/importance_margin_vla_compress/eval_pi05_random_k09_spatial_seed42.log`
- **Results JSON**: `/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.90_libero_spatial_seed42.json`
- **Exit code**: 0 (clean, no errors)

### Overall SR: **54.6%** (273/500)

### Per-Task Breakdown

| Task | Description | SR |
|------|------------|-----|
| T0 | pick up the black bowl between the plate | 84.0% |
| T1 | pick up the black bowl next to the ramekin | 40.0% |
| T2 | pick up the black bowl from table center | 88.0% |
| T3 | pick up the black bowl on the cookie box | 12.0% |
| T4 | pick up the black bowl in the top drawer | 24.0% |
| T5 | pick up the black bowl on the ramekin and... | 52.0% |
| T6 | pick up the black bowl next to the cookie... | 62.0% |
| T7 | pick up the black bowl on the stove and... | 68.0% |
| T8 | pick up the black bowl next to the plate | 88.0% |
| T9 | pick up the black bowl on the wooden cab... | 28.0% |

### Hypothesis Verification

| Condition | SR | Drop from baseline |
|-----------|----|--------------------|
| **Spatial baseline** | 97.2% | — |
| **Spatial random k=0.9** | **54.6%** | **−42.6pp** (−43.8% relative) |
| **Object random k=0.9** | 10.8% | catastrophic cliff |

### Conclusion: **Cliff is Object-specific, not model-intrinsic**

Spatial random k=0.9 = 54.6%, far from the ~10% cliff seen on Object. The degradation pattern is qualitatively different:

- **Object k=0.9**: near-total collapse to 10.8% — a cliff
- **Spatial k=0.9**: substantial degradation to 54.6% — a steep slope, but NOT a cliff

Randomly pruning 10% of vision tokens hurts both suites, but only Object exhibits catastrophic failure. This means the V-dip cliff at k=0.9 is **Object-specific**, likely because Object tasks require precise spatial-visual discrimination where even small random token loss destroys critical information. Spatial tasks are more robust to random token removal — they degrade gracefully rather than falling off a cliff.

Task-level variance is notable: Spatial T2/T8 (88%) are barely affected while T3 (12%) and T4 (24%) are severely impacted, suggesting token importance is task-dependent even within a suite.

---
