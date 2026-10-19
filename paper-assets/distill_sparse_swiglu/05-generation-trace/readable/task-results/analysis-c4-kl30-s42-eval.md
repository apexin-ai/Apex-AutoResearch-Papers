# analysis c4 kl30 s42 eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c4_kl30_s42_eval_20260523T030806_result.json`
- **Structured JSON:** [`2acec1dcdd8782b7f246.json`](../../sessions/2a/2acec1dcdd8782b7f246.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正常完成，EXIT_CODE=0，无报错。

## C4 KL30 S42 Eval 结果 vs 基线

| Task | Metric | C4 KL30 | Baseline (WT103) | Δ |
|------|--------|---------|-------------------|---|
| WikiText-2 | PPL ↓ | **11.554** | 8.81 | +2.74 (worse) |
| ARC-Challenge | acc_norm | **43.09%** | 43.7% | −0.61pp |
| WinoGrande | acc | **68.67%** | 68.9% | −0.23pp |
| MMLU | acc | **39.95%** | 40.7% | −0.75pp |
| GSM8K | exact_match | **4.09%** | 7.5% | −3.41pp |
| HellaSwag | acc_norm | **69.24%** | — | — |
| PIQA | acc | **75.03%** | — | — |

模型级稀疏率：29.5%（TEAL uniform allocation）。

## 总结

C4 训练数据**未能改善** MMLU 和 GSM8K，反而全面退步：

- **PPL 大幅恶化** (+2.74)，说明 C4 训练的 predictor 在 WikiText-2 上泛化更差
- **GSM8K 跌幅最大** (−3.41pp)，从 7.5% 降到 4.09%
- **MMLU 也下降** (−0.75pp)，与预期的"多样数据改善下游"相反
- ARC-c 和 WinoGrande 基本持平，略微下降

结论：WikiText-103 训练的 predictor 在所有可比指标上优于 C4 训练版本。C4 数据的多样性未能转化为更好的稀疏掩码质量。

---
