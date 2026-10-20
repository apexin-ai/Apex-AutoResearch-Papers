# ssh eval sft s44 r3 and check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval-sft-s44-r3-and-check_20260515T132932_result.json`
- **Structured JSON:** [`2c13126b75ff045fe18f.json`](../../sessions/2c/2c13126b75ff045fe18f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总报告：

---

## s44-r3 eval_sta 结果

| 指标 | s42 | s43 | **s44** |
|------|-----|-----|---------|
| n_proved | 13 | 11 | **15** |
| prove_rate | 0.13 | 0.11 | **0.15** |
| mean_isr | 0.0738 | 0.0699 | **0.0884** |
| isr_std | 0.2077 | 0.2155 | **0.2268** |
| proved_only_mean_isr | 0.5677 | 0.6352 | **0.5892** |

**按 answer_type 分组 (s44)**:
| type | count | proved | prove_rate | mean_isr |
|------|-------|--------|------------|----------|
| true | 34 | 15 | 44.1% | 0.260 |
| false | 25 | 0 | 0% | 0.0 |
| unknown | 41 | 0 | 0% | 0.0 |

**注意**: eval_sta_results.json 中**没有** h7/h1/h8/genuine 指标。三个 seed 的 eval 结果格式一致，均无此类字段。用户提到的 "genuine=92.3%/90.9%" 可能来自其他评估管道。

s44 是三个 seed 中最好的（prove_rate 15% vs 13%/11%），但差异在随机波动范围内。

---

## exec-only s43-1000 训练进度

- 当前 step: **79 / 1000** (7.9%)
- 已用时间: ~11:53
- 速度: ~8-9 s/step
- 预计剩余: **~2h17m**（约 23:50 完成）

---

## 额外发现

cuda:1 上除了 eval（已完成），还有一个 **plan001-exec-only-s44-1000** 训练（PID 357079），使用 `--seed 44 --output_dir plan001_exec_only_s44_1000`。这不在你提供的任务列表中——可能是另一个 worker 启动的。

---
