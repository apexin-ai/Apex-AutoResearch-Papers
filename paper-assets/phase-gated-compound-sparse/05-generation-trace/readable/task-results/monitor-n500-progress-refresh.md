# monitor n500 progress refresh

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_n500_progress_refresh_20260515T014838_result.json`
- **Structured JSON:** [`9b2c1dd2719a6c8a095c.json`](../../sessions/9b/9b2c1dd2719a6c8a095c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态 (09:51 UTC)

| GPU | Utilization | Memory Used | Running |
|-----|-------------|-------------|---------|
| 0 | 76% | 33.4/97.9 GB | ds_imp_s025 |
| 1 | 77% | 33.9/97.9 GB | ds_rand_s025 |
| 2 | 96% | 34.1/97.9 GB | qw_imp_s025 |
| 3 | 98% | 34.7/97.9 GB | qw_rand_s025 |

### 实验进度

| Model | Condition | s015 | s020 | s025 | s030 | ETA (s030 完成) |
|-------|-----------|------|------|------|------|----------------|
| DeepSeek | imp | ✓ 500 | ✓ 500 | **334/500** | queued | ~15:40 UTC |
| DeepSeek | rand | ✓ 500 | ✓ 500 | **382/500** | queued | ~15:15 UTC |
| Qwen | imp | ✓ 500 | ✓ 500 | **496/500** | queued | ~13:25 UTC |
| Qwen | rand | ✓ 500 | ✓ 500 | **477/500** | queued | ~13:25 UTC |

### 数据完整性

- s015/s020 全部 8 个 condition：**已验证，每个 500 problems，无 error/traceback**
- 输出格式：`profiling_results.json`（dict with 8 keys，含 `per_problem_ii` 等）
- s025 运行中日志无异常

### 关键时间点

- **Qwen s025 完成** → ~10:00 UTC（几分钟内），自动启动 s030
- **DeepSeek s025 完成** → ds_rand ~10:53 UTC, ds_imp ~11:17 UTC，自动启动 s030
- **全部实验完成** → ~15:40 UTC（约 6 小时后）

### 异常告警

无。所有进程正常运行，脚本串行逻辑正确，s030 会自动启动。

---
