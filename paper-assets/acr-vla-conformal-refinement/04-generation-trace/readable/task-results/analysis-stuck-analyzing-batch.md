# analysis stuck analyzing batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_stuck-analyzing-batch_20260519T133427_result.json`
- **Structured JSON:** [`a7036db4fd10583d778e.json`](../../sessions/a7/a7036db4fd10583d778e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都已更新到 DONE。汇总如下：

## 实验 1: eval-obs-only-object-default-seed45-r2
- **SR: 18%** (18/100)
- 服务器: bjb2-28827 | 状态: DONE (success)
- Per-task: alphabet_soup=0, cream_cheese=0, salad_dressing=30%, bbq_sauce=30%, ketchup=10%, tomato_sauce=10%, butter=10%, milk=20%, chocolate_pudding=40%, orange_juice=30%

## 实验 2: eval-perdof-object-norm01-seed43
- **SR: 12%** (12/100)
- 服务器: bjb1-32546 | 状态: DONE (success)
- Per-task: alphabet_soup=0, cream_cheese=0, salad_dressing=20%, bbq_sauce=30%, ketchup=0, tomato_sauce=0, butter=0, milk=0, chocolate_pudding=40%, orange_juice=30%

## 实验 3: eval-vla-only-spatial-seed43
- **PID 80070 仍在运行**，已跑 33 分钟
- 命令: `evaluate.py --mode vla_only --benchmark spatial --n_rollouts 10 --seed 43`，输出到 `logs/eval_spatial_vla_only_seed43.json`
- 使用 `CUDA_VISIBLE_DEVICES=1`
- 状态正常，无需干预，等待自然完成即可

---
