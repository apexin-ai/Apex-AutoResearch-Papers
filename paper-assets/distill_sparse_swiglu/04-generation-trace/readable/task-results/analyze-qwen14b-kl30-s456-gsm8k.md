# analyze qwen14b kl30 s456 gsm8k

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_qwen14b_kl30_s456_gsm8k_20260520T000133_result.json`
- **Structured JSON:** [`9b34dfcfd8bb6d5a0039.json`](../../sessions/9b/9b34dfcfd8bb6d5a0039.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。结果汇总：

## Metrics — qwen14b_kl30_s456_gsm8k

| 指标 | 值 |
|------|-----|
| gsm8k_exact_match (flexible) | 0.2608 |
| gsm8k_exact_match_stderr | ±0.0121 |
| gsm8k_exact_match_strict | 0.2547 |
| gsm8k_exact_match_strict_stderr | ±0.0120 |
| actual_sparsity | 0.297 |
| 错误/警告 | 无（仅 transformers max_length 常规 warning） |

## 3-seed GSM8K 汇总

| Seed | exact_match | sparsity |
|------|-------------|----------|
| s42 | 0.3571 | 0.296 |
| s123 | 0.3442 | 0.297 |
| s456 | **0.2608** | 0.297 |
| **Mean±Std** | **0.3207±0.0523** | 0.297 |

## 异常

**s456 是明显的 outlier**，比 s42/s123 低约 8-10pp。sparsity 一致（0.297），所以不是 mask 差异导致的。三 seed 标准差 0.0523 偏高——GSM8K 本身方差较大（stderr ~0.012），但跨 seed 这个量级的波动可能指向 predictor 训练的 seed 敏感性，或 s456 predictor 质量本身较差。建议检查 s456 predictor 的训练 loss 曲线与 s42/s123 对比，确认是否存在训练异常。

---
