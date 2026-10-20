# BEV Auxiliary Head Code Changes

## New: prismatic/models/occ_head.py
- BEVOccupancyHead: Linear(2176→256) → ConvTranspose2d 16→32→64 → Conv2d → (B,1,64,64)
- 1.2M params, takes fused visual features before projector
- FocalLoss(alpha=0.25, gamma=2.0)

## Modified: prismatic/extern/hf/modeling_prismatic.py
- Cache patch_features before projector: self._cached_patch_features = patch_features

## Modified: vla-scripts/finetune.py
- Config: use_occ_head, occ_data_dir, occ_loss_weight(0.01), occ_loss_decay_steps(50000), occ_detach(True)
- Training: loss = loss_action + λ*loss_occ, λ = 0.01*exp(-step/50000)
- OccHead wrapped in DDP, included in optimizer

## Modified: prismatic/vla/datasets/datasets.py
- RLDSBatchTransform loads BEV labels from HDF5
- Fallback to zeros if label not found

## Modified: prismatic/util/data_utils.py
- PaddedCollatorForActionPrediction collates occ_labels

## Dry-run: ALL PASSED (33 integration points)
