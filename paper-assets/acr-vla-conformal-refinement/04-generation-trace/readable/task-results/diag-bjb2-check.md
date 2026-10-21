# diag bjb2 check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_bjb2-check_20260514T020848_result.json`
- **Structured JSON:** [`b7822e67b68a4369df5d.json`](../../sessions/b7/b7822e67b68a4369df5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**进程状态：正常运行中（未 hang）**

| 项目 | 详情 |
|------|------|
| PID 125830 | 状态 `Rl`（Running），已运行 **2h06m52s** |
| GPU | RTX 4090D, 2784MiB 占用, GPU-Util 11%, 35°C |
| 命令 | `python -u src/evaluate.py --mode vla_only --benchmark object --n_rollouts 10 --seed 42` |

**进度：10 个任务中已完成 7 个，正在跑第 8 个（pick_up_the_butter）**

已完成任务的成功率：
| 任务 | 成功率 |
|------|--------|
| alphabet_soup | 0/10 (0%) |
| cream_cheese | 0/10 (0%) |
| salad_dressing | 2/10 (20%) |
| bbq_sauce | 3/10 (30%) |
| ketchup | 0/10 (0%) |
| tomato_sauce | 1/10 (10%) |
| butter | 进行中 (0/5) |

**结论：进程正常运行，并非 hang。** 实际运行时间只有 ~2 小时（不是 14 小时），可能之前看到的是旧进程或之前重启过。按当前进度，剩余 3 个任务预计 ~45 分钟内完成。GPU 利用率 11% 偏低，符合 VLA inference 特征（模型小、主要瓶颈在环境 rollout）。

---
