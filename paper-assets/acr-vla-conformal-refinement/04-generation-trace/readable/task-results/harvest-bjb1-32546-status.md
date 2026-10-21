# harvest bjb1 32546 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_bjb1-32546-status_20260526T200024_result.json`
- **Structured JSON:** [`d3f62bf1fd200a7f7728.json`](../../sessions/d3/d3f62bf1fd200a7f7728.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## 优先汇报：π0.5 Adaptive Long（Table 2 关键格）

```
exp_id: pi05-adaptive-long-s43-bjb1
status: STILL_RUNNING
PID: 903949 (running, elapsed 4h15m, GPU 0)
progress: 6/10 tasks done, task 6 at rollout 15/20
已完成 tasks SR: 85%, 100%, 100%, 95%, 85%, (task 6 ~67%)
log_path: /root/acr-vla-conformal-refinement/logs/eval-pi05-adaptive-long-s43-bjb1.log

exp_id: pi05-adaptive-long-s44-bjb1
status: STILL_RUNNING
PID: 904304 (running, elapsed 4h14m, GPU 1)
progress: 6/10 tasks done, task 6 at rollout 10/20
已完成 tasks SR: 90%, 95%, 100%, 90%, 90%, (task 6 ~80%)
log_path: /root/acr-vla-conformal-refinement/logs/eval-pi05-adaptive-long-s44-bjb1.log
```

两个 pi05-long 实验都在正常跑，无 OOM/CUDA error，预计还需 ~2.5-3h 完成。

---

## 已完成的 4 个 CRM 实验

```
exp_id: eval-crm-spatial-s48-d149-bjb1
status: COMPLETED ✓
PID: 908783 (dead)
SR: 80.5% (161/200)
注意: pick_up_bowl_on_ramekin 0% (已知难 task)
log_path: /root/acr-vla-conformal-refinement/logs/eval-crm-spatial-s48-d149-bjb1.log
output: logs/eval_spatial_crm_norm005_s48_d149.json

exp_id: eval-crm-object-s42-d149-bjb1
status: COMPLETED ✓
PID: 909918 (dead)
SR: 77.0% (154/200)
log_path: /root/acr-vla-conformal-refinement/logs/eval-crm-object-s42-d149-bjb1.log
output: logs/eval_object_crm_norm005_s42_d149.json

exp_id: eval-crm-object-s43-d149-bjb1
status: COMPLETED ✓
PID: 911462 (dead)
SR: 78.5% (157/200)
log_path: /root/acr-vla-conformal-refinement/logs/eval-crm-object-s43-d149-bjb1.log
output: logs/eval_object_crm_norm005_s43_d149.json

exp_id: eval-crm-goal-s43-d149-bjb1
status: COMPLETED ✓
PID: 912825 (dead)
SR: 82.0% (164/200)
log_path: /root/acr-vla-conformal-refinement/logs/eval-crm-goal-s43-d149-bjb1.log
output: logs/eval_goal_crm_norm005_s43_d149.json
```

所有 4 个已完成实验日志干净，无 OOM/CUDA error，无 0% 异常（spatial 的 ramekin task 0% 是已知难 task，非 bug）。

---

## GPU 状态

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 11907/24564 MiB | 25% | pi05-s43 占用 |
| 1 | 11907/24564 MiB | 24% | pi05-s44 占用 |
| 2 | 2 MiB | 0% | **空闲** |
| 3 | 2 MiB | 0% | **空闲** |
| 4 | 2 MiB | 0% | **空闲** |
| 5 | 2 MiB | 0% | **空闲** |

---

## 汇总

- **4/6 完成**：CRM spatial-s48 (80.5%), object-s42 (77.0%), object-s43 (78.5%), goal-s43 (82.0%)
- **2/6 运行中**：pi05-adaptive-long s43 和 s44，进度约 60%，预计还需 ~2.5-3h
- **4 张 GPU 空闲**（GPU 2-5），可提交新实验

---
