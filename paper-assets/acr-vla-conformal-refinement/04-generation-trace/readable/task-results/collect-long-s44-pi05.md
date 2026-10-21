# collect long s44 pi05

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_long-s44-pi05_20260527T231021_result.json`
- **Structured JSON:** [`a6c1b3c53eb38a6aa2cc.json`](../../sessions/a6/a6c1b3c53eb38a6aa2cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 registry 更新完成。汇总报告：

---

## 实验状态总览

### Task 1: CRM always-on Long s44 (bjb1-32546)
**RUNNING** — 当前在第 7/10 个 task (KITCHEN_SCENE8, rollout 15/20)，约 70% 完成

已完成 task 的 SR：
| Task | SR |
|---|---|
| KITCHEN_SCENE3 (stove+moka) | 75.0% |
| KITCHEN_SCENE4 (bowl+drawer) | 60.0% |
| LIVING_ROOM_SCENE5 (two mugs) | 20.0% |
| STUDY_SCENE1 (book+caddy) | 65.0% |
| LIVING_ROOM_SCENE6 (mug+pudding) | 20.0% |
| LIVING_ROOM_SCENE1 (soup+cheese) | 55.0% |
| KITCHEN_SCENE8 (two mokas) | 0/15 进行中 |

预计 ~1-1.5h 完成。JSON 结果尚未生成。

### Task 2: Pi05 CRM always-on (cqa1-32758) — 4 个实验
全部确认 **RUNNING**，registry 已更新，hypothesis 已设置。

| 实验 | GPU | 当前进度 |
|---|---|---|
| pi05-crm-always-on-object-s42 | cuda:1 | salad_dressing rollout 15/20 |
| pi05-crm-always-on-spatial-s42 | cuda:2 | black_bowl_top_drawer rollout 5/20 |
| pi05-crm-always-on-goal-s42 | cuda:3 | wine_bottle rollout 15/20 |
| pi05-crm-always-on-long-s42 | cuda:5 | LIVING_ROOM_SCENE2 cream_cheese rollout 10/20 |

启动于 ~1h20m 前。object/spatial/goal 预计再 ~1-2h 完成，long 预计再 ~2-3h。

### Task 3: cqa1-32758 GPU 状态 + 新提交

| GPU | 状态 | 用途 |
|---|---|---|
| cuda:0 | **已提交新任务** | pi05-crm-always-on-object-s43 (刚启动，正加载模型) |
| cuda:1 | 13113 MiB, 22% | pi05-crm-always-on-object-s42 |
| cuda:2 | 12502 MiB, 22% | pi05-crm-always-on-spatial-s42 |
| cuda:3 | 13019 MiB, 49% | pi05-crm-always-on-goal-s42 |
| cuda:4 | 1981 MiB, 40% | smolvla-tau010-long-s42 (KITCHEN_SCENE8 rollout 5/20, ~65% 完成) |
| cuda:5 | 14018 MiB, 60% | pi05-crm-always-on-long-s42 |

**附带发现**：pi05-goal-tau015-s43-r3 已完成 (EXIT_CODE=0)，SR=**87.5%**，trigger_rate=20.5%，τ=0.15。

---

**关键待收割**：bjb1-32546 Long s44 的 SR 需等 ~1-1.5h 后提取。6 个 cqa1 实验全部在跑，无异常。

---
