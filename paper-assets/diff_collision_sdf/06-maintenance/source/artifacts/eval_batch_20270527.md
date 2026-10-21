# Batch Eval Preparation — 2026-05-27

## Eval Command Template (westd-35807)
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/colliforce-vla && export WANDB_MODE=disabled && python scripts/eval_safelibero.py \
  --checkpoint {CKPT_PATH} \
  --config_name pi05_libero \
  --model_type lora_baseline \
  --suite {SUITE} \
  --pi05 \
  --gpu {GPU_ID} \
  --output_path /root/autodl-tmp/eval_results/{OUTPUT_NAME}.json
```

## Eval Command Template (westd-45947)
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/colliforce-vla && export WANDB_MODE=disabled && python scripts/eval_safelibero.py \
  --checkpoint {CKPT_PATH} \
  --config_name pi05_libero \
  --model_type lora_baseline \
  --suite {SUITE} \
  --pi05 \
  --gpu {GPU_ID} \
  --output_path /root/autodl-tmp/eval_results/{OUTPUT_NAME}.json
```

---

## Eval 1: spatial_bowl SDF s0 (plan_008)
- **When**: ~06:30 UTC 5/27 (after train_pi05_a1_spatial_bowl_s0_l005 finishes)
- **Server**: westd-35807
- **GPU**: cuda:0 (same as training)
- **Suite**: safelibero_spatial
- **Training registry**: train_pi05_a1_spatial_bowl_s0_l005
- **Checkpoint**: Worker must locate — likely `/root/autodl-tmp/checkpoints/a1_sdf_pi05_spatial_bowl/.../30000` or check training log for final checkpoint path
- **Output**: eval_spatial_bowl_sdf_s0_l005.json
- **Registry ID**: eval_spatial_bowl_sdf_s0_l005
- **Hypothesis**: Cross-scene SDF eval on spatial_bowl: does λ=0.005 SDF produce CAR improvement over Pi0.5 baseline (13% on spatial_bowl) in a bilateral obstacle layout?

## Eval 2: λ=0.1 s0 (plan_010)
- **When**: ~17:05 UTC 5/27 (after train_pi05_a1_obj_s0_l01_high finishes)
- **Server**: westd-35807
- **GPU**: cuda:1 (same as training)
- **Suite**: safelibero_object
- **Training registry**: train_pi05_a1_obj_s0_l01_high
- **Checkpoint**: Worker must locate — check training log at `/root/colliforce-vla/logs/train_lambda01_s0_gpu1.log` for final checkpoint path
- **Output**: eval_sdf_s0_l01_high_30k.json
- **Registry ID**: eval_sdf_s0_l01_high_30k
- **Hypothesis**: λ=0.1 seed0 eval for A/B/C scenario determination. If CAR > 57%, Level A signal masking has a breakpoint.

## Eval 3: λ=0.1 s1 (plan_010)
- **When**: ~17:50 UTC 5/27 (after train_pi05_a1_obj_s1_l01_high finishes)
- **Server**: westd-35807
- **GPU**: cuda:2 (same as training)
- **Suite**: safelibero_object
- **Training registry**: train_pi05_a1_obj_s1_l01_high
- **Checkpoint**: Worker must locate — check training log at `/root/colliforce-vla/logs/train_lambda01_s1_gpu2.log`
- **Output**: eval_sdf_s1_l01_high_30k.json
- **Registry ID**: eval_sdf_s1_l01_high_30k
- **Hypothesis**: λ=0.1 seed1 eval, paired with s0 for 2-seed mean and A/B/C determination.

## Eval 4: LoRA baseline s2 (plan_013 dependent)
- **When**: ~20:20 UTC 5/27 (after train_pi05_lora_baseline_s2 finishes)
- **Server**: westd-45947
- **GPU**: cuda:0 (same as training)
- **Suite**: safelibero_object
- **Training registry**: train_pi05_lora_baseline_s2
- **Checkpoint**: Worker must locate — default pattern: `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed2/30000`
- **Output**: eval_lora_baseline_s2_30k.json
- **Registry ID**: eval_lora_baseline_s2_30k
- **Hypothesis**: LoRA baseline seed2 for 3v3 statistical comparison. Expected CAR ≈ 54.5% (consistent with s0=56.5%, s1=52.5%).

---

## Priority Order
1. λ=0.1 s0 + s1 (highest — A/B/C determination for paper)
2. spatial_bowl SDF s0 (cross-scene validation)
3. LoRA s2 (3v3 statistics)

## Note on LoRA s0
LoRA s0 eval is ALREADY DONE (eval_lora_baseline_30k_s0_reeval, CAR=56.5%). No re-eval needed unless Director specifies otherwise. The freed cuda:0 at 06:30 should be used for spatial_bowl SDF s0 eval (Eval 1).

## Worker Instructions
When a training cron fires [DONE]:
1. Read training log to find final checkpoint path
2. Verify checkpoint exists on disk
3. Submit eval via `submit_training_job` using the command template above
4. Register eval experiment in registry with hypothesis from this document
