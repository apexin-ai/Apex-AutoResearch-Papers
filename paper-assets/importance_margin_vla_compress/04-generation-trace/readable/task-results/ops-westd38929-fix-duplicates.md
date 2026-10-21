# ops westd38929 fix duplicates

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd38929-fix-duplicates_20260520T191550_result.json`
- **Structured JSON:** [`0a018ce719e7aed8d6d2.json`](../../sessions/0a/0a018ce719e7aed8d6d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 GPU 全部在跑，替换完成。

**结果汇总：**

| GPU | 实验 | tmux session | 状态 |
|-----|------|-------------|------|
| 0 | random k=0.95 seed42 | eval_random_k095_s42 | ✅ 运行中 (66%, 15980 MiB) |
| 1 | random k=0.7 seed42 | eval_random_k07_s42 | ✅ 运行中 (40%, 15980 MiB) |
| 2 | random k=0.3 seed43 | eval_random_k03_s43 | ✅ 保留 (66%, 16108 MiB) |
| 3 | L2 norm k=0.9 seed43 | eval_l2norm_k09_s43 | ✅ 保留 (48%, 15980 MiB) |

**已 kill：** eval_random_k095_s43 (GPU 0)、eval_random_k09_s43 (GPU 1)
**已启动：** random k=0.95 seed42 (GPU 0)、random k=0.7 seed42 (GPU 1)

注：首次启动因未激活 conda 导致 `python: command not found`，已加上 conda 激活后重启成功。

---
