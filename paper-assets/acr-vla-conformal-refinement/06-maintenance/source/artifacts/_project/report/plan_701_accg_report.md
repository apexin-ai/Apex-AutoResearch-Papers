# Plan 701 Execution Report
Date: 2026-05-17

## Part 1: FiLM -> Action-Conditioned Correction Gating (ACCG)

### What was replaced
FiLM (Feature-wise Linear Modulation) conditioning in `crm_k1_model.py`:
- Static `film_scale` parameter: `nn.Parameter(torch.ones(num_scale_layers, bottleneck_dim))`
- Static `film_shift` parameter: `nn.Parameter(torch.zeros(num_scale_layers, bottleneck_dim))`
- Forward: `p = p * self.film_scale[idx] + self.film_shift[idx]` (affine transform per layer)

### What replaced it
Action-Conditioned Correction Gating (ACCG), motivated by VLA correction mechanics:

```python
self.correction_gate = nn.Sequential(
    nn.Linear(action_dim, bottleneck_dim),  # 30 -> 192
    nn.Sigmoid(),
)
self.layer_importance = nn.Parameter(torch.zeros(num_scale_layers))  # 4 params
```

Forward:
```python
gate = self.correction_gate(action_norm)  # (B, 192), dynamic per-sample
layer_w = F.softmax(self.layer_importance, dim=0)  # learned per-layer weights
p = self.layer_proj(feat_norm) * gate * layer_w[idx]  # gated + weighted
```

### Design motivation
The proposed VLA action encodes the error pattern: spatial misalignment activates different correction dimensions than wrong grasp angle or wrong target. FiLM's static per-layer affine transform cannot adapt to per-sample error structure. ACCG uses the action itself to compute dynamic, input-dependent gates that select which projected feature dimensions carry correction signal.

### Parameter count
Total: 327,522 (within 320K +/- 20% = 256K-384K)
- layer_proj: 184,512
- correction_gate: 5,952
- layer_importance: 4
- action_query_proj: 5,952
- MLP: 131,102

### Verification
- Forward pass: multi-scale (4x960D) and fallback (1x960D) both produce (B, 30)
- Epsilon-bound clipping: delta norms <= max_correction_norm verified
- Gradient flow: all modules receive gradients
- Inference: Single linear + sigmoid gate, no additional overhead vs FiLM

---

## Part 2: Reviewer Warning Fixes

### A. --no_wandb flag (NEW)
Added `--no_wandb` argument to `train_crm_k1.py`:
```python
p.add_argument("--no_wandb", action="store_true", help="Disable W&B logging for debug runs")
```
W&B init now uses:
```python
wandb.init(
    project=args.wandb_project,
    name=args.wandb_run_name,
    mode="disabled" if args.no_wandb else "online",
    config={...}
)
```

### B. W&B logging keys
Updated wandb.log keys with `train/` and `val/` prefixes:
```python
log_dict = {
    "train/loss": avg_train_loss,
    "val/loss": avg_val_loss,
    "train/lr": scheduler.get_last_lr()[0],
    "train/epoch": epoch,
}
# loss components: log_dict[f"train/{k}_loss"] = v
```

### C. Batch precompute
Already implemented in current code (contrary to task description). Precompute uses `--precompute_batch_size` (default 4) with DataLoader for batched feature extraction.

---

## Part 3: Training Command (plan_701)

**Ready to submit, awaiting Director approval.**

```bash
CUDA_VISIBLE_DEVICES=1 bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement/src && python -u train_crm_k1.py --benchmark object --epochs 50 --batch_size 512 --lr 1e-3 --seed 42 --loss_mode multi --lambda_dir 0.1 --lambda_tri 0.05 --lambda_mag 0.01 --max_correction_norm 0.2 --wandb_project acr-vla-conformal-refinement --wandb_run_name crm-k1-v2-accg-object --auto"
```

Notes:
- `--auto` triggers precompute if K=1 cache is empty, then trains
- GPU 1 on bjb2-28827 (4090)
- K=1 precompute cache does not yet exist; will be created automatically
- Precompute requires SmolVLA model at `/root/autodl-tmp/models/smolvla_libero/`

---

## Part 4: File Sync

### Files synced
| File | Source | Targets |
|------|--------|---------|
| crm_k1_model.py | bjb2-28827 | bjb1-18228, bjb1-32546 |
| train_crm_k1.py | bjb2-28827 | bjb1-18228, bjb1-32546 |

### MD5 verification (all match)
| File | MD5 |
|------|-----|
| crm_k1_model.py | 0fa57e832133ed3d38dc1b641bed02eb |
| train_crm_k1.py | 5b08fffd994951be545c8f65ef48605e |

### Backup
FiLM version backed up on bjb2-28827 as `crm_k1_model.py.bak_film`
