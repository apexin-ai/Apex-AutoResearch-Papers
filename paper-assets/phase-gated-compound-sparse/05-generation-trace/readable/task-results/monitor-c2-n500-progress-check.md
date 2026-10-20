# monitor c2 n500 progress check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_c2_n500_progress_check_20260515T043831_result.json`
- **Structured JSON:** [`9e237862b4a8f14a9717.json`](../../sessions/9e/9e237862b4a8f14a9717.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## n=500 实验进度汇总

### GPU 状态
4 块 GPU 全部在用，利用率 72-77%：
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 77% | 23.7/97.9 GB |
| 1 | 77% | 27.4/97.9 GB |
| 2 | 72% | 34.1/97.9 GB |
| 3 | 76% | 34.7/97.9 GB |

### 已完成 (12/16 conditions)

| Condition | Qwen | DeepSeek |
|-----------|------|----------|
| imp_s015 | ✅ 500/500 | ✅ 500/500 |
| rand_s015 | ✅ 500/500 | ✅ 500/500 |
| imp_s020 | ✅ 500/500 | ✅ 500/500 |
| rand_s020 | ✅ 500/500 | ✅ 500/500 |
| imp_s025 | ✅ 500/500 | ✅ 500/500 |
| rand_s025 | ✅ 500/500 | ✅ 500/500 |

### 正在运行 (4/16 conditions, 全是 s030)

| Condition | 进度 | 开始时间 | 预估剩余 |
|-----------|------|----------|----------|
| qw_imp_s030 | **407/500** (81%) | 09:53 | ~38 min |
| qw_rand_s030 | **402/500** (80%) | 10:01 | ~39 min |
| ds_rand_s030 | **205/500** (41%) | 10:54 | ~2.5h |
| ds_imp_s030 | **154/500** (31%) | 11:19 | ~3h |

Qwen 两个 s030 条件约 **13:20** 前完成。DeepSeek 两个 s030 条件预计 **15:30-16:00** 完成（DeepSeek 每题生成 token 更多，速度约 2 problems/min vs Qwen 的 2.5/min）。

---
