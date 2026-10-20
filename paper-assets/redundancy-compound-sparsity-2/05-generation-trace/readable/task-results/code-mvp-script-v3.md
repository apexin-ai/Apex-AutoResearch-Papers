# code mvp script v3

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_script_v3_20260512T084432_result.json`
- **Structured JSON:** [`5af324821d7b14fd19e8.json`](../../sessions/5a/5af324821d7b14fd19e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All changes complete. Here's a summary of what was modified:

### carc_utils.py
- **`EMAAnchorManager`**: Added `num_kv_heads` and `per_head` params. New `_compute_scores_per_head()` does per-head cosine similarity with variance-aware head weighting. Original concatenated implementation preserved as `_compute_scores_concat()` fallback.
- **`residualize(x, z)`**: OLS residualization for position-controlled partial correlations.
- **`load_math_data()`**: Loads problems from `hendrycks/competition_math` test split, formats as CoT prompts.
- Added `import numpy as np`.

### carc_mvp.py — 7 changes
1. **MATH-500 reasoning traces**: `--dataset math` (new default) generates chains via `model.generate()` before analysis. Generation runs with no hooks.
2. **Measurement (c)**: Surprisal computed from baseline logits; Pearson r(EMA, -surprisal) reported.
3. **Measurement (a)**: MLP gate_proj near-zero fractions captured during baseline via hooks, split by EMA redundancy.
4. **Measurement (d)**: 4th forward pass with `sparse_twotier` mode routes tokens by EMA score (redundant@55%, novel@40%). PPL comparison with uniform@40%.
5. **Measurement (e)**: Position-residualized partial correlations for both EMA↔perturbation and EMA↔surprisal.
6. **Multi-chain statistics**: Chain-level Pearson r across 60 independent chains, median lag-1 autocorrelation diagnostic.
7. **Per-head EMA**: `--per-head` (default) / `--no-per-head` flag. Reads `num_key_value_heads` from model config.
8. **Refined `judge()`**: PASS-Strong (|r|>0.5 AND diff≥20%) / PASS-Suggestive / DISCORDANT-A / DISCORDANT-B / FAIL.

---
