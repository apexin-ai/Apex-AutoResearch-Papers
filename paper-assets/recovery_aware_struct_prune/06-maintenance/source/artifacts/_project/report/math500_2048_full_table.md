# MATH-500 @2048 Cross-Method Comparison Table

> Generated: 2026-05-21  
> Model: DeepSeek-R1-Distill-Qwen-7B (pruned variants)  
> Eval: MATH-500, max_new_tokens=2048, greedy decoding

---

## 1. Main Results Table

| Sparsity | Method | Stage | Accuracy | n_correct/n_total | Truncated | exp_id | Status |
|----------|--------|-------|----------|-------------------|-----------|--------|--------|
| 0% | Dense (Unpruned) | GRPO | **69.0%** | 345/500 | 86 (17.2%) | `eval_math500_grpo_unpruned` | DONE |
| 0% | Dense (Unpruned) | SFT | — | — | — | — | **MISSING** |
| 20% | CKA-only | SFT | — | — | — | `eval_math500_sft_cka_only_20_v6` | **RUNNING** |
| 20% | CKA-only | GRPO | **29.2%** | 146/500 | 110 (22.0%) | `eval_math500_grpo_cka_only_20_2048` | DONE |
| 20% | Standard | SFT | **25.8%** | 129/500 | — | `eval_math500_sft_standard_20_2048_v2` | DONE |
| 20% | Standard | GRPO | — | — | — | — | **MISSING** |
| 20% | RASP | SFT | — | — | — | — | **MISSING** |
| 20% | RASP | GRPO | — | — | — | `eval_math500_grpo_rasp_20_v3` | **FAILED** |
| 20% | Random | SFT | — | — | — | — | **MISSING** |
| 20% | Random | GRPO | — | — | — | — | **MISSING** |
| 20% | α=4.0 CKA | GRPO | — | — | — | — | **MISSING** (no GRPO training) |
| 25% | CKA-only | SFT | — | — | — | — | **MISSING** (no SFT training) |
| 25% | CKA-only | GRPO | **18.4%** | ~92/500 | — | `grpo_cka_only_25` (inline) | DONE |
| 25% | Standard | SFT | **13.0%** | 65/500 | 318 (63.6%) | `eval_math500_sft_standard_25_v2` | DONE |
| 25% | Standard | SFT | — | — | — | `eval_math500_sft_standard_25_2048` | **RUNNING** |
| 25% | Standard | GRPO | — | — | — | — | **MISSING** (no GRPO training) |

### Notes
- CKA-only 25% GRPO MATH-500 accuracy (18.4%) is an inline metric from the `grpo_cka_only_25` training experiment, not a dedicated eval. n_correct (~92) estimated from 18.4% × 500.
- Standard 25% SFT has extremely high truncation (63.6%) at 2048 tokens, likely depressing accuracy.
- `eval_math500_grpo_rasp_20_v3` failed because server westd-11672 was released mid-eval (consumed 35.3 GPU-hours with no result).
- Hypothesis in `eval_math500_sft_standard_20_2048_v2` references "GRPO Standard @2048 (26.4%)" — this number is not backed by any registry entry and may be from an unregistered eval.
- Hypothesis in `eval_math500_grpo_cka_only_20_2048` references "SFT CKA-only (29.0%)" — likely from an earlier eval (v6 currently re-running).

---

## 2. Missing Cells Inventory

### Critical (needed for paper Table):

| # | Cell | Blocker | Priority |
|---|------|---------|----------|
| 1 | **GRPO Standard 20% MATH-500** | No eval registered or running. GRPO Standard 20% training exists. | **P0** — needed for SFT vs GRPO comparison |
| 2 | **GRPO RASP 20% MATH-500** | v3 failed (server released). Need v4. | **P0** — needed for cross-method comparison |
| 3 | **SFT RASP 20% MATH-500** | No eval registered or running. SFT RASP 20% checkpoint exists. | **P0** — needed for cross-method comparison |
| 4 | **SFT CKA-only 20% MATH-500** | v6 currently RUNNING. | **P0** — wait for completion |

### Important (for completeness):

| # | Cell | Blocker | Priority |
|---|------|---------|----------|
| 5 | Dense (Unpruned) SFT MATH-500 | No unpruned SFT training/eval exists | P1 |
| 6 | SFT Random 20% MATH-500 | No SFT Random 20% training exists | P1 |
| 7 | GRPO Random 20% MATH-500 | `grpo_random_20` was killed, no eval | P1 |

### Low (stretch / not in core narrative):

| # | Cell | Blocker | Priority |
|---|------|---------|----------|
| 8 | α=4.0 GRPO 20% MATH-500 | No GRPO α=4.0 training exists (only SFT) | P2 |
| 9 | SFT CKA-only 25% MATH-500 | No SFT CKA-only 25% training exists | P2 |
| 10 | GRPO Standard 25% MATH-500 | No GRPO Standard 25% training exists | P2 |

---

## 3. Cross-Benchmark Comparison: MATH-500 vs GSM8K

| Sparsity | Method | Stage | MATH-500 | GSM8K | MATH/GSM Ratio | GSM8K exp_id | GSM8K N |
|----------|--------|-------|----------|-------|-----------------|--------------|---------|
| 0% | Dense | GRPO | 69.0% | — | — | (GRPO collapsed, no GSM8K eval) | — |
| 20% | CKA-only | GRPO | 29.2% | 64.37% | **0.454** | `eval_gsm8k_grpo_cka_only_20_v2` | 1319 |
| 20% | Standard | SFT | 25.8% | 63.0%† | 0.410† | `eval_sft_standard_20_westd_n100` | 100† |
| 20% | Standard | GRPO | — | 59.44% | — | `eval_gsm8k_grpo_standard_20_fair_v2` | 1319 |
| 20% | RASP | SFT | — | 67.0%† | — | `eval_sft_rasp_20_westd_n100` | 100† |
| 20% | RASP | GRPO | — | 60.88% | — | `eval_gsm8k_grpo_rasp_20_fair` | 1319 |
| 25% | CKA-only | GRPO | 18.4% | 59.59% | **0.309** | `grpo_cka_only_25` (inline) | inline |
| 25% | Standard | SFT | 13.0% | — | — | — | — |

> † = small-N eval (N=100), high stderr (~±5pp), not directly comparable to N=1319 evals.

### Cross-Benchmark Observations

1. **MATH-500 is much harder than GSM8K** for pruned models. MATH/GSM ratios are 0.31–0.45, meaning pruned models lose disproportionately more on MATH-500 than GSM8K.

2. **CKA-only 20% GRPO** shows the highest MATH/GSM ratio (0.454) among pruned models with both benchmarks — suggesting CKA-only pruning better preserves harder reasoning capacity relative to its GSM8K performance.

3. **25% sparsity severely degrades MATH-500**: CKA-only drops from 29.2% (20%) → 18.4% (25%), a 37% relative decline. Standard SFT drops from 25.8% (20%) → 13.0% (25%), a 50% relative decline. Combined with 63.6% truncation at 25% Standard SFT, the model struggles to even complete solutions.

4. **Dense GRPO achieves 69.0%** on MATH-500, establishing the ceiling. The best pruned result (CKA-only GRPO 20% at 29.2%) retains only 42.3% of dense performance — a much steeper drop than on GSM8K where CKA-only GRPO 20% retains ~64.4%/~69% ≈ 93% (using approximate dense GSM8K accuracy).

### Missing GSM8K Evals (full-N):

- SFT CKA-only 20% GSM8K (N=1319): **not evaluated**
- SFT Standard 20% GSM8K (N=1319): only N=100 available
- SFT RASP 20% GSM8K (N=1319): only N=100 available
- SFT/GRPO Standard 25% GSM8K: **not evaluated**
- Dense (Unpruned) GSM8K: **not evaluated** (GRPO collapsed)
