# eval grid b0 1 posthoc

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_grid_b0_1_posthoc_20260516T085819_result.json`
- **Structured JSON:** [`9a8c202c0bd21a8cd552.json`](../../sessions/9a/9a8c202c0bd21a8cd552.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。

**结果汇总：**

| 实验 | PPL | vs uniform |
|------|-----|-----------|
| uniform baseline | 17.694 | — |
| **grid_b0_1_seed42** | **17.657** | **-0.037** |
| grid_b0_3_seed42 | 17.640 | -0.054 |

b=0.1 的 PPL 介于 uniform 和 b=0.3 之间，改善幅度约为 b=0.3 的 69%。符合预期：b 越小权重越接近均匀，reweighting 效果越弱。

---
