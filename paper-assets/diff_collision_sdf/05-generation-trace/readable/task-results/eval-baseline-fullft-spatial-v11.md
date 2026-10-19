# eval baseline fullft spatial v11

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_baseline_fullft_spatial_v11_20260522T153711_result.json`
- **Structured JSON:** [`44565e826fd4e6a92b91.json`](../../sessions/44/44565e826fd4e6a92b91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval process confirmed running (PID 690045, 483% CPU). It's in the `torch.compile(max-autotune)` phase — this is CPU-intensive and takes ~5-10 minutes before GPU memory is allocated. Once compilation completes, GPU 1 memory will ramp up and episodes will start.

**Summary:**
- **Tmux session**: `eval_baseline_fullft_spatial_v11`
- **GPU**: cuda:1 (via `CUDA_VISIBLE_DEVICES=1`)
- **Checkpoint**: `/root/autodl-tmp/checkpoints/baseline_spatial_bowl/baseline_spatial_bowl_seed0/best`
- **Suite**: `safelibero_spatial`, all 4 tasks × 50 episodes = 200 total
- **Config**: `pi0_libero_low_mem_finetune`, `model_type=baseline`, `replan_steps=5`
- **Output**: `/root/autodl-tmp/eval_results/baseline_fullft_v11_eval_safelibero_spatial_all_levelII_best_seed0.json`
- **Log**: `/root/autodl-tmp/eval_results/eval_baseline_fullft_spatial_v11.log`

---
