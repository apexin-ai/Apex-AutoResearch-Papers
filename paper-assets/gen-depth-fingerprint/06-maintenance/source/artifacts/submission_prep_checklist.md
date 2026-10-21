# EMNLP 2026 ARR Submission Preparation Checklist

**Paper:** Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains  
**Target:** EMNLP 2026 via ACL Rolling Review (May 2026 cycle)  
**Deadline:** 2026-05-25  
**Date of check:** 2026-05-17

---

## 1. Compilation Check

| Item | Status | Details |
|------|--------|---------|
| Full compilation (pdflatex x3 + bibtex) | ✅ | Clean build, 15 pages, 357 KB |
| Errors | ✅ | 0 errors |
| Undefined references | ✅ | 0 after full 3-pass build |
| Undefined citations | ✅ | 0 — all 56 bib entries resolve |
| `\input{}` files exist | ✅ | All 24 .tex files present |
| `\includegraphics{}` files exist | ✅ | `fig1_differential_response.pdf` and `fig3_baseline_comparison.png` found via `\graphicspath{{../chart/}}` |
| Float specifier warnings | ⚠️ | 2x `[h]` changed to `[ht]` — cosmetic, no action needed |
| Overfull/Underfull hbox | ⚠️ | ~40 Underfull hbox, 1 Overfull (23.8pt in appendix_error_analysis.tex line 20-34). Consider manual line breaks for the overfull. |
| TODO/FIXME markers | ✅ | None found |

---

## 2. Anonymization Check (Review Version)

| Item | Status | Details |
|------|--------|---------|
| `\usepackage[review]{acl}` | ✅ | Correctly set — enables anonymization + line numbers + page numbers |
| Author field | ✅ | `\author{Anonymous}` |
| Line numbers enabled | ✅ | `\usepackage{lineno}` + `\linenumbers` |
| GitHub/GitLab links in content | ✅ | None in .tex body (only in `build.sh` comment and `acl.sty` header — not included in PDF) |
| Personal names/institutions | ✅ | None found in any .tex file |
| Email addresses | ✅ | None |
| Acknowledgements section | ✅ | Not present (correct for review version) |
| Figure watermarks/signatures | ✅ | Figures are generated plots, no identifying marks |
| Self-citations de-anonymized | ✅ | No self-citations detected (paper is novel work) |

---

## 3. Page Limit Compliance

| Item | Status | Details |
|------|--------|---------|
| Main body (before Limitations) | ✅ | ~6.5 pages (well within 8-page limit) |
| Limitations section | ✅ | Present (page 7), substantial (30 lines), does NOT count toward limit |
| Ethics Statement | ✅ | Present (8 lines), does NOT count toward limit |
| References | ✅ | ~1 page, does NOT count toward limit |
| Appendix | ✅ | ~7 pages (11 appendix sections), does NOT count toward limit |
| Total PDF | ✅ | 15 pages |

---

## 4. Responsible NLP Research Checklist

Based on the [ARR Responsible NLP Research Checklist](https://aclrollingreview.org/responsibleNLPresearch/):

### Section A: For Every Submission

| Q | Question | Answer | Justification |
|---|----------|--------|---------------|
| A1 | Did you describe the limitations of your work? | **Yes** | Comprehensive Limitations section covers: base-model-only scope, scale limits (8B max), prompt-type dependence, instruct model degradation, 3-class ceiling, language (English only), domain constraints |
| A2 | Did you discuss any potential risks of your work? | **Yes** | Ethics Statement discusses: no personal data, not authorship attribution, risk of suppressing legitimate AI text, encourages provenance transparency over removal |
| A3 | Do the abstract and introduction summarize the paper's main claims? | **Yes** | Abstract covers problem/method/results; Introduction lists 2 explicit contributions |

### Section B: Scientific Artifacts

| Q | Question | Answer | Justification |
|---|----------|--------|---------------|
| B1 | Did you cite the creators of artifacts you used? | **Yes** | All 8 generators cited (Pythia, OLMo, Qwen, Llama, Mistral), XGBoost cited, all baselines cited |
| B2 | Did you discuss the license or terms for use? | ⚠️ **Partial** | Model citations present but no explicit license discussion for models or Wikipedia data. **Recommend:** Add 1-2 sentences in Method or Ethics noting model licenses (Apache 2.0 for OLMo/Qwen/Mistral, Llama Community License) and Wikipedia CC-BY-SA |
| B3 | Was use consistent with intended use? | **Yes** | All models used for text generation (their primary purpose); Wikipedia used as seed text |
| B4 | Did you check for PII or offensive content? | **Yes** | Ethics states "no personal or sensitive data"; Wikipedia seeds are public |
| B5 | Did you provide documentation of artifacts? | **Yes** | Method section details generation parameters, feature extraction, dataset construction |
| B6 | Did you report relevant statistics? | **Yes** | N=37,058 texts, per-generator counts in Appendix A (Dataset Statistics table), train/test via LOGO protocol |

### Section C: Computational Experiments

| Q | Question | Answer | Justification |
|---|----------|--------|---------------|
| C1 | Did you report parameters, compute budget, infrastructure? | ⚠️ **Partial** | Parameter counts reported (0.6B-8B generators, 410M reference). **Missing:** total GPU hours and hardware description (GPU type, memory). **Recommend:** Add compute details to Method or Appendix |
| C2 | Did you discuss hyperparameter search? | **Yes** | XGBoost settings explicitly stated (n_estimators=200, max_depth=6, lr=0.1); sampling ablation in Appendix |
| C3 | Did you report descriptive statistics? | **Yes** | Bootstrap 95% CIs (n=1000), per-generator breakdowns, McNemar tests, Bonferroni correction |
| C4 | Did you report packages/implementations used? | ⚠️ **Partial** | XGBoost cited. **Missing:** explicit version numbers for key packages (transformers, scikit-learn, Python version). **Recommend:** Add to supplementary or appendix |

### Section D: Human Annotators/Participants

| Q | Question | Answer | Justification |
|---|----------|--------|---------------|
| D1-D5 | All human participant questions | **N/A** | No human annotation or participant studies conducted |

### Section E: AI Assistants

| Q | Question | Answer | Justification |
|---|----------|--------|---------------|
| E1 | Did you disclose AI assistant use? | ⚠️ **Needs decision** | If AI assistants were used in writing/coding, this must be disclosed. **Action:** Add disclosure if applicable |

---

## 5. Supplementary Materials Checklist

### Code (Software upload, max 200MB .zip/.tgz)

Files to include (anonymized):

| Path on server | Description | Anonymization needed |
|----------------|-------------|---------------------|
| `/root/gen-depth-fingerprint/generate_chain.py` | Generation chain construction | Remove any hardcoded paths |
| `/root/gen-depth-fingerprint/extract_features.py` | 7-feature extraction | Remove paths |
| `/root/gen-depth-fingerprint/classify_and_eval.py` | XGBoost LOGO evaluation | Remove paths |
| `/root/gen-depth-fingerprint/scripts/plot_fig1.py` | Figure 1 generation | Remove paths |
| `/root/gen-depth-fingerprint/scripts/plot_fig3.py` | Figure 3 generation | Remove paths |
| `/root/gen-depth-fingerprint/scripts/bootstrap_ci.py` | Statistical testing | Remove paths |
| `/root/gen-depth-fingerprint/scripts/lofo_ablation.py` | LOFO analysis | Remove paths |
| `/root/gen-depth-fingerprint/scripts/ordinal_baseline.py` | Ordinal regression baselines | Remove paths |

**Action items:**
- ❌ Create `requirements.txt` with package versions
- ❌ Create `README.md` with reproduction instructions
- ❌ Remove all hardcoded server paths (replace with relative or argparse)
- ❌ Remove any API keys or credentials
- ❌ Package as anonymous zip (no git history)

### Data (Data upload, max 200MB .zip/.tgz)

| Item | Description | Action |
|------|-------------|--------|
| `features_all_models.csv` | Extracted features for all 37K texts | Include (anonymized) |
| `wiki_seed_1000.jsonl` | Wikipedia seed passages | Include |
| Dataset statistics | Already documented in Appendix A | N/A |

**Action items:**
- ❌ Verify data files fit within 200MB limit
- ❌ Remove any file metadata that could identify authors
- ❌ Add data README with column descriptions

### Appendix (already in paper)

11 appendix sections covering:
- A: Dataset Statistics (table)
- B: Length Confound Analysis
- C: Prompt Type Generalization
- D: Finer-Grained Depth (5-class)
- E: End-to-End QLoRA
- F: Leave-One-Feature-Out
- G: Confusion Matrix
- H: Classifier Sensitivity + Sampling Sensitivity
- I: Robustness to Text Perturbation
- J: Cross-Domain Generalization
- K: Error Analysis
- L: Downstream Utility

---

## 6. OpenReview Submission Form Fields

Based on [ARR Submission Form](https://aclrollingreview.org/submissionform):

| Field | Suggested Content |
|-------|-------------------|
| **Title** | Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains |
| **Authors** | [Add all authors with OpenReview profiles] |
| **TL;DR** | We show that recursive LLM generation produces structured distributional drift enabling ordinal depth classification (gen-0/gen-1/gen-2+) via a lightweight 7-feature ensemble. |
| **Abstract** | Copy from paper (already ≤250 words) |
| **PDF** | Upload compiled `main.pdf` |
| **Paper Type** | Long paper |
| **Area** | NLP Applications / Computational Social Science / Machine Learning for NLP (check ARR track list) |
| **Software** | Anonymous code zip |
| **Data** | Anonymous data zip |
| **Preprint** | Decision needed — allow anonymous preprint on OpenReview? |
| **Existing Preprints** | List any arXiv uploads (if applicable) |
| **Preferred Venue** | EMNLP 2026 |
| **Consent to Share Data** | Yes (recommended) |
| **Consent to Review** | Yes (all authors must agree to review if eligible) |
| **Responsible NLP Checklist** | Fill per Section 4 above |

**Pre-submission action items:**
- ❌ All authors must have updated OpenReview profiles (affiliation, semantic scholar, DBLP, ACL Anthology links)
- ❌ All authors must register as reviewers by May 27, 2026
- ❌ Decide on preprint policy

---

## 7. Critical Action Items Summary

### Must Fix (❌)

| # | Item | Priority | Effort |
|---|------|----------|--------|
| 1 | Package anonymized code supplement | High | 2-3 hours |
| 2 | Package anonymized data supplement | High | 1 hour |
| 3 | Add compute budget info (GPU type, hours) to paper | High | 15 min |
| 4 | All authors update OpenReview profiles | High | 30 min each |
| 5 | Fill Responsible NLP Research Checklist in form | High | 30 min |
| 6 | Register all authors as reviewers (by May 27) | High | 5 min each |

### Should Fix (⚠️)

| # | Item | Priority | Effort |
|---|------|----------|--------|
| 7 | Add license info for models/data (B2) | Medium | 15 min |
| 8 | Add package version numbers (C4) | Medium | 15 min |
| 9 | Fix 1 overfull hbox in appendix_error_analysis.tex | Low | 5 min |
| 10 | Decide on AI assistant disclosure (E1) | Medium | 10 min |
| 11 | Decide on preprint policy | Medium | 5 min |

### Already Satisfied (✅)

- Compilation clean (0 errors, 0 undefined refs)
- Anonymization complete
- Page limits met (~6.5 pages body)
- Limitations section comprehensive
- Ethics statement present
- All figures and tables compile
- Statistical reporting rigorous (CIs, significance tests, Bonferroni)
- No TODOs/FIXMEs remaining

---

## Sources

- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [ARR Responsible NLP Research Checklist](https://aclrollingreview.org/responsibleNLPresearch/)
- [ARR Submission Form Fields](https://aclrollingreview.org/submissionform)
- [ARR Authors Guidelines](https://aclrollingreview.org/authors)
- [ARR Call for Papers](https://aclrollingreview.org/cfp)
- [ARR Common Submission Problems](https://aclrollingreview.org/authorchecklist)
