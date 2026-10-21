# analysis kl only seeds

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_kl_only_seeds_20260515T175825_result.json`
- **Structured JSON:** [`11483e3d27b1b0d3a6d1.json`](../../sessions/11/11483e3d27b1b0d3a6d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成分析并更新 registry 为 DONE。

## 汇总

### 训练结果
| | kl_only_s0 (seed=0) | kl_only_s1 (seed=1) |
|---|---|---|
| 训练步数 | 1000/1000 | 1000/1000 |
| 最终 loss | 0.305 | 0.332 |
| 最终 sparsity | 0.488 | 0.484 |
| lambda/tau | 1000/0.100 | 1000/0.100 |

### 评估结果 (WikiText-2, sparsity_target=50%)
| | s0 | s1 | s42 | s123 | s456 |
|---|---|---|---|---|---|
| true_dense | 6.12 | 6.12 | - | - | - |
| Dense PPL | 9.19 | 9.15 | 9.21 | 9.25 | 9.14 |
| Sparse PPL | 12.03 | 11.99 | 12.08 | 11.91 | 13.58 |
| PPL increase | 30.9% | 31.0% | 31.2% | 28.8% | 48.6% |

### 5-seed Headline
- **Sparse PPL: 12.32 ± 0.71** (5-seed)
- 排除 s456 异常值后: **12.00 ± 0.07** (4-seed)
- Dense PPL: **9.19 ± 0.04** (极度稳定)
- s0 和 s1 与 s42/s123 高度一致，s456 仍为唯一异常值
- 结论: 两个实验均 **success**

---
