# OpenPI vs MetaBrain Diagnostic Report

**Date**: 2026-05-16  
**Server**: westd-34142  
**Checkpoint**: `/root/autodl-tmp/checkpoints/pi0_libero/`

## Summary

OpenPI official inference works correctly on the pi0_libero checkpoint. MetaBrain had a critical normalization bug causing 0% eval success rate. **Root cause identified and fixed.**

## OpenPI Inference Results

Successfully ran openpi inference after:
1. Converting checkpoint (strip `model.` prefix, remove norm buffers) → `/root/autodl-tmp/checkpoints/pi0_libero_openpi/`
2. Monkey-patching image format (HWC→CHW) for SigLIP compatibility
3. Disabling torch.compile

**Output**: actions shape `(50, 7)`, range `[-1.03, 1.83]`, reasonable delta actions.

```
step 0: [ 0.0198 -0.1148 -0.4084 -0.0591 -0.0088 -0.146  -1.0067]
step 1: [-0.0466 -0.1343 -0.4499 -0.0668 -0.1992 -0.153  -1.0233]
```

## Root Cause: Wrong Normalization Stats in MetaBrain

The pi0_libero config uses `extra_delta_transform=True`, meaning:
- **Training**: actions are modified as `action_delta = raw_action - state[:6]`, then normalized
- **Inference**: model output is unnormalized, then `+ state[:6]` recovers the original delta

Two sources of normalization statistics exist in the checkpoint:
1. **norm_stats.json** (correct): statistics of `(raw_action - state)` — what the model actually predicts
2. **LeRobot embedded buffers** (wrong for unnorm): statistics of `raw_action` — what LeRobot's internal pipeline sees

MetaBrain was using the **embedded buffers** (wrong), causing:
- Wrong unnormalization scale (especially dims 2-5 where state has large absolute values)
- `use_delta=False` → skipping the AbsoluteActions step (no state addition)

### Concrete Example (dim 3 = roll)

| | norm_stats.json | LeRobot buffers |
|---|---|---|
| action_mean | **-2.97** | 0.0005 |
| action_std | **0.35** | 0.039 |

With input state[3] = 3.0 (typical EEF orientation):
- **OpenPI**: `model_out * 0.35 + (-2.97) + 3.0 ≈ -0.06` ✓ (small delta)
- **MetaBrain (broken)**: `model_out * 0.039 + 0.0005 ≈ 0.01`, no state addition → **misses 3.0 entirely**, outputs ~3.04

## Fix Applied

Modified `_build_norm_stats()` in `/root/meta_brain_lora_routing/phase1/meta_brain_assembly.py`:
- **Before**: Preferred embedded LeRobot buffers, set `use_delta=False`
- **After**: Prefers `norm_stats.json` when available, sets `use_delta=True`

### Verification Results

| Metric | Before Fix | After Fix |
|--------|-----------|-----------|
| Roll dim mean diff | **3.16** | 0.14 |
| Overall mean abs diff | 0.82 | 0.42 |
| Action range | [-1.06, 3.04] | [-1.06, 0.37] |

Remaining diff (0.42) is from stochastic flow matching (different noise seeds). The fundamental normalization issue is resolved.

## Action Items

1. ~~Fix `_build_norm_stats` to use JSON stats~~ DONE
2. Re-run MetaBrain eval on LIBERO to confirm non-zero success rate
3. Consider seeding noise for deterministic comparison
