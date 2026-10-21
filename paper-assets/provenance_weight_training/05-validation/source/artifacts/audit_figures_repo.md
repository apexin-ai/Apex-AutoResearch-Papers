# Figure Data Source Audit & Anonymous Repo Check
**Date:** 2026-05-24 | **DDL:** 2026-05-25 (EMNLP 2026 ARR May)

---

## Part A: Figure Data Source Verification

### Authoritative Figure Script
**`artifacts/figures/generate_paper_figures.py`** (local) — generates all 4 paper figures with hardcoded data.

Server also has `scripts/generate_figures.py` (reads from `figure_data.json`) and individual scripts in `scripts/figures/`, but these are **stale/superseded**.

---

### Figure 1: grid_b_trend_clean (Main Text)

| Data Point | Figure Script | Registry (seed 42) | Match? |
|---|---|---|---|
| b=0.1 PPL | 17.657 | 17.657 | OK |
| b=0.2 PPL | 17.640 | 17.640 | OK |
| b=0.3 PPL | 17.640 | 17.640 | OK |
| b=0.5 PPL | 17.651 | 17.651 | OK |
| b=1.0 PPL | 17.692 | 17.692 | OK |
| b=1.5 PPL | 17.718 | 17.718 | OK |
| b=2.0 PPL | 17.741 | 17.741 | OK |
| b=3.0 PPL | 17.774 | 17.774 | OK |
| b=5.0 PPL | 17.818 | 17.818 | OK |
| Uniform baseline | 17.694 | 17.6939 (seed 42) | OK (rounded) |
| Cross-seed b=0.5 s123 | 17.638 | 17.638 | OK |
| Cross-seed b=0.5 s456 | 17.650 | 17.650 | OK |
| ESS-only b* mean ~3.5 | annotation | ~3.5 (registry) | OK |
| Adaptive b* mean ~0.9 | annotation | ~1.4 (tau=0.8 extraction) | **MINOR**: caption says ~0.9, extraction says ~1.4 for tau=0.8; may refer to tau=0.7 |

**Caption (results.tex):** Mentions b>=2 degradation zone, ESS-only b*~3.5, adaptive b*~0.9. Consistent with figure script annotations.

**Verdict: OK** (all grid data match registry)

---

### Figure 2: constraint_regime_decomposition (Appendix) — CRITICAL MISMATCH

| Data Point | Figure Script | binding_stats_seed42.json (server) | Paper Text / Caption | Match? |
|---|---|---|---|---|
| rho=0.4 alpha_eff % | **38.2%** | 38.3% | **~50%** | **CRITICAL MISMATCH** |
| rho=0.4 ESS % | **59.8%** | 59.78% | **~44%** | **CRITICAL MISMATCH** |
| rho=0.4 clean % | **2.0%** | 1.91% | **~6% (5.8%)** | **CRITICAL MISMATCH** |
| rho=0.6 alpha_eff % | **33.4%** | N/A | **~47%** | **CRITICAL MISMATCH** |
| rho=0.6 ESS % | **66.0%** | N/A | **~49%** | **CRITICAL MISMATCH** |
| rho=0.6 clean % | **0.6%** | N/A | **~5%** | **CRITICAL MISMATCH** |

**Root cause:** The figure script and `binding_stats_seed42.json` use regime stats from **tau=0.8** experiment (`adaptive_fix_seed42`). The paper text and caption report stats from **tau=0.7** (the paper's recommended setting). The `classify_regime()` in `extract_figure_data.py` uses `tau=0.8` as default:
```python
def classify_regime(b, alpha_eff, tau=0.8):
    if b == 0.0: return "clean"
    if alpha_eff >= tau - 0.005: return "alpha_eff_binding"
    return "ess_binding"
```
At tau=0.7 the threshold for alpha_eff-binding is lower (0.695), so more batches qualify as alpha_eff-binding (~50% vs 38%), and more batches have b*=0 (clean ~6% vs 2%).

**Impact:** The rendered figure bars will show 38/60/2 while the caption reads ~50/44/6. A reviewer will immediately notice this inconsistency.

**Fix needed:** Re-extract regime stats with tau=0.7 (from `tau_0.7_seed42` experiment), or regenerate from step_metrics.jsonl with `classify_regime(b, alpha_eff, tau=0.7)`. Update figure script hardcoded values.

---

### Figure 3: tau_rho_rank_preservation (Appendix, 2-panel)

| Data Point | Figure Script | Registry | Paper Caption | Match? |
|---|---|---|---|---|
| tau=0.5, rho=0.4 | 17.688 | 17.688 | — | OK |
| tau=0.6, rho=0.4 | 17.6805 | 17.681 | — | OK (rounding) |
| tau=0.7, rho=0.4 | 17.6793 | 17.679-17.680 | — | OK (rounding) |
| tau=0.8, rho=0.4 | **17.6527** | **17.644** | — | **DISCREPANCY (0.009)** |
| tau=0.9, rho=0.4 | 17.712 | 17.712 | — | OK |
| tau=0.95, rho=0.4 | 17.723 | 17.723 | — | OK |
| tau=0.6, rho=0.6 | 17.7359 | ~17.735 | — | OK |
| tau=0.7, rho=0.6 | 17.730 | ~17.732 | — | OK (close) |
| tau=0.8, rho=0.6 | 17.740 | ~17.735 | — | OK (close) |
| Uniform rho=0.4 | 17.6939 | 17.6939 | — | OK |
| Uniform rho=0.6 | 17.766 | 17.766 (seed 42) | — | OK |
| Caption: tau=0.7 better at rho=0.6 | — | — | t=-4.70, p<0.05, Delta=-0.005 | Internally consistent |

**tau=0.8 discrepancy:** Figure uses 17.6527 but registry says 17.644. Likely the figure uses an older run result. Difference is 0.009 PPL — small but visible on a zoomed-in plot. The star marker (optimal at tau=0.8) will be plotted at wrong height.

**Note:** This figure correctly shows tau=0.8 as optimal for rho=0.4 and tau=0.7 for rho=0.6, consistent with paper narrative.

---

### Figure 4: dr_dual_curve (Appendix) — MODERATE ISSUE

| Data Point | Figure Script | Registry / Text | Match? |
|---|---|---|---|
| D&R raw q>0.3 PPL | 17.250 | 17.250 ± 0.001 (3 seeds) | OK |
| D&R raw retention 31.5% | 31.5 | 31.5% (results.tex) | OK |
| D&R epoch-matched q>0.07 | 17.620 | 17.620 (registry) | OK |
| D&R epoch-matched q>0.09 | 17.628 | 17.628 (registry) | OK |
| Uniform reference line | 17.694 | 17.694 | OK |
| **Adaptive reference line** | **17.651** | **17.674 (paper main result, tau=0.7 mean)** | **MISMATCH** |
| Epoch annotations (6.7x, 3.2x, 1.6x) | present | consistent with text | OK |

**Adaptive reference line:** Figure labels it "Adaptive b*" at 17.651, but the paper's main adaptive result is 17.674 (tau=0.7, 3-seed mean). 17.651 matches grid b=0.5 (seed 42), not the adaptive dual-constraint method. This mislabels a grid-search result as "Adaptive b*".

**Fix needed:** Update adaptive reference to 17.674 (tau=0.7 mean) or 17.680 (tau=0.7 seed 42) to match the paper's reported adaptive result.

---

### Figure 5: delta_vs_rho (Appendix, referenced in tex)

Not in `generate_paper_figures.py`. Generated separately. Caption mentions transition between rho=0.3 and rho=0.4. Numbers in caption are qualitative (no hardcoded PPL), consistent with paper narrative.

---

### Stale/Superseded Figure Scripts (NOT used for final figures)

| Script | Location | Issue |
|---|---|---|
| `plot_tau_ppl_curve.py` | local artifacts/ | Uses different PPL values (e.g., tau=0.8: 17.653 vs 17.6527 in authoritative script) |
| `plot_rho_comparison.py` | local artifacts/ | Uses old ESS-only value 17.730 vs registry ~17.737 |
| `plot_grid_b_sweep.py` | local artifacts/ | Missing b=0.1, b=0.2 data points |
| `fig_b_ppl_curve.py` | server scripts/figures/ | Different seed42 b=0.3 value (17.64 vs 17.640) |
| `fig_tau_sweep.py` | server scripts/figures/ | Uses tau=0.8 PPL=17.653 (different from both 17.6527 and 17.644) |
| `fig_rho_sensitivity.py` | server scripts/figures/ | Uses "Adaptive tau=0.8" label — stale, paper uses tau=0.7 |
| `generate_figures.py` | server scripts/ | Reads figure_data.json; adaptive_mean=17.6508 differs from registry |

---

### CSV Data File Cross-Check

**`figure_data.json` (server):**
- tau_sweep PPL values match `generate_paper_figures.py` Fig 3 data exactly
- method_comparison adaptive_dual = [17.6527, 17.6432, 17.6566] — but registry says [17.644, 17.6308, 17.6419]. **All three seeds are ~0.01 higher in figure_data.json than registry.** Likely an older evaluation run.

**`binding_stats_seed42.json` (server):**
- Regime percentages: 38.3% / 59.8% / 1.9% — matches figure script but NOT paper text (~50% / ~44% / ~6%)
- Confirmed: this data is from tau=0.8 experiment, NOT tau=0.7

---

### Text/Caption Number Cross-Check Summary

| Number in Paper Text | Source | Figure Consistent? |
|---|---|---|
| Adaptive B=4: 17.674 ± 0.007 | results.tex (tau=0.7 mean) | Fig 4 uses 17.651 — **NO** |
| Uniform B=4: 17.694 ± 0.008 | results.tex | All figures use 17.694 — YES |
| Delta(B=4) = -0.020 | results.tex | Not directly in figures — N/A |
| Delta(B=8) = -0.052 | results.tex | Not in figures — N/A |
| Delta(B=16) = -0.068 | results.tex | Not in figures — N/A |
| ~50% alpha_eff / ~44% ESS / ~6% clean | results.tex + caption | Fig 2 shows 38.2/59.8/2.0 — **NO** |
| Sharpening ratio ~5.9x | ROADMAP | Not directly in any figure — N/A |
| ESS-only: 17.737 | results.tex | Not in authoritative figures — N/A |
| alpha_eff-only: 17.742 | results.tex | Not in authoritative figures — N/A |

---

## Part B: Anonymous Repository Check

| Check | Result |
|---|---|
| URL | https://github.com/anonymous-nlp-2026/provenance_weight_training |
| Visibility | **Public** (confirmed via API: `"private": false, "visibility": "public"`) |
| Default branch | main |
| Commits | 2 |
| Branches | 1 (main) |
| Last push | **2026-05-23T19:02:12Z** (yesterday) |
| Size | 123 KB |
| Languages | Python 68.6%, Shell 31.4% |
| Root structure | 8 directories (analysis, data_generation, detector, evaluation, figures, scripts, training, weighting) + ~50 root-level files |
| Total file count | **Cannot verify 144 files** — WebFetch only shows root-level items; subdirectory contents not enumerable via web. Root shows ~58 items. |
| README | Present, title matches paper: "When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining" |

**Issues:**
1. Only 2 commits — typical for anonymous submission (squashed history), acceptable
2. Cannot confirm exact 144 file count from web — would need `git clone` to verify
3. Repo was pushed yesterday (May 23) — current

---

## Summary: Action Items (Priority Order)

### CRITICAL (must fix before submission)

1. **Fig 2 constraint_regime_decomposition:** Re-extract regime stats from tau=0.7 experiment and update hardcoded values in `generate_paper_figures.py`. Current figure shows tau=0.8 data (38/60/2%) while caption and text describe tau=0.7 data (~50/44/6%).

2. **Fig 4 adaptive reference line:** Change from 17.651 (grid b=0.5) to 17.674 (tau=0.7 3-seed mean, the paper's reported adaptive result). Currently mislabels a grid-search result as "Adaptive b*".

### MODERATE (should fix)

3. **Fig 3 tau=0.8 PPL:** Update 17.6527 → 17.644 to match registry. Discrepancy of 0.009 PPL.

4. **figure_data.json on server:** adaptive values ~0.01 higher than registry across all seeds. Server data appears stale; not critical if `generate_paper_figures.py` is used for final figures.

### LOW (cosmetic)

5. **Stale scripts cleanup:** 6+ superseded figure scripts on server and local. Non-blocking but could cause confusion if someone re-runs wrong script.

6. **Anonymous repo file count:** Verify 144 files by cloning locally if needed.
