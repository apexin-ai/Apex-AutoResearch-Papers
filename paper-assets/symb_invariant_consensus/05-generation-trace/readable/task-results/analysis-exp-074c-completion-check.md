# analysis exp 074c completion check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-074c-completion-check_20260519T210435_result.json`
- **Structured JSON:** [`dd8c11c0971598418bdc.json`](../../sessions/dd/dd8c11c0971598418bdc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/negative。

**exp-074c 结果汇报：**

| 指标 | 值 |
|------|-----|
| SC accuracy | 57.35% (117/204) |
| ICG accuracy | 58.82% (120/204) |
| **Delta** | **+1.47pp** |
| n_samples | 204 |
| Wall time | 56.5 min |

Conclusion: **negative**。Δ=+1.47pp 虽然方向为正，但幅度极小，与 exp-074 (seed=42, Δ=-2.0pp) 综合看，ICG 在 FOLIO 上的效果在零附近波动，无统计显著性。两个 seed 一正一负，进一步确认 ICG 方法对 Mistral-7B×FOLIO 无实质改进。等 exp-074d (seed=456) 完成后可做 3-seed 汇总。

---
