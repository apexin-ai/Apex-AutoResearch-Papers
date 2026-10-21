# Table 7 D105+D111 Unified K-Value Audit

**Date**: 2026-05-20
**Corrections applied**: D105 (3σ threshold) + D111 (peak_lag > 0 for naive/diff)

**Voting rules (per pair, 5 votes):**
1. naive_xcorr: `significant`=True AND `peak_lag` > 0
2. diff_xcorr: `significant_fdr`=True AND `peak_lag` > 0
3. threshold_onset: `significant_3sigma`=True (or 3x_sigma_drift config)
4. permG: `p_value_fdr_bh` < 0.05 (strict) AND direction=fwd
5. TY: `significant`=True

---

## 1. Pythia-6.9B s42 (bf16)

Source: westd-17855:`results/scale_check/pythia69b_wiki_a100_s42/analysis_results.json`
Format: analysis_results.json (no significant_3sigma field)

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh_3σ | permG_fdr | TY | K |
|------|-----------|-----------|-----------|----------|--------------|----------|-----------|-----------|-----|---|
| te→d1 | -1 | T | F | -1 | T | F | T* | T (0.007) | F | 2 |
| te→d2 | -2 | T | F | -2 | T | F | T* | T (0.005) | T | 3 |
| te→d3 | 5 | T | **T** | -4 | T | F | T* | T (0.007) | T | 4 |
| te→mauve | 4 | T | **T** | 2 | F | F | T* | F (0.058) | T | 3 |
| ece→d1 | -1 | T | F | -1 | T | F | T* | T (0.003) | F | 2 |
| ece→d2 | -1 | T | F | -1 | T | F | T* | T (0.003) | F | 2 |
| ece→d3 | -3 | T | F | -3 | T | F | T* | T (0.003) | T | 3 |
| ece→mauve | 4 | T | **T** | -1 | F | F | T* | T (0.033) | F | 2 |

Summary: naive_fwd=3/8, diff_fwd=0/8, thresh_3σ=8/8*, permG_fdr=7/8, TY=4/8, **K≥3=5/8, K≥4=1/8**
vs Registry: K≥3 8/8→5/8 ↓, K≥4 3/8→1/8 ↓
Flags: **MISSING_3SIGMA** (using 2σ `significant` as fallback for all 8 pairs)

---

## 2. Qwen3.5-0.8B s42

Source: westd-17855:`results/generalize/qwen35_08b_wiki_a100_s42_fp32_v2/analysis_results.json`
Format: analysis_results.json (no significant_3sigma field)

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh_3σ | permG_fdr | TY | K |
|------|-----------|-----------|-----------|----------|--------------|----------|-----------|-----------|-----|---|
| te→d1 | 5 | T | **T** | -1 | T | F | T* | T (0.017) | F | 3 |
| te→d2 | 5 | T | **T** | -1 | T | F | T* | T (0.037) | T | 4 |
| te→d3 | 5 | T | **T** | -1 | T | F | T* | T (0.037) | F | 3 |
| te→mauve | 2 | T | **T** | -1 | T | F | T* | T (0.048) | T | 4 |
| ece→d1 | -1 | T | F | -1 | T | F | T* | T (0.017) | T | 3 |
| ece→d2 | -1 | T | F | -1 | T | F | T* | T (0.023) | T | 3 |
| ece→d3 | -4 | T | F | -1 | T | F | T* | T (0.037) | T | 3 |
| ece→mauve | -5 | T | F | 4 | T | **T** | T* | T (0.048) | T | 4 |

Summary: naive_fwd=4/8, diff_fwd=1/8, thresh_3σ=8/8*, permG_fdr=8/8, TY=6/8, **K≥3=8/8, K≥4=3/8**
vs Registry: K≥3 8/8→8/8 =, K≥4 6/8→3/8 ↓
Flags: **MISSING_3SIGMA** (using 2σ `significant` as fallback for all 8 pairs)

---

## 3. GPT-2m s42

Source: westd-19828:`results/generalize/gpt2m_wiki_a100_s42/analysis/5method_leadlag.json`
Format: 5method_leadlag.json (config: threshold_criterion=3x_sigma_drift)

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh_3σ | permG_fdr | TY | K |
|------|-----------|-----------|-----------|----------|--------------|----------|-----------|-----------|-----|---|
| te→d1 | -1 | T | F | -1 | T | F | F | T (0.002) | F | 1 |
| te→d2 | -1 | T | F | -2 | T | F | F | T (0.003) | T | 2 |
| te→d3 | -2 | T | F | -2 | T | F | F | T (0.003) | T | 2 |
| te→mauve | 4 | T | **T** | -1 | F | F | F | F (0.130) | F | 1 |
| ece→d1 | -1 | T | F | -1 | T | F | F | T (0.002) | F | 1 |
| ece→d2 | -1 | T | F | -1 | T | F | F | T (0.002) | F | 1 |
| ece→d3 | -1 | T | F | -1 | T | F | F | T (0.002) | F | 1 |
| ece→mauve | 4 | T | **T** | -1 | F | F | F | F (0.130) | F | 1 |

Summary: naive_fwd=2/8, diff_fwd=0/8, thresh_3σ=0/8, permG_fdr=6/8, TY=2/8, **K≥3=0/8, K≥4=0/8**
vs Registry: K≥3 6/8→0/8 ↓↓, K≥4 2/8→0/8 ↓

---

## 4. GPT-2m s43

Source: westd-19828:`results/gen_wiki_gpt2m_a100_s43/analysis/5method_leadlag.json`
Format: 5method_leadlag.json (config: threshold_criterion=3x_sigma_drift)

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh_3σ | permG_fdr | TY | K |
|------|-----------|-----------|-----------|----------|--------------|----------|-----------|-----------|-----|---|
| te→d1 | -2 | T | F | -3 | T | F | F | T (0.007) | F | 1 |
| te→d2 | -2 | T | F | -3 | T | F | F | T (0.014) | T | 2 |
| te→d3 | 4 | T | **T** | -4 | T | F | F | T (0.014) | T | 3 |
| te→mauve | -2 | T | F | -2 | F | F | F | F (0.331) | F | 0 |
| ece→d1 | -1 | T | F | -1 | T | F | F | T (0.003) | F | 1 |
| ece→d2 | -2 | T | F | -2 | T | F | F | T (0.003) | T | 2 |
| ece→d3 | -5 | T | F | -3 | T | F | F | T (0.003) | T | 2 |
| ece→mauve | -2 | T | F | -2 | F | F | T | F (0.493) | F | 1 |

Summary: naive_fwd=1/8, diff_fwd=0/8, thresh_3σ=1/8, permG_fdr=6/8, TY=4/8, **K≥3=1/8, K≥4=0/8**
vs Registry: K≥3 6/8→1/8 ↓↓, K≥4 4/8→0/8 ↓↓

---

## 5. OPT-1.3B s42

Source: westd-19828:`results/generalize/opt1b_wiki_a100_s42/analysis/5method_leadlag.json`
Format: 5method_leadlag.json (config: threshold_criterion=3x_sigma_drift)

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh_3σ | permG_fdr | TY | K |
|------|-----------|-----------|-----------|----------|--------------|----------|-----------|-----------|-----|---|
| te→d1 | -1 | T | F | -1 | T | F | F | T (0.005) | F | 1 |
| te→d2 | -1 | T | F | -1 | T | F | F | T (0.009) | F | 1 |
| te→d3 | -1 | T | F | -1 | T | F | F | T (0.017) | F | 1 |
| te→mauve | -4 | T | F | 3 | T | **T** | F | F (0.668) | F | 1 |
| ece→d1 | -1 | T | F | -1 | T | F | T | T (0.005) | F | 2 |
| ece→d2 | -1 | T | F | -1 | T | F | F | T (0.009) | F | 1 |
| ece→d3 | 3 | T | **T** | -1 | T | F | F | T (0.017) | F | 2 |
| ece→mauve | -4 | T | F | 3 | F | F | T | F (0.694) | F | 1 |

Summary: naive_fwd=1/8, diff_fwd=1/8, thresh_3σ=2/8, permG_fdr=6/8, TY=0/8, **K≥3=0/8, K≥4=0/8**
vs Registry: K≥3 6/8→0/8 ↓↓, K≥4 2/8→0/8 ↓

---

## 6. Padding-410M s42

Source: westd-17855:`results/padding_robustness/a100_s42_fp32/analysis_results.json`
Format: analysis_results.json (no significant_3sigma field)

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh_3σ | permG_fdr | TY | K |
|------|-----------|-----------|-----------|----------|--------------|----------|-----------|-----------|-----|---|
| te→d1 | -1 | T | F | -1 | T | F | T* | T (0.006) | T | 3 |
| te→d2 | -1 | T | F | -1 | T | F | T* | T (0.006) | T | 3 |
| te→d3 | -2 | T | F | -2 | T | F | T* | T (0.005) | T | 3 |
| te→mauve | -4 | F | F | -5 | F | F | T* | F (0.452) | F | 1 |
| ece→d1 | -2 | T | F | -2 | T | F | T* | T (0.005) | T | 3 |
| ece→d2 | -3 | T | F | -1 | T | F | T* | T (0.005) | T | 3 |
| ece→d3 | -3 | T | F | -1 | T | F | T* | T (0.005) | T | 3 |
| ece→mauve | -4 | F | F | -5 | F | F | T* | F (0.519) | F | 1 |

Summary: naive_fwd=0/8, diff_fwd=0/8, thresh_3σ=8/8*, permG_fdr=6/8, TY=6/8, **K≥3=6/8, K≥4=0/8**
vs Registry: K≥3 6/8→6/8 =, K≥4 6/8→0/8 ↓↓
Flags: **MISSING_3SIGMA** (using 2σ `significant` as fallback for all 8 pairs)

---

## 7. SmolLM3-3B s42

Source: westd-19828:`results/generalize/smollm3_3b_wiki_a100_s42_fp32_v3/analysis/5method_leadlag.json`
Format: 5method_leadlag.json (config: threshold_criterion=3x_sigma_drift)

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh_3σ | permG_fdr | TY | K |
|------|-----------|-----------|-----------|----------|--------------|----------|-----------|-----------|-----|---|
| te→d1 | 5 | T | **T** | -2 | T | F | F | F (0.066) | F | 1 |
| te→d2 | 5 | T | **T** | -2 | T | F | F | F (0.058) | F | 1 |
| te→d3 | 5 | T | **T** | -2 | T | F | F | F (0.058) | F | 1 |
| te→mauve | 4 | T | **T** | -3 | F | F | F | F (0.730) | F | 1 |
| ece→d1 | -1 | T | F | -2 | T | F | F | T (0.030) | F | 1 |
| ece→d2 | -1 | T | F | -2 | T | F | F | T (0.030) | F | 1 |
| ece→d3 | -2 | T | F | -2 | T | F | F | T (0.030) | F | 1 |
| ece→mauve | -3 | T | F | -3 | F | F | F | F (0.161) | F | 0 |

Summary: naive_fwd=4/8, diff_fwd=0/8, thresh_3σ=0/8, permG_fdr=3/8, TY=0/8, **K≥3=0/8, K≥4=0/8**
vs Registry: K≥3 0/8→0/8 =, K≥4 0/8→0/8 =

---

## 8. Pythia-410M s43

Source: westd-17855:`results/generalize/pythia410m_wiki_a100_s43/analysis_results.json`
Format: analysis_results.json (no significant_3sigma field)

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh_3σ | permG_fdr | TY | K |
|------|-----------|-----------|-----------|----------|--------------|----------|-----------|-----------|-----|---|
| te→d1 | -1 | T | F | -1 | T | F | T* | T (0.003) | T | 3 |
| te→d2 | -1 | T | F | -1 | T | F | T* | T (0.003) | T | 3 |
| te→d3 | -1 | T | F | -2 | T | F | T* | T (0.007) | T | 3 |
| te→mauve | -5 | F | F | 5 | F | F | T* | F (0.242) | F | 1 |
| ece→d1 | -3 | T | F | -1 | T | F | T* | T (0.003) | T | 3 |
| ece→d2 | -3 | T | F | -1 | T | F | T* | T (0.001) | T | 3 |
| ece→d3 | -3 | T | F | -1 | T | F | T* | T (0.001) | T | 3 |
| ece→mauve | -5 | F | F | -2 | F | F | T* | F (0.391) | F | 1 |

Summary: naive_fwd=0/8, diff_fwd=0/8, thresh_3σ=8/8*, permG_fdr=6/8, TY=6/8, **K≥3=6/8, K≥4=0/8**
vs Registry: K≥3 6/8→6/8 =, K≥4 0/8→0/8 =
Flags: **MISSING_3SIGMA** (using 2σ `significant` as fallback for all 8 pairs)

---

## 9. C4 Pythia-1B s42

Source: westd-19828:`results/generalize/pythia1b_c4_a100_s42/analysis/5method_leadlag.json`
Format: 5method_leadlag.json (config: threshold_criterion=3x_sigma_drift)

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh_3σ | permG_fdr | TY | K |
|------|-----------|-----------|-----------|----------|--------------|----------|-----------|-----------|-----|---|
| te→d1 | -1 | T | F | -1 | T | F | T | T (0.016) | F | 2 |
| te→d2 | -1 | T | F | -1 | T | F | T | T (0.020) | F | 2 |
| te→d3 | 4 | T | **T** | -2 | T | F | T | T (0.026) | F | 3 |
| te→mauve | -1 | T | F | -1 | T | F | T | T (0.024) | F | 2 |
| ece→d1 | -1 | T | F | -1 | T | F | T | T (0.010) | T | 3 |
| ece→d2 | -1 | T | F | -1 | T | F | T | T (0.014) | T | 3 |
| ece→d3 | 3 | T | **T** | -2 | T | F | T | T (0.016) | T | 4 |
| ece→mauve | -1 | T | F | -1 | T | F | T | T (0.024) | T | 3 |

Summary: naive_fwd=2/8, diff_fwd=0/8, thresh_3σ=8/8, permG_fdr=8/8, TY=4/8, **K≥3=5/8, K≥4=1/8**
vs Registry: K≥3 8/8→5/8 ↓, K≥4 4/8→1/8 ↓

---

## 10. C4 Pythia-1B s43

Source: westd-19828:`results/generalize/pythia1b_c4_a100_s43/analysis/5method_leadlag.json`
Format: 5method_leadlag.json (config: threshold_criterion=3x_sigma_drift)

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh_3σ | permG_fdr | TY | K |
|------|-----------|-----------|-----------|----------|--------------|----------|-----------|-----------|-----|---|
| te→d1 | -1 | T | F | -1 | T | F | T | T (0.020) | F | 2 |
| te→d2 | 5 | T | **T** | -1 | T | F | T | T (0.043) | F | 3 |
| te→d3 | 5 | T | **T** | -1 | T | F | T | F (0.050) | F | 2 |
| te→mauve | -1 | T | F | -1 | T | F | T | T (0.039) | F | 2 |
| ece→d1 | -1 | T | F | -1 | T | F | T | T (0.018) | T | 3 |
| ece→d2 | 3 | T | **T** | -1 | T | F | T | T (0.020) | T | 4 |
| ece→d3 | 2 | T | **T** | -1 | T | F | T | T (0.039) | T | 4 |
| ece→mauve | -1 | T | F | -1 | T | F | T | T (0.020) | T | 3 |

Summary: naive_fwd=4/8, diff_fwd=0/8, thresh_3σ=8/8, permG_fdr=7/8, TY=4/8, **K≥3=5/8, K≥4=2/8**
vs Registry: K≥3 8/8→5/8 ↓, K≥4 5/8→2/8 ↓
Note: te→d3 permG p_fdr=0.050 exactly, fails strict <0.05. Registry PermG was 8/8, now 7/8.

---

## 11. Pythia-1.4B s42

Source: westd-19828:`results/generalize/pythia14b_wiki_a100_s42/analysis/5method_leadlag.json`
Format: 5method_leadlag.json (config: threshold_criterion=3x_sigma_drift)

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh_3σ | permG_fdr | TY | K |
|------|-----------|-----------|-----------|----------|--------------|----------|-----------|-----------|-----|---|
| te→d1 | -1 | T | F | -1 | T | F | T | F (0.055) | F | 1 |
| te→d2 | -5 | T | F | -1 | T | F | T | F (0.055) | F | 1 |
| te→d3 | -5 | T | F | -1 | T | F | T | F (0.071) | F | 1 |
| te→mauve | -5 | T | F | -5 | F | F | T | F (0.242) | F | 1 |
| ece→d1 | -1 | T | F | -1 | T | F | T | T (0.034) | F | 2 |
| ece→d2 | 3 | T | **T** | -1 | T | F | T | T (0.034) | F | 3 |
| ece→d3 | 3 | T | **T** | -1 | T | F | T | F (0.055) | F | 2 |
| ece→mauve | -5 | T | F | 4 | T | **T** | T | F (0.240) | F | 2 |

Summary: naive_fwd=2/8, diff_fwd=1/8, thresh_3σ=8/8, permG_fdr=2/8, TY=0/8, **K≥3=1/8, K≥4=0/8**
vs Registry: K≥3 2/8→1/8 ↓, K≥4 0/8→0/8 =

---

## 12. Pythia-1.4B s43

Source: westd-19828:`results/generalize/pythia14b_wiki_a100_s43/analysis/5method_leadlag.json`
Format: 5method_leadlag.json (config: threshold_criterion=3x_sigma_drift)

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig_fdr | diff_fwd | thresh_3σ | permG_fdr | TY | K |
|------|-----------|-----------|-----------|----------|--------------|----------|-----------|-----------|-----|---|
| te→d1 | 5 | T | **T** | -1 | T | F | T | T (0.012) | T | 4 |
| te→d2 | 5 | T | **T** | -1 | T | F | T | T (0.012) | F | 3 |
| te→d3 | 5 | T | **T** | -4 | T | F | T | T (0.016) | F | 3 |
| te→mauve | 1 | T | **T** | 5 | T | **T** | T | F (0.098) | F | 3 |
| ece→d1 | 1 | T | **T** | -1 | T | F | T | T (0.012) | T | 4 |
| ece→d2 | 1 | T | **T** | -1 | T | F | T | T (0.016) | T | 4 |
| ece→d3 | 1 | T | **T** | -1 | T | F | T | T (0.019) | T | 4 |
| ece→mauve | -5 | F | F | 5 | T | **T** | T | F (0.075) | F | 2 |

Summary: naive_fwd=7/8, diff_fwd=2/8, thresh_3σ=8/8, permG_fdr=6/8, TY=4/8, **K≥3=7/8, K≥4=4/8**
vs Registry: K≥3 6/8→7/8 ↑, K≥4 3/8→4/8 ↑
Flags: **K_INCREASED** — K values rose vs registry. This likely indicates the registry was computed from a different analysis run or with additional corrections not reflected in the current 5method JSON. The raw data consistently supports K≥3=7/8. Cross-checked: permG=6/8 matches registry permG=6/8.

---

## 13. OPT-1.3B s43 (verification target)

Source: westd-19828:`results/gen_opt13b_wiki_a100_s43_fp32/analysis/d105_analysis.json`
Format: d105_analysis.json (threshold_onset_3sigma explicit)
d111_direction_ok field: 0 (zero pairs pass direction check)

| pair | naive_lag | naive_sig | naive_fwd | diff_lag | diff_sig | diff_fwd | thresh_3σ | permG_fdr | TY | K |
|------|-----------|-----------|-----------|----------|----------|----------|-----------|-----------|-----|---|
| te→d1 | -2 | T | F | -1 | T | F | F | T (0.002) | F | 1 |
| te→d2 | -1 | T | F | -1 | T | F | F | T (0.002) | F | 1 |
| te→d3 | -1 | T | F | -1 | T | F | F | T (0.003) | T | 2 |
| te→mauve | -4 | T | F | -4 | F | F | F | F (0.115) | F | 0 |
| ece→d1 | -3 | T | F | -2 | T | F | F | T (0.002) | T | 2 |
| ece→d2 | -3 | T | F | -1 | T | F | F | T (0.002) | T | 2 |
| ece→d3 | -1 | T | F | -1 | T | F | F | T (0.002) | T | 2 |
| ece→mauve | -3 | T | F | -4 | F | F | F | F (0.120) | T | 1 |

Summary: naive_fwd=0/8, diff_fwd=0/8, thresh_3σ=0/8, permG_fdr=6/8, TY=4/8, **K≥3=0/8, K≥4=0/8**
vs Registry: K≥3 0/8→0/8 = ✓ (verification passed)

---

## Table 7 D105+D111 Unified Summary

| # | Model | Seed | PermG | naive_fwd | diff_fwd | thresh_3σ | TY | K≥3 (old→new) | K≥4 (old→new) | flags |
|---|-------|------|-------|-----------|----------|-----------|-----|----------------|----------------|-------|
| 1 | Pythia-6.9B | s42 | 7/8 | 3/8 | 0/8 | 8/8* | 4/8 | 8/8→**5/8** ↓ | 3/8→**1/8** ↓ | MISSING_3SIGMA |
| 2 | Qwen3.5-0.8B | s42 | 8/8 | 4/8 | 1/8 | 8/8* | 6/8 | 8/8→**8/8** = | 6/8→**3/8** ↓ | MISSING_3SIGMA |
| 3 | GPT-2m | s42 | 6/8 | 2/8 | 0/8 | 0/8 | 2/8 | 6/8→**0/8** ↓↓ | 2/8→**0/8** ↓ | |
| 4 | GPT-2m | s43 | 6/8 | 1/8 | 0/8 | 1/8 | 4/8 | 6/8→**1/8** ↓↓ | 4/8→**0/8** ↓↓ | |
| 5 | OPT-1.3B | s42 | 6/8 | 1/8 | 1/8 | 2/8 | 0/8 | 6/8→**0/8** ↓↓ | 2/8→**0/8** ↓ | |
| 6 | Padding-410M | s42 | 6/8 | 0/8 | 0/8 | 8/8* | 6/8 | 6/8→**6/8** = | 6/8→**0/8** ↓↓ | MISSING_3SIGMA |
| 7 | SmolLM3-3B | s42 | 3/8 | 4/8 | 0/8 | 0/8 | 0/8 | 0/8→**0/8** = | 0/8→**0/8** = | |
| 8 | Pythia-410M | s43 | 6/8 | 0/8 | 0/8 | 8/8* | 6/8 | 6/8→**6/8** = | 0/8→**0/8** = | MISSING_3SIGMA |
| 9 | C4 Pythia-1B | s42 | 8/8 | 2/8 | 0/8 | 8/8 | 4/8 | 8/8→**5/8** ↓ | 4/8→**1/8** ↓ |  |
| 10 | C4 Pythia-1B | s43 | 7/8 | 4/8 | 0/8 | 8/8 | 4/8 | 8/8→**5/8** ↓ | 5/8→**2/8** ↓ | p_fdr=0.050 边界 |
| 11 | Pythia-1.4B | s42 | 2/8 | 2/8 | 1/8 | 8/8 | 0/8 | 2/8→**1/8** ↓ | 0/8→**0/8** = | |
| 12 | Pythia-1.4B | s43 | 6/8 | 7/8 | 2/8 | 8/8 | 4/8 | 6/8→**7/8** ↑ | 3/8→**4/8** ↑ | K_INCREASED |
| 13 | OPT-1.3B | s43 | 6/8 | 0/8 | 0/8 | 0/8 | 4/8 | 0/8→**0/8** = ✓ | — | verification ✓ |

`*` = MISSING_3SIGMA: 使用 2σ `significant` 作为 fallback，实际 3σ 值可能更低

## Key Observations

1. **D111 impact is severe**: diff_xcorr peak_lag 几乎全部 ≤ 0，diff_fwd 最高仅 2/8 (Pythia-1.4B s43)。naive_fwd 在有正 lag 的实验中保留，但多数实验 naive lag 也是负数。

2. **D105 impact**: 3σ threshold 在 GPT-2m/OPT/SmolLM3 等实验中全部为 False，大幅削减 K 值。只有 C4 Pythia-1B (两个 seed) 和 Pythia-1.4B (两个 seed) 保持全部 8/8 threshold_3σ=True。

3. **联合影响**: K≥3 从 mean ~5.5/8 降至 mean ~3.0/8。K≥4 从 mean ~2.8/8 降至 mean ~0.8/8。

4. **MISSING_3SIGMA 风险**: 实验 1/2/6/8 的 threshold 使用 2σ fallback。如果实际 3σ 结果更差，K≥3 可能进一步下降：
   - Padding-410M s42 和 Pythia-410M s43 的 K≥3=6/8 依赖于 thresh*+permG+TY=3，如果 thresh 3σ 变 False，K≥3 将降至 4/8 (仅 permG+TY=2 的 pair 会失去 K≥3)
   - 但对于这两个实验，6个非 mauve pair 的 permG+TY 都=2，加上 thresh=1 恰好=3。thresh 变 False → K=2 → K≥3 降到 0/8

5. **Pythia-1.4B s43 K 上升**: 唯一 K 值上升的实验。7/8 naive_fwd (多数 lag=1 或 lag=5) + 8/8 thresh_3σ + 6/8 permG + 4/8 TY 给出强 K 值。上升原因可能是 registry 基于不同分析文件或计算方法。

6. **验证通过**: OPT-1.3B s43 K≥3=0/8 符合预期。
