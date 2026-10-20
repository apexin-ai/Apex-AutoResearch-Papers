# restart exp 002 signals

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_restart_exp-002-signals_20260514T125545_result.json`
- **Structured JSON:** [`1e315ff99dd3c987eead.json`](../../sessions/1e/1e315ff99dd3c987eead.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：GPU 0 已被占用，不能提交新任务。**

状态汇总：

### GPU 0 确认空闲：❌

GPU 0 已有 exp-002 batch runner 在运行：
- **PID 370957** (`run_batch.py --model-size 0.5B --gpu 0`)，子进程 **PID 370959** (`compute_signals.py` d000_s42/mmlu)
- 启动时间：20:55:17，手动从 tmux session `exp_001_sft_0pct_05B` 里通过 `tee run_05B.log` 启动（非 submit_training_job）
- 当前在跑 [1/9] `Qwen2.5-0.5B_d000_s42/mmlu`，占 13390 MiB 显存

### 代码修复确认：✅
- `max_answer_tokens=64` ✅
- `timeout=14400` (4h) ✅  
- `_load_cached_signal` per-signal 缓存 ✅

### 已有 cached signals（会被自动跳过）：
| checkpoint | signal | benchmarks |
|---|---|---|
| d000_s42 | embedding | mmlu, gsm8k, arc_challenge |
| d000_s42 | minkpp | mmlu, gsm8k |
| d005_s42 | embedding | mmlu |

缺失：d000 minkpp_arc_challenge + 全部 selfcritique，d005/d100 大部分。

### 操作
**根据 C001 约束，GPU 0 已有同类进程，不提交新任务。** 当前进程正在用修复后的代码跑，无需干预。建议等当前任务完成后检查日志确认 selfcritique 是否成功（前一轮 18:19 的运行 selfcritique 全部失败导致 task-level FAIL）。

---
