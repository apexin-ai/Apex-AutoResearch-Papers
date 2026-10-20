# New Scripts Manifest (2026-05-15)

## Code Change
- **training/pretrain_weighted.py**: Added `golden_ratio` weighting method
  - L8: docstring updated (4 methods)
  - L153-160: `compute_loss` branch — q>0.5 → w=1/φ≈0.618, q≤0.5 → w=1.0, normalized to sum=batch_size
  - L222: argparse choices updated

## Training Scripts

| Script | Method | batch_size | grad_accum | effective_batch | n_min | output_dir |
|--------|--------|-----------|-----------|----------------|-------|------------|
| `run_golden_ratio_seed42.sh` | golden_ratio | 4 | 4 | 16 | auto (2) | output/models/golden_ratio_seed42 |
| `run_batchsize8_seed42.sh` | adaptive | 8 | 2 | 16 | 2 | output/models/batchsize8_seed42 |
| `run_batchsize16_seed42.sh` | adaptive | 16 | 1 | 16 | 2 | output/models/batchsize16_seed42 |

Common params: seed=42, lr=5e-5, max_length=2048, num_train_tokens=200M, bf16, WANDB_MODE=disabled, eval_steps=500, save_steps=500, contamination_ratio=0.4, model=Qwen3-0.6B
