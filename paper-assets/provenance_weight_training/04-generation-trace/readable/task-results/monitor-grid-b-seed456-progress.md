# monitor grid b seed456 progress

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_grid_b_seed456_progress_20260514T233106_result.json`
- **Structured JSON:** [`639bec28e7869891fa05.json`](../../sessions/63/639bec28e7869891fa05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个进程全部存活，4 GPU 满载运行。

| exp_id | GPU | current_step/total | progress% | ETA | GPU利用率 | 显存占用 |
|--------|-----|--------------------|-----------|-----|-----------|---------|
| grid_b2_0_seed456 | cuda:0 | 44/6103 | 0.7% | ~3h34m | 99% | 46.5/97.9 GB |
| grid_b0_5_seed456 | cuda:1 | 3703/6103 | 60.7% | ~1h25m | 94% | 46.5/97.9 GB |
| grid_b1_0_seed456 | cuda:2 | 3904/6103 | 64.0% | ~1h18m | 97% | 46.5/97.9 GB |
| grid_b1_5_seed456 | cuda:3 | 3908/6103 | 64.0% | ~1h18m | 99% | 46.5/97.9 GB |

速度均为 ~2.12s/it。

- **grid_b2_0_seed456** 启动最晚（运行仅 1m47s），刚开始跑
- **grid_b0_5_seed456** 因 OOM retry 比 b1.0/b1.5 慢约 200 steps
- **grid_b1_0 / b1_5** 进度基本同步，预计约 1h18m 后完成
- 全部实验预计在 ~3.5h 内完成（以 b2.0 为瓶颈）

---
