# paper n2a downstream bootstrap

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_n2a-downstream-bootstrap_20260516T043728_result.json`
- **Structured JSON:** [`813b04f02c99da4d091d.json`](../../sessions/81/813b04f02c99da4d091d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果摘要：

**Primary comparison (size_matched vs depth01):**
- Mean diff: −0.0202 ppl (depth01 略差)
- 95% Bootstrap CI: [−0.0207, −0.0199]
- Cohen's d: −65.5 (极大效应量，但这是因为 within-group variance 极小——3 seeds 几乎一致)
- Exact permutation p = 0.10 (C(6,3)=20，最小非零 p=0.05，当前不显著)

**关键 caveat:** n=3/group 下 exact permutation test 只有 20 种排列，p 值分辨率极低（最小 0.05）。Cohen's d 数值巨大是因为 seed 间方差几乎为零，不代表实际效应大。CI 窄也是同理。论文中应表述为 "directional evidence with limited statistical power" 而非确定性结论。

所有 10 组 pairwise 比较已写入 `artifacts/n2a_downstream_bootstrap.json`，已注册为 `art_20260516_a4d103`。

---
