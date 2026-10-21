---
dream_id: dream_20260521T032813
tier: median
overall_score: 3 — Weak Reject
timestamp: 2026-05-21T04:32:57.362355+00:00
---

# Dream Review Report

**Paper:** Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics

**Review Mode:** Simple (single reviewer, full coverage)

**Overall Score:** 3 — Weak Reject

**Confidence:** 4 (High — familiar with G-theory, LLM evaluation, and variance decomposition literature)

---

## 1. Summary

The paper applies Generalizability Theory (G-theory) to decompose variance in LLM evaluation by crossing infrastructure factors (GPU hardware, numerical precision) with methodology factors (prompt template, random seed, temperature, option ordering) across five benchmarks (MMLU, GSM8K, ARC-Challenge, HellaSwag, MATH), three 7–8B models, two scoring metrics, and two GPU types. Over 3.3 million evaluation records yield three findings: (1) item selection and model×item interaction jointly dominate variance, with benchmark-conditional relative magnitude; (2) infrastructure×methodology separability holds under binary scoring on knowledge benchmarks but fails under text-match scoring; (3) reproducibility budgets (480–950 items for G≥0.90) are benchmark-specific. Supplementary experiments cover 14B scale validation, fine-tuning variance hierarchy inversion, LayerCast precision diagnostics, and MATH extension.

---

## 2. Strengths

**S1. Well-motivated research question.** Prior work isolates individual variance sources (prompt, seed, precision, ordering) in separate studies. The key question — whether these factors interact or can be composed — is practically important. The paper is the first to cross infrastructure and methodology factors systematically in a multi-benchmark G-theory design.

**S2. Rigorous factorial design and impressive scale.** 3.3M records across 8 experiments with fully crossed (or nearly so) designs. The G-theory framework is well-suited to the research question: it naturally decomposes variance into main effects and interactions, and D-studies project reliability under hypothetical designs. The use of `enforce_eager` to eliminate engine confounds shows careful attention to experimental validity.

**S3. Honest, nuanced reporting.** The GSM8K CI overlap (item_id vs model×item statistically indistinguishable) is reported transparently rather than being hidden. The HellaSwag≈MMLU non-monotonicity that breaks the expected knowledge→reasoning gradient is acknowledged. Separability is qualified as "metric-conditional" rather than being oversold. This intellectual honesty is commendable.

**S4. Model-as-facet reanalysis is a genuine contribution.** The shift from single-model analysis (item_id ~53%) to model-as-facet (item_id ~35%, model×item ~22%) is methodologically important and reveals that much of what appears as "item variance" in single-model studies is actually differential item functioning across models. The GSM8K reversal (model×item > item_id) is a clean, interesting finding.

**S5. Thorough methodological defense.** Six defenses systematically address predictable criticisms: Bernoulli mechanical effects (r=0.72 acknowledged, text-match parallel validates), fixed vs random facet treatment, bootstrap vs jackknife CI comparison (ratio 1.15), REML sensitivity (2.8pp max deviation, rank preserved), design asymmetry robustness (2.1pp), and full-benchmark G verification (0.985 at 14K). This builds substantial confidence in the primary estimates.

**S6. Practical D-study recommendations.** The 480–950 item range for G≥0.90 (binary) and the 6.2× gap vs IRT-based subsampling are actionable findings. The explicit quantification of "the cost of multi-facet reliability" gives practitioners concrete guidance.

**S7. Inference vs fine-tuning contrast.** The variance hierarchy inversion (item_id drops from #1 to #4; LR/seed/shuffle rise) is a clean finding that properly scopes the claims to inference-time evaluation.

---

## 3. Weaknesses

**W1. Severely limited model diversity undermines model-as-facet analysis (Major).** Only 3 models at 7–8B (Llama-3.1-8B, Qwen3-8B, Mistral-7B), all instruction-tuned, all open-weight, all served via vLLM. The model-as-facet analysis — a core contribution — has df=2 for the model main effect. With 3 models, model×item estimates are dominated by pairwise contrasts; a single unusual model (Mistral, with notably lower accuracy) can drive the entire interaction. The 14B extension adds 2 models but in a separate analysis, not in the main crossed design. No API-served models, no models >14B in the main analysis, no architectural diversity (e.g., mixture-of-experts). This is the paper's most significant limitation: the "model-as-facet" claim requires substantially more models to be convincing for the community.

**W2. Hardware crossing is severely underpowered (Major).** Only 2 GPU types, with only 2 of 3 models completing the full design on the secondary GPU. The separability claim (Contribution 2) partly rests on this evidence. With 2 GPUs × 2 models, bootstrap CIs on hardware variance components are extremely wide. The 0.5% binary infra×method interaction is labeled as meeting the <1% threshold, but the confidence interval likely spans well above 1%. The paper says "preliminary" but then elevates separability to a main contribution.

**W3. Separability untested where it matters most (Major).** Reasoning benchmarks (GSM8K, MATH) used only bf16/fp16 — near-identical precisions where interaction is trivially small. The precision-related separability test on reasoning benchmarks is essentially vacuous (precision×temp <0.2% because bf16≈fp16, not because separability holds). The paper acknowledges this in Limitations but Contribution 2 ("infrastructure×methodology interactions are negligible") does not sufficiently qualify that this was only tested on MMLU under binary scoring. Separability on reasoning tasks remains genuinely open.

**W4. fp32 degradation is a software artifact, not a precision property (Moderate-Major).** The ~8pp fp32 degradation persists under `enforce_eager` and is shown by LayerCast to originate from vLLM's fp32 code path, not from numerical precision per se. This means the "precision" facet in the G-study is partly measuring a software bug/artifact. When fp32 is the level driving most of the precision×item variance (7.0% on MMLU), the interpretation of this variance component is confounded. The paper partially addresses this with LayerCast but doesn't fully resolve what "precision" means in the decomposition when one of its three levels is a software artifact rather than a meaningful numerical precision condition.

**W5. 200-item subsampling creates internal tension (Moderate).** The paper's central finding is that item selection dominates variance, yet all experiments use a single 200-item stratified subsample per benchmark. The resampling stability test shows SD=3.9pp for item_id share — substantial uncertainty. While the paper argues for interval reporting, headline numbers throughout (Tables 2, 4, 8) are point estimates from one draw. This is not fatal (the qualitative findings are robust across draws) but the presentation should foreground the uncertainty more consistently.

**W6. Large unexplained "other" variance on some benchmarks (Moderate).** The "other" category in Table 4 reaches 15.25% (ARC) and 16.3% (HellaSwag) — larger than several named components. This is not discussed. What interactions are lumped into "other"? If these are higher-order interactions, which ones? If they are artifacts of the reduced 2×2 design, this needs explanation. Readers cannot assess the decomposition's completeness without understanding this residual.

**W7. G-theory assumptions violated by binary data (Moderate).** Classical G-theory assumes continuous data. Binary (0/1) outcomes violate this, and the Bernoulli correlation (r=0.72 with p(1-p)) confirms ~50% of item variance is mechanical. The text-match parallel analysis helps, but binary scoring is the primary presentation throughout. Generalized G-theory for binary data (Brennan, 2001) is mentioned in Limitations as "a natural extension" — but if such methods exist, why not use them? This weakens confidence in the exact variance percentages, though likely not the rank ordering.

**W8. D-study assumptions may not match practice (Minor-Moderate).** The D-study recommendations (620 items for MMLU G≥0.90) assume 6 prompts and 6 seeds are averaged. Practitioners typically use 1 prompt and 1 seed. The paper states G<0.35 under this common practice but doesn't provide D-study projections for the 1-prompt, 1-seed scenario. How many items would be needed for G≥0.90 with 1 prompt and 1 seed? This would make the practical gap more concrete and actionable.

---

## 4. Questions for Authors

1. How sensitive are the model-as-facet variance estimates to removing one of the three models (leave-one-out)? If removing Mistral substantially changes the item_id/model×item ratio, the df=2 concern is not just theoretical.

2. Could you report D-study projections for the common-practice scenario (1 prompt, 1 seed, varying items only)? This would directly quantify what practitioners should expect.

3. What specific interactions constitute the "other" category in Table 4? The 15–16% on ARC/HellaSwag demands explanation.

4. The MATH entry for G≥0.80 in Table 10 shows "—" — is this because 200 items already exceeds G≥0.80 for MATH, or a data issue? (Given G_binary=0.18 at 200 items, this seems like it should have a value.)

---

## 5. Experiment Coverage Assessment

All 8 imagined experiments (exp-001 through exp-008) are represented in the paper:
- exp-001 (MMLU precision study) → Section 4.1, Tables 1–2 ✓
- exp-001b (Resampling stability) → Section 4.2, Table 3 ✓
- exp-002 (Multi-benchmark) → Section 4.3, Tables 4–6 ✓
- exp-003 (Multi-hardware) → Section 4.4, Table 7 ✓
- exp-004 (Comprehensive analysis) → Section 4.5, Tables 8–11 ✓
- exp-005 (14B models) → Section 4.6, Table 15 (Appendix) ✓
- exp-006 (Fine-tuning) → Section 4.7, Table 12 ✓
- exp-007 (LayerCast) → Section 4.8, Table 16 (Appendix) ✓
- exp-008 (MATH) → Section 4.9, Tables 13–14 (Appendix) ✓

Coverage is complete. Numerical results in the paper match the expected results from the experiment design. No imagined experiment is missing.

---

## 6. Minor Issues

- Table 4: MMLU column values are from exp-001 (3 prec × 3 temp) while other benchmarks use 2×2. The design asymmetry complicates direct comparison of precision-related components. The paper notes this but the table itself does not flag it.
- Several references are arXiv-only (Yuan et al. 2025, Mesting 2026). Mesting (2026) is the closest prior work and its publication status matters.
- Computational cost (~650 GPU hours total) is not explicitly reported in the paper. This would be useful for reproducibility.
- The paper has no figures in the main text (only tables). The signature figures described in the experiment design (stacked-bar decompositions, D-study curves, CI forest plots) would significantly improve readability and impact.
- Dehghani et al. (2021) "The benchmark lottery" is cited in the reference list but not referenced in the text.

---

## 7. Overall Assessment

**The paper tackles a genuinely important question** — whether variance sources in LLM evaluation interact or can be studied in isolation — using an appropriate framework at an impressive experimental scale. The three main findings are directionally supported, the methodological defenses are thorough, and the reporting is refreshingly honest.

**However, the claims outrun the evidence in critical ways.** The model-as-facet analysis (a core contribution) rests on 3 models with df=2 — far too few to credibly estimate model×item variance for the community. The separability claim is elevated to a main contribution but is only tested on MMLU under binary scoring with fp32 (a software artifact), and is entirely untested on reasoning benchmarks where it matters most. The hardware crossing has 2 GPUs × 2 models — insufficient for the confidence the paper projects.

**For a top ML venue (~25% acceptance rate):** The work is competent and the question is timely, but the gap between claim scope and evidence strength is too wide. The paper would benefit from: (a) at least 5–6 models in the main crossed design, (b) full-precision crossing on at least one reasoning benchmark, (c) a third GPU type, and (d) figures in the main text. In its current form, the contribution is incremental over Mesting (2026) — multi-benchmark and infrastructure crossing are extensions rather than fundamental advances.

**Score: 3 (Weak Reject).** Important question, solid framework choice, impressive scale, but insufficient model/hardware diversity for the claim scope and untested separability on reasoning tasks. Revisions addressing W1–W3 could move this to borderline accept.

---

## 8. Scores Summary

| Criterion | Score (1–6) | Notes |
|---|---|---|
| Novelty | 3.5 | Incremental over Mesting (2026); multi-benchmark + infra crossing are extensions |
| Soundness | 3 | G-theory application is correct; major gaps in evidence for two of three claims |
| Significance | 4 | Practical value of D-study budgets and separability test if claims were better supported |
| Clarity | 3.5 | Dense but well-structured; no figures hurts readability; "other" unexplained |
| Reproducibility | 4 | Design is well-specified; code/data availability not mentioned |
| **Overall** | **3** | **Weak Reject** |
