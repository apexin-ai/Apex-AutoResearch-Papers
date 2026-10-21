# 14B Scorer Confound Contingency: Prep Report

**Date:** 2025-05-18
**Server:** cqa1-22115

## 1. Model

| Item | Value |
|------|-------|
| Model | Qwen2.5-14B-Instruct-AWQ |
| Quantization | AWQ 4-bit (group_size=128, zero_point=True) |
| Disk path | `/root/autodl-tmp/.hf_cache/Qwen2.5-14B-Instruct-AWQ/` |
| Disk size | 9.4 GB |
| GPU memory (loaded) | 9.98 GB |
| GPU peak memory | 13.09 GB |
| Target GPU | Single 4090D (24 GB) |

**Why AWQ-4bit instead of GPTQ-Int8:**
- Qwen official does not publish GPTQ-Int8 or AWQ quantization for base (non-Instruct) 14B model
- `gptqmodel` package failed to build on current environment (pyproject.toml metadata issue with transformers 5.8.1)
- AWQ 4-bit loads via `autoawq` backend, validated working
- 4-bit AWQ (14B params) still has far more capacity than fp16 1.5B, sufficient to test the scorer-capacity confound

**Why Instruct instead of Base:**
- No quantized base 14B model available from Qwen
- Downloading unquantized Qwen2.5-14B base (~28GB fp16) would require bitsandbytes dynamic int8 quantization
- For scorer use (surprisal/perplexity computation), the Instruct vs Base distinction is secondary to model capacity (14B vs 1.5B)

## 2. Installed Dependencies

| Package | Version |
|---------|---------|
| autoawq | 0.2.9 |
| bitsandbytes | (installed, version TBD) |
| accelerate | (installed) |
| transformers | 5.8.1 |
| torch | 2.8.0+cu128 |

## 3. Scoring Scripts

### Main script
`/root/autodl-tmp/gen-depth-contamination/scripts/score_14b_confound.py`

- Imports feature extraction functions from `run_pipeline.py` (no code duplication)
- Loads AWQ model with `AwqConfig(backend='autoawq')` + `low_cpu_mem_usage=True`
- Creates working data dir with symlinks to source depth files
- Saves `features.csv` in the working dir, then runs `run_analysis()`

### Shell launcher
`/root/autodl-tmp/gen-depth-contamination/scripts/exp_14b_scorer_confound.sh`

Key parameters to update before running:
- `SRC_DATA_DIR`: set to wherever exp_14b_c4 depth chain output lands (default: `data/exp_14b_c4`)
- `CUDA_VISIBLE_DEVICES`: pick a free GPU (default: 0)

### How to run
```bash
cd /root/autodl-tmp/gen-depth-contamination
CUDA_VISIBLE_DEVICES=0 bash scripts/exp_14b_scorer_confound.sh
```

Or directly:
```bash
CUDA_VISIBLE_DEVICES=0 python scripts/score_14b_confound.py \
    --src_data_dir data/exp_14b_c4 \
    --results_dir results_14b_scorer_confound \
    --max_depth 5 --batch_size 8
```

## 4. Dry-Run Results

| Metric | Value |
|--------|-------|
| Model load time | 9.4s (includes first-run Marlin kernel compilation) |
| Batch-16 forward pass | 0.08s (5ms/sample) |
| Surprisal text 0 | 3.28 bits |
| Surprisal text 1 | 3.64 bits |
| Surprisal text 2 | 2.50 bits |

Model loaded and forward pass ran correctly. Surprisal values are reasonable.

## 5. Time Estimates

| Step | Estimate |
|------|----------|
| Model loading | ~10s (subsequent runs, kernels cached) |
| Surprisal extraction (30k samples) | ~2 min |
| Vocab diversity + tail features | ~5-10 min (self-BLEU is CPU-bound) |
| LightGBM analysis | ~1 min |
| **Total** | **~15-20 min** |

## 6. Blockers

- **Waiting for exp_14b_c4 data**: `data/exp_14b_c4/depth_{0..5}.jsonl` must exist before running
- **GPU contention**: GPU 1 currently occupied by `exp_wiki_scorer_confound_1b5` (process 180548). Use GPU 0, 2, or 3.

## 7. Expected Output

```
results_14b_scorer_confound/
  data_14b_scored/
    depth_0.jsonl -> (symlink to source)
    ...
    depth_5.jsonl -> (symlink to source)
    features.csv          # 14B scorer features
  pairwise_auc.json
  kstar.json
  summary.txt
```

Compare `summary.txt` K* values with 1.5B scorer results to determine if scorer capacity is a confound.
