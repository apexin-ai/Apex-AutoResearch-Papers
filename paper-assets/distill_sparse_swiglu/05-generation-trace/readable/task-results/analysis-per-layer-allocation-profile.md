# analysis per layer allocation profile

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_per_layer_allocation_profile_20260517T133538_result.json`
- **Structured JSON:** [`6d841ce2520cedfe3d62.json`](../../sessions/6d/6d841ce2520cedfe3d62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Here are the results:

## Per-Layer Allocation: s42 vs s123 (Global Top-K, 30% Sparsity)

### Key Finding: The allocation profiles are remarkably similar between seeds. The MMLU anomaly is NOT caused by gross allocation pattern differences.

**Comparison Table:**
```
Layer  s42 ret   s123 ret  delta     flag
0      0.8159    0.8117    -0.0042
...
14     0.7808    0.7406    -0.0402
15     0.8543    0.8201    -0.0342
16     0.9010    0.8587    -0.0423   (peak: mid-layers dominate)
17     0.8656    0.8646    -0.0010
18     0.8871    0.8768    -0.0103
...
24     0.5345    0.6985    +0.1640   BIG_DELTA (only big outlier)
25     0.5090    0.4901    -0.0189   s123_starved
26     0.4807    0.4939    +0.0132   both starved
27     0.4675    0.4926    +0.0251   both starved
28     0.4570    0.4604    +0.0034   both starved (minimum)
29     0.5369    0.5229    -0.0140
30     0.7806    0.7762    -0.0044
31     0.8345    0.8447    +0.0102
```

### Summary Statistics

| Region | s42 | s123 | delta |
|---|---|---|---|
| Early (0-7) | 0.7397 | 0.7386 | -0.0011 |
| Mid (8-23) | 0.7426 | 0.7319 | -0.0107 |
| Knowledge (12-20) | **0.8071** | **0.7856** | -0.0215 |
| Late (24-31) | 0.5751 | 0.5974 | +0.0223 |

**Starved layers (<50% retention):**
- s42: layers [26, 27, 28] (3 layers)
- s123: layers [25, 26, 27, 28] (4 layers)
- No layers starved below 10%

### Analysis Conclusions

1. **Both seeds show the same "bathtub" pattern**: high retention at edges (L0, L30-31), peak in mid-layers (L15-18 at ~85-90%), and a starvation zone at L25-28 (~45-50%). This is a structural property of global allocation, not seed-specific.

2. **The only significant difference is layer 24**: s42 retains 53.5% vs s123's 69.9% (delta=+16.4%). This is the sole BIG_DELTA. Paradoxically, **s42 is MORE starved at L24, yet s123 (which retains more there) has the worse MMLU**... wait, actually s42 has MMLU=25.27% and s123 has MMLU=38.07%. So s42 (the worse MMLU seed) is more starved at L24 specifically.

3. **Knowledge layers (L12-20) are actually well-fed in both seeds** (80.7% vs 78.6%). The "late-layer starvation destroys MMLU" hypothesis doesn't hold because the starved zone (L25-28 at ~46%) is common to both seeds with similar severity.

4. **The s42 MMLU anomaly cannot be explained by gross allocation differences.** The profiles differ by only ~2% on average. The root cause is more likely in the specific neurons selected within each layer (which neurons are kept vs pruned), not the layer-level allocation ratio. This points to a quality-of-selection issue (predictor calibration) rather than a quantity-of-allocation issue.

JSON saved to `/root/distill_sparse_swiglu/results/per_layer_allocation_s42_vs_s123.json`.

---
