# ops check exp progress

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-exp-progress_20260523T131535_result.json`
- **Structured JSON:** [`5c3d104986a218a1fcc8.json`](../../sessions/5c/5c3d104986a218a1fcc8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在运行。

---

## exp_019 — fixed_mix r=0.2, seed44
- **状态**: 运行中 (PID 757601, 100% CPU)
- **已跑**: 9h+ (12:08 启动)
- **当前进度**: gen 0–4 完成 (eval + 4 个训练周期), 共需 10 个训练周期
- **Metrics** (已完成的 gen):

| Gen | eff_rank | log_det | PPL | distinct-4 |
|-----|----------|---------|-----|-----------|
| 0 | 417.5 | 2366.7 | 9.55 | 0.730 |
| 1 | 476.6 | 2369.4 | 10.28 | 0.654 |
| 2 | 483.2 | 2361.1 | 10.73 | 0.562 |
| 3 | 486.5 | 2365.6 | 11.14 | 0.469 |
| 4 | 489.2 | 2377.1 | 11.50 | 0.399 |

- **预估剩余**: ~2.25h/cycle × 6 cycles ≈ **13.5h**, ETA ~明天 10:40 (+0800)

---

## exp_020 — GPT-2-medium pure_collapse, seed42
- **状态**: 运行中 (PID 783957, 100% CPU)
- **已跑**: 2.5h+ (18:43 启动)
- **当前进度**: gen 0–1 完成, gen 2 数据生成阶段 (2880/50000 ≈ 5.8%), 共需 10 个训练周期
- **Metrics** (已完成的 gen):

| Gen | eff_rank | log_det | PPL | distinct-4 |
|-----|----------|---------|-----|-----------|
| 0 | 23.1 | 689.4 | 15.45 | 0.913 |
| 1 | 155.2 | 885.3 | 16.42 | 0.891 |

- **预估剩余**: ~2.5h/cycle × 9 cycles ≈ **22.5h**, ETA ~明天 17:00 (+0800)

---
