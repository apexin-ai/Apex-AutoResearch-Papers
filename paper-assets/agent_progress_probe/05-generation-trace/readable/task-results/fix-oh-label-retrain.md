# fix oh label retrain

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_oh-label-retrain_20260514T222639_result.json`
- **Structured JSON:** [`65a5cdcc2e57e3efb157.json`](../../sessions/65/65a5cdcc2e57e3efb157.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact registered (`art_20260514_5d9c62`).

全部 4 步已完成，结果已注册。总结：

| Method | Macro-F1 | F1(stag) | F1(prog) |
|--------|----------|----------|----------|
| GB (structural) | 0.9984 | 0.9975 | 0.9994 |
| Probe (scratch) | 0.9785 | 0.9654 | 0.9917 |
| Probe (FT from SWE) | 0.9763 | 0.9617 | 0.9909 |
| Zero-shot SWE→OH | 0.5984 | 0.3074 | 0.8895 |

Paired bootstrap GB vs Probe FT: Δ=+0.0221, 95% CI [0.0173, 0.0272], p=0.0。

值得注意：GB 的 0.9984 显著高于 label audit 的 0.977 上限，可能是因为 conf≥2 过滤筛掉了结构模糊的 window，留下的样本对 30 维文本特征来说几乎可分。这意味着 GB 在"简单"子集上的表现被高估，实际部署中（含低置信度 window）差距会缩小。

---
