# eval acts2 ckpt5000 scp eval

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_acts2-ckpt5000-scp-eval_20260522T184657_result.json`
- **Structured JSON:** [`eb9189d9607dad2cb627.json`](../../sessions/eb/eb9189d9607dad2cb627.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成！结果如下：

## exp-004-act-baseline-s2 checkpoint-5000 评估结果

| 指标 | 值 |
|------|-----|
| **SYCONScore** | **0.2480** |
| **ToF** | 0.1436 |
| **NoF** | 0.9061 |
| Samples | 362 (valid=181, invalid=181) |
| 耗时 | 1940s |

## vs Vanilla baseline

| | SYCONScore | 比较 |
|---|---|---|
| Vanilla | 0.1335 | - |
| **ACT s2 ckpt-5000** | **0.2480** | **+0.1145 (+85.8%)** |

**SYCONScore > vanilla：是** — 从 0.1335 提升到 0.2480，相对提升 85.8%。

## 当前训练状态

westd-29046 上 exp-004-act-baseline-s2 训练在 **step 5360/8000**，sft_loss ~3e-06，total_loss ~0.000116。

---
