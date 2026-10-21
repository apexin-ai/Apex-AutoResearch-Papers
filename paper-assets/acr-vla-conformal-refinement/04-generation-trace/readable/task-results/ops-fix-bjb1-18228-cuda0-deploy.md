# ops fix bjb1 18228 cuda0 deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-bjb1-18228-cuda0-deploy_20260518T194019_result.json`
- **Structured JSON:** [`0d6b5a30ac15e8f3e8f6.json`](../../sessions/0d/0d6b5a30ac15e8f3e8f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

## 任务 1: perdof_norm003_seed44 状态

- **`eval-perdof-object-norm003-seed44`**: 正在运行（cuda:2, PID 853864）。已完成 4/10 tasks，当前跑第 5 个 task `pick_up_the_ketchup` (rollout 6/10)。进度正常。
- **`eval-perdof-object-norm003-seed44-r2`**: session 已不存在，无需手动清理。

## 任务 2: cuda:0 双跑实验 — **无法执行**

cuda:0 **不是 IDLE**，当前已有 2 个实验在跑：
- `eval-obs-only-object-norm003-seed47` (PID 889257, 5645 MiB)
- `eval-perdof-object-norm03-seed48` (PID 889453, 5645 MiB)

合计占用 ~11290 MiB，GPU 利用率 99%。

当前 bjb1-18228 全部 4 张卡的分布：

| GPU | 实验 1 | 实验 2 |
|-----|--------|--------|
| cuda:0 | obs_only norm003 seed47 | perdof norm03 seed48 |
| cuda:1 | obs_only norm003 seed43 | obs_only norm003 seed46 |
| cuda:2 | obs_only norm005 seed46 | **perdof norm003 seed44** |
| cuda:3 | perdof default seed43 | obs_only norm01 seed48 |

每张卡都在双跑。需要等现有实验完成后才能部署新实验，或者你确认可以 kill 掉 cuda:0 上的某个实验腾位置。

---
