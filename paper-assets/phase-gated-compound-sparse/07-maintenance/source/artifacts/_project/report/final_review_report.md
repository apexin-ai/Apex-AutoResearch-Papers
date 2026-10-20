# Final Visual Review & Reference Audit Report

**Date:** 2026-05-14
**Paper:** Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models
**Target:** EMNLP ARR submission
**PDF:** 11 pages (main body + limitations + references + appendix)

---

## Verdict: SUBMISSION READY

No Critical issues found. All warnings are low-risk and addressable at the author's discretion.

---

## 1. Page Count

| Section | Pages |
|---------|-------|
| Abstract -- Conclusion | ~4.3 pages (pp.1--5 top) |
| Limitations | p.5 (partial) |
| References | pp.5--6 |
| Appendix A--I | pp.6--11 |

Main body (Abstract to Conclusion) = ~4.3 pages. **Well within the 8-page limit.**

## 2. Visual Review (all 11 pages inspected)

| Check | Status |
|-------|--------|
| Figures clear & readable | PASS -- Figures 1-4 all sharp, legends visible, no truncation |
| Tables aligned, no overflow | PASS -- Tables 1-7 properly formatted within column/page width |
| Formulas rendered correctly | PASS -- all equations and inline math render cleanly |
| Font consistency | PASS -- uniform throughout |
| ACL format margins | PASS -- standard two-column ACL layout |
| Line numbers | PASS -- continuous 1--825 across all pages |
| Anonymity | PASS -- "Anonymous ACL submission", no author names or affiliations anywhere |

## 3. Reference Audit

**Summary:** 31 bib entries, 25 unique cited keys, 0 missing bib entries (all citations resolve).

### Warning: 6 orphan bib entries (in .bib but never cited)

| Key | Status |
|-----|--------|
| `compression-ordering-2025` | Not cited |
| `doing-more-with-less-2026` | Not cited |
| `mustafar-neurips2025` | Not cited |
| `obcache-2025` | Not cited |
| `pagedeviction-eacl2026` | Not cited |
| `raas-acl2025` | Not cited |

**Recommendation:** Remove these 6 entries from `references.bib` to keep the bibliography clean. They do not affect the compiled PDF (LaTeX only renders cited entries with `\bibliography`), so this is cosmetic.

### Online verification

- **23/31 verified** via OpenAlex (title match confirmed)
- **3 not found online:** `deepseek-r1-2025` (Nature paper, DOI valid), `defensivekv-iclr2026` (recent ICLR), `phase-transition-compression-2026` (recent npj AI) -- all have valid DOIs or arXiv IDs; not found due to OpenAlex indexing lag for recent publications. No action needed.
- **4 author-format mismatches:** Minor parsing differences (e.g., "von Rad" vs "Rad", corporate author "DeepSeek-AI" vs individual). Not actual errors.
- **`h2o-neurips2023`:** Title uses `\textsubscript` LaTeX command which the parser couldn't extract, but renders correctly as "H2O: Heavy-Hitter Oracle..." in the compiled PDF. No action needed.

### Format consistency

- All entries use consistent field formatting (title case with LaTeX braces for acronyms)
- Years range 1993--2026 -- all reasonable
- No duplicate keys
- arXiv IDs follow valid format (YYMM.NNNNN)

## 4. Content Consistency

### Abstract vs. Results numbers

| Claim (Abstract) | Source (Results) | Match |
|------------------|------------------|-------|
| Delta 0.39 at s=0.15 to 14.59 at s=0.30 | Table 1: Importance row | MATCH |
| Cohen's d_z 0.44 to 0.80 | Table 3: DS d_z column | MATCH |
| p < 0.005 at all four levels | Section 4.5: p_Bonf < 0.005 | MATCH |
| 7/8 random conditions non-significant | Section 4.1 + Table 1 | MATCH |
| Crossover II = 0.032 vs 0.818 (high phase) | Table 2: s=0.25 Importance/Random high | MATCH |
| Crossover II = 7.196 vs 1.363 (low phase) | Table 2: s=0.25 Importance/Random low | MATCH |
| Qwen d_z >= 0.55, rho = 1.0, p = 0.043 | Section 4.4 | MATCH |

All abstract numbers are backed by reported results.

### Figure/Table numbering

- Figures: 1, 2, 3, 4 -- sequential, all referenced in text
- Tables: 1, 2, 3, 4, 5, 6, 7 -- sequential, all referenced in text

### Automated checker flags (adjudicated)

| Flag | Severity | Adjudication |
|------|----------|-------------|
| "0.50 in conclusion unsupported" | Flagged Critical | **FALSE POSITIVE** -- the 0.50 appears in `$s > 0.50$` in the Limitations section as a speculative future direction ("may exhibit qualitatively different interaction dynamics"), not a claimed result |
| 16 precision mismatches (analysis vs results) | Flagged Warning | **FALSE POSITIVE** -- checker compared numbers across unrelated metrics (e.g., Gini coefficient deltas -0.040 matched against II values 0.04). Same-metric values are consistent |

## 5. Issue Summary

| Severity | Count | Details |
|----------|-------|---------|
| Critical | 0 | -- |
| Warning | 1 | 6 orphan bib entries (cosmetic, does not affect PDF output) |
| Minor | 0 | -- |
