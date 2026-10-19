# harvest eval supp long adapt tau025 s47 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval-supp-long-adapt-tau025-s47-r2_20260524T165652_result.json`
- **Structured JSON:** [`028089477e5058e2b64d.json`](../../sessions/02/028089477e5058e2b64d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验 eval-supp-long-adapt-tau025-s47-r2 — 成功完成**

| 指标 | 值 |
|------|-----|
| Overall SR | **55.0%** (110/200) |
| Mean uncertainty | 0.1235 |
| Trigger rate | 3.65% (2707/74115 steps) |
| τ | 0.25 |

Per-task 分布：

| Task | SR |
|------|-----|
| KITCHEN_SCENE3 (stove+moka) | 95% |
| KITCHEN_SCENE4 (bowl+drawer) | 95% |
| STUDY_SCENE1 (book+caddy) | 90% |
| LIVING_ROOM_SCENE2 (cheese+butter) | 80% |
| KITCHEN_SCENE6 (mug+microwave) | 60% |
| LIVING_ROOM_SCENE1 (soup+cheese) | 60% |
| LIVING_ROOM_SCENE5 (mugs+plates) | 35% |
| LIVING_ROOM_SCENE6 (mug+pudding) | 20% |
| LIVING_ROOM_SCENE2 (soup+tomato) | 15% |
| KITCHEN_SCENE8 (moka pots) | 0% |

s47 的 55.0% 低于 s42 (59.0%) 和 s46 (58.5%)，但在合理方差范围内。3-seed mean 约 57.5%。

Registry 已更新 conclusion=success + metrics，cron 已删除。

---
