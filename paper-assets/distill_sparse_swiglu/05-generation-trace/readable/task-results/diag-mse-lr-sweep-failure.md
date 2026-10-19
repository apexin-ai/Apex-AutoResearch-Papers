# diag mse lr sweep failure

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_mse_lr_sweep_failure_20260524T111454_result.json`
- **Structured JSON:** [`7b37c0b88728ad0cd838.json`](../../sessions/7b/7b37c0b88728ad0cd838.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**两个实验都没有失败——均正常跑完 1000/1000 步并保存了 checkpoint 和 eval 结果。**

## 实验结果

| 实验 | LR | 最终 MSE | 最终 Sparsity | Lambda | WikiText-2 PPL | 状态 |
|------|-----|---------|---------------|--------|---------------|------|
| mse30_lr2e4_s42 | 2e-4 | 0.000422 | **0.188** | **1000.0 (cap)** | **15.17** | Lagrangian 爆炸 |
| mse30_lr1e4_s42 | 1e-4 | 0.001531 | **0.309** | 0.01 | **17.50** | 正常收敛 |

## 分析

**mse30_lr2e4_s42** 有严重的 Lagrangian 不稳定问题：
- lambda 从 1.0 飙升到 1000.0（cap），说明 sparsity 始终无法满足 target=0.30 的约束
- 最终 sparsity=0.188，远低于目标 0.30——模型过度稀疏
- constraint 项 (7.8125~8.5625) 完全压倒 MSE 项 (0.0004)，优化已脱轨
- 尽管 PPL 数字更好 (15.17)，但这是因为 sparsity 远低于目标，不是公平对比

**mse30_lr1e4_s42** 行为正常：
- sparsity 稳定收敛到 0.309，接近 target 0.30
- constraint=0.000，lambda 保持 0.01
- PPL=17.50

## 环境状态

- **GPU**: 两块 RTX PRO 6000 (98GB)，当前空闲 (0 MiB used)
- **磁盘**: 根分区 30G 用了 23G (74%)，剩余 7.9G
- **Checkpoints**: 两个实验均已保存在 `/root/distill_sparse_swiglu/checkpoints/mse30_lr{2e4,1e4}_s42/`

## 结论

不存在进程级失败。如果你指的"失败"是 mse30_lr2e4_s42 的 Lagrangian 发散，根因是 LR=2e-4 过高导致 predictor 学得太快、sparsity 过早坍缩到远低于 target 的水平，lambda 被持续推高至 cap。可能的修复：降低 lambda growth rate、提高 cap、或用更保守的 LR（1e-4 版本已证明可行）。环境具备立即重跑条件。

---
