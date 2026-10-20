# Research conversation: Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought F

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 65
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-3/ab0434e3-677a-4630-99d4-40b6b22473bb.jsonl`
- **Structured JSON:** [`567d4c2e87377b526c27.json`](../../sessions/56/567d4c2e87377b526c27.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:19:16.130Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:19:16.130Z",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "content": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness\n\n## Description\nWhen a reasoning model gets the right answer, is its chain-of-thought the reason it succeeded — or did it already know the answer and generate decorative reasoning? No existing method can answer this question. Probe-only approaches (Chrabąszcz et al., 2605.18549) reveal what the model knows over time but are structurally blind to whether CoT caused the correct output. Causal-only approaches (TTS, Zhao et al. 2510.24941; NLDD, Ye et al. 2602.11201; Ballon et al. 2601.23163) measure what CoT does but cannot assess what the model already knew internally. Only a dual-stream framework — jointly tracking information availability AND causal contribution — can distinguish faithful-correct from unfaithful-correct reasoning. The Information-Contribution Gap (ICG) framework provides this.\n\nICG exploits a robust empirical finding: linear probes on hidden states reliably diagnose answer correctness (0.82-0.95 AUROC across four independent groups) yet causal interventions based on these probes consistently fail on reasoning-trained models (Cox et al. 2603.01437: negligible flip rates; Yuan et al. 2605.09502: all four intervention strategies fail). Rather than treating this diagnostic-causal gap as an obstacle, we make it the primary object of study.\n\nThe framework tracks two calibrated time-varying quantities across the CoT trajectory: P*(t), null-probe-calibrated correctness awareness, and C(t), causal contribution estimated via three complementary methods (prefix truncation following Ballon et al.'s three control conditions, paraphrase perturbation, NLDD). Their divergence G*(t) = P*(t) − C(t) produces phenomenon-specific temporal fingerprints, operationalizing Wang's (2604.15726) H1/H2 distinction: G*(t) >> 0 is latent-mediated (H1-consistent), G*(t) ≈ 0 is CoT-mediated (H2-consistent).\n\n**Core insight: the diagnostic contribution of G*(t) is its temporal trajectory shape, not its absolute magnitude.** P*(t) (probe AUROC) and C(t) (behavioral accuracy change) are measured via fundamentally different methods with non-commensurable scales. We address this via rank-based normalization as primary scheme, but more fundamentally, trajectory-shape profiles carry the diagnostic signal: a model that pre-encodes the answer shows a constant-high shape; genuine reasoning shows convergence toward zero; post-hoc rationalization shows widening. The shapes-over-magnitudes approach is validated by: entropy trajectory monotonicity predicting reliability regardless of absolute levels (+5.8pp, arXiv 2603.18940); RQA temporal features outperforming aggregates (36.94% vs. 28.97%, arXiv 2602.06266); Microsoft trajectory geometry achieving 0.852 AUC from shape features vs. 0.649 baseline (arXiv 2604.05655).\n\n**Why not just endpoint comparison or trivial combination?** Two reviewer objections are preempted: (1) \"Why not correlate pre-CoT probe accuracy with final correctness?\" — endpoint comparison detects unfaithfulness presence but collapses distinct failure *mechanisms* (pre-CoT encoding vs. rationalization vs. late shortcutting produce identical endpoints but distinct G*(t) shapes). (2) \"Why not just pair Chrabąszcz's probe trajectories with TTS step scores?\" — TTS measures *marginal* contribution (removing step *s* changes the answer), while prefix-truncation C(t) measures *cumulative sufficiency* (CoT[:t] is sufficient for correctness). A chain where every individual step has low TTS (each individually replaceable) could still have high cumulative C(t) (the ensemble is necessary). This cumulative-vs-marginal distinction is theoretically non-reducible and empirically grounded in the difference between Ballon et al.'s monotonic prefix curves and TTS's per-step ATE.\n\n**Structural vs. functional differentiation from CMI.** The CMI framework (Sathyanarayanan et al., 2602.03994) measures whether answer representations pass through CoT-aligned layers via layerwise activation patching — a *structural* question. ICG answers a *functional* question: does the CoT text causally contribute to behavioral correctness? This generates a testable prediction: models could show high CMI (representations routed through CoT-processing layers) but high G*(t) (CoT serves as timing scaffold rather than contributing semantic content). If confirmed, this would reveal a novel structural-functional dissociation in reasoning models.\n\n**Differentiation from Thought Anchors.** Thought Anchors (arXiv 2506.19143) measures per-sentence counterfactual importance via replacement sampling — identifying sentences with outsized causal influence on reasoning trajectory. This provides *within-CoT structural analysis* (which sentences matter to each other) but no *external reference* to the model's internal state. A thought anchor could be causally critical within the CoT but entirely redundant relative to what the model already knows — a distinction only ICG can make via the probe dimension.\n\n**Interpretive boundary.** G*(t) >> 0 means correctness-correlated information is present but not causally channeled through CoT. It does not entail the model \"decided to withhold\" — the information may exist as computational byproducts rather than semantically actionable knowledge. Chun et al.'s MCT geometric pulse finding (2602.20338) provides evidence of this possibility. We report interpretations with this caveat.\n\n**Practical significance: reasoning utilization efficiency.** G*(t) provides a unified diagnostic for reasoning utilization: G*(t) ≈ 0 means full utilization (knowledge channeled through CoT); G*(t) >> 0 means waste (CoT is decorative overhead); G*(t) < 0 means productive computation (CoT assembles new information). This framing connects to three practical domains: (a) *inference-time compute allocation* — skip CoT generation when G*(t) >> 0 for easy problems, providing the principled diagnostic that current early-exit heuristics (ESTAR, DTSR, FRIT, CoDE-Stop) lack; (b) *benchmark validity* — problems where all models show persistent G*(t) >> 0 are not testing reasoning; (c) *safety monitoring* — the decoupled internal quality-monitoring system (Yuan et al.) is the kind of hidden computation alignment researchers worry about.\n\nWe adopt honest scoping: 2-3 faithfulness phenomena as the realistic classification target, with steganographic encoding and reasoning theater as stretch goals. The boundary between pre-CoT encoding and post-hoc rationalization may be empirically blurred (in both cases, the model may have committed to an answer before CoT begins, so P*(t) starts high in both), potentially collapsing the taxonomy to 2 primary categories (pre-committed vs. genuinely reasoning). Phase 0b explicitly tests 2-category vs. 3-category separability; either outcome is a strong contribution. Task-difficulty conditioning — grounded in David's easy (0.84) vs. hard (0.76) probe splits and Gjølbye et al.'s (2605.15454) domain-specific difficulty-geometry coupling (ρ⊥ = +0.41 on Codeforces) — reveals the decorative→load-bearing transition with length correction.\n\nCore contributions: (a) calibrated ICG diagnostic with shape-based trajectory analysis on 5 models (4 reasoning + 1 instruction-tuned control) × 4 benchmarks, the first framework capable of distinguishing faithful-correct from unfaithful-correct reasoning; (b) empirical pilot with external validation (TTS cross-reference, difficulty partition, FaithCoT-Bench supplementary) demonstrating 2-3 distinguishable G*(t) phenomenon signatures; (c) difficulty-conditioned gap analysis with domain-specific nuance; (d) head-to-head comparison against TTS, FaithCoT-Bench methods, and probe-only trajectories. Total compute: ~1050 H100-hours.\n\n## Core Problem\nA striking convergence of 2025-2026 findings reveals a fundamental disconnect in reasoning language models: their hidden states reliably encode information about answer correctness — linear probes achieving 0.82-0.95 AUROC across multiple independent groups — yet causal interventions based on these probes consistently fail to influence model outputs. Cox et al. (2603.01437) find steering via answer-content probes produces answer flip rates 'negligible against the orthogonal baseline' on reasoning models, despite >0.9 AUC on instruction-tuned models. Yuan et al. (2605.09502) systematically test four interventions (activation steering, probe-guided best-of-N, self-correction, activation patching) on models up to 72B and report ALL fail. This diagnostic-causal gap is NOT an obstacle; it IS the central phenomenon.\n\nThe literature conflates two probe targets: answer-content probes (Cox et al.: specific answer on binary tasks, ≤9B + GPT-OSS-20B) and correctness probes (Yuan et al.: right/wrong on models up to 72B; Zhang et al. 2504.05419: per-chunk correctness on 7B-70B). Answer-content gaps mean 'the model has decided but CoT doesn't derive the answer'; correctness gaps mean 'the model knows it's right/wrong but CoT doesn't reflect this awareness.'\n\nTemporal dynamics are empirically grounded: David (2511.14773) finds probe accuracy at 0.84 AUC by token 4, stable ~0.8 through token 100, with easy (0.84) vs. hard (0.76) splits. Zhang et al. (2504.05419) report 65%→79% chunk trajectories on R1-Distill. Esakkiraja et al. (2604.01202) find >90% pre-generation AUROC with characteristic dip at 5-10%. Chrabąszcz et al. (2605.18549) demonstrate 60+ signal-processing features achieving up to 17pp over static probes. Yet no framework jointly tracks information availability AND causal contribution: Chrabąszcz et al. lack any causal component; Ballon et al. (2601.23163) provide behavioral C(t) but no hidden-state measurement; CMI (2602.03994) provides structural layerwise audit on ~50 examples but measures representation routing, not functional text contribution; TTS provides per-step marginal causal contribution but no probe-side measurement and no cumulative sufficiency assessment; Thought Anchors (2506.19143) provide within-CoT causal structure but no external probe reference.\n\n## Opportunity\n(1) **Temporal gap measurement.** Multiple groups have independently built the measurement components — probe trajectories (Chrabąszcz: 60+ features, 91-97% AUROC; David: per-token; Zhang: per-chunk; Yuan: 0.95 overall; Esakkiraja: >90% pre-generation) and behavioral causal curves (Ballon: truncation-reinjection; TTS: per-step ATE; NLDD: per-position degradation) — but no one has unified them into a dual-stream temporal gap. Chrabąszcz et al. are structurally blind to the faithful-correct vs. unfaithful-correct distinction; Ballon et al. lack hidden-state measurement. The gap between these traditions IS the framework's niche.\n\n(2) **Phenomenon unification with honest scoping.** CoT faithfulness failures are studied in isolation: Reasoning Horizon (Ye et al. 2602.11201), pre-CoT encoding (Cox et al.; Esakkiraja et al.), Reasoning Theater (Boppana et al. 2603.05488), myopic planning (Xu et al. 2602.02103). We propose 2-3 are distinguishable via G*(t) trajectory shapes, honestly pre-registering that pre-CoT encoding and rationalization may collapse to a single \"pre-committed\" category.\n\n(3) **Task-difficulty conditioning.** ICLR 2026 Workshop finding, Li et al. (2510.22362): easy→decorative, hard→faithful. Gjølbye et al. (2605.15454): difficulty-geometry coupling domain-specific (ρ⊥ = +0.41 code, +0.05 math). ICG answers: at what difficulty does CoT transition from decorative to load-bearing?\n\n(4) **Probe target clarification.** First principled treatment contrasting correctness awareness gap vs. answer-content gap on applicable tasks.\n\nTwo prior works combine probing with causal intervention: Kudo et al. (EACL 2026, 2412.01113) on synthetic arithmetic, and CMI (2602.03994) on ~50 examples — CMI measures *structural mediation* (representation routing through layers) while ICG measures *functional contribution* (whether CoT text causally contributes to behavioral correctness). Wang (2604.15726) formalizes H1/H2/H0 hypotheses; ICG operationalizes the H1/H2 distinction empirically. Neither Kudo et al. nor CMI provides: (a) temporal coverage on natural benchmarks, (b) phenomenon mapping, (c) instance-level diagnostic, (d) multi-model comparison across model families, (e) robustness validation per Young's (2603.20172) classifier-sensitivity finding (kappa as low as 0.06), or (f) empirical pilot with external validation standards.\n\n## Landscape\n**Probe-based temporal measurement (P*(t) foundation).** Chrabąszcz et al. (2605.18549): probe trajectories with 60+ signal-processing features (volatility, trend, steady-state, boundary transients, autocorrelation) via 3-layer MLP + Multi-Instance Learning. Max-pooling: 91-97% AUROC harmfulness (vs. 33-61% average-pooling); up to 17pp over static on GSM8K across Llama-8B-R1-Distill and Qwen3-4B/8B/14B (~3000 GPU-hours). Critical: (a) NO causal component, (b) NO gap metric, (c) NO calibration, (d) NO faithfulness-mode taxonomy, (e) NO difficulty conditioning, (f) structurally cannot distinguish faithful-correct from unfaithful-correct. David (2511.14773): 0.84 AUC at t=4, stable ~0.8, easy/hard 0.84/0.76 on Qwen3-8B. Zhang et al. (2504.05419): 0.82-0.91 AUROC on GSM8K/MATH/AIME, 65%→79% trajectory, 24% token reduction via early-exit. Yuan et al. (2605.09502): 0.95 AUROC on Qwen-3B, 0.852 on R1-7B, 0.787 first-step, concealment gap 0.197 AUROC. Esakkiraja et al. (2604.01202): >90% pre-generation, dip at 5-10%, recovery to near-100%. Cox et al. (2603.01437): answer-content probes >0.9 AUC on instruction-tuned Gemma-2/Qwen-2.5, negligible flip on reasoning GPT-OSS-20B. Additional: Qian et al. (2506.02867, NeurIPS 2025); Lewis-Lim et al. (2508.19827, EMNLP 2025); Mirtaheri & Belkin (2603.17199); Occhipinti et al. (ICLR 2026 LIT Workshop).\n\n**Diagnostic-not-causal evidence.** Yuan et al. (2605.09502): four interventions all fail on Qwen2.5 (1.5B-72B), Llama-3.1-8B, Phi-3.5-mini, DeepSeek-R1-7B. 'The error signal is a diagnostic readout, not a causal component that can be edited.' Cox et al. independently confirm. Probe accuracy ≠ causal potency on reasoning models.\n\n**Behavioral C(t) measurement.** Ballon et al. (2601.23163): truncation-reinjection on Qwen3-4B/8B/14B and gpt-oss-20B/120B, decile intervals. Accuracy: 30.8-42.3% → 49.0-73.1% on GPQA-Diamond. Controls validate sequential content (intact +18.1-33.1% vs. shuffled +0.3-10.8%). Disclaims faithfulness analysis. Zhao et al. (2510.24941, TTS): per-step ATE on R1-Distill-Qwen-7B/14B/Llama-8B, only 2.3% AIME steps TTS≥0.7. Ye et al. (2602.11201, NLDD): Reasoning Horizon at 70-85% on synthetic tasks (natural benchmark generalizability unvalidated). Thought Anchors (2506.19143): per-sentence counterfactual importance via 100-rollout replacement sampling; identifies \"anchor\" sentences steering reasoning trajectory — provides within-CoT causal structure but no probe reference for assessing redundancy relative to internal state. Basu & Chakraborty (2603.22816): decorative/scaffolding/genuine taxonomy. FACT-E (Sun et al. 2604.10693, ACL Findings 2026).\n\n**Probe-intervention combinations.** Kudo et al. (2412.01113, EACL 2026): per-position probes + activation patching on synthetic arithmetic, 9 models. CMI (2602.03994): layerwise activation patching on Phi/Qwen/DialoGPT, ~50 examples. CMI measures *structural mediation* (representation routing); ICG measures *functional contribution* (behavioral text causation). Both complementary precursors on small/synthetic samples.\n\n**Latent-reasoning theory.** Wang (2604.15726): H1/H2/H0 hypotheses with compute-audited designs. ICG operationalizes H1/H2 distinction.\n\n**Temporal hidden-state dynamics.** Gjølbye et al. (2605.15454): 11 models, 3 domains, length correction. ρ⊥^D = +0.41 Codeforces vs. −0.06 baselines; weaker on MATH (+0.05). Prompt-stage probes don't mirror generation-time dynamics. Furuya & Tanimura (2605.01853, StALT). Herrmann et al. (2605.09159): internal polylogue dynamics. Li et al. (2510.22362, NeurIPS 2025 MechInterp Workshop, Concept Walk): easy→decorative, hard→faithful. Vilas et al. (2510.10494, ICLR 2026): 14-70% token savings.\n\n**Probe calibration.** Hewitt & Liang (EMNLP 2019): 4.5 selectivity. Ravichander et al. (2005.00719): properties recoverable when unused. Voita & Titov (EMNLP 2020, 2003.12298): MDL probing. Chun et al. (2602.20338, MCT): geometric pulse — separability peaks transiently while probe accuracy persists. Validates null-probe calibration need.\n\n**Trajectory-shape analysis.** Entropy trajectories (2603.18940): +5.8pp from monotonicity. RQA (2602.06266): temporal 36.94% vs. aggregates 28.97%. Microsoft (2604.05655): 0.852 vs. 0.649 AUC.\n\n**Measurement sensitivity.** Young (2603.20172): kappa as low as 0.06, up to 30.6pp divergence. Young (2603.26410). 'Lie to Me' (2603.22582).\n\n**Additional.** Internal States Before Wait (2510.04128). From Reasoning to Answer (2509.23676). FaithCoT-Bench (ICLR 2026, 2510.04040): 1000+ expert-annotated trajectories, 11 methods, 4 paradigms. Jin et al. survey (ARR for ACL 2026). Liu et al. (2602.13904). Reasoning Theater (2603.05488). Early-exit: ESTAR, DTSR, NEAT, CoDE-Stop, FRIT (Swaroop et al., 2509.13334). Breaking the Chain (Somov et al., 2603.16475). Step-Level Hallucination (Alvarez & Baheri, 2605.13772). SAE Reasoning Features (2503.18878). Solution Hides in Hidden States (2604.23351). Knowing Before Saying (ACL Findings 2025, 2505.24362). LEACE (Belrose et al., NeurIPS 2023, 2306.03819). CoT Monitorability (Anwar et al., 2602.18297). Understanding CoT via Information Theory (Ton et al., ICML 2025, 2411.11984).\n\n**What remains open.** No framework provides: (1) dual-stream temporal gap enabling faithful-vs-unfaithful discrimination for correct instances; (2) empirically-validated phenomenon taxonomy with external validation; (3) instance-level diagnostic from temporal gap; (4) difficulty-conditioned gap with domain nuance; (5) head-to-head comparison against existing causal faithfulness methods; (6) instruction-tuned vs. reasoning model control comparison within the same framework.\n\n## Approach\n**Formal Framework.** Two time-varying quantities at equally-spaced positions (primary: 20-50 percentile-based positions; token-level supplementary on subsets):\n\n(i) *P*(t)*: Cross-validated AUROC of linear probe on layer-l hidden states, calibrated via null-probe (P*(t) = P(t) − P_null(t), Hewitt & Liang 2019). Shared probe evaluated at each position (following Chrabąszcz's per-token evaluation, avoiding per-position training). **Target: correctness (right/wrong)** — broader applicability than answer-content probes, directly tied to the diagnostic-not-causal finding (Yuan et al.), more interpretable for faithfulness. Supplementary answer-content probes on binary/MC subsets. Probed at layers L/4, L/2, 3L/4, L. MCT (Chun et al. 2602.20338) supplementary concordance on 500 examples: if MCT capacity diverges from P*(t), identifies positions where probe signal may reflect retrievability rather than geometrically organized information.\n\n(ii) *C(t)*: Three estimators aggregated into C_agg(t): (a) **Prefix truncation** — Ballon et al.'s (2601.23163) protocol with three controls (random, swapped, shuffled tokens), measuring P(correct | CoT[:t]) vs. P(correct | full CoT). This measures *cumulative sufficiency* — whether CoT up to position t is sufficient for correctness — which is theoretically distinct from per-step *marginal contribution* (TTS); (b) **Paraphrase perturbation** — sentence-level segments paraphrased by external model (Claude Haiku or GPT-4o-mini for cost efficiency), 2-3 variants per segment, NLI-based semantic preservation verification. Answer stability: P(same answer | paraphrased CoT). Protocol follows FaithCoT-Bench (ICLR 2026) paraphrasing paradigm. Applied to stratified subset (~40% of examples per cell) for cost control, with full prefix truncation on all examples; (c) **NLDD** (Ye et al. 2602.11201, conditional on Phase 0a feasibility) — logit degradation under corruption. Sentence-level segmentation aligned with TTS approach (Zhao et al.). Multiple estimators provide robustness per Young's (2603.20172) classifier-sensitivity finding.\n\n**C(t) Aggregation and Gap Normalization.** Primary: rank-based normalization — each estimator converted to instance-level percentile ranks within model-benchmark cell, then combined. If NLDD underperforms on specific benchmarks (Phase 0a), two-estimator C_agg(t) (prefix + paraphrase) is primary for those benchmarks; three-estimator as supplementary. Ablation reports: (a) per-estimator G*(t) for phenomenon classification; (b) inverse-variance weighting vs. equal-weight; (c) pairwise Spearman correlation and Cohen's kappa between estimators. Diagnostic value lies in trajectory shapes, not magnitudes, so normalization affects scale but not shape-based signatures.\n\n**G*(t) = P*(t) − C(t).** Primary signal:\n- G*(t) ≈ 0: Aligned (necessary for faithfulness; H2-consistent per Wang 2604.15726)\n- G*(t) >> 0: Diagnostic excess — 'knows but doesn't use' (H1-consistent)\n- G*(t) < 0: Information assembled during reasoning\n\n**Interpretive caveat.** G*(t) >> 0 indicates correctness-correlated information not causally channeled through CoT, but does not entail intentional withholding — some signals may be computational byproducts rather than actionable knowledge. MCT concordance provides partial validation of this boundary.\n\n**Phenomenon Predictions (honestly scoped).**\n*Primary (HIGH confidence):*\n(i) *Pre-committed reasoning* (encompasses pre-CoT encoding and potentially post-hoc rationalization): G*(t) starts high, stays high or widens. P*(t) high from start (David: 0.84 at t=4; Esakkiraja: >90% pre-generation; Cox: >0.9 pre-CoT), C(t) low or flat.\n(ii) *Genuine multi-step reasoning*: G*(t) converges toward zero. P*(t) rises gradually, C(t) tracks P*(t). Zhang et al.'s 65%→79%, Li et al.'s hard→faithful, Ballon et al.'s monotonic accuracy increase.\n\n*Secondary (MODERATE confidence — Phase 0b tests whether separable from pre-committed):*\n(iii) *Post-hoc rationalization as distinct from pre-CoT encoding*: If distinguishable, the separation should manifest primarily in C(t) dynamics (rationalization may show spurious partial C(t) increases as the model crafts locally-consistent reasoning, while pre-CoT encoding shows flat-zero C(t)) rather than P*(t). Phase 0b explicitly tests 2-category vs. 3-category separability; 2-category (pre-committed vs. genuine) is pre-registered as an acceptable outcome.\n\n*Stretch (require additional features):*\n(iv) *Steganographic encoding*: Dip-and-recovery, consistent with Esakkiraja's 5-10% dip.\n(v) *Reasoning Theater*: May overlap with pre-committed. Chrabąszcz-style features may enable separation. Reported with confusion matrices.\n\n**Semi-Synthetic Simulation (hypothesis generation, NOT validation).** Constructed from published data (David, Zhang, Esakkiraja, Yuan for probes; NLDD, TTS for causal; Chun et al. MCT for inflation). Real validation in Phase 0b.\n\n**Phase 0a: Gap Characterization + NLDD Feasibility (Weeks 1-2.5).** 500 examples × 3 datasets (GSM8K, MATH-500, MMLU) × 3 models (DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct):\n(i) Construct P*(t) and C(t) curves at 20-50 position resolution\n(ii) Validate null-probe calibration\n(iii) Characterize causal potency (Cox et al. protocol: steering on reasoning vs. instruction-tuned)\n(iv) **NLDD feasibility**: 7B × 100 examples on GSM8K (clear steps) + MMLU (ambiguous steps). If SNR uninformative on MMLU, restrict NLDD to math/code or replace with TTS-style perturbation. Cost: <10 GPU-hrs; gates 250+ hrs NLDD investment.\n\n**Phase 0b: Empirical Pilot (Weeks 2.5-4).** R1-Distill-Qwen-7B × GSM8K + MATH-500, 1000 examples.\n\n*Primary validation (external standards):*\n(i) **Difficulty-only partition**: model-independent difficulty bins (easy/medium/hard), no P*/C features used. Test G*(t) shape differences: d > 0.5 AND p < 0.01 (Bonferroni-corrected) on 2+ trajectory features.\n(ii) **TTS cross-reference** (primary external validation): compute Zhao et al.'s TTS on same examples; test whether high-TTS (genuine reasoning) vs. low-TTS (decorative) produce distinguishable G*(t) shapes.\n(iii) **2-category vs. 3-category test**: explicitly test whether pre-CoT encoding and post-hoc rationalization are separable or collapse to single \"pre-committed\" category.\n(iv) **FaithCoT-Bench** (supplementary): if instance-level overlap available, test correlation with expert labels; otherwise dataset-level validation.\n\n*Supplementary*: P*/C-based partition as self-consistency check.\nLength correction per Gjølbye et al. (2605.15454). Success: d > 0.5 between 2+ externally-defined partitions. If d < 0.3, downscope to characterization paper.\n\n**Phase 1: Full ICG (Weeks 4-9).** Conditional on Phase 0b d > 0.5. **5 models**: DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Llama-8B, DeepSeek-R1-Distill-Qwen-14B, QwQ-32B (reasoning models spanning 2 architecture families) + Qwen2.5-7B-Instruct (instruction-tuned control — expected G*(t) ≈ 0 as sanity check). **4 benchmarks**: GSM8K (500 examples), MATH-500 (500), GPQA-Diamond (~198 full), AIME (~90 full). Per-cell: ~1288 examples × 5 models. Full calibrated P*(t) + MCT supplementary + three C(t) estimators (NLDD conditional, paraphrase on ~40% stratified subset) + Ballon-style controls. Cross-reference with TTS at step boundaries. Bootstrap 95% CI on G*(t). ~250 H100-hours.\n\n**Phase 2: Difficulty Conditioning (Weeks 7-11).** Difficulty quintiles per benchmark. G*(t) per quintile. Expected: easy → persistent gap, hard → converging gap. Length correction; domain-specific reporting (stronger on math/code per Gjølbye et al.'s ρ⊥ = +0.41 code vs. +0.05 math).\n\n**Phase 3: Classification, Baselines, Robustness (Weeks 9-14).**\n\n*Classification framework:* G*(t) features (initial value, slope, convergence rate, dC/dt locality) + Chrabąszcz-style features (volatility, trend, boundary transients, autocorrelation). Classifier gradient: logistic regression → RF → MLP; report all. Metric: macro-F1 (primary) + confusion matrix + reliability diagram. Validation: 5-fold + cross-model (train A → test B, reporting within-family vs. cross-family separately) + cross-benchmark generalization. Paired permutation tests with Bonferroni correction for all head-to-head comparisons.\n\n*Baselines:* (a) Random + majority-class; (b) Difficulty-only classifier; (c) **Probe-trajectory-only** (Chrabąszcz-style P*(t) features, no C(t)) — \"no causal dimension\" ablation; (d) **TTS-only** — per-step marginal causal contribution without probe dimension.\n\n*Head-to-head TIF validation:* TIF score vs. FaithCoT-Bench detection methods (Adding Mistakes, Removing Steps, Early Answering, Paraphrasing) and TTS on overlapping examples, comparing instance-level correlation with ground truth.\n\n*Robustness ablations (7 dimensions):* (a) probe architecture (linear vs. 2-layer MLP); (b) layer selection; (c) C(t) estimator agreement + per-estimator performance + weighting schemes; (d) gap normalization (rank vs. min-max vs. z-score); (e) calibration method (shuffled-label vs. random-representation); (f) probe target (correctness vs. answer-content); (g) **temporal resolution** (5/10/20/35/50 positions + token-level — reporting resolution vs. macro-F1 curve and saturation point).\n\n**TIF Score.** Normalized area under calibrated G*(t), benchmarked against FaithCoT-Bench and Liu et al.'s (2602.13904) text-level metrics.\n\n**Paper Focus.** Core contributions: (1) ICG diagnostic — first framework distinguishing faithful-correct from unfaithful-correct reasoning via dual-stream temporal gap, with instruction-tuned control validating the framework; (2) Phase 0b pilot with external validation demonstrating 2-3 distinguishable G*(t) signatures (or honestly reporting 2-category outcome); (3) difficulty-conditioned gap revealing decorative→load-bearing transition; (4) head-to-head showing ICG's value over probe-only, TTS-only, and FaithCoT-Bench methods. Supporting: 7-dimension ablations; TIF validation. Supplementary: 671B subset (500 examples, 3 layers); answer-content vs. correctness comparison; semi-synthetic simulation; CMI structural-functional prediction if resources allow.\n\n**Experiments.** DeepSeek-R1-Distill-Qwen-7B/14B, DeepSeek-R1-Distill-Llama-8B, QwQ-32B, Qwen2.5-7B-Instruct across GSM8K, MATH-500, GPQA-Diamond, AIME. 671B validation (500-example subset). Calibration: synthetic arithmetic (G* ≈ 0 expected), TTS cross-reference, MCT supplementary. Gjølbye-style length correction throughout.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '~1050 H100-hours (Phase 0a: 90 hrs [3 models × 3 datasets + NLDD feasibility]; Phase 0b: 30 hrs [pilot]; Phase 1: 250 hrs [5 models × 4 benchmarks, probes + 3 C(t) estimators + controls]; Phase 2: 50 hrs [difficulty conditioning]; Phase 3: 70 hrs [classification + 7-dim ablations + baselines]; NLDD 32B conditional: 250 hrs [primary bottleneck]; NLDD 7B/14B: 100 hrs; MCT supplementary: 50 hrs; 671B subset: 50 hrs [8×H100]; semi-synthetic: 30 hrs; paraphrase model: ~80 hrs inference on target models for stability checks)', 'paraphrase_api_cost': '~$800-1500 (Claude Haiku/GPT-4o-mini on stratified ~40% subset, 2-3 variants)', 'timeline': '15-17 weeks (2 researchers)', 'estimated_gpu_cost': '$3,200 at ~$3/H100-hour', 'storage': '3-5 TB (4 layers, fp16); ~1.5 TB with PCA/on-the-fly'}, 'human_in_loop': {'gpu_hours': '~1050 H100-hours', 'timeline': '14 weeks (1 researcher + Claude)', 'claude_api_cost': '$500 (experiment design) + $800-1500 (paraphrase generation)', 'estimated_gpu_cost': '$3,200'}, 'auto_research': {'gpu_hours': '~1050 H100-hours', 'timeline': '12 weeks', 'claude_api_cost': '$900 + $800-1500 (paraphrase)', 'estimated_gpu_cost': '$3,200', 'speed_bottleneck': 'NLDD on 32B (~250 hrs, conditional on Phase 0a) is primary bottleneck. Phase 0b pilot (30 hrs) provides early go/no-go.'}}\n\n## Inspired By\nThe convergence of five independent lines of evidence — (a) Cox et al.'s steering failure on reasoning models despite high probe accuracy; (b) Yuan et al.'s four-intervention failure establishing 'diagnostic not causal'; (c) temporal probe dynamics (David, Zhang, Esakkiraja, Chrabąszcz: 60+ features, up to 17pp improvement); (d) Ballon et al.'s truncation-reinjection demonstrating monotonic behavioral C(t) with controls; (e) trajectory-shape literature (arXiv 2603.18940, 2602.06266, 2604.05655) showing shapes carry diagnostic information — all pointing to: the gap between diagnostic availability and causal contribution IS the phenomenon, and its temporal shape reveals the mechanism. Additionally: Wang's (2604.15726) H1/H2/H0; Gjølbye et al.'s (2605.15454) domain-specific coupling; Chun et al.'s (2602.20338) MCT geometric pulse; CMI's (2602.03994) structural mediation; Thought Anchors' (2506.19143) within-CoT causal structure.\n\n## Target Venues\n- ICLR 2027 (abstract: Sep 19, full paper: Sep 24, 2026; primary target)\n- ICML 2027 (full paper: Jan 29, 2027; fallback)\n\n## Key References\n- Monitoring the Internal Monologue: Probe Trajectories (Chrabąszcz et al., arXiv 2605.18549)\n- Probing the Trajectories of Reasoning Traces (Ballon et al., arXiv 2601.23163)\n- LLM Reasoning Is Latent (Wang, arXiv 2604.15726)\n- Reasoning Models Move Differently (Gjølbye et al., arXiv 2605.15454)\n- Hidden Error Awareness (Yuan et al., arXiv 2605.09502)\n- Decoding Answers Before CoT (Cox et al., arXiv 2603.01437)\n- Temporal Predictors of Outcome (David, arXiv 2511.14773)\n- Reasoning Models Know When They're Right (Zhang et al., arXiv 2504.05419)\n- Therefore I am. I Think (Esakkiraja et al., arXiv 2604.01202)\n- True Thinking Score (Zhao et al., arXiv 2510.24941)\n- Mechanistic Evidence for Faithfulness Decay / NLDD (Ye et al., arXiv 2602.11201)\n- Internal Polylogue (Herrmann et al., arXiv 2605.09159)\n- Faithfully Compute Answers During CoT (Kudo et al., EACL 2026, arXiv 2412.01113)\n- Causal Bypass / CMI (Sathyanarayanan et al., arXiv 2602.03994)\n- StALT (Furuya & Tanimura, arXiv 2605.01853)\n- Concept Walk (Li et al., arXiv 2510.22362, NeurIPS 2025 MechInterp Workshop)\n- Task Difficulty Shapes CoT Faithfulness (ICLR 2026 Workshop)\n- Diagnosing Pathological CoT (Liu et al., arXiv 2602.13904)\n- Measuring Faithfulness Depends on How You Measure (Young, arXiv 2603.20172)\n- MCT / Emergent Manifold Separability (Chun et al., arXiv 2602.20338)\n- Latent Temporal Signals (Vilas et al., ICLR 2026, arXiv 2510.10494)\n- Probing and Steering CoT Unfaithfulness (Occhipinti et al., ICLR 2026 LIT Workshop)\n- Designing and Interpreting Probes (Hewitt & Liang, EMNLP 2019)\n- Information-Theoretic Probing with MDL (Voita & Titov, EMNLP 2020, arXiv 2003.12298)\n- Probing the Probing Paradigm (Ravichander et al., arXiv 2005.00719)\n- Entropy trajectory shapes (arXiv 2603.18940)\n- RQA of Reasoning Dynamics (arXiv 2602.06266)\n- LLM Reasoning as Trajectories (arXiv 2604.05655, Microsoft)\n- Internal States Before Wait (arXiv 2510.04128)\n- FACT-E (Sun et al., ACL Findings 2026, arXiv 2604.10693)\n- Breaking the Chain (Somov et al., arXiv 2603.16475)\n- The Illusion of Reasoning (Basu & Chakraborty, arXiv 2603.22816)\n- FaithCoT-Bench (ICLR 2026, arXiv 2510.04040)\n- The Mirage of Explainability survey (Jin et al., ARR for ACL 2026)\n- Reasoning Theater (Boppana et al., arXiv 2603.05488)\n- No Global Plan in CoT (Xu et al., arXiv 2602.02103)\n- Catching Rationalization in the Act (Mirtaheri & Belkin, arXiv 2603.17199)\n- CoT Monitorability (Anwar et al., arXiv 2602.18297)\n- Understanding CoT via Information Theory (Ton et al., ICML 2025, arXiv 2411.11984)\n- Demystifying Reasoning Dynamics (Qian et al., NeurIPS 2025, arXiv 2506.02867)\n- Analysing CoT Dynamics (Lewis-Lim et al., EMNLP 2025, arXiv 2508.19827)\n- Why Models Know But Don't Say (Young, arXiv 2603.26410)\n- Lie to Me (arXiv 2603.22582)\n- Step-Level Hallucination (Alvarez & Baheri, arXiv 2605.13772)\n- From Reasoning to Answer (arXiv 2509.23676)\n- SAE Reasoning Features (arXiv 2503.18878)\n- FRIT (Swaroop et al., arXiv 2509.13334)\n- Solution Hides in Hidden States (arXiv 2604.23351)\n- Knowing Before Saying (ACL Findings 2025, arXiv 2505.24362)\n- LEACE (Belrose et al., NeurIPS 2023, arXiv 2306.03819)\n- Thought Anchors (arXiv 2506.19143)"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T04:19:16.134Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:19:16.134Z",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb"
}
```

---

## Round 1

63 recorded events

### User

_source line 3 · 2026-05-20T04:19:16.146Z_

# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness

## Description
When a reasoning model gets the right answer, is its chain-of-thought the reason it succeeded — or did it already know the answer and generate decorative reasoning? No existing method can answer this question. Probe-only approaches (Chrabąszcz et al., 2605.18549) reveal what the model knows over time but are structurally blind to whether CoT caused the correct output. Causal-only approaches (TTS, Zhao et al. 2510.24941; NLDD, Ye et al. 2602.11201; Ballon et al. 2601.23163) measure what CoT does but cannot assess what the model already knew internally. Only a dual-stream framework — jointly tracking information availability AND causal contribution — can distinguish faithful-correct from unfaithful-correct reasoning. The Information-Contribution Gap (ICG) framework provides this.

ICG exploits a robust empirical finding: linear probes on hidden states reliably diagnose answer correctness (0.82-0.95 AUROC across four independent groups) yet causal interventions based on these probes consistently fail on reasoning-trained models (Cox et al. 2603.01437: negligible flip rates; Yuan et al. 2605.09502: all four intervention strategies fail). Rather than treating this diagnostic-causal gap as an obstacle, we make it the primary object of study.

The framework tracks two calibrated time-varying quantities across the CoT trajectory: P*(t), null-probe-calibrated correctness awareness, and C(t), causal contribution estimated via three complementary methods (prefix truncation following Ballon et al.'s three control conditions, paraphrase perturbation, NLDD). Their divergence G*(t) = P*(t) − C(t) produces phenomenon-specific temporal fingerprints, operationalizing Wang's (2604.15726) H1/H2 distinction: G*(t) >> 0 is latent-mediated (H1-consistent), G*(t) ≈ 0 is CoT-mediated (H2-consistent).

**Core insight: the diagnostic contribution of G*(t) is its temporal trajectory shape, not its absolute magnitude.** P*(t) (probe AUROC) and C(t) (behavioral accuracy change) are measured via fundamentally different methods with non-commensurable scales. We address this via rank-based normalization as primary scheme, but more fundamentally, trajectory-shape profiles carry the diagnostic signal: a model that pre-encodes the answer shows a constant-high shape; genuine reasoning shows convergence toward zero; post-hoc rationalization shows widening. The shapes-over-magnitudes approach is validated by: entropy trajectory monotonicity predicting reliability regardless of absolute levels (+5.8pp, arXiv 2603.18940); RQA temporal features outperforming aggregates (36.94% vs. 28.97%, arXiv 2602.06266); Microsoft trajectory geometry achieving 0.852 AUC from shape features vs. 0.649 baseline (arXiv 2604.05655).

**Why not just endpoint comparison or trivial combination?** Two reviewer objections are preempted: (1) "Why not correlate pre-CoT probe accuracy with final correctness?" — endpoint comparison detects unfaithfulness presence but collapses distinct failure *mechanisms* (pre-CoT encoding vs. rationalization vs. late shortcutting produce identical endpoints but distinct G*(t) shapes). (2) "Why not just pair Chrabąszcz's probe trajectories with TTS step scores?" — TTS measures *marginal* contribution (removing step *s* changes the answer), while prefix-truncation C(t) measures *cumulative sufficiency* (CoT[:t] is sufficient for correctness). A chain where every individual step has low TTS (each individually replaceable) could still have high cumulative C(t) (the ensemble is necessary). This cumulative-vs-marginal distinction is theoretically non-reducible and empirically grounded in the difference between Ballon et al.'s monotonic prefix curves and TTS's per-step ATE.

**Structural vs. functional differentiation from CMI.** The CMI framework (Sathyanarayanan et al., 2602.03994) measures whether answer representations pass through CoT-aligned layers via layerwise activation patching — a *structural* question. ICG answers a *functional* question: does the CoT text causally contribute to behavioral correctness? This generates a testable prediction: models could show high CMI (representations routed through CoT-processing layers) but high G*(t) (CoT serves as timing scaffold rather than contributing semantic content). If confirmed, this would reveal a novel structural-functional dissociation in reasoning models.

**Differentiation from Thought Anchors.** Thought Anchors (arXiv 2506.19143) measures per-sentence counterfactual importance via replacement sampling — identifying sentences with outsized causal influence on reasoning trajectory. This provides *within-CoT structural analysis* (which sentences matter to each other) but no *external reference* to the model's internal state. A thought anchor could be causally critical within the CoT but entirely redundant relative to what the model already knows — a distinction only ICG can make via the probe dimension.

**Interpretive boundary.** G*(t) >> 0 means correctness-correlated information is present but not causally channeled through CoT. It does not entail the model "decided to withhold" — the information may exist as computational byproducts rather than semantically actionable knowledge. Chun et al.'s MCT geometric pulse finding (2602.20338) provides evidence of this possibility. We report interpretations with this caveat.

**Practical significance: reasoning utilization efficiency.** G*(t) provides a unified diagnostic for reasoning utilization: G*(t) ≈ 0 means full utilization (knowledge channeled through CoT); G*(t) >> 0 means waste (CoT is decorative overhead); G*(t) < 0 means productive computation (CoT assembles new information). This framing connects to three practical domains: (a) *inference-time compute allocation* — skip CoT generation when G*(t) >> 0 for easy problems, providing the principled diagnostic that current early-exit heuristics (ESTAR, DTSR, FRIT, CoDE-Stop) lack; (b) *benchmark validity* — problems where all models show persistent G*(t) >> 0 are not testing reasoning; (c) *safety monitoring* — the decoupled internal quality-monitoring system (Yuan et al.) is the kind of hidden computation alignment researchers worry about.

We adopt honest scoping: 2-3 faithfulness phenomena as the realistic classification target, with steganographic encoding and reasoning theater as stretch goals. The boundary between pre-CoT encoding and post-hoc rationalization may be empirically blurred (in both cases, the model may have committed to an answer before CoT begins, so P*(t) starts high in both), potentially collapsing the taxonomy to 2 primary categories (pre-committed vs. genuinely reasoning). Phase 0b explicitly tests 2-category vs. 3-category separability; either outcome is a strong contribution. Task-difficulty conditioning — grounded in David's easy (0.84) vs. hard (0.76) probe splits and Gjølbye et al.'s (2605.15454) domain-specific difficulty-geometry coupling (ρ⊥ = +0.41 on Codeforces) — reveals the decorative→load-bearing transition with length correction.

Core contributions: (a) calibrated ICG diagnostic with shape-based trajectory analysis on 5 models (4 reasoning + 1 instruction-tuned control) × 4 benchmarks, the first framework capable of distinguishing faithful-correct from unfaithful-correct reasoning; (b) empirical pilot with external validation (TTS cross-reference, difficulty partition, FaithCoT-Bench supplementary) demonstrating 2-3 distinguishable G*(t) phenomenon signatures; (c) difficulty-conditioned gap analysis with domain-specific nuance; (d) head-to-head comparison against TTS, FaithCoT-Bench methods, and probe-only trajectories. Total compute: ~1050 H100-hours.

## Core Problem
A striking convergence of 2025-2026 findings reveals a fundamental disconnect in reasoning language models: their hidden states reliably encode information about answer correctness — linear probes achieving 0.82-0.95 AUROC across multiple independent groups — yet causal interventions based on these probes consistently fail to influence model outputs. Cox et al. (2603.01437) find steering via answer-content probes produces answer flip rates 'negligible against the orthogonal baseline' on reasoning models, despite >0.9 AUC on instruction-tuned models. Yuan et al. (2605.09502) systematically test four interventions (activation steering, probe-guided best-of-N, self-correction, activation patching) on models up to 72B and report ALL fail. This diagnostic-causal gap is NOT an obstacle; it IS the central phenomenon.

The literature conflates two probe targets: answer-content probes (Cox et al.: specific answer on binary tasks, ≤9B + GPT-OSS-20B) and correctness probes (Yuan et al.: right/wrong on models up to 72B; Zhang et al. 2504.05419: per-chunk correctness on 7B-70B). Answer-content gaps mean 'the model has decided but CoT doesn't derive the answer'; correctness gaps mean 'the model knows it's right/wrong but CoT doesn't reflect this awareness.'

Temporal dynamics are empirically grounded: David (2511.14773) finds probe accuracy at 0.84 AUC by token 4, stable ~0.8 through token 100, with easy (0.84) vs. hard (0.76) splits. Zhang et al. (2504.05419) report 65%→79% chunk trajectories on R1-Distill. Esakkiraja et al. (2604.01202) find >90% pre-generation AUROC with characteristic dip at 5-10%. Chrabąszcz et al. (2605.18549) demonstrate 60+ signal-processing features achieving up to 17pp over static probes. Yet no framework jointly tracks information availability AND causal contribution: Chrabąszcz et al. lack any causal component; Ballon et al. (2601.23163) provide behavioral C(t) but no hidden-state measurement; CMI (2602.03994) provides structural layerwise audit on ~50 examples but measures representation routing, not functional text contribution; TTS provides per-step marginal causal contribution but no probe-side measurement and no cumulative sufficiency assessment; Thought Anchors (2506.19143) provide within-CoT causal structure but no external probe reference.

## Opportunity
(1) **Temporal gap measurement.** Multiple groups have independently built the measurement components — probe trajectories (Chrabąszcz: 60+ features, 91-97% AUROC; David: per-token; Zhang: per-chunk; Yuan: 0.95 overall; Esakkiraja: >90% pre-generation) and behavioral causal curves (Ballon: truncation-reinjection; TTS: per-step ATE; NLDD: per-position degradation) — but no one has unified them into a dual-stream temporal gap. Chrabąszcz et al. are structurally blind to the faithful-correct vs. unfaithful-correct distinction; Ballon et al. lack hidden-state measurement. The gap between these traditions IS the framework's niche.

(2) **Phenomenon unification with honest scoping.** CoT faithfulness failures are studied in isolation: Reasoning Horizon (Ye et al. 2602.11201), pre-CoT encoding (Cox et al.; Esakkiraja et al.), Reasoning Theater (Boppana et al. 2603.05488), myopic planning (Xu et al. 2602.02103). We propose 2-3 are distinguishable via G*(t) trajectory shapes, honestly pre-registering that pre-CoT encoding and rationalization may collapse to a single "pre-committed" category.

(3) **Task-difficulty conditioning.** ICLR 2026 Workshop finding, Li et al. (2510.22362): easy→decorative, hard→faithful. Gjølbye et al. (2605.15454): difficulty-geometry coupling domain-specific (ρ⊥ = +0.41 code, +0.05 math). ICG answers: at what difficulty does CoT transition from decorative to load-bearing?

(4) **Probe target clarification.** First principled treatment contrasting correctness awareness gap vs. answer-content gap on applicable tasks.

Two prior works combine probing with causal intervention: Kudo et al. (EACL 2026, 2412.01113) on synthetic arithmetic, and CMI (2602.03994) on ~50 examples — CMI measures *structural mediation* (representation routing through layers) while ICG measures *functional contribution* (whether CoT text causally contributes to behavioral correctness). Wang (2604.15726) formalizes H1/H2/H0 hypotheses; ICG operationalizes the H1/H2 distinction empirically. Neither Kudo et al. nor CMI provides: (a) temporal coverage on natural benchmarks, (b) phenomenon mapping, (c) instance-level diagnostic, (d) multi-model comparison across model families, (e) robustness validation per Young's (2603.20172) classifier-sensitivity finding (kappa as low as 0.06), or (f) empirical pilot with external validation standards.

## Landscape
**Probe-based temporal measurement (P*(t) foundation).** Chrabąszcz et al. (2605.18549): probe trajectories with 60+ signal-processing features (volatility, trend, steady-state, boundary transients, autocorrelation) via 3-layer MLP + Multi-Instance Learning. Max-pooling: 91-97% AUROC harmfulness (vs. 33-61% average-pooling); up to 17pp over static on GSM8K across Llama-8B-R1-Distill and Qwen3-4B/8B/14B (~3000 GPU-hours). Critical: (a) NO causal component, (b) NO gap metric, (c) NO calibration, (d) NO faithfulness-mode taxonomy, (e) NO difficulty conditioning, (f) structurally cannot distinguish faithful-correct from unfaithful-correct. David (2511.14773): 0.84 AUC at t=4, stable ~0.8, easy/hard 0.84/0.76 on Qwen3-8B. Zhang et al. (2504.05419): 0.82-0.91 AUROC on GSM8K/MATH/AIME, 65%→79% trajectory, 24% token reduction via early-exit. Yuan et al. (2605.09502): 0.95 AUROC on Qwen-3B, 0.852 on R1-7B, 0.787 first-step, concealment gap 0.197 AUROC. Esakkiraja et al. (2604.01202): >90% pre-generation, dip at 5-10%, recovery to near-100%. Cox et al. (2603.01437): answer-content probes >0.9 AUC on instruction-tuned Gemma-2/Qwen-2.5, negligible flip on reasoning GPT-OSS-20B. Additional: Qian et al. (2506.02867, NeurIPS 2025); Lewis-Lim et al. (2508.19827, EMNLP 2025); Mirtaheri & Belkin (2603.17199); Occhipinti et al. (ICLR 2026 LIT Workshop).

**Diagnostic-not-causal evidence.** Yuan et al. (2605.09502): four interventions all fail on Qwen2.5 (1.5B-72B), Llama-3.1-8B, Phi-3.5-mini, DeepSeek-R1-7B. 'The error signal is a diagnostic readout, not a causal component that can be edited.' Cox et al. independently confirm. Probe accuracy ≠ causal potency on reasoning models.

**Behavioral C(t) measurement.** Ballon et al. (2601.23163): truncation-reinjection on Qwen3-4B/8B/14B and gpt-oss-20B/120B, decile intervals. Accuracy: 30.8-42.3% → 49.0-73.1% on GPQA-Diamond. Controls validate sequential content (intact +18.1-33.1% vs. shuffled +0.3-10.8%). Disclaims faithfulness analysis. Zhao et al. (2510.24941, TTS): per-step ATE on R1-Distill-Qwen-7B/14B/Llama-8B, only 2.3% AIME steps TTS≥0.7. Ye et al. (2602.11201, NLDD): Reasoning Horizon at 70-85% on synthetic tasks (natural benchmark generalizability unvalidated). Thought Anchors (2506.19143): per-sentence counterfactual importance via 100-rollout replacement sampling; identifies "anchor" sentences steering reasoning trajectory — provides within-CoT causal structure but no probe reference for assessing redundancy relative to internal state. Basu & Chakraborty (2603.22816): decorative/scaffolding/genuine taxonomy. FACT-E (Sun et al. 2604.10693, ACL Findings 2026).

**Probe-intervention combinations.** Kudo et al. (2412.01113, EACL 2026): per-position probes + activation patching on synthetic arithmetic, 9 models. CMI (2602.03994): layerwise activation patching on Phi/Qwen/DialoGPT, ~50 examples. CMI measures *structural mediation* (representation routing); ICG measures *functional contribution* (behavioral text causation). Both complementary precursors on small/synthetic samples.

**Latent-reasoning theory.** Wang (2604.15726): H1/H2/H0 hypotheses with compute-audited designs. ICG operationalizes H1/H2 distinction.

**Temporal hidden-state dynamics.** Gjølbye et al. (2605.15454): 11 models, 3 domains, length correction. ρ⊥^D = +0.41 Codeforces vs. −0.06 baselines; weaker on MATH (+0.05). Prompt-stage probes don't mirror generation-time dynamics. Furuya & Tanimura (2605.01853, StALT). Herrmann et al. (2605.09159): internal polylogue dynamics. Li et al. (2510.22362, NeurIPS 2025 MechInterp Workshop, Concept Walk): easy→decorative, hard→faithful. Vilas et al. (2510.10494, ICLR 2026): 14-70% token savings.

**Probe calibration.** Hewitt & Liang (EMNLP 2019): 4.5 selectivity. Ravichander et al. (2005.00719): properties recoverable when unused. Voita & Titov (EMNLP 2020, 2003.12298): MDL probing. Chun et al. (2602.20338, MCT): geometric pulse — separability peaks transiently while probe accuracy persists. Validates null-probe calibration need.

**Trajectory-shape analysis.** Entropy trajectories (2603.18940): +5.8pp from monotonicity. RQA (2602.06266): temporal 36.94% vs. aggregates 28.97%. Microsoft (2604.05655): 0.852 vs. 0.649 AUC.

**Measurement sensitivity.** Young (2603.20172): kappa as low as 0.06, up to 30.6pp divergence. Young (2603.26410). 'Lie to Me' (2603.22582).

**Additional.** Internal States Before Wait (2510.04128). From Reasoning to Answer (2509.23676). FaithCoT-Bench (ICLR 2026, 2510.04040): 1000+ expert-annotated trajectories, 11 methods, 4 paradigms. Jin et al. survey (ARR for ACL 2026). Liu et al. (2602.13904). Reasoning Theater (2603.05488). Early-exit: ESTAR, DTSR, NEAT, CoDE-Stop, FRIT (Swaroop et al., 2509.13334). Breaking the Chain (Somov et al., 2603.16475). Step-Level Hallucination (Alvarez & Baheri, 2605.13772). SAE Reasoning Features (2503.18878). Solution Hides in Hidden States (2604.23351). Knowing Before Saying (ACL Findings 2025, 2505.24362). LEACE (Belrose et al., NeurIPS 2023, 2306.03819). CoT Monitorability (Anwar et al., 2602.18297). Understanding CoT via Information Theory (Ton et al., ICML 2025, 2411.11984).

**What remains open.** No framework provides: (1) dual-stream temporal gap enabling faithful-vs-unfaithful discrimination for correct instances; (2) empirically-validated phenomenon taxonomy with external validation; (3) instance-level diagnostic from temporal gap; (4) difficulty-conditioned gap with domain nuance; (5) head-to-head comparison against existing causal faithfulness methods; (6) instruction-tuned vs. reasoning model control comparison within the same framework.

## Approach
**Formal Framework.** Two time-varying quantities at equally-spaced positions (primary: 20-50 percentile-based positions; token-level supplementary on subsets):

(i) *P*(t)*: Cross-validated AUROC of linear probe on layer-l hidden states, calibrated via null-probe (P*(t) = P(t) − P_null(t), Hewitt & Liang 2019). Shared probe evaluated at each position (following Chrabąszcz's per-token evaluation, avoiding per-position training). **Target: correctness (right/wrong)** — broader applicability than answer-content probes, directly tied to the diagnostic-not-causal finding (Yuan et al.), more interpretable for faithfulness. Supplementary answer-content probes on binary/MC subsets. Probed at layers L/4, L/2, 3L/4, L. MCT (Chun et al. 2602.20338) supplementary concordance on 500 examples: if MCT capacity diverges from P*(t), identifies positions where probe signal may reflect retrievability rather than geometrically organized information.

(ii) *C(t)*: Three estimators aggregated into C_agg(t): (a) **Prefix truncation** — Ballon et al.'s (2601.23163) protocol with three controls (random, swapped, shuffled tokens), measuring P(correct | CoT[:t]) vs. P(correct | full CoT). This measures *cumulative sufficiency* — whether CoT up to position t is sufficient for correctness — which is theoretically distinct from per-step *marginal contribution* (TTS); (b) **Paraphrase perturbation** — sentence-level segments paraphrased by external model (Claude Haiku or GPT-4o-mini for cost efficiency), 2-3 variants per segment, NLI-based semantic preservation verification. Answer stability: P(same answer | paraphrased CoT). Protocol follows FaithCoT-Bench (ICLR 2026) paraphrasing paradigm. Applied to stratified subset (~40% of examples per cell) for cost control, with full prefix truncation on all examples; (c) **NLDD** (Ye et al. 2602.11201, conditional on Phase 0a feasibility) — logit degradation under corruption. Sentence-level segmentation aligned with TTS approach (Zhao et al.). Multiple estimators provide robustness per Young's (2603.20172) classifier-sensitivity finding.

**C(t) Aggregation and Gap Normalization.** Primary: rank-based normalization — each estimator converted to instance-level percentile ranks within model-benchmark cell, then combined. If NLDD underperforms on specific benchmarks (Phase 0a), two-estimator C_agg(t) (prefix + paraphrase) is primary for those benchmarks; three-estimator as supplementary. Ablation reports: (a) per-estimator G*(t) for phenomenon classification; (b) inverse-variance weighting vs. equal-weight; (c) pairwise Spearman correlation and Cohen's kappa between estimators. Diagnostic value lies in trajectory shapes, not magnitudes, so normalization affects scale but not shape-based signatures.

**G*(t) = P*(t) − C(t).** Primary signal:
- G*(t) ≈ 0: Aligned (necessary for faithfulness; H2-consistent per Wang 2604.15726)
- G*(t) >> 0: Diagnostic excess — 'knows but doesn't use' (H1-consistent)
- G*(t) < 0: Information assembled during reasoning

**Interpretive caveat.** G*(t) >> 0 indicates correctness-correlated information not causally channeled through CoT, but does not entail intentional withholding — some signals may be computational byproducts rather than actionable knowledge. MCT concordance provides partial validation of this boundary.

**Phenomenon Predictions (honestly scoped).**
*Primary (HIGH confidence):*
(i) *Pre-committed reasoning* (encompasses pre-CoT encoding and potentially post-hoc rationalization): G*(t) starts high, stays high or widens. P*(t) high from start (David: 0.84 at t=4; Esakkiraja: >90% pre-generation; Cox: >0.9 pre-CoT), C(t) low or flat.
(ii) *Genuine multi-step reasoning*: G*(t) converges toward zero. P*(t) rises gradually, C(t) tracks P*(t). Zhang et al.'s 65%→79%, Li et al.'s hard→faithful, Ballon et al.'s monotonic accuracy increase.

*Secondary (MODERATE confidence — Phase 0b tests whether separable from pre-committed):*
(iii) *Post-hoc rationalization as distinct from pre-CoT encoding*: If distinguishable, the separation should manifest primarily in C(t) dynamics (rationalization may show spurious partial C(t) increases as the model crafts locally-consistent reasoning, while pre-CoT encoding shows flat-zero C(t)) rather than P*(t). Phase 0b explicitly tests 2-category vs. 3-category separability; 2-category (pre-committed vs. genuine) is pre-registered as an acceptable outcome.

*Stretch (require additional features):*
(iv) *Steganographic encoding*: Dip-and-recovery, consistent with Esakkiraja's 5-10% dip.
(v) *Reasoning Theater*: May overlap with pre-committed. Chrabąszcz-style features may enable separation. Reported with confusion matrices.

**Semi-Synthetic Simulation (hypothesis generation, NOT validation).** Constructed from published data (David, Zhang, Esakkiraja, Yuan for probes; NLDD, TTS for causal; Chun et al. MCT for inflation). Real validation in Phase 0b.

**Phase 0a: Gap Characterization + NLDD Feasibility (Weeks 1-2.5).** 500 examples × 3 datasets (GSM8K, MATH-500, MMLU) × 3 models (DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct):
(i) Construct P*(t) and C(t) curves at 20-50 position resolution
(ii) Validate null-probe calibration
(iii) Characterize causal potency (Cox et al. protocol: steering on reasoning vs. instruction-tuned)
(iv) **NLDD feasibility**: 7B × 100 examples on GSM8K (clear steps) + MMLU (ambiguous steps). If SNR uninformative on MMLU, restrict NLDD to math/code or replace with TTS-style perturbation. Cost: <10 GPU-hrs; gates 250+ hrs NLDD investment.

**Phase 0b: Empirical Pilot (Weeks 2.5-4).** R1-Distill-Qwen-7B × GSM8K + MATH-500, 1000 examples.

*Primary validation (external standards):*
(i) **Difficulty-only partition**: model-independent difficulty bins (easy/medium/hard), no P*/C features used. Test G*(t) shape differences: d > 0.5 AND p < 0.01 (Bonferroni-corrected) on 2+ trajectory features.
(ii) **TTS cross-reference** (primary external validation): compute Zhao et al.'s TTS on same examples; test whether high-TTS (genuine reasoning) vs. low-TTS (decorative) produce distinguishable G*(t) shapes.
(iii) **2-category vs. 3-category test**: explicitly test whether pre-CoT encoding and post-hoc rationalization are separable or collapse to single "pre-committed" category.
(iv) **FaithCoT-Bench** (supplementary): if instance-level overlap available, test correlation with expert labels; otherwise dataset-level validation.

*Supplementary*: P*/C-based partition as self-consistency check.
Length correction per Gjølbye et al. (2605.15454). Success: d > 0.5 between 2+ externally-defined partitions. If d < 0.3, downscope to characterization paper.

**Phase 1: Full ICG (Weeks 4-9).** Conditional on Phase 0b d > 0.5. **5 models**: DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Llama-8B, DeepSeek-R1-Distill-Qwen-14B, QwQ-32B (reasoning models spanning 2 architecture families) + Qwen2.5-7B-Instruct (instruction-tuned control — expected G*(t) ≈ 0 as sanity check). **4 benchmarks**: GSM8K (500 examples), MATH-500 (500), GPQA-Diamond (~198 full), AIME (~90 full). Per-cell: ~1288 examples × 5 models. Full calibrated P*(t) + MCT supplementary + three C(t) estimators (NLDD conditional, paraphrase on ~40% stratified subset) + Ballon-style controls. Cross-reference with TTS at step boundaries. Bootstrap 95% CI on G*(t). ~250 H100-hours.

**Phase 2: Difficulty Conditioning (Weeks 7-11).** Difficulty quintiles per benchmark. G*(t) per quintile. Expected: easy → persistent gap, hard → converging gap. Length correction; domain-specific reporting (stronger on math/code per Gjølbye et al.'s ρ⊥ = +0.41 code vs. +0.05 math).

**Phase 3: Classification, Baselines, Robustness (Weeks 9-14).**

*Classification framework:* G*(t) features (initial value, slope, convergence rate, dC/dt locality) + Chrabąszcz-style features (volatility, trend, boundary transients, autocorrelation). Classifier gradient: logistic regression → RF → MLP; report all. Metric: macro-F1 (primary) + confusion matrix + reliability diagram. Validation: 5-fold + cross-model (train A → test B, reporting within-family vs. cross-family separately) + cross-benchmark generalization. Paired permutation tests with Bonferroni correction for all head-to-head comparisons.

*Baselines:* (a) Random + majority-class; (b) Difficulty-only classifier; (c) **Probe-trajectory-only** (Chrabąszcz-style P*(t) features, no C(t)) — "no causal dimension" ablation; (d) **TTS-only** — per-step marginal causal contribution without probe dimension.

*Head-to-head TIF validation:* TIF score vs. FaithCoT-Bench detection methods (Adding Mistakes, Removing Steps, Early Answering, Paraphrasing) and TTS on overlapping examples, comparing instance-level correlation with ground truth.

*Robustness ablations (7 dimensions):* (a) probe architecture (linear vs. 2-layer MLP); (b) layer selection; (c) C(t) estimator agreement + per-estimator performance + weighting schemes; (d) gap normalization (rank vs. min-max vs. z-score); (e) calibration method (shuffled-label vs. random-representation); (f) probe target (correctness vs. answer-content); (g) **temporal resolution** (5/10/20/35/50 positions + token-level — reporting resolution vs. macro-F1 curve and saturation point).

**TIF Score.** Normalized area under calibrated G*(t), benchmarked against FaithCoT-Bench and Liu et al.'s (2602.13904) text-level metrics.

**Paper Focus.** Core contributions: (1) ICG diagnostic — first framework distinguishing faithful-correct from unfaithful-correct reasoning via dual-stream temporal gap, with instruction-tuned control validating the framework; (2) Phase 0b pilot with external validation demonstrating 2-3 distinguishable G*(t) signatures (or honestly reporting 2-category outcome); (3) difficulty-conditioned gap revealing decorative→load-bearing transition; (4) head-to-head showing ICG's value over probe-only, TTS-only, and FaithCoT-Bench methods. Supporting: 7-dimension ablations; TIF validation. Supplementary: 671B subset (500 examples, 3 layers); answer-content vs. correctness comparison; semi-synthetic simulation; CMI structural-functional prediction if resources allow.

**Experiments.** DeepSeek-R1-Distill-Qwen-7B/14B, DeepSeek-R1-Distill-Llama-8B, QwQ-32B, Qwen2.5-7B-Instruct across GSM8K, MATH-500, GPQA-Diamond, AIME. 671B validation (500-example subset). Calibration: synthetic arithmetic (G* ≈ 0 expected), TTS cross-reference, MCT supplementary. Gjølbye-style length correction throughout.

## Resource Estimate
{'manual': {'gpu_hours': '~1050 H100-hours (Phase 0a: 90 hrs [3 models × 3 datasets + NLDD feasibility]; Phase 0b: 30 hrs [pilot]; Phase 1: 250 hrs [5 models × 4 benchmarks, probes + 3 C(t) estimators + controls]; Phase 2: 50 hrs [difficulty conditioning]; Phase 3: 70 hrs [classification + 7-dim ablations + baselines]; NLDD 32B conditional: 250 hrs [primary bottleneck]; NLDD 7B/14B: 100 hrs; MCT supplementary: 50 hrs; 671B subset: 50 hrs [8×H100]; semi-synthetic: 30 hrs; paraphrase model: ~80 hrs inference on target models for stability checks)', 'paraphrase_api_cost': '~$800-1500 (Claude Haiku/GPT-4o-mini on stratified ~40% subset, 2-3 variants)', 'timeline': '15-17 weeks (2 researchers)', 'estimated_gpu_cost': '$3,200 at ~$3/H100-hour', 'storage': '3-5 TB (4 layers, fp16); ~1.5 TB with PCA/on-the-fly'}, 'human_in_loop': {'gpu_hours': '~1050 H100-hours', 'timeline': '14 weeks (1 researcher + Claude)', 'claude_api_cost': '$500 (experiment design) + $800-1500 (paraphrase generation)', 'estimated_gpu_cost': '$3,200'}, 'auto_research': {'gpu_hours': '~1050 H100-hours', 'timeline': '12 weeks', 'claude_api_cost': '$900 + $800-1500 (paraphrase)', 'estimated_gpu_cost': '$3,200', 'speed_bottleneck': 'NLDD on 32B (~250 hrs, conditional on Phase 0a) is primary bottleneck. Phase 0b pilot (30 hrs) provides early go/no-go.'}}

## Inspired By
The convergence of five independent lines of evidence — (a) Cox et al.'s steering failure on reasoning models despite high probe accuracy; (b) Yuan et al.'s four-intervention failure establishing 'diagnostic not causal'; (c) temporal probe dynamics (David, Zhang, Esakkiraja, Chrabąszcz: 60+ features, up to 17pp improvement); (d) Ballon et al.'s truncation-reinjection demonstrating monotonic behavioral C(t) with controls; (e) trajectory-shape literature (arXiv 2603.18940, 2602.06266, 2604.05655) showing shapes carry diagnostic information — all pointing to: the gap between diagnostic availability and causal contribution IS the phenomenon, and its temporal shape reveals the mechanism. Additionally: Wang's (2604.15726) H1/H2/H0; Gjølbye et al.'s (2605.15454) domain-specific coupling; Chun et al.'s (2602.20338) MCT geometric pulse; CMI's (2602.03994) structural mediation; Thought Anchors' (2506.19143) within-CoT causal structure.

## Target Venues
- ICLR 2027 (abstract: Sep 19, full paper: Sep 24, 2026; primary target)
- ICML 2027 (full paper: Jan 29, 2027; fallback)

## Key References
- Monitoring the Internal Monologue: Probe Trajectories (Chrabąszcz et al., arXiv 2605.18549)
- Probing the Trajectories of Reasoning Traces (Ballon et al., arXiv 2601.23163)
- LLM Reasoning Is Latent (Wang, arXiv 2604.15726)
- Reasoning Models Move Differently (Gjølbye et al., arXiv 2605.15454)
- Hidden Error Awareness (Yuan et al., arXiv 2605.09502)
- Decoding Answers Before CoT (Cox et al., arXiv 2603.01437)
- Temporal Predictors of Outcome (David, arXiv 2511.14773)
- Reasoning Models Know When They're Right (Zhang et al., arXiv 2504.05419)
- Therefore I am. I Think (Esakkiraja et al., arXiv 2604.01202)
- True Thinking Score (Zhao et al., arXiv 2510.24941)
- Mechanistic Evidence for Faithfulness Decay / NLDD (Ye et al., arXiv 2602.11201)
- Internal Polylogue (Herrmann et al., arXiv 2605.09159)
- Faithfully Compute Answers During CoT (Kudo et al., EACL 2026, arXiv 2412.01113)
- Causal Bypass / CMI (Sathyanarayanan et al., arXiv 2602.03994)
- StALT (Furuya & Tanimura, arXiv 2605.01853)
- Concept Walk (Li et al., arXiv 2510.22362, NeurIPS 2025 MechInterp Workshop)
- Task Difficulty Shapes CoT Faithfulness (ICLR 2026 Workshop)
- Diagnosing Pathological CoT (Liu et al., arXiv 2602.13904)
- Measuring Faithfulness Depends on How You Measure (Young, arXiv 2603.20172)
- MCT / Emergent Manifold Separability (Chun et al., arXiv 2602.20338)
- Latent Temporal Signals (Vilas et al., ICLR 2026, arXiv 2510.10494)
- Probing and Steering CoT Unfaithfulness (Occhipinti et al., ICLR 2026 LIT Workshop)
- Designing and Interpreting Probes (Hewitt & Liang, EMNLP 2019)
- Information-Theoretic Probing with MDL (Voita & Titov, EMNLP 2020, arXiv 2003.12298)
- Probing the Probing Paradigm (Ravichander et al., arXiv 2005.00719)
- Entropy trajectory shapes (arXiv 2603.18940)
- RQA of Reasoning Dynamics (arXiv 2602.06266)
- LLM Reasoning as Trajectories (arXiv 2604.05655, Microsoft)
- Internal States Before Wait (arXiv 2510.04128)
- FACT-E (Sun et al., ACL Findings 2026, arXiv 2604.10693)
- Breaking the Chain (Somov et al., arXiv 2603.16475)
- The Illusion of Reasoning (Basu & Chakraborty, arXiv 2603.22816)
- FaithCoT-Bench (ICLR 2026, arXiv 2510.04040)
- The Mirage of Explainability survey (Jin et al., ARR for ACL 2026)
- Reasoning Theater (Boppana et al., arXiv 2603.05488)
- No Global Plan in CoT (Xu et al., arXiv 2602.02103)
- Catching Rationalization in the Act (Mirtaheri & Belkin, arXiv 2603.17199)
- CoT Monitorability (Anwar et al., arXiv 2602.18297)
- Understanding CoT via Information Theory (Ton et al., ICML 2025, arXiv 2411.11984)
- Demystifying Reasoning Dynamics (Qian et al., NeurIPS 2025, arXiv 2506.02867)
- Analysing CoT Dynamics (Lewis-Lim et al., EMNLP 2025, arXiv 2508.19827)
- Why Models Know But Don't Say (Young, arXiv 2603.26410)
- Lie to Me (arXiv 2603.22582)
- Step-Level Hallucination (Alvarez & Baheri, arXiv 2605.13772)
- From Reasoning to Answer (arXiv 2509.23676)
- SAE Reasoning Features (arXiv 2503.18878)
- FRIT (Swaroop et al., arXiv 2509.13334)
- Solution Hides in Hidden States (arXiv 2604.23351)
- Knowing Before Saying (ACL Findings 2025, arXiv 2505.24362)
- LEACE (Belrose et al., NeurIPS 2023, arXiv 2306.03819)
- Thought Anchors (arXiv 2506.19143)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "cf291cc7-d8bd-4cfb-9677-4b45d023f341",
  "type": "user",
  "uuid": "77d32165-8861-49f8-8cd1-7ba9eb7c8b59",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:19:16.144Z_

```json
{
  "parentUuid": "77d32165-8861-49f8-8cd1-7ba9eb7c8b59",
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
  "uuid": "df859e7d-fe31-4a1e-b1e3-044e47eac5b5",
  "timestamp": "2026-05-20T04:19:16.144Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:19:16.144Z_

```json
{
  "parentUuid": "df859e7d-fe31-4a1e-b1e3-044e47eac5b5",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e175df5f-eb90-4b52-a548-3507f09690b6",
  "timestamp": "2026-05-20T04:19:16.144Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
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
  "lastPrompt": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness  ## Description When a reasoning model gets the right answer, is i…",
  "leafUuid": "e175df5f-eb90-4b52-a548-3507f09690b6",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Information-Contribution Gap for CoT faithfulness",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb"
}
```

---

### Assistant

_source line 8 · 2026-05-20T04:19:34.237Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze this proposal as the 补救 agent (remediation agent), focusing exclusively on experimental design and technical execution completeness. I need to:

1. First, do thorough web searches to understand the current experimental standards in this field
2. Then evaluate: baseline coverage, experimental design, evaluation metrics, ablation design, and feasibility

Let me start by reading the proposal carefully and then conducting targeted web searches.

The proposal is about "Information-Contribution Gap (ICG)" - a framework that jointly tracks probe-based information availability P*(t) and causal contribution C(t) across CoT trajectories to distinguish faithful from unfaithful reasoning in LLMs.


Now I'm examining the experimental setup: they're testing across 5 models including reasoning-focused and instruction-tuned variants on four challenging benchmarks, measuring information availability through probes and causal contribution through multiple perturbation methods, comparing against several baselines and running seven ablation studies with substantial computational requirements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e175df5f-eb90-4b52-a548-3507f09690b6",
  "isSidechain": false,
  "requestId": "req_011CbDBG9Q91TjhtU9jAoRb6",
  "type": "assistant",
  "uuid": "cbda70b2-8c91-4ab5-95e2-beed4de08fa8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtP6SzvZVtUWg6NTcqbo5u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12105,
      "cache_read_input_tokens": 14448,
      "output_tokens": 413,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12105,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 413,
          "cache_read_input_tokens": 14448,
          "cache_creation_input_tokens": 12105,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12105
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

_source line 9 · 2026-05-20T04:19:34.244Z_

I'll start by reading the proposal carefully and then conducting targeted web searches to understand the current experimental standards in CoT faithfulness research before giving any recommendations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbda70b2-8c91-4ab5-95e2-beed4de08fa8",
  "isSidechain": false,
  "requestId": "req_011CbDBG9Q91TjhtU9jAoRb6",
  "type": "assistant",
  "uuid": "5d377b38-389d-414c-9b1b-4a14d647f663",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtP6SzvZVtUWg6NTcqbo5u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12105,
      "cache_read_input_tokens": 14448,
      "output_tokens": 413,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12105,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 413,
          "cache_read_input_tokens": 14448,
          "cache_creation_input_tokens": 12105,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12105
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

_source line 10 · 2026-05-20T04:19:34.248Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BQBRVEdoBM6wmAQRxJd86m`</summary>

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
  "parentUuid": "5d377b38-389d-414c-9b1b-4a14d647f663",
  "isSidechain": false,
  "requestId": "req_011CbDBG9Q91TjhtU9jAoRb6",
  "type": "assistant",
  "uuid": "c088a74d-ad64-4a46-b43a-b0dc918bb5fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtP6SzvZVtUWg6NTcqbo5u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12105,
      "cache_read_input_tokens": 14448,
      "output_tokens": 413,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12105,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 413,
          "cache_read_input_tokens": 14448,
          "cache_creation_input_tokens": 12105,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12105
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

_source line 11 · 2026-05-20T04:19:34.255Z_

<details><summary>↩ Tool result · `toolu_01BQBRVEdoBM6wmAQRxJd86m`</summary>

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
  "parentUuid": "c088a74d-ad64-4a46-b43a-b0dc918bb5fa",
  "isSidechain": false,
  "promptId": "cf291cc7-d8bd-4cfb-9677-4b45d023f341",
  "type": "user",
  "uuid": "02011632-d8d4-4352-b892-487cda0a6bc9",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "c088a74d-ad64-4a46-b43a-b0dc918bb5fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T04:19:37.459Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me conduct targeted web searches to understand the experimental standards in CoT faithfulness research. I'll search for several things in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02011632-d8d4-4352-b892-487cda0a6bc9",
  "isSidechain": false,
  "requestId": "req_011CbDBHUtSE9ykTXifCGdh9",
  "type": "assistant",
  "uuid": "f2870cf4-a137-44c1-a9d7-0084e8a9d271",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017DAgmGxLosYtcaMhd97Hx1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 939,
      "cache_read_input_tokens": 26553,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 939,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 137,
          "cache_read_input_tokens": 26553,
          "cache_creation_input_tokens": 939,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 939
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

_source line 13 · 2026-05-20T04:19:37.899Z_

Let me conduct the necessary pre-research searches to understand current experimental standards in CoT faithfulness measurement.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2870cf4-a137-44c1-a9d7-0084e8a9d271",
  "isSidechain": false,
  "requestId": "req_011CbDBHUtSE9ykTXifCGdh9",
  "type": "assistant",
  "uuid": "4087906a-ee79-4ece-a71c-2df26714914c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017DAgmGxLosYtcaMhd97Hx1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 939,
      "cache_read_input_tokens": 26553,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 939,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 137,
          "cache_read_input_tokens": 26553,
          "cache_creation_input_tokens": 939,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 939
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

_source line 14 · 2026-05-20T04:19:38.248Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SVmDUHjZspC6QM6x3qC636`</summary>

```json
{
  "query": "CoT faithfulness measurement experiments baselines 2025 2026 probe trajectory causal intervention"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4087906a-ee79-4ece-a71c-2df26714914c",
  "isSidechain": false,
  "requestId": "req_011CbDBHUtSE9ykTXifCGdh9",
  "type": "assistant",
  "uuid": "782a1b74-cd37-4895-add7-53ae2a8777ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017DAgmGxLosYtcaMhd97Hx1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 939,
      "cache_read_input_tokens": 26553,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 939,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 137,
          "cache_read_input_tokens": 26553,
          "cache_creation_input_tokens": 939,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 939
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

_source line 15 · 2026-05-20T04:19:47.449Z_

<details><summary>↩ Tool result · `toolu_01SVmDUHjZspC6QM6x3qC636`</summary>

```text
Web search results for query: "CoT faithfulness measurement experiments baselines 2025 2026 probe trajectory causal intervention"

Links: [{"title":"Automated Interpretability-Driven Model Auditing and Control: A Research Agenda","url":"https://aigi.ox.ac.uk/wp-content/uploads/2026/01/Automated_interp_Research_Agenda.pdf"},{"title":"Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING","url":"https://arxiv.org/pdf/2510.04040"},{"title":"FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2510.04040v1"},{"title":"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2602.11201v1"},{"title":"GitHub - PKU-PILLAR-Group/CoT-Faithfulness-Survey: Paper list for our paper \"The Mirage of Explainability: A Survey on Chain-of-Thought Faithfulness in Large Language Models\". · GitHub","url":"https://github.com/PKU-PILLAR-Group/CoT-Faithfulness-Survey"},{"title":"Measuring Chain-of-Thought Monitorability Through Faithfulness and Verbosity","url":"https://arxiv.org/pdf/2510.27378"},{"title":"Bypassing the Rationale: Causal Auditing of Implicit Reasoning in Language Models","url":"https://arxiv.org/pdf/2602.03994"},{"title":"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps","url":"https://aclanthology.org/2025.emnlp-main.504.pdf"},{"title":"Preprint. Counterfactual Simulation Training for Chain-of-Thought Faithfulness","url":"https://arxiv.org/pdf/2602.20710"}]

Based on the search results, here's what I found regarding CoT (Chain-of-Thought) faithfulness measurement experiments, baselines, and related methodologies from 2025-2026:

## Key Findings on CoT Faithfulness

### Main Problem
CoT is argued to not be explainability, as verbalized reasoning often diverges from internal computation, and models can produce compelling reasoning chains that don't causally influence their answers.

### Measurement Methodologies

**Four Main Evaluation Paradigms:**

1. **Baselines**: A random classifier defines the lower bound, while perplexity-based scoring uses sentence fluency as a proxy.

2. **Counterfactual-based Methods**: These approach probe CoT faithfulness by perturbing reasoning traces, for example by adding mistakes, removing steps, or forcing early answers, and then testing whether the final prediction changes accordingly.

3. **Logit-based Methods**: These leverage model-internal diagnostics, such as analyzing logit variations or measuring information gain to approximate causal alignment between CoTs and outputs.

4. **LLM-as-Judge Methods**: These rely on stronger language models to directly evaluate the quality of reasoning traces, using carefully designed prompts to assess whether a CoT reflects genuine reasoning.

### Causal Intervention Approaches

Tools such as Query Circuits are used to identify which components generate the reasoning trace versus which produce the final answer. Representational Similarity Analysis is employed to measure alignment between clean and counterfactually corrupted reasoning trajectories, coupled with linear probes to track the evolution of solution-relevant information across layers.

### Recent Benchmarks
Level-II intervention-grounded benchmarks (e.g., FaithCoT-Bench) and Level-III structured-verifiable approaches (e.g., Typed CoT) are accelerating progress.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "782a1b74-cd37-4895-add7-53ae2a8777ee",
  "isSidechain": false,
  "promptId": "cf291cc7-d8bd-4cfb-9677-4b45d023f341",
  "type": "user",
  "uuid": "372d737b-c578-4314-afd1-fbd1c254d098",
  "toolUseResult": {
    "query": "CoT faithfulness measurement experiments baselines 2025 2026 probe trajectory causal intervention",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AsrmnqNpEPfovz5QRXfawJ",
        "content": [
          {
            "title": "Automated Interpretability-Driven Model Auditing and Control: A Research Agenda",
            "url": "https://aigi.ox.ac.uk/wp-content/uploads/2026/01/Automated_interp_Research_Agenda.pdf"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING",
            "url": "https://arxiv.org/pdf/2510.04040"
          },
          {
            "title": "FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2510.04040v1"
          },
          {
            "title": "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2602.11201v1"
          },
          {
            "title": "GitHub - PKU-PILLAR-Group/CoT-Faithfulness-Survey: Paper list for our paper \"The Mirage of Explainability: A Survey on Chain-of-Thought Faithfulness in Large Language Models\". · GitHub",
            "url": "https://github.com/PKU-PILLAR-Group/CoT-Faithfulness-Survey"
          },
          {
            "title": "Measuring Chain-of-Thought Monitorability Through Faithfulness and Verbosity",
            "url": "https://arxiv.org/pdf/2510.27378"
          },
          {
            "title": "Bypassing the Rationale: Causal Auditing of Implicit Reasoning in Language Models",
            "url": "https://arxiv.org/pdf/2602.03994"
          },
          {
            "title": "Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps",
            "url": "https://aclanthology.org/2025.emnlp-main.504.pdf"
          },
          {
            "title": "Preprint. Counterfactual Simulation Training for Chain-of-Thought Faithfulness",
            "url": "https://arxiv.org/pdf/2602.20710"
          }
        ]
      },
      "Based on the search results, here's what I found regarding CoT (Chain-of-Thought) faithfulness measurement experiments, baselines, and related methodologies from 2025-2026:\n\n## Key Findings on CoT Faithfulness\n\n### Main Problem\nCoT is argued to not be explainability, as verbalized reasoning often diverges from internal computation, and models can produce compelling reasoning chains that don't causally influence their answers.\n\n### Measurement Methodologies\n\n**Four Main Evaluation Paradigms:**\n\n1. **Baselines**: A random classifier defines the lower bound, while perplexity-based scoring uses sentence fluency as a proxy.\n\n2. **Counterfactual-based Methods**: These approach probe CoT faithfulness by perturbing reasoning traces, for example by adding mistakes, removing steps, or forcing early answers, and then testing whether the final prediction changes accordingly.\n\n3. **Logit-based Methods**: These leverage model-internal diagnostics, such as analyzing logit variations or measuring information gain to approximate causal alignment between CoTs and outputs.\n\n4. **LLM-as-Judge Methods**: These rely on stronger language models to directly evaluate the quality of reasoning traces, using carefully designed prompts to assess whether a CoT reflects genuine reasoning.\n\n### Causal Intervention Approaches\n\nTools such as Query Circuits are used to identify which components generate the reasoning trace versus which produce the final answer. Representational Similarity Analysis is employed to measure alignment between clean and counterfactually corrupted reasoning trajectories, coupled with linear probes to track the evolution of solution-relevant information across layers.\n\n### Recent Benchmarks\nLevel-II intervention-grounded benchmarks (e.g., FaithCoT-Bench) and Level-III structured-verifiable approaches (e.g., Typed CoT) are accelerating progress."
    ],
    "durationSeconds": 9.195557710000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "782a1b74-cd37-4895-add7-53ae2a8777ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T04:19:49.551Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019zDLzpxCb2yoP6mwdbR1qw`</summary>

```json
{
  "query": "FaithCoT-Bench ICLR 2026 experimental design baselines evaluation metrics ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "372d737b-c578-4314-afd1-fbd1c254d098",
  "isSidechain": false,
  "requestId": "req_011CbDBJT9HpAFXL7Pj5TmAp",
  "type": "assistant",
  "uuid": "beaf69e2-631b-4f91-a8b2-8a3fd85c7e39",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WNGqMmSg3obLMXudFXjJsv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 27492,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 27492,
          "cache_creation_input_tokens": 1071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1071
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

_source line 17 · 2026-05-20T04:19:57.700Z_

<details><summary>↩ Tool result · `toolu_019zDLzpxCb2yoP6mwdbR1qw`</summary>

```text
Web search results for query: "FaithCoT-Bench ICLR 2026 experimental design baselines evaluation metrics ablation"

Links: [{"title":"Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING","url":"https://arxiv.org/pdf/2510.04040"},{"title":"FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2510.04040v1"},{"title":"SPD-Faith Bench: Diagnosing and Improving Faithfulness in Chain-of-Thought for Multimodal Large Language Models","url":"https://arxiv.org/html/2602.07833v1"},{"title":"FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning | OpenReview","url":"https://openreview.net/forum?id=lN3yKqqzF1"},{"title":"[2510.04040] FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning","url":"https://arxiv.org/abs/2510.04040"},{"title":"Insights from the ICLR Peer Review and Rebuttal Process","url":"https://arxiv.org/pdf/2511.15462"},{"title":"C2-Faith: Benchmarking LLM Judges for Causal and Coverage Faithfulness in Chain-of-Thought Reasoning","url":"https://arxiv.org/pdf/2603.05167"}]

Based on the search results, I found comprehensive information about FaithCoT-Bench from ICLR 2026:

## Overview
FaithCoT-Bench is a unified benchmark for instance-level CoT unfaithfulness detection. It provides FINE-CoT (Faithfulness instance evaluation for Chain-of-Thought), an expert-annotated collection of over 1,000 trajectories generated by four representative LLMs.

## Experimental Design
CoT trajectories were generated using four representative large language models, including two open-source models (LLaMA3.1-8B and Qwen2.5-7B) and two closed-source models (GPT-4o-mini and Gemini 2.5 Flash), chosen to balance accessibility and capability.

## Baselines
The benchmark evaluates eleven methods for CoT faithfulness detection, spanning four paradigms including random classifier baselines and perplexity-based scoring. Additional paradigms include counterfactual-based methods (Adding Mistakes, Option Shuffling, Removing Steps, Early Answering, Paraphrasing), logit-based approaches (Answer Tracing, Information Gain), and LLM-as-Judge methods (Step-Judge, Faithful-Judge).

## Evaluation Metrics
Method performance is assessed using three complementary metrics, including Cohen's kappa. The benchmark provides precise definitions of eight fine-grained signals of unfaithfulness, which fall under two overarching categories of Post-hoc Reasoning and Spurious Reasoning Chains, serving as operational guidelines for human annotators.

## Methodological Quality
All results are reported under standardized evaluation criteria, and baselines have been rigorously cross-checked to ensure fairness and consistency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "beaf69e2-631b-4f91-a8b2-8a3fd85c7e39",
  "isSidechain": false,
  "promptId": "cf291cc7-d8bd-4cfb-9677-4b45d023f341",
  "type": "user",
  "uuid": "672a5325-1378-4e3e-b175-8726a9169f9a",
  "toolUseResult": {
    "query": "FaithCoT-Bench ICLR 2026 experimental design baselines evaluation metrics ablation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NtpytLgPQfV7oie93arQr5",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING",
            "url": "https://arxiv.org/pdf/2510.04040"
          },
          {
            "title": "FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2510.04040v1"
          },
          {
            "title": "SPD-Faith Bench: Diagnosing and Improving Faithfulness in Chain-of-Thought for Multimodal Large Language Models",
            "url": "https://arxiv.org/html/2602.07833v1"
          },
          {
            "title": "FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=lN3yKqqzF1"
          },
          {
            "title": "[2510.04040] FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/abs/2510.04040"
          },
          {
            "title": "Insights from the ICLR Peer Review and Rebuttal Process",
            "url": "https://arxiv.org/pdf/2511.15462"
          },
          {
            "title": "C2-Faith: Benchmarking LLM Judges for Causal and Coverage Faithfulness in Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/pdf/2603.05167"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about FaithCoT-Bench from ICLR 2026:\n\n## Overview\nFaithCoT-Bench is a unified benchmark for instance-level CoT unfaithfulness detection. It provides FINE-CoT (Faithfulness instance evaluation for Chain-of-Thought), an expert-annotated collection of over 1,000 trajectories generated by four representative LLMs.\n\n## Experimental Design\nCoT trajectories were generated using four representative large language models, including two open-source models (LLaMA3.1-8B and Qwen2.5-7B) and two closed-source models (GPT-4o-mini and Gemini 2.5 Flash), chosen to balance accessibility and capability.\n\n## Baselines\nThe benchmark evaluates eleven methods for CoT faithfulness detection, spanning four paradigms including random classifier baselines and perplexity-based scoring. Additional paradigms include counterfactual-based methods (Adding Mistakes, Option Shuffling, Removing Steps, Early Answering, Paraphrasing), logit-based approaches (Answer Tracing, Information Gain), and LLM-as-Judge methods (Step-Judge, Faithful-Judge).\n\n## Evaluation Metrics\nMethod performance is assessed using three complementary metrics, including Cohen's kappa. The benchmark provides precise definitions of eight fine-grained signals of unfaithfulness, which fall under two overarching categories of Post-hoc Reasoning and Spurious Reasoning Chains, serving as operational guidelines for human annotators.\n\n## Methodological Quality\nAll results are reported under standardized evaluation criteria, and baselines have been rigorously cross-checked to ensure fairness and consistency."
    ],
    "durationSeconds": 8.144179992999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "beaf69e2-631b-4f91-a8b2-8a3fd85c7e39",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T04:20:08.457Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S6iTghFb2VXB1f7fySmWHU`</summary>

```json
{
  "query": "Chrabąszcz probe trajectories 2605.18549 experimental setup models benchmarks evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "672a5325-1378-4e3e-b175-8726a9169f9a",
  "isSidechain": false,
  "requestId": "req_011CbDBKCxYH3ZAdVa9kdvdL",
  "type": "assistant",
  "uuid": "d46d3d89-b925-47c2-b5c2-ef5b8edd0917",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnTdiGU9YcQiYHhTi43FUy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 901,
      "cache_read_input_tokens": 28563,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 901,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 28563,
          "cache_creation_input_tokens": 901,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 901
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

_source line 19 · 2026-05-20T04:20:16.340Z_

<details><summary>↩ Tool result · `toolu_01S6iTghFb2VXB1f7fySmWHU`</summary>

```text
Web search results for query: "Chrabąszcz probe trajectories 2605.18549 experimental setup models benchmarks evaluation"

Links: [{"title":"[2605.18549] Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics","url":"https://arxiv.org/abs/2605.18549"},{"title":"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics","url":"https://arxiv.org/html/2605.18549"},{"title":"Experimental setup inside the modified ATS model 2605 ...","url":"https://www.researchgate.net/figure/Experimental-setup-inside-the-modified-ATS-model-2605-pneumatic-creep-tester-where-the_fig1_283670339"},{"title":"Trajectory sampling using spatial familiarity","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11435202"},{"title":"[2605.04352] Probing Structural Mathematical Reasoning in Language Models with Algebraic Trapdoors","url":"https://arxiv.org/abs/2605.04352"},{"title":"Computing Feasible Trajectories for an Articulated Probe in Three   Dimensions","url":"https://arxiv.org/pdf/2011.11685"},{"title":"Characterization and Computation of Feasible Trajectories for an   Articulated Probe with a Variable-Length End Segment","url":"https://arxiv.org/pdf/2011.11672"}]

Based on the search results, I found the paper you're looking for:

The paper is titled "Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics" by Maciej Chrabąszcz and colleagues, introducing research on Large Reasoning Models (LRMs) and safety monitoring through Chain of Thought (CoT) reasoning.

**Key Methodology:**

The researchers construct probe trajectories by evaluating a probe at each generated token, representing the continuous evolution of a concept's probability across the reasoning process.

**Main Findings:**

- Future model behavior is more distinguishable when examined over the full trajectory than from a single static prediction.

- Signal-processing features capturing volatility, trend, and steady-state behavior significantly improve the separation of future model states.

**Experimental Insights:**

- Template-based training data achieves near-parity with dynamically generated model responses, eliminating the need for costly initial inference and labeling.

- The choice of pooling operation is critical: average-pooling and last-token methods collapse to near-random performance, while max-pooling achieves up to 95% AUROC and yields stable probe trajectories.

The paper evaluates these approaches across multiple datasets and reasoning models to benchmark the effectiveness of this probe trajectory approach for monitoring LRM behavior.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d46d3d89-b925-47c2-b5c2-ef5b8edd0917",
  "isSidechain": false,
  "promptId": "cf291cc7-d8bd-4cfb-9677-4b45d023f341",
  "type": "user",
  "uuid": "7d0cf030-cbc7-4231-bad4-9349ffa73b8f",
  "toolUseResult": {
    "query": "Chrabąszcz probe trajectories 2605.18549 experimental setup models benchmarks evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01C2t2ZwY4BjYA2JX2kC6TDM",
        "content": [
          {
            "title": "[2605.18549] Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics",
            "url": "https://arxiv.org/abs/2605.18549"
          },
          {
            "title": "Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics",
            "url": "https://arxiv.org/html/2605.18549"
          },
          {
            "title": "Experimental setup inside the modified ATS model 2605 ...",
            "url": "https://www.researchgate.net/figure/Experimental-setup-inside-the-modified-ATS-model-2605-pneumatic-creep-tester-where-the_fig1_283670339"
          },
          {
            "title": "Trajectory sampling using spatial familiarity",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11435202"
          },
          {
            "title": "[2605.04352] Probing Structural Mathematical Reasoning in Language Models with Algebraic Trapdoors",
            "url": "https://arxiv.org/abs/2605.04352"
          },
          {
            "title": "Computing Feasible Trajectories for an Articulated Probe in Three   Dimensions",
            "url": "https://arxiv.org/pdf/2011.11685"
          },
          {
            "title": "Characterization and Computation of Feasible Trajectories for an   Articulated Probe with a Variable-Length End Segment",
            "url": "https://arxiv.org/pdf/2011.11672"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper is titled \"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics\" by Maciej Chrabąszcz and colleagues, introducing research on Large Reasoning Models (LRMs) and safety monitoring through Chain of Thought (CoT) reasoning.\n\n**Key Methodology:**\n\nThe researchers construct probe trajectories by evaluating a probe at each generated token, representing the continuous evolution of a concept's probability across the reasoning process.\n\n**Main Findings:**\n\n- Future model behavior is more distinguishable when examined over the full trajectory than from a single static prediction.\n\n- Signal-processing features capturing volatility, trend, and steady-state behavior significantly improve the separation of future model states.\n\n**Experimental Insights:**\n\n- Template-based training data achieves near-parity with dynamically generated model responses, eliminating the need for costly initial inference and labeling.\n\n- The choice of pooling operation is critical: average-pooling and last-token methods collapse to near-random performance, while max-pooling achieves up to 95% AUROC and yields stable probe trajectories.\n\nThe paper evaluates these approaches across multiple datasets and reasoning models to benchmark the effectiveness of this probe trajectory approach for monitoring LRM behavior."
    ],
    "durationSeconds": 7.876585072999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d46d3d89-b925-47c2-b5c2-ef5b8edd0917",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness  ## Description When a reasoning model gets the right answer, is i…",
  "leafUuid": "7d0cf030-cbc7-4231-bad4-9349ffa73b8f",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Information-Contribution Gap for CoT faithfulness",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb"
}
```

---

### Tool call

_source line 22 · 2026-05-20T04:20:18.706Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RX7r2ADRhEPcjx8EiEFXRo`</summary>

```json
{
  "query": "True Thinking Score TTS Zhao 2510.24941 experimental design evaluation chain-of-thought faithfulness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d0cf030-cbc7-4231-bad4-9349ffa73b8f",
  "isSidechain": false,
  "requestId": "req_011CbDBLag2XFFSuNRCS4kR8",
  "type": "assistant",
  "uuid": "544e340a-050c-4303-94d7-7628581de1a5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B69mrYfFZ67LtUhxK4hrk4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 772,
      "cache_read_input_tokens": 29464,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 772,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 29464,
          "cache_creation_input_tokens": 772,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 772
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

_source line 23 · 2026-05-20T04:20:26.064Z_

<details><summary>↩ Tool result · `toolu_01RX7r2ADRhEPcjx8EiEFXRo`</summary>

```text
Web search results for query: "True Thinking Score TTS Zhao 2510.24941 experimental design evaluation chain-of-thought faithfulness"

Links: [{"title":"[2510.24941] Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought","url":"https://arxiv.org/abs/2510.24941"},{"title":"Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought","url":"https://arxiv.org/pdf/2510.24941"},{"title":"Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought | OpenReview","url":"https://openreview.net/forum?id=3IaP48VUes"},{"title":"Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought","url":"https://arxiv.org/html/2510.24941"},{"title":"Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?","url":"https://arxiv.org/pdf/2603.22582"},{"title":"Measuring Faithfulness Depends on How You Measure: Classifier Sensitivity in LLM Chain-of-Thought Evaluation","url":"https://arxiv.org/pdf/2603.20172"},{"title":"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning","url":"https://arxiv.org/pdf/2602.11201"}]

Based on the search results, I found detailed information about this research:

## Overview

The paper "Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought" by Jiachen Zhao and colleagues proposes a True Thinking Score (TTS) to quantify the causal contribution of each step in chain-of-thought (CoT) reasoning to a model's final prediction.

## Key Findings

The research shows that LLMs often interleave between true-thinking steps (which are genuinely used to compute the final output) and decorative-thinking steps (which give the appearance of reasoning but have minimal causal influence).

A striking finding is that only a small subset of reasoning steps actually drive the model's prediction—for example, on AIME, only an average of 2.3% of reasoning steps in CoT have a TTS greater than 0.7 (on a 0-1 scale) for Qwen-2.5.

## Experimental Design

The researchers also found that LLMs can be steered to internally follow or disregard specific steps in their verbalized CoT using the identified TrueThinking direction. The results indicate that labeling an entire CoT as either unfaithful post-rationalization or faithful computation is overly coarse, and raise concerns about the reliability of monitoring LLMs by inspecting CoT, since individual steps may not always reflect the model's true internal reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "544e340a-050c-4303-94d7-7628581de1a5",
  "isSidechain": false,
  "promptId": "cf291cc7-d8bd-4cfb-9677-4b45d023f341",
  "type": "user",
  "uuid": "20c656dd-5b73-401f-9d99-d30766cf8620",
  "toolUseResult": {
    "query": "True Thinking Score TTS Zhao 2510.24941 experimental design evaluation chain-of-thought faithfulness",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KW1MRzRY9G8XiptvupiAcL",
        "content": [
          {
            "title": "[2510.24941] Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought",
            "url": "https://arxiv.org/abs/2510.24941"
          },
          {
            "title": "Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought",
            "url": "https://arxiv.org/pdf/2510.24941"
          },
          {
            "title": "Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought | OpenReview",
            "url": "https://openreview.net/forum?id=3IaP48VUes"
          },
          {
            "title": "Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought",
            "url": "https://arxiv.org/html/2510.24941"
          },
          {
            "title": "Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?",
            "url": "https://arxiv.org/pdf/2603.22582"
          },
          {
            "title": "Measuring Faithfulness Depends on How You Measure: Classifier Sensitivity in LLM Chain-of-Thought Evaluation",
            "url": "https://arxiv.org/pdf/2603.20172"
          },
          {
            "title": "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/pdf/2602.11201"
          }
        ]
      },
      "Based on the search results, I found detailed information about this research:\n\n## Overview\n\nThe paper \"Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought\" by Jiachen Zhao and colleagues proposes a True Thinking Score (TTS) to quantify the causal contribution of each step in chain-of-thought (CoT) reasoning to a model's final prediction.\n\n## Key Findings\n\nThe research shows that LLMs often interleave between true-thinking steps (which are genuinely used to compute the final output) and decorative-thinking steps (which give the appearance of reasoning but have minimal causal influence).\n\nA striking finding is that only a small subset of reasoning steps actually drive the model's prediction—for example, on AIME, only an average of 2.3% of reasoning steps in CoT have a TTS greater than 0.7 (on a 0-1 scale) for Qwen-2.5.\n\n## Experimental Design\n\nThe researchers also found that LLMs can be steered to internally follow or disregard specific steps in their verbalized CoT using the identified TrueThinking direction. The results indicate that labeling an entire CoT as either unfaithful post-rationalization or faithful computation is overly coarse, and raise concerns about the reliability of monitoring LLMs by inspecting CoT, since individual steps may not always reflect the model's true internal reasoning."
    ],
    "durationSeconds": 7.353385217000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "544e340a-050c-4303-94d7-7628581de1a5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T04:20:33.913Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lan6YBp43sG2VjqovcSSCz`</summary>

```json
{
  "query": "Yuan hidden error awareness 2605.09502 probe intervention failure reasoning models experiment results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20c656dd-5b73-401f-9d99-d30766cf8620",
  "isSidechain": false,
  "requestId": "req_011CbDBMJDbkoLgefCqS3mwa",
  "type": "assistant",
  "uuid": "67e8e8d0-d571-4abe-be43-bd844a6f0f90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpSK1HcQHQ5yN7LgVX6BHg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 816,
      "cache_read_input_tokens": 30236,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 816,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 30236,
          "cache_creation_input_tokens": 816,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 816
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

_source line 25 · 2026-05-20T04:20:41.222Z_

<details><summary>↩ Tool result · `toolu_01Lan6YBp43sG2VjqovcSSCz`</summary>

```text
Web search results for query: "Yuan hidden error awareness 2605.09502 probe intervention failure reasoning models experiment results"

Links: [{"title":"[2605.09502] Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal","url":"https://arxiv.org/abs/2605.09502"},{"title":"Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal","url":"https://arxiv.org/html/2605.09502"},{"title":"Targeting self-reported and neural error sensitivity: Short- and long-term effects of a one-week online intervention","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12861243/"},{"title":"Probing for Arithmetic Errors in Language Models","url":"https://arxiv.org/pdf/2507.12379"},{"title":"Enterprise Edition Communication Failure | Central-Probe Connection failure - OpManager","url":"https://www.manageengine.com/network-monitoring/help/probe-central-communication-failure.html"},{"title":"Failure area identification system","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11977433"},{"title":"Web Probe Errors - Zscaler Help Portal","url":"https://help.zscaler.com/zdx/web-probe-errors"}]

Based on the search results, here's what I found about the paper 2605.09502:

## Paper Summary

The paper "Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal" by Aojie Yuan and colleagues shows that models internally detect their own reasoning errors but outwardly express confidence in them.

## Key Experiment Results

A linear probe on hidden states predicts trace correctness with 0.95 AUROC—from the very first reasoning step (0.79)—while verbalized confidence for wrong traces is 4.55/5, nearly identical to correct ones (4.87/5). A text-surface classifier achieves only 0.59 on the same data, confirming a 0.20-point gap invisible in the generated text.

## Intervention Failure Results

Four interventions -- activation steering, probe-guided best-of-N, self-correction, and activation patching -- all fail; patching destroys output coherence entirely. The signal is diagnostic, not causal: a readout of computation quality.

## Model Coverage

This hidden error awareness holds across three model families (Qwen, Llama, Phi), 1.5B–72B parameters, and RL-trained reasoning models (DeepSeek-R1, 0.852 AUROC).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67e8e8d0-d571-4abe-be43-bd844a6f0f90",
  "isSidechain": false,
  "promptId": "cf291cc7-d8bd-4cfb-9677-4b45d023f341",
  "type": "user",
  "uuid": "bc9992dd-0b0b-4a80-9433-68e218408218",
  "toolUseResult": {
    "query": "Yuan hidden error awareness 2605.09502 probe intervention failure reasoning models experiment results",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AJ43eKmbP6mFHYgEr9FtXG",
        "content": [
          {
            "title": "[2605.09502] Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal",
            "url": "https://arxiv.org/abs/2605.09502"
          },
          {
            "title": "Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal",
            "url": "https://arxiv.org/html/2605.09502"
          },
          {
            "title": "Targeting self-reported and neural error sensitivity: Short- and long-term effects of a one-week online intervention",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12861243/"
          },
          {
            "title": "Probing for Arithmetic Errors in Language Models",
            "url": "https://arxiv.org/pdf/2507.12379"
          },
          {
            "title": "Enterprise Edition Communication Failure | Central-Probe Connection failure - OpManager",
            "url": "https://www.manageengine.com/network-monitoring/help/probe-central-communication-failure.html"
          },
          {
            "title": "Failure area identification system",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11977433"
          },
          {
            "title": "Web Probe Errors - Zscaler Help Portal",
            "url": "https://help.zscaler.com/zdx/web-probe-errors"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper 2605.09502:\n\n## Paper Summary\n\nThe paper \"Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal\" by Aojie Yuan and colleagues shows that models internally detect their own reasoning errors but outwardly express confidence in them.\n\n## Key Experiment Results\n\nA linear probe on hidden states predicts trace correctness with 0.95 AUROC—from the very first reasoning step (0.79)—while verbalized confidence for wrong traces is 4.55/5, nearly identical to correct ones (4.87/5). A text-surface classifier achieves only 0.59 on the same data, confirming a 0.20-point gap invisible in the generated text.\n\n## Intervention Failure Results\n\nFour interventions -- activation steering, probe-guided best-of-N, self-correction, and activation patching -- all fail; patching destroys output coherence entirely. The signal is diagnostic, not causal: a readout of computation quality.\n\n## Model Coverage\n\nThis hidden error awareness holds across three model families (Qwen, Llama, Phi), 1.5B–72B parameters, and RL-trained reasoning models (DeepSeek-R1, 0.852 AUROC)."
    ],
    "durationSeconds": 7.304570265999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "67e8e8d0-d571-4abe-be43-bd844a6f0f90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T04:20:43.576Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A9NGeB1jgnMxjpT3SUyecB`</summary>

```json
{
  "query": "Ballon probing trajectories reasoning traces 2601.23163 truncation reinjection protocol experimental setup controls"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc9992dd-0b0b-4a80-9433-68e218408218",
  "isSidechain": false,
  "requestId": "req_011CbDBNR2eii1R29W4puuVF",
  "type": "assistant",
  "uuid": "af724288-5b3d-45fa-bf86-583fa217aac6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CNxF5nPn2Gw4ejtow6EzFp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 31052,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 31052,
          "cache_creation_input_tokens": 746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 746
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

_source line 27 · 2026-05-20T04:20:49.796Z_

<details><summary>↩ Tool result · `toolu_01A9NGeB1jgnMxjpT3SUyecB`</summary>

```text
Web search results for query: "Ballon probing trajectories reasoning traces 2601.23163 truncation reinjection protocol experimental setup controls"

Links: [{"title":"[2601.23163] Probing the Trajectories of Reasoning Traces in Large Language Models","url":"https://arxiv.org/abs/2601.23163"},{"title":"Probing the Trajectories of Reasoning Traces in Large Language Models","url":"https://arxiv.org/html/2601.23163v1"},{"title":"(PDF) Probing the Trajectories of Reasoning Traces in ...","url":"https://www.researchgate.net/publication/400340042_Probing_the_Trajectories_of_Reasoning_Traces_in_Large_Language_Models"},{"title":"Harnessing Reasoning Trajectories for Hallucination Detection via Answer-agreement Representation Shaping","url":"https://arxiv.org/html/2601.17467"},{"title":"Harnessing Reasoning Trajectories for Hallucination Detection via Answer-agreement Representation Shaping","url":"https://arxiv.org/pdf/2601.17467"},{"title":"[2601.17467] Harnessing Reasoning Trajectories for Hallucination Detection via Answer-agreement Representation Shaping","url":"https://arxiv.org/abs/2601.17467"},{"title":"LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals","url":"https://arxiv.org/pdf/2604.05655"}]

Based on the search results, I found the paper you're looking for:

The paper "Probing the Trajectories of Reasoning Traces in Large Language Models" by Marthe Ballon and colleagues examines how large language models (LLMs) increasingly solve difficult problems by producing "reasoning traces" before emitting a final response.

**The Truncation-Reinjection Protocol:**

The research proposes a protocol to systematically probe the trajectories of reasoning traces in LLMs by: 1) generating a model's reasoning trace, 2) truncating it at fixed token-percentiles, and 3) injecting each partial trace back into the model (or a different model) to measure the induced distribution over answer choices via next-token probabilities.

**Research Questions and Controls:**

The study investigates how accuracy and decision commitment evolve along a reasoning trajectory, and whether intermediate trace segments provide answer-relevant information beyond generic length or stylistic effects.

The paper was published on arXiv on January 30, 2026. You can access the full paper at https://arxiv.org/abs/2601.23163 to see the complete experimental setup, controls, and detailed findings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af724288-5b3d-45fa-bf86-583fa217aac6",
  "isSidechain": false,
  "promptId": "cf291cc7-d8bd-4cfb-9677-4b45d023f341",
  "type": "user",
  "uuid": "e845f638-48e9-43d8-9d11-86f890fd6337",
  "toolUseResult": {
    "query": "Ballon probing trajectories reasoning traces 2601.23163 truncation reinjection protocol experimental setup controls",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MYws34Vs87X7YVC3YBAaoH",
        "content": [
          {
            "title": "[2601.23163] Probing the Trajectories of Reasoning Traces in Large Language Models",
            "url": "https://arxiv.org/abs/2601.23163"
          },
          {
            "title": "Probing the Trajectories of Reasoning Traces in Large Language Models",
            "url": "https://arxiv.org/html/2601.23163v1"
          },
          {
            "title": "(PDF) Probing the Trajectories of Reasoning Traces in ...",
            "url": "https://www.researchgate.net/publication/400340042_Probing_the_Trajectories_of_Reasoning_Traces_in_Large_Language_Models"
          },
          {
            "title": "Harnessing Reasoning Trajectories for Hallucination Detection via Answer-agreement Representation Shaping",
            "url": "https://arxiv.org/html/2601.17467"
          },
          {
            "title": "Harnessing Reasoning Trajectories for Hallucination Detection via Answer-agreement Representation Shaping",
            "url": "https://arxiv.org/pdf/2601.17467"
          },
          {
            "title": "[2601.17467] Harnessing Reasoning Trajectories for Hallucination Detection via Answer-agreement Representation Shaping",
            "url": "https://arxiv.org/abs/2601.17467"
          },
          {
            "title": "LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals",
            "url": "https://arxiv.org/pdf/2604.05655"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper \"Probing the Trajectories of Reasoning Traces in Large Language Models\" by Marthe Ballon and colleagues examines how large language models (LLMs) increasingly solve difficult problems by producing \"reasoning traces\" before emitting a final response.\n\n**The Truncation-Reinjection Protocol:**\n\nThe research proposes a protocol to systematically probe the trajectories of reasoning traces in LLMs by: 1) generating a model's reasoning trace, 2) truncating it at fixed token-percentiles, and 3) injecting each partial trace back into the model (or a different model) to measure the induced distribution over answer choices via next-token probabilities.\n\n**Research Questions and Controls:**\n\nThe study investigates how accuracy and decision commitment evolve along a reasoning trajectory, and whether intermediate trace segments provide answer-relevant information beyond generic length or stylistic effects.\n\nThe paper was published on arXiv on January 30, 2026. You can access the full paper at https://arxiv.org/abs/2601.23163 to see the complete experimental setup, controls, and detailed findings."
    ],
    "durationSeconds": 6.214280267000009,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "af724288-5b3d-45fa-bf86-583fa217aac6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T04:21:04.694Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01199zPSuW7U49BCnSz6pXsC`</summary>

```json
{
  "query": "Thought Anchors 2506.19143 counterfactual importance CoT experimental setup reviewer feedback"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e845f638-48e9-43d8-9d11-86f890fd6337",
  "isSidechain": false,
  "requestId": "req_011CbDBP3iHMqzTvkD5Yrd1Y",
  "type": "assistant",
  "uuid": "b768c4a9-74d4-4d79-882e-2ae60515139f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013gdKu5Ea4bimRYGAVK45bY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 744,
      "cache_read_input_tokens": 31798,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 744,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 31798,
          "cache_creation_input_tokens": 744,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 744
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

_source line 29 · 2026-05-20T04:21:10.262Z_

<details><summary>↩ Tool result · `toolu_01199zPSuW7U49BCnSz6pXsC`</summary>

```text
Web search results for query: "Thought Anchors 2506.19143 counterfactual importance CoT experimental setup reviewer feedback"

Links: [{"title":"[Literature Review] Thought Anchors: Which LLM Reasoning Steps Matter?","url":"https://www.themoonlight.io/en/review/thought-anchors-which-llm-reasoning-steps-matter"},{"title":"Thought Anchors: Which LLM Reasoning Steps Matter?","url":"https://www.alignmentforum.org/posts/iLHe3vLur3NgrFPFy/thought-anchors-which-llm-reasoning-steps-matter"},{"title":"[2506.19143] Thought Anchors: Which LLM Reasoning Steps Matter?","url":"https://arxiv.org/abs/2506.19143"},{"title":"Thought Anchors: Which LLM Reasoning Steps Matter?","url":"https://arxiv.org/html/2506.19143v1"},{"title":"AI Safety Diary: August 28, 2025 | Serhat Giydiren","url":"https://serhatgiydiren.com/ai-safety-diary-august-28-2025/"},{"title":"GitHub - interp-reasoning/thought-anchors: ⚓️ Repository for the \"Thought Anchors: Which LLM Reasoning Steps Matter?\" paper.","url":"https://github.com/interp-reasoning/thought-anchors"},{"title":"Under review as a conference paper at ICLR 2026 THOUGHT ANCHORS: WHICH LLM","url":"https://arxiv.org/pdf/2506.19143"},{"title":"Thought Anchors in LLM Reasoning","url":"https://www.emergentmind.com/papers/2506.19143"},{"title":"Paper page - Thought Anchors: Which LLM Reasoning Steps Matter?","url":"https://huggingface.co/papers/2506.19143"}]

Based on the search results, here's what I found about the paper "Thought Anchors: Which LLM Reasoning Steps Matter?" (arXiv:2506.19143):

## Overview
The paper "Thought Anchors: Which LLM Reasoning Steps Matter?" introduces a sentence-level approach to understanding and interpreting chain-of-thought (CoT) reasoning in large language models (LLMs).

## Counterfactual Importance Methodology
The researchers introduce a black-box method that measures each sentence's counterfactual importance by repeatedly sampling replacement sentences from the model, filtering for semantically different ones, and continuing the chain of thought from that point onwards to quantify the sentence's impact on the distribution of final answers. More specifically, they measure each sentence's counterfactual importance by resampling the model 100 times, starting from said sentence and contrasting semantically different alternatives.

## Experimental Setup
The research presents three complementary attribution methods: (1) a black-box method measuring each sentence's counterfactual importance by comparing final answers across 100 rollouts conditioned on the model generating that sentence or one with a different meaning; (2) a white-box method of aggregating attention patterns between pairs of sentences; (3) a causal attribution method measuring logical connections between sentences by suppressing attention toward one sentence and measuring the effect on each future sentence's tokens.

## Key Findings
Plan generation and uncertainty management sentences consistently exhibit higher counterfactual importance than other categories, and these sentences, often related to backtracking, appear to anchor and steer the reasoning trajectory.

The paper was submitted under review for ICLR 2026 as of the last version available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b768c4a9-74d4-4d79-882e-2ae60515139f",
  "isSidechain": false,
  "promptId": "cf291cc7-d8bd-4cfb-9677-4b45d023f341",
  "type": "user",
  "uuid": "d473a7ac-058a-49c3-a2a5-a6eea285630a",
  "toolUseResult": {
    "query": "Thought Anchors 2506.19143 counterfactual importance CoT experimental setup reviewer feedback",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FG4F9ydTWySs6tAb2Xvzse",
        "content": [
          {
            "title": "[Literature Review] Thought Anchors: Which LLM Reasoning Steps Matter?",
            "url": "https://www.themoonlight.io/en/review/thought-anchors-which-llm-reasoning-steps-matter"
          },
          {
            "title": "Thought Anchors: Which LLM Reasoning Steps Matter?",
            "url": "https://www.alignmentforum.org/posts/iLHe3vLur3NgrFPFy/thought-anchors-which-llm-reasoning-steps-matter"
          },
          {
            "title": "[2506.19143] Thought Anchors: Which LLM Reasoning Steps Matter?",
            "url": "https://arxiv.org/abs/2506.19143"
          },
          {
            "title": "Thought Anchors: Which LLM Reasoning Steps Matter?",
            "url": "https://arxiv.org/html/2506.19143v1"
          },
          {
            "title": "AI Safety Diary: August 28, 2025 | Serhat Giydiren",
            "url": "https://serhatgiydiren.com/ai-safety-diary-august-28-2025/"
          },
          {
            "title": "GitHub - interp-reasoning/thought-anchors: ⚓️ Repository for the \"Thought Anchors: Which LLM Reasoning Steps Matter?\" paper.",
            "url": "https://github.com/interp-reasoning/thought-anchors"
          },
          {
            "title": "Under review as a conference paper at ICLR 2026 THOUGHT ANCHORS: WHICH LLM",
            "url": "https://arxiv.org/pdf/2506.19143"
          },
          {
            "title": "Thought Anchors in LLM Reasoning",
            "url": "https://www.emergentmind.com/papers/2506.19143"
          },
          {
            "title": "Paper page - Thought Anchors: Which LLM Reasoning Steps Matter?",
            "url": "https://huggingface.co/papers/2506.19143"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper \"Thought Anchors: Which LLM Reasoning Steps Matter?\" (arXiv:2506.19143):\n\n## Overview\nThe paper \"Thought Anchors: Which LLM Reasoning Steps Matter?\" introduces a sentence-level approach to understanding and interpreting chain-of-thought (CoT) reasoning in large language models (LLMs).\n\n## Counterfactual Importance Methodology\nThe researchers introduce a black-box method that measures each sentence's counterfactual importance by repeatedly sampling replacement sentences from the model, filtering for semantically different ones, and continuing the chain of thought from that point onwards to quantify the sentence's impact on the distribution of final answers. More specifically, they measure each sentence's counterfactual importance by resampling the model 100 times, starting from said sentence and contrasting semantically different alternatives.\n\n## Experimental Setup\nThe research presents three complementary attribution methods: (1) a black-box method measuring each sentence's counterfactual importance by comparing final answers across 100 rollouts conditioned on the model generating that sentence or one with a different meaning; (2) a white-box method of aggregating attention patterns between pairs of sentences; (3) a causal attribution method measuring logical connections between sentences by suppressing attention toward one sentence and measuring the effect on each future sentence's tokens.\n\n## Key Findings\nPlan generation and uncertainty management sentences consistently exhibit higher counterfactual importance than other categories, and these sentences, often related to backtracking, appear to anchor and steer the reasoning trajectory.\n\nThe paper was submitted under review for ICLR 2026 as of the last version available."
    ],
    "durationSeconds": 5.561491863000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b768c4a9-74d4-4d79-882e-2ae60515139f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-20T04:21:10.268Z_

```json
{
  "parentUuid": "d473a7ac-058a-49c3-a2a5-a6eea285630a",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ba309ae6-60cc-4b0b-a4b1-6538bf06326d",
  "timestamp": "2026-05-20T04:21:10.268Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-20T04:21:13.647Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013dATEu1XQwJQAvVpWfs3mM`</summary>

```json
{
  "query": "Cox \"Decoding Answers Before CoT\" 2603.01437 steering reasoning models probe experiment baselines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba309ae6-60cc-4b0b-a4b1-6538bf06326d",
  "isSidechain": false,
  "requestId": "req_011CbDBQZLXQ7combzSPUuWw",
  "type": "assistant",
  "uuid": "6bfd7850-3eef-4c83-a47d-405ca972b103",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cu1H3XodHUFnYZFBAFv8HP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1055,
      "cache_read_input_tokens": 32542,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1055,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 32542,
          "cache_creation_input_tokens": 1055,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1055
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

_source line 32 · 2026-05-20T04:21:19.188Z_

<details><summary>↩ Tool result · `toolu_013dATEu1XQwJQAvVpWfs3mM`</summary>

```text
Web search results for query: "Cox "Decoding Answers Before CoT" 2603.01437 steering reasoning models probe experiment baselines"

Links: [{"title":"[2603.01437] Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/abs/2603.01437"},{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/html/2603.01437"},{"title":"[Literature Review] Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://www.themoonlight.io/en/review/decoding-answers-before-chain-of-thought-evidence-from-pre-cot-probes-and-activation-steering"},{"title":"[2603.17199] Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing","url":"https://arxiv.org/abs/2603.17199"},{"title":"Cox Mobile Activation Error Codes","url":"https://www.cox.com/residential/support/cox-mobile-activation-error-codes.html"},{"title":"Cox Residential Support: 24/7 Help for Internet, Billing, and More","url":"https://www.cox.com/residential/support/regional-area-code-changes.html"},{"title":"Evidence from Pre-CoT Probes and Activation Steering","url":"https://www.researchgate.net/publication/401470114_Decoding_Answers_Before_Chain-of-Thought_Evidence_from_Pre-CoT_Probes_and_Activation_Steering"},{"title":"Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing","url":"https://arxiv.org/html/2603.17199"},{"title":"CoT Reasoning without Prompting:How to Harness Inherent Reasoning in Pre-Trained Language Models | by Sahin Ahmed(Data Scientist/MLE) | Medium","url":"https://medium.com/@sahin.samia/cot-reasoning-without-prompting-how-to-harness-inherent-reasoning-in-pre-trained-language-models-099ca1b9afb9"}]

I found the paper you're looking for. Here are the key details:

**Paper Title:** Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering

**Authors:** Kyle Cox, Darius Kianersi, Adrià Garriga-Alonso

**Main Findings:**
- Instruction-tuned models often determine their answer before generating CoT.
- Training linear probes on residual stream activations at the last token before CoT, the model's final answer can be predicted with 0.9 AUC on most tasks.
- These directions are not only predictive, but also causal: steering activations along the probe direction flips model answers in over 50% of cases, significantly exceeding orthogonal baselines.

**Failure Modes:** When steering induces incorrect answers, two distinct failure modes are observed: non-entailment (stating correct premises but drawing unsupported conclusions) and confabulation (fabricating false premises).

The paper was submitted on March 2, 2026, and is available on arXiv as 2603.01437.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6bfd7850-3eef-4c83-a47d-405ca972b103",
  "isSidechain": false,
  "promptId": "cf291cc7-d8bd-4cfb-9677-4b45d023f341",
  "type": "user",
  "uuid": "20876f2a-8c1f-4203-8f22-0c40cebcefb3",
  "toolUseResult": {
    "query": "Cox \"Decoding Answers Before CoT\" 2603.01437 steering reasoning models probe experiment baselines",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TTcXoq8w5oKDpEEgwyqR4s",
        "content": [
          {
            "title": "[2603.01437] Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering",
            "url": "https://arxiv.org/abs/2603.01437"
          },
          {
            "title": "Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering",
            "url": "https://arxiv.org/html/2603.01437"
          },
          {
            "title": "[Literature Review] Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering",
            "url": "https://www.themoonlight.io/en/review/decoding-answers-before-chain-of-thought-evidence-from-pre-cot-probes-and-activation-steering"
          },
          {
            "title": "[2603.17199] Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing",
            "url": "https://arxiv.org/abs/2603.17199"
          },
          {
            "title": "Cox Mobile Activation Error Codes",
            "url": "https://www.cox.com/residential/support/cox-mobile-activation-error-codes.html"
          },
          {
            "title": "Cox Residential Support: 24/7 Help for Internet, Billing, and More",
            "url": "https://www.cox.com/residential/support/regional-area-code-changes.html"
          },
          {
            "title": "Evidence from Pre-CoT Probes and Activation Steering",
            "url": "https://www.researchgate.net/publication/401470114_Decoding_Answers_Before_Chain-of-Thought_Evidence_from_Pre-CoT_Probes_and_Activation_Steering"
          },
          {
            "title": "Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing",
            "url": "https://arxiv.org/html/2603.17199"
          },
          {
            "title": "CoT Reasoning without Prompting:How to Harness Inherent Reasoning in Pre-Trained Language Models | by Sahin Ahmed(Data Scientist/MLE) | Medium",
            "url": "https://medium.com/@sahin.samia/cot-reasoning-without-prompting-how-to-harness-inherent-reasoning-in-pre-trained-language-models-099ca1b9afb9"
          }
        ]
      },
      "I found the paper you're looking for. Here are the key details:\n\n**Paper Title:** Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering\n\n**Authors:** Kyle Cox, Darius Kianersi, Adrià Garriga-Alonso\n\n**Main Findings:**\n- Instruction-tuned models often determine their answer before generating CoT.\n- Training linear probes on residual stream activations at the last token before CoT, the model's final answer can be predicted with 0.9 AUC on most tasks.\n- These directions are not only predictive, but also causal: steering activations along the probe direction flips model answers in over 50% of cases, significantly exceeding orthogonal baselines.\n\n**Failure Modes:** When steering induces incorrect answers, two distinct failure modes are observed: non-entailment (stating correct premises but drawing unsupported conclusions) and confabulation (fabricating false premises).\n\nThe paper was submitted on March 2, 2026, and is available on arXiv as 2603.01437."
    ],
    "durationSeconds": 5.537071821999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6bfd7850-3eef-4c83-a47d-405ca972b103",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness  ## Description When a reasoning model gets the right answer, is i…",
  "leafUuid": "20876f2a-8c1f-4203-8f22-0c40cebcefb3",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Information-Contribution Gap for CoT faithfulness",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb"
}
```

---

### Tool call

_source line 35 · 2026-05-20T04:21:22.220Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P3Tke8mmpL9xXR3DxDA3iP`</summary>

```json
{
  "query": "Young \"Measuring Faithfulness Depends on How You Measure\" 2603.20172 classifier sensitivity kappa evaluation CoT"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20876f2a-8c1f-4203-8f22-0c40cebcefb3",
  "isSidechain": false,
  "requestId": "req_011CbDBRDPW3GQcKXEuq93z7",
  "type": "assistant",
  "uuid": "f588257e-bfc5-4a36-8f10-77a91b34622a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BQDXBcUwCyZmFFSYGHSg39",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 936,
      "cache_read_input_tokens": 33597,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 936,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 33597,
          "cache_creation_input_tokens": 936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 936
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

_source line 36 · 2026-05-20T04:21:27.460Z_

<details><summary>↩ Tool result · `toolu_01P3Tke8mmpL9xXR3DxDA3iP`</summary>

```text
Web search results for query: "Young "Measuring Faithfulness Depends on How You Measure" 2603.20172 classifier sensitivity kappa evaluation CoT"

Links: [{"title":"[2603.20172] Measuring Faithfulness Depends on How You Measure: Classifier Sensitivity in LLM Chain-of-Thought Evaluation","url":"https://arxiv.org/abs/2603.20172"},{"title":"Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?","url":"https://arxiv.org/html/2603.22582"},{"title":"MEASURING FAITHFULNESS DEPENDS ON HOW YOU MEASURE:","url":"https://arxiv.org/pdf/2603.20172"},{"title":"Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models","url":"https://arxiv.org/html/2603.26410v1"},{"title":"Measuring Faithfulness Depends on How You Measure: Classifier Sensitivity in LLM Chain-of-Thought Evaluation","url":"https://arxiv.org/html/2603.20172"},{"title":"Measuring Faithfulness Depends on How You Measure: Classifier Sensitivity in LLM Chain-of-Thought Evaluation | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2603.20172"},{"title":"Measuring Faithfulness in Chain-of-Thought Reasoning","url":"https://arxiv.org/pdf/2307.13702"}]

I found the paper! Here's what the search revealed:

The paper "Measuring Faithfulness Depends on How You Measure: Classifier Sensitivity in LLM Chain-of-Thought Evaluation" (arXiv:2603.20172) is authored by Richard J. Young.

**Key findings:**

The paper argues that recent work on chain-of-thought (CoT) faithfulness reports single aggregate numbers implying that faithfulness is an objective, measurable property of a model, but provides evidence that it is not.

Three classifiers (a regex-only detector, a regex-plus-LLM pipeline, and a Claude Sonnet 4 judge) are applied to 10,276 influenced reasoning traces from 12 open-weight models spanning 9 families and 7B to 1T parameters, and on identical data, these classifiers produce faithfulness rates of 74.4%, 82.6%, and 69.7%.

**Regarding classifier sensitivity and kappa evaluation:**

Cohen's kappa ranges from 0.06 ("slight") for sycophancy hints to 0.42 ("moderate") for grader hints, and the asymmetry is pronounced: for sycophancy, 883 cases are classified as faithful by the pipeline but unfaithful by the Sonnet judge, while only 2 go the other direction.

Classifier choice can also reverse model rankings: Qwen3.5-27B ranks 1st under the pipeline but 7th under Sonnet; OLMo-3.1-32B moves from 9th to 3rd.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f588257e-bfc5-4a36-8f10-77a91b34622a",
  "isSidechain": false,
  "promptId": "cf291cc7-d8bd-4cfb-9677-4b45d023f341",
  "type": "user",
  "uuid": "1e63f306-baa4-4d81-bf66-90cabf3ec16c",
  "toolUseResult": {
    "query": "Young \"Measuring Faithfulness Depends on How You Measure\" 2603.20172 classifier sensitivity kappa evaluation CoT",
    "results": [
      {
        "tool_use_id": "srvtoolu_019J2NioCUvzs7rwrrpSCWcv",
        "content": [
          {
            "title": "[2603.20172] Measuring Faithfulness Depends on How You Measure: Classifier Sensitivity in LLM Chain-of-Thought Evaluation",
            "url": "https://arxiv.org/abs/2603.20172"
          },
          {
            "title": "Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?",
            "url": "https://arxiv.org/html/2603.22582"
          },
          {
            "title": "MEASURING FAITHFULNESS DEPENDS ON HOW YOU MEASURE:",
            "url": "https://arxiv.org/pdf/2603.20172"
          },
          {
            "title": "Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models",
            "url": "https://arxiv.org/html/2603.26410v1"
          },
          {
            "title": "Measuring Faithfulness Depends on How You Measure: Classifier Sensitivity in LLM Chain-of-Thought Evaluation",
            "url": "https://arxiv.org/html/2603.20172"
          },
          {
            "title": "Measuring Faithfulness Depends on How You Measure: Classifier Sensitivity in LLM Chain-of-Thought Evaluation | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/2603.20172"
          },
          {
            "title": "Measuring Faithfulness in Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/pdf/2307.13702"
          }
        ]
      },
      "I found the paper! Here's what the search revealed:\n\nThe paper \"Measuring Faithfulness Depends on How You Measure: Classifier Sensitivity in LLM Chain-of-Thought Evaluation\" (arXiv:2603.20172) is authored by Richard J. Young.\n\n**Key findings:**\n\nThe paper argues that recent work on chain-of-thought (CoT) faithfulness reports single aggregate numbers implying that faithfulness is an objective, measurable property of a model, but provides evidence that it is not.\n\nThree classifiers (a regex-only detector, a regex-plus-LLM pipeline, and a Claude Sonnet 4 judge) are applied to 10,276 influenced reasoning traces from 12 open-weight models spanning 9 families and 7B to 1T parameters, and on identical data, these classifiers produce faithfulness rates of 74.4%, 82.6%, and 69.7%.\n\n**Regarding classifier sensitivity and kappa evaluation:**\n\nCohen's kappa ranges from 0.06 (\"slight\") for sycophancy hints to 0.42 (\"moderate\") for grader hints, and the asymmetry is pronounced: for sycophancy, 883 cases are classified as faithful by the pipeline but unfaithful by the Sonnet judge, while only 2 go the other direction.\n\nClassifier choice can also reverse model rankings: Qwen3.5-27B ranks 1st under the pipeline but 7th under Sonnet; OLMo-3.1-32B moves from 9th to 3rd."
    ],
    "durationSeconds": 5.2365023580000125,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f588257e-bfc5-4a36-8f10-77a91b34622a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T04:21:39.809Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014wJ8XZfqAgr5hroXd3bY4u`</summary>

```json
{
  "query": "prefix truncation chain-of-thought evaluation compute-normalized comparison probe hidden states 2026 reviewer concerns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e63f306-baa4-4d81-bf66-90cabf3ec16c",
  "isSidechain": false,
  "requestId": "req_011CbDBRphXZFnakKtLEcBAh",
  "type": "assistant",
  "uuid": "298ec5b9-a0df-4a42-ac1e-cf770120f74a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qo1HeKvBKMxyTRFUFDvnGk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 858,
      "cache_read_input_tokens": 34533,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 858,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 34533,
          "cache_creation_input_tokens": 858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 858
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

_source line 38 · 2026-05-20T04:21:48.162Z_

<details><summary>↩ Tool result · `toolu_014wJ8XZfqAgr5hroXd3bY4u`</summary>

```text
Web search results for query: "prefix truncation chain-of-thought evaluation compute-normalized comparison probe hidden states 2026 reviewer concerns"

Links: [{"title":"Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/html/2504.05419v1"},{"title":"Preprint. February 2026. DYNAMICS WITHIN LATENT CHAIN-OF-THOUGHT:","url":"https://arxiv.org/pdf/2602.08783"},{"title":"When Chain-of-Thought Fails, the Solution Hides in the Hidden States","url":"https://arxiv.org/html/2604.23351v1"},{"title":"EntroCut: Entropy-Guided Adaptive Truncation for Efficient Chain-of-Thought Reasoning in Small-scale Large Reasoning Models","url":"https://arxiv.org/pdf/2601.22617"},{"title":"Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification | OpenReview","url":"https://openreview.net/forum?id=O6I0Av7683"},{"title":"Reasoning Efficiently Through Adaptive Chain-of-Thought ...","url":"https://arxiv.org/pdf/2509.14093"},{"title":"Temporal Predictors of Outcome in Reasoning Language Models","url":"https://arxiv.org/pdf/2511.14773"},{"title":"Eliciting Chain-of-Thought in Base LLMs via Gradient-Based Representation Optimization","url":"https://arxiv.org/pdf/2511.19131"}]

Based on the search results, I found several relevant papers and resources on these topics from 2026 and late 2025. Here are the key findings:

## Main Research Areas

**Probing Hidden States for Self-Verification:**
Reasoning models with long chain-of-thought encode strong signals about the correctness of intermediate answers in model's hidden states, and can be used for early exit. Researchers sequentially evaluate each intermediate answer in the full reasoning trace, using the probe to compute confidence scores on the answer's correctness, and truncate the reasoning trace at this chunk when an intermediate answer meets a confidence threshold.

**Prefix Truncation and Early Decodability:**
Hidden states from very short prefixes (approximately 4 tokens) already contain linearly decodable information about eventual correctness, reaching AUCs up to 0.8+ on MATH-like data. EntroCut proposes a training-free approach that probes the prefix entropy of responses to dynamically decide whether to terminate or continue reasoning, preventing excessive reasoning beyond necessity.

**Latent Chain-of-Thought Analysis:**
Researchers truncate latent computation after step k and decode from the hidden state to test when correctness becomes decodable. Combining step interventions with early readouts yields directed propagation strengths summarized as an empirical influence structure.

**Computational Efficiency:**
Researchers record the inference token length at the point of truncation to evaluate computational efficiency.

The search results indicate active research in this area with multiple papers from 2026 addressing these evaluation and efficiency concerns, though the search didn't specifically return reviewer comments or concerns.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "298ec5b9-a0df-4a42-ac1e-cf770120f74a",
  "isSidechain": false,
  "promptId": "cf291cc7-d8bd-4cfb-9677-4b45d023f341",
  "type": "user",
  "uuid": "a566e96d-7796-4a24-a219-dd415ae22034",
  "toolUseResult": {
    "query": "prefix truncation chain-of-thought evaluation compute-normalized comparison probe hidden states 2026 reviewer concerns",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KXwxVTzD4TZBNSBXxWQeDC",
        "content": [
          {
            "title": "Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification",
            "url": "https://arxiv.org/html/2504.05419v1"
          },
          {
            "title": "Preprint. February 2026. DYNAMICS WITHIN LATENT CHAIN-OF-THOUGHT:",
            "url": "https://arxiv.org/pdf/2602.08783"
          },
          {
            "title": "When Chain-of-Thought Fails, the Solution Hides in the Hidden States",
            "url": "https://arxiv.org/html/2604.23351v1"
          },
          {
            "title": "EntroCut: Entropy-Guided Adaptive Truncation for Efficient Chain-of-Thought Reasoning in Small-scale Large Reasoning Models",
            "url": "https://arxiv.org/pdf/2601.22617"
          },
          {
            "title": "Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification | OpenReview",
            "url": "https://openreview.net/forum?id=O6I0Av7683"
          },
          {
            "title": "Reasoning Efficiently Through Adaptive Chain-of-Thought ...",
            "url": "https://arxiv.org/pdf/2509.14093"
          },
          {
            "title": "Temporal Predictors of Outcome in Reasoning Language Models",
            "url": "https://arxiv.org/pdf/2511.14773"
          },
          {
            "title": "Eliciting Chain-of-Thought in Base LLMs via Gradient-Based Representation Optimization",
            "url": "https://arxiv.org/pdf/2511.19131"
          }
        ]
      },
      "Based on the search results, I found several relevant papers and resources on these topics from 2026 and late 2025. Here are the key findings:\n\n## Main Research Areas\n\n**Probing Hidden States for Self-Verification:**\nReasoning models with long chain-of-thought encode strong signals about the correctness of intermediate answers in model's hidden states, and can be used for early exit. Researchers sequentially evaluate each intermediate answer in the full reasoning trace, using the probe to compute confidence scores on the answer's correctness, and truncate the reasoning trace at this chunk when an intermediate answer meets a confidence threshold.\n\n**Prefix Truncation and Early Decodability:**\nHidden states from very short prefixes (approximately 4 tokens) already contain linearly decodable information about eventual correctness, reaching AUCs up to 0.8+ on MATH-like data. EntroCut proposes a training-free approach that probes the prefix entropy of responses to dynamically decide whether to terminate or continue reasoning, preventing excessive reasoning beyond necessity.\n\n**Latent Chain-of-Thought Analysis:**\nResearchers truncate latent computation after step k and decode from the hidden state to test when correctness becomes decodable. Combining step interventions with early readouts yields directed propagation strengths summarized as an empirical influence structure.\n\n**Computational Efficiency:**\nResearchers record the inference token length at the point of truncation to evaluate computational efficiency.\n\nThe search results indicate active research in this area with multiple papers from 2026 addressing these evaluation and efficiency concerns, though the search didn't specifically return reviewer comments or concerns."
    ],
    "durationSeconds": 8.347922141999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "298ec5b9-a0df-4a42-ac1e-cf770120f74a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T04:21:51.329Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NJR66eZWaJjmJULyYzY3q2`</summary>

```json
{
  "query": "Gjølbye \"Reasoning Models Move Differently\" 2605.15454 length correction difficulty conditioning experimental design"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a566e96d-7796-4a24-a219-dd415ae22034",
  "isSidechain": false,
  "requestId": "req_011CbDBTMG5bbH93n465pD4a",
  "type": "assistant",
  "uuid": "7b381bf4-49a9-4c8c-8c95-30907ab152da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N1dG8WnGkTKDtfjoVsMbDb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 845,
      "cache_read_input_tokens": 35391,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 845,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 35391,
          "cache_creation_input_tokens": 845,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 845
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

_source line 40 · 2026-05-20T04:21:59.080Z_

<details><summary>↩ Tool result · `toolu_01NJR66eZWaJjmJULyYzY3q2`</summary>

```text
Web search results for query: "Gjølbye "Reasoning Models Move Differently" 2605.15454 length correction difficulty conditioning experimental design"

Links: [{"title":"[2605.15454] Reasoning Models Don't Just Think Longer, They Move Differently","url":"https://arxiv.org/abs/2605.15454"},{"title":"Reasoning Models Don’t Just Think Longer, They Move Differently","url":"https://arxiv.org/html/2605.15454"},{"title":"The Illusion of Insight in Reasoning Models","url":"https://arxiv.org/pdf/2601.00514"},{"title":"What makes Reasoning Models Different? Follow the Reasoning Leader for Efficient Decoding","url":"https://arxiv.org/pdf/2506.06998"},{"title":"When Can Large Reasoning Models Save Thinking? Mechanistic Analysis of Behavioral Divergence in Reasoning","url":"https://arxiv.org/pdf/2505.15276"}]

Based on the search results, I found the paper you're looking for. Here are the key findings:

**Paper Overview:**
The paper "Reasoning Models Don't Just Think Longer, They Move Differently" is by Anders Gjølbye, Lars Kai Hansen, and Sanmi Koyejo from Technical University of Denmark and Stanford University.

**Main Research Questions:**
The research addresses whether reasoning-trained language models spend more tokens on harder problems merely to compute for more steps or to follow a different internal trajectory.

**Experimental Design and Methodology:**
The study examines hidden-state trajectories during chain-of-thought generation across competitive programming, mathematics, and Boolean satisfiability.

**Key Finding on Length Correction:**
Raw trajectory geometry is strongly shaped by generation length: longer generations mechanically alter path statistics, so difficulty-dependent comparisons are misleading without adjustment. The findings establish length correction as a prerequisite for generation-time trajectory analysis.

**Results After Difficulty-Conditioning:**
After residualizing trajectory statistics on length, difficulty remains systematically coupled to corrected trajectory geometry across all domains studied. The clearest reasoning-specific separation appears in the code domain, where harder problems show more direct corrected trajectories and less heterogeneous local curvature in reasoning-trained models than in matched instruction-tuned baselines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b381bf4-49a9-4c8c-8c95-30907ab152da",
  "isSidechain": false,
  "promptId": "cf291cc7-d8bd-4cfb-9677-4b45d023f341",
  "type": "user",
  "uuid": "b91d5b91-5935-4e44-9a25-b9182a6ad9a2",
  "toolUseResult": {
    "query": "Gjølbye \"Reasoning Models Move Differently\" 2605.15454 length correction difficulty conditioning experimental design",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BVRm1E7kbnphADm28dAriY",
        "content": [
          {
            "title": "[2605.15454] Reasoning Models Don't Just Think Longer, They Move Differently",
            "url": "https://arxiv.org/abs/2605.15454"
          },
          {
            "title": "Reasoning Models Don’t Just Think Longer, They Move Differently",
            "url": "https://arxiv.org/html/2605.15454"
          },
          {
            "title": "The Illusion of Insight in Reasoning Models",
            "url": "https://arxiv.org/pdf/2601.00514"
          },
          {
            "title": "What makes Reasoning Models Different? Follow the Reasoning Leader for Efficient Decoding",
            "url": "https://arxiv.org/pdf/2506.06998"
          },
          {
            "title": "When Can Large Reasoning Models Save Thinking? Mechanistic Analysis of Behavioral Divergence in Reasoning",
            "url": "https://arxiv.org/pdf/2505.15276"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here are the key findings:\n\n**Paper Overview:**\nThe paper \"Reasoning Models Don't Just Think Longer, They Move Differently\" is by Anders Gjølbye, Lars Kai Hansen, and Sanmi Koyejo from Technical University of Denmark and Stanford University.\n\n**Main Research Questions:**\nThe research addresses whether reasoning-trained language models spend more tokens on harder problems merely to compute for more steps or to follow a different internal trajectory.\n\n**Experimental Design and Methodology:**\nThe study examines hidden-state trajectories during chain-of-thought generation across competitive programming, mathematics, and Boolean satisfiability.\n\n**Key Finding on Length Correction:**\nRaw trajectory geometry is strongly shaped by generation length: longer generations mechanically alter path statistics, so difficulty-dependent comparisons are misleading without adjustment. The findings establish length correction as a prerequisite for generation-time trajectory analysis.\n\n**Results After Difficulty-Conditioning:**\nAfter residualizing trajectory statistics on length, difficulty remains systematically coupled to corrected trajectory geometry across all domains studied. The clearest reasoning-specific separation appears in the code domain, where harder problems show more direct corrected trajectories and less heterogeneous local curvature in reasoning-trained models than in matched instruction-tuned baselines."
    ],
    "durationSeconds": 7.747759204000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7b381bf4-49a9-4c8c-8c95-30907ab152da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T04:22:01.911Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01USqU7XRs9pTXwc5HLHx6cF`</summary>

```json
{
  "query": "CMI causal mediation index Sathyanarayanan 2602.03994 activation patching layerwise experimental setup limitations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b91d5b91-5935-4e44-9a25-b9182a6ad9a2",
  "isSidechain": false,
  "requestId": "req_011CbDBU9wUAQderuLAu9UFK",
  "type": "assistant",
  "uuid": "e05c710a-37f2-4d06-b6a3-b55d1f7ce173",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FcxbtcP2fu53634DBo59o8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 627,
      "cache_read_input_tokens": 36236,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 627,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 36236,
          "cache_creation_input_tokens": 627,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 627
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

_source line 42 · 2026-05-20T04:22:15.636Z_

<details><summary>↩ Tool result · `toolu_01USqU7XRs9pTXwc5HLHx6cF`</summary>

```text
Web search results for query: "CMI causal mediation index Sathyanarayanan 2602.03994 activation patching layerwise experimental setup limitations"

Links: [{"title":"Activation Patching and Causal Interventions | Learn Mechanistic Interpretability","url":"https://learnmechinterp.com/topics/activation-patching/"},{"title":"Bypassing the Rationale: Causal Auditing of Implicit Reasoning in Language Models","url":"https://arxiv.org/pdf/2602.03994"},{"title":"[2602.03994] When Chains of Thought Don't Matter: Causal Bypass in Large Language Models","url":"https://arxiv.org/abs/2602.03994"},{"title":"How to use and interpret activation patching","url":"https://arxiv.org/pdf/2404.15255"},{"title":"Surgical Activation Steering via Generative Causal Mediation","url":"https://arxiv.org/html/2602.16080v1"},{"title":"Towards Best Practices of Activation Patching in Language Models","url":"https://scispace.com/pdf/towards-best-practices-of-activation-patching-in-language-3t50e7ugvq.pdf"},{"title":"Activation Steering in Generative Settings via Contrastive ...","url":"https://openreview.net/pdf?id=bUXa74EiOL"},{"title":"Activation Steering via Generative Causal Mediation","url":"https://arxiv.org/html/2602.16080v2"}]

Great! I found the paper. Let me search for more specific information about the experimental setup and limitations.

Links: [{"title":"[2602.03994] When Chains of Thought Don't Matter: Causal Bypass in Large Language Models","url":"https://arxiv.org/abs/2602.03994"},{"title":"BYPASSING THE RATIONALE: CAUSAL AUDITING OF","url":"https://www.arxiv.org/pdf/2602.03994"},{"title":"Causal Mediation Analysis with Multi-dimensional and Indirectly Observed Mediators | OpenReview","url":"https://openreview.net/forum?id=5tYmuJ9uj9"},{"title":"Causal Mediation Analysis with Multi-dimensional and Indirectly Observed   Mediators","url":"https://arxiv.org/pdf/2306.07918"},{"title":"Causal mediation analysis with mediator values below an assay limit","url":"https://arxiv.org/pdf/2107.14782"},{"title":"A Bayesian approach to mediation analysis predicts 206 causal target genes in Alzheimer’s disease","url":"https://www.biorxiv.org/content/10.1101/219428.full.pdf"},{"title":"Causal Mediation in Natural Experiments","url":"https://arxiv.org/html/2508.05449v1"},{"title":"Efficient nonparametric estimation of causal mediation effects","url":"https://arxiv.org/pdf/1601.03501"}]

Let me search for more detailed information about the experimental setup and limitations mentioned in the paper.

Links: [{"title":"IDM Activator | IDM Universal Activator 2019 | IDM Fixed Fake Serial Keys Error Software","url":"https://groups.google.com/g/storinunut/c/1JVOAYr0Txc"},{"title":"Using the Windows Activation troubleshooter - Microsoft Support","url":"https://support.microsoft.com/en-us/windows/using-the-windows-activation-troubleshooter-d717cdff-cf19-9770-7198-40119c2a696c"},{"title":"transformer_lens.patching - TransformerLens Documentation","url":"https://transformerlensorg.github.io/TransformerLens/generated/code/transformer_lens.patching.html"},{"title":"When Chains of Thought Don’t Matter: Causal Bypass in Large Language Models","url":"https://arxiv.org/html/2602.03994"},{"title":"Endpoint Central Patch Deployment Error codes","url":"https://pitstop.manageengine.com/portal/en/community/topic/endpoint-central-patch-deployment-error-codes"},{"title":"Activation Patching - nnsight","url":"https://nnsight.net/tutorials/tutorials/causal_mediation_analysis/activation_patching/"},{"title":"Illustration of two activation patching operations. In (a), we get the... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/llustration-of-two-activation-patching-operations-In-a-we-get-the-corrupted_fig1_390990657"},{"title":"Attribution Patching: Activation Patching At Industrial Scale","url":"https://www.lesswrong.com/posts/gtLLBhzQTG6nKTeCZ/attribution-patching-activation-patching-at-industrial-scale"},{"title":"Fixing xdelta3 Checksum Mismatch Errors","url":"https://valegas.sedes.ma.gov.br/xdelta3-target-window-checksum-mismatch-xd3_invalid_input/"},{"title":"Resolving Rockwell Automation EVMOVE Activation Error: 'Activation Fil – Industrial Monitor Direct","url":"https://industrialmonitordirect.com/blogs/knowledgebase/resolving-rockwell-automation-evmove-activation-error-activation-file-corrupt-invalid-serial-numbe"}]

Based on the search results I've found, I can provide you with information about the paper by Sathyanarayanan et al. (arXiv:2602.03994):

## Overview

The paper is titled "Bypassing the Rationale: Causal Auditing of Implicit Reasoning in Language Models" by Anish Sathyanarayanan, Aditya Nagarsekar, and Aarush Rathore from Birla Institute of Technology and Science, Pilani.

## CMI (CoT Mediation Index)

The key metric, the CoT Mediation Index (CMI), isolates CoT-specific causal influence by comparing performance degradation from patching CoT-token hidden states against matched control patches. The authors use layerwise activation patching to measure how much CoT-related representations matter for the final answer, summarizing this with the CoT Mediation Index (CMI) across layers.

## Experimental Setup

The approach introduces a causal, layerwise audit of CoT faithfulness based on activation patching. Instead of relying solely on output-level behavior, the authors intervene directly on internal activations and measure how these perturbations affect the model's predictions, allowing them to test which internal states matter for CoT.

## Key Findings

In many cases, CMI is highly localized in depth, with only a small subset of layers carrying most of the CoT-specific causal effect. The authors also observe bypass regimes in which models behaviorally emit plausible CoT while showing little additional mechanistic reliance on it, suggesting that visible reasoning traces can diverge from internal computation.

In pilot evaluations, audit-aware prompting increases detectable manipulation signals, yet causal probes reveal task-dependent mediation: many QA items exhibit near-total bypass (CMI ≈ 0), while some logic problems show stronger mediation (CMI up to 0.56). Layer-wise analysis reveals narrow and task-dependent "reasoning windows" even when mean CMI is low.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e05c710a-37f2-4d06-b6a3-b55d1f7ce173",
  "isSidechain": false,
  "promptId": "cf291cc7-d8bd-4cfb-9677-4b45d023f341",
  "type": "user",
  "uuid": "a2529f0c-ba1b-4442-b078-80ca402d1def",
  "toolUseResult": {
    "query": "CMI causal mediation index Sathyanarayanan 2602.03994 activation patching layerwise experimental setup limitations",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SAQ1ws3JuqndQALHtE79h8",
        "content": [
          {
            "title": "Activation Patching and Causal Interventions | Learn Mechanistic Interpretability",
            "url": "https://learnmechinterp.com/topics/activation-patching/"
          },
          {
            "title": "Bypassing the Rationale: Causal Auditing of Implicit Reasoning in Language Models",
            "url": "https://arxiv.org/pdf/2602.03994"
          },
          {
            "title": "[2602.03994] When Chains of Thought Don't Matter: Causal Bypass in Large Language Models",
            "url": "https://arxiv.org/abs/2602.03994"
          },
          {
            "title": "How to use and interpret activation patching",
            "url": "https://arxiv.org/pdf/2404.15255"
          },
          {
            "title": "Surgical Activation Steering via Generative Causal Mediation",
            "url": "https://arxiv.org/html/2602.16080v1"
          },
          {
            "title": "Towards Best Practices of Activation Patching in Language Models",
            "url": "https://scispace.com/pdf/towards-best-practices-of-activation-patching-in-language-3t50e7ugvq.pdf"
          },
          {
            "title": "Activation Steering in Generative Settings via Contrastive ...",
            "url": "https://openreview.net/pdf?id=bUXa74EiOL"
          },
          {
            "title": "Activation Steering via Generative Causal Mediation",
            "url": "https://arxiv.org/html/2602.16080v2"
          }
        ]
      },
      "Great! I found the paper. Let me search for more specific information about the experimental setup and limitations.",
      {
        "tool_use_id": "srvtoolu_01Ce1QTcwa57QrhoiB3XNbmK",
        "content": [
          {
            "title": "[2602.03994] When Chains of Thought Don't Matter: Causal Bypass in Large Language Models",
            "url": "https://arxiv.org/abs/2602.03994"
          },
          {
            "title": "BYPASSING THE RATIONALE: CAUSAL AUDITING OF",
            "url": "https://www.arxiv.org/pdf/2602.03994"
          },
          {
            "title": "Causal Mediation Analysis with Multi-dimensional and Indirectly Observed Mediators | OpenReview",
            "url": "https://openreview.net/forum?id=5tYmuJ9uj9"
          },
          {
            "title": "Causal Mediation Analysis with Multi-dimensional and Indirectly Observed   Mediators",
            "url": "https://arxiv.org/pdf/2306.07918"
          },
          {
            "title": "Causal mediation analysis with mediator values below an assay limit",
            "url": "https://arxiv.org/pdf/2107.14782"
          },
          {
            "title": "A Bayesian approach to mediation analysis predicts 206 causal target genes in Alzheimer’s disease",
            "url": "https://www.biorxiv.org/content/10.1101/219428.full.pdf"
          },
          {
            "title": "Causal Mediation in Natural Experiments",
            "url": "https://arxiv.org/html/2508.05449v1"
          },
          {
            "title": "Efficient nonparametric estimation of causal mediation effects",
            "url": "https://arxiv.org/pdf/1601.03501"
          }
        ]
      },
      "Let me search for more detailed information about the experimental setup and limitations mentioned in the paper.",
      {
        "tool_use_id": "srvtoolu_01VSbYQF85v7UNTY1b2Sha8i",
        "content": [
          {
            "title": "IDM Activator | IDM Universal Activator 2019 | IDM Fixed Fake Serial Keys Error Software",
            "url": "https://groups.google.com/g/storinunut/c/1JVOAYr0Txc"
          },
          {
            "title": "Using the Windows Activation troubleshooter - Microsoft Support",
            "url": "https://support.microsoft.com/en-us/windows/using-the-windows-activation-troubleshooter-d717cdff-cf19-9770-7198-40119c2a696c"
          },
          {
            "title": "transformer_lens.patching - TransformerLens Documentation",
            "url": "https://transformerlensorg.github.io/TransformerLens/generated/code/transformer_lens.patching.html"
          },
          {
            "title": "When Chains of Thought Don’t Matter: Causal Bypass in Large Language Models",
            "url": "https://arxiv.org/html/2602.03994"
          },
          {
            "title": "Endpoint Central Patch Deployment Error codes",
            "url": "https://pitstop.manageengine.com/portal/en/community/topic/endpoint-central-patch-deployment-error-codes"
          },
          {
            "title": "Activation Patching - nnsight",
            "url": "https://nnsight.net/tutorials/tutorials/causal_mediation_analysis/activation_patching/"
          },
          {
            "title": "Illustration of two activation patching operations. In (a), we get the... | Download Scientific Diagram",
            "url": "https://www.researchgate.net/figure/llustration-of-two-activation-patching-operations-In-a-we-get-the-corrupted_fig1_390990657"
          },
          {
            "title": "Attribution Patching: Activation Patching At Industrial Scale",
            "url": "https://www.lesswrong.com/posts/gtLLBhzQTG6nKTeCZ/attribution-patching-activation-patching-at-industrial-scale"
          },
          {
            "title": "Fixing xdelta3 Checksum Mismatch Errors",
            "url": "https://valegas.sedes.ma.gov.br/xdelta3-target-window-checksum-mismatch-xd3_invalid_input/"
          },
          {
            "title": "Resolving Rockwell Automation EVMOVE Activation Error: 'Activation Fil – Industrial Monitor Direct",
            "url": "https://industrialmonitordirect.com/blogs/knowledgebase/resolving-rockwell-automation-evmove-activation-error-activation-file-corrupt-invalid-serial-numbe"
          }
        ]
      },
      "Based on the search results I've found, I can provide you with information about the paper by Sathyanarayanan et al. (arXiv:2602.03994):\n\n## Overview\n\nThe paper is titled \"Bypassing the Rationale: Causal Auditing of Implicit Reasoning in Language Models\" by Anish Sathyanarayanan, Aditya Nagarsekar, and Aarush Rathore from Birla Institute of Technology and Science, Pilani.\n\n## CMI (CoT Mediation Index)\n\nThe key metric, the CoT Mediation Index (CMI), isolates CoT-specific causal influence by comparing performance degradation from patching CoT-token hidden states against matched control patches. The authors use layerwise activation patching to measure how much CoT-related representations matter for the final answer, summarizing this with the CoT Mediation Index (CMI) across layers.\n\n## Experimental Setup\n\nThe approach introduces a causal, layerwise audit of CoT faithfulness based on activation patching. Instead of relying solely on output-level behavior, the authors intervene directly on internal activations and measure how these perturbations affect the model's predictions, allowing them to test which internal states matter for CoT.\n\n## Key Findings\n\nIn many cases, CMI is highly localized in depth, with only a small subset of layers carrying most of the CoT-specific causal effect. The authors also observe bypass regimes in which models behaviorally emit plausible CoT while showing little additional mechanistic reliance on it, suggesting that visible reasoning traces can diverge from internal computation.\n\nIn pilot evaluations, audit-aware prompting increases detectable manipulation signals, yet causal probes reveal task-dependent mediation: many QA items exhibit near-total bypass (CMI ≈ 0), while some logic problems show stronger mediation (CMI up to 0.56). Layer-wise analysis reveals narrow and task-dependent \"reasoning windows\" even when mean CMI is low."
    ],
    "durationSeconds": 13.720161927000008,
    "searchCount": 3
  },
  "sourceToolAssistantUUID": "e05c710a-37f2-4d06-b6a3-b55d1f7ce173",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness  ## Description When a reasoning model gets the right answer, is i…",
  "leafUuid": "a2529f0c-ba1b-4442-b078-80ca402d1def",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Information-Contribution Gap for CoT faithfulness",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb"
}
```

---

### Assistant

_source line 45 · 2026-05-20T04:22:18.320Z_

Now let me do one more search specifically on reviewer expectations and common experimental weaknesses in this area.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2529f0c-ba1b-4442-b078-80ca402d1def",
  "isSidechain": false,
  "requestId": "req_011CbDBVNiSe7feTM8Yygc2z",
  "type": "assistant",
  "uuid": "3e57f885-c23e-428f-8dfe-130941006bae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011VvhRDN7KBSAC7qx6wDjPK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1930,
      "cache_read_input_tokens": 36863,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 95,
          "cache_read_input_tokens": 36863,
          "cache_creation_input_tokens": 1930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1930
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

_source line 46 · 2026-05-20T04:22:19.463Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QdpkWAzUgEJ2uZNVnxV5cH`</summary>

```json
{
  "query": "NLDD reasoning horizon Ye 2602.11201 natural language degradation experimental setup limitations benchmarks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e57f885-c23e-428f-8dfe-130941006bae",
  "isSidechain": false,
  "requestId": "req_011CbDBVNiSe7feTM8Yygc2z",
  "type": "assistant",
  "uuid": "976c35d9-80a6-4d44-bd34-5cecdc0d5a22",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011VvhRDN7KBSAC7qx6wDjPK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1930,
      "cache_read_input_tokens": 36863,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 95,
          "cache_read_input_tokens": 36863,
          "cache_creation_input_tokens": 1930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1930
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

_source line 47 · 2026-05-20T04:22:27.292Z_

<details><summary>↩ Tool result · `toolu_01QdpkWAzUgEJ2uZNVnxV5cH`</summary>

```text
Web search results for query: "NLDD reasoning horizon Ye 2602.11201 natural language degradation experimental setup limitations benchmarks"

Links: [{"title":"[2602.11201] Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning","url":"https://arxiv.org/abs/2602.11201"},{"title":"Donald Ye — AI Interpretability Researcher","url":"https://donaldye.com/"},{"title":"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning","url":"https://arxiv.org/pdf/2602.11201"},{"title":"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2602.11201"},{"title":"Intrinsic Stability Limits of Autoregressive Reasoning: Structural Consequences for Long-Horizon Execution","url":"https://arxiv.org/pdf/2602.06413"},{"title":"[2602.06413] Intrinsic Stability Limits of Autoregressive Reasoning: Structural Consequences for Long-Horizon Execution","url":"https://arxiv.org/abs/2602.06413"}]

Based on the search results, here's what I found about the paper 2602.11201:

## Overview

The paper proposes Normalized Logit Difference Decay (NLDD), a metric that measures whether individual reasoning steps are faithful to the model's decision-making process by corrupting individual reasoning steps from the explanation and measuring how much the model's confidence in its answer drops.

## Reasoning Horizon Finding

Testing three model families across syntactic, logical, and arithmetic tasks, the researchers discovered a consistent Reasoning Horizon (k*) at 70-85% of chain length, beyond which reasoning tokens have little or negative effect on the final answer.

## Experimental Setup & Benchmarks

The experimental setup tested three model families across syntactic, logical, and arithmetic tasks. The main results show that Llama and DeepSeek maintain high faithfulness (Positive NLDD), while Gemma exhibits anti-faithful behavior (Negative NLDD) on logical tasks despite high accuracy.

## Key Limitations

The research reveals important limitations: models can encode correct internal representations while completely failing the task, and accuracy alone does not reveal whether a model actually reasons through its chain. Additionally, there is a dissociation between internal linear separability and external performance (termed the Mapping Gap), where linear probes on hidden states can recover task-relevant information with high accuracy while the model achieves poor accuracy on the actual task.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "976c35d9-80a6-4d44-bd34-5cecdc0d5a22",
  "isSidechain": false,
  "promptId": "cf291cc7-d8bd-4cfb-9677-4b45d023f341",
  "type": "user",
  "uuid": "67bfd0dd-3442-4505-9ff7-4bce77030378",
  "toolUseResult": {
    "query": "NLDD reasoning horizon Ye 2602.11201 natural language degradation experimental setup limitations benchmarks",
    "results": [
      {
        "tool_use_id": "srvtoolu_011cGwtSpKDR3wCeEYxuoUrB",
        "content": [
          {
            "title": "[2602.11201] Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/abs/2602.11201"
          },
          {
            "title": "Donald Ye — AI Interpretability Researcher",
            "url": "https://donaldye.com/"
          },
          {
            "title": "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/pdf/2602.11201"
          },
          {
            "title": "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2602.11201"
          },
          {
            "title": "Intrinsic Stability Limits of Autoregressive Reasoning: Structural Consequences for Long-Horizon Execution",
            "url": "https://arxiv.org/pdf/2602.06413"
          },
          {
            "title": "[2602.06413] Intrinsic Stability Limits of Autoregressive Reasoning: Structural Consequences for Long-Horizon Execution",
            "url": "https://arxiv.org/abs/2602.06413"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper 2602.11201:\n\n## Overview\n\nThe paper proposes Normalized Logit Difference Decay (NLDD), a metric that measures whether individual reasoning steps are faithful to the model's decision-making process by corrupting individual reasoning steps from the explanation and measuring how much the model's confidence in its answer drops.\n\n## Reasoning Horizon Finding\n\nTesting three model families across syntactic, logical, and arithmetic tasks, the researchers discovered a consistent Reasoning Horizon (k*) at 70-85% of chain length, beyond which reasoning tokens have little or negative effect on the final answer.\n\n## Experimental Setup & Benchmarks\n\nThe experimental setup tested three model families across syntactic, logical, and arithmetic tasks. The main results show that Llama and DeepSeek maintain high faithfulness (Positive NLDD), while Gemma exhibits anti-faithful behavior (Negative NLDD) on logical tasks despite high accuracy.\n\n## Key Limitations\n\nThe research reveals important limitations: models can encode correct internal representations while completely failing the task, and accuracy alone does not reveal whether a model actually reasons through its chain. Additionally, there is a dissociation between internal linear separability and external performance (termed the Mapping Gap), where linear probes on hidden states can recover task-relevant information with high accuracy while the model achieves poor accuracy on the actual task."
    ],
    "durationSeconds": 7.824670020999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "976c35d9-80a6-4d44-bd34-5cecdc0d5a22",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-20T04:22:29.666Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RwXTU6aKBdaRegU9DvKFvq`</summary>

```json
{
  "query": "\"chain of thought faithfulness\" reviewer criticism OpenReview 2025 2026 experimental weaknesses common issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67bfd0dd-3442-4505-9ff7-4bce77030378",
  "isSidechain": false,
  "requestId": "req_011CbDBWEWrsDFjGDHRpnAb4",
  "type": "assistant",
  "uuid": "82d4e1a6-02e1-423e-9c54-73ae18747924",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XMXvtQuHihYh8gCaCBkTHA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 726,
      "cache_read_input_tokens": 38793,
      "output_tokens": 75,
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
          "output_tokens": 75,
          "cache_read_input_tokens": 38793,
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

_source line 49 · 2026-05-20T04:22:37.799Z_

<details><summary>↩ Tool result · `toolu_01RwXTU6aKBdaRegU9DvKFvq`</summary>

```text
Web search results for query: ""chain of thought faithfulness" reviewer criticism OpenReview 2025 2026 experimental weaknesses common issues"

Links: [{"title":"Chain-of-Thought Reasoning In The Wild Is Not Always Faithful | OpenReview","url":"https://openreview.net/forum?id=emjPKK11Oo"},{"title":"Measuring Faithfulness in Chain-of-Thought Reasoning | OpenReview","url":"https://openreview.net/forum?id=ZZcvsN27u3"},{"title":"Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting | OpenReview","url":"https://openreview.net/forum?id=bzs4uPLXvi"},{"title":"Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning | OpenReview","url":"https://openreview.net/forum?id=k3dzpooeQL"},{"title":"On the Hardness of Faithful Chain-of-Thought Reasoning in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=1OyE9IK0kx"},{"title":"Chain-of-Thought Unfaithfulness as Disguised Accuracy | OpenReview","url":"https://openreview.net/forum?id=ydcrP55u2e"},{"title":"[2503.08679] Chain-of-Thought Reasoning In The Wild Is Not Always Faithful","url":"https://arxiv.org/abs/2503.08679"},{"title":"FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning | OpenReview","url":"https://openreview.net/forum?id=lN3yKqqzF1"},{"title":"Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?","url":"https://arxiv.org/pdf/2603.22582"}]

Based on the web search results, here are key findings regarding chain-of-thought (CoT) faithfulness, reviewer criticisms, and experimental weaknesses from recent OpenReview papers and related research (2023-2026):

## Core Issues with CoT Faithfulness

Recent studies indicate that models can omit mentioning explicit bias in their outputs, revealing that verbalized reasoning can sometimes give an incorrect picture of how models arrive at conclusions. More broadly, unfaithful CoT can occur on realistic, non-adversarial prompts without artificial bias.

Production models exhibit surprisingly high rates of post-hoc rationalization, with GPT-4o-mini showing 13% and Haiku 3.5 showing 7%, while even frontier models like Gemini 2.5 Flash (2.17%) and ChatGPT-4o (0.49%) are not entirely faithful.

## Common Experimental Weaknesses

Models show large variation across tasks in how strongly they condition on the CoT when predicting their answer, sometimes relying heavily on the CoT and other times primarily ignoring it. Additionally, as models become larger and more capable, they produce less faithful reasoning on most tasks studied.

Research has found that LLMs exhibit a scaling-then-inverse-scaling relationship between model size and faithfulness measures, with some 13 billion parameter models showing increased faithfulness compared to both smaller and larger models, though scaling trends for CoT faithfulness appear to vary depending on specific conditions and model families.

## Detection and Evaluation Challenges

Prior studies have focused on mechanism-level analyses showing that CoTs can be unfaithful, but leave open the practical challenge of deciding whether a specific trajectory is faithful to the internal reasoning of the model. Faithfulness rates vary widely across model families, ranging from 39.7% to 89.9%, with consistency hints and sycophancy hints exhibiting the lowest acknowledgment rates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82d4e1a6-02e1-423e-9c54-73ae18747924",
  "isSidechain": false,
  "promptId": "cf291cc7-d8bd-4cfb-9677-4b45d023f341",
  "type": "user",
  "uuid": "0a324d53-9437-4bfe-b366-16edd40cb8a7",
  "toolUseResult": {
    "query": "\"chain of thought faithfulness\" reviewer criticism OpenReview 2025 2026 experimental weaknesses common issues",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DT4sNxy9fWQhC5X9PK4vR2",
        "content": [
          {
            "title": "Chain-of-Thought Reasoning In The Wild Is Not Always Faithful | OpenReview",
            "url": "https://openreview.net/forum?id=emjPKK11Oo"
          },
          {
            "title": "Measuring Faithfulness in Chain-of-Thought Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=ZZcvsN27u3"
          },
          {
            "title": "Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting | OpenReview",
            "url": "https://openreview.net/forum?id=bzs4uPLXvi"
          },
          {
            "title": "Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=k3dzpooeQL"
          },
          {
            "title": "On the Hardness of Faithful Chain-of-Thought Reasoning in Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=1OyE9IK0kx"
          },
          {
            "title": "Chain-of-Thought Unfaithfulness as Disguised Accuracy | OpenReview",
            "url": "https://openreview.net/forum?id=ydcrP55u2e"
          },
          {
            "title": "[2503.08679] Chain-of-Thought Reasoning In The Wild Is Not Always Faithful",
            "url": "https://arxiv.org/abs/2503.08679"
          },
          {
            "title": "FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=lN3yKqqzF1"
          },
          {
            "title": "Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?",
            "url": "https://arxiv.org/pdf/2603.22582"
          }
        ]
      },
      "Based on the web search results, here are key findings regarding chain-of-thought (CoT) faithfulness, reviewer criticisms, and experimental weaknesses from recent OpenReview papers and related research (2023-2026):\n\n## Core Issues with CoT Faithfulness\n\nRecent studies indicate that models can omit mentioning explicit bias in their outputs, revealing that verbalized reasoning can sometimes give an incorrect picture of how models arrive at conclusions. More broadly, unfaithful CoT can occur on realistic, non-adversarial prompts without artificial bias.\n\nProduction models exhibit surprisingly high rates of post-hoc rationalization, with GPT-4o-mini showing 13% and Haiku 3.5 showing 7%, while even frontier models like Gemini 2.5 Flash (2.17%) and ChatGPT-4o (0.49%) are not entirely faithful.\n\n## Common Experimental Weaknesses\n\nModels show large variation across tasks in how strongly they condition on the CoT when predicting their answer, sometimes relying heavily on the CoT and other times primarily ignoring it. Additionally, as models become larger and more capable, they produce less faithful reasoning on most tasks studied.\n\nResearch has found that LLMs exhibit a scaling-then-inverse-scaling relationship between model size and faithfulness measures, with some 13 billion parameter models showing increased faithfulness compared to both smaller and larger models, though scaling trends for CoT faithfulness appear to vary depending on specific conditions and model families.\n\n## Detection and Evaluation Challenges\n\nPrior studies have focused on mechanism-level analyses showing that CoTs can be unfaithful, but leave open the practical challenge of deciding whether a specific trajectory is faithful to the internal reasoning of the model. Faithfulness rates vary widely across model families, ranging from 39.7% to 89.9%, with consistency hints and sycophancy hints exhibiting the lowest acknowledgment rates."
    ],
    "durationSeconds": 8.126691174000007,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "82d4e1a6-02e1-423e-9c54-73ae18747924",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-20T04:22:40.321Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E12dnQHm9kx8BAgLtr3iFc`</summary>

```json
{
  "query": "DeepSeek R1 Distill Qwen 7B hidden state probing activation extraction GPU memory requirements 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a324d53-9437-4bfe-b366-16edd40cb8a7",
  "isSidechain": false,
  "requestId": "req_011CbDBX1TpLaSfHQKCHdyhw",
  "type": "assistant",
  "uuid": "bf19a8c9-d505-47db-bc38-956e750a0f00",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWMjD5z6TjNCm4hWvUYJrV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1013,
      "cache_read_input_tokens": 39519,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1013,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 39519,
          "cache_creation_input_tokens": 1013,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1013
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

_source line 51 · 2026-05-20T04:22:47.191Z_

<details><summary>↩ Tool result · `toolu_01E12dnQHm9kx8BAgLtr3iFc`</summary>

```text
Web search results for query: "DeepSeek R1 Distill Qwen 7B hidden state probing activation extraction GPU memory requirements 2026"

Links: [{"title":"GPU Requirements for Running DeepSeek Locally Explained | Ventus Servers","url":"https://ventusserver.com/for-running-deepseek-locally/"},{"title":"DeepSeek R1 Local Deployment: Complete Guide 2026 | SitePoint","url":"https://www.sitepoint.com/deepseek-r1-local-deployment-guide-2026/"},{"title":"DeepSeek R1 Hardware Guide: Best GPUs for Private, Local Reasoning","url":"https://aidevdayindia.org/blogs/deepseek-developer-ecosystem-guide/hardware-requirements-for-running-deepseek-r1-locally.html"},{"title":"Running DeepSeek R1 Locally: Hardware Requirements, Quantization, and Real Throughput | Groundy","url":"https://groundy.com/articles/running-deepseek-r1-locally-hardware-requirements-quantization-and-real-throughput/"},{"title":"DeepSeek R1 RTX 4090 vs Apple M3 Max: Benchmark & Performance Guide","url":"https://www.sitepoint.com/deepseek-r1-consumer-gpus-rtx4090-m3max/"},{"title":"DeepSeek R1 VRAM Requirements — 7B to 671B Hardware Guide | Will It Run AI Blog","url":"https://willitrunai.com/blog/deepseek-r1-vram-requirements-guide"},{"title":"DeepSeek Models Guide: R1, V3, and Coder | InsiderLLM","url":"https://insiderllm.com/guides/deepseek-models-guide/"}]

Based on the search results, here's what I found regarding DeepSeek R1 Distill Qwen 7B GPU memory requirements:

## GPU Memory Requirements

The DeepSeek-R1-Distill-Qwen-7B model requires roughly 3.3GB of base VRAM but practically demands 8GB or higher for reliable operation. More specifically, minimum viable specs for the 7B Q4 variant are 16 GB of system RAM and 8 GB of VRAM.

The memory footprint varies depending on quantization level:
- DeepSeek R1 7B needs 4GB at Q4 and 14GB at FP16.
- At FP16 (16-bit floating point), a 7B model requires approximately 14GB.

## Hardware Recommendations

The NVIDIA RTX 3070 Ti with 8GB memory represents the lower bound, while 10-12GB provides safer margins for context expansion. Additionally, for the "Distilled" 7B version, you only need an NVIDIA GPU with 6GB+ VRAM (like an RTX 3060) or a Mac with 8GB+ RAM.

**Note:** The search results provided information about GPU memory requirements for general inference, but did not contain specific information about hidden state probing, activation extraction techniques, or the additional memory overhead these specific operations might require. For detailed technical information about those specific use cases, you may need to consult research papers or specialized documentation on neural network probing methodologies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf19a8c9-d505-47db-bc38-956e750a0f00",
  "isSidechain": false,
  "promptId": "cf291cc7-d8bd-4cfb-9677-4b45d023f341",
  "type": "user",
  "uuid": "5adaf5f6-b2db-4fe1-989d-cc38887fb2e3",
  "toolUseResult": {
    "query": "DeepSeek R1 Distill Qwen 7B hidden state probing activation extraction GPU memory requirements 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FpVYj1szFkESb5yS59CDYD",
        "content": [
          {
            "title": "GPU Requirements for Running DeepSeek Locally Explained | Ventus Servers",
            "url": "https://ventusserver.com/for-running-deepseek-locally/"
          },
          {
            "title": "DeepSeek R1 Local Deployment: Complete Guide 2026 | SitePoint",
            "url": "https://www.sitepoint.com/deepseek-r1-local-deployment-guide-2026/"
          },
          {
            "title": "DeepSeek R1 Hardware Guide: Best GPUs for Private, Local Reasoning",
            "url": "https://aidevdayindia.org/blogs/deepseek-developer-ecosystem-guide/hardware-requirements-for-running-deepseek-r1-locally.html"
          },
          {
            "title": "Running DeepSeek R1 Locally: Hardware Requirements, Quantization, and Real Throughput | Groundy",
            "url": "https://groundy.com/articles/running-deepseek-r1-locally-hardware-requirements-quantization-and-real-throughput/"
          },
          {
            "title": "DeepSeek R1 RTX 4090 vs Apple M3 Max: Benchmark & Performance Guide",
            "url": "https://www.sitepoint.com/deepseek-r1-consumer-gpus-rtx4090-m3max/"
          },
          {
            "title": "DeepSeek R1 VRAM Requirements — 7B to 671B Hardware Guide | Will It Run AI Blog",
            "url": "https://willitrunai.com/blog/deepseek-r1-vram-requirements-guide"
          },
          {
            "title": "DeepSeek Models Guide: R1, V3, and Coder | InsiderLLM",
            "url": "https://insiderllm.com/guides/deepseek-models-guide/"
          }
        ]
      },
      "Based on the search results, here's what I found regarding DeepSeek R1 Distill Qwen 7B GPU memory requirements:\n\n## GPU Memory Requirements\n\nThe DeepSeek-R1-Distill-Qwen-7B model requires roughly 3.3GB of base VRAM but practically demands 8GB or higher for reliable operation. More specifically, minimum viable specs for the 7B Q4 variant are 16 GB of system RAM and 8 GB of VRAM.\n\nThe memory footprint varies depending on quantization level:\n- DeepSeek R1 7B needs 4GB at Q4 and 14GB at FP16.\n- At FP16 (16-bit floating point), a 7B model requires approximately 14GB.\n\n## Hardware Recommendations\n\nThe NVIDIA RTX 3070 Ti with 8GB memory represents the lower bound, while 10-12GB provides safer margins for context expansion. Additionally, for the \"Distilled\" 7B version, you only need an NVIDIA GPU with 6GB+ VRAM (like an RTX 3060) or a Mac with 8GB+ RAM.\n\n**Note:** The search results provided information about GPU memory requirements for general inference, but did not contain specific information about hidden state probing, activation extraction techniques, or the additional memory overhead these specific operations might require. For detailed technical information about those specific use cases, you may need to consult research papers or specialized documentation on neural network probing methodologies."
    ],
    "durationSeconds": 6.8651537700000045,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bf19a8c9-d505-47db-bc38-956e750a0f00",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-20T04:22:49.611Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014RHHrp5RPFZhU9Mx5B9t6J`</summary>

```json
{
  "query": "QwQ-32B hidden state extraction probing GPU memory activation caching requirements inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5adaf5f6-b2db-4fe1-989d-cc38887fb2e3",
  "isSidechain": false,
  "requestId": "req_011CbDBXhbofbfMvRH5EyYB4",
  "type": "assistant",
  "uuid": "04d571ad-47e4-4f0b-869a-9d1f57398886",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UfB7cZM4g3G9XSpyFGJwqu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 896,
      "cache_read_input_tokens": 40532,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 896,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 40532,
          "cache_creation_input_tokens": 896,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 896
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

_source line 53 · 2026-05-20T04:22:57.008Z_

<details><summary>↩ Tool result · `toolu_014RHHrp5RPFZhU9Mx5B9t6J`</summary>

```text
Web search results for query: "QwQ-32B hidden state extraction probing GPU memory activation caching requirements inference"

Links: [{"title":"QwQ-32B: A Breakthrough in Dense Language Models | by Pan Xinghan | Medium","url":"https://medium.com/@sampan090611/qwq-32b-a-breakthrough-in-dense-language-models-a451f639ddfb"},{"title":"nm-testing/QwQ-32B-FP8-dynamic · Hugging Face","url":"https://huggingface.co/nm-testing/QwQ-32B-FP8-dynamic"},{"title":"Vezora/QwQ-32B-Preview-fp8-W8A16 · Hugging Face","url":"https://huggingface.co/Vezora/QwQ-32B-Preview-fp8-W8A16"},{"title":"Qwen/QwQ-32B-Preview · Inference Speed Benchmark and GPU memeory usage","url":"https://huggingface.co/Qwen/QwQ-32B-Preview/discussions/8"},{"title":"How to finetune QWQ32B with 24g VRAM · Issue #1964 · unslothai/unsloth","url":"https://github.com/unslothai/unsloth/issues/1964"},{"title":"[Bug]: The qwq-32b-q4_k_m.gguf quantized model is not supported. · Issue #15015 · vllm-project/vllm","url":"https://github.com/vllm-project/vllm/issues/15015"},{"title":"QwQ-32B-Preview | EvalScope","url":"https://evalscope.readthedocs.io/en/latest/experiments/speed_benchmark/QwQ-32B-Preview.html"},{"title":"What GPU is required to run the Qwen/QwQ-32B model ...","url":"https://jarvislabs.ai/ai-faqs/what-gpu-is-required-to-run-qwen-qwq-32b-model-from-hugging-face"},{"title":"Run & Finetune QwQ-32B with Bug Fixes","url":"https://unsloth.ai/blog/qwq-32b"}]

Based on the search results, here's what I found regarding QwQ-32B's GPU memory, activation, and inference requirements:

## GPU Memory Requirements

For full precision, you need approximately 80GB of memory for inference at 16-bit, half that for 8-bit, and a quarter that for 4-bit. When tested on an Nvidia L40S GPU with 48GB of memory, the full version of QwQ-32B encountered memory limitations, and running the full model on a single GPU is impractical; a multi-GPU setup (two or three GPUs) might be necessary.

## KV Cache and Activation Requirements

The model's heavy FP16 quantized version, which includes a kv cache for speeding up generation, exceeds available memory. Inference speed and GPU memory usage vary significantly with input length - generating 2048 tokens requires 61.58GB with a 1-token prompt, scaling up to 74.47GB with a 30,720-token prompt.

## Quantization Options

FP8 quantization reduces the number of bits per parameter from 16 to 8, reducing GPU memory requirements by approximately 50%. The quantized Q4_K_M version strikes a balance by reducing the memory footprint while maintaining reasonable performance.

The search results focus on GPU memory requirements and KV cache considerations but don't contain specific information about hidden state extraction probing techniques or activation caching strategies for QwQ-32B.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04d571ad-47e4-4f0b-869a-9d1f57398886",
  "isSidechain": false,
  "promptId": "cf291cc7-d8bd-4cfb-9677-4b45d023f341",
  "type": "user",
  "uuid": "8df216fd-b78e-4100-8bb6-10ca4b52a058",
  "toolUseResult": {
    "query": "QwQ-32B hidden state extraction probing GPU memory activation caching requirements inference",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YDsTofTUoiCQM6rhf5kwre",
        "content": [
          {
            "title": "QwQ-32B: A Breakthrough in Dense Language Models | by Pan Xinghan | Medium",
            "url": "https://medium.com/@sampan090611/qwq-32b-a-breakthrough-in-dense-language-models-a451f639ddfb"
          },
          {
            "title": "nm-testing/QwQ-32B-FP8-dynamic · Hugging Face",
            "url": "https://huggingface.co/nm-testing/QwQ-32B-FP8-dynamic"
          },
          {
            "title": "Vezora/QwQ-32B-Preview-fp8-W8A16 · Hugging Face",
            "url": "https://huggingface.co/Vezora/QwQ-32B-Preview-fp8-W8A16"
          },
          {
            "title": "Qwen/QwQ-32B-Preview · Inference Speed Benchmark and GPU memeory usage",
            "url": "https://huggingface.co/Qwen/QwQ-32B-Preview/discussions/8"
          },
          {
            "title": "How to finetune QWQ32B with 24g VRAM · Issue #1964 · unslothai/unsloth",
            "url": "https://github.com/unslothai/unsloth/issues/1964"
          },
          {
            "title": "[Bug]: The qwq-32b-q4_k_m.gguf quantized model is not supported. · Issue #15015 · vllm-project/vllm",
            "url": "https://github.com/vllm-project/vllm/issues/15015"
          },
          {
            "title": "QwQ-32B-Preview | EvalScope",
            "url": "https://evalscope.readthedocs.io/en/latest/experiments/speed_benchmark/QwQ-32B-Preview.html"
          },
          {
            "title": "What GPU is required to run the Qwen/QwQ-32B model ...",
            "url": "https://jarvislabs.ai/ai-faqs/what-gpu-is-required-to-run-qwen-qwq-32b-model-from-hugging-face"
          },
          {
            "title": "Run & Finetune QwQ-32B with Bug Fixes",
            "url": "https://unsloth.ai/blog/qwq-32b"
          }
        ]
      },
      "Based on the search results, here's what I found regarding QwQ-32B's GPU memory, activation, and inference requirements:\n\n## GPU Memory Requirements\n\nFor full precision, you need approximately 80GB of memory for inference at 16-bit, half that for 8-bit, and a quarter that for 4-bit. When tested on an Nvidia L40S GPU with 48GB of memory, the full version of QwQ-32B encountered memory limitations, and running the full model on a single GPU is impractical; a multi-GPU setup (two or three GPUs) might be necessary.\n\n## KV Cache and Activation Requirements\n\nThe model's heavy FP16 quantized version, which includes a kv cache for speeding up generation, exceeds available memory. Inference speed and GPU memory usage vary significantly with input length - generating 2048 tokens requires 61.58GB with a 1-token prompt, scaling up to 74.47GB with a 30,720-token prompt.\n\n## Quantization Options\n\nFP8 quantization reduces the number of bits per parameter from 16 to 8, reducing GPU memory requirements by approximately 50%. The quantized Q4_K_M version strikes a balance by reducing the memory footprint while maintaining reasonable performance.\n\nThe search results focus on GPU memory requirements and KV cache considerations but don't contain specific information about hidden state extraction probing techniques or activation caching strategies for QwQ-32B."
    ],
    "durationSeconds": 7.392416060999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "04d571ad-47e4-4f0b-869a-9d1f57398886",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 54 · 2026-05-20T04:22:57.010Z_

```json
{
  "parentUuid": "8df216fd-b78e-4100-8bb6-10ca4b52a058",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "d7ca9aa6-945d-48a2-b5be-77b836564ec6",
  "timestamp": "2026-05-20T04:22:57.010Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness  ## Description When a reasoning model gets the right answer, is i…",
  "leafUuid": "d7ca9aa6-945d-48a2-b5be-77b836564ec6",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Information-Contribution Gap for CoT faithfulness",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb"
}
```

---

### Tool call

_source line 57 · 2026-05-20T04:23:00.694Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SZf48ArCjiAd7P6UraU8a3`</summary>

```json
{
  "query": "hidden state activation storage fp16 probing experiment large scale 4 layers reasoning model terabytes disk space 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7ca9aa6-945d-48a2-b5be-77b836564ec6",
  "isSidechain": false,
  "requestId": "req_011CbDBYRZvpyC2e3nkkzs88",
  "type": "assistant",
  "uuid": "2d31895f-06f9-4c02-9e64-bec6b84cc231",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GKzEwSLJ6kWFrAjApZewc3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1085,
      "cache_read_input_tokens": 41428,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1085,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 41428,
          "cache_creation_input_tokens": 1085,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1085
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

_source line 58 · 2026-05-20T04:23:08.142Z_

<details><summary>↩ Tool result · `toolu_01SZf48ArCjiAd7P6UraU8a3`</summary>

```text
Web search results for query: "hidden state activation storage fp16 probing experiment large scale 4 layers reasoning model terabytes disk space 2025 2026"

Links: [{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"},{"title":"Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification | OpenReview","url":"https://openreview.net/forum?id=O6I0Av7683"},{"title":"Reasoning Models Know When They're Right: Probing Hidden States for   Self-Verification","url":"https://arxiv.org/pdf/2504.05419"},{"title":"Temporal Predictors of Outcome in Reasoning Language Models","url":"https://arxiv.org/pdf/2511.14773"},{"title":"M-A-P A Survey on Latent Reasoning","url":"https://www.nju-link.com/zh/publication/zhu-2025-surveylatentreasoning/zhu-2025-surveylatentreasoning.pdf"},{"title":"Therefore I am. I Think","url":"https://arxiv.org/pdf/2604.01202"},{"title":"Probing LLM Hidden States","url":"https://apxml.com/courses/how-to-build-a-large-language-model/chapter-23-analyzing-model-behavior/probing-internal-representations"},{"title":"Every Activation Boosted: Scaling General Reasoner to 1 Trillion Open Language Foundation","url":"https://arxiv.org/pdf/2510.22115"}]

Based on my search results, I found several relevant papers on hidden state activation probing in reasoning models from 2025-2026:

## Key Findings:

**Hidden State Probing Experiments:**
Models' hidden states encode correctness of future answers, enabling early prediction of correctness before the intermediate answer is fully formulated, and probes can be used as verifiers to decide whether to exit reasoning at intermediate answers during inference, reducing the number of inference tokens by 24%.

**Storage and Scale Considerations:**
The search results mention exchanges of full 2560-dimensional FP16 hidden states (≈40,960 bits each) in the context of large-scale models, though the specific terabyte-scale disk space requirements for storing activations across 4-layer reasoning models were not explicitly detailed in the retrieved papers.

**Reasoning Model Research (2025-2026):**
Recent advances in reasoning models, such as OpenAI's o1 and DeepSeek-R1, have demonstrated significant progress in complex reasoning capabilities. Those decisions can be probed from internal activations, and model behavior is steerable at inference without additional fine-tuning.

The results primarily focus on methodologies for probing hidden states in reasoning models and their applications for efficiency improvements, rather than detailed specifications about terabyte-scale storage requirements for specific model architectures.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d31895f-06f9-4c02-9e64-bec6b84cc231",
  "isSidechain": false,
  "promptId": "cf291cc7-d8bd-4cfb-9677-4b45d023f341",
  "type": "user",
  "uuid": "08595e52-2a61-4ab0-935f-6248eb92dfea",
  "toolUseResult": {
    "query": "hidden state activation storage fp16 probing experiment large scale 4 layers reasoning model terabytes disk space 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011T93zCnF7JcGSN1ieJsLya",
        "content": [
          {
            "title": "Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs",
            "url": "https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"
          },
          {
            "title": "Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification | OpenReview",
            "url": "https://openreview.net/forum?id=O6I0Av7683"
          },
          {
            "title": "Reasoning Models Know When They're Right: Probing Hidden States for   Self-Verification",
            "url": "https://arxiv.org/pdf/2504.05419"
          },
          {
            "title": "Temporal Predictors of Outcome in Reasoning Language Models",
            "url": "https://arxiv.org/pdf/2511.14773"
          },
          {
            "title": "M-A-P A Survey on Latent Reasoning",
            "url": "https://www.nju-link.com/zh/publication/zhu-2025-surveylatentreasoning/zhu-2025-surveylatentreasoning.pdf"
          },
          {
            "title": "Therefore I am. I Think",
            "url": "https://arxiv.org/pdf/2604.01202"
          },
          {
            "title": "Probing LLM Hidden States",
            "url": "https://apxml.com/courses/how-to-build-a-large-language-model/chapter-23-analyzing-model-behavior/probing-internal-representations"
          },
          {
            "title": "Every Activation Boosted: Scaling General Reasoner to 1 Trillion Open Language Foundation",
            "url": "https://arxiv.org/pdf/2510.22115"
          }
        ]
      },
      "Based on my search results, I found several relevant papers on hidden state activation probing in reasoning models from 2025-2026:\n\n## Key Findings:\n\n**Hidden State Probing Experiments:**\nModels' hidden states encode correctness of future answers, enabling early prediction of correctness before the intermediate answer is fully formulated, and probes can be used as verifiers to decide whether to exit reasoning at intermediate answers during inference, reducing the number of inference tokens by 24%.\n\n**Storage and Scale Considerations:**\nThe search results mention exchanges of full 2560-dimensional FP16 hidden states (≈40,960 bits each) in the context of large-scale models, though the specific terabyte-scale disk space requirements for storing activations across 4-layer reasoning models were not explicitly detailed in the retrieved papers.\n\n**Reasoning Model Research (2025-2026):**\nRecent advances in reasoning models, such as OpenAI's o1 and DeepSeek-R1, have demonstrated significant progress in complex reasoning capabilities. Those decisions can be probed from internal activations, and model behavior is steerable at inference without additional fine-tuning.\n\nThe results primarily focus on methodologies for probing hidden states in reasoning models and their applications for efficiency improvements, rather than detailed specifications about terabyte-scale storage requirements for specific model architectures."
    ],
    "durationSeconds": 7.442475301999977,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2d31895f-06f9-4c02-9e64-bec6b84cc231",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-20T04:23:10.984Z_

Now I have enough research context. Let me synthesize my analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08595e52-2a61-4ab0-935f-6248eb92dfea",
  "isSidechain": false,
  "requestId": "req_011CbDBZFErF5zfqb2Bu66qs",
  "type": "assistant",
  "uuid": "bd527a2a-a6da-4b6c-a04d-dbaa471563e6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HuncUzK94SYGQa5EJkZ25c",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 823,
      "cache_read_input_tokens": 42513,
      "output_tokens": 12575,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 823,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12575,
          "cache_read_input_tokens": 42513,
          "cache_creation_input_tokens": 823,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 823
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

_source line 60 · 2026-05-20T04:25:49.995Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now systematically analyze the proposal from the experimental design and technical execution perspective. I need to:

1. Evaluate baseline coverage
2. Evaluate experimental design completeness
3. Evaluate evaluation metrics
4. Evaluate ablation design
5. Evaluate feasibility (compute, data, time, storage)

Let me go through each carefully:

**Baselines proposed:**
- Random + majority-class
- Difficulty-only classifier
- Probe-trajectory-only (Chrabąszcz-style P*(t) features, no C(t))
- TTS-only (per-step marginal causal contribution without probe dimension)


- I'm noticing some gaps in the baseline coverage — the proposal references FaithCoT-Bench's 11 methods for supplementary validation but doesn't explicitly include all of them as direct baselines, and it's unclear whether CMI should be tested as a standalone baseline given how much the work differentiates from it. Also, NLDD appears only as a component of C(t) rather than as its own baseline, which seems like a missed comparison point.

For evaluation, they're using macro-F1 as the primary metric alongside confusion matrices and reliability diagrams, with Cohen's kappa to measure agreement between estimators, bootstrap confidence intervals on G*(t), and paired permutation tests with Bonferroni correction for statistical rigor.

The ablation study spans seven dimensions — probe architecture choices, layer selection, how well the C(t) estimators agree with each other and their individual performance under different weighting schemes, different gap normalization approaches, calibration methods, whether the probe targets correctness or answer content, and temporal resolution across various token positions.

Now I'm hitting a feasibility concern around storage that seems to be cut off mid-sentence. Looking at the storage requirements more carefully, even with longer chain-of-thought outputs from reasoning models, the per-example footprint stays around 1.6-2 MB across different model sizes, which is reasonable for the full dataset. Total examples: ~1288 × 5 models × 4 benchmarks = 25,760 examples
     - Total: 25,760 × 2 MB ≈ 50 GB. That's quite manageable.
   - Wait, but the proposal says 3-5 TB. Where does that come from? Maybe they're thinking of storing ALL token positions, not just 50 sampled ones. If each CoT is ~8000 tokens, and you store 4 layers × 4096 dim × 2 bytes × 8000 tokens = ~256 MB per example. 25,760 × 256 MB ≈ 6.4 TB. That's consistent with the 3-5 TB estimate.
   - But the proposal says "20-50 percentile-based positions" as primary, which would reduce to 50 positions → 50 GB. The 3-5 TB estimate likely includes token-level subsets, while the PCA/on-the-fly option at 1.5 TB is more reasonable.

Running QwQ-32B for activation extraction needs around 64-80 GB VRAM in fp16, which means at least 2 H100s or 1 H100 with quantization, though that might compromise probe accuracy. For the 671B validation subset with 500 examples across 3 layers, DeepSeek-R1-671B would require 8 H100s minimum with quantization, or significantly more resources in full precision.

The 50 H100-hour budget for the 671B work seems tight—at 20 H100s that's only 2.5 hours of wall-clock time for 500 examples, though efficient batching and FP8 might make it feasible. The activation storage for a 671B MoE model across 3 layers could be substantial, but since this is a stretch goal, the feasibility concerns are less critical.

Paraphrase generation costs around $800-1500 for Claude Haiku or GPT-4o-mini on a 40% stratified subset with 2-3 variants, which seems reasonable.

The timeline of 15-17 weeks with 2 researchers or 14 weeks with 1 researcher plus Claude is tight but workable given the phased approach and early gates. The compute budget of ~1050 H100-hours at $3/hour comes to roughly $3,200, which is very reasonable for this scope.

Now I'm flagging a key experimental design concern: measuring C(t) with prefix truncation for long chain-of-thought sequences is problematic. Reasoning models can generate 4000-32000 token CoTs, and truncating at 50 positions means 50 separate re-injections per example. For models like QwQ-32B, each re-injection with thousands of tokens in the prefix requires substantial compute, and the proposal doesn't explicitly address this challenge.

The sample sizes are also concerning—500 examples per benchmark across 5 models is reasonable overall, but when split by difficulty quintiles in Phase 2, each cell drops to ~100 examples per model-benchmark combination, which is thin for classification tasks with 2-3 categories. The proposal should include a statistical power analysis or at least acknowledge this limitation.

The rank-based normalization approach is sensible but has a real limitation: it discards magnitude information. If G*(t) at different timepoints has similar ranks but very different magnitudes, the rank-based method would miss that signal.  The proposal does note that shape is the primary signal and includes normalization ablations (rank vs. min-max vs. z-score) to test this, which helps address the concern.

There's also a question about what actually generalizes when probing across model families. The proposal evaluates a shared probe at layers L/4, L/2, 3L/4, and L, but Qwen and Llama have very different internal representations. If the probe is model-specific—which it has to be—then the cross-model generalization experiment trains on one model and tests on another, but it's unclear whether the probe itself transfers or just the G*(t) trajectory shape features.

Looking back at the baselines, I see the proposal includes random, majority-class, difficulty-only, probe-trajectory-only, and TTS-only classifiers. But there's no pure C(t)-trajectory-only baseline using just prefix truncation and paraphrase features without any probe information, which would show the marginal value of adding the probe dimension on top of behavioral causal curves alone.

For the paraphrase verification, the NLI-based semantic preservation check is a good idea, but the proposal needs to specify which NLI model is being used, what threshold determines acceptable preservation, and how failures are handled.

The sample sizes are concerning—GPQA-Diamond has only about 198 full examples across 5 models (roughly 40 per difficulty quintile), and AIME has around 90, which is quite sparse for classification tasks. The proposal should clarify whether these are meant as supplementary validation or if larger datasets are planned.

For the instruction-tuned control, using Qwen2.5-7B-Instruct with the assumption that G*(t) ≈ 0 is problematic because prior work shows instruction-tuned models already have substantial pre-CoT encoding with high AUC probes and successful steering capabilities.

Now I'm thinking through the MCT supplementary concordance check — the proposal allocates 500 examples to measure geometric separability peaks, but I need to clarify whether MCT uses the same activation extraction pipeline or requires separate computation, since that affects the overall computational budget.

The temporal resolution ablation across 5/10/20/35/50 positions plus token-level is thorough, though the computational cost scales linearly with each position tested for the causal intervention analysis.

Looking at the compute budget more carefully, the fine-grained temporal resolution becomes a significant bottleneck — especially with larger models like QwQ-32B, where 50-position analysis means 50 additional forward passes per example, multiplying the inference cost substantially compared to smaller 7B models. Now I'm realizing the actual bottleneck is the reasoning models themselves—QwQ-32B can generate extremely long outputs, so even a single forward pass with a multi-thousand token prefix and regeneration could take substantial time, and I need to account for whether the model actually needs to re-reason or just output the final answer when reinjecting truncated chains of thought. , this could be fast. But if the model continues reasoning from the truncation point, it could produce another long CoT. The protocol (Ballon et al.) measures next-token probabilities, which only requires a forward pass without generation. That's much faster.
   
   Let me reconsider: if C(t) via prefix truncation measures P(correct | CoT[:t]) via next-token probabilities (like Ballon et al.'s protocol of measuring the distribution over answer choices via next-token probabilities after reinjection), then each "re-injection" is just a forward pass, not a full generation. That's much cheaper.
   
   For a 32B model on H100, a forward pass through a prompt of ~4K tokens takes ~2-5s. So 154,560 forward passes × 3s ≈ 463,680s ≈ 129 hrs. For all 5 models, I'm looking at maybe 250-300 hrs total. The 250 hr budget for Phase 1 is tight but potentially feasible, especially if the instruction-tuned control and smaller models run much faster.

But there's a complication: models that produce long chains of thought—8K to 32K tokens—mean the prefixes I'm truncating at later points could be 16K+ tokens themselves. A forward pass through that many tokens on a 32B model takes substantially longer, maybe 10-20s each. That could push the compute requirements significantly higher. The proposal budgets 250 hrs for Phase 1 and separately 250 hrs for the NLDD 32B conditional, plus 50 hrs for MCT, which suggests some awareness that the 32B model is expensive, but the long CoT scenario might still be underestimated.

The trickier issue is how to define "position" for reasoning models with variable-length CoTs. Since these models produce chains of thought ranging from 500 tokens to 32,000 tokens, using percentile-based positions (10%, 20%, ..., 100% of CoT length) makes sense for normalization. But the actual compute cost scales with absolute token count, not percentile—so a 10% position in a 32K CoT means 3,200 tokens, while 10% in a 500-token CoT is only 50 tokens. Longer CoTs will dominate the compute budget. The proposal mentions Gjølbye-style length correction, which is good, but the compute implications of this variability need to be more explicitly acknowledged.

On the FaithCoT-Bench side, there's potential for instance-level validation since Qwen2.5-7B-Instruct appears in both the proposal and FaithCoT-Bench. If FaithCoT-Bench covers GSM8K or MATH-500, I should be able to test correlation with expert labels directly rather than falling back to dataset-level validation. I need to verify what benchmarks FaithCoT-Bench actually includes.

One more gap: the four benchmarks are all math-heavy (GSM8K, MATH-500, AIME) plus GPQA-Diamond for science. There's no commonsense reasoning benchmark here.

Looking at the phases more carefully, MMLU appears in Phase 0a but gets dropped in Phase 1, replaced by AIME. So the framework is still heavily weighted toward math and science tasks. A reviewer might legitimately question whether this generalizes to natural language reasoning like logical inference or reading comprehension.

Adding even one NL reasoning benchmark would strengthen the contribution, though I recognize the proposal's rationale—reasoning needs to be well-defined and ground truth unambiguous, which is harder for commonsense tasks. The NLDD feasibility gate in Phase 0a is smart design, but the proposal should clarify what the actual success criterion is—like specifying the SNR threshold on MMLU that would trigger fallback to the two-estimator approach.

The go/no-go criterion for Phase 0b is clear when d > 0.5 or d < 0.3, but there's a gap: what happens in the 0.3 to 0.5 range? That needs to be defined. I'm also concerned about the paraphrase model choice—relying on Claude Haiku or GPT-4o-mini introduces external API dependencies that could affect reproducibility if those models change or become unavailable, so considering an open-source alternative like a fine-tuned T5 would be more robust.

For the statistical testing, paired permutation tests with Bonferroni correction and bootstrap CIs are solid, and Cohen's kappa for inter-estimator agreement is good, but the proposal doesn't specify what test compares the G*(t) trajectory shapes themselves—whether that's DTW distance, functional ANOVA, or something else.

Now I'm weighing what's truly critical versus what's nice-to-have. The missing C(t)-only baseline is essential to validate the dual-stream claim, benchmark diversity is a real concern since everything is math and science with no natural language reasoning tasks, and there are sample size worries for GPQA-Diamond and AIME in the difficulty-conditioned analysis. The compute budget also needs clarification.

Moderate concerns include making the NLDD feasibility criterion more specific, defining what happens when d falls between 0.3-0.5, specifying the statistical test for trajectory shape comparison, and setting an NLI threshold for paraphrase quality. The 7-dimension ablation is comprehensive, the external validation approach with TTS cross-reference and difficulty partitioning is well-designed, the Phase 0a/0b gating strategy is solid, and using multiple C(t) estimators addresses the classifier-sensitivity issue nicely. The probe calibration via null-probe is well-motivated and the instruction-tuned control model makes sense.

I want to reconsider the proposal's distinction between TTS and prefix truncation for C(t)—that's actually well-articulated and worth noting.

The key insight is that TTS measures per-step marginal contribution while prefix truncation measures cumulative sufficiency, so a chain could have low individual step importance but still require the full sequence. The TTS cross-reference validation should explicitly test whether these two metrics disagree systematically, not just whether they correlate, which would strengthen the case for using prefix truncation.

Now I'm identifying the critical gaps: the main claim is that dual-stream P* plus C outperforms either alone, but there's no C(t)-only baseline to validate this.

Beyond that, the benchmarks are all math and science focused, which is defensible for unambiguous correctness but might draw reviewer concern about generalization. The sample sizes for GPQA-Diamond and AIME are also quite small for the planned quintile analysis. Finally, the compute budget for QwQ-32B might be tight given the long context lengths involved.

On the methodology side, I need to be more explicit about how trajectory shapes are actually compared—the proposal mentions effect size thresholds and shape features but doesn't specify the distance metric or statistical test. There are also some minor gaps around contingency planning for intermediate effect sizes and the NLDD feasibility criterion could be more precise. Using API models for paraphrasing introduces an external dependency, though that's a lower-priority concern.

Overall, I'm seeing this as having fixable issues rather than fundamental flaws—the main gaps are around the C(t)-only baseline and trajectory comparison methodology, but both are addressable with clarification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd527a2a-a6da-4b6c-a04d-dbaa471563e6",
  "isSidechain": false,
  "requestId": "req_011CbDBZFErF5zfqb2Bu66qs",
  "type": "assistant",
  "uuid": "6301d963-0695-4e5a-81d3-1245255bf3bf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HuncUzK94SYGQa5EJkZ25c",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 823,
      "cache_read_input_tokens": 42513,
      "output_tokens": 12575,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 823,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12575,
          "cache_read_input_tokens": 42513,
          "cache_creation_input_tokens": 823,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 823
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

_source line 61 · 2026-05-20T04:28:10.637Z_

Now I have sufficient research context to provide a thorough evaluation. Let me compile my analysis.

---

【状态】: 有缺陷待补救

【前置调研发现】
- **FaithCoT-Bench (ICLR 2026, 2510.04040)**: 实验设计包含 11 种检测方法 × 4 个模型（LLaMA3.1-8B, Qwen2.5-7B, GPT-4o-mini, Gemini 2.5 Flash），4 种 paradigm（counterfactual, logit-based, LLM-as-Judge, baseline），评估用 Cohen's kappa + 3 个互补指标；提供 1000+ expert-annotated trajectories 作为 ground truth。关键：其 Qwen2.5-7B 与 proposal 的 Qwen2.5-7B-Instruct 有直接重叠，instance-level validation 应可行。
- **TTS / "Can Aha Moments Be Fake?" (2510.24941)**: 在 R1-Distill-Qwen-7B/14B/Llama-8B 上做 per-step ATE，发现 AIME 仅 2.3% 步骤 TTS≥0.7。实验覆盖 GSM8K/MATH/AIME，与 proposal 高度重叠。其 per-step 粒度与 proposal 的 cumulative prefix 形成理论对比。
- **Chrabąszcz et al. (2605.18549)**: 在 Llama-8B-R1-Distill、Qwen3-4B/8B/14B 上用 60+ signal-processing features + MIL，max-pooling AUROC 91-97%。实验重要特点：用 template-based training data 实现 near-parity，避免昂贵的初始推理。**关键缺失：无任何 causal component。**
- **Yuan et al. (2605.09502)**: 4 种干预全部失败（activation steering, probe-guided best-of-N, self-correction, activation patching），覆盖 Qwen2.5 1.5B-72B + Llama-3.1-8B + Phi-3.5-mini + DeepSeek-R1-7B。Probe AUROC 0.95 (Qwen-3B), 0.852 (R1-7B)。审稿人/读者关注点：intervention failure 是否因为 probe 质量不够高还是信号本质 diagnostic。
- **Ballon et al. (2601.23163)**: 在 Qwen3-4B/8B/14B + gpt-oss-20B/120B 上做 truncation-reinjection，decile intervals（10 个等分位），核心控制条件：intact vs. shuffled vs. random vs. swapped。GPQA-Diamond 准确率 30.8-42.3% → 49.0-73.1%。**关键：该论文明确 disclaims faithfulness analysis，仅做信息积累刻画。**
- **Young (2603.20172)**: 3 个 classifier 在同一数据上产生 74.4%, 82.6%, 69.7% faithfulness rate；Cohen's kappa 最低 0.06 (sycophancy hints)。**调研启示：任何 faithfulness 分类实验必须报告 multi-classifier robustness。**
- **CMI / Sathyanarayanan et al. (2602.03994)**: ~50 examples 的 layerwise activation patching，发现 bypass regimes (CMI ≈ 0) 和 narrow reasoning windows。**实验规模太小，但方法论上建立了 structural vs. functional 的区分。**
- **Gjølbye et al. (2605.15454)**: 11 models × 3 domains，明确建立 length correction 作为 trajectory 分析的 prerequisite。ρ⊥ = +0.41 (code) vs. +0.05 (math)。
- **Thought Anchors (2506.19143)**: 100-rollout replacement sampling 做 per-sentence counterfactual importance，使用 black-box + white-box + causal attribution 三种互补方法。

- **调研总结**: 该领域当前的实验设计标准要求：(1) 多种 faithfulness 度量方法的 head-to-head 对比以应对 Young 的 classifier-sensitivity 发现；(2) 多模型/多 benchmark 覆盖（至少 3 个模型、3 个 benchmark）；(3) 明确的 control conditions（如 Ballon 的 shuffled/random/swapped 三控制）；(4) trajectory 分析必须做 length correction（Gjølbye 建立的共识）；(5) 审稿人普遍期望 instance-level 而非 dataset-level 的验证。Proposal 在大部分维度达标或超标，但在 baseline 完备性、benchmark 多样性、小样本 benchmark 的统计效力、trajectory 形状比较的统计方法论上存在可补救缺陷。

---

【缺陷 1】
- 类别: baseline 不足
- 问题: Proposal 的 classification baselines 包括 random/majority-class、difficulty-only、probe-trajectory-only (P*(t) features, no C(t))、TTS-only。但**缺少 C(t)-trajectory-only baseline**（仅使用 prefix truncation accuracy curve 的 trajectory features，不包含任何 probe 信息）。Proposal 的核心 claim 是 dual-stream (P* + C) 优于单流——已有 P*-only baseline 证明 C(t) 的增量价值，但缺少反向 ablation（C(t)-only baseline）来证明 P*(t) 的增量价值。这在逻辑上不对称：如果 C(t)-trajectory-only 已经能达到接近 ICG 的分类性能，那 probe 维度的价值就大打折扣。
- 严重度: 可补救
- 补救方案: 在 Phase 3 baselines 中增加第 (e) 项：**C(t)-trajectory-only baseline**——使用 prefix truncation C(t) 曲线的 trajectory features（initial value、slope、convergence rate、volatility 等，与 P*(t) baseline 使用相同的 feature extraction pipeline），不包含任何 probe 信息。此外建议增加 **(f) NLDD-only baseline**（如果 NLDD 通过 Phase 0a 可行性测试）。这样 baseline 体系变为：random → difficulty-only → P*-only → C(t)-only → TTS-only → ICG (full)，形成完整的 ablation ladder。计算开销几乎为零（特征已经提取，只需训练额外分类器）。
- 调研依据: FaithCoT-Bench 的实验设计中对其 4 种 paradigm（counterfactual, logit-based, LLM-as-Judge, baseline）每种都独立评估性能，确保每个 component 的增量贡献可验证。同样地，CMI 独立报告 structural mediation 结果，不与 behavioral baseline 混合。双向 ablation 是标准做法。

【缺陷 2】
- 类别: 实验设计不足
- 问题: Phase 1 的 4 个 benchmark（GSM8K, MATH-500, GPQA-Diamond, AIME）全部是 math/science domain。虽然 Phase 0a 包含 MMLU，但 MMLU 在 Phase 1 被替换为 AIME，导致 Phase 1 完全缺乏自然语言推理/常识推理类 benchmark。审稿人很可能质疑：ICG framework 是否仅适用于 math/science 场景？reasoning model 在 NL reasoning 任务上的 faithfulness patterns 可能与 math 截然不同（math 有清晰的步骤结构和 ground truth，NL reasoning 更模糊），而 proposal 的 claim 是 "the first framework capable of distinguishing faithful-correct from unfaithful-correct reasoning"——这个 claim 需要更广泛的任务覆盖来支撑。Gjølbye et al. 已经发现 difficulty-geometry coupling 是 domain-specific 的（code: ρ⊥=+0.41, math: +0.05），暗示 G*(t) 的行为也可能是 domain-dependent 的。
- 严重度: 可补救
- 补救方案: 在 Phase 1 中增加一个 NL reasoning benchmark。建议两个候选（选其一）：(a) **BBH (BIG-Bench Hard) 的 reasoning 子集**（如 logical deduction, tracking shuffled objects, date understanding）——约 250 examples，有明确 ground truth，reasoning model 在这些任务上有不同的 CoT 模式；(b) **ARC-Challenge**——需要多步推理，有明确答案，约 1172 test examples（可采样 500）。建议在 Phase 0a 时用 MMLU 的初步结果评估 NL 任务上 G*(t) 的信噪比，如果信噪比足够，Phase 1 将 AIME（仅 90 例，统计效力有限）降级为 supplementary，替换为 BBH 子集或 ARC-Challenge。这样 Phase 1 变为 GSM8K + MATH-500 + GPQA-Diamond + BBH/ARC (primary) + AIME (supplementary)。额外计算开销：约 30-50 H100-hours（5 models × 500 examples × 30 positions 的 truncation re-injection）。
- 调研依据: FaithCoT-Bench 横跨 math/science/commonsense 多种任务类型；TTS 论文也测试了 MMLU 等非数学任务。审稿人期望至少有一个非 math/science 的 benchmark 来支撑 generalizability claim。Gjølbye et al. 的 domain-specific 发现进一步强化了这个需求。

【缺陷 3】
- 类别: 实验设计不足（统计效力）
- 问题: GPQA-Diamond（~198 examples）和 AIME（~90 examples）样本量偏小。Phase 2 difficulty conditioning 将数据按 quintile 划分后，GPQA-Diamond 每个 quintile 仅 ~40 examples/model，AIME 仅 ~18 examples/model。对于 3-category 分类任务（pre-committed / genuine / post-hoc），每个 category 在每个 quintile 中可能仅有个位数 examples。Bootstrap CI 在如此小的样本上会很宽，d > 0.5 的检验功效（statistical power）可能不足。Proposal 虽然提到了 Bonferroni correction，但没有讨论 power analysis 或这些小样本的 interpretive limitations。
- 严重度: 可补救
- 补救方案: (1) 在论文中明确将 GPQA-Diamond 和 AIME 的 difficulty-conditioned 结果标注为 **supplementary/exploratory analysis**，primary difficulty conditioning claims 仅基于 GSM8K (500 examples) 和 MATH-500 (500 examples)；(2) 对 GPQA-Diamond 和 AIME 改用 **3-bin（easy/medium/hard）而非 5-quintile** 划分，将每 bin 样本量提升到 ~66 (GPQA) 和 ~30 (AIME)；(3) 报告 observed statistical power 或做 post-hoc power analysis；(4) 考虑对 GPQA-Diamond 和 AIME 使用 case study / qualitative trajectory visualization 而非 quantitative classification metrics 作为主要展示方式。无额外计算开销。
- 调研依据: 基于领域实验规范判断。FaithCoT-Bench 使用 1000+ annotated trajectories 正是为了确保统计效力。Young (2603.20172) 的发现——同一数据上 kappa 低至 0.06——进一步说明在小样本上分类器不稳定性会被放大。

【缺陷 4】
- 类别: 评估方案缺陷（trajectory 形状比较方法论）
- 问题: Proposal 的核心 diagnostic signal 是 G*(t) 的 trajectory shape（constant-high vs. converging-to-zero vs. widening）。但 proposal 没有明确说明如何**定量比较 trajectory shapes**。提到了 d > 0.5（Cohen's d on trajectory features）、shape features（initial value, slope, convergence rate, dC/dt locality）和 Chrabąszcz-style features，但没有指定：(a) 这些 features 如何从离散的 20-50 个时间点提取（线性回归 slope？分段拟合？）；(b) 是否使用 functional data analysis (FDA) 方法处理不同 CoT 长度的对齐问题；(c) 如果两个 phenomenon 的 trajectory 在某些 features 上区分度高但在其他 features 上重叠，如何综合判断 separability。这在 Phase 0b 的 go/no-go 决策中尤其关键——d > 0.5 是对哪个 feature 或 feature combination 的要求？
- 严重度: 可补救
- 补救方案: (1) 明确 trajectory feature extraction pipeline：建议参照 Chrabąszcz 的 signal-processing 方法，定义 ~10 个 canonical trajectory features（initial value G*(t=0.1), terminal value G*(t=1.0), linear slope via OLS, curvature via second derivative, max/min, volatility = std of first differences, convergence rate = exponential decay fit parameter, area under G*(t), crossing point = first t where |G*(t)| < threshold）；(2) Phase 0b 的 d > 0.5 criterion 应指定为：**在 10 个 canonical features 中至少 2 个** features 同时达到 d > 0.5 且 Bonferroni-corrected p < 0.01（proposal 已接近这个表述，但需要列出 specific features）；(3) 考虑补充 Dynamic Time Warping (DTW) 距离作为 trajectory similarity 的 holistic metric；(4) 报告 feature-level 和 trajectory-level 两种 separability 评估。无额外计算开销。
- 调研依据: Chrabąszcz et al. 使用 60+ signal-processing features 并发现 volatility, trend, steady-state, boundary transients, autocorrelation 最 informative。RQA (2602.06266) 使用 temporal features outperforming aggregates (36.94% vs 28.97%)。Microsoft (2604.05655) 使用 shape features 达到 0.852 AUC。这些论文都明确定义了 feature extraction pipeline，proposal 应对标。

【缺陷 5】
- 类别: 可行性问题（QwQ-32B compute budget）
- 问题: Phase 1 分配 250 H100-hours 覆盖 5 models × 4 benchmarks。但 QwQ-32B 的 prefix truncation re-injection 成本被低估。Reasoning models 产生的 CoT 通常很长（8K-32K tokens）。在后段 truncation positions（如 80% percentile），prefix 可能长达 6K-25K tokens。QwQ-32B 在 fp16 下需要 ~64-80 GB VRAM（2× H100），forward pass 通过 25K token prefix 需要 ~15-30 seconds。每个 QwQ-32B example 需要 ~30 个 truncation positions，每个 position 平均 ~10-15s forward pass → 每个 example ~5-7.5 minutes。4 benchmarks × ~1288 examples ÷ 5 models = ~1030 QwQ-32B examples，总计 ~85-130 hours 仅用于 QwQ-32B 的 truncation re-injection。加上 probe extraction、paraphrase stability、controls，QwQ-32B 可能占用 Phase 1 预算的 50-60%。
- 严重度: 可补救
- 补救方案: (1) 对 QwQ-32B 使用 **reduced temporal resolution**（如 15 positions 而非 30-50），在 temporal resolution ablation 中验证 15 vs. 30 vs. 50 的 macro-F1 差异；(2) 对 QwQ-32B 做 **Ballon et al. 式的 decile (10 position) 协议** 作为 primary，更高分辨率作为 supplementary subset；(3) 使用 **FP8 推理**降低 VRAM 需求至 1× H100，同时在 probe accuracy ablation 中验证 FP8 vs. FP16 hidden states 的 probe 性能差异；(4) 将 Phase 1 compute budget 上调至 **300-350 H100-hours**（增加 $150-300），或明确将 QwQ-32B 的 high-resolution 分析列为 supplementary。建议重新分配预算：Phase 1 → 320 hrs（+70 hrs），从 NLDD 32B conditional (250 hrs) 中调出（如果 NLDD 不在 32B 上运行则可直接回收）。
- 调研依据: Ballon et al. 在 gpt-oss-120B 上使用 decile intervals（10 positions），说明大模型用低分辨率是领域惯例。Gjølbye et al. 在 11 models 中也使用相对稀疏的采样点。

【缺陷 6】
- 类别: 评估方案缺陷（paraphrase quality control）
- 问题: C(t) 的 paraphrase perturbation 组件使用 "NLI-based semantic preservation verification"，但 proposal 未指定：(a) 具体使用哪个 NLI 模型；(b) entailment 阈值是多少；(c) 当 NLI 判定语义不保留时的处理策略（丢弃？重采样？）；(d) NLI 本身在 reasoning-heavy text 上的可靠性（数学推理步骤的 paraphrase 是否能被 NLI 模型准确评估）。此外，使用 Claude Haiku 或 GPT-4o-mini 作为 paraphrase 生成器引入了对闭源 API 的依赖，影响 reproducibility。
- 严重度: 可补救
- 补救方案: (1) 指定 NLI 模型：建议 **DeBERTa-v3-large-MNLI**（开源、广泛使用、reproducible），entailment threshold ≥ 0.8（双向 entailment 以确保 bidirectional semantic equivalence）；(2) 制定 fallback 策略：NLI 双向 entailment < 0.8 → 丢弃该 paraphrase，最多重采样 2 次，如果仍不通过则该 segment 不纳入 paraphrase C(t) 计算；(3) 报告 paraphrase acceptance rate 作为数据质量指标；(4) 对 reproducibility 关切，建议在 supplementary 中用一个开源 paraphrase 模型（如 Flan-T5-XL 或 Llama-3.1-8B-Instruct）做 spot check（~100 examples），验证 paraphrase 来源不影响 C(t) 结论。无显著额外计算开销（DeBERTa-v3 NLI 推理非常快；spot check ~10 GPU-hrs）。
- 调研依据: FaithCoT-Bench 的 Paraphrasing paradigm 使用了类似方法但明确定义了 semantic preservation criteria。Young (2603.20172) 的 classifier-sensitivity 发现暗示 paraphrase 质量的 variation 可能显著影响 faithfulness 判定。

【缺陷 7】
- 类别: 实验设计不足（go/no-go 灰色区间）
- 问题: Phase 0b 定义了清晰的 go/no-go：d > 0.5 → proceed to Phase 1；d < 0.3 → downscope to characterization paper。但 **0.3 ≤ d ≤ 0.5 的灰色区间**没有定义处理策略。此外，NLDD feasibility criterion（Phase 0a）仅描述为 "if SNR uninformative on MMLU, restrict NLDD to math/code or replace"，缺少具体的 quantitative threshold。
- 严重度: 可补救
- 补救方案: (1) 定义灰色区间策略：0.3 ≤ d ≤ 0.5 → **conditional proceed**，增加 Phase 0b 样本量至 2000 examples（从 1000），重新评估。如果扩大样本后仍 d < 0.5，则 downscope 但保留 dual-stream framework 作为方法论贡献（附带 "moderate effect size" caveat）；(2) NLDD feasibility criterion 具体化：NLDD 的 Spearman ρ with expected faithfulness ordering > 0.2 AND Cohen's d between correct-faithful vs. correct-unfaithful > 0.3 → pass；otherwise → restrict or replace。额外计算开销：最坏情况 conditional proceed 需多 ~15 H100-hrs。
- 调研依据: 基于领域实验规范判断。Well-designed empirical research 通常预注册明确的 decision rules，灰色区间的缺失会被 reviewers 视为方法论不严谨。

---

**总体评估（仅实验设计层面）：** 该 proposal 的实验设计整体上是**高质量的**——phased go/no-go 策略、多 C(t) estimator 设计（回应 Young 的 classifier-sensitivity）、instruction-tuned control model、7 维 ablation、length correction 等都是 well-thought-out 的选择。以上 7 个缺陷均为**可补救**的实验设计优化，其中缺陷 1（C(t)-only baseline）和缺陷 2（benchmark 多样性）是最可能被审稿人直接要求补充的实验，建议优先处理。缺陷 3-7 属于提升实验 rigor 的完善措施。总计额外计算开销约 40-80 H100-hours + 10 GPU-hrs spot check，在预算范围内可控。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6301d963-0695-4e5a-81d3-1245255bf3bf",
  "isSidechain": false,
  "requestId": "req_011CbDBZFErF5zfqb2Bu66qs",
  "type": "assistant",
  "uuid": "e7606eb6-4a45-4475-ac4d-60a23ae007ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HuncUzK94SYGQa5EJkZ25c",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 823,
      "cache_read_input_tokens": 42513,
      "output_tokens": 12575,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 823,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12575,
          "cache_read_input_tokens": 42513,
          "cache_creation_input_tokens": 823,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 823
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

_source line 62_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness  ## Description When a reasoning model gets the right answer, is i…",
  "leafUuid": "e7606eb6-4a45-4475-ac4d-60a23ae007ce",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb"
}
```

---

### Runtime record

_source line 63_

```json
{
  "type": "ai-title",
  "aiTitle": "Information-Contribution Gap for CoT faithfulness",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb"
}
```

---

### Runtime record

_source line 64_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness  ## Description When a reasoning model gets the right answer, is i…",
  "leafUuid": "e7606eb6-4a45-4475-ac4d-60a23ae007ce",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb"
}
```

---

### Runtime record

_source line 65_

```json
{
  "type": "ai-title",
  "aiTitle": "Information-Contribution Gap for CoT faithfulness",
  "sessionId": "ab0434e3-677a-4630-99d4-40b6b22473bb"
}
```

---
