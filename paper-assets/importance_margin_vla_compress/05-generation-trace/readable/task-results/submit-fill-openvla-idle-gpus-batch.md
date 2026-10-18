# submit fill openvla idle gpus batch

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_fill_openvla_idle_gpus_batch_20260526T152129_result.json`
- **Structured JSON:** [`a9cafe1b91684d87ad48.json`](../../sessions/a9/a9cafe1b91684d87ad48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 1 已成功提交并运行。

**汇总：**

| 实验 | 状态 |
|------|------|
| **实验 1**: westd-38929:cuda:1 — Random k=0.85 Long | **RUNNING** (PID 668236, 模型已加载) |
| **实验 2**: westd-27271:cuda:1 — Random k=0.7 Goal | **无法提交** — GPU 被 `random_prune k=0.5 libero_goal` 占用 |
| **实验 3**: westd-41074:cuda:1 — Random k=0.5 Object | **无法提交** — GPU 被 `attention_prune k=0.5 libero_object` 占用（即 reconcile 中的 PID 652888） |

westd-27271 和 westd-41074 的 cuda:1 当前各有一个 eval 实验在跑，需要等它们完成后再提交实验 2 和 3。

---
