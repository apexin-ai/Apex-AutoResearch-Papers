# monitor actual progress 17855 v2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_actual-progress-17855-v2_20260521T221331_result.json`
- **Structured JSON:** [`a64b3f5948858769d8c6.json`](../../sessions/a6/a64b3f5948858769d8c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 6 experiments have active python processes, no exit files.

```
t25_a045_s42_fp32: gen 22/25 | RUNNING | 最早启动，进度最快
t25_a060_s42_fp32: gen  8/25 | RUNNING | 正在 gen_7 生成合成数据
t25_a050_s42_fp32: gen  8/25 | RUNNING | 03:32 启动
t20_a060_s43_fp32: gen  8/20 | RUNNING | 03:32 启动
t15_a060_s43_fp32: gen 10/15 | RUNNING | 02:42 启动
t15_a045_s43_fp32: gen  8/15 | RUNNING | 正在 gen_8 训练中 (4800/5000 steps, 97%)
```

6/6 全部存活运行中。t25_a045 接近完成（还剩 3 gen），t15_a060 也过半（10/15）。其余 4 个在 ~40% 进度。

---
