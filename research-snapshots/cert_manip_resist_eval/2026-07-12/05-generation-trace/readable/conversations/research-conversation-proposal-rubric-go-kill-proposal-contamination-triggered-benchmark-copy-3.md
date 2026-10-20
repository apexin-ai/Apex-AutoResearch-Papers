# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Contamination-Triggered Benchmark

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/e7a41451-686f-4998-8d4e-dc44ee26098e.jsonl`
- **Structured JSON:** [`6f693061fdfd2198d285.json`](../../sessions/6f/6f693061fdfd2198d285.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:32:36.114Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:32:36.114Z",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Contamination-Triggered Benchmark Regeneration with Bifactor IRT Equating\n\n## Description\nWe propose a self-healing benchmark framework that closes the full loop from multi-signal contamination detection through construct-constrained generation to bifactor IRT-equated replacement, with formal graceful-degradation guarantees. The system makes four integrated contributions: (1) A multi-signal contamination sentinel with explicit RL-robustness guarantees, now supported by an analytical demonstration. The ensemble combines five signals: ConStat-style perturbation testing, a novel Differential Item Functioning (DIF) analysis across model release cohorts, IRT aberrance detection, DVD-style generation-variance testing (adapted from Liang et al., arXiv 2601.04895), and membership-inference probes — with formal FDR control. The DIF-based cohort analysis is both novel and analytically RL-robust: we demonstrate via a concrete scenario (200 items, N=80/cohort, 20 contaminated items with P(correct) boosted from 0.50 to 0.80) that logistic regression DIF detects contamination as large uniform DIF (ETS Category C, |Δ_MH|≈3.3) because it examines between-group item-level performance conditional on ability, not within-model output distributions that RL smoothing affects. Quantitative power analysis grounded in PMC5978487 simulations establishes that at N=80/group with contamination-typical effect sizes (δ≈0.8-1.4 logits, consistent with GSM1K's 10-13% accuracy drops), DIF power reaches 60-85%, further enhanced by cumulative Bayesian priors (Sinharay et al., 2006), Item-Focused Trees (Tutz & Berger, 2016), and the 2-of-5 ensemble voting threshold. We acknowledge DIF is underpowered for small effects (14.4% at δ=0.4, N=50/group) — its value is detecting the large effects that threaten benchmark validity, complemented by other signals for subtler contamination. We further address the interaction with task familiarity artifacts (Wang & Heckel, arXiv 2603.12875): task familiarity produces uniform improvements (no DIF signal) while contamination produces item-specific advantages (DIF signal), making DIF a principled discriminator between the two. DVD is labeled as promising but untested against RL-trained models; our RL-contamination experimental condition will resolve this empirical gap. (2) A construct-constrained generation pipeline that abandons direct IRT-parameter conditioning (shown to achieve only rho=0.10-0.45 by arXiv 2602.06631) in favor of construct/taxonomy-based generation, student-simulation pre-screening (r=0.75-0.82), optional pre-filtering via signed isotonic R² scalability coefficients (Hardy et al., arXiv 2603.24999) for fast nonparametric quality control, multi-agent iterative refinement, and empirical calibration on a panel of 200-300 diverse LLMs via Bayesian fixed-parameter calibration (OH2PL, König et al., 2020, achieving unbiased estimates at N≥50). (3) A bifactor IRT equating gate using Projective IRT (PIRT) to handle the multi-construct nature of benchmarks like MMLU — fitting a general ability factor plus domain-specific factors, then projecting to unidimensional equivalents for standard equating (Kim, 2022). Only items whose projected parameters fall within 95% CIs of originals and preserve test information, construct coverage, and model rankings (rho >= 0.95) are accepted. (4) A formal graceful-degradation framework defining validity boundaries grounded in the test equating literature: minimum 20% anchor set for standard equating (Kolen & Brennan, 2004), degraded-but-valid operation via robust LAV equating at 15-20%, halt-and-review below 15%, minimum marginal reliability ≥ 0.80 for benchmark release, and transparent partial-release protocols when full regeneration fails for >15% of items. This uniquely differentiates from Growing Pains (cross-time evaluation without contamination detection or regeneration), from CCV (solution-diversity detection for coding tasks without remediation or psychometric equating), from watermarking approaches (Sander et al., arXiv 2502.17259; proactive prevention requiring pre-release embedding, complementary to our post-hoc detection and remediation), from Wang et al./Self-Critique (identifying the RL-fragility problem without providing a robust detection alternative), from DVD (detecting variant contamination without remediation and untested on RL models), from RIDE/BeTaL (altering difficulty rather than preserving it), and from ConStat (detecting but not remediating contamination). We validate on LiveBench subsets and MMLU-CF under simulated contamination at 10-50% rates — including an RL-contamination condition using GRPO fine-tuning following Wang et al.'s protocol to empirically test DIF robustness and DVD behavior under RL — with naturally-contaminated MMLU/GSM8K as positive controls, and include a pilot feasibility study reporting the first empirical convergence statistics for IRT-equated benchmark item generation.\n\n## Core Problem\nHow can we build self-healing benchmarks that automatically detect contaminated items via multi-signal triangulation — including a novel DIF-based cohort analysis robust to RL-trained reasoning models — and regenerate psychometrically equivalent replacements through empirically calibrated generation with bifactor IRT equating, while maintaining benchmark validity through formal graceful-degradation guarantees?\n\n## Opportunity\nDynamic benchmarks face a fundamental tension: increased contamination resistance via strong rewriting degrades question fidelity and may alter intended difficulty. LiveBench updates monthly but without psychometric calibration; VarBench perturbs inputs but difficulty shifts unpredictably; BenchBench evaluates generation quality but without equating. Educational testing has solved the analogous problem of maintaining test comparability across administrations using IRT equating with anchor items — a mature methodology with decades of validation. However, directly applying this to LLM benchmarks requires solving four underappreciated sub-problems: (1) distinguishing contamination from genuine capability gains — this is especially critical for RL-trained reasoning models (o1, o3, DeepSeek-R1), where Wang et al. (ICLR 2026) demonstrate that GRPO/PPO training conceals contamination signals that reference-free detection methods rely on, with AUROC degradation of 14-20 percentage points (Loss: 14.22pp, Min-K%: 16.42pp, Max-K%: 19.84pp after only ~156 GRPO steps), reducing most to near-random (~50%) AUROC; furthermore, Wang & Heckel (arXiv 2603.12875) show that test-time RL alignment can close fine-tuning performance gaps by ~27 percentage points on average, suggesting some apparent contamination signals may reflect task familiarity artifacts rather than memorization, making item-specific detection even more critical; (2) detecting variant contamination (paraphrased/restructured benchmark items in training data) which evades standard detectors — DVD (arXiv 2601.04895) shows conventional methods achieve only 0.43-0.68 AUC on variant contamination; (3) generating replacement items with controlled psychometric properties (LLMs systematically underestimate difficulty with correlations of only rho=0.10-0.45, per arXiv 2602.06631, necessitating empirical calibration rather than prompt-based difficulty targeting); and (4) equating across multi-construct benchmarks (requiring bifactor or multidimensional IRT rather than naive unidimensional models). No existing work addresses all four sub-problems in an integrated pipeline with formal graceful-degradation guarantees.\n\n## Landscape\nLiveBench (ICLR 2025) updates monthly from recent sources but applies objective scoring without difficulty calibration. LiveCodeBench (ICLR 2025) uses time-segmented evaluation but doesn't ensure psychometric equivalence across segments. BeTaL (ICLR 2026) performs dynamic benchmark design with LLM-in-the-loop but focuses on increasing difficulty, not preserving it. BenchBench (March 2026) evaluates automated benchmark generation using discrimination and validity metrics but without IRT equating. ArenaBencher progressively generates harder items but provides no formal difficulty-equivalence guarantees. CRITICAL CONCURRENT WORK: 'Growing Pains' (arXiv April 2026) uses multidimensional IRT with fixed-parameter calibration and 100 anchor items per dataset to make LLM evaluation extensible across time — achieving Spearman rho >= 0.9 for ranking preservation using 400+ models. However, it addresses efficient evaluation (comparing scores across time), NOT contamination detection or item regeneration. PSN-IRT (AAAI 2026 Oral) analyzes benchmark quality via 4PL IRT but does not regenerate items. RIDE (ICLR 2026) uses IRT-guided perturbation for difficulty evolution in math but does not perform equating. ATLAS (arXiv 2025) applies adaptive testing with IRT to reduce evaluation cost but does not handle contamination. Cross-Context Verification (CCV; arXiv 2603.21454, March 2026) achieves perfect separation between contaminated and genuine reasoning (Mann-Whitney U=0, r=1.0) on SWE-bench Verified by measuring solution diversity across independent sessions — a powerful black-box method, but currently validated only on coding tasks (9 SWE-bench problems, 45 trials) and relying on temperature-0 determinism that may not generalize to knowledge/reasoning benchmarks with inherent answer variability. Hardy et al. (arXiv 2603.24999, March 2026) introduce nonparametric signed isotonic R² scalability coefficients that outperform IRT-based item diagnostics for detecting bad benchmark items on HS Math, GSM8K, and MMLU — lightweight (bivariate monotone fits in seconds) and robust under small-n/large-p conditions; this complements our IRT-based quality control by providing a fast model-agnostic pre-filter for item quality before parametric calibration. On proactive contamination prevention: Sander et al. (arXiv 2502.17259, Feb 2025) propose watermarking benchmarks before release, reformulating questions with a watermarked LLM and detecting 'radioactivity' traces via statistical tests; validated on ARC and MMLU with 1B models, this represents a fundamentally different paradigm (prevention at release time vs. post-hoc detection and remediation). Our approach is complementary: watermarking prevents future contamination, while our pipeline detects and remediates existing contamination in already-deployed benchmarks — the two could be combined in a defense-in-depth strategy. On contamination detection: ConStat (2024) provides performance-based detection with formal FDR control; shortcut neuron analysis (ACL 2025) can isolate contamination to ~1.1-1.4% of neurons with only ~3% false positive impact; 'Test of Time' (arXiv 2025) demonstrates temporal signals are unreliable as standalone contamination indicators. CRITICALLY, 'On The Fragility of Benchmark Contamination Detection in Reasoning Models' (Wang et al., arXiv 2510.02386, ICLR 2026) systematically demonstrates that GRPO/PPO-style RL training conceals contamination signals: reference-free methods show AUROC degradation of 14-20 percentage points after only ~156 GRPO steps (Loss: 14.22pp drop from 75.48% to 61.26%; Min-K%: 16.42pp drop from 74.96% to 58.54%; Max-K%: 19.84pp drop from 69.83% to 49.99% — essentially random), while perturbation-based methods show different degradation patterns. The concealment mechanism is PPO's clipping objective, which contracts the NLL gap between contaminated and clean items. Self-Critique (Tao et al., arXiv 2510.09259, ICLR 2026) partially addresses this via policy-collapse detection but remains an individual-model-level method. DVD (Liang et al., arXiv 2601.04895, Jan 2026) introduces detection via variance of generation distribution and is specifically designed for variant contamination, achieving 0.73-0.74 AUC where Min-K%++ achieves only 0.43-0.68; however, DVD was validated only on SFT-contaminated models and its behavior under RL training is untested. On task familiarity vs. contamination: Wang & Heckel (arXiv 2603.12875, March 2026) show that test-time RL alignment (TTRA) closes the performance gap between base and fine-tuned models by ~27 percentage points on average, suggesting many reported fine-tuning gains are task familiarity artifacts rather than genuine capability improvements; this has a dual implication — it strengthens the need for item-specific contamination detection (since task familiarity produces uniform improvements with no DIF signal, while contamination produces item-specific advantages that DIF detects), but also suggests that contamination-driven DIF effects may be partially confounded with format-familiarity effects that TTRA could remove. On item generation: arXiv 2602.06631 shows LLMs achieve only rho=0.10-0.45 for difficulty estimation, but student simulation approaches (arXiv 2601.09953) achieve r=0.75-0.82 and multi-agent frameworks like ReQUESTA improve discrimination from 0.17 to 0.39. On IRT methodology: bifactor models with Projective IRT (PIRT) enable equating of multidimensional tests while remaining tractable; fixed-parameter calibration requires only N>=200 examinees vs N>=500 for full calibration (Kim & Kolen, 2019); the OH2PL (König, Spoden, & Frey, 2020) achieves unbiased estimates at N>=50 using optimized Bayesian hierarchical priors. No existing work closes the full loop from multi-signal contamination detection (robust to RL-trained models) through construct-constrained generation to bifactor IRT-equated regeneration with graceful-degradation guarantees.\n\n## Approach\nBuild a closed-loop pipeline with three stages plus a formal graceful-degradation framework, each substantially revised to address known limitations:\n\n**Stage 1: Multi-Signal Contamination Sentinel (with RL-Robustness Guarantees).** Deploy an ensemble of five complementary detection signals, explicitly designed so that at least two signals remain informative even against RL-trained reasoning models:\n\n(a) *ConStat-style perturbation testing* — compare model performance on original items vs. semantically-equivalent reformulations, with formal False Discovery Rate (FDR) control. NOTE: Wang et al. (ICLR 2026) show reference-free detectors degrade 14-20pp under RL training (Loss: 14.22pp, Min-K%: 16.42pp, Max-K%: 19.84pp after ~156 GRPO steps); we retain perturbation testing as effective against non-RL models (which still constitute the majority of the model ecosystem) but do not rely on it alone.\n\n(b) *Differential Item Functioning (DIF) across model release cohorts* — a novel application treating model release date as a grouping variable and flagging items that become differentially easier for newer cohorts beyond what general ability gains predict. **This is our primary RL-robust signal.** The key argument: DIF operates on group-level statistical patterns (comparing Item Characteristic Curves across model cohorts matched on overall ability), not individual output distributions. Wang et al. prove that PPO/GRPO clipping contracts the NLL gap *within a single model* between seen and unseen items — but DIF does not examine within-model NLL gaps. It detects whether the structural relationship between ability and item response differs across groups. A contaminated cohort shows anomalous ICCs on specific items regardless of how smooth individual output distributions appear, because contamination must, by definition, create differential item advantage — the one signal RL cannot conceal without negating the purpose of contamination. Furthermore, DIF leverages IRT's invariance principle: item parameters should be group-invariant after controlling for ability, and systematic DIF violations on specific items constitute contamination evidence that is orthogonal to all 10 methods shown to fail.\n\n**Analytical Demonstration of DIF RL-Robustness.** Consider a concrete scenario: 200 binary items evaluated by two annual model cohorts (pre-2026, post-2026) with N=80 models each. Suppose 20 items are contaminated in the newer cohort, boosting P(correct) from 0.50 to 0.80 on those items (δ≈1.4 logits — a conservative estimate given GSM1K's documented 13% average accuracy drop across models, which implies item-level boosts of 20-40% on memorized items for heavily contaminated models). RL smoothing via GRPO/PPO contracts the NLL gap between contaminated and clean items within each individual model's output distribution — this is the mechanism Wang et al. demonstrate. However, the 30-percentage-point accuracy advantage on contaminated items persists at the behavioral level: RL training does not cause models to answer memorized items incorrectly, because doing so would negate the purpose of contamination. Logistic regression DIF with sum-score matching compares the probability of correctly answering each item across the two cohorts, conditioning on total score (overall ability). On the 180 uncontaminated items, both cohorts show similar ICCs after controlling for ability. On the 20 contaminated items, the newer cohort shows systematically higher probability of correct response at every matched ability level — large uniform DIF (ETS Category C: |Δ_MH| = -2.35 × ln(odds ratio) = -2.35 × ln(4.0) ≈ 3.3 delta units, far exceeding the C threshold of 1.5). This differential pattern is detectable because DIF examines between-group item-level performance conditional on ability, not within-model output distributions. RL smoothing is irrelevant to DIF: it modifies how confidently a model generates its answer (the NLL surface), not whether it gets the answer right or wrong (the binary response pattern that DIF analyzes).\n\n**Quantitative DIF Power Analysis.** Independent simulation evidence (PMC5978487) establishes that logistic regression DIF at N=50/group achieves 14.4% power for small effects (δ=0.4) and 31.0% for medium effects (δ=0.6); at N=100/group, these rise to 24.7% and 55.2% respectively. These figures appear concerning for small-sample detection, but benchmark contamination typically produces large effects: GSM1K documents 10-13% average accuracy drops from contamination across models, corresponding to item-level δ≈0.8-1.4 logits on memorized items. DIF power scales super-linearly with effect size; at δ=1.4 with N=80/group (annual cohorts), power is estimated at 60-85% based on extrapolation from PMC5978487 simulation curves, consistent with the general finding that the likelihood ratio test achieves the highest statistical power in most DIF configurations. Furthermore, three factors substantially improve effective power beyond these baseline estimates: (i) cumulative Bayesian priors (Sinharay et al., 2006) accumulate evidence across successive benchmark administrations, borrowing strength from previous DIF estimates to improve detection over time — particularly effective for persistent contamination that affects multiple administrations; (ii) Item-Focused Trees (Tutz & Berger, 2016) avoid arbitrary categorical group splits by treating release date as a continuous covariate, leveraging the full model sample (N=160 rather than two groups of 80) and letting the method identify natural breakpoints where DIF emerges; (iii) the 2-of-5 ensemble voting threshold means even 40-50% individual DIF power yields acceptable ensemble sensitivity when combined with DVD and ConStat signals on non-RL models. We acknowledge that DIF alone is underpowered for small contamination effects (δ<0.6); its value lies in detecting the large effects that matter most for benchmark validity, complemented by other ensemble signals for smaller effects.\n\n**Interaction with Task Familiarity Artifacts.** Wang & Heckel (arXiv 2603.12875, March 2026) demonstrate that test-time RL alignment (TTRA) closes the performance gap between base and fine-tuned models by ~27 percentage points on average, suggesting many reported fine-tuning gains reflect task familiarity rather than genuine capability. This has a dual implication for DIF-based detection. First, it *strengthens* the DIF rationale: task familiarity artifacts produce uniform improvements across all items (no DIF signal), while memorization-based contamination produces item-specific advantages (DIF signal) — DIF thus provides a principled way to distinguish the two, a distinction no other detection method explicitly makes. Second, it introduces a nuance: if some contamination manifests partially as enhanced task-format familiarity rather than item-specific memorization, the item-level DIF effect sizes may be modestly smaller than the raw accuracy gaps suggest. We address this by: (a) noting that DIF would be computed on models as deployed (without TTRA), since TTRA is an analysis tool, not a standard deployment procedure; (b) observing that DIF controls for overall ability via sum-score matching, so any uniform familiarity-driven improvements are absorbed into the ability estimate, leaving item-specific contamination signals intact; (c) reporting DIF effect sizes with uncertainty intervals rather than relying on significance thresholds alone, making the analysis transparent about power limitations.\n\n**DIF Small-Sample Strategy (detailed).** Classical DIF methods (Mantel-Haenszel, logistic regression) require N≥200 per group for optimal performance (Mazor et al., 1992; Scott et al., 2009), far exceeding our ~10-20 models per quarterly cohort. We address this through a four-pronged strategy: (i) *Temporal aggregation*: use semi-annual or annual cohorts rather than quarterly, yielding N=40-80 per group; as the model ecosystem grows (~100+ new models per year as of 2026), annual cohorts will approach the N≥100 threshold where regularized methods become viable. (ii) *Cumulative Bayesian DIF*: following Sinharay et al. (2006, ETS), use DIF estimates from previous benchmark administrations as informative priors for new cohorts, accumulating statistical power over time rather than analyzing each cohort in isolation. (iii) *Item-Focused Trees* (Tutz & Berger, 2016): treat release date as a continuous covariate rather than creating arbitrary categorical cohorts, letting the method identify natural breakpoints where DIF emerges — this avoids the small-group problem entirely while leveraging the full model sample. (iv) *Parsimonious models*: following Belzak (2020, Multivariate Behavioral Research), use logistic regression with sum scores rather than complex IRT models for DIF detection, as simpler models outperform complex ones in small samples even when misspecified. We report DIF effect sizes (ETS delta classification: A/B/C, where C indicates |Δ_MH|≥1.5) with uncertainty intervals rather than relying solely on significance tests, acknowledging power limitations transparently.\n\n(c) *IRT aberrance detection* — flag items whose observed easiness significantly exceeds calibrated difficulty, used as one signal among several rather than a standalone detector.\n\n(d) *DVD-style generation variance testing* (adapted from Liang et al., arXiv 2601.04895) — for models with inference access, generate 50 responses per item via temperature sampling and compute the variance of synthetic-difficulty scores. Contaminated items exhibit bimodal generation distributions (alternating between memorized templates and free generation) yielding high variance, while clean items show unimodal low-variance distributions. This specifically detects variant contamination (paraphrased/restructured benchmark items) where ConStat and Min-K% fail (AUC 0.43-0.68 vs. DVD's 0.73-0.74). NOTE: DVD is promising but untested against RL-trained models — it was validated only on SFT-contaminated models (Qwen2.5, Llama3.1 fine-tuned). Whether the bimodal variance signature persists after GRPO/PPO training is an open empirical question that our RL-contamination experimental condition will directly test. DVD's value in the ensemble is therefore primarily for detecting variant contamination in the non-RL model majority, with DIF providing the RL-robust complement.\n\n(e) *Membership-inference probes* (Min-K% Prob / ReCaLL) where white-box access is available — retained as a cheap first-pass filter effective against non-RL models, but explicitly acknowledged as fragile against GRPO/PPO-trained models per Wang et al. (AUROC drops to ~50% after ~156 GRPO steps).\n\nTrigger regeneration when an item is flagged by >= 2 independent signals, with FDR-controlled thresholds. The ensemble is explicitly designed so that DIF (group-level, analytically RL-robust as demonstrated above) and DVD (generation-variance, variant-robust on SFT models) provide coverage where individual-level methods fail. Genuine capability gains will produce uniform improvement across original and perturbed items (no ConStat signal), across cohorts controlling for ability (no DIF signal), and across temperature samples (no DVD signal), while contamination produces item-specific anomalies in at least two of these dimensions.\n\n**Stage 2: Construct-Constrained Generation with Empirical Calibration.** Critically, we abandon the original approach of conditioning generators on raw IRT parameters — research shows LLMs achieve only rho=0.10-0.45 correlation with actual difficulty (arXiv 2602.06631). Instead: (a) For each flagged item, prompt a frontier generator (DeepSeek-V4-Pro or Qwen-3.5-397B) conditioned on the item's construct tag, cognitive complexity level (Bloom's taxonomy), format template, and 3-5 exemplar items from the same difficulty band — but NOT explicit IRT parameters; (b) Generate 8-10 candidates per flagged item using a multi-agent framework (generator + evaluator + refiner) inspired by ReQUESTA, with iterative critique loops; (c) Pre-screen candidates using student simulation — have a diverse panel of weaker/mid-tier LLMs (4B-14B parameters) role-play as examinees at varying ability levels, estimating approximate difficulty via simulated IRT (achieving r=0.75-0.82 per arXiv 2601.09953), and discard candidates whose estimated difficulty deviates by >1.5 logits from the target; (d) Optionally pre-filter candidates using Hardy et al.'s signed isotonic R² scalability coefficients (arXiv 2603.24999) as a fast, nonparametric quality check — items with anomalously low scalability coefficients (indicating poor construct alignment) are discarded before expensive panel calibration; (e) Empirically calibrate surviving candidates on the full calibration panel of 200-300 diverse LLMs via Bayesian fixed-parameter calibration (OH2PL, König, Spoden, & Frey, 2020), anchored to a preserved clean set (>= 20% of items, following the Kolen & Brennan 20% rule for stable equating). This generate-screen-calibrate pipeline is expected to achieve 30-50% rejection rates based on analogous AIG literature; we report convergence statistics as a key empirical contribution.\n\n**Stage 3: Bifactor IRT Equating Gate.** Move from naive unidimensional 2PL to a bifactor model (general LLM ability + domain-specific factors), which captures the inherently multi-construct nature of benchmarks like MMLU while remaining tractable for equating. Use Projective IRT (PIRT) to project bifactor parameters onto unidimensional equivalents compatible with standard equating software (demonstrated to produce very similar equating outcomes to full numerical integration, with practical advantages for implementation; Kim, 2022). Accept only replacements whose projected difficulty and discrimination fall within the 95% CI of the original item's parameters. Verify that the regenerated benchmark's test information function, construct coverage vector, and model ranking (Spearman rho >= 0.95) match the pre-contamination gold standard. Reject and re-generate otherwise, with a maximum of 3 regeneration cycles per item before flagging for human review.\n\n**Graceful Degradation Framework.** We define formal validity boundaries and fallback strategies for each failure mode, grounded in the test equating literature (Kolen & Brennan, 2004; Angoff, 1984):\n\n(i) *Anchor set integrity*: Maintain a minimum of 20% clean (uncontaminated) anchor items. If contamination detection flags items bringing the clean set below 20%, enter a degraded-but-valid operating mode: switch from standard Stocking-Lord equating to robust Area-Weighted or Least Absolute Values (LAV) equating methods (which tolerate outlying anchor items) and widen acceptance CIs to 99%. If the clean set drops below 15%, halt automated regeneration and flag the entire benchmark version for human review and potential full re-calibration. Below 10%, do not release.\n\n(ii) *Stage 1 error propagation*: False positives (flagging clean items as contaminated) trigger unnecessary regeneration but do not compromise validity — the equating gate (Stage 3) ensures replacements are psychometrically equivalent regardless of whether the original was truly contaminated. False negatives (missing contaminated items) are the more dangerous failure mode; we mitigate this by requiring only 2-of-5 signal agreement, with the understanding that DIF and DVD provide complementary coverage against RL-concealment and variant contamination respectively.\n\n(iii) *Stage 2 generation failure*: If <50% of candidates survive pre-screening for a given item (below the expected 50-70% survival rate), the system relaxes the logit-deviation threshold from 1.5 to 2.0 and generates a second batch of 8-10 candidates. If the item still fails after 3 regeneration cycles, it is flagged for human review but the benchmark continues operating with the original (potentially contaminated) item marked with a quality warning — preferable to reducing test length.\n\n(iv) *Stage 3 equating failure*: If >15% of items fail the equating gate after all regeneration cycles (meaning the benchmark cannot be fully regenerated), we release a partial-regeneration version with: (a) adjusted test information function reported alongside all scores, (b) model rankings computed on both the full benchmark and the clean-items-only subset for comparison, (c) marginal reliability coefficient reported — release only if marginal reliability ≥ 0.80 for group-level comparisons (per APA standards). This partial-release strategy provides transparent validity information rather than silently degraded scores.\n\n(v) *Minimum viable benchmark*: Formally, a regenerated benchmark version is released only if: marginal IRT reliability ≥ 0.80, Spearman rho ≥ 0.90 with the pre-contamination gold standard (relaxed from 0.95 in degraded mode), anchor set ≥ 15%, and SEM ≤ 0.35 across ≥ 70% of the target ability range. These thresholds are derived from operational testing standards (Kolen & Brennan, 2004) adapted for the LLM evaluation context where group-level comparisons (model rankings) are the primary use case.\n\n**Evaluation Strategy.** Validate on three tiers: (a) Primary — LiveBench subsets (math, reasoning, coding) as currently-uncontaminated benchmarks with diverse task types and temporal structure; simulate contamination by fine-tuning open-weight models on specific LiveBench items at controlled rates (10-50%) and measuring detection sensitivity and ranking recovery. Critically, include an RL-contamination condition: apply GRPO fine-tuning (following Wang et al.'s protocol of ~156 steps on contaminated data) to open-weight models on benchmark items and verify that DIF-based detection remains effective while individual-level methods degrade — this directly tests the analytical demonstration's predictions. Additionally, test DVD's bimodal variance signature under RL contamination to determine whether it is robust, partially robust, or fragile (resolving the current empirical gap). (b) Secondary — MMLU-CF (the contamination-free MMLU replacement, ACL 2025) for knowledge-domain evaluation, running the full regeneration pipeline on synthetically contaminated subsets. (c) Positive control — use naturally-contaminated MMLU/GSM8K items (with documented contamination evidence from GSM1K studies) to verify that the contamination sentinel detects known real-world contamination. Additionally, include a **pilot feasibility study** on a single LiveBench math subset (~200 items): run the full generate-screen-calibrate-gate pipeline and report rejection rates, convergence speed, parameter recovery accuracy, ranking preservation, and graceful-degradation trigger rates — providing the first empirical evidence of generate-test-reject convergence for IRT-equated benchmark items.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '900-1300 (inference of 200-300 models on ~5K items each for IRT calibration across multiple rounds, plus item generation with 70B+ models, plus student simulation panel, plus DVD temperature-sampling at 50 generations/item)', 'timeline': '5-6 months (1.5 months multi-signal contamination detector including DIF infrastructure and DVD adaptation, 1.5 months bifactor IRT calibration infrastructure, 1.5 months generation pipeline with student simulation, 1.5 months experiments including RL-contamination condition, pilot feasibility study, and writing)', 'estimated_gpu_cost': '$1800-$2600 at ~$2/hr H100 spot pricing', 'closed_source_api_cost': '$800-$2000 (API calls for ~30-50 closed-source models in calibration panel: GPT-4o, Claude, Gemini, etc. at ~5K items each, plus student simulation inference, plus DVD temperature-sampling for closed-source models)'}, 'human_in_loop': {'gpu_hours': '800-1100 (same inference needs, Claude handles generation orchestration, IRT analysis code, DIF implementation, and DVD adaptation)', 'timeline': '3.5-4.5 months (Claude drafts contamination detection, equating code, DIF pipeline, and student simulation; human validates IRT assumptions, bifactor model specification, DIF power analysis, and experimental design)', 'claude_api_cost': '$400-$700 (Sonnet 4.6 for code generation and pipeline orchestration, ~120M tokens total with caching)', 'estimated_gpu_cost': '$1600-$2200', 'closed_source_api_cost': '$800-$2000'}, 'auto_research': {'gpu_hours': '900-1200 (cannot reduce inference needs for 200-300 model calibration panel; DVD temperature-sampling adds ~10% overhead)', 'timeline': '8-12 weeks (parallelized model evaluation is the critical path; 200-300 model panel requires ~3 weeks per calibration round even with full parallelism; pilot feasibility study adds ~2 weeks; RL-contamination condition adds ~1 week for GRPO training)', 'claude_api_cost': '$800-$1200 (Opus 4.7 for experimental design and IRT analysis, Sonnet 4.6 for implementation, ~180M tokens with caching)', 'estimated_gpu_cost': '$1800-$2400', 'closed_source_api_cost': '$800-$2000', 'speed_bottleneck': 'IRT calibration panel: collecting responses from 200-300 diverse LLMs on pilot items requires sequential API calls to closed-source models (rate limits) and batched inference on open-weight models (GPU scheduling). Minimum ~3 weeks for a single calibration round with full parallelism across ~150 open-weight models and ~50 closed-source APIs. The pilot feasibility study requires at least 2 full calibration rounds. DVD temperature-sampling (50 generations/item) adds ~10% to inference costs.'}}\n\n## Inspired By\nField guide finding that 'contamination resistance degrades question fidelity'; gap between dynamic evaluation (LiveBench, DyVal) and psychometric rigor (IRT, ATLAS); cross-domain transfer of IRT equating from educational testing to benchmark maintenance; arXiv 2602.06631's demonstration that LLMs cannot directly target difficulty parameters, motivating empirical calibration; 'Test of Time' (2025) showing temporal contamination signals are unreliable, motivating multi-signal approaches; Wang et al. (ICLR 2026) showing RL conceals all individual-level contamination signals, motivating group-level DIF analysis; Wang & Heckel (2026) showing task familiarity artifacts produce uniform improvements distinguishable from item-specific contamination via DIF; DVD's demonstration that variant contamination requires specialized detection signals; Hardy et al.'s signed isotonic R² as a lightweight pre-filter complementing parametric IRT; Sander et al.'s watermarking paradigm motivating a complementary post-hoc remediation approach; bifactor IRT and PIRT as a practical bridge between unidimensional oversimplification and intractable full MIRT; Kolen & Brennan's anchor-set theory providing formal graceful-degradation thresholds.\n\n## Target Venues\n- ICLR 2027 (deadline expected ~October 2026 based on historical pattern — not yet announced; ideal timeline for thorough experiments including pilot feasibility study and RL-contamination condition; PRIMARY TARGET)\n- AAAI 2027 (abstract July 21, paper July 28, 2026 — tight but feasible if pilot study is scoped to single domain; 2 months)\n- EACL 2027 via ARR August 2026 cycle (submission August 3, 2026 — feasible with focused experiments on LiveBench math subset)\n\n## Key References\n- LiveBench: A Challenging, Contamination-Free LLM Benchmark (ICLR 2025)\n- LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code (ICLR 2025)\n- Automating Benchmark Design [BeTaL] (ICLR 2026)\n- BenchBench: Benchmarking Automated Benchmark Generation (arXiv 2026)\n- Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration (arXiv April 2026)\n- Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory [PSN-IRT] (AAAI 2026 Oral)\n- The stability of IRT parameters under several test equating conditions (Frontiers in Psychology 2026)\n- Estimating Exam Item Difficulty with LLMs: A Benchmark on Brazil's ENEM Corpus (arXiv 2602.06631, Feb 2026)\n- Take Out Your Calculators: Estimating Real Difficulty with LLM Student Simulations (arXiv 2601.09953, Jan 2026)\n- Reconstructing Item Characteristic Curves with Fine-Tuned LLMs (arXiv 2601.02580, Jan 2026)\n- ReQUESTA: Hybrid Multi-Agent Framework for MCQ Generation (arXiv 2602.03704, Feb 2026)\n- Test of Time: Rethinking Temporal Signal of Benchmark Contamination (arXiv 2509.00072, 2025)\n- ConStat: Performance-Based Contamination Detection with FDR Control (ETH Zurich 2024)\n- Establishing Trustworthy LLM Evaluation via Shortcut Neuron Analysis (ACL 2025)\n- On The Fragility of Benchmark Contamination Detection in Reasoning Models (Wang et al., arXiv 2510.02386, ICLR 2026)\n- Detecting Data Contamination from Reinforcement Learning Post-training [Self-Critique / RL-MIA] (Tao et al., arXiv 2510.09259, ICLR 2026)\n- DVD: Detection via Variance of Generation Distribution for Variant Contamination (Liang et al., arXiv 2601.04895, Jan 2026)\n- Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis [CCV] (arXiv 2603.21454, March 2026)\n- Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients (Hardy et al., arXiv 2603.24999, March 2026)\n- Detecting Benchmark Contamination Through Watermarking (Sander et al., arXiv 2502.17259, Feb 2025)\n- Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks (Wang & Heckel, arXiv 2603.12875, March 2026)\n- Application of IRT Fixed Parameter Calibration to Multiple-Group Test Data (Kim & Kolen, Applied Measurement in Education 2019)\n- An Optimized Bayesian Hierarchical Two-Parameter Logistic Model for Small-Sample Item Calibration [OH2PL] (König, Spoden, & Frey, Applied Psychological Measurement 2020, PMC7262992)\n- Robustness of the OH2PL for Small-Sample Item Calibration (König, Spoden, & Frey, Behavior Research Methods 2022)\n- Approximating Bifactor IRT Equating with Projective IRT [PIRT] (PMC 2020)\n- Item Response Theory True Score Equating for the Bifactor Model (Kim, Journal of Educational Measurement 2022)\n- Several Variations of Simple-Structure MIRT Equating (Kim, Journal of Educational Measurement 2023)\n- MMLU-CF: A Contamination-Free Multi-task Language Understanding Benchmark (ACL 2025)\n- Simulating Training Data Leakage in Multiple-Choice Benchmarks (arXiv 2505.24263, 2025)\n- VarBench: Robust Language Model Benchmarking Through Dynamic Variable Perturbation (EMNLP 2024)\n- DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks (ICLR 2024)\n- RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning (arXiv 2025)\n- Adaptive Testing for LLM Evaluation [ATLAS] (arXiv 2025)\n- Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation (EMNLP 2025)\n- Automatic- and Transformer-Based AIG: A Critical Review (Sommer & Arendasy, Intelligence 2025)\n- Can LLMs Estimate Student Struggles? The Curse of Knowledge Effect (arXiv 2512.18880, 2025)\n- Quantifying Data Contamination in Psychometric Evaluations of LLMs (Han et al., arXiv 2510.07175, 2025)\n- Using Past Data to Enhance Small-Sample DIF Estimation: A Bayesian Approach (Sinharay et al., ETS Research Report RR-06-09, 2006)\n- Testing Differential Item Functioning in Small Samples (Belzak, Multivariate Behavioral Research 2020)\n- Item-Focused Trees for the Detection of Differential Item Functioning (Tutz & Berger, Psychometrika 2016)\n- Test Equating, Scaling, and Linking: Methods and Practices 3rd ed. (Kolen & Brennan, Springer 2014)\n- A Careful Examination of Large Language Model Performance on Grade School Arithmetic [GSM1K] (arXiv 2405.00332, 2024)\n- Power and Sample Size Calculations for Logistic Regression Tests for Differential Item Functioning (PMC5978487)\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T04:32:36.123Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:32:36.123Z",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e"
}
```

---

## Round 1

47 recorded events

### User

_source line 3 · 2026-05-20T04:32:36.140Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Contamination-Triggered Benchmark Regeneration with Bifactor IRT Equating

## Description
We propose a self-healing benchmark framework that closes the full loop from multi-signal contamination detection through construct-constrained generation to bifactor IRT-equated replacement, with formal graceful-degradation guarantees. The system makes four integrated contributions: (1) A multi-signal contamination sentinel with explicit RL-robustness guarantees, now supported by an analytical demonstration. The ensemble combines five signals: ConStat-style perturbation testing, a novel Differential Item Functioning (DIF) analysis across model release cohorts, IRT aberrance detection, DVD-style generation-variance testing (adapted from Liang et al., arXiv 2601.04895), and membership-inference probes — with formal FDR control. The DIF-based cohort analysis is both novel and analytically RL-robust: we demonstrate via a concrete scenario (200 items, N=80/cohort, 20 contaminated items with P(correct) boosted from 0.50 to 0.80) that logistic regression DIF detects contamination as large uniform DIF (ETS Category C, |Δ_MH|≈3.3) because it examines between-group item-level performance conditional on ability, not within-model output distributions that RL smoothing affects. Quantitative power analysis grounded in PMC5978487 simulations establishes that at N=80/group with contamination-typical effect sizes (δ≈0.8-1.4 logits, consistent with GSM1K's 10-13% accuracy drops), DIF power reaches 60-85%, further enhanced by cumulative Bayesian priors (Sinharay et al., 2006), Item-Focused Trees (Tutz & Berger, 2016), and the 2-of-5 ensemble voting threshold. We acknowledge DIF is underpowered for small effects (14.4% at δ=0.4, N=50/group) — its value is detecting the large effects that threaten benchmark validity, complemented by other signals for subtler contamination. We further address the interaction with task familiarity artifacts (Wang & Heckel, arXiv 2603.12875): task familiarity produces uniform improvements (no DIF signal) while contamination produces item-specific advantages (DIF signal), making DIF a principled discriminator between the two. DVD is labeled as promising but untested against RL-trained models; our RL-contamination experimental condition will resolve this empirical gap. (2) A construct-constrained generation pipeline that abandons direct IRT-parameter conditioning (shown to achieve only rho=0.10-0.45 by arXiv 2602.06631) in favor of construct/taxonomy-based generation, student-simulation pre-screening (r=0.75-0.82), optional pre-filtering via signed isotonic R² scalability coefficients (Hardy et al., arXiv 2603.24999) for fast nonparametric quality control, multi-agent iterative refinement, and empirical calibration on a panel of 200-300 diverse LLMs via Bayesian fixed-parameter calibration (OH2PL, König et al., 2020, achieving unbiased estimates at N≥50). (3) A bifactor IRT equating gate using Projective IRT (PIRT) to handle the multi-construct nature of benchmarks like MMLU — fitting a general ability factor plus domain-specific factors, then projecting to unidimensional equivalents for standard equating (Kim, 2022). Only items whose projected parameters fall within 95% CIs of originals and preserve test information, construct coverage, and model rankings (rho >= 0.95) are accepted. (4) A formal graceful-degradation framework defining validity boundaries grounded in the test equating literature: minimum 20% anchor set for standard equating (Kolen & Brennan, 2004), degraded-but-valid operation via robust LAV equating at 15-20%, halt-and-review below 15%, minimum marginal reliability ≥ 0.80 for benchmark release, and transparent partial-release protocols when full regeneration fails for >15% of items. This uniquely differentiates from Growing Pains (cross-time evaluation without contamination detection or regeneration), from CCV (solution-diversity detection for coding tasks without remediation or psychometric equating), from watermarking approaches (Sander et al., arXiv 2502.17259; proactive prevention requiring pre-release embedding, complementary to our post-hoc detection and remediation), from Wang et al./Self-Critique (identifying the RL-fragility problem without providing a robust detection alternative), from DVD (detecting variant contamination without remediation and untested on RL models), from RIDE/BeTaL (altering difficulty rather than preserving it), and from ConStat (detecting but not remediating contamination). We validate on LiveBench subsets and MMLU-CF under simulated contamination at 10-50% rates — including an RL-contamination condition using GRPO fine-tuning following Wang et al.'s protocol to empirically test DIF robustness and DVD behavior under RL — with naturally-contaminated MMLU/GSM8K as positive controls, and include a pilot feasibility study reporting the first empirical convergence statistics for IRT-equated benchmark item generation.

## Core Problem
How can we build self-healing benchmarks that automatically detect contaminated items via multi-signal triangulation — including a novel DIF-based cohort analysis robust to RL-trained reasoning models — and regenerate psychometrically equivalent replacements through empirically calibrated generation with bifactor IRT equating, while maintaining benchmark validity through formal graceful-degradation guarantees?

## Opportunity
Dynamic benchmarks face a fundamental tension: increased contamination resistance via strong rewriting degrades question fidelity and may alter intended difficulty. LiveBench updates monthly but without psychometric calibration; VarBench perturbs inputs but difficulty shifts unpredictably; BenchBench evaluates generation quality but without equating. Educational testing has solved the analogous problem of maintaining test comparability across administrations using IRT equating with anchor items — a mature methodology with decades of validation. However, directly applying this to LLM benchmarks requires solving four underappreciated sub-problems: (1) distinguishing contamination from genuine capability gains — this is especially critical for RL-trained reasoning models (o1, o3, DeepSeek-R1), where Wang et al. (ICLR 2026) demonstrate that GRPO/PPO training conceals contamination signals that reference-free detection methods rely on, with AUROC degradation of 14-20 percentage points (Loss: 14.22pp, Min-K%: 16.42pp, Max-K%: 19.84pp after only ~156 GRPO steps), reducing most to near-random (~50%) AUROC; furthermore, Wang & Heckel (arXiv 2603.12875) show that test-time RL alignment can close fine-tuning performance gaps by ~27 percentage points on average, suggesting some apparent contamination signals may reflect task familiarity artifacts rather than memorization, making item-specific detection even more critical; (2) detecting variant contamination (paraphrased/restructured benchmark items in training data) which evades standard detectors — DVD (arXiv 2601.04895) shows conventional methods achieve only 0.43-0.68 AUC on variant contamination; (3) generating replacement items with controlled psychometric properties (LLMs systematically underestimate difficulty with correlations of only rho=0.10-0.45, per arXiv 2602.06631, necessitating empirical calibration rather than prompt-based difficulty targeting); and (4) equating across multi-construct benchmarks (requiring bifactor or multidimensional IRT rather than naive unidimensional models). No existing work addresses all four sub-problems in an integrated pipeline with formal graceful-degradation guarantees.

## Landscape
LiveBench (ICLR 2025) updates monthly from recent sources but applies objective scoring without difficulty calibration. LiveCodeBench (ICLR 2025) uses time-segmented evaluation but doesn't ensure psychometric equivalence across segments. BeTaL (ICLR 2026) performs dynamic benchmark design with LLM-in-the-loop but focuses on increasing difficulty, not preserving it. BenchBench (March 2026) evaluates automated benchmark generation using discrimination and validity metrics but without IRT equating. ArenaBencher progressively generates harder items but provides no formal difficulty-equivalence guarantees. CRITICAL CONCURRENT WORK: 'Growing Pains' (arXiv April 2026) uses multidimensional IRT with fixed-parameter calibration and 100 anchor items per dataset to make LLM evaluation extensible across time — achieving Spearman rho >= 0.9 for ranking preservation using 400+ models. However, it addresses efficient evaluation (comparing scores across time), NOT contamination detection or item regeneration. PSN-IRT (AAAI 2026 Oral) analyzes benchmark quality via 4PL IRT but does not regenerate items. RIDE (ICLR 2026) uses IRT-guided perturbation for difficulty evolution in math but does not perform equating. ATLAS (arXiv 2025) applies adaptive testing with IRT to reduce evaluation cost but does not handle contamination. Cross-Context Verification (CCV; arXiv 2603.21454, March 2026) achieves perfect separation between contaminated and genuine reasoning (Mann-Whitney U=0, r=1.0) on SWE-bench Verified by measuring solution diversity across independent sessions — a powerful black-box method, but currently validated only on coding tasks (9 SWE-bench problems, 45 trials) and relying on temperature-0 determinism that may not generalize to knowledge/reasoning benchmarks with inherent answer variability. Hardy et al. (arXiv 2603.24999, March 2026) introduce nonparametric signed isotonic R² scalability coefficients that outperform IRT-based item diagnostics for detecting bad benchmark items on HS Math, GSM8K, and MMLU — lightweight (bivariate monotone fits in seconds) and robust under small-n/large-p conditions; this complements our IRT-based quality control by providing a fast model-agnostic pre-filter for item quality before parametric calibration. On proactive contamination prevention: Sander et al. (arXiv 2502.17259, Feb 2025) propose watermarking benchmarks before release, reformulating questions with a watermarked LLM and detecting 'radioactivity' traces via statistical tests; validated on ARC and MMLU with 1B models, this represents a fundamentally different paradigm (prevention at release time vs. post-hoc detection and remediation). Our approach is complementary: watermarking prevents future contamination, while our pipeline detects and remediates existing contamination in already-deployed benchmarks — the two could be combined in a defense-in-depth strategy. On contamination detection: ConStat (2024) provides performance-based detection with formal FDR control; shortcut neuron analysis (ACL 2025) can isolate contamination to ~1.1-1.4% of neurons with only ~3% false positive impact; 'Test of Time' (arXiv 2025) demonstrates temporal signals are unreliable as standalone contamination indicators. CRITICALLY, 'On The Fragility of Benchmark Contamination Detection in Reasoning Models' (Wang et al., arXiv 2510.02386, ICLR 2026) systematically demonstrates that GRPO/PPO-style RL training conceals contamination signals: reference-free methods show AUROC degradation of 14-20 percentage points after only ~156 GRPO steps (Loss: 14.22pp drop from 75.48% to 61.26%; Min-K%: 16.42pp drop from 74.96% to 58.54%; Max-K%: 19.84pp drop from 69.83% to 49.99% — essentially random), while perturbation-based methods show different degradation patterns. The concealment mechanism is PPO's clipping objective, which contracts the NLL gap between contaminated and clean items. Self-Critique (Tao et al., arXiv 2510.09259, ICLR 2026) partially addresses this via policy-collapse detection but remains an individual-model-level method. DVD (Liang et al., arXiv 2601.04895, Jan 2026) introduces detection via variance of generation distribution and is specifically designed for variant contamination, achieving 0.73-0.74 AUC where Min-K%++ achieves only 0.43-0.68; however, DVD was validated only on SFT-contaminated models and its behavior under RL training is untested. On task familiarity vs. contamination: Wang & Heckel (arXiv 2603.12875, March 2026) show that test-time RL alignment (TTRA) closes the performance gap between base and fine-tuned models by ~27 percentage points on average, suggesting many reported fine-tuning gains are task familiarity artifacts rather than genuine capability improvements; this has a dual implication — it strengthens the need for item-specific contamination detection (since task familiarity produces uniform improvements with no DIF signal, while contamination produces item-specific advantages that DIF detects), but also suggests that contamination-driven DIF effects may be partially confounded with format-familiarity effects that TTRA could remove. On item generation: arXiv 2602.06631 shows LLMs achieve only rho=0.10-0.45 for difficulty estimation, but student simulation approaches (arXiv 2601.09953) achieve r=0.75-0.82 and multi-agent frameworks like ReQUESTA improve discrimination from 0.17 to 0.39. On IRT methodology: bifactor models with Projective IRT (PIRT) enable equating of multidimensional tests while remaining tractable; fixed-parameter calibration requires only N>=200 examinees vs N>=500 for full calibration (Kim & Kolen, 2019); the OH2PL (König, Spoden, & Frey, 2020) achieves unbiased estimates at N>=50 using optimized Bayesian hierarchical priors. No existing work closes the full loop from multi-signal contamination detection (robust to RL-trained models) through construct-constrained generation to bifactor IRT-equated regeneration with graceful-degradation guarantees.

## Approach
Build a closed-loop pipeline with three stages plus a formal graceful-degradation framework, each substantially revised to address known limitations:

**Stage 1: Multi-Signal Contamination Sentinel (with RL-Robustness Guarantees).** Deploy an ensemble of five complementary detection signals, explicitly designed so that at least two signals remain informative even against RL-trained reasoning models:

(a) *ConStat-style perturbation testing* — compare model performance on original items vs. semantically-equivalent reformulations, with formal False Discovery Rate (FDR) control. NOTE: Wang et al. (ICLR 2026) show reference-free detectors degrade 14-20pp under RL training (Loss: 14.22pp, Min-K%: 16.42pp, Max-K%: 19.84pp after ~156 GRPO steps); we retain perturbation testing as effective against non-RL models (which still constitute the majority of the model ecosystem) but do not rely on it alone.

(b) *Differential Item Functioning (DIF) across model release cohorts* — a novel application treating model release date as a grouping variable and flagging items that become differentially easier for newer cohorts beyond what general ability gains predict. **This is our primary RL-robust signal.** The key argument: DIF operates on group-level statistical patterns (comparing Item Characteristic Curves across model cohorts matched on overall ability), not individual output distributions. Wang et al. prove that PPO/GRPO clipping contracts the NLL gap *within a single model* between seen and unseen items — but DIF does not examine within-model NLL gaps. It detects whether the structural relationship between ability and item response differs across groups. A contaminated cohort shows anomalous ICCs on specific items regardless of how smooth individual output distributions appear, because contamination must, by definition, create differential item advantage — the one signal RL cannot conceal without negating the purpose of contamination. Furthermore, DIF leverages IRT's invariance principle: item parameters should be group-invariant after controlling for ability, and systematic DIF violations on specific items constitute contamination evidence that is orthogonal to all 10 methods shown to fail.

**Analytical Demonstration of DIF RL-Robustness.** Consider a concrete scenario: 200 binary items evaluated by two annual model cohorts (pre-2026, post-2026) with N=80 models each. Suppose 20 items are contaminated in the newer cohort, boosting P(correct) from 0.50 to 0.80 on those items (δ≈1.4 logits — a conservative estimate given GSM1K's documented 13% average accuracy drop across models, which implies item-level boosts of 20-40% on memorized items for heavily contaminated models). RL smoothing via GRPO/PPO contracts the NLL gap between contaminated and clean items within each individual model's output distribution — this is the mechanism Wang et al. demonstrate. However, the 30-percentage-point accuracy advantage on contaminated items persists at the behavioral level: RL training does not cause models to answer memorized items incorrectly, because doing so would negate the purpose of contamination. Logistic regression DIF with sum-score matching compares the probability of correctly answering each item across the two cohorts, conditioning on total score (overall ability). On the 180 uncontaminated items, both cohorts show similar ICCs after controlling for ability. On the 20 contaminated items, the newer cohort shows systematically higher probability of correct response at every matched ability level — large uniform DIF (ETS Category C: |Δ_MH| = -2.35 × ln(odds ratio) = -2.35 × ln(4.0) ≈ 3.3 delta units, far exceeding the C threshold of 1.5). This differential pattern is detectable because DIF examines between-group item-level performance conditional on ability, not within-model output distributions. RL smoothing is irrelevant to DIF: it modifies how confidently a model generates its answer (the NLL surface), not whether it gets the answer right or wrong (the binary response pattern that DIF analyzes).

**Quantitative DIF Power Analysis.** Independent simulation evidence (PMC5978487) establishes that logistic regression DIF at N=50/group achieves 14.4% power for small effects (δ=0.4) and 31.0% for medium effects (δ=0.6); at N=100/group, these rise to 24.7% and 55.2% respectively. These figures appear concerning for small-sample detection, but benchmark contamination typically produces large effects: GSM1K documents 10-13% average accuracy drops from contamination across models, corresponding to item-level δ≈0.8-1.4 logits on memorized items. DIF power scales super-linearly with effect size; at δ=1.4 with N=80/group (annual cohorts), power is estimated at 60-85% based on extrapolation from PMC5978487 simulation curves, consistent with the general finding that the likelihood ratio test achieves the highest statistical power in most DIF configurations. Furthermore, three factors substantially improve effective power beyond these baseline estimates: (i) cumulative Bayesian priors (Sinharay et al., 2006) accumulate evidence across successive benchmark administrations, borrowing strength from previous DIF estimates to improve detection over time — particularly effective for persistent contamination that affects multiple administrations; (ii) Item-Focused Trees (Tutz & Berger, 2016) avoid arbitrary categorical group splits by treating release date as a continuous covariate, leveraging the full model sample (N=160 rather than two groups of 80) and letting the method identify natural breakpoints where DIF emerges; (iii) the 2-of-5 ensemble voting threshold means even 40-50% individual DIF power yields acceptable ensemble sensitivity when combined with DVD and ConStat signals on non-RL models. We acknowledge that DIF alone is underpowered for small contamination effects (δ<0.6); its value lies in detecting the large effects that matter most for benchmark validity, complemented by other ensemble signals for smaller effects.

**Interaction with Task Familiarity Artifacts.** Wang & Heckel (arXiv 2603.12875, March 2026) demonstrate that test-time RL alignment (TTRA) closes the performance gap between base and fine-tuned models by ~27 percentage points on average, suggesting many reported fine-tuning gains reflect task familiarity rather than genuine capability. This has a dual implication for DIF-based detection. First, it *strengthens* the DIF rationale: task familiarity artifacts produce uniform improvements across all items (no DIF signal), while memorization-based contamination produces item-specific advantages (DIF signal) — DIF thus provides a principled way to distinguish the two, a distinction no other detection method explicitly makes. Second, it introduces a nuance: if some contamination manifests partially as enhanced task-format familiarity rather than item-specific memorization, the item-level DIF effect sizes may be modestly smaller than the raw accuracy gaps suggest. We address this by: (a) noting that DIF would be computed on models as deployed (without TTRA), since TTRA is an analysis tool, not a standard deployment procedure; (b) observing that DIF controls for overall ability via sum-score matching, so any uniform familiarity-driven improvements are absorbed into the ability estimate, leaving item-specific contamination signals intact; (c) reporting DIF effect sizes with uncertainty intervals rather than relying on significance thresholds alone, making the analysis transparent about power limitations.

**DIF Small-Sample Strategy (detailed).** Classical DIF methods (Mantel-Haenszel, logistic regression) require N≥200 per group for optimal performance (Mazor et al., 1992; Scott et al., 2009), far exceeding our ~10-20 models per quarterly cohort. We address this through a four-pronged strategy: (i) *Temporal aggregation*: use semi-annual or annual cohorts rather than quarterly, yielding N=40-80 per group; as the model ecosystem grows (~100+ new models per year as of 2026), annual cohorts will approach the N≥100 threshold where regularized methods become viable. (ii) *Cumulative Bayesian DIF*: following Sinharay et al. (2006, ETS), use DIF estimates from previous benchmark administrations as informative priors for new cohorts, accumulating statistical power over time rather than analyzing each cohort in isolation. (iii) *Item-Focused Trees* (Tutz & Berger, 2016): treat release date as a continuous covariate rather than creating arbitrary categorical cohorts, letting the method identify natural breakpoints where DIF emerges — this avoids the small-group problem entirely while leveraging the full model sample. (iv) *Parsimonious models*: following Belzak (2020, Multivariate Behavioral Research), use logistic regression with sum scores rather than complex IRT models for DIF detection, as simpler models outperform complex ones in small samples even when misspecified. We report DIF effect sizes (ETS delta classification: A/B/C, where C indicates |Δ_MH|≥1.5) with uncertainty intervals rather than relying solely on significance tests, acknowledging power limitations transparently.

(c) *IRT aberrance detection* — flag items whose observed easiness significantly exceeds calibrated difficulty, used as one signal among several rather than a standalone detector.

(d) *DVD-style generation variance testing* (adapted from Liang et al., arXiv 2601.04895) — for models with inference access, generate 50 responses per item via temperature sampling and compute the variance of synthetic-difficulty scores. Contaminated items exhibit bimodal generation distributions (alternating between memorized templates and free generation) yielding high variance, while clean items show unimodal low-variance distributions. This specifically detects variant contamination (paraphrased/restructured benchmark items) where ConStat and Min-K% fail (AUC 0.43-0.68 vs. DVD's 0.73-0.74). NOTE: DVD is promising but untested against RL-trained models — it was validated only on SFT-contaminated models (Qwen2.5, Llama3.1 fine-tuned). Whether the bimodal variance signature persists after GRPO/PPO training is an open empirical question that our RL-contamination experimental condition will directly test. DVD's value in the ensemble is therefore primarily for detecting variant contamination in the non-RL model majority, with DIF providing the RL-robust complement.

(e) *Membership-inference probes* (Min-K% Prob / ReCaLL) where white-box access is available — retained as a cheap first-pass filter effective against non-RL models, but explicitly acknowledged as fragile against GRPO/PPO-trained models per Wang et al. (AUROC drops to ~50% after ~156 GRPO steps).

Trigger regeneration when an item is flagged by >= 2 independent signals, with FDR-controlled thresholds. The ensemble is explicitly designed so that DIF (group-level, analytically RL-robust as demonstrated above) and DVD (generation-variance, variant-robust on SFT models) provide coverage where individual-level methods fail. Genuine capability gains will produce uniform improvement across original and perturbed items (no ConStat signal), across cohorts controlling for ability (no DIF signal), and across temperature samples (no DVD signal), while contamination produces item-specific anomalies in at least two of these dimensions.

**Stage 2: Construct-Constrained Generation with Empirical Calibration.** Critically, we abandon the original approach of conditioning generators on raw IRT parameters — research shows LLMs achieve only rho=0.10-0.45 correlation with actual difficulty (arXiv 2602.06631). Instead: (a) For each flagged item, prompt a frontier generator (DeepSeek-V4-Pro or Qwen-3.5-397B) conditioned on the item's construct tag, cognitive complexity level (Bloom's taxonomy), format template, and 3-5 exemplar items from the same difficulty band — but NOT explicit IRT parameters; (b) Generate 8-10 candidates per flagged item using a multi-agent framework (generator + evaluator + refiner) inspired by ReQUESTA, with iterative critique loops; (c) Pre-screen candidates using student simulation — have a diverse panel of weaker/mid-tier LLMs (4B-14B parameters) role-play as examinees at varying ability levels, estimating approximate difficulty via simulated IRT (achieving r=0.75-0.82 per arXiv 2601.09953), and discard candidates whose estimated difficulty deviates by >1.5 logits from the target; (d) Optionally pre-filter candidates using Hardy et al.'s signed isotonic R² scalability coefficients (arXiv 2603.24999) as a fast, nonparametric quality check — items with anomalously low scalability coefficients (indicating poor construct alignment) are discarded before expensive panel calibration; (e) Empirically calibrate surviving candidates on the full calibration panel of 200-300 diverse LLMs via Bayesian fixed-parameter calibration (OH2PL, König, Spoden, & Frey, 2020), anchored to a preserved clean set (>= 20% of items, following the Kolen & Brennan 20% rule for stable equating). This generate-screen-calibrate pipeline is expected to achieve 30-50% rejection rates based on analogous AIG literature; we report convergence statistics as a key empirical contribution.

**Stage 3: Bifactor IRT Equating Gate.** Move from naive unidimensional 2PL to a bifactor model (general LLM ability + domain-specific factors), which captures the inherently multi-construct nature of benchmarks like MMLU while remaining tractable for equating. Use Projective IRT (PIRT) to project bifactor parameters onto unidimensional equivalents compatible with standard equating software (demonstrated to produce very similar equating outcomes to full numerical integration, with practical advantages for implementation; Kim, 2022). Accept only replacements whose projected difficulty and discrimination fall within the 95% CI of the original item's parameters. Verify that the regenerated benchmark's test information function, construct coverage vector, and model ranking (Spearman rho >= 0.95) match the pre-contamination gold standard. Reject and re-generate otherwise, with a maximum of 3 regeneration cycles per item before flagging for human review.

**Graceful Degradation Framework.** We define formal validity boundaries and fallback strategies for each failure mode, grounded in the test equating literature (Kolen & Brennan, 2004; Angoff, 1984):

(i) *Anchor set integrity*: Maintain a minimum of 20% clean (uncontaminated) anchor items. If contamination detection flags items bringing the clean set below 20%, enter a degraded-but-valid operating mode: switch from standard Stocking-Lord equating to robust Area-Weighted or Least Absolute Values (LAV) equating methods (which tolerate outlying anchor items) and widen acceptance CIs to 99%. If the clean set drops below 15%, halt automated regeneration and flag the entire benchmark version for human review and potential full re-calibration. Below 10%, do not release.

(ii) *Stage 1 error propagation*: False positives (flagging clean items as contaminated) trigger unnecessary regeneration but do not compromise validity — the equating gate (Stage 3) ensures replacements are psychometrically equivalent regardless of whether the original was truly contaminated. False negatives (missing contaminated items) are the more dangerous failure mode; we mitigate this by requiring only 2-of-5 signal agreement, with the understanding that DIF and DVD provide complementary coverage against RL-concealment and variant contamination respectively.

(iii) *Stage 2 generation failure*: If <50% of candidates survive pre-screening for a given item (below the expected 50-70% survival rate), the system relaxes the logit-deviation threshold from 1.5 to 2.0 and generates a second batch of 8-10 candidates. If the item still fails after 3 regeneration cycles, it is flagged for human review but the benchmark continues operating with the original (potentially contaminated) item marked with a quality warning — preferable to reducing test length.

(iv) *Stage 3 equating failure*: If >15% of items fail the equating gate after all regeneration cycles (meaning the benchmark cannot be fully regenerated), we release a partial-regeneration version with: (a) adjusted test information function reported alongside all scores, (b) model rankings computed on both the full benchmark and the clean-items-only subset for comparison, (c) marginal reliability coefficient reported — release only if marginal reliability ≥ 0.80 for group-level comparisons (per APA standards). This partial-release strategy provides transparent validity information rather than silently degraded scores.

(v) *Minimum viable benchmark*: Formally, a regenerated benchmark version is released only if: marginal IRT reliability ≥ 0.80, Spearman rho ≥ 0.90 with the pre-contamination gold standard (relaxed from 0.95 in degraded mode), anchor set ≥ 15%, and SEM ≤ 0.35 across ≥ 70% of the target ability range. These thresholds are derived from operational testing standards (Kolen & Brennan, 2004) adapted for the LLM evaluation context where group-level comparisons (model rankings) are the primary use case.

**Evaluation Strategy.** Validate on three tiers: (a) Primary — LiveBench subsets (math, reasoning, coding) as currently-uncontaminated benchmarks with diverse task types and temporal structure; simulate contamination by fine-tuning open-weight models on specific LiveBench items at controlled rates (10-50%) and measuring detection sensitivity and ranking recovery. Critically, include an RL-contamination condition: apply GRPO fine-tuning (following Wang et al.'s protocol of ~156 steps on contaminated data) to open-weight models on benchmark items and verify that DIF-based detection remains effective while individual-level methods degrade — this directly tests the analytical demonstration's predictions. Additionally, test DVD's bimodal variance signature under RL contamination to determine whether it is robust, partially robust, or fragile (resolving the current empirical gap). (b) Secondary — MMLU-CF (the contamination-free MMLU replacement, ACL 2025) for knowledge-domain evaluation, running the full regeneration pipeline on synthetically contaminated subsets. (c) Positive control — use naturally-contaminated MMLU/GSM8K items (with documented contamination evidence from GSM1K studies) to verify that the contamination sentinel detects known real-world contamination. Additionally, include a **pilot feasibility study** on a single LiveBench math subset (~200 items): run the full generate-screen-calibrate-gate pipeline and report rejection rates, convergence speed, parameter recovery accuracy, ranking preservation, and graceful-degradation trigger rates — providing the first empirical evidence of generate-test-reject convergence for IRT-equated benchmark items.

## Resource Estimate
{'manual': {'gpu_hours': '900-1300 (inference of 200-300 models on ~5K items each for IRT calibration across multiple rounds, plus item generation with 70B+ models, plus student simulation panel, plus DVD temperature-sampling at 50 generations/item)', 'timeline': '5-6 months (1.5 months multi-signal contamination detector including DIF infrastructure and DVD adaptation, 1.5 months bifactor IRT calibration infrastructure, 1.5 months generation pipeline with student simulation, 1.5 months experiments including RL-contamination condition, pilot feasibility study, and writing)', 'estimated_gpu_cost': '$1800-$2600 at ~$2/hr H100 spot pricing', 'closed_source_api_cost': '$800-$2000 (API calls for ~30-50 closed-source models in calibration panel: GPT-4o, Claude, Gemini, etc. at ~5K items each, plus student simulation inference, plus DVD temperature-sampling for closed-source models)'}, 'human_in_loop': {'gpu_hours': '800-1100 (same inference needs, Claude handles generation orchestration, IRT analysis code, DIF implementation, and DVD adaptation)', 'timeline': '3.5-4.5 months (Claude drafts contamination detection, equating code, DIF pipeline, and student simulation; human validates IRT assumptions, bifactor model specification, DIF power analysis, and experimental design)', 'claude_api_cost': '$400-$700 (Sonnet 4.6 for code generation and pipeline orchestration, ~120M tokens total with caching)', 'estimated_gpu_cost': '$1600-$2200', 'closed_source_api_cost': '$800-$2000'}, 'auto_research': {'gpu_hours': '900-1200 (cannot reduce inference needs for 200-300 model calibration panel; DVD temperature-sampling adds ~10% overhead)', 'timeline': '8-12 weeks (parallelized model evaluation is the critical path; 200-300 model panel requires ~3 weeks per calibration round even with full parallelism; pilot feasibility study adds ~2 weeks; RL-contamination condition adds ~1 week for GRPO training)', 'claude_api_cost': '$800-$1200 (Opus 4.7 for experimental design and IRT analysis, Sonnet 4.6 for implementation, ~180M tokens with caching)', 'estimated_gpu_cost': '$1800-$2400', 'closed_source_api_cost': '$800-$2000', 'speed_bottleneck': 'IRT calibration panel: collecting responses from 200-300 diverse LLMs on pilot items requires sequential API calls to closed-source models (rate limits) and batched inference on open-weight models (GPU scheduling). Minimum ~3 weeks for a single calibration round with full parallelism across ~150 open-weight models and ~50 closed-source APIs. The pilot feasibility study requires at least 2 full calibration rounds. DVD temperature-sampling (50 generations/item) adds ~10% to inference costs.'}}

## Inspired By
Field guide finding that 'contamination resistance degrades question fidelity'; gap between dynamic evaluation (LiveBench, DyVal) and psychometric rigor (IRT, ATLAS); cross-domain transfer of IRT equating from educational testing to benchmark maintenance; arXiv 2602.06631's demonstration that LLMs cannot directly target difficulty parameters, motivating empirical calibration; 'Test of Time' (2025) showing temporal contamination signals are unreliable, motivating multi-signal approaches; Wang et al. (ICLR 2026) showing RL conceals all individual-level contamination signals, motivating group-level DIF analysis; Wang & Heckel (2026) showing task familiarity artifacts produce uniform improvements distinguishable from item-specific contamination via DIF; DVD's demonstration that variant contamination requires specialized detection signals; Hardy et al.'s signed isotonic R² as a lightweight pre-filter complementing parametric IRT; Sander et al.'s watermarking paradigm motivating a complementary post-hoc remediation approach; bifactor IRT and PIRT as a practical bridge between unidimensional oversimplification and intractable full MIRT; Kolen & Brennan's anchor-set theory providing formal graceful-degradation thresholds.

## Target Venues
- ICLR 2027 (deadline expected ~October 2026 based on historical pattern — not yet announced; ideal timeline for thorough experiments including pilot feasibility study and RL-contamination condition; PRIMARY TARGET)
- AAAI 2027 (abstract July 21, paper July 28, 2026 — tight but feasible if pilot study is scoped to single domain; 2 months)
- EACL 2027 via ARR August 2026 cycle (submission August 3, 2026 — feasible with focused experiments on LiveBench math subset)

## Key References
- LiveBench: A Challenging, Contamination-Free LLM Benchmark (ICLR 2025)
- LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code (ICLR 2025)
- Automating Benchmark Design [BeTaL] (ICLR 2026)
- BenchBench: Benchmarking Automated Benchmark Generation (arXiv 2026)
- Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration (arXiv April 2026)
- Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory [PSN-IRT] (AAAI 2026 Oral)
- The stability of IRT parameters under several test equating conditions (Frontiers in Psychology 2026)
- Estimating Exam Item Difficulty with LLMs: A Benchmark on Brazil's ENEM Corpus (arXiv 2602.06631, Feb 2026)
- Take Out Your Calculators: Estimating Real Difficulty with LLM Student Simulations (arXiv 2601.09953, Jan 2026)
- Reconstructing Item Characteristic Curves with Fine-Tuned LLMs (arXiv 2601.02580, Jan 2026)
- ReQUESTA: Hybrid Multi-Agent Framework for MCQ Generation (arXiv 2602.03704, Feb 2026)
- Test of Time: Rethinking Temporal Signal of Benchmark Contamination (arXiv 2509.00072, 2025)
- ConStat: Performance-Based Contamination Detection with FDR Control (ETH Zurich 2024)
- Establishing Trustworthy LLM Evaluation via Shortcut Neuron Analysis (ACL 2025)
- On The Fragility of Benchmark Contamination Detection in Reasoning Models (Wang et al., arXiv 2510.02386, ICLR 2026)
- Detecting Data Contamination from Reinforcement Learning Post-training [Self-Critique / RL-MIA] (Tao et al., arXiv 2510.09259, ICLR 2026)
- DVD: Detection via Variance of Generation Distribution for Variant Contamination (Liang et al., arXiv 2601.04895, Jan 2026)
- Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis [CCV] (arXiv 2603.21454, March 2026)
- Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients (Hardy et al., arXiv 2603.24999, March 2026)
- Detecting Benchmark Contamination Through Watermarking (Sander et al., arXiv 2502.17259, Feb 2025)
- Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks (Wang & Heckel, arXiv 2603.12875, March 2026)
- Application of IRT Fixed Parameter Calibration to Multiple-Group Test Data (Kim & Kolen, Applied Measurement in Education 2019)
- An Optimized Bayesian Hierarchical Two-Parameter Logistic Model for Small-Sample Item Calibration [OH2PL] (König, Spoden, & Frey, Applied Psychological Measurement 2020, PMC7262992)
- Robustness of the OH2PL for Small-Sample Item Calibration (König, Spoden, & Frey, Behavior Research Methods 2022)
- Approximating Bifactor IRT Equating with Projective IRT [PIRT] (PMC 2020)
- Item Response Theory True Score Equating for the Bifactor Model (Kim, Journal of Educational Measurement 2022)
- Several Variations of Simple-Structure MIRT Equating (Kim, Journal of Educational Measurement 2023)
- MMLU-CF: A Contamination-Free Multi-task Language Understanding Benchmark (ACL 2025)
- Simulating Training Data Leakage in Multiple-Choice Benchmarks (arXiv 2505.24263, 2025)
- VarBench: Robust Language Model Benchmarking Through Dynamic Variable Perturbation (EMNLP 2024)
- DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks (ICLR 2024)
- RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning (arXiv 2025)
- Adaptive Testing for LLM Evaluation [ATLAS] (arXiv 2025)
- Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation (EMNLP 2025)
- Automatic- and Transformer-Based AIG: A Critical Review (Sommer & Arendasy, Intelligence 2025)
- Can LLMs Estimate Student Struggles? The Curse of Knowledge Effect (arXiv 2512.18880, 2025)
- Quantifying Data Contamination in Psychometric Evaluations of LLMs (Han et al., arXiv 2510.07175, 2025)
- Using Past Data to Enhance Small-Sample DIF Estimation: A Bayesian Approach (Sinharay et al., ETS Research Report RR-06-09, 2006)
- Testing Differential Item Functioning in Small Samples (Belzak, Multivariate Behavioral Research 2020)
- Item-Focused Trees for the Detection of Differential Item Functioning (Tutz & Berger, Psychometrika 2016)
- Test Equating, Scaling, and Linking: Methods and Practices 3rd ed. (Kolen & Brennan, Springer 2014)
- A Careful Examination of Large Language Model Performance on Grade School Arithmetic [GSM1K] (arXiv 2405.00332, 2024)
- Power and Sample Size Calculations for Logistic Regression Tests for Differential Item Functioning (PMC5978487)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "6cc66108-81d2-49b2-977a-aa0548bb7fe1",
  "type": "user",
  "uuid": "0ddf393d-52d7-40ff-83b2-91dc73ba8ee4",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:32:36.138Z_

```json
{
  "parentUuid": "0ddf393d-52d7-40ff-83b2-91dc73ba8ee4",
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
  "uuid": "629e8199-e034-4042-ae6c-41fd28043d1d",
  "timestamp": "2026-05-20T04:32:36.138Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:32:36.138Z_

```json
{
  "parentUuid": "629e8199-e034-4042-ae6c-41fd28043d1d",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "396d4cf9-7b21-43cf-a43d-e5655cf0e350",
  "timestamp": "2026-05-20T04:32:36.138Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-20T04:32:36.138Z_

```json
{
  "parentUuid": "396d4cf9-7b21-43cf-a43d-e5655cf0e350",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "200e0cad-fd7b-4219-94b7-21c82450432c",
  "timestamp": "2026-05-20T04:32:36.138Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Contamination-Triggered Benchmark Regeneration with Bifactor IRT Equating  ## Description We propose a self-heal…",
  "leafUuid": "200e0cad-fd7b-4219-94b7-21c82450432c",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Self-healing benchmarks with DIF-robust contamination detection",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e"
}
```

---

### Assistant

_source line 9 · 2026-05-20T04:32:43.776Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for EMNLP 2026 submission potential. This is a detailed proposal about "Contamination-Triggered Benchmark Regeneration with Bifactor IRT Equating." 

Let me first do the required web searches to understand the current landscape before making any judgments. I need to search for:

1. Recent work on benchmark contamination detection, especially for RL-trained models
2. IRT-based benchmark evaluation and equating for LLMs
3. Dynamic benchmark regeneration approaches
4. DIF (Differential Item Functioning) applied to LLM evaluation


5. The specific papers cited in the proposal

Now I'll start running these targeted searches to get a sense of what's already out there in this space.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "200e0cad-fd7b-4219-94b7-21c82450432c",
  "isSidechain": false,
  "requestId": "req_011CbDCH7i5uGgZeqqJuqBNr",
  "type": "assistant",
  "uuid": "45d7878a-4a0c-48b9-99c6-9beb86e78ece",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WueLxQ3vqbjN55gncDdgma",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12446,
      "cache_read_input_tokens": 13939,
      "output_tokens": 274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12446,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 274,
          "cache_read_input_tokens": 13939,
          "cache_creation_input_tokens": 12446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12446
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

_source line 10 · 2026-05-20T04:32:43.780Z_

I need to conduct thorough literature research before evaluating this proposal. Let me start with targeted web searches across the key topics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45d7878a-4a0c-48b9-99c6-9beb86e78ece",
  "isSidechain": false,
  "requestId": "req_011CbDCH7i5uGgZeqqJuqBNr",
  "type": "assistant",
  "uuid": "1cf0ee41-72e5-4d62-a56d-e847600510e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WueLxQ3vqbjN55gncDdgma",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12446,
      "cache_read_input_tokens": 13939,
      "output_tokens": 274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12446,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 274,
          "cache_read_input_tokens": 13939,
          "cache_creation_input_tokens": 12446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12446
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

_source line 11 · 2026-05-20T04:32:43.783Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PJeUeJGxEdh5pXb4GAyCc7`</summary>

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
  "parentUuid": "1cf0ee41-72e5-4d62-a56d-e847600510e4",
  "isSidechain": false,
  "requestId": "req_011CbDCH7i5uGgZeqqJuqBNr",
  "type": "assistant",
  "uuid": "d05f3beb-db6c-49eb-8002-e23f8bf54038",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WueLxQ3vqbjN55gncDdgma",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12446,
      "cache_read_input_tokens": 13939,
      "output_tokens": 274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12446,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 274,
          "cache_read_input_tokens": 13939,
          "cache_creation_input_tokens": 12446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12446
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

_source line 12 · 2026-05-20T04:32:43.792Z_

<details><summary>↩ Tool result · `toolu_01PJeUeJGxEdh5pXb4GAyCc7`</summary>

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
  "parentUuid": "d05f3beb-db6c-49eb-8002-e23f8bf54038",
  "isSidechain": false,
  "promptId": "6cc66108-81d2-49b2-977a-aa0548bb7fe1",
  "type": "user",
  "uuid": "9a40ec6e-79f1-49ea-8309-21f5a63a094e",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "d05f3beb-db6c-49eb-8002-e23f8bf54038",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-20T04:32:46.659Z_

Now let me conduct the required literature searches. I'll run multiple searches in parallel to cover the key areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a40ec6e-79f1-49ea-8309-21f5a63a094e",
  "isSidechain": false,
  "requestId": "req_011CbDCHgoQrg81uZ5R13zRv",
  "type": "assistant",
  "uuid": "a6b79070-51ca-42da-a75c-b844e7fc4ade",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Via5tJm7torcX3Y9i5BXs6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 799,
      "cache_read_input_tokens": 26385,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 799,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 97,
          "cache_read_input_tokens": 26385,
          "cache_creation_input_tokens": 799,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 799
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

_source line 14 · 2026-05-20T04:32:47.252Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q8Z5eGzUjdDEahkbvZAe8i`</summary>

```json
{
  "query": "benchmark contamination detection RL reasoning models 2025 2026 fragility Wang ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6b79070-51ca-42da-a75c-b844e7fc4ade",
  "isSidechain": false,
  "requestId": "req_011CbDCHgoQrg81uZ5R13zRv",
  "type": "assistant",
  "uuid": "26237007-fc5f-4672-8069-39c685518c09",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Via5tJm7torcX3Y9i5BXs6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 799,
      "cache_read_input_tokens": 26385,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 799,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 97,
          "cache_read_input_tokens": 26385,
          "cache_creation_input_tokens": 799,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 799
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

_source line 15 · 2026-05-20T04:32:54.690Z_

<details><summary>↩ Tool result · `toolu_01Q8Z5eGzUjdDEahkbvZAe8i`</summary>

```text
Web search results for query: "benchmark contamination detection RL reasoning models 2025 2026 fragility Wang ICLR"

Links: [{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/pdf/2510.02386"},{"title":"[2510.02386] On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/abs/2510.02386"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=bhR00j6Mku"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/html/2510.02386v1"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://www.researchgate.net/publication/396223620_On_The_Fragility_of_Benchmark_Contamination_Detection_in_Reasoning_Models"},{"title":"gies for llm benchmark data contamination - Gang Wang","url":"https://gangw.cs.illinois.edu/cvpr_Emperor25.pdf"}]

Based on the search results, I found the paper you were looking for:

## On The Fragility of Benchmark Contamination Detection in Reasoning Models

This paper is by Han Wang and 3 other authors, and it addresses critical vulnerabilities in benchmark contamination detection for Large Reasoning Models (LRMs).

### Key Findings:

The study finds that evading contamination detections for LRMs is alarmingly easy. When a base model evolves into an LRM via SFT and RL, contamination during SFT can initially be identified by contamination detection methods, yet even a brief GRPO (Group Relative Policy Optimization) training can markedly conceal contamination signals that most detection methods rely on.

The work reveals that RL fine-tuning can conceal benchmark contamination when base models evolve into LRMs, and contamination with CoT (chain-of-thought) applied to advanced LRMs leaves little evidence detectable by existing memorization-based methods.

The paper notes that PPO style importance sampling and clipping objectives are the root cause of this detection concealment, indicating that a broad class of RL methods may inherently exhibit similar properties.

The paper appears to be from September 2025 and is under review or has been published in the ICLR 2025 venue or related workshops.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26237007-fc5f-4672-8069-39c685518c09",
  "isSidechain": false,
  "promptId": "6cc66108-81d2-49b2-977a-aa0548bb7fe1",
  "type": "user",
  "uuid": "0172ba83-edcc-4fe9-9599-867bbbbcf7df",
  "toolUseResult": {
    "query": "benchmark contamination detection RL reasoning models 2025 2026 fragility Wang ICLR",
    "results": [
      {
        "tool_use_id": "srvtoolu_01F9cpfeWcsc8JFDSPBuBobC",
        "content": [
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/pdf/2510.02386"
          },
          {
            "title": "[2510.02386] On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/abs/2510.02386"
          },
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models | OpenReview",
            "url": "https://openreview.net/forum?id=bhR00j6Mku"
          },
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/html/2510.02386v1"
          },
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://www.researchgate.net/publication/396223620_On_The_Fragility_of_Benchmark_Contamination_Detection_in_Reasoning_Models"
          },
          {
            "title": "gies for llm benchmark data contamination - Gang Wang",
            "url": "https://gangw.cs.illinois.edu/cvpr_Emperor25.pdf"
          }
        ]
      },
      "Based on the search results, I found the paper you were looking for:\n\n## On The Fragility of Benchmark Contamination Detection in Reasoning Models\n\nThis paper is by Han Wang and 3 other authors, and it addresses critical vulnerabilities in benchmark contamination detection for Large Reasoning Models (LRMs).\n\n### Key Findings:\n\nThe study finds that evading contamination detections for LRMs is alarmingly easy. When a base model evolves into an LRM via SFT and RL, contamination during SFT can initially be identified by contamination detection methods, yet even a brief GRPO (Group Relative Policy Optimization) training can markedly conceal contamination signals that most detection methods rely on.\n\nThe work reveals that RL fine-tuning can conceal benchmark contamination when base models evolve into LRMs, and contamination with CoT (chain-of-thought) applied to advanced LRMs leaves little evidence detectable by existing memorization-based methods.\n\nThe paper notes that PPO style importance sampling and clipping objectives are the root cause of this detection concealment, indicating that a broad class of RL methods may inherently exhibit similar properties.\n\nThe paper appears to be from September 2025 and is under review or has been published in the ICLR 2025 venue or related workshops."
    ],
    "durationSeconds": 7.434191213000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "26237007-fc5f-4672-8069-39c685518c09",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T04:32:57.324Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CPH5r3wwhpB1etU7tvQWyt`</summary>

```json
{
  "query": "IRT equating LLM benchmark evaluation \"Growing Pains\" fixed parameter calibration 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0172ba83-edcc-4fe9-9599-867bbbbcf7df",
  "isSidechain": false,
  "requestId": "req_011CbDCJUt5u2zp1dtaXu934",
  "type": "assistant",
  "uuid": "6b1d3eb5-ac53-4b49-863a-265c6061538d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VYQ84u2AasKh9CAo3HLb72",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 27184,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 27184,
          "cache_creation_input_tokens": 729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 729
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

_source line 17 · 2026-05-20T04:33:06.585Z_

<details><summary>↩ Tool result · `toolu_01CPH5r3wwhpB1etU7tvQWyt`</summary>

```text
Web search results for query: "IRT equating LLM benchmark evaluation "Growing Pains" fixed parameter calibration 2026"

Links: [{"title":"[2604.12843] Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/abs/2604.12843"},{"title":"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/html/2604.12843"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/pdf/2511.04689"},{"title":"Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of Large Language Models in Medical Benchmarking","url":"https://arxiv.org/pdf/2603.23506"},{"title":"Estimating Exam Item Difficulty with LLMs: A Benchmark on Brazil's ENEM Corpus","url":"https://arxiv.org/pdf/2602.06631"},{"title":"Efficient Inference for Noisy LLM-as-a-Judge Evaluation","url":"https://arxiv.org/pdf/2601.05420"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/pdf/2505.15055"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/html/2511.04689"}]

I found relevant research on your query. Here are the key findings:

## "Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration"

The paper proposes a framework based on multidimensional Item Response Theory (IRT) that uses anchor items to calibrate new benchmarks to the evaluation suite while holding previously calibrated item parameters fixed.

The approach supports a realistic evaluation setting in which datasets are introduced over time and models are evaluated only on the datasets available at the time of evaluation, while a fixed anchor set for each dataset is used so that results from different evaluation periods can be compared directly.

In large-scale experiments on more than 400 models, the framework predicts full-evaluation performance within 2-3 percentage points using only 100 anchor questions per dataset, with Spearman ρ≥0.9 for ranking preservation.

The paper was published on April 15, 2026 on arXiv (paper ID: 2604.12843). This research addresses the challenge of efficiently evaluating the rapidly growing number of LLMs and benchmarks by using IRT-based equating methods with fixed parameter calibration.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b1d3eb5-ac53-4b49-863a-265c6061538d",
  "isSidechain": false,
  "promptId": "6cc66108-81d2-49b2-977a-aa0548bb7fe1",
  "type": "user",
  "uuid": "4170ce37-a4ea-461a-b8d5-92a363037bef",
  "toolUseResult": {
    "query": "IRT equating LLM benchmark evaluation \"Growing Pains\" fixed parameter calibration 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BiEe5mHzTfCrmtWEH9xHB3",
        "content": [
          {
            "title": "[2604.12843] Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration",
            "url": "https://arxiv.org/abs/2604.12843"
          },
          {
            "title": "Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration",
            "url": "https://arxiv.org/html/2604.12843"
          },
          {
            "title": "Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks",
            "url": "https://arxiv.org/pdf/2511.04689"
          },
          {
            "title": "Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of Large Language Models in Medical Benchmarking",
            "url": "https://arxiv.org/pdf/2603.23506"
          },
          {
            "title": "Estimating Exam Item Difficulty with LLMs: A Benchmark on Brazil's ENEM Corpus",
            "url": "https://arxiv.org/pdf/2602.06631"
          },
          {
            "title": "Efficient Inference for Noisy LLM-as-a-Judge Evaluation",
            "url": "https://arxiv.org/pdf/2601.05420"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/pdf/2505.15055"
          },
          {
            "title": "Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks",
            "url": "https://arxiv.org/html/2511.04689"
          }
        ]
      },
      "I found relevant research on your query. Here are the key findings:\n\n## \"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration\"\n\nThe paper proposes a framework based on multidimensional Item Response Theory (IRT) that uses anchor items to calibrate new benchmarks to the evaluation suite while holding previously calibrated item parameters fixed.\n\nThe approach supports a realistic evaluation setting in which datasets are introduced over time and models are evaluated only on the datasets available at the time of evaluation, while a fixed anchor set for each dataset is used so that results from different evaluation periods can be compared directly.\n\nIn large-scale experiments on more than 400 models, the framework predicts full-evaluation performance within 2-3 percentage points using only 100 anchor questions per dataset, with Spearman ρ≥0.9 for ranking preservation.\n\nThe paper was published on April 15, 2026 on arXiv (paper ID: 2604.12843). This research addresses the challenge of efficiently evaluating the rapidly growing number of LLMs and benchmarks by using IRT-based equating methods with fixed parameter calibration."
    ],
    "durationSeconds": 9.256897956000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6b1d3eb5-ac53-4b49-863a-265c6061538d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T04:33:09.270Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0187AUDhHij8JtjEyAVpAfN4`</summary>

```json
{
  "query": "Differential Item Functioning DIF LLM evaluation benchmark contamination detection novel 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4170ce37-a4ea-461a-b8d5-92a363037bef",
  "isSidechain": false,
  "requestId": "req_011CbDCKMkjp6oRTR2xAXcBW",
  "type": "assistant",
  "uuid": "d75607e3-8a87-4274-a143-4f3cdb8cf628",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T2kqg2TsS28FE43TJxo18r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 753,
      "cache_read_input_tokens": 27913,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 753,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 27913,
          "cache_creation_input_tokens": 753,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 753
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

_source line 19 · 2026-05-20T04:33:16.995Z_

<details><summary>↩ Tool result · `toolu_0187AUDhHij8JtjEyAVpAfN4`</summary>

```text
Web search results for query: "Differential Item Functioning DIF LLM evaluation benchmark contamination detection novel 2025 2026"

Links: [{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"},{"title":"DVD: A Robust Method for Detecting Variant Contamination in Large Language Model Evaluation","url":"https://arxiv.org/pdf/2601.04895"},{"title":"Detecting Benchmark Contamination Through Watermarking","url":"https://arxiv.org/pdf/2502.17259"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/pdf/2510.02386"},{"title":"NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination   for each Benchmark","url":"https://arxiv.org/pdf/2310.18018"},{"title":"A Log-Linear Modeling Approach for Differential Item Functioning Detection in Polytomously Scored Items - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC6943994/"},{"title":"Towards Contamination Resistant Benchmarks","url":"https://arxiv.org/pdf/2505.08389"}]

I found search results related to LLM benchmark contamination detection, but the results focus on contamination detection in large language model evaluation rather than on "Differential Item Functioning" (DIF) specifically in that context.

Here's what I found:

**LLM Benchmark Contamination Detection (2025-2026):**

Five detection methods work in 2026: time-based partition (the Codeforces cliff), Min-K% probability, the Time Travel guided-completion attack, ConStat performance gaps on rephrased samples, and BIG-Bench canary GUID memorization.

Even when training data contains only variants with no exact duplicates, models can achieve significantly inflated accuracy on evaluation benchmarks, and widely used contamination detection methods fail in this setting exhibiting unstable performance.

As LLMs have evolved into Large Reasoning Models (LRMs), benchmark contamination detection faces key challenges since LRMs rely on chain-of-thought reasoning, contamination evidence can be concealed through RL training, and extensive contamination with CoT on advanced LRMs barely leaves evidence for existing memorization-based detection methods.

**Note:** The search results do not contain information specifically connecting Differential Item Functioning (DIF) as a methodology to LLM evaluation benchmark contamination detection. DIF appears in the results as a traditional psychometric testing concept, but not in application to novel LLM evaluation approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d75607e3-8a87-4274-a143-4f3cdb8cf628",
  "isSidechain": false,
  "promptId": "6cc66108-81d2-49b2-977a-aa0548bb7fe1",
  "type": "user",
  "uuid": "fe2fe6ba-c22e-48c7-a6f5-b28aa33f6f03",
  "toolUseResult": {
    "query": "Differential Item Functioning DIF LLM evaluation benchmark contamination detection novel 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HVNELPxZK5BgZvYYtsbYCh",
        "content": [
          {
            "title": "What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide",
            "url": "https://llm-stats.com/blog/research/what-is-a-contaminated-llm"
          },
          {
            "title": "DVD: A Robust Method for Detecting Variant Contamination in Large Language Model Evaluation",
            "url": "https://arxiv.org/pdf/2601.04895"
          },
          {
            "title": "Detecting Benchmark Contamination Through Watermarking",
            "url": "https://arxiv.org/pdf/2502.17259"
          },
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/pdf/2510.02386"
          },
          {
            "title": "NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination   for each Benchmark",
            "url": "https://arxiv.org/pdf/2310.18018"
          },
          {
            "title": "A Log-Linear Modeling Approach for Differential Item Functioning Detection in Polytomously Scored Items - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6943994/"
          },
          {
            "title": "Towards Contamination Resistant Benchmarks",
            "url": "https://arxiv.org/pdf/2505.08389"
          }
        ]
      },
      "I found search results related to LLM benchmark contamination detection, but the results focus on contamination detection in large language model evaluation rather than on \"Differential Item Functioning\" (DIF) specifically in that context.\n\nHere's what I found:\n\n**LLM Benchmark Contamination Detection (2025-2026):**\n\nFive detection methods work in 2026: time-based partition (the Codeforces cliff), Min-K% probability, the Time Travel guided-completion attack, ConStat performance gaps on rephrased samples, and BIG-Bench canary GUID memorization.\n\nEven when training data contains only variants with no exact duplicates, models can achieve significantly inflated accuracy on evaluation benchmarks, and widely used contamination detection methods fail in this setting exhibiting unstable performance.\n\nAs LLMs have evolved into Large Reasoning Models (LRMs), benchmark contamination detection faces key challenges since LRMs rely on chain-of-thought reasoning, contamination evidence can be concealed through RL training, and extensive contamination with CoT on advanced LRMs barely leaves evidence for existing memorization-based detection methods.\n\n**Note:** The search results do not contain information specifically connecting Differential Item Functioning (DIF) as a methodology to LLM evaluation benchmark contamination detection. DIF appears in the results as a traditional psychometric testing concept, but not in application to novel LLM evaluation approaches."
    ],
    "durationSeconds": 7.720454376000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d75607e3-8a87-4274-a143-4f3cdb8cf628",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T04:33:20.829Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019goLTXiedwQG229TRvhH7W`</summary>

```json
{
  "query": "dynamic benchmark regeneration self-healing LLM evaluation psychometric equating item generation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe2fe6ba-c22e-48c7-a6f5-b28aa33f6f03",
  "isSidechain": false,
  "requestId": "req_011CbDCL8QbGwRrWsyWSf269",
  "type": "assistant",
  "uuid": "75f64b78-c1cf-4072-83f4-275d41b6cf0d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhHktvcUsWuqHJw7JuAf3f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 748,
      "cache_read_input_tokens": 28666,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 28666,
          "cache_creation_input_tokens": 748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 748
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

_source line 21 · 2026-05-20T04:33:27.203Z_

<details><summary>↩ Tool result · `toolu_019goLTXiedwQG229TRvhH7W`</summary>

```text
Web search results for query: "dynamic benchmark regeneration self-healing LLM evaluation psychometric equating item generation 2025 2026"

Links: [{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks | OpenReview","url":"https://openreview.net/forum?id=iX39LhePyd"},{"title":"[2402.11443] Benchmark Self-Evolving: A Multi-Agent Framework for Dynamic LLM Evaluation","url":"https://ar5iv.labs.arxiv.org/html/2402.11443"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/pdf/2511.04689"},{"title":"Benchmark Self-Evolving: A Multi-Agent Framework for Dynamic LLM   Evaluation","url":"https://arxiv.org/pdf/2402.11443"},{"title":"Dynamic Benchmark Construction for Evaluating Large Language Models on Real-World Codes","url":"https://arxiv.org/html/2508.07180v1"},{"title":"Benchmark Self-Evolving: A Multi-Agent Framework for Dynamic LLM Evaluation - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.223/"}]

The search found several relevant papers on dynamic and adaptive LLM evaluation systems:

## Key Results:

**ATLAS: Adaptive Testing Framework (2025-2026)**
ATLAS is an adaptive testing framework based on Item Response Theory (IRT) that estimates model ability using Fisher information–guided item selection, reducing the number of required items by up to 90% while maintaining measurement precision. ATLAS calibrates benchmark items using three-parameter logistic (3PL) IRT models to estimate item difficulty, discrimination, and guessing parameters, then dynamically selects items with maximum Fisher information for each model's current estimated ability.

**Benchmark Self-Evolving Framework (2025)**
This framework utilizes a multi-agent system to manipulate the context or question of original instances, reframing new evolving instances with high confidence that dynamically extend existing benchmarks, implementing six reframing operations to construct evolving instances testing LLMs against diverse queries, data noise and probing their problem-solving sub-abilities.

**Dynamic Benchmark Construction (2025)**
Code2Bench extracted function candidates from commits between August 2024 and May 2025, refining an initial pool of 1,442 candidates into a final benchmark dataset of 1,163 instances.

These papers represent recent advances in creating self-evolving and adaptive evaluation mechanisms for LLMs that address scalability and the ability to regenerate test items dynamically.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75f64b78-c1cf-4072-83f4-275d41b6cf0d",
  "isSidechain": false,
  "promptId": "6cc66108-81d2-49b2-977a-aa0548bb7fe1",
  "type": "user",
  "uuid": "b9fa3037-9882-40ee-ab8f-deedd51e6fcb",
  "toolUseResult": {
    "query": "dynamic benchmark regeneration self-healing LLM evaluation psychometric equating item generation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LqwQtG7gTwmYy5DRMMhfwM",
        "content": [
          {
            "title": "Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks | OpenReview",
            "url": "https://openreview.net/forum?id=iX39LhePyd"
          },
          {
            "title": "[2402.11443] Benchmark Self-Evolving: A Multi-Agent Framework for Dynamic LLM Evaluation",
            "url": "https://ar5iv.labs.arxiv.org/html/2402.11443"
          },
          {
            "title": "Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks",
            "url": "https://arxiv.org/pdf/2511.04689"
          },
          {
            "title": "Benchmark Self-Evolving: A Multi-Agent Framework for Dynamic LLM   Evaluation",
            "url": "https://arxiv.org/pdf/2402.11443"
          },
          {
            "title": "Dynamic Benchmark Construction for Evaluating Large Language Models on Real-World Codes",
            "url": "https://arxiv.org/html/2508.07180v1"
          },
          {
            "title": "Benchmark Self-Evolving: A Multi-Agent Framework for Dynamic LLM Evaluation - ACL Anthology",
            "url": "https://aclanthology.org/2025.coling-main.223/"
          }
        ]
      },
      "The search found several relevant papers on dynamic and adaptive LLM evaluation systems:\n\n## Key Results:\n\n**ATLAS: Adaptive Testing Framework (2025-2026)**\nATLAS is an adaptive testing framework based on Item Response Theory (IRT) that estimates model ability using Fisher information–guided item selection, reducing the number of required items by up to 90% while maintaining measurement precision. ATLAS calibrates benchmark items using three-parameter logistic (3PL) IRT models to estimate item difficulty, discrimination, and guessing parameters, then dynamically selects items with maximum Fisher information for each model's current estimated ability.\n\n**Benchmark Self-Evolving Framework (2025)**\nThis framework utilizes a multi-agent system to manipulate the context or question of original instances, reframing new evolving instances with high confidence that dynamically extend existing benchmarks, implementing six reframing operations to construct evolving instances testing LLMs against diverse queries, data noise and probing their problem-solving sub-abilities.\n\n**Dynamic Benchmark Construction (2025)**\nCode2Bench extracted function candidates from commits between August 2024 and May 2025, refining an initial pool of 1,442 candidates into a final benchmark dataset of 1,163 instances.\n\nThese papers represent recent advances in creating self-evolving and adaptive evaluation mechanisms for LLMs that address scalability and the ability to regenerate test items dynamically."
    ],
    "durationSeconds": 6.369978766,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "75f64b78-c1cf-4072-83f4-275d41b6cf0d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Contamination-Triggered Benchmark Regeneration with Bifactor IRT Equating  ## Description We propose a self-heal…",
  "leafUuid": "b9fa3037-9882-40ee-ab8f-deedd51e6fcb",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Self-healing benchmarks with DIF-robust contamination detection",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e"
}
```

---

### Tool call

_source line 24 · 2026-05-20T04:33:29.689Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019WRYJ8y5DN94TvPg2qf2Yj`</summary>

```json
{
  "query": "DVD detection variance generation distribution variant contamination LLM arXiv 2601.04895 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9fa3037-9882-40ee-ab8f-deedd51e6fcb",
  "isSidechain": false,
  "requestId": "req_011CbDCLstF55zdpAr9Vqtse",
  "type": "assistant",
  "uuid": "ce21be4c-29e1-444c-a523-90f37ac7f386",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EENu7LcivX9yKL8vBLLH7K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 29414,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 29414,
          "cache_creation_input_tokens": 732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 732
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

_source line 25 · 2026-05-20T04:33:37.428Z_

<details><summary>↩ Tool result · `toolu_019WRYJ8y5DN94TvPg2qf2Yj`</summary>

```text
Web search results for query: "DVD detection variance generation distribution variant contamination LLM arXiv 2601.04895 2026"

Links: [{"title":"[2601.04895] DVD: A Robust Method for Detecting Variant Contamination in Large Language Model Evaluation","url":"https://arxiv.org/abs/2601.04895"},{"title":"Detecting Variant Contamination in LLMs via Variance of Generation Distribution | OpenReview","url":"https://openreview.net/forum?id=Ubi631nNbI"},{"title":"DVD: A Robust Method for Detecting Variant Contamination in Large Language Model Evaluation","url":"https://arxiv.org/html/2601.04895"},{"title":"DVD: A Robust Method for Detecting Variant Contamination in Large","url":"https://arxiv.org/pdf/2601.04895"},{"title":"DETECTING VARIANT CONTAMINATION IN LLMS VIA ...","url":"https://openreview.net/pdf/2767f6fb89b7f7b0c804a63b2957e214b98038d1.pdf"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/pdf/2510.27055"},{"title":"DICE: Detecting In-distribution Contamination in LLM's Fine-tuning Phase   for Math Reasoning","url":"https://arxiv.org/pdf/2406.04197"},{"title":"Generalization or Memorization: Data Contamination and Trustworthy   Evaluation for Large Language Models","url":"https://arxiv.org/pdf/2402.15938"}]

Based on the search results, here's information about the arXiv paper 2601.04895:

## DVD: Detection via Variance of generation Distribution

Evaluating large language models (LLMs) is increasingly confounded by variant contamination: the training corpus contains semantically equivalent yet lexically or syntactically altered versions of test items.

Unlike verbatim leakage, these paraphrased or structurally transformed variants evade existing detectors based on sampling consistency or perplexity, thereby inflating benchmark scores via memorization rather than genuine reasoning.

### The DVD Method

The paper introduces DVD (Detection via Variance of generation Distribution), a single-sample detector that models the local output distribution induced by temperature sampling.

The key insight is that contaminated items trigger alternation between a "memory-adherence" state and a "perturbation-drift" state, yielding abnormally high variance in the synthetic difficulty of low-probability tokens; uncontaminated items remain in drift with comparatively smooth variance.

### Evaluation and Results

The researchers construct the first benchmark for variant contamination across two domains—Omni-MATH and SuperGPQA—by generating and filtering semantically equivalent variants, and simulate contamination via fine-tuning models of different scales and architectures (Qwen2.5 and Llama3.1).

Across datasets and models, DVD consistently outperforms perplexity-based, Min-k%++, edit-distance (CDD), and embedding-similarity baselines, while exhibiting strong robustness to hyperparameters.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce21be4c-29e1-444c-a523-90f37ac7f386",
  "isSidechain": false,
  "promptId": "6cc66108-81d2-49b2-977a-aa0548bb7fe1",
  "type": "user",
  "uuid": "b4743722-0985-47b6-91bb-fa8c04508421",
  "toolUseResult": {
    "query": "DVD detection variance generation distribution variant contamination LLM arXiv 2601.04895 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BP7YhnCXrZhJimYZpkCmRw",
        "content": [
          {
            "title": "[2601.04895] DVD: A Robust Method for Detecting Variant Contamination in Large Language Model Evaluation",
            "url": "https://arxiv.org/abs/2601.04895"
          },
          {
            "title": "Detecting Variant Contamination in LLMs via Variance of Generation Distribution | OpenReview",
            "url": "https://openreview.net/forum?id=Ubi631nNbI"
          },
          {
            "title": "DVD: A Robust Method for Detecting Variant Contamination in Large Language Model Evaluation",
            "url": "https://arxiv.org/html/2601.04895"
          },
          {
            "title": "DVD: A Robust Method for Detecting Variant Contamination in Large",
            "url": "https://arxiv.org/pdf/2601.04895"
          },
          {
            "title": "DETECTING VARIANT CONTAMINATION IN LLMS VIA ...",
            "url": "https://openreview.net/pdf/2767f6fb89b7f7b0c804a63b2957e214b98038d1.pdf"
          },
          {
            "title": "Detecting Data Contamination in LLMs via In-Context Learning",
            "url": "https://arxiv.org/pdf/2510.27055"
          },
          {
            "title": "DICE: Detecting In-distribution Contamination in LLM's Fine-tuning Phase   for Math Reasoning",
            "url": "https://arxiv.org/pdf/2406.04197"
          },
          {
            "title": "Generalization or Memorization: Data Contamination and Trustworthy   Evaluation for Large Language Models",
            "url": "https://arxiv.org/pdf/2402.15938"
          }
        ]
      },
      "Based on the search results, here's information about the arXiv paper 2601.04895:\n\n## DVD: Detection via Variance of generation Distribution\n\nEvaluating large language models (LLMs) is increasingly confounded by variant contamination: the training corpus contains semantically equivalent yet lexically or syntactically altered versions of test items.\n\nUnlike verbatim leakage, these paraphrased or structurally transformed variants evade existing detectors based on sampling consistency or perplexity, thereby inflating benchmark scores via memorization rather than genuine reasoning.\n\n### The DVD Method\n\nThe paper introduces DVD (Detection via Variance of generation Distribution), a single-sample detector that models the local output distribution induced by temperature sampling.\n\nThe key insight is that contaminated items trigger alternation between a \"memory-adherence\" state and a \"perturbation-drift\" state, yielding abnormally high variance in the synthetic difficulty of low-probability tokens; uncontaminated items remain in drift with comparatively smooth variance.\n\n### Evaluation and Results\n\nThe researchers construct the first benchmark for variant contamination across two domains—Omni-MATH and SuperGPQA—by generating and filtering semantically equivalent variants, and simulate contamination via fine-tuning models of different scales and architectures (Qwen2.5 and Llama3.1).\n\nAcross datasets and models, DVD consistently outperforms perplexity-based, Min-k%++, edit-distance (CDD), and embedding-similarity baselines, while exhibiting strong robustness to hyperparameters."
    ],
    "durationSeconds": 7.7351843949999965,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ce21be4c-29e1-444c-a523-90f37ac7f386",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T04:33:40.182Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SFa8xUwWUVJB5b4dPrDHRF`</summary>

```json
{
  "query": "bifactor IRT projective IRT PIRT benchmark equating multidimensional Kim 2022 educational measurement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4743722-0985-47b6-91bb-fa8c04508421",
  "isSidechain": false,
  "requestId": "req_011CbDCMddH5vcxPr2wprmh4",
  "type": "assistant",
  "uuid": "68297dff-2768-498d-b831-ea5cca94c100",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TGLJ5vgfbMa3ggKuGoiYzE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 30146,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 852,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 30146,
          "cache_creation_input_tokens": 852,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 852
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

_source line 27 · 2026-05-20T04:33:46.786Z_

<details><summary>↩ Tool result · `toolu_01SFa8xUwWUVJB5b4dPrDHRF`</summary>

```text
Web search results for query: "bifactor IRT projective IRT PIRT benchmark equating multidimensional Kim 2022 educational measurement"

Links: [{"title":"Item Response Theory True Score Equating for the Bifactor Model Under the Common-Item Nonequivalent Groups Design - Kyung Yong Kim, 2022","url":"https://journals.sagepub.com/doi/10.1177/01466216221108995"},{"title":"Approximating Bifactor IRT True-Score Equating With a Projective Item Response Model - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/32341608/"},{"title":"Item Response Theory True Score Equating for the Bifactor Model Under the Common-Item Nonequivalent Groups Design - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC9382090/"},{"title":"Full article: Using Projective IRT to Evaluate the Effects of Multidimensionality on Unidimensional IRT Model Parameters","url":"https://www.tandfonline.com/doi/full/10.1080/00273171.2024.2430630"},{"title":"Two IRT Fixed Parameter Calibration Methods for the Bifactor Model - Kim - 2020 - Journal of Educational Measurement - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1111/jedm.12230"},{"title":"Item Response Theory True Score Equating for the Bifactor Model Under the Common-Item Nonequivalent Groups Design - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/35991829/"},{"title":"Robustness of Projective IRT to Misspecification of the Underlying Multidimensional Model - PMC","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7433385/"},{"title":"Robustness of Projective IRT to Misspecification of the Underlying Multidimensional Model - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/32879536/"}]

Based on the search results, here's what I found on this topic:

## Key Research by Kim (2022)

Under the common-item nonequivalent groups design, Kim's 2022 study introduced two IRT true score equating procedures that adopted different dimension reduction strategies for the bifactor model.

### The Two Procedures

1. **Integration Procedure**: This procedure linked the latent variable scales for the bifactor model and integrated out the specific factors from the item response function of the bifactor model, then IRT true score equating was applied to the marginalized bifactor model.

2. **PIRT-Based Procedure**: This procedure projected the specific dimensions onto the general dimension to obtain a locally dependent unidimensional IRT (UIRT) model and linked the scales of the UIRT model, followed by the application of IRT true score equating.

## Context and Significance

Applying item response theory (IRT) true score equating to multidimensional IRT models is not straightforward due to the one-to-many relationship between a true score and latent variables. Although the common-item nonequivalent groups (CINEG) design is widely used in practice, IRT true score equating procedures for MIRT models under the CINEG design have been an infrequent topic of discussion in the literature.

The research was published in *Applied Psychological Measurement* in September 2022 and addresses an important gap in educational measurement methodology for handling multidimensional test equating.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68297dff-2768-498d-b831-ea5cca94c100",
  "isSidechain": false,
  "promptId": "6cc66108-81d2-49b2-977a-aa0548bb7fe1",
  "type": "user",
  "uuid": "5f45a4bb-8cbe-400d-9e64-fda7814d4710",
  "toolUseResult": {
    "query": "bifactor IRT projective IRT PIRT benchmark equating multidimensional Kim 2022 educational measurement",
    "results": [
      {
        "tool_use_id": "srvtoolu_012R3NrtNkgjpcpgAZ5uJkti",
        "content": [
          {
            "title": "Item Response Theory True Score Equating for the Bifactor Model Under the Common-Item Nonequivalent Groups Design - Kyung Yong Kim, 2022",
            "url": "https://journals.sagepub.com/doi/10.1177/01466216221108995"
          },
          {
            "title": "Approximating Bifactor IRT True-Score Equating With a Projective Item Response Model - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/32341608/"
          },
          {
            "title": "Item Response Theory True Score Equating for the Bifactor Model Under the Common-Item Nonequivalent Groups Design - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9382090/"
          },
          {
            "title": "Full article: Using Projective IRT to Evaluate the Effects of Multidimensionality on Unidimensional IRT Model Parameters",
            "url": "https://www.tandfonline.com/doi/full/10.1080/00273171.2024.2430630"
          },
          {
            "title": "Two IRT Fixed Parameter Calibration Methods for the Bifactor Model - Kim - 2020 - Journal of Educational Measurement - Wiley Online Library",
            "url": "https://onlinelibrary.wiley.com/doi/10.1111/jedm.12230"
          },
          {
            "title": "Item Response Theory True Score Equating for the Bifactor Model Under the Common-Item Nonequivalent Groups Design - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/35991829/"
          },
          {
            "title": "Robustness of Projective IRT to Misspecification of the Underlying Multidimensional Model - PMC",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7433385/"
          },
          {
            "title": "Robustness of Projective IRT to Misspecification of the Underlying Multidimensional Model - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/32879536/"
          }
        ]
      },
      "Based on the search results, here's what I found on this topic:\n\n## Key Research by Kim (2022)\n\nUnder the common-item nonequivalent groups design, Kim's 2022 study introduced two IRT true score equating procedures that adopted different dimension reduction strategies for the bifactor model.\n\n### The Two Procedures\n\n1. **Integration Procedure**: This procedure linked the latent variable scales for the bifactor model and integrated out the specific factors from the item response function of the bifactor model, then IRT true score equating was applied to the marginalized bifactor model.\n\n2. **PIRT-Based Procedure**: This procedure projected the specific dimensions onto the general dimension to obtain a locally dependent unidimensional IRT (UIRT) model and linked the scales of the UIRT model, followed by the application of IRT true score equating.\n\n## Context and Significance\n\nApplying item response theory (IRT) true score equating to multidimensional IRT models is not straightforward due to the one-to-many relationship between a true score and latent variables. Although the common-item nonequivalent groups (CINEG) design is widely used in practice, IRT true score equating procedures for MIRT models under the CINEG design have been an infrequent topic of discussion in the literature.\n\nThe research was published in *Applied Psychological Measurement* in September 2022 and addresses an important gap in educational measurement methodology for handling multidimensional test equating."
    ],
    "durationSeconds": 6.5992368300000015,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "68297dff-2768-498d-b831-ea5cca94c100",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T04:33:49.454Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014gLhDNVWLjaXvf3ZWrGaz1`</summary>

```json
{
  "query": "Cross-Context Verification CCV benchmark contamination SWE-bench session diversity arXiv 2603.21454"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f45a4bb-8cbe-400d-9e64-fda7814d4710",
  "isSidechain": false,
  "requestId": "req_011CbDCNKfogdMR1m2LprwrE",
  "type": "assistant",
  "uuid": "7a6e6a4e-ee96-4ba9-9465-2291fac05b48",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DGhzMi92HwKeAVapkP53CM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 970,
      "cache_read_input_tokens": 30998,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 970,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 30998,
          "cache_creation_input_tokens": 970,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 970
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

_source line 29 · 2026-05-20T04:33:56.037Z_

<details><summary>↩ Tool result · `toolu_014gLhDNVWLjaXvf3ZWrGaz1`</summary>

```text
Web search results for query: "Cross-Context Verification CCV benchmark contamination SWE-bench session diversity arXiv 2603.21454"

Links: [{"title":"[2603.21454] Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis","url":"https://arxiv.org/abs/2603.21454"},{"title":"Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis","url":"https://arxiv.org/pdf/2603.21454"},{"title":"Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis","url":"https://arxiv.org/html/2603.21454v1"},{"title":"SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark","url":"https://arxiv.org/pdf/2603.00520"},{"title":"More Rounds, More Noise: Why Multi-Turn Review Fails to Improve Cross-Context Verification","url":"https://arxiv.org/pdf/2603.16244"}]

Based on the search results, here's what I found about the paper:

The paper addresses a credibility crisis in LLM coding benchmarks, where widespread solution leakage and test quality issues undermine SWE-bench Verified, while existing detection methods (paraphrase consistency, n-gram overlap, perplexity analysis) never directly observe whether a model reasons or recalls.

The authors introduce Cross-Context Verification (CCV), a black-box method that solves the same benchmark problem in N independent sessions and measures solution diversity, combined with the Hierarchical Cross-Context Architecture (HCCA), a multi-agent analysis framework that prevents confirmation bias through intentional information restriction across specialized analytical roles.

**Key Results:**

On 9 SWE-bench Verified problems (45 trials, Claude Opus 4.6, temperature 0), CCV achieves perfect separation between contaminated and genuine reasoning. Key findings include that contamination is binary (models either recall perfectly or not at all), reasoning absence is a perfect discriminator, 33% of prior contamination labels are false positives, and HCCA's independent analysis structure discovers contamination-flaw composite cases that single-analyst approaches miss.

The paper was published on arXiv on March 23, 2026, and the authors released all code and data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a6e6a4e-ee96-4ba9-9465-2291fac05b48",
  "isSidechain": false,
  "promptId": "6cc66108-81d2-49b2-977a-aa0548bb7fe1",
  "type": "user",
  "uuid": "23e93bbc-b9d3-49fa-b00a-148e5fc195ff",
  "toolUseResult": {
    "query": "Cross-Context Verification CCV benchmark contamination SWE-bench session diversity arXiv 2603.21454",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FsHcLgVk1SZdZckvkiFnqn",
        "content": [
          {
            "title": "[2603.21454] Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis",
            "url": "https://arxiv.org/abs/2603.21454"
          },
          {
            "title": "Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis",
            "url": "https://arxiv.org/pdf/2603.21454"
          },
          {
            "title": "Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis",
            "url": "https://arxiv.org/html/2603.21454v1"
          },
          {
            "title": "SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark",
            "url": "https://arxiv.org/pdf/2603.00520"
          },
          {
            "title": "More Rounds, More Noise: Why Multi-Turn Review Fails to Improve Cross-Context Verification",
            "url": "https://arxiv.org/pdf/2603.16244"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper:\n\nThe paper addresses a credibility crisis in LLM coding benchmarks, where widespread solution leakage and test quality issues undermine SWE-bench Verified, while existing detection methods (paraphrase consistency, n-gram overlap, perplexity analysis) never directly observe whether a model reasons or recalls.\n\nThe authors introduce Cross-Context Verification (CCV), a black-box method that solves the same benchmark problem in N independent sessions and measures solution diversity, combined with the Hierarchical Cross-Context Architecture (HCCA), a multi-agent analysis framework that prevents confirmation bias through intentional information restriction across specialized analytical roles.\n\n**Key Results:**\n\nOn 9 SWE-bench Verified problems (45 trials, Claude Opus 4.6, temperature 0), CCV achieves perfect separation between contaminated and genuine reasoning. Key findings include that contamination is binary (models either recall perfectly or not at all), reasoning absence is a perfect discriminator, 33% of prior contamination labels are false positives, and HCCA's independent analysis structure discovers contamination-flaw composite cases that single-analyst approaches miss.\n\nThe paper was published on arXiv on March 23, 2026, and the authors released all code and data."
    ],
    "durationSeconds": 6.579570227000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7a6e6a4e-ee96-4ba9-9465-2291fac05b48",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-20T04:33:56.043Z_

```json
{
  "parentUuid": "23e93bbc-b9d3-49fa-b00a-148e5fc195ff",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3a4405fa-5f05-4c97-888a-db6c644fdfa1",
  "timestamp": "2026-05-20T04:33:56.043Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-20T04:33:59.062Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AEjDgP2uD5NfdgBUv1gD2H`</summary>

```json
{
  "query": "Wang Heckel \"task familiarity\" test-time RL alignment benchmark contamination arXiv 2603.12875 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a4405fa-5f05-4c97-888a-db6c644fdfa1",
  "isSidechain": false,
  "requestId": "req_011CbDCP1CLMH3hG1yvv9kQG",
  "type": "assistant",
  "uuid": "9b51636b-6279-468d-9cb6-ffddb476574e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jV1R2z1ts3NKCoCTkWCz4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 773,
      "cache_read_input_tokens": 31968,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 773,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 31968,
          "cache_creation_input_tokens": 773,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 773
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

_source line 32 · 2026-05-20T04:34:05.791Z_

<details><summary>↩ Tool result · `toolu_01AEjDgP2uD5NfdgBUv1gD2H`</summary>

```text
Web search results for query: "Wang Heckel "task familiarity" test-time RL alignment benchmark contamination arXiv 2603.12875 2026"

Links: [{"title":"[2603.12875] Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks","url":"https://arxiv.org/abs/2603.12875"},{"title":"Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks · benchmark | Festivus","url":"https://festivus.hapticlabs.ai/data/benchmarks/test-time-rl-alignment-exposes-task-familiarity-artifacts-in-llm-benchmarks"},{"title":"Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks","url":"https://arxiv.org/pdf/2603.12875"},{"title":"GitHub - smiles724/Awesome-LLM-RLVR: Collection of latest papers and materials in the area of RLVR! · GitHub","url":"https://github.com/smiles724/Awesome-LLM-RLVR"},{"title":"1 Fine-tuning gains are largely diminished after task alignment. Left: The reported performance reveals substantial accuracy gaps between base models and their fine-tuned variants. Right: After applying TTRA to all models, the base model’s performance increases significantly, nearly matching that of the fine-tuned models, suggesting that many gains from RLVR/SFT reported in the literature are not a difference in reasoning capability, but rather artifacts of task familiarity.","url":"https://arxiv.org/html/2603.12875"},{"title":"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/pdf/2510.09259"}]

Based on the search results, I found the paper you're looking for:

The paper arXiv:2603.12875 is titled "Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks" by Kun Wang and Reinhard Heckel, submitted on March 13, 2026.

**Overview:**

The paper addresses how direct evaluation of LLMs on benchmarks can be misleading because comparatively strong performance may reflect task familiarity rather than capability. The authors propose a two-stage test-time reinforcement learning alignment method where first, RL with a single sample provides initial alignment to the task format, and second, test-time RL with majority-voting reward aligns the model to the benchmark distribution.

**Key Findings:**

The research suggests that for reasoning tasks, the performance gap between fine-tuned models and their base models largely disappears after alignment, suggesting that many gains from RLVR/SFT reported in the literature are not a difference in reasoning capability, but rather artifacts of task familiarity. Their test-time RL alignment method aligns similarly well as SFT-based train-before-test, but without requiring a task-specific training set.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b51636b-6279-468d-9cb6-ffddb476574e",
  "isSidechain": false,
  "promptId": "6cc66108-81d2-49b2-977a-aa0548bb7fe1",
  "type": "user",
  "uuid": "b602331b-f834-4fe0-b7d9-610de97ba02a",
  "toolUseResult": {
    "query": "Wang Heckel \"task familiarity\" test-time RL alignment benchmark contamination arXiv 2603.12875 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NZy9sD8BWdcXfUGTVeYFgs",
        "content": [
          {
            "title": "[2603.12875] Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks",
            "url": "https://arxiv.org/abs/2603.12875"
          },
          {
            "title": "Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks · benchmark | Festivus",
            "url": "https://festivus.hapticlabs.ai/data/benchmarks/test-time-rl-alignment-exposes-task-familiarity-artifacts-in-llm-benchmarks"
          },
          {
            "title": "Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks",
            "url": "https://arxiv.org/pdf/2603.12875"
          },
          {
            "title": "GitHub - smiles724/Awesome-LLM-RLVR: Collection of latest papers and materials in the area of RLVR! · GitHub",
            "url": "https://github.com/smiles724/Awesome-LLM-RLVR"
          },
          {
            "title": "1 Fine-tuning gains are largely diminished after task alignment. Left: The reported performance reveals substantial accuracy gaps between base models and their fine-tuned variants. Right: After applying TTRA to all models, the base model’s performance increases significantly, nearly matching that of the fine-tuned models, suggesting that many gains from RLVR/SFT reported in the literature are not a difference in reasoning capability, but rather artifacts of task familiarity.",
            "url": "https://arxiv.org/html/2603.12875"
          },
          {
            "title": "Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models",
            "url": "https://arxiv.org/pdf/2510.09259"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper arXiv:2603.12875 is titled \"Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks\" by Kun Wang and Reinhard Heckel, submitted on March 13, 2026.\n\n**Overview:**\n\nThe paper addresses how direct evaluation of LLMs on benchmarks can be misleading because comparatively strong performance may reflect task familiarity rather than capability. The authors propose a two-stage test-time reinforcement learning alignment method where first, RL with a single sample provides initial alignment to the task format, and second, test-time RL with majority-voting reward aligns the model to the benchmark distribution.\n\n**Key Findings:**\n\nThe research suggests that for reasoning tasks, the performance gap between fine-tuned models and their base models largely disappears after alignment, suggesting that many gains from RLVR/SFT reported in the literature are not a difference in reasoning capability, but rather artifacts of task familiarity. Their test-time RL alignment method aligns similarly well as SFT-based train-before-test, but without requiring a task-specific training set."
    ],
    "durationSeconds": 6.725302401000008,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9b51636b-6279-468d-9cb6-ffddb476574e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-20T04:34:09.945Z_

Now let me search for whether anyone has already proposed using DIF specifically for LLM benchmark contamination detection, and also look for the most recent self-healing/auto-regenerating benchmark work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b602331b-f834-4fe0-b7d9-610de97ba02a",
  "isSidechain": false,
  "requestId": "req_011CbDCPixJn1zHnNwBuuYCS",
  "type": "assistant",
  "uuid": "92bbc768-88fc-4382-9ac5-7ba509e42287",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJJu2rLRfR3rtsZAAdLoQw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 819,
      "cache_read_input_tokens": 32741,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 819,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 118,
          "cache_read_input_tokens": 32741,
          "cache_creation_input_tokens": 819,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 819
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

_source line 34 · 2026-05-20T04:34:10.797Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015ewVbueCiZ3MoDEgDBJv7R`</summary>

```json
{
  "query": "\"differential item functioning\" LLM benchmark model cohort contamination psychometric 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92bbc768-88fc-4382-9ac5-7ba509e42287",
  "isSidechain": false,
  "requestId": "req_011CbDCPixJn1zHnNwBuuYCS",
  "type": "assistant",
  "uuid": "9831c4ea-364c-44f1-9745-8e08bf3fee8c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJJu2rLRfR3rtsZAAdLoQw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 819,
      "cache_read_input_tokens": 32741,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 819,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 118,
          "cache_read_input_tokens": 32741,
          "cache_creation_input_tokens": 819,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 819
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Contamination-Triggered Benchmark Regeneration with Bifactor IRT Equating  ## Description We propose a self-heal…",
  "leafUuid": "9831c4ea-364c-44f1-9745-8e08bf3fee8c",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Self-healing benchmarks with DIF-robust contamination detection",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e"
}
```

---

### Tool result

_source line 37 · 2026-05-20T04:34:16.477Z_

<details><summary>↩ Tool result · `toolu_015ewVbueCiZ3MoDEgDBJv7R`</summary>

```text
Web search results for query: ""differential item functioning" LLM benchmark model cohort contamination psychometric 2024 2025 2026"

Links: [{"title":"Quantifying Data Contamination in Psychometric Evaluations of LLMs","url":"https://arxiv.org/html/2510.07175v2"},{"title":"Quantifying Data Contamination in Psychometric Evaluations of LLMs","url":"https://arxiv.org/pdf/2510.07175"},{"title":"Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation","url":"https://arxiv.org/html/2502.17521v2"},{"title":"A Survey on Data Contamination for Large Language Models","url":"https://arxiv.org/pdf/2502.14425"},{"title":"NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination   for each Benchmark","url":"https://arxiv.org/pdf/2310.18018"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v3"},{"title":"[2510.07175] Quantifying Data Contamination in Psychometric Evaluations of LLMs","url":"https://arxiv.org/abs/2510.07175"}]

I found several highly relevant research papers on this topic. Here are the key findings:

## Quantifying Data Contamination in Psychometric Evaluations of LLMs

Studies have raised concerns that relying on established questionnaires entails the risk of data contamination, as LLMs may have encountered psychometric items or scoring procedures during pretraining. A framework was proposed to systematically measure data contamination in psychometric evaluations of LLMs, evaluating three aspects: (1) item memorization, (2) evaluation memorization, and (3) target score matching. When applied to 21 models and four widely used psychometric inventories, popular inventories such as the Big Five Inventory (BFI-44) and Portrait Values Questionnaire (PVQ-40) exhibit strong contamination, where models not only memorize items but can also adjust their responses to achieve specific target scores.

## Dynamic Benchmarking Approaches

Dynamic methods aim to reduce contamination risk either by continuously updating benchmark datasets based on LLM training timestamps, or by regenerating test data to reconstruct and replace original benchmarks.

## Psychometric Framework Application

Item Response Theory (IRT) offers a psychometric framework for data-driven, item-level analysis, which has been explored as a method to assess and analyze LLM benchmark quality in more nuanced ways, including detecting differential item functioning across model cohorts.

These papers from 2024-2026 represent the cutting edge of research on how data contamination affects psychometric evaluations of LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9831c4ea-364c-44f1-9745-8e08bf3fee8c",
  "isSidechain": false,
  "promptId": "6cc66108-81d2-49b2-977a-aa0548bb7fe1",
  "type": "user",
  "uuid": "832e7580-ef13-4cbf-a64e-b2c9276d8893",
  "toolUseResult": {
    "query": "\"differential item functioning\" LLM benchmark model cohort contamination psychometric 2024 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_017AY9EFsk2zkH4sBD5gj5BA",
        "content": [
          {
            "title": "Quantifying Data Contamination in Psychometric Evaluations of LLMs",
            "url": "https://arxiv.org/html/2510.07175v2"
          },
          {
            "title": "Quantifying Data Contamination in Psychometric Evaluations of LLMs",
            "url": "https://arxiv.org/pdf/2510.07175"
          },
          {
            "title": "Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation",
            "url": "https://arxiv.org/html/2502.17521v2"
          },
          {
            "title": "A Survey on Data Contamination for Large Language Models",
            "url": "https://arxiv.org/pdf/2502.14425"
          },
          {
            "title": "NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination   for each Benchmark",
            "url": "https://arxiv.org/pdf/2310.18018"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/html/2505.15055v3"
          },
          {
            "title": "[2510.07175] Quantifying Data Contamination in Psychometric Evaluations of LLMs",
            "url": "https://arxiv.org/abs/2510.07175"
          }
        ]
      },
      "I found several highly relevant research papers on this topic. Here are the key findings:\n\n## Quantifying Data Contamination in Psychometric Evaluations of LLMs\n\nStudies have raised concerns that relying on established questionnaires entails the risk of data contamination, as LLMs may have encountered psychometric items or scoring procedures during pretraining. A framework was proposed to systematically measure data contamination in psychometric evaluations of LLMs, evaluating three aspects: (1) item memorization, (2) evaluation memorization, and (3) target score matching. When applied to 21 models and four widely used psychometric inventories, popular inventories such as the Big Five Inventory (BFI-44) and Portrait Values Questionnaire (PVQ-40) exhibit strong contamination, where models not only memorize items but can also adjust their responses to achieve specific target scores.\n\n## Dynamic Benchmarking Approaches\n\nDynamic methods aim to reduce contamination risk either by continuously updating benchmark datasets based on LLM training timestamps, or by regenerating test data to reconstruct and replace original benchmarks.\n\n## Psychometric Framework Application\n\nItem Response Theory (IRT) offers a psychometric framework for data-driven, item-level analysis, which has been explored as a method to assess and analyze LLM benchmark quality in more nuanced ways, including detecting differential item functioning across model cohorts.\n\nThese papers from 2024-2026 represent the cutting edge of research on how data contamination affects psychometric evaluations of LLMs."
    ],
    "durationSeconds": 5.676751459000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9831c4ea-364c-44f1-9745-8e08bf3fee8c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T04:34:19.958Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F9MzMjyVNQ8h3eUj73Qzfq`</summary>

```json
{
  "query": "BeTaL ICLR 2026 automating benchmark design LLM difficulty RIDE IRT perturbation Hardy scalability coefficients arXiv 2603.24999"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "832e7580-ef13-4cbf-a64e-b2c9276d8893",
  "isSidechain": false,
  "requestId": "req_011CbDCQWcvnVfwQXgUa7o8S",
  "type": "assistant",
  "uuid": "1bce3559-5e65-46d6-921f-fe1404353d24",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BfaQxMdAeMx5jV3JBtuKMV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 817,
      "cache_read_input_tokens": 33560,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 817,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 92,
          "cache_read_input_tokens": 33560,
          "cache_creation_input_tokens": 817,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 817
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

_source line 39 · 2026-05-20T04:34:27.723Z_

<details><summary>↩ Tool result · `toolu_01F9MzMjyVNQ8h3eUj73Qzfq`</summary>

```text
Web search results for query: "BeTaL ICLR 2026 automating benchmark design LLM difficulty RIDE IRT perturbation Hardy scalability coefficients arXiv 2603.24999"

Links: [{"title":"AUTOMATING BENCHMARK DESIGN","url":"https://openreview.net/pdf/6c3a6173bbbcaecd92e5714bac096167f405a38b.pdf"},{"title":"Automating Benchmark Design","url":"https://arxiv.org/html/2510.25039v1"},{"title":"Automating Benchmark Design | OpenReview","url":"https://openreview.net/forum?id=efAANptQmt"},{"title":"RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning","url":"https://arxiv.org/pdf/2511.04120"},{"title":"[2510.25039] Automating Benchmark Design","url":"https://arxiv.org/abs/2510.25039"},{"title":"Automating Benchmark Design Amanda Dsouza 1 Harit Vishwakarma 1 Zhengyang Qi 1","url":"https://arxiv.org/pdf/2510.25039"},{"title":"Preprint. Accepted at the ICLR 2026 LIT Workshop","url":"https://arxiv.org/pdf/2602.09924"}]

Based on the search results, I found information about BeTaL and related work on automating benchmark design for LLMs:

## BeTaL Framework

BeTaL (Benchmark Tuning with an LLM-in-the-loop) is a framework that leverages environment design principles to automate the process of dynamic benchmark design. BeTaL works by parameterizing key design choices in base benchmark templates and uses LLMs to reason through the resulting parameter space to obtain target properties (such as difficulty and realism) in a cost-efficient manner.

## RIDE Framework

Related to the LLM difficulty measurement you mentioned, RIDE is a benchmark perturbation rewriting framework that incorporates Item Response Theory (IRT) to measure question difficulty. 35 cutting-edge LLMs are treated as students to answer 2,000 questions sampled from the high-difficulty mathematical dataset DeepMath.

## Key Features

BeTaL is built on two key ideas: first, strengthening grounding through explicit feedback from real rollouts of the designed benchmarks; and second, leveraging LLM reasoning to systematically explore and refine the design space, which mirrors how humans design benchmarks through iterative loops of experimentation and observation.

The BeTaL paper appears to be under review for ICLR 2026. However, I was unable to find the specific arXiv identifier "2603.24999" in these results or additional details about scalability coefficients and Hardy perturbation methods you mentioned in your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bce3559-5e65-46d6-921f-fe1404353d24",
  "isSidechain": false,
  "promptId": "6cc66108-81d2-49b2-977a-aa0548bb7fe1",
  "type": "user",
  "uuid": "ca65d71f-d8a1-455a-9940-2193104c125e",
  "toolUseResult": {
    "query": "BeTaL ICLR 2026 automating benchmark design LLM difficulty RIDE IRT perturbation Hardy scalability coefficients arXiv 2603.24999",
    "results": [
      {
        "tool_use_id": "srvtoolu_016PRdyDvimQzL1vfA1ppg2v",
        "content": [
          {
            "title": "AUTOMATING BENCHMARK DESIGN",
            "url": "https://openreview.net/pdf/6c3a6173bbbcaecd92e5714bac096167f405a38b.pdf"
          },
          {
            "title": "Automating Benchmark Design",
            "url": "https://arxiv.org/html/2510.25039v1"
          },
          {
            "title": "Automating Benchmark Design | OpenReview",
            "url": "https://openreview.net/forum?id=efAANptQmt"
          },
          {
            "title": "RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2511.04120"
          },
          {
            "title": "[2510.25039] Automating Benchmark Design",
            "url": "https://arxiv.org/abs/2510.25039"
          },
          {
            "title": "Automating Benchmark Design Amanda Dsouza 1 Harit Vishwakarma 1 Zhengyang Qi 1",
            "url": "https://arxiv.org/pdf/2510.25039"
          },
          {
            "title": "Preprint. Accepted at the ICLR 2026 LIT Workshop",
            "url": "https://arxiv.org/pdf/2602.09924"
          }
        ]
      },
      "Based on the search results, I found information about BeTaL and related work on automating benchmark design for LLMs:\n\n## BeTaL Framework\n\nBeTaL (Benchmark Tuning with an LLM-in-the-loop) is a framework that leverages environment design principles to automate the process of dynamic benchmark design. BeTaL works by parameterizing key design choices in base benchmark templates and uses LLMs to reason through the resulting parameter space to obtain target properties (such as difficulty and realism) in a cost-efficient manner.\n\n## RIDE Framework\n\nRelated to the LLM difficulty measurement you mentioned, RIDE is a benchmark perturbation rewriting framework that incorporates Item Response Theory (IRT) to measure question difficulty. 35 cutting-edge LLMs are treated as students to answer 2,000 questions sampled from the high-difficulty mathematical dataset DeepMath.\n\n## Key Features\n\nBeTaL is built on two key ideas: first, strengthening grounding through explicit feedback from real rollouts of the designed benchmarks; and second, leveraging LLM reasoning to systematically explore and refine the design space, which mirrors how humans design benchmarks through iterative loops of experimentation and observation.\n\nThe BeTaL paper appears to be under review for ICLR 2026. However, I was unable to find the specific arXiv identifier \"2603.24999\" in these results or additional details about scalability coefficients and Hardy perturbation methods you mentioned in your query."
    ],
    "durationSeconds": 7.760782294999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1bce3559-5e65-46d6-921f-fe1404353d24",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-20T04:34:31.036Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EsXaEXf9TTZnfCD1hYJ9xM`</summary>

```json
{
  "query": "benchmark item generation IRT calibration LLM student simulation difficulty estimation arXiv 2601.09953 2602.06631"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca65d71f-d8a1-455a-9940-2193104c125e",
  "isSidechain": false,
  "requestId": "req_011CbDCRLnN5c9P2xwWJRWbi",
  "type": "assistant",
  "uuid": "90655f84-9a6b-45a6-af3f-ca7725c1b98e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0125GNN2Mj8EKcehMLsWNm3p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 800,
      "cache_read_input_tokens": 34377,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 800,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 34377,
          "cache_creation_input_tokens": 800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 800
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

_source line 41 · 2026-05-20T04:34:38.358Z_

<details><summary>↩ Tool result · `toolu_01EsXaEXf9TTZnfCD1hYJ9xM`</summary>

```text
Web search results for query: "benchmark item generation IRT calibration LLM student simulation difficulty estimation arXiv 2601.09953 2602.06631"

Links: [{"title":"Estimating Exam Item Difficulty with LLMs: A Benchmark on Brazil's ENEM Corpus","url":"https://arxiv.org/pdf/2602.06631"},{"title":"[2601.09953] Take Out Your Calculators: Estimating the Real Difficulty of Question Items with LLM Student Simulations","url":"https://arxiv.org/abs/2601.09953"},{"title":"Take Out Your Calculators: Estimating the Real Difficulty of Question Items with LLM Student Simulations","url":"https://arxiv.org/pdf/2601.09953"},{"title":"Synthetic Student Responses: LLM-Extracted Features for IRT Difficulty Parameter Estimation","url":"https://arxiv.org/pdf/2602.00034"},{"title":"Take Out Your Calculators: Estimating the Real Difficulty of Question Items with LLM Student Simulations","url":"https://arxiv.org/html/2601.09953"},{"title":"Can LLMs Estimate Student Struggles? Human-AI Difficulty Alignment with Proficiency Simulation for Item Difficulty Prediction","url":"https://arxiv.org/html/2512.18880v1"},{"title":"[2602.00034] Synthetic Student Responses: LLM-Extracted Features for IRT Difficulty Parameter Estimation","url":"https://arxiv.org/abs/2602.00034"}]

I found relevant research papers matching your search query. Here are the key findings:

## ArXiv 2601.09953: "Take Out Your Calculators"

This paper investigates the predictive value of open-source large language models (LLMs) for evaluating the difficulty of multiple-choice math questions for real-world students. The approach simulates a "classroom" of students by prompting the LLM to role-play students of varying proficiency levels, and uses the outcomes to fit Item Response Theory (IRT) models, comparing learned difficulty parameters to real-world difficulties from NAEP data.

The results achieved correlations as high as 0.75, 0.76, and 0.82 for grades 4, 8, and 12, respectively. The study found that roleplays with named students improves predictions compared to student IDs, and stratifying names across gender and race further improves predictions.

## ArXiv 2602.06631: "Estimating Exam Item Difficulty with LLMs"

This paper focuses on exam difficulty prediction, item response theory, and prompt engineering using the Brazil's ENEM corpus. The results reveal a significant trade-off: while the best models achieve moderate rank correlation, they systematically underestimate difficulty and degrade significantly on multimodal items. The paper concludes that LLMs function best as calibrated screeners rather than authoritative oracles, supporting an "evaluation-before-generation" pipeline for responsible assessment design.

Both papers address the problem of using LLMs for difficulty estimation as an alternative to expensive traditional item calibration processes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90655f84-9a6b-45a6-af3f-ca7725c1b98e",
  "isSidechain": false,
  "promptId": "6cc66108-81d2-49b2-977a-aa0548bb7fe1",
  "type": "user",
  "uuid": "dbe8a352-1d7f-48e3-b19b-f7d5fbfbc639",
  "toolUseResult": {
    "query": "benchmark item generation IRT calibration LLM student simulation difficulty estimation arXiv 2601.09953 2602.06631",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AP5j2iX7Fv3AACsgVjdGMz",
        "content": [
          {
            "title": "Estimating Exam Item Difficulty with LLMs: A Benchmark on Brazil's ENEM Corpus",
            "url": "https://arxiv.org/pdf/2602.06631"
          },
          {
            "title": "[2601.09953] Take Out Your Calculators: Estimating the Real Difficulty of Question Items with LLM Student Simulations",
            "url": "https://arxiv.org/abs/2601.09953"
          },
          {
            "title": "Take Out Your Calculators: Estimating the Real Difficulty of Question Items with LLM Student Simulations",
            "url": "https://arxiv.org/pdf/2601.09953"
          },
          {
            "title": "Synthetic Student Responses: LLM-Extracted Features for IRT Difficulty Parameter Estimation",
            "url": "https://arxiv.org/pdf/2602.00034"
          },
          {
            "title": "Take Out Your Calculators: Estimating the Real Difficulty of Question Items with LLM Student Simulations",
            "url": "https://arxiv.org/html/2601.09953"
          },
          {
            "title": "Can LLMs Estimate Student Struggles? Human-AI Difficulty Alignment with Proficiency Simulation for Item Difficulty Prediction",
            "url": "https://arxiv.org/html/2512.18880v1"
          },
          {
            "title": "[2602.00034] Synthetic Student Responses: LLM-Extracted Features for IRT Difficulty Parameter Estimation",
            "url": "https://arxiv.org/abs/2602.00034"
          }
        ]
      },
      "I found relevant research papers matching your search query. Here are the key findings:\n\n## ArXiv 2601.09953: \"Take Out Your Calculators\"\n\nThis paper investigates the predictive value of open-source large language models (LLMs) for evaluating the difficulty of multiple-choice math questions for real-world students. The approach simulates a \"classroom\" of students by prompting the LLM to role-play students of varying proficiency levels, and uses the outcomes to fit Item Response Theory (IRT) models, comparing learned difficulty parameters to real-world difficulties from NAEP data.\n\nThe results achieved correlations as high as 0.75, 0.76, and 0.82 for grades 4, 8, and 12, respectively. The study found that roleplays with named students improves predictions compared to student IDs, and stratifying names across gender and race further improves predictions.\n\n## ArXiv 2602.06631: \"Estimating Exam Item Difficulty with LLMs\"\n\nThis paper focuses on exam difficulty prediction, item response theory, and prompt engineering using the Brazil's ENEM corpus. The results reveal a significant trade-off: while the best models achieve moderate rank correlation, they systematically underestimate difficulty and degrade significantly on multimodal items. The paper concludes that LLMs function best as calibrated screeners rather than authoritative oracles, supporting an \"evaluation-before-generation\" pipeline for responsible assessment design.\n\nBoth papers address the problem of using LLMs for difficulty estimation as an alternative to expensive traditional item calibration processes."
    ],
    "durationSeconds": 7.318572009999989,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "90655f84-9a6b-45a6-af3f-ca7725c1b98e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-20T04:34:41.818Z_

Now I have sufficient research to make a well-informed evaluation. Let me synthesize my findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbe8a352-1d7f-48e3-b19b-f7d5fbfbc639",
  "isSidechain": false,
  "requestId": "req_011CbDCS8A8LEyfKP6KMbtkB",
  "type": "assistant",
  "uuid": "05125873-ec10-42a1-a40a-d33d493802bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WeYQziCr9HwMVvfuYiW4M7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 840,
      "cache_read_input_tokens": 35177,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 840,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 110,
          "cache_read_input_tokens": 35177,
          "cache_creation_input_tokens": 840,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 840
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

_source line 43 · 2026-05-20T04:34:42.649Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VeBKuv73bjtiFFBELXWYSn`</summary>

```json
{
  "query": "Self-Critique RL-MIA Tao contamination detection reinforcement learning post-training arXiv 2510.09259 ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05125873-ec10-42a1-a40a-d33d493802bb",
  "isSidechain": false,
  "requestId": "req_011CbDCS8A8LEyfKP6KMbtkB",
  "type": "assistant",
  "uuid": "1680fb0a-31e0-42ae-a275-eb93fd924ac9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WeYQziCr9HwMVvfuYiW4M7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 840,
      "cache_read_input_tokens": 35177,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 840,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 110,
          "cache_read_input_tokens": 35177,
          "cache_creation_input_tokens": 840,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 840
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

_source line 44 · 2026-05-20T04:34:48.307Z_

<details><summary>↩ Tool result · `toolu_01VeBKuv73bjtiFFBELXWYSn`</summary>

```text
Web search results for query: "Self-Critique RL-MIA Tao contamination detection reinforcement learning post-training arXiv 2510.09259 ICLR 2026"

Links: [{"title":"[2510.09259] Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/abs/2510.09259"},{"title":"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/html/2510.09259v1"},{"title":"detecting data contamination from reinforcement learning ...","url":"https://arxiv.org/pdf/2510.09259"},{"title":"The Impact of Post-training on Data Contamination","url":"https://arxiv.org/pdf/2601.06103"},{"title":"[2510.24320] Critique-RL: Training Language Models for Critiquing through Two-Stage Reinforcement Learning","url":"https://arxiv.org/abs/2510.24320"},{"title":"Critique-RL: Training Language Models for Critiquing through Two-Stage Reinforcement Learning","url":"https://arxiv.org/pdf/2510.24320"}]

Based on the search results, I found the paper you're looking for:

The research conducts the first systematic study of data detection within RL post-training scenario and proposes Self-Critique. The method is motivated by the observation that after RL phase, the output entropy distribution of LLMs tends to collapse into highly specific and sparse modes, and Self-Critique probes for the underlying policy collapse, i.e., the model's convergence to a narrow reasoning path.

The research introduces RL-MIA, a benchmark constructed to simulate the contamination scenario in RL post-training. Extensive experiments show that Self-Critique significantly outperforms baseline methods across multiple models and contamination tasks, achieving an AUC improvement of up to 30%.

The paper is available at arXiv with ID 2510.09259, and the benchmark and code are available at https://github.com/yongding-tao/RL-Data-Contamination.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1680fb0a-31e0-42ae-a275-eb93fd924ac9",
  "isSidechain": false,
  "promptId": "6cc66108-81d2-49b2-977a-aa0548bb7fe1",
  "type": "user",
  "uuid": "edb513a5-0520-44e7-addd-c7fd7b40182a",
  "toolUseResult": {
    "query": "Self-Critique RL-MIA Tao contamination detection reinforcement learning post-training arXiv 2510.09259 ICLR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Khoc6Vyf3zPTiYXiFuoHxi",
        "content": [
          {
            "title": "[2510.09259] Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models",
            "url": "https://arxiv.org/abs/2510.09259"
          },
          {
            "title": "Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models",
            "url": "https://arxiv.org/html/2510.09259v1"
          },
          {
            "title": "detecting data contamination from reinforcement learning ...",
            "url": "https://arxiv.org/pdf/2510.09259"
          },
          {
            "title": "The Impact of Post-training on Data Contamination",
            "url": "https://arxiv.org/pdf/2601.06103"
          },
          {
            "title": "[2510.24320] Critique-RL: Training Language Models for Critiquing through Two-Stage Reinforcement Learning",
            "url": "https://arxiv.org/abs/2510.24320"
          },
          {
            "title": "Critique-RL: Training Language Models for Critiquing through Two-Stage Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2510.24320"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe research conducts the first systematic study of data detection within RL post-training scenario and proposes Self-Critique. The method is motivated by the observation that after RL phase, the output entropy distribution of LLMs tends to collapse into highly specific and sparse modes, and Self-Critique probes for the underlying policy collapse, i.e., the model's convergence to a narrow reasoning path.\n\nThe research introduces RL-MIA, a benchmark constructed to simulate the contamination scenario in RL post-training. Extensive experiments show that Self-Critique significantly outperforms baseline methods across multiple models and contamination tasks, achieving an AUC improvement of up to 30%.\n\nThe paper is available at arXiv with ID 2510.09259, and the benchmark and code are available at https://github.com/yongding-tao/RL-Data-Contamination."
    ],
    "durationSeconds": 5.653155186999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1680fb0a-31e0-42ae-a275-eb93fd924ac9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-20T04:36:38.379Z_

Now I have comprehensive research to provide a well-grounded evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:

1. **Wang et al., "On The Fragility of Benchmark Contamination Detection in Reasoning Models" (arXiv 2510.02386, ICLR 2026)**: 系统性证明了 GRPO/PPO 训练可在约 156 步内将 reference-free 检测方法的 AUROC 降低 14-20pp，部分方法降至接近随机（~50%）。这是本 proposal 的核心动机之一，论文真实存在且描述准确。

2. **Tao et al., "Detecting Data Contamination from Reinforcement Learning Post-training" / Self-Critique (arXiv 2510.09259, ICLR 2026)**: 提出 RL-MIA benchmark 和 Self-Critique 方法，通过检测 policy collapse 来识别 RL 后训练中的污染，AUC 提升最高 30%。这是目前**唯一**直接针对 RL 后训练污染检测的已发表方法，是 proposal 的直接竞争者。

3. **"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration" (arXiv 2604.12843, April 2026)**: 用多维 IRT + 固定参数校准 + 100 个 anchor items 实现跨时段 LLM 评估，400+ 模型上 Spearman ρ≥0.9。**最直接的 concurrent work**——也用了 IRT equating，但只做 cross-time evaluation，不做 contamination detection 或 item regeneration。

4. **DVD: Detection via Variance of Generation Distribution (arXiv 2601.04895, Jan 2026)**: 检测 variant contamination（改写后的测试题），AUC 0.73-0.74 vs. Min-K%++ 的 0.43-0.68。但仅在 SFT 模型上验证，未测试 RL 训练模型。论文真实，描述准确。

5. **CCV: Cross-Context Verification (arXiv 2603.21454, March 2026)**: 通过多 session 独立求解同一题目并测量 solution diversity 来检测污染，在 SWE-bench 上实现完美分离。但仅验证了 9 个编码问题，泛化性未知。

6. **Wang & Heckel, "Test-time RL alignment exposes task familiarity artifacts" (arXiv 2603.12875, March 2026)**: 证明 TTRA 可弥合 base model 与 fine-tuned model ~27pp 的性能差距，暗示很多 fine-tuning gains 是 task familiarity artifact 而非真实能力提升。论文真实，proposal 中的引用准确。

7. **arXiv 2602.06631 (Estimating Exam Item Difficulty with LLMs)** 和 **arXiv 2601.09953 (Student Simulation for Difficulty)**: 前者证明 LLM 直接估计难度仅 ρ=0.10-0.45；后者 student simulation 可达 r=0.75-0.82。两篇论文均真实，描述准确。

8. **Kim (2022), Journal of Educational Measurement**: Bifactor IRT True Score Equating 和 PIRT 确实存在，是教育测量领域的成熟方法论。

9. **Han et al., "Quantifying Data Contamination in Psychometric Evaluations of LLMs" (arXiv 2510.07175, 2025)**: 用 IRT 框架量化 LLM 心理测量评估中的数据污染，但**未使用 DIF 作为污染检测手段**。

10. **Benchmark Self-Evolving (COLING 2025)**: 多 agent 框架动态扩展 benchmark，但无 IRT equating，无 contamination detection。

- **调研总结**: 这个领域目前呈"碎片化"格局——contamination detection（ConStat, DVD, Self-Critique）、dynamic evaluation（LiveBench, BeTaL）、IRT-based evaluation（Growing Pains, ATLAS, PSN-IRT）各自为阵，**没有工作尝试将 contamination detection → item regeneration → psychometric equating 闭环整合**。此外，**DIF 作为 contamination detection 手段**在 LLM benchmark 领域确实**尚无先例**——这是一个真实的 novelty claim。然而，将 DIF 从教育测量迁移到 LLM 评估面临严重的样本量问题（LLM cohort 远小于人类考生群体），这一点 proposal 已有所讨论但解决方案说服力有限。


【Trivial Alternative 检验】:

**存在部分 trivial alternative 威胁，但不致命。** 

最显然的 trivial alternative 是："直接定期更新 benchmark（LiveBench 模式）+ 用 ConStat/DVD 等现有方法做 contamination detection，不需要 IRT equating"。这已经是社区的主流做法。增量价值在于：(1) 现有定期更新方式**不保证难度等价性**，无法进行跨版本公平比较；(2) 现有检测方法**对 RL 模型无效**，而 DIF 提供了一个理论上 RL-robust 的信号。

但第二点的增量价值取决于 DIF 在 LLM 场景下是否真的可行（样本量问题，见下），以及 Self-Critique（Tao et al.）是否已经"够用"地解决了 RL contamination detection。如果 Self-Critique 在实际场景中表现良好，DIF 的增量价值就变成了"多一个互补信号"而不是"唯一可行方案"。

另一个 trivial alternative：对于 equating，Growing Pains 已经展示了用 IRT fixed-parameter calibration + anchor items 做跨时段评估的可行性。虽然 Growing Pains 不做 regeneration，但加上简单的 item generation（甚至人工出题）+ Growing Pains 式的 equating，可能就够用了——不需要整个 bifactor IRT + PIRT 管线。

**增量价值的核心**在于"全闭环自动化"和"DIF as RL-robust signal"。前者是系统工程贡献（有价值但 novelty 有限），后者是方法论贡献（genuinely novel 但可行性存疑）。


【前提假设检验】:

核心 claim 的逻辑链条中有以下**未经验证的关键假设**：

1. **DIF 在 LLM cohort 上的可行性是最大的未验证假设。** Proposal 承认了小样本问题但给出的解决方案（temporal aggregation 到 N=40-80、Bayesian priors、Item-Focused Trees）尚无实证支持——没有人在 LLM benchmark 上跑过 DIF。"模型即考生"这一映射是否满足 DIF 的统计前提（如 local independence、unidimensionality within matched groups）完全未知。LLM 的 response patterns 与人类考生有本质不同（deterministic at temperature=0, correlated architectures, training data overlap），这些可能严重违反 DIF 的统计假设。

2. **"RL 不能在不消除污染收益的情况下消除 DIF 信号"这一论证是理论推导而非实证。** Proposal 给出了一个 analytical demonstration，但其核心论点——"RL smoothing 修改的是 NLL surface 而非 binary response pattern"——假设 RL 训练不会改变模型在 contaminated items 上的准确率。这在大多数情况下可能成立，但并非绝对：如果 RL 训练导致模型对 memorized items 的 accuracy 小幅下降（从 0.80 到 0.70），DIF 效应量就会显著缩小。这个"RL 不影响 behavioral accuracy"的假设需要实验验证。

3. **200-300 LLMs 的 calibration panel 假设 response independence。** IRT 模型要求 examinees 独立，但同一 family 的 LLMs（Llama 系列各版本）高度相关，这会 inflate effective sample size 并影响参数估计的可靠性。这个问题在 Growing Pains 中也存在但未被充分讨论。

4. **Bifactor IRT 对 LLM benchmark 的适用性未经验证。** 人类考生的 bifactor 结构（general + domain-specific abilities）是否同样适用于 LLMs 是开放问题。LLM 的能力结构可能不符合 bifactor 假设。


【3 维度打分】:

1. **Novelty: 中（偏强）**
   - **正面**: DIF 作为 contamination detection 信号应用于 LLM benchmark 确实是全新的（调研中未找到任何先例，包括 Han et al. 2510.07175 使用 IRT 分析污染但未用 DIF）。"Detection → Regeneration → Equating"全闭环整合也确实无人做过。将教育测量的成熟方法论（bifactor IRT, PIRT equating）系统性迁移到 LLM 评估是一个有价值的 cross-domain transfer。
   - **负面**: 核心 novelty 可以概括为"把教育测量的现有工具迁移到 LLM benchmark 场景"——这是 application novelty 而非 methodological novelty。每个组件（DIF, bifactor IRT, PIRT, ConStat, DVD）都是现有方法，proposal 的贡献是**整合而非发明**。Growing Pains 已经走了类似路线（IRT + fixed-parameter calibration for LLM benchmarks），只是没做 contamination detection 和 regeneration。此外，Self-Critique（Tao et al., ICLR 2026）已经提出了针对 RL 后训练的 contamination detection 方法，这削弱了 DIF 作为"唯一 RL-robust 方案"的独特性。
   - **总评**: 有真实的 novelty delta（DIF for contamination + 闭环整合），但属于 systems integration + cross-domain application 类型的贡献，而非开创性方法论突破。对 EMNLP 审稿人而言，"educational measurement → NLP evaluation" 的迁移本身有吸引力，但 contribution 的技术深度可能被质疑。

2. **Significance: 中**
   - **正面**: Benchmark contamination 是 NLP/AI 社区公认的重大问题。RL 训练逃逸 contamination detection 的发现（Wang et al., ICLR 2026）使问题更加紧迫。一个可行的 self-healing benchmark 框架如果成功将有广泛影响。
   - **负面**: 框架的复杂度（5-signal ensemble, bifactor IRT, PIRT, graceful degradation）意味着实际部署可能性较低——社区更可能采用 LiveBench 式的简单定期更新。影响力还取决于 DIF 是否真的能在 LLM 场景下 work（可行性风险直接限制 significance 的实现）。此外，如果核心实验结果是 positive（DIF 确实能检测 RL 训练后的污染），审稿人的反应可能是"interesting but expected"——DIF 检测 group-level 差异是它设计的本意，证明它能 work 并不算 surprising。
   - **总评**: 问题重要性毋庸置疑，但方案的实际影响力受限于复杂度和可行性。

3. **Related Work: 强**
   - Proposal 对相关工作的覆盖**异常全面**。涵盖了 contamination detection（ConStat, DVD, Self-Critique, CCV, watermarking）、dynamic evaluation（LiveBench, LiveCodeBench, BeTaL, VarBench, DyVal）、IRT for LLM（Growing Pains, PSN-IRT, ATLAS, RIDE）、item generation（arXiv 2602.06631, arXiv 2601.09953, ReQUESTA）、task familiarity（Wang & Heckel）等多个子领域。差异化定位清晰——明确指出了与 Growing Pains（不做 detection/regeneration）、CCV（仅 coding tasks）、DVD（未测 RL）、Self-Critique（individual-level method）等的区别。我在调研中发现的所有关键竞争工作 proposal 都已覆盖，未发现显著遗漏。
   - **唯一轻微不足**: Benchmark Self-Evolving (COLING 2025) 未被提及，但该工作与 proposal 差异较大，非关键遗漏。


【概率估计】: [22% - 32%] 中位 27%

【估计理由】: 
这个 proposal 的 idea 内核处于"有实质 novelty 但不够 surprising"的区间。DIF for contamination detection 是一个 genuinely novel 的 cross-domain transfer，但属于 "application of existing methodology to new domain" 类型的贡献。核心发现如果 positive（DIF 能检测 RL contamination），审稿人大概率反应是 "makes sense — DIF tests group-level differences by design" 而非 "surprising"。全闭环整合是系统贡献，有价值但不是 idea-level breakthrough。

**上界受限于 Novelty 的技术深度**: 审稿人可能认为"把 educational measurement 的现有工具搬到 LLM evaluation"虽然有用但 novelty 有限，尤其是 Growing Pains 已经走了 IRT-for-LLM-evaluation 的路线。

**下界受支撑于**: 问题的重要性和 related work 的覆盖质量；DIF 确实是全新应用；闭环框架确实填补了 gap。

概率未能进入 35%+ 区间的核心原因：(1) DIF 的小样本可行性是未经验证的关键假设，如果 DIF 在 LLM cohort 上根本 work 不了，整个框架的核心 novelty 就坍塌了；(2) contribution 以 integration 为主，methodological novelty 深度有限；(3) 核心发现的 surprise factor 不足——"DIF 能检测 group-level contamination"几乎是 tautological。

【主要风险】: 
1. **DIF 在 LLM cohort 上的可行性风险**: 这是存在性风险。如果小样本 + 违反 independence 假设 + LLM response patterns 的特殊性导致 DIF 在实际场景中不可靠，proposal 的核心 novelty 和 RL-robustness claim 同时失效。审稿人会问 "did you actually test DIF on real LLM cohorts or is this all analytical speculation?"
2. **Contribution 被认为是 "engineering integration" 而非 "scientific contribution"**: 每个组件都是现有方法的直接迁移或整合（DIF from educational testing, IRT equating from psychometrics, DVD/ConStat from prior work），审稿人可能认为 technical contribution 不足以支撑主会论文。
```

Sources:
- [On The Fragility of Benchmark Contamination Detection in Reasoning Models](https://arxiv.org/abs/2510.02386)
- [Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration](https://arxiv.org/abs/2604.12843)
- [DVD: A Robust Method for Detecting Variant Contamination in LLM Evaluation](https://arxiv.org/abs/2601.04895)
- [Cross-Context Verification: Hierarchical Detection of Benchmark Contamination](https://arxiv.org/abs/2603.21454)
- [Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks](https://arxiv.org/abs/2603.12875)
- [Detecting Data Contamination from Reinforcement Learning Post-training for LLMs (Self-Critique)](https://arxiv.org/abs/2510.09259)
- [Estimating Exam Item Difficulty with LLMs (arXiv 2602.06631)](https://arxiv.org/abs/2602.06631)
- [Take Out Your Calculators: Student Simulation for Difficulty Estimation](https://arxiv.org/abs/2601.09953)
- [Quantifying Data Contamination in Psychometric Evaluations of LLMs](https://arxiv.org/abs/2510.07175)
- [Kim (2022) IRT True Score Equating for the Bifactor Model](https://journals.sagepub.com/doi/10.1177/01466216221108995)
- [Approximating Bifactor IRT with Projective IRT (PIRT)](https://pubmed.ncbi.nlm.nih.gov/32341608/)
- [BeTaL: Automating Benchmark Design (ICLR 2026)](https://arxiv.org/abs/2510.25039)
- [Benchmark Self-Evolving: A Multi-Agent Framework for Dynamic LLM Evaluation](https://arxiv.org/abs/2402.11443)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edb513a5-0520-44e7-addd-c7fd7b40182a",
  "isSidechain": false,
  "requestId": "req_011CbDCSrjTgezc6f3XkpsXw",
  "type": "assistant",
  "uuid": "b81eb47d-6452-4a7b-bd53-706c794d515f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KsrnMQiDnmCc2crMzQwEx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 647,
      "cache_read_input_tokens": 36017,
      "output_tokens": 4908,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4908,
          "cache_read_input_tokens": 36017,
          "cache_creation_input_tokens": 647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 647
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

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Contamination-Triggered Benchmark Regeneration with Bifactor IRT Equating  ## Description We propose a self-heal…",
  "leafUuid": "b81eb47d-6452-4a7b-bd53-706c794d515f",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Self-healing benchmarks with DIF-robust contamination detection",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Contamination-Triggered Benchmark Regeneration with Bifactor IRT Equating  ## Description We propose a self-heal…",
  "leafUuid": "b81eb47d-6452-4a7b-bd53-706c794d515f",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e"
}
```

---

### Runtime record

_source line 49_

```json
{
  "type": "ai-title",
  "aiTitle": "Self-healing benchmarks with DIF-robust contamination detection",
  "sessionId": "e7a41451-686f-4998-8d4e-dc44ee26098e"
}
```

---
