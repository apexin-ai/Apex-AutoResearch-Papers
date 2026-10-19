# ops check and deploy spatial eval

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-and-deploy-spatial-eval_20260519T013442_result.json`
- **Structured JSON:** [`50dddb6f0900758c2030.json`](../../sessions/50/50dddb6f0900758c2030.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程运行正常（R 状态，11 分钟 CPU 时间，3:45 挂钟时间）。第一条 rollout 日志要等第 5 个 rollout 完成。

## 汇报

### Spatial CRM 状态
- **Spatial-specific CRM**: `/root/autodl-tmp/checkpoints/crm_spatial_only/crm_best.pt` 存在（非 obs_only 变体）
- **obs_only CRM**: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt` 存在（327,198 params），用于本次 spatial benchmark 评估
- **无 spatial+obs_only 联合 checkpoint**

### 已有 Spatial 数据
- 无已有 `eval_*spatial*` 结果
- 有 `eval_mag_obsonly_norm003.json`（不同 benchmark/参数）

### 部署结果
- tmux session: `eval-spatial-obs-only-norm02-seq`
- **顺序执行** seed43 → seed44 → seed45（GPU 24GB 不够并行跑多个 eval）
- CRM: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`
- 参数: `--mode crm_obs_only --benchmark spatial --n_rollouts 10 --K 10 --max_correction_norm 0.2`
- GPU 当前 15GB/24.5GB（与 scalar-seed45-r2 和 random-selection-seed46-t16 共享）
- seed43 已在 rollout 中，预计 3 个 seed 总耗时十几小时

---
