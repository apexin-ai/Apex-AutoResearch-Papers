# deploy bjb2 crm always on

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-crm-always-on_20260528T001548_result.json`
- **Structured JSON:** [`5c629c103ced4c5ca697.json`](../../sessions/5c/5c629c103ced4c5ca697.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU status summary:
- **GPUs 0-3**: Long tau-sweep (τ=0.15/0.20/0.30/0.35), all on task 3/10 — many hours remaining
- **GPU 4**: Spatial τ=0.15 s42-fix, near task 8-9/10
- **GPU 5**: Long τ=0.05 s42, on task 9/10 (rollout 15/20) — closest to completion

**0 GPUs available** per C001 (all memory.used > 500 MiB). Cannot deploy any experiments now.

I've extracted the SmolVLA CRM always-on command template from the completed `crm-always-on-long-s42` experiment:

```bash
python -u src/evaluate.py \
  --model smolvla \
  --mode adaptive_conformal_crm \
  --benchmark {SUITE} \
  --K 2 \
  --seed {SEED} \
  --n_rollouts 20 \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt \
  --max_correction_norm 0.2 \
  --conformal_threshold 0.001 \
  --output_file logs/eval_{SUITE}_crm_always_on_k2_norm0.2_seed{SEED}.json
```

**Estimated GPU availability:**
- GPU 5 (τ=0.05 Long): ~1-2 hours (task 9/10, rollout 15/20)
- GPU 4 (τ=0.15 Spatial): ~2-4 hours
- GPUs 0-3 (Long tau-sweep): ~6+ hours (task 3/10)

**Options:**
1. Wait for GPU 5 to free up and deploy the first experiment (crm-always-on-object-s45), then cascade as GPUs free up
2. Deploy on a different server if one is available

Which approach do you prefer?

---
