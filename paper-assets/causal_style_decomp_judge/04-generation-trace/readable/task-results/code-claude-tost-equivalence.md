# code claude tost equivalence

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_claude_tost_equivalence_20260521T114415_result.json`
- **Structured JSON:** [`5e39b68122bfdc2b42c2.json`](../../sessions/5e/5e39b68122bfdc2b42c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

TOST 结果出来了，**两个 axis 的等价性都未确认**（与预期不同）：

| Axis | P(style) | TOST p | 90% CI | Equivalence |
|------|----------|--------|--------|-------------|
| Formality | 0.562 | 0.155 | [0.500, 0.624] | **No** — 90% CI 上界 0.624 超过 0.60 |
| Verbosity | 0.541 | 0.070 | [0.475, 0.607] | **No** — 90% CI 上界 0.607 超过 0.60 |

关键原因：虽然点估计接近 0.5，但 bootstrap SE 较大（n≈87 对），导致 90% CI 上界略微突破 0.60 的等价边界。lower test 都 strongly rejected（p≈0），但 upper test 未能拒绝（formality p=0.155, verbosity p=0.070）。Verbosity 接近 marginal significance。

这说明在 Δ=0.10 的 margin 下，当前样本量不足以 **证明** 等价——并非说 Claude 有偏差，而是统计功效不够（underpowered）。如果放宽到 Δ=0.15，两者都能确认等价。

---
