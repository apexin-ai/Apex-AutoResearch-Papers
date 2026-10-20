# analysis contamination 60 uniform seed456

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_contamination_60_uniform_seed456_20260518T052307_result.json`
- **Structured JSON:** [`a94551cdaf0fcd0147bd.json`](../../sessions/a9/a94551cdaf0fcd0147bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已全部更新完成，状态 DONE/success。

**结果汇总：**

| Metric | seed42 | seed123 | seed456 | Mean ± Std |
|---|---|---|---|---|
| uniform PPL | 17.766 | 17.754 | 17.77 | 17.763 ± 0.008 |
| uniform loss | 2.8773 | 2.8766 | 2.8775 | 2.8771 |
| adaptive PPL | 17.74 | 17.732 | (training) | -- |
| Δ(adaptive-uniform) | -0.026 | -0.022 | TBD | -- |

3-seed uniform baseline 在 ρ=0.6 下非常稳定（PPL range 0.016）。seed42/seed123 的 adaptive vs uniform gap 分别为 -0.026 和 -0.022，等 contamination_60_adaptive_seed456 训练完成后可完成 Claim 3 的 3-seed 证据。

---
