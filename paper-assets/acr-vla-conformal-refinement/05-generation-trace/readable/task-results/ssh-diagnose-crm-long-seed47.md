# ssh diagnose crm long seed47

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose-crm-long-seed47_20260520T002002_result.json`
- **Structured JSON:** [`19a43ffa9949fbb4b073.json`](../../sessions/19/19a43ffa9949fbb4b073.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成。结果如下：

**Overall SR: 17%**（10 tasks × 10 rollouts = 100 episodes）

| Task | SR | Succ/Total |
|------|-----|-----------|
| KITCHEN_SCENE3 turn on stove & put moka pot | **0.80** | 8/10 |
| KITCHEN_SCENE6 mug in microwave & close | **0.50** | 5/10 |
| LIVING_ROOM_SCENE5 mugs on plates | 0.20 | 2/10 |
| STUDY_SCENE1 book in caddy | 0.20 | 2/10 |
| LIVING_ROOM_SCENE2 soup & sauce in basket | 0.00 | 0/10 |
| LIVING_ROOM_SCENE2 cheese & butter in basket | 0.00 | 0/10 |
| KITCHEN_SCENE4 bowl in drawer & close | 0.00 | 0/10 |
| LIVING_ROOM_SCENE6 mug on plate & pudding | 0.00 | 0/10 |
| LIVING_ROOM_SCENE1 soup & cheese in basket | 0.00 | 0/10 |
| KITCHEN_SCENE8 both moka pots on stove | 0.00 | 0/10 |

Baseline（`eval_long_obs_only_norm02_seed47`）的 JSON 不存在——只有 CRM 的结果文件。

---
