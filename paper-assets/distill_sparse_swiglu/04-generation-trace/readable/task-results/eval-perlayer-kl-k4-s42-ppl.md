# eval perlayer kl k4 s42 ppl

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_perlayer_kl_k4_s42_ppl_20260522T113248_result.json`
- **Structured JSON:** [`8198b8bf925fad70b96a.json`](../../sessions/81/8198b8bf925fad70b96a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已经完成，registry 里已有结果。

## K=4 Per-layer KL PPL 结果

| 方法 | WikiText-2 PPL | Δ vs K=1 |
|------|---------------|----------|
| K=1 per-layer KL | 9.05 | — |
| **K=4 per-layer KL** | **8.8932** | **-0.157** |
| E2E KL | 8.81 | -0.24 |

**关键判断**：K=4 PPL = 8.89，落在 K=1 (9.05) 和 E2E KL (8.81) 之间，距 E2E KL 仅差 0.08。

这属于第一种情况：**K=4 大幅缩小了 mismatch**。增加同时激活的层数从 1→4，per-layer KL 已经接近 E2E KL 表现。说明 K=1 的 PPL 劣势主要来自 train-inference mismatch（训练时只看 1 层，推理时全部层同时激活），而非 per-layer KL 目标本身的根本缺陷。

**对叙事的影响**：
- coupling claim 需要弱化 — K=4 证明 mismatch 是可修复的
- 但 K=4 仍未完全追平 E2E KL（差 0.08），说明残余 gap 可能来自跨层交互效应
- Registry 标记 conclusion=negative，符合预期（对 "mismatch 不可修复" 假设是 negative evidence）

---
