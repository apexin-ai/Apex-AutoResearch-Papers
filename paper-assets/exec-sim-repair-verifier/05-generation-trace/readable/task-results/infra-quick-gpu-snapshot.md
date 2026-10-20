# infra quick gpu snapshot

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_quick-gpu-snapshot_20260518T105547_result.json`
- **Structured JSON:** [`37632bdbe941a175eee3.json`](../../sessions/37/37632bdbe941a175eee3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| GPU | 任务 | 进度 | running_acc | 利用率 | 显存 |
|-----|------|------|-------------|--------|------|
| 0 | CLS v5 | tmux 无输出（可能已结束或 session 名变了） | — | 98% | 24.9 GiB |
| 1 | CWM s42 epoch3 | 5391/9784 (55.1%) | 56.2% | 56% | 17.7 GiB |
| 2 | CWM s42 epoch2 (D124) | 2200/9784 (22.5%) | 66.6% | 64% | 17.9 GiB |
| 3 | CWM s123 | 5009/9784 (51.2%) | 61.5% | 52% | 17.5 GiB |

GPU 0 占满显存且利用率 98%，但 tmux session `deepseek-cls-repo-v5` 没捕获到 step/loss/epoch 行——可能 session 名已变或输出格式不匹配。需要我查一下 GPU 0 上跑的是什么进程吗？

---
