# deploy obs only object norm02 seed43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_obs-only-object-norm02-seed43_20260515T133846_result.json`
- **Structured JSON:** [`57d879cc5981ad405f59.json`](../../sessions/57/57d879cc5981ad405f59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:0 仍被占用，无法部署。**

cuda:0 上正在运行 `eval-mag-obsonly-norm03-r2`（PID 325264，已运行 6h49m）：

```
python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt \
  --max_correction_norm 0.3 --output_file logs/eval_mag_obsonly_norm03.json
```

这个 spatial magnitude sweep 进程还在跑，未结束。按指令不 kill，等它自然完成后再部署 seed=43。

---
