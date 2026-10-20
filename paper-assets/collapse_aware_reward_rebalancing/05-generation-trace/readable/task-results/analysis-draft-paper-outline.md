# analysis draft paper outline

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_draft_paper_outline_20260517T033408_result.json`
- **Structured JSON:** [`8e37e193a510493c7621.json`](../../sessions/8e/8e37e193a510493c7621.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Outline 已写入 `artifacts/paper_outline_d.md`。核心结构：

**Title 推荐**: "Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training"

**论文主线**: intuitive fear → systematic test → surprising negative → deeper understanding → actionable guidance

**正文 8 页分配**:
- Introduction (1.2p): 从 Kirk et al. 的 RLHF diversity loss 延伸到 iterative 设置的 compounding collapse 担忧，5 条 contributions
- Results (2.0p): 主发现 (无 collapse) + 3 个 sub-findings (relative suppression / LoRA artifact / quality non-tradeoff) + conditional K=16
- Analysis (1.5p): 三个假说解释 why not collapse + boundary conditions + CARR dry-run negative finding

**图表**: 主文 4 Figure + 3 Table，附录 1 Figure + 3-4 Table。核心可视化是 Figure 2 (Vendi 轨迹折线图，curated 平坦 vs baseline 微升)。

**关键 framing 策略**: 不是 "我们失败了"，而是 "contrary to expectation, collapse doesn't hold under standard conditions, which refines when diversity-preserving methods are truly needed"。

需要调整或深入展开哪个部分？

---
