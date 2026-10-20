# Pythia-1.4B MAUVE=None Bug Diagnosis

## Root Cause

**Two-layer failure:**

1. **Environment bug (primary):** The 1.4B experiment launch commands on westd-17855 did NOT set `HF_HOME=/root/autodl-tmp/.hf_cache` or `TRANSFORMERS_OFFLINE=1`. Without these, the MAUVE library tried to download the GPT-2-large featurizer from huggingface.co, which is unreachable from AutoDL (network restriction). The cached model exists at `/root/autodl-tmp/.hf_cache/hub/models--gpt2-large/` but MAUVE looked in the default `~/.cache/huggingface/` (empty).

2. **Code bug (secondary):** `metrics.py:343` set `results["mauve"] = None` on failure (other metrics use `float("nan")`). Then `iterative_train.py:358` tried `f"mauve={metrics['mauve']:.4f}"` which crashes on `None.__format__`.

The 410M experiments that worked either (a) had `HF_HOME` set correctly in the launch command, or (b) ran when the network happened to be accessible.

## Crash Details

| Experiment | Crashed at | Training OK? | Checkpoint saved? |
|---|---|---|---|
| scale_14b_t10_a060_s42_fp32 | Gen 1, after metrics compute | Yes (5000 steps, loss=1.928) | Yes (5.3G) |
| scale_14b_t10_a075_s42_fp32 | Gen 1, after metrics compute | Yes (5000 steps, loss=1.655) | Yes (5.3G) |

MAUVE also failed at Gen 0 (baseline) but didn't crash because Gen 0's print statement doesn't format MAUVE.

## Checkpoint Status

Both experiments have:
- `gen_0/`: metrics.json + synthetic_data (no checkpoint — baseline uses original model)
- `gen_1/`: checkpoint (5.3G, complete) + metrics.json (mauve=null) + synthetic_data + trainer dir
- No `all_metrics.json` (crash prevented consolidation)

## Code Fixes Applied

### 1. `metrics.py` line 343
```python
# Before:
results["mauve"] = None
# After:
results["mauve"] = float("nan")
```

### 2. `iterative_train.py` line 358
```python
# Before:
f"mauve={metrics['mauve']:.4f}"
# After:
f"mauve={metrics.get('mauve', float('nan')):.4f}"
```

Fixes applied to: westd-17855, westd-19828, local artifacts/

## Resume Instructions

Both experiments can resume from gen 2 using `--start_gen 2`. The launch command **must** include:
```bash
export HF_HOME=/root/autodl-tmp/.hf_cache
export TRANSFORMERS_OFFLINE=1
export HF_HUB_OFFLINE=1
```

The gen_1 metrics.json files have `mauve: null` — these will need to be recomputed or left as-is (they won't block resume since the checkpoint is complete).
