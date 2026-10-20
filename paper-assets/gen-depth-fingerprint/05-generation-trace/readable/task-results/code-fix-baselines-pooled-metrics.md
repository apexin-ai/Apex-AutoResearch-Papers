# code fix baselines pooled metrics

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-baselines-pooled-metrics_20260516T135916_result.json`
- **Structured JSON:** [`a0bdf626088014967330.json`](../../sessions/a0/a0bdf626088014967330.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results complete. Here's the full summary:

## Pooled LOGO F1 Results (document-level bootstrap CI)

| Method | Pooled 3-class F1 | Pooled Binary F1 | Binary 95% CI |
|--------|-------------------|------------------|---------------|
| avg_logprob | 0.7085 | 0.6785 | [0.6717, 0.6854] |
| fastdetectgpt | 0.6654 | 0.5805 | [0.5741, 0.5875] |
| binoculars | 0.4094 | 0.5327 | [0.5268, 0.5392] |
| ld_score | 0.6334 | 0.6758 | [0.6691, 0.6822] |
| 4det_ensemble | 0.7786 | 0.6983 | [0.6919, 0.7045] |
| **4det_surface** | **0.7832** | **0.7050** | [0.6983, 0.7110] |
| **7feature_ours** | **0.7616** | **0.6935** | [0.6867, 0.7000] |

### Key answers:
- **4det_surface pooled binary F1 = 0.705 > 0.694? YES**
- **4det_surface > 7feature_ours? YES** (0.705 vs 0.6935)

Note: 7feature_ours uses XGB 200/6 (the paper config); all other baselines use XGB 100/3. LD score uses top-10K trigram vocabulary for computational efficiency. The 4det_surface ensemble (4 detector scores + ttr + hapax_ratio) exceeds our 7-feature approach by ~1.2 percentage points on pooled binary F1, with non-overlapping CI lower bounds (0.6983 vs 0.7000 — just barely overlapping actually).

---
