# analysis prepare val sweep compilation

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_prepare-val-sweep-compilation_20260515T220241_result.json`
- **Structured JSON:** [`ed6f43e8edf142c4a1ef.json`](../../sessions/ed/ed6f43e8edf142c4a1ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 已注册。总结：

**Val sweep 覆盖度**

| 区间 | 数据点数 | 状态 |
|------|---------|------|
| ckpt-200, 400 | 2 | 原始训练数据，不在 resume 范围内 |
| ckpt-600 | 1 | resume 起点 = 原始 ckpt-600（相同权重），可直接复用 |
| ckpt-800→1600 | 5 | 仅有原始训练 val 数据，resume checkpoint 存在但未评估 |
| ckpt-1800→5800 | 21 | 正在跑（2 GPU 并行），预计 ~May 16 05:00-10:00 UTC |

**完成后的 resume val curve 完整性**
- **确认可用**：22 点（ckpt-600 + ckpt-1800→5800）
- **需验证**：5 点（ckpt-800→1600）— 原始数据可作 proxy，但 resume 可能因环境差异（conda→resume env）或 CUDA 非确定性产生偏差
- **建议**：sweep 完成后 spot-check resume ckpt-1000 val acc，若与原始 88.23% 偏差 <0.5pp，则全部 5 个 overlap 点可直接复用

**关键风险**：resume 训练 epoch 2 后严重过拟合（best resume eval_loss 在 ckpt-4200），val accuracy peak 可能从原始 ckpt-1000 偏移。

---
