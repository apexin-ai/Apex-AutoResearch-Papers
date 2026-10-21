# D141 Data Fix & Rerun v2 Report

## 1. Entity Matching Revert

Reverted entity matching from `(text, type)` back to `(start, end, type)` (span-based) in **2 files**:

| File | Before | After | Status |
|------|--------|-------|--------|
| `code/evaluation.py` (`entity_strict_match`) | `(e["text"], e["type"])` | `(e["start"], e["end"], e["type"])` | **Fixed** |
| `analysis_d141_scatter_plot.py` (`entity_f1`) | `(e["text"], e["type"])` | `(e["start"], e["end"], e["type"])` | **Fixed** |
| `analysis_d141_conditional_decomp.py` (`entity_f1`) | Already `(start, end, type)` | N/A | No change needed |
| `analysis_d141_entity_merge.py` | Imports `entity_strict_match` from `code/evaluation.py` | Fixed via evaluation.py | **Fixed by import** |

## 2. Data Path Verification

All paths already correct, no modification needed:

| Dataset | Path | Lines |
|---------|------|-------|
| CoNLL | `output/exp_002_conll_n16_r1024/samples.jsonl` | 3453 |
| FewNERD | `output/exp_027_fewnerd_n16/samples.jsonl` | 5000 |
| SciERC | `output/exp_012_rerun_1024/samples.jsonl` | 551 |

Both conditional_decomp and entity_merge use identical paths.

## 3. Gold Filter & N=8

- **Gold filter**: Both scripts already have `if len(gold_ents) == 0: continue`. No change needed.
- **N=8**: Conditional decomp uses `samples[:8]` and `logprobs[:8]`. Entity merge uses `MAX_N = 8` with threshold sweep k=1..8. No change needed.

## 4. Conditional Decomposition Results

Delta = LP_sel F1 - Greedy F1 (per-instance macro average)

### SciERC (N=529, median LP range=0.040121)

| Bucket | N_inst | % | Greedy_F1 | LP_F1 | Delta (pp) | 95% CI |
|--------|--------|---|-----------|-------|------------|--------|
| Favorable | 227 | 42.9 | 0.6333 | 0.6585 | **+2.52** | [+0.34, +4.76] |
| Cond1-only | 208 | 39.3 | 0.6632 | 0.6546 | -0.86 | [-3.30, +1.62] |
| Cond2-only | 37 | 7.0 | 0.4434 | 0.4254 | -1.80 | [-5.41, 0.00] |
| Unfavorable | 57 | 10.8 | 0.7461 | 0.7461 | 0.00 | [0.00, 0.00] |

### CoNLL (N=2756, median LP range=0.062012)

| Bucket | N_inst | % | Greedy_F1 | LP_F1 | Delta (pp) | 95% CI |
|--------|--------|---|-----------|-------|------------|--------|
| **Favorable** | **841** | **30.5** | **0.8679** | **0.8491** | **-1.88** | **[-2.93, -0.85]** |
| Cond1-only | 318 | 11.5 | 0.8441 | 0.8239 | -2.02 | [-4.31, +0.17] |
| Cond2-only | 537 | 19.5 | 0.8887 | 0.8887 | 0.00 | [0.00, 0.00] |
| Unfavorable | 1060 | 38.5 | 0.9661 | 0.9661 | 0.00 | [0.00, 0.00] |

### FewNERD (N=4351, median LP range=0.066996)

| Bucket | N_inst | % | Greedy_F1 | LP_F1 | Delta (pp) | 95% CI |
|--------|--------|---|-----------|-------|------------|--------|
| Favorable | 2064 | 47.4 | 0.7829 | 0.7898 | **+0.69** | [+0.05, +1.35] |
| Cond1-only | 1659 | 38.1 | 0.7548 | 0.7821 | +2.74 | [+1.82, +3.71] |
| Cond2-only | 111 | 2.5 | 0.1171 | 0.1141 | -0.30 | [-0.90, 0.00] |
| Unfavorable | 517 | 11.9 | 0.7206 | 0.7171 | -0.35 | [-0.89, 0.00] |

## 5. Entity Merge Results

### Macro F1 Summary

| Dataset | Greedy | LP_Sel | Oracle | Majority_Merge | LP_Wt_Merge | Best_Thresh_F1 | Best_k |
|---------|--------|--------|--------|----------------|-------------|----------------|--------|
| SciERC | 0.6439 | 0.6501 | 0.7758 | 0.6515 | 0.6458 | 0.6596 | k=3 |
| CoNLL | 0.9070 | 0.8989 | 0.9494 | 0.9006 | 0.9002 | 0.9032 | k=3 |
| FewNERD | 0.7478 | 0.7610 | 0.8686 | 0.7157 | 0.7137 | 0.7435 | k=2 |

### Gap Recovery

Gap recovery % = (Best_Thresh_F1 - Greedy) / (Oracle - Greedy) * 100

| Dataset | Oracle-Greedy Gap | Merge-Greedy Delta | Gap Recovery % |
|---------|-------------------|--------------------|----------------|
| SciERC | 0.1319 | +0.0157 | **+11.9%** |
| CoNLL | 0.0424 | -0.0038 | **-9.0%** (merge < greedy) |
| FewNERD | 0.1208 | -0.0043 | **-3.6%** (merge < greedy) |

### Micro F1 (reference)

| Dataset | Greedy | Majority | LP_Wt |
|---------|--------|----------|-------|
| SciERC | 0.6663 | 0.6693 | 0.6685 |
| CoNLL | 0.9116 | 0.9096 | 0.9099 |
| FewNERD | 0.7926 | 0.7740 | 0.7738 |

### Degenerate Subset

| Dataset | Degen% | N_degen | Delta merge-greedy on degen |
|---------|--------|---------|-----------------------------|
| SciERC | 17.8% | 94 | -0.0078 |
| CoNLL | 57.9% | 1597 | -0.0013 |
| FewNERD | 14.4% | 628 | -0.0119 |

## 6. CoNLL Favorable Bucket: Confirmed Negative

**CoNLL Favorable bucket delta = -1.88 pp**, with 95% CI entirely below zero **[-2.93, -0.85]**. This is statistically significant.

Under span-based matching `(start, end, type)`, LP selection hurts even in the "favorable" bucket for CoNLL. This contrasts with the previous (incorrect) text-based matching results and is consistent with CoNLL's high degeneracy rate (57.9%) and high baseline greedy F1 (0.9070), leaving little room for LP selection to improve.

Key observations:
- SciERC is the only dataset where Favorable bucket shows significant positive delta (+2.52 pp)
- FewNERD Favorable shows marginal positive delta (+0.69 pp, CI barely above zero)
- FewNERD Cond1-only (non-degenerate, low LP range) unexpectedly shows the largest positive delta (+2.74 pp)
- Entity merge does not break oracle ceiling on any dataset
- Only SciERC shows positive gap recovery from merge (11.9%)
