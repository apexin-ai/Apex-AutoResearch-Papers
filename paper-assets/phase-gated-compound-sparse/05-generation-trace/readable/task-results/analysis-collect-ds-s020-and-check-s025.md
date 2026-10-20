# analysis collect ds s020 and check s025

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_collect_ds_s020_and_check_s025_20260515T211751_result.json`
- **Structured JSON:** [`d1837071a9aa5c1de833.json`](../../sessions/d1/d1837071a9aa5c1de833.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Both experiments DONE.

## Summary

### DS s020 (v2 rescored)
| Metric | Value |
|--------|-------|
| Accuracy | **0.26** (13/50) |
| Delta vs dense | **-0.26** |
| Truncated (2048) | 32/50 (64%) |
| Extraction failure | 31/50 (62%) |

### DS s025 (v2 rescored)
| Metric | Value |
|--------|-------|
| Accuracy | **0.08** (4/50) |
| Delta vs dense | **-0.44** |
| Truncated (2048) | 38/50 (76%) |
| Extraction failure | 37/50 (74%) |

Rescore produced **0 changes** — the v2 radical+degree matcher didn't flip any DS results.

### Complete Dose-Response Table (MATH-500 n=50, importance pruning)

| Sparsity | DS Acc | DS Delta | QW Acc | QW Delta |
|----------|--------|----------|--------|----------|
| dense | 0.52 | — | 0.32 | — |
| s015 | 0.36 | -0.16 | 0.34 | +0.02 |
| s020 | **0.26** | **-0.26** | 0.26 | -0.06 |
| s025 | **0.08** | **-0.44** | 0.32 | 0.00 |
| s030 | 0.10 | -0.42 | 0.14 | -0.18 |

DS shows steep monotonic degradation from s015→s025, with massive truncation driving extraction failures. QW is far more robust — flat through s025, only crashing at s030. The DS s025→s030 reversal (0.08→0.10) is noise within the truncation-dominated regime.

---
