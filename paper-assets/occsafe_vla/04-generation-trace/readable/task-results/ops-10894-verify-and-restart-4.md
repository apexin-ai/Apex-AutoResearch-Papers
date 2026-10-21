# ops 10894 verify and restart 4

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_10894-verify-and-restart-4_20260527T004716_result.json`
- **Structured JSON:** [`49714885dfd41909a69d.json`](../../sessions/49/49714885dfd41909a69d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**停止操作，汇报异常。**

westd-10894 上 4 张卡全部被占用，正在运行 4 个 finetune 训练（已运行约 10 分钟）：

| GPU | PID | 运行时间 | 实验 | 参数 |
|-----|--------|---------|------|------|
| 0 | 481426 | 10:39 | `full_occ_ln_v2_s1c` | detach=false, ln, seed=43 |
| 1 | 481643 | 10:35 | `full_occ_ln_v2_s2` | detach=false, ln, seed=44 |
| 2 | 481988 | 10:32 | `detach_ln_v2_s0c` | detach=true, ln, seed=42 |
| 3 | 482336 | 10:28 | `detach_ln_v2_s1c` | detach=true, ln, seed=43 |

这些是**已有的训练任务**，与你要启动的 4 个实验参数有部分重叠但 exp_id 不同（`s1c/s2/s0c/s1c` vs `s0d/s1d/s0d/s2`）。无法在不 kill 现有进程的情况下启动新训练。

请确认：
1. 是否需要终止这 4 个正在运行的实验，再启动新的？
2. 还是等它们跑完再启动？

---
