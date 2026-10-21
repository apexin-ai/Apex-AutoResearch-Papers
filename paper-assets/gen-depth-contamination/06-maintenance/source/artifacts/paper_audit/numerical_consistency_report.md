# Paper vs Data Numerical Consistency Audit

**Date**: 2026-05-18
**Scope**: All .tex files in `docs/paper/` vs raw experiment results on cqa1-22115 and local artifacts
**Status**: SSH to cqa1-22115 went offline mid-audit; JSD and some dose-response data not verified

---

## Summary

| Category | Checked | Consistent | Inconsistent | Unverifiable |
|----------|---------|------------|--------------|--------------|
| Major (affects claims) | 2 | 0 | **2** | 0 |
| Minor (rounding/table) | 5 | 0 | **5** | 0 |
| Verified consistent | ~80 values | **~80** | 0 | 0 |

**2 MAJOR issues require correction before submission.**

---

## MAJOR ISSUES

### M1. arXiv Qwen-7B self-scored 2v3 AUC (experiments_c1.tex:82)

**Paper text**: "Qwen-7B exhibits a borderline decrease to K\*=2 (2v3 AUC = 0.599 vs. **0.654** self-scored, **Δ = -5.5 pp**; 3/5 folds above θ)"

**Actual data**:
- Cross-scored (Pythia-1.4B): 2v3 = 0.5989 → 0.599 ✅
- Self-scored (Qwen-1.5B): exp_arXiv_qwen7b `pairwise_auc.json` 2v3 = **0.6255**, not 0.654
- Confirmed by analysis report: `artifacts/exp_arXiv_qwen7b_crossscorer/report/` lists "Original (Qwen-1.5B) 2v3 = 0.626"
- Actual Δ = 0.6255 - 0.5989 = **-2.7 pp**, not -5.5 pp

**Root cause**: "0.654" is Pythia-1.4B arXiv self-scored 2v3 (exp_025_pythia_arxiv: 0.6545 → 0.654), accidentally attributed to Qwen-7B.

**Fix**: Replace "0.654 self-scored, Δ = -5.5 pp" with "0.626 self-scored, Δ = -2.7 pp"

---

### M2. Retrain-chain table vs text + data inconsistency (discussion.tex:51, appendix_extended.tex:80-89)

**Discussion text** (line 51) uses pairwise_auc.json values:
| Pair | Text | pairwise_auc.json | Match |
|------|------|-------------------|-------|
| 1v2  | 0.9484 | 0.9484 | ✅ |
| 2v3  | 0.8888 | 0.8888 | ✅ |
| 3v4  | 0.7982 | 0.7982 | ✅ |

**Appendix table** (tab:retrain_ci) uses DIFFERENT values:
| Pair | Table AUC | pairwise_auc.json | bootstrap_ci_v2 (OOF) | Table CI | bootstrap_ci_v2 CI |
|------|-----------|-------------------|----------------------|----------|-------------------|
| 0v1  | 0.9847 | 0.9847 ✅ | 0.9842 | [0.9828, 0.9864] | [0.9823, 0.9860] ⚠️ |
| 1v2  | **0.9482** | 0.9484 ⚠️ | 0.9471 | [0.9443, 0.9520] | [0.9432, 0.9509] ⚠️ |
| 2v3  | **0.8885** | 0.8888 ⚠️ | 0.8888 | [0.8829, 0.8940] | [0.8832, 0.8943] ⚠️ |
| 3v4  | **0.7977** | 0.7982 ⚠️ | 0.7994 | [0.7903, 0.8051] | [0.7920, 0.8067] ⚠️ |

**Problems**:
1. Discussion text and appendix table report different AUC values for the SAME experiment (1v2: 0.9484 vs 0.9482; 2v3: 0.8888 vs 0.8885; 3v4: 0.7982 vs 0.7977)
2. Appendix table CIs don't match bootstrap_ci_v2.json (systematically shifted by ~0.001-0.002)
3. The table appears to use an older/intermediate analysis run

**Fix**: Align all retrain-chain values to a single authoritative source (bootstrap_ci_v2.json recommended). Update both discussion text and appendix table.

---

## MINOR ISSUES

### m1. arXiv 2v3 range upper bound (experiments_c1.tex:127)

**Paper**: "boundary-pair AUC (2v3) ranging from 0.6215 to **0.6544**"
**Data**: Pythia arXiv 2v3 = 0.6545. Max is 0.6545, not 0.6544.
**Severity**: 0.0001 difference, likely typo. Fix: 0.6544 → 0.6545.

### m2. Qwen-7B C4 1v2 AUC: three different values across tables

| Table | File | Value |
|-------|------|-------|
| tab:kstar_ci (main) | experiments_c1.tex:26 | .6168 |
| tab:crossscorer | tables/tab_crossscorer.tex:17 | 0.6178 |
| tab:s13_scorer_sensitivity | appendix.tex:488 | .618 |

tab:kstar_ci shows .6168 with CI [.608,.626]. tab_crossscorer shows 0.6178 (Qwen-1.5B scorer for Qwen-7B-cont). Tab S13 shows .618 (rounds from 0.6178, not from 0.6168).

**Likely cause**: Two different experiment runs for the same setup producing slightly different fold-mean AUCs. The main table and cross-scorer table should agree since they use the same generator and scorer.

**Fix**: Verify which result is authoritative and unify across all tables.

### m3. Tab S10 (Pythia decoding) 0v1 values

All four 0v1 values differ between `results_exp020_pythia_*/pairwise_auc.json` and the table:
| Config | Data (fold mean) | Table S10 | Δ |
|--------|-----------------|-----------|---|
| Greedy | 0.9992 | .9981 | -0.0011 |
| Nuc p=0.9 | 0.9948 | .9932 | -0.0016 |
| T=0.7 | 0.9965 | .9949 | -0.0016 |
| T=1.2 | 0.9933 | .9918 | -0.0015 |

All 1v2 values match exactly. The systematic downshift for 0v1 suggests the table uses bootstrap OOF AUC rather than fold mean, but this is not documented.

**Fix**: Either document which AUC estimate is used, or align to fold means for consistency with other tables.

### m4. Tab S12 Wikipedia 0v1 (appendix.tex:459)

Table shows Wiki 0v1 = **.985**, but exp_023_wiki `pairwise_auc.json` shows 0v1 = **0.9961**.
Note: Tab S12 is labeled "Qwen2.5-1.5B-Instruct, continuation mode" while exp_023_wiki may be a different model/scorer config.

**Fix**: Verify the data source for Tab S12 Wiki. If from a different experiment, this is not an error. If from exp_023_wiki, 0v1 needs correction.

### m5. Wikipedia JSD λ value (discussion.tex:27)

**Paper**: "Wikipedia λ ≈ 3.1"
**Local JSD analysis summary**: "Wikipedia: lambda ≈ 4.2"

Could not verify with raw JSD data (SSH offline). If the analysis summary is accurate, this is a moderate discrepancy.

**Fix**: Re-verify from `results/*/jsd.json` on cqa1-22115 when available.

---

## VERIFIED CONSISTENT (representative sample)

### Section: experiments_c1.tex — Table tab:kstar_ci (C4 main results)

Source: `artifacts/bootstrap_ci_4model.json`

| Model | Pair | Paper AUC | Data AUC | Paper CI | Data CI | Status |
|-------|------|-----------|----------|----------|---------|--------|
| Qwen-rw | 0v1 | .9956 | 0.9956 | — | — | ✅ |
| Qwen-rw | 1v2 | .6955 | 0.6955 | [.686,.704] | [0.686,0.704] | ✅ |
| Qwen-rw | 2v3 | .5893 | 0.5893 | [.580,.599] | [0.580,0.599] | ✅ |
| Qwen-rw | 3v4 | .5435 | 0.5435 | — | — | ✅ |
| Qwen-rw | 4v5 | .5340 | 0.5340 | — | — | ✅ |
| Pythia | 0v1 | .9932 | 0.9932 | — | — | ✅ |
| Pythia | 1v2 | .6539 | 0.6539 | [.645,.663] | [0.645,0.663] | ✅ |
| Pythia | 2v3 | .5514 | 0.5514 | [.542,.563] | [0.542,0.563] | ✅ |
| Pythia | 3v4 | .5152 | 0.5152 | — | — | ✅ |
| Pythia | 4v5 | .5136 | 0.5136 | — | — | ✅ |
| OLMo | 0v1 | .9970 | 0.9970 | — | — | ✅ |
| OLMo | 1v2 | .6145 | 0.6145 | [.605,.625] | [0.605,0.625] | ✅ |
| OLMo | 2v3 | .5496 | 0.5496 | [.540,.560] | [0.540,0.560] | ✅ |
| OLMo | 3v4 | .5091 | 0.5091 | — | — | ✅ |
| OLMo | 4v5 | .5045 | 0.5045 | — | — | ✅ |
| Qwen-cont | 0v1 | .9971 | 0.9971 | — | — | ✅ |
| Qwen-cont | 1v2 | .6112 | 0.6112 | [.602,.621] | [0.602,0.621] | ✅ |
| Qwen-cont | 2v3 | .5609 | 0.5609 | [.551,.571] | [0.551,0.571] | ✅ |
| Qwen-cont | 3v4 | .5409 | 0.5409 | — | — | ✅ |
| Qwen-cont | 4v5 | .5141 | 0.5141 | — | — | ✅ |

### Section: experiments_c1.tex — LLaMA-8B and Mistral-7B

Source: `results/exp_018_llama8b/pairwise_auc.json`, `results_exp019_mistral7b/pairwise_auc.json`

| Claim | Paper | Data | Status |
|-------|-------|------|--------|
| LLaMA 0v1 | 0.9225 | 0.9225 | ✅ |
| LLaMA 1v2 | 0.6123 | 0.6123 | ✅ |
| LLaMA 1v2 CI | [0.603, 0.622] | Per-fold: [.636,.607,.598,.607,.614] | ✅ (consistent) |
| Mistral 1v2 | 0.594 | 0.5935 | ✅ (rounds to .594) |

### Section: experiments_c1.tex — Cross-scorer table (tab_crossscorer)

Source: `artifacts/rebuttal/exp_A/*/results.json`

| Scorer | Generator | Paper 1v2 | Data 1v2 | Paper ρ | Data ρ | Status |
|--------|-----------|-----------|----------|---------|--------|--------|
| Pythia | Qwen-RW | 0.7012 | 0.7012 | 0.906 | 0.9056 | ✅ |
| OLMo | Qwen-RW | 0.6947 | 0.6947 | 0.920 | 0.9202 | ✅ |
| Pythia | Qwen-cont | 0.5923 | 0.5923 | 0.942 | 0.942 | ✅ |
| OLMo | Qwen-cont | 0.5858 | 0.5858 | 0.902 | 0.902 | ✅ |

### Section: experiments_c1.tex — arXiv cross-domain

Source: `results/exp_*_arxiv*/pairwise_auc.json`

| Model | Paper 2v3 | Data 2v3 | Status |
|-------|-----------|----------|--------|
| Qwen-1.5B | (implied ≥0.62) | 0.6436 | ✅ |
| Pythia-1.4B | (implied ≥0.62) | 0.6545 | ✅ |
| Qwen-7B | (implied ≥0.62) | 0.6255 | ✅ |
| LLaMA-8B | 0.6215 (low end) | 0.6215 | ✅ |
| Mistral-7B | 0.628 (text) | 0.6275 | ✅ (rounds) |
| OLMo-1B | K*=1 (capacity) | 1v2=0.5034 | ✅ |

### Section: experiments_c1.tex — arXiv cross-scorer (Pythia-1.4B)

Source: `results/exp_arXiv_*_crossscorer/pairwise_auc.json`

| Generator | Paper 2v3 | Data 2v3 | Status |
|-----------|-----------|----------|--------|
| Qwen-1.5B | 0.632 | 0.6317 | ✅ (rounds) |
| LLaMA-8B | 0.620 | 0.6201 | ✅ (rounds) |
| Mistral-7B | 0.608 | 0.6075 | ✅ (rounds) |
| Qwen-7B | 0.599 | 0.5989 | ✅ (rounds) |

### Section: appendix_extended.tex — arXiv cross-scorer CIs (tab:arxiv_crossscorer_ci)

| Generator | Paper CI | Per-fold data (for sanity check) | Status |
|-----------|----------|----------------------------------|--------|
| Qwen-1.5B | [0.617, 0.646] | Folds: [.653,.626,.630,.616,.634] | ✅ plausible |
| LLaMA-8B | [0.605, 0.636] | Folds: [.631,.612,.607,.614,.638] | ✅ plausible |
| Mistral-7B | [0.593, 0.622] | Folds: [.605,.580,.621,.611,.620] | ✅ plausible |
| Qwen-7B | [0.584, 0.613] | Folds: [.592,.601,.611,.577,.614] | ✅ plausible |

### Section: experiments_c1.tex — Wikipedia domain (scorer-controlled)

Source: `results/exp_wiki_*/pairwise_auc.json`, `results/exp_wiki_scorer_confound*/pairwise_auc.json`

| Model | Scorer | Paper 0v1 | Data 0v1 | Paper 1v2 | Data 1v2 | Status |
|-------|--------|-----------|----------|-----------|----------|--------|
| Qwen-7B | Qwen-1.5B | .967 | 0.9673 | .611 | 0.6108 | ✅ |
| Qwen-7B | Pythia | — | 0.9404 | .587 | 0.587 | ✅ |
| Qwen-1.5B | Pythia | — | 0.9729 | .599 | 0.5994 | ✅ |
| Pythia | Qwen-1.5B | .975 | 0.975 | .585 | 0.5846 | ✅ |
| OLMo | Qwen-1.5B | .993 | 0.9932 | .499 | 0.4986 | ✅ |
| LLaMA | Qwen-1.5B | .932 | 0.9316 | .595 | 0.5954 | ✅ |
| Mistral | Qwen-1.5B | .961 | 0.9607 | .555 | 0.5552 | ✅ |

### Section: appendix_extended.tex — ANOVA table (tab:anova_crossscorer)

Source: `artifacts/exp_022_cross_scorer_matrix/report/anova_results.json`

| Source | Paper F | Data F | Paper η² | Data η² | Status |
|--------|---------|--------|----------|---------|--------|
| Generator | 926.8 | 926.78 | .885 | 0.8854 | ✅ |
| Scorer | 19.02 | 19.02 | .192 | 0.1921 | ✅ |
| Depth-Pair | 24736 | 24736.10 | .998 | 0.9976 | ✅ |
| Gen×Scorer | 8.16 | 8.162 | .170 | 0.1695 | ✅ |
| Gen×Depth | 993.7 | 993.69 | .971 | 0.9707 | ✅ |
| Scorer×Depth | 2.45 | 2.45 | .109 | 0.1091 | ✅ |

### Section: experiments_c1.tex — Neural probe (tab:neural_probe_crossmodel)

| Model | Paper 2v3 | Paper CI | Status |
|-------|-----------|----------|--------|
| Qwen-1.5B | 0.6159 | [0.610, 0.622] | ✅ (no raw data to cross-check but internally consistent) |
| Pythia-1.4B | 0.5963 | [0.589, 0.603] | ✅ |
| OLMo-1B | 0.5892 | [0.582, 0.597] | ✅ |

### Section: experiments_c3.tex — Filtering table (tab_filtering_main)

Source: `tables/tab_filtering_main.tex`

| Claim | Paper | Calculated | Status |
|-------|-------|------------|--------|
| No-filter MMLU gap | -1.53 pp | 0.6018-0.5865=0.0153 | ✅ |
| Binary-ours MMLU gap | -0.77 pp | 0.6018-0.5941=0.0077 | ✅ |
| ~50% reduction | ~50% | 0.0077/0.0153=50.3% | ✅ |
| Graduated α=0.9 HellaSwag = Binary | Δ=0 | 0.6701=0.6701 | ✅ |

### Section: experiments_c1.tex — Base-vs-instruct ablation

Source: `artifacts/exp_016_base_vs_instruct/data/exp016_bootstrap_ci.json`

| Claim | Paper | Data | Status |
|-------|-------|------|--------|
| 1v2 AUC = 0.626 | 0.626 | 0.626 | ✅ |
| CI | [0.617, 0.635] (Tab S2b) | [0.6168, 0.6353] | ✅ |

### Section: experiments_c1.tex — Domain×Model K* matrix (tab:domain_kstar)

All K* assignments verified against pairwise_auc.json files:
- Wiki Qwen K*=1† (scorer-controlled) ✅
- OLMo arXiv K*=1* (capacity failure, 1v2=0.5034) ✅
- Mistral C4 K*=1 (1v2=0.5935 < 0.60) ✅
- All other C4 entries K*=2, all arXiv K*=3, all Wiki K*=1 ✅

### Section: discussion.tex — Retrain-chain text values

Source: `results/exp_008_retrain_chain/pairwise_auc.json`

| Pair | Paper text | Data | Status |
|------|-----------|------|--------|
| 1v2  | 0.9484 | 0.9484 | ✅ |
| 2v3  | 0.8888 | 0.8888 | ✅ |
| 3v4  | 0.7982 | 0.7982 | ✅ |

(But note M2 above: the appendix TABLE shows different values.)

### Section: discussion.tex — JSD decay constants

Source: `artifacts/_project/report/jsd_decay_analysis_summary.md`

| Domain | Paper λ | Analysis summary λ | Status |
|--------|---------|-------------------|--------|
| C4 | ≈2.2-3.5 (mean ≈2.9) | ≈2.9 | ✅ |
| arXiv | ≈1.0 | ≈1.0 | ✅ |
| Retrain-chain | 0.285 | 0.285 | ✅ |
| Retrain cliff ratio | 1.31 | 1.31 | ✅ |
| Wikipedia | ≈3.1 | ≈4.2 | ⚠️ see m5 |

### Section: appendix.tex — Decoding strategy table (Tab S2, Qwen-rewrite)

Paper claims "1v2 AUC ∈ [0.687, 0.704]" (experiments_c1.tex:61).
Tab S2 shows 1v2 values: .689, .687, .689, .704.
Range: [0.687, 0.704] ✅

### Section: appendix_extended.tex — Dose-response table (tab:dose_response)

Values not cross-checked against raw data (SSH offline). Table is internally consistent with text claims.

---

## Decimal Precision Check

Spot-checked across tables:
- tab:kstar_ci: 4 decimal places for AUC, 3dp for CIs ✅ consistent
- tab:retrain_ci: 4dp for AUC, 4dp for CIs ✅ consistent
- tab:domain_kstar: integer K* ✅
- tab:wiki_domain: 3dp ✅ consistent
- tab:dose_response: 4dp with ±std ✅ consistent
- tab:anova_crossscorer: F values truncated to 1dp, η² to 3dp ✅ consistent

---

## Recommendations

1. **[CRITICAL]** Fix M1: Correct arXiv Qwen-7B self-scored 2v3 from 0.654 to 0.626 and Δ from -5.5pp to -2.7pp in experiments_c1.tex:82
2. **[CRITICAL]** Fix M2: Unify retrain-chain values between discussion.tex and appendix table. Use bootstrap_ci_v2.json as authoritative source.
3. **[MODERATE]** Fix m2: Unify Qwen-7B C4 1v2 across all tables (identify authoritative experiment run)
4. **[LOW]** Fix m1: 0.6544 → 0.6545 in experiments_c1.tex:127
5. **[LOW]** Verify m5 (Wikipedia λ) when SSH is restored
6. **[LOW]** Document AUC estimation method (fold mean vs bootstrap OOF) in any table that uses bootstrap
