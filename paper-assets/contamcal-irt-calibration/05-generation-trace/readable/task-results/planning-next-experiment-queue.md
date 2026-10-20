# planning next experiment queue

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_planning_next-experiment-queue_20260516T022325_result.json`
- **Structured JSON:** [`8c79525f770b888dc0f0.json`](../../sessions/8c/8c79525f770b888dc0f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

队列计划已写入 `artifacts/next_experiment_queue.md`，包含 7 个优先级排序的任务：

| 优先级 | 触发条件 | 任务 | exp_id |
|--------|---------|------|--------|
| 1 | cuda:0 释放 | **d100_s42 eval batch** (aligned+para) | exp_001_eval_3B_d100_s42_a32_v3_batch |
| 2 | cuda:1 释放 | d000_s42 signals (s1+s2+s4) | exp_002_signals_3B_d000_s42 |
| 3 | cuda:2 释放 | d005_s42 signals | exp_002_signals_3B_d005_s42 |
| 4 | cuda:3 释放 | d025_v3_s42 remaining signals | exp_002_signals_3B_d025_v3_s42_remaining |
| 5 | d100_s42 eval 完成后 | d100_s42 signals | exp_002_signals_3B_d100_s42 |
| 6 | cuda:4 释放 | d100_s123 signals recovery (if v9 有缺口) | exp_002_signals_3B_d100_s123_v10 |
| 7 | 任意空闲 GPU | 0.5B s123 signals 重跑 (inline cmd 修复 127) | exp_002_signals_05B_s123_v2 |

每个任务都包含完整的 `bash -c` 命令（显式 `CUDA_VISIBLE_DEVICES`、`HF_DATASETS_OFFLINE=1`）、C001/C002/C004/C006 前置检查项、hypothesis 文本和 registry 字段。d100_s42 eval 是最高优先级，因为它是 d100_s42 signals 的前置依赖。

---
