# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Contamination-Triggered Benchmark

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-1/7de8aab4-8c5e-461b-b9ea-b233d22ef3d0.jsonl`
- **Structured JSON:** [`cdea2c11ce35bc2b08d8.json`](../../sessions/cd/cdea2c11ce35bc2b08d8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:32:35.966Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:32:35.966Z",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Contamination-Triggered Benchmark Regeneration with Bifactor IRT Equating\n\n## Description\nWe propose a self-healing benchmark framework that closes the full loop from multi-signal contamination detection through construct-constrained generation to bifactor IRT-equated replacement, with formal graceful-degradation guarantees. The system makes four integrated contributions: (1) A multi-signal contamination sentinel with explicit RL-robustness guarantees, now supported by an analytical demonstration. The ensemble combines five signals: ConStat-style perturbation testing, a novel Differential Item Functioning (DIF) analysis across model release cohorts, IRT aberrance detection, DVD-style generation-variance testing (adapted from Liang et al., arXiv 2601.04895), and membership-inference probes — with formal FDR control. The DIF-based cohort analysis is both novel and analytically RL-robust: we demonstrate via a concrete scenario (200 items, N=80/cohort, 20 contaminated items with P(correct) boosted from 0.50 to 0.80) that logistic regression DIF detects contamination as large uniform DIF (ETS Category C, |Δ_MH|≈3.3) because it examines between-group item-level performance conditional on ability, not within-model output distributions that RL smoothing affects. Quantitative power analysis grounded in PMC5978487 simulations establishes that at N=80/group with contamination-typical effect sizes (δ≈0.8-1.4 logits, consistent with GSM1K's 10-13% accuracy drops), DIF power reaches 60-85%, further enhanced by cumulative Bayesian priors (Sinharay et al., 2006), Item-Focused Trees (Tutz & Berger, 2016), and the 2-of-5 ensemble voting threshold. We acknowledge DIF is underpowered for small effects (14.4% at δ=0.4, N=50/group) — its value is detecting the large effects that threaten benchmark validity, complemented by other signals for subtler contamination. We further address the interaction with task familiarity artifacts (Wang & Heckel, arXiv 2603.12875): task familiarity produces uniform improvements (no DIF signal) while contamination produces item-specific advantages (DIF signal), making DIF a principled discriminator between the two. DVD is labeled as promising but untested against RL-trained models; our RL-contamination experimental condition will resolve this empirical gap. (2) A construct-constrained generation pipeline that abandons direct IRT-parameter conditioning (shown to achieve only rho=0.10-0.45 by arXiv 2602.06631) in favor of construct/taxonomy-based generation, student-simulation pre-screening (r=0.75-0.82), optional pre-filtering via signed isotonic R² scalability coefficients (Hardy et al., arXiv 2603.24999) for fast nonparametric quality control, multi-agent iterative refinement, and empirical calibration on a panel of 200-300 diverse LLMs via Bayesian fixed-parameter calibration (OH2PL, König et al., 2020, achieving unbiased estimates at N≥50). (3) A bifactor IRT equating gate using Projective IRT (PIRT) to handle the multi-construct nature of benchmarks like MMLU — fitting a general ability factor plus domain-specific factors, then projecting to unidimensional equivalents for standard equating (Kim, 2022). Only items whose projected parameters fall within 95% CIs of originals and preserve test information, construct coverage, and model rankings (rho >= 0.95) are accepted. (4) A formal graceful-degradation framework defining validity boundaries grounded in the test equating literature: minimum 20% anchor set for standard equating (Kolen & Brennan, 2004), degraded-but-valid operation via robust LAV equating at 15-20%, halt-and-review below 15%, minimum marginal reliability ≥ 0.80 for benchmark release, and transparent partial-release protocols when full regeneration fails for >15% of items. This uniquely differentiates from Growing Pains (cross-time evaluation without contamination detection or regeneration), from CCV (solution-diversity detection for coding tasks without remediation or psychometric equating), from watermarking approaches (Sander et al., arXiv 2502.17259; proactive prevention requiring pre-release embedding, complementary to our post-hoc detection and remediation), from Wang et al./Self-Critique (identifying the RL-fragility problem without providing a robust detection alternative), from DVD (detecting variant contamination without remediation and untested on RL models), from RIDE/BeTaL (altering difficulty rather than preserving it), and from ConStat (detecting but not remediating contamination). We validate on LiveBench subsets and MMLU-CF under simulated contamination at 10-50% rates — including an RL-contamination condition using GRPO fine-tuning following Wang et al.'s protocol to empirically test DIF robustness and DVD behavior under RL — with naturally-contaminated MMLU/GSM8K as positive controls, and include a pilot feasibility study reporting the first empirical convergence statistics for IRT-equated benchmark item generation.\n\n## Core Problem\nHow can we build self-healing benchmarks that automatically detect contaminated items via multi-signal triangulation — including a novel DIF-based cohort analysis robust to RL-trained reasoning models — and regenerate psychometrically equivalent replacements through empirically calibrated generation with bifactor IRT equating, while maintaining benchmark validity through formal graceful-degradation guarantees?\n\n## Opportunity\nDynamic benchmarks face a fundamental tension: increased contamination resistance via strong rewriting degrades question fidelity and may alter intended difficulty. LiveBench updates monthly but without psychometric calibration; VarBench perturbs inputs but difficulty shifts unpredictably; BenchBench evaluates generation quality but without equating. Educational testing has solved the analogous problem of maintaining test comparability across administrations using IRT equating with anchor items — a mature methodology with decades of validation. However, directly applying this to LLM benchmarks requires solving four underappreciated sub-problems: (1) distinguishing contamination from genuine capability gains — this is especially critical for RL-trained reasoning models (o1, o3, DeepSeek-R1), where Wang et al. (ICLR 2026) demonstrate that GRPO/PPO training conceals contamination signals that reference-free detection methods rely on, with AUROC degradation of 14-20 percentage points (Loss: 14.22pp, Min-K%: 16.42pp, Max-K%: 19.84pp after only ~156 GRPO steps), reducing most to near-random (~50%) AUROC; furthermore, Wang & Heckel (arXiv 2603.12875) show that test-time RL alignment can close fine-tuning performance gaps by ~27 percentage points on average, suggesting some apparent contamination signals may reflect task familiarity artifacts rather than memorization, making item-specific detection even more critical; (2) detecting variant contamination (paraphrased/restructured benchmark items in training data) which evades standard detectors — DVD (arXiv 2601.04895) shows conventional methods achieve only 0.43-0.68 AUC on variant contamination; (3) generating replacement items with controlled psychometric properties (LLMs systematically underestimate difficulty with correlations of only rho=0.10-0.45, per arXiv 2602.06631, necessitating empirical calibration rather than prompt-based difficulty targeting); and (4) equating across multi-construct benchmarks (requiring bifactor or multidimensional IRT rather than naive unidimensional models). No existing work addresses all four sub-problems in an integrated pipeline with formal graceful-degradation guarantees.\n\n## Landscape\nLiveBench (ICLR 2025) updates monthly from recent sources but applies objective scoring without difficulty calibration. LiveCodeBench (ICLR 2025) uses time-segmented evaluation but doesn't ensure psychometric equivalence across segments. BeTaL (ICLR 2026) performs dynamic benchmark design with LLM-in-the-loop but focuses on increasing difficulty, not preserving it. BenchBench (March 2026) evaluates automated benchmark generation using discrimination and validity metrics but without IRT equating. ArenaBencher progressively generates harder items but provides no formal difficulty-equivalence guarantees. CRITICAL CONCURRENT WORK: 'Growing Pains' (arXiv April 2026) uses multidimensional IRT with fixed-parameter calibration and 100 anchor items per dataset to make LLM evaluation extensible across time — achieving Spearman rho >= 0.9 for ranking preservation using 400+ models. However, it addresses efficient evaluation (comparing scores across time), NOT contamination detection or item regeneration. PSN-IRT (AAAI 2026 Oral) analyzes benchmark quality via 4PL IRT but does not regenerate items. RIDE (ICLR 2026) uses IRT-guided perturbation for difficulty evolution in math but does not perform equating. ATLAS (arXiv 2025) applies adaptive testing with IRT to reduce evaluation cost but does not handle contamination. Cross-Context Verification (CCV; arXiv 2603.21454, March 2026) achieves perfect separation between contaminated and genuine reasoning (Mann-Whitney U=0, r=1.0) on SWE-bench Verified by measuring solution diversity across independent sessions — a powerful black-box method, but currently validated only on coding tasks (9 SWE-bench problems, 45 trials) and relying on temperature-0 determinism that may not generalize to knowledge/reasoning benchmarks with inherent answer variability. Hardy et al. (arXiv 2603.24999, March 2026) introduce nonparametric signed isotonic R² scalability coefficients that outperform IRT-based item diagnostics for detecting bad benchmark items on HS Math, GSM8K, and MMLU — lightweight (bivariate monotone fits in seconds) and robust under small-n/large-p conditions; this complements our IRT-based quality control by providing a fast model-agnostic pre-filter for item quality before parametric calibration. On proactive contamination prevention: Sander et al. (arXiv 2502.17259, Feb 2025) propose watermarking benchmarks before release, reformulating questions with a watermarked LLM and detecting 'radioactivity' traces via statistical tests; validated on ARC and MMLU with 1B models, this represents a fundamentally different paradigm (prevention at release time vs. post-hoc detection and remediation). Our approach is complementary: watermarking prevents future contamination, while our pipeline detects and remediates existing contamination in already-deployed benchmarks — the two could be combined in a defense-in-depth strategy. On contamination detection: ConStat (2024) provides performance-based detection with formal FDR control; shortcut neuron analysis (ACL 2025) can isolate contamination to ~1.1-1.4% of neurons with only ~3% false positive impact; 'Test of Time' (arXiv 2025) demonstrates temporal signals are unreliable as standalone contamination indicators. CRITICALLY, 'On The Fragility of Benchmark Contamination Detection in Reasoning Models' (Wang et al., arXiv 2510.02386, ICLR 2026) systematically demonstrates that GRPO/PPO-style RL training conceals contamination signals: reference-free methods show AUROC degradation of 14-20 percentage points after only ~156 GRPO steps (Loss: 14.22pp drop from 75.48% to 61.26%; Min-K%: 16.42pp drop from 74.96% to 58.54%; Max-K%: 19.84pp drop from 69.83% to 49.99% — essentially random), while perturbation-based methods show different degradation patterns. The concealment mechanism is PPO's clipping objective, which contracts the NLL gap between contaminated and clean items. Self-Critique (Tao et al., arXiv 2510.09259, ICLR 2026) partially addresses this via policy-collapse detection but remains an individual-model-level method. DVD (Liang et al., arXiv 2601.04895, Jan 2026) introduces detection via variance of generation distribution and is specifically designed for variant contamination, achieving 0.73-0.74 AUC where Min-K%++ achieves only 0.43-0.68; however, DVD was validated only on SFT-contaminated models and its behavior under RL training is untested. On task familiarity vs. contamination: Wang & Heckel (arXiv 2603.12875, March 2026) show that test-time RL alignment (TTRA) closes the performance gap between base and fine-tuned models by ~27 percentage points on average, suggesting many reported fine-tuning gains are task familiarity artifacts rather than genuine capability improvements; this has a dual implication — it strengthens the need for item-specific contamination detection (since task familiarity produces uniform improvements with no DIF signal, while contamination produces item-specific advantages that DIF detects), but also suggests that contamination-driven DIF effects may be partially confounded with format-familiarity effects that TTRA could remove. On item generation: arXiv 2602.06631 shows LLMs achieve only rho=0.10-0.45 for difficulty estimation, but student simulation approaches (arXiv 2601.09953) achieve r=0.75-0.82 and multi-agent frameworks like ReQUESTA improve discrimination from 0.17 to 0.39. On IRT methodology: bifactor models with Projective IRT (PIRT) enable equating of multidimensional tests while remaining tractable; fixed-parameter calibration requires only N>=200 examinees vs N>=500 for full calibration (Kim & Kolen, 2019); the OH2PL (König, Spoden, & Frey, 2020) achieves unbiased estimates at N>=50 using optimized Bayesian hierarchical priors. No existing work closes the full loop from multi-signal contamination detection (robust to RL-trained models) through construct-constrained generation to bifactor IRT-equated regeneration with graceful-degradation guarantees.\n\n## Approach\nBuild a closed-loop pipeline with three stages plus a formal graceful-degradation framework, each substantially revised to address known limitations:\n\n**Stage 1: Multi-Signal Contamination Sentinel (with RL-Robustness Guarantees).** Deploy an ensemble of five complementary detection signals, explicitly designed so that at least two signals remain informative even against RL-trained reasoning models:\n\n(a) *ConStat-style perturbation testing* — compare model performance on original items vs. semantically-equivalent reformulations, with formal False Discovery Rate (FDR) control. NOTE: Wang et al. (ICLR 2026) show reference-free detectors degrade 14-20pp under RL training (Loss: 14.22pp, Min-K%: 16.42pp, Max-K%: 19.84pp after ~156 GRPO steps); we retain perturbation testing as effective against non-RL models (which still constitute the majority of the model ecosystem) but do not rely on it alone.\n\n(b) *Differential Item Functioning (DIF) across model release cohorts* — a novel application treating model release date as a grouping variable and flagging items that become differentially easier for newer cohorts beyond what general ability gains predict. **This is our primary RL-robust signal.** The key argument: DIF operates on group-level statistical patterns (comparing Item Characteristic Curves across model cohorts matched on overall ability), not individual output distributions. Wang et al. prove that PPO/GRPO clipping contracts the NLL gap *within a single model* between seen and unseen items — but DIF does not examine within-model NLL gaps. It detects whether the structural relationship between ability and item response differs across groups. A contaminated cohort shows anomalous ICCs on specific items regardless of how smooth individual output distributions appear, because contamination must, by definition, create differential item advantage — the one signal RL cannot conceal without negating the purpose of contamination. Furthermore, DIF leverages IRT's invariance principle: item parameters should be group-invariant after controlling for ability, and systematic DIF violations on specific items constitute contamination evidence that is orthogonal to all 10 methods shown to fail.\n\n**Analytical Demonstration of DIF RL-Robustness.** Consider a concrete scenario: 200 binary items evaluated by two annual model cohorts (pre-2026, post-2026) with N=80 models each. Suppose 20 items are contaminated in the newer cohort, boosting P(correct) from 0.50 to 0.80 on those items (δ≈1.4 logits — a conservative estimate given GSM1K's documented 13% average accuracy drop across models, which implies item-level boosts of 20-40% on memorized items for heavily contaminated models). RL smoothing via GRPO/PPO contracts the NLL gap between contaminated and clean items within each individual model's output distribution — this is the mechanism Wang et al. demonstrate. However, the 30-percentage-point accuracy advantage on contaminated items persists at the behavioral level: RL training does not cause models to answer memorized items incorrectly, because doing so would negate the purpose of contamination. Logistic regression DIF with sum-score matching compares the probability of correctly answering each item across the two cohorts, conditioning on total score (overall ability). On the 180 uncontaminated items, both cohorts show similar ICCs after controlling for ability. On the 20 contaminated items, the newer cohort shows systematically higher probability of correct response at every matched ability level — large uniform DIF (ETS Category C: |Δ_MH| = -2.35 × ln(odds ratio) = -2.35 × ln(4.0) ≈ 3.3 delta units, far exceeding the C threshold of 1.5). This differential pattern is detectable because DIF examines between-group item-level performance conditional on ability, not within-model output distributions. RL smoothing is irrelevant to DIF: it modifies how confidently a model generates its answer (the NLL surface), not whether it gets the answer right or wrong (the binary response pattern that DIF analyzes).\n\n**Quantitative DIF Power Analysis.** Independent simulation evidence (PMC5978487) establishes that logistic regression DIF at N=50/group achieves 14.4% power for small effects (δ=0.4) and 31.0% for medium effects (δ=0.6); at N=100/group, these rise to 24.7% and 55.2% respectively. These figures appear concerning for small-sample detection, but benchmark contamination typically produces large effects: GSM1K documents 10-13% average accuracy drops from contamination across models, corresponding to item-level δ≈0.8-1.4 logits on memorized items. DIF power scales super-linearly with effect size; at δ=1.4 with N=80/group (annual cohorts), power is estimated at 60-85% based on extrapolation from PMC5978487 simulation curves, consistent with the general finding that the likelihood ratio test achieves the highest statistical power in most DIF configurations. Furthermore, three factors substantially improve effective power beyond these baseline estimates: (i) cumulative Bayesian priors (Sinharay et al., 2006) accumulate evidence across successive benchmark administrations, borrowing strength from previous DIF estimates to improve detection over time — particularly effective for persistent contamination that affects multiple administrations; (ii) Item-Focused Trees (Tutz & Berger, 2016) avoid arbitrary categorical group splits by treating release date as a continuous covariate, leveraging the full model sample (N=160 rather than two groups of 80) and letting the method identify natural breakpoints where DIF emerges; (iii) the 2-of-5 ensemble voting threshold means even 40-50% individual DIF power yields acceptable ensemble sensitivity when combined with DVD and ConStat signals on non-RL models. We acknowledge that DIF alone is underpowered for small contamination effects (δ<0.6); its value lies in detecting the large effects that matter most for benchmark validity, complemented by other ensemble signals for smaller effects.\n\n**Interaction with Task Familiarity Artifacts.** Wang & Heckel (arXiv 2603.12875, March 2026) demonstrate that test-time RL alignment (TTRA) closes the performance gap between base and fine-tuned models by ~27 percentage points on average, suggesting many reported fine-tuning gains reflect task familiarity rather than genuine capability. This has a dual implication for DIF-based detection. First, it *strengthens* the DIF rationale: task familiarity artifacts produce uniform improvements across all items (no DIF signal), while memorization-based contamination produces item-specific advantages (DIF signal) — DIF thus provides a principled way to distinguish the two, a distinction no other detection method explicitly makes. Second, it introduces a nuance: if some contamination manifests partially as enhanced task-format familiarity rather than item-specific memorization, the item-level DIF effect sizes may be modestly smaller than the raw accuracy gaps suggest. We address this by: (a) noting that DIF would be computed on models as deployed (without TTRA), since TTRA is an analysis tool, not a standard deployment procedure; (b) observing that DIF controls for overall ability via sum-score matching, so any uniform familiarity-driven improvements are absorbed into the ability estimate, leaving item-specific contamination signals intact; (c) reporting DIF effect sizes with uncertainty intervals rather than relying on significance thresholds alone, making the analysis transparent about power limitations.\n\n**DIF Small-Sample Strategy (detailed).** Classical DIF methods (Mantel-Haenszel, logistic regression) require N≥200 per group for optimal performance (Mazor et al., 1992; Scott et al., 2009), far exceeding our ~10-20 models per quarterly cohort. We address this through a four-pronged strategy: (i) *Temporal aggregation*: use semi-annual or annual cohorts rather than quarterly, yielding N=40-80 per group; as the model ecosystem grows (~100+ new models per year as of 2026), annual cohorts will approach the N≥100 threshold where regularized methods become viable. (ii) *Cumulative Bayesian DIF*: following Sinharay et al. (2006, ETS), use DIF estimates from previous benchmark administrations as informative priors for new cohorts, accumulating statistical power over time rather than analyzing each cohort in isolation. (iii) *Item-Focused Trees* (Tutz & Berger, 2016): treat release date as a continuous covariate rather than creating arbitrary categorical cohorts, letting the method identify natural breakpoints where DIF emerges — this avoids the small-group problem entirely while leveraging the full model sample. (iv) *Parsimonious models*: following Belzak (2020, Multivariate Behavioral Research), use logistic regression with sum scores rather than complex IRT models for DIF detection, as simpler models outperform complex ones in small samples even when misspecified. We report DIF effect sizes (ETS delta classification: A/B/C, where C indicates |Δ_MH|≥1.5) with uncertainty intervals rather than relying solely on significance tests, acknowledging power limitations transparently.\n\n(c) *IRT aberrance detection* — flag items whose observed easiness significantly exceeds calibrated difficulty, used as one signal among several rather than a standalone detector.\n\n(d) *DVD-style generation variance testing* (adapted from Liang et al., arXiv 2601.04895) — for models with inference access, generate 50 responses per item via temperature sampling and compute the variance of synthetic-difficulty scores. Contaminated items exhibit bimodal generation distributions (alternating between memorized templates and free generation) yielding high variance, while clean items show unimodal low-variance distributions. This specifically detects variant contamination (paraphrased/restructured benchmark items) where ConStat and Min-K% fail (AUC 0.43-0.68 vs. DVD's 0.73-0.74). NOTE: DVD is promising but untested against RL-trained models — it was validated only on SFT-contaminated models (Qwen2.5, Llama3.1 fine-tuned). Whether the bimodal variance signature persists after GRPO/PPO training is an open empirical question that our RL-contamination experimental condition will directly test. DVD's value in the ensemble is therefore primarily for detecting variant contamination in the non-RL model majority, with DIF providing the RL-robust complement.\n\n(e) *Membership-inference probes* (Min-K% Prob / ReCaLL) where white-box access is available — retained as a cheap first-pass filter effective against non-RL models, but explicitly acknowledged as fragile against GRPO/PPO-trained models per Wang et al. (AUROC drops to ~50% after ~156 GRPO steps).\n\nTrigger regeneration when an item is flagged by >= 2 independent signals, with FDR-controlled thresholds. The ensemble is explicitly designed so that DIF (group-level, analytically RL-robust as demonstrated above) and DVD (generation-variance, variant-robust on SFT models) provide coverage where individual-level methods fail. Genuine capability gains will produce uniform improvement across original and perturbed items (no ConStat signal), across cohorts controlling for ability (no DIF signal), and across temperature samples (no DVD signal), while contamination produces item-specific anomalies in at least two of these dimensions.\n\n**Stage 2: Construct-Constrained Generation with Empirical Calibration.** Critically, we abandon the original approach of conditioning generators on raw IRT parameters — research shows LLMs achieve only rho=0.10-0.45 correlation with actual difficulty (arXiv 2602.06631). Instead: (a) For each flagged item, prompt a frontier generator (DeepSeek-V4-Pro or Qwen-3.5-397B) conditioned on the item's construct tag, cognitive complexity level (Bloom's taxonomy), format template, and 3-5 exemplar items from the same difficulty band — but NOT explicit IRT parameters; (b) Generate 8-10 candidates per flagged item using a multi-agent framework (generator + evaluator + refiner) inspired by ReQUESTA, with iterative critique loops; (c) Pre-screen candidates using student simulation — have a diverse panel of weaker/mid-tier LLMs (4B-14B parameters) role-play as examinees at varying ability levels, estimating approximate difficulty via simulated IRT (achieving r=0.75-0.82 per arXiv 2601.09953), and discard candidates whose estimated difficulty deviates by >1.5 logits from the target; (d) Optionally pre-filter candidates using Hardy et al.'s signed isotonic R² scalability coefficients (arXiv 2603.24999) as a fast, nonparametric quality check — items with anomalously low scalability coefficients (indicating poor construct alignment) are discarded before expensive panel calibration; (e) Empirically calibrate surviving candidates on the full calibration panel of 200-300 diverse LLMs via Bayesian fixed-parameter calibration (OH2PL, König, Spoden, & Frey, 2020), anchored to a preserved clean set (>= 20% of items, following the Kolen & Brennan 20% rule for stable equating). This generate-screen-calibrate pipeline is expected to achieve 30-50% rejection rates based on analogous AIG literature; we report convergence statistics as a key empirical contribution.\n\n**Stage 3: Bifactor IRT Equating Gate.** Move from naive unidimensional 2PL to a bifactor model (general LLM ability + domain-specific factors), which captures the inherently multi-construct nature of benchmarks like MMLU while remaining tractable for equating. Use Projective IRT (PIRT) to project bifactor parameters onto unidimensional equivalents compatible with standard equating software (demonstrated to produce very similar equating outcomes to full numerical integration, with practical advantages for implementation; Kim, 2022). Accept only replacements whose projected difficulty and discrimination fall within the 95% CI of the original item's parameters. Verify that the regenerated benchmark's test information function, construct coverage vector, and model ranking (Spearman rho >= 0.95) match the pre-contamination gold standard. Reject and re-generate otherwise, with a maximum of 3 regeneration cycles per item before flagging for human review.\n\n**Graceful Degradation Framework.** We define formal validity boundaries and fallback strategies for each failure mode, grounded in the test equating literature (Kolen & Brennan, 2004; Angoff, 1984):\n\n(i) *Anchor set integrity*: Maintain a minimum of 20% clean (uncontaminated) anchor items. If contamination detection flags items bringing the clean set below 20%, enter a degraded-but-valid operating mode: switch from standard Stocking-Lord equating to robust Area-Weighted or Least Absolute Values (LAV) equating methods (which tolerate outlying anchor items) and widen acceptance CIs to 99%. If the clean set drops below 15%, halt automated regeneration and flag the entire benchmark version for human review and potential full re-calibration. Below 10%, do not release.\n\n(ii) *Stage 1 error propagation*: False positives (flagging clean items as contaminated) trigger unnecessary regeneration but do not compromise validity — the equating gate (Stage 3) ensures replacements are psychometrically equivalent regardless of whether the original was truly contaminated. False negatives (missing contaminated items) are the more dangerous failure mode; we mitigate this by requiring only 2-of-5 signal agreement, with the understanding that DIF and DVD provide complementary coverage against RL-concealment and variant contamination respectively.\n\n(iii) *Stage 2 generation failure*: If <50% of candidates survive pre-screening for a given item (below the expected 50-70% survival rate), the system relaxes the logit-deviation threshold from 1.5 to 2.0 and generates a second batch of 8-10 candidates. If the item still fails after 3 regeneration cycles, it is flagged for human review but the benchmark continues operating with the original (potentially contaminated) item marked with a quality warning — preferable to reducing test length.\n\n(iv) *Stage 3 equating failure*: If >15% of items fail the equating gate after all regeneration cycles (meaning the benchmark cannot be fully regenerated), we release a partial-regeneration version with: (a) adjusted test information function reported alongside all scores, (b) model rankings computed on both the full benchmark and the clean-items-only subset for comparison, (c) marginal reliability coefficient reported — release only if marginal reliability ≥ 0.80 for group-level comparisons (per APA standards). This partial-release strategy provides transparent validity information rather than silently degraded scores.\n\n(v) *Minimum viable benchmark*: Formally, a regenerated benchmark version is released only if: marginal IRT reliability ≥ 0.80, Spearman rho ≥ 0.90 with the pre-contamination gold standard (relaxed from 0.95 in degraded mode), anchor set ≥ 15%, and SEM ≤ 0.35 across ≥ 70% of the target ability range. These thresholds are derived from operational testing standards (Kolen & Brennan, 2004) adapted for the LLM evaluation context where group-level comparisons (model rankings) are the primary use case.\n\n**Evaluation Strategy.** Validate on three tiers: (a) Primary — LiveBench subsets (math, reasoning, coding) as currently-uncontaminated benchmarks with diverse task types and temporal structure; simulate contamination by fine-tuning open-weight models on specific LiveBench items at controlled rates (10-50%) and measuring detection sensitivity and ranking recovery. Critically, include an RL-contamination condition: apply GRPO fine-tuning (following Wang et al.'s protocol of ~156 steps on contaminated data) to open-weight models on benchmark items and verify that DIF-based detection remains effective while individual-level methods degrade — this directly tests the analytical demonstration's predictions. Additionally, test DVD's bimodal variance signature under RL contamination to determine whether it is robust, partially robust, or fragile (resolving the current empirical gap). (b) Secondary — MMLU-CF (the contamination-free MMLU replacement, ACL 2025) for knowledge-domain evaluation, running the full regeneration pipeline on synthetically contaminated subsets. (c) Positive control — use naturally-contaminated MMLU/GSM8K items (with documented contamination evidence from GSM1K studies) to verify that the contamination sentinel detects known real-world contamination. Additionally, include a **pilot feasibility study** on a single LiveBench math subset (~200 items): run the full generate-screen-calibrate-gate pipeline and report rejection rates, convergence speed, parameter recovery accuracy, ranking preservation, and graceful-degradation trigger rates — providing the first empirical evidence of generate-test-reject convergence for IRT-equated benchmark items.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '900-1300 (inference of 200-300 models on ~5K items each for IRT calibration across multiple rounds, plus item generation with 70B+ models, plus student simulation panel, plus DVD temperature-sampling at 50 generations/item)', 'timeline': '5-6 months (1.5 months multi-signal contamination detector including DIF infrastructure and DVD adaptation, 1.5 months bifactor IRT calibration infrastructure, 1.5 months generation pipeline with student simulation, 1.5 months experiments including RL-contamination condition, pilot feasibility study, and writing)', 'estimated_gpu_cost': '$1800-$2600 at ~$2/hr H100 spot pricing', 'closed_source_api_cost': '$800-$2000 (API calls for ~30-50 closed-source models in calibration panel: GPT-4o, Claude, Gemini, etc. at ~5K items each, plus student simulation inference, plus DVD temperature-sampling for closed-source models)'}, 'human_in_loop': {'gpu_hours': '800-1100 (same inference needs, Claude handles generation orchestration, IRT analysis code, DIF implementation, and DVD adaptation)', 'timeline': '3.5-4.5 months (Claude drafts contamination detection, equating code, DIF pipeline, and student simulation; human validates IRT assumptions, bifactor model specification, DIF power analysis, and experimental design)', 'claude_api_cost': '$400-$700 (Sonnet 4.6 for code generation and pipeline orchestration, ~120M tokens total with caching)', 'estimated_gpu_cost': '$1600-$2200', 'closed_source_api_cost': '$800-$2000'}, 'auto_research': {'gpu_hours': '900-1200 (cannot reduce inference needs for 200-300 model calibration panel; DVD temperature-sampling adds ~10% overhead)', 'timeline': '8-12 weeks (parallelized model evaluation is the critical path; 200-300 model panel requires ~3 weeks per calibration round even with full parallelism; pilot feasibility study adds ~2 weeks; RL-contamination condition adds ~1 week for GRPO training)', 'claude_api_cost': '$800-$1200 (Opus 4.7 for experimental design and IRT analysis, Sonnet 4.6 for implementation, ~180M tokens with caching)', 'estimated_gpu_cost': '$1800-$2400', 'closed_source_api_cost': '$800-$2000', 'speed_bottleneck': 'IRT calibration panel: collecting responses from 200-300 diverse LLMs on pilot items requires sequential API calls to closed-source models (rate limits) and batched inference on open-weight models (GPU scheduling). Minimum ~3 weeks for a single calibration round with full parallelism across ~150 open-weight models and ~50 closed-source APIs. The pilot feasibility study requires at least 2 full calibration rounds. DVD temperature-sampling (50 generations/item) adds ~10% to inference costs.'}}\n\n## Inspired By\nField guide finding that 'contamination resistance degrades question fidelity'; gap between dynamic evaluation (LiveBench, DyVal) and psychometric rigor (IRT, ATLAS); cross-domain transfer of IRT equating from educational testing to benchmark maintenance; arXiv 2602.06631's demonstration that LLMs cannot directly target difficulty parameters, motivating empirical calibration; 'Test of Time' (2025) showing temporal contamination signals are unreliable, motivating multi-signal approaches; Wang et al. (ICLR 2026) showing RL conceals all individual-level contamination signals, motivating group-level DIF analysis; Wang & Heckel (2026) showing task familiarity artifacts produce uniform improvements distinguishable from item-specific contamination via DIF; DVD's demonstration that variant contamination requires specialized detection signals; Hardy et al.'s signed isotonic R² as a lightweight pre-filter complementing parametric IRT; Sander et al.'s watermarking paradigm motivating a complementary post-hoc remediation approach; bifactor IRT and PIRT as a practical bridge between unidimensional oversimplification and intractable full MIRT; Kolen & Brennan's anchor-set theory providing formal graceful-degradation thresholds.\n\n## Target Venues\n- ICLR 2027 (deadline expected ~October 2026 based on historical pattern — not yet announced; ideal timeline for thorough experiments including pilot feasibility study and RL-contamination condition; PRIMARY TARGET)\n- AAAI 2027 (abstract July 21, paper July 28, 2026 — tight but feasible if pilot study is scoped to single domain; 2 months)\n- EACL 2027 via ARR August 2026 cycle (submission August 3, 2026 — feasible with focused experiments on LiveBench math subset)\n\n## Key References\n- LiveBench: A Challenging, Contamination-Free LLM Benchmark (ICLR 2025)\n- LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code (ICLR 2025)\n- Automating Benchmark Design [BeTaL] (ICLR 2026)\n- BenchBench: Benchmarking Automated Benchmark Generation (arXiv 2026)\n- Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration (arXiv April 2026)\n- Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory [PSN-IRT] (AAAI 2026 Oral)\n- The stability of IRT parameters under several test equating conditions (Frontiers in Psychology 2026)\n- Estimating Exam Item Difficulty with LLMs: A Benchmark on Brazil's ENEM Corpus (arXiv 2602.06631, Feb 2026)\n- Take Out Your Calculators: Estimating Real Difficulty with LLM Student Simulations (arXiv 2601.09953, Jan 2026)\n- Reconstructing Item Characteristic Curves with Fine-Tuned LLMs (arXiv 2601.02580, Jan 2026)\n- ReQUESTA: Hybrid Multi-Agent Framework for MCQ Generation (arXiv 2602.03704, Feb 2026)\n- Test of Time: Rethinking Temporal Signal of Benchmark Contamination (arXiv 2509.00072, 2025)\n- ConStat: Performance-Based Contamination Detection with FDR Control (ETH Zurich 2024)\n- Establishing Trustworthy LLM Evaluation via Shortcut Neuron Analysis (ACL 2025)\n- On The Fragility of Benchmark Contamination Detection in Reasoning Models (Wang et al., arXiv 2510.02386, ICLR 2026)\n- Detecting Data Contamination from Reinforcement Learning Post-training [Self-Critique / RL-MIA] (Tao et al., arXiv 2510.09259, ICLR 2026)\n- DVD: Detection via Variance of Generation Distribution for Variant Contamination (Liang et al., arXiv 2601.04895, Jan 2026)\n- Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis [CCV] (arXiv 2603.21454, March 2026)\n- Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients (Hardy et al., arXiv 2603.24999, March 2026)\n- Detecting Benchmark Contamination Through Watermarking (Sander et al., arXiv 2502.17259, Feb 2025)\n- Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks (Wang & Heckel, arXiv 2603.12875, March 2026)\n- Application of IRT Fixed Parameter Calibration to Multiple-Group Test Data (Kim & Kolen, Applied Measurement in Education 2019)\n- An Optimized Bayesian Hierarchical Two-Parameter Logistic Model for Small-Sample Item Calibration [OH2PL] (König, Spoden, & Frey, Applied Psychological Measurement 2020, PMC7262992)\n- Robustness of the OH2PL for Small-Sample Item Calibration (König, Spoden, & Frey, Behavior Research Methods 2022)\n- Approximating Bifactor IRT Equating with Projective IRT [PIRT] (PMC 2020)\n- Item Response Theory True Score Equating for the Bifactor Model (Kim, Journal of Educational Measurement 2022)\n- Several Variations of Simple-Structure MIRT Equating (Kim, Journal of Educational Measurement 2023)\n- MMLU-CF: A Contamination-Free Multi-task Language Understanding Benchmark (ACL 2025)\n- Simulating Training Data Leakage in Multiple-Choice Benchmarks (arXiv 2505.24263, 2025)\n- VarBench: Robust Language Model Benchmarking Through Dynamic Variable Perturbation (EMNLP 2024)\n- DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks (ICLR 2024)\n- RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning (arXiv 2025)\n- Adaptive Testing for LLM Evaluation [ATLAS] (arXiv 2025)\n- Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation (EMNLP 2025)\n- Automatic- and Transformer-Based AIG: A Critical Review (Sommer & Arendasy, Intelligence 2025)\n- Can LLMs Estimate Student Struggles? The Curse of Knowledge Effect (arXiv 2512.18880, 2025)\n- Quantifying Data Contamination in Psychometric Evaluations of LLMs (Han et al., arXiv 2510.07175, 2025)\n- Using Past Data to Enhance Small-Sample DIF Estimation: A Bayesian Approach (Sinharay et al., ETS Research Report RR-06-09, 2006)\n- Testing Differential Item Functioning in Small Samples (Belzak, Multivariate Behavioral Research 2020)\n- Item-Focused Trees for the Detection of Differential Item Functioning (Tutz & Berger, Psychometrika 2016)\n- Test Equating, Scaling, and Linking: Methods and Practices 3rd ed. (Kolen & Brennan, Springer 2014)\n- A Careful Examination of Large Language Model Performance on Grade School Arithmetic [GSM1K] (arXiv 2405.00332, 2024)\n- Power and Sample Size Calculations for Logistic Regression Tests for Differential Item Functioning (PMC5978487)\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T04:32:35.971Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:32:35.971Z",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0"
}
```

---

## Round 1

45 recorded events

### User

_source line 3 · 2026-05-20T04:32:35.993Z_

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
  "promptId": "f5da0e7a-be33-4146-af6f-49b94cea0851",
  "type": "user",
  "uuid": "c32f7ae9-7839-480d-824e-2cfc864cd15a",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:32:35.991Z_

```json
{
  "parentUuid": "c32f7ae9-7839-480d-824e-2cfc864cd15a",
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
  "uuid": "3eefc648-68fa-4030-ae7d-0d2a18390872",
  "timestamp": "2026-05-20T04:32:35.991Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:32:35.991Z_

```json
{
  "parentUuid": "3eefc648-68fa-4030-ae7d-0d2a18390872",
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
  "uuid": "ae529d20-23b6-4410-b12e-9ed6101a543f",
  "timestamp": "2026-05-20T04:32:35.991Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-20T04:32:35.991Z_

```json
{
  "parentUuid": "ae529d20-23b6-4410-b12e-9ed6101a543f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4b7c4b48-2555-4303-95ab-d4f9deddbbae",
  "timestamp": "2026-05-20T04:32:35.991Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
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
  "leafUuid": "4b7c4b48-2555-4303-95ab-d4f9deddbbae",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Self-healing benchmarks with IRT equating and contamination detection",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0"
}
```

---

### Assistant

_source line 9 · 2026-05-20T04:32:41.144Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this proposal carefully. It's about a "self-healing benchmark framework" that combines contamination detection, item generation, and IRT equating. Let me first do the required web searches to understand the current landscape before making any judgments.

Let me search for:
1. Recent work on benchmark contamination detection and remediation
2. IRT equating for LLM benchmarks
3. DIF-based contamination detection
4. The key papers cited in this proposal
5. Dynamic benchmark generation approaches
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b7c4b48-2555-4303-95ab-d4f9deddbbae",
  "isSidechain": false,
  "requestId": "req_011CbDCH7789LDv3u9nVNNeQ",
  "type": "assistant",
  "uuid": "96aa24d3-0f33-4108-938e-a73409aefeac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0162a1sRkhjwN4aV4bJEhQ4C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12446,
      "cache_read_input_tokens": 13939,
      "output_tokens": 228,
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
          "output_tokens": 228,
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

_source line 10 · 2026-05-20T04:32:42.211Z_

I'll start by conducting the required literature searches before making any assessment. Let me search for the key areas this proposal touches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96aa24d3-0f33-4108-938e-a73409aefeac",
  "isSidechain": false,
  "requestId": "req_011CbDCH7789LDv3u9nVNNeQ",
  "type": "assistant",
  "uuid": "bfbcf09b-d746-4bee-b7e7-f82bbca2644a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0162a1sRkhjwN4aV4bJEhQ4C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12446,
      "cache_read_input_tokens": 13939,
      "output_tokens": 228,
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
          "output_tokens": 228,
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

_source line 11 · 2026-05-20T04:32:42.818Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QQcBkVrmAxWY2ZSWnkc3PF`</summary>

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
  "parentUuid": "bfbcf09b-d746-4bee-b7e7-f82bbca2644a",
  "isSidechain": false,
  "requestId": "req_011CbDCH7789LDv3u9nVNNeQ",
  "type": "assistant",
  "uuid": "504a7470-00be-44d7-978e-bffece3a0a3a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0162a1sRkhjwN4aV4bJEhQ4C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12446,
      "cache_read_input_tokens": 13939,
      "output_tokens": 228,
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
          "output_tokens": 228,
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

_source line 12 · 2026-05-20T04:32:42.825Z_

<details><summary>↩ Tool result · `toolu_01QQcBkVrmAxWY2ZSWnkc3PF`</summary>

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
  "parentUuid": "504a7470-00be-44d7-978e-bffece3a0a3a",
  "isSidechain": false,
  "promptId": "f5da0e7a-be33-4146-af6f-49b94cea0851",
  "type": "user",
  "uuid": "637ed7e3-5969-4eaa-a03c-f8eb8c7baac8",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "504a7470-00be-44d7-978e-bffece3a0a3a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-20T04:32:48.690Z_

Now let me conduct the required searches in parallel to understand the current landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "637ed7e3-5969-4eaa-a03c-f8eb8c7baac8",
  "isSidechain": false,
  "requestId": "req_011CbDCHcpYq1SjUAwyqt77F",
  "type": "assistant",
  "uuid": "0a2af9dc-ea45-414b-8aaa-21923dc2ffcc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AiWHzwy4r4XnxVuGwgRP83",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 26385,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 754,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 84,
          "cache_read_input_tokens": 26385,
          "cache_creation_input_tokens": 754,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 754
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

_source line 14 · 2026-05-20T04:32:49.097Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WNEyLA7VvsD2xHCsBfkz8L`</summary>

```json
{
  "query": "benchmark contamination detection RL reasoning models 2025 2026 survey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a2af9dc-ea45-414b-8aaa-21923dc2ffcc",
  "isSidechain": false,
  "requestId": "req_011CbDCHcpYq1SjUAwyqt77F",
  "type": "assistant",
  "uuid": "cc3ddfe5-a135-4d13-9760-b1b29fff96fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AiWHzwy4r4XnxVuGwgRP83",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 26385,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 754,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 84,
          "cache_read_input_tokens": 26385,
          "cache_creation_input_tokens": 754,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 754
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

_source line 15 · 2026-05-20T04:32:58.299Z_

<details><summary>↩ Tool result · `toolu_01WNEyLA7VvsD2xHCsBfkz8L`</summary>

```text
Web search results for query: "benchmark contamination detection RL reasoning models 2025 2026 survey"

Links: [{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/pdf/2510.02386"},{"title":"[2510.02386] On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/abs/2510.02386"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=bhR00j6Mku"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/html/2510.02386v1"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://www.researchgate.net/publication/396223620_On_The_Fragility_of_Benchmark_Contamination_Detection_in_Reasoning_Models"},{"title":"Reasoning or Memorization? Unreliable Results of Reinforcement Learning Due to Data Contamination","url":"https://arxiv.org/pdf/2507.10532"}]

Based on the web search results, here are the key findings related to benchmark contamination detection in RL reasoning models for 2025-2026:

## Main Research Area

Benchmark samples may appear in LLM pre-training due to web-scraped data, and some model developers may deliberately incorporate benchmark data into training sets, resulting in inflated performance.

## Core Challenges with Reasoning Models

As LLMs have evolved into Large Reasoning Models (LRMs), benchmark contamination detection faces key challenges because LRMs rely on chain-of-thought (CoT) reasoning to reach final answers. Contamination detectors typically only have access to question-answer pairs without the intermediate reasoning steps used during training.

## Key Fragility Issues

Recent research reveals significant vulnerabilities in detection methods:

- When contamination occurs during supervised fine-tuning (SFT) of a base model into an LRM, it can be initially identified by detection methods, but even brief GRPO training can markedly conceal contamination signals that detection methods rely on.

- Although exclusive SFT on benchmark samples with CoT yields inflated performance, it leaves little evidence to existing detection approaches.

- While rejection sampling won't reduce separability between seen and unseen samples, variants that add importance sampling/clipping terms make detection harder, demonstrating a significant risk to benchmark evaluation integrity as many RL algorithms adopt similar training objectives.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc3ddfe5-a135-4d13-9760-b1b29fff96fc",
  "isSidechain": false,
  "promptId": "f5da0e7a-be33-4146-af6f-49b94cea0851",
  "type": "user",
  "uuid": "9401f324-89f6-428d-b96b-a2645e53700f",
  "toolUseResult": {
    "query": "benchmark contamination detection RL reasoning models 2025 2026 survey",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Mei36MgSteiqJM3T7SnjUX",
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
            "title": "Reasoning or Memorization? Unreliable Results of Reinforcement Learning Due to Data Contamination",
            "url": "https://arxiv.org/pdf/2507.10532"
          }
        ]
      },
      "Based on the web search results, here are the key findings related to benchmark contamination detection in RL reasoning models for 2025-2026:\n\n## Main Research Area\n\nBenchmark samples may appear in LLM pre-training due to web-scraped data, and some model developers may deliberately incorporate benchmark data into training sets, resulting in inflated performance.\n\n## Core Challenges with Reasoning Models\n\nAs LLMs have evolved into Large Reasoning Models (LRMs), benchmark contamination detection faces key challenges because LRMs rely on chain-of-thought (CoT) reasoning to reach final answers. Contamination detectors typically only have access to question-answer pairs without the intermediate reasoning steps used during training.\n\n## Key Fragility Issues\n\nRecent research reveals significant vulnerabilities in detection methods:\n\n- When contamination occurs during supervised fine-tuning (SFT) of a base model into an LRM, it can be initially identified by detection methods, but even brief GRPO training can markedly conceal contamination signals that detection methods rely on.\n\n- Although exclusive SFT on benchmark samples with CoT yields inflated performance, it leaves little evidence to existing detection approaches.\n\n- While rejection sampling won't reduce separability between seen and unseen samples, variants that add importance sampling/clipping terms make detection harder, demonstrating a significant risk to benchmark evaluation integrity as many RL algorithms adopt similar training objectives."
    ],
    "durationSeconds": 9.195649243999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "cc3ddfe5-a135-4d13-9760-b1b29fff96fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T04:33:01.281Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XU1Gg5xxnT9HiRwLXTWQWU`</summary>

```json
{
  "query": "IRT equating LLM benchmark evaluation Growing Pains bifactor 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9401f324-89f6-428d-b96b-a2645e53700f",
  "isSidechain": false,
  "requestId": "req_011CbDCJkMFktboxaC8BdVrB",
  "type": "assistant",
  "uuid": "0bfcd3ab-74fb-420f-bf1e-0705cfde6e04",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eju6W4pTz6X2tzo8tj52vF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 726,
      "cache_read_input_tokens": 27139,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 726,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 27139,
          "cache_creation_input_tokens": 726,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 726
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

_source line 17 · 2026-05-20T04:33:09.975Z_

<details><summary>↩ Tool result · `toolu_01XU1Gg5xxnT9HiRwLXTWQWU`</summary>

```text
Web search results for query: "IRT equating LLM benchmark evaluation Growing Pains bifactor 2026"

Links: [{"title":"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/html/2604.12843"},{"title":"Measuring Competency, Not Performance: Item-Aware Evaluation Across Medical Benchmarks","url":"https://arxiv.org/html/2509.24186"},{"title":"An Interpretable and Scalable Framework for Evaluating Large Language Models","url":"https://arxiv.org/html/2605.07046"},{"title":"[2605.07046] An Interpretable and Scalable Framework for Evaluating Large Language Models","url":"https://arxiv.org/abs/2605.07046"},{"title":"Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of Large Language Models in Medical Benchmarking","url":"https://arxiv.org/pdf/2603.23506"},{"title":"Measuring Competency, Not Performance: Item-Aware Evaluation Across Medical Benchmarks","url":"https://arxiv.org/pdf/2509.24186"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/pdf/2511.04689"},{"title":"IQ Test for LLMs: An Evaluation Framework for Uncovering Core Skills in LLMs","url":"https://arxiv.org/pdf/2507.20208"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/pdf/2505.15055"}]

I found several relevant results about IRT equating and LLM benchmark evaluation. Here's what I discovered:

## Key Finding: "Growing Pains" Paper

The "Growing Pains" research proposes a framework based on multidimensional Item Response Theory (IRT) that uses anchor items to calibrate new benchmarks to the evaluation suite while holding previously calibrated item parameters fixed. This directly addresses the challenge of extending LLM benchmark evaluation suites while maintaining consistency.

## Related IRT Applications in LLM Evaluation

Previous psychometric methods largely overlooked equating across different test forms, focusing instead on ability estimation within a fixed item pool. The "Growing Pains" work appears to bridge this gap by introducing IRT equating methods specifically designed for LLM benchmarking.

## Bifactor and Latent Structure Analysis

Factor-analytic studies have identified between three and eight interpretable skill dimensions that explain much of the variance in model performance across diverse tasks. This relates to bifactor modeling approaches for uncovering latent capability structures in LLMs.

## Other Notable 2026 Work

Recent research proposes an interpretable and scalable framework for LLM evaluation based on the majorization–minimization principle, reformulating the problem as a sequence of constrained matrix factorization subproblems for stable and efficient parameter estimation.

The search results show active research in 2026 on applying psychometric methods and IRT to create more robust and equatable LLM evaluation frameworks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0bfcd3ab-74fb-420f-bf1e-0705cfde6e04",
  "isSidechain": false,
  "promptId": "f5da0e7a-be33-4146-af6f-49b94cea0851",
  "type": "user",
  "uuid": "2b7d9919-04b9-4f49-8d04-571a373444cf",
  "toolUseResult": {
    "query": "IRT equating LLM benchmark evaluation Growing Pains bifactor 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QD25sv8D9FyzzCMFAgnATz",
        "content": [
          {
            "title": "Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration",
            "url": "https://arxiv.org/html/2604.12843"
          },
          {
            "title": "Measuring Competency, Not Performance: Item-Aware Evaluation Across Medical Benchmarks",
            "url": "https://arxiv.org/html/2509.24186"
          },
          {
            "title": "An Interpretable and Scalable Framework for Evaluating Large Language Models",
            "url": "https://arxiv.org/html/2605.07046"
          },
          {
            "title": "[2605.07046] An Interpretable and Scalable Framework for Evaluating Large Language Models",
            "url": "https://arxiv.org/abs/2605.07046"
          },
          {
            "title": "Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of Large Language Models in Medical Benchmarking",
            "url": "https://arxiv.org/pdf/2603.23506"
          },
          {
            "title": "Measuring Competency, Not Performance: Item-Aware Evaluation Across Medical Benchmarks",
            "url": "https://arxiv.org/pdf/2509.24186"
          },
          {
            "title": "Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks",
            "url": "https://arxiv.org/pdf/2511.04689"
          },
          {
            "title": "IQ Test for LLMs: An Evaluation Framework for Uncovering Core Skills in LLMs",
            "url": "https://arxiv.org/pdf/2507.20208"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/pdf/2505.15055"
          }
        ]
      },
      "I found several relevant results about IRT equating and LLM benchmark evaluation. Here's what I discovered:\n\n## Key Finding: \"Growing Pains\" Paper\n\nThe \"Growing Pains\" research proposes a framework based on multidimensional Item Response Theory (IRT) that uses anchor items to calibrate new benchmarks to the evaluation suite while holding previously calibrated item parameters fixed. This directly addresses the challenge of extending LLM benchmark evaluation suites while maintaining consistency.\n\n## Related IRT Applications in LLM Evaluation\n\nPrevious psychometric methods largely overlooked equating across different test forms, focusing instead on ability estimation within a fixed item pool. The \"Growing Pains\" work appears to bridge this gap by introducing IRT equating methods specifically designed for LLM benchmarking.\n\n## Bifactor and Latent Structure Analysis\n\nFactor-analytic studies have identified between three and eight interpretable skill dimensions that explain much of the variance in model performance across diverse tasks. This relates to bifactor modeling approaches for uncovering latent capability structures in LLMs.\n\n## Other Notable 2026 Work\n\nRecent research proposes an interpretable and scalable framework for LLM evaluation based on the majorization–minimization principle, reformulating the problem as a sequence of constrained matrix factorization subproblems for stable and efficient parameter estimation.\n\nThe search results show active research in 2026 on applying psychometric methods and IRT to create more robust and equatable LLM evaluation frameworks."
    ],
    "durationSeconds": 8.689181576,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0bfcd3ab-74fb-420f-bf1e-0705cfde6e04",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T04:33:12.395Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EgUU6vvojYNP6GeFeZ14Wv`</summary>

```json
{
  "query": "differential item functioning DIF contamination detection benchmark LLM novel 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b7d9919-04b9-4f49-8d04-571a373444cf",
  "isSidechain": false,
  "requestId": "req_011CbDCKcG7bgbwpg4m6J4nF",
  "type": "assistant",
  "uuid": "5ddfc4ab-cd7f-4f8e-b3b1-e3bf0bbb76df",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PNsUEut8wMLRQGRuUBzCPa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 841,
      "cache_read_input_tokens": 27865,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 841,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 27865,
          "cache_creation_input_tokens": 841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 841
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

_source line 19 · 2026-05-20T04:33:19.693Z_

<details><summary>↩ Tool result · `toolu_01EgUU6vvojYNP6GeFeZ14Wv`</summary>

```text
Web search results for query: "differential item functioning DIF contamination detection benchmark LLM novel 2025 2026"

Links: [{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"},{"title":"A Log-Linear Modeling Approach for Differential Item Functioning Detection in Polytomously Scored Items - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/31933496/"},{"title":"Detecting Differential Item Functioning across Multiple Groups Using Group Pairwise Penalty","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12805199/"},{"title":"Detection of Uniform and Non-Uniform Differential Item Functioning by   Item Focussed Trees","url":"https://arxiv.org/pdf/1511.07178"},{"title":"LLM benchmarks in 2026: What they prove and what your business actually needs | High-Quality AI Data to Power Innovation | LXT","url":"https://www.lxt.ai/blog/llm-benchmarks/"},{"title":"Detecting Benchmark Contamination Through Watermarking","url":"https://arxiv.org/pdf/2502.17259"}]

I've performed the web search with your query. Here are the relevant results:

## Key Findings:

The search returned information on two distinct but related topics:

### LLM Benchmark Contamination Detection (2025-2026)

Five detection methods work in 2026: time-based partition (the Codeforces cliff), Min-K% probability, the Time Travel guided-completion attack, ConStat performance gaps on rephrased samples, and BIG-Bench canary GUID memorization.

A novel strategy involves embedding non-intrusive watermarks in benchmark datasets before release, enabling reporting of both model performance and a reliable p-value as a contamination score.

Contamination-resistant benchmarks include LiveCodeBench, FrontierMath, MMLU-Pro, and LiveBench.

### Differential Item Functioning (DIF) Detection

Recent work includes a novel regularization method for detecting differential item functioning in two-parameter logistic models, published in 2025. DIF occurs when individuals with the same ability level respond differently to a particular test item.

The search results show active research in both contamination detection for LLMs and DIF detection methods, though these appear to be separate research domains rather than integrated approaches combining both concepts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ddfc4ab-cd7f-4f8e-b3b1-e3bf0bbb76df",
  "isSidechain": false,
  "promptId": "f5da0e7a-be33-4146-af6f-49b94cea0851",
  "type": "user",
  "uuid": "88a71408-ff76-4cc3-8ec6-51ddb3b99289",
  "toolUseResult": {
    "query": "differential item functioning DIF contamination detection benchmark LLM novel 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Nsme7eujzGFge8q42tJDVV",
        "content": [
          {
            "title": "What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide",
            "url": "https://llm-stats.com/blog/research/what-is-a-contaminated-llm"
          },
          {
            "title": "A Log-Linear Modeling Approach for Differential Item Functioning Detection in Polytomously Scored Items - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/31933496/"
          },
          {
            "title": "Detecting Differential Item Functioning across Multiple Groups Using Group Pairwise Penalty",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12805199/"
          },
          {
            "title": "Detection of Uniform and Non-Uniform Differential Item Functioning by   Item Focussed Trees",
            "url": "https://arxiv.org/pdf/1511.07178"
          },
          {
            "title": "LLM benchmarks in 2026: What they prove and what your business actually needs | High-Quality AI Data to Power Innovation | LXT",
            "url": "https://www.lxt.ai/blog/llm-benchmarks/"
          },
          {
            "title": "Detecting Benchmark Contamination Through Watermarking",
            "url": "https://arxiv.org/pdf/2502.17259"
          }
        ]
      },
      "I've performed the web search with your query. Here are the relevant results:\n\n## Key Findings:\n\nThe search returned information on two distinct but related topics:\n\n### LLM Benchmark Contamination Detection (2025-2026)\n\nFive detection methods work in 2026: time-based partition (the Codeforces cliff), Min-K% probability, the Time Travel guided-completion attack, ConStat performance gaps on rephrased samples, and BIG-Bench canary GUID memorization.\n\nA novel strategy involves embedding non-intrusive watermarks in benchmark datasets before release, enabling reporting of both model performance and a reliable p-value as a contamination score.\n\nContamination-resistant benchmarks include LiveCodeBench, FrontierMath, MMLU-Pro, and LiveBench.\n\n### Differential Item Functioning (DIF) Detection\n\nRecent work includes a novel regularization method for detecting differential item functioning in two-parameter logistic models, published in 2025. DIF occurs when individuals with the same ability level respond differently to a particular test item.\n\nThe search results show active research in both contamination detection for LLMs and DIF detection methods, though these appear to be separate research domains rather than integrated approaches combining both concepts."
    ],
    "durationSeconds": 7.293492615000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5ddfc4ab-cd7f-4f8e-b3b1-e3bf0bbb76df",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T04:33:22.368Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K77YgZS5mz6d7WCDU4XUD2`</summary>

```json
{
  "query": "DVD detection variance generation distribution variant contamination arXiv 2601.04895 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88a71408-ff76-4cc3-8ec6-51ddb3b99289",
  "isSidechain": false,
  "requestId": "req_011CbDCLKnhPFCBy1w6hBZkx",
  "type": "assistant",
  "uuid": "4668f438-cb5a-435d-baee-b498a68f7174",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014UiumdhKV9uoZmV1rd3qyr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 28706,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 700,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 28706,
          "cache_creation_input_tokens": 700,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 700
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

_source line 21 · 2026-05-20T04:33:40.192Z_

<details><summary>↩ Tool result · `toolu_01K77YgZS5mz6d7WCDU4XUD2`</summary>

```text
Web search results for query: "DVD detection variance generation distribution variant contamination arXiv 2601.04895 2026"

Links: [{"title":"[2601.04895] DVD: A Robust Method for Detecting Variant Contamination in Large Language Model Evaluation","url":"https://arxiv.org/abs/2601.04895"},{"title":"DVD: A Robust Method for Detecting Variant Contamination in Large Language Model Evaluation","url":"https://arxiv.org/html/2601.04895"},{"title":"DVD: A Robust Method for Detecting Variant Contamination in Large","url":"https://arxiv.org/pdf/2601.04895"},{"title":"clrDV: A differential variability test for RNA-Seq data based on the skew-normal distribution","url":"https://www.biorxiv.org/content/10.1101/2022.09.25.508885.full.pdf"},{"title":"Detection of AI generated images using combined uncertainty measures and particle swarm optimised rejection mechanism","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12711871/"},{"title":"[2601.22703] DAVIS: OOD Detection via Dominant Activations and Variance for Increased Separation","url":"https://arxiv.org/abs/2601.22703"},{"title":"QTL Mapping on a Background of Variance Heterogeneity","url":"https://www.biorxiv.org/content/10.1101/276980.full.pdf"},{"title":"OUT-OF-DISTRIBUTION DETECTION BASED ON TOTAL VARIATION ESTIMATION","url":"https://arxiv.org/pdf/2601.15867"},{"title":"RVD: a command-line program for ultrasensitive rare single nucleotide variant detection using targeted next-generation DNA resequencing","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3695852/"}]

Based on the search results, I found information about arXiv paper 2601.04895. Here's what the paper is about:

DVD (Detection via Variance of generation Distribution) is a single-sample detector that models the local output distribution induced by temperature sampling. The paper addresses variant contamination: when the training corpus contains semantically equivalent yet lexically or syntactically altered versions of test items.

Unlike verbatim leakage, these paraphrased or structurally transformed variants evade existing detectors based on sampling consistency or perplexity, thereby inflating benchmark scores via memorization rather than genuine reasoning.

The key insight is that contaminated items trigger alternation between a memory-adherence state and a perturbation-drift state, yielding abnormally high variance in the synthetic difficulty of low-probability tokens; uncontaminated items remain in drift with comparatively smooth variance.

The researchers construct the first benchmark for variant contamination across two domains Omni-MATH and SuperGPQA by generating and filtering semantically equivalent variants, and simulate contamination via fine-tuning models of different scales and architectures (Qwen2.5 and Llama3.1). DVD consistently outperforms perplexity-based, Min-k%++, edit-distance (CDD), and embedding-similarity baselines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4668f438-cb5a-435d-baee-b498a68f7174",
  "isSidechain": false,
  "promptId": "f5da0e7a-be33-4146-af6f-49b94cea0851",
  "type": "user",
  "uuid": "f79cf4e6-33cb-40cf-8460-03f316d216f5",
  "toolUseResult": {
    "query": "DVD detection variance generation distribution variant contamination arXiv 2601.04895 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FdbS2JP1cPSa2LmupmWBNA",
        "content": [
          {
            "title": "[2601.04895] DVD: A Robust Method for Detecting Variant Contamination in Large Language Model Evaluation",
            "url": "https://arxiv.org/abs/2601.04895"
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
            "title": "clrDV: A differential variability test for RNA-Seq data based on the skew-normal distribution",
            "url": "https://www.biorxiv.org/content/10.1101/2022.09.25.508885.full.pdf"
          },
          {
            "title": "Detection of AI generated images using combined uncertainty measures and particle swarm optimised rejection mechanism",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12711871/"
          },
          {
            "title": "[2601.22703] DAVIS: OOD Detection via Dominant Activations and Variance for Increased Separation",
            "url": "https://arxiv.org/abs/2601.22703"
          },
          {
            "title": "QTL Mapping on a Background of Variance Heterogeneity",
            "url": "https://www.biorxiv.org/content/10.1101/276980.full.pdf"
          },
          {
            "title": "OUT-OF-DISTRIBUTION DETECTION BASED ON TOTAL VARIATION ESTIMATION",
            "url": "https://arxiv.org/pdf/2601.15867"
          },
          {
            "title": "RVD: a command-line program for ultrasensitive rare single nucleotide variant detection using targeted next-generation DNA resequencing",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3695852/"
          }
        ]
      },
      "Based on the search results, I found information about arXiv paper 2601.04895. Here's what the paper is about:\n\nDVD (Detection via Variance of generation Distribution) is a single-sample detector that models the local output distribution induced by temperature sampling. The paper addresses variant contamination: when the training corpus contains semantically equivalent yet lexically or syntactically altered versions of test items.\n\nUnlike verbatim leakage, these paraphrased or structurally transformed variants evade existing detectors based on sampling consistency or perplexity, thereby inflating benchmark scores via memorization rather than genuine reasoning.\n\nThe key insight is that contaminated items trigger alternation between a memory-adherence state and a perturbation-drift state, yielding abnormally high variance in the synthetic difficulty of low-probability tokens; uncontaminated items remain in drift with comparatively smooth variance.\n\nThe researchers construct the first benchmark for variant contamination across two domains Omni-MATH and SuperGPQA by generating and filtering semantically equivalent variants, and simulate contamination via fine-tuning models of different scales and architectures (Qwen2.5 and Llama3.1). DVD consistently outperforms perplexity-based, Min-k%++, edit-distance (CDD), and embedding-similarity baselines."
    ],
    "durationSeconds": 17.818565618,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4668f438-cb5a-435d-baee-b498a68f7174",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
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
  "leafUuid": "f79cf4e6-33cb-40cf-8460-03f316d216f5",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Self-healing benchmarks with IRT equating and contamination detection",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0"
}
```

---

### Tool call

_source line 24 · 2026-05-20T04:33:44.734Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DibiXr7LhUVsPimGgHov3o`</summary>

```json
{
  "query": "self-healing benchmark regeneration automated item generation IRT equating LLM evaluation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f79cf4e6-33cb-40cf-8460-03f316d216f5",
  "isSidechain": false,
  "requestId": "req_011CbDCMqXtSWbnjqwpUMHA7",
  "type": "assistant",
  "uuid": "450ff8b0-4955-4075-9540-59048609e7c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XH9GXniKx9CM7M3nonAiyw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 864,
      "cache_read_input_tokens": 29406,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 864,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 29406,
          "cache_creation_input_tokens": 864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 864
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

_source line 25 · 2026-05-20T04:33:52.489Z_

<details><summary>↩ Tool result · `toolu_01DibiXr7LhUVsPimGgHov3o`</summary>

```text
Web search results for query: "self-healing benchmark regeneration automated item generation IRT equating LLM evaluation 2025 2026"

Links: [{"title":"BenchBench: Benchmarking Automated Benchmark Generation","url":"https://arxiv.org/pdf/2603.20807"},{"title":"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/html/2604.12843"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/pdf/2511.04689"},{"title":"Automated Evaluation of Retrieval-Augmented Language Models with Task-Specific Exam Generation","url":"https://arxiv.org/html/2405.13622v1"},{"title":"The Anatomy of an LLM Benchmark - Deep (Learning) Focus","url":"https://cameronrwolfe.substack.com/p/llm-bench"},{"title":"Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores","url":"https://arxiv.org/pdf/2601.13885"},{"title":"Deconstructing Self-Bias in LLM-generated Translation Benchmarks","url":"https://arxiv.org/pdf/2509.26600"}]

Based on my search results, I found several relevant papers addressing topics related to your query about self-healing benchmarks, automated benchmark generation, IRT equating, and LLM evaluation. Here's what I found:

## Automated Benchmark Generation and Self-Healing

BenchBench is a three-stage pipeline for benchmarking automated benchmark generation that extracts structured domain cards from seed benchmarks, prompts multiple designer LLMs to generate quota-controlled suites, and validates items with a multimodel answerer panel. The project generated 16.7K items, retained approximately 15K core items post-filtering, and produced approximately 152K graded model-item responses.

## IRT Equating for Evolving Benchmarks

A framework based on multidimensional Item Response Theory (IRT) uses anchor items to calibrate new benchmarks to the evaluation suite while holding previously calibrated item parameters fixed. This approach supports a realistic evaluation setting in which datasets are introduced over time and models are evaluated only on the datasets available at the time of evaluation, while a fixed anchor set for each dataset is used so that results from different evaluation periods can be compared directly.

## Adaptive Testing and IRT for LLM Evaluation

ATLAS is a large-scale adaptive testing framework for LLMs that achieves up to 90% item reduction while maintaining measurement precision through SE-controlled stopping, enabling flexible and precision-targeted evaluation.

These recent works (2025-2026) demonstrate active research in automated benchmark regeneration, IRT-based equating, and psychometric approaches to LLM evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "450ff8b0-4955-4075-9540-59048609e7c8",
  "isSidechain": false,
  "promptId": "f5da0e7a-be33-4146-af6f-49b94cea0851",
  "type": "user",
  "uuid": "c1604f3d-c860-447b-84bc-d05de867045d",
  "toolUseResult": {
    "query": "self-healing benchmark regeneration automated item generation IRT equating LLM evaluation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BNJFuuew43Fidy2CvLAGXB",
        "content": [
          {
            "title": "BenchBench: Benchmarking Automated Benchmark Generation",
            "url": "https://arxiv.org/pdf/2603.20807"
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
            "title": "Automated Evaluation of Retrieval-Augmented Language Models with Task-Specific Exam Generation",
            "url": "https://arxiv.org/html/2405.13622v1"
          },
          {
            "title": "The Anatomy of an LLM Benchmark - Deep (Learning) Focus",
            "url": "https://cameronrwolfe.substack.com/p/llm-bench"
          },
          {
            "title": "Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores",
            "url": "https://arxiv.org/pdf/2601.13885"
          },
          {
            "title": "Deconstructing Self-Bias in LLM-generated Translation Benchmarks",
            "url": "https://arxiv.org/pdf/2509.26600"
          }
        ]
      },
      "Based on my search results, I found several relevant papers addressing topics related to your query about self-healing benchmarks, automated benchmark generation, IRT equating, and LLM evaluation. Here's what I found:\n\n## Automated Benchmark Generation and Self-Healing\n\nBenchBench is a three-stage pipeline for benchmarking automated benchmark generation that extracts structured domain cards from seed benchmarks, prompts multiple designer LLMs to generate quota-controlled suites, and validates items with a multimodel answerer panel. The project generated 16.7K items, retained approximately 15K core items post-filtering, and produced approximately 152K graded model-item responses.\n\n## IRT Equating for Evolving Benchmarks\n\nA framework based on multidimensional Item Response Theory (IRT) uses anchor items to calibrate new benchmarks to the evaluation suite while holding previously calibrated item parameters fixed. This approach supports a realistic evaluation setting in which datasets are introduced over time and models are evaluated only on the datasets available at the time of evaluation, while a fixed anchor set for each dataset is used so that results from different evaluation periods can be compared directly.\n\n## Adaptive Testing and IRT for LLM Evaluation\n\nATLAS is a large-scale adaptive testing framework for LLMs that achieves up to 90% item reduction while maintaining measurement precision through SE-controlled stopping, enabling flexible and precision-targeted evaluation.\n\nThese recent works (2025-2026) demonstrate active research in automated benchmark regeneration, IRT-based equating, and psychometric approaches to LLM evaluation."
    ],
    "durationSeconds": 7.750755808000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "450ff8b0-4955-4075-9540-59048609e7c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T04:33:56.532Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PTio9Mv6WkzEQwtvKCiCmU`</summary>

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
  "parentUuid": "c1604f3d-c860-447b-84bc-d05de867045d",
  "isSidechain": false,
  "requestId": "req_011CbDCNk321EZzqfk6G9zig",
  "type": "assistant",
  "uuid": "64c0011c-1854-4863-94ed-2f8faa3133a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QWAE3opXkohWsLzvsGcFDV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 777,
      "cache_read_input_tokens": 30270,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 777,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 30270,
          "cache_creation_input_tokens": 777,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 777
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

_source line 27 · 2026-05-20T04:34:17.695Z_

<details><summary>↩ Tool result · `toolu_01PTio9Mv6WkzEQwtvKCiCmU`</summary>

```text
Web search results for query: "Wang Heckel test-time RL alignment task familiarity artifacts benchmarks arXiv 2603.12875"

Links: [{"title":"[2603.12875] Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks","url":"https://arxiv.org/abs/2603.12875"},{"title":"MCML - Research Group Reinhard Heckel","url":"https://mcml.ai/research/groups/heckel/"},{"title":"Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks","url":"https://arxiv.org/pdf/2603.12875"},{"title":"Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks · benchmark | Festivus","url":"https://festivus.hapticlabs.ai/data/benchmarks/test-time-rl-alignment-exposes-task-familiarity-artifacts-in-llm-benchmarks"},{"title":"GitHub - smiles724/Awesome-LLM-RLVR: Collection of latest papers and materials in the area of RLVR! · GitHub","url":"https://github.com/smiles724/Awesome-LLM-RLVR"},{"title":"1 Fine-tuning gains are largely diminished after task alignment. Left: The reported performance reveals substantial accuracy gaps between base models and their fine-tuned variants. Right: After applying TTRA to all models, the base model’s performance increases significantly, nearly matching that of the fine-tuned models, suggesting that many gains from RLVR/SFT reported in the literature are not a difference in reasoning capability, but rather artifacts of task familiarity.","url":"https://arxiv.org/html/2603.12875"},{"title":"s1: Simple test-time scaling | Request PDF","url":"https://www.researchgate.net/publication/397423327_s1_Simple_test-time_scaling"},{"title":"Mirage or Method? How Model-Task Alignment Induces Divergent RL Conclusions","url":"https://arxiv.org/pdf/2508.21188"}]

Based on the search results, here's what I found about this paper:

## Overview

The paper "Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks" by Kun Wang and Reinhard Heckel addresses how direct evaluation of LLMs on benchmarks can be misleading because comparatively strong performance may reflect task familiarity rather than capability.

## Key Problem and Solution

The train-before-test approach controls for task familiarity by giving each model task-relevant training before evaluation, originally through supervised finetuning, but suitable training data is often hard to come by, and evaluation results vary with the data chosen.

The paper proposes a two-stage test-time reinforcement learning (RL) alignment method where first, RL with a single sample provides a first alignment of the model to the task format, and second, test-time RL with majority-voting reward aligns the model to the benchmark distribution.

## Key Findings

The test-time RL alignment method aligns similarly well as SFT-based train-before test, but without requiring a task-specific training set.

For reasoning tasks, the performance gap between fine-tuned models and their base models largely disappears after alignment, suggesting that many gains from RLVR/SFT reported in the literature are not a difference in reasoning capability, but rather artifacts of task familiarity.

The paper was submitted to arXiv on March 13, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64c0011c-1854-4863-94ed-2f8faa3133a3",
  "isSidechain": false,
  "promptId": "f5da0e7a-be33-4146-af6f-49b94cea0851",
  "type": "user",
  "uuid": "63be2fe0-4b11-47d8-9e45-b09222d07fc0",
  "toolUseResult": {
    "query": "Wang Heckel test-time RL alignment task familiarity artifacts benchmarks arXiv 2603.12875",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SWd6CKSV2CHMJepWPA3Apq",
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
      "Based on the search results, here's what I found about this paper:\n\n## Overview\n\nThe paper \"Test-time RL alignment exposes task familiarity artifacts in LLM benchmarks\" by Kun Wang and Reinhard Heckel addresses how direct evaluation of LLMs on benchmarks can be misleading because comparatively strong performance may reflect task familiarity rather than capability.\n\n## Key Problem and Solution\n\nThe train-before-test approach controls for task familiarity by giving each model task-relevant training before evaluation, originally through supervised finetuning, but suitable training data is often hard to come by, and evaluation results vary with the data chosen.\n\nThe paper proposes a two-stage test-time reinforcement learning (RL) alignment method where first, RL with a single sample provides a first alignment of the model to the task format, and second, test-time RL with majority-voting reward aligns the model to the benchmark distribution.\n\n## Key Findings\n\nThe test-time RL alignment method aligns similarly well as SFT-based train-before test, but without requiring a task-specific training set.\n\nFor reasoning tasks, the performance gap between fine-tuned models and their base models largely disappears after alignment, suggesting that many gains from RLVR/SFT reported in the literature are not a difference in reasoning capability, but rather artifacts of task familiarity.\n\nThe paper was submitted to arXiv on March 13, 2026."
    ],
    "durationSeconds": 21.157775114999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "64c0011c-1854-4863-94ed-2f8faa3133a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T04:34:20.218Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017xDxLcahawUfUKaYdhx8Ha`</summary>

```json
{
  "query": "Cross-Context Verification CCV benchmark contamination session-isolated arXiv 2603.21454"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63be2fe0-4b11-47d8-9e45-b09222d07fc0",
  "isSidechain": false,
  "requestId": "req_011CbDCQbpxe8REZAuA725nH",
  "type": "assistant",
  "uuid": "33f0d394-4bd8-4d11-b7b6-b0cd542e9380",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016rKLzF1iV8JMPMaoMzCXEu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 947,
      "cache_read_input_tokens": 31047,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 947,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 31047,
          "cache_creation_input_tokens": 947,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 947
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

_source line 29 · 2026-05-20T04:34:27.221Z_

<details><summary>↩ Tool result · `toolu_017xDxLcahawUfUKaYdhx8Ha`</summary>

```text
Web search results for query: "Cross-Context Verification CCV benchmark contamination session-isolated arXiv 2603.21454"

Links: [{"title":"Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis","url":"https://arxiv.org/html/2603.21454v1"},{"title":"[2603.21454] Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis","url":"https://arxiv.org/abs/2603.21454"},{"title":"Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis","url":"https://arxiv.org/pdf/2603.21454"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/pdf/2510.27055"},{"title":"Data Contamination Can Cross Language Barriers","url":"https://arxiv.org/pdf/2406.13236"}]

I found the paper you were searching for. Here are the key details:

**Title:** Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis

**arXiv ID:** 2603.21454

**Author:** Tae-Eun Song

**Submission Date:** March 23, 2026

**Overview:**

The paper addresses a credibility crisis in LLM coding benchmarks due to widespread solution leakage and test quality issues.

**Main Contribution:**

The paper introduces Cross-Context Verification (CCV), a black-box method that solves the same benchmark problem in N independent sessions and measures solution diversity, combined with the Hierarchical Cross-Context Architecture (HCCA), a multi-agent analysis framework that prevents confirmation bias through intentional information restriction across specialized analytical roles.

**Results:**

On 9 SWE-bench Verified problems (45 trials, Claude Opus 4.6, temperature 0), CCV achieves perfect separation between contaminated and genuine reasoning, with key findings showing that contamination is binary (models either recall perfectly or not at all) and that reasoning absence is a perfect discriminator.

The paper is available on arXiv with full code and data to be released.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33f0d394-4bd8-4d11-b7b6-b0cd542e9380",
  "isSidechain": false,
  "promptId": "f5da0e7a-be33-4146-af6f-49b94cea0851",
  "type": "user",
  "uuid": "865b2106-2d72-4ac7-bc51-09d3e221f0ae",
  "toolUseResult": {
    "query": "Cross-Context Verification CCV benchmark contamination session-isolated arXiv 2603.21454",
    "results": [
      {
        "tool_use_id": "srvtoolu_0157yPQepbk8x7HLFxmZTSsA",
        "content": [
          {
            "title": "Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis",
            "url": "https://arxiv.org/html/2603.21454v1"
          },
          {
            "title": "[2603.21454] Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis",
            "url": "https://arxiv.org/abs/2603.21454"
          },
          {
            "title": "Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis",
            "url": "https://arxiv.org/pdf/2603.21454"
          },
          {
            "title": "Detecting Data Contamination in LLMs via In-Context Learning",
            "url": "https://arxiv.org/pdf/2510.27055"
          },
          {
            "title": "Data Contamination Can Cross Language Barriers",
            "url": "https://arxiv.org/pdf/2406.13236"
          }
        ]
      },
      "I found the paper you were searching for. Here are the key details:\n\n**Title:** Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis\n\n**arXiv ID:** 2603.21454\n\n**Author:** Tae-Eun Song\n\n**Submission Date:** March 23, 2026\n\n**Overview:**\n\nThe paper addresses a credibility crisis in LLM coding benchmarks due to widespread solution leakage and test quality issues.\n\n**Main Contribution:**\n\nThe paper introduces Cross-Context Verification (CCV), a black-box method that solves the same benchmark problem in N independent sessions and measures solution diversity, combined with the Hierarchical Cross-Context Architecture (HCCA), a multi-agent analysis framework that prevents confirmation bias through intentional information restriction across specialized analytical roles.\n\n**Results:**\n\nOn 9 SWE-bench Verified problems (45 trials, Claude Opus 4.6, temperature 0), CCV achieves perfect separation between contaminated and genuine reasoning, with key findings showing that contamination is binary (models either recall perfectly or not at all) and that reasoning absence is a perfect discriminator.\n\nThe paper is available on arXiv with full code and data to be released."
    ],
    "durationSeconds": 6.999047709000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "33f0d394-4bd8-4d11-b7b6-b0cd542e9380",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-20T04:34:27.227Z_

```json
{
  "parentUuid": "865b2106-2d72-4ac7-bc51-09d3e221f0ae",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "33529a6a-7ca3-4f7a-8bff-216868737398",
  "timestamp": "2026-05-20T04:34:27.227Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-20T04:34:30.165Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FYEUzMRtQTyWKrNB6sAjaH`</summary>

```json
{
  "query": "BeTaL ICLR 2026 dynamic benchmark design LLM difficulty RIDE IRT perturbation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33529a6a-7ca3-4f7a-8bff-216868737398",
  "isSidechain": false,
  "requestId": "req_011CbDCRJYfum668SHQNr2Tf",
  "type": "assistant",
  "uuid": "a028dcdf-9ace-466d-a947-022ea53e7feb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMDjRVnMoU2SHtkiwkB2SJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 31994,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 725,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 31994,
          "cache_creation_input_tokens": 725,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 725
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

_source line 32 · 2026-05-20T04:34:37.157Z_

<details><summary>↩ Tool result · `toolu_01FYEUzMRtQTyWKrNB6sAjaH`</summary>

```text
Web search results for query: "BeTaL ICLR 2026 dynamic benchmark design LLM difficulty RIDE IRT perturbation 2026"

Links: [{"title":"AUTOMATING BENCHMARK DESIGN","url":"https://openreview.net/pdf/6c3a6173bbbcaecd92e5714bac096167f405a38b.pdf"},{"title":"Automating Benchmark Design","url":"https://arxiv.org/html/2510.25039"},{"title":"Automating Benchmark Design","url":"https://arxiv.org/pdf/2510.25039"},{"title":"[2510.25039] Automating Benchmark Design","url":"https://arxiv.org/abs/2510.25039"},{"title":"Automating Benchmark Design | OpenReview","url":"https://openreview.net/forum?id=efAANptQmt"},{"title":"Published as a conference paper at ICLR 2026 FROM STATIC BENCHMARKS TO DYNAMIC","url":"https://arxiv.org/pdf/2602.23729v1"},{"title":"ICLR 2026 Schedule","url":"https://iclr.cc/virtual/2026/calendar"},{"title":"ICLR 2026 Orals","url":"https://iclr.cc/virtual/2026/events/oral"}]

Based on the search results, I found information about BeTaL, which is being submitted to ICLR 2026. Here's what I found:

## BeTaL: Automating Benchmark Design

BeTaL (Benchmark Tuning with an LLM-in-the-loop) is a framework that leverages environment design principles to automate the process of dynamic benchmark design. BeTaL works by parameterizing key design choices in base benchmark templates and uses LLMs to reason through the resulting parameter space to obtain target properties (such as difficulty and realism) in a cost-efficient manner.

## Problem Context

The rapid progress and widespread deployment of LLMs and LLM-powered agents has outpaced our ability to evaluate them. Hand-crafted, static benchmarks are the primary tool for assessing model capabilities, but these quickly become saturated. In contrast, dynamic benchmarks evolve alongside the models they evaluate, but are expensive to create and continuously update.

## Performance Results

BeTaL produces benchmarks much closer to the desired difficulty, with average deviations ranging from 5.3% to 13.2% — a 2-4× improvement over the baselines.

The search results don't contain specific information about RIDE, IRT (Item Response Theory), or perturbation methods in relation to BeTaL. The paper is currently under review for ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a028dcdf-9ace-466d-a947-022ea53e7feb",
  "isSidechain": false,
  "promptId": "f5da0e7a-be33-4146-af6f-49b94cea0851",
  "type": "user",
  "uuid": "c9646843-b080-456a-9679-e5ac48b21570",
  "toolUseResult": {
    "query": "BeTaL ICLR 2026 dynamic benchmark design LLM difficulty RIDE IRT perturbation 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ET7GTsvRm3HpW6zXmZJkoy",
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
            "title": "Automating Benchmark Design",
            "url": "https://arxiv.org/pdf/2510.25039"
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
            "title": "Published as a conference paper at ICLR 2026 FROM STATIC BENCHMARKS TO DYNAMIC",
            "url": "https://arxiv.org/pdf/2602.23729v1"
          },
          {
            "title": "ICLR 2026 Schedule",
            "url": "https://iclr.cc/virtual/2026/calendar"
          },
          {
            "title": "ICLR 2026 Orals",
            "url": "https://iclr.cc/virtual/2026/events/oral"
          }
        ]
      },
      "Based on the search results, I found information about BeTaL, which is being submitted to ICLR 2026. Here's what I found:\n\n## BeTaL: Automating Benchmark Design\n\nBeTaL (Benchmark Tuning with an LLM-in-the-loop) is a framework that leverages environment design principles to automate the process of dynamic benchmark design. BeTaL works by parameterizing key design choices in base benchmark templates and uses LLMs to reason through the resulting parameter space to obtain target properties (such as difficulty and realism) in a cost-efficient manner.\n\n## Problem Context\n\nThe rapid progress and widespread deployment of LLMs and LLM-powered agents has outpaced our ability to evaluate them. Hand-crafted, static benchmarks are the primary tool for assessing model capabilities, but these quickly become saturated. In contrast, dynamic benchmarks evolve alongside the models they evaluate, but are expensive to create and continuously update.\n\n## Performance Results\n\nBeTaL produces benchmarks much closer to the desired difficulty, with average deviations ranging from 5.3% to 13.2% — a 2-4× improvement over the baselines.\n\nThe search results don't contain specific information about RIDE, IRT (Item Response Theory), or perturbation methods in relation to BeTaL. The paper is currently under review for ICLR 2026."
    ],
    "durationSeconds": 6.989386455,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a028dcdf-9ace-466d-a947-022ea53e7feb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-20T04:34:41.434Z_

Now let me do one more targeted search on whether anyone has combined DIF with LLM contamination detection before, and on the Hardy et al. scalability coefficients paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9646843-b080-456a-9679-e5ac48b21570",
  "isSidechain": false,
  "requestId": "req_011CbDCS2z5TJzarze8kLRSx",
  "type": "assistant",
  "uuid": "f53282b7-34ff-4cae-82eb-3075bbd2cccb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqSzpUVDjsFzSKqftj4DWJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 753,
      "cache_read_input_tokens": 32719,
      "output_tokens": 111,
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
          "output_tokens": 111,
          "cache_read_input_tokens": 32719,
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

### Tool call

_source line 34 · 2026-05-20T04:34:41.931Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011T7NKXC9Ko8r7sDVrijRr6`</summary>

```json
{
  "query": "Hardy signed isotonic scalability coefficients benchmark items arXiv 2603.24999 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f53282b7-34ff-4cae-82eb-3075bbd2cccb",
  "isSidechain": false,
  "requestId": "req_011CbDCS2z5TJzarze8kLRSx",
  "type": "assistant",
  "uuid": "63c2840a-91ce-456f-86a6-83d4b2dee7d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqSzpUVDjsFzSKqftj4DWJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 753,
      "cache_read_input_tokens": 32719,
      "output_tokens": 111,
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
          "output_tokens": 111,
          "cache_read_input_tokens": 32719,
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

_source line 35 · 2026-05-20T04:34:49.230Z_

<details><summary>↩ Tool result · `toolu_011T7NKXC9Ko8r7sDVrijRr6`</summary>

```text
Web search results for query: "Hardy signed isotonic scalability coefficients benchmark items arXiv 2603.24999 2026"

Links: [{"title":"[2603.24999] Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients","url":"https://arxiv.org/abs/2603.24999"},{"title":"Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients","url":"https://arxiv.org/pdf/2603.24999"},{"title":"Optimal Hardy weights on the Euclidean lattice","url":"https://arxiv.org/pdf/2103.17019"},{"title":"Isotonic regression with unknown permutations: Statistics, computation,   and adaptation","url":"https://arxiv.org/pdf/2009.02609"},{"title":"On a more accurate Hardy-Mulholland-type inequality","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5508048/"},{"title":"Sharp constant of Hardy operators corresponding to general positive measures","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5891599/"}]

Based on the search results, I found the paper you're looking for. The research introduces a new family of nonparametric scalability coefficients based on interitem isotonic regression for efficiently detecting globally bad items, with the central contribution being the signed isotonic R², which measures the maximal proportion of variance in one item explainable by a monotone function of another while preserving the direction of association via Kendall's τ.

Across three AI benchmark datasets (HS Math, GSM8K, MMLU) and two human assessment datasets, the signed isotonic R² consistently achieves top-tier AUC for ranking bad items above good ones, outperforming or matching a comprehensive battery of classical test theory, item response theory, and dimensionality-based diagnostics.

The method remains robust under the small-n/large-p conditions typical of AI evaluation, requires only bivariate monotone fits computable in seconds, and handles mixed item types (binary, ordinal, continuous) without modification.

The paper (arXiv 2603.24999) was authored by Michael Hardy and colleagues and posted on March 27, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63c2840a-91ce-456f-86a6-83d4b2dee7d1",
  "isSidechain": false,
  "promptId": "f5da0e7a-be33-4146-af6f-49b94cea0851",
  "type": "user",
  "uuid": "8048f6c2-3827-4f05-b684-77b9ae1ef844",
  "toolUseResult": {
    "query": "Hardy signed isotonic scalability coefficients benchmark items arXiv 2603.24999 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01W2KYRfyiUjxdWAnR1NuZZE",
        "content": [
          {
            "title": "[2603.24999] Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients",
            "url": "https://arxiv.org/abs/2603.24999"
          },
          {
            "title": "Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients",
            "url": "https://arxiv.org/pdf/2603.24999"
          },
          {
            "title": "Optimal Hardy weights on the Euclidean lattice",
            "url": "https://arxiv.org/pdf/2103.17019"
          },
          {
            "title": "Isotonic regression with unknown permutations: Statistics, computation,   and adaptation",
            "url": "https://arxiv.org/pdf/2009.02609"
          },
          {
            "title": "On a more accurate Hardy-Mulholland-type inequality",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5508048/"
          },
          {
            "title": "Sharp constant of Hardy operators corresponding to general positive measures",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5891599/"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. The research introduces a new family of nonparametric scalability coefficients based on interitem isotonic regression for efficiently detecting globally bad items, with the central contribution being the signed isotonic R², which measures the maximal proportion of variance in one item explainable by a monotone function of another while preserving the direction of association via Kendall's τ.\n\nAcross three AI benchmark datasets (HS Math, GSM8K, MMLU) and two human assessment datasets, the signed isotonic R² consistently achieves top-tier AUC for ranking bad items above good ones, outperforming or matching a comprehensive battery of classical test theory, item response theory, and dimensionality-based diagnostics.\n\nThe method remains robust under the small-n/large-p conditions typical of AI evaluation, requires only bivariate monotone fits computable in seconds, and handles mixed item types (binary, ordinal, continuous) without modification.\n\nThe paper (arXiv 2603.24999) was authored by Michael Hardy and colleagues and posted on March 27, 2026."
    ],
    "durationSeconds": 7.2942956910000065,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "63c2840a-91ce-456f-86a6-83d4b2dee7d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Contamination-Triggered Benchmark Regeneration with Bifactor IRT Equating  ## Description We propose a self-heal…",
  "leafUuid": "8048f6c2-3827-4f05-b684-77b9ae1ef844",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Self-healing benchmarks with IRT equating and contamination detection",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0"
}
```

---

### Tool call

_source line 38 · 2026-05-20T04:34:52.023Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E9HuHvFtUtQfxrdrQL6Cpj`</summary>

```json
{
  "query": "\"benchmark contamination\" \"item response theory\" \"equating\" regeneration replacement items pipeline 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8048f6c2-3827-4f05-b684-77b9ae1ef844",
  "isSidechain": false,
  "requestId": "req_011CbDCSveMREFmonVuvhrp8",
  "type": "assistant",
  "uuid": "67c67dad-4505-4026-a0da-0a80065148d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8sByUMJi8DxD8Nxy8Lo4Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 670,
      "cache_read_input_tokens": 33472,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 670,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 33472,
          "cache_creation_input_tokens": 670,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 670
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

_source line 39 · 2026-05-20T04:35:01.785Z_

<details><summary>↩ Tool result · `toolu_01E9HuHvFtUtQfxrdrQL6Cpj`</summary>

```text
Web search results for query: ""benchmark contamination" "item response theory" "equating" regeneration replacement items pipeline 2025 2026"

Links: [{"title":"Item Response Theory of Test Equating for Anchor Items","url":"https://ijisrt.com/assets/upload/files/IJISRT20MAY820.pdf"},{"title":"Beyond Memorization: Reasoning-Driven Synthesis as a Mitigation Strategy Against Benchmark Contamination","url":"https://arxiv.org/pdf/2509.00072"},{"title":"Efficiency Analysis of Item Response Theory Kernel Equating for Mixed-Format Tests","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10664743/"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/pdf/2505.15055"},{"title":"The stability of IRT parameters under several test equating conditions","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12832260/"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/pdf/2510.02386"},{"title":"Detecting Benchmark Contamination Through Watermarking","url":"https://arxiv.org/pdf/2502.17259"}]

I found several relevant search results related to your query. Here's what I discovered:

## Benchmark Contamination & Item Response Theory

The search returned research on multiple related topics:

**Benchmark Contamination in LLMs (2025-2026):**
LLM benchmarks exhibit data contamination in numerous items, compromising their reliability. Recent work addresses this challenge through various approaches. Periodic collection methods such as LiveBench (White et al., 2025) promised to complete regular content updates but suffer from short shelf life and resource-intensive maintenance requirements.

A contamination-resistant evaluation framework has been developed that leverages the natural temporal structure of research publication to scale automatically with scientific progress, making it impossible for models to encounter evaluation content synthesized from papers published after their training cutoff dates.

**Item Response Theory & Test Equating:**
Test equating research focuses on comparing results from different test sets (e.g., re-testing, parallel test forms), with test sets often linked using anchor items as a common denominator alongside distinct items.

More recent work applies IRT to benchmark analysis: A benchmark analysis framework called PSN-IRT was proposed with superior estimation accuracy and reliability, and LLM benchmarks suffer from widespread saturation and insufficient difficulty ceilings, limiting their ability to challenge and accurately evaluate advanced models.

**Item Regeneration/Replacement:**
The search results suggest that addressing contamination involves creating new evaluation content rather than replacing existing contaminated items, though direct information about item regeneration pipelines for 2025-2026 was limited in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67c67dad-4505-4026-a0da-0a80065148d7",
  "isSidechain": false,
  "promptId": "f5da0e7a-be33-4146-af6f-49b94cea0851",
  "type": "user",
  "uuid": "2e734618-26a9-4ba6-a2c9-c7a3bc7d4869",
  "toolUseResult": {
    "query": "\"benchmark contamination\" \"item response theory\" \"equating\" regeneration replacement items pipeline 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JiBe2s4mkZxTshsee7WFb8",
        "content": [
          {
            "title": "Item Response Theory of Test Equating for Anchor Items",
            "url": "https://ijisrt.com/assets/upload/files/IJISRT20MAY820.pdf"
          },
          {
            "title": "Beyond Memorization: Reasoning-Driven Synthesis as a Mitigation Strategy Against Benchmark Contamination",
            "url": "https://arxiv.org/pdf/2509.00072"
          },
          {
            "title": "Efficiency Analysis of Item Response Theory Kernel Equating for Mixed-Format Tests",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10664743/"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/pdf/2505.15055"
          },
          {
            "title": "The stability of IRT parameters under several test equating conditions",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12832260/"
          },
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/pdf/2510.02386"
          },
          {
            "title": "Detecting Benchmark Contamination Through Watermarking",
            "url": "https://arxiv.org/pdf/2502.17259"
          }
        ]
      },
      "I found several relevant search results related to your query. Here's what I discovered:\n\n## Benchmark Contamination & Item Response Theory\n\nThe search returned research on multiple related topics:\n\n**Benchmark Contamination in LLMs (2025-2026):**\nLLM benchmarks exhibit data contamination in numerous items, compromising their reliability. Recent work addresses this challenge through various approaches. Periodic collection methods such as LiveBench (White et al., 2025) promised to complete regular content updates but suffer from short shelf life and resource-intensive maintenance requirements.\n\nA contamination-resistant evaluation framework has been developed that leverages the natural temporal structure of research publication to scale automatically with scientific progress, making it impossible for models to encounter evaluation content synthesized from papers published after their training cutoff dates.\n\n**Item Response Theory & Test Equating:**\nTest equating research focuses on comparing results from different test sets (e.g., re-testing, parallel test forms), with test sets often linked using anchor items as a common denominator alongside distinct items.\n\nMore recent work applies IRT to benchmark analysis: A benchmark analysis framework called PSN-IRT was proposed with superior estimation accuracy and reliability, and LLM benchmarks suffer from widespread saturation and insufficient difficulty ceilings, limiting their ability to challenge and accurately evaluate advanced models.\n\n**Item Regeneration/Replacement:**\nThe search results suggest that addressing contamination involves creating new evaluation content rather than replacing existing contaminated items, though direct information about item regeneration pipelines for 2025-2026 was limited in these results."
    ],
    "durationSeconds": 9.756886047999986,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "67c67dad-4505-4026-a0da-0a80065148d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-20T04:35:04.656Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TfJmTqVgj2DQ1cgjWNAMwF`</summary>

```json
{
  "query": "LLM difficulty estimation item generation student simulation arXiv 2602.06631 arXiv 2601.09953"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e734618-26a9-4ba6-a2c9-c7a3bc7d4869",
  "isSidechain": false,
  "requestId": "req_011CbDCTrHSytsaUgTqGqcvB",
  "type": "assistant",
  "uuid": "49f8433a-058c-47fb-b1a8-e401f7fb3f43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193br6sQYFb9CjNt1FvGg8G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 34142,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 781,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 34142,
          "cache_creation_input_tokens": 781,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 781
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

_source line 41 · 2026-05-20T04:35:11.083Z_

<details><summary>↩ Tool result · `toolu_01TfJmTqVgj2DQ1cgjWNAMwF`</summary>

```text
Web search results for query: "LLM difficulty estimation item generation student simulation arXiv 2602.06631 arXiv 2601.09953"

Links: [{"title":"[2601.09953] Take Out Your Calculators: Estimating the Real Difficulty of Question Items with LLM Student Simulations","url":"https://arxiv.org/abs/2601.09953"},{"title":"Estimating Exam Item Difficulty with LLMs: A Benchmark on Brazil's ENEM Corpus","url":"https://arxiv.org/pdf/2602.06631"},{"title":"The LLM Already Knows: Estimating LLM-Perceived Question Difficulty via Hidden Representations","url":"https://arxiv.org/pdf/2509.12886"},{"title":"Estimating Exam Item Difficulty with LLMs: A Benchmark on Brazil’s ENEM Corpus","url":"https://arxiv.org/html/2602.06631v1"},{"title":"The LLM Already Knows: Estimating LLM-Perceived Question Difficulty via Hidden Representations","url":"https://arxiv.org/html/2509.12886"},{"title":"Take Out Your Calculators: Estimating the Real Difficulty of Question Items with LLM Student Simulations","url":"https://arxiv.org/pdf/2601.09953"},{"title":"[2509.12886] The LLM Already Knows: Estimating LLM-Perceived Question Difficulty via Hidden Representations","url":"https://arxiv.org/abs/2509.12886"}]

Based on the search results, I found both papers you referenced:

**arXiv 2601.09953 - "Take Out Your Calculators: Estimating the Real Difficulty of Question Items with LLM Student Simulations"**

This paper investigates the predictive value of open-source large language models (LLMs) for evaluating the difficulty of multiple-choice math questions for real-world students. The research uses Item Response Theory (IRT) to estimate both difficulty and discriminability parameters, since difficulty inherently depends on who answers, not just what is asked.

**arXiv 2602.06631 - "Estimating Exam Item Difficulty with LLMs: A Benchmark on Brazil's ENEM Corpus"**

This paper benchmarks ten proprietary and open-weight LLMs against official Item Response Theory (IRT) parameters for 1,031 questions from Brazil's high-stakes ENEM exam. The results reveal that while the best models achieve moderate rank correlation, they systematically underestimate difficulty and degrade significantly on multimodal items. The authors conclude that LLMs function best as calibrated screeners rather than authoritative oracles, supporting an "evaluation-before-generation" pipeline for responsible assessment design.

Both papers address the critical question of whether LLMs can reliably estimate question difficulty for educational assessment and item generation purposes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49f8433a-058c-47fb-b1a8-e401f7fb3f43",
  "isSidechain": false,
  "promptId": "f5da0e7a-be33-4146-af6f-49b94cea0851",
  "type": "user",
  "uuid": "96b4b481-7155-4ba7-af68-38bc096538f3",
  "toolUseResult": {
    "query": "LLM difficulty estimation item generation student simulation arXiv 2602.06631 arXiv 2601.09953",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QUbCM3nrS1iM43UcVa23Sg",
        "content": [
          {
            "title": "[2601.09953] Take Out Your Calculators: Estimating the Real Difficulty of Question Items with LLM Student Simulations",
            "url": "https://arxiv.org/abs/2601.09953"
          },
          {
            "title": "Estimating Exam Item Difficulty with LLMs: A Benchmark on Brazil's ENEM Corpus",
            "url": "https://arxiv.org/pdf/2602.06631"
          },
          {
            "title": "The LLM Already Knows: Estimating LLM-Perceived Question Difficulty via Hidden Representations",
            "url": "https://arxiv.org/pdf/2509.12886"
          },
          {
            "title": "Estimating Exam Item Difficulty with LLMs: A Benchmark on Brazil’s ENEM Corpus",
            "url": "https://arxiv.org/html/2602.06631v1"
          },
          {
            "title": "The LLM Already Knows: Estimating LLM-Perceived Question Difficulty via Hidden Representations",
            "url": "https://arxiv.org/html/2509.12886"
          },
          {
            "title": "Take Out Your Calculators: Estimating the Real Difficulty of Question Items with LLM Student Simulations",
            "url": "https://arxiv.org/pdf/2601.09953"
          },
          {
            "title": "[2509.12886] The LLM Already Knows: Estimating LLM-Perceived Question Difficulty via Hidden Representations",
            "url": "https://arxiv.org/abs/2509.12886"
          }
        ]
      },
      "Based on the search results, I found both papers you referenced:\n\n**arXiv 2601.09953 - \"Take Out Your Calculators: Estimating the Real Difficulty of Question Items with LLM Student Simulations\"**\n\nThis paper investigates the predictive value of open-source large language models (LLMs) for evaluating the difficulty of multiple-choice math questions for real-world students. The research uses Item Response Theory (IRT) to estimate both difficulty and discriminability parameters, since difficulty inherently depends on who answers, not just what is asked.\n\n**arXiv 2602.06631 - \"Estimating Exam Item Difficulty with LLMs: A Benchmark on Brazil's ENEM Corpus\"**\n\nThis paper benchmarks ten proprietary and open-weight LLMs against official Item Response Theory (IRT) parameters for 1,031 questions from Brazil's high-stakes ENEM exam. The results reveal that while the best models achieve moderate rank correlation, they systematically underestimate difficulty and degrade significantly on multimodal items. The authors conclude that LLMs function best as calibrated screeners rather than authoritative oracles, supporting an \"evaluation-before-generation\" pipeline for responsible assessment design.\n\nBoth papers address the critical question of whether LLMs can reliably estimate question difficulty for educational assessment and item generation purposes."
    ],
    "durationSeconds": 6.422524208999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "49f8433a-058c-47fb-b1a8-e401f7fb3f43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-20T04:35:59.535Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information from my searches to do a thorough evaluation. Let me synthesize what I've found and analyze this proposal critically.

## Summary of the Proposal

This proposal describes a "self-healing benchmark framework" with four integrated components:
1. Multi-signal contamination detection (with a novel DIF-based approach claimed to be RL-robust)
2. Construct-constrained item generation with empirical calibration
3. Bifactor IRT equating gate
4. Graceful degradation framework

## My Analysis

### Trivial Alternative Check
Is there a simpler way to achieve similar goals?

The most trivial alternative is what LiveBench already does: just create new benchmarks from scratch on a regular schedule. 

The proposal's main advantage over this is maintaining score comparability across time through IRT equating, but in practice leaderboards get refreshed and old rankings disappear anyway — so the real value of strict psychometric equating might be overstated. Similarly, for contamination detection, time-bounded benchmarks like LiveBench's approach (only evaluating on post-training-cutoff questions) eliminate the problem by construction, which is simpler than the proposal's multi-signal detection system. The proposal acknowledges this but argues its approach adds psychometric rigor — which is true, though the practical necessity of that added complexity remains unclear.

The DIF-based contamination detection for RL models is genuinely novel and the logic holds: DIF examines between-group behavioral patterns rather than within-model distributions, making it robust to RL training dynamics. The full pipeline from detection through generation to equating is also comprehensive in a way existing work isn't, and the psychometric grounding is solid. But the core tension is whether this level of system complexity — with multiple interdependent components — justifies the incremental gains over simpler alternatives like just refreshing benchmarks regularly.

The novelty of applying DIF to LLMs is real, though the underlying insight of comparing model cohorts on specific items is fairly intuitive once you frame it that way. A much simpler cross-cohort comparison tracking accuracy shifts on individual items across model generations might yield similar results without needing the full IRT machinery. The sample size constraints are also problematic — the proposal needs 40-80 models per cohort for DIF to work, and while it proposes mitigations like Bayesian priors and temporal aggregation, these haven't been validated in the LLM benchmark space yet. There's also a risk that by trying to solve detection, generation, equating, and degradation all in one paper, the work becomes too sprawling and doesn't develop any single component deeply enough for publication.

Most reviewers familiar with psychometrics would immediately recognize that DIF across model cohorts makes sense for contamination detection — it's not a surprising leap. The full integration is novel in scope but mostly combines existing methods. The bifactor IRT equating for benchmarks is a new application, though Growing Pains already uses MIRT. The graceful degradation framework is a fresh framing, but the actual thresholds and procedures follow standard testing practices pretty directly. The core problem — contamination plus score drift — is genuinely significant, but I need to assess whether this particular approach is the right vehicle for addressing it.

The practical barriers are substantial: benchmark creators would need to maintain large calibration panels and invest in serious psychometric infrastructure. The related work section is genuinely exceptional — I've rarely seen this level of thoroughness in addressing competing approaches. But stepping back, the proposal feels like a highly competent execution of an idea that's more "sensible" than "surprising." The system's complexity might exceed what the field actually needs, and it's unclear how anyone would realistically adopt this. The scope also seems ambitious for a single effort.

Looking at this more carefully though, I'm reconsidering the novelty angle. Using DIF specifically for contamination detection is genuinely new — no one's done this before. And closing the full loop from detection through generation, equating, and degradation assessment is also novel in a way that matters. The execution will be critical here, and while the DIF insight is sound, it's more of an incremental application of existing methodology than a surprising finding. I'd estimate this around 30% — the direction is right and the novelty is real, but it's the kind of idea where the core insight feels somewhat predictable once you see it. I'm settling on 28-30% as my confidence estimate. The core contribution—using DIF as a contamination detection signal—is genuinely useful and analytically sound, but the overall work is fundamentally a systems integration of existing components. While that approach can succeed at EMNLP with strong empirical validation, the conceptual novelty here isn't quite sufficient to carry it if the results are merely solid rather than exceptional.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96b4b481-7155-4ba7-af68-38bc096538f3",
  "isSidechain": false,
  "requestId": "req_011CbDCUY6LuniN9gk7CNito",
  "type": "assistant",
  "uuid": "aa3fe2c4-7806-47fc-87aa-a210176c5ae9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016T3CQ9NJ7ZFdLY8B6dreky",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 788,
      "cache_read_input_tokens": 34923,
      "output_tokens": 6229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 788,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6229,
          "cache_read_input_tokens": 34923,
          "cache_creation_input_tokens": 788,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 788
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

_source line 43 · 2026-05-20T04:37:43.518Z_

Now I have sufficient information from my literature search. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:

1. Wang et al. "On The Fragility of Benchmark Contamination Detection in Reasoning Models" (arXiv 2510.02386, ICLR 2026):
   - 验证了 proposal 的核心前提：GRPO/PPO 训练确实会使 reference-free 检测方法 AUROC 降低 14-20pp，Min-K% 降至接近随机（~50%）。Proposal 对此文献的引用和描述准确。
   - 与本 proposal 关系：proposal 的 DIF 方案直接回应此论文揭示的问题。该论文没有提出 group-level DIF 方法，只展示了 individual-level 方法的脆弱性。

2. "Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration" (arXiv 2604.12843, April 2026):
   - 使用 multidimensional IRT + fixed-parameter calibration + 100 anchor items，实现跨时间的 LLM 评估可比性（Spearman ρ ≥ 0.9，400+ models）。
   - 与本 proposal 关系：最直接的并发竞争者。但 Growing Pains 只做 evaluation extensibility，不做 contamination detection 或 item regeneration。Proposal 对此文献定位准确。差异真实存在——但 Growing Pains 已经占据了"IRT for LLM benchmark"的核心叙事位置。

3. DVD "A Robust Method for Detecting Variant Contamination" (arXiv 2601.04895, Jan 2026):
   - 通过 generation variance 检测 variant contamination，AUC 0.73-0.74 vs Min-K%++ 的 0.43-0.68。但仅在 SFT 模型上验证。
   - 与本 proposal 关系：被整合为 ensemble 的一个 signal。Proposal 诚实地标注 DVD 未在 RL 模型上测试，并将此设为实验目标。

4. BeTaL "Automating Benchmark Design" (ICLR 2026):
   - LLM-in-the-loop 自动化 benchmark 设计，聚焦于调控 difficulty。
   - 与本 proposal 关系：BeTaL 追求"增加难度"，本 proposal 追求"保持等值"——方向不同。Proposal 定位准确。

5. Wang & Heckel "Test-time RL alignment exposes task familiarity artifacts" (arXiv 2603.12875, March 2026):
   - TTRA 使 base model 性能接近 fine-tuned model，表明很多 fine-tuning gains 是 task familiarity artifacts。
   - 与本 proposal 关系：proposal 用此区分 DIF 信号（item-specific contamination → DIF signal）vs. task familiarity（uniform improvement → no DIF signal）。论点逻辑上成立。

6. Cross-Context Verification CCV (arXiv 2603.21454, March 2026):
   - 通过 session-isolated solution diversity 检测 coding benchmark contamination，在 SWE-bench 上达到完美分离。
   - 与本 proposal 关系：CCV 仅验证于 coding tasks（9 problems），泛化性存疑。Proposal 正确指出其局限。

7. Hardy et al. "Efficient Detection of Bad Benchmark Items" (arXiv 2603.24999, March 2026):
   - 提出 signed isotonic R² scalability coefficients，在 HS Math/GSM8K/MMLU 上 AUC 优于 IRT-based diagnostics。
   - 与本 proposal 关系：被整合为 pre-filter。合理但非核心贡献。

8. BenchBench "Benchmarking Automated Benchmark Generation" (arXiv 2603.20807, March 2026):
   - 系统化评估 automated benchmark generation pipeline 的 discrimination 和 validity。
   - 与本 proposal 关系：评估 generation quality 但不做 equating。Proposal 定位准确。

9. arXiv 2602.06631 "Estimating Exam Item Difficulty with LLMs" (Feb 2026):
   - LLM 直接估计难度仅达 ρ=0.10-0.45。Proposal 引用准确，并据此放弃直接 IRT parameter conditioning。

10. arXiv 2601.09953 "Take Out Your Calculators" (Jan 2026):
    - Student simulation 难度估计达 r=0.75-0.82。Proposal 引用准确。

- **调研总结**：该领域当前处于"各组件分散发展"阶段——contamination detection（Wang et al., DVD, ConStat）、IRT-based evaluation（Growing Pains, PSN-IRT, ATLAS）、item generation（BenchBench, BeTaL, ReQUESTA）各自独立。没有现有工作完成 detection → generation → equating 的全闭环。Proposal 处于"系统集成+一个新检测信号（DIF）"的位置。DIF 用于 LLM contamination detection 是检索范围内的首次提出。

【Trivial Alternative 检验】:

存在两个重要的 trivial alternative：

(1) **LiveBench 模式（时间隔离法）**：直接从训练截止日期之后的新来源创建评估题目，从根本上避免 contamination。无需检测、无需 equating。Proposal 的增量价值在于：(a) 不是所有 benchmark 都能用时间隔离（如 MMLU 的知识域题目）；(b) LiveBench 式刷新不保证 psychometric equivalence，分数不可跨版本比较。但问题是：**NLP 社区实际上多大程度上需要跨版本分数严格可比？** 现实中 leaderboard 定期重置，旧排名被丢弃。这个增量价值是真实的但可能被高估。

(2) **简单跨 cohort accuracy delta**：不用完整的 logistic regression DIF，只是直接比较新旧 cohort 在各 item 上的 accuracy 差异（控制总分后做 residual analysis）。这种 trivial version 可能捕获 DIF 所检测信号的大部分。Proposal 的增量价值在于：DIF 提供正式的 psychometric 框架、effect size 分类（ETS A/B/C）、和 FDR 控制。但核心信号（跨 cohort 的 item-level differential performance）可以用更简单的方法获取。

**判断**：trivial alternative 威胁中等。全闭环管道确实比任何单一替代方案更完整，但核心检测信号（DIF）的简化版本可能效果接近。Proposal 的不可替代价值主要在 equating guarantee + graceful degradation，而非 detection 本身。

【前提假设检验】:

核心逻辑链中以下假设未经验证：

(1) **"Contamination 必然产生 item-specific advantage → DIF signal"**——这是最关键的假设。Proposal 论证：contamination 必须创造 differential item advantage，否则 contamination 就失去了意义（"RL cannot conceal without negating the purpose of contamination"）。这个论证在逻辑上成立，但忽略了一个微妙情况：**如果一个 model 被 contaminated 但 contamination 效果分散在大量 items 上（例如整个 dataset 都泄露了），则每个 item 的 DIF effect size 可能很小，导致 DIF underpowered**。Proposal 部分承认了这一点（"DIF is underpowered for small effects"），但将此定位为"检测大效应的工具"。问题是：如果整个 benchmark 都泄露了（这在 MMLU 等知名 benchmark 中很常见），effect sizes 可能是 medium-small 而非 large，因为所有 items 都有 boost。

(2) **"200-300 diverse LLMs 的 calibration panel 可以提供足够的 IRT calibration"**——教育测试中 IRT calibration 通常需要 N≥500 examinees。Proposal 使用 OH2PL 在 N≥50 时声称 unbiased estimates，但这些结论来自人类考试场景（item responses 更接近 IRT 假设），LLM responses 的 IRT model fit 可能完全不同（如 4PL 或 more complex patterns）。

(3) **"Bifactor IRT 适合 LLM benchmark 的 latent structure"**——这假设 LLM 能力可以分解为 general factor + domain-specific factors。但 LLM 的能力结构可能更复杂（不同 training recipe 导致完全不同的 factor structure），bifactor 模型可能不够灵活。Growing Pains 使用 MIRT 而非 bifactor，暗示 factor structure 选择是开放问题。

(4) **"Student simulation pre-screening (r=0.75-0.82) 足以替代 direct difficulty targeting"**——这些相关系数来自教育测试场景，在 LLM benchmark 场景中未经验证。LLM-as-student 和 LLM-as-examinee 的一致性可能更低。

【3 维度打分】:

1. **Novelty: 中** — DIF 用于 LLM contamination detection 在我的调研范围内确实是首次提出，且 RL-robustness 论证有逻辑说服力——这是真实的 novelty delta。但透过 surface 看本质：(a) DIF 本身是 1980s 就有的成熟方法，应用到新场景是"novel application"而非"novel methodology"；(b) 全闭环管道的各组件（ConStat perturbation testing, DVD variance detection, IRT equating, student simulation）均为已有方法的组装，system-level novelty 但非 methodological novelty；(c) DIF 的 RL-robustness 论证虽然 sound，但核心洞察（"behavioral response pattern 不受 output distribution smoothing 影响"）一旦说出来是 intuitive 的，审稿人不太会说"surprising"。与 Growing Pains（MIRT + fixed-parameter calibration for temporal extension）相比，本 proposal 的 novelty 在 contamination detection + remediation 维度，但在 IRT methodology 维度是 incremental。

2. **Significance: 中偏强** — 研究问题（benchmark contamination + score comparability over time）是 LLM 社区真正关心的问题。Wang et al. (ICLR 2026) 揭示 RL 训练破坏现有检测方法的事实让这个方向格外重要和及时。如果 DIF 方法被验证有效，它将是社区应对 RL contamination 的一个重要工具。但显著性受限于：(a) 系统的实际部署门槛极高（需要 200-300 model calibration panel），可能限制社区采用；(b) 论文可能过于 systems-oriented——"我们把很多东西粘在一起"可能被视为 engineering contribution 而非 scientific insight；(c) 最有洞察力的单一贡献（DIF for RL-robust detection）可能足以独立成篇，而将其埋在一个巨型 pipeline 中反而稀释了它的 impact。

3. **Related Work: 强** — 这是该 proposal 最突出的优点。对几乎所有相关工作的覆盖都是准确的、有差异化定位的：Wang et al. (RL fragility), Growing Pains (temporal extension without detection), DVD (variant detection without remediation), BeTaL (difficulty evolution not preservation), CCV (coding-only), ConStat (detection without remediation), Sander et al. (watermarking = prevention not post-hoc), Wang & Heckel (task familiarity).每篇工作的引用和描述经搜索验证基本准确。差异化清晰且公正。唯一的小瑕疵：对 Growing Pains 的区分虽然准确，但审稿人可能会问"为什么不在 Growing Pains 的 framework 上增加 contamination detection module"——proposal 应该更明确地回应这个自然的 follow-up。

【概率估计】: [22% - 35%] 中位 27%

【估计理由】:
- Novelty 为"中"限制了上界。核心贡献（DIF for RL-robust contamination detection）是一个 sound 但 unsurprising 的 insight——将教育测试的成熟方法应用到 LLM 评估的新场景。审稿人看到后大概率反应是"makes sense"而非"I wouldn't have guessed this"。全闭环管道是 system-level novelty，但 NLP 会议对 systems paper 的评价标准更侧重于 empirical impact 而非 pipeline 完整性。
- Significance 中偏强为本 proposal 提供了一些上行空间——问题确实重要且及时，Wang et al. (ICLR 2026) 的发现让 RL-robust detection 成为一个真实需求。
- Related Work 的出色覆盖降低了被拒的下行风险（不太可能因为 missing related work 被拒），但 related work 好只能防止扣分，不能加分。
- 概率主要被 novelty 的"中"评级锚定在 25-30% 区间。如果 DIF 实验结果强势（特别是 RL contamination condition 展示 DIF 成功检测而其他方法失败），empirical contribution 可以将概率推向上界（~35%）。但 idea 本身的 ceiling 大约就在这里。
- 此外，论文可能面临"too much for one paper"的审稿批评——四个组件中任何一个都可以是一篇独立论文，压缩在一起可能导致每个组件都不够深入。

【主要风险】:
1. **"Novel application of existing methodology" vs. "novel methodology"**：审稿人可能认为 DIF 用于 contamination detection 是一个 straightforward application，novelty 不足以支撑顶会论文。这尤其危险，因为 DIF 的 RL-robustness 论证虽然 sound，但一旦说出来就显得 obvious——"当然 behavioral patterns 不受 output distribution smoothing 影响"。
2. **Pipeline 过于庞大导致 depth 不足**：四个 contribution（detection ensemble + generation pipeline + bifactor equating + graceful degradation）在一篇论文中可能无法充分展示任何一个的深度。审稿人可能建议"focus on DIF detection and do it thoroughly"或"focus on the equating framework"，认为当前 scope 太广。这是 idea framing 层面的风险，不是执行层面的——即使实验做得很好，"我们做了一个大 pipeline"的 narrative 在 novelty 评审中天然处于劣势。
```

Sources:
- [On The Fragility of Benchmark Contamination Detection in Reasoning Models](https://arxiv.org/abs/2510.02386)
- [Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration](https://arxiv.org/html/2604.12843)
- [DVD: A Robust Method for Detecting Variant Contamination](https://arxiv.org/abs/2601.04895)
- [Automating Benchmark Design (BeTaL)](https://arxiv.org/abs/2510.25039)
- [Test-time RL alignment exposes task familiarity artifacts](https://arxiv.org/abs/2603.12875)
- [Cross-Context Verification (CCV)](https://arxiv.org/abs/2603.21454)
- [Efficient Detection of Bad Benchmark Items (Hardy et al.)](https://arxiv.org/abs/2603.24999)
- [Estimating Exam Item Difficulty with LLMs](https://arxiv.org/abs/2602.06631)
- [Take Out Your Calculators: LLM Student Simulations](https://arxiv.org/abs/2601.09953)
- [BenchBench: Benchmarking Automated Benchmark Generation](https://arxiv.org/abs/2603.20807)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa3fe2c4-7806-47fc-87aa-a210176c5ae9",
  "isSidechain": false,
  "requestId": "req_011CbDCUY6LuniN9gk7CNito",
  "type": "assistant",
  "uuid": "64703f3e-0ade-41b4-9523-1254dfff4649",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016T3CQ9NJ7ZFdLY8B6dreky",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 788,
      "cache_read_input_tokens": 34923,
      "output_tokens": 6229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 788,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6229,
          "cache_read_input_tokens": 34923,
          "cache_creation_input_tokens": 788,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 788
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

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Contamination-Triggered Benchmark Regeneration with Bifactor IRT Equating  ## Description We propose a self-heal…",
  "leafUuid": "64703f3e-0ade-41b4-9523-1254dfff4649",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Self-healing benchmarks with IRT equating and contamination detection",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Contamination-Triggered Benchmark Regeneration with Bifactor IRT Equating  ## Description We propose a self-heal…",
  "leafUuid": "64703f3e-0ade-41b4-9523-1254dfff4649",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Self-healing benchmarks with IRT equating and contamination detection",
  "sessionId": "7de8aab4-8c5e-461b-b9ea-b233d22ef3d0"
}
```

---
