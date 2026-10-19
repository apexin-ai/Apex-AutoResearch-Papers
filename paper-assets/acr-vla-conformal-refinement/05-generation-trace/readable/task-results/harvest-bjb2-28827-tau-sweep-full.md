# harvest bjb2 28827 tau sweep full

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_bjb2-28827-tau-sweep-full_20260526T213205_result.json`
- **Structured JSON:** [`22bcba973bf17d343841.json`](../../sessions/22/22bcba973bf17d343841.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Background agent found the pi05 goal tau=0.25 data. Let me add it to the scatter CSV.

**补充数据 — pi05 Goal tau=0.25 (来自 westd/bjb1)**:

| seed | SR | trigger_rate |
|------|-----|-------------|
| s42 | 88.0% | ~3.5% (westd) |
| s43 | 87.5% | ~3.8% (westd) |
| s44 | 87.5% | 10.0% (bjb1 detailed) |

## 更新后完整 Scatter CSV

```csv
exp_id,suite,seed,tau,success_rate,trigger_rate,mean_correction_norm,fast_path_ratio
pi05-adaptive-spatial-s42-tau015,spatial,42,0.15,0.970,0.112,0.200,0.888
pi05-adaptive-spatial-s42-tau025,spatial,42,0.25,0.965,0.048,0.200,0.952
pi05-adaptive-spatial-s43-tau025,spatial,43,0.25,0.980,0.044,0.200,0.956
pi05-adaptive-spatial-s44-tau025,spatial,44,0.25,0.970,0.039,0.200,0.961
pi05-adaptive-spatial-s42-tau035,spatial,42,0.35,0.965,0.026,0.200,0.974
pi05-adaptive-goal-s42-tau015,goal,42,0.15,0.920,0.174,0.200,0.826
pi05-adaptive-goal-s42-tau025,goal,42,0.25,0.880,0.035,0.200,0.965
pi05-adaptive-goal-s43-tau025,goal,43,0.25,0.875,0.038,0.200,0.962
pi05-adaptive-goal-s44-tau025,goal,44,0.25,0.875,0.100,0.200,0.900
pi05-adaptive-goal-s42-tau035,goal,42,0.35,0.875,0.057,0.200,0.943
```

**注意**：goal tau=0.25 的 trigger_rate 差异大（s42/s43 ~3.5-3.8% vs s44 10%），s44 来自 bjb1（有 detailed metrics），westd 的 s42/s43 trigger_rate 是从 registry 中提取的近似值。`eval_goal_adaptive_seed42.json`（SR=83.5%, trigger=8.3%）不是 pi05 实验。

**下一步**：4 个 RUNNING 实验预计 2-4h 内完成，GPU 3 空闲可调度新任务。Object 实验的 alphabet_soup OOM 结果需在论文中标注或补跑。

---
