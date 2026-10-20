# ops submit grid b3 b5 seed456

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit_grid_b3_b5_seed456_20260515T005412_result.json`
- **Structured JSON:** [`8ee705e7a782cee27f28.json`](../../sessions/8e/8ee705e7a782cee27f28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 GPU 全部状态正常，无需操作：

| GPU | 实验 | PID | 显存 |
|-----|------|-----|------|
| cuda:0 | grid_b2_0_seed456 | 152488 | 75007 MiB |
| cuda:1 | grid_b0_5_seed456 | 145062 | 46523 MiB |
| cuda:2 | grid_b5_0_seed456 + 2个eval | 158300, 158523, 159262 | 64823 MiB |
| cuda:3 | grid_b3_0_seed456 | 158216 | 46523 MiB |

grid_b3_0_seed456 和 grid_b5_0_seed456 已经被提交并在运行中，跳过重复提交。

---
