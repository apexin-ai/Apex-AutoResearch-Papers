# SciERC 5-Seed Metric Consistency Verification

**Date**: 2026-05-24  
**Status**: CRITICAL — construction gain disappears under paper-consistent metric

## Key Finding

The +1.11pp LP construction gain reported in `scierc_5seed_construction_aligned.json` is an **artifact of metric mismatch**. The construction script used instance-averaged F1, but the paper (Table 4) reports micro-F1.

| Metric | Construction Δ | Direction | Pooled p |
|--------|----------------|-----------|----------|
| Instance-averaged F1 | **+1.11pp** | 4/5 positive | 0.0000 |
| **Micro-F1 (paper metric)** | **-0.20pp** | **1/5 positive** | **0.7774** |

## Verification Details

### 1. Greedy Field
- `greedy` field IS present in all `samples.jsonl` files (551/551 instances per seed)
- It contains T=0 greedy decode output, NOT samples[0]
- The old construction script correctly used this field via `inst.get("greedy", inst["samples"][0])`

### 2. Baseline Discrepancy Explained
| Source | Greedy F1 | Metric |
|--------|-----------|--------|
| Paper Table 4 | ~66.3% | micro-F1 |
| report.json mean (n=551) | 66.33% | micro-F1 |
| Recomputed (n=529) | 66.64% | micro-F1 |
| Old construction script (n=529) | 64.67% | instance-averaged |

The ~1.6pp gap is entirely from metric type (micro vs instance-averaged), not wrong baseline.

### 3. Why Metrics Diverge
Micro-F1 aggregates TP/FP/FN across all instances before computing P/R/F1. Instance-averaged computes F1 per instance then averages. The gap arises because:
- Instances with many entities (correctly predicted) contribute more to micro-F1
- Instances with few/no entities contribute equally to instance-averaged, dragging it down
- Construction tends to improve instance-averaged by boosting low-entity instances, but this doesn't translate to micro-F1

### 4. Per-Seed Results (Micro-F1, Paper-Consistent)

| Seed | Greedy | LP Constr | Δpp | p |
|------|--------|-----------|-----|---|
| 42 | 0.6683 | 0.6597 | -0.85 | 0.940 |
| 123 | 0.6663 | 0.6652 | -0.10 | 0.577 |
| 456 | 0.6663 | 0.6683 | +0.20 | 0.367 |
| 2024 | 0.6675 | 0.6668 | -0.06 | 0.541 |
| 3141 | 0.6639 | 0.6619 | -0.19 | 0.624 |

**Mean ± σ: -0.20 ± 0.39 pp (1/5 positive)**  
**Pooled (n=2645): Δ=-0.20pp, p=0.7774**

### 5. Implications for Paper Patch
The paper patch claiming +1.11pp construction gain on SciERC is **invalid** when measured with the paper's own metric (micro-F1). Options:
1. Report instance-averaged F1 consistently throughout (requires changing Table 4 baseline)
2. Accept that construction doesn't improve SciERC under micro-F1
3. Investigate why instance-averaged shows improvement but micro doesn't

## Files
- Server script: `/root/autodl-tmp/struct_self_consist_ie/output/scierc_metric_verification.py`
- Server results: `/root/autodl-tmp/struct_self_consist_ie/output/scierc_metric_verification.txt`
- Server JSON: `/root/autodl-tmp/struct_self_consist_ie/output/scierc_metric_verification.json`
