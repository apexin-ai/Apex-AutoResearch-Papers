# analysis pi05 adaptive object s44 cqa1 r3

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pi05-adaptive-object-s44-cqa1-r3_20260526T152254_result.json`
- **Structured JSON:** [`97f6586341ec4017a80a.json`](../../sessions/97/97f6586341ec4017a80a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No W&B run found. Experiment completed normally, no OOM/CUDA errors. Results:

```
success_rate: 0.88 (176/200)
trigger_rate: 0.035 (3.5%, 1155/33220 steps)
mean_correction_norm: 0.200
mean_uncertainty: 0.082
per_task:
  alphabet_soup:       100.0% (20/20)
  cream_cheese:         70.0% (14/20)
  salad_dressing:       95.0% (19/20)
  bbq_sauce:            95.0% (19/20)
  ketchup:              60.0% (12/20)
  tomato_sauce:         85.0% (17/20)
  butter:               95.0% (19/20)
  milk:                100.0% (20/20)
  chocolate_pudding:    90.0% (18/20)
  orange_juice:         90.0% (18/20)
total_rollouts: 200
n_tasks: 10
wandb_run_id: none
conclusion: negative
```

**分析**: SR=88.0% 显著低于 VLA-only baseline 99.5%（Δ=-11.5pp）。与前两个 seed 一致（s42=85.5%, s43=83.0%），s44 的 88.0% 略高但同一量级。Adaptive 模式 trigger_rate 仅 3.5%（τ=0.25 下大部分 step 未触发），correction 被 clamp 到 max_norm=0.2，但即便低触发率仍造成明显性能损伤。三 seed 均值 ~85.5%，确认 π0.5 + Adaptive CRM 在 Object suite 上的负向结果稳定。

---
