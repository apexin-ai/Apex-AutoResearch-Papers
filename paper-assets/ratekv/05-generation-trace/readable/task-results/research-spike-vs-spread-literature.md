# research spike vs spread literature

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_spike-vs-spread-literature_20260514T185634_result.json`
- **Structured JSON:** [`2dc29aeeab7e1b2cbed8.json`](../../sessions/2d/2dc29aeeab7e1b2cbed8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文献调研完成。产出文件：`artifacts/spike_vs_spread_literature.md`

**核心结论**：

**Spike vs spread 分析具有 novelty。** 已有工作（RateQuant, HeadKV, AdaKV 等）均确认 head-level heterogeneity 存在且可利用，但无一分析异质性的**分布形状**如何决定分配效果。

**最近的竞争者是 RateQuant（arXiv:2605.06675, 2026年5月）**——同样做 per-head bit allocation，提出 AM/GM ratio 作为标量异质性度量。但 AM/GM 只捕捉异质性大小，不区分 spike vs spread。我们的 Yi-1.5-9B case（高 AM/GM 但 spike pattern → 负收益）正是 RateQuant 无法解释的 failure mode。

**我们的独特贡献**：
1. 分布形状分析（spike/spread 分类法），超越标量度量
2. GQA ratio ≠ heterogeneity proxy 的实证反例
3. MCKP 分配器的 failure mode 刻画（spike 集中在单一 head 时无法差异化）
4. 跨 5 个模型的 shape taxonomy 与 MCKP 效果的预测关系

---
