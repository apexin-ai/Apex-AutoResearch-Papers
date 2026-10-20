# analysis h7 prevalence calibration

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_h7-prevalence-calibration_20260514T100951_result.json`
- **Structured JSON:** [`0d91ca69a9d2dea81b72.json`](../../sessions/0d/0d91ca69a9d2dea81b72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果出来了。有一个重要发现需要说明。

## H7 分类结果

| 实验 | proved | H7 strict (any premise==conclusion) | H7 relaxed (single+ISR≥0.5) | single premise | ISR=1.0 |
|------|--------|------|---------|---------|---------|
| **s43** | 61 | 59/61 (96.7%) | 57/61 (93.4%) | 61/61 (100%) | 40/61 (65.6%) |
| **s44** | 89 | 77/89 (86.5%) | 82/89 (92.1%) | 89/89 (100%) | 65/89 (73.0%) |
| **s42** | 81 | 55/81 (67.9%) | 13/81 (16.0%) | 15/81 (18.5%) | 10/81 (12.3%) |
| **random s42** | 79 | 56/79 (70.9%) | 0/79 (0.0%) | 0/79 (0.0%) | 0/79 (0.0%) |

## 关键发现：strict 标准捕获了两种不同现象

**s43/s44 的 H7 strict 是真正的退化**：100% 单前提，且该前提就是结论的复制。这是论文关注的病理性模式。

**s42/random 的 H7 strict 是前提包含（premise subsumption）**：结论出现在多前提中的某一个（如 s42 folio_66 有 6 个前提，其中一个恰好等于结论，但 ISR=0.14）。这是多前提证明中的合理现象，不是退化。

因此论文中真正的 H7 标准应该是 **"single premise AND premise == conclusion"**，而非仅 "any premise == conclusion"。按此标准：

| 实验 | H7 (single premise + exact match) |
|------|-----------------------------------|
| **s43** | 59/61 (96.7%) |
| **s44** | 77/89 (86.5%) |
| **s42** | 10/81 (12.3%) |
| **random s42** | 0/79 (0.0%) |

s43 的 96.7% 与之前报告一致。与 ISR=1.0 的 65.6% 不矛盾——59 个 H7 样本中有 19 个 premise==conclusion 但 ISR=0.5（因为 STA 分解 conclusion 为多个 component，premise 只覆盖部分）。

---
