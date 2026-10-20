# Gradient Analysis V2 — Verified Commands (50K Checkpoints)

Generated: 2026-05-27
All checkpoint paths verified to exist on their respective servers.

## Condition 1: Vanilla (westd-34685, cuda:0)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
python3 /root/occsafe_vla/scripts/run_gradient_analysis_v2.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints/vanilla_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--vanilla_v2_s1--50000_chkpt \
  --condition_name "Vanilla_v2" \
  --seed 42 \
  --output_dir /root/occsafe_vla/artifacts/gradient_v2/ \
  --gpu 0
```

## Condition 2: Full OCC BN — Grad ON + BN (westd-34685, cuda:1)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
python3 /root/occsafe_vla/scripts/run_gradient_analysis_v2.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints/full_occ_bn_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_bn_v2_s1--50000_chkpt \
  --condition_name "Full_OCC_BN_v2" \
  --occ_norm bn \
  --seed 42 \
  --output_dir /root/occsafe_vla/artifacts/gradient_v2/ \
  --gpu 1
```

## Condition 3: Full OCC LN — Grad ON + LN (westd-10894, cuda:0)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
python3 /root/occsafe_vla/scripts/run_gradient_analysis_v2.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints/full_occ_ln_s3_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_s3_v2--50000_chkpt \
  --condition_name "Full_OCC_LN_v2" \
  --seed 42 \
  --output_dir /root/occsafe_vla/artifacts/gradient_v2/ \
  --gpu 0
```

## Condition 4: Detach BN — Grad OFF + BN (westd-34685, cuda:2)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
python3 /root/occsafe_vla/scripts/run_gradient_analysis_v2.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints/detach_bn_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_bn_v2_s1--50000_chkpt \
  --condition_name "Detach_BN_v2" \
  --occ_norm bn \
  --seed 42 \
  --output_dir /root/occsafe_vla/artifacts/gradient_v2/ \
  --gpu 2
```

## Condition 5: Detach LN — Grad OFF + LN (westd-34685, cuda:3)

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
python3 /root/occsafe_vla/scripts/run_gradient_analysis_v2.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints/detach_ln_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_s3--50000_chkpt \
  --condition_name "Detach_LN_v2" \
  --seed 42 \
  --output_dir /root/occsafe_vla/artifacts/gradient_v2/ \
  --gpu 3
```

## Summary

| # | Condition | Server | GPU | Checkpoint Run | --occ_norm |
|---|-----------|--------|-----|----------------|------------|
| 1 | Vanilla | westd-34685 | cuda:0 | vanilla_v2_s1 | (auto) |
| 2 | Full OCC BN | westd-34685 | cuda:1 | full_occ_bn_v2_s1 | bn |
| 3 | Full OCC LN | westd-10894 | cuda:0 | full_occ_ln_s3_v2 | (auto/ln) |
| 4 | Detach BN | westd-34685 | cuda:2 | detach_bn_v2_s1 | bn |
| 5 | Detach LN | westd-34685 | cuda:3 | detach_ln_s3 | (auto/ln) |

## Notes

- Condition 5 **corrected**: original artifact had a duplicate of Detach BN; now uses `detach_ln_s3` checkpoint
- 4 of 5 conditions run on westd-34685 (cuda:0-3), 1 on westd-10894 (cuda:0) — all 5 can run in parallel
- All condition_names are unique
- Script auto-detects `occ_detach` from condition_name (conditions with "detach" → detach=true, "vanilla" → no OCC head)
