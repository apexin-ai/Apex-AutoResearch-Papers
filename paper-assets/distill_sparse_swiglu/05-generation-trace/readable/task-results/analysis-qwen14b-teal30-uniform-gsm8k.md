# analysis qwen14b teal30 uniform gsm8k

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen14b_teal30_uniform_gsm8k_20260520T020501_result.json`
- **Structured JSON:** [`488043501604941c9888.json`](../../sessions/48/488043501604941c9888.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## 结果汇总

### 提取指标

| 指标 | 值 |
|------|-----|
| gsm8k_exact_match (strict) | **0.5208** |
| gsm8k_exact_match (flexible) | 0.5208 |
| gsm8k_exact_match_stderr | ±0.01376 |
| actual_sparsity (model-level) | 0.293 |
| sample_len | 1319 |

无 W&B run（纯 lm-eval-harness 离线评测）。

### 对比（Qwen-2.5-14B GSM8K）

| 条件 | gsm8k_exact_match | Δ vs Dense |
|------|-------------------|------------|
| Dense | 0.8757 | — |
| TEAL@27.5% uniform | 0.5709 | -30.48pp |
| **TEAL@30% uniform (本实验)** | **0.5208** | **-35.49pp** |
| TEAL@30% global | 0.4951 | -38.06pp |
| KL@30% uniform s42 | 0.3571 | -51.86pp |
| KL@30% uniform s123 | 0.3442 | -53.15pp |
| KL@30% uniform s456 | 0.2608 | -61.49pp |

### Conclusion: success

- TEAL@30% uniform GSM8K=0.5208，显著高于所有 KL@30% uniform 变体（+16.4~26.0pp）
- 比 TEAL@30% global (0.4951) 高 +2.57pp
- 比 TEAL@27.5% uniform (0.5709) 低 5.01pp，符合预期（更高稀疏度→更多退化）
- 数据可用于填补附录表格 TEAL@30% uniform 行的 GSM8K 列

### Registry 更新

metrics/conclusion/status/spec 全部更新成功，状态已转为 DONE。

---
