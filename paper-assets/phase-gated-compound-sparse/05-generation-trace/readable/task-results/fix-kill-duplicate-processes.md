# fix kill duplicate processes

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill-duplicate-processes_20260514T002837_result.json`
- **Structured JSON:** [`468034de548ff67b471b.json`](../../sessions/46/468034de548ff67b471b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Kill 结果
| PID | 状态 |
|-----|------|
| 38482 (GPU 0 s025 重复) | ✓ 已 kill |
| 38619 (GPU 1 s035 重复) | ✓ 已 kill |
| 39848 (GPU 2 s040 重复) | ✓ 已 kill |

## nvidia-smi（kill 后）
每张 GPU 恢复为单进程：
| GPU | PID | 显存 | 利用率 |
|-----|-----|------|--------|
| 0 | 38125 (s025) | 25216 MiB | 77% |
| 1 | 39001 (s035) | 25216 MiB | 76% |
| 2 | 38760 (v4d) | 25216 MiB | 76% |
| 3 | 32192 (random_r2) | 23520 MiB | 99% |

## 数据完整性
4 个输出目录全部为空（无 profiling_results.json）——结果尚未写入，无数据损坏。

| 目录 | 状态 |
|------|------|
| profiling_output_v4_s025 | 空，无损坏 |
| profiling_output_v4_s035 | 空，无损坏 |
| profiling_output_v4_s040 | 空，无损坏 |
| profiling_output_v4d | 空，无损坏 |

## 存活进程状态
| PID | 任务 | 运行时间 | 状态 |
|-----|------|---------|------|
| 38120/38125 | s025 (GPU 0) | 6m22s | ✓ 存活 |
| 38996/39001 | s035 (GPU 1) | 5m52s | ✓ 存活 |
| 38760 | v4d (GPU 2) | 5m54s | ✓ 存活 |
| 32187/32192 | random_r2 (GPU 3) | 1h00m | ✓ 存活 |

注意：PID 39843（s040 的 bash wrapper）随子进程 39848 被 kill 后已退出。

## 是否需要重启
**否。** 所有输出目录为空（结果一次性写入，尚未到写入阶段），无数据竞争损坏。4 个存活实验进程均健康运行。

---
