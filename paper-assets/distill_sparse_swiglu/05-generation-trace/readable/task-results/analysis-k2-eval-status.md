# analysis k2 eval status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k2_eval_status_20260523T063719_result.json`
- **Structured JSON:** [`cfe21640edea2a6ae2b2.json`](../../sessions/cf/cfe21640edea2a6ae2b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## K=2 实验状态

**Eval 仍在运行中**，GPU 1 (98% utilization, 66GB VRAM)。

### 进度
| 阶段 | 状态 |
|------|------|
| WikiText-2 PPL | **完成**: 10.7958 |
| arc_challenge (25-shot) | **完成** |
| winogrande + mmlu (5-shot) | **完成** |
| gsm8k (8-shot) | **完成** |
| hellaswag (10-shot) | **进行中**: 1129/40168 (~3%), ~36min |
| piqa | **未开始**, ~4min |

**预计完成时间**: ~40 分钟后

### 训练状态
训练已完成 (EXIT_CODE=0)，checkpoint: `/root/distill_sparse_swiglu/checkpoints/perlayer_kl_k2_s42/predictor_perlayer_kl_k4.pt`

---

## K-curve 对比（已有数据, 30% sparsity, TEAL uniform）

| Metric | Dense | K=2* | K=4 | K=8 | K=16 |
|--------|-------|------|-----|-----|------|
| **WikiText-2 PPL** ↓ | 6.12 | **10.80** | 8.89 | 8.97 | **8.67** |
| ARC-C (acc_norm) ↑ | 58.28 | — | 40.96 | 41.04 | 41.04 |
| WinoGrande (acc) ↑ | 78.06 | — | 66.69 | 67.40 | 68.43 |
| MMLU (acc) ↑ | 65.27 | — | 43.53 | 39.80 | 44.03 |
| GSM8K (em) ↑ | 48.75 | — | 5.16 | 5.61 | 8.11 |
| HellaSwag (acc_norm) ↑ | 82.35 | — | 68.49 | 69.19 | 69.63 |
| PIQA (acc_norm) ↑ | 80.90 | — | 73.99 | 76.12 | 75.90 |

\* K=2 downstream tasks 仍在运行，PPL 已确认为 10.80（teal_global 模式）。

### 关键观察
- K=2 PPL (10.80) 显著高于 K=4 (8.89)，差距 +1.91
- K=4/K=8/K=16 的 PPL 差异很小 (8.67–8.97)，但 K=16 在 downstream tasks 全面领先
- K=2 是明显的拐点——predictor 容量不足以捕获 sparsity pattern

**不更新 registry**——eval 未完成。建议 ~40 分钟后再次检查提取最终结果。

---
