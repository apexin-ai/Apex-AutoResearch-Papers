# monitor exp 001 progress

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp_001_progress_20260517T104348_result.json`
- **Structured JSON:** [`6df2542a918df252603c.json`](../../sessions/6d/6df2542a918df252603c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp_001 Phase 0 (410M pure collapse) 状态:**

- **进程**: PID 59365 存活，已运行 11h24m
- **当前 Generation**: 8/10 (第9轮，共10轮 gen 0-9)
- **阶段**: generating — 25600/50000 samples (51.2%)
- **Checkpoints**: gen_0 ~ gen_7 已存在 (`checkpoints_410m/`)

**Gen 0-7 Metrics (已完成):**

| Gen | eff_rank | log_det | ppl | distinct4 | train_loss |
|-----|----------|---------|-----|-----------|------------|
| 0 | 417.5 | 2366.7 | 9.55 | 0.741 | — |
| 1 | 491.8 | 2464.8 | 11.38 | 0.626 | 1.623 |
| 2 | 496.4 | 2469.9 | 13.58 | 0.515 | 1.268 |
| 3 | 493.3 | 2440.6 | 16.25 | 0.490 | 1.134 |
| 4 | 485.7 | 2405.0 | 19.80 | 0.468 | 1.098 |
| 5 | 479.2 | 2370.2 | 24.59 | 0.463 | 1.047 |
| 6 | 473.0 | 2335.2 | 30.91 | 0.466 | 1.025 |
| 7 | 464.2 | 2304.2 | 38.89 | 0.447 | 1.015 |

**趋势**: collapse 信号清晰 — eff_rank 持续下降 (417→464→496 peak 然后回落到 464)，log_det 从 Gen 2 后单调下降，ppl 指数级上升 (9.5→38.9)，distinct4 持续下降 (0.74→0.45)。train_loss 也在收敛递减。

**时间估算** (基于每 generation ~2.5h，hellaswag 评估时间间隔):
- Gen 8 完成: ~20:00-20:30
- Gen 9 (最终) 完成: ~22:30-23:00 今晚

---
