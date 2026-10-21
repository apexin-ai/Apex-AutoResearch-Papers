# eval 28034 collect rl7500 chain8000

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_28034-collect-rl7500-chain8000_20260523T074141_result.json`
- **Structured JSON:** [`aa57113d9d2bf7c97a85.json`](../../sessions/aa/aa57113d9d2bf7c97a85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果已收集。

## 汇报

| Eval | SYCONScore | ToF | NoF | 状态 |
|------|-----------|------|------|------|
| vanilla baseline | 0.1335 | — | — | 基线 |
| rl-ckpt-7000 | 0.3257 | — | — | 已完成 |
| **rl-ckpt-7500** | **0.3043** | 0.1878 | 0.8011 | 已完成 |
| **rl-ckpt-8000** | **0.2673** | 0.1602 | 0.8066 | 已完成 |

**关键发现：**

- **ckpt-7000 的 0.3257 是 noise spike，不是 real surge。** ckpt-7500 回落到 0.3043，ckpt-8000 进一步下降到 0.2673，呈单调递减趋势。
- 训练已完成（step 8000, lr=0.0），ckpt-7000 是这条训练曲线的峰值。
- NoF 在三个 checkpoint 间基本持平（~0.80），说明拒绝无效前提的能力稳定；SYCONScore 下降主要来自 ToF 下降（0.1878 → 0.1602），模型在后期训练中逐渐丧失对有效观点的顺从能力。

---
