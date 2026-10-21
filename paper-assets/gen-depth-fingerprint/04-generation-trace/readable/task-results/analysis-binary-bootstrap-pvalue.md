# analysis binary bootstrap pvalue

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_binary-bootstrap-pvalue_20260515T141519_result.json`
- **Structured JSON:** [`f07018c5c08fdd3f9092.json`](../../sessions/f0/f07018c5c08fdd3f9092.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 5 comparisons complete. Results:

## Binary F1 Paired Bootstrap Significance Test Results

| Comparison | Delta F1 | p-value | 95% CI | Sig |
|---|---|---|---|---|
| 7-feat vs Avg-LogProb | +0.0109 | < 0.0001 | [+0.0061, +0.0157] | *** |
| 7-feat vs LD-Score | +0.0224 | < 0.0001 | [+0.0167, +0.0281] | *** |
| 7-feat vs FastDetectGPT | +0.1079 | < 0.0001 | [+0.1005, +0.1151] | *** |
| 7-feat vs Binoculars | +0.1994 | < 0.0001 | [+0.1918, +0.2068] | *** |
| 7-feat vs 4-det ensemble | +0.0116 | < 0.0001 | [+0.0065, +0.0167] | *** |

**All 5 comparisons are significant at p < 0.0001** (0 out of 10,000 bootstrap samples had delta ≤ 0).

### Key findings:
- The **p < 0.001 claim holds** for all binary comparisons, including the tightest ones (vs Avg-LogProb at +1.1pp and vs 4-det ensemble at +1.2pp).
- Even the smallest gap — 7-feat vs Avg-LogProb (delta = +0.0109, CI: [+0.0061, +0.0157]) — has the CI entirely above zero.
- The 7-feat vs 4-det ensemble gap (delta = +0.0116, CI: [+0.0065, +0.0167]) is also clearly significant.
- **No claim downgrade needed.** The binary-specific p-values independently confirm p < 0.001.

### JSON output

```json
{
  "7feat_vs_avglogprob": {"delta": 0.0109, "p_value": 0.0, "ci95": [0.0061, 0.0157]},
  "7feat_vs_ldscore": {"delta": 0.0224, "p_value": 0.0, "ci95": [0.0167, 0.0281]},
  "7feat_vs_fastdetectgpt": {"delta": 0.1079, "p_value": 0.0, "ci95": [0.1005, 0.1151]},
  "7feat_vs_binoculars": {"delta": 0.1994, "p_value": 0.0, "ci95": [0.1918, 0.2068]},
  "7feat_vs_4det_ensemble": {"delta": 0.0116, "p_value": 0.0, "ci95": [0.0065, 0.0167]}
}
```

Method: stratified paired bootstrap (n=10,000), resampling within each generator independently, computing per-generator macro F1 and averaging — matching the LOGO evaluation protocol. Saved to `results/binary_bootstrap_pvalue.json` on autodl-5090.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "7feat_vs_avglogprob": {
      "delta": 0.0109,
      "p_value": 0.0,
      "ci95": [
        0.0061,
        0.0157
      ]
    },
    "7feat_vs_ldscore": {
      "delta": 0.0224,
      "p_value": 0.0,
      "ci95": [
        0.0167,
        0.0281
      ]
    },
    "7feat_vs_fastdetectgpt": {
      "delta": 0.1079,
      "p_value": 0.0,
      "ci95": [
        0.1005,
        0.1151
      ]
    },
    "7feat_vs_binoculars": {
      "delta": 0.1994,
      "p_value": 0.0,
      "ci95": [
        0.1918,
        0.2068
      ]
    },
    "7feat_vs_4det_ensemble": {
      "delta": 0.0116,
      "p_value": 0.0,
      "ci95": [
        0.0065,
        0.0167
      ]
    }
  }
}
```

</details>

---
