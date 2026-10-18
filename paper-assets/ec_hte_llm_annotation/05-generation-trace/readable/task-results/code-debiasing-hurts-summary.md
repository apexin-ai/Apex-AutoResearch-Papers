# code debiasing hurts summary

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_debiasing-hurts-summary_20260523T145836_result.json`
- **Structured JSON:** [`6ee77aed9032902d4338.json`](../../sessions/6e/6ee77aed9032902d4338.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Results

**Grand Total: Across 2,132 subgroup-configuration pairs, global correction increases |bias| in 26.5% of cases; in 15.2% the increase exceeds 2×.**

### Per-source breakdown:

| Data Source | N | Hurts (%) | Severely Hurts (%) | Worst Ratio |
|---|---|---|---|---|
| **Synthetic (exp002 grid)** | 2,080 | 520 (25.0%) | 320 (15.4%) | 7.14× |
| **Synthetic (extreme examples)** | 12 | 4 (33.3%) | 4 (33.3%) | 2.86× |
| **Real LLM (MC validation)** | 39 | 39 (100%) | 0 (0%) | 1.45× |
| **F-L comparison** | 1 | 1 (100%) | 0 (0%) | 1.04× |

Key findings:
- **Synthetic data**: 1 in 4 subgroup-config pairs is hurt by global correction; the worst case inflates bias by 7×
- **Real LLM data**: global correction hurts in **100% of 39 LLM×dataset×n_expert configurations** (mean ratio 1.20×) — no severe cases, but universally worse than naive
- The `exp_realcm_bias_identity.csv` was skipped for this analysis because it only contains predicted/observed bias of the global corrected estimator without a naive baseline for direct comparison

Outputs:
- `artifacts/debiasing_hurts_summary.pdf` + `.png`
- `artifacts/debiasing_hurts_summary.csv`

---
