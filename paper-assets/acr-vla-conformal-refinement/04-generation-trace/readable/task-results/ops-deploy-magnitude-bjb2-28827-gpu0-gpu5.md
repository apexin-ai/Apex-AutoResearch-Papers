# ops deploy magnitude bjb2 28827 gpu0 gpu5

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-magnitude-bjb2-28827-gpu0-gpu5_20260517T230444_result.json`
- **Structured JSON:** [`0ea565cf9dfae6d4f290.json`](../../sessions/0e/0ea565cf9dfae6d4f290.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU0 和 GPU5 显存从 1 MiB 升至 4 MiB，进程正在初始化加载中（模型较大，显存会逐步上升）。

部署完成：

| 实验 | GPU | PID | tmux session |
|------|-----|-----|-------------|
| eval-obs-only-object-norm02-seed48 | cuda:0 | 488388 | eval-obs-only-object-norm02-seed48 |
| eval-perdof-object-norm02-seed48 | cuda:5 | 488656 | eval-perdof-object-norm02-seed48 |

残留 tmux session `train-crm-k1-v2` 已清理，registry hypothesis 已更新。

---
