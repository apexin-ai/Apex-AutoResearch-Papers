# code cross model per class

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cross-model-per-class_20260517T150156_result.json`
- **Structured JSON:** [`872b60acc2655045468d.json`](../../sessions/87/872b60acc2655045468d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Here's the summary:

## Cross-Model Chains Per-Class Metrics

**File:** `results/cross_model_chains_per_class.json`  
**N = 2964** (988 per class, balanced), 5 generators × 3 families

### 3-Class (macro F1 = 0.8305 [0.8172, 0.8439])

| Class | Precision | Recall | F1 | Support |
|-------|-----------|--------|----|---------|
| gen-0 | 0.9213 [.905,.938] | 0.9484 [.934,.962] | 0.9347 [.923,.946] | 988 |
| gen-1 | 0.7370 [.711,.765] | 0.8026 [.777,.827] | 0.7684 [.748,.788] | 988 |
| gen-2+ | 0.8416 [.817,.866] | 0.7419 [.715,.769] | 0.7886 [.768,.809] | 988 |

### Binary gen-0 vs gen-1+ (macro F1 = 0.9506 [0.9421, 0.9589])

| Class | Precision | Recall | F1 | Support |
|-------|-----------|--------|----|---------|
| gen-0 | 0.9213 | 0.9484 | 0.9347 | 988 |
| gen-1+ | 0.9738 | 0.9595 | 0.9666 | 1976 |

### Other results files confirmed
- **distributional_tests.json** — KS tests across 7 features, all 3 depth-pair comparisons, Bonferroni-corrected
- **tost_multi_margin.json** — TOST equivalence tests at multiple margins (1%–5%), comparing all vs size-matched configurations

---
