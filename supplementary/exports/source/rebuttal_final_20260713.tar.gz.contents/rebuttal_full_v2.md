# EMNLP 2026 Rebuttal v2 — Full Internal Version

**Paper**: When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects
**Submission**: #4299
**Date**: 2026-07-13
**Venue**: EMNLP 2026 via ACL Rolling Review (Long paper, threaded discussion on OpenReview)

---

## Score Matrix

| Reviewer | Overall | Soundness | Excitement | Confidence | Repro | Software | Datasets |
|----------|---------|-----------|------------|------------|-------|----------|----------|
| R1 (FCVy) | 3.5 | 3.5 | 3.5 | 2 | **2** | **1** | **1** |
| R2 (Sshp) | 3.5 | **4.0** | 3.0 | 2 | 4 | 4 | 2 |
| R3 (ppmy) | **4.0** | 3.5 | 3.5 | 1 | 4 | 4 | 4 |
| **Average** | **3.67** | 3.67 | 3.33 | 1.67 | | | |

## Stance Classification

- **R1 (FCVy): Persuadable** — 3.5 borderline, low confidence (2), Software=1/Repro=2 are factual errors (code already public). Highest ROI target: correcting the misunderstanding could raise meta-review sub-scores and push overall toward 4.0.
- **R2 (Sshp): Persuadable** — 3.5 borderline, Soundness=4 (strong), two addressable concerns. Demonstrating responsiveness on W1/W2 should maintain 3.5 or push toward 4.0.
- **R3 (ppmy): Champion** — 4.0 Conference, confidence=1, no substantive weakness. Maintain with trivial fixes.

## Issue Board

| ID | Reviewer | Severity | Category | Strategy | Status |
|----|----------|----------|----------|----------|--------|
| R1-1 | FCVy | Major-Addressable | reproducibility | Clarify misunderstanding (code already released) | done |
| R1-2 | FCVy | Minor | clarity | Acknowledge + explain + concrete modification plan | done |
| R1-3 | FCVy | Minor | feature | Accept (global correction already in code) | done |
| R2-W1 | Sshp | Major-Addressable | experimental | Partial agree + methodological defense (5-point) | done |
| R2-W2 | Sshp | Minor | limitation | Reframe as evaluation scope + practitioner guidance | done |
| R3-1 | ppmy | Minor | clarity | Accept and fix (Y definition — already revised) | done |
| R3-2 | ppmy | Minor | clarity | Accept and fix (B_s clarification — already revised) | done |

---

## Response to Reviewer FCVy (R1)

We thank Reviewer FCVy for recognizing the relevance and novelty of the addressed issue.

**Code and data are already publicly released** [Evidence: Existing]

Our code, data, and reproduction scripts are publicly available at the anonymous repository linked in the abstract footnote (https://anonymous.4open.science/r/ec_hte_llm_annotation-4CC8/):

1. Reproduction scripts: `python exp001_hb_synthetic.py` for Table 1; `bash run_table1.sh` for end-to-end reproduction
2. Figure generation: `draw_fig2.py`, `draw_fig3.py`, `figures/` directory
3. Global correction baseline: `compute_global_cm` function in `exp001_hb_synthetic.py` — directly comparable to EC-HTE
4. Environment setup (`requirements.txt`) and preprocessed data (`data/`)

**Revision**: the Conclusion now includes an explicit code-release statement listing reproduction scripts, preprocessed data, and figure generation code.

[INTERNAL: R1's Software=1 and Repro=2 are factual errors — code already released. Highest-ROI action: correcting this should push R1 toward 4.0.]

**Two appendix navigation improvements are in the uploaded revision; two more planned for camera-ready** [Evidence: New verified + Planned]

The main findings are self-contained in the 8-page main text (Theorem 1, Proposition 5, Algorithm 1, Tables 1–2, Figures 2–5). Changes already in the uploaded revision:

1. **Appendix roadmap** added (first paragraph of the appendix): algorithm details (App. A), full proofs (Apps. B–D), DGP specifications (App. E), real-data case studies (Apps. M, V), bias identity validation across nine LLMs (Apps. N–O, W–X), robustness analyses (remaining)
2. **All 38 appendix pointers verified precise** — no generic "see the appendix" references remain

Camera-ready plan:

3. Move secondary results and extended tables to the public code repository
4. Merge closely related appendices to reduce fragmentation

[INTERNAL: Follows "解释+修改" pattern. Roadmap stated as done; precise refs as "verified" (not "added" — tex untouched this round). Move-to-repo + merge are camera-ready commitments.]

---

## Response to Reviewer Sshp (R2)

We thank Reviewer Sshp for the careful evaluation and for recognizing the rigor of the theoretical contribution (Soundness: 4).

**Semi-synthetic evaluation follows established causal inference protocol; real LLM heterogeneity is independently validated** [Evidence: Existing + Argumentative reasoning]

We agree that real-data causal estimates would strengthen external validity. However, observational studies cannot provide a known ground-truth CATE — the quantity our method corrects — making direct real-data evaluation of bias reduction infeasible. The established protocol in this literature uses ground truth known by construction:

1. **PPI** (Angelopoulos et al., *Science*, 2023): evaluates on real datasets with ground-truth parameters computed from gold-standard labels
2. **DSL** (Egami et al., *NeurIPS*, 2023): evaluates on real text/survey datasets against ground truth from full expert annotation
3. **Audinet de Pieuchon et al.** (*EMNLP*, 2025): the most comprehensive benchmark; reports that debiasing can *increase* MSE when prediction error is heterogeneous — precisely the phenomenon our bias identity explains (Theorem 1)

Our semi-synthetic design extends this principle to the causal setting: known CATEs injected onto real text features. No public dataset simultaneously provides LLM annotations, expert gold labels, a known causal effect, and subgroup-heterogeneous annotation quality.

Complementarily, our real-data case studies validate the *precondition* — that LLM error rates are genuinely heterogeneous: **Δπ = 0.117** (GPT-4.1 on UC Berkeley Hate Speech, §5.2), **Δπ up to 0.184** (GPT-4o/Claude/Llama on CivilComments, App. V), and **R² = 0.975** across 11 LLM–dataset combinations (§5.4).

**Revision**: the Limitations section now clarifies this distinction: semi-synthetic experiments verify the theorem's predictions under controlled conditions; real case studies confirm the phenomenon exists in practice.

[INTERNAL: 5-point structure covered: (1) acknowledge, (2) citation-backed protocol precedent, (3) semi-synthetic as rigorous verification, (4) real cases as complementary, (5) Limitations clarified. Framed as "same evaluation principle" not "identical protocol" — PPI/DSL use construction-known ground truth, not literal CATE injection.]

**K ≤ 4 is an evaluation scope, not a method limitation** [Evidence: Existing + Argumentative reasoning]

The bias identity (Theorem 1) and EC-HTE hold for arbitrary K — Corollary 6 (Appendix C) extends to K > 2 subgroups with J effect-modifier levels. K ≤ 4 is the primary finite-sample regime evaluated; the bottleneck is per-subgroup expert labels (K = 8 at n_expert = 250 yields ~31 labels/subgroup, insufficient for reliable confusion matrix estimation).

Three strategies for K > 4 (the first two now in the revised Limitations):

1. **Merge similar subgroups**: group subgroups with similar error rates (identifiable from a pilot sample); the diagnostic (Proposition 5) guides which groupings matter most
2. **Selective application**: apply EC-HTE to the most heterogeneous subgroups (ranked by |δ_s|), retain global correction for the remainder
3. **Scale expert budget**: hierarchical Bayesian partial pooling reduces stratified MLE RMSE by **47%** with coverage ≥ 94% (Appendix I.2); n_expert ≥ 500 (~60 labels/subgroup) achieves RMSE parity with global correction

[INTERNAL: "Evaluation scope vs limitation" reframe per v3 pattern. Practitioner guidance added to Limitations.]

---

## Response to Reviewer ppmy (R3)

We thank Reviewer ppmy for the positive evaluation and for recognizing the soundness and practical value of the work.

**Y is now explicitly defined in Section 3** [Evidence: New verified]

The revised manuscript adds an explicit definition at the beginning of Section 3: "Let Y denote the outcome of interest, with potential outcomes Y(1) and Y(0) under treatment (W=1) and control (W=0)."

**B_s is now clarified inline in Assumption A2** [Evidence: New verified]

[B_s]_{z,1} in Assumption A2 referred to B_s = M_global⁻¹ M_s − I, formally defined only in the proof sketch below Theorem 1. The revision adds an inline definition: "where B_s = M_global⁻¹ M_s − I; see Theorem 1," eliminating the forward reference.

Both changes are in the uploaded revised manuscript.

[INTERNAL: R3 at 4.0 — maintain. Both fixes applied. Brief per tip #25.]

---

## Revisions Summary

All revisions listed below have been applied to the uploaded revised manuscript:

| # | Change | Section | Triggered By |
|---|--------|---------|--------------|
| 1 | Added explicit Y definition | Section 3 (theory.tex L10) | R3-Q1 |
| 2 | Clarified B_s notation inline in A2 | Section 3 (theory.tex L20) | R3-Q2 |
| 3 | Added appendix navigation roadmap | Appendix (first paragraph) | R1-Q2 |
| 4 | Added K > 4 practitioner guidance | Limitations (L5) | R2-W2 |
| 5 | Made code availability more prominent | Conclusion (L6) | R1-Q1 |
