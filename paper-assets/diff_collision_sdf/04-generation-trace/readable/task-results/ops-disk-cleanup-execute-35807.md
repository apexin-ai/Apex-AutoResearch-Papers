# ops disk cleanup execute 35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-execute-35807_20260528T232852_result.json`
- **Structured JSON:** [`a6bc9bfb994281fa8604.json`](../../sessions/a6/a6bc9bfb994281fa8604.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 已用 | 346G (99%) | 268G (77%) |
| 可用 | 4.3G | 83G |
| 回收 | — | **78G** |

15 项全部执行：4 个空/近空目录 + 11 个中间 checkpoint（各 7.2G）。每个实验的 best/ 和最高 step 均已保留。

---
