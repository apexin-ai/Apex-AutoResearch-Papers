# ops cleanup k5 cache gpu check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup-k5-cache-gpu-check_20260514T075942_result.json`
- **Structured JSON:** [`a083640f83e10d08674e.json`](../../sessions/a0/a083640f83e10d08674e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**K5 缓存清理** — 已删除，`ls` 确认 `No such file or directory`。

**GPU 状态** — 无 orphan 进程，4 个进程 PID 与预期一致：

| GPU | PID | 显存占用 | GPU 利用率 |
|-----|-------|---------|-----------|
| cuda:0 | 180256 (shard0) | 1534 MiB / 24564 MiB | 26% |
| cuda:1 | 180405 (shard1) | 1534 MiB / 24564 MiB | 25% |
| cuda:2 | 118108 (eval-spatial-v3) | 1414 MiB / 24564 MiB | 19% |
| cuda:3 | 180485 (shard2) | 1534 MiB / 24564 MiB | 25% |

注：PID 与预期略有偏差（180251→180256, 180400→180405, 180480→180485），差值很小，可能是任务重启过，不算 orphan。

**Precompute 进度** — 三个 shard 都在跑 spatial 阶段，当前均处理到 ~400/4056 样本（约 10%），速度 ~0.45s/sample，预计每个 shard 还需 ~27 分钟完成。

---
