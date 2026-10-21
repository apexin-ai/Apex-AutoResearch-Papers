---
dream_id: dream_20260522T021705
tier: median
overall_score: weak reject (5/10)
timestamp: 2026-05-22T03:27:57.039425+00:00
---

# Dream Review Report: Token-Level Instruction Routing in VLAs

**Paper**: "Token-Level Instruction Routing in Vision-Language-Action Models: A Cross-Architecture Analysis"
**Venue**: CoRL 2026
**Review mode**: Full (2 reviewers, 4-step roundtable)
**Date**: 2026-05-22

---

## Venue Calibration

CoRL 2026. ~30% acceptance rate. OpenReview 1–10 scale (10 = top 5% seminal; 8 = clear accept; 6 = marginally above threshold; 5 = marginally below; 3 = clear reject). Evaluation criteria: significance and novelty of results, degree to which results are objectively established, relevance to robot learning. Honestly reported limitations are valued.

---

## R1 Review — Methods & Experiments

### Summary
The paper applies five established analysis methods (R² probing, L1 attention decomposition, cross-instruction classification, counterfactual sensitivity, RSA) across a 3-architecture × 4-suite matrix to characterize how VLA fine-tuning reshapes instruction processing. R² exit collapse is confirmed in 8/10 cells with statistical support (Wilcoxon p=0.002, r=0.81). Two weak cells (OpenVLA Spatial, OpenVLA Long/OFT) and a CF metric inconsistency weaken the broader claims.

### Strengths
- **Well-structured factorial design.** The 3×4 architecture–task matrix with paired trained/untrained controls is rigorous. Testing on architecturally distinct backbones (Llama-2 MHA 32L, Phi-3 MHA 32L, Qwen2.5-VL GQA 36L) provides meaningful breadth.
- **R² exit collapse is the paper's strongest contribution.** 8/10 confirmed cells with trained Δ ranging from 0.121 to 0.691 vs. untrained Δ of 0.01–0.08 is a clear, robust signal. The continuous slope metric (Table 9) corroborates the binary classification.
- **Honest trained-vs-inherited decomposition.** Demonstrating that L1 attention routing is base-model-dependent (e.g., TracVLA untrained 32/32 heads *decreasing* to 27–30/32 with training) is counterintuitive and reflects scientific integrity.
- **Transparent exception handling.** Weak cells, the OFT confound, and the RSA/CKA disagreement are openly reported rather than hidden.
- **Exit collapse rate analysis** provides a continuous alternative to the binary Δ≥0.05 threshold, strengthening the statistical narrative.

### Weaknesses

**Major:**

1. **CF "7–10× amplification" is methodologically invalid.** Trained models use Cohen's d in action space; untrained VLM bases (Tier-1) use cosine distance in hidden-state space. These are incommensurable metrics — ratios across them are meaningless. Critically, when the same metric IS used (OpenVLA OXE-pretrained, Tier-2), the ratios are 1.12× (Goal), ~2× (Object), and *inverted* at 0.81× (Spatial). The one case where fair comparison exists contradicts the amplification narrative.

2. **OpenVLA Spatial undermines the "8/10" narrative more than acknowledged.** Δ=0.037 fails the paper's own threshold AND the CF ratio is inverted (0.81×). Combined with OpenVLA Long/OFT (Δ=0.004), OpenVLA's per-architecture pass rate is only 50% (2/4). This is the most-studied VLA family — if half its cells fail, "consistent across architectures" is a stretch.

3. **Three-tier gradient rests on n=1 for Tier-2.** Only OpenVLA has an OXE-pretrained intermediate checkpoint. TracVLA and NORA jump from VLM base to task-finetuned with no intermediate. This is a single-architecture observation elevated to a contribution (C4).

4. **No behavioral validation at a robotics venue.** All analysis is open-loop representational. No connection to downstream task performance is demonstrated. The paper's own ablation (removing 24/32 instruction-dominant heads → no MSE effect) creates an interpretive puzzle: if routing is functionally important, why does removing it not affect actions?

5. **Main text is OpenVLA-centric despite cross-architecture framing.** The title and abstract promise a cross-architecture analysis of three VLAs, but the body reads as an OpenVLA study with a confirmatory paragraph on TracVLA and minimal NORA coverage. The full 3×4 matrix results are not presented in a unified way in the main text.

**Minor:**

6. **Δ≥0.05 threshold is unjustified.** No formal motivation is given for why 0.05 rather than 0.03 or 0.10. This appears arbitrary and happens to place both problematic cells below threshold.

7. **NORA covers only 2/4 suites** (Object and Long checkpoints unavailable). This is an external constraint but means the "three architecture" claim is unevenly supported.

8. **Baseline asymmetry** between Tier-1 (pure VLM) and Tier-2 (OXE 970K episodes) untrained models confounds cross-architecture comparisons of CF sensitivity and R² magnitudes. This deserves more prominent discussion than it receives.

### Questions for Authors
1. Can you report CF results using the *same* metric for both trained and untrained conditions (cosine distance for trained, or Cohen's d for OXE-pretrained)?
2. How sensitive is the Wilcoxon p=0.002 to recoding the two weak cells as "no collapse"?
3. The head-ablation experiment shows no MSE effect — how do you reconcile this with claims of functional importance of instruction routing?
4. Have you attempted to obtain intermediate pretraining checkpoints for TracVLA or NORA to test the three-tier hypothesis?
5. Can you correlate exit collapse magnitude with task success rate across the 10 cells?

### R1 Scores
| Dimension | Score |
|-----------|-------|
| Overall | **5** / 10 (marginally below threshold) |
| Soundness | 3 / 4 |
| Contribution | 2 / 4 |
| Clarity | 3 / 4 |
| Confidence | 4 / 5 |

**R1 Decision: Weak Reject**

---

## R2 Review — Novelty & Related Work

### Summary
The paper applies standard mechanistic interpretability tools (probing, attention analysis, counterfactual perturbation, RSA) to three VLA architectures, documenting R² exit collapse as a training-induced signature. While the empirical observation is robust within the tested scope, the framework contributes method application rather than method innovation, the explanatory depth is shallow (documenting *that* collapse occurs without explaining *why*), and the related work is critically thin.

### Strengths
- **R² exit collapse is a genuine empirical finding.** The 8/10 cell confirmation with Wilcoxon p=0.002 and effect size r=0.81 is convincing within the tested scope.
- **Training-vs-inherited decomposition** (L1 heads = base-model property) is a useful conceptual contribution that prevents misattribution in future work.
- **Scientific transparency is above average.** The paper honestly qualifies its claims, reports exceptions, and relegates metric-dependent findings (RSA/CKA) to appendix. The six explicit limitations are admirably self-aware.
- **Systematic experimental coverage.** 10 evaluable cells across 3 architectures and 4 task suites represents substantial effort.

### Weaknesses

**Major:**

1. **C1 (framework) is method application, not method innovation.** Every component — R² probing, attention decomposition, cross-instruction classification, counterfactual perturbation, RSA — is an established technique from NLP/vision interpretability. The contribution is applying them to VLAs in a structured way, which is useful but does not constitute a novel method. Framing it as "a systematic experimental framework" inflates a study design into a method contribution.

2. **Exit collapse is descriptive, not explanatory.** The paper documents *that* R² declines in exit layers of trained models, but not *why*. The trivial explanation — exit layers specialize for next-token (action) generation under the fine-tuning loss, discarding information not directly useful for the immediate action prediction — is never engaged with or ruled out. Without a mechanistic explanation or causal intervention, exit collapse remains an empirical regularity, not a scientific insight.

3. **CF metric incommensurability.** (Same as R1.) The "7–10× amplification" conflates Cohen's d (action space) with cosine distance (hidden space). When measured commensurably (OpenVLA OXE), ratios drop to 0.81–2×, and the Spatial cell shows *inversion*.

4. **"Architecture-independent" is overclaimed.** All three tested models are decoder-only autoregressive transformers. They differ in backbone LLM and attention mechanism (MHA vs GQA) but share the fundamental architecture. Claiming "architecture-independent" when the architectural diversity is backbone-within-decoder-only-transformer is misleading. Moreover, OpenVLA has 50% anomalous cells.

5. **Related work is critically thin.** Only 10 references in total. Missing:
   - Concurrent VLA interpretability work (multiple 2025-2026 papers on probing VLA representations)
   - Broader probing literature in LLMs (Hewitt & Manning 2019 on probing design; Voita & Titov 2020 on information-theoretic probing)
   - Instruction grounding in embodied AI (Shridhar et al. 2022, ALFRED/TEACH benchmarks)
   - Mechanistic interpretability in multimodal models (Palit et al. 2023 on CLIP internals)
   - The 10-reference count is far below CoRL norms (~30-50 references)

6. **C4 (three-tier gradient) should not be listed as a contribution.** A single datapoint observation acknowledged as "suggestive" does not meet the threshold for a numbered contribution. It belongs in Discussion, not in the contribution list.

**Minor:**

7. **Claim calibration issues.** "Consistent across three tested architectures with caveats" when one architecture (the most studied one) passes only 2/4 cells is optimistic framing. A more accurate summary: "Robust across two architectures (TracVLA 4/4, NORA 2/2), partially confirmed in a third (OpenVLA 2/4)."

8. **No discussion of how findings should change VLA design.** If exit collapse and CF sensitivity are training-induced, what should practitioners *do* differently? The paper identifies a phenomenon but offers no design recommendations, reducing practical impact at a robotics venue.

### Missing References/Comparisons
- Concurrent VLA interpretability papers (2025-2026)
- Hewitt & Manning 2019 (structural probe design)
- Voita & Titov 2020 (information-theoretic probing)
- Elhage et al. 2021/2022 (mechanistic interpretability in transformers)
- Palit et al. 2023 (multimodal model internals)
- Shridhar et al. 2022 / TEACH / ALFRED (instruction grounding in embodied AI)
- Broader VLA evaluation literature beyond Grant and Haon

### R2 Scores
| Dimension | Score |
|-----------|-------|
| Overall | **4** / 10 (below threshold, insufficient novelty) |
| Soundness | 3 / 4 |
| Contribution | 2 / 4 |
| Clarity | 3 / 4 |
| Confidence | 4 / 5 |

**R2 Decision: Weak Reject**

---

## Roundtable Synthesis

### Step 2 — Cross-Sharing
R1 and R2 independently converged on Weak Reject. Both identified the same four core problems: (1) CF metric incommensurability, (2) three-tier n=1, (3) missing behavioral validation, (4) claim overcalibration. R2 was more critical on novelty (framework = method application, exit collapse = descriptive) and related work thinness. R1 was more specific on the structural gap between cross-architecture framing and OpenVLA-centric content.

### Step 3 — Convergence

**Agreed strengths:**
- R² exit collapse (8/10, p=0.002, r=0.81) is a genuine, robust empirical finding
- Training-vs-inherited L1 decomposition is a useful insight
- Scientific transparency and limitation reporting are above average
- The factorial experimental design is well-structured

**Agreed weaknesses (consensus):**
1. CF "7–10×" claim is methodologically invalid (incommensurable metrics); the one fair comparison shows minimal or inverted amplification
2. Three-tier gradient has n=1 Tier-2 support — insufficient for a numbered contribution
3. No behavioral validation; the head-ablation null result raises questions about functional relevance
4. "Architecture-independent" overclaims relative to evidence (OpenVLA 2/4, all decoder-only)
5. Claims need tempering throughout

**Disagreements:**
- R2 views the novelty gap as more fundamental (method application + descriptive finding may be below threshold even with perfect execution); R1 sees a viable revision path (restructure main text, fix CF claim, add behavioral pilot)
- R2 flags critically thin related work as a standalone major weakness; R1 treats it as minor

### Step 4 — Consolidated Assessment

**Overall Score: 5 / 10 (Marginally Below Acceptance Threshold)**

**Decision: Weak Reject**

**Rationale:**

The paper's core finding — R² exit collapse as a training-induced signature across VLA architectures — is a genuine empirical contribution. The 8/10 cell confirmation rate with Wilcoxon p=0.002 and large effect size (r=0.81) establishes a real phenomenon. The training-vs-inherited decomposition of L1 routing heads is a useful conceptual contribution. Scientific transparency is commendable.

However, five issues collectively place the paper below the CoRL acceptance threshold:

1. **Invalid CF amplification claim.** The "7–10×" headline result compares incompatible metrics. When measured commensurably (OpenVLA Tier-2), amplification is minimal or inverted. This is not a minor caveat — it undermines the second-most-prominent finding.

2. **Descriptive rather than explanatory.** Exit collapse is documented but not explained. The trivial hypothesis (exit layers specialize for action prediction) is not engaged with. Without mechanism or behavioral consequence, the finding's scientific value is limited.

3. **Claim-evidence mismatch.** "Consistent across three tested architectures" when OpenVLA passes 2/4 cells; "architecture-independent" when all models are decoder-only transformers; a "suggestive observation" listed as Contribution #4.

4. **Missing behavioral link.** At a robotics venue, purely representational analysis without any connection to task performance — especially when the one reported ablation shows null effect — is a significant gap.

5. **Thin positioning.** 10 references, no engagement with concurrent VLA interpretability work, no practical design recommendations.

**Path to acceptance:** The R² exit collapse finding is strong enough to anchor a revised paper. Key revisions needed: (a) remove or honestly reframe the CF amplification claim using consistent metrics, (b) restructure main text to present the full cross-architecture matrix, (c) add at least a correlational behavioral analysis, (d) expand related work substantially, (e) demote three-tier gradient from contribution to discussion, (f) temper "architecture-independent" language. With these changes, the paper would likely reach 6/10.

**Experiment Coverage Assessment:**
Comparing the paper against the full experiment design (review_context.yaml):
- openvla_goal_standardized_v1: Fully reflected in paper (Tables 2, 5)
- openvla_spatial_standardized_v1: Fully reflected (Tables 3, 6), including the problematic CF inversion
- cf_batch_missing_v1: Reflected in Table 7 (untrained CF baselines), but the massive OXE-vs-Phi-3 baseline asymmetry deserves more discussion
- exit_collapse_rate_analysis: Fully reflected (Tables 9, 10)
- aggregate_metrics_summary: Partially reflected — the full cross-architecture matrix (Table 1) is present but per-architecture pass rates and geometric mean CF ratios are not explicitly stated
- NORA results: Only 2/4 suites covered, acknowledged as limitation
- Missing from imagined but not in paper: no intermediate training checkpoint analysis, no closed-loop behavioral correlation

**Score Summary Table:**

| | R1 | R2 | Consensus |
|---|---|---|---|
| Overall | 5 | 4 | **5** |
| Soundness | 3/4 | 3/4 | **3/4** |
| Contribution | 2/4 | 2/4 | **2/4** |
| Clarity | 3/4 | 3/4 | **3/4** |
| Decision | Weak Reject | Weak Reject | **Weak Reject** |

**Accept Probability Estimate: ~0.30**
Would require a champion reviewer (not among R1/R2) who values the empirical breadth of R² exit collapse highly enough to outweigh the CF and behavioral gaps. Possible but below the ~0.35 bar that a "needs champion" paper typically requires.

---

## 引用验证结果

**统计**: 62 篇文献 / 98 处引用 / 在线验证 62/62 篇

### 问题 (14)

- ⚠️ `liu2023_libero` — 元数据不匹配: first_author: bib=liu vs api=feng
- ⚠️ `haon2025` — 元数据不匹配: first_author: bib=h\"aon vs api=häon
- ⚠️ `fei2025` — 元数据不匹配: first_author: bib=fei vs api=senyu
- ⚠️ `meng2022_rome` — 元数据不匹配: first_author: bib=meng vs api=andonian
- ❌ `elhage2021` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.22 below threshold 0.82
- ❌ `hewitt2019` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.32 below threshold 0.82
- ⚠️ `neo2025` — 元数据不匹配: first_author: bib=neo vs api=leng
- ⚠️ `lakens2017equivalence` — 元数据不匹配: title: similarity=0.34 (possible wrong DOI)
- ❌ `bills2023language` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.31 below threshold 0.82
- ❌ `templeton2024scaling` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.26 below threshold 0.82
- ❌ `nostalgebraist2020` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.35 below threshold 0.82
- ⚠️ `padalkar2023_oxe` — 元数据不匹配: first_author: bib=padalkar vs api=collaboration
- ⚠️ `michel2019sixteen` — 元数据不匹配: year: bib=2019 vs api=2014, first_author: bib=michel vs api=narla
- ⚠️ `ouyang2022training` — 元数据不匹配: first_author: bib=ouyang vs api=agarwal

### ✅ 通过 (48)