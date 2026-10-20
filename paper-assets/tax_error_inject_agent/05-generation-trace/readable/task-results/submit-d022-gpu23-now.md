# submit d022 gpu23 now

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_d022-gpu23-now_20260515T101304_result.json`
- **Structured JSON:** [`371d438a03d0463aa3ff.json`](../../sessions/37/371d438a03d0463aa3ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 2,3 — Random inject50 训练完成，TaxEI eval 已提交

| 实验 | 状态 | train_loss | token_acc | 运行时间 |
|------|------|-----------|-----------|---------|
| v4-random-fixed-inject50-s0 | **完成** ✓ | 0.4355 | 0.911 | 53m 29s |
| v4-random-fixed-inject50-s123 | **完成** ✓ | 0.257 (final) | 0.911 | 54m 17s |

**TaxEI inject50 eval 已提交：**
- `v4-taxei-fixed-inject50-s0-eval` → GPU 2, PID 138210
- `v4-taxei-fixed-inject50-s123-eval` → GPU 3, PID 138352

### GPU 0,1 — Random inject25 训练进行中

| 实验 | 进度 | 剩余时间 |
|------|------|---------|
| v4-random-fixed-inject25-s0 | 1300/1635 (79.5%) | ~11m 32s |
| v4-random-fixed-inject25-s123 | 1295/1635 (79.2%) | ~11m 43s |

预计 ~12 分钟后完成。

---
