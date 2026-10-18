# ops harvest l2norm k09 s43 cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-l2norm-k09-s43-cqa1_20260527T180531_result.json`
- **Structured JSON:** [`e869f590099c891f2c86.json`](../../sessions/e8/e869f590099c891f2c86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验完成，registry 已更新。**

**eval_pi05_l2norm_k09_long_seed43_strict_cqa1** — π0.5 L2norm k=0.9 Long seed43

- **Overall SR: 81.2%**（seed42 为 80.0%，差 1.2pp，稳定性良好）
- Per-task: T0=92, T1=96, T2=92, T3=100, T4=88, T5=96, **T6=12**, T7=86, T8=60, T9=90
- 运行时间：~218 min（约 3.6h）
- T6 依然是瓶颈（12%），与 seed42 一致

---
