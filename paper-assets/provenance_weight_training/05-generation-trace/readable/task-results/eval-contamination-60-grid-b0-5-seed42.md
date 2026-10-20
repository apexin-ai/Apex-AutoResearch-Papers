# eval contamination 60 grid b0 5 seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_contamination_60_grid_b0_5_seed42_20260516T013652_result.json`
- **Structured JSON:** [`60611354d81f9cee5242.json`](../../sessions/60/60611354d81f9cee5242.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

## 评估结果

| 实验 | 方法 | ρ | PPL |
|------|------|---|-----|
| contamination_60_uniform_seed42 | uniform | 0.6 | 17.766 |
| **contamination_60_grid_b0_5_seed42** | **grid b=0.5** | **0.6** | **17.704** |
| grid_b0_5_seed42 | grid b=0.5 | 0.4 | 17.644 |

**结论：grid b=0.5 在 ρ=0.6 下 PPL=17.704，beat uniform（17.766），差值 0.062。** 说明从 ρ=0.4 搜到的最优 b=0.5 在更高污染比下仍然有效，但优势收窄（ρ=0.4 时 grid b=0.5 比 uniform 好 0.12+）。

---
