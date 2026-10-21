# infra diagnose bce s123 exit

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_diagnose_bce_s123_exit_20260517T213538_result.json`
- **Structured JSON:** [`7dd6f6a01089fd4e0f2d.json`](../../sessions/7d/7dd6f6a01089fd4e0f2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能之前已删除或由其他 session 创建）。

**结果：正常完成。**

| 项目 | 值 |
|---|---|
| 状态 | 正常完成 ("BCE training complete") |
| 总 steps | 2700/2700 |
| 最终 loss | 0.6362 (bce=0.6350, reg=0.0011) |
| 最终 sparsity | 0.511 |
| 训练耗时 | 2823.8s (~47min), 1.05s/step |
| Checkpoint | `checkpoints/bce_isocompute_v3_s123/predictor_bce.pt` (145MB) |

---
