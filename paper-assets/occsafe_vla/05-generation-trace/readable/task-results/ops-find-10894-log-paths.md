# ops find 10894 log paths

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_find-10894-log-paths_20260526T182255_result.json`
- **Structured JSON:** [`38cce1db394123547dbd.json`](../../sessions/38/38cce1db394123547dbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

## 1. 日志文件路径

| 实验 | 日志路径 |
|------|---------|
| full_occ_ln_v2_s0 | `/root/autodl-tmp/checkpoints/full_occ_ln_v2_s0/train.log` |
| full_occ_ln_v2_s1 | `/root/autodl-tmp/checkpoints/full_occ_ln_v2_s1/train.log` |
| detach_ln_v2_s0 | `/root/autodl-tmp/checkpoints/detach_ln_v2_s0/train.log` |

## 2. 训练状态：3 个实验都已停止

**tmux sessions 不存在** — `tmux list-sessions` 只有 `reverse_cutoff_s2_v2`。`ps aux | grep finetune` 也只有 reverse_cutoff_s2_v2 的进程。

日志显示这 3 个实验都在 05/27 02:15 左右启动，跑到 **step ~275**（约 5 分钟）后停止。速度约 **1.07-1.08 it/s**。

| 实验 | 最后 step | 初始 loss | 状态 |
|------|-----------|-----------|------|
| full_occ_ln_v2_s0 | ~275 | occ=0.1096, action=0.6719 | **已停止** |
| full_occ_ln_v2_s1 | ~276 | occ=0.1727, action=0.6953 | **已停止** |
| detach_ln_v2_s0 | ~275 | occ=0.1077, action=0.6797 | **已停止** |

这 3 个实验需要重新启动。当前服务器上唯一在跑的 finetune 是 `reverse_cutoff_s2_v2`（在 cuda:0 上）。

---
