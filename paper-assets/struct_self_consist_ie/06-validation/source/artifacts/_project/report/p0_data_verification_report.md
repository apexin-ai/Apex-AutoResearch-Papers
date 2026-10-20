# P0/P1 Data Verification Report

**Date**: 2026-05-19
**Scope**: Four claim-audit flagged inconsistencies in paper vs registry data

---

## Investigation 1: SciERC AUROC Table 1 vs Registry (P0) → FALSE ALARM

### Discrepancy reported

| Signal | Paper Table 1 | Registry exp_012_rerun_1024 | Δ |
|--------|--------------|---------------------------|------|
| VC | .663 | .684 | -2.1pp |
| SJ | .650 | .692 | -4.2pp |
| FK | .602 | .629 | -2.7pp |
| EM | .614 | .749 | -13.5pp |
| LP | .578 | .578 | 0pp |

### Finding

**Not an error.** The paper and registry use different AUROC binarization thresholds:

- **Paper Table 1**: median-split AUROC (`binary = (F1 >= median_F1)`), computed by `analyze_exp015_unified.py`. SciERC NER median F1 = 0.6667.
- **Registry exp_012_rerun_1024**: perfect-extraction AUROC (`binary = (F1 >= 1.0)`), computed by `eval_exp012_rerun_auroc.py`.

For CoNLL (median F1 = 1.0), both definitions coincide → LP matches. For SciERC (median F1 = 0.667), they diverge substantially.

Previous investigation (`d114_auroc_investigation/table1_update.md`) verified all 15 Table 1 values match within rounding error (<0.0005).

### Verification source
- `output/d114_auroc_investigation/unified_auroc.json` — per-seed and aggregated verified AUROC
- `output/d114_auroc_investigation/table1_update.md` — full verification report

### Correct value
Paper Table 1 values are **correct**. No fix needed.

### Recommendation
Registry `exp_012_rerun_1024` AUROC fields should be annotated as "perfect-extraction AUROC (F1>=1.0 threshold)" to prevent future confusion with the paper's median-split AUROC.

---

## Investigation 2: CoNLL LP Selection Δ Inconsistency (P0) → CONFIRMED ERROR

### Discrepancy reported
- Table 3 (experiments.tex:122): CoNLL LP Δ = **-0.85pp**
- Appendix cross-selection (appendix.tex:248): LP F1 = .897, Greedy = .908 → Δ = **-1.1pp**

### Finding

**Table 3's -0.85pp is incorrect.** Two sub-issues:

**Issue A: Wrong LP Δ value.** From `w1_table3_multiseed.json`, CoNLL N=8 seed 42:
- `greedy_f1 = 0.9079`, `lp_sel_f1 = 0.8974`
- `lp_delta_pp = -1.0482`

The appendix cross-selection's -1.1pp = (.897 - .908) is the same computation rounded to 3 decimal places. Both are consistent: **Δ ≈ -1.05pp**.

No known data source produces -0.85pp. The closest match is the SJ selection delta (-0.89pp from `sj_delta_pp = -0.8914`), suggesting a possible column-swap error during table composition.

**Issue B: "3-seed means" claim is false for CoNLL.** The `w1_table3_multiseed.json` file shows `"n_seeds": 1` for `conll_n8` — only seed 42 data exists. The Table 3 caption states "Few-NERD/CoNLL: 3-seed means" which is incorrect.

### Correct value
- LP Δ = **-1.05pp** (seed 42 single-seed, rounded to -1.0pp or -1.1pp)
- Caption should either say "CoNLL: single-seed" or 3-seed data must be generated

### Suggested fix
1. Update Table 3 CoNLL LP Δ from -0.85pp to -1.05pp (or -1.0pp)
2. Update caption to clarify CoNLL and FewNERD are single-seed (seed 42)
3. Or generate seeds 123/456 CoNLL N=8 data and report true 3-seed mean

---

## Investigation 3: FewNERD Degeneracy 13.8% Source (P1) → CORRECT VALUE, WRONG CAPTION

### Discrepancy reported
Paper Table 3: FewNERD degen = 13.8%. Registry per-seed values:
- Seed 42 (exp_021_fewnerd_full): 10.1%
- Seed 123: 13.1%, Seed 456: 12.1%, Seed 789: 11.8%
- 3-seed mean (42/123/456) = 11.8% ≠ 13.8%

### Finding

**13.8% is correct for seed 42** using the unified_metrics definition:

| Source | Definition | Seed 42 value |
|--------|-----------|---------------|
| Registry exp_021_fewnerd_full | `degeneracy_rate` (old, no source tag) | 10.1% |
| `unified_tab_fewnerd_maxlp.json` | constant-F1 gold-filtered | **13.754% → 13.8%** |
| Registry exp_021_fewnerd_n8_seed123 | unified_metrics_constant_f1_gold_filtered | 13.12% |

The registry's 10.1% for seed 42 uses an older/different degeneracy definition (possibly different denominator — total vs gold-filtered, or different F1 comparison logic). The seed-specific experiments (123/456/789) use the unified definition and produce different values.

The `w1_table3_multiseed.json` confirms FewNERD also has `"n_seeds": 1` (seed 42 only).

### Correct value
- **13.8%** is correct for seed 42, unified_metrics constant-F1 gold-filtered
- True 3-seed mean (42/123/456) under unified definition ≈ **13.0%** = (13.75 + 13.12 + 12.12) / 3

### Suggested fix
1. Update Table 3 caption to say "single-seed (seed 42)" for FewNERD (same as CoNLL fix)
2. Or compute unified-definition degen for seeds 123/456 and report 3-seed mean (~13.0%)
3. Update registry exp_021_fewnerd_full to include `degen_rate_source` tag and reconcile with unified definition

---

## Investigation 4: CoNLL Degeneracy 48.4% N=8 vs N=16 (P1) → CONFIRMED ERROR

### Discrepancy reported
Table 3 header says N=8, CoNLL degen = 48.4%. Registry exp_002_conll_n16 (N=16) has degen_rate = 0.4844.

### Finding

**Confirmed: 48.4% is N=16 data, not N=8.**

| Source | N | Degen rate |
|--------|---|-----------|
| `unified_tab_fewnerd_maxlp.json` (seed 42) | 8 | **59.14%** |
| Registry exp_002_conll_n16 (seed 42) | 16 | **48.44%** |
| Registry exp_002_conll_n16_seed123 | 16 | 47.10% |
| Registry exp_002_conll_n16_seed456 | 16 | 55.44% |
| N=16 3-seed mean | 16 | 50.3% |

N=8 produces higher degeneracy (59.1%) because fewer samples → less chance of F1 variation. Table 3 claims N=8 but reports the N=16 value (48.4%).

Other Table 3 CoNLL values (n=2,756, greedy=.908, LP ρ=.302) are consistent with N=8 seed 42 data. Only the degeneracy column was pulled from N=16.

### Correct value
- N=8 CoNLL degeneracy (seed 42) = **59.1%**
- N=16 CoNLL degeneracy (seed 42) = 48.4%

### Suggested fix
Update Table 3 CoNLL degen from 48.4% to 59.1%

---

## Summary

| # | Issue | Severity | Status | Fix needed |
|---|-------|----------|--------|-----------|
| 1 | SciERC AUROC Table 1 vs registry | P0 | **False alarm** | Annotate registry AUROC definition |
| 2 | CoNLL LP Δ inconsistency | P0 | **Confirmed error** | Table 3: -0.85pp → -1.05pp; fix "3-seed" caption |
| 3 | FewNERD degen 13.8% source | P1 | **Value correct, caption wrong** | Fix "3-seed" caption or generate multi-seed data |
| 4 | CoNLL degen 48.4% N mismatch | P1 | **Confirmed error** | Table 3: 48.4% → 59.1% (N=8 value) |

### Cross-cutting issue: Table 3 "3-seed means" caption
Table 3 caption claims "Few-NERD/CoNLL: 3-seed means" but both datasets have only seed 42 data in `w1_table3_multiseed.json`. Either:
- (a) Generate seeds 123/456 for CoNLL N=8 and FewNERD N=8, then report true 3-seed means
- (b) Correct the caption to "single-seed (seed 42)" for these datasets

Option (b) is simpler but weakens statistical credibility. Option (a) requires new inference runs.
