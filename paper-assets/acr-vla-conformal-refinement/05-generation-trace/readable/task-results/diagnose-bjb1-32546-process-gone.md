# diagnose bjb1 32546 process gone

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bjb1-32546-process-gone_20260519T205640_result.json`
- **Structured JSON:** [`7335b5cccfab2b05aad7.json`](../../sessions/73/7335b5cccfab2b05aad7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### Cron 报告有误 — 4 个进程全部在运行

cuda:1 和 cuda:3 上不是原来失败的 crm-goal-seed44/45，而是**新启动的 crm_obs_only (norm=0.2)** 实验。

---

### GPU 状态

| GPU | 利用率 | 显存占用 | 状态 | 实验 |
|-----|--------|----------|------|------|
| 0 | 0% | 2 MiB | **空闲** | — |
| 1 | 36% | 4254 MiB | 运行中 | crm_obs_only goal seed44 (norm0.2), ~4/10 tasks |
| 2 | 0% | 2 MiB | **空闲** | — |
| 3 | 39% | 4254 MiB | 运行中 | crm_obs_only goal seed45 (norm0.2), ~4/10 tasks |
| 4 | 21% | 4931 MiB | 运行中 | eval vla_only long seed47 |
| 5 | 20% | 4619 MiB | 运行中 | eval vla_only spatial seed48, 3/10 tasks done |

**空闲 GPU: cuda:0, cuda:2**

---

### 实验状态

**1. eval-vla-only-long-seed47 (cuda:4) — 已完成，JSON 已写入**

`overall_success_rate = 0.14` (14%)

| Task | Success Rate |
|------|-------------|
| LIVING_ROOM_SCENE2 alphabet_soup + tomato_sauce → basket | 0% |
| LIVING_ROOM_SCENE2 cream_cheese + butter → basket | 0% |
| KITCHEN_SCENE3 stove + moka_pot | **80%** |
| KITCHEN_SCENE4 black_bowl → drawer + close | 0% |
| LIVING_ROOM_SCENE5 mugs → plates | **40%** |
| STUDY_SCENE1 book → caddy | 10% |
| LIVING_ROOM_SCENE6 mug + pudding | 10% |
| LIVING_ROOM_SCENE1 alphabet_soup + cream_cheese → basket | 0% |
| KITCHEN_SCENE8 both moka_pots → stove | 0% |
| KITCHEN_SCENE6 mug → microwave + close | 0% |

**2. eval-vla-only-spatial-seed48 (cuda:5) — 运行中, 3/10 tasks done**

已完成的 tasks:
- pick_up bowl between plate & ramekin → plate: **70%**
- pick_up bowl next to ramekin → plate: **100%**
- pick_up bowl from table center → plate: **0%**

**3. crm_obs_only goal seed44 (cuda:1) — 运行中, ~4/10 tasks done**

已完成: open_middle_drawer 60%, put_bowl_on_stove 90%, wine_bottle_on_cabinet 50%, open_top_drawer 进行中

**4. crm_obs_only goal seed45 (cuda:3) — 运行中, ~4/10 tasks done**

已完成: open_middle_drawer 70%, put_bowl_on_stove 90%, wine_bottle_on_cabinet 40%, open_top_drawer 进行中

---
