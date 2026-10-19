# A1 SDF Decoder Integration Report

## Summary
A1 SDF auxiliary task successfully integrated into openpi pi0 training pipeline. All 37/37 verification checks passed on cuda:3 (NVIDIA RTX PRO 6000 Blackwell, 95GB).

## Architecture
```
Images + Language → PaliGemma → prefix tokens
State + Noisy Actions → Action Expert → suffix_out [B, 50, 1024]
                                          │
                                          ├─→ action_out_proj → velocity (原有, action_dim=32)
                                          │
                                          └─→ mean pool → [B, 1024]
                                              ├─→ SDF Decoder (395,777 params)
                                              │   Input: features [B,1024] + query_xyz [B,N,3]
                                              │   Output: SDF values [B,N]
                                              │   Loss: L1 clamped + 0.1×Eikonal
                                              │
                                              └─→ EE Extractor (263,171 params)
                                                  Input: features [B,1024]
                                                  Output: EE position [B,3]
                                                  Loss: MSE vs state[:,:3]
```

## Key Implementation Details

### Hook Mechanism
- Forward hook on `model.action_out_proj` captures `suffix_out` as `input[0]`
- suffix_out shape: `[B, 50, 1024]` (action_horizon=50, width=1024)
- Mean-pooled to `[B, 1024]` for SDF decoder and EE extractor

### Data Pipeline
- State is 32-dim after `PadStatesAndActions` (raw 8-dim LIBERO state zero-padded)
- Normalization applied BEFORE padding → `state[:, :3]` = normalized EE position
- Actions are 32-dim (padded from raw 7-dim), matching pi0_base model's action_dim
- Norm stats loaded from `/root/colliforce-vla/assets/baseline_spatial_bowl/safelibero_spatial/norm_stats.json`

### Two-Phase Training
- **Phase 1 (warmup, steps 0–5000)**: Backbone frozen, only SDF decoder + EE extractor trained. `pooled_features` detached.
- **Phase 2 (end-to-end, steps 5000–30000)**: All model parameters unfrozen (PyTorch pi0 has no separate LoRA adapter; all params are full-rank).

### Loss Composition
- Phase 1: `total = λ_sdf × sdf_total + λ_ee × ee_loss`
- Phase 2: `total = action_loss + λ_sdf × sdf_total + λ_ee × ee_loss`
- Default: λ_sdf=0.1, λ_ee=0.01, eikonal_weight=0.1, sdf_clamp=0.05

### SDF Ground Truth
- 4076 points from `/root/colliforce-vla/data/sdf_gt_spatial_bowl.npz`
- Already clamped to [-0.05, 0.05], plate obstacle
- 64 points randomly sampled per batch

## Verification Results (37/37 PASS)

| Test | Result |
|------|--------|
| SDF Decoder standalone (shape, finite, loss) | 7/7 PASS |
| EE Extractor standalone | 2/2 PASS |
| Pi0 model load + hook | 4/4 PASS |
| Data loading + forward pass | 5/5 PASS |
| Hook capture verification | 4/4 PASS |
| SDF loss with real features | 3/3 PASS |
| EE position loss | 1/1 PASS |
| Phase 1 backward (frozen) | 5/5 PASS |
| Phase 2 backward (unfrozen) | 4/4 PASS |
| Full optimizer step | 2/2 PASS |

Peak GPU memory: 62.93 GB (single batch, B=2)

## Files Deployed
```
/root/colliforce-vla/
├── colliforce/
│   ├── __init__.py
│   ├── sdf_decoder.py     # 4-layer MLP, skip@L2, Softplus(β=5)
│   └── ee_extractor.py    # 2-layer MLP → xyz
├── scripts/
│   ├── train_a1_sdf_aux.py  # Full training script
│   └── verify_a1.py         # 37-check verification
└── data/
    └── a1_integration_report.txt
```

## Usage
```bash
# Dry-run (2 steps)
CUDA_VISIBLE_DEVICES=3 python scripts/train_a1_sdf_aux.py --scene spatial_bowl --dry_run

# Full training
CUDA_VISIBLE_DEVICES=3 python scripts/train_a1_sdf_aux.py --scene spatial_bowl --seed 0
```

## Gotchas Discovered
1. **No LoRA in PyTorch**: openpi's PyTorch PI0 model has no separate LoRA adapters. `gemma_300m_lora` config only affects Flax/JAX. All parameters are full-rank in PyTorch → Phase 2 unfreezes all params.
2. **action_dim=32**: Pi0 base model uses action_dim=32, not 7. LIBERO's 7-dim actions are zero-padded to 32 by `PadStatesAndActions` transform.
3. **State float64**: Data loader returns `observation.state` as float64. Must `.float()` before MSE loss.
4. **Norm stats path**: Must use `AssetsConfig(assets_dir=...)` to point to precomputed norm stats from baseline training.
