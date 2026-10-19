---
dream_id: dream_20260520T201854
tier: worst
overall_score: 3/6 Weak Reject
timestamp: 2026-05-20T21:20:50.109808+00:00
---

# Dream Review Report — Full Roundtable

**Paper**: "Does Probe-Based Calibration Work Beyond English? A Systematic Investigation Across 3 Architectures and 52 Languages"

**Review mode**: full (2 reviewers, 4-step roundtable)
**Venue standard**: Top ML venue, ~25% acceptance rate, 6-point scale

---

## Reviewer Assignments
- **R1** (Methods + Experiments): methodology soundness, statistical rigor, experimental coverage
- **R2** (Novelty + Related Work): contribution novelty, significance, positioning, writing quality

---

## Step 1: Independent Reviews

### R1 — Methods and Experiments (Score: 4/6, Confidence: 4/5)

**Strengths:**
1. Unprecedented experimental scope: 3 architectures × 52 languages × 5 transfer methods × 3 benchmarks with systematic controls (Hewitt & Liang control tasks, random-direction control, INT8 validation, probe complexity comparison). This is one of the most thorough cross-lingual probing studies attempted.
2. Mean-shift rank-invariance proof (Theorem 1) is mathematically clean and empirically validated at ΔAUROC = 0.000 across 2 models × all probed layers × 19 languages. The theoretical-empirical pairing is exemplary.
3. Control task analysis (Table 13) is the most methodologically important contribution — revealing that 28% of low-resource language-layer pairs have selectivity < 8pp, with Swahili and Yoruba actually scoring BELOW the random-label control at the English-optimal layer. This is a genuine methodological insight for the field.
4. Linear projection data efficiency analysis (Table 12) is practically actionable: saturation at ~100 pairs, high-resource viable at 20 pairs, low-resource fails even at 200.
5. CaCLR ablation (Table 7) and β sensitivity sweep (Table 8) are well-designed: the monotonic decrease with β and the finding that removing consistency IMPROVES performance cleanly isolates the failure.

**Weaknesses:**

1. **(Major) CKA "mechanistic explanation" is confounded with depth.** Both CKA and transfer AUROC correlate with depth independently. The paper reports Pearson r = 0.32 (Table 11) but does not report partial correlation controlling for layer depth. Without this control, CKA may add zero explanatory power beyond depth itself. The claim that CKA explains "why CaCLR fails" (geometric rotation vs distributional shift) is plausible but not supported by the correlation analysis as presented. The qualitative argument (MMD can't correct rotation) is sound but the quantitative CKA evidence is insufficient.

2. **(Major) Architecture-dependence claim is severely confounded.** The three models differ simultaneously in: architecture (MoE vs Dense), scale (235B vs 48-layer vs 31B), number of layers (94/48/60), training data composition, and quantization (INT8 vs FP16). Attributing the Pareto frontier differences to "architecture" (specifically MoE routing) is unsupported. The non-monotonic jumps at layers 20–28 on Llama 4 are attributed to "MoE routing transitions" but no routing analysis is presented. With n=3 architectures and multiple confounds per comparison, no causal claim about architecture type is warranted.

3. **(Major) CaCLR implementation is critically underspecified.** The paper defines CaCLR's loss (§3.2) but omits: MMD kernel choice (Gaussian? linear? polynomial?), kernel bandwidth selection, optimizer, learning rate, number of epochs, early stopping criterion, batch size, and initialization strategy. For a negative result to be convincing, the community must be able to verify that the method was given a fair chance. The ablation and β sweep suggest thorough tuning of α and β, but the base training configuration is missing. This is essential for reproducibility regardless of whether CaCLR succeeds or fails.

4. **(Moderate) Statistical rigor is applied asymmetrically.** Bootstrap CIs and permutation tests are reported for CaCLR vs zero-shot (p = 0.71) and effect sizes for transfer methods (Table 6), but missing for: (a) the architecture comparison — no statistical test for whether Qwen3 ρ = −0.38 differs significantly from Llama4 ρ = −0.18; (b) the resource-tier boundaries — the taxonomy (high/mid/low) appears to be defined post-hoc without statistical justification for the tier boundaries; (c) CKA threshold analysis — the 0.35 threshold appears arbitrary.

5. **(Moderate) Selective reporting in main text.** Table 1 shows 5/24 layers for Qwen3, 4/12 for Llama4, 1 for Gemma4. Table 4 has full per-language data for Qwen3 only. The three-architecture comparison (Table 5) compresses Gemma 4 to a single row. Readers cannot independently evaluate claims about Gemma 4's Pareto frontier without the full per-language breakdown.

**Questions for Authors:**
1. What is the partial correlation between CKA and transfer AUROC after controlling for layer depth? If CKA adds no explanatory power beyond "deeper layers transfer worse," the mechanistic framing should be revised.
2. Please provide complete CaCLR training details: MMD kernel, bandwidth, optimizer, learning rate schedule, epochs, batch size. Without these, the negative result cannot be reproduced.
3. How were the resource-tier boundaries (high/mid/low) determined? Is there a natural clustering, or were they assigned based on external resource metrics?

---

### R2 — Novelty and Related Work (Score: 2/6, Confidence: 4/5)

**Novelty Assessment:**

*Contribution 1 — Mean-shift rank-invariance theorem:* This is mathematically trivial. The proof amounts to: subtracting a constant from all inputs to a monotonic function preserves their ordering; AUROC depends only on ordering; therefore ΔAUROC = 0. Any researcher who writes down the mean-shift formula and thinks about what AUROC measures would arrive at this in minutes. The paper claims this "distinguishes our setup from Xiao et al." — but the distinction is simply that Xiao et al. used accuracy (threshold-dependent) while this paper uses AUROC (rank-dependent). This is a difference in metric choice, not a theorem. **Verdict: obvious, not novel.**

*Contribution 2 — Resource-tier taxonomy:* The observation that transfer performance degrades with resource level is predicted by domain adaptation theory (Ben-David et al. 2010, which the paper itself cites). The H-divergence framework directly predicts that languages with larger distributional distance from the source (English) will transfer worse, and resource level is a proxy for distributional overlap in training data. The specific quantification (7–8pp for high, 10–12pp for mid, 13–20pp for low) is useful documentation, but documenting a predicted effect at scale is incremental empiricism, not a novel contribution. The extended coverage to 52 languages strengthens the documentation but doesn't change the qualitative picture. **Verdict: confirmatory, incremental.**

*Contribution 3 — Practical recommendation:* "Use few-shot with 25–100 labels" is not a research contribution — it is a practical observation that follows directly from contributions 1 (mean-shift doesn't work) and 2 (zero-shot fails for low-resource). Any practitioner who saw the zero-shot and mean-shift results would arrive at the same conclusion. **Verdict: follows from prior findings, not independently novel.**

**Significance:**
The paper has practical utility as a reference — practitioners wondering "should I use English correctness probes on Hindi?" can now cite specific numbers. But the answer ("probably not without some target-language data") is unsurprising. The most significant finding is actually the control task analysis (§5.10): the revelation that 28% of low-resource probing results are capacity artifacts is a genuine methodological contribution that the cross-lingual probing community needs to internalize. However, this finding is buried in §5.10 rather than centered as a main contribution.

**Who benefits?** Practitioners working on multilingual LLM calibration (narrow audience). The negative results on CaCLR save the community from pursuing distributional matching for this specific problem, but CaCLR is the authors' own proposed method — a negative result on your own untested method carries less weight than debunking an established technique.

**Related Work Positioning:**

1. The differentiation from Xiao et al. [2025] is fair but could be sharper. The paper correctly identifies that Xiao et al. targeted knowledge boundaries (input-level answerability) vs. correctness (output-dependent), and used accuracy vs. AUROC. But it underplays a key difference: Xiao et al. worked with 8 languages while this paper scales to 52 — the scale itself is a contribution that deserves more emphasis.

2. **Missing references (potentially significant):**
   - The paper does not cite Civelli et al. in the references despite mentioning them in §3.4 and §2 ("Civelli et al. transferred difficulty probes cross-lingually"). This is a significant omission — they appear to be the closest prior work on cross-lingual probing methodology.
   - No engagement with the broader cross-lingual transfer learning literature beyond alignment methods (MUSE, VecMap). Works on cross-lingual zero-shot transfer for NLU tasks (e.g., Pires et al. 2019 on multilingual BERT, Wu & Dredze 2019) are relevant for establishing that cross-lingual transfer degrades with language distance — the same finding this paper reports for probing specifically.
   - No discussion of concurrent work on calibration beyond Kadeethum et al. [2024].

3. The related work is organized well (5 clear subcategories) but is thin at 12 references total. For a survey-style paper claiming to be the "first systematic" investigation, the literature coverage should be more comprehensive.

**Writing Quality:**
- **Density**: 13 tables in 11 pages is excessive. Several could be merged or moved to supplementary (Tables 7+8 into one, Tables 9+10 could be supplementary). The paper reads like a technical report rather than a conference paper with a clear narrative arc.
- **Structure**: The 12 subsections in §5 (Results) create a fragmented reading experience. Key findings are spread across subsections without a unifying thread pulling them together. The Analysis section (§6) attempts synthesis but is only 0.5 pages — too short for a paper with this many findings.
- **Framing**: "Sobering empirical reality check" is appropriate but the paper doesn't fully commit to this framing. It oscillates between presenting CaCLR as a method contribution (§3.2, detailed loss function) and as an attempted-and-failed approach. If CaCLR is not a contribution, the method section should be shorter.
- **Abstract**: Overpacked with numbers. Three separate ρ values, three separate pp ranges, p-value and Cohen's d — the abstract reads like a results dump rather than a narrative.

**Strengths:**
1. Honest framing of negative results — the paper does not oversell. The "three surviving contributions" framing transparently acknowledges what didn't work.
2. Scale is impressive: 3 architectures, 52 languages, 5 transfer methods, 3 benchmarks. No prior work has attempted this for correctness probing.
3. The control task analysis (§5.10) is a genuinely important methodological contribution that the cross-lingual probing community needs.
4. Clear practical guidance (§6) organized by resource tier is useful for practitioners.

**Weaknesses:**
1. **(Major) Core contributions are either trivial (rank-invariance), confirmatory (resource-tier gradient), or derivative (practical recommendation).** None clear the novelty bar for a top ML venue individually. The paper's value is in comprehensiveness, but comprehensiveness alone is typically a findings-track or workshop contribution.
2. **(Major) CaCLR is the authors' own untested method, and its failure is the primary "result."** This is structurally weak: proposing a method, testing it, finding it doesn't work, and then claiming the negative result as a contribution. A stronger paper would debunk an established method or provide mechanistic insight into WHY distributional matching fails (the CKA analysis attempts this but is too weak at r = 0.32).
3. **(Moderate) The most novel finding (capacity artifacts in low-resource probing, §5.10) is buried.** If this were centered — "Probing low-resource languages is unreliable: a methodological warning" — the paper would have a stronger identity.
4. **(Moderate) Related work is too thin for a survey-style paper.** 12 references, missing Civelli et al. from the reference list, no engagement with cross-lingual transfer learning more broadly.
5. **(Minor) Writing density and fragmentation** undermine readability. 13 tables, 12 result subsections, 0.5-page analysis section.

**Questions for Authors:**
1. If mean-shift rank-invariance is "obvious" once you note that AUROC is rank-based, what is the intended contribution? Is it that the community has been applying mean-shift without realizing it's inert for AUROC? If so, can you cite specific works that make this mistake?
2. Could the paper be restructured to center the control-task finding (§5.10) as the primary contribution, with the resource-tier taxonomy and transfer method comparison as supporting evidence? This would give the paper a clearer identity.
3. Why is Civelli et al. mentioned in the text but missing from the references?

---

## Step 2: Cross-Sharing

**R1 → R2**: R1 notes the experimental rigor is genuinely strong — the control tasks, ablation design, and statistical tests are above average for an empirical ML paper. The CaCLR β sweep across 3 OOM is particularly convincing as evidence that the failure is fundamental, not a tuning artifact. R1 asks R2 to consider whether the sheer completeness of the experimental design partially compensates for individual contribution weakness.

**R2 → R1**: R2 asks R1 to consider whether the methodology, while competent, is serving contributions that are too thin. A well-executed investigation of a question whose answer was predictable doesn't become stronger just because the execution is thorough. R2 also flags that R1's score (4/6) may reflect methodology appreciation rather than overall paper merit — methodology is necessary but not sufficient.

## Step 3: Convergence

**Points of agreement:**
- The experimental scope is impressive and the execution is competent
- The control task finding (§5.10) is the most genuinely novel and impactful result
- The mean-shift theorem is mathematically correct but trivially obvious
- The CKA mechanistic analysis is insufficiently convincing (depth confound, r = 0.32)
- The architecture-dependence claim is confounded beyond what n=3 can support
- CaCLR is underspecified, weakening the negative result
- The paper is too dense (13 tables, 12 subsections) and would benefit from restructuring

**Points of disagreement (resolved):**
- R1 initially scored 4/6 based on methodology quality; after R2's argument that contributions must independently clear the novelty bar, R1 revises to 3/6. The methodology is sound but serves insufficiently novel claims.
- R2 initially scored 2/6; after R1's point about the control task finding's genuine value and the CaCLR ablation design quality, R2 revises to 3/6. The paper has real merit that the community should see, but not at a top venue main track.

**Consensus score: 3/6 (Weak Reject)**

## Step 4: Consolidated Assessment

### Overall Score: 3/6 (Weak Reject)
### Confidence: 4/5 (High — both reviewers have expertise in probing methods and cross-lingual NLP)

### Summary
This paper presents the first systematic cross-lingual evaluation of correctness probe transfer, covering an impressive scope: 3 architectures, 52 languages, 5 transfer methods, 3 benchmarks. The experimental execution is competent, with appropriate controls (Hewitt & Liang control tasks, random-direction baselines, INT8 validation) and statistical tests. However, the core contributions do not clear the novelty bar for a top ML venue:

1. The mean-shift rank-invariance "theorem" is trivially obvious — it restates that rank-based metrics are invariant to constant shifts.
2. The resource-tier taxonomy confirms what domain adaptation theory predicts — transfer degrades with distributional distance, and resource level proxies for this.
3. The practical recommendation (use few-shot) follows directly from the other findings.
4. CaCLR's failure is a negative result on the authors' own proposed method, with insufficient implementation details for reproducibility.

The most genuinely novel finding — that 28% of low-resource probing results are capacity artifacts (selectivity < 8pp) — is buried in §5.10 rather than centered as a main contribution.

### Strengths (consolidated)
1. **Experimental scope and rigor**: 3 architectures × 52 languages × 5 methods × 3 benchmarks with control tasks, random-direction controls, INT8 validation, and probe complexity comparison. The most comprehensive cross-lingual probing study to date.
2. **Control task revelation**: The finding that Swahili and Yoruba score BELOW the random-label control at the English-optimal layer is a genuine methodological contribution with implications for how the community evaluates cross-lingual probing.
3. **CaCLR negative result is well-designed**: The ablation (Table 7) cleanly isolates the consistency loss as the failing component, and the β sweep (Table 8) across 3 OOM rules out tuning failure. The mechanistic explanation (geometric rotation vs distributional shift) is qualitatively compelling.
4. **Honest framing**: The paper does not oversell. The "surviving contributions" framing transparently acknowledges what didn't work. The limitations section is candid about MCQA restriction and resource-tier coarseness.
5. **Practical utility**: Clear, actionable guidance organized by resource tier in §6. Practitioners can use Table 6 and Table 12 directly.

### Weaknesses (consolidated)
1. **(Major — Novelty) Core contributions are trivial, confirmatory, or derivative.** The rank-invariance theorem is obvious once stated. The resource-tier gradient is predicted by theory. The practical recommendation follows mechanically. None individually justify a top-venue paper. The paper's value is in comprehensiveness, which is a findings-track strength, not a main-track contribution.
2. **(Major — Reproducibility) CaCLR implementation is underspecified.** MMD kernel, bandwidth, optimizer, learning rate, epochs, and batch size are missing. A negative result demands higher reproducibility standards than a positive one — reviewers must be able to verify the method was given a fair trial.
3. **(Major — Confounding) Architecture-dependence claim is unsupported at n=3.** The three models differ in architecture type (MoE/Dense), scale, layer count, training data, and quantization. No causal attribution to "architecture" is warranted. The MoE routing explanation is plausible but untested.
4. **(Moderate — Analysis) CKA mechanistic analysis is unconvincing.** r = 0.32 overall, no partial correlation controlling for depth (the obvious confound), architecture-dependent (0.38 vs 0.24). The qualitative argument (geometric rotation explains CaCLR failure) is sound but unsupported by the quantitative evidence presented.
5. **(Moderate — Presentation) Paper is too dense and fragmented.** 13 tables and 12 result subsections in 11 pages create a technical-report feel. The most novel finding (control task artifacts) is buried. The analysis section is too short (0.5 pages) relative to the results section (4 pages). 12 references is thin for a survey-style paper.
6. **(Minor — Missing references) Civelli et al.** is cited in the text but missing from the reference list. Cross-lingual transfer learning literature (beyond alignment methods) is not engaged.

### Recommendations for Improvement
1. **Restructure around the control-task finding.** Center the paper on "Probing low-resource languages is methodologically unreliable" with the resource-tier taxonomy and capacity artifacts as the main contribution. CaCLR and decomposition become supporting negative results.
2. **Provide complete CaCLR details.** Full training configuration, ideally with code release. Consider testing additional alignment objectives (e.g., Procrustes alignment, adversarial domain adaptation) to strengthen the claim that distributional matching fundamentally fails, not just your specific MMD variant.
3. **Report partial CKA correlations.** Control for depth when reporting CKA-transfer correlations. If CKA adds nothing beyond depth, drop the mechanistic framing.
4. **Expand related work.** Engage with cross-lingual transfer learning literature more broadly. Fix missing Civelli et al. reference.
5. **Consolidate tables.** Move CaCLR β sensitivity, decomposition details, INT8 validation, probe complexity to supplementary. Target 7-8 tables in the main text.
6. **Consider a findings track or workshop.** The paper's strength is comprehensiveness, which is better suited to a findings track at *ACL or a workshop paper. Alternatively, a shorter, focused version centering the control-task finding could work for a main track.

### Detailed Scores
| Criterion | Score | Notes |
|-----------|-------|-------|
| Novelty | 2/6 | Trivial theorem, confirmatory taxonomy, derivative recommendation |
| Significance | 3/6 | Practical utility for narrow audience; control-task finding is significant but buried |
| Methodology | 4/6 | Strong experimental design, appropriate controls, some statistical gaps |
| Clarity | 3/6 | Dense, fragmented; 13 tables in 11 pages; buried key finding |
| Reproducibility | 2/6 | CaCLR underspecified; Gemma 4 results compressed; code not mentioned |
| **Overall** | **3/6** | **Weak Reject** — competent execution of insufficiently novel claims |

### Experiment Coverage Assessment
All 12 planned experiments are represented in the paper:
- Plans 001-002 (Pareto frontiers): ✓ Tables 1-5
- Plan 003 (CaCLR): ✓ Tables 6-8
- Plan 004 (Decomposition): ✓ Table 9
- Plan 005 (Orthogonality): ✓ Table 10
- Plan 006 (Probe complexity): ✓ mentioned in §5.1
- Plan 007 (Additional benchmarks): ✓ §5.12
- Plan 008 (Gemma 4): ✓ Table 5 (compressed)
- Plan 009 (52 languages): ✓ Table 3
- Plan 010 (INT8 validation): ✓ §5.11
- Plan 011 (CKA): ✓ Table 11, §5.8
- Plan 012 (LinProj sensitivity): ✓ Table 12
- Plan 013 (Control tasks): ✓ Table 13

Coverage is comprehensive. The main gaps are in reporting depth (Gemma 4 is severely underreported) and CaCLR implementation details.
