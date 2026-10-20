# ops c2 qw n500 r3 cron check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c2_qw_n500_r3_cron_check_20260514T193048_result.json`
- **Structured JSON:** [`1b2e7ccc969534c18970.json`](../../sessions/1b/1b2e7ccc969534c18970.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总结

**进程活着，又是 cron 误判。**

### Qwen c2 进程 (GPU2/3)
| GPU | PID | Condition | 进度 | 状态 |
|-----|-----|-----------|------|------|
| GPU2 | 159269 | qw_imp_s020 | **67/500** | 运行中 |
| GPU3 | 159794 | qw_rand_s020 | **48/500** | 运行中 |

Screen sessions `c2_qw_gpu2` (PID 131857) 和 `c2_qw_gpu3` (PID 131995) 都在。

### 8 Conditions 完成情况
| Condition | 状态 |
|-----------|------|
| qw_imp_s015 | **DONE** (profiling_results.json 18.7MB, 03:02完成) |
| qw_rand_s015 | **DONE** (profiling_results.json 18.7MB, 03:11完成) |
| qw_imp_s020 | **运行中** 67/500 |
| qw_rand_s020 | **运行中** 48/500 |
| qw_imp_s025 | 未开始（目录不存在） |
| qw_rand_s025 | 未开始 |
| qw_imp_s030 | 未开始 |
| qw_rand_s030 | 未开始 |

s020 输出目录虽然存在但内容为空——profiling 数据看起来只在完成整个 condition 后一次性写入 profiling_results.json。

另外 GPU0/1 上还在跑 DeepSeek 的 ds_imp_s020 (PID 156554) 和 ds_rand_s020 (PID 154305)。

---
