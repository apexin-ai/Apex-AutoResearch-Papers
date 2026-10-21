# harvest cqa1 32758 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_cqa1-32758-status_20260526T200036_result.json`
- **Structured JSON:** [`0c335594c4f20cb1d81c.json`](../../sessions/0c/0c335594c4f20cb1d81c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有日志无 OOM/CUDA error/Traceback。汇总结果：

---

## cqa1-32758 实验状态汇总

### 1. pi05-adaptive-long-s43-cqa1-r3 ⭐ (Table 2 关键)
```
exp_id: pi05-adaptive-long-s43-cqa1-r3
status: STILL_RUNNING (PID 350882, cuda:4, elapsed 9h+)
progress: 9/10 tasks completed, task 10 (KITCHEN_SCENE6_microwave) rollout 15/20
```
**已完成 task SR：**
| Task | SR |
|------|-----|
| SCENE2_alphabet_soup_tomato_sauce | 80.0% (16/20) |
| SCENE2_cream_cheese_butter | 100.0% (20/20) |
| SCENE3_stove_moka_pot | 95.0% (19/20) |
| SCENE4_black_bowl_drawer | 90.0% (18/20) |
| SCENE5_white_mug_plates | 90.0% (18/20) |
| SCENE1_book_caddy | 75.0% (15/20) |
| SCENE6_white_mug_chocolate | 65.0% (13/20) |
| SCENE1_alphabet_soup_cream_cheese | 80.0% (16/20) |
| SCENE8_moka_pots | 40.0% (8/20) |

**9 task 均值: 79.4% (143/180)**，最后一个 task 跑到 14/15，预计 ~1h 内完成。日志干净，无 OOM/error。

---

### 2. smolvla-adapt-tau015-object-s42-cqa1
```
exp_id: smolvla-adapt-tau015-object-s42-cqa1
status: STILL_RUNNING (PID 488512, cuda:0)
progress: 8/10 tasks done, task 9 (chocolate_pudding) rollout 10/15
SR so far (8 tasks): 77.5% (124/160)
```

### 3. smolvla-adapt-tau015-object-s43-cqa1
```
exp_id: smolvla-adapt-tau015-object-s43-cqa1
status: STILL_RUNNING (PID 489509, cuda:1)
progress: 8/10 tasks done, task 9 (chocolate_pudding) rollout 12/15
SR so far (8 tasks): 75.0% (120/160)
```

### 4. smolvla-adapt-tau015-object-s44-cqa1
```
exp_id: smolvla-adapt-tau015-object-s44-cqa1
status: STILL_RUNNING (PID 491099, cuda:2)
progress: 9/10 tasks done, running task 10
SR so far (9 tasks): 72.2% (130/180)
```

### 5. smolvla-crm-norm005-k10-object-s44-cqa1
```
exp_id: smolvla-crm-norm005-k10-object-s44-cqa1 (crm_obs_only K=10 norm=0.05)
status: STILL_RUNNING (PID 492013, cuda:3)
progress: 8/10 tasks done, task 9 (chocolate_pudding) rollout 13/15
SR so far (8 tasks): 76.3% (122/160)
```

---

### 6-9. Spatial 实验 (E_smolvla_*)
```
exp_id: E_smolvla_crm_norm005_spatial_s42_d149
status: NOT_FOUND — 无进程、无日志、无 exit file

exp_id: E_smolvla_adaptive_tau045_spatial_s42
status: NOT_FOUND

exp_id: E_smolvla_adaptive_tau015_spatial_s42
status: NOT_FOUND

exp_id: E_smolvla_adaptive_tau035_spatial_s42
status: NOT_FOUND
```
**这 4 个 Spatial 实验在 cqa1-32758 上不存在**，可能在其他服务器或尚未提交。

---

### GPU 使用情况
| GPU | 显存占用 | 利用率 | 用途 |
|-----|---------|--------|------|
| 0 | 2173/24564 MiB | 18% | smolvla adapt tau015 s42 |
| 1 | 2173/24564 MiB | 30% | smolvla adapt tau015 s43 |
| 2 | 2173/24564 MiB | 18% | smolvla adapt tau015 s44 |
| 3 | 2247/24564 MiB | 39% | smolvla crm norm005 s44 |
| 4 | 10281/24564 MiB | 21% | pi05 adaptive long s43 |
| **5** | **1/24564 MiB** | **0%** | **空闲** |

**GPU 5 完全空闲**，可用于新实验。所有 5 个运行中实验预计 1-3 小时内陆续完成。

---
