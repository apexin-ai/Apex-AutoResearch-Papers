# V2 Gradient Analysis Commands (50K Checkpoints)

## Checkpoint Paths

```bash
# Pattern: /root/autodl-tmp/checkpoints/{exp_id}/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--{exp_id}--50000_chkpt

VANILLA_CKPT="/root/autodl-tmp/checkpoints/vanilla_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--vanilla_v2_s1--50000_chkpt"
FULL_OCC_CKPT="/root/autodl-tmp/checkpoints/full_occ_ln_v2_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s0--50000_chkpt"
DETACH_CKPT="/root/autodl-tmp/checkpoints/detach_ln_v2_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_v2_s0--50000_chkpt"
```

## Pre-requisite: SCP Vanilla v2 from 34685 to 10894

Vanilla v2 trains on westd-34685. Must copy the 50K checkpoint to 10894 before analysis.

```bash
# On 10894:
mkdir -p /root/autodl-tmp/checkpoints/vanilla_v2_s1/
scp -r westd-34685:/root/autodl-tmp/checkpoints/vanilla_v2_s1/ /root/autodl-tmp/checkpoints/vanilla_v2_s1/
```

## Step 1: Run Per-Condition Gradient Analysis

```bash
cd /root/occsafe_vla
OUTPUT_DIR=/root/occsafe_vla/artifacts/gradient_v2_50k

# Vanilla v2
python3 scripts/run_gradient_analysis_v2.py \
  --checkpoint_dir "$VANILLA_CKPT" \
  --condition_name "Vanilla v2" \
  --seed 42 --num_samples 200 --batch_size 4 \
  --output_dir $OUTPUT_DIR --gpu 0

# Full OCC LN v2
python3 scripts/run_gradient_analysis_v2.py \
  --checkpoint_dir "$FULL_OCC_CKPT" \
  --condition_name "Full OCC LN v2" \
  --seed 42 --num_samples 200 --batch_size 4 \
  --output_dir $OUTPUT_DIR --gpu 0

# Detach LN v2
python3 scripts/run_gradient_analysis_v2.py \
  --checkpoint_dir "$DETACH_CKPT" \
  --condition_name "Detach LN v2" \
  --seed 42 --num_samples 200 --batch_size 4 \
  --output_dir $OUTPUT_DIR --gpu 0
```

## Step 2: Run Comparison

### Option A: From pre-computed JSONs

```bash
python3 scripts/compare_gradient_conditions.py \
  --vanilla-json $OUTPUT_DIR/"Vanilla v2_gradient_stats.json" \
  --full-occ-json $OUTPUT_DIR/"Full OCC LN v2_gradient_stats.json" \
  --detach-json $OUTPUT_DIR/"Detach LN v2_gradient_stats.json" \
  --output-json $OUTPUT_DIR/comparison_results.json
```

### Option B: From checkpoints (runs all 3 analyses sequentially)

```bash
python3 scripts/compare_gradient_conditions.py \
  --vanilla-ckpt "$VANILLA_CKPT" \
  --full-occ-ckpt "$FULL_OCC_CKPT" \
  --detach-ckpt "$DETACH_CKPT" \
  --num-samples 200 --batch-size 4 --gpu 0 \
  --output-dir $OUTPUT_DIR \
  --output-json $OUTPUT_DIR/comparison_results.json
```

## Notes

- Each condition takes ~15-20 min on a single GPU with 200 samples
- Total wall time for all 3: ~45-60 min
- Use `--gpu 0` (or any free GPU on 10894 cuda:0-3)
- Output JSON contains per-layer ratios (Full OCC/Vanilla, Detach/Vanilla) for paper figures
