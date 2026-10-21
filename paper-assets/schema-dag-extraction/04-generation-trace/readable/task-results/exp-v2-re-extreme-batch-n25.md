# exp v2 re extreme batch n25

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_v2-re-extreme-batch-n25_20260516T051154_result.json`
- **Structured JSON:** [`fc0b5fda99ae25559fdb.json`](../../sessions/fc/fc0b5fda99ae25559fdb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment complete and artifact registered. Here are the results:

## FewRel v2 RE Extreme-Batch n=25 Results

| Metric | Value |
|--------|-------|
| **n_low / n_high** | 25 / 25 |
| **Low BCS mean acc** | 0.8521 |
| **High BCS mean acc** | 0.5967 |
| **Delta (low − high)** | **+25.54 pp** |
| **95% Bootstrap CI** | **[+22.42, +28.62] pp** |
| **Permutation p-value** | **0.0000** |
| **Pearson r (BCS vs acc)** | **−0.919** (p ≈ 0) |
| Low BCS range | [0.356, 0.367] |
| High BCS range | [0.791, 0.811] |

**CONFIRMED**: CI entirely above zero. The BCS → accuracy effect is massive and highly significant under the v2 anti-hallucination prompt.

Comparison with n=5 run:
- n=5: delta=+7.9pp, CI=[−5.2, +21.5] — CI crossed zero, inconclusive
- n=25: delta=+25.5pp, CI=[+22.4, +28.6] — CI excludes zero decisively

The larger effect size (25.5 vs 7.9 pp) is due to the wider BCS separation achieved by stochastic greedy batch generation (BCS gap 0.44 vs 0.21 in n=5).

Output files on server: `/root/schema-dag-extraction/artifacts/exp_v2_re_n25/`

---
