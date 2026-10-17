# ARR Submission Preparation — EMNLP 2026

Updated 2026-05-22 (v34: cross-model error taxonomy added, semipartial R² corrected, Limitations W1 updated).

## 1. Supplementary Materials Status

### Appendix (in-paper)
- Pages 10–26+ of main.pdf contain all appendices (A–Y)
- Covers: SDGD details, factorial analysis, prompt templates, cross-model validation, power analysis, error analysis, contamination analysis, cross-model error taxonomy (Table `cross_model_error_taxonomy`), etc.

### Anonymous Code Repository
- `artifacts/anonymous_github/` contains a prepared anonymous repo:
  - `src/` — 42 Python scripts (experiment runners, analysis, evaluation)
  - `scripts/` — 24 auxiliary scripts (figure generation, embedding computation, Monte Carlo simulation)
  - `data/README.md` — data documentation
  - `requirements.txt`, `LICENSE`, `README.md`
- **Action needed (user):** Upload to Anonymous GitHub (https://anonymous.4open.science/) and paste the link in OpenReview supplementary field
- **Check before upload:** Ensure no hardcoded server paths (e.g. `/root/`) remain in scripts

### Data
- All four datasets (Few-NERD, FewRel, DocRED, MAVEN) are publicly available with citations
- Sampled evaluation sets (1,000 instances each) should be included in the anonymous repo `data/` directory or described with exact reproduction steps
- SCS matrices and batch configurations should be included for full reproducibility

### Supplementary ZIP
- ARR allows a single supplementary PDF or ZIP
- **Recommendation:** Not strictly needed if anonymous GitHub link is provided. If preferred, ZIP the anonymous_github directory.

---

## 2. ARR Responsible NLP Checklist (OpenReview Form)

Below are suggested answers for each question on the OpenReview submission form. The user should review and adjust before submitting.

### A. For Every Submission

**A1. Did you describe the limitations of your work?**
- **Answer:** Yes
- **Section:** Limitations section (after §6), 6 items covering model coverage (W1: TOST/SDGD remain single-model; error taxonomy now cross-model validated), effect size, task scope, causal mechanism, domain scope, and multiple comparisons

**A2. Did you discuss any potential risks of your work?**
- **Answer:** Yes
- **Justification:** Limitations section. SCS/BCS are diagnostic proxies, not deployment criteria. Risk of misuse as automatic schema rejection is noted.

**A3. Do the abstract and introduction summarize the paper's main claims?**
- **Answer:** Yes
- **Section:** Abstract (3 numbered findings), Introduction §1 (4 findings + 3 contributions)

**A4. Did you use AI assistants?**
- **Answer:** Yes
- **Justification:** Claude (Anthropic) for writing assistance and experimental code development. Research design, execution, and interpretation are the authors' own work.

### B. Scientific Artifacts

**B1. Did you cite the creators of artifacts you used?**
- **Answer:** Yes
- **Section:** §3.1 (datasets), §3.5 (models). All datasets (Few-NERD, FewRel, DocRED, MAVEN), models (Qwen3, LLaMA, Gemini), and tools (vLLM, MiniLM) cited.

**B2. Did you discuss the license or terms?**
- **Answer:** Yes
- **Justification:** Few-NERD: CC-BY-SA 4.0; FewRel/DocRED/MAVEN: publicly released for research. Open-weight models used under respective licenses; Gemini via API terms of service.

**B3. Did you discuss if your use is consistent with intended use?**
- **Answer:** Yes
- **Justification:** All datasets used for their intended IE evaluation purpose.

**B4. Did you discuss PII or offensive content?**
- **Answer:** N/A
- **Justification:** Established benchmarks, no new data collection or annotation.

**B5. Did you provide documentation of artifacts?**
- **Answer:** Yes
- **Section:** Table 1 (dataset statistics), §3.1 (provenance, sampling)

**B6. Did you report relevant statistics?**
- **Answer:** Yes
- **Section:** §3.1, Table 1 (sizes, type counts, sampling), §3.3 (count levels, batch sizes)

### C. Computational Experiments

**C1. Did you report parameters, compute budget, and infrastructure?**
- **Answer:** Yes
- **Section:** §3.5. Models: Qwen3-32B (FP8), LLaMA-70B (FP8), LLaMA-8B, Gemini Flash (API). Hardware: NVIDIA RTX PRO 6000 (96GB). Total: ~72 GPU-hours inference (open-weight models), no training. Gemini Flash runs via API (cost not GPU-hours). Cross-model error taxonomy analysis reuses existing prediction outputs.

**C2. Did you discuss experimental setup and hyperparameters?**
- **Answer:** Yes
- **Section:** §3.3 (count curves, BCS-controlled design), §3.5 (greedy decoding, temp=0, seed=42). No hyperparameter search (zero-shot evaluation study).

**C3. Did you report descriptive statistics?**
- **Answer:** Yes
- **Justification:** All key metrics include 95% bootstrap CIs (B=10,000 for pairwise, B=1,000 for batch-level). Correlations with p-values throughout §4. Permutation tests for slope comparisons. Semipartial R² (ΔR²) correctly computed as R²_full − R²_reduced (verified v34).

**C4. Did you report implementation details?**
- **Answer:** Yes
- **Section:** §3.5 (vLLM v0.20.2, model versions). Code release upon acceptance.

### D. Human Annotators or Crowdworkers

**D1–D5:** All N/A. No human annotation or crowdsourcing conducted.

### E. AI-Assisted Research

**E1. Did you report the use of AI assistants?**
- **Answer:** Yes
- **Section:** A4 above. AI used for code development and document formatting; research design/execution/interpretation by authors.

---

## 3. PDF Sanity Check Results

| Check | Status | Details |
|-------|--------|---------|
| Path leaks (/home/, /root/, etc.) | ✅ PASS | 0 found |
| TODO / FIXME / placeholder | ✅ PASS | 0 in source; 1 benign "Placeholders" in prompt template description |
| Undefined references | ✅ PASS | 0 |
| Undefined citations | ✅ PASS | 0 |
| Line numbers (review mode) | ✅ PASS | `\usepackage[review]{acl}`, 587 numbered lines |
| Abstract word count | ✅ PASS | ~133 words (limit: 250) |
| Body page count | ✅ PASS | ≤ 8 pages (Discussion ends p.8, Limitations starts p.8) |
| Total pages | ℹ️ INFO | ~27 pages (8 body + Limitations + References + Appendix; exact count may shift after cross-model error taxonomy table addition — recompile to verify) |
| Anonymous submission | ✅ PASS | No author names in PDF; "Code and data will be released upon acceptance" |
| Compute budget disclosed | ✅ PASS | ~72 GPU-hours in checklist C1 |

### Items for User Action
1. **Anonymous GitHub:** Upload `artifacts/anonymous_github/` to https://anonymous.4open.science/, add link to OpenReview supplementary field
2. **Check scripts for paths:** `grep -r '/root/' artifacts/anonymous_github/` before upload
3. **Fill OpenReview form:** Use Section 2 above as reference for the Responsible NLP Checklist
4. **Verify checklist.tex vs form:** The paper-embedded checklist (checklist.tex) should be consistent with what you enter in the OpenReview form
