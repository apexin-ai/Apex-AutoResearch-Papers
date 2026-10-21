# Falcon3-7B-Base DiD Analysis — Data Availability Report

**Date**: 2026-05-22  
**Status**: BLOCKED — missing d000 baseline

## Available Data on cqa1-21977

| Component | Path | Status |
|-----------|------|--------|
| Falcon3 base model (HF cache) | `/root/autodl-tmp/.hf_cache/Falcon3-7B-Base` | ✅ |
| SFT checkpoint d100_s42 | `/root/autodl-tmp/exp001/checkpoints/Falcon3-7B-Base_d100_s42` | ✅ |
| Eval d100 correctness_matrix | `/root/autodl-tmp/exp001/eval_results/Falcon3-7B-Base_d100_s42_aligned/correctness_matrix.json` | ✅ |
| Contamination labels (all dosages) | `/root/autodl-tmp/exp001/sft_data/contamination_labels_{mmlu,arc_challenge,gsm8k}_{d005..d100}.json` | ✅ |
| SFT checkpoint d000_s42 | — | ❌ Never trained |
| Eval d000 correctness_matrix | — | ❌ Does not exist |
| SFT checkpoint d005/d025/d050 | — | ❌ Never trained |

## Why DiD Cannot Run

The DiD script (`falcon3_did_analysis.py`) computes:

```
DiD = (treated_acc_d100 - treated_acc_d000) - (untreated_acc_d100 - untreated_acc_d000)
```

This requires `Falcon3-7B-Base_d000_s42_aligned/correctness_matrix.json` as baseline, which does not exist because no Falcon3 d000 (clean SFT, 0% contamination) checkpoint was ever trained.

## Options to Unblock

### Option A: Train Falcon3 d000 SFT (recommended)
- Train `Falcon3-7B-Base_d000_s42` using the same SFT config as d100 but with 0% contamination data
- Run eval to produce correctness_matrix.json
- Then DiD analysis works for d000→d100 comparison
- **Pros**: Clean, proper DiD with matched SFT conditions
- **Cons**: Requires GPU time for training + eval

### Option B: Eval pretrained Falcon3-7B-Base as d000 proxy
- Run the eval pipeline on the raw pretrained model (no SFT)
- Use as approximate baseline
- **Pros**: Faster (no training, just eval)
- **Cons**: Confounds SFT effect with contamination effect; less clean than Option A

### Option C: Single-snapshot treated vs untreated (d100 only)
- Compare treated vs untreated item accuracy within d100 alone
- No pre-post comparison, so not a real DiD
- **Pros**: Can run immediately with existing data
- **Cons**: Cannot control for pre-existing item difficulty differences; weaker evidence

## Comparison with Other Cross-Family Models

| Model | d000 | d005 | d025 | d050 | d100 | DiD Ready? |
|-------|------|------|------|------|------|------------|
| Llama-3.2-3B | ✅ | ✅ | ✅ | — | ✅ | ✅ Yes |
| Falcon3-7B-Base | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ No |
| Gemma-2-9B | ckpt only | ckpt only | ckpt only | ckpt only | — | ❌ No eval |

## Existing Analysis Infrastructure on cqa1

- No `treated_untreated_analysis.py` found on cqa1
- Analysis scripts in `/root/contamcal-irt-calibration/analysis/`: IRT fitting, signal analysis, classification sensitivity, bootstrap stability — none are DiD scripts
- The `falcon3_did_analysis.py` would need to be synced to cqa1 to run
