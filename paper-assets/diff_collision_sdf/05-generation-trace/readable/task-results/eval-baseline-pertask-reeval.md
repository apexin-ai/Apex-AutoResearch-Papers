# eval baseline pertask reeval

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_baseline_pertask_reeval_20260528T001944_result.json`
- **Structured JSON:** [`c8de81cebfac487e0231.json`](../../sessions/c8/c8de81cebfac487e0231.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval is running well. GPU 0 at 49% utilization, 74.2 GB VRAM. Process PID 932512, elapsed 2:21.

**Summary:**

- **Command:**
```
python scripts/eval_safelibero.py \
  --checkpoint /root/autodl-tmp/.cache/openpi/openpi-assets/checkpoints/pi05_libero \
  --config_name pi05_libero \
  --suite safelibero_object --safety_level II \
  --n_episodes 50 --seed 7 --gpu 0 \
  --output_path /root/autodl-tmp/eval_results/reeval_baseline_pertask.json
```
- **PID:** 932512 (python), 932507 (bash wrapper)
- **GPU:** cuda:0, westd-35807
- **Log:** `/root/runs/diff_collision_sdf/reeval_baseline_pertask.log`
- **Output:** `/root/autodl-tmp/eval_results/reeval_baseline_pertask.json`
- **Model:** Pi0.5 pretrained (no LoRA, no fine-tuning), config `pi05_libero`, `pi05=True`
- **Eval protocol:** seed=7, 50 episodes/task, 4 tasks, safety_level II, 300 max_steps, replan_steps=5
- **v3 fixes confirmed:** 180° image rotation (`[::-1, ::-1]`) + 256px camera resolution
- **Estimated completion:** ~08:50-09:00 UTC (based on ~5-10s/episode × 200 episodes = 17-33 min, started 08:28)

---
