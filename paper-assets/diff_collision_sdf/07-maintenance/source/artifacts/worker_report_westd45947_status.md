# Worker Report: westd-45947 Status
**Date**: 2026-05-22 04:30 CST  
**Server**: westd-45947 (2x NVIDIA RTX PRO 6000 Blackwell, 97887 MiB each)

---

## 1. A3 object_pudding Training — ✅ COMPLETED
- **Steps**: 30000/30000
- **Checkpoint**: `/root/autodl-tmp/checkpoints/a3_grad_refine_object_pudding/a3_grad_refine_object_pudding_seed0/best/`
- **Contents**: lora_params.pt (504 LoRA params), SDF decoder, EE extractor

## 2. A3 spatial_bowl Training — 🔄 RUNNING
- **PID**: 191747 (cuda:0, tmux `a3_spatial`)
- **Progress**: step ~8000/30000 (27%)
- **Best loss**: 0.0520 at step 8000 (improved from 0.0827 at step 6000)
- **GPU 0**: 23926 MiB, 100% utilization
- **ETA**: ~5h remaining

## 3. MVP Eval — ✅ COMPLETED (with critical findings)

### 3a: A3 with refinement — ✅ COMPLETED

**Config**: `--model_type a3 --checkpoint best --suite safelibero_object --task_id 1 --n_episodes 50 --gpu 1`  
**JSON**: `/root/autodl-tmp/eval_results/eval_safelibero_object_task1_levelII_best_a3_refine_seed0.json`  
**Runtime**: ~67 minutes (PID 222345)

| Metric | Value |
|--------|-------|
| **TSR** | **0.0** (0/50) |
| **CAR** | **0.0** (0/50) |
| avg_smoothness | 0.0114 |
| avg_max_displacement | 0.822 |

**Critical observations:**
- **ALL 50 episodes collide at step 0** — collision detected at the very first simulation step
- **refine_count = 0 in every episode** — SDF gradient refinement NEVER triggered
- SDF min values: 0.015–0.445 (all positive = SDF reports "no obstacle nearby")
- Collision obstacles: mostly `moka_pot_obstacle_1`, some `white_storage_box_obstacle_1`

### 3b: A3 no refinement — ❌ CRASHED (x2, abandoned)

Two launch attempts both crashed mid-run:
- **Attempt 1** (PID 235230): reached episode 10/50 then died (no traceback, possible MuJoCo segfault)
- **Attempt 2** (PID 250971): crashed during first episode (no traceback in log)

**Since refine_count=0 in all 50 episodes of eval 3a, results would be identical** — refinement never triggered, so disabling it changes nothing.

### 3c: Baseline eval — ❌ NOT POSSIBLE
- No baseline checkpoint exists on westd-45947

### Supplementary: Task 0 single-episode eval (from separate process PID 250563)

**JSON**: `/root/autodl-tmp/eval_results/eval_safelibero_object_task0_levelII_best_a3_seed0.json`

| Metric | Value |
|--------|-------|
| TSR | 0.0 (0/1) |
| CAR | 0.0 (0/1) |
| collision_step | 0 |
| sdf_min | 0.665 |
| refine_count | 0 |

Same pattern on a different task (orange juice instead of chocolate pudding).

## 4. Root Cause Analysis

The eval results reveal **three compounding issues**:

### Issue 1: Collision at step 0
Every episode across both tasks reports `collision_step: 0`. The simulator detects a collision at the very first step before the policy takes any action. Possible causes:
- Safety level II obstacle placement puts objects in the robot's initial workspace
- The collision detection threshold (0.001) is extremely sensitive
- Initial robot configuration may already be in near-contact with obstacles

### Issue 2: SDF-simulator geometry mismatch
The SDF decoder reports positive sdf_min values (0.015–0.665) while the simulator detects collision. The learned SDF does not align with the simulator's collision geometry. Possible causes:
- SDF GT (`sdf_gt_object_chocolate.npz`, 4084 points) was generated for a different scene configuration
- The SDF operates in a different coordinate frame than the collision checker
- The SDF only models the end-effector vs. obstacle distance, not the full robot geometry

### Issue 3: refine_margin too tight
`refine_margin=0.01` means refinement only triggers when sdf_min < 0.01. But sdf_min values are 0.015–0.665 — the SDF never reports danger. Even if the SDF were perfectly calibrated, a margin of 0.01 may be too conservative. A larger margin (e.g., 0.1–0.5) would trigger refinement more frequently.

### Impact
With all three issues compounding, the A3 gradient refinement is **effectively disabled**:
- Collision happens before the policy acts (step 0)
- SDF doesn't detect the collision
- Even if it did, the margin is too tight to trigger refinement

## 5. Bugs Fixed During Eval Setup (v1→v7)
1. LoRALinear missing `.weight`/`.bias`/`.in_features`/`.out_features` → added delegating properties
2. torch.compile (`max-autotune`) incompatible with custom LoRALinear.forward() → disabled via `TORCHDYNAMO_DISABLE=1`
3. LoRA params (lora_A, lora_B) stuck on CPU after checkpoint load → explicit `.cuda()` move
4. CUDA device ordinal mismatch → shell-level `export CUDA_VISIBLE_DEVICES=1` + `--gpu 0` conflicts with Python line 748 override. Fix: use `--gpu 1` only, no shell CUDA_VISIBLE_DEVICES

## 6. GPU Summary (current)
| GPU | Task | Memory | Utilization |
|-----|------|--------|-------------|
| 0 | spatial_bowl training | 23926 MiB | 100% |
| 1 | idle | 0 MiB | 0% |

## 7. Next Steps
- [ ] Investigate collision_step=0: is this expected for safety level II? Check environment init state
- [ ] Verify SDF GT alignment with simulator collision geometry
- [ ] Test with larger refine_margin (0.1, 0.5) and re-run eval
- [ ] Consider evaluating at safety_level=I (fewer/farther obstacles) as sanity check
- [ ] Monitor spatial_bowl training to 30000 steps (~5h remaining)
- [ ] Baseline eval: needs baseline checkpoint transfer to westd-45947
