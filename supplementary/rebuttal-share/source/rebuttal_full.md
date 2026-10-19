# EMNLP 2026 Rebuttal — Full Internal Version

**Paper**: When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects
**Submission**: #4299
**Date**: 2026-07-12

---

## Score Matrix

| Reviewer | Overall | Soundness | Excitement | Confidence | Repro | Software | Datasets |
|----------|---------|-----------|------------|------------|-------|----------|----------|
| R1 (FCVy) | 3.5 | 3.5 | 3.5 | 2 | **2** | **1** | **1** |
| R2 (Sshp) | 3.5 | **4.0** | 3.0 | 2 | 4 | 4 | 2 |
| R3 (ppmy) | **4.0** | 3.5 | 3.5 | 1 | 4 | 4 | 4 |
| **Average** | **3.67** | 3.67 | 3.33 | 1.67 | | | |

## Stance Classification

- **R1 (FCVy): Persuadable** — 3.5 borderline, low confidence, Software/Repro scored 1/2 (factual error — code already released)
- **R2 (Sshp): Persuadable** — 3.5 borderline, Soundness=4, two specific addressable concerns
- **R3 (ppmy): Champion** — 4.0 Conference, no substantive weakness

## Issue Board

| ID | Reviewer | Severity | Category | Strategy | Status |
|----|----------|----------|----------|----------|--------|
| R1-1 | FCVy | Major-Addressable | reproducibility | Clarify misunderstanding | done |
| R1-2 | FCVy | Minor | clarity | Acknowledge + roadmap | done |
| R1-3 | FCVy | Minor | feature | Accept (already in code) | done |
| R2-W1 | Sshp | Major-Addressable | experimental | Partial agree + justify methodology | done |
| R2-W2 | Sshp | Minor | limitation | Accept + add guidance | done |
| R3-1 | ppmy | Minor | clarity | Accept and fix | done |
| R3-2 | ppmy | Minor | clarity | Accept and fix | done |

---

## Response to Reviewer FCVy (R1)

We thank Reviewer FCVy for recognizing the relevance and novelty of the addressed issue.

**Q1 (Software/Reproducibility): "Will you release the code? Can you include the function for the global correction as well?"**

Our code and data are already publicly released. The anonymous repository is linked in the abstract footnote (https://anonymous.4open.science/r/ec_hte_llm_annotation-4CC8/), containing:

- Full reproduction scripts for all experiments (e.g., `python exp001_hb_synthetic.py` for Table 1, `bash run_table1.sh` for full reproduction)
- Figure generation scripts (`draw_fig2.py`, `draw_fig3.py`, `figures/` directory)
- Global correction is implemented as the `Global` baseline in all experiment scripts (e.g., Lines 86–89 in Table 1) — users can directly compare global vs. EC-HTE correction
- `requirements.txt` for environment setup
- Preprocessed data files in `data/`

We apologize if the footnote link was not sufficiently prominent. We will make the code availability more visible in the camera-ready version (e.g., a dedicated "Code Availability" paragraph).

**Q2 (Appendix organization): "High number of appendices, difficult to get main findings."**

We appreciate this feedback. The main text (Sections 1–6, 8 pages) is designed to be self-contained: it presents the bias identity (Theorem 1), diagnostic (Proposition 1), method (Algorithm 1), and main results (Tables 1–2, Figures 2–5) without requiring the appendix. The 21-page appendix provides full proofs, robustness validations across 8 conditions, and details for reproducibility, following standard practice for theory-heavy papers at *ACL venues. We will add a roadmap at the beginning of the appendix in the camera-ready to improve navigability.

[INTERNAL: R1's Software=1 and Repro=2 are factual errors — the code is already released. Pointing this out should raise these meta-review scores significantly. Combined with Excitement=3.5, this should push R1's overall toward 4.0.]

---

## Response to Reviewer Sshp (R2)

We thank Reviewer Sshp for the careful evaluation and for recognizing the rigor of the theoretical contribution (Soundness: 4).

**W1: No real-data causal estimate; only synthetic CATE injection.**

We agree this is an important consideration and appreciate the suggestion. We address this at three levels:

(1) **Methodological standard.** Synthetic CATE injection on real text features is the established evaluation protocol in this literature. PPI (Angelopoulos et al., 2023), DSL (Egami et al., 2023), and the recent benchmark by Audinet et al. (2025) all use the same approach because no public dataset simultaneously provides: (a) LLM annotations, (b) expert gold labels, (c) a known causal effect, and (d) subgroup structure with heterogeneous annotation quality. Our paper explicitly acknowledges this gap (Limitations section).

(2) **Real annotation heterogeneity is validated.** While CATEs are synthetic, the LLM annotation errors are entirely real. Our case studies use actual GPT-4.1 annotations on UC Berkeley Hate Speech (Δπ = 0.117 across demographic subgroups, Section 5.2) and actual GPT-4o/Claude/Llama annotations on CivilComments (Δπ up to 0.184, Appendix P). These confirm that subgroup-heterogeneous error — the phenomenon driving our bias identity — arises in real annotation settings. The bias identity's R² ≥ 0.97 is validated on confusion matrices from all nine real LLMs (Section 5.3).

(3) **The contribution is primarily theoretical.** The core result (Theorem 1) is an exact algebraic identity: global correction introduces bias = δ_s · Δτ / (1−2π̄). This holds by construction whenever error rates are heterogeneous, regardless of how CATEs arise. The synthetic evaluation verifies the theorem's predictions, not a specific empirical claim about a particular domain.

We acknowledge constructing a fully real causal benchmark with LLM annotation as valuable future work.

**W2: K ≤ 4 is an important limitation; what should practitioners do with finer subgroups?**

We agree and offer the following guidance (which we will add to the Limitations section):

- **Hierarchical grouping**: When the natural subgroup structure has K > 4, practitioners can merge subgroups with similar error rates (identifiable from a pilot sample) to reduce K to ≤ 4 before applying EC-HTE. The diagnostic criterion (Proposition 1) can guide which groupings preserve the most heterogeneity.
- **Selective application**: Apply EC-HTE only to the top-K most heterogeneous subgroups (ranked by |δ_s|) and retain global correction for the remainder.
- **The K = 8 analysis in Appendix R** shows that HB partial pooling reduces stratified MLE RMSE by 47%, but still exceeds global correction at n_expert = 250 (~31 labels per subgroup). The bottleneck is per-subgroup sample size, not a fundamental limitation of the method — with sufficient expert budget (≥ 1000), K = 8 becomes viable.

[INTERNAL: R2's Soundness=4 is strong. The real-data concern is the hardest to fully resolve without new experiments, but the three-level defense (standard methodology + real error heterogeneity + theoretical contribution) should be sufficient. R2's overall is unlikely to drop; we aim to maintain 3.5 or push to 4.0 by showing responsiveness on W2.]

---

## Response to Reviewer ppmy (R3)

We thank Reviewer ppmy for the positive evaluation and for recognizing the soundness and practical value of the work.

**Q1: Define Y in E[Y(1) − Y(0) | Z = z].**

Thank you for this suggestion. Y denotes the outcome variable of interest (e.g., an individual's response to treatment). Y(1) and Y(0) are the potential outcomes under treatment and control, respectively, following the Neyman-Rubin framework. We will add an explicit definition at the beginning of Section 3 in the revised version: "Let Y denote the outcome of interest, with Y(1) and Y(0) the potential outcomes under treatment (W=1) and control (W=0)."

**Q2: Clarify B in Assumption A2.**

The notation [B_s]_{z,1} in Assumption A2 refers to the bias matrix B_s = M_global⁻¹ M_s − I, which is formally defined in the proof sketch below Theorem 1 (Section 3). We acknowledge the forward reference is confusing. In the revised version, we will either move the definition before A2 or replace the forward reference with an inline note: "where B_s is the bias matrix defined in Eq. (3) below."

[INTERNAL: R3 is already at 4.0, just maintain. These are trivial fixes.]

---

## Planned Revisions (Camera-Ready)

| # | Change | Affected Section | Triggered By |
|---|--------|-----------------|--------------|
| 1 | Add explicit definition of Y (outcome variable) | Section 3 | R3-1 |
| 2 | Clarify B_s notation in Assumption A2 | Section 3 | R3-2 |
| 3 | Add appendix navigation roadmap | Appendix (top) | R1-2 |
| 4 | Add K > 4 practitioner guidance | Limitations | R2-W2 |
| 5 | Make code availability more prominent | Section 1 or after Conclusion | R1-1 |
