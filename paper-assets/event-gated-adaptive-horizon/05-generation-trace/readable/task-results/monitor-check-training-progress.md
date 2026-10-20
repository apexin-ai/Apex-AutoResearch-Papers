# monitor check training progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_check_training_progress_20260516T014042_result.json`
- **Structured JSON:** [`f84558c830863a61bae6.json`](../../sessions/f8/f84558c830863a61bae6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇报

### exp_009d_baseline_walker_s0 (cuda:0, PID 149708)

| 指标 | 值 |
|------|------|
| 当前 step | **312,000** / 500,000 (62.4%) |
| 最新 eval_return | **925.86** (@ 308K) |
| FPS | 7.24 |
| 已运行 | 13h16m |
| 剩余 steps | 188,000 |
| 预估剩余时间 | **~7.2h** (约 UTC 今晚完成) |

趋势：eval_return 持续上升（228K→692, 268K→705, 288K→846, 308K→926），表现良好。

---

### exp_010a_cheetah_baseline_s1 (cuda:1, PID 536890)

| 指标 | 值 |
|------|------|
| 当前 step | **116,000** / 512,000 (22.7%) |
| 最新 eval_return | **546.73** (@ 115K) |
| FPS | 11.63 |
| 已运行 | 2h53m |
| 剩余 steps | 396,000 |
| 预估剩余时间 | **~9.5h** (约 UTC 明早完成) |

趋势：eval_return 在 115K 跳升至 547（之前 85K-105K 在 390-420 区间震荡），有起色。

---

两个实验均正常运行，无异常。

---
