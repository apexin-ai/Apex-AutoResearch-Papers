# ops check d100 eval results

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_d100_eval_results_20260514T020912_result.json`
- **Structured JSON:** [`02a8fbc0e47e574149e4.json`](../../sessions/02/02a8fbc0e47e574149e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### d100 eval — 仍在运行，未完成

- 结果目录为空，尚无 `eval_results.json`
- 日志显示：MMLU 已完成，当前 GSM8K 进度 **27% (359/1319)**，速度 ~5.5s/it
- 剩余 GSM8K 约 88 min，之后还有 arc_challenge + humaneval
- 预计还需 **2-3 小时**

**注意：d100 有两个进程同时在跑同一个 eval，写同一个输出目录**：
| PID | GPU | Elapsed |
|-----|-----|---------|
| 255703 | 默认 | 40 min |
| 256509 | cuda:4 | 37 min |

这可能导致结果文件冲突或覆盖。

### d000_s42 eval — 仍在运行

- PID 257034，cuda:2，已运行 35 min
- 结果目录为空，尚无产出

---
