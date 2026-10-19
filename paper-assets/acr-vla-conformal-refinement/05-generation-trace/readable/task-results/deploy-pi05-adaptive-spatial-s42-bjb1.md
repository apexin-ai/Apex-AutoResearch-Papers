# deploy pi05 adaptive spatial s42 bjb1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_pi05-adaptive-spatial-s42-bjb1_20260525T045341_result.json`
- **Structured JSON:** [`9f9d933da1d509b33e32.json`](../../sessions/9f/9f9d933da1d509b33e32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

π0.5 模型正在加载中（`Loading PI05 from ...`），GPU 显存尚未增长（模型先在 CPU 加载再移到 GPU）。进程运行正常。

实验已部署完成：

- **exp_id**: `eval-pi05-adaptive-spatial-s42`
- **server**: bjb1-18228 cuda:0
- **tmux session**: `eval-pi05-adaptive-spatial-s42`
- **CRM checkpoint**: `/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt`
- **参数**: `--mode adaptive_conformal_crm --benchmark spatial --seed 42 --n_rollouts 20 --K 2 --conformal_threshold 0.25`
- **日志**: `logs/eval_spatial_adaptive_pi05_seed42.log`
- **输出**: `logs/eval_spatial_adaptive_pi05_seed42.json`

π0.5 模型正在加载，后续会占用 cuda:0 显存并开始 rollout。

---
