# scan bjb2 28827 spot check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_scan_bjb2-28827-spot-check_20260523T212945_result.json`
- **Structured JSON:** [`546229a65c897b3ae389.json`](../../sessions/54/546229a65c897b3ae389.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

所有 6 个实验正常运行，无异常。无已完成未收割的结果。

### Long Horizon 实验

| GPU | 实验 | 进度 | 当前任务 | 备注 |
|-----|------|------|----------|------|
| cuda:3 | Long Reconvla s44 | 7/10 tasks, task 8 @ 15/20 | LIVING_ROOM_SCENE1 basket | ~78% |
| cuda:5 | Long K2mean s44 | 7/10 tasks, task 8 @ 10/20 | LIVING_ROOM_SCENE1 basket | ~75% |
| cuda:4 | Long K2mean s45 | 1/10 tasks, task 2 @ 15/20 | LIVING_ROOM_SCENE2 cream_cheese_butter | ~18%，刚部署 |

Long Reconvla s44 和 K2mean s44 部分已完成任务的 SR 快照：

| 任务 | Reconvla s44 | K2mean s44 |
|------|-------------|------------|
| LIVING_ROOM_SCENE2 basket | 85% | 60% |
| KITCHEN_SCENE3 stove | 95% | 95% |
| KITCHEN_SCENE4 drawer | 95% | 90% |
| LIVING_ROOM_SCENE5 mugs | 50% | 35% |
| STUDY_SCENE1 book | 90% | 85% |
| LIVING_ROOM_SCENE6 pudding | 25% | 25% |

Reconvla 在大多数任务上领先 K2mean 5-25pp。

### Goal 实验 (s45 三件套)

| GPU | 实验 | 进度 | 当前任务 | 备注 |
|-----|------|------|----------|------|
| cuda:0 | Goal VLA-only s45 | 4/10 tasks, task 5 @ 15/20 | put_bowl_on_cabinet | ~48% |
| cuda:1 | Goal CRM s45 | 4/10 tasks, task 5 @ 5/20 | put_bowl_on_cabinet | ~43% |
| cuda:2 | Goal Reconvla s45 | 4/10 tasks, task 5 @ 10/20 | put_bowl_on_cabinet | ~45% |

已完成任务 SR：

| 任务 | VLA-only | CRM | Reconvla |
|------|----------|-----|----------|
| open_middle_drawer | 90% | 70% | 85% |
| put_bowl_on_stove | 100% | 100% | 95% |
| wine_bottle_on_cabinet | 90% | 85% | 90% |
| open_top_drawer_bowl | 65% | 60% | 65% |

Goal 三者差异不大，VLA-only 略占优。

### GPU 显存

所有 GPU 显存使用正常（2.3-5.6GB / 24GB），inference 模式下属正常水平。

### 预计完成时间

- Long Reconvla s44 / K2mean s44：还剩 ~2-3 个 task，预计 **2-4 小时**完成
- Long K2mean s45：刚开始，预计 **10-12 小时**
- Goal s45 三件套：~一半进度，预计 **4-6 小时**

---
