# monitor training progress check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training_progress_check_20260514T185749_result.json`
- **Structured JSON:** [`815f7583197b28e9b8d8.json`](../../sessions/81/815f7583197b28e9b8d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/training_progress_check_20260514.md`。

**摘要：**

**exp_008e_v3_s1** (Crown Jewel C6 seed 1)：刚启动 ~9 分钟，仅到 step 5K/105K (4.8%)。eval_return=31，value 几乎为零，太早无法评估 v/e 或 delusional critic。gate_dt_mean=1.0 符合 fixed dt=1 配置。预计 4-5 小时后完成。建议 1 小时后再查。

**exp_009a_baseline_s2**：运行 9.4 小时，step 235K/500K (47%)。eval_return=914.8，峰值 956.0@215K 已超 exp_001 最终水平 (~950)。v/e=0.725，无 value overestimation。fps=7.67 稳定。预计 ~9.4 小时后完成。训练一切正常。

---
