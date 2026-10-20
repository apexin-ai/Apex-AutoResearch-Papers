# paper claim wording audit

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_claim_wording_audit_20260523T071232_result.json`
- **Structured JSON:** [`0473460515b17144555b.json`](../../sessions/04/0473460515b17144555b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 8 edits complete. Summary of changes:

| File | Original | Revised | Reason |
|------|----------|---------|--------|
| **main.tex** | "the necessary condition preventing" | "a necessary condition for preventing" | 只证明了 necessary，没证明唯一性 |
| **introduction.tex** | "Mechanism identification" | "Mechanistic evidence" | 提供证据 ≠ 完全鉴定机制 |
| **introduction.tex** | "isolate...as the necessary condition" | "identify...as a necessary condition for preventing degradation" | 同上 |
| **introduction.tex** | "confirming that gradient flow...is the operative factor" | "suggesting that...is the primary operative factor" | Full OCC vs Vanilla Δ=+0.017 不显著，不能用 "confirming" |
| **conclusion.tex** | "confirming that spatial content..." | "indicating that spatial content..." | 同上 |
| **conclusion.tex** | "loses most of the CAR advantage...indicating that collision avoidance requires continuous gradient flow" | "exhibits task-specific vulnerability...suggesting...is sensitive to the temporal extent" | Cutoff 总体 CAR≈Vanilla，无 "advantage" 可 "lose"；"requires" 过强 |
| **discussion.tex** | "the data establish that" | "the data suggest that" | 1.7pp 差异不显著 |
| **discussion.tex** | "The consistent ordering...raises the question" | "The directional ordering...though not statistically significant with 3--4 seeds, raises the question" | 明确标注排序方向性非显著性 |
| **discussion.tex** | "requires continuous gradient flow---the benefit does not persist" | "appears sensitive to the temporal extent of gradient flow: Cutoff's aggregate CAR matches Vanilla...but Task~5 collapses to 0.00" | 总体 CAR 不支持 "requires"；改为基于数据的 hedged 表述 |

---
