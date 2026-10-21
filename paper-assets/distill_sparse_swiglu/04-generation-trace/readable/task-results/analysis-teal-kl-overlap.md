# analysis teal kl overlap

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_teal_kl_overlap_20260517T041951_result.json`
- **Structured JSON:** [`c821534bf94587100931.json`](../../sessions/c8/c821534bf94587100931.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果摘要：

## TEAL vs KL Neuron Overlap 分析结果

| 指标 | 值 |
|------|-----|
| **Overall Jaccard** | **0.396** (低重叠) |
| 分歧比例 | 43.3% 的 pruned neurons 互不重合 |
| KL-only pruned mean \|act\| | 0.0588 (**1.48x** 高于全局均值 0.0398) |
| TEAL-only pruned mean gate prob | 0.614 (KL 想保留这些 neuron) |
| 分析 token 数 | 55,296 (27 samples × 2048) |

**Per-layer 模式**（U 形曲线）：
- 最低重叠（最大分歧）：**L17-L18** (Jaccard ≈ 0.19) — 中间层
- 最高重叠：**L26-L28** (Jaccard ≈ 0.55) — 后层

**结论**：假设验证成功。KL predictor 和 TEAL 选择 prune 的 neuron 高度不同（Jaccard 仅 0.40）。KL 牺牲了 magnitude 显著高于均值（1.48x）的 neuron 来优化输出分布匹配（PPL），而 TEAL 保留了这些 neuron。中间层分歧最大，恰好是 LLM 中知识存储层（knowledge neurons 研究已发现 factual knowledge 集中在中间层）。这解释了为什么 TEAL 在 MMLU 上不输甚至优于 KL：TEAL 的 magnitude-based 策略天然保护了高 activation 的知识 neuron。

脚本：`/root/distill_sparse_swiglu/scripts/teal_kl_overlap.py`
结果：`/root/distill_sparse_swiglu/artifacts/teal_kl_overlap_analysis.json`

---
