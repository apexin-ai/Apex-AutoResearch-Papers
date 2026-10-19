# analysis experiment logs check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_experiment_logs_check_20260525T194712_result.json`
- **Structured JSON:** [`140dc85d7dfe6194c147.json`](../../sessions/14/140dc85d7dfe6194c147.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均 **SUCCESS**（EXIT_CODE=0）。

## 结果汇总

| 实验 | Metric | 值 |
|------|--------|----|
| qwen14b_kl30_s456_gsm8k_bs1 | GSM8K exact_match | **0.2638** |
| mistral_kl30_s42_ppl | WikiText-2 PPL | **6.9886** |

### 实验 1 分析（GSM8K bs=1）

s456 bs=1 得到 0.2638，对比：
- s42 bs=8: 0.3548
- s123 bs=8: 0.3609
- s456 bs=8: 0.2608

bs=1 的 0.2638 与 bs=8 的 0.2608 基本一致（差 0.003），说明 **s456 的低分不是 batch_size padding confound 导致的**，而是 seed 本身的方差。Padding confound 假设可以排除。

### 实验 2 分析（Mistral PPL）

Mistral-7B 30% sparsity, seed 42 的 WikiText-2 PPL = **6.9886**，模型级实际稀疏率 0.297。数据已保存到 results.json，可用于填补论文中 Mistral PPL 缺失。

---
