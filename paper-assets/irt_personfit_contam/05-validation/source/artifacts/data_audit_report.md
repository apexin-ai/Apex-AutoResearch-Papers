# Paper Data Correctness Audit Report

**Date:** 2026-05-24  
**Scope:** Tables 1, 2, 3 + GRPO MIA + baseline consistency  
**Server:** westd-35694  
**Method:** Cell-by-cell comparison of paper LaTeX vs server JSON result files

---

## Summary

| Category | Count |
|----------|-------|
| MATCH | 38 cells |
| MISMATCH | 2 cells (Mistral free-θ d) |
| UNVERIFIABLE | 6 cells (Mistral baseline, ARC-C) |
| MINOR INCONSISTENCY | 1 (ARC-C CI rounding) |

**Critical finding:** Mistral MMLU free-θ Cohen's d(15%) = −3.01 is mathematically inconsistent with the contam lz* values on the server, regardless of baseline. Recommend immediate verification.

---

## Table 1: Cohen's d for Δℓz* (tab:cohens_d)

### Qwen MMLU (n=10 clean seeds)
**Source:** `ctrl_contam_pilot/results/cohens_d_n10.json`, `contam_5_cohens_d.json`, `theta_fixed_all_seeds.json`  
**Clean baseline:** mean=8.684, std=0.735 ← consistent across all files ✓

| Condition | Paper d | Paper CI | Data d | Data CI | Verdict |
|-----------|---------|----------|--------|---------|---------|
| 5% | −4.15 | [−9.9, −2.7] | −4.152 | [−9.85, −2.74] | **MATCH** ✓ |
| 15% (mean±SD) | −5.36 (±1.10) | — | −5.36 (±1.10)* | — | **MATCH** ✓ |
| 25% (mean±SD) | −7.44 (±1.86) | — | −7.44 (±1.86)* | — | **MATCH** ✓ |
| 50% (mean±SD) | −5.08 (±3.02) | — | −5.08 (±3.02)* | — | **MATCH** ✓ |

*Multi-seed means computed from per-seed d values in theta_fixed_all_seeds.json; individually verified in prior session.

### Llama MMLU (n=10 clean seeds)
**Source:** `ctrl_contam_llama/compute_cohens_d.py` (clean baseline), pilot + llama result files  
**Clean baseline:** mean=0.262, std(ddof=1)=1.542

| Condition | Paper d | Paper CI | Data d | Data CI | Verdict |
|-----------|---------|----------|--------|---------|---------|
| 15% | −2.11 | [−4.8, −1.4] | −2.111 | [−4.80, −1.40] | **MATCH** ✓ |
| 25% | −1.99 | [−4.4, −1.3] | −1.99 | [−4.40, −1.30] | **MATCH** ✓ |
| 50% | −2.33 | [−5.1, −1.6] | −2.331 | [−5.10, −1.60] | **MATCH** ✓ |

### Mistral MMLU ⚠️
**Source:** `ctrl_contam_mistral/results/` (6 clean seeds; 4 lost with server 19912)  
**Paper baseline:** mean=+4.02, SD=2.05 (claimed n=10)  
**Reproducible baseline (n=6):** mean=3.40, std=2.43

| Condition | Paper d | Paper CI | Data d (n=6) | Data d (paper baseline) | Verdict |
|-----------|---------|----------|--------------|------------------------|---------|
| 15% | −3.01 | [−8.2, −1.8] | −1.97 | −2.64 | **MISMATCH** ⚠️ |
| 50% | −3.50 | [−9.4, −2.1] | −2.69 | −3.50 | **d(50%) MATCH**, baseline unverifiable |

**Mathematical proof of inconsistency:** d(15%)=−3.01 and d(50%)=−3.50 require mean=9.46, std=3.60 — implausible given observed clean lz* range [−1.05, +5.80]. No single (mean, std) pair produces both d values with contam_15 lz*=−1.385 and contam_50 lz*=−3.150.

**Root cause:** 4 clean seeds' response vectors lost with old server 19912. Paper footnote acknowledges: "4–7 response vectors not retained in pipeline."

### ARC-C Qwen ⚠️
**Source:** `ctrl_contam_arcc/results/` (only 2 of 10 clean seeds on server)  
**Paper baseline:** −5.42 (SD=0.16)  
**Available 2 seeds:** lz*=−5.511, −5.493 (mean=−5.50)

| Condition | Paper d | Paper CI | Computed (paper baseline) | Verdict |
|-----------|---------|----------|--------------------------|---------|
| 15% | +3.16 | [2.0, 9.5] | +2.43 | **UNVERIFIABLE** |
| 50% | +5.30 | [3.6, 15.2] | +7.72 | **UNVERIFIABLE** |

Paper d values cannot be reproduced even with the stated baseline (−5.42, 0.16). 8 of 10 clean seed files missing from server.

**ARC-C CI inconsistency:** Table 1 reports 50% CI upper bound as **15.2**, but `gen_fig_heatmap.py` uses **15.5** and `gen_fig_theta_scatter.py` uses **(3.64, 15.49)**. Minor rounding difference.

---

## Table 2: Fixed-θ vs Free-θ Cohen's |d| (tab:theta_fixed)

**Source:** `theta_fixed_results.json` (master file), `theta_fixed_n10_recompute.json` (Mistral)

| Model | Cond | Paper d_free | Paper d_fixed | Paper CI_fixed | Data d_fixed | Data CI | Verdict |
|-------|------|--------------|---------------|----------------|--------------|---------|---------|
| Qwen | 5% | 4.15 | 3.52 | [2.9, 5.7] | 3.516 | [2.90, 5.71] | **MATCH** ✓ |
| Qwen† | 15% | 5.36 | 6.85 (±1.80) | — | 6.85* | — | **MATCH** ✓ |
| Qwen† | 50% | 5.08 | 12.32 (±2.38) | — | 12.32* | — | **MATCH** ✓ |
| Llama | 15% | 2.11 | 0.58 | [0, 2.37] | 0.582 | [0.04, 2.37] | **MATCH** ✓ |
| Llama | 50% | 2.33 | 0.84 | [0.17, 2.97] | 0.837 | [0.17, 2.97] | **MATCH** ✓ |
| Mistral‡ | 15% | 3.01 | 2.69 | [1.53, 9.06] | 2.686 | [1.53, 9.06] | **MATCH** ✓ |
| Mistral‡ | 50% | 3.50 | 5.80 | [3.87, 18.45] | 5.797 | [3.87, 18.45] | **MATCH** ✓ |

*Multi-seed means verified from per-seed values.  
†Qwen multi-seed d_fixed computed as mean of 3 per-seed |d| values.  
‡Mistral fixed-θ uses θ from 10 clean MLE (−1.088), lz*_fixed from 6 clean RVs.

**Ratio column verification:**
| Model | Cond | Paper ratio | Computed | Verdict |
|-------|------|-------------|----------|---------|
| Qwen | 5% | 0.8× | 3.52/4.15=0.85 | ✓ |
| Qwen | 15% | 1.3× | 6.85/5.36=1.28 | ✓ |
| Qwen | 50% | 2.4× | 12.32/5.08=2.42 | ✓ |
| Llama | 15% | 0.3× | 0.58/2.11=0.27 | ✓ |
| Llama | 50% | 0.4× | 0.84/2.33=0.36 | ✓ |
| Mistral | 15% | 0.9× | 2.69/3.01=0.89 | ✓ |
| Mistral | 50% | 1.7× | 5.80/3.50=1.66 | ✓ |

---

## Table 3: Detection-Diagnosis Tradeoff (tab:degradation)

**Source:** `ht_zscore_results_n10.json`, `multiseed_ht_accz_cohens_d.json`

### Qwen (multi-seed mean ± SD)
| Statistic | Paper d(15%) | Data d(15%) | Paper d(50%) | Data d(50%) | Verdict |
|-----------|-------------|-------------|-------------|-------------|---------|
| ℓz* | 5.36 (±1.10) | 5.36 (±1.10) | 5.08 (±3.02) | 5.08 (±3.02) | **MATCH** ✓ |
| HT | 5.83 (±1.30) | 5.832 (±1.301) | 5.29 (±3.41) | 5.290 (±3.408) | **MATCH** ✓ |
| Acc z | 45.0 (±2.5) | 45.003 (±2.539) | 70.0 (±1.1) | 69.964 (±1.121) | **MATCH** ✓ |

### Llama (bootstrap CI)
| Statistic | Paper d(15%) | Data d(15%) | Paper d(50%) | Data d(50%) | Verdict |
|-----------|-------------|-------------|-------------|-------------|---------|
| ℓz* | 2.11 [1.4, 4.8] | 2.11 [1.40, 4.80] | 2.33 [1.6, 5.1] | 2.33 [1.60, 5.10] | **MATCH** ✓ |
| HT | 2.45 [1.5, 4.3] | 2.454 [1.46, 4.29] | 3.07 [1.9, 5.3] | 3.066 [1.90, 5.34] | **MATCH** ✓ |
| Acc z | 22.5 [13.6, 47.0] | 22.498 [13.55, 46.98] | 32.8 [19.8, 68.6] | 32.821 [19.81, 68.56] | **MATCH** ✓ |

### Mistral (bootstrap CI)
| Statistic | Paper d(15%) | Data d(15%) | Paper d(50%) | Data d(50%) | Verdict |
|-----------|-------------|-------------|-------------|-------------|---------|
| ℓz* | 3.01 [1.8, 8.2] | See Table 1 Mistral issue | 3.50 [2.1, 9.4] | See Table 1 Mistral issue | **MISMATCH** (same as Table 1) |
| HT | 4.36 [1.2, 7.0] | 4.356 [1.22, 6.97] | 5.89 [1.9, 9.4] | 5.895 [1.85, 9.42] | **MATCH** ✓ |
| Acc z | 7.81 [4.4, 14.4] | 7.814 [4.38, 14.37] | 16.6 [9.7, 34.6] | 16.597 [9.71, 34.57] | **MATCH** ✓ |

---

## GRPO MIA Data

**Source:** GRPO experiment results on server

| Metric | Paper value | Data value | Verdict |
|--------|------------|------------|---------|
| SFT Min-K% AUC | 0.611 | 0.6111 (k=10) | **MATCH** ✓ |
| GRPO step500 AUC | 0.493 | 0.4930 | **MATCH** ✓ |
| GRPO step1000 AUC | 0.493 | 0.4928 | **MATCH** ✓ |
| GRPO step1500 AUC | 0.493 | 0.4930 | **MATCH** ✓ |

---

## Baseline Consistency Check

### Qwen MMLU (PASS ✓)
All computation files use identical baseline:
- `cohens_d_n10.json`: mean=8.684, std=0.735, n=10
- `contam_5_cohens_d.json`: mean=8.684, std=0.735
- `theta_fixed_results.json`: clean_lz_star_free values match exactly
- `compute_cohens_d.py`: CLEAN_LZ_STARS array matches

### Llama MMLU (MINOR ISSUE)
Two source files have different lz* values for seeds s2/s3:
- `compute_cohens_d.py` (used for free-θ Table 1): s2=−1.877, s3=0.345
- `theta_fixed_results.json` (used for fixed-θ Table 2): s2=−0.182, s3=−1.084

These produce different means (0.262 vs 0.368) and stds. Both files are internally consistent within their own usage (Table 1 free-θ d matches compute_cohens_d.py; Table 2 fixed-θ d matches theta_fixed_results.json). However, free-θ and fixed-θ baselines are computed from DIFFERENT clean lz* values for the same seeds, which represents a data provenance issue.

### Mistral MMLU (FAIL ✗)
Paper claims mean=+4.02 (SD=2.05) from n=10.  
Available 6 seeds: mean=3.40, std=2.43.  
4 seeds lost; baseline unverifiable. The paper's d values are inconsistent with the stated baseline (see Table 1 analysis).

### ARC-C Qwen (UNVERIFIABLE)
Paper claims n=10, baseline=−5.42 (SD=0.16).  
Only 2 clean seeds on server (mean=−5.50).

---

## Fix Recommendations

### Priority 1 — Mistral d(15%) (CRITICAL)
The paper reports d(15%)=−3.01 for Mistral MMLU. This value is:
- Not reproducible from the 6 available clean seeds (gives −1.97)
- Not reproducible from the paper's own baseline of (4.02, 2.05) (gives −2.64)
- Mathematically inconsistent with d(50%)=−3.50 given contam lz* values on server

**Recommended action:** 
1. If original n=10 computation exists in logs/backups, verify and document the source
2. If unrecoverable, recompute with n=6 baseline and update: d(15%)≈−1.97 [−7.0, −1.0], d(50%)≈−2.69 [−8.9, −1.5]
3. Update baseline text: mean=+3.40 (SD=2.43), n=6
4. Add explicit note that seeds 4–7 were lost

### Priority 2 — ARC-C CI rounding
Table 1: `[3.6, 15.2]` → Figure scripts: `[3.6, 15.5]`  
**Fix:** Change Table 1 to `[3.6, 15.5]` to match data source (gen_fig_heatmap.py value 15.49 rounds to 15.5).

### Priority 3 — ARC-C verification
8 of 10 clean seed results missing. If on backup, restore and verify. The d values in Table 1 cannot be verified with available data and don't match even with the stated baseline.

### Priority 4 — Llama baseline provenance
Document why compute_cohens_d.py and theta_fixed_results.json have different s2/s3 lz* values. While this doesn't affect reported numbers (each file is used consistently for its respective table), it indicates a potential re-evaluation that wasn't propagated.

---

## Data File Map

| Paper Element | Source File | Status |
|--------------|-------------|--------|
| Table 1 Qwen MMLU | `ctrl_contam_pilot/results/cohens_d_n10.json` | ✓ |
| Table 1 Qwen MMLU multi-seed | `ctrl_contam_pilot/results/theta_fixed_all_seeds.json` | ✓ |
| Table 1 Llama MMLU | `ctrl_contam_llama/compute_cohens_d.py` + pilot results | ✓ |
| Table 1 Mistral MMLU | Original n=10 computation **LOST** | ⚠️ |
| Table 1 ARC-C | Original computation **NOT ON SERVER** | ⚠️ |
| Table 2 all models | `theta_fixed_results.json` + `theta_fixed_n10_recompute.json` | ✓ |
| Table 3 Qwen | `multiseed_ht_accz_cohens_d.json` | ✓ |
| Table 3 Llama/Mistral | `ht_zscore_results_n10.json` | ✓ |
| GRPO MIA | GRPO experiment results | ✓ |
