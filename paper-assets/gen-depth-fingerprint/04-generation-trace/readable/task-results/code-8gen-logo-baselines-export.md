# code 8gen logo baselines export

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_8gen-logo-baselines-export_20260516T172209_result.json`
- **Structured JSON:** [`b444f64d9580e34425e8.json`](../../sessions/b4/b444f64d9580e34425e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Results saved to `/root/gen-depth-fingerprint/results/8gen_logo_baselines.json`.

**Summary table (8-gen LOGO):**

| Method | 3-class F1 | Binary F1 |
|--------|-----------|-----------|
| avg_logprob | 0.6834 | 0.6405 |
| fastdetectgpt | 0.6552 | 0.5642 |
| binoculars | 0.3950 | 0.5196 |
| ld_score | 0.6189 | 0.6574 |
| 4det_ensemble | 0.7696 | 0.6860 |
| 4det_surface | **0.7873** | **0.6986** |
| 7feature_ours | 0.7401 | 0.6614 |

Key observations:
- 4det_surface beats 7feature_ours on LOGO (0.787 vs 0.740 3-class, 0.699 vs 0.661 binary)
- llama-3.2-3b and mistral-7b-v0.3 drag down averages substantially for all methods (new, unseen generator families)
- CIs are pooled bootstrap (slightly above per-gen average F1 due to sample-count weighting)

The file is at the expected path: `/root/gen-depth-fingerprint/results/8gen_logo_baselines.json`

---
