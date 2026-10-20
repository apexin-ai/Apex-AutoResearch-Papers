# D141 v2 Fix Report

## 1. Code Changes Summary

### CRITICAL 1: Evaluation function changed to (text, type) matching

**Files modified:**
- `code/evaluation.py` L34-35: `entity_strict_match` now uses `(e["text"], e["type"])` instead of `(e["start"], e["end"], e["type"])`
- `analysis_d141_conditional_decomp.py` L24-25: inline `entity_f1` same change
- `analysis_d141_scatter_plot.py` L39-40: inline `entity_f1` same change

### CRITICAL 2: Data sources unified

**File: `analysis_d141_conditional_decomp.py`**
- CoNLL: `exp_002_conll_n16` -> `exp_002_conll_n16_r1024`
- FewNERD: `exp_021_inference` -> `exp_027_fewnerd_n16`

**File: `analysis_d141_scatter_plot.py`**
- CoNLL: `exp_002_conll_n16` -> `exp_002_conll_n16_r1024`
- FewNERD: `exp_021_inference` -> `exp_027_fewnerd_n16`

Entity merge script (`analysis_d141_entity_merge.py`) already had correct data sources.

### WARNING 1: Gold filter added

**File: `analysis_d141_entity_merge.py` main()**
- Added: `instances = [inst for inst in instances if len(inst["gold"].get("entities", [])) > 0]`

(Conditional decomp already had gold filter.)

### WARNING 2: N=8 unified

**Files modified:**
- `analysis_d141_entity_merge.py` main(): truncates `samples[:8]` and `logprobs[:8]`
- `analysis_d141_conditional_decomp.py` load_instances(): truncates `samples[:8]` and `logprobs[:8]`

Actual N in data: SciERC=8 (already correct), CoNLL=16 (truncated to 8), FewNERD=16 (truncated to 8).

---

## 2. Sanity Check

SciERC with (text, type) matching, N=8:
- Greedy F1: 0.6441
- Oracle F1: 0.7758
- Gap: 0.1317

**Confirms fix is effective** (v1 used span-based matching which produced different numbers).

---

## 3. Entity Merge Results (all datasets, N=8)

| Dataset | N_inst | Greedy | LP_Sel | Oracle | Majority_Merge | LP_Weighted | Best_Thresh | Best_k |
|---------|--------|--------|--------|--------|----------------|-------------|-------------|--------|
| SciERC  | 529    | 0.6441 | 0.6505 | 0.7758 | 0.6532         | 0.6476      | 0.6610      | 3      |
| CoNLL   | 2756   | 0.9077 | 0.8998 | 0.9497 | 0.9037         | 0.9033      | 0.9063      | 3      |
| FewNERD | 4351   | 0.7493 | 0.7621 | 0.8701 | 0.7247         | 0.7224      | 0.7521      | 2      |

### Gap Recovery (Best Threshold Merge)

| Dataset | Gap (Oracle-Greedy) | Merge Gain | Gap Recovery % |
|---------|---------------------|------------|----------------|
| SciERC  | 0.1317              | +0.0169    | 12.8%          |
| CoNLL   | 0.0420              | -0.0014    | -3.3%          |
| FewNERD | 0.1208              | +0.0028    | 2.3%           |

### Micro F1

| Dataset | Greedy | Majority_Merge | LP_Weighted |
|---------|--------|----------------|-------------|
| SciERC  | 0.6671 | 0.6717         | 0.6710      |
| CoNLL   | 0.9135 | 0.9158         | 0.9160      |
| FewNERD | 0.7946 | 0.7859         | 0.7857      |

### Degenerate Subset

| Dataset | Degen% | N_degen | Greedy | Merge  | Oracle | Delta_Merge_vs_Greedy |
|---------|--------|---------|--------|--------|--------|-----------------------|
| SciERC  | 17.8%  | 94      | 0.6270 | 0.6191 | 0.6199 | -0.0078               |
| CoNLL   | 58.0%  | 1599    | 0.9396 | 0.9396 | 0.9396 | +0.0000               |
| FewNERD | 14.5%  | 632     | 0.6158 | 0.6128 | 0.6124 | -0.0030               |

### Non-Degenerate Subset

| Dataset | N    | Greedy | Oracle | Majority_Merge | Best_Thresh |
|---------|------|--------|--------|----------------|-------------|
| SciERC  | 435  | 0.6478 | 0.8095 | 0.6606         | 0.6719      |
| CoNLL   | 1157 | 0.8637 | 0.9637 | 0.8540         | 0.8607      |
| FewNERD | 3719 | 0.7720 | 0.9138 | 0.7437         | 0.7764      |

### Threshold Sweep

**SciERC (N=8):** k=1: 0.6214, k=2: 0.6599, **k=3: 0.6610**, k=4: 0.6532, k=5: 0.6289, k=6: 0.5995, k=7: 0.5470, k=8: 0.4255

**CoNLL (N=8):** k=1: 0.8391, k=2: 0.8974, **k=3: 0.9063**, k=4: 0.9037, k=5: 0.8946, k=6: 0.8729, k=7: 0.8404, k=8: 0.7244

**FewNERD (N=8):** k=1: 0.6744, **k=2: 0.7521**, k=3: 0.7507, k=4: 0.7247, k=5: 0.6794, k=6: 0.6110, k=7: 0.5013, k=8: 0.3079

### Bootstrap 95% CI (Merge vs Oracle)

| Dataset | Method               | Mean Diff | 95% CI              | Significant |
|---------|----------------------|-----------|---------------------|-------------|
| SciERC  | majority_merge       | -0.1226   | [-0.1407, -0.1065]  | YES         |
| SciERC  | lp_weighted_merge    | -0.1282   | [-0.1455, -0.1108]  | YES         |
| SciERC  | best_threshold_merge | -0.1148   | [-0.1296, -0.1010]  | YES         |
| CoNLL   | majority_merge       | -0.0461   | [-0.0527, -0.0402]  | YES         |
| CoNLL   | lp_weighted_merge    | -0.0464   | [-0.0537, -0.0406]  | YES         |
| CoNLL   | best_threshold_merge | -0.0435   | [-0.0496, -0.0380]  | YES         |
| FewNERD | majority_merge       | -0.1454   | [-0.1531, -0.1380]  | YES         |
| FewNERD | lp_weighted_merge    | -0.1477   | [-0.1557, -0.1402]  | YES         |
| FewNERD | best_threshold_merge | -0.1179   | [-0.1235, -0.1125]  | YES         |

---

## 4. Conditional Decomposition Results

### SciERC (N=529, median LP range=0.040121)

| Bucket      | N_inst | %     | Greedy_F1 | LP_F1  | Delta   | 95% CI              |
|-------------|--------|-------|-----------|--------|---------|----------------------|
| Favorable   | 227    | 42.9% | 0.6344    | 0.6591 | +0.0247 | [0.0030, 0.0470]    |
| Cond1-only  | 208    | 39.3% | 0.6625    | 0.6549 | -0.0075 | [-0.0319, 0.0172]   |
| Cond2-only  | 37     | 7.0%  | 0.4434    | 0.4254 | -0.0180 | [-0.0541, 0.0000]   |
| Unfavorable | 57     | 10.8% | 0.7461    | 0.7461 | +0.0000 | [0.0000, 0.0000]    |

### CoNLL (N=2756, median LP range=0.062012)

| Bucket      | N_inst | %     | Greedy_F1 | LP_F1  | Delta   | 95% CI              |
|-------------|--------|-------|-----------|--------|---------|----------------------|
| Favorable   | 843    | 30.6% | 0.8692    | 0.8514 | -0.0178 | [-0.0283, -0.0076]  |
| Cond1-only  | 314    | 11.4% | 0.8488    | 0.8269 | -0.0219 | [-0.0448, -0.0000]  |
| Cond2-only  | 535    | 19.4% | 0.8883    | 0.8883 | +0.0000 | [0.0000, 0.0000]    |
| Unfavorable | 1064   | 38.6% | 0.9654    | 0.9654 | +0.0000 | [0.0000, 0.0000]    |

### FewNERD (N=4351, median LP range=0.066996)

| Bucket      | N_inst | %     | Greedy_F1 | LP_F1  | Delta   | 95% CI              |
|-------------|--------|-------|-----------|--------|---------|----------------------|
| Favorable   | 2064   | 47.4% | 0.7857    | 0.7920 | +0.0063 | [-0.0002, 0.0130]   |
| Cond1-only  | 1655   | 38.0% | 0.7548    | 0.7820 | +0.0271 | [0.0179, 0.0365]    |
| Cond2-only  | 111    | 2.6%  | 0.1081    | 0.1051 | -0.0030 | [-0.0090, 0.0000]   |
| Unfavorable | 521    | 12.0% | 0.7239    | 0.7204 | -0.0035 | [-0.0088, 0.0000]   |

---

## 5. Scatter Plot (Degeneracy vs Capability)

| Experiment              | Greedy F1 | Degeneracy% |
|-------------------------|-----------|-------------|
| Qwen3-8B SciERC 3ep    | 0.6507    | 6.4%        |
| Qwen3-8B SciERC 5ep    | 0.6441    | 17.8%       |
| Qwen3-8B SciERC 10ep   | 0.6467    | 47.8%       |
| Qwen3-8B CoNLL         | 0.9077    | 47.5%       |
| Qwen3-8B FewNERD       | 0.7493    | 7.1%        |
| Qwen3-4B SciERC        | 0.6618    | 10.4%       |
| Qwen3-4B CoNLL         | 0.9215    | 90.6%       |
| LLaMA-3B SciERC        | 0.6486    | 25.5%       |
| LLaMA-3B CoNLL         | 0.9240    | 86.3%       |
| Qwen3-8B FewNERD 5ep   | 0.7788    | 31.4%       |

Spearman rho=0.5030, p=0.1383

---

## 6. Key Observations (v2 vs v1)

1. **Text matching changes the game**: With (text, type) matching, entity merge still provides modest gains on SciERC (12.8% gap recovery) but the benefit disappears on CoNLL (-3.3%) and is marginal on FewNERD (2.3%).

2. **All merge methods significantly underperform oracle**: Bootstrap CIs confirm all merge vs oracle differences are significantly negative across all three datasets.

3. **Degeneracy is high for CoNLL**: 58% of CoNLL instances are degenerate (all samples have identical F1), limiting the scope for any selection/merge strategy.

4. **Conditional decomp findings**:
   - SciERC: LP selection helps in Favorable bucket (+2.5%, significant)
   - CoNLL: LP selection *hurts* even in Favorable bucket (-1.8%, significant negative)
   - FewNERD: LP selection shows strongest benefit in Cond1-only bucket (+2.7%, significant), with Favorable bucket marginally positive (+0.6%, borderline)
