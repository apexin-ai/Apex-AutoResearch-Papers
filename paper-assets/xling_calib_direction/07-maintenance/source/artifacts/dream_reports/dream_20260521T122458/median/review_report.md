---
dream_id: dream_20260521T122458
tier: median
overall_score: borderline
timestamp: 2026-05-21T13:56:29.956991+00:00
---


# Review Report: Cross-Lingual Correctness Probe Transfer Reveals Architecture-Dependent Depth Effects

**Venue**: EACL via ACL Rolling Review (ARR)
**Review mode**: simple (single reviewer, full coverage)

---

## Summary

This paper investigates whether English-trained correctness probes — linear features in LLM hidden states that predict answer correctness — transfer cross-lingually. The study spans three architectures (Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense), 20 languages across four resource tiers, and five transfer strategies. Four interlinked findings are reported: (1) a depth-transferability Pareto tradeoff that varies by architecture, with 9/20 languages showing significant negative depth-transfer correlation on Qwen3 versus 5/20 on Llama4 and 7/20 on Gemma4; (2) a Simpson's Paradox in the CKA-transfer relationship where raw correlations are negative but partial correlations controlling for depth turn positive in 2/3 architectures; (3) CaCLR (MMD-based consistency loss) is inert across a full β sweep, with CORAL and high-dimensional MMD variants also failing — geometric explanation via correctness subspace angle analysis; and (4) linear projection with ~80 parallel pairs achieves 95% of maximum improvement, with a Procrustes reversal threshold at ZS AUROC ~0.57.

The paper additionally contributes probing controls revealing 22% of language-layer combinations are capacity artifacts, a difficulty decomposition analysis (descriptive, not prescriptive — 56% accuracy vs 50% chance), cross-lingual orthogonality confirmation, LR vs MLP comparison, cross-benchmark generalization on Belebele and MMLU-ProX, quantization validation, and a 52-language extension. All 13 planned experiments are reported across 16 tables in 10 pages. The paper contains zero figures.

## Strengths

1. **Unprecedented experimental scope with careful confound control.** Three architectures spanning both MoE and dense designs, 20 languages across 4 resource tiers, 3 benchmarks, and systematic ablations. Gemma 4 Dense serves as a crucial control ruling out that the Pareto tradeoff is an MoE routing artifact. This is genuinely the first large-scale study of cross-lingual correctness probe transfer, and the scale is impressive for a 10-page paper.

2. **Intellectually honest treatment of the CaCLR negative result.** Rather than burying an unsuccessful method, the paper elevates the negative finding with a principled geometric explanation grounded in Zhao et al. (2019): MMD reduces marginal distance but leaves the correctness subspace angle unchanged (Table 7: HIGH tier angle 11° → 10.5°, MID 23° → 22°, LOW 44° → 42° after CaCLR, while MMD distance halves). The systematic β sweep across 3 orders of magnitude (0.001–1.0), CORAL comparison, and high-dimensional MMD variants (PCA d=50, d=100) thoroughly close the distributional matching path.

3. **Simpson's Paradox finding is non-trivial and has mechanistic support.** The sign reversal from raw negative ρ (−0.24 to −0.30) to positive partial ρ controlling for depth is a genuine insight about CKA's explanatory role. The subspace angle analysis (Table 4: HIGH 10–13°, MID 22–26°, LOW 41–46° across architectures) provides concrete geometric evidence for why within-layer CKA predicts transfer quality even though the raw correlation is misleading.

4. **Probing controls at cross-lingual scale.** Applying Hewitt & Liang (2019) controls to all 20 languages × 3 architectures × all probed layers is a first. The finding that 22% of combinations are artifacts — concentrated in LOW-resource shallow layers (80% artifact rate at 0–25% depth for LOW tier) — is an important methodological warning. The confirmation that am/yo have selectivity < 0.03 at EN-optimal depth validates treating their high orthogonality cosines as noise artifacts.

5. **Actionable practical contribution.** The linear projection saturation curves stratified by resource tier (Table 9: HIGH saturates at ~38 pairs, LOW at ~95 pairs), the Procrustes reversal threshold at ZS AUROC ~0.57 (Table 10), and the layer selection recommendation (70–75% depth) are directly deployable. The finding that projection *harms* well-aligned languages (−1.8pp mean for ZS AUROC > 0.72) is a valuable practitioner caveat.

6. **Cross-benchmark generalization.** Replication on Belebele (reading comprehension) and MMLU-ProX (translated MMLU) with cross-benchmark language ranking ρ = 0.89 and all qualitative findings preserved (Table 13) strengthens confidence that results are not benchmark-specific.

## Weaknesses

1. **Complete absence of figures is a critical presentation failure (Major).** The paper's core contributions are geometric — Pareto frontiers, CKA depth profiles, Simpson's Paradox sign reversals, subspace angles, saturation curves, Procrustes reversal — yet it contains 16 tables and zero figures. This is untenable. A reader cannot assess the shape of the Pareto frontier, the steepness of the CKA cliff (plateau-then-drop for Qwen3 vs gradual for Llama4), the cleanness of the Simpson's sign reversal, or the saturation curve plateau from tabulated numbers alone. Key visualizations that are essential: (a) Pareto scatter plots per architecture, (b) CKA depth profiles showing the three architectural patterns, (c) Simpson's Paradox scatter with per-depth-bin regression lines, (d) β sweep curve with confidence bands, (e) Procrustes reversal scatter. This omission materially harms readability and reviewability.

2. **Simpson's Paradox universality is overstated (Major).** The Qwen3 partial correlation (ρ=+0.16, p=0.072) is NOT significant at conventional thresholds. The paper's framing of "partial correlation reverses the sign" applies to 2/3 architectures, not all three. The CKA depth profile explanation (Qwen3's step-function shape limits linear partial correlation effectiveness) is reasonable but also means the finding is contingent on architecture-specific geometric properties. The within-layer analysis (17/24 layers with positive ρ) provides directional evidence but with n=20 per layer, individual significance is limited. The paper should transparently present this as "confirmed in 2/3 architectures with a consistent trend in the third" rather than as a universal finding.

3. **Architecture attribution is fundamentally confounded (Moderate).** The three architectures differ simultaneously in model family, active parameter count (22B/17B/31B), total parameters, training data, tokenizer, layer count (94/48/60), and quantization format (INT4/W4A16/BF16). With n=3 and all dimensions confounded, claims about "architecture dependence" are observational descriptions, not causal findings. The paper acknowledges this in Limitations but uses stronger language throughout the main body (e.g., "architecture-dependent" in the title). Particularly, the Pareto strength difference (9 vs 5 vs 7 significant languages) could equally reflect training data composition or scale differences.

4. **Difficulty decomposition adds limited value (Moderate).** Prescriptive accuracy of 56% versus 50% chance is essentially uninformative. The mean effect (+1.8pp) exceeds random-direction control (+0.7pp) by a factor of 2.6, but this is driven by a few MID-resource languages (hi: +2.8pp, tr: +2.5pp, bn: +3.5pp) while harming others (ko: −0.6pp, sw: −1.2pp). The "descriptive, not prescriptive" framing is appropriate but raises the question of whether this section earns its page budget. Given the paper's space constraints (zero figures, 12 subsections in Results), this could be compressed to a paragraph or moved to an appendix.

5. **The label-free framing understates data requirements (Moderate).** Linear projection with ~80 parallel pairs requires parallel sentence-level data, which is non-trivial for genuinely low-resource languages. The paper correctly notes CaCLR requires ~10K parallel items, but the headline framing ("label-free") may mislead readers about the true annotation effort. The irony is that the languages most needing improvement (LOW tier: +5.2pp at 50 pairs, +6.2pp at 200 pairs) are precisely those where parallel data is hardest to obtain. Yoruba (yo), the lowest-performing language, consistently shows the worst results (ZS AUROC 0.535, selectivity 0.023).

6. **Paper is severely compressed (Moderate).** 12 subsections under Section 4, 16 tables in 10 pages, some analyses receiving only 2–3 sentences (orthogonality, quantization validation, 52-language extension). The paper reads as a technical report compressed into a conference paper format. Several analyses that receive cursory treatment (probe complexity, extended coverage) could be moved to an appendix to give core findings more breathing room — and more critically, space for figures.

## Questions for Authors

1. Can you provide HIGH+MID-only versions of the three key aggregate statistics (mean ZS AUROC, Pareto prevalence, Simpson's partial ρ) to confirm that the 22% artifact rate in LOW-resource combinations does not materially affect core findings?

2. For the Qwen3 Simpson's Paradox (ρ=+0.16, p=0.072): have you tested a non-linear control (e.g., adding depth² as a quadratic term) given the step-function CKA profile? Would this change significance?

3. Table 7 shows CaCLR reduces MMD distance by ~50% (e.g., HIGH: 0.018 → 0.008) while subspace angle barely changes (11° → 10.5°). Was this verification done on the same runs as the β sweep, or separately? This is the key evidence for the geometric explanation and its provenance matters.

4. The mean-shift ΔAUROC ≡ 0 result is described as a mathematical invariance under StandardScaler + LR. Can you include a proof sketch in the appendix? This clean theoretical result distinguishes your setting from Xiao et al. (2025) and deserves formal treatment.

5. The Procrustes reversal threshold (ZS AUROC ~0.57, CI [0.48, 0.64]) — is the mechanism primarily estimation noise in the rotation matrix (finite sample of ~80 pairs) overwhelming the small misalignment for already-aligned languages, or is there a deeper geometric explanation?

6. For the 52-language extension: how many of the 52 languages have artifact rates exceeding 20%? Does the rank correlation (0.95) hold when restricted to languages with artifact rate < 10%?

7. What is the computational cost of the full experimental pipeline? The paper probes every 4th layer across 3 large models on 20 languages with 3 seeds — this is substantial compute. Reporting GPU-hours would help readers assess reproducibility.

## Minor Issues

- The title is 19 words long with a colon-separated subtitle. Consider shortening.
- "Distributional Matching Fails but Linear Projection Succeeds" in the title is a strong binary; the reality is more nuanced (distributional matching is *inert*, not catastrophically failing).
- 12 subsections under Section 4 (4.1–4.12) is unusual. Consider grouping into 4–5 thematic sections (Core Findings, Transfer Methods, Methodological Validation, Extensions).
- The paper lacks an appendix despite clear candidates: per-language full tables, β sweep details, mean-shift proof, quantization per-layer results, 52-language full results.
- "CKA cliff slope" is used repeatedly but never formally defined (threshold for "cliff" onset, linear fit specification).
- Table 2 shows only 13/20 languages (selected); the remaining 7 (pt, hi, vi, tr, id, sw, bn) are referenced but not shown. Consider a full table in the appendix.
- The distinction between "correctness probes" (this work) and "knowledge-boundary probes" (Xiao et al.) could be more prominent in the abstract.

## Missing References

- Belinkov (2022) "Probing Classifiers: Promises, Shortcomings, and Advances" — directly relevant to the probing methodology discussion and capacity artifact concerns.
- Muller et al. (2021) "First Align, Then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT" — relevant to the CKA analysis and cross-lingual alignment mechanisms.
- Conneau et al. (2020) "Emerging Cross-Lingual Structure in Pretrained Language Models" — foundational work on cross-lingual representation structure that contextualizes the CKA findings.
- Yin et al. (2022) "Do All Languages Cost the Same? Tokenization in the Era of Commercial Language Models" — relevant to the tokenizer confound in cross-architecture comparison.

## Ethical Considerations

No major concerns. The paper appropriately acknowledges limitations of low-resource language evaluation and the potential for translation quality to affect results. The use of publicly available benchmarks (GlobalMMLU, Belebele, MMLU-ProX) is standard. Minor consideration: the practical recommendation "use linear projection below ZS AUROC 0.57, skip above 0.65" could be misapplied if users treat calibration probes as ground-truth correctness indicators rather than statistical estimators with meaningful uncertainty.

## Scores

- **Soundness**: 3/5 — Methodology is thorough (proper controls, multi-seed, quantization validation, cross-benchmark), but Simpson's Paradox universality is overstated (significant in only 2/3 architectures), difficulty decomposition prescriptive accuracy (56%) undermines its utility, and the 22% artifact rate without HIGH+MID-only validation of aggregates introduces uncertainty about whether core statistics are distorted.
- **Excitement**: 3/5 — The research question is timely and the scope is impressive, but the main method contribution (CaCLR) is a negative result, the positive practical finding (linear projection via Procrustes) is a known technique applied to a new domain, and individual effect sizes are modest (the best label-free method achieves +3.0pp over zero-shot).
- **Overall Assessment**: 3/5 — Borderline. The experimental scale is commendable and several findings (CaCLR negative result with geometric explanation, probing artifact rates, linear projection saturation with reversal threshold) are valuable for the community. However, the complete absence of figures in a geometry-heavy paper, the overstated Simpson's Paradox universality, and the compression of 13 experiments into 10 figure-less pages make this a borderline paper in its current form.
- **Confidence**: 4/5 — Strong familiarity with probing methodology, cross-lingual transfer, and calibration literature.

## Meta-Review Assessment

This paper makes a genuine contribution by being the first systematic study of cross-lingual correctness probe transfer at scale. The experimental design is thoughtful, the CaCLR negative result is handled with intellectual honesty and theoretical grounding, and the probing control artifact findings have implications beyond this paper. However, three issues prevent a clear accept: (1) the complete absence of figures is disqualifying for a paper about geometric phenomena — adding 4–5 key visualizations (Pareto overlay, Simpson's scatter, CKA depth profiles, β sweep curve, Procrustes reversal) is essential; (2) the Simpson's Paradox universality claim needs modulation to reflect the non-significant Qwen3 result (p=0.072); and (3) the paper tries to do too much in too little space — 13 experiments in 10 figure-less pages creates a compressed, hard-to-absorb presentation. The strongest path forward: add figures, move 3–4 supporting analyses (quantization, 52-language extension, probe complexity, orthogonality) to an appendix, expand the core narrative (Pareto + CaCLR negative result + linear projection), and correct the Simpson's claim. These changes would likely move the score to Accept (4/5). In its current form: **borderline, revise and resubmit**.
