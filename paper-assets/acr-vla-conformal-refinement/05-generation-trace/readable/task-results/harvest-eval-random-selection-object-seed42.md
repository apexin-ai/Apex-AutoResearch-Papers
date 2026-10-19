# harvest eval random selection object seed42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval-random-selection-object-seed42_20260520T092524_result.json`
- **Structured JSON:** [`d40669981d864f7e0620.json`](../../sessions/d4/d40669981d864f7e0620.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 摘要

**eval-random-selection-object-seed42** 完成收割。

| Seed | SR | Status |
|------|-----|--------|
| seed42 | **0.11** | DONE ✓ |
| seed43 | 0.12 | DONE |
| seed44 | 0.11 | DONE |

三个 seed 的 Random Selection (K=10) SR 均在 0.11–0.12 范围，与 VLA-only baseline (~10.9%) 基本持平，符合预期——随机选 action 不带来有意义的提升，验证了 CRM uncertainty-guided selection 的价值。

---
