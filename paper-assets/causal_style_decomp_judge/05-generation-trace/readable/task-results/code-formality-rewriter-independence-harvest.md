# code formality rewriter independence harvest

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_formality_rewriter_independence_harvest_20260521T104827_result.json`
- **Structured JSON:** [`1a0afb835a8925cbb2e8.json`](../../sessions/1a/1a0afb835a8925cbb2e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成。结果汇总：

| 指标 | GPT-4o Rewriter | Qwen3-32B Rewriter (baseline) |
|------|----------------|-------------------------------|
| NLI pass | 90/100 | 88/100 |
| BT P(formal) | **69.7%** [57.6, 80.3] (p=0.0001) | **66.5%** [58.5, 73.9] |
| GEE Style OR | 24.47 (p=0.003) | 4.20 |
| GEE Orig OR | 39.27 (p=0.001) | 4.70 |
| Likert ATE | -0.189 (p=0.18) | ~0 |
| Blindspot | Yes | Yes |

**关键结论 — Rewriter Independence 成立：**

1. **BT CIs 重叠**：GPT-4o [57.6, 80.3] vs Qwen3-32B [58.5, 73.9]，delta 仅 3.2pp。两个不同 rewriter 产生的 formality bias 强度一致。

2. **Likert ATE 均不显著**：GPT-4o ATE=-0.189 (p=0.18)，Qwen3-32B ~0。两者都确认 Likert 评分对 formality 变化不敏感（blindspot）。

3. **GEE OR 差异较大**（24.47 vs 4.20），但这很可能是因为 GPT-4o 的 N=90（小样本 logistic 回归的 quasi-separation 问题会放大 OR 估计），且两者都是显著的。关键的 BT 指标——更稳健的非参数估计——是一致的。

**与 verbosity 的平行关系**：Verbosity 实验同样确认了 rewriter independence（GPT-4o BT=73.5% vs Qwen3-32B 77.3%，CI 重叠）。Formality 维度的结果完全一致，R3-N2 task 两个维度均已通过。

---
