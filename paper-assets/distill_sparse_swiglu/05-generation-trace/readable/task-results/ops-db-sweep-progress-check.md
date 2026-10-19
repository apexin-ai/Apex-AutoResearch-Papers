# ops db sweep progress check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_db-sweep-progress-check_20260516T210334_result.json`
- **Structured JSON:** [`5ece88d3822ca0df03b0.json`](../../sessions/5e/5ece88d3822ca0df03b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## d_b Sweep 进度报告

| d_b | 状态 | PPL (wikitext2) |
|-----|------|-----------------|
| **64** | 完成（训练+评估） | **10.158** |
| **256** | 训练中，Step 610/1000 | 待评估 |
| **512** | 未开始 | — |

### 当前 GPU 状态
- GPU 0: 100% 利用率，66GB/98GB VRAM，正在跑 d_b=256 训练
- GPU 1: 空闲

### d_b=256 训练趋势
- Loss 从 step 1 的 ~1.19 稳步下降到 step 610 的 ~0.24
- Sparsity 稳定在 ~0.48-0.50，目标约束满足良好
- Lambda 基本稳定在 1000

### 预计完成时间
- d_b=64: 1000 steps 约 30 min → ~1.8 sec/step
- d_b=256: 610 steps 用了约 22 min → ~2.2 sec/step，剩余 390 steps ≈ 14 min + eval 6 min → **约 05:23 完成**
- d_b=512: 预计 ~45 min 训练 + 6 min eval → **约 06:14 完成**
- **全部完成预计：~06:15 CST（约 1 小时后）**

---
