# submit exp 002 signals 3B v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_exp_002_signals_3B_v2_20260515T155701_result.json`
- **Structured JSON:** [`7e4649568d8828fa9f88.json`](../../sessions/7e/7e4649568d8828fa9f88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**全部 6 张 GPU 均被占用，都在跑 exp001 评估任务：**

| GPU | PID | 运行时间 | 任务 |
|-----|-----|---------|------|
| 0 | 566224 | 2h16m | 1.5B d005_s123 aligned eval |
| 1 | 566311 | 2h16m | 1.5B d025_s123 aligned eval |
| 2 | 580698 | 52m | 3B d005_s123 aligned eval |
| 3 | 576735 | 1h07m | 3B d025_s123 aligned eval |
| 4 | 584233 | 24m | 3B d005_s123 para_aligned eval |
| 5 | 584315 | 24m | 3B d025_s123 para_aligned eval |

GPU 0/1 上的 1.5B 评估已跑 2h+，可能最先完成。GPU 4/5 才跑 24 分钟，短期不会空出。

按 C001 约束，无法在有进程的 GPU 上提交。需要等某张 GPU 空闲后再提交 exp_002_signals_3B_v2。

要我等 GPU 0 或 1 空闲后自动提交，还是你想手动指定？

---
