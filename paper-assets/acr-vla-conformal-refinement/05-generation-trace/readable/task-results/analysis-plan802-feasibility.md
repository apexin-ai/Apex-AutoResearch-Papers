# analysis plan802 feasibility

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan802-feasibility_20260517T221717_result.json`
- **Structured JSON:** [`42a8246d3125eaf36ff7.json`](../../sessions/42/42a8246d3125eaf36ff7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成。核心结论：**SmolVLA CRM 无法直接用于 OpenVLA**，存在 5 重不兼容（feature dim、action 生成机制、multi-sample 依赖、action chunk 结构、归一化方案）。如果要做，需要全新设计，最可行方案是退化为 obs_only residual corrector，但会失去 conformal 的理论保证。

---
