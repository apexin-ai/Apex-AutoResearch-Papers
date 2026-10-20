# analyze 8b s44 noevi results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_8b-s44-noevi-results_20260523T080022_result.json`
- **Structured JSON:** [`a6310746f742b7d5e289.json`](../../sessions/a6/a6310746f742b7d5e289.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。结果汇总：

**8B s44 no-evi test eval**
- ign_f1 = **0.3264**
- precision = 0.5006, recall = 0.2422
- format_ok_rate = 0.992, n_truncated = 39

**s44 evidence tax**
- with-evi ign_f1 = 0.3329, no-evi ign_f1 = 0.3264
- tax = 0.3264 − 0.3329 = **−0.65pp**（evidence helps）

**8B 3-seed evidence tax 统计**

| Seed | with-evi | no-evi | Tax (pp) |
|------|----------|--------|----------|
| s42  | 0.3353   | 0.3319 | −0.34    |
| s43  | 0.3398   | 0.3224 | −1.74    |
| s44  | 0.3329   | 0.3264 | −0.65    |

- **Mean = −0.91pp ± 0.74pp** (std, N=3)

所有 3 个 seed 的 evidence tax 均为负值，表明 evidence 一致性地帮助了关系分类（平均提升 ~0.91pp ign_f1）。Registry 已更新为 DONE/success。

---
