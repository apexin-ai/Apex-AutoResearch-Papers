# submit eval acr spatial v4 scalar

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_eval-acr-spatial-v4-scalar_20260514T222244_result.json`
- **Structured JSON:** [`70dab9f182c7a6fc1340.json`](../../sessions/70/70dab9f182c7a6fc1340.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU 0 未空闲。** 当前有进程占用：

- **PID**: 270097
- **运行时间**: 1h47m
- **命令**: `python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.1`
- **显存占用**: 6221 MiB / 15292 MiB total on GPU 0

这是三方消融实验中的 obs_only eval，还在运行中。

其余验证已通过：
- Checkpoint `/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt` 存在 (1.3MB)
- `evaluate.py` 支持 `--max_correction_norm` 参数 (L77-78)

**选项：**
1. 等 obs_only 跑完后再部署 scalar_unc
2. 用其他空闲 GPU（GPU 1/2/3 各占 ~1.4GB，可能是 idle 进程）
3. 强制 kill obs_only 进程，立即部署

怎么处理？

---
