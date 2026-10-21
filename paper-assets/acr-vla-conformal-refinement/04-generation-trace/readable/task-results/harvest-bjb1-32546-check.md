# harvest bjb1 32546 check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_bjb1-32546-check_20260526T195918_result.json`
- **Structured JSON:** [`17d6887e382d4e710d9e.json`](../../sessions/17/17d6887e382d4e710d9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 CRM D149 实验已全部 DONE。Registry 已更新。

## bjb1-32546 实验状态

| exp_id | PID | 状态 | SR | 备注 |
|--------|-----|------|-----|------|
| pi05-adaptive-long-s43-bjb1 | 903949 | **alive** | — | task 7/10 (STUDY_SCENE1 rollout 15/20)，已跑 4h14m，预计还 ~1.5h |
| pi05-adaptive-long-s44-bjb1 | 904304 | **alive** | — | task 6/10 (STUDY_SCENE1 rollout 10/20)，已跑 4h13m，预计还 ~2h |
| eval-crm-spatial-s48-d149-bjb1 | 908783 | **done** → DONE | **80.5%** | on_ramekin 0%（known hard），其余 75-100% |
| eval-crm-object-s42-d149-bjb1 | 909918 | **done** → DONE | **77.0%** | all tasks 70-90% |
| eval-crm-object-s43-d149-bjb1 | 911462 | **done** → DONE | **78.5%** | all tasks 65-90% |
| eval-crm-goal-s43-d149-bjb1 | 912825 | **done** → DONE | **82.0%** | cream_cheese_in_bowl 50%（最低） |
| E_smolvla_crm_norm005_spatial_s42_d149 | — | **不在此服务器** | — | 注册在 bjb1-18228 |
| E_smolvla_adaptive_tau045_spatial_s42 | — | **不在此服务器** | — | 注册在 bjb1-18228 |
| E_smolvla_adaptive_tau015_spatial_s42 | — | **不在此服务器** | — | 注册在 bjb1-18228 |
| E_smolvla_adaptive_tau035_spatial_s42 | — | **不在此服务器** | — | 注册在 bjb1-18228 |

**关键发现：**
- 4 个 CRM D149 补跑全部完成，日志干净（无 OOM/CUDA error），registry 已更新为 DONE
- π0.5 Long s43/s44 hedge run 仍在跑，s43 略领先 s44 约 1 个 task
- τ-sweep 4 个实验不在 bjb1-32546 上（注册服务器是 bjb1-18228），bjb1-32546 上目前只有 GPU 0/1 被 π0.5 占用，GPU 2-5 已空闲

---
