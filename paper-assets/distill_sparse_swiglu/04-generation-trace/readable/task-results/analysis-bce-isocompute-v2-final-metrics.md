# analysis bce isocompute v2 final metrics

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bce_isocompute_v2_final_metrics_20260515T204429_result.json`
- **Structured JSON:** [`80bd37b74135b702e44c.json`](../../sessions/80/80bd37b74135b702e44c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Registry 已更新为 DONE。

**最终 metrics 汇总：**

| 指标 | 值 |
|------|-----|
| final_loss | 0.6637 |
| final_bce_loss | 0.6586 |
| final_reg_loss | 0.0051 |
| final_sparsity | 0.502 (target 0.50 ✓) |
| training_steps | 1000 |
| training_time | 1047.8s (1.05s/step) |
| checkpoints | step_250, step_500, step_750, step_1000, final |

Sparsity 稳定收敛到 ~0.50，reg_loss 从 0.0171 降到 0.0051，BCE loss 从 0.6714 降到 0.6586。

---
