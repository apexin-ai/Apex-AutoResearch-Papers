# analysis run pooled 4bench irt v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_run-pooled-4bench-irt-v2_20260515T132925_result.json`
- **Structured JSON:** [`6bee239acb1e667cb12c.json`](../../sessions/6b/6bee239acb1e667cb12c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All results collected. Here's the complete summary:

---

## Pooled 4-Benchmark IRT Results (2PL+gamma, v2 with subsampling)

### Per-benchmark fits

| Benchmark | gamma | CI95 | CI excl. 0 | rhat | ESS | div | N_models | N_items | subsampled | fit_time | PPP |
|-----------|-------|------|-----------|------|-----|-----|----------|---------|------------|----------|-----|
| **MMLU** | 0.0888 | [-0.218, 0.394] | no | 1.0101 | 720 | 0 | 10 | 2000 | 14042→2000 | 1512s | 0.271 |
| **GSM8K** | -0.4033 | [-0.911, 0.066] | no | 1.0125 | 249 | 0 | 12 | 1319 | no | 1162s | 0.953 |
| **ARC** | 0.4879 | [0.114, 0.878] | **yes** | 1.0081 | 1174 | 0 | 10 | 1172 | no | 763s | 0.006 |
| **HumanEval** | -1.0545 | [-1.749, -0.362] | **yes** | 1.0062 | 843 | 0 | 18 | 164 | no | 110s | 1.000 |

### Joint fit (shared gamma)

| Metric | Value |
|--------|-------|
| global_gamma mean | 0.2666 |
| global_gamma sd | 7.1362 |
| CI95 | [-7.183, 7.807] |
| rhat | **1.7417** |
| ESS | **6.1** |
| divergences | 0 |
| PPP | 0.5 |
| residual_mae | 0.1152 |
| N_models | 6 |
| N_total_items | 4655 |
| fit_time | 2774s |
| Dosages | [5, 25, 100, 100, 100, 100] |

**Joint fit did NOT converge** — rhat=1.74 >> 1.05, ESS=6 << 100. Root cause: only 6 common models (after per-benchmark exclusions intersected), no d000 controls in the intersection, and 4655 items severely underidentifies the model.

### Comparison to S1-only reference
| Benchmark | Previous (S1-only) | Current (pooled) |
|-----------|-------------------|-----------------|
| GSM8K | gamma=0.19 | gamma=-0.40 |
| ARC | gamma=-1.46 | gamma=+0.49 |

Signs flipped — likely due to different exposure model (oracle dosage vs S1 signals), different model exclusions, and pooled multi-scale data.

### Output files
All saved to `/root/autodl-tmp/exp006/results_pooled_4bench_aligned_2pl/`:
- `pooled_4bench_results.json` (full results)
- `joint_fit_results.json`
- `mmlu/irt_results.json`, `gsm8k/irt_results.json`, `arc_challenge/irt_results.json`, `humaneval/irt_results.json`

---
