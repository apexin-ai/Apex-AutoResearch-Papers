# fix tost cls traj

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_tost-cls-traj_20260519T065959_result.json`
- **Structured JSON:** [`5e395d4bfd5d1aceeb72.json`](../../sessions/5e/5e395d4bfd5d1aceeb72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Results Summary

### Per-test level comparison (CLS per-test vs TRAJ per-test, 3 paired seeds)

| Margin | p-value | Equivalent? |
|--------|---------|-------------|
| ±0.5pp | 0.9960  | NO          |
| **±1.0pp** | **0.9904** | **NO** |
| ±1.5pp | 0.9550  | NO          |
| **±2.0pp** | **0.2302** | **NO** |
| ±2.5pp | 0.0195  | YES         |
| ±3.0pp | 0.0062  | YES         |
| ±3.5pp | 0.0030  | YES         |
| ±4.0pp | 0.0017  | YES         |
| ±4.5pp | 0.0011  | YES         |
| ±5.0pp | 0.0008  | YES         |

**Minimum equivalence margin: ±2.25pp**

### Key findings

**Mean CLS-TRAJ gap = +1.89pp** (CLS is BETTER, not equivalent at ±2pp). This directly contradicts the paper's claim of -0.45pp gap and p=0.007.

### Comparison with old (incorrect) numbers

| Metric | Old (CLS-CWM mislabeled) | New (CLS-TRAJ correct) |
|--------|--------------------------|------------------------|
| Mean diff | 1.24pp | **1.89pp** |
| p at ±2pp | 0.007 (equiv) | **0.230 (NOT equiv)** |
| p at ±1pp | 0.871 | 0.990 |
| Min margin | ±1.63pp | **±2.25pp** |

### Data limitations

- Only 3 paired seeds available (0, 42, 789) out of the claimed 5, df=2
- TRAJ per-instance predictions not available for Qwen3-4B (checkpoints were on a different server)
- CLS variant-level accuracy (~91%) is much higher than TRAJ per-test (~86%), so the variant-level gap is even larger (~5.3pp)

The paper's §Equivalence claim of CLS-TRAJ equivalence at p=0.007 is not supported by the corrected data. At per-test level, the minimum equivalence margin is ±2.25pp (larger than the ±2pp threshold used). The old p=0.007 was from CLS-CWM data (gap=1.24pp, 5 seeds), not CLS-TRAJ.

---
