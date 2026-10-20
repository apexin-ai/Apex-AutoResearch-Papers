# monitor c2 n500 progress check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_c2_n500_progress_check_20260515T025552_result.json`
- **Structured JSON:** [`c23a7bdb1db87476fc42.json`](../../sessions/c2/c23a7bdb1db87476fc42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

### DeepSeek（gpu0 + gpu1）

| Condition | 进度 | 状态 |
|-----------|------|------|
| ds_imp_s015 | 500/500 | ✅ 完成 |
| ds_imp_s020 | 500/500 | ✅ 完成 |
| ds_imp_s025 | ~461/500 | 🔄 运行中 (gpu0) |
| ds_imp_s030 | 0/500 | ⏳ 未开始（目录不存在）|
| ds_rand_s015 | 500/500 | ✅ 完成 |
| ds_rand_s020 | 500/500 | ✅ 完成 |
| ds_rand_s025 | 500/500 | ✅ 完成 |
| ds_rand_s030 | ~5/500 | 🔄 运行中 (gpu1，刚启动) |

### Qwen（gpu2 + gpu3）

| Condition | 进度 | 状态 |
|-----------|------|------|
| qw_imp_s015 | 500/500 | ✅ 完成 |
| qw_imp_s020 | 500/500 | ✅ 完成 |
| qw_imp_s025 | 500/500 | ✅ 完成 |
| qw_imp_s030 | ~152/500 | 🔄 运行中 (gpu2) |
| qw_rand_s015 | 500/500 | ✅ 完成 |
| qw_rand_s020 | 500/500 | ✅ 完成 |
| qw_rand_s025 | 500/500 | ✅ 完成 |
| qw_rand_s030 | ~134/500 | 🔄 运行中 (gpu3) |

**总结**：12/16 conditions 已完成，4 个正在运行。`ds_imp_s030` 尚未开始（排在 gpu0 的 `ds_imp_s025` 之后）。按当前速度估算，`ds_imp_s025` 约 30 分钟内完成；`ds_rand_s030`/`qw_imp_s030`/`qw_rand_s030` 预计还需 3-4 小时。

---
