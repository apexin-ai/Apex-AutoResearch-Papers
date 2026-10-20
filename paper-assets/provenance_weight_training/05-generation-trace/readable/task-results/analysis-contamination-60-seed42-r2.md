# analysis contamination 60 seed42 r2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_contamination_60_seed42_r2_20260516T015309_result.json`
- **Structured JSON:** [`ab60b5bab5b0258533d3.json`](../../sessions/ab/ab60b5bab5b0258533d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 总结

**contamination_60_seed42_r2** 完成，conclusion = **success**。

| 指标 | 值 |
|------|-----|
| eval_ppl_holdout | **17.74** |
| eval_loss_holdout | 2.8759 |
| eval_tokens | 4,077,068 |
| train_loss | 9.6349 |
| train_runtime | 14092s (~3h55m) |

**Baseline 对比（ρ=0.6）：**
- vs uniform (PPL=17.766): adaptive **优** -0.026 PPL
- vs grid b=0.5 (PPL=17.704): adaptive **劣** +0.036 PPL

Adaptive weighting 在 ρ=0.6 高污染场景下仍能小幅优于 uniform baseline，验证了 graceful degradation 假设。不过 grid b=0.5 的固定权重方案在此设置下表现更好。

---
