# ops cleanup and submit cell2 4

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup-and-submit-cell2-4_20260526T120547_result.json`
- **Structured JSON:** [`98e6899cdce93bc49d42.json`](../../sessions/98/98e6899cdce93bc49d42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**停止操作。** GPU 1/2/3 全部在满载训练中：

| GPU | 显存占用 | PID |
|-----|---------|-----|
| 0 | 62194 MiB (99%) | 170698 (reverse_cutoff_s2_v2) |
| 1 | 63028 MiB (99%) | 341771 |
| 2 | 62194 MiB (99%) | 341987 |
| 3 | 62194 MiB (99%) | 342341 |

4 个 tmux session 全部存在：
- `reverse_cutoff_s2_v2` — 17:02 创建
- `full_occ_ln_v2_s0` — 20:05 创建
- `full_occ_ln_v2_s1` — 20:05 创建
- `detach_ln_v2_s0` — 20:05 创建

**之前的 submit_training_job 虽然报了 "duplicate session" 错误，但 3 个训练实际上已经成功启动并在运行。** 不需要清理，也不需要重新提交。所有实验正在正常训练。

---
