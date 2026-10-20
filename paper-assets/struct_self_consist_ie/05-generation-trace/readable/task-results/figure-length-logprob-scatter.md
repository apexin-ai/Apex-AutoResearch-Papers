# figure length logprob scatter

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_length_logprob_scatter_20260515T022113_result.json`
- **Structured JSON:** [`c6e95bc13d2dd383d7bc.json`](../../sessions/c6/c6e95bc13d2dd383d7bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**数据量**
- NER: 4232 个数据点（529 instances × 8 samples）
- RE: 3176 个数据点（397 instances × 8 samples）

**Length-Logprob 相关性**
- NER: Spearman ρ = **+0.386** (p = 9.3e-151)
- RE: Spearman ρ = **+0.326** (p = 2.8e-79)

**结论：不存在审稿人担心的 length bias。** 相关性是**正的**——更长的输出反而有略高的 mean logprob（更接近 0）。这意味着 logprob-based selection 不会系统性地惩罚长输出。OLS 回归线也呈上升趋势。

图表已保存至：
- `artifacts/figures/fig_length_logprob_scatter.pdf`
- `artifacts/figures/fig_length_logprob_scatter.png`

---
