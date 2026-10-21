# ops db sweep status check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_db-sweep-status-check_20260516T205953_result.json`
- **Structured JSON:** [`5f6f7882a949186ff368.json`](../../sessions/5f/5f6f7882a949186ff368.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已齐。汇总如下：

---

## d_b Sweep 状态 (2026-05-17 05:00 UTC)

| d_b | 状态 | 进度 | 关键 Metrics |
|-----|------|------|-------------|
| **64** | **完成** (train + eval) | 1000/1000 | final_loss=0.361, final_sparsity=0.484, **WikiText-2 PPL=10.158** |
| **256** | **训练中** | ~500/1000 | 当前 loss≈0.236, sparsity≈0.480 |
| **512** | **未开始** | — | 等 d_b=256 完成后自动启动 |

**详细说明**:
- GPU 0 在跑 d_b=256 (PID 265221, 100% utilization, 66GB VRAM)
- d_b=64 的 eval 结果已保存：`results/benchmark/db_sweep_64/results.json`
- d_b=256 训练从 04:41 开始，d_b=64 用了约 36 分钟（04:05→04:41），预计 d_b=256 约 05:20 完成训练，加上 eval 约 05:22
- d_b=512 预计 ~06:00 全部结束

**d_b=64 final step metrics** (Step 1000): loss=0.361, kl_norm=0.361, sparsity=0.484, lambda=1000, tau=0.100

---
