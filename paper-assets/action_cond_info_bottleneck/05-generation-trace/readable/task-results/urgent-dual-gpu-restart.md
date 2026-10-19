# urgent dual gpu restart

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_dual-gpu-restart_20260516T134820_result.json`
- **Structured JSON:** [`760b565df2fca7df5c65.json`](../../sessions/76/760b565df2fca7df5c65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**两个训练都已经在正常运行，不需要重启。**

诊断结果：

| GPU | 实验 | PID | 进度 | GPU 利用率 | 显存 |
|-----|------|-----|------|-----------|------|
| cuda:0 | acib_v7_contrastive (seed 42) | 21363 | step 6600/20000 | 99% | 16220 MiB |
| cuda:1 | acib_v7_seed2 (seed 1337) | 27427 | step 300/20000 | 65% | 16216 MiB |

详情：
- **v7_contrastive**: 旧 PID 960110 确实已死，但已被重新启动为 tmux 会话 `acib_v7_contrastive`（新 PID 21363，启动于 20:45）。从日志看训练从头开始，当前在 step 6600，checkpoint-5000 已保存（1.3GB）。速度 1.8 steps/s。
- **v7_seed2**: PID 27422 wrapper 存活，实际训练进程 PID 27427（启动于 21:44）。当前 step 300，正在加速中。
- **磁盘**: 根分区 46%（17GB 空闲），数据盘 30%（176GB 空闲），没问题。

两个 GPU 都满载运行，无需干预。

---
