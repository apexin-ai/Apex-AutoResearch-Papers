# code plan 004 step3 gsm1k correlation

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_004_step3_gsm1k_correlation_20260521T011144_result.json`
- **Structured JSON:** [`bfe33c7a1b5ed116058e.json`](../../sessions/bf/bfe33c7a1b5ed116058e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Step 3 完成。核心结果：

**Pearson r = −0.478, p = 0.005** — 效应量超过 |r| > 0.3 的 breakthrough 阈值，但方向是**负的**，与污染假设相反。

关键发现：
- 33 个 matched 模型（falcon-180B-chat 不在 MetaBench 中被排除）
- 所有模型在 DIF-C items 上的 accuracy **低于** non-DIF items（DIF-C items 更难）
- 高污染模型（gap 大）在 DIF-C items 上表现**更差**，而非更好
- Partial correlation 控制 GSM8K overall accuracy 后仍显著（r = −0.385, p = 0.027）
- Permutation test 证实信号真实（empirical p = 0.014）
- Leave-one-out 分析显示结果稳健，无单点驱动

**解读**：DIF-C items 不是"污染 items"，而是捕捉了跨时间队列的真实能力差异。249 个 DIF-C items 中有 171 个不利于新模型（α<1）。污染模型的优势集中在 non-DIF items 上，在 DIF items 上反而更弱——暗示污染产生的是"窄"提升，无法泛化到具有非典型难度特征的题目。

---
