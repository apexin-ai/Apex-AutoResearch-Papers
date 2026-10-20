# analysis recency s015 full

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_recency_s015_full_20260516T231349_result.json`
- **Structured JSON:** [`e54d9dcc1c4782c155c2.json`](../../sessions/e5/e54d9dcc1c4782c155c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**Triple dissociation 成立** — recency eviction (d_z=0.083, p=0.77, NS) 和 random eviction (d_z=-0.045, p=0.86, NS) 均无 phase gradient，而 importance eviction 有 medium effect (d_z=0.574, p<1e-70)。

这证实 phase-dependent compound sparsity 是 attention-score-based eviction 特有的，不是任何 token removal 策略的 trivial 副产物。报告已写入：
`artifacts/recency_s015/report/recency_s015_analysis.md`

---
