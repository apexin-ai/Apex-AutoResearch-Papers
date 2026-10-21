# Response to R39 Review — Revision Summary

We thank the reviewers for their thorough feedback. Below we detail all changes made, organized by direct reviewer concerns followed by proactive improvements.

---

## Tier 1: Direct Responses to R39 Concerns

### 1. Statistical Significance (W4 / N2)

**Concern:** 3-seed Holm-Bonferroni p_adj=0.055 does not survive alpha=0.05; core positive claim borderline.

**What we did:** Added 2 seeds (2024, 3141) for 5-seed coverage on core configurations. Ran seed-replication Fisher z-test with Holm correction (k=5), yielding p_adj=0.013.

> **Before:** "Holm p_adj=0.055" reported alone; abstract uses "statistically significant."
>
> **After:** Main text retains global Holm p=0.055 (honest reporting). Section 4.2 adds seed-replication p=0.013 as complementary evidence. Appendix bootstrap signal section provides full analysis.

### 2. Claim Calibration

**Concern:** Abstract/intro state "statistically significant" while Holm p=0.055 > alpha=0.05 -- a direct contradiction.

> **Before:** "statistically significant conditional gains ... Holm p_adj=0.055"
>
> **After:** "conditional gains ... significant under per-family correction p_adj=0.006, global Holm p_adj=0.055"

Removed the phrase "statistically significant." Both p-values are reported; the reader draws their own conclusion.

### 3. Metric Transparency

**Concern:** Table 4 LP +1.39pp lacks metric annotation; 15x discrepancy with corpus micro-F1 (+0.09pp) unexplained.

> **Before:** Table 4 caption has no metric label; +1.39pp cited without micro-F1 counterpart.
>
> **After:** Table 4 caption adds "(instance-averaged F1)." All +1.39pp references include footnote: "Under corpus micro-F1, LP Delta=+0.09 +/- 0.03pp; the larger instance-averaged gains concentrate on few-entity instances."

---

## Tier 2: Proactive Improvements

### 4. ESJ Cross-Dataset Baseline

Added entailment-based self-judgment (ESJ) experiments across all 3 datasets to strengthen the introspection boundary claim (previously single-dataset).

| Dataset | ESJ AUROC | Agreement-based AUROC |
|---------|-----------|----------------------|
| SciERC  | 0.512     | 0.79                 |
| CoNLL   | 0.553     | 0.94                 |
| FewNERD | 0.495     | 0.88                 |

ESJ performs at chance level across all datasets. Added `discussion.tex` paragraph ("Self-verification ruled out") and Appendix `app:esj` table.

### 5. Numerical Audit -- 7 Corrections

| Item | Before | After |
|------|--------|-------|
| LP selection gain | +8pp (no data source found) | +1.39pp (instance-averaged F1) |
| WNUT zero-F1 rate | 51% | 53.7% (unified calculation) |
| Epoch confound LP delta | +0.12 (max seed) | +0.09±0.04 (3-seed mean) |
| SciERC MV sign | ambiguous | confirmed negative across 3 seeds (-0.74 +/- 0.46pp) |
| FewNERD LP rho variance | unchecked | s42 not outlier (sigma=0.04 vs SJ 2.02) |
| Multi-seed table caption | seeds unlisted | Qwen 5 seeds / LLaMA 3 seeds, seed IDs listed |
| fig_bound | missing | degeneracy bound visualization generated |

### 6. Holm Framework Disambiguation

**Concern (implicit):** Two distinct correction frameworks conflated in presentation.

> **Before:** Single "Holm p=0.055" reported without framework specification.
>
> **After:** Explicitly distinguishes global Holm k=57 (p_adj=0.055) vs seed-replication Holm k=5 (p_adj=0.013). All global correction references retain p=0.055. Section 4.2 adds one sentence presenting seed-replication result.

### 7. Language Calibration

> **Before:** "definitive contrast"; "confirming LP as the most robust"
>
> **After:** "clearest positive case"; "consistent with LP being the most stable positive signal"
