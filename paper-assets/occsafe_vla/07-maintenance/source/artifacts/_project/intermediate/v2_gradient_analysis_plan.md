# V2 Gradient Analysis Execution Plan (5 Conditions)

## Server: westd-10894
All 5 checkpoints and data are available on this server. No cross-server SCP needed.

## Checkpoint Status: ALL READY

| Condition | Checkpoint Dir | Status |
|-----------|---------------|--------|
| Full OCC BN v2 | `mvp_occ_s3_v2/..--mvp_occ_s3_v2--50000_chkpt` | ✅ Ready |
| Full OCC LN v2 | `full_occ_ln_s3_v2/..--full_occ_ln_s3_v2--50000_chkpt` | ✅ Ready |
| Detach BN v2 | `ablation_occ_detach_s3_v2/..--ablation_occ_detach_s3_v2--50000_chkpt` | ✅ Ready |
| Detach LN v2 | `detach_ln_s3/..--detach_ln_s3--50000_chkpt` | ✅ Ready |
| Vanilla v2 | `vanilla_v2_s1/..--vanilla_v2_s1--50000_chkpt` | ✅ Ready |

Checkpoint base: `/root/autodl-tmp/checkpoints/`
Prefix: `openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug`

## Run Commands (sequential, single GPU)

Environment preamble (prepend to each):
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/scripts
```

### 1. Full OCC BN v2
```bash
python3 run_gradient_analysis_v2.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints/mvp_occ_s3_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--mvp_occ_s3_v2--50000_chkpt \
  --condition_name "Full OCC BN v2" \
  --occ_norm bn \
  --seed 42 --num_samples 800 --batch_size 4 \
  --output_dir /root/occsafe_vla/artifacts/gradient_v2_5cond/ \
  --gpu 0
```

### 2. Full OCC LN v2
```bash
python3 run_gradient_analysis_v2.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints/full_occ_ln_s3_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_s3_v2--50000_chkpt \
  --condition_name "Full OCC LN v2" \
  --occ_norm ln \
  --seed 42 --num_samples 800 --batch_size 4 \
  --output_dir /root/occsafe_vla/artifacts/gradient_v2_5cond/ \
  --gpu 0
```

### 3. Detach BN v2
```bash
python3 run_gradient_analysis_v2.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints/ablation_occ_detach_s3_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--ablation_occ_detach_s3_v2--50000_chkpt \
  --condition_name "Detach BN v2" \
  --occ_norm bn \
  --seed 42 --num_samples 800 --batch_size 4 \
  --output_dir /root/occsafe_vla/artifacts/gradient_v2_5cond/ \
  --gpu 0
```

### 4. Detach LN v2
```bash
python3 run_gradient_analysis_v2.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints/detach_ln_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_s3--50000_chkpt \
  --condition_name "Detach LN v2" \
  --occ_norm ln \
  --seed 42 --num_samples 800 --batch_size 4 \
  --output_dir /root/occsafe_vla/artifacts/gradient_v2_5cond/ \
  --gpu 0
```

### 5. Vanilla v2
```bash
python3 run_gradient_analysis_v2.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints/vanilla_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--vanilla_v2_s1--50000_chkpt \
  --condition_name "Vanilla v2" \
  --occ_norm ln \
  --seed 42 --num_samples 800 --batch_size 4 \
  --output_dir /root/occsafe_vla/artifacts/gradient_v2_5cond/ \
  --gpu 0
```

### 6. Plot (after all 5 complete)
```bash
python3 plot_gradient_analysis_v2.py \
  --results_dir /root/occsafe_vla/artifacts/gradient_v2_5cond/ \
  --output /root/occsafe_vla/artifacts/gradient_v2_5cond/gradient_analysis_v2_combined.pdf
```

## Time Estimates
- Per condition: ~15-20 min (200 batches × 4 samples, single GPU)
- Total 5 conditions: ~75-100 min
- Plot: < 1 min
- **Total: ~80-105 min on 1 GPU**

## Notes
1. **Condition names use spaces** (e.g., "Full OCC BN v2"), NOT underscores. This matches `CONDITION_STYLES` in `plot_gradient_analysis_v2.py` for correct colors/markers. The existing `run_gradient_analysis_5cond.sh` has underscore names — do NOT use that script as-is.
2. Script parameter is `--checkpoint_dir` (directory path), not `--checkpoint_path`.
3. The batch script also calls `compare_gradient_5cond.py` at the end for a comparison JSON — optional but available.
4. Data dirs verified: RLDS data at `/root/autodl-tmp/data/modified_libero_rlds/libero_spatial_no_noops/`, OCC data at `/root/occsafe_vla/occ_data/`.
5. Conda env: `occsafe` (not `base`).
