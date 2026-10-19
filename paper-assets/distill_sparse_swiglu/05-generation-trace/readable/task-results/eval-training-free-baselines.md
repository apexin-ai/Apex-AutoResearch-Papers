# eval training free baselines

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_training_free_baselines_20260515T180055_result.json`
- **Structured JSON:** [`0bddbaacf115f8c23cca.json`](../../sessions/0b/0bddbaacf115f8c23cca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完整结果

### WikiText-2 PPL @ 50% Sparsity (LLaMA-3.1-8B)

| Method | PPL | Model Sparsity |
|---|---|---|
| **Dense (baseline)** | **6.12** | 0% |
| **TEAL Greedy** | **50,035** | 50.0% |
| **Vanilla TEAL** | **66,036** | 49.9% |
| **R-Sparse** (rank=256) | **74,929** | 50.0% |
| **WINA** | **82,567** | 50.0% |

### Per-layer Sparsity 分布特征

四个 baseline 呈现相同模式：
- **Layer 0-5**: 几乎完全 sparse (95-100%)
- **Layer 6-15**: 中等 sparsity (50-95%)
- **Layer 16-23**: 轻度 sparse (2-50%)
- **Layer 24-31**: 完全 dense (0%)

TEAL Greedy 稍好是因为 greedy allocation 基于 reconstruction error，但仍然把前层 prune 得太狠。WINA 和 R-Sparse 虽然引入了 weight-aware scoring，但 global topk 分配仍导致相同的结构性问题。

### 关键结论

所有 training-free baseline 在 50% sparsity 下完全崩溃（PPL 50k-83k vs Dense 6.12）。根因：global allocation 系统性地 over-prune 前层 MLP，而这些层对模型输出至关重要。这为 distillation-based 方法提供了强有力的 motivation——需要通过训练学习 per-layer allocation 来避免灾难性退化。

---
