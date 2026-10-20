# GSM8K Profiling Preparation Report

## Overview

GSM8K (n=50) profiling adapter for cross-dataset validation of compound interaction severity. Code prepared and dry-run validated on westd-22162.

## Files on Server (`/root/autodl-tmp/pacs/`)

| File | Description |
|------|-------------|
| `run_profiling_gsm8k.py` | Main profiling script (standalone, based on `run_profiling_qwen.py`) |
| `data/gsm8k_test.json` | Pre-downloaded GSM8K test split (1319 problems) |
| `run_gsm8k_ds_gpu0.sh` | DeepSeek: imp+rand × 4 sparsity on GPU 0 |
| `run_gsm8k_qw_gpu1.sh` | Qwen: imp+rand × 4 sparsity on GPU 1 |
| `gsm8k_profiling/` | Output directory |

## Launch Commands

```bash
# Terminal 1 — DeepSeek on GPU 0
nohup bash run_gsm8k_ds_gpu0.sh > gsm8k_profiling/ds_full.log 2>&1 &

# Terminal 2 — Qwen on GPU 1
nohup bash run_gsm8k_qw_gpu1.sh > gsm8k_profiling/qw_full.log 2>&1 &
```

Both scripts run sequentially through 8 conditions each (importance/random × s=0.15/0.20/0.25/0.30). The two models run in parallel on separate GPUs.

## Estimated Runtime

| Component | Time |
|-----------|------|
| Model loading | ~5s per invocation |
| Per problem (generation + II profiling) | ~45-55s |
| Per condition (50 problems) | ~40 min |
| Per model (8 conditions, sequential) | ~5.3 hours |
| **Total wall time (2 GPUs parallel)** | **~5.5 hours** |

## Dry-Run Results

### Run 1: 1 problem × 128 tokens (quick sanity)
- Pipeline loads GSM8K, generates text, segments phases, computes II
- With 128 tokens only 1 phase detected (expected for short sequences)

### Run 2: 2 problems × 2048 tokens (full validation)
- Problem 0 (`gsm8k_test/13`): 18 phases, ii_high=0.00076, ii_mid=0.0, ii_low=0.0
- Problem 1 (`gsm8k_test/51`): 11 phases, ii_high=-0.0147, ii_mid=None, ii_low=None
- Phase stats: high=470 tokens (12 segments), low=648 tokens (12 segments), mid=449 tokens (5 segments)
- II[high_sparsity, 0.15]: mean=-0.0037, CI=[-0.0127, +0.0063]
- Output JSON loads correctly, `per_problem_ii` format compatible with `extract_table2.py`

## Differences from MATH-500

| Aspect | MATH-500 | GSM8K |
|--------|----------|-------|
| Data source | Local JSON (`data/math500.json`) | Local JSON (`data/gsm8k_test.json`), pre-downloaded from HuggingFace |
| Sampling | Stratified by difficulty level (10 per level × 5 levels = 50) | Random sample (seed=42, n=50 from 1319) |
| Problem field | `"problem"` | `"question"` (mapped to `"problem"` in adapter) |
| Answer format | LaTeX boxed answer | `#### <number>` final answer |
| Prompt template | `"Solve the following math problem step by step.\n\nProblem: {text}\n\nSolution:"` | **Identical** |
| Profiling logic | Same | Same |
| II formula | `r_both - r_attn - r_kv + 1` | **Identical** |
| Phase segmentation | Quantile-based (3 groups) | **Identical** |
| Output format | JSON with `per_problem_ii` | **Identical** |

## Output Structure

Each condition produces `gsm8k_profiling/{model}_{method}_s{sparsity}/profiling_results.json` with:
- `config`: model path, dataset="gsm8k", sparsity levels, masking method
- `phase_stats`: per-phase token/segment counts
- `perplexity`: per-phase mean PPL under 4 conditions (dense/attn/kv/both)
- `interaction_index`: per-phase II with bootstrap 95% CI
- `per_problem_ii`: per-problem II values (compatible with `extract_table2.py`)
- `pass_fail`: CI overlap test + sign reversal test
- `diagnostics`: per-problem sparsity values

## Conditions Matrix

| Model | Method | Sparsity | Output Dir |
|-------|--------|----------|------------|
| DeepSeek-R1-Distill-Qwen-7B | importance | 0.15, 0.20, 0.25, 0.30 | `gsm8k_profiling/ds_imp_s{015,020,025,030}/` |
| DeepSeek-R1-Distill-Qwen-7B | random | 0.15, 0.20, 0.25, 0.30 | `gsm8k_profiling/ds_rand_s{015,020,025,030}/` |
| Qwen2.5-7B-Instruct | importance | 0.15, 0.20, 0.25, 0.30 | `gsm8k_profiling/qw_imp_s{015,020,025,030}/` |
| Qwen2.5-7B-Instruct | random | 0.15, 0.20, 0.25, 0.30 | `gsm8k_profiling/qw_rand_s{015,020,025,030}/` |

Total: 2 models × 2 methods × 4 sparsity = 16 output directories.
