# ops check eval kl30 teal

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_eval_kl30_teal_20260516T062124_result.json`
- **Structured JSON:** [`1d051022db7e961a5222.json`](../../sessions/1d/1d051022db7e961a5222.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**eval_kl30_teal_30pct — 成功完成。**

Metrics（WikiText-2, sparsity_target=0.3）：

| 指标 | PPL |
|------|-----|
| Dense | 6.12 |
| Predictor Hard Mask | 7.30 |
| TEAL Sparse | 8.98 |

Model-level actual sparsity 精确命中 0.300。相比之前误跑 sparsity_target=0.5 得到的 13.63，正确 target=0.3 下 TEAL PPL 降到 8.98，符合预期。

Registry 已更新 (conclusion=success, status=DONE, metrics 已写入)，cron 已删除。

---
