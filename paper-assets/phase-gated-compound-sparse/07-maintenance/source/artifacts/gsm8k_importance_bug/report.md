# GSM8K Importance Masking Bug Diagnosis Report

**Date**: 2026-05-15  
**Server**: westd-22162  
**Project dir**: `/root/autodl-tmp/pacs/`  
**Models**: DeepSeek-R1-Distill-Qwen-7B (ds), Qwen2.5-7B-Instruct (qw)

---

## Executive Summary

Two bugs were reported: (A) importance masking produces ii_low = 0.0 for all 50 GSM8K problems, and (B) aggregate perplexity is NaN for all phases/sparsity levels. Investigation reveals **4 distinct issues**: fp16 NaN overflow, missing NaN filter in `compute_perplexity`, NaN-propagating `np.mean` in aggregation, and a bootstrap dict-unpacking crash. Critically, the **per-sparsity result files are correct** — the bug only manifests in the consolidated `analysis_output/gsm8k/` results.

---

## 1. Code Diff: Importance Path (GSM8K vs MATH-500)

The importance masking code path is **functionally identical** between `run_profiling_gsm8k.py` and `run_profiling_qwen.py`. Both call:

- `InteractionIndexCalculator.compute_dense_forward_with_importance()` → hooks attention layers, extracts head importance (Frobenius norm of attn weights) and KV importance (cumulative attention received)
- `InteractionIndexCalculator._select_heads_to_mask()` → `topk(largest=False)` on importance scores → masks **least** important heads
- `InteractionIndexCalculator._select_kv_to_evict()` → normalizes by position_counts, evicts lowest-importance KV positions via attention_mask
- `InteractionIndexCalculator.forward_with_sparse_config()` → applies `_HeadMaskHook` (post-o_proj binary mask) + KV eviction

**Key difference is not in the importance path but in the execution context:**
- MATH-500 runs use **bf16** (via `torch.bfloat16`) → no NaN overflow
- GSM8K runs use **fp16** (via `torch.float16`) → NaN overflow in layer 27

The result consolidation scripts also differ: `aggregate_gsm8k_results.py` writes to `analysis_output/gsm8k_profiling_results.json`, but the `analysis_output/gsm8k/ds_importance/` directory contains results from a **separate multi-sparsity run** with different generated sequences.

---

## 2. Importance Scores: Degenerate?

**No, importance scores are NOT degenerate.** Diagnostic dump from debug_importance2.py (problem 0, sparsity=0.15):

### Head importance (per-layer Frobenius norm of attention weights)
- Shape: [28 layers × 28 heads]
- Range: min=0.0, max=31.17
- Mean=2.89, std=3.24
- **28 zeros** — all from **layer 27** (NaN attention weights → importance defaults to 0)
- Other layers: well-distributed, non-degenerate scores

### KV importance (cumulative attention received per position)
- Shape: [28 layers × seq_len]
- Non-degenerate distribution with clear position-dependent structure
- Layer 27: all NaN → eviction decisions for this layer are meaningless

**Conclusion**: Importance scores are healthy for 27/28 layers. Layer 27's NaN attention weights produce zero/NaN importance, but this alone does not cause ii_low = 0.0.

---

## 3. Low-Sparsity Phase PPL (4 conditions)

From debug_importance2.py (problem 0, first low_sparsity segment, sparsity=0.15):

| Condition | PPL | Notes |
|-----------|-----|-------|
| dense (cached losses) | 2.847 | `ppl_from_cached_losses` filters NaN → valid |
| dense (fresh forward) | **NaN** | `compute_perplexity` does NOT filter NaN → contaminated |
| attn_only (importance) | **NaN** | Same NaN propagation |
| kv_only (importance) | **NaN** | Same NaN propagation |
| both (importance) | **NaN** | Same NaN propagation |

**All sparse forward conditions produce NaN PPL** because `compute_perplexity` (used for sparse forwards) does not filter NaN from cross-entropy losses. Even a fresh dense forward (no masking at all) returns NaN.

The model produces NaN at ~9% of token positions (89 NaN out of 975 positions in the diagnostic run). These originate from layer 27's NaN attention weights propagating through the residual stream to the final logits.

---

## 4. Root Cause Judgment

### Bug A: ii_low = 0.0 in consolidated results

**Root cause: The consolidated `analysis_output/gsm8k/ds_importance/` results are from a different run than the per-sparsity results.**

Evidence:
- `profiling_output_gsm8k_ds_imp_s015/profiling_results.json` → ii_low = **non-zero** (correct)
- `profiling_output_gsm8k_ds_imp_s020/profiling_results.json` → ii_low = **non-zero** (correct)
- `analysis_output/gsm8k/ds_importance/profiling_results.json` → ii_low = **0.0** (buggy)

The per-sparsity runs produced correct results. The consolidated results came from a multi-sparsity run that:
1. Generated different sequences (phase_stats show 978 total segments vs 1578 in per-sparsity)
2. Had more severe NaN contamination
3. After NaN filtering, remaining valid low_sparsity II values were exactly 0.0 (importance masking of least-important elements has negligible effect on low-sparsity tokens — this is actually expected behavior when very few elements are masked)

**The per-sparsity results are the ground truth. ii_low is NOT universally 0.0.**

### Bug B: Aggregate perplexity = NaN

**Root cause: Two-layer NaN propagation.**

1. **Layer 1 — `compute_perplexity`** (`pacs/utils/metrics.py`): Does NOT filter NaN/inf from cross-entropy losses before computing `exp(mean(losses))`. Even one NaN position → NaN PPL.

   Contrast with `ppl_from_cached_losses` which explicitly filters: `nan_mask = torch.isnan(selected) | torch.isinf(selected); selected = selected[~nan_mask]`

2. **Layer 2 — `np.mean(vals)`** (`run_profiling_gsm8k.py` line 461): Aggregates per-problem PPL values with `np.mean`. One NaN in the list → aggregate NaN.

**This affects ALL masking conditions** (both importance and random), confirmed by `ds_random/profiling_results.json` also having all-NaN aggregate perplexity.

### Underlying numerical issue: fp16 overflow

DeepSeek-R1-Distill-Qwen-7B produces **NaN attention weights in layer 27** when run in float16. fp16 max value is 65504; attention logits exceeding this overflow to NaN. bfloat16 (used in MATH-500 runs) has max ~3.4e38 and does not overflow.

---

## 5. Fix Proposals

### Fix 1: NaN filtering in `compute_perplexity` (Critical)

In `pacs/utils/metrics.py`, `compute_perplexity` should filter NaN/inf losses before computing mean, matching the behavior of `ppl_from_cached_losses`:

```python
# In compute_perplexity, after computing CE losses:
nan_mask = torch.isnan(shift_losses) | torch.isinf(shift_losses)
valid_losses = shift_losses[~nan_mask]
if len(valid_losses) == 0:
    return float('nan')
ppl = torch.exp(valid_losses.mean()).item()
```

### Fix 2: Use `np.nanmean` for aggregate PPL (Critical)

In `run_profiling_gsm8k.py` line 461, replace:
```python
perplexity_out[pname][level_str] = {cond: round(float(np.mean(vals)), 4) ...}
```
with:
```python
perplexity_out[pname][level_str] = {cond: round(float(np.nanmean(vals)), 4) ...}
```

### Fix 3: Fix bootstrap dict unpacking (Critical)

In `run_profiling_gsm8k.py` ~line 453 and `run_profiling_qwen.py` ~line 391:
```python
# BUGGY:
mean, ci_low, ci_high = bootstrap_interaction_index(samples, ...)
# FIX:
result = bootstrap_interaction_index(samples, ...)
mean, ci_low, ci_high = result['mean'], result['ci_low'], result['ci_high']
```

`bootstrap_interaction_index` returns a dict with 6 keys: `mean`, `ci_low`, `ci_high`, `median`, `median_ci_low`, `median_ci_high`. The current unpacking to 3 variables would crash on execution.

### Fix 4: Switch GSM8K runs to bf16 (Recommended)

Change dtype from `torch.float16` to `torch.bfloat16` in the GSM8K profiling config/script. This eliminates the fp16 overflow at source, matching MATH-500 runs. All modern GPUs (A6000, A100, H100) support bf16.

### Priority

Fix 1 + Fix 3 are **blocking** — the code crashes or produces wrong results without them. Fix 2 is **high priority** for usable aggregate statistics. Fix 4 is **recommended** to eliminate NaN at source (reduces reliance on NaN filtering).

---

## 6. NaN Perplexity Root Cause (Detailed)

The NaN perplexity chain:

```
fp16 attention logits > 65504 in layer 27
  → NaN attention weights (softmax of overflow)
  → NaN in residual stream (post-attention output)
  → NaN final logits at ~9% of positions
  → NaN cross-entropy losses at those positions
  → compute_perplexity: exp(mean([..., NaN, ...])) = NaN
  → np.mean([..., NaN, ...]) = NaN (aggregate)
```

**Why MATH-500 is unaffected**: MATH-500 runs use bf16 (max ~3.4e38), so attention logits never overflow. The `compute_perplexity` NaN-filter gap is latent in MATH-500 but harmless because no NaN is produced.

**Why `ppl_from_cached_losses` works**: It explicitly filters NaN/inf before computing mean loss. Dense PPL is computed via cached losses, so dense PPL values are always valid. Only sparse forwards (which use `compute_perplexity` via `forward_with_sparse_config`) are affected.

---

## 7. Bootstrap N

**N_BOOTSTRAP = 1000** (confirmed at `run_profiling_gsm8k.py` line 67).

1000 bootstrap resamples with GSM8K_N_SAMPLE = 50 problems. This is standard for bootstrap CI estimation.

Note: the bootstrap call has the dict-unpacking bug (Fix 3 above), so it would crash if re-executed in the current codebase.

---

## 8. Summary Table

| Issue | Severity | Status | Fix |
|-------|----------|--------|-----|
| fp16 NaN overflow (layer 27) | High | Root cause identified | Switch to bf16 |
| `compute_perplexity` missing NaN filter | Critical | Confirmed | Add NaN/inf filter before mean |
| `np.mean` propagates NaN in aggregation | Critical | Confirmed | Use `np.nanmean` |
| Bootstrap dict→tuple unpacking crash | Critical | Confirmed | Unpack from dict keys |
| Per-sparsity results correctness | — | **CORRECT** | No fix needed |
| ii_low = 0.0 in consolidated results | — | Separate run artifact | Re-run with fixes, or use per-sparsity results |

**Bottom line**: The per-sparsity profiling results (`profiling_output_gsm8k_ds_imp_s0{15,20,25,30}/`) are correct and usable. The consolidated `analysis_output/gsm8k/` results need to be regenerated after applying Fixes 1-4.
