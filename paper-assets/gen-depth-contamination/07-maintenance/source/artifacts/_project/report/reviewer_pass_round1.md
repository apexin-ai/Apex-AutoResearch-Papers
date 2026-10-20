# Reviewer Pass Round 1 — Structured Audit Report

**Date:** 2026-05-14
**Scope:** Full paper review covering Abstract, Introduction, Related Work, Method, Experiments, Discussion, Conclusion, Appendix, References
**Registry snapshot:** All 12 experiments checked (exp_001 through exp_017, mvp_pilot)

---

## Critical

No critical issues found. All quantitative claims match the registry within rounding tolerance. No broken cross-references detected. No missing bib entries.

---

## Warning

### W1. Abstract: cross-model transfer claim lacks mode qualification
- **File:** `main.tex`, line 34
- **Text:** `"Cross-model transfer shows classifiers retain 80--92\% accuracy across generators"`
- **Problem:** The 80--92% range applies only to **continuation-mode** model pairs. Qwen-rewrite→Pythia/OLMo retention is 61--63% (registry exp_013). The abstract says "across generators" without specifying mode, which a reviewer could read as covering all generator pairs including rewrite mode.
- **Context:** Introduction (line 35) correctly says "trained on one continuation-mode model." Conclusion (line 32) correctly says "across continuation-mode model pairs."
- **Fix:** Change to `"classifiers retain 80--92\% accuracy across continuation-mode generators"` or `"across generators in the canonical continuation mode"`.

### W2. Abstract: notation inconsistency — $\Kstar=2$ should be $\Kempirical=2$
- **File:** `main.tex`, line 34
- **Text:** `"we find $\Kstar=2$ is consistent"`
- **Problem:** The task specified `Kstar→Kempirical` notation change in the abstract. The change was applied in later occurrences (abstract uses $\Kempirical=2$ and $\Kempirical^{\text{neural}}=3$ later), but the first occurrence of the finding still uses $\Kstar$. The introduction (line 28) and all other sections consistently use $\Kempirical=2$ for the empirical finding.
- **Fix:** Change `"we find $\Kstar=2$ is consistent"` → `"we find $\Kempirical=2$ is consistent"`. Keep the earlier conceptual mention `"the discrimination boundary $\Kstar$"` as-is (that's the generic concept, not the empirical finding).

### W3. Discussion: graduated filtering paragraph is a visible placeholder
- **File:** `discussion.tex`, lines 135--136
- **Text:** `"\paragraph{Graduated Filtering.} Results for graduated filtering will be added upon completion of ongoing experiments."`
- **Problem:** This renders as a visible placeholder paragraph in the PDF. Exp_006 is RUNNING (10/50 runs done, ETA 05-15 10:43 UTC). The conclusion also has commented-out TODO lines (51--53) but those don't render.
- **Fix:** Remove the placeholder paragraph before any external sharing. Replace with actual results once exp_006 completes.

### W4. Neural probe data sourced from a failed experiment
- **File:** `discussion.tex`, lines 29--35; `conclusion.tex`, lines 45--46
- **Problem:** The neural probe results ($\Kempirical^{\text{neural}}=3$, 2v3 AUC=0.6195) come from exp_015, which the registry marks as **FAILED** (GPU OOM) with the note "仅单数据集，不可用于论文". Only Qwen-cont data was collected; Pythia and OLMo embedding extraction failed.
- **Mitigation:** The paper properly qualifies these as "preliminary" (discussion line 35) and "on one dataset" (abstract line 34). All mentions include caveats about pending cross-model validation. This is defensible for a draft but the registry note explicitly flags this data as unsuitable for the paper.
- **Fix:** Either (a) re-run exp_015 with full 3-dataset coverage after exp_006 frees the GPU, then update the numbers, or (b) further strengthen the caveat language (e.g., "single-dataset pilot result, awaiting replication").

### W5. Discussion: θ-sensitivity paragraph has confusing topic switch
- **File:** `discussion.tex`, lines 110--113
- **Text:** The paragraph starts discussing θ-sensitivity for **decoding strategies**, then the semicolon-joined clause `"at $\theta = 0.70$, $\Kempirical = 1$ for all model-mode configurations"` switches to **model-mode** results without transition.
- **Problem:** At θ=0.70 for decoding, the result is K\*=1 for 3/4 configs and K\*=2 for config4\_t12 (registry exp_003). The text skips the decoding result at θ=0.70 entirely and jumps to model-mode. A reviewer following the decoding analysis would expect the decoding result.
- **Fix:** Either (a) add the decoding θ=0.70 result first (`"at $\theta = 0.70$, $\Kempirical = 1$ for 3/4 decoding configurations (the exception being $T{=}1.2$, which retains $\Kempirical = 2$)"`) then transition to model-mode, or (b) split into two explicit paragraphs.

---

## Info

### I1. Abstract length
- **File:** `main.tex`, lines 33--35
- **Problem:** The abstract is a single dense paragraph (~230 words). ARR/EMNLP guidelines typically recommend 150--200 words. The neural probe and LLM baseline sentences could be trimmed.
- **Suggestion:** Consider cutting to essentials: K\*=2 finding, cross-model transfer headline, and one secondary finding.

### I2. OBD acronym redefined in Related Work
- **File:** `related_work.tex`, line 39
- **Text:** `"our Ordinal Binary Decomposition (OBD) head"`
- **Problem:** OBD is first defined in `introduction.tex` line 20. Re-defining in Related Work is redundant.
- **Fix:** Remove parenthetical: `"our OBD head follows this principle"`.

### I3. Related Work: frank2001 placement
- **File:** `related_work.tex`, line 39
- **Problem:** Frank & Hall (2001) is cited in the Ordinal Classification paragraph as the origin of decomposing ordinal problems into binary decisions. The bib section header comment (line 210) places it under `% === Ordinal Classification (additional) ===` but the actual bib entry is at line 238, interleaved with newer papers in a different section. Not a rendering issue but source organization is inconsistent.
- **Fix:** Move the bib entry under the Ordinal Classification comment block for source clarity.

### I4. Appendix is minimal
- **File:** `appendix.tex`
- **Problem:** Only one supplementary figure (fig\_s1\_auc\_decay\_ci). Reviewers may expect supplementary tables (full bootstrap CIs, cross-transfer τ matrix, per-depth LLM confusion matrices, feature importance heatmaps).
- **Suggestion:** Expand appendix with exp_003 decoding ablation details, exp_011 per-depth accuracy breakdown, and exp_005 full degradation analysis tables.

### I5. Conclusion: exp-006 TODO comments
- **File:** `conclusion.tex`, lines 51--53
- **Text:** `% TODO: exp-006 graduated filtering 具体结果填充。`
- **Problem:** These are LaTeX comments and don't render, so no reader impact. But Chinese-language TODO comments should be removed before submission to avoid accidental inclusion if comment handling changes.
- **Fix:** Remove or translate to English before final submission.

### I6. Discussion: LLM baseline exclusion rationale could be sharper
- **File:** `discussion.tex`, line 76
- **Text:** `"excluding depth~5 from the 6-class range used in the main feature-based experiments since depths $\geq 3$ are mutually indistinguishable ($\Kempirical = 2$)"`
- **Problem:** If depths ≥3 are mutually indistinguishable, why include depths 3 and 4? The rationale is that K\*=2 means adjacent depths ≥3 are indistinguishable, not that depth 3 = depth 4 in absolute terms. But the parenthetical explanation is ambiguous.
- **Fix:** Clarify: `"excluding depth~5 since adjacent-generation discrimination beyond depth~2 is unreliable ($\Kempirical = 2$)"`.

### I7. Precision: rounding conventions vary
- **File:** Multiple
- **Problem:** AUC values are reported at 4 decimal places in tables (0.6955), 2 decimal places in running text (0.69, 0.70), and 4 decimal places in CIs (0.6015). MAE is 3dp in method (0.984) but 2dp in discussion (1.10, 1.11). While each instance is independently defensible, the inconsistent rounding could be streamlined.
- **Suggestion:** Adopt a uniform convention: 4dp in tables/CIs, 2dp in running text for rounded references.

---

## Verification Summary

### A. Number Consistency ✅

| Claim | Paper value | Registry value | Status |
|-------|-------------|----------------|--------|
| Abstract: cross-model retention | 80--92% | 80.3--91.6% (cont-mode) | ✅ |
| Abstract: binary LLM acc | ~88% | 87.8%, 88.2% | ✅ |
| Abstract: 5-class LLM acc | ~33% | 33.2%, 33.1% | ✅ |
| Abstract: OBD acc | 38.6% | 0.386 | ✅ |
| Abstract: K\*=2 | K\*=2 | All 8 configs K\*=2 | ✅ |
| Abstract: K\*\_neural=3 | 3 | 3 (exp_015, Qwen-cont only) | ✅ |
| Table 3 (kstar\_ci): all values | Match | exp_007 registry | ✅ |
| Table 4 (transfer): all values | Match | exp_013 accuracy\_matrix | ✅ |
| Discussion: 2v3 range | 0.5496--0.5917 | min OLMo 0.5496, max nuc09 0.5917 | ✅ |
| Discussion: 1v2 decoding range | [0.6866, 0.7039] | exp_003 configs | ✅ |
| Discussion: neural 2v3 AUC | 0.6195 | ~0.62 (registry rounds) | ✅ |
| Method: OBD vs multiclass MAE | All 3 families | exp_010 | ✅ |
| Conclusion: T=0.70 | 0.70 | — (formatting) | ✅ |

### B. Claim Strength Consistency ✅ (with W1, W2 exceptions)

| Pattern | Abstract | Intro | Discussion | Conclusion |
|---------|----------|-------|------------|------------|
| K\*=2 "consistent" | ✅ (but uses $\Kstar$, see W2) | ✅ | ✅ | ✅ |
| Neural probe "preliminary" | ✅ | — | ✅ | ✅ |
| Cross-model "tested" qualifier | ⚠️ missing (W1) | ✅ | ✅ | ✅ |

### C. Citation Completeness ✅

- All 28 `\cite` keys have matching `.bib` entries
- 7 new bib entries verified: dohmatob2025strong, feng2025beyond, bao2024fast, frank2001ordinal, alain2017understanding, conneau2018probing, belinkov2022probing
- shumailov2024collapse: volume=631, pages=755--759 ✅
- alain2017: venue=ICLR Workshop ✅
- shi2025: booktitle=Advances in NeurIPS ✅

### D. LaTeX Format ✅

- No bare `AUC` found (all use `\auc` macro)
- K\* notation consistent across body (only abstract W2 exception)
- No `??` cross-references detected (all `\ref`/`\label` pairs matched)
- No hardcoded Figure/Table/Section numbers
- Bootstrap resamples: consistently 1,000 across all files
- Appendix: Figure~\ref{fig:auc_decay} (not hardcoded Figure 2) ✅

### E. Logic Coherence ✅

- Related Work new paragraphs connect to experiments: probing classifiers → neural probe experiment; Frank & Hall → OBD method; dohmatob2025strong → model collapse motivation; feng2025beyond → graduated filtering; bao2024fast → binary detection landscape
- Discussion subsections all have corresponding experimental evidence
- Conclusion contributions match presented results (graduated filtering acknowledged as pending)
- Limitations cover 8 dimensions (model scale, prompt/retrain chain, language/domain, decoding, θ-sensitivity, boundary marginality, operational vs theoretical, feature representation)
