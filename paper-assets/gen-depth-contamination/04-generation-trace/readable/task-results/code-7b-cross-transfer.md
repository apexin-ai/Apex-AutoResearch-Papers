# code 7b cross transfer

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_7b_cross_transfer_20260524T084729_result.json`
- **Structured JSON:** [`00a0db3e0495d84b0b3a.json`](../../sessions/00/00a0db3e0495d84b0b3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。以下是结果汇总：

## 产出

**脚本**: `scripts/run_7b_cross_transfer_v2.py` on cqa1-22115
**结果**: `results/7b_cross_transfer_v2/cross_transfer_7b_full_metrics.json`
**GPU**: 不需要，纯 CPU 任务
**运行时间**: ~90 秒（5K docs, 2×2 matrix）

## 数据说明

- **exp-004 (Qwen2.5-7B, 5K)** 原始数据在 westc-26893，不在 cqa1-22115。使用 `exp_qwen_cont_10k`（10K 版本）子采样到 5K docs
- **exp-018 (LLaMA-3.1-8B, 5K)** 直接使用 `data/exp_018_llama8b/features.csv`
- 两者均为 Qwen2.5-1.5B cross-scoring，15D features

## 2×2 Transfer Matrix

| Metric | Train\Test | Qwen2.5-7B | LLaMA-3.1-8B |
|--------|-----------|------------|--------------|
| **6-class Acc** | Qwen-7B | **0.378** | 0.312 |
| | LLaMA-8B | 0.346 | **0.331** |
| **MAE** | Qwen-7B | **1.169** | 1.510 |
| | LLaMA-8B | 1.249 | **1.321** |
| **Kendall τ_b** | Qwen-7B | **0.463** | 0.376 |
| | LLaMA-8B | 0.418 | **0.383** |
| **Mean AUC** | Qwen-7B | **0.640** | 0.619 |
| | LLaMA-8B | 0.635 | **0.620** |

## Transfer Retention

| Direction | Accuracy | τ_b | Mean AUC |
|-----------|----------|-----|----------|
| Qwen→LLaMA | 82.7% | 81.2% | 85.0% |
| LLaMA→Qwen | 104.4% | 109.3% | 111.8% |

LLaMA→Qwen 方向 retention >100% 说明 LLaMA 训练的 classifier 在 Qwen 上表现反而优于 LLaMA 自身（因为 Qwen 数据 signal 更强）。Qwen→LLaMA 方向 retention 82-85%，说明 transfer 有损但仍保持较高水平，与 1.5B 规模的 transfer pattern 一致。

---
