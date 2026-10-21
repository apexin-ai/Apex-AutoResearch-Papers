# analysis spon 2048 s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_spon_2048_s42_20260515T191953_result.json`
- **Structured JSON:** [`bc623383c16d80740899.json`](../../sessions/bc/bc623383c16d80740899.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## spon_2048_s42 分析完成

### 结论：**Negative** — SPON recovery 7.3% < 10% 阈值

### Eval 结果

| 指标 | 值 |
|------|-----|
| True Dense PPL | 6.12 |
| Sparse PPL (no SPON) | 9.22 |
| SPON Sparse PPL | **8.99** |
| **SPON recovery** | **7.3%** |
| Mean bias norm | 0.053 |

### 与前次实验对比 (seq_len=128 → 2048)

| | seq_len=128 | seq_len=2048 |
|--|-------------|--------------|
| SPON recovery | 3.8% | 7.3% (+3.5pp) |
| PPL improvement | 0.12 | 0.23 |
| Bias norm | 0.041 | 0.053 (+30%) |

### 解读
- seq_len mismatch 确实是部分原因（recovery 翻倍），但不是根本原因
- 即使匹配条件下，static bias 仍只恢复 7.3% 的稀疏化误差
- **确认 D009 "KL subsumes SPON"**：KL predictor 的 per-token mask 已经较好地保留重要 neuron，残余误差非 additive bias 能补偿
- Claim 2 "additive composition" 路线不可行，需要更高表达力的补偿机制

---
