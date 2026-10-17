# EMNLP 2026 ARR Submission Checklist

**Paper:** Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts
**Venue:** EMNLP 2026 via ARR (DDL: 2026-05-25)
**Format:** Long paper, ACL style

---

## 1. Format Compliance

| Check | Status | Notes |
|-------|--------|-------|
| Main text ≤ 8 pages | PASS | Sections 1-6 (Abstract through Conclusion) fit on pages 1-8 |
| Limitations section present | PASS | Starts on page 8, extends to page 9 (does not count toward 8pp) |
| Limitations in main body (not appendix) | PASS | `\input{limitations}` before `\appendix` in main.tex |
| Abstract ≤ 200 words | PASS | ~160 words (LaTeX-stripped estimate; wc reports 176 including commands) |
| ACL style file with review mode | PASS | `\usepackage[review]{acl}` (main.tex L2) |
| Line numbers enabled | PASS | Visible in compiled PDF (review mode enables this) |
| 11pt font | PASS | `\documentclass[11pt]{article}` (main.tex L1) |
| References: unlimited pages | PASS | References start page 9, extend to page 11 |
| Appendix: unlimited pages | PASS | Appendix starts page 12, extends to page 29 |

## 2. Anonymity

| Check | Status | Notes |
|-------|--------|-------|
| Author field anonymous | PASS | `\author{Anonymous}` (main.tex L26) |
| No self-identifying URLs | PASS | No `\url{}` or `\href{}` in any .tex file |
| No GitHub links to own repo | PASS | Only GitHub URL is in acl.sty (template file) |
| No acknowledgments section | PASS | Not present |
| Code release phrased conditionally | PASS | "Code and data generation scripts will be released upon acceptance" (limitations.tex L34) |
| No "we previously showed" self-citations | VERIFY | Manual check recommended — grep found no obvious self-refs |

## 3. References

| Check | Status | Notes |
|-------|--------|-------|
| BibTeX file present | PASS | references.bib (525 lines, ~53 entries) |
| All citations resolve | PASS | No "Undefined" warnings in LaTeX log |
| No fake/hallucinated citations | VERIFY | Manual audit recommended (reference-audit skill available) |
| Citation format (author, year) | PASS | Uses acl_natbib.bst |
| Consistent venue names | VERIFY | Spot-check recommended |

## 4. Compilation

| Check | Status | Notes |
|-------|--------|-------|
| Compiles without errors | PASS | pdflatex succeeds, 29 pages output |
| No undefined references | PASS | No "Undefined" in log |
| No missing figures | PASS | No missing-file warnings |
| Float placement warnings only | PASS | 5 `[h]→[ht]` warnings (cosmetic, acceptable) |
| PDF size reasonable | PASS | 762KB |

## 5. Content Quality (Quick Checks)

| Check | Status | Notes |
|-------|--------|-------|
| All AUC values verified | PASS | Data integrity audit completed 2026-05-23 (3 issues resolved) |
| Consistent notation throughout | VERIFY | Spot-check δ_s, π_s, Δπ, Δτ usage |
| Table/Figure numbering sequential | PASS | Table 1, Figure 1-2 in main text |
| Theorem/Proposition numbering | PASS | Theorem 1, Remark 2, Proposition 3 |
| All appendix cross-refs valid | VERIFY | Many appendix refs (A-Z) — compile shows no undefined |

## 6. ARR Responsible NLP Checklist

**Location:** OpenReview submission form (NOT in PDF). Draft answers below for copy-paste.

> Note: checklist.tex exists in paper directory but is commented out in main.tex (L52). This is correct — ARR collects checklist via the OpenReview form, not as a PDF section.

### Draft Answers

**A. Did you describe the limitations of your work?**
Yes. The Limitations section (after Section 6) discusses: (1) expert budget thresholds per subgroup, (2) RMSE variance cost at K=4 with small n, (3) baseline classifier accuracy requirements, (4) plug-in SE vs bootstrap coverage calibration, (5) untestable A1 assumption with sensitivity analysis, (6) diagnostic AUC degradation on real CMs, (7) symmetric/additive assumptions with robustness checks, (8) discrete pre-defined subgroup requirement.

**B. Did you discuss any potential risks of your work?**
Yes. We discuss conditions under which EC-HTE should NOT be applied (low error heterogeneity, insufficient expert budget, K=8 boundary), preventing misuse of stratified correction. The diagnostic criterion (Proposition 3) guards against inappropriate application.

**C. Do the abstract and introduction summarize the paper's main claims?**
Yes. The abstract states three contributions (bias identity, diagnostic, EC-HTE method) with quantitative results. The introduction provides a numbered contribution list (page 2).

**D1. Did you describe the experimental setup?**
Yes. Section 5.1 specifies DGP parameters (N=5000, K∈{2,4}, controlled Δτ and Δπ), MC configuration (100 runs), and method variants. Appendix E provides the complete DGP specification. The HB estimator uses a Gamma(3,1) hyperprior with sensitivity analysis (Appendix I).

**D2. Did you report error bars or statistical significance?**
Yes. All results averaged over 100 MC runs. 95% CI coverage is a primary metric. We do not use "significant" without formal testing. Monte Carlo SEs reported in Appendix Q.

**D3. Did you include computational budget?**
Yes. MCMC: 4 chains × 4000 iterations. Bootstrap: B=100, ~1.5 min/dataset. All experiments run on CPU (no GPU required). Total compute is modest.

**D4. Did you report hyperparameter search range?**
Yes. Hyperprior sensitivity: 0.5× to 2× scaling of Gamma(3,1) concentration (Appendix I). CausalForest: n_estimators=200 (standard). No other hyperparameters tuned.

**E1. Did you use or create scientific artifacts?**
Yes. We use TweetEval sentiment corpus and Civil Comments dataset for semi-synthetic experiments. LLM annotations obtained via OpenAI and open-source model APIs. Code release upon acceptance.

**E2. Did you discuss licenses?**
TweetEval and Civil Comments are publicly available under their original licenses. Code will be released under open-source license.

**E3. Consistent with intended use?**
Yes. Both datasets used as research benchmarks for semi-synthetic CATE experiments.

**F1-F4. Human subjects?**
Not applicable. No human participants. Expert labels in semi-synthetic experiments are simulated from known ground truth.

**G. Misuse discussion?**
Yes. Primary risk is applying EC-HTE when assumptions are violated. The diagnostic criterion and Limitations section guard against inappropriate application.

## 7. Pre-Submission Actions

| Action | Status | Priority |
|--------|--------|----------|
| Final pdflatex + bibtex + pdflatex ×2 | TODO | HIGH — ensures all refs resolve |
| Upload PDF to OpenReview | TODO | HIGH |
| Fill ARR checklist form (use draft above) | TODO | HIGH |
| Enter title, abstract, keywords in form | TODO | HIGH |
| Select track/area (if applicable) | TODO | MEDIUM |
| Verify PDF renders correctly in browser | TODO | MEDIUM |
| Task G bootstrap results → update paper if needed | WAITING | Depends on worker completion |
| Reference audit (optional) | OPTIONAL | Run reference-audit skill |
| Final read-through for typos | TODO | MEDIUM |

---

*Generated: 2026-05-23. Last compilation: main.pdf (762KB, 29 pages, no errors).*
