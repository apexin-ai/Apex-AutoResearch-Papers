# ops collect sweep bjb2 28827

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-sweep-bjb2-28827_20260515T043856_result.json`
- **Structured JSON:** [`5fc6709e3d1cd6eafd68.json`](../../sessions/5f/5fc6709e3d1cd6eafd68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**这 6 个实验都还在运行中，并非已跑 12+ 小时。** 进程 etime 显示仅 ~1h30m，当前都在早期阶段（1-2/10 tasks）。

## 当前进度

```
exp_id: eval-mag-perdof-norm003
Status: RUNNING (~1.5h elapsed)
norm: 0.03, mode: acr_vla (perdof)
Tasks: 1/10 complete, T2 in progress
  T1 pick_up_black_bowl_between_plate_ramekin → plate: 60% (6/10) ✓
  T2 pick_up_black_bowl_next_to_ramekin → plate: 5/5 at rollout 5... (running)

exp_id: eval-mag-perdof-norm005
Status: RUNNING
norm: 0.05, mode: acr_vla (perdof)
Tasks: 1/10 complete, T2 in progress
  T1 pick_up_black_bowl_between_plate_ramekin → plate: 50% (5/10) ✓
  T2 pick_up_black_bowl_next_to_ramekin → plate: 5/5 at rollout 5... (running)

exp_id: eval-mag-perdof-norm02
Status: RUNNING
norm: 0.2, mode: acr_vla (perdof)
Tasks: 1/10 complete
  T1 pick_up_black_bowl_between_plate_ramekin → plate: 60% (6/10) ✓

exp_id: eval-mag-perdof-norm03
Status: RUNNING
norm: 0.3, mode: acr_vla (perdof)
Tasks: 1/10 complete
  T1 pick_up_black_bowl_between_plate_ramekin → plate: 70% (7/10) ✓

exp_id: eval-mag-obsonly-norm005
Status: RUNNING
norm: 0.05, mode: crm_obs_only
Tasks: 1/10 complete, T2 in progress
  T1 pick_up_black_bowl_between_plate_ramekin → plate: 80% (8/10) ✓
  T2 pick_up_black_bowl_next_to_ramekin → plate: 5/5 at rollout 5... (running)

exp_id: eval-mag-obsonly-norm02
Status: RUNNING (fastest)
norm: 0.2, mode: crm_obs_only
Tasks: 2/10 complete
  T1 pick_up_black_bowl_between_plate_ramekin → plate: 90% (9/10) ✓
  T2 pick_up_black_bowl_next_to_ramekin → plate: 100% (10/10) ✓
```

## 预估

按 ~45min/task 计算，10 tasks 总计约 **7-8 小时**，还需 **~6 小时** 才能全部完成（大约 UTC 18:30-19:00，即今天下午/晚间）。

## T1 部分结果对比（仅供参考，1/10 tasks）

| norm | perdof T1 | obs_only T1 |
|------|-----------|-------------|
| 0.03 | 60% | — |
| 0.05 | 50% | 80% |
| 0.2  | 60% | 90% |
| 0.3  | 70% | — |

不更新 registry 到 DONE——实验远未完成。需要我稍后再来查看吗？

---
