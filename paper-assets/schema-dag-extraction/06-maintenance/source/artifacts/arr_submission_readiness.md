# ARR Submission Readiness Report

**Generated**: 2026-05-22 | **DDL**: 2026-05-25 | **Venue**: EMNLP 2026 via ARR

---

## 1. Paper PDF

| Check | Status | Detail |
|-------|--------|--------|
| Body ≤ 8 pages | **READY** | Limitations on p.8, References start p.9 |
| Limitations section | **READY** | 3 points, 1 paragraph (~25 lines). No excessive content. |
| Anonymous submission | **READY** | `\author{Anonymous}`, "Anonymous ACL submission" on p.1. No author names, affiliations, acknowledgments, or identifying URLs in body. |
| ACL format | **READY** | `\documentclass[11pt]{article}` + `\usepackage[review]{acl}`, acl_natbib, two-column |
| Page size | **READY** | A4 (595.276 × 841.89 pts) |
| Font size | **READY** | 11pt base (ACL template default) |
| Fonts embedded | **READY** | All fonts embedded (Type 1, subset) |
| PDF version | **READY** | 1.7 |
| Compilation | **READY** | 0 errors, 0 undefined refs, 0 citation warnings, 27 pages total |
| checklist.tex | **READY** | Correctly commented out (`% \input{checklist}`); EMNLP 2026 checklist goes in OpenReview form |

## 2. Supplementary Material

| Check | Status | Detail |
|-------|--------|--------|
| Appendix in PDF | **READY** | 25 appendix sections (A–Y) embedded in main.pdf after `\appendix`. No separate appendix file needed. |
| Anonymous GitHub package | **READY** | `artifacts/anonymous_github/` prepared: `src/` (43 files), `scripts/` (21 files), `configs/` (3 files), `data/README.md`, `requirements.txt`, `LICENSE`, `README.md` |
| API key cleaned | **READY** | `run_fewrel_gpt4o_mini.py:42`: `os.environ.get("OPENAI_API_KEY", "YOUR_API_KEY_HERE")` |
| Path leak check | **READY** | No `/root/`, `/home/` paths found in anonymous_github. `args.api_key` usage at line 378/400 is safe (reads from argparse default). |
| Upload to anonymous.4open.science | **USER ACTION REQUIRED** | Package prepared but not uploaded. User must create anonymous repo and obtain URL. |

## 3. ARR Responsible NLP Checklist

All items reviewed (see `artifacts/arr_checklist_final.md` for full detail). Summary:

| Section | Status | Notes |
|---------|--------|-------|
| A. Every Submission (A1–A4) | **READY** | Limitations ✓, Risks ✓, Claims ✓, AI use ✓ |
| B. Scientific Artifacts (B1–B6) | **READY** | All 9 artifacts cited, licenses documented |
| C. Computational Experiments (C1–C4) | **READY** | GPU hours (~72h inference), hardware (RTX PRO 6000 96GB), vLLM v0.20.2, seed=42 |
| D. Human Annotators (D1–D5) | **READY** | N/A — no human annotation |
| E. AI-Assisted Research (E1) | **READY** | Claude for writing/code; research design by authors |

**Note**: Gemini API cost not quantified in C1. Consider adding "Gemini API cost not tracked" in OpenReview form if asked.

## 4. OpenReview Form Pre-Fill

| Field | Value | Status |
|-------|-------|--------|
| **Title** | How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? | **READY** (matches PDF) |
| **Abstract** | (from `abstract.tex`, 155 words / 1210 chars) | **READY** — within typical ARR limits (~250 word limit) |
| **Keywords** | information extraction, schema complexity, type confusability, zero-shot prompting, LLM evaluation | **USER ACTION REQUIRED** — suggested; user confirms |
| **TL;DR** | Type count and inter-type confusability independently predict performance degradation in training-free LLM IE; BCS explains ~27% of RE accuracy variance on FewRel. | **USER ACTION REQUIRED** — suggested; user confirms |
| **Submission type** | Long paper | **READY** |
| **Track** | (EMNLP 2026 ARR uses unified review; no track selection) | **READY** — N/A |
| **Conflicts of interest** | (User fills based on co-author affiliations) | **USER ACTION REQUIRED** |
| **Supplementary material** | Upload `anonymous_github.zip` OR paste anonymous.4open.science URL | **USER ACTION REQUIRED** |
| **Responsible NLP Checklist** | Copy from `artifacts/arr_checklist_final.md` | **USER ACTION REQUIRED** |

## 5. Anonymous GitHub

| Check | Status | Detail |
|-------|--------|--------|
| Content completeness | **READY** | src/ (inference, analysis, SDGD, evaluation), scripts/ (figures, experiments), configs/ (type definitions), data/README.md |
| API key sanitized | **READY** | Verified |
| configs/ present | **READY** | 3 JSON files (fewrel_relation_types, few_nerd_types, maven_event_types) |
| README accuracy | **READY** | Filename references corrected (few_nerd_types.json) |
| Upload to anonymous.4open.science | **USER ACTION REQUIRED** | User creates anonymous repo, obtains URL |

---

## Summary

| Category | READY | USER ACTION REQUIRED |
|----------|-------|---------------------|
| Paper PDF | 10/10 | 0 |
| Supplementary | 4/5 | 1 (upload anonymous GitHub) |
| Checklist | 5/5 | 0 |
| OpenReview Form | 3/8 | 5 (keywords, TL;DR, COI, supplementary upload, checklist form) |
| Anonymous GitHub | 4/5 | 1 (upload) |
| **Total** | **26/33** | **7 (all user-side)** |

---

## User Submission Steps

### Before submission (can do now)

1. **Upload anonymous GitHub**:
   - Go to https://anonymous.4open.science/
   - Create new anonymous repo
   - Upload contents of `artifacts/anonymous_github/`
   - Save the generated anonymous URL

2. **Prepare OpenReview form answers**:
   - Review suggested Keywords and TL;DR above
   - Prepare Conflicts of Interest list (co-author affiliations, recent collaborators)
   - Review checklist answers in `artifacts/arr_checklist_final.md`

### Submission day (DDL 2026-05-25)

3. **Go to OpenReview ARR submission page**
4. **Upload PDF**: `docs/paper/main.pdf`
5. **Fill form fields**:
   - Title: copy from above
   - Abstract: copy from `abstract.tex` (strip LaTeX markup)
   - Keywords, TL;DR: as suggested above (or user's preference)
   - Submission type: Long paper
   - Supplementary: paste anonymous GitHub URL (or upload zip)
6. **Fill Responsible NLP Checklist**: transcribe from `artifacts/arr_checklist_final.md`
7. **Declare Conflicts of Interest**
8. **Submit**

### Post-submission

9. **Author response template**: `artifacts/author_response_template.md` (5 Q&A blocks pre-written for anticipated reviewer questions)
