# ops restart cutoff s0

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restart-cutoff-s0_20260522T075622_result.json`
- **Structured JSON:** [`57213470404a42996b70.json`](../../sessions/57/57213470404a42996b70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

新 cutoff_s0 已启动，GPU 0 利用率 99%。汇报：

| 项目 | 结果 |
|------|------|
| 旧 cutoff_s0 checkpoint | **15GB** |
| 清理后可用空间 | **299GB** (350GB 总量, 52GB 已用) |
| 磁盘预算 | 4×5×15GB=300GB vs 299GB 可用 — **基本够用**，实际不会 4 个实验同时满 5 个 checkpoint |
| 现有其他 checkpoint | occ_s1_fresh 30GB；depth_s0/depth_s1/cutoff_s1 尚为空 |
| 新 cutoff_s0 PID | **136037**，cuda:0，99% GPU 利用率，已开始训练 |
| save_freq | 10000（原 2500） |

---
