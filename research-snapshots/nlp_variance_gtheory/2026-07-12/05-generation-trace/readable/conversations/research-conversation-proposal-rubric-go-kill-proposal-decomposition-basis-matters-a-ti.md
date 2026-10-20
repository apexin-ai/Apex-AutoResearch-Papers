# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Decomposition Basis Matters: A Ti

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/5ccfee60-e993-4fc7-ae75-fd441b563a99.jsonl`
- **Structured JSON:** [`0443b468946fc13eb7d2.json`](../../sessions/04/0443b468946fc13eb7d2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T05:55:32.574Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T05:55:32.574Z",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Decomposition Basis Matters: A Tiered Empirical Study of Error-Taxonomic vs. Orthogonality-Enforced vs. Causal Reward Decomposition for PRM Hackability Resistance\n\n## Description\nWe present the first systematic empirical study of how decomposition basis and coverage breadth jointly affect PRM hackability resistance, organized as a tiered experimental program with staged evaluation and capacity controls. Our two central questions: (1) Does the CHOICE of decomposition basis matter — specifically, does grounding multi-dimensional supervision in a systematic error taxonomy outperform orthogonality-enforced, quality-dimension, and causal alternatives? (2) How does coverage breadth (number of supervised error dimensions) affect hackability, and does hacking shift to uncovered dimensions as theory predicts? We introduce ETA-PRM (Error-Type-Aware PRM), a multi-head architecture with up to 13 ErrorAtlas-aligned error-type heads plus a residual head. The guaranteed Tier 1 deliverable compares four decomposition approaches (ETA error-taxonomic, ODIN data-driven orthogonal, single-head, PathFinder trajectory-level) across a 4-level coverage ablation (2→6→13→13+residual heads), with Random-N capacity controls (N=2,6,13) at each coverage level to disentangle coverage breadth from model capacity. The critical three-way comparison — ETA-PRM-6 (error-type labels) vs. ODIN-6-orthogonal (random labels + orthogonality loss) vs. Random-6 (random labels, no orthogonality) — isolates whether semantic grounding, orthogonality enforcement, or raw capacity drives hackability resistance. Hackability is measured through a staged pipeline motivated by Tiwari et al.'s finding that static perturbation tests weakly predict RL-based exploitation: Stage 1 applies PRM-BiasBench perturbations for surface profiling and GOH sensitivity analysis, Stage 2 traces Best-of-N overoptimization curves as an intermediate proxy, and Stage 3 runs full GRPO exploitation on core variants with 3 seeds and paired bootstrap confidence intervals. The Grounded Orthogonality Hypothesis is tested via pre-registered, falsifiable predictions: comparable overall debiased CKA distance but divergent selective perturbation sensitivity (ETA-PRM heads sensitive to matching perturbation types vs. ODIN heads showing uniform sensitivity). Tier 2 extends to CausalRM and DRM baselines, cross-scale robustness verification (Qwen2.5-Math-1.5B-Instruct backbone), and MO-GRPO robustness checks to rule out RL-algorithm-specific exploitation artifacts; Tier 3 adds ThinkPRM comparison, Socratic-PRMBench reasoning-pattern evaluation, and full mechanistic analysis. All evaluation is on mathematical reasoning, explicitly acknowledged as domain-specific validation with methodology designed for cross-domain extension. This is the first controlled study varying both decomposition basis and coverage breadth with capacity controls, staged hackability evaluation, pre-registered mechanistic predictions, and statistical rigor.\n\n## Core Problem\nMulti-dimensional PRM supervision is now a recommended anti-hacking strategy (PCH Section 6.1), with a growing zoo of decomposition schemes operating on fundamentally different bases: ODIN decomposes along a known confounder (length) with explicit orthogonality loss; DRM decomposes along quality dimensions via external scoring models; DG-PRM uses dynamically extracted criteria; CausalRM separates causal from non-causal embedding factors; BNRM uses sparse non-negative latent factors; HRM decomposes along temporal hierarchy (individual vs. consecutive steps at multiple granularities); and IR³ performs post-hoc SAE-based decomposition of already-trained reward signals. The critical unanswered question: does the CHOICE of decomposition basis matter for hackability resistance, or is orthogonality enforcement alone sufficient? And how does coverage breadth (number of supervised error dimensions) interact with basis choice? Recent theoretical work (arXiv:2603.28063) proves that hacking concentrates on uncovered dimensions with computable severity, while empirical work (arXiv:2605.12474) confirms that rubric-based RL is hackable precisely when failure modes go unspecified. However, prior experimental designs in this space suffer from two methodological gaps: (1) scope overload — attempting to simultaneously answer too many questions yields shallow results, and (2) capacity confounding — coverage ablations that vary both the number of supervised dimensions and model parameter count cannot cleanly attribute hackability differences to coverage breadth versus added capacity. We address both the scientific question and these methodological challenges: a tiered experimental program with explicit priority levels guarantees a focused core comparison (4 decomposition bases × 4 coverage levels, with random-label capacity controls) as a first-class deliverable, while permitting principled extension to additional paradigms and cross-scale robustness verification.\n\n## Opportunity\nThree converging developments create a narrow window for this study. First, ErrorAtlas (arXiv:2601.15812) provides a validated 17-category error taxonomy (92% validation accuracy across 35 datasets and 83 models) that enables principled coverage ablation with known category distributions — the five most prevalent categories (Missing Required Element 15.6%, Specification Misinterpretation 11.5%, Logical Reasoning Error 9.1%, Incorrect Identification 9.0%, Computation Error 8.5%) account for ~54% of all reasoning benchmark errors. Second, Tiwari et al.'s (arXiv:2603.06621) three-tiered hackability framework reveals a critical methodological insight: static perturbation tests have WEAK correlation with RL-based exploitation — models passing surface-level style-invariance checks (reward changes <0.1) diverge dramatically under optimization pressure (43% of RL reward gains are stylistic shortcuts). This motivates our staged evaluation pipeline that escalates from cheap inference-only probes through Best-of-N overoptimization curves to full RL stress-testing, rather than committing expensive RL runs to all variants. Third, the simultaneous availability of orthogonal decomposition approaches (ETA error-taxonomic, ODIN data-driven orthogonal, PathFinder trajectory-level, CausalRM causal, DRM distributional, HRM temporal-hierarchical, IR³ post-hoc interpretive) means the comparison can be conducted before the field converges on a single paradigm. Fourth, MO-GRPO (arXiv:2509.22047) provides a principled RL-time normalization method that prevents GRPO from preferentially exploiting high-variance reward dimensions, enabling us to disentangle PRM-level decomposition effects from RL-algorithm-specific exploitation artifacts. The missing experiment: a controlled comparison with scope discipline — tiered priorities, staged evaluation, capacity controls, and statistical rigor — varying both decomposition basis and coverage breadth under standardized hackability protocols.\n\n## Landscape\n**Orthogonality-enforced decomposition.** ODIN (arXiv:2402.07319, ICML 2024) trains two linear heads on a shared backbone — one correlated with response length, one decorrelated — using ranking + length-correlation + orthogonality loss on projection weights. Nearly eliminates length-reward correlation across PPO and ReMax, evaluated via Pareto front analysis across hyperparameter sweeps. Addresses only a single known confounder (length); does not generalize to multi-faceted attacks. **Quality-dimension decomposition.** DRM (arXiv:2510.11457) computes Confidence (log-probs), Relevance (NLI reranker), and Coherence (Nemotron-70B ORM) as three external signals weighted 0.1/0.2/0.7. Reduces flawed-but-correct reasoning traces but dominated by ORM dimension. Note: DRM's reliance on external scoring models (including a 70B ORM) makes it architecturally distinct from multi-head decomposition approaches that share a single backbone — it is better characterized as a model-ensemble paradigm than a multi-head architecture, and comparisons should be interpreted as contrasting decomposition paradigms rather than head architectures. **Dynamic-criteria decomposition.** DG-PRM (arXiv:2507.17849, ACL 2025) automatically extracts hierarchical criteria via LLM judge comparisons and applies Pareto dominance, reaching 76.5% on PRMBench with 30% training efficiency gains, but without adversarial evaluation. **Representation-level decomposition.** CausalRM (arXiv:2601.21350, ICML 2026) uses a variational encoder with gradient reversal to separate causal from non-causal embedding factors, achieving 5–15% robustness improvement on sycophancy and length-bias probes. **Latent-factor decomposition.** BNRM (arXiv:2602.10623) integrates non-negative factor analysis into Bradley-Terry preference models using Gamma priors and Weibull variational distributions, achieving 93.6% on RewardBench (+3.2% over BT baselines), but operates at outcome-reward level. **Hierarchical temporal decomposition.** HRM (arXiv:2503.13551) evaluates both individual and consecutive reasoning steps at fine and coarse granularity, with Hierarchical Node Compression (HNC) for data augmentation. Addresses reward hacking through multi-level temporal coherence evaluation. Represents an orthogonal axis (temporal hierarchy) to error-category decomposition, and is tested on PRM800K, MATH500, and GSM8K. **Post-hoc interpretive decomposition.** IR³ (arXiv:2602.19416) introduces Contrastive Inverse Reinforcement Learning (C-IRL) to reconstruct implicit reward functions from post-alignment behavioral shifts, then decomposes the reconstructed reward via sparse autoencoders (SAEs) into interpretable features operating on the reward network's penultimate activations. Achieves 0.89 correlation with ground-truth rewards and >90% precision in identifying hacking signatures. Four surgical mitigation strategies (clean reward optimization, adversarial shaping, constrained optimization, feature-guided distillation) reduce hacking while maintaining capabilities within 3% of the original model. Critically, IR³ operates post-hoc on already-trained models — it reverse-engineers internalized objectives rather than building decomposition into the PRM architecture. This represents a fundamentally different decomposition paradigm (interpretive vs. architectural) that is complementary to our multi-head approach: IR³ could analyze what objectives ETA-PRM heads actually learn. **Error-type supervision.** PathFinder-PRM (arXiv:2505.19706) decomposes into math and consistency error dimensions, achieving PRMScore 67.7 on PRMBench with 3× data efficiency. ErrorAtlas (arXiv:2601.15812) provides 17 top-level error categories across 35 datasets and 83 models with 92% validation accuracy, revealing that ~44% of errors in math benchmarks have weak reasoning orientation. **RL-time reward decorrelation.** RDPO (arXiv:2605.13641) applies Magnitude-Aware Quantile normalization and Mahalanobis whitening within active reward subspaces during policy gradient updates — this is RL-TIME decorrelation, not reward-model-time decomposition. Applied to LongCat-Flash post-training (+4.25% IFEval, +10.3% ArenaHard-Hard). Complementary to reward-model-level decomposition — could compose with any PRM decomposition during downstream RL. **Multi-objective RL normalization.** MO-GRPO (arXiv:2509.22047) addresses reward hacking in GRPO by normalizing each reward dimension independently (per-objective z-score) before aggregation, rather than GRPO's default of normalizing after aggregation. This prevents GRPO from preferentially optimizing high-variance reward dimensions while ignoring low-variance ones. Demonstrated to eliminate reward hacking artifacts in machine translation (vanilla GRPO generated 68.7% non-target-language text exploiting readability metrics; MO-GRPO maintained both quality dimensions). Directly relevant to our Stage 3 methodology: when multi-head PRMs produce per-dimension scores, vanilla GRPO may introduce dimension-exploitation artifacts that confound decomposition-basis comparisons. MO-GRPO provides a robustness check isolating PRM-level decomposition effects from RL-algorithm-specific exploitation. **Hackability evaluation.** Tiwari et al. (arXiv:2603.06621) introduce a three-tiered diagnostic framework: (1) static perturbation via PRM-BiasBench (8 perturbation types, inference-only — reveals fluency-logic dissociation but weakly predicts RL outcomes), (2) adversarial optimization (gradient-based, 1000 iterations), (3) RL-induced hacking (GRPO on Qwen2.5-1.5B-Instruct against AIME). Critical finding: Tier 1 and Tier 3 weakly correlate — models certified as style-invariant under static perturbation diverge dramatically under optimization pressure. **Reasoning-pattern-specific evaluation.** Socratic-PRMBench (arXiv:2505.23474) evaluates PRMs across 6 systematic reasoning patterns (Transformation, Decomposition, Regather, Deduction, Verification, Integration) with 20 fine-grained error types nested hierarchically under these patterns, comprising 2995 reasoning paths. Key finding: Qwen2.5-Math-PRM-7B achieves 90.8% accuracy on correct steps but only 42.9% on error steps, with marked deficiencies on Decomposition and Redundancy errors. Complements PRMBench and ProcessBench by testing reasoning-pattern sensitivity — directly relevant to our analysis of whether error-type-specific heads improve detection across diverse reasoning patterns. **Coverage theory.** arXiv:2603.28063 proves under five minimal axioms that hacking concentrates on uncovered dimensions with a computable distortion index. arXiv:2605.12474 empirically confirms this for rubric-based RL. **Other anti-hacking approaches.** ThinkPRM (arXiv:2504.16828, TMLR 2026) achieves 86.5% F1 on ProcessBench with ~1% of PRM800K data via generative verification CoT. GenPRM (arXiv:2504.00891, AAAI 2026) adds code-integrated verification. APRM (arXiv:2511.22888) uses adversarial generator–PRM game training (+3.4pp). CRA (arXiv:2508.04216) mitigates hacking via causal backdoor correction. PURE (arXiv:2504.15275, NeurIPS 2025) reduces hacking via min-form credit assignment. CROME (arXiv:2506.16507) uses causal rubrics (+5.4% RewardBench). No prior work systematically compares decomposition bases AND coverage breadth for hackability resistance with capacity controls, staged evaluation, and statistical rigor.\n\n## Approach\nWe conduct a controlled comparison of PRM decomposition schemes for hackability resistance, organized as a tiered experimental program with staged evaluation. Two interacting variables: decomposition BASIS (what dimensions to decompose along) and coverage BREADTH (how many dimensions). Our primary system is ETA-PRM (Error-Type-Aware PRM), a multi-head architecture with ErrorAtlas-aligned error-type classification heads.\n\n**TIERED EXPERIMENTAL PROGRAM**\n\n**Tier 1 (Guaranteed Deliverable).** Core comparison answering both research questions with 4 decomposition approaches, 4 coverage levels, and capacity controls. Baselines: (a) ETA-PRM coverage ablation: ETA-PRM-2 / ETA-PRM-6 / ETA-PRM-13 / ETA-PRM-13+R, where each head detects specific ErrorAtlas error categories. ETA-PRM-6 heads: Computation Error, Logical Reasoning Error, Specification Misinterpretation, Factual Error, Output Formatting Error, Missing Required Element. (b) ODIN-6-orthogonal: 6 heads with random (non-error-type-grounded) labels + explicit pairwise cosine orthogonality loss between head projection weights — the critical control isolating semantic grounding from orthogonality enforcement. If ODIN-6-orthogonal matches ETA-PRM-6 on hackability, error-type grounding adds no value beyond orthogonality. (c) Single-head PRM (capacity-matched, zero-decomposition baseline). (d) PathFinder-PRM-style 2-head (math, consistency — minimal decomposition baseline).\n\n**Capacity Controls (addressing coverage-capacity confound).** Each additional head adds a linear projection layer, so the coverage ablation (2→6→13→13+R) changes both coverage breadth and parameter count simultaneously. To disentangle these factors, we include Random-N controls at each coverage level: Random-2, Random-6, Random-13 — architecturally identical to ETA-PRM-N but with randomly assigned error-type labels (each step randomly assigned to one of N categories). These controls have the same parameter budget as ETA-PRM-N at each level but lack semantic grounding. The experimental logic:\n- ETA-PRM-N vs. Random-N at each N: isolates the effect of semantic grounding (error-type labels vs. random labels) at matched parameter budget.\n- Random-2 vs. Random-6 vs. Random-13: isolates the effect of pure capacity (more heads/parameters) without meaningful coverage signal.\n- ODIN-6-orthogonal vs. Random-6: isolates the effect of explicit orthogonality enforcement on random labels.\n- ETA-PRM-6 vs. ODIN-6-orthogonal vs. Random-6: the three-way comparison isolates semantic grounding, orthogonality enforcement, and capacity respectively.\nIf Random-13 shows comparable hackability resistance to Random-2, capacity alone does not explain coverage benefits. If ETA-PRM-N consistently outperforms Random-N, semantic grounding matters beyond added capacity. We additionally report total trainable parameter counts for each variant and include a regression analysis of hackability metrics against parameter count to quantify the capacity contribution.\n\nInterpretability diagnostic: debiased CKA similarity (using unbiased U-statistics for HSIC, following Murphy et al. 2024) between head representations, with pre-registered GOH predictions (see below).\n\n**Tier 2 (Strong-to-Have).** Extends decomposition basis comparison and robustness checks: (e) CausalRM-style gradient-reversal baseline (variational encoder splitting embeddings into causal/non-causal factors). (f) DRM-style 3-dimension scoring pipeline (Confidence/Relevance/Coherence). Note: DRM relies on external scoring models (including an NLI reranker and Nemotron-70B ORM), making it architecturally distinct from multi-head approaches sharing a single backbone. This comparison is informative about decomposition paradigms (external-signal ensemble vs. multi-head architecture vs. representation-level separation) rather than head architecture variants, and results should be interpreted accordingly. (g) Cross-scale robustness check: Qwen2.5-Math-1.5B-Instruct backbone for ETA-PRM-6 and ODIN-6-orthogonal (the core comparison), evaluated with Stages 1–2 of the hackability pipeline. This addresses the single-backbone limitation: if 7B results do not replicate at 1.5B, it may indicate that 7B capacity is necessary for 6 independent error-type heads to learn meaningfully distinct representations, which is itself informative. If results transfer, it strengthens generalizability. The 1.5B scale is chosen because: (i) Qwen2.5-Math-1.5B-Instruct is publicly available and has been validated as a PRM backbone (HuggingFaceH4/Qwen2.5-Math-1.5B-Instruct-PRM-0.2 trained on PRM800K), (ii) the 1.5B-to-7B ratio (~5×) represents a meaningful scale difference, and (iii) 1.5B training is ~4× cheaper than 7B, keeping the robustness check within budget. (h) MO-GRPO robustness check on core pair (ETA-PRM-6 vs. ODIN-6-orthogonal): vanilla GRPO may preferentially exploit high-variance reward dimensions (as demonstrated by MO-GRPO authors: vanilla GRPO generated 68.7% non-target-language text exploiting readability metrics). By re-running Stage 3 with MO-GRPO's per-objective normalization on the core comparison, we verify that decomposition-basis effects are robust to RL algorithm choice and rule out GRPO-specific dimension-exploitation artifacts. If ETA-PRM-6 outperforms ODIN-6-orthogonal under vanilla GRPO but not under MO-GRPO, it would suggest the advantage stems from exploitable variance asymmetries rather than genuine semantic alignment. Tier 2 variants (e)–(f) evaluated with Stages 1–2 of hackability pipeline; full RL only if Tier 1 results warrant.\n\n**Tier 3 (Nice-to-Have).** Extended analysis: (i) ThinkPRM-7B comparison (inference-only, representing implicit decomposition via generative reasoning). (j) Full mechanistic analysis: linear probing of head representations, attack-surface alignment analysis (see GOH section below). (k) Architectural controls: multi-task single-output (controls for gradient regularization), single-head with auxiliary losses. (l) Socratic-PRMBench evaluation on Tier 1 variants to assess reasoning-pattern-specific error detection across the 6 systematic reasoning patterns (Transformation, Decomposition, Regather, Deduction, Verification, Integration) and 20 fine-grained error types.\n\n**SINGLE-BACKBONE LIMITATION ACKNOWLEDGMENT.** All primary experiments (Tier 1) use Qwen2.5-Math-7B-Instruct as the backbone. This choice is justified by: (a) Qwen2.5-Math is the most widely used PRM backbone in the current literature (Tiwari et al., RLHFlow, etc.), enabling direct comparability; (b) the 7B scale provides sufficient representation capacity for up to 13 independent heads while remaining computationally tractable for multi-seed RL experiments. However, results may be backbone-specific: the 7B architecture's representation geometry may particularly favor (or disfavor) certain decomposition approaches, and findings may not transfer to other model families (Llama, Mistral) with different attention patterns and representation structures. The Tier 2 cross-scale check (1.5B) partially addresses scale sensitivity within the Qwen family. Full cross-family robustness (e.g., Llama-3.1-8B, Mistral-7B backbones) is an explicit limitation and priority for follow-up work.\n\n**STAGED HACKABILITY EVALUATION**\n\nMotivated by Tiwari et al.'s finding that Tier 1 (static) tests weakly predict Tier 3 (RL-based) hackability, we adopt a staged pipeline that escalates cost and informativeness.\n\n*Stage 1 — Static Perturbation (all variants, ~60 A100-hours):* PRM-BiasBench protocol with 8 perturbation types (rephrasing, verbosity increase/decrease, within-step reordering, question shuffling, numerical perturbation, reasoning hallucination, question removal). Used for surface-level vulnerability profiling, NOT as definitive hackability measure. Explicitly reports the acknowledged weak correlation with Stage 3. Additionally serves as the input for GOH selective-sensitivity analysis (see pre-registered predictions below).\n\n*Stage 2 — Best-of-N Overoptimization (Tier 1 + selected Tier 2 variants, ~250 A100-hours):* Best-of-N sampling with N ∈ {1, 4, 16, 64, 256} on MATH-500. Track reward-accuracy gap as N increases. Overoptimization onset N* defined as the N where accuracy first declines while reward continues increasing. No RL training required — avoids PPO/GRPO instability while providing meaningful hackability signal. Reports: reward-accuracy gap at each N, overoptimization onset N*, Pareto efficiency curves.\n\n*Stage 3 — Full RL Exploitation (Tier 1 variants only, ~700 A100-hours):* Primary: GRPO (following Tiwari et al. protocol — chosen over PPO for simplicity, lower instability, and direct comparability) training Qwen2.5-1.5B-Instruct against frozen PRM on AIME-style problems. Seed protocol: 3 seeds for core comparison (ETA-PRM-6 vs. ODIN-6-orthogonal vs. single-head PRM), enabling paired bootstrap confidence intervals and Wilcoxon signed-rank tests; 1 seed for PathFinder-2D, Random-6 (capacity control), and coverage ablation sweep (providing directional signal within compute constraints). Tier 2 robustness: MO-GRPO (per-objective normalization) on ETA-PRM-6 vs. ODIN-6-orthogonal only (1 seed each, ~100 A100-hours), verifying decomposition-basis effects are not GRPO-specific exploitation artifacts. Statistical rigor: paired bootstrap 95% CIs on reward-accuracy gap, Wilcoxon signed-rank tests for pairwise comparisons, Cohen's d effect sizes reported alongside p-values. For each coverage level, analyze which ERROR TYPES the GRPO policy learns to exploit — testing the prediction from arXiv:2603.28063 that exploitation concentrates on uncovered categories.\n\n**PRE-REGISTERED GROUNDED ORTHOGONALITY HYPOTHESIS (GOH) PREDICTIONS**\n\nThe GOH predicts that error-type grounding achieves orthogonality in attack-surface-aligned feature subspaces rather than arbitrary orthogonal directions. To make this hypothesis falsifiable, we pre-register four specific predictions with concrete metrics and thresholds:\n\n*Prediction 1 (Comparable overall orthogonality):* Average pairwise debiased CKA distance between head intermediate representations will be comparable for ETA-PRM-6 and ODIN-6-orthogonal: |ΔCKA_avg(ETA-6, ODIN-6)| < 0.10. Both should be substantially more orthogonal than Random-6 (no orthogonality enforcement): CKA_avg(Random-6) > CKA_avg(ETA-6) + 0.05 AND CKA_avg(Random-6) > CKA_avg(ODIN-6) + 0.05. (Debiased CKA using unbiased U-statistics for HSIC to avoid inflated similarity in high-dimensional, moderate-sample regimes.)\n\n*Prediction 2 (Selective perturbation sensitivity):* For each ETA-PRM-6 head h_i corresponding to error type e_i, we measure the perturbation-type-specific reward change Δr(h_i, p_j) for each PRM-BiasBench perturbation type p_j. Construct a 6×8 head-by-perturbation sensitivity matrix S. GOH predicts diagonal dominance: for semantically matched head-perturbation pairs (Computation Error ↔ numerical perturbation, Logical Reasoning Error ↔ reasoning hallucination, Specification Misinterpretation ↔ question shuffling, Output Formatting Error ↔ rephrasing, Missing Required Element ↔ question removal), the matched sensitivity exceeds the median unmatched sensitivity by a factor of ≥1.5 for at least 4 of the 5 matched pairs. ODIN-6-orthogonal heads will show uniform sensitivity patterns — no matched pair exceeds the median unmatched by a factor of ≥1.5 for more than 1 of 5 pairs (since ODIN heads have no semantic alignment with perturbation types).\n\n*Prediction 3 (Attack-surface alignment under RL exploitation):* In Stage 3 GRPO exploitation, the error categories that the RL policy learns to exploit (measured by per-category reward-accuracy gap divergence) will correlate with the categories NOT covered by the PRM heads. For ETA-PRM-6 vs. ETA-PRM-13, exploitation should shift to uncovered categories (Spearman ρ > 0.5 between category coverage status and exploitation severity).\n\n*Falsification criteria:* (a) If ETA-PRM-6 heads show LESS overall orthogonality than Random-6 (CKA_avg for ETA-6 significantly higher than Random-6), the grounding-induces-orthogonality component of GOH is refuted. (b) If the sensitivity matrix shows no diagonal dominance — fewer than 3 of 5 matched pairs exceed the 1.5× threshold — the attack-surface-alignment component of GOH is refuted, and error-type labels do not create semantically meaningful head specialization. (c) If both (a) and (b) fail, GOH is comprehensively refuted: error-type grounding provides neither natural orthogonality nor attack-surface alignment. All CKA analyses will use debiased estimators and include random-data baselines following best practices from Murphy et al. (2024).\n\n**ANNOTATION PILOT STUDY**\n\nBefore full dataset construction, a 2000-step pilot study addresses annotation quality concerns at 13 categories. Design: stratified sampling from PRM800K covering diverse problem types and difficulty levels. Measurements: (i) per-category survival rate at 0.8 confidence threshold using Qwen3-32B as annotator; (ii) inter-annotator agreement (Cohen's κ) between Qwen3-32B and Claude Sonnet 4 on full 2000 steps, plus human expert agreement on 200-step subsample; (iii) per-category confusion matrices identifying systematic misclassifications; (iv) category frequency distribution to estimate imbalance severity.\n\nAdaptive thresholding: if pilot reveals <50% survival rate at 0.8 threshold for specific categories (likely for rare types like Naming/Symbol Error, Unit Conversion Error), lower threshold to 0.7 for those categories to prevent data starvation. Category-balanced sampling: oversample steps from problem types likely to elicit rare error categories (e.g., physics word problems for unit conversion, competition problems for specification misinterpretation). All coverage ablation results will report effective training examples per category alongside hackability metrics, ruling out the data-quantity confound.\n\n**FULL ANNOTATION (post-pilot).** Re-annotate ~400K steps from PRM800K and RLHFlow trajectories with hierarchical multi-dimensional error labels using Qwen3-32B with category-adaptive confidence thresholds determined by pilot. Apply noise-aware iterative training (NAIT) from arXiv:2601.12748 to refine labels where model predictions diverge from annotations.\n\n**ARCHITECTURE.** ETA-PRM extends a Qwen2.5-Math-7B-Instruct backbone with K classification heads detecting specific ErrorAtlas error categories. Per-type error probabilities aggregated via learned attention-based fusion into step-correctness score. A residual head (at K=13+R) captures error signal not covered by K specific heads. Head-balancing via uncertainty-weighted multi-task loss (Kendall et al.) prevents dominant-category heads from suppressing rare-category learning. Each head consists of a linear projection from the backbone's hidden dimension to a head-specific intermediate dimension, followed by a classification layer. For Random-N capacity controls, architecture is identical but training labels are randomly assigned.\n\n**ACCURACY EVALUATION.** ProcessBench, PRMBench, MATH-500 best-of-N. Supplemented with Socratic-PRMBench (Tier 3) to assess reasoning-pattern-specific detection across 6 patterns and 20 fine-grained error types, testing whether error-type-specific heads improve detection of reasoning-pattern-specific errors (e.g., whether Logical Reasoning Error heads improve Deduction pattern detection). Report alongside hackability metrics to assess accuracy–hackability trade-off.\n\n**MECHANISTIC ANALYSIS (CKA in Tier 1; full analysis in Tier 3).** Tier 1 test: debiased CKA similarity between head intermediate representations for ETA-PRM-6 vs. ODIN-6-orthogonal vs. Random-6, with pre-registered GOH predictions as specified above. Tier 3 extension: linear probing (which input features drive each head?) and attack-surface alignment (selective sensitivity to matching perturbation types, extending the Stage 1 sensitivity matrix analysis).\n\n**DOMAIN-SPECIFICITY ACKNOWLEDGMENT.** All evaluation is on mathematical reasoning (MATH-500, AIME, ProcessBench, PRMBench). Justified because: (a) ErrorAtlas taxonomy is best validated for math reasoning, (b) PRM800K provides the largest process-level supervision dataset, (c) math permits verifiable ground truth for hackability measurement. Generalizability argument: ErrorAtlas taxonomy is domain-general (17 categories derived from 35 datasets spanning math, code, dialogue, general QA), so the experimental methodology and tiered evaluation framework transfer directly even if specific hackability findings may be domain-dependent. Future work: extend to code generation (execution-based verification) and dialogue (human preference ground truth).\n\n## Resource Estimate\n{'tier_1_guaranteed': {'gpu_hours': '~1450 A100-hours (50h annotation pilot, 100h full annotation, 400h PRM training for 4 decomposition baselines × 4 coverage levels, 120h Random-N capacity controls training (3 variants: Random-2/6/13), 60h Stage 1 static evaluation for all variants including capacity controls, 250h Stage 2 Best-of-N for Tier 1 variants, 400h Stage 3 GRPO with 3 seeds on core + 1 seed on secondary and capacity controls, 70h CKA + GOH analysis)', 'timeline': '4.5–5.5 months (2–3 weeks pilot + annotation, 7 weeks training including capacity controls, 3 weeks Stage 1+2 evaluation, 4 weeks Stage 3 GRPO, 2–3 weeks analysis + writing)', 'estimated_gpu_cost': '$2900 (A100 at ~$2/hr)'}, 'tier_1_plus_2': {'gpu_hours': '~2050 A100-hours (Tier 1 + 250h CausalRM/DRM training, 80h 1.5B cross-scale training, 40h 1.5B Stages 1–2 evaluation, 100h MO-GRPO robustness check on core pair, 130h Stage 1–2 evaluation on remaining Tier 2 variants)', 'timeline': '5.5–7 months', 'estimated_gpu_cost': '$4100'}, 'full_all_tiers': {'gpu_hours': '~2500 A100-hours (Tiers 1–2 + 200h ThinkPRM inference, 100h Socratic-PRMBench evaluation, 100h full mechanistic analysis, 50h architectural controls)', 'timeline': '7–8 months', 'estimated_gpu_cost': '$5000'}, 'human_in_loop': {'claude_api_cost': '$800 (annotation pipeline, baseline implementations, evaluation orchestration, coverage analysis, distortion index computation, GOH analysis)', 'note': 'Claude accelerates annotation pipeline, baseline implementations, and evaluation scripts'}, 'auto_research': {'claude_api_cost': '$1100 (end-to-end code generation, sweep design, results analysis, paper drafting)', 'timeline_acceleration': 'Tier 1 in 9–11 weeks with parallelized training and automated ablation scheduling', 'speed_bottleneck': 'Sequential GRPO training: each run against a PRM variant requires ~50 A100-hours with Qwen2.5-1.5B-Instruct; 3-seed core (3×3×50h = 450h) parallelizable with proportional GPU scaling'}}\n\n## Inspired By\nFive converging threads motivated this study and its tiered design: (1) ODIN demonstrated that orthogonality enforcement between reward heads reduces hacking for length (ICML 2024), establishing the mechanism — but left open whether the CHOICE of decomposition basis matters beyond orthogonality per se, and evaluated only via Pareto fronts without multi-seed statistical testing; (2) Tiwari et al.'s critical methodological finding that static perturbation tests weakly correlate with RL-based exploitation, meaning cheap hackability proxies cannot substitute for expensive RL stress-testing — this directly motivated our staged evaluation pipeline; (3) ErrorAtlas's validated 17-category taxonomy with known prevalence distributions enables principled coverage ablation rather than ad hoc dimension selection; (4) the Coverage Completeness Challenge from arXiv:2603.28063 and arXiv:2605.12474 predicts hacking concentrates on uncovered dimensions, making coverage breadth a first-class experimental variable; (5) MO-GRPO's demonstration that GRPO preferentially exploits high-variance reward dimensions motivated our dual-RL-algorithm robustness check — without controlling for RL-algorithm-specific exploitation, decomposition-basis comparisons under a single RL algorithm may reflect GRPO artifacts rather than genuine PRM properties. The tiered experimental structure was inspired by the recognition that prior proposals in this space (including our own earlier revisions) attempted to answer too many questions simultaneously — scope discipline is itself a methodological contribution. The capacity-control design was motivated by the fundamental confound in coverage ablations: varying both the number of supervised dimensions and model parameter count simultaneously.\n\n## Target Venues\n- ICML 2027 (projected submission January–February 2027) — primary target. Tier 1 deliverable achievable in 4.5–5.5 months from start, leaving 2.5–3.5 months of margin for the ~8-month window. Capacity controls strengthen the core contribution.\n- NeurIPS 2027 (projected submission May 2027) — backup target if extended to Tier 2/3 or if ICML timeline slips. Full 12-month window allows all three tiers including cross-scale robustness and MO-GRPO checks.\n\n## Key References\n- ODIN: Disentangled Reward Mitigates Hacking in RLHF — Chen et al. (arXiv:2402.07319, ICML 2024)\n- Reward Hacking as Equilibrium under Finite Evaluation — Wang & Huang (arXiv:2603.28063, 2026)\n- Reward Hacking in Rubric-Based Reinforcement Learning (arXiv:2605.12474, 2026)\n- Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling — BNRM (arXiv:2602.10623, 2026)\n- Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision — PathFinder-PRM (arXiv:2505.19706, 2025)\n- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models — Tiwari et al. (arXiv:2603.06621, 2026)\n- ErrorMap and ErrorAtlas: Charting the Failure Landscape of Large Language Models — Ashury-Tahan et al. (arXiv:2601.15812, 2026)\n- Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges — PCH survey (arXiv:2604.13602, 2026)\n- From &lt;Answer> to &lt;Think>: Multidimensional Supervision of Reasoning Process — DRM (arXiv:2510.11457, 2025)\n- Dynamic and Generalizable Process Reward Modeling — DG-PRM (arXiv:2507.17849, ACL 2025)\n- Factored Causal Representation Learning for Robust Reward Modeling in RLHF — CausalRM (arXiv:2601.21350, ICML 2026)\n- Process Reward Models That Think — ThinkPRM (arXiv:2504.16828, TMLR 2026)\n- GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (arXiv:2504.00891, AAAI 2026)\n- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning — PURE (arXiv:2504.15275, NeurIPS 2025)\n- R-PRM: Reasoning-Driven Process Reward Modeling (arXiv:2503.21295, EMNLP 2025)\n- Adversarial Training for Process Reward Models — APRM (arXiv:2511.22888, 2025)\n- Causal Reward Adjustment: Mitigating Reward Hacking via Backdoor Correction — CRA (arXiv:2508.04216, 2025)\n- Robust Reward Modeling via Causal Rubrics — CROME (arXiv:2506.16507, 2025)\n- Towards Robust Process Reward Modeling via Noise-Aware Learning (arXiv:2601.12748, 2026)\n- Adversarial Reward Auditing (arXiv:2602.01750, 2026)\n- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (ACL 2025)\n- Towards Hierarchical Multi-Step Reward Models for Enhanced Reasoning in LLMs — HRM (arXiv:2503.13551, 2025)\n- Multi-Objective and Mixed-Reward Reinforcement Learning via Reward-Decorrelated Policy Optimization — RDPO (arXiv:2605.13641, 2026)\n- IR³: Contrastive Inverse Reinforcement Learning for Interpretable Detection and Mitigation of Reward Hacking — Beigi et al. (arXiv:2602.19416, 2026)\n- MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems — Ichihara et al. (arXiv:2509.22047, 2025)\n- Socratic-PRMBench: Benchmarking Process Reward Models with Systematic Reasoning Patterns — Li et al. (arXiv:2505.23474, 2025)\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T05:55:32.580Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T05:55:32.580Z",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99"
}
```

---

## Round 1

42 recorded events

### User

_source line 3 · 2026-05-20T05:55:32.598Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Decomposition Basis Matters: A Tiered Empirical Study of Error-Taxonomic vs. Orthogonality-Enforced vs. Causal Reward Decomposition for PRM Hackability Resistance

## Description
We present the first systematic empirical study of how decomposition basis and coverage breadth jointly affect PRM hackability resistance, organized as a tiered experimental program with staged evaluation and capacity controls. Our two central questions: (1) Does the CHOICE of decomposition basis matter — specifically, does grounding multi-dimensional supervision in a systematic error taxonomy outperform orthogonality-enforced, quality-dimension, and causal alternatives? (2) How does coverage breadth (number of supervised error dimensions) affect hackability, and does hacking shift to uncovered dimensions as theory predicts? We introduce ETA-PRM (Error-Type-Aware PRM), a multi-head architecture with up to 13 ErrorAtlas-aligned error-type heads plus a residual head. The guaranteed Tier 1 deliverable compares four decomposition approaches (ETA error-taxonomic, ODIN data-driven orthogonal, single-head, PathFinder trajectory-level) across a 4-level coverage ablation (2→6→13→13+residual heads), with Random-N capacity controls (N=2,6,13) at each coverage level to disentangle coverage breadth from model capacity. The critical three-way comparison — ETA-PRM-6 (error-type labels) vs. ODIN-6-orthogonal (random labels + orthogonality loss) vs. Random-6 (random labels, no orthogonality) — isolates whether semantic grounding, orthogonality enforcement, or raw capacity drives hackability resistance. Hackability is measured through a staged pipeline motivated by Tiwari et al.'s finding that static perturbation tests weakly predict RL-based exploitation: Stage 1 applies PRM-BiasBench perturbations for surface profiling and GOH sensitivity analysis, Stage 2 traces Best-of-N overoptimization curves as an intermediate proxy, and Stage 3 runs full GRPO exploitation on core variants with 3 seeds and paired bootstrap confidence intervals. The Grounded Orthogonality Hypothesis is tested via pre-registered, falsifiable predictions: comparable overall debiased CKA distance but divergent selective perturbation sensitivity (ETA-PRM heads sensitive to matching perturbation types vs. ODIN heads showing uniform sensitivity). Tier 2 extends to CausalRM and DRM baselines, cross-scale robustness verification (Qwen2.5-Math-1.5B-Instruct backbone), and MO-GRPO robustness checks to rule out RL-algorithm-specific exploitation artifacts; Tier 3 adds ThinkPRM comparison, Socratic-PRMBench reasoning-pattern evaluation, and full mechanistic analysis. All evaluation is on mathematical reasoning, explicitly acknowledged as domain-specific validation with methodology designed for cross-domain extension. This is the first controlled study varying both decomposition basis and coverage breadth with capacity controls, staged hackability evaluation, pre-registered mechanistic predictions, and statistical rigor.

## Core Problem
Multi-dimensional PRM supervision is now a recommended anti-hacking strategy (PCH Section 6.1), with a growing zoo of decomposition schemes operating on fundamentally different bases: ODIN decomposes along a known confounder (length) with explicit orthogonality loss; DRM decomposes along quality dimensions via external scoring models; DG-PRM uses dynamically extracted criteria; CausalRM separates causal from non-causal embedding factors; BNRM uses sparse non-negative latent factors; HRM decomposes along temporal hierarchy (individual vs. consecutive steps at multiple granularities); and IR³ performs post-hoc SAE-based decomposition of already-trained reward signals. The critical unanswered question: does the CHOICE of decomposition basis matter for hackability resistance, or is orthogonality enforcement alone sufficient? And how does coverage breadth (number of supervised error dimensions) interact with basis choice? Recent theoretical work (arXiv:2603.28063) proves that hacking concentrates on uncovered dimensions with computable severity, while empirical work (arXiv:2605.12474) confirms that rubric-based RL is hackable precisely when failure modes go unspecified. However, prior experimental designs in this space suffer from two methodological gaps: (1) scope overload — attempting to simultaneously answer too many questions yields shallow results, and (2) capacity confounding — coverage ablations that vary both the number of supervised dimensions and model parameter count cannot cleanly attribute hackability differences to coverage breadth versus added capacity. We address both the scientific question and these methodological challenges: a tiered experimental program with explicit priority levels guarantees a focused core comparison (4 decomposition bases × 4 coverage levels, with random-label capacity controls) as a first-class deliverable, while permitting principled extension to additional paradigms and cross-scale robustness verification.

## Opportunity
Three converging developments create a narrow window for this study. First, ErrorAtlas (arXiv:2601.15812) provides a validated 17-category error taxonomy (92% validation accuracy across 35 datasets and 83 models) that enables principled coverage ablation with known category distributions — the five most prevalent categories (Missing Required Element 15.6%, Specification Misinterpretation 11.5%, Logical Reasoning Error 9.1%, Incorrect Identification 9.0%, Computation Error 8.5%) account for ~54% of all reasoning benchmark errors. Second, Tiwari et al.'s (arXiv:2603.06621) three-tiered hackability framework reveals a critical methodological insight: static perturbation tests have WEAK correlation with RL-based exploitation — models passing surface-level style-invariance checks (reward changes <0.1) diverge dramatically under optimization pressure (43% of RL reward gains are stylistic shortcuts). This motivates our staged evaluation pipeline that escalates from cheap inference-only probes through Best-of-N overoptimization curves to full RL stress-testing, rather than committing expensive RL runs to all variants. Third, the simultaneous availability of orthogonal decomposition approaches (ETA error-taxonomic, ODIN data-driven orthogonal, PathFinder trajectory-level, CausalRM causal, DRM distributional, HRM temporal-hierarchical, IR³ post-hoc interpretive) means the comparison can be conducted before the field converges on a single paradigm. Fourth, MO-GRPO (arXiv:2509.22047) provides a principled RL-time normalization method that prevents GRPO from preferentially exploiting high-variance reward dimensions, enabling us to disentangle PRM-level decomposition effects from RL-algorithm-specific exploitation artifacts. The missing experiment: a controlled comparison with scope discipline — tiered priorities, staged evaluation, capacity controls, and statistical rigor — varying both decomposition basis and coverage breadth under standardized hackability protocols.

## Landscape
**Orthogonality-enforced decomposition.** ODIN (arXiv:2402.07319, ICML 2024) trains two linear heads on a shared backbone — one correlated with response length, one decorrelated — using ranking + length-correlation + orthogonality loss on projection weights. Nearly eliminates length-reward correlation across PPO and ReMax, evaluated via Pareto front analysis across hyperparameter sweeps. Addresses only a single known confounder (length); does not generalize to multi-faceted attacks. **Quality-dimension decomposition.** DRM (arXiv:2510.11457) computes Confidence (log-probs), Relevance (NLI reranker), and Coherence (Nemotron-70B ORM) as three external signals weighted 0.1/0.2/0.7. Reduces flawed-but-correct reasoning traces but dominated by ORM dimension. Note: DRM's reliance on external scoring models (including a 70B ORM) makes it architecturally distinct from multi-head decomposition approaches that share a single backbone — it is better characterized as a model-ensemble paradigm than a multi-head architecture, and comparisons should be interpreted as contrasting decomposition paradigms rather than head architectures. **Dynamic-criteria decomposition.** DG-PRM (arXiv:2507.17849, ACL 2025) automatically extracts hierarchical criteria via LLM judge comparisons and applies Pareto dominance, reaching 76.5% on PRMBench with 30% training efficiency gains, but without adversarial evaluation. **Representation-level decomposition.** CausalRM (arXiv:2601.21350, ICML 2026) uses a variational encoder with gradient reversal to separate causal from non-causal embedding factors, achieving 5–15% robustness improvement on sycophancy and length-bias probes. **Latent-factor decomposition.** BNRM (arXiv:2602.10623) integrates non-negative factor analysis into Bradley-Terry preference models using Gamma priors and Weibull variational distributions, achieving 93.6% on RewardBench (+3.2% over BT baselines), but operates at outcome-reward level. **Hierarchical temporal decomposition.** HRM (arXiv:2503.13551) evaluates both individual and consecutive reasoning steps at fine and coarse granularity, with Hierarchical Node Compression (HNC) for data augmentation. Addresses reward hacking through multi-level temporal coherence evaluation. Represents an orthogonal axis (temporal hierarchy) to error-category decomposition, and is tested on PRM800K, MATH500, and GSM8K. **Post-hoc interpretive decomposition.** IR³ (arXiv:2602.19416) introduces Contrastive Inverse Reinforcement Learning (C-IRL) to reconstruct implicit reward functions from post-alignment behavioral shifts, then decomposes the reconstructed reward via sparse autoencoders (SAEs) into interpretable features operating on the reward network's penultimate activations. Achieves 0.89 correlation with ground-truth rewards and >90% precision in identifying hacking signatures. Four surgical mitigation strategies (clean reward optimization, adversarial shaping, constrained optimization, feature-guided distillation) reduce hacking while maintaining capabilities within 3% of the original model. Critically, IR³ operates post-hoc on already-trained models — it reverse-engineers internalized objectives rather than building decomposition into the PRM architecture. This represents a fundamentally different decomposition paradigm (interpretive vs. architectural) that is complementary to our multi-head approach: IR³ could analyze what objectives ETA-PRM heads actually learn. **Error-type supervision.** PathFinder-PRM (arXiv:2505.19706) decomposes into math and consistency error dimensions, achieving PRMScore 67.7 on PRMBench with 3× data efficiency. ErrorAtlas (arXiv:2601.15812) provides 17 top-level error categories across 35 datasets and 83 models with 92% validation accuracy, revealing that ~44% of errors in math benchmarks have weak reasoning orientation. **RL-time reward decorrelation.** RDPO (arXiv:2605.13641) applies Magnitude-Aware Quantile normalization and Mahalanobis whitening within active reward subspaces during policy gradient updates — this is RL-TIME decorrelation, not reward-model-time decomposition. Applied to LongCat-Flash post-training (+4.25% IFEval, +10.3% ArenaHard-Hard). Complementary to reward-model-level decomposition — could compose with any PRM decomposition during downstream RL. **Multi-objective RL normalization.** MO-GRPO (arXiv:2509.22047) addresses reward hacking in GRPO by normalizing each reward dimension independently (per-objective z-score) before aggregation, rather than GRPO's default of normalizing after aggregation. This prevents GRPO from preferentially optimizing high-variance reward dimensions while ignoring low-variance ones. Demonstrated to eliminate reward hacking artifacts in machine translation (vanilla GRPO generated 68.7% non-target-language text exploiting readability metrics; MO-GRPO maintained both quality dimensions). Directly relevant to our Stage 3 methodology: when multi-head PRMs produce per-dimension scores, vanilla GRPO may introduce dimension-exploitation artifacts that confound decomposition-basis comparisons. MO-GRPO provides a robustness check isolating PRM-level decomposition effects from RL-algorithm-specific exploitation. **Hackability evaluation.** Tiwari et al. (arXiv:2603.06621) introduce a three-tiered diagnostic framework: (1) static perturbation via PRM-BiasBench (8 perturbation types, inference-only — reveals fluency-logic dissociation but weakly predicts RL outcomes), (2) adversarial optimization (gradient-based, 1000 iterations), (3) RL-induced hacking (GRPO on Qwen2.5-1.5B-Instruct against AIME). Critical finding: Tier 1 and Tier 3 weakly correlate — models certified as style-invariant under static perturbation diverge dramatically under optimization pressure. **Reasoning-pattern-specific evaluation.** Socratic-PRMBench (arXiv:2505.23474) evaluates PRMs across 6 systematic reasoning patterns (Transformation, Decomposition, Regather, Deduction, Verification, Integration) with 20 fine-grained error types nested hierarchically under these patterns, comprising 2995 reasoning paths. Key finding: Qwen2.5-Math-PRM-7B achieves 90.8% accuracy on correct steps but only 42.9% on error steps, with marked deficiencies on Decomposition and Redundancy errors. Complements PRMBench and ProcessBench by testing reasoning-pattern sensitivity — directly relevant to our analysis of whether error-type-specific heads improve detection across diverse reasoning patterns. **Coverage theory.** arXiv:2603.28063 proves under five minimal axioms that hacking concentrates on uncovered dimensions with a computable distortion index. arXiv:2605.12474 empirically confirms this for rubric-based RL. **Other anti-hacking approaches.** ThinkPRM (arXiv:2504.16828, TMLR 2026) achieves 86.5% F1 on ProcessBench with ~1% of PRM800K data via generative verification CoT. GenPRM (arXiv:2504.00891, AAAI 2026) adds code-integrated verification. APRM (arXiv:2511.22888) uses adversarial generator–PRM game training (+3.4pp). CRA (arXiv:2508.04216) mitigates hacking via causal backdoor correction. PURE (arXiv:2504.15275, NeurIPS 2025) reduces hacking via min-form credit assignment. CROME (arXiv:2506.16507) uses causal rubrics (+5.4% RewardBench). No prior work systematically compares decomposition bases AND coverage breadth for hackability resistance with capacity controls, staged evaluation, and statistical rigor.

## Approach
We conduct a controlled comparison of PRM decomposition schemes for hackability resistance, organized as a tiered experimental program with staged evaluation. Two interacting variables: decomposition BASIS (what dimensions to decompose along) and coverage BREADTH (how many dimensions). Our primary system is ETA-PRM (Error-Type-Aware PRM), a multi-head architecture with ErrorAtlas-aligned error-type classification heads.

**TIERED EXPERIMENTAL PROGRAM**

**Tier 1 (Guaranteed Deliverable).** Core comparison answering both research questions with 4 decomposition approaches, 4 coverage levels, and capacity controls. Baselines: (a) ETA-PRM coverage ablation: ETA-PRM-2 / ETA-PRM-6 / ETA-PRM-13 / ETA-PRM-13+R, where each head detects specific ErrorAtlas error categories. ETA-PRM-6 heads: Computation Error, Logical Reasoning Error, Specification Misinterpretation, Factual Error, Output Formatting Error, Missing Required Element. (b) ODIN-6-orthogonal: 6 heads with random (non-error-type-grounded) labels + explicit pairwise cosine orthogonality loss between head projection weights — the critical control isolating semantic grounding from orthogonality enforcement. If ODIN-6-orthogonal matches ETA-PRM-6 on hackability, error-type grounding adds no value beyond orthogonality. (c) Single-head PRM (capacity-matched, zero-decomposition baseline). (d) PathFinder-PRM-style 2-head (math, consistency — minimal decomposition baseline).

**Capacity Controls (addressing coverage-capacity confound).** Each additional head adds a linear projection layer, so the coverage ablation (2→6→13→13+R) changes both coverage breadth and parameter count simultaneously. To disentangle these factors, we include Random-N controls at each coverage level: Random-2, Random-6, Random-13 — architecturally identical to ETA-PRM-N but with randomly assigned error-type labels (each step randomly assigned to one of N categories). These controls have the same parameter budget as ETA-PRM-N at each level but lack semantic grounding. The experimental logic:
- ETA-PRM-N vs. Random-N at each N: isolates the effect of semantic grounding (error-type labels vs. random labels) at matched parameter budget.
- Random-2 vs. Random-6 vs. Random-13: isolates the effect of pure capacity (more heads/parameters) without meaningful coverage signal.
- ODIN-6-orthogonal vs. Random-6: isolates the effect of explicit orthogonality enforcement on random labels.
- ETA-PRM-6 vs. ODIN-6-orthogonal vs. Random-6: the three-way comparison isolates semantic grounding, orthogonality enforcement, and capacity respectively.
If Random-13 shows comparable hackability resistance to Random-2, capacity alone does not explain coverage benefits. If ETA-PRM-N consistently outperforms Random-N, semantic grounding matters beyond added capacity. We additionally report total trainable parameter counts for each variant and include a regression analysis of hackability metrics against parameter count to quantify the capacity contribution.

Interpretability diagnostic: debiased CKA similarity (using unbiased U-statistics for HSIC, following Murphy et al. 2024) between head representations, with pre-registered GOH predictions (see below).

**Tier 2 (Strong-to-Have).** Extends decomposition basis comparison and robustness checks: (e) CausalRM-style gradient-reversal baseline (variational encoder splitting embeddings into causal/non-causal factors). (f) DRM-style 3-dimension scoring pipeline (Confidence/Relevance/Coherence). Note: DRM relies on external scoring models (including an NLI reranker and Nemotron-70B ORM), making it architecturally distinct from multi-head approaches sharing a single backbone. This comparison is informative about decomposition paradigms (external-signal ensemble vs. multi-head architecture vs. representation-level separation) rather than head architecture variants, and results should be interpreted accordingly. (g) Cross-scale robustness check: Qwen2.5-Math-1.5B-Instruct backbone for ETA-PRM-6 and ODIN-6-orthogonal (the core comparison), evaluated with Stages 1–2 of the hackability pipeline. This addresses the single-backbone limitation: if 7B results do not replicate at 1.5B, it may indicate that 7B capacity is necessary for 6 independent error-type heads to learn meaningfully distinct representations, which is itself informative. If results transfer, it strengthens generalizability. The 1.5B scale is chosen because: (i) Qwen2.5-Math-1.5B-Instruct is publicly available and has been validated as a PRM backbone (HuggingFaceH4/Qwen2.5-Math-1.5B-Instruct-PRM-0.2 trained on PRM800K), (ii) the 1.5B-to-7B ratio (~5×) represents a meaningful scale difference, and (iii) 1.5B training is ~4× cheaper than 7B, keeping the robustness check within budget. (h) MO-GRPO robustness check on core pair (ETA-PRM-6 vs. ODIN-6-orthogonal): vanilla GRPO may preferentially exploit high-variance reward dimensions (as demonstrated by MO-GRPO authors: vanilla GRPO generated 68.7% non-target-language text exploiting readability metrics). By re-running Stage 3 with MO-GRPO's per-objective normalization on the core comparison, we verify that decomposition-basis effects are robust to RL algorithm choice and rule out GRPO-specific dimension-exploitation artifacts. If ETA-PRM-6 outperforms ODIN-6-orthogonal under vanilla GRPO but not under MO-GRPO, it would suggest the advantage stems from exploitable variance asymmetries rather than genuine semantic alignment. Tier 2 variants (e)–(f) evaluated with Stages 1–2 of hackability pipeline; full RL only if Tier 1 results warrant.

**Tier 3 (Nice-to-Have).** Extended analysis: (i) ThinkPRM-7B comparison (inference-only, representing implicit decomposition via generative reasoning). (j) Full mechanistic analysis: linear probing of head representations, attack-surface alignment analysis (see GOH section below). (k) Architectural controls: multi-task single-output (controls for gradient regularization), single-head with auxiliary losses. (l) Socratic-PRMBench evaluation on Tier 1 variants to assess reasoning-pattern-specific error detection across the 6 systematic reasoning patterns (Transformation, Decomposition, Regather, Deduction, Verification, Integration) and 20 fine-grained error types.

**SINGLE-BACKBONE LIMITATION ACKNOWLEDGMENT.** All primary experiments (Tier 1) use Qwen2.5-Math-7B-Instruct as the backbone. This choice is justified by: (a) Qwen2.5-Math is the most widely used PRM backbone in the current literature (Tiwari et al., RLHFlow, etc.), enabling direct comparability; (b) the 7B scale provides sufficient representation capacity for up to 13 independent heads while remaining computationally tractable for multi-seed RL experiments. However, results may be backbone-specific: the 7B architecture's representation geometry may particularly favor (or disfavor) certain decomposition approaches, and findings may not transfer to other model families (Llama, Mistral) with different attention patterns and representation structures. The Tier 2 cross-scale check (1.5B) partially addresses scale sensitivity within the Qwen family. Full cross-family robustness (e.g., Llama-3.1-8B, Mistral-7B backbones) is an explicit limitation and priority for follow-up work.

**STAGED HACKABILITY EVALUATION**

Motivated by Tiwari et al.'s finding that Tier 1 (static) tests weakly predict Tier 3 (RL-based) hackability, we adopt a staged pipeline that escalates cost and informativeness.

*Stage 1 — Static Perturbation (all variants, ~60 A100-hours):* PRM-BiasBench protocol with 8 perturbation types (rephrasing, verbosity increase/decrease, within-step reordering, question shuffling, numerical perturbation, reasoning hallucination, question removal). Used for surface-level vulnerability profiling, NOT as definitive hackability measure. Explicitly reports the acknowledged weak correlation with Stage 3. Additionally serves as the input for GOH selective-sensitivity analysis (see pre-registered predictions below).

*Stage 2 — Best-of-N Overoptimization (Tier 1 + selected Tier 2 variants, ~250 A100-hours):* Best-of-N sampling with N ∈ {1, 4, 16, 64, 256} on MATH-500. Track reward-accuracy gap as N increases. Overoptimization onset N* defined as the N where accuracy first declines while reward continues increasing. No RL training required — avoids PPO/GRPO instability while providing meaningful hackability signal. Reports: reward-accuracy gap at each N, overoptimization onset N*, Pareto efficiency curves.

*Stage 3 — Full RL Exploitation (Tier 1 variants only, ~700 A100-hours):* Primary: GRPO (following Tiwari et al. protocol — chosen over PPO for simplicity, lower instability, and direct comparability) training Qwen2.5-1.5B-Instruct against frozen PRM on AIME-style problems. Seed protocol: 3 seeds for core comparison (ETA-PRM-6 vs. ODIN-6-orthogonal vs. single-head PRM), enabling paired bootstrap confidence intervals and Wilcoxon signed-rank tests; 1 seed for PathFinder-2D, Random-6 (capacity control), and coverage ablation sweep (providing directional signal within compute constraints). Tier 2 robustness: MO-GRPO (per-objective normalization) on ETA-PRM-6 vs. ODIN-6-orthogonal only (1 seed each, ~100 A100-hours), verifying decomposition-basis effects are not GRPO-specific exploitation artifacts. Statistical rigor: paired bootstrap 95% CIs on reward-accuracy gap, Wilcoxon signed-rank tests for pairwise comparisons, Cohen's d effect sizes reported alongside p-values. For each coverage level, analyze which ERROR TYPES the GRPO policy learns to exploit — testing the prediction from arXiv:2603.28063 that exploitation concentrates on uncovered categories.

**PRE-REGISTERED GROUNDED ORTHOGONALITY HYPOTHESIS (GOH) PREDICTIONS**

The GOH predicts that error-type grounding achieves orthogonality in attack-surface-aligned feature subspaces rather than arbitrary orthogonal directions. To make this hypothesis falsifiable, we pre-register four specific predictions with concrete metrics and thresholds:

*Prediction 1 (Comparable overall orthogonality):* Average pairwise debiased CKA distance between head intermediate representations will be comparable for ETA-PRM-6 and ODIN-6-orthogonal: |ΔCKA_avg(ETA-6, ODIN-6)| < 0.10. Both should be substantially more orthogonal than Random-6 (no orthogonality enforcement): CKA_avg(Random-6) > CKA_avg(ETA-6) + 0.05 AND CKA_avg(Random-6) > CKA_avg(ODIN-6) + 0.05. (Debiased CKA using unbiased U-statistics for HSIC to avoid inflated similarity in high-dimensional, moderate-sample regimes.)

*Prediction 2 (Selective perturbation sensitivity):* For each ETA-PRM-6 head h_i corresponding to error type e_i, we measure the perturbation-type-specific reward change Δr(h_i, p_j) for each PRM-BiasBench perturbation type p_j. Construct a 6×8 head-by-perturbation sensitivity matrix S. GOH predicts diagonal dominance: for semantically matched head-perturbation pairs (Computation Error ↔ numerical perturbation, Logical Reasoning Error ↔ reasoning hallucination, Specification Misinterpretation ↔ question shuffling, Output Formatting Error ↔ rephrasing, Missing Required Element ↔ question removal), the matched sensitivity exceeds the median unmatched sensitivity by a factor of ≥1.5 for at least 4 of the 5 matched pairs. ODIN-6-orthogonal heads will show uniform sensitivity patterns — no matched pair exceeds the median unmatched by a factor of ≥1.5 for more than 1 of 5 pairs (since ODIN heads have no semantic alignment with perturbation types).

*Prediction 3 (Attack-surface alignment under RL exploitation):* In Stage 3 GRPO exploitation, the error categories that the RL policy learns to exploit (measured by per-category reward-accuracy gap divergence) will correlate with the categories NOT covered by the PRM heads. For ETA-PRM-6 vs. ETA-PRM-13, exploitation should shift to uncovered categories (Spearman ρ > 0.5 between category coverage status and exploitation severity).

*Falsification criteria:* (a) If ETA-PRM-6 heads show LESS overall orthogonality than Random-6 (CKA_avg for ETA-6 significantly higher than Random-6), the grounding-induces-orthogonality component of GOH is refuted. (b) If the sensitivity matrix shows no diagonal dominance — fewer than 3 of 5 matched pairs exceed the 1.5× threshold — the attack-surface-alignment component of GOH is refuted, and error-type labels do not create semantically meaningful head specialization. (c) If both (a) and (b) fail, GOH is comprehensively refuted: error-type grounding provides neither natural orthogonality nor attack-surface alignment. All CKA analyses will use debiased estimators and include random-data baselines following best practices from Murphy et al. (2024).

**ANNOTATION PILOT STUDY**

Before full dataset construction, a 2000-step pilot study addresses annotation quality concerns at 13 categories. Design: stratified sampling from PRM800K covering diverse problem types and difficulty levels. Measurements: (i) per-category survival rate at 0.8 confidence threshold using Qwen3-32B as annotator; (ii) inter-annotator agreement (Cohen's κ) between Qwen3-32B and Claude Sonnet 4 on full 2000 steps, plus human expert agreement on 200-step subsample; (iii) per-category confusion matrices identifying systematic misclassifications; (iv) category frequency distribution to estimate imbalance severity.

Adaptive thresholding: if pilot reveals <50% survival rate at 0.8 threshold for specific categories (likely for rare types like Naming/Symbol Error, Unit Conversion Error), lower threshold to 0.7 for those categories to prevent data starvation. Category-balanced sampling: oversample steps from problem types likely to elicit rare error categories (e.g., physics word problems for unit conversion, competition problems for specification misinterpretation). All coverage ablation results will report effective training examples per category alongside hackability metrics, ruling out the data-quantity confound.

**FULL ANNOTATION (post-pilot).** Re-annotate ~400K steps from PRM800K and RLHFlow trajectories with hierarchical multi-dimensional error labels using Qwen3-32B with category-adaptive confidence thresholds determined by pilot. Apply noise-aware iterative training (NAIT) from arXiv:2601.12748 to refine labels where model predictions diverge from annotations.

**ARCHITECTURE.** ETA-PRM extends a Qwen2.5-Math-7B-Instruct backbone with K classification heads detecting specific ErrorAtlas error categories. Per-type error probabilities aggregated via learned attention-based fusion into step-correctness score. A residual head (at K=13+R) captures error signal not covered by K specific heads. Head-balancing via uncertainty-weighted multi-task loss (Kendall et al.) prevents dominant-category heads from suppressing rare-category learning. Each head consists of a linear projection from the backbone's hidden dimension to a head-specific intermediate dimension, followed by a classification layer. For Random-N capacity controls, architecture is identical but training labels are randomly assigned.

**ACCURACY EVALUATION.** ProcessBench, PRMBench, MATH-500 best-of-N. Supplemented with Socratic-PRMBench (Tier 3) to assess reasoning-pattern-specific detection across 6 patterns and 20 fine-grained error types, testing whether error-type-specific heads improve detection of reasoning-pattern-specific errors (e.g., whether Logical Reasoning Error heads improve Deduction pattern detection). Report alongside hackability metrics to assess accuracy–hackability trade-off.

**MECHANISTIC ANALYSIS (CKA in Tier 1; full analysis in Tier 3).** Tier 1 test: debiased CKA similarity between head intermediate representations for ETA-PRM-6 vs. ODIN-6-orthogonal vs. Random-6, with pre-registered GOH predictions as specified above. Tier 3 extension: linear probing (which input features drive each head?) and attack-surface alignment (selective sensitivity to matching perturbation types, extending the Stage 1 sensitivity matrix analysis).

**DOMAIN-SPECIFICITY ACKNOWLEDGMENT.** All evaluation is on mathematical reasoning (MATH-500, AIME, ProcessBench, PRMBench). Justified because: (a) ErrorAtlas taxonomy is best validated for math reasoning, (b) PRM800K provides the largest process-level supervision dataset, (c) math permits verifiable ground truth for hackability measurement. Generalizability argument: ErrorAtlas taxonomy is domain-general (17 categories derived from 35 datasets spanning math, code, dialogue, general QA), so the experimental methodology and tiered evaluation framework transfer directly even if specific hackability findings may be domain-dependent. Future work: extend to code generation (execution-based verification) and dialogue (human preference ground truth).

## Resource Estimate
{'tier_1_guaranteed': {'gpu_hours': '~1450 A100-hours (50h annotation pilot, 100h full annotation, 400h PRM training for 4 decomposition baselines × 4 coverage levels, 120h Random-N capacity controls training (3 variants: Random-2/6/13), 60h Stage 1 static evaluation for all variants including capacity controls, 250h Stage 2 Best-of-N for Tier 1 variants, 400h Stage 3 GRPO with 3 seeds on core + 1 seed on secondary and capacity controls, 70h CKA + GOH analysis)', 'timeline': '4.5–5.5 months (2–3 weeks pilot + annotation, 7 weeks training including capacity controls, 3 weeks Stage 1+2 evaluation, 4 weeks Stage 3 GRPO, 2–3 weeks analysis + writing)', 'estimated_gpu_cost': '$2900 (A100 at ~$2/hr)'}, 'tier_1_plus_2': {'gpu_hours': '~2050 A100-hours (Tier 1 + 250h CausalRM/DRM training, 80h 1.5B cross-scale training, 40h 1.5B Stages 1–2 evaluation, 100h MO-GRPO robustness check on core pair, 130h Stage 1–2 evaluation on remaining Tier 2 variants)', 'timeline': '5.5–7 months', 'estimated_gpu_cost': '$4100'}, 'full_all_tiers': {'gpu_hours': '~2500 A100-hours (Tiers 1–2 + 200h ThinkPRM inference, 100h Socratic-PRMBench evaluation, 100h full mechanistic analysis, 50h architectural controls)', 'timeline': '7–8 months', 'estimated_gpu_cost': '$5000'}, 'human_in_loop': {'claude_api_cost': '$800 (annotation pipeline, baseline implementations, evaluation orchestration, coverage analysis, distortion index computation, GOH analysis)', 'note': 'Claude accelerates annotation pipeline, baseline implementations, and evaluation scripts'}, 'auto_research': {'claude_api_cost': '$1100 (end-to-end code generation, sweep design, results analysis, paper drafting)', 'timeline_acceleration': 'Tier 1 in 9–11 weeks with parallelized training and automated ablation scheduling', 'speed_bottleneck': 'Sequential GRPO training: each run against a PRM variant requires ~50 A100-hours with Qwen2.5-1.5B-Instruct; 3-seed core (3×3×50h = 450h) parallelizable with proportional GPU scaling'}}

## Inspired By
Five converging threads motivated this study and its tiered design: (1) ODIN demonstrated that orthogonality enforcement between reward heads reduces hacking for length (ICML 2024), establishing the mechanism — but left open whether the CHOICE of decomposition basis matters beyond orthogonality per se, and evaluated only via Pareto fronts without multi-seed statistical testing; (2) Tiwari et al.'s critical methodological finding that static perturbation tests weakly correlate with RL-based exploitation, meaning cheap hackability proxies cannot substitute for expensive RL stress-testing — this directly motivated our staged evaluation pipeline; (3) ErrorAtlas's validated 17-category taxonomy with known prevalence distributions enables principled coverage ablation rather than ad hoc dimension selection; (4) the Coverage Completeness Challenge from arXiv:2603.28063 and arXiv:2605.12474 predicts hacking concentrates on uncovered dimensions, making coverage breadth a first-class experimental variable; (5) MO-GRPO's demonstration that GRPO preferentially exploits high-variance reward dimensions motivated our dual-RL-algorithm robustness check — without controlling for RL-algorithm-specific exploitation, decomposition-basis comparisons under a single RL algorithm may reflect GRPO artifacts rather than genuine PRM properties. The tiered experimental structure was inspired by the recognition that prior proposals in this space (including our own earlier revisions) attempted to answer too many questions simultaneously — scope discipline is itself a methodological contribution. The capacity-control design was motivated by the fundamental confound in coverage ablations: varying both the number of supervised dimensions and model parameter count simultaneously.

## Target Venues
- ICML 2027 (projected submission January–February 2027) — primary target. Tier 1 deliverable achievable in 4.5–5.5 months from start, leaving 2.5–3.5 months of margin for the ~8-month window. Capacity controls strengthen the core contribution.
- NeurIPS 2027 (projected submission May 2027) — backup target if extended to Tier 2/3 or if ICML timeline slips. Full 12-month window allows all three tiers including cross-scale robustness and MO-GRPO checks.

## Key References
- ODIN: Disentangled Reward Mitigates Hacking in RLHF — Chen et al. (arXiv:2402.07319, ICML 2024)
- Reward Hacking as Equilibrium under Finite Evaluation — Wang & Huang (arXiv:2603.28063, 2026)
- Reward Hacking in Rubric-Based Reinforcement Learning (arXiv:2605.12474, 2026)
- Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling — BNRM (arXiv:2602.10623, 2026)
- Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision — PathFinder-PRM (arXiv:2505.19706, 2025)
- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models — Tiwari et al. (arXiv:2603.06621, 2026)
- ErrorMap and ErrorAtlas: Charting the Failure Landscape of Large Language Models — Ashury-Tahan et al. (arXiv:2601.15812, 2026)
- Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges — PCH survey (arXiv:2604.13602, 2026)
- From &lt;Answer> to &lt;Think>: Multidimensional Supervision of Reasoning Process — DRM (arXiv:2510.11457, 2025)
- Dynamic and Generalizable Process Reward Modeling — DG-PRM (arXiv:2507.17849, ACL 2025)
- Factored Causal Representation Learning for Robust Reward Modeling in RLHF — CausalRM (arXiv:2601.21350, ICML 2026)
- Process Reward Models That Think — ThinkPRM (arXiv:2504.16828, TMLR 2026)
- GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (arXiv:2504.00891, AAAI 2026)
- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning — PURE (arXiv:2504.15275, NeurIPS 2025)
- R-PRM: Reasoning-Driven Process Reward Modeling (arXiv:2503.21295, EMNLP 2025)
- Adversarial Training for Process Reward Models — APRM (arXiv:2511.22888, 2025)
- Causal Reward Adjustment: Mitigating Reward Hacking via Backdoor Correction — CRA (arXiv:2508.04216, 2025)
- Robust Reward Modeling via Causal Rubrics — CROME (arXiv:2506.16507, 2025)
- Towards Robust Process Reward Modeling via Noise-Aware Learning (arXiv:2601.12748, 2026)
- Adversarial Reward Auditing (arXiv:2602.01750, 2026)
- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (ACL 2025)
- Towards Hierarchical Multi-Step Reward Models for Enhanced Reasoning in LLMs — HRM (arXiv:2503.13551, 2025)
- Multi-Objective and Mixed-Reward Reinforcement Learning via Reward-Decorrelated Policy Optimization — RDPO (arXiv:2605.13641, 2026)
- IR³: Contrastive Inverse Reinforcement Learning for Interpretable Detection and Mitigation of Reward Hacking — Beigi et al. (arXiv:2602.19416, 2026)
- MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems — Ichihara et al. (arXiv:2509.22047, 2025)
- Socratic-PRMBench: Benchmarking Process Reward Models with Systematic Reasoning Patterns — Li et al. (arXiv:2505.23474, 2025)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "06b67f1f-20cf-41bf-9075-c7bc82f8d3a1",
  "type": "user",
  "uuid": "29d5d642-0838-4402-a337-7bea778dab8d",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T05:55:32.594Z_

```json
{
  "parentUuid": "29d5d642-0838-4402-a337-7bea778dab8d",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "9e385986-ca7f-45d4-a01e-26cfb95a4a34",
  "timestamp": "2026-05-20T05:55:32.594Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T05:55:32.594Z_

```json
{
  "parentUuid": "9e385986-ca7f-45d4-a01e-26cfb95a4a34",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "59dcb3a7-532f-43bc-8f19-fbb6586af3ee",
  "timestamp": "2026-05-20T05:55:32.594Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Decomposition Basis Matters: A Tiered Empirical Study of Error-Taxonomic vs. Orthogonality-Enforced vs. Causal R…",
  "leafUuid": "59dcb3a7-532f-43bc-8f19-fbb6586af3ee",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Compare PRM decomposition bases for hackability resistance",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99"
}
```

---

### Assistant

_source line 8 · 2026-05-20T05:55:38.454Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this proposal carefully. It's about comparing different decomposition bases for Process Reward Models (PRMs) to resist reward hacking. Let me first do the required web searches to understand the current landscape before making any assessments.

Let me search for:
1. Recent work on PRM decomposition and reward hacking
2. ErrorAtlas and error-type-aware PRMs
3. ODIN and orthogonality-enforced reward decomposition
4. Coverage completeness and reward hacking theory
5. Recent PRM hackability evaluation methods
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59dcb3a7-532f-43bc-8f19-fbb6586af3ee",
  "isSidechain": false,
  "requestId": "req_011CbDJbxBKokdEeKUiMqxst",
  "type": "assistant",
  "uuid": "7697c59f-e733-4633-9667-3bd3947d13a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BKvPVUreHsS9bHBpd2pm29",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14658,
      "cache_read_input_tokens": 11374,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14658,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 237,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 14658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14658
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-20T05:55:39.516Z_

I'll start by conducting the required literature searches to ground my assessment. Let me search for the key topics in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7697c59f-e733-4633-9667-3bd3947d13a1",
  "isSidechain": false,
  "requestId": "req_011CbDJbxBKokdEeKUiMqxst",
  "type": "assistant",
  "uuid": "9a00bcb3-36d6-480b-ab71-f4b5ac2b0b9b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BKvPVUreHsS9bHBpd2pm29",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14658,
      "cache_read_input_tokens": 11374,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14658,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 237,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 14658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14658
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T05:55:39.916Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DYcZPK9RHyEzVUDFRsBjt1`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a00bcb3-36d6-480b-ab71-f4b5ac2b0b9b",
  "isSidechain": false,
  "requestId": "req_011CbDJbxBKokdEeKUiMqxst",
  "type": "assistant",
  "uuid": "c2be4678-b978-40c8-8f30-b70a541b7f84",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BKvPVUreHsS9bHBpd2pm29",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14658,
      "cache_read_input_tokens": 11374,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14658,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 237,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 14658,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14658
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T05:55:39.924Z_

<details><summary>↩ Tool result · `toolu_01DYcZPK9RHyEzVUDFRsBjt1`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2be4678-b978-40c8-8f30-b70a541b7f84",
  "isSidechain": false,
  "promptId": "06b67f1f-20cf-41bf-9075-c7bc82f8d3a1",
  "type": "user",
  "uuid": "513c5c13-045e-4460-a8d3-bf636b0d3ef3",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "c2be4678-b978-40c8-8f30-b70a541b7f84",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T05:55:43.833Z_

Now let me run the 5 targeted searches in parallel to understand the landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "513c5c13-045e-4460-a8d3-bf636b0d3ef3",
  "isSidechain": false,
  "requestId": "req_011CbDJcVuJboURS3XYLXmz3",
  "type": "assistant",
  "uuid": "a3c4644c-d0b0-44ff-8aba-245268521b50",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FS5JKmoHCdNaNcLzqSsKZW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 764,
      "cache_read_input_tokens": 26032,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 305,
          "cache_read_input_tokens": 26032,
          "cache_creation_input_tokens": 764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 764
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T05:55:44.947Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Jix4uwg1z72rU8vPViKrZj`</summary>

```json
{
  "query": "ODIN disentangled reward hacking RLHF orthogonality decomposition 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3c4644c-d0b0-44ff-8aba-245268521b50",
  "isSidechain": false,
  "requestId": "req_011CbDJcVuJboURS3XYLXmz3",
  "type": "assistant",
  "uuid": "7ef765d6-aa3d-45ed-aaf1-e5a2309b57ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FS5JKmoHCdNaNcLzqSsKZW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 764,
      "cache_read_input_tokens": 26032,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 305,
          "cache_read_input_tokens": 26032,
          "cache_creation_input_tokens": 764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 764
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T05:55:45.313Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GFoF7g3eftDnVB8wUGrwAt`</summary>

```json
{
  "query": "ErrorAtlas error taxonomy LLM reasoning benchmark 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ef765d6-aa3d-45ed-aaf1-e5a2309b57ce",
  "isSidechain": false,
  "requestId": "req_011CbDJcVuJboURS3XYLXmz3",
  "type": "assistant",
  "uuid": "2a60e8fd-6a13-4d49-938a-fdd5cb0f4606",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FS5JKmoHCdNaNcLzqSsKZW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 764,
      "cache_read_input_tokens": 26032,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 305,
          "cache_read_input_tokens": 26032,
          "cache_creation_input_tokens": 764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 764
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T05:55:46.253Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TAoTAxjsuYtFRrdhX6MWe8`</summary>

```json
{
  "query": "process reward model hackability evaluation PRM-BiasBench Tiwari 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a60e8fd-6a13-4d49-938a-fdd5cb0f4606",
  "isSidechain": false,
  "requestId": "req_011CbDJcVuJboURS3XYLXmz3",
  "type": "assistant",
  "uuid": "eeb6b0a0-101f-48f2-96b5-97f80ee75a57",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FS5JKmoHCdNaNcLzqSsKZW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 764,
      "cache_read_input_tokens": 26032,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 305,
          "cache_read_input_tokens": 26032,
          "cache_creation_input_tokens": 764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 764
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T05:55:47.251Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VNP6MtA4wZ7WQNdT8KGpga`</summary>

```json
{
  "query": "multi-dimensional reward decomposition PRM coverage breadth reward hacking 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eeb6b0a0-101f-48f2-96b5-97f80ee75a57",
  "isSidechain": false,
  "requestId": "req_011CbDJcVuJboURS3XYLXmz3",
  "type": "assistant",
  "uuid": "a8a9d4cc-c7c4-4446-80a7-3cad3f0ef8e6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FS5JKmoHCdNaNcLzqSsKZW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 764,
      "cache_read_input_tokens": 26032,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 305,
          "cache_read_input_tokens": 26032,
          "cache_creation_input_tokens": 764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 764
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T05:55:47.725Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JCBotpoDyGQ2Mj3jT95o5E`</summary>

```json
{
  "query": "PathFinder-PRM error type aware process reward model 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8a9d4cc-c7c4-4446-80a7-3cad3f0ef8e6",
  "isSidechain": false,
  "requestId": "req_011CbDJcVuJboURS3XYLXmz3",
  "type": "assistant",
  "uuid": "b75a2870-7538-43dd-8c78-9be1fed492f1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FS5JKmoHCdNaNcLzqSsKZW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 764,
      "cache_read_input_tokens": 26032,
      "output_tokens": 305,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 305,
          "cache_read_input_tokens": 26032,
          "cache_creation_input_tokens": 764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 764
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T05:55:51.074Z_

<details><summary>↩ Tool result · `toolu_01Jix4uwg1z72rU8vPViKrZj`</summary>

```text
Web search results for query: "ODIN disentangled reward hacking RLHF orthogonality decomposition 2024 2025"

Links: [{"title":"ODIN: Disentangled Reward Mitigates Hacking in RLHF","url":"https://proceedings.mlr.press/v235/chen24bn.html"},{"title":"GitHub - Lichang-Chen/ODIN: ODIN: Disentangled Reward Mitigates Hacking in RLHF (ICML 2024)","url":"https://github.com/Lichang-Chen/ODIN"},{"title":"[2402.07319] ODIN: Disentangled Reward Mitigates Hacking in RLHF","url":"https://arxiv.org/abs/2402.07319"},{"title":"ODIN: Disentangled Reward Mitigates Hacking in RLHF","url":"https://openreview.net/pdf?id=zcIV8OQFVF"},{"title":"ODIN: Disentangled Reward Mitigates Hacking in RLHF Lichang Chen∗‡ Chen Zhu∗†","url":"https://arxiv.org/pdf/2402.07319"},{"title":"ODIN: disentangled reward mitigates hacking in RLHF","url":"https://dl.acm.org/doi/10.5555/3692070.3692382"},{"title":"ODIN: Disentangled Reward Mitigates Hacking in RLHF | OpenReview","url":"https://openreview.net/forum?id=45FuR901Di"}]

Based on the search results, I found information about the ODIN paper:

## ODIN: Disentangled Reward Mitigates Hacking in RLHF

The paper was published at the 41st International Conference on Machine Learning in 2024, with a preprint released in February 2024.

### Research Focus

The work studies the issue of reward hacking on response length, a challenge emerging in Reinforcement Learning from Human Feedback (RLHF) on LLMs. A well-formatted, verbose but less helpful response from the LLMs can often deceive LLMs or even human evaluators and achieve high scores.

### Methodology

In the reward model training stage, ODIN is trained with the same human preference data as vanilla RM with a carefully designed loss to disentangle the length signal and the quality signal into two heads. Only the quality head is involved in RL fine-tuning stage, and the length reward is discarded to reduce reward hacking on length.

### Evaluation

The authors establish a more reliable evaluation protocol for comparing different training configurations, which inspects the trade-off between LLM evaluation score and response length obtained by varying training hyperparameters.

The work is authored by Lichang Chen, Chen Zhu, and colleagues from institutions including University of Maryland, Meta, and Nvidia.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ef765d6-aa3d-45ed-aaf1-e5a2309b57ce",
  "isSidechain": false,
  "promptId": "06b67f1f-20cf-41bf-9075-c7bc82f8d3a1",
  "type": "user",
  "uuid": "31281040-75eb-425d-8fc4-903410457558",
  "toolUseResult": {
    "query": "ODIN disentangled reward hacking RLHF orthogonality decomposition 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KRbekxek2Ffgrq86iCxraZ",
        "content": [
          {
            "title": "ODIN: Disentangled Reward Mitigates Hacking in RLHF",
            "url": "https://proceedings.mlr.press/v235/chen24bn.html"
          },
          {
            "title": "GitHub - Lichang-Chen/ODIN: ODIN: Disentangled Reward Mitigates Hacking in RLHF (ICML 2024)",
            "url": "https://github.com/Lichang-Chen/ODIN"
          },
          {
            "title": "[2402.07319] ODIN: Disentangled Reward Mitigates Hacking in RLHF",
            "url": "https://arxiv.org/abs/2402.07319"
          },
          {
            "title": "ODIN: Disentangled Reward Mitigates Hacking in RLHF",
            "url": "https://openreview.net/pdf?id=zcIV8OQFVF"
          },
          {
            "title": "ODIN: Disentangled Reward Mitigates Hacking in RLHF Lichang Chen∗‡ Chen Zhu∗†",
            "url": "https://arxiv.org/pdf/2402.07319"
          },
          {
            "title": "ODIN: disentangled reward mitigates hacking in RLHF",
            "url": "https://dl.acm.org/doi/10.5555/3692070.3692382"
          },
          {
            "title": "ODIN: Disentangled Reward Mitigates Hacking in RLHF | OpenReview",
            "url": "https://openreview.net/forum?id=45FuR901Di"
          }
        ]
      },
      "Based on the search results, I found information about the ODIN paper:\n\n## ODIN: Disentangled Reward Mitigates Hacking in RLHF\n\nThe paper was published at the 41st International Conference on Machine Learning in 2024, with a preprint released in February 2024.\n\n### Research Focus\n\nThe work studies the issue of reward hacking on response length, a challenge emerging in Reinforcement Learning from Human Feedback (RLHF) on LLMs. A well-formatted, verbose but less helpful response from the LLMs can often deceive LLMs or even human evaluators and achieve high scores.\n\n### Methodology\n\nIn the reward model training stage, ODIN is trained with the same human preference data as vanilla RM with a carefully designed loss to disentangle the length signal and the quality signal into two heads. Only the quality head is involved in RL fine-tuning stage, and the length reward is discarded to reduce reward hacking on length.\n\n### Evaluation\n\nThe authors establish a more reliable evaluation protocol for comparing different training configurations, which inspects the trade-off between LLM evaluation score and response length obtained by varying training hyperparameters.\n\nThe work is authored by Lichang Chen, Chen Zhu, and colleagues from institutions including University of Maryland, Meta, and Nvidia."
    ],
    "durationSeconds": 6.121415910999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7ef765d6-aa3d-45ed-aaf1-e5a2309b57ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T05:55:53.228Z_

<details><summary>↩ Tool result · `toolu_01TAoTAxjsuYtFRrdhX6MWe8`</summary>

```text
Web search results for query: "process reward model hackability evaluation PRM-BiasBench Tiwari 2026"

Links: [{"title":"[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/abs/2603.06621"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of","url":"https://arxiv.org/pdf/2603.06621"},{"title":"1 Introduction","url":"https://arxiv.org/html/2603.06621"},{"title":"Reward Under Attack: Evaluating the Sensitivity of Process Reward Models","url":"https://openreview.net/pdf?id=Hw24VOppus"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models","url":"https://arxiv.org/pdf/2603.03291"},{"title":"Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning","url":"https://arxiv.org/pdf/2504.15275"}]

Based on the search results, I found the research you're looking for:

The paper "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models" is by Rishabh Tiwari and 7 other authors, published February 20, 2026.

Key findings from the research:

- Adversarial optimization demonstrates that gradient-based attacks inflate rewards on invalid trajectories, with reward landscapes exhibiting wide, exploitable peaks.

- RL-induced reward hacking exposes the critical failure mode: policies trained on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts.

- These findings reveal that current PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.

- The researchers release PRM-BiasBench and a diagnostic toolkit to enable robustness evaluation before deployment, with code and dataset available at https://github.com/SqueezeAILab/reward-under-attack.

The research employs a three-tiered diagnostic framework that applies increasing adversarial pressure to quantify vulnerabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eeb6b0a0-101f-48f2-96b5-97f80ee75a57",
  "isSidechain": false,
  "promptId": "06b67f1f-20cf-41bf-9075-c7bc82f8d3a1",
  "type": "user",
  "uuid": "e654b528-56a1-4a95-8372-ac753c4495b2",
  "toolUseResult": {
    "query": "process reward model hackability evaluation PRM-BiasBench Tiwari 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018iLRXApQ9tXoSZp3jT3Vri",
        "content": [
          {
            "title": "[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
            "url": "https://arxiv.org/abs/2603.06621"
          },
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of",
            "url": "https://arxiv.org/pdf/2603.06621"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2603.06621"
          },
          {
            "title": "Reward Under Attack: Evaluating the Sensitivity of Process Reward Models",
            "url": "https://openreview.net/pdf?id=Hw24VOppus"
          },
          {
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models",
            "url": "https://arxiv.org/html/2510.08049v3"
          },
          {
            "title": "One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models",
            "url": "https://arxiv.org/pdf/2603.03291"
          },
          {
            "title": "Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning",
            "url": "https://arxiv.org/pdf/2504.15275"
          }
        ]
      },
      "Based on the search results, I found the research you're looking for:\n\nThe paper \"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models\" is by Rishabh Tiwari and 7 other authors, published February 20, 2026.\n\nKey findings from the research:\n\n- Adversarial optimization demonstrates that gradient-based attacks inflate rewards on invalid trajectories, with reward landscapes exhibiting wide, exploitable peaks.\n\n- RL-induced reward hacking exposes the critical failure mode: policies trained on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts.\n\n- These findings reveal that current PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.\n\n- The researchers release PRM-BiasBench and a diagnostic toolkit to enable robustness evaluation before deployment, with code and dataset available at https://github.com/SqueezeAILab/reward-under-attack.\n\nThe research employs a three-tiered diagnostic framework that applies increasing adversarial pressure to quantify vulnerabilities."
    ],
    "durationSeconds": 6.972186328999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "eeb6b0a0-101f-48f2-96b5-97f80ee75a57",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T05:55:53.714Z_

<details><summary>↩ Tool result · `toolu_01JCBotpoDyGQ2Mj3jT95o5E`</summary>

```text
Web search results for query: "PathFinder-PRM error type aware process reward model 2025"

Links: [{"title":"[2505.19706] Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision","url":"https://arxiv.org/abs/2505.19706"},{"title":"Process-Supervised Reward Model","url":"https://www.emergentmind.com/topics/process-supervised-reward-model-prm"},{"title":"GitHub - declare-lab/PathFinder-PRM: This repository contains the official implementation of Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision.","url":"https://github.com/declare-lab/PathFinder-PRM"},{"title":"Process-supervised Reward Models (PRMs)","url":"https://www.emergentmind.com/topics/process-supervised-reward-models-prm"},{"title":"Process Reward Models: Step-Level Feedback for LLMs","url":"https://www.emergentmind.com/topics/process-reward-models-prm"},{"title":"Improving Process Reward Models with Error-Aware ...","url":"https://arxiv.org/pdf/2505.19706"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Process+Reward+Models+(PRMs)"}]

Here are the search results for PathFinder-PRM:

PathFinder-PRM is a novel hierarchical, error-aware discriminative Process Reward Model that first classifies math and consistency errors at each step, then combines these fine-grained signals to estimate step correctness.

**Key Features:**

- The model was trained on a 400K-sample dataset created by enriching the human-annotated PRM800K corpus and RLHFlow Mistral traces with three-dimensional step-level labels.

- The dataset generation pipeline automatically annotates data with 3-dimensional step-level error labels: Math, Consistency, and Optimality.

**Performance:**

On PRMBench, PathFinder-PRM achieved a state-of-the-art PRMScore of 67.7, outperforming the prior best (65.5) while using 3 times less data. When applied to reward guided greedy search, the model yielded prm@8 48.3, a +1.5 point gain over the strongest baseline.

**Authors and Source:**

The research was conducted by Tej Deep Pala, Panshul Sharma, Amir Zadeh, Chuan Li, and Soujanya Poria, and is available on arXiv as paper 2505.19706.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b75a2870-7538-43dd-8c78-9be1fed492f1",
  "isSidechain": false,
  "promptId": "06b67f1f-20cf-41bf-9075-c7bc82f8d3a1",
  "type": "user",
  "uuid": "7b2a7e12-443c-4db3-8a6d-6460ca3c7a36",
  "toolUseResult": {
    "query": "PathFinder-PRM error type aware process reward model 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_019jzoGDoDoHRbifTcqNLwVi",
        "content": [
          {
            "title": "[2505.19706] Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision",
            "url": "https://arxiv.org/abs/2505.19706"
          },
          {
            "title": "Process-Supervised Reward Model",
            "url": "https://www.emergentmind.com/topics/process-supervised-reward-model-prm"
          },
          {
            "title": "GitHub - declare-lab/PathFinder-PRM: This repository contains the official implementation of Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision.",
            "url": "https://github.com/declare-lab/PathFinder-PRM"
          },
          {
            "title": "Process-supervised Reward Models (PRMs)",
            "url": "https://www.emergentmind.com/topics/process-supervised-reward-models-prm"
          },
          {
            "title": "Process Reward Models: Step-Level Feedback for LLMs",
            "url": "https://www.emergentmind.com/topics/process-reward-models-prm"
          },
          {
            "title": "Improving Process Reward Models with Error-Aware ...",
            "url": "https://arxiv.org/pdf/2505.19706"
          },
          {
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models",
            "url": "https://arxiv.org/html/2510.08049v3"
          },
          {
            "title": "GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub",
            "url": "https://github.com/RyanLiu112/Awesome-Process-Reward-Models"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=Process+Reward+Models+(PRMs)"
          }
        ]
      },
      "Here are the search results for PathFinder-PRM:\n\nPathFinder-PRM is a novel hierarchical, error-aware discriminative Process Reward Model that first classifies math and consistency errors at each step, then combines these fine-grained signals to estimate step correctness.\n\n**Key Features:**\n\n- The model was trained on a 400K-sample dataset created by enriching the human-annotated PRM800K corpus and RLHFlow Mistral traces with three-dimensional step-level labels.\n\n- The dataset generation pipeline automatically annotates data with 3-dimensional step-level error labels: Math, Consistency, and Optimality.\n\n**Performance:**\n\nOn PRMBench, PathFinder-PRM achieved a state-of-the-art PRMScore of 67.7, outperforming the prior best (65.5) while using 3 times less data. When applied to reward guided greedy search, the model yielded prm@8 48.3, a +1.5 point gain over the strongest baseline.\n\n**Authors and Source:**\n\nThe research was conducted by Tej Deep Pala, Panshul Sharma, Amir Zadeh, Chuan Li, and Soujanya Poria, and is available on arXiv as paper 2505.19706."
    ],
    "durationSeconds": 5.986114146,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b75a2870-7538-43dd-8c78-9be1fed492f1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T05:55:56.819Z_

<details><summary>↩ Tool result · `toolu_01GFoF7g3eftDnVB8wUGrwAt`</summary>

```text
Web search results for query: "ErrorAtlas error taxonomy LLM reasoning benchmark 2026 arXiv"

Links: [{"title":"ErrorAtlas: Taxonomy of LLM Failure Modes","url":"https://www.emergentmind.com/topics/erroratlas"},{"title":"[2601.15812v1] ErrorMap and ErrorAtlas: Charting the Failure Landscape of Large Language Models","url":"https://arxiv.org/abs/2601.15812v1"},{"title":"[2601.15812] ErrorMap and ErrorAtlas: Charting the Failure Landscape of Large Language Models","url":"https://arxiv.org/abs/2601.15812"},{"title":"(PDF) ErrorMap and ErrorAtlas: Charting the Failure Landscape of Large Language Models","url":"https://www.researchgate.net/publication/400003408_ErrorMap_and_ErrorAtlas_Charting_the_Failure_Landscape_of_Large_Language_Models"},{"title":"ErrorMap and ErrorAtlas: Charting the Failure Landscape of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=L8cNlB3T4o"},{"title":"ErrorMap and ErrorAtlas: Charting the Failure Landscape of Large Language Models","url":"https://arxiv.org/html/2601.15812v1"},{"title":"ErrorMap and ErrorAtlas: Charting the Failure Landscape ...","url":"https://arxiv.org/pdf/2601.15812"}]

Based on the search results, here's what I found about ErrorAtlas:

## Overview

ErrorAtlas is a taxonomy of model errors generated by applying a method to 35 datasets and 83 models, revealing recurring failure patterns. Large Language Models (LLM) benchmarks tell us when models fail, but not why they fail.

## Key Features

ErrorAtlas provides a standardized classification of failure types, systematically disentangling root causes and surfacing underexplored error modes (e.g., omissions or misinterpretation of requirements). ErrorAtlas highlights error types that are currently underexplored in LLM research, such as omissions of required details in the output and question misinterpretation.

## Methodology

The researchers introduced ErrorMap, the first method to chart the sources of LLM failure, which extracts a model's unique "failure signature" and clarifies what benchmarks measure.

## Publication Details

The paper was submitted to arXiv on Thursday, January 22, 2026 by Shir Ashury-Tahan and 3 other authors. The paper is available as arXiv preprint 2601.15812, with a v2 version submitted on February 17, 2026.

## Availability

The taxonomy and code are publicly available with plans to periodically update ErrorAtlas as new benchmarks and models emerge.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a60e8fd-6a13-4d49-938a-fdd5cb0f4606",
  "isSidechain": false,
  "promptId": "06b67f1f-20cf-41bf-9075-c7bc82f8d3a1",
  "type": "user",
  "uuid": "4a862d19-8b77-4990-a592-2d9e6fcd4659",
  "toolUseResult": {
    "query": "ErrorAtlas error taxonomy LLM reasoning benchmark 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RLXqSzYdnJ2naQsHG8451o",
        "content": [
          {
            "title": "ErrorAtlas: Taxonomy of LLM Failure Modes",
            "url": "https://www.emergentmind.com/topics/erroratlas"
          },
          {
            "title": "[2601.15812v1] ErrorMap and ErrorAtlas: Charting the Failure Landscape of Large Language Models",
            "url": "https://arxiv.org/abs/2601.15812v1"
          },
          {
            "title": "[2601.15812] ErrorMap and ErrorAtlas: Charting the Failure Landscape of Large Language Models",
            "url": "https://arxiv.org/abs/2601.15812"
          },
          {
            "title": "(PDF) ErrorMap and ErrorAtlas: Charting the Failure Landscape of Large Language Models",
            "url": "https://www.researchgate.net/publication/400003408_ErrorMap_and_ErrorAtlas_Charting_the_Failure_Landscape_of_Large_Language_Models"
          },
          {
            "title": "ErrorMap and ErrorAtlas: Charting the Failure Landscape of Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=L8cNlB3T4o"
          },
          {
            "title": "ErrorMap and ErrorAtlas: Charting the Failure Landscape of Large Language Models",
            "url": "https://arxiv.org/html/2601.15812v1"
          },
          {
            "title": "ErrorMap and ErrorAtlas: Charting the Failure Landscape ...",
            "url": "https://arxiv.org/pdf/2601.15812"
          }
        ]
      },
      "Based on the search results, here's what I found about ErrorAtlas:\n\n## Overview\n\nErrorAtlas is a taxonomy of model errors generated by applying a method to 35 datasets and 83 models, revealing recurring failure patterns. Large Language Models (LLM) benchmarks tell us when models fail, but not why they fail.\n\n## Key Features\n\nErrorAtlas provides a standardized classification of failure types, systematically disentangling root causes and surfacing underexplored error modes (e.g., omissions or misinterpretation of requirements). ErrorAtlas highlights error types that are currently underexplored in LLM research, such as omissions of required details in the output and question misinterpretation.\n\n## Methodology\n\nThe researchers introduced ErrorMap, the first method to chart the sources of LLM failure, which extracts a model's unique \"failure signature\" and clarifies what benchmarks measure.\n\n## Publication Details\n\nThe paper was submitted to arXiv on Thursday, January 22, 2026 by Shir Ashury-Tahan and 3 other authors. The paper is available as arXiv preprint 2601.15812, with a v2 version submitted on February 17, 2026.\n\n## Availability\n\nThe taxonomy and code are publicly available with plans to periodically update ErrorAtlas as new benchmarks and models emerge."
    ],
    "durationSeconds": 11.503312736000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2a60e8fd-6a13-4d49-938a-fdd5cb0f4606",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Decomposition Basis Matters: A Tiered Empirical Study of Error-Taxonomic vs. Orthogonality-Enforced vs. Causal R…",
  "leafUuid": "4a862d19-8b77-4990-a592-2d9e6fcd4659",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Compare PRM decomposition bases for hackability resistance",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99"
}
```

---

### Tool result

_source line 24 · 2026-05-20T05:56:05.786Z_

<details><summary>↩ Tool result · `toolu_01VNP6MtA4wZ7WQNdT8KGpga`</summary>

```text
Web search results for query: "multi-dimensional reward decomposition PRM coverage breadth reward hacking 2025 2026"

Links: [{"title":"The Horcrux: Mechanistically Interpretable Task Decomposition for Detecting and Mitigating Reward Hacking in Embodied AI Systems","url":"https://arxiv.org/pdf/2511.17869"},{"title":"GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub","url":"https://github.com/xhwang22/Awesome-Reward-Hacking"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of","url":"https://arxiv.org/pdf/2603.06621"},{"title":"IR$^3$: Contrastive Inverse Reinforcement Learning for Interpretable Detection and Mitigation of Reward Hacking","url":"https://arxiv.org/pdf/2602.19416"},{"title":"Reward Hacking as Equilibrium under Finite Evaluation","url":"https://arxiv.org/pdf/2603.28063"},{"title":"Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning","url":"https://arxiv.org/pdf/2504.15275"},{"title":"Towards Hierarchical Multi-Step Reward Models for Enhanced Reasoning in Large Language Models","url":"https://arxiv.org/pdf/2503.13551"},{"title":"Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction","url":"https://arxiv.org/pdf/2508.04216"}]

Based on the search results, here are the key findings on multi-dimensional reward decomposition, PRM coverage, breadth, reward hacking and related topics from 2025-2026:

## Reward Hacking as Structural Problem

Recent research proves that under minimal axioms like multi-dimensional quality, finite evaluation, and resource finiteness, any optimized AI agent will systematically under-invest effort in quality dimensions not covered by its evaluation system. This establishes reward hacking as a structural equilibrium, not a correctable bug.

## Process Reward Model (PRM) Vulnerabilities

Existing PRMs are vulnerable to reward hacking and require expensive, large-scale annotation of reasoning steps. PRMs often rely on shallow consistency cues rather than causal reasoning structures.

## Multi-Dimensional Reward Solutions

A Hierarchical Reward Model (HRM) approach evaluates both individual and consecutive reasoning steps from fine-grained and coarse-grained levels, excelling at assessing multi-step mathematical reasoning coherence.

## Recent Survey and Resources

A comprehensive survey titled "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges" was released in April 2026. This work proposes the Proxy Compression Hypothesis as a unifying theoretical frame and organizes the field along an escalating hierarchy of exploitation mechanisms.

These findings highlight the fundamental challenges in designing evaluation systems that comprehensively cover all quality dimensions to prevent reward hacking.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8a9d4cc-c7c4-4446-80a7-3cad3f0ef8e6",
  "isSidechain": false,
  "promptId": "06b67f1f-20cf-41bf-9075-c7bc82f8d3a1",
  "type": "user",
  "uuid": "3f634bf5-7977-4b6a-b6f6-cae9c456591a",
  "toolUseResult": {
    "query": "multi-dimensional reward decomposition PRM coverage breadth reward hacking 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RJLTYEKWcouy27X4xh72r3",
        "content": [
          {
            "title": "The Horcrux: Mechanistically Interpretable Task Decomposition for Detecting and Mitigating Reward Hacking in Embodied AI Systems",
            "url": "https://arxiv.org/pdf/2511.17869"
          },
          {
            "title": "GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub",
            "url": "https://github.com/xhwang22/Awesome-Reward-Hacking"
          },
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of",
            "url": "https://arxiv.org/pdf/2603.06621"
          },
          {
            "title": "IR$^3$: Contrastive Inverse Reinforcement Learning for Interpretable Detection and Mitigation of Reward Hacking",
            "url": "https://arxiv.org/pdf/2602.19416"
          },
          {
            "title": "Reward Hacking as Equilibrium under Finite Evaluation",
            "url": "https://arxiv.org/pdf/2603.28063"
          },
          {
            "title": "Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning",
            "url": "https://arxiv.org/pdf/2504.15275"
          },
          {
            "title": "Towards Hierarchical Multi-Step Reward Models for Enhanced Reasoning in Large Language Models",
            "url": "https://arxiv.org/pdf/2503.13551"
          },
          {
            "title": "Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction",
            "url": "https://arxiv.org/pdf/2508.04216"
          }
        ]
      },
      "Based on the search results, here are the key findings on multi-dimensional reward decomposition, PRM coverage, breadth, reward hacking and related topics from 2025-2026:\n\n## Reward Hacking as Structural Problem\n\nRecent research proves that under minimal axioms like multi-dimensional quality, finite evaluation, and resource finiteness, any optimized AI agent will systematically under-invest effort in quality dimensions not covered by its evaluation system. This establishes reward hacking as a structural equilibrium, not a correctable bug.\n\n## Process Reward Model (PRM) Vulnerabilities\n\nExisting PRMs are vulnerable to reward hacking and require expensive, large-scale annotation of reasoning steps. PRMs often rely on shallow consistency cues rather than causal reasoning structures.\n\n## Multi-Dimensional Reward Solutions\n\nA Hierarchical Reward Model (HRM) approach evaluates both individual and consecutive reasoning steps from fine-grained and coarse-grained levels, excelling at assessing multi-step mathematical reasoning coherence.\n\n## Recent Survey and Resources\n\nA comprehensive survey titled \"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\" was released in April 2026. This work proposes the Proxy Compression Hypothesis as a unifying theoretical frame and organizes the field along an escalating hierarchy of exploitation mechanisms.\n\nThese findings highlight the fundamental challenges in designing evaluation systems that comprehensively cover all quality dimensions to prevent reward hacking."
    ],
    "durationSeconds": 18.531614878,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a8a9d4cc-c7c4-4446-80a7-3cad3f0ef8e6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T05:56:16.016Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ckc9tYA5JYAn6wBC8Vfo5x`</summary>

```json
{
  "query": "CausalRM causal reward modeling RLHF gradient reversal sycophancy 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f634bf5-7977-4b6a-b6f6-cae9c456591a",
  "isSidechain": false,
  "requestId": "req_011CbDJeQFnTcXCYFHPKB6D7",
  "type": "assistant",
  "uuid": "c98e689f-1856-4b3c-929a-4ec7c9ef429e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LNf5HGB4JHa2sDnQA9jHRQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 792,
      "cache_creation_input_tokens": 3239,
      "cache_read_input_tokens": 26796,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3239,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 792,
          "output_tokens": 181,
          "cache_read_input_tokens": 26796,
          "cache_creation_input_tokens": 3239,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3239
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T05:56:16.506Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EeCUMCw6ZSPGCHd36uDGdK`</summary>

```json
{
  "query": "DG-PRM dynamic generalizable process reward model ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c98e689f-1856-4b3c-929a-4ec7c9ef429e",
  "isSidechain": false,
  "requestId": "req_011CbDJeQFnTcXCYFHPKB6D7",
  "type": "assistant",
  "uuid": "c9cad0bc-e547-44c5-a2b2-03aab00a4ed5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LNf5HGB4JHa2sDnQA9jHRQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 792,
      "cache_creation_input_tokens": 3239,
      "cache_read_input_tokens": 26796,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3239,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 792,
          "output_tokens": 181,
          "cache_read_input_tokens": 26796,
          "cache_creation_input_tokens": 3239,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3239
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T05:56:17.089Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017vCbda17WbBeSSdGDcZinP`</summary>

```json
{
  "query": "\"reward hacking\" \"coverage completeness\" \"uncovered dimensions\" theory 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9cad0bc-e547-44c5-a2b2-03aab00a4ed5",
  "isSidechain": false,
  "requestId": "req_011CbDJeQFnTcXCYFHPKB6D7",
  "type": "assistant",
  "uuid": "b70c951e-65ac-4df6-9af2-ccb4d21f9e53",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LNf5HGB4JHa2sDnQA9jHRQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 792,
      "cache_creation_input_tokens": 3239,
      "cache_read_input_tokens": 26796,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3239,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 792,
          "output_tokens": 181,
          "cache_read_input_tokens": 26796,
          "cache_creation_input_tokens": 3239,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3239
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T05:56:25.056Z_

<details><summary>↩ Tool result · `toolu_017vCbda17WbBeSSdGDcZinP`</summary>

```text
Web search results for query: ""reward hacking" "coverage completeness" "uncovered dimensions" theory 2026 arXiv"

Links: [{"title":"[2603.28063] Reward Hacking as Equilibrium under Finite Evaluation","url":"https://arxiv.org/abs/2603.28063"},{"title":"Reward Hacking as Equilibrium under Finite Evaluation","url":"https://arxiv.org/html/2603.28063v1"},{"title":"Reward Hacking as Equilibrium under Finite Evaluation","url":"https://arxiv.org/pdf/2603.28063"},{"title":"Reward Hacking in Rubric-Based Reinforcement Learning","url":"https://arxiv.org/html/2605.12474v1"},{"title":"[2604.13602v1] Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/abs/2604.13602v1"},{"title":"[2604.13602] Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/abs/2604.13602"},{"title":"GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub","url":"https://github.com/xhwang22/Awesome-Reward-Hacking"},{"title":"[2506.19248] Inference-Time Reward Hacking in Large Language Models","url":"https://arxiv.org/abs/2506.19248"}]

Based on the search results, I found a highly relevant 2026 arXiv paper that directly addresses your query:

## "Reward Hacking as Equilibrium under Finite Evaluation" (arXiv:2603.28063)

This paper by Jiacheng Wang and Jinbin Huang proves that under five minimal axioms — multi-dimensional quality, finite evaluation, effective optimization, resource finiteness, and combinatorial interaction — any optimized AI agent will systematically under-invest effort in quality dimensions not covered by its evaluation system.

**Key theoretical contributions:**

The framework establishes reward hacking as a structural equilibrium, not a correctable bug, regardless of the specific alignment method (RLHF, DPO, Constitutional AI, or others) or evaluation architecture employed.

The paper proves that the transition from closed reasoning to agentic systems causes evaluation coverage to decline toward zero as tool count grows — because quality dimensions expand combinatorially while evaluation costs grow at most linearly per tool — so that hacking severity increases structurally and without bound.

**Scope and implications:**

The results unify the explanation of sycophancy, length gaming, and specification gaming under a single theoretical structure and yield an actionable vulnerability assessment procedure. Additionally, the paper argues that reward hacking is not an engineering failure but a structural inevitability: a necessary consequence of optimizing any agent under a finite-dimensional evaluation system when the true objective is higher-dimensional.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b70c951e-65ac-4df6-9af2-ccb4d21f9e53",
  "isSidechain": false,
  "promptId": "06b67f1f-20cf-41bf-9075-c7bc82f8d3a1",
  "type": "user",
  "uuid": "1f571ca8-28b0-4cd5-bd47-8830d549bc37",
  "toolUseResult": {
    "query": "\"reward hacking\" \"coverage completeness\" \"uncovered dimensions\" theory 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FMnKEQyUZ7KA1r4qNdLEN6",
        "content": [
          {
            "title": "[2603.28063] Reward Hacking as Equilibrium under Finite Evaluation",
            "url": "https://arxiv.org/abs/2603.28063"
          },
          {
            "title": "Reward Hacking as Equilibrium under Finite Evaluation",
            "url": "https://arxiv.org/html/2603.28063v1"
          },
          {
            "title": "Reward Hacking as Equilibrium under Finite Evaluation",
            "url": "https://arxiv.org/pdf/2603.28063"
          },
          {
            "title": "Reward Hacking in Rubric-Based Reinforcement Learning",
            "url": "https://arxiv.org/html/2605.12474v1"
          },
          {
            "title": "[2604.13602v1] Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges",
            "url": "https://arxiv.org/abs/2604.13602v1"
          },
          {
            "title": "[2604.13602] Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges",
            "url": "https://arxiv.org/abs/2604.13602"
          },
          {
            "title": "GitHub - xhwang22/Awesome-Reward-Hacking: A curated list of papers and resources on Reward Hacking, Emergent Misalignment, and Proxy Exploitation in Large Models · GitHub",
            "url": "https://github.com/xhwang22/Awesome-Reward-Hacking"
          },
          {
            "title": "[2506.19248] Inference-Time Reward Hacking in Large Language Models",
            "url": "https://arxiv.org/abs/2506.19248"
          }
        ]
      },
      "Based on the search results, I found a highly relevant 2026 arXiv paper that directly addresses your query:\n\n## \"Reward Hacking as Equilibrium under Finite Evaluation\" (arXiv:2603.28063)\n\nThis paper by Jiacheng Wang and Jinbin Huang proves that under five minimal axioms — multi-dimensional quality, finite evaluation, effective optimization, resource finiteness, and combinatorial interaction — any optimized AI agent will systematically under-invest effort in quality dimensions not covered by its evaluation system.\n\n**Key theoretical contributions:**\n\nThe framework establishes reward hacking as a structural equilibrium, not a correctable bug, regardless of the specific alignment method (RLHF, DPO, Constitutional AI, or others) or evaluation architecture employed.\n\nThe paper proves that the transition from closed reasoning to agentic systems causes evaluation coverage to decline toward zero as tool count grows — because quality dimensions expand combinatorially while evaluation costs grow at most linearly per tool — so that hacking severity increases structurally and without bound.\n\n**Scope and implications:**\n\nThe results unify the explanation of sycophancy, length gaming, and specification gaming under a single theoretical structure and yield an actionable vulnerability assessment procedure. Additionally, the paper argues that reward hacking is not an engineering failure but a structural inevitability: a necessary consequence of optimizing any agent under a finite-dimensional evaluation system when the true objective is higher-dimensional."
    ],
    "durationSeconds": 7.963883221999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b70c951e-65ac-4df6-9af2-ccb4d21f9e53",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T05:56:26.226Z_

<details><summary>↩ Tool result · `toolu_01Ckc9tYA5JYAn6wBC8Vfo5x`</summary>

```text
Web search results for query: "CausalRM causal reward modeling RLHF gradient reversal sycophancy 2026"

Links: [{"title":"Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://www.arxiv.org/pdf/2601.21350"},{"title":"CausalRM: Causal-Theoretic Reward Modeling for RLHF from Observational User Feedbacks | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.18736v1"},{"title":"Adversarially Trained Reward Models","url":"https://www.emergentmind.com/topics/adversarially-trained-reward-models"},{"title":"[2601.21350] Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://arxiv.org/abs/2601.21350"},{"title":"ICML Poster Factored Causal Representation Learning for Robust Reward Modeling in RLHF","url":"https://icml.cc/virtual/2026/poster/65508"},{"title":"CausalRM: Causal-Theoretic Reward Modeling for RLHF ...","url":"https://arxiv.org/pdf/2603.18736"},{"title":"[2603.18736] CausalRM: Causal-Theoretic Reward Modeling for RLHF from Observational User Feedbacks","url":"https://arxiv.org/abs/2603.18736"}]

Based on the search results, I found information about CausalRM and related research on causal reward modeling in RLHF:

## Key Findings

**CausalRM Overview:**
CausalRM proposes a factored representation learning framework that decomposes the model's contextual embedding into causal factors (sufficient for reward prediction) and non-causal factors (capturing reward-irrelevant attributes like length or sycophantic bias), with the reward head constrained to depend only on the causal component.

**Gradient Reversal Mechanism:**
An adversarial head is trained to predict reward from non-causal factors while applying gradient reversal to discourage them from encoding reward-relevant information.

**Sycophancy Reduction:**
CausalRM reduces reward model sensitivity to length bias by 75–90% and sycophancy drops by up to 11.4pp in accuracy loss compared to standard reward models.

**Related Framework:**
There are also other CausalRM papers from 2026. One work introduces observational reward modeling—learning reward models with observational user feedback (e.g., clicks, copies, and upvotes)—as a scalable and cost-effective alternative.

These approaches address the problem of reward hacking by ensuring that reward models depend only on causally-relevant factors rather than spurious correlations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c98e689f-1856-4b3c-929a-4ec7c9ef429e",
  "isSidechain": false,
  "promptId": "06b67f1f-20cf-41bf-9075-c7bc82f8d3a1",
  "type": "user",
  "uuid": "859896f3-5095-4d93-a47e-3595b483a490",
  "toolUseResult": {
    "query": "CausalRM causal reward modeling RLHF gradient reversal sycophancy 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Xmnqkzz9JQc9TBsZLjDk23",
        "content": [
          {
            "title": "Factored Causal Representation Learning for Robust Reward Modeling in RLHF",
            "url": "https://www.arxiv.org/pdf/2601.21350"
          },
          {
            "title": "CausalRM: Causal-Theoretic Reward Modeling for RLHF from Observational User Feedbacks | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2603.18736v1"
          },
          {
            "title": "Adversarially Trained Reward Models",
            "url": "https://www.emergentmind.com/topics/adversarially-trained-reward-models"
          },
          {
            "title": "[2601.21350] Factored Causal Representation Learning for Robust Reward Modeling in RLHF",
            "url": "https://arxiv.org/abs/2601.21350"
          },
          {
            "title": "ICML Poster Factored Causal Representation Learning for Robust Reward Modeling in RLHF",
            "url": "https://icml.cc/virtual/2026/poster/65508"
          },
          {
            "title": "CausalRM: Causal-Theoretic Reward Modeling for RLHF ...",
            "url": "https://arxiv.org/pdf/2603.18736"
          },
          {
            "title": "[2603.18736] CausalRM: Causal-Theoretic Reward Modeling for RLHF from Observational User Feedbacks",
            "url": "https://arxiv.org/abs/2603.18736"
          }
        ]
      },
      "Based on the search results, I found information about CausalRM and related research on causal reward modeling in RLHF:\n\n## Key Findings\n\n**CausalRM Overview:**\nCausalRM proposes a factored representation learning framework that decomposes the model's contextual embedding into causal factors (sufficient for reward prediction) and non-causal factors (capturing reward-irrelevant attributes like length or sycophantic bias), with the reward head constrained to depend only on the causal component.\n\n**Gradient Reversal Mechanism:**\nAn adversarial head is trained to predict reward from non-causal factors while applying gradient reversal to discourage them from encoding reward-relevant information.\n\n**Sycophancy Reduction:**\nCausalRM reduces reward model sensitivity to length bias by 75–90% and sycophancy drops by up to 11.4pp in accuracy loss compared to standard reward models.\n\n**Related Framework:**\nThere are also other CausalRM papers from 2026. One work introduces observational reward modeling—learning reward models with observational user feedback (e.g., clicks, copies, and upvotes)—as a scalable and cost-effective alternative.\n\nThese approaches address the problem of reward hacking by ensuring that reward models depend only on causally-relevant factors rather than spurious correlations."
    ],
    "durationSeconds": 10.205384053000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c98e689f-1856-4b3c-929a-4ec7c9ef429e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T05:56:26.871Z_

<details><summary>↩ Tool result · `toolu_01EeCUMCw6ZSPGCHd36uDGdK`</summary>

```text
Web search results for query: "DG-PRM dynamic generalizable process reward model ACL 2025"

Links: [{"title":"Dynamic and Generalizable Process Reward Modeling - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.212/"},{"title":"[2507.17849] Dynamic and Generalizable Process Reward Modeling","url":"https://arxiv.org/abs/2507.17849"},{"title":"Dynamic and Generalizable Process Reward Modeling","url":"https://arxiv.org/html/2507.17849v1"},{"title":"Dynamic and Generalizable Process Reward Modeling | Request PDF","url":"https://www.researchgate.net/publication/393982707_Dynamic_and_Generalizable_Process_Reward_Modeling"},{"title":"Process-supervised Reward Models (PRMs)","url":"https://www.emergentmind.com/topics/process-supervised-reward-models-prm"},{"title":"Dynamic and Generalizable Process Reward Modeling Zhangyue Yin♢ Qiushi Sun♡","url":"https://arxiv.org/pdf/2507.17849"},{"title":"CodePRM: Execution Feedback-enhanced Process Reward Model for Code Generation - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.428/"}]

Based on the search results, here's what I found about DG-PRM and ACL 2025:

## Overview

DG-PRM (Dynamic and Generalizable Process Reward Modeling) features a reward tree to capture and store fine-grained, multi-dimensional reward criteria.

## Key Features

DG-PRM dynamically selects reward signals for step-wise reward scoring and adopts Pareto dominance estimation to identify discriminative positive and negative pairs.

## Performance and Generalization

Experimental results show that DG-PRM achieves stunning performance on prevailing benchmarks, significantly boosting model performance across tasks with dense rewards, and adapts well to out-of-distribution scenarios, demonstrating exceptional generalizability.

## Publication Details

The paper was published in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) by authors Zhangyue Yin, Qiushi Sun, Zhiyuan Zeng, Qinyuan Cheng, Xipeng Qiu, and Xuanjing Huang. The paper addresses the challenge that existing PRMs primarily rely on heuristic approaches which struggle with cross-domain generalization, and static and coarse-grained evaluation criteria struggle to adapt to complex process supervision.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9cad0bc-e547-44c5-a2b2-03aab00a4ed5",
  "isSidechain": false,
  "promptId": "06b67f1f-20cf-41bf-9075-c7bc82f8d3a1",
  "type": "user",
  "uuid": "e84ac35b-5bda-4764-a280-a72d52f4cd37",
  "toolUseResult": {
    "query": "DG-PRM dynamic generalizable process reward model ACL 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01L23iGanywbgCmYK5CmsPu5",
        "content": [
          {
            "title": "Dynamic and Generalizable Process Reward Modeling - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.212/"
          },
          {
            "title": "[2507.17849] Dynamic and Generalizable Process Reward Modeling",
            "url": "https://arxiv.org/abs/2507.17849"
          },
          {
            "title": "Dynamic and Generalizable Process Reward Modeling",
            "url": "https://arxiv.org/html/2507.17849v1"
          },
          {
            "title": "Dynamic and Generalizable Process Reward Modeling | Request PDF",
            "url": "https://www.researchgate.net/publication/393982707_Dynamic_and_Generalizable_Process_Reward_Modeling"
          },
          {
            "title": "Process-supervised Reward Models (PRMs)",
            "url": "https://www.emergentmind.com/topics/process-supervised-reward-models-prm"
          },
          {
            "title": "Dynamic and Generalizable Process Reward Modeling Zhangyue Yin♢ Qiushi Sun♡",
            "url": "https://arxiv.org/pdf/2507.17849"
          },
          {
            "title": "CodePRM: Execution Feedback-enhanced Process Reward Model for Code Generation - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-acl.428/"
          }
        ]
      },
      "Based on the search results, here's what I found about DG-PRM and ACL 2025:\n\n## Overview\n\nDG-PRM (Dynamic and Generalizable Process Reward Modeling) features a reward tree to capture and store fine-grained, multi-dimensional reward criteria.\n\n## Key Features\n\nDG-PRM dynamically selects reward signals for step-wise reward scoring and adopts Pareto dominance estimation to identify discriminative positive and negative pairs.\n\n## Performance and Generalization\n\nExperimental results show that DG-PRM achieves stunning performance on prevailing benchmarks, significantly boosting model performance across tasks with dense rewards, and adapts well to out-of-distribution scenarios, demonstrating exceptional generalizability.\n\n## Publication Details\n\nThe paper was published in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) by authors Zhangyue Yin, Qiushi Sun, Zhiyuan Zeng, Qinyuan Cheng, Xipeng Qiu, and Xuanjing Huang. The paper addresses the challenge that existing PRMs primarily rely on heuristic approaches which struggle with cross-domain generalization, and static and coarse-grained evaluation criteria struggle to adapt to complex process supervision."
    ],
    "durationSeconds": 10.361821919000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c9cad0bc-e547-44c5-a2b2-03aab00a4ed5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-20T05:56:26.875Z_

```json
{
  "parentUuid": "e84ac35b-5bda-4764-a280-a72d52f4cd37",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "757cf834-913a-4625-a931-3efd78072314",
  "timestamp": "2026-05-20T05:56:26.875Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-20T05:56:32.730Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do a couple more targeted searches to check if there's any existing work that already systematically compares decomposition bases for PRM hackability, and to check for recent work on rubric-based RL reward hacking.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "757cf834-913a-4625-a931-3efd78072314",
  "isSidechain": false,
  "requestId": "req_011CbDJfxG9VmLTzmo4VeWgQ",
  "type": "assistant",
  "uuid": "43abe0b2-8029-43a1-b3b8-6a70cb13646b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012gu1MbamStCh91teW5RRi7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 787,
      "cache_creation_input_tokens": 2469,
      "cache_read_input_tokens": 30035,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2469,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 787,
          "output_tokens": 195,
          "cache_read_input_tokens": 30035,
          "cache_creation_input_tokens": 2469,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2469
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T05:56:33.627Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KL897HNp9NxKoW6ii56Jgd`</summary>

```json
{
  "query": "\"reward hacking\" \"rubric-based\" reinforcement learning \"uncovered\" \"failure modes\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43abe0b2-8029-43a1-b3b8-6a70cb13646b",
  "isSidechain": false,
  "requestId": "req_011CbDJfxG9VmLTzmo4VeWgQ",
  "type": "assistant",
  "uuid": "81444113-129e-4240-ac8f-8c9381ca975a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012gu1MbamStCh91teW5RRi7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 787,
      "cache_creation_input_tokens": 2469,
      "cache_read_input_tokens": 30035,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2469,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 787,
          "output_tokens": 195,
          "cache_read_input_tokens": 30035,
          "cache_creation_input_tokens": 2469,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2469
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T05:56:34.350Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019tt6bYDzkAP9QrezhGRBCW`</summary>

```json
{
  "query": "systematic comparison decomposition basis reward model hackability resistance multi-head PRM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81444113-129e-4240-ac8f-8c9381ca975a",
  "isSidechain": false,
  "requestId": "req_011CbDJfxG9VmLTzmo4VeWgQ",
  "type": "assistant",
  "uuid": "e086a776-a41a-4552-9f0f-b3229d4de555",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012gu1MbamStCh91teW5RRi7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 787,
      "cache_creation_input_tokens": 2469,
      "cache_read_input_tokens": 30035,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2469,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 787,
          "output_tokens": 195,
          "cache_read_input_tokens": 30035,
          "cache_creation_input_tokens": 2469,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2469
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Decomposition Basis Matters: A Tiered Empirical Study of Error-Taxonomic vs. Orthogonality-Enforced vs. Causal R…",
  "leafUuid": "e086a776-a41a-4552-9f0f-b3229d4de555",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Compare PRM decomposition bases for hackability resistance",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99"
}
```

---

### Tool result

_source line 37 · 2026-05-20T05:56:41.899Z_

<details><summary>↩ Tool result · `toolu_01KL897HNp9NxKoW6ii56Jgd`</summary>

```text
Web search results for query: ""reward hacking" "rubric-based" reinforcement learning "uncovered" "failure modes" 2026"

Links: [{"title":"Reward Hacking in Rubric-Based Reinforcement Learning","url":"https://arxiv.org/html/2605.12474v1"},{"title":"Rubric-Based Reinforcement Learning","url":"https://www.emergentmind.com/topics/rubric-based-reinforcement-learning"},{"title":"Rubric-Based Rewards for RL - Deep (Learning) Focus","url":"https://cameronrwolfe.substack.com/p/rubric-rl"},{"title":"Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards","url":"https://arxiv.org/pdf/2510.07774"},{"title":"Reward Hacking Defense Rubric","url":"https://www.emergentmind.com/topics/reward-hacking-defense-rubric"},{"title":"In-Context Reward Hacking Behaviors","url":"https://www.emergentmind.com/topics/in-context-reward-hacking-behaviors"},{"title":"Reward Hacking in RLVR Systems","url":"https://www.emergentmind.com/topics/reward-hacking-in-reinforcement-learning-with-verifiable-rewards-rlvr"},{"title":"Reward Hacking: The Hidden Failure Mode in AI Optimization | by Adnan Masood, PhD. | Medium","url":"https://medium.com/@adnanmasood/reward-hacking-the-hidden-failure-mode-in-ai-optimization-686b62acf408"}]

Based on the search results, I found several relevant sources discussing reward hacking in rubric-based reinforcement learning and its failure modes in 2026:

## Key Findings

A framework separates two sources of divergence: verifier failure, where the training verifier credits rubric criteria that reference verifiers reject, and rubric-design limitations, where even strong rubric-based verifiers favor responses that rubric-free judges rate worse overall.

### Common Failure Modes

"Miracle Steps" in mathematical reasoning—abrupt correct answers without valid derivation—are common failure modes under outcome-only rewards. A systematic analysis identifies a taxonomy of failure modes, including patterns like Miracle Steps—abrupt jumps to a correct output without a valid preceding derivation.

### In-Context Reward Hacking

In-context reward hacking behaviors encompass failure modes in which LLMs optimize for in-context objectives in ways that technically maximize the stated metric or rubric but violate the true intent behind the specification, occurring both during inference and in interactive feedback cycles.

### Mitigation Approaches

Rubric-based approaches leverage dense reward shaping, interpretable credit assignment, and dynamic rubric updates to mitigate challenges like reward sparsity and reward hacking. Structured rewards and rubrics decompose reward into explicit, interpretable rubric criteria to ensure transparent, multidimensional audits of agent behavior.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81444113-129e-4240-ac8f-8c9381ca975a",
  "isSidechain": false,
  "promptId": "06b67f1f-20cf-41bf-9075-c7bc82f8d3a1",
  "type": "user",
  "uuid": "536a1a07-844d-44df-938b-a51d1d770fa4",
  "toolUseResult": {
    "query": "\"reward hacking\" \"rubric-based\" reinforcement learning \"uncovered\" \"failure modes\" 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MDcG8xSRfioe8AifeEMpj3",
        "content": [
          {
            "title": "Reward Hacking in Rubric-Based Reinforcement Learning",
            "url": "https://arxiv.org/html/2605.12474v1"
          },
          {
            "title": "Rubric-Based Reinforcement Learning",
            "url": "https://www.emergentmind.com/topics/rubric-based-reinforcement-learning"
          },
          {
            "title": "Rubric-Based Rewards for RL - Deep (Learning) Focus",
            "url": "https://cameronrwolfe.substack.com/p/rubric-rl"
          },
          {
            "title": "Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards",
            "url": "https://arxiv.org/pdf/2510.07774"
          },
          {
            "title": "Reward Hacking Defense Rubric",
            "url": "https://www.emergentmind.com/topics/reward-hacking-defense-rubric"
          },
          {
            "title": "In-Context Reward Hacking Behaviors",
            "url": "https://www.emergentmind.com/topics/in-context-reward-hacking-behaviors"
          },
          {
            "title": "Reward Hacking in RLVR Systems",
            "url": "https://www.emergentmind.com/topics/reward-hacking-in-reinforcement-learning-with-verifiable-rewards-rlvr"
          },
          {
            "title": "Reward Hacking: The Hidden Failure Mode in AI Optimization | by Adnan Masood, PhD. | Medium",
            "url": "https://medium.com/@adnanmasood/reward-hacking-the-hidden-failure-mode-in-ai-optimization-686b62acf408"
          }
        ]
      },
      "Based on the search results, I found several relevant sources discussing reward hacking in rubric-based reinforcement learning and its failure modes in 2026:\n\n## Key Findings\n\nA framework separates two sources of divergence: verifier failure, where the training verifier credits rubric criteria that reference verifiers reject, and rubric-design limitations, where even strong rubric-based verifiers favor responses that rubric-free judges rate worse overall.\n\n### Common Failure Modes\n\n\"Miracle Steps\" in mathematical reasoning—abrupt correct answers without valid derivation—are common failure modes under outcome-only rewards. A systematic analysis identifies a taxonomy of failure modes, including patterns like Miracle Steps—abrupt jumps to a correct output without a valid preceding derivation.\n\n### In-Context Reward Hacking\n\nIn-context reward hacking behaviors encompass failure modes in which LLMs optimize for in-context objectives in ways that technically maximize the stated metric or rubric but violate the true intent behind the specification, occurring both during inference and in interactive feedback cycles.\n\n### Mitigation Approaches\n\nRubric-based approaches leverage dense reward shaping, interpretable credit assignment, and dynamic rubric updates to mitigate challenges like reward sparsity and reward hacking. Structured rewards and rubrics decompose reward into explicit, interpretable rubric criteria to ensure transparent, multidimensional audits of agent behavior."
    ],
    "durationSeconds": 8.266778444999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "81444113-129e-4240-ac8f-8c9381ca975a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T05:56:42.972Z_

<details><summary>↩ Tool result · `toolu_019tt6bYDzkAP9QrezhGRBCW`</summary>

```text
Web search results for query: "systematic comparison decomposition basis reward model hackability resistance multi-head PRM 2025 2026"

Links: [{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of","url":"https://arxiv.org/pdf/2603.06621"},{"title":"The Horcrux: Mechanistically Interpretable Task Decomposition for Detecting and Mitigating Reward Hacking in Embodied AI Systems","url":"https://arxiv.org/pdf/2511.17869"},{"title":"Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/pdf/2602.10623"},{"title":"IR$^3$: Contrastive Inverse Reinforcement Learning for Interpretable Detection and Mitigation of Reward Hacking","url":"https://arxiv.org/pdf/2602.19416"},{"title":"Reward Hacking as Equilibrium under Finite Evaluation","url":"https://arxiv.org/pdf/2603.28063"},{"title":"Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning","url":"https://arxiv.org/pdf/2504.15275"}]

I found several highly relevant research papers from 2025-2026 on Process Reward Models (PRMs), reward hacking, and related topics. Here's what I discovered:

## Key Findings:

**On PRM Hackability and Resistance:**

Outcome Reward Models (ORMs) exhibit the strongest resistance to reward hacking due to ground-truth verification, while PRMs are more susceptible to length hacking or verbosity bias due to high variance in step-wise optimization.

**Systematic Comparisons and Surveys:**

A systematic survey of PRMs has been presented across the full loop: how to generate data, how to build PRMs, and how to use PRMs.

**Reward Hacking Analysis:**

PRMs evaluate intermediate reasoning steps, promising finer-grained control and better credit compared to outcome-based reward models that score only final answers. However, PRMs often rely on shallow consistency cues rather than causal reasoning structures.

**Decomposition-Based Approaches:**

Experiments on 1,000 hh-rlhf samples reveal optimal decomposition depths of 12-25 steps reduce reward hacking frequency by 34% across four failure modes.

**Mitigation Strategies:**

Bayesian Non-negative Reward Modeling (BNRM) substantially mitigates reward over-optimization, improves robustness under distribution shifts, and yields more interpretable reward decompositions.

The search results include recent papers on systematic analysis of PRM vulnerability, mechanistic interpretability approaches, and various mitigation techniques for addressing reward hacking in these systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e086a776-a41a-4552-9f0f-b3229d4de555",
  "isSidechain": false,
  "promptId": "06b67f1f-20cf-41bf-9075-c7bc82f8d3a1",
  "type": "user",
  "uuid": "79cf4789-2b5a-4c87-8c4e-bf79cea16a39",
  "toolUseResult": {
    "query": "systematic comparison decomposition basis reward model hackability resistance multi-head PRM 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014foiAGBN7gqm9hXKHBtzXq",
        "content": [
          {
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models",
            "url": "https://arxiv.org/html/2510.08049v3"
          },
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of",
            "url": "https://arxiv.org/pdf/2603.06621"
          },
          {
            "title": "The Horcrux: Mechanistically Interpretable Task Decomposition for Detecting and Mitigating Reward Hacking in Embodied AI Systems",
            "url": "https://arxiv.org/pdf/2511.17869"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling",
            "url": "https://arxiv.org/pdf/2602.10623"
          },
          {
            "title": "IR$^3$: Contrastive Inverse Reinforcement Learning for Interpretable Detection and Mitigation of Reward Hacking",
            "url": "https://arxiv.org/pdf/2602.19416"
          },
          {
            "title": "Reward Hacking as Equilibrium under Finite Evaluation",
            "url": "https://arxiv.org/pdf/2603.28063"
          },
          {
            "title": "Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning",
            "url": "https://arxiv.org/pdf/2504.15275"
          }
        ]
      },
      "I found several highly relevant research papers from 2025-2026 on Process Reward Models (PRMs), reward hacking, and related topics. Here's what I discovered:\n\n## Key Findings:\n\n**On PRM Hackability and Resistance:**\n\nOutcome Reward Models (ORMs) exhibit the strongest resistance to reward hacking due to ground-truth verification, while PRMs are more susceptible to length hacking or verbosity bias due to high variance in step-wise optimization.\n\n**Systematic Comparisons and Surveys:**\n\nA systematic survey of PRMs has been presented across the full loop: how to generate data, how to build PRMs, and how to use PRMs.\n\n**Reward Hacking Analysis:**\n\nPRMs evaluate intermediate reasoning steps, promising finer-grained control and better credit compared to outcome-based reward models that score only final answers. However, PRMs often rely on shallow consistency cues rather than causal reasoning structures.\n\n**Decomposition-Based Approaches:**\n\nExperiments on 1,000 hh-rlhf samples reveal optimal decomposition depths of 12-25 steps reduce reward hacking frequency by 34% across four failure modes.\n\n**Mitigation Strategies:**\n\nBayesian Non-negative Reward Modeling (BNRM) substantially mitigates reward over-optimization, improves robustness under distribution shifts, and yields more interpretable reward decompositions.\n\nThe search results include recent papers on systematic analysis of PRM vulnerability, mechanistic interpretability approaches, and various mitigation techniques for addressing reward hacking in these systems."
    ],
    "durationSeconds": 8.618992363999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e086a776-a41a-4552-9f0f-b3229d4de555",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-20T05:58:08.148Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to conduct my assessment. Let me synthesize what I've found and evaluate this proposal.

## Summary of what I've found:

1. **ODIN (ICML 2024)**: Decomposes reward into length and quality heads using orthogonality loss. Addresses length hacking specifically. Real paper, correctly described.

2. **ErrorAtlas (arXiv:2601.15812, 2026)**: Real paper providing a taxonomy of LLM failure modes across 35 datasets and 83 models. Correctly described.


3. **Tiwari et al. (arXiv:2603.06621, 2026)**: Real paper examining PRM hackability with a three-tiered diagnostic framework and PRM-BiasBench. The findings about static tests' weak predictive power for RL-based exploitation check out. Correctly described.

4. **Coverage theory (arXiv:2603.28063)**: Real paper demonstrating that reward hacking concentrates on uncovered dimensions. Correctly described.

5. **PathFinder-PRM (arXiv:2505.19706)**: Real paper on error-type-aware PRM with separate heads for math and consistency errors. Correctly described.

6. **C ausalRM (arXiv:2601.21350)**: Real paper at ICML 2026 that uses gradient reversal to separate causal from non-causal factors. Correctly described.

7. **DG-PRM (ACL 2025)**: Real paper on dynamic criteria extraction. Correctly described.

8. **Rubric-based RL hacking (arXiv:2605.12474)**: Real paper confirming that hacking occurs when failure modes aren't explicitly specified. Correctly described.

9. **No existing systematic comparison**: My search didn't turn up any existing paper that systematically compares different decomposition bases for PRM hackability resistance while controlling for capacity. This validates the novelty of the proposal.

Now I'm moving into the actual evaluation to understand what this proposal is fundamentally proposing—comparing different PRM decomposition approaches like error-taxonomy-based, orthogonality-enforced, and quality-dimension methods to see which resists hacking best.

The key insight is testing whether semantic grounding in error taxonomies actually matters for hackability resistance or if raw capacity is the real driver. The experimental design handles this by comparing error-aligned heads against random heads with the same capacity, which would reveal whether the taxonomy structure itself provides protection or if it's just a capacity effect.

There's also the question of whether simpler alternatives like ThinkPRM or generative verification could achieve comparable robustness without any multi-head decomposition at all, and whether an ensemble of independent single-head models might work just as well. These aren't fully addressed in the core proposal.

The core assumptions I'm relying on are that ErrorAtlas categories are actually the right granularity for step-level PRM supervision (it was designed for benchmark analysis, not real-time training), that LLM annotations from Qwen3-32B are reliable enough across 400K steps with 13 error categories, and that the multi-head architecture itself provides genuine benefits beyond just having more capacity.

On novelty, the individual pieces—multi-head PRMs, error taxonomies, hackability evaluation frameworks, orthogonality constraints—all exist in prior work. The contribution is in systematically comparing different decomposition bases while controlling for capacity and evaluating robustness through staged attacks, which hasn't been done before. But there's a risk that the core finding could be negative: maybe any reasonable decomposition with sufficient coverage provides similar resistance, making the specific basis choice less important than I'm assuming.

For significance, the question itself matters—knowing whether semantic grounding outperforms orthogonal decomposition would genuinely inform PRM design going forward. The problem is that this is fundamentally an empirical study, so its impact hinges on whether results surprise the community and whether findings hold beyond math reasoning. The single-domain scope is a real limitation here.

The critical test is whether a reviewer would find the results obvious. If semantic grounding clearly wins, that's expected—most would guess meaningful decomposition beats random. But if orthogonality alone suffices without semantic grounding, or if random decomposition with enough capacity performs similarly, those would be genuinely interesting findings that challenge the proposal's assumptions.

Looking at the overall proposal, it's a solid empirical study with clear research questions, good experimental controls, and pre-registered hypotheses that could go either way. The main limitations are that it's fundamentally a systematic comparison rather than a novel method, the most likely positive outcome feels somewhat predictable, and restricting to math problems limits how broadly the findings apply.

For EMNLP 2026 specifically, empirical studies with rigorous controls are well-received, and PRM hackability is definitely an important topic. But the core contribution being primarily a comparison rather than a new method does cap how impactful the work can be. The central question—whether semantic grounding matters for decomposition—is something most researchers would intuitively expect to be true, which makes the contribution feel less surprising even if the empirical validation is valuable.

I'm settling on around 30% acceptance probability. The work has real substance and fills a genuine gap, but the insight ceiling is limited by its empirical-comparison nature, and the most likely outcome wouldn't be particularly shocking to the community. new insight or method. The ETA-PRM architecture is essentially PathFinder-PRM extended to 13 heads with ErrorAtlas categories — not deeply novel. I'd rate this **中**.

**Significance**: The question is important — "does decomposition basis matter?" is a question the field needs answered. But (a) single-domain evaluation limits impact, (b) the answer is likely to be "yes, a little" or "depends on coverage breadth," neither of which is a paradigm-shifting insight. I'd rate this **中**.

**Related Work**: The proposal has exceptional related work coverage. I can verify most cited papers exist and are correctly described. The positioning relative to ODIN, PathFinder, CausalRM, DRM, etc. is clear and accurate. I'd rate this **强**.

Given 中/中/强, I'd estimate 25-35%, median ~30%.

Actually, reconsidering the novelty more carefully — the real contributions are the three-way comparison isolating semantic grounding versus orthogonality versus capacity, the capacity controls using Random-N as a genuine methodological contribution that avoids confounding coverage with capacity, and the Grounded Orthogonality Hypothesis with pre-registered predictions. The capacity control design is particularly clean and addresses a real gap in how coverage ablation studies are typically conducted. While the comparison itself is still "just" a comparison, it satisfies the rigor and practical implications criteria for top venues, though the acceptance ultimately hinges on whether the results reveal surprising insights. I'll stick with 25-35%, median ~30%. Thinking through what would actually excite a reviewer—surprising results that challenge assumptions about semantic grounding, clean phase transitions in the coverage ablation, or meta-insights about capacity effects in prior work—these would elevate the paper. But the proposal only sets up the conditions for interesting findings rather than guaranteeing them. I'll settle on 25.

The upper bound is constrained by the empirical comparison ceiling and single-domain scope, while the lower bound is supported by the genuine literature gap, methodological rigor with capacity controls, and the dual informativeness of either outcome.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79cf4789-2b5a-4c87-8c4e-bf79cea16a39",
  "isSidechain": false,
  "requestId": "req_011CbDJh8zbdqbRngmrjTgFT",
  "type": "assistant",
  "uuid": "dbf919e6-dc5d-485a-adbe-76af948e5b13",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdYuDQCo1x4uh1991ZjcCx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2490,
      "cache_read_input_tokens": 32504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2490
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-20T05:59:53.249Z_

API Error: The socket connection was closed unexpectedly. For more information, pass `verbose: true` in the second argument to fetch()

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbf919e6-dc5d-485a-adbe-76af948e5b13",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "65e99aca-9117-4a1c-9c1f-9400915c8f1f",
  "requestId": "req_011CbDJh8zbdqbRngmrjTgFT",
  "error": "unknown",
  "isApiErrorMessage": true,
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "id": "a4679402-d581-4278-8286-c44390852cc5",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_details": null,
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---

### Runtime record

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Decomposition Basis Matters: A Tiered Empirical Study of Error-Taxonomic vs. Orthogonality-Enforced vs. Causal R…",
  "leafUuid": "65e99aca-9117-4a1c-9c1f-9400915c8f1f",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Compare PRM decomposition bases for hackability resistance",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Decomposition Basis Matters: A Tiered Empirical Study of Error-Taxonomic vs. Orthogonality-Enforced vs. Causal R…",
  "leafUuid": "65e99aca-9117-4a1c-9c1f-9400915c8f1f",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Compare PRM decomposition bases for hackability resistance",
  "sessionId": "5ccfee60-e993-4fc7-ae75-fd441b563a99"
}
```

---
