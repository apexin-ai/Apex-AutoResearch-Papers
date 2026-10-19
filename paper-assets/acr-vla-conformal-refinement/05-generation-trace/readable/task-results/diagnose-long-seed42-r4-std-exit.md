# diagnose long seed42 r4 std exit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_long-seed42-r4-std-exit_20260522T160350_result.json`
- **Structured JSON:** [`788d7edc461f836b8b1b.json`](../../sessions/78/788d7edc461f836b8b1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：正常完成。**

Eval 已跑完全部 10 个 long-horizon 任务 × 20 rollouts，结果写入 JSON。

**结果：overall SR = 0.0%**

Per-task breakdown（全部 0/20）：

| Task | SR |
|------|----|
| LIVING_ROOM_SCENE2 — alphabet soup + tomato sauce → basket | 0% |
| LIVING_ROOM_SCENE2 — cream cheese + butter → basket | 0% |
| KITCHEN_SCENE3 — turn on stove + put moka pot | 0% |
| KITCHEN_SCENE4 — black bowl → bottom drawer + close | 0% |
| LIVING_ROOM_SCENE5 — white mug → left plate + yellow-white mug → right plate | 0% |
| STUDY_SCENE1 — book → back compartment of caddy | 0% |
| LIVING_ROOM_SCENE6 — white mug → plate + chocolate pudding → right | 0% |
| LIVING_ROOM_SCENE1 — alphabet soup + cream cheese → basket | 0% |
| KITCHEN_SCENE8 — both moka pots → stove | 0% |
| KITCHEN_SCENE6 — yellow-white mug → microwave + close | 0% |

VLA-only baseline 在 long-horizon 任务上全部失败，符合预期——这些多步任务需要高层规划，纯 VLA 无法完成。

---
