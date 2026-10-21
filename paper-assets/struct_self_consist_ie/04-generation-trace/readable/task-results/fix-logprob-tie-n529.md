# fix logprob tie n529

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_logprob_tie_n529_20260515T073507_result.json`
- **Structured JSON:** [`357f1ff2e7de7fd689bf.json`](../../sessions/35/357f1ff2e7de7fd689bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

**Instance-level ties (n=529)**:  ε=0.05 下 60.3% 的 instance 是 tied（range < 0.05）

**Pairwise ties**: 论文声称 "75% of comparisons are ties" 对应 ε ≈ 0.026（P75 of pairwise diffs），在 per-token mean_logprob 尺度上是合理的阈值

**Non-tied 子集 (range ≥ 0.05, n=210)**: LP-best 显著优于 greedy (+2.9 F1, p=0.01)；SJ-best 略低于 LP-best (−1.2, p=0.37 不显著)

**n=529 vs n=551 差异**: 所有核心指标 delta < 0.002，无实质影响

产出已注册：`art_20260515_b672a9`

---
