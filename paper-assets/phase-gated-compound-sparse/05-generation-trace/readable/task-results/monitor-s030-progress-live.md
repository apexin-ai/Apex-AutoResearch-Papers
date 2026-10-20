# monitor s030 progress live

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_s030_progress_live_20260515T044450_result.json`
- **Structured JSON:** [`daeb59efdcf351f86167.json`](../../sessions/da/daeb59efdcf351f86167.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## n=500 s030 实时进度 (12:45 UTC+8)

### GPU 状态

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 76% | 23.7/97.9 GB |
| 1 | 96% | 27.4/97.9 GB |
| 2 | 96% | 34.1/97.9 GB |
| 3 | 96% | 34.7/97.9 GB |

### s030 进度

| 条件 | 模型 | 方法 | 进度 | 启动时间 | 速率 | ETA (UTC+8) |
|------|------|------|------|----------|------|-------------|
| qw_imp_s030 | Qwen-7B | importance | **420/500** (84%) | 09:53 | ~0.41 min/p | ~13:18 |
| qw_rand_s030 | Qwen-7B | random | **415/500** (83%) | 10:01 | ~0.40 min/p | ~13:19 |
| ds_rand_s030 | DeepSeek-7B | random | **217/500** (43%) | 10:54 | ~0.51 min/p | ~15:10 |
| ds_imp_s030 | DeepSeek-7B | importance | **167/500** (33%) | 11:19 | ~0.52 min/p | ~15:37 |

### 小结

- **Qwen 两个条件**约 30 分钟后完成（~13:20）
- **DeepSeek 两个条件**预计 15:10–15:40 完成
- 4 个进程均正常运行，无报错

---
