# monitor w41 progress final

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_w41_progress_final_20260528T113200_result.json`
- **Structured JSON:** [`6f9f2ae24b7ae925e3f2.json`](../../sessions/6f/6f9f2ae24b7ae925e3f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 实验 | 状态 | 进度 | 当前SR | 预计剩余 |
|------|------|------|--------|----------|
| **l2norm_k075** seed46 | **已完成** ✓ | 500/500 | **73.2%** | — |
| **random_k095** seed46 | 运行中 (T9 ep=40) | 490/500 | 58.4% (T0-T8) | ~3 min |
| **random_k05** seed46 | 运行中 (T9 ep=10) | 460/500 | 50.0% (T0-T8) | ~12 min |

注意：
- l2norm 实际日志名为 `l2norm_k075`（非 k07），已于 16:15 完成，EXIT_CODE=0，结果存于 `pi05_l2norm_k0.75_libero_10_seed46.json`
- PID 923767 仍存活（463% CPU, 2h14m），可能已被复用跑其他任务
- random_k095 和 random_k05 均接近完成，预计 ~15 分钟内全部结束

---
