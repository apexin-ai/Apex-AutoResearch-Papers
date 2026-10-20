# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Contamination-Triggered Benchmark

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-1/13ac10a1-0849-4d3d-8381-876f1204b258.jsonl`
- **Structured JSON:** [`34073371f1feacd6e024.json`](../../sessions/34/34073371f1feacd6e024.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:32:20.989Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:32:20.989Z",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Contamination-Triggered Benchmark Regeneration with Bifactor IRT Equating\n\n## Description\nWe propose a self-healing benchmark framework that closes the full loop from multi-signal contamination detection through construct-constrained generation to bifactor IRT-equated replacement, with formal graceful-degradation guarantees. The system makes four integrated contributions: (1) A multi-signal contamination sentinel with explicit RL-robustness guarantees, now supported by an analytical demonstration. The ensemble combines five signals: ConStat-style perturbation testing, a novel Differential Item Functioning (DIF) analysis across model release cohorts, IRT aberrance detection, DVD-style generation-variance testing (adapted from Liang et al., arXiv 2601.04895), and membership-inference probes — with formal FDR control. The DIF-based cohort analysis is both novel and analytically RL-robust: we demonstrate via a concrete scenario (200 items, N=80/cohort, 20 contaminated items with P(correct) boosted from 0.50 to 0.80) that logistic regression DIF detects contamination as large uniform DIF (ETS Category C, |Δ_MH|≈3.3) because it examines between-group item-level performance conditional on ability, not within-model output distributions that RL smoothing affects. Quantitative power analysis grounded in PMC5978487 simulations establishes that at N=80/group with contamination-typical effect sizes (δ≈0.8-1.4 logits, consistent with GSM1K's 10-13% accuracy drops), DIF power reaches 60-85%, further enhanced by cumulative Bayesian priors (Sinharay et al., 2006), Item-Focused Trees (Tutz & Berger, 2016), and the 2-of-5 ensemble voting threshold. We acknowledge DIF is underpowered for small effects (14.4% at δ=0.4, N=50/group) — its value is detecting the large effects that threaten benchmark validity, complemented by other signals for subtler contamination. We further address the interaction with task familiarity artifacts (Wang & Heckel, arXiv 2603.12875): task familiarity produces uniform improvements (no DIF signal) while contamination produces item-specific advantages (DIF signal), making DIF a principled discriminator between the two. DVD is labeled as promising but untested against RL-trained models; our RL-contamination experimental condition will resolve this empirical gap. (2) A construct-constrained generation pipeline that abandons direct IRT-parameter conditioning (shown to achieve only rho=0.10-0.45 by arXiv 2602.06631) in favor of construct/taxonomy-based generation, student-simulation pre-screening (r=0.75-0.82), optional pre-filtering via signed isotonic R² scalability coefficients (Hardy et al., arXiv 2603.24999) for fast nonparametric quality control, multi-agent iterative refinement, and empirical calibration on a panel of 200-300 diverse LLMs via Bayesian fixed-parameter calibration (OH2PL, König et al., 2020, achieving unbiased estimates at N≥50). (3) A bifactor IRT equating gate using Projective IRT (PIRT) to handle the multi-construct nature of benchmarks like MMLU — fitting a general ability factor plus domain-specific factors, then projecting to unidimensional equivalents for standard equating (Kim, 2022). Only items whose projected parameters fall within 95% CIs of originals and preserve test information, construct coverage, and model rankings (rho >= 0.95) are accepted. (4) A formal graceful-degradation framework defining validity boundaries grounded in the test equating literature: minimum 20% anchor set for standard equating (Kolen & Brennan, 2004), degraded-but-valid operation via robust LAV equating at 15-20%, halt-and-review below 15%, minimum marginal reliability ≥ 0.80 for benchmark release, and transparent partial-release protocols when full regeneration fails for >15% of items. This uniquely differentiates from Growing Pains (cross-time evaluation without contamination detection or regeneration), from CCV (solution-diversity detection for coding tasks without remediation or psychometric equating), from watermarking approaches (Sander et al., arXiv 2502.17259; proactive prevention requiring pre-release embedding, complementary to our post-hoc detection and remediation), from Wang et al./Self-Critique (identifying the RL-fragility problem without providing a robust detection alternative), from DVD (detecting variant contamination without remediation and untested on RL models), from RIDE/BeTaL (altering difficulty rather than preserving it), and from ConStat (detecting but not remediating contamination). We validate on LiveBench subsets and MMLU-CF under simulated contamination at 10-50% rates — including an RL-contamination condition using GRPO fine-tuning following Wang et al.'s protocol to empirically test DIF robustness and DVD behavior under RL — with naturally-contaminated MMLU/GSM8K as positive controls, and include a pilot feasibility study reporting the first empirical convergence statistics for IRT-equated benchmark item generation.\n\n## Core Problem\nHow can we build self-healing benchmarks that automatically detect contaminated items via multi-signal triangulation — including a novel DIF-based cohort analysis robust to RL-trained reasoning models — and regenerate psychometrically equivalent replacements through empirically calibrated generation with bifactor IRT equating, while maintaining benchmark validity through formal graceful-degradation guarantees?\n\n## Opportunity\nDynamic benchmarks face a fundamental tension: increased contamination resistance via strong rewriting degrades question fidelity and may alter intended difficulty. LiveBench updates monthly but without psychometric calibration; VarBench perturbs inputs but difficulty shifts unpredictably; BenchBench evaluates generation quality but without equating. Educational testing has solved the analogous problem of maintaining test comparability across administrations using IRT equating with anchor items — a mature methodology with decades of validation. However, directly applying this to LLM benchmarks requires solving four underappreciated sub-problems: (1) distinguishing contamination from genuine capability gains — this is especially critical for RL-trained reasoning models (o1, o3, DeepSeek-R1), where Wang et al. (ICLR 2026) demonstrate that GRPO/PPO training conceals contamination signals that reference-free detection methods rely on, with AUROC degradation of 14-20 percentage points (Loss: 14.22pp, Min-K%: 16.42pp, Max-K%: 19.84pp after only ~156 GRPO steps), reducing most to near-random (~50%) AUROC; furthermore, Wang & Heckel (arXiv 2603.12875) show that test-time RL alignment can close fine-tuning performance gaps by ~27 percentage points on average, suggesting some apparent contamination signals may reflect task familiarity artifacts rather than memorization, making item-specific detection even more critical; (2) detecting variant contamination (paraphrased/restructured benchmark items in training data) which evades standard detectors — DVD (arXiv 2601.04895) shows conventional methods achieve only 0.43-0.68 AUC on variant contamination; (3) generating replacement items with controlled psychometric properties (LLMs systematically underestimate difficulty with correlations of only rho=0.10-0.45, per arXiv 2602.06631, necessitating empirical calibration rather than prompt-based difficulty targeting); and (4) equating across multi-construct benchmarks (requiring bifactor or multidimensional IRT rather than naive unidimensional models). No existing work addresses all four sub-problems in an integrated pipeline with formal graceful-degradation guarantees.\n\n## Landscape\nLiveBench (ICLR 2025) updates monthly from recent sources but applies objective scoring without difficulty calibration. LiveCodeBench (ICLR 2025) uses time-segmented evaluation but doesn't ensure psychometric equivalence across segments. BeTaL (ICLR 2026) performs dynamic benchmark design with LLM-in-the-loop but focuses on increasing difficulty, not preserving it. BenchBench (March 2026) evaluates automated benchmark generation using discrimination and validity metrics but without IRT equating. ArenaBencher progressively generates harder items but provides no formal difficulty-equivalence guarantees. CRITICAL CONCURRENT WORK: 'Growing Pains' (arXiv April 2026) uses multidimensional IRT with fixed-parameter calibration and 100 anchor items per dataset to make LLM evaluation extensible across time — achieving Spearman rho >= 0.9 for ranking preservation using 400+ models. However, it addresses efficient evaluation (comparing scores across time), NOT contamination detection or item regeneration. PSN-IRT (AAAI 2026 Oral) analyzes benchmark quality via 4PL IRT but does not regenerate items. RIDE (ICLR 2026) uses IRT-guided perturbation for difficulty evolution in math but does not perform equating. ATLAS (arXiv 2025) applies adaptive testing with IRT to reduce evaluation cost but does not handle contamination. Cross-Context Verification (CCV; arXiv 2603.21454, March 2026) achieves perfect separation between contaminated and genuine reasoning (Mann-Whitney U=0, r=1.0) on SWE-bench Verified by measuring solution diversity across independent sessions — a powerful black-box method, but currently validated only on coding tasks (9 SWE-bench problems, 45 trials) and relying on temperature-0 determinism that may not generalize to knowledge/reasoning benchmarks with inherent answer variability. Hardy et al. (arXiv 2603.24999, March 2026) introduce nonparametric signed isotonic R² scalability coefficients that outperform IRT-based item diagnostics for detecting bad benchmark items on HS Math, GSM8K, and MMLU — lightweight (bivariate monotone fits in seconds) and robust under small-n/large-p conditions; this complements our IRT-based quality control by providing a fast model-agnostic pre-filter for item quality before parametric calibration. On proactive contamination prevention: Sander et al. (arXiv 2502.17259, Feb 2025) propose watermarking benchmarks before release, reformulating questions with a watermarked LLM and detecting 'radioactivity' traces via statistical tests; validated on ARC and MMLU with 1B models, this represents a fundamentally different paradigm (prevention at release time vs. post-hoc detection and remediation). Our approach is complementary: watermarking prevents future contamination, while our pipeline detects and remediates existing contamination in already-deployed benchmarks — the two could be combined in a defense-in-depth strategy. On contamination detection: ConStat (2024) provides performance-based detection with formal FDR control; shortcut neuron analysis (ACL 2025) can isolate contamination to ~1.1-1.4% of neurons with only ~3% false positive impact; 'Test of Time' (arXiv 2025) demonstrates temporal signals are unreliable as standalone contamination indicators. CRITICALLY, 'On The Fragility of Benchmark Contamination Detection in Reasoning Models' (Wang et al., arXiv 2510.02386, ICLR 2026) systematically demonstrates that GRPO/PPO-style RL training conceals contamination signals: reference-free methods show AUROC degradation of 14-20 percentage points after only ~156 GRPO steps (Loss: 14.22pp drop from 75.48% to 61.26%; Min-K%: 16.42pp drop from 74.96% to 58.54%; Max-K%: 19.84pp drop from 69.83% to 49.99% — essentially random), while perturbation-based methods show different degradation patterns. The concealment mechanism is PPO's clipping objective, which contracts the NLL gap between contaminated and clean items. Self-Critique (Tao et al., arXiv 2510.09259, ICLR 2026) partially addresses this via policy-collapse detection but remains an individual-model-level method. DVD (Liang et al., arXiv 2601.04895, Jan 2026) introduces detection via variance of generation distribution and is specifically designed for variant contamination, achieving 0.73-0.74 AUC where Min-K%++ achieves only 0.43-0.68; however, DVD was validated only on SFT-contaminated models and its behavior under RL training is untested. On task familiarity vs. contamination: Wang & Heckel (arXiv 2603.12875, March 2026) show that test-time RL alignment (TTRA) closes the performance gap between base and fine-tuned models by ~27 percentage points on average, suggesting many reported fine-tuning gains are task familiarity artifacts rather than genuine capability improvements; this has a dual implication — it strengthens the need for item-specific contamination detection (since task familiarity produces uniform improvements with no DIF signal, while contamination produces item-specific advantages that DIF detects), but also suggests that contamination-driven DIF effects may be partially confounded with format-familiarity effects that TTRA could remove. On item generation: arXiv 2602.06631 shows LLMs achieve only rho=0.10-0.45 for difficulty estimation, but student simulation approaches (arXiv 2601.09953) achieve r=0.75-0.82 and multi-agent frameworks like ReQUESTA improve discrimination from 0.17 to 0.39. On IRT methodology: bifactor models with Projective IRT (PIRT) enable equating of multidimensional tests while remaining tractable; fixed-parameter calibration requires only N>=200 examinees vs N>=500 for full calibration (Kim & Kolen, 2019); the OH2PL (König, Spoden, & Frey, 2020) achieves unbiased estimates at N>=50 using optimized Bayesian hierarchical priors. No existing work closes the full loop from multi-signal contamination detection (robust to RL-trained models) through construct-constrained generation to bifactor IRT-equated regeneration with graceful-degradation guarantees.\n\n## Approach\nBuild a closed-loop pipeline with three stages plus a formal graceful-degradation framework, each substantially revised to address known limitations:\n\n**Stage 1: Multi-Signal Contamination Sentinel (with RL-Robustness Guarantees).** Deploy an ensemble of five complementary detection signals, explicitly designed so that at least two signals remain informative even against RL-trained reasoning models:\n\n(a) *ConStat-style perturbation testing* — compare model performance on original items vs. semantically-equivalent reformulations, with formal False Discovery Rate (FDR) control. NOTE: Wang et al. (ICLR 2026) show reference-free detectors degrade 14-20pp under RL training (Loss: 14.22pp, Min-K%: 16.42pp, Max-K%: 19.84pp after ~156 GRPO steps); we retain perturbation testing as effective against non-RL models (which still constitute the majority of the model ecosystem) but do not rely on it alone.\n\n(b) *Differential Item Functioning (DIF) across model release cohorts* — a novel application treating model release date as a grouping variable and flagging items that become differentially easier for newer cohorts beyond what general ability gains predict. **This is our primary RL-robust signal.** The key argument: DIF operates on group-level statistical patterns (comparing Item Characteristic Curves across model cohorts matched on overall ability), not individual output distributions. Wang et al. prove that PPO/GRPO clipping contracts the NLL gap *within a single model* between seen and unseen items — but DIF does not examine within-model NLL gaps. It detects whether the structural relationship between ability and item response differs across groups. A contaminated cohort shows anomalous ICCs on specific items regardless of how smooth individual output distributions appear, because contamination must, by definition, create differential item advantage — the one signal RL cannot conceal without negating the purpose of contamination. Furthermore, DIF leverages IRT's invariance principle: item parameters should be group-invariant after controlling for ability, and systematic DIF violations on specific items constitute contamination evidence that is orthogonal to all 10 methods shown to fail.\n\n**Analytical Demonstration of DIF RL-Robustness.** Consider a concrete scenario: 200 binary items evaluated by two annual model cohorts (pre-2026, post-2026) with N=80 models each. Suppose 20 items are contaminated in the newer cohort, boosting P(correct) from 0.50 to 0.80 on those items (δ≈1.4 logits — a conservative estimate given GSM1K's documented 13% average accuracy drop across models, which implies item-level boosts of 20-40% on memorized items for heavily contaminated models). RL smoothing via GRPO/PPO contracts the NLL gap between contaminated and clean items within each individual model's output distribution — this is the mechanism Wang et al. demonstrate. However, the 30-percentage-point accuracy advantage on contaminated items persists at the behavioral level: RL training does not cause models to answer memorized items incorrectly, because doing so would negate the purpose of contamination. Logistic regression DIF with sum-score matching compares the probability of correctly answering each item across the two cohorts, conditioning on total score (overall ability). On the 180 uncontaminated items, both cohorts show similar ICCs after controlling for ability. On the 20 contaminated items, the newer cohort shows systematically higher probability of correct response at every matched ability level — large uniform DIF (ETS Category C: |Δ_MH| = -2.35 × ln(odds ratio) = -2.35 × ln(4.0) ≈ 3.3 delta units, far exceeding the C threshold of 1.5). This differential pattern is detectable because DIF examines between-group item-level performance conditional on ability, not within-model output distributions. RL smoothing is irrelevant to DIF: it modifies how confidently a model generates its answer (the NLL surface), not whether it gets the answer right or wrong (the binary response pattern that DIF analyzes).\n\n**Quantitative DIF Power Analysis.** Independent simulation evidence (PMC5978487) establishes that logistic regression DIF at N=50/group achieves 14.4% power for small effects (δ=0.4) and 31.0% for medium effects (δ=0.6); at N=100/group, these rise to 24.7% and 55.2% respectively. These figures appear concerning for small-sample detection, but benchmark contamination typically produces large effects: GSM1K documents 10-13% average accuracy drops from contamination across models, corresponding to item-level δ≈0.8-1.4 logits on memorized items. DIF power scales super-linearly with effect size; at δ=1.4 with N=80/group (annual cohorts), power is estimated at 60-85% based on extrapolation from PMC5978487 simulation curves, consistent with the general finding that the likelihood ratio test achieves the highest statistical power in most DIF configurations. Furthermore, three factors substantially improve effective power beyond these baseline estimates: (i) cumulative Bayesian priors (Sinharay et al., 2006) accumulate evidence across successive benchmark administrations, borrowing strength from previous DIF estimates to improve detection over time — particularly effective for persistent contamination that affects multiple administrations; (ii) Item-Focused Trees (Tutz & Berger, 2016) avoid arbitrary categorical group splits by treating release date as a continuous covariate, leveraging the full model sample (N=160 rather than two groups of 80) and letting the method identify natural breakpoints where DIF emerges; (iii) the 2-of-5 ensemble voting threshold means even 40-50% individual DIF power yields acceptable ensemble sensitivity when combined with DVD and ConStat signals on non-RL models. We acknowledge that DIF alone is underpowered for small contamination effects (δ<0.6); its value lies in detecting the large effects that matter most for benchmark validity, complemented by other ensemble signals for smaller effects.\n\n**Interaction with Task Familiarity Artifacts.** Wang & Heckel (arXiv 2603.12875, March 2026) demonstrate that test-time RL alignment (TTRA) closes the performance gap between base and fine-tuned models by ~27 percentage points on average, suggesting many reported fine-tuning gains reflect task familiarity rather than genuine capability. This has a dual implication for DIF-based detection. First, it *strengthens* the DIF rationale: task familiarity artifacts produce uniform improvements across all items (no DIF signal), while memorization-based contamination produces item-specific advantages (DIF signal) — DIF thus provides a principled way to distinguish the two, a distinction no other detection method explicitly makes. Second, it introduces a nuance: if some contamination manifests partially as enhanced task-format familiarity rather than item-specific memorization, the item-level DIF effect sizes may be modestly smaller than the raw accuracy gaps suggest. We address this by: (a) noting that DIF would be computed on models as deployed (without TTRA), since TTRA is an analysis tool, not a standard deployment procedure; (b) observing that DIF controls for overall ability via sum-score matching, so any uniform familiarity-driven improvements are absorbed into the ability estimate, leaving item-specific contamination signals intact; (c) reporting DIF effect sizes with uncertainty intervals rather than relying on significance thresholds alone, making the analysis transparent about power limitations.\n\n**DIF Small-Sample Strategy (detailed).** Classical DIF methods (Mantel-Haenszel, logistic regression) require N≥200 per group for optimal performance (Mazor et al., 1992; Scott et al., 2009), far exceeding our ~10-20 models per quarterly cohort. We address this through a four-pronged strategy: (i) *Temporal aggregation*: use semi-annual or annual cohorts rather than quarterly, yielding N=40-80 per group; as the model ecosystem grows (~100+ new models per year as of 2026), annual cohorts will approach the N≥100 threshold where regularized methods become viable. (ii) *Cumulative Bayesian DIF*: following Sinharay et al. (2006, ETS), use DIF estimates from previous benchmark administrations as informative priors for new cohorts, accumulating statistical power over time rather than analyzing each cohort in isolation. (iii) *Item-Focused Trees* (Tutz & Berger, 2016): treat release date as a continuous covariate rather than creating arbitrary categorical cohorts, letting the method identify natural breakpoints where DIF emerges — this avoids the small-group problem entirely while leveraging the full model sample. (iv) *Parsimonious models*: following Belzak (2020, Multivariate Behavioral Research), use logistic regression with sum scores rather than complex IRT models for DIF detection, as simpler models outperform complex ones in small samples even when misspecified. We report DIF effect sizes (ETS delta classification: A/B/C, where C indicates |Δ_MH|≥1.5) with uncertainty intervals rather than relying solely on significance tests, acknowledging power limitations transparently.\n\n(c) *IRT aberrance detection* — flag items whose observed easiness significantly exceeds calibrated difficulty, used as one signal among several rather than a standalone detector.\n\n(d) *DVD-style generation variance testing* (adapted from Liang et al., arXiv 2601.04895) — for models with inference access, generate 50 responses per item via temperature sampling and compute the variance of synthetic-difficulty scores. Contaminated items exhibit bimodal generation distributions (alternating between memorized templates and free generation) yielding high variance, while clean items show unimodal low-variance distributions. This specifically detects variant contamination (paraphrased/restructured benchmark items) where ConStat and Min-K% fail (AUC 0.43-0.68 vs. DVD's 0.73-0.74). NOTE: DVD is promising but untested against RL-trained models — it was validated only on SFT-contaminated models (Qwen2.5, Llama3.1 fine-tuned). Whether the bimodal variance signature persists after GRPO/PPO training is an open empirical question that our RL-contamination experimental condition will directly test. DVD's value in the ensemble is therefore primarily for detecting variant contamination in the non-RL model majority, with DIF providing the RL-robust complement.\n\n(e) *Membership-inference probes* (Min-K% Prob / ReCaLL) where white-box access is available — retained as a cheap first-pass filter effective against non-RL models, but explicitly acknowledged as fragile against GRPO/PPO-trained models per Wang et al. (AUROC drops to ~50% after ~156 GRPO steps).\n\nTrigger regeneration when an item is flagged by >= 2 independent signals, with FDR-controlled thresholds. The ensemble is explicitly designed so that DIF (group-level, analytically RL-robust as demonstrated above) and DVD (generation-variance, variant-robust on SFT models) provide coverage where individual-level methods fail. Genuine capability gains will produce uniform improvement across original and perturbed items (no ConStat signal), across cohorts controlling for ability (no DIF signal), and across temperature samples (no DVD signal), while contamination produces item-specific anomalies in at least two of these dimensions.\n\n**Stage 2: Construct-Constrained Generation with Empirical Calibration.** Critically, we abandon the original approach of conditioning generators on raw IRT parameters — research shows LLMs achieve only rho=0.10-0.45 correlation with actual difficulty (arXiv 2602.06631). Instead: (a) For each flagged item, prompt a frontier generator (DeepSeek-V4-Pro or Qwen-3.5-397B) conditioned on the item's construct tag, cognitive complexity level (Bloom's taxonomy), format template, and 3-5 exemplar items from the same difficulty band — but NOT explicit IRT parameters; (b) Generate 8-10 candidates per flagged item using a multi-agent framework (generator + evaluator + refiner) inspired by ReQUESTA, with iterative critique loops; (c) Pre-screen candidates using student simulation — have a diverse panel of weaker/mid-tier LLMs (4B-14B parameters) role-play as examinees at varying ability levels, estimating approximate difficulty via simulated IRT (achieving r=0.75-0.82 per arXiv 2601.09953), and discard candidates whose estimated difficulty deviates by >1.5 logits from the target; (d) Optionally pre-filter candidates using Hardy et al.'s signed isotonic R² scalability coefficients (arXiv 2603.24999) as a fast, nonparametric quality check — items with anomalously low scalability coefficients (indicating poor construct alignment) are discarded before expensive panel calibration; (e) Empirically calibrate surviving candidates on the full calibration panel of 200-300 diverse LLMs via Bayesian fixed-parameter calibration (OH2PL, König, Spoden, & Frey, 2020), anchored to a preserved clean set (>= 20% of items, following the Kolen & Brennan 20% rule for stable equating). This generate-screen-calibrate pipeline is expected to achieve 30-50% rejection rates based on analogous AIG literature; we report convergence statistics as a key empirical contribution.\n\n**Stage 3: Bifactor IRT Equating Gate.** Move from naive unidimensional 2PL to a bifactor model (general LLM ability + domain-specific factors), which captures the inherently multi-construct nature of benchmarks like MMLU while remaining tractable for equating. Use Projective IRT (PIRT) to project bifactor parameters onto unidimensional equivalents compatible with standard equating software (demonstrated to produce very similar equating outcomes to full numerical integration, with practical advantages for implementation; Kim, 2022). Accept only replacements whose projected difficulty and discrimination fall within the 95% CI of the original item's parameters. Verify that the regenerated benchmark's test information function, construct coverage vector, and model ranking (Spearman rho >= 0.95) match the pre-contamination gold standard. Reject and re-generate otherwise, with a maximum of 3 regeneration cycles per item before flagging for human review.\n\n**Graceful Degradation Framework.** We define formal validity boundaries and fallback strategies for each failure mode, grounded in the test equating literature (Kolen & Brennan, 2004; Angoff, 1984):\n\n(i) *Anchor set integrity*: Maintain a minimum of 20% clean (uncontaminated) anchor items. If contamination detection flags items bringing the clean set below 20%, enter a degraded-but-valid operating mode: switch from standard Stocking-Lord equating to robust Area-Weighted or Least Absolute Values (LAV) equating methods (which tolerate outlying anchor items) and widen acceptance CIs to 99%. If the clean set drops below 15%, halt automated regeneration and flag the entire benchmark version for human review and potential full re-calibration. Below 10%, do not release.\n\n(ii) *Stage 1 error propagation*: False positives (flagging clean items as contaminated) trigger unnecessary regeneration but do not compromise validity — the equating gate (Stage 3) ensures replacements are psychometrically equivalent regardless of whether the original was truly contaminated. False negatives (missing contaminated items) are the more dangerous failure mode; we mitigate this by requiring only 2-of-5 signal agreement, with the understanding that DIF and DVD provide complementary coverage against RL-concealment and variant contamination respectively.\n\n(iii) *Stage 2 generation failure*: If <50% of candidates survive pre-screening for a given item (below the expected 50-70% survival rate), the system relaxes the logit-deviation threshold from 1.5 to 2.0 and generates a second batch of 8-10 candidates. If the item still fails after 3 regeneration cycles, it is flagged for human review but the benchmark continues operating with the original (potentially contaminated) item marked with a quality warning — preferable to reducing test length.\n\n(iv) *Stage 3 equating failure*: If >15% of items fail the equating gate after all regeneration cycles (meaning the benchmark cannot be fully regenerated), we release a partial-regeneration version with: (a) adjusted test information function reported alongside all scores, (b) model rankings computed on both the full benchmark and the clean-items-only subset for comparison, (c) marginal reliability coefficient reported — release only if marginal reliability ≥ 0.80 for group-level comparisons (per APA standards). This partial-release strategy provides transparent validity information rather than silently degraded scores.\n\n(v) *Minimum viable benchmark*: Formally, a regenerated benchmark version is released only if: marginal IRT reliability ≥ 0.80, Spearman rho ≥ 0.90 with the pre-contamination gold standard (relaxed from 0.95 in degraded mode), anchor set ≥ 15%, and SEM ≤ 0.35 across ≥ 70% of the target ability range. These thresholds are derived from operational testing standards (Kolen & Brennan, 2004) adapted for the LLM evaluation context where group-level comparisons (model rankings) are the primary use case.\n\n**Evaluation Strategy.** Validate on three tiers: (a) Primary — LiveBench subsets (math, reasoning, coding) as currently-uncontaminated benchmarks with diverse task types and temporal structure; simulate contamination by fine-tuning open-weight models on specific LiveBench items at controlled rates (10-50%) and measuring detection sensitivity and ranking recovery. Critically, include an RL-contamination condition: apply GRPO fine-tuning (following Wang et al.'s protocol of ~156 steps on contaminated data) to open-weight models on benchmark items and verify that DIF-based detection remains effective while individual-level methods degrade — this directly tests the analytical demonstration's predictions. Additionally, test DVD's bimodal variance signature under RL contamination to determine whether it is robust, partially robust, or fragile (resolving the current empirical gap). (b) Secondary — MMLU-CF (the contamination-free MMLU replacement, ACL 2025) for knowledge-domain evaluation, running the full regeneration pipeline on synthetically contaminated subsets. (c) Positive control — use naturally-contaminated MMLU/GSM8K items (with documented contamination evidence from GSM1K studies) to verify that the contamination sentinel detects known real-world contamination. Additionally, include a **pilot feasibility study** on a single LiveBench math subset (~200 items): run the full generate-screen-calibrate-gate pipeline and report rejection rates, convergence speed, parameter recovery accuracy, ranking preservation, and graceful-degradation trigger rates — providing the first empirical evidence of generate-test-reject convergence for IRT-equated benchmark items.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '900-1300 (inference of 200-300 models on ~5K items each for IRT calibration across multiple rounds, plus item generation with 70B+ models, plus student simulation panel, plus DVD temperature-sampling at 50 generations/item)', 'timeline': '5-6 months (1.5 months multi-signal contamination detector including DIF infrastructure and DVD adaptation, 1.5 months bifactor IRT calibration infrastructure, 1.5 months generation pipeline with student simulation, 1.5 months experiments including RL-contamination condition, pilot feasibility study, and writing)', 'estimated_gpu_cost': '$1800-$2600 at ~$2/hr H100 spot pricing', 'closed_source_api_cost': '$800-$2000 (API calls for ~30-50 closed-source models in calibration panel: GPT-4o, Claude, Gemini, etc. at ~5K items each, plus student simulation inference, plus DVD temperature-sampling for closed-source models)'}, 'human_in_loop': {'gpu_hours': '800-1100 (same inference needs, Claude handles generation orchestration, IRT analysis code, DIF implementation, and DVD adaptation)', 'timeline': '3.5-4.5 months (Claude drafts contamination detection, equating code, DIF pipeline, and student simulation; human validates IRT assumptions, bifactor model specification, DIF power analysis, and experimental design)', 'claude_api_cost': '$400-$700 (Sonnet 4.6 for code generation and pipeline orchestration, ~120M tokens total with caching)', 'estimated_gpu_cost': '$1600-$2200', 'closed_source_api_cost': '$800-$2000'}, 'auto_research': {'gpu_hours': '900-1200 (cannot reduce inference needs for 200-300 model calibration panel; DVD temperature-sampling adds ~10% overhead)', 'timeline': '8-12 weeks (parallelized model evaluation is the critical path; 200-300 model panel requires ~3 weeks per calibration round even with full parallelism; pilot feasibility study adds ~2 weeks; RL-contamination condition adds ~1 week for GRPO training)', 'claude_api_cost': '$800-$1200 (Opus 4.7 for experimental design and IRT analysis, Sonnet 4.6 for implementation, ~180M tokens with caching)', 'estimated_gpu_cost': '$1800-$2400', 'closed_source_api_cost': '$800-$2000', 'speed_bottleneck': 'IRT calibration panel: collecting responses from 200-300 diverse LLMs on pilot items requires sequential API calls to closed-source models (rate limits) and batched inference on open-weight models (GPU scheduling). Minimum ~3 weeks for a single calibration round with full parallelism across ~150 open-weight models and ~50 closed-source APIs. The pilot feasibility study requires at least 2 full calibration rounds. DVD temperature-sampling (50 generations/item) adds ~10% to inference costs.'}}\n\n## Inspired By\nField guide finding that 'contamination resistance degrades question fidelity'; gap between dynamic evaluation (LiveBench, DyVal) and psychometric rigor (IRT, ATLAS); cross-domain transfer of IRT equating from educational testing to benchmark maintenance; arXiv 2602.06631's demonstration that LLMs cannot directly target difficulty parameters, motivating empirical calibration; 'Test of Time' (2025) showing temporal contamination signals are unreliable, motivating multi-signal approaches; Wang et al. (ICLR 2026) showing RL conceals all individual-level contamination signals, motivating group-level DIF analysis; Wang & Heckel (2026) showing task familiarity artifacts produce uniform improvements distinguishable from item-specific contamination via DIF; DVD's demonstration that variant contamination requires specialized detection signals; Hardy et al.'s signed isotonic R² as a lightweight pre-filter complementing parametric IRT; Sander et al.'s watermarking paradigm motivating a complementary post-hoc remediation approach; bifactor IRT and PIRT as a practical bridge between unidimensional oversimplification and intractable full MIRT; Kolen & Brennan's anchor-set theory providing formal graceful-degradation thresholds.\n\n## Target Venues\n- ICLR 2027 (deadline expected ~October 2026 based on historical pattern — not yet announced; ideal timeline for thorough experiments including pilot feasibility study and RL-contamination condition; PRIMARY TARGET)\n- AAAI 2027 (abstract July 21, paper July 28, 2026 — tight but feasible if pilot study is scoped to single domain; 2 months)\n- EACL 2027 via ARR August 2026 cycle (submission August 3, 2026 — feasible with focused experiments on LiveBench math subset)\n\n## Key References\n- LiveBench: A Challenging, Contamination-Free LLM Benchmark (ICLR 2025)\n- LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code (ICLR 2025)\n- Automating Benchmark Design [BeTaL] (ICLR 2026)\n- BenchBench: Benchmarking Automated Benchmark Generation (arXiv 2026)\n- Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration (arXiv April 2026)\n- Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory [PSN-IRT] (AAAI 2026 Oral)\n- The stability of IRT parameters under several test equating conditions (Frontiers in Psychology 2026)\n- Estimating Exam Item Difficulty with LLMs: A Benchmark on Brazil's ENEM Corpus (arXiv 2602.06631, Feb 2026)\n- Take Out Your Calculators: Estimating Real Difficulty with LLM Student Simulations (arXiv 2601.09953, Jan 2026)\n- Reconstructing Item Characteristic Curves with Fine-Tuned LLMs (arXiv 2601.02580, Jan 2026)\n- ReQUESTA: Hybrid Multi-Agent Framework for MCQ Generation (arXiv 2602.03704, Feb 2026)\n- Test of Time: Rethinking Temporal Signal of Benchmark Contamination (arXiv 2509.00072, 2025)\n- ConStat: Performance-Based Contamination Detection with FDR Control (ETH Zurich 2024)\n- Establishing Trustworthy LLM Evaluation via Shortcut Neuron Analysis (ACL 2025)\n- On The Fragility of Benchmark Contamination Detection in Reasoning Models (Wang et al., arXiv 2510.02386, ICLR 2026)\n- Detecting Data Contamination from Reinforcement Learning Post-training [Self-Critique / RL-MIA] (Tao et al., arXiv 2510.09259, ICLR 2026)\n- DVD: Detection via Variance of Generation Distribution for Variant Contamination (Liang et al., arXiv 2601.04895, Jan 2026)\n- Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis [CCV] (arXiv 2603.21454, March 2026)\n- Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients (Hardy et al., arXiv 2603.24999, March 2026)\n- Detecting Benchmark Contamination Through Watermarking (Sander et al., arXiv 2502.17259, Feb 2025)\n- Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks (Wang & Heckel, arXiv 2603.12875, March 2026)\n- Application of IRT Fixed Parameter Calibration to Multiple-Group Test Data (Kim & Kolen, Applied Measurement in Education 2019)\n- An Optimized Bayesian Hierarchical Two-Parameter Logistic Model for Small-Sample Item Calibration [OH2PL] (König, Spoden, & Frey, Applied Psychological Measurement 2020, PMC7262992)\n- Robustness of the OH2PL for Small-Sample Item Calibration (König, Spoden, & Frey, Behavior Research Methods 2022)\n- Approximating Bifactor IRT Equating with Projective IRT [PIRT] (PMC 2020)\n- Item Response Theory True Score Equating for the Bifactor Model (Kim, Journal of Educational Measurement 2022)\n- Several Variations of Simple-Structure MIRT Equating (Kim, Journal of Educational Measurement 2023)\n- MMLU-CF: A Contamination-Free Multi-task Language Understanding Benchmark (ACL 2025)\n- Simulating Training Data Leakage in Multiple-Choice Benchmarks (arXiv 2505.24263, 2025)\n- VarBench: Robust Language Model Benchmarking Through Dynamic Variable Perturbation (EMNLP 2024)\n- DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks (ICLR 2024)\n- RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning (arXiv 2025)\n- Adaptive Testing for LLM Evaluation [ATLAS] (arXiv 2025)\n- Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation (EMNLP 2025)\n- Automatic- and Transformer-Based AIG: A Critical Review (Sommer & Arendasy, Intelligence 2025)\n- Can LLMs Estimate Student Struggles? The Curse of Knowledge Effect (arXiv 2512.18880, 2025)\n- Quantifying Data Contamination in Psychometric Evaluations of LLMs (Han et al., arXiv 2510.07175, 2025)\n- Using Past Data to Enhance Small-Sample DIF Estimation: A Bayesian Approach (Sinharay et al., ETS Research Report RR-06-09, 2006)\n- Testing Differential Item Functioning in Small Samples (Belzak, Multivariate Behavioral Research 2020)\n- Item-Focused Trees for the Detection of Differential Item Functioning (Tutz & Berger, Psychometrika 2016)\n- Test Equating, Scaling, and Linking: Methods and Practices 3rd ed. (Kolen & Brennan, Springer 2014)\n- A Careful Examination of Large Language Model Performance on Grade School Arithmetic [GSM1K] (arXiv 2405.00332, 2024)\n- Power and Sample Size Calculations for Logistic Regression Tests for Differential Item Functioning (PMC5978487)\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T03:32:20.996Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:32:20.996Z",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258"
}
```

---

## Round 1

38 recorded events

### User

_source line 3 · 2026-05-20T03:32:21.008Z_

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
  "promptId": "2e94d9b7-5180-4424-b4fc-3452186c260e",
  "type": "user",
  "uuid": "de3a4c75-c8c7-4bd7-974a-cb4eadb9cad1",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:32:21.007Z_

```json
{
  "parentUuid": "de3a4c75-c8c7-4bd7-974a-cb4eadb9cad1",
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
  "uuid": "160fae94-3bfa-4cca-8cf3-3285df0560f3",
  "timestamp": "2026-05-20T03:32:21.007Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:32:21.007Z_

```json
{
  "parentUuid": "160fae94-3bfa-4cca-8cf3-3285df0560f3",
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
  "uuid": "1df23234-70f1-4783-a4b2-f243029a1c96",
  "timestamp": "2026-05-20T03:32:21.007Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-20T03:32:21.007Z_

```json
{
  "parentUuid": "1df23234-70f1-4783-a4b2-f243029a1c96",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "79a28b33-3818-4fc8-af05-ac57638ef586",
  "timestamp": "2026-05-20T03:32:21.007Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
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
  "leafUuid": "79a28b33-3818-4fc8-af05-ac57638ef586",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Self-healing benchmarks with DIF-based contamination detection",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258"
}
```

---

### Assistant

_source line 9 · 2026-05-20T03:32:42.343Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for CoRL 2026 (Conference on Robot Learning). Let me first carefully read through the proposal, then conduct web searches to understand the field landscape before providing my assessment.

Wait - the user says "CoRL 2026" but the proposal's target venues are ICLR 2027, AAAI 2027, and EACL 2027. This is about LLM benchmark contamination detection and regeneration using IRT methods - not robotics at all. Let me note this but focus on evaluating the idea quality itself.


There's definitely a venue mismatch here - the proposal targets NLP/ML conferences while CoRL is specifically for robot learning research. I should acknowledge this discrepancy but proceed with evaluating the core idea quality as requested.

Before I assess the proposal, I need to search for recent work in several areas: benchmark contamination detection methods, IRT-based evaluation frameworks for language models, dynamic benchmark generation techniques, differential item functioning analysis applied to LLM benchmarks, and the specific papers this proposal references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79a28b33-3818-4fc8-af05-ac57638ef586",
  "isSidechain": false,
  "requestId": "req_011CbD7gdRp92GLnGtME7CEP",
  "type": "assistant",
  "uuid": "d5630483-7d50-40e8-bf2f-9fd8bc514214",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R3bjF3bJxwCay8WbjJSVcH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12446,
      "cache_read_input_tokens": 13591,
      "output_tokens": 605,
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
          "output_tokens": 605,
          "cache_read_input_tokens": 13591,
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

_source line 10 · 2026-05-20T03:32:42.352Z_

I'll start by conducting the required field research before making any assessment. Let me search for the key topics in this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5630483-7d50-40e8-bf2f-9fd8bc514214",
  "isSidechain": false,
  "requestId": "req_011CbD7gdRp92GLnGtME7CEP",
  "type": "assistant",
  "uuid": "ea06ffc8-a22d-4e6f-8071-6a6a2e777f82",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R3bjF3bJxwCay8WbjJSVcH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12446,
      "cache_read_input_tokens": 13591,
      "output_tokens": 605,
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
          "output_tokens": 605,
          "cache_read_input_tokens": 13591,
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

_source line 11 · 2026-05-20T03:32:42.384Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JQkrKcC1K8TFvX8he3mKDp`</summary>

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
  "parentUuid": "ea06ffc8-a22d-4e6f-8071-6a6a2e777f82",
  "isSidechain": false,
  "requestId": "req_011CbD7gdRp92GLnGtME7CEP",
  "type": "assistant",
  "uuid": "77fee705-f00b-4112-a403-d3a93020f15c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R3bjF3bJxwCay8WbjJSVcH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12446,
      "cache_read_input_tokens": 13591,
      "output_tokens": 605,
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
          "output_tokens": 605,
          "cache_read_input_tokens": 13591,
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

_source line 12 · 2026-05-20T03:32:42.391Z_

<details><summary>↩ Tool result · `toolu_01JQkrKcC1K8TFvX8he3mKDp`</summary>

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
  "parentUuid": "77fee705-f00b-4112-a403-d3a93020f15c",
  "isSidechain": false,
  "promptId": "2e94d9b7-5180-4424-b4fc-3452186c260e",
  "type": "user",
  "uuid": "133bb8de-12ac-40a0-bde2-acf71fac275c",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "77fee705-f00b-4112-a403-d3a93020f15c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-20T03:32:45.493Z_

Now let me conduct the required field research with targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "133bb8de-12ac-40a0-bde2-acf71fac275c",
  "isSidechain": false,
  "requestId": "req_011CbD7iD1C7JSr1pGLpv3FV",
  "type": "assistant",
  "uuid": "73e4da13-402c-4a6e-8949-467fe9dff4c2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZyKy3TL15ucaihsTMNV8m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 26037,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1132,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 287,
          "cache_read_input_tokens": 26037,
          "cache_creation_input_tokens": 1132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1132
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

_source line 14 · 2026-05-20T03:32:46.165Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012H6yRhMaEE6s8eY8qTtQND`</summary>

```json
{
  "query": "benchmark contamination detection RL reasoning models 2025 2026 ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73e4da13-402c-4a6e-8949-467fe9dff4c2",
  "isSidechain": false,
  "requestId": "req_011CbD7iD1C7JSr1pGLpv3FV",
  "type": "assistant",
  "uuid": "47a05861-3c8e-4721-9e80-7887dbec538c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZyKy3TL15ucaihsTMNV8m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 26037,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1132,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 287,
          "cache_read_input_tokens": 26037,
          "cache_creation_input_tokens": 1132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1132
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

_source line 15 · 2026-05-20T03:32:46.444Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CyXTA1iUfjtCgikV8dUna9`</summary>

```json
{
  "query": "IRT equating LLM benchmark evaluation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47a05861-3c8e-4721-9e80-7887dbec538c",
  "isSidechain": false,
  "requestId": "req_011CbD7iD1C7JSr1pGLpv3FV",
  "type": "assistant",
  "uuid": "4de200a5-6480-4397-8fdd-67ef1f8b54d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZyKy3TL15ucaihsTMNV8m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 26037,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1132,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 287,
          "cache_read_input_tokens": 26037,
          "cache_creation_input_tokens": 1132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1132
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

_source line 16 · 2026-05-20T03:32:46.914Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011UjzL7LZQjM8LeSi58gGbQ`</summary>

```json
{
  "query": "dynamic benchmark regeneration self-healing contamination LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4de200a5-6480-4397-8fdd-67ef1f8b54d6",
  "isSidechain": false,
  "requestId": "req_011CbD7iD1C7JSr1pGLpv3FV",
  "type": "assistant",
  "uuid": "cd347ce3-2527-437d-9af0-10701bdfad61",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZyKy3TL15ucaihsTMNV8m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 26037,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1132,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 287,
          "cache_read_input_tokens": 26037,
          "cache_creation_input_tokens": 1132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1132
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

_source line 17 · 2026-05-20T03:32:47.920Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EaiJV23pY1o137239M7Ge9`</summary>

```json
{
  "query": "Differential Item Functioning DIF LLM evaluation benchmark 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd347ce3-2527-437d-9af0-10701bdfad61",
  "isSidechain": false,
  "requestId": "req_011CbD7iD1C7JSr1pGLpv3FV",
  "type": "assistant",
  "uuid": "4763189f-0b00-4f12-a93c-e8765b5e3aea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZyKy3TL15ucaihsTMNV8m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 26037,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1132,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 287,
          "cache_read_input_tokens": 26037,
          "cache_creation_input_tokens": 1132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1132
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

_source line 18 · 2026-05-20T03:32:48.318Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VsAE22dSMCrh1ryDHdDswM`</summary>

```json
{
  "query": "\"Growing Pains\" IRT fixed parameter calibration LLM benchmark 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4763189f-0b00-4f12-a93c-e8765b5e3aea",
  "isSidechain": false,
  "requestId": "req_011CbD7iD1C7JSr1pGLpv3FV",
  "type": "assistant",
  "uuid": "003f62f7-6148-4ac4-b563-4b4ecf3398e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZyKy3TL15ucaihsTMNV8m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 26037,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1132,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 287,
          "cache_read_input_tokens": 26037,
          "cache_creation_input_tokens": 1132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1132
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

_source line 19 · 2026-05-20T03:32:55.285Z_

<details><summary>↩ Tool result · `toolu_01EaiJV23pY1o137239M7Ge9`</summary>

```text
Web search results for query: "Differential Item Functioning DIF LLM evaluation benchmark 2025 2026"

Links: [{"title":"A Log-Linear Modeling Approach for Differential Item Functioning Detection in Polytomously Scored Items - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC6943994/"},{"title":"Finding Words Associated with DIF: Predicting Differential Item Functioning using LLMs and Explainable AI","url":"https://arxiv.org/pdf/2502.07017"},{"title":"DIF: A Framework for Benchmarking and Verifying Implicit Bias in LLMs","url":"https://arxiv.org/pdf/2505.10013"},{"title":"Finding Words Associated with DIF: Predicting Differential Item Functioning Using LLMs and Explainable AI - Maeda - Journal of Educational Measurement - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1111/jedm.70017"},{"title":"On the Complex Sources of Differential Item Functioning: A Comparison of Three Methods - Haeju Lee, Sijia Huang, Dubravka Svetina Valdivia, Ben Schwartzman, 2026","url":"https://journals.sagepub.com/doi/10.1177/00131644251379802"},{"title":"Examining differential item functioning in self-reported health survey data: via multilevel modeling - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/40021525/"},{"title":"LLM benchmarks in 2026: What they prove and what your business actually needs | High-Quality AI Data to Power Innovation | LXT","url":"https://www.lxt.ai/blog/llm-benchmarks/"},{"title":"Differential item functioning between English, German, and Spanish PROMIS® physical function ceiling items","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12064622/"}]

Based on the search results, I found several relevant findings related to your query:

## Recent Work on DIF and LLMs

A framework called DIF (Demographic Implicit Fairness) has been developed to benchmark and verify implicit bias in LLMs by evaluating preexisting LLM logic and math problem datasets with sociodemographic personas.

Items that exhibit bias can be identified using differential item functioning (DIF) analysis, which occurs when correct item response probability depends on the examinee's demographic background, even after accounting for ability.

## Using LLMs to Detect DIF

A study applies LLM approaches among eight DIF group pairs to examine the words associated with DIF, involving both quantitative and qualitative evaluation. Despite the current popularity of decoder-only LLMs like GPT, encoder-only models like BERT have efficiency advantages for specialized, nongenerative tasks, with DeBERTa introducing innovations in attention mechanisms.

## Recent 2025-2026 Research

The recently proposed least absolute shrinkage and selection operator (LASSO) regularization method has shown promising results for detecting DIF on multiple background variables, and has been compared with non-IRT-based logistic regression and IRT-based likelihood ratio test methods.

The search results show active recent research combining DIF analysis with LLM-based approaches for evaluating fairness and bias in both language models and assessment items.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4763189f-0b00-4f12-a93c-e8765b5e3aea",
  "isSidechain": false,
  "promptId": "2e94d9b7-5180-4424-b4fc-3452186c260e",
  "type": "user",
  "uuid": "b1c91bf0-0ddb-4864-bfd8-cca6dfc16c00",
  "toolUseResult": {
    "query": "Differential Item Functioning DIF LLM evaluation benchmark 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HTp5aaVWfPBYQsGJNPvxCe",
        "content": [
          {
            "title": "A Log-Linear Modeling Approach for Differential Item Functioning Detection in Polytomously Scored Items - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6943994/"
          },
          {
            "title": "Finding Words Associated with DIF: Predicting Differential Item Functioning using LLMs and Explainable AI",
            "url": "https://arxiv.org/pdf/2502.07017"
          },
          {
            "title": "DIF: A Framework for Benchmarking and Verifying Implicit Bias in LLMs",
            "url": "https://arxiv.org/pdf/2505.10013"
          },
          {
            "title": "Finding Words Associated with DIF: Predicting Differential Item Functioning Using LLMs and Explainable AI - Maeda - Journal of Educational Measurement - Wiley Online Library",
            "url": "https://onlinelibrary.wiley.com/doi/10.1111/jedm.70017"
          },
          {
            "title": "On the Complex Sources of Differential Item Functioning: A Comparison of Three Methods - Haeju Lee, Sijia Huang, Dubravka Svetina Valdivia, Ben Schwartzman, 2026",
            "url": "https://journals.sagepub.com/doi/10.1177/00131644251379802"
          },
          {
            "title": "Examining differential item functioning in self-reported health survey data: via multilevel modeling - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/40021525/"
          },
          {
            "title": "LLM benchmarks in 2026: What they prove and what your business actually needs | High-Quality AI Data to Power Innovation | LXT",
            "url": "https://www.lxt.ai/blog/llm-benchmarks/"
          },
          {
            "title": "Differential item functioning between English, German, and Spanish PROMIS® physical function ceiling items",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12064622/"
          }
        ]
      },
      "Based on the search results, I found several relevant findings related to your query:\n\n## Recent Work on DIF and LLMs\n\nA framework called DIF (Demographic Implicit Fairness) has been developed to benchmark and verify implicit bias in LLMs by evaluating preexisting LLM logic and math problem datasets with sociodemographic personas.\n\nItems that exhibit bias can be identified using differential item functioning (DIF) analysis, which occurs when correct item response probability depends on the examinee's demographic background, even after accounting for ability.\n\n## Using LLMs to Detect DIF\n\nA study applies LLM approaches among eight DIF group pairs to examine the words associated with DIF, involving both quantitative and qualitative evaluation. Despite the current popularity of decoder-only LLMs like GPT, encoder-only models like BERT have efficiency advantages for specialized, nongenerative tasks, with DeBERTa introducing innovations in attention mechanisms.\n\n## Recent 2025-2026 Research\n\nThe recently proposed least absolute shrinkage and selection operator (LASSO) regularization method has shown promising results for detecting DIF on multiple background variables, and has been compared with non-IRT-based logistic regression and IRT-based likelihood ratio test methods.\n\nThe search results show active recent research combining DIF analysis with LLM-based approaches for evaluating fairness and bias in both language models and assessment items."
    ],
    "durationSeconds": 7.362323182,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4763189f-0b00-4f12-a93c-e8765b5e3aea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T03:32:55.545Z_

<details><summary>↩ Tool result · `toolu_01VsAE22dSMCrh1ryDHdDswM`</summary>

```text
Web search results for query: ""Growing Pains" IRT fixed parameter calibration LLM benchmark 2026"

Links: [{"title":"[2604.12843] Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/abs/2604.12843"},{"title":"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/html/2604.12843"},{"title":"LLM benchmarks in 2026: What they prove and what your business actually needs | High-Quality AI Data to Power Innovation | LXT","url":"https://www.lxt.ai/blog/llm-benchmarks/"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2602.12424"},{"title":"State of LLM Benchmarks 2026: Rankings, Trends, and What Actually Changed | BenchLM.ai","url":"https://benchlm.ai/blog/posts/state-of-llm-benchmarks-2026"},{"title":"Preprint. Accepted at the ICLR 2026 LIT Workshop","url":"https://arxiv.org/pdf/2602.09924"},{"title":"Reconstructing Item Characteristic Curves using Fine-Tuned Large Language Models","url":"https://arxiv.org/pdf/2601.02580"}]

Based on the search results, I found the paper you're looking for:

"Growing Pains" proposes a framework based on multidimensional Item Response Theory (IRT) that uses anchor items to calibrate new benchmarks to the evaluation suite while holding previously calibrated item parameters fixed.

The approach supports a realistic evaluation setting in which datasets are introduced over time and models are evaluated only on the datasets available at the time of evaluation, while a fixed anchor set for each dataset is used so that results from different evaluation periods can be compared directly.

In large-scale experiments on more than 400 models, the framework predicts full-evaluation performance within 2-3 percentage points using only 100 anchor questions per dataset, with Spearman ρ≥0.9 for ranking preservation.

The paper was published on arXiv on April 15, 2026. Code is available at https://github.com/eliyahabba/growing-pains/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "003f62f7-6148-4ac4-b563-4b4ecf3398e7",
  "isSidechain": false,
  "promptId": "2e94d9b7-5180-4424-b4fc-3452186c260e",
  "type": "user",
  "uuid": "a8c0146e-6302-4868-a942-2221067b5b04",
  "toolUseResult": {
    "query": "\"Growing Pains\" IRT fixed parameter calibration LLM benchmark 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013ha5ZKv7wKrN6PJaQYwdeQ",
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
            "title": "LLM benchmarks in 2026: What they prove and what your business actually needs | High-Quality AI Data to Power Innovation | LXT",
            "url": "https://www.lxt.ai/blog/llm-benchmarks/"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2602.12424"
          },
          {
            "title": "State of LLM Benchmarks 2026: Rankings, Trends, and What Actually Changed | BenchLM.ai",
            "url": "https://benchlm.ai/blog/posts/state-of-llm-benchmarks-2026"
          },
          {
            "title": "Preprint. Accepted at the ICLR 2026 LIT Workshop",
            "url": "https://arxiv.org/pdf/2602.09924"
          },
          {
            "title": "Reconstructing Item Characteristic Curves using Fine-Tuned Large Language Models",
            "url": "https://arxiv.org/pdf/2601.02580"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n\"Growing Pains\" proposes a framework based on multidimensional Item Response Theory (IRT) that uses anchor items to calibrate new benchmarks to the evaluation suite while holding previously calibrated item parameters fixed.\n\nThe approach supports a realistic evaluation setting in which datasets are introduced over time and models are evaluated only on the datasets available at the time of evaluation, while a fixed anchor set for each dataset is used so that results from different evaluation periods can be compared directly.\n\nIn large-scale experiments on more than 400 models, the framework predicts full-evaluation performance within 2-3 percentage points using only 100 anchor questions per dataset, with Spearman ρ≥0.9 for ranking preservation.\n\nThe paper was published on arXiv on April 15, 2026. Code is available at https://github.com/eliyahabba/growing-pains/."
    ],
    "durationSeconds": 7.225161469999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "003f62f7-6148-4ac4-b563-4b4ecf3398e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T03:32:57.865Z_

<details><summary>↩ Tool result · `toolu_011UjzL7LZQjM8LeSi58gGbQ`</summary>

```text
Web search results for query: "dynamic benchmark regeneration self-healing contamination LLM 2026"

Links: [{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"},{"title":"Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation","url":"https://arxiv.org/html/2502.17521v2"},{"title":"Benchmark Data Contamination of Large Language Models: A Survey","url":"https://arxiv.org/html/2406.04244v1"},{"title":"LLM Leaderboard 2026: Best AI Models Benchmark & Ranking","url":"https://www.clickrank.ai/llm-leaderboard/"},{"title":"Benchmark Self-Evolving: A Multi-Agent Framework for Dynamic LLM   Evaluation","url":"https://arxiv.org/pdf/2402.11443"},{"title":"Recent Advances in Large Langauge Model Benchmarks against Data Contamination: From Static to Dynamic Evaluation","url":"https://arxiv.org/pdf/2502.17521"},{"title":"SWE-MERA: A Dynamic Benchmark for Agenticly Evaluating Large Language Models on Software Engineering Tasks","url":"https://arxiv.org/pdf/2507.11059"},{"title":"AntiLeakBench: Preventing Data Contamination by Automatically Constructing Benchmarks with Updated Real-World Knowledge","url":"https://arxiv.org/pdf/2412.13670"}]

Based on the search results, I found relevant information about dynamic benchmarks, regeneration, self-healing, and contamination issues with LLMs in 2026:

## Key Findings:

**Dynamic Benchmarking Approaches:**
Dynamic benchmarking methods aim to reduce contamination risk either by continuously updating benchmark datasets based on LLM training timestamps, or by regenerating test data to reconstruct and replace original benchmarks.

**Data Regeneration Methods:**
Data regeneration approaches like EvoEval and DyVal 2 emphasize restructuring and augmentation of existing datasets by dynamically configuring evaluation protocols and introducing new prompts to enhance the granularity and depth of model evaluations.

**Benchmark Self-Evolution:**
A benchmark self-evolving framework reframes existing benchmark instances into new variants for dynamic evaluation by modifying their contexts or questions and corresponding answers.

**Contamination Issues in 2026:**
DeepSeek V3.2 has faced the most public contamination scrutiny in 2026, with independent evaluators flagging statistically unusual score patterns on several well-known benchmarks. The 2026 standard is to use contamination-resistant benchmarks like LiveCodeBench, FrontierMath, and MMLU-Pro.

**Challenges with Dynamic Benchmarks:**
Current dynamic methods often lack standardized evaluation criteria, suffer from limited scalability, and offer little interpretability, while many fail to systematically assess trade-offs like computational overhead and robustness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd347ce3-2527-437d-9af0-10701bdfad61",
  "isSidechain": false,
  "promptId": "2e94d9b7-5180-4424-b4fc-3452186c260e",
  "type": "user",
  "uuid": "041de041-bd49-4d87-b431-c59a016e67b6",
  "toolUseResult": {
    "query": "dynamic benchmark regeneration self-healing contamination LLM 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014fKtw8QnaK39aMnFdrFNFD",
        "content": [
          {
            "title": "What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide",
            "url": "https://llm-stats.com/blog/research/what-is-a-contaminated-llm"
          },
          {
            "title": "Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation",
            "url": "https://arxiv.org/html/2502.17521v2"
          },
          {
            "title": "Benchmark Data Contamination of Large Language Models: A Survey",
            "url": "https://arxiv.org/html/2406.04244v1"
          },
          {
            "title": "LLM Leaderboard 2026: Best AI Models Benchmark & Ranking",
            "url": "https://www.clickrank.ai/llm-leaderboard/"
          },
          {
            "title": "Benchmark Self-Evolving: A Multi-Agent Framework for Dynamic LLM   Evaluation",
            "url": "https://arxiv.org/pdf/2402.11443"
          },
          {
            "title": "Recent Advances in Large Langauge Model Benchmarks against Data Contamination: From Static to Dynamic Evaluation",
            "url": "https://arxiv.org/pdf/2502.17521"
          },
          {
            "title": "SWE-MERA: A Dynamic Benchmark for Agenticly Evaluating Large Language Models on Software Engineering Tasks",
            "url": "https://arxiv.org/pdf/2507.11059"
          },
          {
            "title": "AntiLeakBench: Preventing Data Contamination by Automatically Constructing Benchmarks with Updated Real-World Knowledge",
            "url": "https://arxiv.org/pdf/2412.13670"
          }
        ]
      },
      "Based on the search results, I found relevant information about dynamic benchmarks, regeneration, self-healing, and contamination issues with LLMs in 2026:\n\n## Key Findings:\n\n**Dynamic Benchmarking Approaches:**\nDynamic benchmarking methods aim to reduce contamination risk either by continuously updating benchmark datasets based on LLM training timestamps, or by regenerating test data to reconstruct and replace original benchmarks.\n\n**Data Regeneration Methods:**\nData regeneration approaches like EvoEval and DyVal 2 emphasize restructuring and augmentation of existing datasets by dynamically configuring evaluation protocols and introducing new prompts to enhance the granularity and depth of model evaluations.\n\n**Benchmark Self-Evolution:**\nA benchmark self-evolving framework reframes existing benchmark instances into new variants for dynamic evaluation by modifying their contexts or questions and corresponding answers.\n\n**Contamination Issues in 2026:**\nDeepSeek V3.2 has faced the most public contamination scrutiny in 2026, with independent evaluators flagging statistically unusual score patterns on several well-known benchmarks. The 2026 standard is to use contamination-resistant benchmarks like LiveCodeBench, FrontierMath, and MMLU-Pro.\n\n**Challenges with Dynamic Benchmarks:**\nCurrent dynamic methods often lack standardized evaluation criteria, suffer from limited scalability, and offer little interpretability, while many fail to systematically assess trade-offs like computational overhead and robustness."
    ],
    "durationSeconds": 10.948527088999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "cd347ce3-2527-437d-9af0-10701bdfad61",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
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
  "leafUuid": "041de041-bd49-4d87-b431-c59a016e67b6",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Self-healing benchmarks with DIF-based contamination detection",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258"
}
```

---

### Tool result

_source line 24 · 2026-05-20T03:33:01.418Z_

<details><summary>↩ Tool result · `toolu_01CyXTA1iUfjtCgikV8dUna9`</summary>

```text
Web search results for query: "IRT equating LLM benchmark evaluation 2025 2026"

Links: [{"title":"[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/abs/2505.15055"},{"title":"2025 December \"AI Evaluation\" Digest","url":"https://aievaluation.substack.com/p/2025-december-ai-evaluation-digest"},{"title":"LLM Evaluation Frameworks 2025 vs 2026: What Matters ...","url":"https://www.mlaidigital.com/blogs/llm-evaluation-frameworks-2025-vs-2026-what-matters-now-2026"},{"title":"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/html/2604.12843"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/pdf/2511.04689"},{"title":"Measuring Competency, Not Performance: Item-Aware Evaluation Across Medical Benchmarks","url":"https://arxiv.org/pdf/2509.24186"},{"title":"LLM benchmarks in 2026: What they prove and what your business actually needs | High-Quality AI Data to Power Innovation | LXT","url":"https://www.lxt.ai/blog/llm-benchmarks/"},{"title":"A Survey on Evaluation of LLM-based Agents","url":"https://arxiv.org/html/2503.16416v2"}]

Based on the web search results, here's what I found regarding IRT equating and LLM benchmark evaluation in 2025-2026:

## Key Research and Developments

Recent research addresses inconsistencies between different leaderboards and poor separability among top models, raising concerns about benchmark accuracy in reflecting authentic model capabilities. A notable approach is the Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced IRT framework that was used to analyze 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality.

## IRT Applications in Evaluation

ATLAS, an adaptive testing framework based on Item Response Theory, estimates model ability using Fisher information-guided item selection and reduces the number of required items by up to 90% while maintaining measurement precision.

IRT is the only framework that simultaneously (1) jointly estimates model ability and item difficulty on a shared scale; (2) provides a generative model of model-item interactions supporting prediction on unseen items; and (3) enables construct validation via exploratory factor analysis.

## Broader Evaluation Trends

From 2025 to 2026, LLM evaluation frameworks have advanced from benchmark-based model evaluation to system-level evaluation. Additionally, psychometric methods have been applied to uncover the latent capability structure of LLMs, with factor-analytic studies identifying between three and eight interpretable skill dimensions that explain much of the variance in model performance across diverse tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4de200a5-6480-4397-8fdd-67ef1f8b54d6",
  "isSidechain": false,
  "promptId": "2e94d9b7-5180-4424-b4fc-3452186c260e",
  "type": "user",
  "uuid": "b9614d06-0242-4f61-9deb-efc84501e646",
  "toolUseResult": {
    "query": "IRT equating LLM benchmark evaluation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01V4KGXVavTYxoEbVkbRoNoF",
        "content": [
          {
            "title": "[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/abs/2505.15055"
          },
          {
            "title": "2025 December \"AI Evaluation\" Digest",
            "url": "https://aievaluation.substack.com/p/2025-december-ai-evaluation-digest"
          },
          {
            "title": "LLM Evaluation Frameworks 2025 vs 2026: What Matters ...",
            "url": "https://www.mlaidigital.com/blogs/llm-evaluation-frameworks-2025-vs-2026-what-matters-now-2026"
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
            "title": "Measuring Competency, Not Performance: Item-Aware Evaluation Across Medical Benchmarks",
            "url": "https://arxiv.org/pdf/2509.24186"
          },
          {
            "title": "LLM benchmarks in 2026: What they prove and what your business actually needs | High-Quality AI Data to Power Innovation | LXT",
            "url": "https://www.lxt.ai/blog/llm-benchmarks/"
          },
          {
            "title": "A Survey on Evaluation of LLM-based Agents",
            "url": "https://arxiv.org/html/2503.16416v2"
          }
        ]
      },
      "Based on the web search results, here's what I found regarding IRT equating and LLM benchmark evaluation in 2025-2026:\n\n## Key Research and Developments\n\nRecent research addresses inconsistencies between different leaderboards and poor separability among top models, raising concerns about benchmark accuracy in reflecting authentic model capabilities. A notable approach is the Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced IRT framework that was used to analyze 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality.\n\n## IRT Applications in Evaluation\n\nATLAS, an adaptive testing framework based on Item Response Theory, estimates model ability using Fisher information-guided item selection and reduces the number of required items by up to 90% while maintaining measurement precision.\n\nIRT is the only framework that simultaneously (1) jointly estimates model ability and item difficulty on a shared scale; (2) provides a generative model of model-item interactions supporting prediction on unseen items; and (3) enables construct validation via exploratory factor analysis.\n\n## Broader Evaluation Trends\n\nFrom 2025 to 2026, LLM evaluation frameworks have advanced from benchmark-based model evaluation to system-level evaluation. Additionally, psychometric methods have been applied to uncover the latent capability structure of LLMs, with factor-analytic studies identifying between three and eight interpretable skill dimensions that explain much of the variance in model performance across diverse tasks."
    ],
    "durationSeconds": 14.970500046000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4de200a5-6480-4397-8fdd-67ef1f8b54d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-20T03:33:03.912Z_

<details><summary>↩ Tool result · `toolu_012H6yRhMaEE6s8eY8qTtQND`</summary>

```text
Web search results for query: "benchmark contamination detection RL reasoning models 2025 2026 ICLR"

Links: [{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/pdf/2510.02386"},{"title":"[2510.09259] Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/abs/2510.09259"},{"title":"[2510.02386] On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/abs/2510.02386"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/html/2510.02386v1"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=bhR00j6Mku"},{"title":"DETECTING BENCHMARK CONTAMINATION THROUGH ...","url":"https://openreview.net/pdf?id=WFGxFzFDmQ"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2509.24210"},{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"}]

I've found several relevant research papers and resources on benchmark contamination detection in reasoning models. Here are the key findings:

## Primary Research Papers

Various benchmark contamination detection methods have been proposed to determine whether specific benchmarks were used during training, based on the assumption that contamination in LLMs primarily involves memorizing the benchmark data.

### "On The Fragility of Benchmark Contamination Detection in Reasoning Models" (2025)

As LLMs have evolved into Large Reasoning Models (LRMs), benchmark contamination detection faces two key challenges: LRMs rely on chain-of-thought (CoT) reasoning to reach final answers, but contamination detectors typically only have access to question-answer pairs without the intermediate reasoning steps used during training.

LRMs primarily acquire reasoning abilities during two stages: SFT and RL, which potentially provides developers with opportunities to manipulate leaderboard performance by strategically contaminating benchmarks in the earlier stage while evading detection methods through subsequent training.

PPO style importance sampling and clipping objectives are the root cause of detection concealment, indicating that a broad class of RL methods may inherently exhibit similar concealment capability.

### "Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models" (2025-2026)

While detection methods have been developed for the pre-training and Supervised Fine-Tuning stages, a critical research gap exists for the increasingly significant phase of Reinforcement Learning (RL) post-training.

These papers address significant challenges in detecting benchmark contamination specifically as reasoning models become more sophisticated with RL training and chain-of-thought reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47a05861-3c8e-4721-9e80-7887dbec538c",
  "isSidechain": false,
  "promptId": "2e94d9b7-5180-4424-b4fc-3452186c260e",
  "type": "user",
  "uuid": "ac54e97e-f72c-48d7-9918-d70c759373a9",
  "toolUseResult": {
    "query": "benchmark contamination detection RL reasoning models 2025 2026 ICLR",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Q3xnjSnonppg1JQJm7jXGY",
        "content": [
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/pdf/2510.02386"
          },
          {
            "title": "[2510.09259] Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models",
            "url": "https://arxiv.org/abs/2510.09259"
          },
          {
            "title": "[2510.02386] On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/abs/2510.02386"
          },
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/html/2510.02386v1"
          },
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models | OpenReview",
            "url": "https://openreview.net/forum?id=bhR00j6Mku"
          },
          {
            "title": "DETECTING BENCHMARK CONTAMINATION THROUGH ...",
            "url": "https://openreview.net/pdf?id=WFGxFzFDmQ"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2509.24210"
          },
          {
            "title": "What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide",
            "url": "https://llm-stats.com/blog/research/what-is-a-contaminated-llm"
          }
        ]
      },
      "I've found several relevant research papers and resources on benchmark contamination detection in reasoning models. Here are the key findings:\n\n## Primary Research Papers\n\nVarious benchmark contamination detection methods have been proposed to determine whether specific benchmarks were used during training, based on the assumption that contamination in LLMs primarily involves memorizing the benchmark data.\n\n### \"On The Fragility of Benchmark Contamination Detection in Reasoning Models\" (2025)\n\nAs LLMs have evolved into Large Reasoning Models (LRMs), benchmark contamination detection faces two key challenges: LRMs rely on chain-of-thought (CoT) reasoning to reach final answers, but contamination detectors typically only have access to question-answer pairs without the intermediate reasoning steps used during training.\n\nLRMs primarily acquire reasoning abilities during two stages: SFT and RL, which potentially provides developers with opportunities to manipulate leaderboard performance by strategically contaminating benchmarks in the earlier stage while evading detection methods through subsequent training.\n\nPPO style importance sampling and clipping objectives are the root cause of detection concealment, indicating that a broad class of RL methods may inherently exhibit similar concealment capability.\n\n### \"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models\" (2025-2026)\n\nWhile detection methods have been developed for the pre-training and Supervised Fine-Tuning stages, a critical research gap exists for the increasingly significant phase of Reinforcement Learning (RL) post-training.\n\nThese papers address significant challenges in detecting benchmark contamination specifically as reasoning models become more sophisticated with RL training and chain-of-thought reasoning."
    ],
    "durationSeconds": 17.741057328,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "47a05861-3c8e-4721-9e80-7887dbec538c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T03:33:07.031Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016j5zahqQc3hTkuoQpFuzFC`</summary>

```json
{
  "query": "DVD detection variance generation distribution variant contamination arXiv 2601.04895"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac54e97e-f72c-48d7-9918-d70c759373a9",
  "isSidechain": false,
  "requestId": "req_011CbD7jnnTytV4sdedjcrc8",
  "type": "assistant",
  "uuid": "0d61fbe2-2d74-4c9d-8403-03dcb77d2ed5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U57xh5vSbDFBoXRLmSqpV3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2992,
      "cache_creation_input_tokens": 1065,
      "cache_read_input_tokens": 27169,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1065,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2992,
          "output_tokens": 181,
          "cache_read_input_tokens": 27169,
          "cache_creation_input_tokens": 1065,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1065
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

_source line 27 · 2026-05-20T03:33:07.995Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A6a2wQ4zCf1M2DdwUWrsuQ`</summary>

```json
{
  "query": "Wang Heckel test-time RL alignment task familiarity artifacts benchmarks arXiv 2603.12875"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d61fbe2-2d74-4c9d-8403-03dcb77d2ed5",
  "isSidechain": false,
  "requestId": "req_011CbD7jnnTytV4sdedjcrc8",
  "type": "assistant",
  "uuid": "23b0ce6c-ce87-486d-8ac9-0c48a26db8af",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U57xh5vSbDFBoXRLmSqpV3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2992,
      "cache_creation_input_tokens": 1065,
      "cache_read_input_tokens": 27169,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1065,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2992,
          "output_tokens": 181,
          "cache_read_input_tokens": 27169,
          "cache_creation_input_tokens": 1065,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1065
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

_source line 28 · 2026-05-20T03:33:08.833Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0151ejvPxGGSwwcvjjWxvvEV`</summary>

```json
{
  "query": "BeTaL automating benchmark design ICLR 2026 dynamic difficulty"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23b0ce6c-ce87-486d-8ac9-0c48a26db8af",
  "isSidechain": false,
  "requestId": "req_011CbD7jnnTytV4sdedjcrc8",
  "type": "assistant",
  "uuid": "5fb9b36a-d66b-4104-9fbe-37be4c7442bd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U57xh5vSbDFBoXRLmSqpV3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2992,
      "cache_creation_input_tokens": 1065,
      "cache_read_input_tokens": 27169,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1065,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2992,
          "output_tokens": 181,
          "cache_read_input_tokens": 27169,
          "cache_creation_input_tokens": 1065,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1065
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

_source line 29 · 2026-05-20T03:33:13.650Z_

<details><summary>↩ Tool result · `toolu_01A6a2wQ4zCf1M2DdwUWrsuQ`</summary>

```text
Web search results for query: "Wang Heckel test-time RL alignment task familiarity artifacts benchmarks arXiv 2603.12875"

Links: [{"title":"[2603.12875] Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks","url":"https://arxiv.org/abs/2603.12875"},{"title":"MCML - Research Group Reinhard Heckel","url":"https://mcml.ai/research/groups/heckel/"},{"title":"Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks","url":"https://arxiv.org/pdf/2603.12875"},{"title":"Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks · benchmark | Festivus","url":"https://festivus.hapticlabs.ai/data/benchmarks/test-time-rl-alignment-exposes-task-familiarity-artifacts-in-llm-benchmarks"},{"title":"GitHub - smiles724/Awesome-LLM-RLVR: Collection of latest papers and materials in the area of RLVR! · GitHub","url":"https://github.com/smiles724/Awesome-LLM-RLVR"},{"title":"1 Fine-tuning gains are largely diminished after task alignment. Left: The reported performance reveals substantial accuracy gaps between base models and their fine-tuned variants. Right: After applying TTRA to all models, the base model’s performance increases significantly, nearly matching that of the fine-tuned models, suggesting that many gains from RLVR/SFT reported in the literature are not a difference in reasoning capability, but rather artifacts of task familiarity.","url":"https://arxiv.org/html/2603.12875"},{"title":"s1: Simple test-time scaling | Request PDF","url":"https://www.researchgate.net/publication/397423327_s1_Simple_test-time_scaling"},{"title":"Mirage or Method? How Model-Task Alignment Induces Divergent RL Conclusions","url":"https://arxiv.org/pdf/2508.21188"}]

Based on the search results, here's what I found about the Wang and Heckel paper (arXiv 2603.12875):

## Paper Overview

The paper addresses how direct evaluation of LLMs on benchmarks can be misleading because comparatively strong performance may reflect task familiarity rather than capability.

## Key Contribution

The authors propose a two-stage test-time reinforcement learning (RL) alignment method where first, RL with a single sample provides a first alignment of the model to the task format, and second, test-time RL with majority-voting reward aligns the model to the benchmark distribution.

## Main Findings

Their test-time RL alignment method aligns similarly well as SFT-based train-before test, but without requiring a task-specific training set. 

More importantly, for reasoning tasks, the performance gap between fine-tuned models and their base models largely disappears after alignment, suggesting that many gains from RLVR/SFT reported in the literature are not a difference in reasoning capability, but rather artifacts of task familiarity.

The paper was submitted on March 13, 2026 and authored by Kun Wang and Reinhard Heckel.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23b0ce6c-ce87-486d-8ac9-0c48a26db8af",
  "isSidechain": false,
  "promptId": "2e94d9b7-5180-4424-b4fc-3452186c260e",
  "type": "user",
  "uuid": "80d45f10-b9a6-4612-9d07-a89479d5a81b",
  "toolUseResult": {
    "query": "Wang Heckel test-time RL alignment task familiarity artifacts benchmarks arXiv 2603.12875",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ETxXTkKc9LU3Ch3zRFwdoc",
        "content": [
          {
            "title": "[2603.12875] Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks",
            "url": "https://arxiv.org/abs/2603.12875"
          },
          {
            "title": "MCML - Research Group Reinhard Heckel",
            "url": "https://mcml.ai/research/groups/heckel/"
          },
          {
            "title": "Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks",
            "url": "https://arxiv.org/pdf/2603.12875"
          },
          {
            "title": "Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks · benchmark | Festivus",
            "url": "https://festivus.hapticlabs.ai/data/benchmarks/test-time-rl-alignment-exposes-task-familiarity-artifacts-in-llm-benchmarks"
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
            "title": "s1: Simple test-time scaling | Request PDF",
            "url": "https://www.researchgate.net/publication/397423327_s1_Simple_test-time_scaling"
          },
          {
            "title": "Mirage or Method? How Model-Task Alignment Induces Divergent RL Conclusions",
            "url": "https://arxiv.org/pdf/2508.21188"
          }
        ]
      },
      "Based on the search results, here's what I found about the Wang and Heckel paper (arXiv 2603.12875):\n\n## Paper Overview\n\nThe paper addresses how direct evaluation of LLMs on benchmarks can be misleading because comparatively strong performance may reflect task familiarity rather than capability.\n\n## Key Contribution\n\nThe authors propose a two-stage test-time reinforcement learning (RL) alignment method where first, RL with a single sample provides a first alignment of the model to the task format, and second, test-time RL with majority-voting reward aligns the model to the benchmark distribution.\n\n## Main Findings\n\nTheir test-time RL alignment method aligns similarly well as SFT-based train-before test, but without requiring a task-specific training set. \n\nMore importantly, for reasoning tasks, the performance gap between fine-tuned models and their base models largely disappears after alignment, suggesting that many gains from RLVR/SFT reported in the literature are not a difference in reasoning capability, but rather artifacts of task familiarity.\n\nThe paper was submitted on March 13, 2026 and authored by Kun Wang and Reinhard Heckel."
    ],
    "durationSeconds": 5.6513403800000015,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "23b0ce6c-ce87-486d-8ac9-0c48a26db8af",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T03:33:16.294Z_

<details><summary>↩ Tool result · `toolu_0151ejvPxGGSwwcvjjWxvvEV`</summary>

```text
Web search results for query: "BeTaL automating benchmark design ICLR 2026 dynamic difficulty"

Links: [{"title":"AUTOMATING BENCHMARK DESIGN","url":"https://openreview.net/pdf/6c3a6173bbbcaecd92e5714bac096167f405a38b.pdf"},{"title":"Automating Benchmark Design","url":"https://arxiv.org/html/2510.25039"},{"title":"[2510.25039] Automating Benchmark Design","url":"https://arxiv.org/abs/2510.25039"},{"title":"Automating Benchmark Design | OpenReview","url":"https://openreview.net/forum?id=efAANptQmt"},{"title":"Automating Benchmark Design Amanda Dsouza 1 Harit Vishwakarma 1 Zhengyang Qi 1","url":"https://arxiv.org/pdf/2510.25039"},{"title":"Published as a conference paper at ICLR 2026 FROM STATIC BENCHMARKS TO DYNAMIC","url":"https://arxiv.org/pdf/2602.23729v1"},{"title":"ICLR 2026 Schedule","url":"https://iclr.cc/virtual/2026/calendar"},{"title":"ICLR.2026 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICLR.2026"}]

Based on the search results, here's what I found about BeTaL:

BeTaL (Benchmark Tuning with an LLM-in-the-loop) is a framework that leverages environment design principles to automate the process of dynamic benchmark design. The paper is under review as a conference paper at ICLR 2026.

**Key Features:**

BeTaL works by parameterizing key design choices in base benchmark templates and uses LLMs to reason through the resulting parameter space to obtain target properties such as difficulty and realism in a cost-efficient manner.

The process is interactive and iterative: after the designer specifies an environment, a simulator creates a sample benchmark, and the model or agent being evaluated attempts this benchmark with results provided back to the designer. After each round, the designer must reason over choices and results and make changes in the parameter values so that the new parameters result in a benchmark with desired objectives. This closed-loop multi-round strategy allows the benchmark to dynamically adjust over time to meet the objectives.

**Performance Results:**

BeTaL produces benchmarks much closer to the desired difficulty, with average deviations ranging from 5.3% to 13.2%—a 2–4× improvement over baseline methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5fb9b36a-d66b-4104-9fbe-37be4c7442bd",
  "isSidechain": false,
  "promptId": "2e94d9b7-5180-4424-b4fc-3452186c260e",
  "type": "user",
  "uuid": "362a23e3-3efa-49f1-90cc-607f80139377",
  "toolUseResult": {
    "query": "BeTaL automating benchmark design ICLR 2026 dynamic difficulty",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NWNQseW9BJiHi5rw5Tn9VR",
        "content": [
          {
            "title": "AUTOMATING BENCHMARK DESIGN",
            "url": "https://openreview.net/pdf/6c3a6173bbbcaecd92e5714bac096167f405a38b.pdf"
          },
          {
            "title": "Automating Benchmark Design",
            "url": "https://arxiv.org/html/2510.25039"
          },
          {
            "title": "[2510.25039] Automating Benchmark Design",
            "url": "https://arxiv.org/abs/2510.25039"
          },
          {
            "title": "Automating Benchmark Design | OpenReview",
            "url": "https://openreview.net/forum?id=efAANptQmt"
          },
          {
            "title": "Automating Benchmark Design Amanda Dsouza 1 Harit Vishwakarma 1 Zhengyang Qi 1",
            "url": "https://arxiv.org/pdf/2510.25039"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 FROM STATIC BENCHMARKS TO DYNAMIC",
            "url": "https://arxiv.org/pdf/2602.23729v1"
          },
          {
            "title": "ICLR 2026 Schedule",
            "url": "https://iclr.cc/virtual/2026/calendar"
          },
          {
            "title": "ICLR.2026 | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/venue/ICLR.2026"
          }
        ]
      },
      "Based on the search results, here's what I found about BeTaL:\n\nBeTaL (Benchmark Tuning with an LLM-in-the-loop) is a framework that leverages environment design principles to automate the process of dynamic benchmark design. The paper is under review as a conference paper at ICLR 2026.\n\n**Key Features:**\n\nBeTaL works by parameterizing key design choices in base benchmark templates and uses LLMs to reason through the resulting parameter space to obtain target properties such as difficulty and realism in a cost-efficient manner.\n\nThe process is interactive and iterative: after the designer specifies an environment, a simulator creates a sample benchmark, and the model or agent being evaluated attempts this benchmark with results provided back to the designer. After each round, the designer must reason over choices and results and make changes in the parameter values so that the new parameters result in a benchmark with desired objectives. This closed-loop multi-round strategy allows the benchmark to dynamically adjust over time to meet the objectives.\n\n**Performance Results:**\n\nBeTaL produces benchmarks much closer to the desired difficulty, with average deviations ranging from 5.3% to 13.2%—a 2–4× improvement over baseline methods."
    ],
    "durationSeconds": 7.458585651999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5fb9b36a-d66b-4104-9fbe-37be4c7442bd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T03:33:25.054Z_

<details><summary>↩ Tool result · `toolu_016j5zahqQc3hTkuoQpFuzFC`</summary>

```text
Web search results for query: "DVD detection variance generation distribution variant contamination arXiv 2601.04895"

Links: [{"title":"[2601.04895] DVD: A Robust Method for Detecting Variant Contamination in Large Language Model Evaluation","url":"https://arxiv.org/abs/2601.04895"},{"title":"Detecting Variant Contamination in LLMs via Variance of Generation Distribution | OpenReview","url":"https://openreview.net/forum?id=Ubi631nNbI"},{"title":"DVD: A Robust Method for Detecting Variant Contamination in Large Language Model Evaluation","url":"https://arxiv.org/html/2601.04895v1"},{"title":"DVD: A Robust Method for Detecting Variant Contamination in Large","url":"https://arxiv.org/pdf/2601.04895"},{"title":"Same-Species Contamination Detection with Variant Calling Information from Next Generation Sequencing","url":"https://www.biorxiv.org/content/10.1101/531558.full.pdf"},{"title":"No Memorization, No Detection: Output Distribution-Based Contamination Detection in Small Language Models","url":"https://arxiv.org/pdf/2603.03203"}]

Based on the search results, here's what I found about arXiv paper 2601.04895:

## DVD: Detecting Variant Contamination in Large Language Model Evaluation

DVD (Detection via Variance of generation Distribution) is a single-sample detector that models the local output distribution induced by temperature sampling.

**The Problem:**
The paper addresses variant contamination, where the training corpus contains semantically equivalent yet lexically or syntactically altered versions of test items. Unlike verbatim leakage, these paraphrased or structurally transformed variants evade existing detectors based on sampling consistency or perplexity, thereby inflating benchmark scores via memorization rather than genuine reasoning.

**Key Insight:**
Contaminated items trigger alternation between a memory-adherence state and a perturbation-drift state, yielding abnormally high variance in the synthetic difficulty of low-probability tokens; uncontaminated items remain in drift with comparatively smooth variance.

**Evaluation:**
The researchers constructed the first benchmark for variant contamination across two domains: Omni-MATH and SuperGPQA by generating and filtering semantically equivalent variants, and simulated contamination via fine-tuning models of different scales and architectures (Qwen2.5 and Llama3.1). DVD consistently outperforms perplexity-based, Min-k%++, edit-distance (CDD), and embedding-similarity baselines, while exhibiting strong robustness to hyperparameters.

The paper was published on January 8, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d61fbe2-2d74-4c9d-8403-03dcb77d2ed5",
  "isSidechain": false,
  "promptId": "2e94d9b7-5180-4424-b4fc-3452186c260e",
  "type": "user",
  "uuid": "09a1f25c-f672-4414-9613-58ca121e35cc",
  "toolUseResult": {
    "query": "DVD detection variance generation distribution variant contamination arXiv 2601.04895",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EkHSNtDbyGAH2VgGq7ds2c",
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
            "url": "https://arxiv.org/html/2601.04895v1"
          },
          {
            "title": "DVD: A Robust Method for Detecting Variant Contamination in Large",
            "url": "https://arxiv.org/pdf/2601.04895"
          },
          {
            "title": "Same-Species Contamination Detection with Variant Calling Information from Next Generation Sequencing",
            "url": "https://www.biorxiv.org/content/10.1101/531558.full.pdf"
          },
          {
            "title": "No Memorization, No Detection: Output Distribution-Based Contamination Detection in Small Language Models",
            "url": "https://arxiv.org/pdf/2603.03203"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2601.04895:\n\n## DVD: Detecting Variant Contamination in Large Language Model Evaluation\n\nDVD (Detection via Variance of generation Distribution) is a single-sample detector that models the local output distribution induced by temperature sampling.\n\n**The Problem:**\nThe paper addresses variant contamination, where the training corpus contains semantically equivalent yet lexically or syntactically altered versions of test items. Unlike verbatim leakage, these paraphrased or structurally transformed variants evade existing detectors based on sampling consistency or perplexity, thereby inflating benchmark scores via memorization rather than genuine reasoning.\n\n**Key Insight:**\nContaminated items trigger alternation between a memory-adherence state and a perturbation-drift state, yielding abnormally high variance in the synthetic difficulty of low-probability tokens; uncontaminated items remain in drift with comparatively smooth variance.\n\n**Evaluation:**\nThe researchers constructed the first benchmark for variant contamination across two domains: Omni-MATH and SuperGPQA by generating and filtering semantically equivalent variants, and simulated contamination via fine-tuning models of different scales and architectures (Qwen2.5 and Llama3.1). DVD consistently outperforms perplexity-based, Min-k%++, edit-distance (CDD), and embedding-similarity baselines, while exhibiting strong robustness to hyperparameters.\n\nThe paper was published on January 8, 2026."
    ],
    "durationSeconds": 18.018321260999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0d61fbe2-2d74-4c9d-8403-03dcb77d2ed5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-20T03:33:25.060Z_

```json
{
  "parentUuid": "09a1f25c-f672-4414-9613-58ca121e35cc",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "672a3a65-bdc3-4a10-9f27-a58b012cfe0a",
  "timestamp": "2026-05-20T03:33:25.060Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Contamination-Triggered Benchmark Regeneration with Bifactor IRT Equating  ## Description We propose a self-heal…",
  "leafUuid": "672a3a65-bdc3-4a10-9f27-a58b012cfe0a",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Self-healing benchmarks with DIF-based contamination detection",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258"
}
```

---

### Assistant

_source line 35 · 2026-05-20T03:34:40.038Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the field landscape. Let me also check if there's any existing work that closes this full loop from contamination detection through regeneration with IRT equating, and check on the Cross-Context Verification (CCV) and Hardy et al. papers.

Let me also think carefully about the venue mismatch. The user says "CoRL 2026" but the proposal targets ICLR/AAAI/EACL. CoRL is Conference on Robot Learning - this proposal has nothing to do with robotics. I should note this but evaluate for ML/NLP venues since that's what the proposal actually targets.
 
The user might be using "CoRL" as shorthand or it could be a typo. Since the evaluation rubric specifies NLP/CL venues, I'll assess this against top ML/NLP conferences like ICLR, AAAI, and EACL as the proposal itself indicates.

Looking at the novelty here, applying DIF to detect contamination across model release cohorts is genuinely creative—the traditional DIF literature focuses on human test-taker groups, so repurposing it for model cohorts represents a meaningful contribution.

The full closed-loop system spanning detection, generation, equating, and graceful degradation appears unaddressed by existing work. While Growing Pains handles IRT calibration and ConStat tackles detection, no single work combines all these components. The RL-robustness argument is also logically sound—DIF examines between-group behavioral patterns rather than within-model distributions, making it structurally immune to the individual-level method failures Wang et al. documented. Applying bifactor IRT and projective IRT to LLM benchmarks is similarly novel.

The main tension is whether this is deep novelty or competent systems engineering. The pipeline integrates many known methods (ConStat, DIF, IRT, DVD) but each component is relatively straightforward application. The DIF sample size constraint is real—with only 40-80 new models annually, we're at the edge of statistical viability with 60-85% power for large effects. The "self-healing" framing also oversells what's actually a compute-intensive process requiring a 200-300 model calibration panel and human review fallbacks. A simpler alternative—just rotating benchmarks more frequently like LiveBench and using basic IRT calibration—might achieve similar results without the full detection-regeneration machinery. The practical question of who actually deploys this system looms large, and whether the marginal value of automated regeneration over manual benchmark refresh justifies the overhead remains unclear. The proposal is really a careful systems integration of existing methods rather than a fundamental breakthrough, and while the DIF application to contamination detection is genuinely novel, it's narrow in scope. For a top-tier ML venue, reviewers might dismiss this as competent engineering without sufficient research novelty, putting acceptance odds around 20-30% at ICLR—though I'm realizing the user actually asked about CoRL 2026, which is a robotics conference, so this proposal is completely misaligned with that venue.

Let me refocus on the venues the proposal actually targets and apply a more rigorous test: could a simpler approach achieve the same goals? Monthly benchmark rotation with IRT-based item calibration would handle contamination resistance and score comparability without the full automated detection and regeneration pipeline, so the proposal needs to clearly articulate what marginal value the complex pipeline adds beyond this trivial alternative.

The core tension is whether formal psychometric equivalence across benchmark versions actually matters for LLM evaluation—the community primarily cares about model rankings, and simpler methods like Growing Pains already preserve ranking order with high correlation. This engineering complexity might not be justified if the practical benefit is marginal.

I'm settling on a 25-32% assessment: the paper has genuine novelty in applying DIF to contamination detection and addresses a real problem, but the solution feels over-engineered for what the field actually needs, and the related work is thorough but the core contribution is somewhat narrow.

Actually, reconsidering—the DIF insight is genuinely clever. The observation that RL smoothing affects individual model outputs without changing between-group patterns is a structural insight worth something, especially since existing contamination detection methods fail against RL-based attacks. A method that provably works against RL would be meaningful.

The risk is that wrapping this core idea in a massive pipeline—five-signal ensemble, bifactor IRT equating, graceful degradation—dilutes what could be an elegant, focused contribution. For ICLR, I'd want to see either the DIF method shine as the centerpiece or a clearer argument for why all these components are essential rather than optional.

I'm settling on 22-32%, median 27%. The main concerns are that this reads like an integration paper where each piece is a known method applied to a new domain, simpler alternatives might get most of the value with far less complexity, DIF has power limitations at realistic sample sizes, and deployment seems impractical. Also—the user mentioned CoRL 2026, which is robotics-focused, so this proposal would be completely out of scope there. I'll evaluate this proposal against the NLP and computational linguistics venues it's actually targeting, since that's where the meaningful assessment lies.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "672a3a65-bdc3-4a10-9f27-a58b012cfe0a",
  "isSidechain": false,
  "requestId": "req_011CbD7mMCtjjE6iapaZp7LR",
  "type": "assistant",
  "uuid": "846c6023-65bb-44a9-8a52-c8a6fcdcc4ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8vLPGG7hGwZdhUmw6hTw3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1499,
      "cache_creation_input_tokens": 3964,
      "cache_read_input_tokens": 28234,
      "output_tokens": 7238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3964,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1499,
          "output_tokens": 7238,
          "cache_read_input_tokens": 28234,
          "cache_creation_input_tokens": 3964,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3964
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

_source line 36 · 2026-05-20T03:36:28.581Z_

Now I have enough information. Let me compile my assessment.

---

**⚠️ 前置说明：投稿venue严重不匹配**

Proposal 目标 venue 为 ICLR 2027 / AAAI 2027 / EACL 2027（NLP/ML 方向），但您要求评估 CoRL 2026（Conference on Robot Learning）中稿概率。本 proposal 与机器人学习**完全无关**，投稿 CoRL 会因 scope mismatch 被 desk reject（概率 ~0%）。以下评估基于 proposal 自身目标 venue（ICLR/AAAI/EACL 等 ML/NLP 顶会），如果 "CoRL" 是笔误请忽略此段。

---

```
【阶段】: Triage

【领域调研】:
- [On The Fragility of Benchmark Contamination Detection in Reasoning Models](https://arxiv.org/abs/2510.02386) (ICLR 2026): 直接前置工作。系统证明 GRPO/PPO RL 训练在 ~156 步后使 Loss/Min-K%/Max-K% 等 reference-free 检测方法 AUROC 降至 ~50%（近随机）。本 proposal 的 DIF 方案正是为回应该发现而设计。
- [Detecting Data Contamination from Reinforcement Learning Post-training (Self-Critique/RL-MIA)](https://arxiv.org/abs/2510.09259) (ICLR 2026): 提出 policy-collapse 检测，部分解决 RL 后训练下的污染检测。与本 proposal 的 DIF 方案形成竞争——Self-Critique 是 individual-model-level，DIF 是 group-level，各有优劣但 DIF 的「跨 cohort 比较」思路确实是不同的方法论路径。
- [Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration](https://arxiv.org/abs/2604.12843) (arXiv April 2026): 最直接的竞争者。使用多维 IRT + 固定参数校准 + 100 anchor items/dataset，在 400+ 模型上实现 Spearman ρ≥0.9 ranking preservation。该工作解决了「跨时间评测可比性」问题，但**不做**污染检测或 item 再生。本 proposal 声称补了这一环，逻辑成立。
- [DVD: Detecting Variant Contamination via Variance of Generation Distribution](https://arxiv.org/abs/2601.04895) (Jan 2026): 针对变体污染（paraphrase/restructured），在 SFT 模型上达 0.73-0.74 AUC，但未测 RL 模型。Proposal 将其纳入 ensemble 并计划实证测试 RL 鲁棒性，定位合理。
- [Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks](https://arxiv.org/abs/2603.12875) (Wang & Heckel, March 2026): 证明 TTRA 可消除约 27pp 的 fine-tuning 表观优势，暗示部分「污染信号」实为 task familiarity。Proposal 利用此发现论证 DIF 可区分 uniform（familiarity）vs. item-specific（contamination）效应。
- [BeTaL: Automating Benchmark Design](https://arxiv.org/abs/2510.25039) (ICLR 2026): LLM-in-the-loop 动态 benchmark 设计，但聚焦调难度，不做等值（equating）。
- [Lost in Benchmarks? Rethinking LLM Benchmarking with IRT (PSN-IRT)](https://arxiv.org/abs/2505.15055) (AAAI 2026 Oral): 用 4PL IRT 分析 benchmark 质量，不做 item 再生。
- [ATLAS: Adaptive Testing for LLM Evaluation](https://arxiv.org/abs/2511.04689) (2025): IRT-based adaptive testing 减少评测 cost，不处理污染。
- [BenchBench](https://arxiv.org/abs/) (March 2026): 自动 benchmark 生成的 meta-evaluation，不做 IRT 等值。
- [Cross-Context Verification (CCV)](https://arxiv.org/abs/2603.21454) (March 2026): 通过跨 session solution diversity 检测污染，Mann-Whitney U=0，但仅在 9 个 SWE-bench 问题上验证，且依赖 temperature-0 determinism。
- 调研总结：该领域目前呈「模块化」格局——污染检测（Wang et al., ConStat, DVD, CCV）、IRT 校准（Growing Pains, PSN-IRT, ATLAS）、benchmark 生成（BeTaL, BenchBench）各自独立发展。**没有已发表工作将检测→再生→等值完整串联**，这一 gap 是真实的。但 Growing Pains 已大幅降低了「跨时间可比性」问题的急迫性，使 proposal 的核心 value proposition 需要更精准定位。

【Trivial Alternative 检验】:
存在一个成本显著更低的替代方案：**LiveBench 式定期刷新 + Growing Pains 式 IRT 锚定**。
- LiveBench 每月从新鲜来源更新 benchmark items → 天然抗污染
- Growing Pains 已证明用 100 anchor items + 固定参数校准即可在 400+ 模型上实现 ρ≥0.9 ranking preservation → 跨时间可比性已有 lightweight 方案
- 当污染被怀疑时，手动替换可疑 items 并用 Growing Pains 重新校准

本 proposal 相对于该 trivial alternative 的**增量价值**在于：
1. **自动化检测**（不依赖人工识别污染）—— 但 ConStat 已部分解决了这个问题
2. **形式化等值保证**（bifactor IRT 比 Growing Pains 的 MIRT 更严格）—— 但审稿人会问：对于 LLM 排名这一主要使用场景，Growing Pains 的 ρ≥0.9 是否已经够用？更高的形式严格性带来的实际收益是什么？
3. **RL-robust 检测**（DIF）—— 这是真正的增量价值所在，但可以作为独立贡献发表，不需要整个 pipeline

**结论**：Trivial alternative 威胁是实质性的。Pipeline 的核心增量价值集中在 DIF 这一个点上，但 DIF 被包裹在一个 4-stage pipeline 里，增量价值被稀释而工程成本被放大。

【前提假设检验】:
核心 claim 的逻辑链中，以下环节是未经验证的假设：

1. **「DIF 检测 behavioral pattern 而非 NLL，因此 RL-robust」**—— 这是 proposal 最核心的论证。逻辑推理 *表面上* 合理（RL 平滑 NLL 分布但不改变答对/答错的 binary outcome），但存在一个未检验的假设：**contamination 必然表现为 item-specific accuracy boost（DIF signal），而非 uniform ability improvement**。如果模型通过 RL 训练在 benchmark 上「学会了做这类题」而非「记住了这些题」，DIF 将检测不到——而这恰恰是 Wang & Heckel 所说的 task familiarity artifact 场景。Proposal 自己也承认了这一 confound，但将其视为 edge case 而非核心威胁。这是一个经验性问题，proposal 的 analytical demonstration 无法解决。

2. **「200-300 LLM 构成的 calibration panel 能提供足够的 IRT 校准精度」**—— IRT 校准传统上要求 examinees 之间有真实的 ability 分布变异。LLMs 不是人类考生：它们之间的 ability 分布可能高度非正态、存在 ceiling/floor 效应（很多模型在容易题上 100% 正确率），且模型之间不具备 IRT 假设的 local independence（同一 family 的模型高度相关）。用 LLMs 做「考生」来校准 IRT 参数是否 psychometrically valid，是一个开放问题。Growing Pains 通过 400+ 模型的大规模实验初步验证了可行性，但 proposal 的 bifactor 模型比 Growing Pains 的 MIRT 更复杂，需要更多考生，而 200-300 是否够用是未验证假设。

3. **「DIF 在 N=40-80/group 下有足够 power 检测实际规模的污染效应」**—— Proposal 给出的 power analysis 引用了 PMC5978487，但那是人类考生（连续 ability 分布、大 N）的模拟。LLM cohort 的 ability 分布可能与人类截然不同（discrete、multi-modal），power 估计能否迁移是假设。Proposal 自己也承认 DIF 对 δ<0.6 underpowered，但将此定位为 acceptable tradeoff —— 审稿人可能不同意。

4. **「生成的替代 items 能通过 student simulation 预筛选达到 r=0.75-0.82」**—— 该数据来自 arXiv 2601.09953，但那是在限定领域（数学）上的结果。是否可推广到 MMLU 的 57 个学科、LiveBench 的多种任务类型，是未验证假设。

【3 维度打分】:
  1. Novelty: 中 — 
     核心 novelty 有两层：(a) DIF 用于 LLM 污染检测（genuinely novel，无近期工作做过）；(b) 检测→生成→等值的 full-loop 集成（integration novelty）。但存在以下削弱：
     - 每个单独模块都是已有方法在新领域的应用（DIF 是教育测量的标准方法；ConStat 已有 FDR 控制；DVD 已有；bifactor IRT/PIRT 已有），integration 本身的 novelty 深度有限
     - Self-Critique (Tao et al., ICLR 2026) 已提出了针对 RL post-training 的污染检测方法，虽然方法论不同（individual-model vs. group-level），但 narrative 上分走了部分 novelty credit
     - Growing Pains (April 2026) 已大幅推进了 IRT 在 LLM 评测中的应用，削弱了 bifactor IRT 等值部分的新鲜感
     如果 proposal 聚焦 DIF 作为 RL-robust 检测信号这一核心贡献并做深，novelty 可升至「强」；但当前 4-contribution 结构导致每个贡献都停留在 application-level depth。

  2. Significance: 中 — 
     Benchmark 污染是公认的重要问题（DeepSeek V3.2 在 2026 年面临公开质疑），研究方向正确。但 significance 被以下因素限制：
     - 实际部署路径不清晰：谁会运行一个需要 200-300 LLM calibration panel、900-1300 GPU-hours、5-6 个月开发的 benchmark 维护系统？LiveBench 的轻量级月更新方案在实践中已被社区采纳
     - Growing Pains 已提供了一个相对轻量的跨时间可比性方案（ρ≥0.9），降低了 formal equating 的边际价值
     - 如果核心发现是 positive（pipeline works, DIF detects RL contamination），审稿人的反应更可能是 "nice engineering, makes sense" 而非 "surprising, changes how I think about the problem"
     - 真正 significant 的子贡献是 DIF 的 RL-robustness 论证，但它被淹没在 pipeline 的工程复杂性中

  3. Related Work: 强 — 
     Related work 覆盖极为全面：覆盖了检测（ConStat, Wang et al., Self-Critique, DVD, CCV, watermarking）、IRT（Growing Pains, PSN-IRT, ATLAS）、生成（BeTaL, BenchBench, ReQUESTA, arXiv 2602.06631）、等值（Kolen & Brennan, Kim 2022, PIRT）等多个维度。与 Growing Pains 的差异化定位清晰（「他们做 cross-time evaluation，我们做 contamination detection + remediation」）。对 DIF 在小样本下的 limitations 有诚实 acknowledgment。唯一微小不足：对 Self-Critique 的对比可以更深入（它也声称 RL-robust，DIF 相比它的系统性优势在哪里？）。

【概率估计】: [20% - 32%] 中位 25%
（注：以 ICLR 2027 为目标 venue；若投 CoRL 2026 则为 0-2%，因完全 out of scope）

【估计理由】: 
Novelty 和 Significance 均为「中」，这将概率锁定在 25-35% 区间。但 Trivial Alternative 威胁实质性地压低了上界：Growing Pains + LiveBench 的组合以 1/10 的成本解决了 80% 的问题，使得 full pipeline 的增量价值需要非常强的 DIF 实证结果来证明。此外，这是一个 integration/systems paper，ICLR 对此类论文历来要求 "the whole is greater than the sum of parts" —— 目前各模块的深度均停留在 application level，可能被质疑 intellectual contribution 不足。Novelty 维度（尤其是 DIF 的 application-level depth 和 Self-Critique 的竞争）是限制上界的主要因素。Related Work 的强势覆盖提供了一定下限保护（至少不会因 missing references 被拒），但不足以补偿 idea 内核的 incremental 性质。

【主要风险】:
1. **Trivial Alternative 致命威胁**: 审稿人可能直接问 "Why not just use LiveBench-style rotation + Growing Pains calibration?"，如果 proposal 不能令人信服地论证 full pipeline 相对于该简单组合的增量价值远超其工程成本，likely 成为 reject 理由。这一风险在 Growing Pains (April 2026) 发表后显著加剧。
2. **Integration depth 不足**: 4 个贡献中每个单独来看都是 known method → new domain application，ICLR 审稿人可能判定 "well-executed engineering, but limited intellectual novelty" —— 这对 systems/pipeline paper 是常见的 reject 理由。核心 novel insight（DIF 的 RL-robustness）被 pipeline 的复杂性淹没，无法获得应有的 novelty credit。
```

Sources:
- [On The Fragility of Benchmark Contamination Detection in Reasoning Models](https://arxiv.org/abs/2510.02386)
- [Detecting Data Contamination from Reinforcement Learning Post-training (Self-Critique)](https://arxiv.org/abs/2510.09259)
- [Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration](https://arxiv.org/abs/2604.12843)
- [DVD: Detecting Variant Contamination via Variance of Generation Distribution](https://arxiv.org/abs/2601.04895)
- [Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks](https://arxiv.org/abs/2603.12875)
- [BeTaL: Automating Benchmark Design](https://arxiv.org/abs/2510.25039)
- [Lost in Benchmarks? PSN-IRT](https://arxiv.org/abs/2505.15055)
- [ATLAS: Adaptive Testing for LLM Evaluation](https://arxiv.org/abs/2511.04689)
- [Cross-Context Verification (CCV)](https://arxiv.org/abs/2603.21454)
- [BenchBench: Benchmarking Automated Benchmark Generation](https://arxiv.org/html/2604.12843)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "846c6023-65bb-44a9-8a52-c8a6fcdcc4ab",
  "isSidechain": false,
  "requestId": "req_011CbD7mMCtjjE6iapaZp7LR",
  "type": "assistant",
  "uuid": "e6ab3b4e-b25f-4258-a5e5-73694107e2a7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8vLPGG7hGwZdhUmw6hTw3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1499,
      "cache_creation_input_tokens": 3964,
      "cache_read_input_tokens": 28234,
      "output_tokens": 7238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3964,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1499,
          "output_tokens": 7238,
          "cache_read_input_tokens": 28234,
          "cache_creation_input_tokens": 3964,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3964
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

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Contamination-Triggered Benchmark Regeneration with Bifactor IRT Equating  ## Description We propose a self-heal…",
  "leafUuid": "e6ab3b4e-b25f-4258-a5e5-73694107e2a7",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Self-healing benchmarks with DIF-based contamination detection",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Contamination-Triggered Benchmark Regeneration with Bifactor IRT Equating  ## Description We propose a self-heal…",
  "leafUuid": "e6ab3b4e-b25f-4258-a5e5-73694107e2a7",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Self-healing benchmarks with DIF-based contamination detection",
  "sessionId": "13ac10a1-0849-4d3d-8381-876f1204b258"
}
```

---
