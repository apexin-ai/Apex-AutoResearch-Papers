---
dream_id: dream_20260520T185641
tier: best
overall_score: Weak Accept (4/6)
timestamp: 2026-05-20T19:54:18.620914+00:00
---

## Reviewer 1 (R1): Methods and Experiments

### Summary
This paper systematically evaluates whether English-trained correctness probes on internal LLM representations transfer cross-lingually, across 3 architectures (Qwen3-235B, Llama 4 Scout, Gemma 4 31B), 20-52 languages, and 5 transfer conditions. It discovers a depth-transferability Pareto frontier, proposes CaCLR (a joint calibration-consistency objective), performs difficulty-capability decomposition, and extends the correctness-confidence orthogonality finding to multilingual settings.

### Strengths

**S1. Ambitious and well-structured experimental scope.** 10 experiment plans covering 3 architectures, up to 52 languages, multiple benchmarks, and systematic ablations. The causal chain (discovery → analysis → method → mechanism) is logically coherent. The coverage of MoE vs Dense architectures strengthens generalizability claims.

**S2. Principled negative results honestly reported.** The consistency loss being inert (sweeping beta over 3 OOM changes AUROC <0.3pp), mean-shift failing entirely, and CaCLR never beating linear projection on cross-benchmark evaluation are all valuable findings for the community. The paper does not oversell.

**S3. Comprehensive baseline coverage.** Five transfer conditions (zero-shot, mean-shift, linear projection, few-shot 25/100, CaCLR) provide a fair comparison landscape. The INT8 validation ablation (cosine 0.994, 0.3pp AUROC difference) proactively addresses quantization concerns.

**S4. The difficulty-capability decomposition (Plan 004) is methodologically interesting.** Projecting out IRT difficulty and showing this *hurts* transfer by 1.3-1.4pp is a counterintuitive and informative result that challenges the assumption of clean separability.

### Weaknesses

**W1. The Pareto frontier claim is architecture-dependent to the point of undermining universality.** The paper reports rho=0.41 (Qwen3), 0.22 (Llama4), 0.48 (Gemma4). A rank correlation of 0.22 explains <5% of variance and is barely meaningful. Claiming a "Pareto frontier" when the relationship is this noisy on one of three architectures weakens Claim 1 substantially. The paper should acknowledge this is a *tendency* in some architectures rather than a universal structural property.

**W2. CaCLR's consistency loss is inert — this fundamentally undermines Claim 3.** The paper's proposed method contribution is CaCLR (L_BCE + alpha*L_SB-ECE + beta*L_consistency). If sweeping beta over 3 orders of magnitude changes AUROC by <0.3pp, and *removing* it improves by 0.2pp, then CaCLR reduces to L_BCE + L_SB-ECE, which is simply calibration-aware probe training — not a novel cross-lingual alignment method. The "consistency" component that was supposed to be the differentiator from linear projection is doing nothing. Furthermore, "CaCLR never beats linear projection" on cross-benchmark (Result 7) means the method contribution is essentially negative.

**W3. No confidence intervals or significance tests on the key comparisons.** Effect sizes like Cohen's d=0.18 for probe complexity and the 1.3-1.4pp decomposition degradation are small. Without bootstrap CIs or paired tests across the 19/52 languages, it is impossible to assess whether these effects are reliably non-zero. The MLP transfer penalty of -0.2 to -0.4pp is tiny and may be noise.

**W4. The "parallel activations" requirement for CaCLR is underspecified.** The consistency loss requires comparable EN and non-EN activations. How are these obtained? Translated GlobalMMLU items? If so, how is translation quality controlled? Does it require parallel corpora at inference time? This has major practical implications for the "zero target-language labels" claim — you still need parallel *inputs*, which may be harder to obtain than 25-100 labeled examples.

**W5. Extended 52-language evaluation (Plan 009) shows 23.5% pass rate and 0% for very-low-resource.** This result significantly undermines the practical value proposition. If the method works only for languages that already have reasonable LLM coverage, the incremental value over simply collecting a few dozen labeled examples per language is questionable.

### Questions for Authors

Q1. What exactly are "parallel activations" for L_consistency? Are these from the same MCQA items machine-translated into each language (as in GlobalMMLU)? If so, does CaCLR require access to the evaluation benchmark's translations at training time — creating a form of test-set leakage?

Q2. For the Pareto frontier on Llama 4 Scout (rho=0.22, non-monotonic at layers 20-28), can you provide bootstrap confidence intervals on the rank correlation? With only 12 data points, the sampling uncertainty may be substantial.

Q3. The paper claims "projecting out difficulty hurts transfer by 1.3-1.4pp" — but over how many language-layer combinations? Is this statistically significant by a paired test? What is the variance across the 10 languages x 8 layers = 80 conditions?

Q4. Temperature scaling T values (5-6) are extremely high, implying massive overconfidence in the raw probes. Was T optimized on held-out data or the test set? If the latter, ECE numbers are unreliable.

Q5. How sensitive is CaCLR to the choice of alpha? You report beta is inert, but what about alpha (the SB-ECE weight)?

### Minor Issues

M1. Table 5 reports "Pareto frontier coherence" across 3 architectures but rho values of 0.41, 0.22, 0.48 do not constitute "coherence" in any standard sense. Revise the table title.

M2. The 52-language extension uses only Qwen3 (from context). Cross-architecture validation at this scale would strengthen the claim.

M3. "Orthogonality persists across 20 languages (mean cosine 0.072)" — this is interesting but somewhat expected given the finding is architectural, not language-specific. The novelty here is incremental over Miao & Ungar.

M4. The probe complexity finding (MLP +1pp EN, -0.2 to -0.4pp transfer) with Cohen's d=0.18 is a very small effect. Consider whether this table adds value or could move to supplementary.

M5. The paper uses GlobalMMLU, Belebele, and MMLU-ProX — all MCQA. Generalization beyond MCQA remains entirely open.

### Score: 4 (Weak Accept)

**Justification:** The paper addresses a timely and important question (does probe-based calibration generalize multilingually?) with thorough experimentation across architectures and languages. The systematic characterization is valuable regardless of whether CaCLR succeeds as a method. However, the method contribution (CaCLR) is effectively negative — the consistency loss is inert and the method never beats linear projection cross-benchmark. The Pareto frontier is weak on 1/3 architectures (rho=0.22). These issues reduce the paper from a strong method+discovery paper to primarily a diagnostic/characterization paper with negative results. For a top venue, the paper needs either (a) a working method that actually shifts the frontier, or (b) explicit reframing as a diagnostic study with the CaCLR negative result as a contribution. Currently it sits uncomfortably between these framings. The breadth of experiments, honest reporting of negative results, and field-level significance of answering "does this work multilingually?" push it toward acceptance at a venue like EACL, but the weak method contribution keeps it below the bar for a top ML venue.
