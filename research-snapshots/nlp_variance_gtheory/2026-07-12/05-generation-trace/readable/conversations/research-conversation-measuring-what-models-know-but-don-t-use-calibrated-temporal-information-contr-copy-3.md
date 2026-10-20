# Research conversation: Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought F

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 66
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-3/a8d3cc8a-d625-4edc-ba71-1318a72e9ef0.jsonl`
- **Structured JSON:** [`41004dbf1eb3587aecd9.json`](../../sessions/41/41004dbf1eb3587aecd9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:19:16.028Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:19:16.028Z",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "content": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness\n\n## Description\nWhen a reasoning model gets the right answer, is its chain-of-thought the reason it succeeded — or did it already know the answer and generate decorative reasoning? No existing method can answer this question. Probe-only approaches (Chrabąszcz et al., 2605.18549) reveal what the model knows over time but are structurally blind to whether CoT caused the correct output. Causal-only approaches (TTS, Zhao et al. 2510.24941; NLDD, Ye et al. 2602.11201; Ballon et al. 2601.23163) measure what CoT does but cannot assess what the model already knew internally. Only a dual-stream framework — jointly tracking information availability AND causal contribution — can distinguish faithful-correct from unfaithful-correct reasoning. The Information-Contribution Gap (ICG) framework provides this.\n\nICG exploits a robust empirical finding: linear probes on hidden states reliably diagnose answer correctness (0.82-0.95 AUROC across four independent groups) yet causal interventions based on these probes consistently fail on reasoning-trained models (Cox et al. 2603.01437: negligible flip rates; Yuan et al. 2605.09502: all four intervention strategies fail). Rather than treating this diagnostic-causal gap as an obstacle, we make it the primary object of study.\n\nThe framework tracks two calibrated time-varying quantities across the CoT trajectory: P*(t), null-probe-calibrated correctness awareness, and C(t), causal contribution estimated via three complementary methods (prefix truncation following Ballon et al.'s three control conditions, paraphrase perturbation, NLDD). Their divergence G*(t) = P*(t) − C(t) produces phenomenon-specific temporal fingerprints, operationalizing Wang's (2604.15726) H1/H2 distinction: G*(t) >> 0 is latent-mediated (H1-consistent), G*(t) ≈ 0 is CoT-mediated (H2-consistent).\n\n**Core insight: the diagnostic contribution of G*(t) is its temporal trajectory shape, not its absolute magnitude.** P*(t) (probe AUROC) and C(t) (behavioral accuracy change) are measured via fundamentally different methods with non-commensurable scales. We address this via rank-based normalization as primary scheme, but more fundamentally, trajectory-shape profiles carry the diagnostic signal: a model that pre-encodes the answer shows a constant-high shape; genuine reasoning shows convergence toward zero; post-hoc rationalization shows widening. The shapes-over-magnitudes approach is validated by: entropy trajectory monotonicity predicting reliability regardless of absolute levels (+5.8pp, arXiv 2603.18940); RQA temporal features outperforming aggregates (36.94% vs. 28.97%, arXiv 2602.06266); Microsoft trajectory geometry achieving 0.852 AUC from shape features vs. 0.649 baseline (arXiv 2604.05655).\n\n**Why not just endpoint comparison or trivial combination?** Two reviewer objections are preempted: (1) \"Why not correlate pre-CoT probe accuracy with final correctness?\" — endpoint comparison detects unfaithfulness presence but collapses distinct failure *mechanisms* (pre-CoT encoding vs. rationalization vs. late shortcutting produce identical endpoints but distinct G*(t) shapes). (2) \"Why not just pair Chrabąszcz's probe trajectories with TTS step scores?\" — TTS measures *marginal* contribution (removing step *s* changes the answer), while prefix-truncation C(t) measures *cumulative sufficiency* (CoT[:t] is sufficient for correctness). A chain where every individual step has low TTS (each individually replaceable) could still have high cumulative C(t) (the ensemble is necessary). This cumulative-vs-marginal distinction is theoretically non-reducible and empirically grounded in the difference between Ballon et al.'s monotonic prefix curves and TTS's per-step ATE.\n\n**Structural vs. functional differentiation from CMI.** The CMI framework (Sathyanarayanan et al., 2602.03994) measures whether answer representations pass through CoT-aligned layers via layerwise activation patching — a *structural* question. ICG answers a *functional* question: does the CoT text causally contribute to behavioral correctness? This generates a testable prediction: models could show high CMI (representations routed through CoT-processing layers) but high G*(t) (CoT serves as timing scaffold rather than contributing semantic content). If confirmed, this would reveal a novel structural-functional dissociation in reasoning models.\n\n**Differentiation from Thought Anchors.** Thought Anchors (arXiv 2506.19143) measures per-sentence counterfactual importance via replacement sampling — identifying sentences with outsized causal influence on reasoning trajectory. This provides *within-CoT structural analysis* (which sentences matter to each other) but no *external reference* to the model's internal state. A thought anchor could be causally critical within the CoT but entirely redundant relative to what the model already knows — a distinction only ICG can make via the probe dimension.\n\n**Interpretive boundary.** G*(t) >> 0 means correctness-correlated information is present but not causally channeled through CoT. It does not entail the model \"decided to withhold\" — the information may exist as computational byproducts rather than semantically actionable knowledge. Chun et al.'s MCT geometric pulse finding (2602.20338) provides evidence of this possibility. We report interpretations with this caveat.\n\n**Practical significance: reasoning utilization efficiency.** G*(t) provides a unified diagnostic for reasoning utilization: G*(t) ≈ 0 means full utilization (knowledge channeled through CoT); G*(t) >> 0 means waste (CoT is decorative overhead); G*(t) < 0 means productive computation (CoT assembles new information). This framing connects to three practical domains: (a) *inference-time compute allocation* — skip CoT generation when G*(t) >> 0 for easy problems, providing the principled diagnostic that current early-exit heuristics (ESTAR, DTSR, FRIT, CoDE-Stop) lack; (b) *benchmark validity* — problems where all models show persistent G*(t) >> 0 are not testing reasoning; (c) *safety monitoring* — the decoupled internal quality-monitoring system (Yuan et al.) is the kind of hidden computation alignment researchers worry about.\n\nWe adopt honest scoping: 2-3 faithfulness phenomena as the realistic classification target, with steganographic encoding and reasoning theater as stretch goals. The boundary between pre-CoT encoding and post-hoc rationalization may be empirically blurred (in both cases, the model may have committed to an answer before CoT begins, so P*(t) starts high in both), potentially collapsing the taxonomy to 2 primary categories (pre-committed vs. genuinely reasoning). Phase 0b explicitly tests 2-category vs. 3-category separability; either outcome is a strong contribution. Task-difficulty conditioning — grounded in David's easy (0.84) vs. hard (0.76) probe splits and Gjølbye et al.'s (2605.15454) domain-specific difficulty-geometry coupling (ρ⊥ = +0.41 on Codeforces) — reveals the decorative→load-bearing transition with length correction.\n\nCore contributions: (a) calibrated ICG diagnostic with shape-based trajectory analysis on 5 models (4 reasoning + 1 instruction-tuned control) × 4 benchmarks, the first framework capable of distinguishing faithful-correct from unfaithful-correct reasoning; (b) empirical pilot with external validation (TTS cross-reference, difficulty partition, FaithCoT-Bench supplementary) demonstrating 2-3 distinguishable G*(t) phenomenon signatures; (c) difficulty-conditioned gap analysis with domain-specific nuance; (d) head-to-head comparison against TTS, FaithCoT-Bench methods, and probe-only trajectories. Total compute: ~1050 H100-hours.\n\n## Core Problem\nA striking convergence of 2025-2026 findings reveals a fundamental disconnect in reasoning language models: their hidden states reliably encode information about answer correctness — linear probes achieving 0.82-0.95 AUROC across multiple independent groups — yet causal interventions based on these probes consistently fail to influence model outputs. Cox et al. (2603.01437) find steering via answer-content probes produces answer flip rates 'negligible against the orthogonal baseline' on reasoning models, despite >0.9 AUC on instruction-tuned models. Yuan et al. (2605.09502) systematically test four interventions (activation steering, probe-guided best-of-N, self-correction, activation patching) on models up to 72B and report ALL fail. This diagnostic-causal gap is NOT an obstacle; it IS the central phenomenon.\n\nThe literature conflates two probe targets: answer-content probes (Cox et al.: specific answer on binary tasks, ≤9B + GPT-OSS-20B) and correctness probes (Yuan et al.: right/wrong on models up to 72B; Zhang et al. 2504.05419: per-chunk correctness on 7B-70B). Answer-content gaps mean 'the model has decided but CoT doesn't derive the answer'; correctness gaps mean 'the model knows it's right/wrong but CoT doesn't reflect this awareness.'\n\nTemporal dynamics are empirically grounded: David (2511.14773) finds probe accuracy at 0.84 AUC by token 4, stable ~0.8 through token 100, with easy (0.84) vs. hard (0.76) splits. Zhang et al. (2504.05419) report 65%→79% chunk trajectories on R1-Distill. Esakkiraja et al. (2604.01202) find >90% pre-generation AUROC with characteristic dip at 5-10%. Chrabąszcz et al. (2605.18549) demonstrate 60+ signal-processing features achieving up to 17pp over static probes. Yet no framework jointly tracks information availability AND causal contribution: Chrabąszcz et al. lack any causal component; Ballon et al. (2601.23163) provide behavioral C(t) but no hidden-state measurement; CMI (2602.03994) provides structural layerwise audit on ~50 examples but measures representation routing, not functional text contribution; TTS provides per-step marginal causal contribution but no probe-side measurement and no cumulative sufficiency assessment; Thought Anchors (2506.19143) provide within-CoT causal structure but no external probe reference.\n\n## Opportunity\n(1) **Temporal gap measurement.** Multiple groups have independently built the measurement components — probe trajectories (Chrabąszcz: 60+ features, 91-97% AUROC; David: per-token; Zhang: per-chunk; Yuan: 0.95 overall; Esakkiraja: >90% pre-generation) and behavioral causal curves (Ballon: truncation-reinjection; TTS: per-step ATE; NLDD: per-position degradation) — but no one has unified them into a dual-stream temporal gap. Chrabąszcz et al. are structurally blind to the faithful-correct vs. unfaithful-correct distinction; Ballon et al. lack hidden-state measurement. The gap between these traditions IS the framework's niche.\n\n(2) **Phenomenon unification with honest scoping.** CoT faithfulness failures are studied in isolation: Reasoning Horizon (Ye et al. 2602.11201), pre-CoT encoding (Cox et al.; Esakkiraja et al.), Reasoning Theater (Boppana et al. 2603.05488), myopic planning (Xu et al. 2602.02103). We propose 2-3 are distinguishable via G*(t) trajectory shapes, honestly pre-registering that pre-CoT encoding and rationalization may collapse to a single \"pre-committed\" category.\n\n(3) **Task-difficulty conditioning.** ICLR 2026 Workshop finding, Li et al. (2510.22362): easy→decorative, hard→faithful. Gjølbye et al. (2605.15454): difficulty-geometry coupling domain-specific (ρ⊥ = +0.41 code, +0.05 math). ICG answers: at what difficulty does CoT transition from decorative to load-bearing?\n\n(4) **Probe target clarification.** First principled treatment contrasting correctness awareness gap vs. answer-content gap on applicable tasks.\n\nTwo prior works combine probing with causal intervention: Kudo et al. (EACL 2026, 2412.01113) on synthetic arithmetic, and CMI (2602.03994) on ~50 examples — CMI measures *structural mediation* (representation routing through layers) while ICG measures *functional contribution* (whether CoT text causally contributes to behavioral correctness). Wang (2604.15726) formalizes H1/H2/H0 hypotheses; ICG operationalizes the H1/H2 distinction empirically. Neither Kudo et al. nor CMI provides: (a) temporal coverage on natural benchmarks, (b) phenomenon mapping, (c) instance-level diagnostic, (d) multi-model comparison across model families, (e) robustness validation per Young's (2603.20172) classifier-sensitivity finding (kappa as low as 0.06), or (f) empirical pilot with external validation standards.\n\n## Landscape\n**Probe-based temporal measurement (P*(t) foundation).** Chrabąszcz et al. (2605.18549): probe trajectories with 60+ signal-processing features (volatility, trend, steady-state, boundary transients, autocorrelation) via 3-layer MLP + Multi-Instance Learning. Max-pooling: 91-97% AUROC harmfulness (vs. 33-61% average-pooling); up to 17pp over static on GSM8K across Llama-8B-R1-Distill and Qwen3-4B/8B/14B (~3000 GPU-hours). Critical: (a) NO causal component, (b) NO gap metric, (c) NO calibration, (d) NO faithfulness-mode taxonomy, (e) NO difficulty conditioning, (f) structurally cannot distinguish faithful-correct from unfaithful-correct. David (2511.14773): 0.84 AUC at t=4, stable ~0.8, easy/hard 0.84/0.76 on Qwen3-8B. Zhang et al. (2504.05419): 0.82-0.91 AUROC on GSM8K/MATH/AIME, 65%→79% trajectory, 24% token reduction via early-exit. Yuan et al. (2605.09502): 0.95 AUROC on Qwen-3B, 0.852 on R1-7B, 0.787 first-step, concealment gap 0.197 AUROC. Esakkiraja et al. (2604.01202): >90% pre-generation, dip at 5-10%, recovery to near-100%. Cox et al. (2603.01437): answer-content probes >0.9 AUC on instruction-tuned Gemma-2/Qwen-2.5, negligible flip on reasoning GPT-OSS-20B. Additional: Qian et al. (2506.02867, NeurIPS 2025); Lewis-Lim et al. (2508.19827, EMNLP 2025); Mirtaheri & Belkin (2603.17199); Occhipinti et al. (ICLR 2026 LIT Workshop).\n\n**Diagnostic-not-causal evidence.** Yuan et al. (2605.09502): four interventions all fail on Qwen2.5 (1.5B-72B), Llama-3.1-8B, Phi-3.5-mini, DeepSeek-R1-7B. 'The error signal is a diagnostic readout, not a causal component that can be edited.' Cox et al. independently confirm. Probe accuracy ≠ causal potency on reasoning models.\n\n**Behavioral C(t) measurement.** Ballon et al. (2601.23163): truncation-reinjection on Qwen3-4B/8B/14B and gpt-oss-20B/120B, decile intervals. Accuracy: 30.8-42.3% → 49.0-73.1% on GPQA-Diamond. Controls validate sequential content (intact +18.1-33.1% vs. shuffled +0.3-10.8%). Disclaims faithfulness analysis. Zhao et al. (2510.24941, TTS): per-step ATE on R1-Distill-Qwen-7B/14B/Llama-8B, only 2.3% AIME steps TTS≥0.7. Ye et al. (2602.11201, NLDD): Reasoning Horizon at 70-85% on synthetic tasks (natural benchmark generalizability unvalidated). Thought Anchors (2506.19143): per-sentence counterfactual importance via 100-rollout replacement sampling; identifies \"anchor\" sentences steering reasoning trajectory — provides within-CoT causal structure but no probe reference for assessing redundancy relative to internal state. Basu & Chakraborty (2603.22816): decorative/scaffolding/genuine taxonomy. FACT-E (Sun et al. 2604.10693, ACL Findings 2026).\n\n**Probe-intervention combinations.** Kudo et al. (2412.01113, EACL 2026): per-position probes + activation patching on synthetic arithmetic, 9 models. CMI (2602.03994): layerwise activation patching on Phi/Qwen/DialoGPT, ~50 examples. CMI measures *structural mediation* (representation routing); ICG measures *functional contribution* (behavioral text causation). Both complementary precursors on small/synthetic samples.\n\n**Latent-reasoning theory.** Wang (2604.15726): H1/H2/H0 hypotheses with compute-audited designs. ICG operationalizes H1/H2 distinction.\n\n**Temporal hidden-state dynamics.** Gjølbye et al. (2605.15454): 11 models, 3 domains, length correction. ρ⊥^D = +0.41 Codeforces vs. −0.06 baselines; weaker on MATH (+0.05). Prompt-stage probes don't mirror generation-time dynamics. Furuya & Tanimura (2605.01853, StALT). Herrmann et al. (2605.09159): internal polylogue dynamics. Li et al. (2510.22362, NeurIPS 2025 MechInterp Workshop, Concept Walk): easy→decorative, hard→faithful. Vilas et al. (2510.10494, ICLR 2026): 14-70% token savings.\n\n**Probe calibration.** Hewitt & Liang (EMNLP 2019): 4.5 selectivity. Ravichander et al. (2005.00719): properties recoverable when unused. Voita & Titov (EMNLP 2020, 2003.12298): MDL probing. Chun et al. (2602.20338, MCT): geometric pulse — separability peaks transiently while probe accuracy persists. Validates null-probe calibration need.\n\n**Trajectory-shape analysis.** Entropy trajectories (2603.18940): +5.8pp from monotonicity. RQA (2602.06266): temporal 36.94% vs. aggregates 28.97%. Microsoft (2604.05655): 0.852 vs. 0.649 AUC.\n\n**Measurement sensitivity.** Young (2603.20172): kappa as low as 0.06, up to 30.6pp divergence. Young (2603.26410). 'Lie to Me' (2603.22582).\n\n**Additional.** Internal States Before Wait (2510.04128). From Reasoning to Answer (2509.23676). FaithCoT-Bench (ICLR 2026, 2510.04040): 1000+ expert-annotated trajectories, 11 methods, 4 paradigms. Jin et al. survey (ARR for ACL 2026). Liu et al. (2602.13904). Reasoning Theater (2603.05488). Early-exit: ESTAR, DTSR, NEAT, CoDE-Stop, FRIT (Swaroop et al., 2509.13334). Breaking the Chain (Somov et al., 2603.16475). Step-Level Hallucination (Alvarez & Baheri, 2605.13772). SAE Reasoning Features (2503.18878). Solution Hides in Hidden States (2604.23351). Knowing Before Saying (ACL Findings 2025, 2505.24362). LEACE (Belrose et al., NeurIPS 2023, 2306.03819). CoT Monitorability (Anwar et al., 2602.18297). Understanding CoT via Information Theory (Ton et al., ICML 2025, 2411.11984).\n\n**What remains open.** No framework provides: (1) dual-stream temporal gap enabling faithful-vs-unfaithful discrimination for correct instances; (2) empirically-validated phenomenon taxonomy with external validation; (3) instance-level diagnostic from temporal gap; (4) difficulty-conditioned gap with domain nuance; (5) head-to-head comparison against existing causal faithfulness methods; (6) instruction-tuned vs. reasoning model control comparison within the same framework.\n\n## Approach\n**Formal Framework.** Two time-varying quantities at equally-spaced positions (primary: 20-50 percentile-based positions; token-level supplementary on subsets):\n\n(i) *P*(t)*: Cross-validated AUROC of linear probe on layer-l hidden states, calibrated via null-probe (P*(t) = P(t) − P_null(t), Hewitt & Liang 2019). Shared probe evaluated at each position (following Chrabąszcz's per-token evaluation, avoiding per-position training). **Target: correctness (right/wrong)** — broader applicability than answer-content probes, directly tied to the diagnostic-not-causal finding (Yuan et al.), more interpretable for faithfulness. Supplementary answer-content probes on binary/MC subsets. Probed at layers L/4, L/2, 3L/4, L. MCT (Chun et al. 2602.20338) supplementary concordance on 500 examples: if MCT capacity diverges from P*(t), identifies positions where probe signal may reflect retrievability rather than geometrically organized information.\n\n(ii) *C(t)*: Three estimators aggregated into C_agg(t): (a) **Prefix truncation** — Ballon et al.'s (2601.23163) protocol with three controls (random, swapped, shuffled tokens), measuring P(correct | CoT[:t]) vs. P(correct | full CoT). This measures *cumulative sufficiency* — whether CoT up to position t is sufficient for correctness — which is theoretically distinct from per-step *marginal contribution* (TTS); (b) **Paraphrase perturbation** — sentence-level segments paraphrased by external model (Claude Haiku or GPT-4o-mini for cost efficiency), 2-3 variants per segment, NLI-based semantic preservation verification. Answer stability: P(same answer | paraphrased CoT). Protocol follows FaithCoT-Bench (ICLR 2026) paraphrasing paradigm. Applied to stratified subset (~40% of examples per cell) for cost control, with full prefix truncation on all examples; (c) **NLDD** (Ye et al. 2602.11201, conditional on Phase 0a feasibility) — logit degradation under corruption. Sentence-level segmentation aligned with TTS approach (Zhao et al.). Multiple estimators provide robustness per Young's (2603.20172) classifier-sensitivity finding.\n\n**C(t) Aggregation and Gap Normalization.** Primary: rank-based normalization — each estimator converted to instance-level percentile ranks within model-benchmark cell, then combined. If NLDD underperforms on specific benchmarks (Phase 0a), two-estimator C_agg(t) (prefix + paraphrase) is primary for those benchmarks; three-estimator as supplementary. Ablation reports: (a) per-estimator G*(t) for phenomenon classification; (b) inverse-variance weighting vs. equal-weight; (c) pairwise Spearman correlation and Cohen's kappa between estimators. Diagnostic value lies in trajectory shapes, not magnitudes, so normalization affects scale but not shape-based signatures.\n\n**G*(t) = P*(t) − C(t).** Primary signal:\n- G*(t) ≈ 0: Aligned (necessary for faithfulness; H2-consistent per Wang 2604.15726)\n- G*(t) >> 0: Diagnostic excess — 'knows but doesn't use' (H1-consistent)\n- G*(t) < 0: Information assembled during reasoning\n\n**Interpretive caveat.** G*(t) >> 0 indicates correctness-correlated information not causally channeled through CoT, but does not entail intentional withholding — some signals may be computational byproducts rather than actionable knowledge. MCT concordance provides partial validation of this boundary.\n\n**Phenomenon Predictions (honestly scoped).**\n*Primary (HIGH confidence):*\n(i) *Pre-committed reasoning* (encompasses pre-CoT encoding and potentially post-hoc rationalization): G*(t) starts high, stays high or widens. P*(t) high from start (David: 0.84 at t=4; Esakkiraja: >90% pre-generation; Cox: >0.9 pre-CoT), C(t) low or flat.\n(ii) *Genuine multi-step reasoning*: G*(t) converges toward zero. P*(t) rises gradually, C(t) tracks P*(t). Zhang et al.'s 65%→79%, Li et al.'s hard→faithful, Ballon et al.'s monotonic accuracy increase.\n\n*Secondary (MODERATE confidence — Phase 0b tests whether separable from pre-committed):*\n(iii) *Post-hoc rationalization as distinct from pre-CoT encoding*: If distinguishable, the separation should manifest primarily in C(t) dynamics (rationalization may show spurious partial C(t) increases as the model crafts locally-consistent reasoning, while pre-CoT encoding shows flat-zero C(t)) rather than P*(t). Phase 0b explicitly tests 2-category vs. 3-category separability; 2-category (pre-committed vs. genuine) is pre-registered as an acceptable outcome.\n\n*Stretch (require additional features):*\n(iv) *Steganographic encoding*: Dip-and-recovery, consistent with Esakkiraja's 5-10% dip.\n(v) *Reasoning Theater*: May overlap with pre-committed. Chrabąszcz-style features may enable separation. Reported with confusion matrices.\n\n**Semi-Synthetic Simulation (hypothesis generation, NOT validation).** Constructed from published data (David, Zhang, Esakkiraja, Yuan for probes; NLDD, TTS for causal; Chun et al. MCT for inflation). Real validation in Phase 0b.\n\n**Phase 0a: Gap Characterization + NLDD Feasibility (Weeks 1-2.5).** 500 examples × 3 datasets (GSM8K, MATH-500, MMLU) × 3 models (DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct):\n(i) Construct P*(t) and C(t) curves at 20-50 position resolution\n(ii) Validate null-probe calibration\n(iii) Characterize causal potency (Cox et al. protocol: steering on reasoning vs. instruction-tuned)\n(iv) **NLDD feasibility**: 7B × 100 examples on GSM8K (clear steps) + MMLU (ambiguous steps). If SNR uninformative on MMLU, restrict NLDD to math/code or replace with TTS-style perturbation. Cost: <10 GPU-hrs; gates 250+ hrs NLDD investment.\n\n**Phase 0b: Empirical Pilot (Weeks 2.5-4).** R1-Distill-Qwen-7B × GSM8K + MATH-500, 1000 examples.\n\n*Primary validation (external standards):*\n(i) **Difficulty-only partition**: model-independent difficulty bins (easy/medium/hard), no P*/C features used. Test G*(t) shape differences: d > 0.5 AND p < 0.01 (Bonferroni-corrected) on 2+ trajectory features.\n(ii) **TTS cross-reference** (primary external validation): compute Zhao et al.'s TTS on same examples; test whether high-TTS (genuine reasoning) vs. low-TTS (decorative) produce distinguishable G*(t) shapes.\n(iii) **2-category vs. 3-category test**: explicitly test whether pre-CoT encoding and post-hoc rationalization are separable or collapse to single \"pre-committed\" category.\n(iv) **FaithCoT-Bench** (supplementary): if instance-level overlap available, test correlation with expert labels; otherwise dataset-level validation.\n\n*Supplementary*: P*/C-based partition as self-consistency check.\nLength correction per Gjølbye et al. (2605.15454). Success: d > 0.5 between 2+ externally-defined partitions. If d < 0.3, downscope to characterization paper.\n\n**Phase 1: Full ICG (Weeks 4-9).** Conditional on Phase 0b d > 0.5. **5 models**: DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Llama-8B, DeepSeek-R1-Distill-Qwen-14B, QwQ-32B (reasoning models spanning 2 architecture families) + Qwen2.5-7B-Instruct (instruction-tuned control — expected G*(t) ≈ 0 as sanity check). **4 benchmarks**: GSM8K (500 examples), MATH-500 (500), GPQA-Diamond (~198 full), AIME (~90 full). Per-cell: ~1288 examples × 5 models. Full calibrated P*(t) + MCT supplementary + three C(t) estimators (NLDD conditional, paraphrase on ~40% stratified subset) + Ballon-style controls. Cross-reference with TTS at step boundaries. Bootstrap 95% CI on G*(t). ~250 H100-hours.\n\n**Phase 2: Difficulty Conditioning (Weeks 7-11).** Difficulty quintiles per benchmark. G*(t) per quintile. Expected: easy → persistent gap, hard → converging gap. Length correction; domain-specific reporting (stronger on math/code per Gjølbye et al.'s ρ⊥ = +0.41 code vs. +0.05 math).\n\n**Phase 3: Classification, Baselines, Robustness (Weeks 9-14).**\n\n*Classification framework:* G*(t) features (initial value, slope, convergence rate, dC/dt locality) + Chrabąszcz-style features (volatility, trend, boundary transients, autocorrelation). Classifier gradient: logistic regression → RF → MLP; report all. Metric: macro-F1 (primary) + confusion matrix + reliability diagram. Validation: 5-fold + cross-model (train A → test B, reporting within-family vs. cross-family separately) + cross-benchmark generalization. Paired permutation tests with Bonferroni correction for all head-to-head comparisons.\n\n*Baselines:* (a) Random + majority-class; (b) Difficulty-only classifier; (c) **Probe-trajectory-only** (Chrabąszcz-style P*(t) features, no C(t)) — \"no causal dimension\" ablation; (d) **TTS-only** — per-step marginal causal contribution without probe dimension.\n\n*Head-to-head TIF validation:* TIF score vs. FaithCoT-Bench detection methods (Adding Mistakes, Removing Steps, Early Answering, Paraphrasing) and TTS on overlapping examples, comparing instance-level correlation with ground truth.\n\n*Robustness ablations (7 dimensions):* (a) probe architecture (linear vs. 2-layer MLP); (b) layer selection; (c) C(t) estimator agreement + per-estimator performance + weighting schemes; (d) gap normalization (rank vs. min-max vs. z-score); (e) calibration method (shuffled-label vs. random-representation); (f) probe target (correctness vs. answer-content); (g) **temporal resolution** (5/10/20/35/50 positions + token-level — reporting resolution vs. macro-F1 curve and saturation point).\n\n**TIF Score.** Normalized area under calibrated G*(t), benchmarked against FaithCoT-Bench and Liu et al.'s (2602.13904) text-level metrics.\n\n**Paper Focus.** Core contributions: (1) ICG diagnostic — first framework distinguishing faithful-correct from unfaithful-correct reasoning via dual-stream temporal gap, with instruction-tuned control validating the framework; (2) Phase 0b pilot with external validation demonstrating 2-3 distinguishable G*(t) signatures (or honestly reporting 2-category outcome); (3) difficulty-conditioned gap revealing decorative→load-bearing transition; (4) head-to-head showing ICG's value over probe-only, TTS-only, and FaithCoT-Bench methods. Supporting: 7-dimension ablations; TIF validation. Supplementary: 671B subset (500 examples, 3 layers); answer-content vs. correctness comparison; semi-synthetic simulation; CMI structural-functional prediction if resources allow.\n\n**Experiments.** DeepSeek-R1-Distill-Qwen-7B/14B, DeepSeek-R1-Distill-Llama-8B, QwQ-32B, Qwen2.5-7B-Instruct across GSM8K, MATH-500, GPQA-Diamond, AIME. 671B validation (500-example subset). Calibration: synthetic arithmetic (G* ≈ 0 expected), TTS cross-reference, MCT supplementary. Gjølbye-style length correction throughout.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '~1050 H100-hours (Phase 0a: 90 hrs [3 models × 3 datasets + NLDD feasibility]; Phase 0b: 30 hrs [pilot]; Phase 1: 250 hrs [5 models × 4 benchmarks, probes + 3 C(t) estimators + controls]; Phase 2: 50 hrs [difficulty conditioning]; Phase 3: 70 hrs [classification + 7-dim ablations + baselines]; NLDD 32B conditional: 250 hrs [primary bottleneck]; NLDD 7B/14B: 100 hrs; MCT supplementary: 50 hrs; 671B subset: 50 hrs [8×H100]; semi-synthetic: 30 hrs; paraphrase model: ~80 hrs inference on target models for stability checks)', 'paraphrase_api_cost': '~$800-1500 (Claude Haiku/GPT-4o-mini on stratified ~40% subset, 2-3 variants)', 'timeline': '15-17 weeks (2 researchers)', 'estimated_gpu_cost': '$3,200 at ~$3/H100-hour', 'storage': '3-5 TB (4 layers, fp16); ~1.5 TB with PCA/on-the-fly'}, 'human_in_loop': {'gpu_hours': '~1050 H100-hours', 'timeline': '14 weeks (1 researcher + Claude)', 'claude_api_cost': '$500 (experiment design) + $800-1500 (paraphrase generation)', 'estimated_gpu_cost': '$3,200'}, 'auto_research': {'gpu_hours': '~1050 H100-hours', 'timeline': '12 weeks', 'claude_api_cost': '$900 + $800-1500 (paraphrase)', 'estimated_gpu_cost': '$3,200', 'speed_bottleneck': 'NLDD on 32B (~250 hrs, conditional on Phase 0a) is primary bottleneck. Phase 0b pilot (30 hrs) provides early go/no-go.'}}\n\n## Inspired By\nThe convergence of five independent lines of evidence — (a) Cox et al.'s steering failure on reasoning models despite high probe accuracy; (b) Yuan et al.'s four-intervention failure establishing 'diagnostic not causal'; (c) temporal probe dynamics (David, Zhang, Esakkiraja, Chrabąszcz: 60+ features, up to 17pp improvement); (d) Ballon et al.'s truncation-reinjection demonstrating monotonic behavioral C(t) with controls; (e) trajectory-shape literature (arXiv 2603.18940, 2602.06266, 2604.05655) showing shapes carry diagnostic information — all pointing to: the gap between diagnostic availability and causal contribution IS the phenomenon, and its temporal shape reveals the mechanism. Additionally: Wang's (2604.15726) H1/H2/H0; Gjølbye et al.'s (2605.15454) domain-specific coupling; Chun et al.'s (2602.20338) MCT geometric pulse; CMI's (2602.03994) structural mediation; Thought Anchors' (2506.19143) within-CoT causal structure.\n\n## Target Venues\n- ICLR 2027 (abstract: Sep 19, full paper: Sep 24, 2026; primary target)\n- ICML 2027 (full paper: Jan 29, 2027; fallback)\n\n## Key References\n- Monitoring the Internal Monologue: Probe Trajectories (Chrabąszcz et al., arXiv 2605.18549)\n- Probing the Trajectories of Reasoning Traces (Ballon et al., arXiv 2601.23163)\n- LLM Reasoning Is Latent (Wang, arXiv 2604.15726)\n- Reasoning Models Move Differently (Gjølbye et al., arXiv 2605.15454)\n- Hidden Error Awareness (Yuan et al., arXiv 2605.09502)\n- Decoding Answers Before CoT (Cox et al., arXiv 2603.01437)\n- Temporal Predictors of Outcome (David, arXiv 2511.14773)\n- Reasoning Models Know When They're Right (Zhang et al., arXiv 2504.05419)\n- Therefore I am. I Think (Esakkiraja et al., arXiv 2604.01202)\n- True Thinking Score (Zhao et al., arXiv 2510.24941)\n- Mechanistic Evidence for Faithfulness Decay / NLDD (Ye et al., arXiv 2602.11201)\n- Internal Polylogue (Herrmann et al., arXiv 2605.09159)\n- Faithfully Compute Answers During CoT (Kudo et al., EACL 2026, arXiv 2412.01113)\n- Causal Bypass / CMI (Sathyanarayanan et al., arXiv 2602.03994)\n- StALT (Furuya & Tanimura, arXiv 2605.01853)\n- Concept Walk (Li et al., arXiv 2510.22362, NeurIPS 2025 MechInterp Workshop)\n- Task Difficulty Shapes CoT Faithfulness (ICLR 2026 Workshop)\n- Diagnosing Pathological CoT (Liu et al., arXiv 2602.13904)\n- Measuring Faithfulness Depends on How You Measure (Young, arXiv 2603.20172)\n- MCT / Emergent Manifold Separability (Chun et al., arXiv 2602.20338)\n- Latent Temporal Signals (Vilas et al., ICLR 2026, arXiv 2510.10494)\n- Probing and Steering CoT Unfaithfulness (Occhipinti et al., ICLR 2026 LIT Workshop)\n- Designing and Interpreting Probes (Hewitt & Liang, EMNLP 2019)\n- Information-Theoretic Probing with MDL (Voita & Titov, EMNLP 2020, arXiv 2003.12298)\n- Probing the Probing Paradigm (Ravichander et al., arXiv 2005.00719)\n- Entropy trajectory shapes (arXiv 2603.18940)\n- RQA of Reasoning Dynamics (arXiv 2602.06266)\n- LLM Reasoning as Trajectories (arXiv 2604.05655, Microsoft)\n- Internal States Before Wait (arXiv 2510.04128)\n- FACT-E (Sun et al., ACL Findings 2026, arXiv 2604.10693)\n- Breaking the Chain (Somov et al., arXiv 2603.16475)\n- The Illusion of Reasoning (Basu & Chakraborty, arXiv 2603.22816)\n- FaithCoT-Bench (ICLR 2026, arXiv 2510.04040)\n- The Mirage of Explainability survey (Jin et al., ARR for ACL 2026)\n- Reasoning Theater (Boppana et al., arXiv 2603.05488)\n- No Global Plan in CoT (Xu et al., arXiv 2602.02103)\n- Catching Rationalization in the Act (Mirtaheri & Belkin, arXiv 2603.17199)\n- CoT Monitorability (Anwar et al., arXiv 2602.18297)\n- Understanding CoT via Information Theory (Ton et al., ICML 2025, arXiv 2411.11984)\n- Demystifying Reasoning Dynamics (Qian et al., NeurIPS 2025, arXiv 2506.02867)\n- Analysing CoT Dynamics (Lewis-Lim et al., EMNLP 2025, arXiv 2508.19827)\n- Why Models Know But Don't Say (Young, arXiv 2603.26410)\n- Lie to Me (arXiv 2603.22582)\n- Step-Level Hallucination (Alvarez & Baheri, arXiv 2605.13772)\n- From Reasoning to Answer (arXiv 2509.23676)\n- SAE Reasoning Features (arXiv 2503.18878)\n- FRIT (Swaroop et al., arXiv 2509.13334)\n- Solution Hides in Hidden States (arXiv 2604.23351)\n- Knowing Before Saying (ACL Findings 2025, arXiv 2505.24362)\n- LEACE (Belrose et al., NeurIPS 2023, arXiv 2306.03819)\n- Thought Anchors (arXiv 2506.19143)"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T04:19:16.030Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:19:16.030Z",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0"
}
```

---

## Round 1

64 recorded events

### User

_source line 3 · 2026-05-20T04:19:16.042Z_

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
  "promptId": "336e0584-08d7-4685-ad69-52c0743f6fcf",
  "type": "user",
  "uuid": "f38e4def-26fc-41c9-8612-c8d34fedde4b",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:19:16.040Z_

```json
{
  "parentUuid": "f38e4def-26fc-41c9-8612-c8d34fedde4b",
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
  "uuid": "7a850d71-7659-46b3-a90d-afb17f63c41e",
  "timestamp": "2026-05-20T04:19:16.040Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:19:16.040Z_

```json
{
  "parentUuid": "7a850d71-7659-46b3-a90d-afb17f63c41e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7022eed5-32a8-471d-9a10-bcf923487d59",
  "timestamp": "2026-05-20T04:19:16.040Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
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
  "leafUuid": "7022eed5-32a8-471d-9a10-bcf923487d59",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Information-Contribution Gap for reasoning faithfulness",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0"
}
```

---

### Assistant

_source line 8 · 2026-05-20T04:19:25.271Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze this proposal as the "发掘 agent" (Discovery Agent). I need to first do thorough literature research, then assess the novelty, significance, and related work differentiation of this proposal.

Let me start by reading the proposal carefully, then conduct web searches to understand the current landscape.

The proposal is about "Information-Contribution Gap (ICG)" - a framework that jointly tracks:
1. P*(t): probe-based correctness awareness over time (what the model "knows")
2. C(t): causal contribution of CoT to correctness (what CoT "does")


3. G*(t) = P*(t) - C(t): the gap between knowing and using

The core claim is that this dual-stream approach can distinguish faithful-correct from unfaithful-correct reasoning, which neither probe-only nor causal-only approaches can do alone. Now I need to search for related work to understand what's already been done in this space and where this truly breaks new ground.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7022eed5-32a8-471d-9a10-bcf923487d59",
  "isSidechain": false,
  "requestId": "req_011CbDBG8usJo6p4G8w5771T",
  "type": "assistant",
  "uuid": "1cf4ef54-21cd-49cc-846e-63a573939402",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012gLV8ARPaBiojBkhNQjeM4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12105,
      "cache_read_input_tokens": 14549,
      "output_tokens": 304,
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
          "output_tokens": 304,
          "cache_read_input_tokens": 14549,
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

_source line 9 · 2026-05-20T04:19:25.290Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XjHU6JTY9sDcGPMhL6X18y`</summary>

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
  "parentUuid": "1cf4ef54-21cd-49cc-846e-63a573939402",
  "isSidechain": false,
  "requestId": "req_011CbDBG8usJo6p4G8w5771T",
  "type": "assistant",
  "uuid": "8072ee44-1c83-4923-9e1b-03c4a611382a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012gLV8ARPaBiojBkhNQjeM4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12105,
      "cache_read_input_tokens": 14549,
      "output_tokens": 304,
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
          "output_tokens": 304,
          "cache_read_input_tokens": 14549,
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

_source line 10 · 2026-05-20T04:19:25.296Z_

<details><summary>↩ Tool result · `toolu_01XjHU6JTY9sDcGPMhL6X18y`</summary>

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
  "parentUuid": "8072ee44-1c83-4923-9e1b-03c4a611382a",
  "isSidechain": false,
  "promptId": "336e0584-08d7-4685-ad69-52c0743f6fcf",
  "type": "user",
  "uuid": "73004521-6e82-402a-a768-238a150934a9",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "8072ee44-1c83-4923-9e1b-03c4a611382a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-20T04:19:33.646Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now conduct the required pre-research searches. I need to understand:

1. The current state of CoT faithfulness research (latest 2025-2026 works)
2. Probe-based approaches to reasoning model internals
3. Whether the dual-stream (probe + causal) approach has been attempted
4. Any recent works that might threaten the novelty claim

Let me do 5 targeted searches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73004521-6e82-402a-a768-238a150934a9",
  "isSidechain": false,
  "requestId": "req_011CbDBH2pnCad3NwekZqMp8",
  "type": "assistant",
  "uuid": "08b6900f-6ee6-47ae-93c8-0579d5be81c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011AmEJe32VLLeYdtxNchsGC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 831,
      "cache_read_input_tokens": 26654,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 831,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 26654,
          "cache_creation_input_tokens": 831,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 831
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

_source line 12 · 2026-05-20T04:19:34.655Z_

I'll start by conducting thorough pre-research on the key aspects of this proposal. Let me run multiple targeted searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08b6900f-6ee6-47ae-93c8-0579d5be81c0",
  "isSidechain": false,
  "requestId": "req_011CbDBH2pnCad3NwekZqMp8",
  "type": "assistant",
  "uuid": "a69ece98-b671-4ef9-8026-d1dd4cd346ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011AmEJe32VLLeYdtxNchsGC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 831,
      "cache_read_input_tokens": 26654,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 831,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 26654,
          "cache_creation_input_tokens": 831,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 831
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

_source line 13 · 2026-05-20T04:19:35.060Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GAPaTqdMnQSLBo2SraPRmw`</summary>

```json
{
  "query": "chain-of-thought faithfulness probing causal intervention gap 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a69ece98-b671-4ef9-8026-d1dd4cd346ba",
  "isSidechain": false,
  "requestId": "req_011CbDBH2pnCad3NwekZqMp8",
  "type": "assistant",
  "uuid": "8ce9078d-cf67-4c65-9260-4e7a297a2aa9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011AmEJe32VLLeYdtxNchsGC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 831,
      "cache_read_input_tokens": 26654,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 831,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 208,
          "cache_read_input_tokens": 26654,
          "cache_creation_input_tokens": 831,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 831
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

_source line 14 · 2026-05-20T04:19:42.274Z_

<details><summary>↩ Tool result · `toolu_01GAPaTqdMnQSLBo2SraPRmw`</summary>

```text
Web search results for query: "chain-of-thought faithfulness probing causal intervention gap 2025 2026"

Links: [{"title":"Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models","url":"https://arxiv.org/html/2603.26410"},{"title":"Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING","url":"https://openreview.net/attachment?id=lN3yKqqzF1&name=pdf"},{"title":"Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning | Request PDF","url":"https://www.researchgate.net/publication/386203451_Making_Reasoning_Matter_Measuring_and_Improving_Faithfulness_of_Chain-of-Thought_Reasoning"},{"title":"FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness","url":"https://arxiv.org/pdf/2509.13334"},{"title":"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures","url":"https://arxiv.org/html/2603.16475v1"},{"title":"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps","url":"https://arxiv.org/html/2502.14829v3"},{"title":"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2602.11201v1"},{"title":"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures | OpenReview","url":"https://openreview.net/forum?id=yfqHr7l2tG"}]

Based on the web search results, here's what I found regarding chain-of-thought faithfulness, probing, and causal intervention research from 2025-2026:

## Recent Research on CoT Faithfulness and Causal Interventions

**Key Findings on Systematic Gaps:**

Across nine models and four benchmarks with annotated intermediates, research reveals a systematic gap: while models rely on structures more than the original text (>60% consistency under interventions to original prompt), they fail to update under logically significant structural edits more than 50% of the time.

**Mechanistic Evidence:**

Recent work identified a "Reasoning Horizon" at 70–85% of chain length, beyond which reasoning tokens have diminishing causal influence on the final answer. Additionally, models often commit to answers early in the reasoning chain, with subsequent tokens serving a performative rather than computational role.

**Probing Methods and Benchmarks:**

Recent work addresses the gap by introducing the first benchmark dedicated to instance-level CoT unfaithfulness evaluation, providing the first instance-level dataset for detecting unfaithful reasoning in Chain-of-Thought outputs. Counterfactual approaches analyze how perturbing reasoning steps affects model predictions, while adversarial methods intervene on the CoT or model states to probe causal dependencies.

**Improving CoT Faithfulness:**

One proposed approach uses causality of CoT steps to fine-tune for more faithful outputs, working through automated causal interventions that identify which reasoning steps actually influence the final answer, and an augmentation process that creates paired examples of faithful versus unfaithful reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ce9078d-cf67-4c65-9260-4e7a297a2aa9",
  "isSidechain": false,
  "promptId": "336e0584-08d7-4685-ad69-52c0743f6fcf",
  "type": "user",
  "uuid": "0cc21d7c-e9d1-408c-b9d1-ff4a532c0537",
  "toolUseResult": {
    "query": "chain-of-thought faithfulness probing causal intervention gap 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012AJFuZTDvruehQDjH5LCXz",
        "content": [
          {
            "title": "Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models",
            "url": "https://arxiv.org/html/2603.26410"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING",
            "url": "https://openreview.net/attachment?id=lN3yKqqzF1&name=pdf"
          },
          {
            "title": "Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning | Request PDF",
            "url": "https://www.researchgate.net/publication/386203451_Making_Reasoning_Matter_Measuring_and_Improving_Faithfulness_of_Chain-of-Thought_Reasoning"
          },
          {
            "title": "FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness",
            "url": "https://arxiv.org/pdf/2509.13334"
          },
          {
            "title": "Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures",
            "url": "https://arxiv.org/html/2603.16475v1"
          },
          {
            "title": "Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps",
            "url": "https://arxiv.org/html/2502.14829v3"
          },
          {
            "title": "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2602.11201v1"
          },
          {
            "title": "Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures | OpenReview",
            "url": "https://openreview.net/forum?id=yfqHr7l2tG"
          }
        ]
      },
      "Based on the web search results, here's what I found regarding chain-of-thought faithfulness, probing, and causal intervention research from 2025-2026:\n\n## Recent Research on CoT Faithfulness and Causal Interventions\n\n**Key Findings on Systematic Gaps:**\n\nAcross nine models and four benchmarks with annotated intermediates, research reveals a systematic gap: while models rely on structures more than the original text (>60% consistency under interventions to original prompt), they fail to update under logically significant structural edits more than 50% of the time.\n\n**Mechanistic Evidence:**\n\nRecent work identified a \"Reasoning Horizon\" at 70–85% of chain length, beyond which reasoning tokens have diminishing causal influence on the final answer. Additionally, models often commit to answers early in the reasoning chain, with subsequent tokens serving a performative rather than computational role.\n\n**Probing Methods and Benchmarks:**\n\nRecent work addresses the gap by introducing the first benchmark dedicated to instance-level CoT unfaithfulness evaluation, providing the first instance-level dataset for detecting unfaithful reasoning in Chain-of-Thought outputs. Counterfactual approaches analyze how perturbing reasoning steps affects model predictions, while adversarial methods intervene on the CoT or model states to probe causal dependencies.\n\n**Improving CoT Faithfulness:**\n\nOne proposed approach uses causality of CoT steps to fine-tune for more faithful outputs, working through automated causal interventions that identify which reasoning steps actually influence the final answer, and an augmentation process that creates paired examples of faithful versus unfaithful reasoning."
    ],
    "durationSeconds": 7.206180220000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8ce9078d-cf67-4c65-9260-4e7a297a2aa9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T04:19:45.172Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Nxnid8oEqvGMLAAtW15hgu`</summary>

```json
{
  "query": "probe trajectory hidden states reasoning models diagnostic causal gap 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cc21d7c-e9d1-408c-b9d1-ff4a532c0537",
  "isSidechain": false,
  "requestId": "req_011CbDBJ53G4hxEa3LDWqV3e",
  "type": "assistant",
  "uuid": "7fa214a9-61f5-4188-83bc-87696e55f7a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P2ThYr4bdixwmK22MpFwYF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1047,
      "cache_read_input_tokens": 27485,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1047,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 27485,
          "cache_creation_input_tokens": 1047,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1047
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

_source line 16 · 2026-05-20T04:19:53.266Z_

<details><summary>↩ Tool result · `toolu_01Nxnid8oEqvGMLAAtW15hgu`</summary>

```text
Web search results for query: "probe trajectory hidden states reasoning models diagnostic causal gap 2025 2026 arxiv"

Links: [{"title":"Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING","url":"https://arxiv.org/pdf/2510.04040"},{"title":"Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning","url":"https://arxiv.org/pdf/2603.01326"},{"title":"Temporal Predictors of Outcome in Reasoning Language Models","url":"https://arxiv.org/pdf/2511.14773"},{"title":"Reasoning Models Know When They're Right: Probing Hidden States for   Self-Verification","url":"https://arxiv.org/pdf/2504.05419"},{"title":"More Than Meets the Eye? Uncovering the Reasoning-Planning Disconnect in Training Vision-Language Driving Models","url":"https://arxiv.org/pdf/2510.04532"},{"title":"No Global Plan in Chain-of-Thought: Uncover the Latent Planning Horizon of LLMs","url":"https://arxiv.org/pdf/2602.02103"}]

Based on the search results, I found several relevant papers from arXiv related to probing hidden states in reasoning models:

## Key Results:

1. **"Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification"** (2024/2025):
   This work finds that models' hidden states encode correctness of future answers, enabling early prediction of correctness before answers are fully formulated, and uses probes as verifiers to reduce inference tokens by 24% without compromising performance.

2. **"Temporal Predictors of Outcome in Reasoning Language Models"** (2025):
   This work targets the gap by focusing on math CoT and probing hidden states during the reasoning trajectory, not only in the pre-answer state.

3. **"Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning"** (2025):
   The paper plots layerwise hidden states as trajectories in activation space, finding that correct generations follow smoother paths while incorrect ones exhibit sharp deviations, suggesting that modeling entire trajectories can help distinguish valid from spurious reasoning.

4. **"No Global Plan in Chain-of-Thought: Uncover the Latent Planning Horizon of LLMs"** (February 2026):
   This paper observes that hidden states at the beginning of CoT can reliably predict total reasoning steps, and introduces a probing method called Tele-Lens using a low-rank adapter to transform hidden states to predict various dimensions of information.

5. **"FaithCoT-Bench: Benchmarking"** (ICLR 2026):
   The work mentions that future research will investigate whether observable signals align with the model's actual decision process using mechanistic tools such as causal probing, circuit analysis, and hidden-state inspection.

These papers collectively address diagnostic and causal approaches to understanding hidden state representations in reasoning models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fa214a9-61f5-4188-83bc-87696e55f7a9",
  "isSidechain": false,
  "promptId": "336e0584-08d7-4685-ad69-52c0743f6fcf",
  "type": "user",
  "uuid": "97046790-c728-4f8f-8c34-000d138688b9",
  "toolUseResult": {
    "query": "probe trajectory hidden states reasoning models diagnostic causal gap 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_016GakTyTefvfBaRzCrETZxt",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING",
            "url": "https://arxiv.org/pdf/2510.04040"
          },
          {
            "title": "Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning",
            "url": "https://arxiv.org/pdf/2603.01326"
          },
          {
            "title": "Temporal Predictors of Outcome in Reasoning Language Models",
            "url": "https://arxiv.org/pdf/2511.14773"
          },
          {
            "title": "Reasoning Models Know When They're Right: Probing Hidden States for   Self-Verification",
            "url": "https://arxiv.org/pdf/2504.05419"
          },
          {
            "title": "More Than Meets the Eye? Uncovering the Reasoning-Planning Disconnect in Training Vision-Language Driving Models",
            "url": "https://arxiv.org/pdf/2510.04532"
          },
          {
            "title": "No Global Plan in Chain-of-Thought: Uncover the Latent Planning Horizon of LLMs",
            "url": "https://arxiv.org/pdf/2602.02103"
          }
        ]
      },
      "Based on the search results, I found several relevant papers from arXiv related to probing hidden states in reasoning models:\n\n## Key Results:\n\n1. **\"Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification\"** (2024/2025):\n   This work finds that models' hidden states encode correctness of future answers, enabling early prediction of correctness before answers are fully formulated, and uses probes as verifiers to reduce inference tokens by 24% without compromising performance.\n\n2. **\"Temporal Predictors of Outcome in Reasoning Language Models\"** (2025):\n   This work targets the gap by focusing on math CoT and probing hidden states during the reasoning trajectory, not only in the pre-answer state.\n\n3. **\"Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning\"** (2025):\n   The paper plots layerwise hidden states as trajectories in activation space, finding that correct generations follow smoother paths while incorrect ones exhibit sharp deviations, suggesting that modeling entire trajectories can help distinguish valid from spurious reasoning.\n\n4. **\"No Global Plan in Chain-of-Thought: Uncover the Latent Planning Horizon of LLMs\"** (February 2026):\n   This paper observes that hidden states at the beginning of CoT can reliably predict total reasoning steps, and introduces a probing method called Tele-Lens using a low-rank adapter to transform hidden states to predict various dimensions of information.\n\n5. **\"FaithCoT-Bench: Benchmarking\"** (ICLR 2026):\n   The work mentions that future research will investigate whether observable signals align with the model's actual decision process using mechanistic tools such as causal probing, circuit analysis, and hidden-state inspection.\n\nThese papers collectively address diagnostic and causal approaches to understanding hidden state representations in reasoning models."
    ],
    "durationSeconds": 8.090241097999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7fa214a9-61f5-4188-83bc-87696e55f7a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T04:19:56.272Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SKhCqiZDuSniahR2VSv4L4`</summary>

```json
{
  "query": "Chrabąszcz probe trajectories \"monitoring internal monologue\" 2605.18549 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97046790-c728-4f8f-8c34-000d138688b9",
  "isSidechain": false,
  "requestId": "req_011CbDBJt1GUouAvVvH1kfdg",
  "type": "assistant",
  "uuid": "0b97edd9-5e68-4314-92b6-f0bf82346170",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JVyod3rBJCcrW4DWpAdkRy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 817,
      "cache_read_input_tokens": 28532,
      "output_tokens": 77,
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
          "output_tokens": 77,
          "cache_read_input_tokens": 28532,
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

_source line 18 · 2026-05-20T04:20:03.259Z_

<details><summary>↩ Tool result · `toolu_01SKhCqiZDuSniahR2VSv4L4`</summary>

```text
Web search results for query: "Chrabąszcz probe trajectories "monitoring internal monologue" 2605.18549 2026"

Links: [{"title":"[2605.18549] Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics","url":"https://arxiv.org/abs/2605.18549"},{"title":"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics","url":"https://arxiv.org/html/2605.18549"},{"title":"Beyond the Black Box: Interpretability of Agentic AI Tool Use","url":"https://arxiv.org/html/2605.06890"},{"title":"(PDF) Internal Monologue","url":"https://www.academia.edu/68121407/Internal_Monologue"},{"title":"Trajectory sampling using spatial familiarity","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11435202"},{"title":"Spectroscopic Active Probes for Investigation of Lipid Transformation in Cells and Membranes | The Journal of Physical Chemistry B","url":"https://pubs.acs.org/doi/10.1021/acs.jpcb.5c05981"},{"title":"Method, apparatus, and computer program product for anonymizing trajectories","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11662215"}]

Based on the search results, I found the research paper you're looking for:

The paper "Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics" (arXiv:2605.18549) was submitted on May 18, 2026 by Maciej Chrabąszcz and colleagues, addressing how Large Reasoning Models (LRMs) introduce new opportunities for safety monitoring through their Chain of Thought (CoT) reasoning.

The research investigates the hidden representations of LRMs to determine whether future behavior can be predicted from prompt and CoT representations by evaluating a probe at each generated token to construct a probe trajectory, which is the continuous evolution of a concept's probability across the reasoning process.

The researchers found that future model behavior is more distinguishable when examined over the full trajectory than from a single static prediction. To characterize these temporal dynamics, they extract signal-processing features that capture volatility, trend, and steady-state behavior, significantly improving the separation of future model states.

The paper presents several key methodological findings, including insights about training data generation and the importance of pooling operations in achieving robust results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b97edd9-5e68-4314-92b6-f0bf82346170",
  "isSidechain": false,
  "promptId": "336e0584-08d7-4685-ad69-52c0743f6fcf",
  "type": "user",
  "uuid": "dc05ba70-cf0e-424a-877a-e1fc2e17d57d",
  "toolUseResult": {
    "query": "Chrabąszcz probe trajectories \"monitoring internal monologue\" 2605.18549 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018BEpRyyBTNUVTdxkqJrW32",
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
            "title": "Beyond the Black Box: Interpretability of Agentic AI Tool Use",
            "url": "https://arxiv.org/html/2605.06890"
          },
          {
            "title": "(PDF) Internal Monologue",
            "url": "https://www.academia.edu/68121407/Internal_Monologue"
          },
          {
            "title": "Trajectory sampling using spatial familiarity",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11435202"
          },
          {
            "title": "Spectroscopic Active Probes for Investigation of Lipid Transformation in Cells and Membranes | The Journal of Physical Chemistry B",
            "url": "https://pubs.acs.org/doi/10.1021/acs.jpcb.5c05981"
          },
          {
            "title": "Method, apparatus, and computer program product for anonymizing trajectories",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11662215"
          }
        ]
      },
      "Based on the search results, I found the research paper you're looking for:\n\nThe paper \"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics\" (arXiv:2605.18549) was submitted on May 18, 2026 by Maciej Chrabąszcz and colleagues, addressing how Large Reasoning Models (LRMs) introduce new opportunities for safety monitoring through their Chain of Thought (CoT) reasoning.\n\nThe research investigates the hidden representations of LRMs to determine whether future behavior can be predicted from prompt and CoT representations by evaluating a probe at each generated token to construct a probe trajectory, which is the continuous evolution of a concept's probability across the reasoning process.\n\nThe researchers found that future model behavior is more distinguishable when examined over the full trajectory than from a single static prediction. To characterize these temporal dynamics, they extract signal-processing features that capture volatility, trend, and steady-state behavior, significantly improving the separation of future model states.\n\nThe paper presents several key methodological findings, including insights about training data generation and the importance of pooling operations in achieving robust results."
    ],
    "durationSeconds": 6.982648370999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0b97edd9-5e68-4314-92b6-f0bf82346170",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T04:20:06.909Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Weq6aYPPDvbe8XdNVxVBJr`</summary>

```json
{
  "query": "Yuan \"hidden error awareness\" intervention failure reasoning models 2605.09502 diagnostic readout"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc05ba70-cf0e-424a-877a-e1fc2e17d57d",
  "isSidechain": false,
  "requestId": "req_011CbDBKcry1o6EupZFKvuuJ",
  "type": "assistant",
  "uuid": "046c3243-d50b-4dd0-8cdf-2c1fa7588b47",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PyY9UDwkYazFUFdqLgJpo2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 713,
      "cache_read_input_tokens": 29349,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 713,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 29349,
          "cache_creation_input_tokens": 713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 713
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

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness  ## Description When a reasoning model gets the right answer, is i…",
  "leafUuid": "046c3243-d50b-4dd0-8cdf-2c1fa7588b47",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Information-Contribution Gap for reasoning faithfulness",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0"
}
```

---

### Tool result

_source line 22 · 2026-05-20T04:20:14.947Z_

<details><summary>↩ Tool result · `toolu_01Weq6aYPPDvbe8XdNVxVBJr`</summary>

```text
Web search results for query: "Yuan "hidden error awareness" intervention failure reasoning models 2605.09502 diagnostic readout"

Links: [{"title":"[2605.09502] Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal","url":"https://arxiv.org/abs/2605.09502"},{"title":"Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal","url":"https://arxiv.org/html/2605.09502"},{"title":"Hop, Skip, and Overthink: Diagnosing Why Reasoning Models Fumble during Multi-Hop Analysis","url":"https://arxiv.org/pdf/2508.04699"},{"title":"Stop Before You Fail: Operational Capability Boundaries for Mitigating Unproductive Reasoning in Large Reasoning Models","url":"https://arxiv.org/pdf/2509.24711"},{"title":"Reasoning Can Hurt the Inductive Abilities of Large Language Models","url":"https://arxiv.org/pdf/2505.24225"},{"title":"On the Self-awareness of Large Reasoning Models ...","url":"https://arxiv.org/abs/2509.24711"},{"title":"Are Reasoning LLMs Robust to Interventions on Their Chain-of-Thought?","url":"https://arxiv.org/pdf/2602.07470"},{"title":"Effectively Controlling Reasoning Models through Thinking Intervention","url":"https://arxiv.org/html/2503.24370v3"},{"title":"Towards Safe Reasoning in Large Reasoning Models via Corrective Intervention","url":"https://arxiv.org/html/2509.24393v1"}]

Based on the search results, I found the paper you're looking for. Here's what the research describes:

## Hidden Error Awareness in Chain-of-Thought Reasoning (arXiv:2605.09502)

The paper by Aojie Yuan and colleagues challenges the assumption that generated reasoning reflects a model's internal computation, showing that models internally detect their own reasoning errors but outwardly express confidence in them.

### Key Findings:

**Detection Performance:**
A linear probe on hidden states predicts trace correctness with 0.95 AUROC—from the very first reasoning step (0.79)—while verbalized confidence for wrong traces is 4.55/5, nearly identical to correct ones (4.87/5). A text-surface classifier achieves only 0.59 on the same data, confirming a 0.20-point gap invisible in the generated text.

**Intervention Failures:**
Four interventions—activation steering, probe-guided best-of-N, self-correction, and activation patching—all fail; patching destroys output coherence entirely.

**The Diagnostic Signal:**
The signal is diagnostic, not causal: a readout of computation quality, meaning that while hidden states can detect errors, this signal cannot be directly manipulated to improve model behavior.

**Generality:**
This hidden error awareness holds across three model families (Qwen, Llama, Phi), 1.5B–72B parameters, and RL-trained reasoning models (DeepSeek-R1, 0.852 AUROC).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "046c3243-d50b-4dd0-8cdf-2c1fa7588b47",
  "isSidechain": false,
  "promptId": "336e0584-08d7-4685-ad69-52c0743f6fcf",
  "type": "user",
  "uuid": "62c32bc3-6375-40fa-a98b-7dd10809cecb",
  "toolUseResult": {
    "query": "Yuan \"hidden error awareness\" intervention failure reasoning models 2605.09502 diagnostic readout",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EpVwzjmzSgJtSNwrPmT8bd",
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
            "title": "Hop, Skip, and Overthink: Diagnosing Why Reasoning Models Fumble during Multi-Hop Analysis",
            "url": "https://arxiv.org/pdf/2508.04699"
          },
          {
            "title": "Stop Before You Fail: Operational Capability Boundaries for Mitigating Unproductive Reasoning in Large Reasoning Models",
            "url": "https://arxiv.org/pdf/2509.24711"
          },
          {
            "title": "Reasoning Can Hurt the Inductive Abilities of Large Language Models",
            "url": "https://arxiv.org/pdf/2505.24225"
          },
          {
            "title": "On the Self-awareness of Large Reasoning Models ...",
            "url": "https://arxiv.org/abs/2509.24711"
          },
          {
            "title": "Are Reasoning LLMs Robust to Interventions on Their Chain-of-Thought?",
            "url": "https://arxiv.org/pdf/2602.07470"
          },
          {
            "title": "Effectively Controlling Reasoning Models through Thinking Intervention",
            "url": "https://arxiv.org/html/2503.24370v3"
          },
          {
            "title": "Towards Safe Reasoning in Large Reasoning Models via Corrective Intervention",
            "url": "https://arxiv.org/html/2509.24393v1"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's what the research describes:\n\n## Hidden Error Awareness in Chain-of-Thought Reasoning (arXiv:2605.09502)\n\nThe paper by Aojie Yuan and colleagues challenges the assumption that generated reasoning reflects a model's internal computation, showing that models internally detect their own reasoning errors but outwardly express confidence in them.\n\n### Key Findings:\n\n**Detection Performance:**\nA linear probe on hidden states predicts trace correctness with 0.95 AUROC—from the very first reasoning step (0.79)—while verbalized confidence for wrong traces is 4.55/5, nearly identical to correct ones (4.87/5). A text-surface classifier achieves only 0.59 on the same data, confirming a 0.20-point gap invisible in the generated text.\n\n**Intervention Failures:**\nFour interventions—activation steering, probe-guided best-of-N, self-correction, and activation patching—all fail; patching destroys output coherence entirely.\n\n**The Diagnostic Signal:**\nThe signal is diagnostic, not causal: a readout of computation quality, meaning that while hidden states can detect errors, this signal cannot be directly manipulated to improve model behavior.\n\n**Generality:**\nThis hidden error awareness holds across three model families (Qwen, Llama, Phi), 1.5B–72B parameters, and RL-trained reasoning models (DeepSeek-R1, 0.852 AUROC)."
    ],
    "durationSeconds": 8.033113327999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "046c3243-d50b-4dd0-8cdf-2c1fa7588b47",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T04:20:17.701Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EWhRe4DmqGQh719wqRNZt4`</summary>

```json
{
  "query": "\"dual stream\" OR \"joint probing causal\" OR \"combining probes interventions\" chain-of-thought faithfulness framework 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62c32bc3-6375-40fa-a98b-7dd10809cecb",
  "isSidechain": false,
  "requestId": "req_011CbDBLUiMPXyESdDWif7cP",
  "type": "assistant",
  "uuid": "070597ac-0066-45c8-9f0a-650d89388982",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ur4rq9e4yCAZHdZyzrsZ2V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 865,
      "cache_read_input_tokens": 30062,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 865,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 30062,
          "cache_creation_input_tokens": 865,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 865
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

_source line 24 · 2026-05-20T04:20:25.980Z_

<details><summary>↩ Tool result · `toolu_01EWhRe4DmqGQh719wqRNZt4`</summary>

```text
Web search results for query: ""dual stream" OR "joint probing causal" OR "combining probes interventions" chain-of-thought faithfulness framework 2026"

Links: [{"title":"Published as a LIT workshop paper at ICLR 2026","url":"https://openreview.net/pdf?id=wVj7dB7waI"},{"title":"Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models","url":"https://arxiv.org/html/2603.26410v1"},{"title":"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2602.11201v1"},{"title":"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps","url":"https://arxiv.org/html/2502.14829v3"},{"title":"Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents","url":"https://arxiv.org/pdf/2601.02314"},{"title":"Is VLA Reasoning Faithful? Probing Safety of Chain-of-Causation in Autonomous Driving ModelsAccepted at the DriveX Workshop, CVPR 2026.","url":"https://arxiv.org/html/2605.17268"},{"title":"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures","url":"https://arxiv.org/html/2603.16475v1"},{"title":"FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness","url":"https://arxiv.org/pdf/2509.13334"}]

Based on the search results, I found several relevant papers on chain-of-thought faithfulness frameworks from 2026. Here are the key findings:

## Dual Stream / Dual Lens Approach

One framework combines counterfactual interventions (corrupting specific reasoning steps) with analysis of internal model states to reveal both whether reasoning steps causally influence predictions and how internal representations evolve during multi-step inference, with this dual lens distinguishing genuine reasoning breakdown from superficial output changes.

## Joint Probing and Intervention Methods

Researchers employ Representational Similarity Analysis (RSA) to measure alignment between clean and counterfactually corrupted reasoning trajectories, coupled with linear probes to track the evolution of solution-relevant information across layers. By performing counterfactual interventions that corrupt specific reasoning steps while maintaining surface coherence, they isolate the degree to which models causally depend on their generated reasoning.

## Recent 2026 Mechanistic Evidence

Ye et al. (2026) identified a "Reasoning Horizon" at 70–85% of chain length, beyond which reasoning tokens have diminishing causal influence on the final answer. Boppana et al. (2026) used activation probes to show that models often commit to answers early in the reasoning chain, with subsequent tokens serving a performative rather than computational role.

## Structural Causal Framework

Project Ariadne is a novel XAI framework that utilizes Structural Causal Models (SCMs) and counterfactual logic to audit the causal integrity of agentic reasoning.

The search results show active research in 2026 on combining multiple methodologies—interventions, probing, and causal analysis—to evaluate chain-of-thought faithfulness in language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "070597ac-0066-45c8-9f0a-650d89388982",
  "isSidechain": false,
  "promptId": "336e0584-08d7-4685-ad69-52c0743f6fcf",
  "type": "user",
  "uuid": "d0383118-d8d9-4748-82aa-2afef3d3a6a1",
  "toolUseResult": {
    "query": "\"dual stream\" OR \"joint probing causal\" OR \"combining probes interventions\" chain-of-thought faithfulness framework 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01M7g4WoYNVA7VrDstk5aeXs",
        "content": [
          {
            "title": "Published as a LIT workshop paper at ICLR 2026",
            "url": "https://openreview.net/pdf?id=wVj7dB7waI"
          },
          {
            "title": "Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models",
            "url": "https://arxiv.org/html/2603.26410v1"
          },
          {
            "title": "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2602.11201v1"
          },
          {
            "title": "Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps",
            "url": "https://arxiv.org/html/2502.14829v3"
          },
          {
            "title": "Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents",
            "url": "https://arxiv.org/pdf/2601.02314"
          },
          {
            "title": "Is VLA Reasoning Faithful? Probing Safety of Chain-of-Causation in Autonomous Driving ModelsAccepted at the DriveX Workshop, CVPR 2026.",
            "url": "https://arxiv.org/html/2605.17268"
          },
          {
            "title": "Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures",
            "url": "https://arxiv.org/html/2603.16475v1"
          },
          {
            "title": "FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness",
            "url": "https://arxiv.org/pdf/2509.13334"
          }
        ]
      },
      "Based on the search results, I found several relevant papers on chain-of-thought faithfulness frameworks from 2026. Here are the key findings:\n\n## Dual Stream / Dual Lens Approach\n\nOne framework combines counterfactual interventions (corrupting specific reasoning steps) with analysis of internal model states to reveal both whether reasoning steps causally influence predictions and how internal representations evolve during multi-step inference, with this dual lens distinguishing genuine reasoning breakdown from superficial output changes.\n\n## Joint Probing and Intervention Methods\n\nResearchers employ Representational Similarity Analysis (RSA) to measure alignment between clean and counterfactually corrupted reasoning trajectories, coupled with linear probes to track the evolution of solution-relevant information across layers. By performing counterfactual interventions that corrupt specific reasoning steps while maintaining surface coherence, they isolate the degree to which models causally depend on their generated reasoning.\n\n## Recent 2026 Mechanistic Evidence\n\nYe et al. (2026) identified a \"Reasoning Horizon\" at 70–85% of chain length, beyond which reasoning tokens have diminishing causal influence on the final answer. Boppana et al. (2026) used activation probes to show that models often commit to answers early in the reasoning chain, with subsequent tokens serving a performative rather than computational role.\n\n## Structural Causal Framework\n\nProject Ariadne is a novel XAI framework that utilizes Structural Causal Models (SCMs) and counterfactual logic to audit the causal integrity of agentic reasoning.\n\nThe search results show active research in 2026 on combining multiple methodologies—interventions, probing, and causal analysis—to evaluate chain-of-thought faithfulness in language models."
    ],
    "durationSeconds": 8.275860149,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "070597ac-0066-45c8-9f0a-650d89388982",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T04:20:28.679Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DpGdPtzWfmj1WrrmqguTK5`</summary>

```json
{
  "query": "Thought Anchors 2506.19143 counterfactual importance CoT sentences 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0383118-d8d9-4748-82aa-2afef3d3a6a1",
  "isSidechain": false,
  "requestId": "req_011CbDBMHs2FRPvQFzQx5UY2",
  "type": "assistant",
  "uuid": "eea30f52-ca28-424b-8cd5-1fb744036194",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WBUREVqkuKmQh2LrKpu9Mt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 925,
      "cache_read_input_tokens": 30927,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 30927,
          "cache_creation_input_tokens": 925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 925
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

_source line 26 · 2026-05-20T04:20:35.400Z_

<details><summary>↩ Tool result · `toolu_01DpGdPtzWfmj1WrrmqguTK5`</summary>

```text
Web search results for query: "Thought Anchors 2506.19143 counterfactual importance CoT sentences 2025"

Links: [{"title":"[Literature Review] Thought Anchors: Which LLM Reasoning Steps Matter?","url":"https://www.themoonlight.io/en/review/thought-anchors-which-llm-reasoning-steps-matter"},{"title":"Thought Anchors: Which LLM Reasoning Steps Matter?","url":"https://www.alignmentforum.org/posts/iLHe3vLur3NgrFPFy/thought-anchors-which-llm-reasoning-steps-matter"},{"title":"[2506.19143] Thought Anchors: Which LLM Reasoning Steps Matter?","url":"https://arxiv.org/abs/2506.19143"},{"title":"Thought Anchors: Which LLM Reasoning Steps Matter? | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/thought-anchors-which-llm-reasoning-steps-matter"},{"title":"Under review as a conference paper at ICLR 2026 THOUGHT ANCHORS: WHICH LLM","url":"https://arxiv.org/pdf/2506.19143"},{"title":"Thought Anchors: Which LLM Reasoning Steps Matter?","url":"https://arxiv.org/html/2506.19143v1"},{"title":"Thought Anchors in LLM Reasoning","url":"https://www.emergentmind.com/papers/2506.19143"},{"title":"GitHub - interp-reasoning/thought-anchors: ⚓️ Repository for the \"Thought Anchors: Which LLM Reasoning Steps Matter?\" paper.","url":"https://github.com/interp-reasoning/thought-anchors"},{"title":"Paper page - Thought Anchors: Which LLM Reasoning Steps Matter?","url":"https://huggingface.co/papers/2506.19143"},{"title":"AI Safety Diary: August 28, 2025 | Serhat Giydiren","url":"https://serhatgiydiren.com/ai-safety-diary-august-28-2025/"}]

Based on the search results, here's what I found about the paper "Thought Anchors: Which LLM Reasoning Steps Matter?" (arXiv 2506.19143):

## Overview

The paper "Thought Anchors: Which LLM Reasoning Steps Matter?" introduces a sentence-level approach to understanding and interpreting chain-of-thought (CoT) reasoning in large language models (LLMs).

## Counterfactual Importance Method

The paper introduces a black-box method that measures each sentence's counterfactual importance by repeatedly sampling replacement sentences from the model, filtering for semantically different ones, and continuing the chain of thought from that point onwards to quantify the sentence's impact on the distribution of final answers. More specifically, the method measures each sentence's counterfactual importance by resampling the model 100 times, starting from said sentence and contrasting semantically different alternatives. If replacing one sentence dramatically alters the final answer distribution, that sentence is a thought anchor.

## Key Findings

Certain sentences can have an outsized impact on the trajectory of the reasoning trace and final answer, and these sentences are termed "thought anchors." Plan generation and uncertainty management sentences have significantly higher counterfactual importance than active computation and fact retrieval sentences.

## Attribution Methods

The paper presents three complementary attribution methods: a black-box method measuring counterfactual importance, a white-box method of aggregating attention patterns between pairs of sentences identifying "broadcasting" sentences, and a causal attribution method measuring logical connections between sentences.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eea30f52-ca28-424b-8cd5-1fb744036194",
  "isSidechain": false,
  "promptId": "336e0584-08d7-4685-ad69-52c0743f6fcf",
  "type": "user",
  "uuid": "f5f631b0-2178-42d8-99df-9be6d32420bb",
  "toolUseResult": {
    "query": "Thought Anchors 2506.19143 counterfactual importance CoT sentences 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_016eZPAqtBL4LxL8FcXSaCti",
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
            "title": "Thought Anchors: Which LLM Reasoning Steps Matter? | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/thought-anchors-which-llm-reasoning-steps-matter"
          },
          {
            "title": "Under review as a conference paper at ICLR 2026 THOUGHT ANCHORS: WHICH LLM",
            "url": "https://arxiv.org/pdf/2506.19143"
          },
          {
            "title": "Thought Anchors: Which LLM Reasoning Steps Matter?",
            "url": "https://arxiv.org/html/2506.19143v1"
          },
          {
            "title": "Thought Anchors in LLM Reasoning",
            "url": "https://www.emergentmind.com/papers/2506.19143"
          },
          {
            "title": "GitHub - interp-reasoning/thought-anchors: ⚓️ Repository for the \"Thought Anchors: Which LLM Reasoning Steps Matter?\" paper.",
            "url": "https://github.com/interp-reasoning/thought-anchors"
          },
          {
            "title": "Paper page - Thought Anchors: Which LLM Reasoning Steps Matter?",
            "url": "https://huggingface.co/papers/2506.19143"
          },
          {
            "title": "AI Safety Diary: August 28, 2025 | Serhat Giydiren",
            "url": "https://serhatgiydiren.com/ai-safety-diary-august-28-2025/"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper \"Thought Anchors: Which LLM Reasoning Steps Matter?\" (arXiv 2506.19143):\n\n## Overview\n\nThe paper \"Thought Anchors: Which LLM Reasoning Steps Matter?\" introduces a sentence-level approach to understanding and interpreting chain-of-thought (CoT) reasoning in large language models (LLMs).\n\n## Counterfactual Importance Method\n\nThe paper introduces a black-box method that measures each sentence's counterfactual importance by repeatedly sampling replacement sentences from the model, filtering for semantically different ones, and continuing the chain of thought from that point onwards to quantify the sentence's impact on the distribution of final answers. More specifically, the method measures each sentence's counterfactual importance by resampling the model 100 times, starting from said sentence and contrasting semantically different alternatives. If replacing one sentence dramatically alters the final answer distribution, that sentence is a thought anchor.\n\n## Key Findings\n\nCertain sentences can have an outsized impact on the trajectory of the reasoning trace and final answer, and these sentences are termed \"thought anchors.\" Plan generation and uncertainty management sentences have significantly higher counterfactual importance than active computation and fact retrieval sentences.\n\n## Attribution Methods\n\nThe paper presents three complementary attribution methods: a black-box method measuring counterfactual importance, a white-box method of aggregating attention patterns between pairs of sentences identifying \"broadcasting\" sentences, and a causal attribution method measuring logical connections between sentences."
    ],
    "durationSeconds": 6.7160321960000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "eea30f52-ca28-424b-8cd5-1fb744036194",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T04:20:38.588Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Nh3yebV3UZD8qTa64j8yyj`</summary>

```json
{
  "query": "Occhipinti \"probing steering unfaithfulness\" ICLR 2026 LIT workshop probe intervention reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5f631b0-2178-42d8-99df-9be6d32420bb",
  "isSidechain": false,
  "requestId": "req_011CbDBMzBfvT4J8BacuCa82",
  "type": "assistant",
  "uuid": "8c320527-ee34-45d2-8014-15b28823820d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvgiwxLmSW6kVU71B84Q3b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 976,
      "cache_read_input_tokens": 31852,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 976,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 31852,
          "cache_creation_input_tokens": 976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 976
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

_source line 28 · 2026-05-20T04:20:44.138Z_

<details><summary>↩ Tool result · `toolu_01Nh3yebV3UZD8qTa64j8yyj`</summary>

```text
Web search results for query: "Occhipinti "probing steering unfaithfulness" ICLR 2026 LIT workshop probe intervention reasoning"

Links: [{"title":"ICLR Workshop 2026 - Papers","url":"https://sites.google.com/view/icbinb-2026/papers"},{"title":"ICLR 2026 Workshop | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FWorkshop"},{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/pdf/2603.01437"},{"title":"ICLR 2026 Workshop LIT | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FWorkshop%2FLIT"},{"title":"ICLR 2026 on X: \"RT @LIT_workshop: 📢 Call for Papers &amp; Reviewers | Latent &amp; Implicit Thinking (LIT) @ ICLR 2026 🧠 We’re excited to announce the Latent &amp; Imp…\" / X","url":"https://x.com/ICLR_conf/status/2016331697240080470"},{"title":"ICLR 2026 Workshops","url":"https://iclr.cc/virtual/2026/events/workshop"},{"title":"ICLR 2026 Workshop Proposals | OpenReview","url":"https://openreview.net/group?id=ICLR.cc/2026/Workshop_Proposals"},{"title":"Analysing the Safety Pitfalls of Steering Vectors","url":"https://arxiv.org/pdf/2603.24543"}]

Based on the search results, I found relevant information about the paper you're asking about.

The paper "Probing and Steering Chain-of-Thought Unfaithfulness in Language Models" by Giovanni Maria Occhipinti, Alessandro Abate, and Nandi Schoots is being presented as a poster at an ICLR 2026 workshop. 

The search results confirm the paper exists and is associated with ICLR 2026, though the specific workshop mentioned in the first result appears to be a different workshop (ICBINB 2026). The LIT (Latent & Implicit Thinking) workshop is also confirmed to be part of ICLR 2026 in Rio de Janeiro, Brazil, exploring hidden, efficient, and non-autoregressive reasoning in neural models.

However, the search results don't provide detailed information about the specific content of Occhipinti's paper regarding probe intervention reasoning techniques. To get more details about the paper's methodology and findings, you may want to check the OpenReview page for the LIT workshop or look for the paper's preprint on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c320527-ee34-45d2-8014-15b28823820d",
  "isSidechain": false,
  "promptId": "336e0584-08d7-4685-ad69-52c0743f6fcf",
  "type": "user",
  "uuid": "4326df0d-0a80-430b-b9f2-5af8026b31ed",
  "toolUseResult": {
    "query": "Occhipinti \"probing steering unfaithfulness\" ICLR 2026 LIT workshop probe intervention reasoning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Tb7hCDB864VreJE9aXYzUr",
        "content": [
          {
            "title": "ICLR Workshop 2026 - Papers",
            "url": "https://sites.google.com/view/icbinb-2026/papers"
          },
          {
            "title": "ICLR 2026 Workshop | OpenReview",
            "url": "https://openreview.net/group?id=ICLR.cc%2F2026%2FWorkshop"
          },
          {
            "title": "Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering",
            "url": "https://arxiv.org/pdf/2603.01437"
          },
          {
            "title": "ICLR 2026 Workshop LIT | OpenReview",
            "url": "https://openreview.net/group?id=ICLR.cc%2F2026%2FWorkshop%2FLIT"
          },
          {
            "title": "ICLR 2026 on X: \"RT @LIT_workshop: 📢 Call for Papers &amp; Reviewers | Latent &amp; Implicit Thinking (LIT) @ ICLR 2026 🧠 We’re excited to announce the Latent &amp; Imp…\" / X",
            "url": "https://x.com/ICLR_conf/status/2016331697240080470"
          },
          {
            "title": "ICLR 2026 Workshops",
            "url": "https://iclr.cc/virtual/2026/events/workshop"
          },
          {
            "title": "ICLR 2026 Workshop Proposals | OpenReview",
            "url": "https://openreview.net/group?id=ICLR.cc/2026/Workshop_Proposals"
          },
          {
            "title": "Analysing the Safety Pitfalls of Steering Vectors",
            "url": "https://arxiv.org/pdf/2603.24543"
          }
        ]
      },
      "Based on the search results, I found relevant information about the paper you're asking about.\n\nThe paper \"Probing and Steering Chain-of-Thought Unfaithfulness in Language Models\" by Giovanni Maria Occhipinti, Alessandro Abate, and Nandi Schoots is being presented as a poster at an ICLR 2026 workshop. \n\nThe search results confirm the paper exists and is associated with ICLR 2026, though the specific workshop mentioned in the first result appears to be a different workshop (ICBINB 2026). The LIT (Latent & Implicit Thinking) workshop is also confirmed to be part of ICLR 2026 in Rio de Janeiro, Brazil, exploring hidden, efficient, and non-autoregressive reasoning in neural models.\n\nHowever, the search results don't provide detailed information about the specific content of Occhipinti's paper regarding probe intervention reasoning techniques. To get more details about the paper's methodology and findings, you may want to check the OpenReview page for the LIT workshop or look for the paper's preprint on arXiv."
    ],
    "durationSeconds": 5.546548409999988,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8c320527-ee34-45d2-8014-15b28823820d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T04:20:47.511Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017UsnupcWRbKrAX3rDJKeju`</summary>

```json
{
  "query": "Kudo EACL 2026 \"faithfully compute\" probing activation patching synthetic arithmetic CoT 2412.01113"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4326df0d-0a80-430b-b9f2-5af8026b31ed",
  "isSidechain": false,
  "requestId": "req_011CbDBNdV1874KZK6BfPNVo",
  "type": "assistant",
  "uuid": "59b51e20-d32c-45d8-b6ae-45f93e78b7c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pp7ZgvmBCpN71PX7keuoBj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 817,
      "cache_read_input_tokens": 32828,
      "output_tokens": 82,
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
          "output_tokens": 82,
          "cache_read_input_tokens": 32828,
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

_source line 30 · 2026-05-20T04:20:56.460Z_

<details><summary>↩ Tool result · `toolu_017UsnupcWRbKrAX3rDJKeju`</summary>

```text
Web search results for query: "Kudo EACL 2026 "faithfully compute" probing activation patching synthetic arithmetic CoT 2412.01113"

Links: [{"title":"Probing for Arithmetic Errors in Language Models","url":"https://arxiv.org/pdf/2507.12379"},{"title":"LLMs Faithfully and Iteratively Compute Answers During CoT: A Systematic Analysis With Multi-step Arithmetics - ACL Anthology","url":"https://aclanthology.org/2026.findings-eacl.59/"},{"title":"7 papers were accepted at EACL 2026 | Center for Advanced Intelligence Project","url":"https://aip.riken.jp/news/eacl2026/?lang=en"},{"title":"LLMs Faithfully and Iteratively Compute Answers During CoT: A Systematic Analysis With Multi-step Arithmetics","url":"https://arxiv.org/html/2412.01113"},{"title":"RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching","url":"https://arxiv.org/pdf/2508.21258"},{"title":"[2412.01113] LLMs Faithfully and Iteratively Compute Answers During CoT: A Systematic Analysis With Multi-step Arithmetics","url":"https://arxiv.org/abs/2412.01113"},{"title":"How to use and interpret activation patching","url":"https://arxiv.org/pdf/2404.15255"},{"title":"Probe-Free Low-Rank Activation Intervention","url":"https://arxiv.org/pdf/2502.04043"}]

I found the paper you're looking for! Here are the search results:

**LLMs Faithfully and Iteratively Compute Answers During CoT: A Systematic Analysis With Multi-step Arithmetics** by Keito Kudo, Yoichi Aoki, Tatsuki Kuribayashi, Shusaku Sone, Masaya Taniguchi, Ana Brassard, Keisuke Sakaguchi, and Kentaro Inui at EACL 2026.

The paper investigates the internal information flow of large language models (LLMs) while performing chain-of-thought (CoT) style reasoning, specifically examining the faithfulness of the CoT explanation to LLMs' final answer, exploring when the LLMs' answer is (pre)determined and how strongly the information from CoT has a causal effect on the final answer.

The authors used a synthetic dataset of multi-hop arithmetic problems consisting of strings of assignments and operations ending with a query for a variable's value, which allows for controlled experiments across different levels of problem complexity.

The paper was published in the Findings of the Association for Computational Linguistics: EACL 2026, pages 1114–1153, in Rabat, Morocco. The arxiv preprint is available as 2412.01113.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59b51e20-d32c-45d8-b6ae-45f93e78b7c0",
  "isSidechain": false,
  "promptId": "336e0584-08d7-4685-ad69-52c0743f6fcf",
  "type": "user",
  "uuid": "eeefd661-063f-4ded-86f7-6e8cec3a46c5",
  "toolUseResult": {
    "query": "Kudo EACL 2026 \"faithfully compute\" probing activation patching synthetic arithmetic CoT 2412.01113",
    "results": [
      {
        "tool_use_id": "srvtoolu_016Ct8cZUgkR2pWsCTun1uXx",
        "content": [
          {
            "title": "Probing for Arithmetic Errors in Language Models",
            "url": "https://arxiv.org/pdf/2507.12379"
          },
          {
            "title": "LLMs Faithfully and Iteratively Compute Answers During CoT: A Systematic Analysis With Multi-step Arithmetics - ACL Anthology",
            "url": "https://aclanthology.org/2026.findings-eacl.59/"
          },
          {
            "title": "7 papers were accepted at EACL 2026 | Center for Advanced Intelligence Project",
            "url": "https://aip.riken.jp/news/eacl2026/?lang=en"
          },
          {
            "title": "LLMs Faithfully and Iteratively Compute Answers During CoT: A Systematic Analysis With Multi-step Arithmetics",
            "url": "https://arxiv.org/html/2412.01113"
          },
          {
            "title": "RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching",
            "url": "https://arxiv.org/pdf/2508.21258"
          },
          {
            "title": "[2412.01113] LLMs Faithfully and Iteratively Compute Answers During CoT: A Systematic Analysis With Multi-step Arithmetics",
            "url": "https://arxiv.org/abs/2412.01113"
          },
          {
            "title": "How to use and interpret activation patching",
            "url": "https://arxiv.org/pdf/2404.15255"
          },
          {
            "title": "Probe-Free Low-Rank Activation Intervention",
            "url": "https://arxiv.org/pdf/2502.04043"
          }
        ]
      },
      "I found the paper you're looking for! Here are the search results:\n\n**LLMs Faithfully and Iteratively Compute Answers During CoT: A Systematic Analysis With Multi-step Arithmetics** by Keito Kudo, Yoichi Aoki, Tatsuki Kuribayashi, Shusaku Sone, Masaya Taniguchi, Ana Brassard, Keisuke Sakaguchi, and Kentaro Inui at EACL 2026.\n\nThe paper investigates the internal information flow of large language models (LLMs) while performing chain-of-thought (CoT) style reasoning, specifically examining the faithfulness of the CoT explanation to LLMs' final answer, exploring when the LLMs' answer is (pre)determined and how strongly the information from CoT has a causal effect on the final answer.\n\nThe authors used a synthetic dataset of multi-hop arithmetic problems consisting of strings of assignments and operations ending with a query for a variable's value, which allows for controlled experiments across different levels of problem complexity.\n\nThe paper was published in the Findings of the Association for Computational Linguistics: EACL 2026, pages 1114–1153, in Rabat, Morocco. The arxiv preprint is available as 2412.01113."
    ],
    "durationSeconds": 8.943986633000007,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "59b51e20-d32c-45d8-b6ae-45f93e78b7c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-20T04:20:56.467Z_

```json
{
  "parentUuid": "eeefd661-063f-4ded-86f7-6e8cec3a46c5",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6e9ae073-c904-4d0c-9bb4-8c7e1eee5fcd",
  "timestamp": "2026-05-20T04:20:56.467Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness  ## Description When a reasoning model gets the right answer, is i…",
  "leafUuid": "6e9ae073-c904-4d0c-9bb4-8c7e1eee5fcd",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Information-Contribution Gap for reasoning faithfulness",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0"
}
```

---

### Tool call

_source line 34 · 2026-05-20T04:20:59.590Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011ApQDD6fYKMbjDSYxDc9iy`</summary>

```json
{
  "query": "Wang 2604.15726 \"LLM reasoning is latent\" H1 H2 hypothesis faithful unfaithful 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e9ae073-c904-4d0c-9bb4-8c7e1eee5fcd",
  "isSidechain": false,
  "requestId": "req_011CbDBPYCHdqH6vu5XsgHdg",
  "type": "assistant",
  "uuid": "75c66e34-64e1-475a-a363-f7880a4d008e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ronrm6phfT1yUXEhbS1ZRX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 909,
      "cache_read_input_tokens": 33645,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 909,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 33645,
          "cache_creation_input_tokens": 909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 909
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

_source line 35 · 2026-05-20T04:21:05.217Z_

<details><summary>↩ Tool result · `toolu_011ApQDD6fYKMbjDSYxDc9iy`</summary>

```text
Web search results for query: "Wang 2604.15726 "LLM reasoning is latent" H1 H2 hypothesis faithful unfaithful 2026"

Links: [{"title":"[2604.15726] LLM Reasoning Is Latent, Not the Chain of Thought","url":"https://arxiv.org/abs/2604.15726"},{"title":"LLM Reasoning Is Latent, Not the Chain of Thought","url":"https://arxiv.org/html/2604.15726"},{"title":"Dissociation of Faithful and Unfaithful Reasoning in LLMs","url":"https://arxiv.org/pdf/2405.15092"},{"title":"On the Hardness of Faithful Chain-of-Thought Reasoning in Large Language   Models","url":"https://arxiv.org/pdf/2406.10625"},{"title":"[2604.08401] Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing","url":"https://arxiv.org/abs/2604.08401"}]

I found the paper you're looking for! Here are the key details:

The paper "LLM Reasoning Is Latent, Not the Chain of Thought" (arXiv:2604.15726) argues that large language model reasoning should be studied as latent-state trajectory formation rather than as faithful surface chain-of-thought.

The paper formalizes three competing hypotheses: H1, reasoning is primarily mediated by latent-state trajectories; H2, reasoning is primarily mediated by explicit surface CoT; and H0, most apparent reasoning gains are better explained by generic serial compute than by any privileged representational object.

The paper notes that this matters because claims about faithfulness, interpretability, reasoning benchmarks, and inference-time intervention all depend on what the field takes the primary object of reasoning to be.

The paper was posted on arXiv on April 17, 2026, and is authored by Wenshuo Wang from the School of Future Technology at South China University of Technology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75c66e34-64e1-475a-a363-f7880a4d008e",
  "isSidechain": false,
  "promptId": "336e0584-08d7-4685-ad69-52c0743f6fcf",
  "type": "user",
  "uuid": "2eaff11c-4f71-4e62-bf1d-712a044c95ac",
  "toolUseResult": {
    "query": "Wang 2604.15726 \"LLM reasoning is latent\" H1 H2 hypothesis faithful unfaithful 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UP8uGT7uTzTqRB7WcWuyW9",
        "content": [
          {
            "title": "[2604.15726] LLM Reasoning Is Latent, Not the Chain of Thought",
            "url": "https://arxiv.org/abs/2604.15726"
          },
          {
            "title": "LLM Reasoning Is Latent, Not the Chain of Thought",
            "url": "https://arxiv.org/html/2604.15726"
          },
          {
            "title": "Dissociation of Faithful and Unfaithful Reasoning in LLMs",
            "url": "https://arxiv.org/pdf/2405.15092"
          },
          {
            "title": "On the Hardness of Faithful Chain-of-Thought Reasoning in Large Language   Models",
            "url": "https://arxiv.org/pdf/2406.10625"
          },
          {
            "title": "[2604.08401] Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing",
            "url": "https://arxiv.org/abs/2604.08401"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details:\n\nThe paper \"LLM Reasoning Is Latent, Not the Chain of Thought\" (arXiv:2604.15726) argues that large language model reasoning should be studied as latent-state trajectory formation rather than as faithful surface chain-of-thought.\n\nThe paper formalizes three competing hypotheses: H1, reasoning is primarily mediated by latent-state trajectories; H2, reasoning is primarily mediated by explicit surface CoT; and H0, most apparent reasoning gains are better explained by generic serial compute than by any privileged representational object.\n\nThe paper notes that this matters because claims about faithfulness, interpretability, reasoning benchmarks, and inference-time intervention all depend on what the field takes the primary object of reasoning to be.\n\nThe paper was posted on arXiv on April 17, 2026, and is authored by Wenshuo Wang from the School of Future Technology at South China University of Technology."
    ],
    "durationSeconds": 5.623612450999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "75c66e34-64e1-475a-a363-f7880a4d008e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T04:21:07.803Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F21NYXdPbcj9uc7kegVY1x`</summary>

```json
{
  "query": "combining probe trajectories behavioral causal measurement reasoning faithfulness unified framework temporal 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2eaff11c-4f71-4e62-bf1d-712a044c95ac",
  "isSidechain": false,
  "requestId": "req_011CbDBQBdK1uEFTse5JwA75",
  "type": "assistant",
  "uuid": "fdb16f0e-667f-4bfa-a51a-e020d303f2b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kuzsn2YjmA4YfQDbLWsaMb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 597,
      "cache_read_input_tokens": 34554,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 597,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 34554,
          "cache_creation_input_tokens": 597,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 597
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

_source line 37 · 2026-05-20T04:21:14.208Z_

<details><summary>↩ Tool result · `toolu_01F21NYXdPbcj9uc7kegVY1x`</summary>

```text
Web search results for query: "combining probe trajectories behavioral causal measurement reasoning faithfulness unified framework temporal 2026"

Links: [{"title":"Causal Decoupling for Temporal Knowledge Graph Reasoning via Contrastive Learning and Adaptive Fusion","url":"https://www.mdpi.com/2078-2489/16/9/717"},{"title":"Published at Latent & Implicit Thinking Workshop @ ICLR 2026","url":"https://openreview.net/pdf/d14277b6518be41dfa71a1cd3224d4de191e2b8a.pdf"},{"title":"Measuring and Improving Faithfulness of Chain-of-Thought ...","url":"https://aclanthology.org/2024.findings-emnlp.882.pdf"},{"title":"A General Framework on Conditions for Constraint-based Causal Learning","url":"https://arxiv.org/pdf/2408.07575"},{"title":"[2402.13950] Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning","url":"https://arxiv.org/abs/2402.13950"},{"title":"Temporal Causal Reasoning with (Non-Recursive) Structural Equation Models","url":"https://arxiv.org/pdf/2501.10190"},{"title":"Causal Intervention and Counterfactual Reasoning for Multimodal Pedestrian Trajectory Prediction","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12653532/"}]

The search returned several relevant results related to your query. Here's what I found:

**Most Relevant Match:**

The most directly relevant result appears to be a research paper from the Latent & Implicit Thinking Workshop at ICLR 2026 that tests step necessity and early decodability, characterizes step-to-step influence propagation, and probes trajectory-level superposition across rollouts by conceptualizing latent Chain-of-Thought as a causal system and evaluating it with intervention-based causal analysis.

**Other Related Work:**

The search also identified several other papers addressing related topics:

1. **Faithfulness in Reasoning**: Research examining causal mediation analysis to understand how intermediate reasoning steps influence final outcomes and finding that LLMs do not reliably use their intermediate reasoning steps when generating answers.

2. **Temporal Causal Reasoning**: Work combining structural equation models with temporal reasoning for causal reasoning about actual causality.

3. **Trajectory Prediction**: A framework that shifts trajectory prediction from associative learning to causal inference through hierarchical architecture with causal intervention fusion and counterfactual reasoning components.

The results suggest this is an active research area combining probe methods, behavioral analysis, causal reasoning, and measurement of model faithfulness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdb16f0e-667f-4bfa-a51a-e020d303f2b5",
  "isSidechain": false,
  "promptId": "336e0584-08d7-4685-ad69-52c0743f6fcf",
  "type": "user",
  "uuid": "9074b744-07ed-4016-b149-aa07433da391",
  "toolUseResult": {
    "query": "combining probe trajectories behavioral causal measurement reasoning faithfulness unified framework temporal 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DXL5TM3SkLaMQmi4nFQHfc",
        "content": [
          {
            "title": "Causal Decoupling for Temporal Knowledge Graph Reasoning via Contrastive Learning and Adaptive Fusion",
            "url": "https://www.mdpi.com/2078-2489/16/9/717"
          },
          {
            "title": "Published at Latent & Implicit Thinking Workshop @ ICLR 2026",
            "url": "https://openreview.net/pdf/d14277b6518be41dfa71a1cd3224d4de191e2b8a.pdf"
          },
          {
            "title": "Measuring and Improving Faithfulness of Chain-of-Thought ...",
            "url": "https://aclanthology.org/2024.findings-emnlp.882.pdf"
          },
          {
            "title": "A General Framework on Conditions for Constraint-based Causal Learning",
            "url": "https://arxiv.org/pdf/2408.07575"
          },
          {
            "title": "[2402.13950] Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/abs/2402.13950"
          },
          {
            "title": "Temporal Causal Reasoning with (Non-Recursive) Structural Equation Models",
            "url": "https://arxiv.org/pdf/2501.10190"
          },
          {
            "title": "Causal Intervention and Counterfactual Reasoning for Multimodal Pedestrian Trajectory Prediction",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12653532/"
          }
        ]
      },
      "The search returned several relevant results related to your query. Here's what I found:\n\n**Most Relevant Match:**\n\nThe most directly relevant result appears to be a research paper from the Latent & Implicit Thinking Workshop at ICLR 2026 that tests step necessity and early decodability, characterizes step-to-step influence propagation, and probes trajectory-level superposition across rollouts by conceptualizing latent Chain-of-Thought as a causal system and evaluating it with intervention-based causal analysis.\n\n**Other Related Work:**\n\nThe search also identified several other papers addressing related topics:\n\n1. **Faithfulness in Reasoning**: Research examining causal mediation analysis to understand how intermediate reasoning steps influence final outcomes and finding that LLMs do not reliably use their intermediate reasoning steps when generating answers.\n\n2. **Temporal Causal Reasoning**: Work combining structural equation models with temporal reasoning for causal reasoning about actual causality.\n\n3. **Trajectory Prediction**: A framework that shifts trajectory prediction from associative learning to causal inference through hierarchical architecture with causal intervention fusion and counterfactual reasoning components.\n\nThe results suggest this is an active research area combining probe methods, behavioral analysis, causal reasoning, and measurement of model faithfulness."
    ],
    "durationSeconds": 6.401480387000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fdb16f0e-667f-4bfa-a51a-e020d303f2b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T04:21:17.094Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015KZVGkj8VvktMkEUR1Bbhz`</summary>

```json
{
  "query": "Cox 2603.01437 \"decoding answers before chain-of-thought\" pre-CoT probes activation steering reasoning models failure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9074b744-07ed-4016-b149-aa07433da391",
  "isSidechain": false,
  "requestId": "req_011CbDBQr3N2pBaKkvJPMDfM",
  "type": "assistant",
  "uuid": "d7479987-2bd5-40f1-b5a6-bfa1c5c25dcc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018uhY35FfKfJgXug24Qc7qF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 35151,
      "output_tokens": 81,
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
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 35151,
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

_source line 39 · 2026-05-20T04:21:24.079Z_

<details><summary>↩ Tool result · `toolu_015KZVGkj8VvktMkEUR1Bbhz`</summary>

```text
Web search results for query: "Cox 2603.01437 "decoding answers before chain-of-thought" pre-CoT probes activation steering reasoning models failure"

Links: [{"title":"[2603.01437] Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/abs/2603.01437"},{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/html/2603.01437"},{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/pdf/2603.01437"},{"title":"Post-hoc reasoning in chain of thought - Kyle Cox ·","url":"https://kyle-cox.com/2024/12/26/cot-interp/"},{"title":"[Literature Review] Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://www.themoonlight.io/en/review/decoding-answers-before-chain-of-thought-evidence-from-pre-cot-probes-and-activation-steering"}]

I found the paper! Here's what the search results reveal about arXiv paper 2603.01437:

## Paper Overview

The paper provides mechanistic evidence that instruction-tuned models often determine their answer before generating chain-of-thought (CoT). The authors are Kyle Cox, Darius Kianersi, and Adrià Garriga-Alonso.

## Key Findings

**Pre-CoT Probes:**
By training linear probes on residual stream activations at the last token before CoT, they can predict the model's final answer with 0.9 AUC on most tasks.

**Activation Steering:**
These directions are not only predictive, but also causal: steering activations along the probe direction flips model answers in over 50% of cases, significantly exceeding orthogonal baselines.

## Failure Modes

When steering induces incorrect answers, two distinct failure modes are observed: non-entailment (stating correct premises but drawing unsupported conclusions) and confabulation (fabricating false premises).

## Implications

The utility of CoT toward interpretability depends upon its faithfulness—whether the model's stated reasoning reflects the underlying decision process. The paper suggests that post-hoc reasoning can produce undesirable behaviors when models reason from false beliefs.

The paper was submitted on March 2, 2026, and challenges the assumption that chain-of-thought explanations genuinely reflect how reasoning models arrive at their decisions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7479987-2bd5-40f1-b5a6-bfa1c5c25dcc",
  "isSidechain": false,
  "promptId": "336e0584-08d7-4685-ad69-52c0743f6fcf",
  "type": "user",
  "uuid": "336be388-3e88-4bf4-8631-3d0353894e7c",
  "toolUseResult": {
    "query": "Cox 2603.01437 \"decoding answers before chain-of-thought\" pre-CoT probes activation steering reasoning models failure",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ks9kNKuR5eByyPnsjg5NJM",
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
            "title": "Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering",
            "url": "https://arxiv.org/pdf/2603.01437"
          },
          {
            "title": "Post-hoc reasoning in chain of thought - Kyle Cox ·",
            "url": "https://kyle-cox.com/2024/12/26/cot-interp/"
          },
          {
            "title": "[Literature Review] Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering",
            "url": "https://www.themoonlight.io/en/review/decoding-answers-before-chain-of-thought-evidence-from-pre-cot-probes-and-activation-steering"
          }
        ]
      },
      "I found the paper! Here's what the search results reveal about arXiv paper 2603.01437:\n\n## Paper Overview\n\nThe paper provides mechanistic evidence that instruction-tuned models often determine their answer before generating chain-of-thought (CoT). The authors are Kyle Cox, Darius Kianersi, and Adrià Garriga-Alonso.\n\n## Key Findings\n\n**Pre-CoT Probes:**\nBy training linear probes on residual stream activations at the last token before CoT, they can predict the model's final answer with 0.9 AUC on most tasks.\n\n**Activation Steering:**\nThese directions are not only predictive, but also causal: steering activations along the probe direction flips model answers in over 50% of cases, significantly exceeding orthogonal baselines.\n\n## Failure Modes\n\nWhen steering induces incorrect answers, two distinct failure modes are observed: non-entailment (stating correct premises but drawing unsupported conclusions) and confabulation (fabricating false premises).\n\n## Implications\n\nThe utility of CoT toward interpretability depends upon its faithfulness—whether the model's stated reasoning reflects the underlying decision process. The paper suggests that post-hoc reasoning can produce undesirable behaviors when models reason from false beliefs.\n\nThe paper was submitted on March 2, 2026, and challenges the assumption that chain-of-thought explanations genuinely reflect how reasoning models arrive at their decisions."
    ],
    "durationSeconds": 6.980806213000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d7479987-2bd5-40f1-b5a6-bfa1c5c25dcc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-20T04:21:27.536Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me also search for some more specific aspects to understand whether anyone has already proposed the specific dual-stream framework this proposal describes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "336be388-3e88-4bf4-8631-3d0353894e7c",
  "isSidechain": false,
  "requestId": "req_011CbDBRaGN9vftShDazbd1E",
  "type": "assistant",
  "uuid": "445d2451-f474-4ad4-b9a2-98ceac3c37a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qxasbedszajcfZ6RhNgGy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 758,
      "cache_read_input_tokens": 35905,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 758,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 35905,
          "cache_creation_input_tokens": 758,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 758
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

_source line 41 · 2026-05-20T04:21:28.061Z_

Now let me search for a couple more critical aspects before forming my assessment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "445d2451-f474-4ad4-b9a2-98ceac3c37a8",
  "isSidechain": false,
  "requestId": "req_011CbDBRaGN9vftShDazbd1E",
  "type": "assistant",
  "uuid": "9c8eeea8-0b10-4c6d-a584-3278e313da11",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qxasbedszajcfZ6RhNgGy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 758,
      "cache_read_input_tokens": 35905,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 758,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 35905,
          "cache_creation_input_tokens": 758,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 758
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

_source line 42 · 2026-05-20T04:21:28.749Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018wmoemGjQR9DKzZr7aZTqY`</summary>

```json
{
  "query": "\"information contribution gap\" OR \"ICG\" probe causal gap faithfulness reasoning trajectory temporal 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c8eeea8-0b10-4c6d-a584-3278e313da11",
  "isSidechain": false,
  "requestId": "req_011CbDBRaGN9vftShDazbd1E",
  "type": "assistant",
  "uuid": "1065dec2-0371-48e7-aa66-33b8f8c4de60",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qxasbedszajcfZ6RhNgGy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 758,
      "cache_read_input_tokens": 35905,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 758,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 35905,
          "cache_creation_input_tokens": 758,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 758
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

_source line 43 · 2026-05-20T04:21:36.791Z_

<details><summary>↩ Tool result · `toolu_018wmoemGjQR9DKzZr7aZTqY`</summary>

```text
Web search results for query: ""information contribution gap" OR "ICG" probe causal gap faithfulness reasoning trajectory temporal 2026"

Links: [{"title":"Towards Transparent Reasoning: What Drives Faithfulness in Large Language Models?","url":"https://arxiv.org/html/2510.24236v2"},{"title":"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2602.11201"},{"title":"Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING","url":"https://openreview.net/pdf?id=lN3yKqqzF1"},{"title":"Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning | Request PDF","url":"https://www.researchgate.net/publication/386203451_Making_Reasoning_Matter_Measuring_and_Improving_Faithfulness_of_Chain-of-Thought_Reasoning"},{"title":"Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2402.13950v3"},{"title":"faithcot-bench: benchmarking instance- level faithfulness of ...","url":"https://arxiv.org/pdf/2510.04040"},{"title":"FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2510.04040v1"},{"title":"CausalGPT: Illuminating Faithfulness and Causality for Knowledge Reasoning with Foundation Models","url":"https://arxiv.org/html/2308.11914"}]

Based on the search results, I found relevant research on reasoning, faithfulness, and causal gaps in large language models, though I didn't find specific results using the exact term "Information Contribution Gap" (ICG). Here's what the search revealed:

## Recent Research on Faithfulness and Causal Analysis

Recent work has identified that unfaithfulness can arise when the reasoning process breaks down, with trajectories failing to maintain internal logical continuity, leaving gaps, contradictions, or irrelevant reasoning.

One study demonstrates that models can encode task-relevant structure without utilizing it, challenging assumptions in interpretability research. The research identifies a reasoning horizon that marks a consistent transition point at 70–85% of chain length, beyond which reasoning tokens contribute negligible or harmful causal influence.

## Methods for Probing Faithfulness

Researchers use several approaches to probe chain-of-thought (CoT) faithfulness:

- Perturbation methods perturb reasoning traces through adding mistakes, removing steps, or forcing early answers, then test whether the final prediction changes, treating causal sensitivity as evidence of faithfulness.

- Logit-based methods leverage model-internal diagnostics, such as analyzing logit variations or measuring information gain to approximate causal alignment between CoTs and outputs.

If you're looking for more specific information about "ICG" or "Information Contribution Gap" as a particular metric or framework, the search results suggest this may be very recent work from 2026 or use different terminology in published papers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1065dec2-0371-48e7-aa66-33b8f8c4de60",
  "isSidechain": false,
  "promptId": "336e0584-08d7-4685-ad69-52c0743f6fcf",
  "type": "user",
  "uuid": "cdb7b363-faef-4698-ac4e-fe868fe04f97",
  "toolUseResult": {
    "query": "\"information contribution gap\" OR \"ICG\" probe causal gap faithfulness reasoning trajectory temporal 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XzqpGxRNf5kbfXSDwTNssp",
        "content": [
          {
            "title": "Towards Transparent Reasoning: What Drives Faithfulness in Large Language Models?",
            "url": "https://arxiv.org/html/2510.24236v2"
          },
          {
            "title": "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2602.11201"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING",
            "url": "https://openreview.net/pdf?id=lN3yKqqzF1"
          },
          {
            "title": "Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning | Request PDF",
            "url": "https://www.researchgate.net/publication/386203451_Making_Reasoning_Matter_Measuring_and_Improving_Faithfulness_of_Chain-of-Thought_Reasoning"
          },
          {
            "title": "Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2402.13950v3"
          },
          {
            "title": "faithcot-bench: benchmarking instance- level faithfulness of ...",
            "url": "https://arxiv.org/pdf/2510.04040"
          },
          {
            "title": "FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2510.04040v1"
          },
          {
            "title": "CausalGPT: Illuminating Faithfulness and Causality for Knowledge Reasoning with Foundation Models",
            "url": "https://arxiv.org/html/2308.11914"
          }
        ]
      },
      "Based on the search results, I found relevant research on reasoning, faithfulness, and causal gaps in large language models, though I didn't find specific results using the exact term \"Information Contribution Gap\" (ICG). Here's what the search revealed:\n\n## Recent Research on Faithfulness and Causal Analysis\n\nRecent work has identified that unfaithfulness can arise when the reasoning process breaks down, with trajectories failing to maintain internal logical continuity, leaving gaps, contradictions, or irrelevant reasoning.\n\nOne study demonstrates that models can encode task-relevant structure without utilizing it, challenging assumptions in interpretability research. The research identifies a reasoning horizon that marks a consistent transition point at 70–85% of chain length, beyond which reasoning tokens contribute negligible or harmful causal influence.\n\n## Methods for Probing Faithfulness\n\nResearchers use several approaches to probe chain-of-thought (CoT) faithfulness:\n\n- Perturbation methods perturb reasoning traces through adding mistakes, removing steps, or forcing early answers, then test whether the final prediction changes, treating causal sensitivity as evidence of faithfulness.\n\n- Logit-based methods leverage model-internal diagnostics, such as analyzing logit variations or measuring information gain to approximate causal alignment between CoTs and outputs.\n\nIf you're looking for more specific information about \"ICG\" or \"Information Contribution Gap\" as a particular metric or framework, the search results suggest this may be very recent work from 2026 or use different terminology in published papers."
    ],
    "durationSeconds": 8.036659188999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1065dec2-0371-48e7-aa66-33b8f8c4de60",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-20T04:21:39.696Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012M49JUZ3DAQgZhwEMeoEGZ`</summary>

```json
{
  "query": "Ballon 2601.23163 \"probing trajectories reasoning traces\" truncation reinjection prefix accuracy 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdb7b363-faef-4698-ac4e-fe868fe04f97",
  "isSidechain": false,
  "requestId": "req_011CbDBSWdceuj1jkd4wDar1",
  "type": "assistant",
  "uuid": "4c4b508d-4907-475a-88e5-b844516cdc0d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7ZSMioJrWp9YxSEVBz3bX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 915,
      "cache_read_input_tokens": 36663,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 915,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 36663,
          "cache_creation_input_tokens": 915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 915
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

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness  ## Description When a reasoning model gets the right answer, is i…",
  "leafUuid": "4c4b508d-4907-475a-88e5-b844516cdc0d",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Information-Contribution Gap for reasoning faithfulness",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0"
}
```

---

### Tool result

_source line 47 · 2026-05-20T04:21:46.997Z_

<details><summary>↩ Tool result · `toolu_012M49JUZ3DAQgZhwEMeoEGZ`</summary>

```text
Web search results for query: "Ballon 2601.23163 "probing trajectories reasoning traces" truncation reinjection prefix accuracy 2026"

Links: [{"title":"[2601.23163] Probing the Trajectories of Reasoning Traces in Large Language Models","url":"https://arxiv.org/abs/2601.23163"},{"title":"Probing the Trajectories of Reasoning Traces in Large Language Models","url":"https://arxiv.org/html/2601.23163"},{"title":"(PDF) Probing the Trajectories of Reasoning Traces in ...","url":"https://www.researchgate.net/publication/400340042_Probing_the_Trajectories_of_Reasoning_Traces_in_Large_Language_Models"},{"title":"The Path of Least Resistance: Guiding LLM Reasoning Trajectories with Prefix Consensus","url":"https://arxiv.org/pdf/2601.21494"},{"title":"The path of least Resistance: Guiding LLM reasoning trajectories with Prefix consensus","url":"https://arxiv.org/html/2601.21494v2"},{"title":"[2601.21494] The Path of Least Resistance: Guiding LLM Reasoning Trajectories with Prefix Consensus","url":"https://arxiv.org/abs/2601.21494"}]

Based on the search results, I found the paper you're looking for:

The paper titled "Probing the Trajectories of Reasoning Traces in Large Language Models" is by Marthe Ballon and 3 other authors (arXiv 2601.23163).

The research proposes a protocol to systematically probe the trajectories of reasoning traces in LLMs by 1) generating a model's reasoning trace, 2) truncating it at fixed token-percentiles, and 3) injecting each partial trace back into the model (or a different model) to measure the induced distribution over answer choices via next-token probabilities.

Key findings from the paper include:

- It examines how accuracy and decision commitment evolve along a reasoning trajectory, and whether intermediate trace segments provide answer-relevant information beyond generic length or stylistic effects.

- The research found a negative correlation between full-trace length and accuracy, contributing to the underthinking/overthinking debate, with longer traces appearing largely difficulty-reactive rather than inherently beneficial.

- The observation that accuracy gains derive from instance-aligned semantic content (rather than mere length or structural form) suggests that naive truncation or trace-compression strategies risk discarding signal that materially affects correctness.

The paper was submitted on January 30, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c4b508d-4907-475a-88e5-b844516cdc0d",
  "isSidechain": false,
  "promptId": "336e0584-08d7-4685-ad69-52c0743f6fcf",
  "type": "user",
  "uuid": "1c48e8e8-296d-4d19-b308-14b64e25aa1f",
  "toolUseResult": {
    "query": "Ballon 2601.23163 \"probing trajectories reasoning traces\" truncation reinjection prefix accuracy 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HxKJVUoGWCG9mBZnAihM8R",
        "content": [
          {
            "title": "[2601.23163] Probing the Trajectories of Reasoning Traces in Large Language Models",
            "url": "https://arxiv.org/abs/2601.23163"
          },
          {
            "title": "Probing the Trajectories of Reasoning Traces in Large Language Models",
            "url": "https://arxiv.org/html/2601.23163"
          },
          {
            "title": "(PDF) Probing the Trajectories of Reasoning Traces in ...",
            "url": "https://www.researchgate.net/publication/400340042_Probing_the_Trajectories_of_Reasoning_Traces_in_Large_Language_Models"
          },
          {
            "title": "The Path of Least Resistance: Guiding LLM Reasoning Trajectories with Prefix Consensus",
            "url": "https://arxiv.org/pdf/2601.21494"
          },
          {
            "title": "The path of least Resistance: Guiding LLM reasoning trajectories with Prefix consensus",
            "url": "https://arxiv.org/html/2601.21494v2"
          },
          {
            "title": "[2601.21494] The Path of Least Resistance: Guiding LLM Reasoning Trajectories with Prefix Consensus",
            "url": "https://arxiv.org/abs/2601.21494"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper titled \"Probing the Trajectories of Reasoning Traces in Large Language Models\" is by Marthe Ballon and 3 other authors (arXiv 2601.23163).\n\nThe research proposes a protocol to systematically probe the trajectories of reasoning traces in LLMs by 1) generating a model's reasoning trace, 2) truncating it at fixed token-percentiles, and 3) injecting each partial trace back into the model (or a different model) to measure the induced distribution over answer choices via next-token probabilities.\n\nKey findings from the paper include:\n\n- It examines how accuracy and decision commitment evolve along a reasoning trajectory, and whether intermediate trace segments provide answer-relevant information beyond generic length or stylistic effects.\n\n- The research found a negative correlation between full-trace length and accuracy, contributing to the underthinking/overthinking debate, with longer traces appearing largely difficulty-reactive rather than inherently beneficial.\n\n- The observation that accuracy gains derive from instance-aligned semantic content (rather than mere length or structural form) suggests that naive truncation or trace-compression strategies risk discarding signal that materially affects correctness.\n\nThe paper was submitted on January 30, 2026."
    ],
    "durationSeconds": 7.297282500999979,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4c4b508d-4907-475a-88e5-b844516cdc0d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-20T04:21:50.235Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G9Kd4pBNfM1Ujdo85SJzmf`</summary>

```json
{
  "query": "Gjølbye 2605.15454 \"reasoning models move differently\" difficulty geometry coupling temporal hidden states 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c48e8e8-296d-4d19-b308-14b64e25aa1f",
  "isSidechain": false,
  "requestId": "req_011CbDBTGETgFUj8JyLAFvY3",
  "type": "assistant",
  "uuid": "f2699e21-ac91-4cd9-81d5-ecdbe3a3a886",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4c8m3uS5hBMHW2G52KsBN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 37578,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 723,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 37578,
          "cache_creation_input_tokens": 723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 723
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

_source line 49 · 2026-05-20T04:21:56.556Z_

<details><summary>↩ Tool result · `toolu_01G9Kd4pBNfM1Ujdo85SJzmf`</summary>

```text
Web search results for query: "Gjølbye 2605.15454 "reasoning models move differently" difficulty geometry coupling temporal hidden states 2026"

Links: [{"title":"[2605.15454] Reasoning Models Don't Just Think Longer, They Move Differently","url":"https://arxiv.org/abs/2605.15454"},{"title":"Reasoning Models Don’t Just Think Longer, They Move Differently","url":"https://arxiv.org/html/2605.15454"},{"title":"GeomVerse: A Systematic Evaluation of Large Models for Geometric Reasoning | OpenReview","url":"https://openreview.net/forum?id=1AUbiBrOF1"},{"title":"The Geometry of Thought: How Scale Restructures Reasoning In Large Language Models","url":"https://arxiv.org/pdf/2601.13358"},{"title":"GenesisGeo: Technical Report","url":"https://arxiv.org/pdf/2509.21896"},{"title":"GeometryZero: Improving Geometry Solving for LLM with Group Contrastive Policy Optimization","url":"https://arxiv.org/pdf/2506.07160"}]

Based on the web search results, I found the paper you're looking for:

"Reasoning Models Don't Just Think Longer, They Move Differently" (arXiv:2605.15454) by Anders Gjølbye, Lars Kai Hansen, and Sanmi Koyejo was published on May 14, 2026.

The paper investigates whether reasoning-trained language models simply compute for more steps or follow fundamentally different internal trajectories. The researchers study this distinction through hidden-state trajectories during chain-of-thought generation across competitive programming, mathematics, and Boolean satisfiability.

A key finding is that raw trajectory geometry is strongly shaped by generation length, so comparisons without adjustment are misleading, but after residualizing trajectory statistics on length, difficulty remains systematically coupled to corrected trajectory geometry across all domains studied.

The clearest reasoning-specific separation appears in the code domain, where harder problems show more direct corrected trajectories and less heterogeneous local curvature in reasoning-trained models than in matched instruction-tuned baselines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2699e21-ac91-4cd9-81d5-ecdbe3a3a886",
  "isSidechain": false,
  "promptId": "336e0584-08d7-4685-ad69-52c0743f6fcf",
  "type": "user",
  "uuid": "6d097578-e95d-46d4-8ed9-fb64792c3f68",
  "toolUseResult": {
    "query": "Gjølbye 2605.15454 \"reasoning models move differently\" difficulty geometry coupling temporal hidden states 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JNvgrSnSLVSvi1FYTVBsyX",
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
            "title": "GeomVerse: A Systematic Evaluation of Large Models for Geometric Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=1AUbiBrOF1"
          },
          {
            "title": "The Geometry of Thought: How Scale Restructures Reasoning In Large Language Models",
            "url": "https://arxiv.org/pdf/2601.13358"
          },
          {
            "title": "GenesisGeo: Technical Report",
            "url": "https://arxiv.org/pdf/2509.21896"
          },
          {
            "title": "GeometryZero: Improving Geometry Solving for LLM with Group Contrastive Policy Optimization",
            "url": "https://arxiv.org/pdf/2506.07160"
          }
        ]
      },
      "Based on the web search results, I found the paper you're looking for:\n\n\"Reasoning Models Don't Just Think Longer, They Move Differently\" (arXiv:2605.15454) by Anders Gjølbye, Lars Kai Hansen, and Sanmi Koyejo was published on May 14, 2026.\n\nThe paper investigates whether reasoning-trained language models simply compute for more steps or follow fundamentally different internal trajectories. The researchers study this distinction through hidden-state trajectories during chain-of-thought generation across competitive programming, mathematics, and Boolean satisfiability.\n\nA key finding is that raw trajectory geometry is strongly shaped by generation length, so comparisons without adjustment are misleading, but after residualizing trajectory statistics on length, difficulty remains systematically coupled to corrected trajectory geometry across all domains studied.\n\nThe clearest reasoning-specific separation appears in the code domain, where harder problems show more direct corrected trajectories and less heterogeneous local curvature in reasoning-trained models than in matched instruction-tuned baselines."
    ],
    "durationSeconds": 6.315202827000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f2699e21-ac91-4cd9-81d5-ecdbe3a3a886",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-20T04:23:00.288Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the landscape. Let me synthesize my findings and assess this proposal as the Discovery Agent.

Key observations from my research:

1. **The dual-stream approach (probe + causal) is genuinely novel.** No existing work combines temporal probe trajectories with temporal causal contribution measurement. The closest are:
   - Kudo et al. (EACL 2026): per-position probes + activation patching, but on synthetic arithmetic only
   - CMI (Sathyanarayanan et al.): layerwise activation patching, but structural mediation on ~50 examples
   - Occhipinti et al. 

The diagnostic-causal gap is well-established across multiple independent studies, providing a solid empirical foundation. Trajectory shapes themselves carry meaningful signal beyond static features, as shown by work on entropy patterns and geometric analysis. The proposal demonstrates thorough research with comprehensive related work coverage and clear differentiation from existing methods, and the experimental design appears well-conceived.

On novelty, the G*(t) = P*(t) - C(t) temporal gap metric is genuinely original, as is the phenomenon taxonomy derived from trajectory shapes, though the core contribution combines existing techniques rather than introducing fundamentally new components—which is valid framework-level novelty but might invite "obvious combination" critiques. The significance is clear: understanding whether chain-of-thought reasoning actually drives correct answers matters for safety, interpretability, and computational efficiency, with practical applications in inference optimization and benchmark validation. The difficulty-conditioning angle adds another layer of practical value.

The differentiation from prior work is well-executed—the distinctions from Chrabąszcz, TTS, CMI, and Thought Anchors are clearly laid out, and the cumulative-versus-marginal framing against TTS is theoretically strong. But there's a potential vulnerability: could someone just correlate pre-CoT probe accuracy with final correctness, or use trajectory features alone without explicit causal measurement to detect unfaithfulness? The proposal claims the causal dimension is necessary to distinguish faithful-correct from unfaithful-correct cases, but this needs empirical backing—if Chrabąszcz's 60+ features already capture faithfulness patterns without explicit causality, that's a real threat to the novelty claim.

There's also a deeper assumption problem with comparing P*(t) and C(t) even after normalization. The gap between these quantities might reflect confounders like problem difficulty or CoT length rather than genuine unfaithfulness, especially if they respond differently to these factors. And the "shapes over magnitudes" claim is actually quite strong—if trajectory shape is the real diagnostic signal, why not just analyze probe trajectories directly like Chrabąszcz does? The causal framing needs to demonstrate what it adds to shape-based analysis that probe-only approaches can't already provide.

One way to strengthen this would be framing the ICG framework as providing *interpretable* faithfulness diagnostics with clear semantic meaning—"knows but doesn't use" versus "genuinely computes"—rather than just predictive features. The honest scoping about potential 2-category collapse is also good practice.

But there's a circularity problem I keep coming back to: if the probe is trained to predict correctness and the model's hidden states encode correctness information early, P*(t) will naturally be high early regardless of whether the model actually "knows" the answer or just encodes surface-level correctness signals.

The null-probe calibration helps, but it only accounts for random baseline performance, not confounders like problem difficulty being encoded in the representation. A harder problem might have different hidden state characteristics that correlate with lower correctness, but that's not the same as the model "knowing" it will fail. The proposal does address this through calibration, but the core interpretive claim—that P*(t) measures "knowledge" and C(t) measures "use"—conflates probe-detectable linear structure correlated with correctness with actual knowledge.

Looking at the remaining gaps: the instruction-tuned control assumes G*(t) ≈ 0 as a sanity check, but instruction-tuned models don't do extended reasoning, so the temporal trajectories are too short to make a meaningful comparison. More fundamentally, the proposal could position this as a measurement instrument for the field—something like how causal mediation analysis became standard—rather than just a faithfulness diagnostic.

On novelty, I'm checking whether anyone else has combined probe-based information tracking with causal contribution measurement in a temporal framework. Kudo et al. use probes with activation patching but only on synthetic data without temporal gap analysis, and CMI does layerwise patching with representational analysis but structurally rather than functionally. The specific G*(t) = P*(t) - C(t) formulation with trajectory shape analysis appears genuinely novel—it's the particular combination of temporal probe trajectories, temporal causal measurement, and gap analysis that hasn't been proposed before.

Now I'm considering whether there are genuine improvements to strengthen this work. I think the framing could shift from positioning ICG as a diagnostic tool to establishing it as a measurement standard that future work must address, similar to how FaithCoT-Bench set a benchmark. Additionally, the insight about trajectory shapes could be elevated theoretically: different failure modes of CoT faithfulness have characteristic temporal signatures that remain invariant across measurement scales, which is more powerful than just treating shapes as a practical workaround for non-commensurable scales.

Let me check what's already covered in the proposal against what's missing. The proposal addresses inference-time compute allocation, benchmark validity, and safety monitoring, but there's a real gap around how ICG could inform RL training of reasoning models — understanding when CoT is decorative versus load-bearing could directly shape how we train these systems. The measurement standard framing is also implicit rather than explicit, which weakens the significance claim.

The core novelty here is more precise than just measuring faithfulness — it's capturing faithfulness as a temporal trajectory and using the shape of that trajectory to classify different types of unfaithfulness. Existing approaches give a single score per instance, but ICG reveals the underlying mechanism through its temporal signature. This is genuinely novel. I should search for whether the ICLR 2026 LIT workshop paper by Occhipinti et al. already covers similar ground, since that could affect how I position the contribution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d097578-e95d-46d4-8ed9-fb64792c3f68",
  "isSidechain": false,
  "requestId": "req_011CbDBTy9LL4Tsivr1HPJsg",
  "type": "assistant",
  "uuid": "63499a41-efd3-41b7-879d-575dc5e5cc3d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FcZxm9V3CLTXKzY5nVVoFR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 619,
      "cache_read_input_tokens": 38301,
      "output_tokens": 2452,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 619,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2452,
          "cache_read_input_tokens": 38301,
          "cache_creation_input_tokens": 619,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 619
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

_source line 51 · 2026-05-20T04:23:00.444Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S5qEueCV899z9eBDddAmob`</summary>

```json
{
  "query": "Occhipinti Abate Schoots \"probing steering chain-of-thought unfaithfulness\" ICLR 2026 LIT workshop paper methodology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63499a41-efd3-41b7-879d-575dc5e5cc3d",
  "isSidechain": false,
  "requestId": "req_011CbDBTy9LL4Tsivr1HPJsg",
  "type": "assistant",
  "uuid": "81dee174-bcff-42e1-b0ac-b1b5379aee4e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FcZxm9V3CLTXKzY5nVVoFR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 619,
      "cache_read_input_tokens": 38301,
      "output_tokens": 2452,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 619,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2452,
          "cache_read_input_tokens": 38301,
          "cache_creation_input_tokens": 619,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 619
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

_source line 52_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness  ## Description When a reasoning model gets the right answer, is i…",
  "leafUuid": "81dee174-bcff-42e1-b0ac-b1b5379aee4e",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0"
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "Information-Contribution Gap for reasoning faithfulness",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0"
}
```

---

### Tool result

_source line 54 · 2026-05-20T04:23:05.298Z_

<details><summary>↩ Tool result · `toolu_01S5qEueCV899z9eBDddAmob`</summary>

```text
Web search results for query: "Occhipinti Abate Schoots "probing steering chain-of-thought unfaithfulness" ICLR 2026 LIT workshop paper methodology"

Links: [{"title":"ICLR Workshop 2026 - Papers","url":"https://sites.google.com/view/icbinb-2026/papers"},{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/pdf/2603.01437"},{"title":"Chain-of-Thought Reasoning In The Wild Is Not Always Faithful","url":"https://arxiv.org/pdf/2503.08679"},{"title":"Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING","url":"https://arxiv.org/pdf/2510.04040"},{"title":"Is Chain-of-Thought Really Not Explainability? Chain-of-Thought Can Be Faithful without Hint Verbalization","url":"https://arxiv.org/pdf/2512.23032"},{"title":"Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?","url":"https://arxiv.org/pdf/2508.19827"}]

Based on the search results, I found information about the paper you're looking for:

"Probing and Steering Chain-of-Thought Unfaithfulness in Language Models" is a paper by Giovanni Maria Occhipinti, Alessandro Abate, and Nandi Schoots that was presented as a poster at an ICLR 2026 workshop.

However, the search results only provide the title and author information from a workshop program listing. The results do not contain detailed information about the specific methodology used in their paper. To get more detailed information about their research methodology, you would need to access the full paper directly, which may be available through the workshop's proceedings or the authors' institutional repositories.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81dee174-bcff-42e1-b0ac-b1b5379aee4e",
  "isSidechain": false,
  "promptId": "336e0584-08d7-4685-ad69-52c0743f6fcf",
  "type": "user",
  "uuid": "6ed1b323-e08a-41bf-af89-732ac3cb2a61",
  "toolUseResult": {
    "query": "Occhipinti Abate Schoots \"probing steering chain-of-thought unfaithfulness\" ICLR 2026 LIT workshop paper methodology",
    "results": [
      {
        "tool_use_id": "srvtoolu_013Q3oFqyvHS7KiTGCKz75Mr",
        "content": [
          {
            "title": "ICLR Workshop 2026 - Papers",
            "url": "https://sites.google.com/view/icbinb-2026/papers"
          },
          {
            "title": "Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering",
            "url": "https://arxiv.org/pdf/2603.01437"
          },
          {
            "title": "Chain-of-Thought Reasoning In The Wild Is Not Always Faithful",
            "url": "https://arxiv.org/pdf/2503.08679"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING",
            "url": "https://arxiv.org/pdf/2510.04040"
          },
          {
            "title": "Is Chain-of-Thought Really Not Explainability? Chain-of-Thought Can Be Faithful without Hint Verbalization",
            "url": "https://arxiv.org/pdf/2512.23032"
          },
          {
            "title": "Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?",
            "url": "https://arxiv.org/pdf/2508.19827"
          }
        ]
      },
      "Based on the search results, I found information about the paper you're looking for:\n\n\"Probing and Steering Chain-of-Thought Unfaithfulness in Language Models\" is a paper by Giovanni Maria Occhipinti, Alessandro Abate, and Nandi Schoots that was presented as a poster at an ICLR 2026 workshop.\n\nHowever, the search results only provide the title and author information from a workshop program listing. The results do not contain detailed information about the specific methodology used in their paper. To get more detailed information about their research methodology, you would need to access the full paper directly, which may be available through the workshop's proceedings or the authors' institutional repositories."
    ],
    "durationSeconds": 4.848182602000016,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "81dee174-bcff-42e1-b0ac-b1b5379aee4e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T04:23:08.157Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W8Zj64UtvFEBZVPJVtgbu8`</summary>

```json
{
  "query": "site:openreview.net Occhipinti \"probing and steering\" unfaithfulness chain-of-thought 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ed1b323-e08a-41bf-af89-732ac3cb2a61",
  "isSidechain": false,
  "requestId": "req_011CbDBZ33NuaSu1CXRMcUA7",
  "type": "assistant",
  "uuid": "ea74bf20-db22-48f1-971b-54eb8ac33924",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ASghua4Q7MgsWz16ADzVt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2958,
      "cache_read_input_tokens": 38920,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2958,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 38920,
          "cache_creation_input_tokens": 2958,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2958
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

_source line 56 · 2026-05-20T04:23:13.621Z_

<details><summary>↩ Tool result · `toolu_01W8Zj64UtvFEBZVPJVtgbu8`</summary>

```text
Web search results for query: "site:openreview.net Occhipinti "probing and steering" unfaithfulness chain-of-thought 2026"

Links: [{"title":"PROBING AND STEERING CHAIN-OF-THOUGHT UN","url":"https://openreview.net/attachment?id=LocRunEIxK&name=pdf"},{"title":"Post-Hoc Reasoning in Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering | OpenReview","url":"https://openreview.net/forum?id=UMUYpeXtJQ"},{"title":"Faithful and Unfaithful Error Recovery in Chain of Thought | OpenReview","url":"https://openreview.net/forum?id=IPZ28ZqD4I"},{"title":"Measuring Faithfulness in Chain-of-Thought Reasoning | OpenReview","url":"https://openreview.net/forum?id=ZZcvsN27u3"},{"title":"VERIFYING CHAIN-OF-THOUGHT REASONING VIA ITS ...","url":"https://openreview.net/pdf/4b72bddac9695c95d680fc17b59f2c250c29cd63.pdf"},{"title":"Chain-of-Thought Reasoning In The Wild Is Not Always Faithful | OpenReview","url":"https://openreview.net/forum?id=emjPKK11Oo"},{"title":"Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting | OpenReview","url":"https://openreview.net/forum?id=bzs4uPLXvi"},{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/pdf/2603.01437"},{"title":"Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?","url":"https://arxiv.org/pdf/2508.19827"}]

Based on the search results, I found the paper you're looking for. The work is titled "Probing and Steering Chain-of-Thought Unfaithfulness in Language Models" by Giovanni Maria Occhipinti, Alessandro Abate, and Nandi Schoots, presented at the ICLR 2026 Test-Time Updates (TTU) Workshop.

The paper addresses how Chain-of-Thought (CoT) explanations are essential for monitoring and safety of Large Language Models (LLMs), yet they are susceptible to unfaithful rationalization that could obfuscate dangerous behaviors. The authors employ representation engineering to investigate the latent geometry of faithfulness in thinking language models, demonstrating that instances of faithfulness are, to some extent, encoded as linear directions in middle-to-late layers, as shown by successful probing and steering.

The paper can be found on OpenReview at the URL provided in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea74bf20-db22-48f1-971b-54eb8ac33924",
  "isSidechain": false,
  "promptId": "336e0584-08d7-4685-ad69-52c0743f6fcf",
  "type": "user",
  "uuid": "6fed3193-cac7-4db9-bae8-3909c2cbbcec",
  "toolUseResult": {
    "query": "site:openreview.net Occhipinti \"probing and steering\" unfaithfulness chain-of-thought 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012wruJTUe9sRNbweepB2D7J",
        "content": [
          {
            "title": "PROBING AND STEERING CHAIN-OF-THOUGHT UN",
            "url": "https://openreview.net/attachment?id=LocRunEIxK&name=pdf"
          },
          {
            "title": "Post-Hoc Reasoning in Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering | OpenReview",
            "url": "https://openreview.net/forum?id=UMUYpeXtJQ"
          },
          {
            "title": "Faithful and Unfaithful Error Recovery in Chain of Thought | OpenReview",
            "url": "https://openreview.net/forum?id=IPZ28ZqD4I"
          },
          {
            "title": "Measuring Faithfulness in Chain-of-Thought Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=ZZcvsN27u3"
          },
          {
            "title": "VERIFYING CHAIN-OF-THOUGHT REASONING VIA ITS ...",
            "url": "https://openreview.net/pdf/4b72bddac9695c95d680fc17b59f2c250c29cd63.pdf"
          },
          {
            "title": "Chain-of-Thought Reasoning In The Wild Is Not Always Faithful | OpenReview",
            "url": "https://openreview.net/forum?id=emjPKK11Oo"
          },
          {
            "title": "Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting | OpenReview",
            "url": "https://openreview.net/forum?id=bzs4uPLXvi"
          },
          {
            "title": "Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering",
            "url": "https://arxiv.org/pdf/2603.01437"
          },
          {
            "title": "Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?",
            "url": "https://arxiv.org/pdf/2508.19827"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. The work is titled \"Probing and Steering Chain-of-Thought Unfaithfulness in Language Models\" by Giovanni Maria Occhipinti, Alessandro Abate, and Nandi Schoots, presented at the ICLR 2026 Test-Time Updates (TTU) Workshop.\n\nThe paper addresses how Chain-of-Thought (CoT) explanations are essential for monitoring and safety of Large Language Models (LLMs), yet they are susceptible to unfaithful rationalization that could obfuscate dangerous behaviors. The authors employ representation engineering to investigate the latent geometry of faithfulness in thinking language models, demonstrating that instances of faithfulness are, to some extent, encoded as linear directions in middle-to-late layers, as shown by successful probing and steering.\n\nThe paper can be found on OpenReview at the URL provided in the search results."
    ],
    "durationSeconds": 5.461526457,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ea74bf20-db22-48f1-971b-54eb8ac33924",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-20T04:23:17.286Z_

<details><summary>Logged reasoning block</summary>

```text
Let me try to access the Occhipinti paper to understand its methodology more precisely - this is a potentially close competitor.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fed3193-cac7-4db9-bae8-3909c2cbbcec",
  "isSidechain": false,
  "requestId": "req_011CbDBZf2aSQx17dC52aNTm",
  "type": "assistant",
  "uuid": "aa2431a0-8cca-4059-a865-f00bd67dccbe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011kaw2MRAKWpFxKwymAh115",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 828,
      "cache_read_input_tokens": 41878,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 828,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 41878,
          "cache_creation_input_tokens": 828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 828
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

_source line 58 · 2026-05-20T04:23:17.700Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SRch6fSMVDSQCVykRbtDTj`</summary>

```json
{
  "query": "Occhipinti ICLR 2026 representation engineering faithfulness probing steering linear direction middle late layers methodology results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa2431a0-8cca-4059-a865-f00bd67dccbe",
  "isSidechain": false,
  "requestId": "req_011CbDBZf2aSQx17dC52aNTm",
  "type": "assistant",
  "uuid": "ef601f46-9b21-40b7-bdb4-7901562449b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011kaw2MRAKWpFxKwymAh115",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 828,
      "cache_read_input_tokens": 41878,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 828,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 41878,
          "cache_creation_input_tokens": 828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 828
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

_source line 59 · 2026-05-20T04:23:35.217Z_

<details><summary>↩ Tool result · `toolu_01SRch6fSMVDSQCVykRbtDTj`</summary>

```text
Web search results for query: "Occhipinti ICLR 2026 representation engineering faithfulness probing steering linear direction middle late layers methodology results"

Links: [{"title":"Vector researchers advance representation learning and deep learning research at ICLR 2026 - Vector Institute for Artificial Intelligence","url":"https://vectorinstitute.ai/vector-researchers-advance-representation-learning-and-deep-learning-research-at-iclr-2026/"},{"title":"USC at ICLR 2026 - USC Viterbi | School of Engineering","url":"https://viterbischool.usc.edu/news/2026/04/usc-at-iclr-2026/"},{"title":"ICLR 2026 Orals","url":"https://iclr.cc/virtual/2026/events/oral"},{"title":"IAI Researchers Have 23 Papers Accepted in ICLR 2026 - Institute of Artificial Intelligence","url":"https://ai.ucf.edu/iai-researchers-have-23-papers-accepted-in-iclr-2026/"},{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"ICLR 2026 - International Conference on Learning Representations (ICLR) - NAVER LABS Europe","url":"https://europe.naverlabs.com/updates/iclr/"},{"title":"Representation Fidelity:Auditing Algorithmic Decisions About Humans Using Self-Descriptions","url":"https://arxiv.org/pdf/2603.05136"},{"title":"2026 Conference","url":"https://iclr.cc/Conferences/2026"}]

Let me search more specifically for Occhipinti:

Links: [{"title":"An Introduction to Representation Engineering","url":"https://www.alignmentforum.org/posts/3ghj8EuKzwD3MQR5G/an-introduction-to-representation-engineering-an-activation"},{"title":"Representation Engineering (RepE)","url":"https://www.emergentmind.com/topics/representation-engineering-repe"},{"title":"GitHub - chrisliu298/awesome-representation-engineering: A resource repository for representation engineering in large language models · GitHub","url":"https://github.com/chrisliu298/awesome-representation-engineering"},{"title":"Representation Engineering in AI Systems","url":"https://www.emergentmind.com/topics/representation-engineering"},{"title":"arXiv:2502.19649v3 [cs.LG] 12 Mar 2025 - Jan Wehner","url":"https://janwehner.com/files/representation_engineering.pdf"},{"title":"Representation Engineering for Large-Language Models: Survey and Research Challenges","url":"https://arxiv.org/html/2502.17601v1"},{"title":"STEERING LANGUAGE MODELS WITH ACTIVATION EN- GINEERING Alexander Matt Turner","url":"https://arxiv.org/pdf/2308.10248"},{"title":"Improved Representation Steering for Language Models | OpenReview","url":"https://openreview.net/forum?id=VHb883Gs1u"},{"title":"GitHub - yuzhaouoe/SAE-based-representation-engineering: [NAACL'25 Oral] Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://github.com/yuzhaouoe/SAE-based-representation-engineering"}]

Let me search more specifically for Occhipinti and ICLR 2026:

Links: [{"title":"Published as a LIT workshop paper at ICLR 2026","url":"https://openreview.net/pdf?id=wVj7dB7waI"},{"title":"Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING","url":"https://openreview.net/attachment?id=lN3yKqqzF1&name=pdf"},{"title":"LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.","url":"https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"},{"title":"APPEL – MANIFESTATIONS SCIENTIFIQUES 2026 FEDERATION DE RECHERCHE AGORANTIC","url":"https://agorantic.univ-avignon.fr/wp-content/uploads/sites/6/2026/04/IDOS_ARTS_3_AnimFR_2026.pdf"},{"title":"Is VLA Reasoning Faithful? Probing Safety of Chain-of-Causation in Autonomous Driving ModelsAccepted at the DriveX Workshop, CVPR 2026.","url":"https://arxiv.org/html/2605.17268"},{"title":"RAG System Metrics: Recall, Precision, Faithfulness 2026","url":"https://www.digitalapplied.com/blog/rag-system-metrics-recall-precision-faithfulness-2026"}]

Let me try a different search focusing on the paper title and ICLR:

Links: [{"title":"Learning representations of learning representations","url":"https://arxiv.org/pdf/2404.08403"},{"title":"Learning representations of learning representations","url":"https://arxiv.org/html/2404.08403v1"},{"title":"ICLR Neural Networks Learn Representation Theory: Reverse Engineering how Networks Perform Group Operations","url":"https://iclr.cc/virtual/2023/14593"},{"title":"2021 Conference","url":"https://iclr.cc/Conferences/2021"},{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"ICLR | LinkedIn","url":"https://www.linkedin.com/company/iclr"},{"title":"Recovery of a hierarchical functional representation of an integrated circuit","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11651126"}]

Let me try one more search with a different approach:

Links: [{"title":"Steering Safely or Off a Cliff? Rethinking Specificity and Robustness in Inference-Time Interventions","url":"https://arxiv.org/html/2602.06256"},{"title":"[2512.17639] Linear Personality Probing and Steering in LLMs: A Big Five Study","url":"https://arxiv.org/abs/2512.17639"},{"title":"[2603.25052] Closing the Confidence-Faithfulness Gap in Large Language Models","url":"https://arxiv.org/abs/2603.25052"},{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/pdf/2603.01437"},{"title":"The Geometry of Harmfulness in LLMs through Subconcept Probing","url":"https://arxiv.org/pdf/2507.21141"},{"title":"[2602.17881] Understanding Unreliability of Steering Vectors in Language Models: Geometric Predictors and the Limits of Linear Approximations","url":"https://arxiv.org/abs/2602.17881"},{"title":"Probing and Steering Evaluation Awareness of Language Models","url":"https://arxiv.org/html/2507.01786v2"},{"title":"Towards Tracing Trustworthiness Dynamics: Revisiting Pre-training Period   of Large Language Models","url":"https://arxiv.org/pdf/2402.19465"},{"title":"Transferring Features Across Language Models With Model Stitching","url":"https://arxiv.org/html/2506.06609v1"}]

I apologize, but I was unable to find specific information about an "Occhipinti ICLR 2026" paper on representation engineering with the specific topics you mentioned (faithfulness probing, steering, linear direction, middle late layers, methodology, and results). 

The search results returned general information about representation engineering in LLMs, probing and steering techniques, and ICLR 2026 papers on related topics, but I could not locate the specific Occhipinti paper you're asking about. This could be because:

1. The paper may not yet be widely indexed on public platforms
2. The author name or title might be slightly different
3. It may be a very recent submission that hasn't been widely disseminated

To find this specific paper, I'd recommend:
- Checking the official ICLR 2026 proceedings or OpenReview platform directly
- Searching for the author on arXiv or the ICLR website
- Looking for the specific paper title if you have it
- Checking the author's institutional website or Google Scholar profile

If you have more details about the paper (such as the full title, author affiliations, or a specific link), I'd be happy to help you locate and summarize the information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef601f46-9b21-40b7-bdb4-7901562449b7",
  "isSidechain": false,
  "promptId": "336e0584-08d7-4685-ad69-52c0743f6fcf",
  "type": "user",
  "uuid": "ebb5d020-d30d-4ae6-9930-ef65be868f59",
  "toolUseResult": {
    "query": "Occhipinti ICLR 2026 representation engineering faithfulness probing steering linear direction middle late layers methodology results",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NohGrynX4HkUAX9Z7oMueH",
        "content": [
          {
            "title": "Vector researchers advance representation learning and deep learning research at ICLR 2026 - Vector Institute for Artificial Intelligence",
            "url": "https://vectorinstitute.ai/vector-researchers-advance-representation-learning-and-deep-learning-research-at-iclr-2026/"
          },
          {
            "title": "USC at ICLR 2026 - USC Viterbi | School of Engineering",
            "url": "https://viterbischool.usc.edu/news/2026/04/usc-at-iclr-2026/"
          },
          {
            "title": "ICLR 2026 Orals",
            "url": "https://iclr.cc/virtual/2026/events/oral"
          },
          {
            "title": "IAI Researchers Have 23 Papers Accepted in ICLR 2026 - Institute of Artificial Intelligence",
            "url": "https://ai.ucf.edu/iai-researchers-have-23-papers-accepted-in-iclr-2026/"
          },
          {
            "title": "ICLR 2026",
            "url": "https://iclr.cc/"
          },
          {
            "title": "ICLR 2026 - International Conference on Learning Representations (ICLR) - NAVER LABS Europe",
            "url": "https://europe.naverlabs.com/updates/iclr/"
          },
          {
            "title": "Representation Fidelity:Auditing Algorithmic Decisions About Humans Using Self-Descriptions",
            "url": "https://arxiv.org/pdf/2603.05136"
          },
          {
            "title": "2026 Conference",
            "url": "https://iclr.cc/Conferences/2026"
          }
        ]
      },
      "Let me search more specifically for Occhipinti:",
      {
        "tool_use_id": "srvtoolu_014kb266pXjoMgB6oiVAdbst",
        "content": [
          {
            "title": "An Introduction to Representation Engineering",
            "url": "https://www.alignmentforum.org/posts/3ghj8EuKzwD3MQR5G/an-introduction-to-representation-engineering-an-activation"
          },
          {
            "title": "Representation Engineering (RepE)",
            "url": "https://www.emergentmind.com/topics/representation-engineering-repe"
          },
          {
            "title": "GitHub - chrisliu298/awesome-representation-engineering: A resource repository for representation engineering in large language models · GitHub",
            "url": "https://github.com/chrisliu298/awesome-representation-engineering"
          },
          {
            "title": "Representation Engineering in AI Systems",
            "url": "https://www.emergentmind.com/topics/representation-engineering"
          },
          {
            "title": "arXiv:2502.19649v3 [cs.LG] 12 Mar 2025 - Jan Wehner",
            "url": "https://janwehner.com/files/representation_engineering.pdf"
          },
          {
            "title": "Representation Engineering for Large-Language Models: Survey and Research Challenges",
            "url": "https://arxiv.org/html/2502.17601v1"
          },
          {
            "title": "STEERING LANGUAGE MODELS WITH ACTIVATION EN- GINEERING Alexander Matt Turner",
            "url": "https://arxiv.org/pdf/2308.10248"
          },
          {
            "title": "Improved Representation Steering for Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=VHb883Gs1u"
          },
          {
            "title": "GitHub - yuzhaouoe/SAE-based-representation-engineering: [NAACL'25 Oral] Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering",
            "url": "https://github.com/yuzhaouoe/SAE-based-representation-engineering"
          }
        ]
      },
      "Let me search more specifically for Occhipinti and ICLR 2026:",
      {
        "tool_use_id": "srvtoolu_01AtpXSZYMK6L8Utqho1myvi",
        "content": [
          {
            "title": "Published as a LIT workshop paper at ICLR 2026",
            "url": "https://openreview.net/pdf?id=wVj7dB7waI"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING",
            "url": "https://openreview.net/attachment?id=lN3yKqqzF1&name=pdf"
          },
          {
            "title": "LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most Persistent Quirk | Lakera – Protecting AI teams that disrupt the world.",
            "url": "https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models"
          },
          {
            "title": "APPEL – MANIFESTATIONS SCIENTIFIQUES 2026 FEDERATION DE RECHERCHE AGORANTIC",
            "url": "https://agorantic.univ-avignon.fr/wp-content/uploads/sites/6/2026/04/IDOS_ARTS_3_AnimFR_2026.pdf"
          },
          {
            "title": "Is VLA Reasoning Faithful? Probing Safety of Chain-of-Causation in Autonomous Driving ModelsAccepted at the DriveX Workshop, CVPR 2026.",
            "url": "https://arxiv.org/html/2605.17268"
          },
          {
            "title": "RAG System Metrics: Recall, Precision, Faithfulness 2026",
            "url": "https://www.digitalapplied.com/blog/rag-system-metrics-recall-precision-faithfulness-2026"
          }
        ]
      },
      "Let me try a different search focusing on the paper title and ICLR:",
      {
        "tool_use_id": "srvtoolu_011Jdi4wvECPyQ6qWH2uZPZb",
        "content": [
          {
            "title": "Learning representations of learning representations",
            "url": "https://arxiv.org/pdf/2404.08403"
          },
          {
            "title": "Learning representations of learning representations",
            "url": "https://arxiv.org/html/2404.08403v1"
          },
          {
            "title": "ICLR Neural Networks Learn Representation Theory: Reverse Engineering how Networks Perform Group Operations",
            "url": "https://iclr.cc/virtual/2023/14593"
          },
          {
            "title": "2021 Conference",
            "url": "https://iclr.cc/Conferences/2021"
          },
          {
            "title": "ICLR 2026",
            "url": "https://iclr.cc/"
          },
          {
            "title": "ICLR | LinkedIn",
            "url": "https://www.linkedin.com/company/iclr"
          },
          {
            "title": "Recovery of a hierarchical functional representation of an integrated circuit",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11651126"
          }
        ]
      },
      "Let me try one more search with a different approach:",
      {
        "tool_use_id": "srvtoolu_01DiG94k4ro4CUaLyxLSZoto",
        "content": [
          {
            "title": "Steering Safely or Off a Cliff? Rethinking Specificity and Robustness in Inference-Time Interventions",
            "url": "https://arxiv.org/html/2602.06256"
          },
          {
            "title": "[2512.17639] Linear Personality Probing and Steering in LLMs: A Big Five Study",
            "url": "https://arxiv.org/abs/2512.17639"
          },
          {
            "title": "[2603.25052] Closing the Confidence-Faithfulness Gap in Large Language Models",
            "url": "https://arxiv.org/abs/2603.25052"
          },
          {
            "title": "Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering",
            "url": "https://arxiv.org/pdf/2603.01437"
          },
          {
            "title": "The Geometry of Harmfulness in LLMs through Subconcept Probing",
            "url": "https://arxiv.org/pdf/2507.21141"
          },
          {
            "title": "[2602.17881] Understanding Unreliability of Steering Vectors in Language Models: Geometric Predictors and the Limits of Linear Approximations",
            "url": "https://arxiv.org/abs/2602.17881"
          },
          {
            "title": "Probing and Steering Evaluation Awareness of Language Models",
            "url": "https://arxiv.org/html/2507.01786v2"
          },
          {
            "title": "Towards Tracing Trustworthiness Dynamics: Revisiting Pre-training Period   of Large Language Models",
            "url": "https://arxiv.org/pdf/2402.19465"
          },
          {
            "title": "Transferring Features Across Language Models With Model Stitching",
            "url": "https://arxiv.org/html/2506.06609v1"
          }
        ]
      },
      "I apologize, but I was unable to find specific information about an \"Occhipinti ICLR 2026\" paper on representation engineering with the specific topics you mentioned (faithfulness probing, steering, linear direction, middle late layers, methodology, and results). \n\nThe search results returned general information about representation engineering in LLMs, probing and steering techniques, and ICLR 2026 papers on related topics, but I could not locate the specific Occhipinti paper you're asking about. This could be because:\n\n1. The paper may not yet be widely indexed on public platforms\n2. The author name or title might be slightly different\n3. It may be a very recent submission that hasn't been widely disseminated\n\nTo find this specific paper, I'd recommend:\n- Checking the official ICLR 2026 proceedings or OpenReview platform directly\n- Searching for the author on arXiv or the ICLR website\n- Looking for the specific paper title if you have it\n- Checking the author's institutional website or Google Scholar profile\n\nIf you have more details about the paper (such as the full title, author affiliations, or a specific link), I'd be happy to help you locate and summarize the information."
    ],
    "durationSeconds": 17.514087266999994,
    "searchCount": 5
  },
  "sourceToolAssistantUUID": "ef601f46-9b21-40b7-bdb4-7901562449b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 60 · 2026-05-20T04:23:35.221Z_

```json
{
  "parentUuid": "ebb5d020-d30d-4ae6-9930-ef65be868f59",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "64101319-d6f5-43e5-ab88-b73e7b3b14b4",
  "timestamp": "2026-05-20T04:23:35.221Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 61 · 2026-05-20T04:24:46.796Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now synthesize all my findings and produce the analysis. I have enough information from my research.

Let me summarize what I've found:

1. **Novelty is real but has a specific vulnerability**: The dual-stream framework combining probe trajectories (P*) with causal contribution (C) is indeed novel. No existing work does this. The closest competitors are:
   - Kudo et al. (EACL 2026): probes + activation patching on synthetic arithmetic
   - CMI: structural mediation, not functional contribution
   - Occhipinti et al.: representation engineering for faithfulness probing + steering, but appears to be a workshop paper with limited scope
   - Chrabąszcz et al.: probe trajectories only, no causal component

2. **The "trivial alternative" question is partially answered**: The proposal addresses "why not endpoint comparison" and "why not pair Chrabąszcz + TTS" but there's a deeper trivial alternative concern: could Chrabąszcz's 60+ signal-processing features on probe trajectories alone already capture faithfulness patterns without needing an explicit causal measurement? If probe trajectory shapes already distinguish faithful from unfaithful reasoning (because the hidden state dynamics differ), then the causal dimension might be unnecessary.

3. **Assumption concern**: P*(t) measures "correctness-correlated information availability" but the interpretation as "knowledge" is a leap that needs more justification.

4. **Significance can be elevated**: The proposal frames significance in terms of diagnosis and efficiency, but could be elevated to frame ICG as establishing a fundamental measurement paradigm for reasoning interpretability.

5. **The training implications are missing**: If ICG can distinguish decorative from load-bearing CoT, this has direct implications for RL training of reasoning models (e.g., training signal design, curriculum).

The proposal is extremely detailed and addresses many potential objections proactively. I'm seeing 2-3 genuine points where the idea's ceiling can be raised: the strongest trivial alternative is whether Chrabąszcz's probe-trajectory features alone could already detect faithfulness without causal measurement, and the significance could be elevated from diagnosis and efficiency to establishing a fundamental measurement paradigm for reasoning interpretability.

The proposal actually does plan to test the probe-trajectory-only baseline empirically in Phase 3, but the conceptual argument for why the causal dimension is necessary could be stronger. The current reasoning is that probe trajectories can't distinguish faithful-correct from unfaithful-correct because they don't measure causal contribution, but Chrabąszcz's features might implicitly capture this through dynamics that correlate with causal contribution. The proposal needs a more rigorous argument for why the causal dimension adds irreducible information beyond what trajectory dynamics alone could provide.

The proposal does claim that Chrabąszcz et al. are "structurally blind" to the faithful-correct vs. unfaithful-correct distinction, but this needs to be sharpened into an actual argument. The key insight is that a probe showing early high activation that persists could mean either the model pre-encoded the answer without using chain-of-thought, or it pre-encoded the answer but uses chain-of-thought to verify and refine—and only the causal dimension can distinguish between these two scenarios. This observational equivalence result is already somewhat present in the proposal but needs to be made much more explicit and rigorous.

Now I'm ready to structure my feedback. I'll identify three key areas where the proposal could be strengthened: sharpening the theoretical argument for why the causal dimension is irreducible, elevating the framing from a diagnostic tool to a measurement paradigm with training implications, and grounding this more firmly in information-theoretic frameworks.

Actually, let me reconsider whether these are genuine improvements or just minor refinements. Re-reading the proposal, I notice it already pre-empts most objections and has strong significance framing with practical applications. But there are real contributions here: the observational equivalence argument would formalize why Chrabąszcz alone is insufficient, the training implications could show how this diagnostic tool actually shapes how we design reward signals during reinforcement learning, and there's an interesting temporal asymmetry in how P*(t) evolves that deserves deeper exploration.

The proposal does touch on information bypass through the latent-mediated versus CoT-mediated distinction, so that's largely covered. What I should focus on is sharpening the core argument: why probe trajectories alone can't answer the question about whether CoT is genuinely reasoning or just decorating the output.

The real issue is observational equivalence — P*(t) curves alone can't distinguish between a model that pre-encodes the answer and doesn't use CoT versus one that pre-encodes it but uses CoT to refine or validate. Similarly, C(t) alone can't tell whether CoT is doing the actual work or just elaborating on something the model already knew. Only measuring both simultaneously breaks this degeneracy and reveals which pathway is actually load-bearing.

But there's something deeper here: even when both metrics are high, the dual-stream approach distinguishes between a model that knows the answer upfront and uses CoT for formalization versus one where CoT is genuinely doing computational work. The causal dimension provides irreducible information about CoT's actual role that neither metric can capture alone — this is the strongest theoretical justification for the framework.

Beyond diagnosis, I'm realizing ICG has implications for training too, not just inference-time decisions.

During reinforcement learning of reasoning models, measuring the causal signal could identify where models generate decorative reasoning versus genuine problem-solving, then use that to target training toward making CoT more faithful and pinpoint the difficulty threshold where models transition from decoration to actual reasoning. This could guide curriculum design by focusing on problems near that boundary.

And the domain-specificity finding — that the decorative-to-load-bearing transition varies across domains — shouldn't be treated as a limitation requiring domain-specific reporting, but as a feature revealing how the transition happens differently depending on the problem structure.

Now I'm checking whether simpler alternatives could work instead. The proposal already handles the endpoint comparison approach by showing it collapses distinct failure mechanisms. For using just Chrabąszcz's features with binary labels, the proposal has a probe-only baseline, but my observational equivalence argument fills in why that fundamentally can't work. And I should assess whether FaithCoT-Bench methods alone could suffice.

FaithCoT-Bench relies on text-level perturbations while ICG operates on internal representations, and the proposal addresses this by including FaithCoT-Bench as an external validation benchmark. The trickier case is whether I could just extend Kudo et al.'s approach from synthetic to natural benchmarks—they combine probes with activation patching on arithmetic tasks and show faithful computation. The key distinction is that ICG uses behavioral interventions like truncation and paraphrase rather than representational intervention through activation patching, which matters because Yuan et al. demonstrate that representational intervention fails on reasoning models. So behavioral C(t) becomes the necessary approach here.

The real insight is that this choice isn't arbitrary—it's forced by the diagnostic-causal gap itself. Since representational interventions don't work, causal contribution has to be measured behaviorally through perturbation, while the diagnostic signal comes from probes on hidden states. This creates a natural framework where I'm measuring P*(t) from representations and C(t) from behavior, each capturing what it can actually measure.

I'm identifying three key discovery points that strengthen the argument: the observational equivalence case for the causal dimension, the training implications for RL reasoning models, and one more I'm still crystallizing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64101319-d6f5-43e5-ab88-b73e7b3b14b4",
  "isSidechain": false,
  "requestId": "req_011CbDBbEy32tPLghDKL9TLf",
  "type": "assistant",
  "uuid": "03a635b6-ccfb-4efa-afbf-a981d463aa12",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JG48ue16A2pa585SNFiryD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2413,
      "cache_read_input_tokens": 42706,
      "output_tokens": 6822,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2413,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6822,
          "cache_read_input_tokens": 42706,
          "cache_creation_input_tokens": 2413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2413
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

_source line 62 · 2026-05-20T04:26:15.878Z_

Now I have a comprehensive picture of the research landscape. Let me formulate my assessment.

---

【状态】: 有发掘空间

【前置调研发现】
- [Chrabąszcz et al., arXiv 2605.18549] (2026): Probe trajectories with 60+ signal-processing features achieving 91-97% AUROC on harmfulness. Purely diagnostic — no causal component, no faithfulness taxonomy. The most direct "probe-only" competitor; proposal's head-to-head baseline.
- [Yuan et al., arXiv 2605.09502] (2026): Four intervention strategies (steering, probe-guided BoN, self-correction, patching) ALL fail on reasoning models despite 0.95 AUROC probes. Establishes "diagnostic not causal" as a robust finding across 3 families, 1.5B-72B. This is the empirical bedrock for the proposal.
- [Cox et al., arXiv 2603.01437] (2026): Pre-CoT probes achieve 0.9 AUC on instruction-tuned models with >50% flip rate via steering, but negligible on reasoning models. Independent confirmation of Yuan et al.'s gap, with the critical detail that *representational* intervention fails specifically on reasoning-trained models.
- [Ballon et al., arXiv 2601.23163] (2026): Truncation-reinjection protocol measuring behavioral accuracy curves from partial CoT prefixes. Demonstrates monotonic accuracy increase with semantic content (not length). Key: purely behavioral, no hidden-state measurement.
- [Wang, arXiv 2604.15726] (2026): Formalizes H1 (latent-mediated) / H2 (CoT-mediated) / H0 (generic compute) hypotheses. Theoretical framing paper; calls for empirical operationalization but provides none.
- [Kudo et al., EACL 2026, arXiv 2412.01113]: Per-position probes + activation patching on synthetic arithmetic (9 models). The closest existing "dual-stream" precursor, but: synthetic data only, no temporal gap metric, no faithfulness taxonomy, no trajectory-shape analysis. Critical detail: uses *representational* intervention (activation patching) for causality.
- [CMI, Sathyanarayanan et al., arXiv 2602.03994]: Layerwise activation patching on ~50 examples measuring structural mediation (does representation route through CoT-processing layers?). Complementary to ICG's functional question but fundamentally different measurement target.
- [Occhipinti et al., ICLR 2026 LIT Workshop]: Representation engineering for faithfulness probing + steering. Workshop paper; uses linear probing of "faithfulness direction" in middle-to-late layers. Appears to be a steering paper, not a temporal diagnostic framework. Limited public detail on methodology.
- [Thought Anchors, arXiv 2506.19143]: Per-sentence counterfactual importance via 100-rollout replacement. Provides within-CoT causal structure (which sentences matter) but no external probe reference.
- [Gjølbye et al., arXiv 2605.15454] (2026): Hidden-state trajectory geometry across domains; difficulty-geometry coupling is domain-specific (ρ⊥ = +0.41 code, +0.05 math). Critical for difficulty conditioning design.
- 调研总结: The field has independently built high-quality components on both sides — probe trajectories (Chrabąszcz, David, Yuan, Esakkiraja, Zhang) and behavioral causal curves (Ballon, TTS, NLDD, Thought Anchors) — but **no one has formally unified them into a temporal gap metric**. The theoretical need is articulated (Wang's H1/H2) but not operationalized. Meanwhile, the representational-intervention-fails finding (Yuan, Cox) is robustly established, creating a natural asymmetry: diagnostic signal lives in hidden states, but causal signal can only be measured behaviorally. This asymmetry is the framework's deepest justification, and it's currently underexploited in the proposal.

---

【发掘点 1】
- 维度: 核心 claim 强化
- 内容: **将"representational intervention fails on reasoning models"从背景提升为核心理论动机。** 当前 proposal 将 Yuan/Cox 的 intervention failure 作为 motivating observation（"this gap IS the central phenomenon"），但没有将其逻辑推到底：representational intervention 在 reasoning models 上失效意味着 causal contribution 不可能通过 activation patching/steering 测量；因此 C(t) 必须从 behavioral intervention（truncation, perturbation, NLDD）获得。而 P*(t) 必须来自 hidden states（因为这是唯一能探测 correctness awareness 的途径）。这就产生了一个**由 diagnostic-causal gap 本身决定的 architectural necessity**：hidden states for diagnostics, behavior for causality。这不是设计选择，而是由现有 empirical evidence 强制决定的。当前 proposal 将 behavioral C(t) 呈现为方法选择之一；如果将其重新定位为 "the only viable option given intervention failure"，核心 claim 从 "we propose a useful combination" 变成 "the empirical landscape forces this specific framework architecture"。这是一个更难被审稿人 dismiss 的 claim。
- 价值: 命中 **Novelty** 和 **Significance**。将 framework 从 "novel combination" 提升到 "empirically-necessitated architecture"，后者是更高级别的 novelty claim。审稿人对 "we combine A and B" 的常见反应是 "obvious combination"；对 "A fails representationally, B fails diagnostically, the gap forces this specific asymmetric design" 的反应则完全不同。
- 调研依据: 直接基于 Yuan et al. (2605.09502) 的四种 intervention failure + Cox et al. (2603.01437) 的 reasoning-specific steering failure。两组独立工作共同确立了 representational intervention 在 reasoning models 上的系统性失败，这是 behavioral C(t) 的 necessity argument 的经验基础。

【发掘点 2】
- 维度: novelty 锐化
- 内容: **补充 observational equivalence argument，理论证明 probe-only approaches 的 fundamental identifiability limitation。** 当前 proposal 说 Chrabąszcz "structurally blind to faithful-correct vs. unfaithful-correct distinction"，但这是一个未加证明的 assertion。应该将其提升为一个 explicit theoretical argument：存在两种明确定义的 scenario 会产生 identical P*(t) trajectories 但完全不同的 faithfulness 状态——(A) 模型 pre-encode 答案，CoT 纯装饰（unfaithful-correct）；(B) 模型 pre-encode 答案，CoT 用于验证/细化（faithful-correct）。两种情况下 P*(t) 都是 early-high + flat（因为模型同样拥有 correctness-correlated information），但 C(t) 分离它们（A 的 C(t) ≈ 0，B 的 C(t) > 0）。这构成一个 formal identifiability result：P*(t) alone is insufficient to identify the causal role of CoT。反方向同理：C(t) high + 模型 pre-know vs. C(t) high + 模型不 pre-know 在 C(t) alone 下不可区分。只有 dual-stream 打破 degeneracy。这比目前的 "structurally blind" 论述强得多。
- 价值: 命中 **Novelty** 和 **Related Work 差异化**。当 proposal 包含一个 explicit identifiability argument 时，probe-only baseline（Chrabąszcz-style features）从 "empirically inferior" 变成 "theoretically insufficient"——后者是审稿人更难反驳的定位。同时也预防了 "your C(t) dimension might be redundant" 的审稿意见。
- 调研依据: 基于 Chrabąszcz et al. (2605.18549) 的方法论分析——其 60+ features 全部基于 probe trajectory 的 signal processing，原理上无法区分 "high P*(t) because model knows AND uses CoT" 和 "high P*(t) because model knows but doesn't use CoT"。

【发掘点 3】
- 维度: significance 提升
- 内容: **增加 "RL training signal design" 作为 ICG 的第四个 practical significance domain。** 当前 proposal 列出三个 practical applications（inference-time compute allocation, benchmark validity, safety monitoring），全部是 inference-time/evaluation-time 应用。但 ICG 的 highest-impact downstream application 可能是 training-time：如果 G*(t) 可以在 RL fine-tuning 期间实时计算（或离线估算），则可以：(1) 为 decorative CoT（G*(t) >> 0）降低 reward signal 权重——当前 RL training 无法区分"模型因为 CoT 正确推理而答对"和"模型本来就知道答案，CoT 纯粹浪费 token"，导致对 decorative CoT 的 reward 强化了不忠实推理；(2) 识别 training curriculum 中的"临界难度"：G*(t) 从持续 >> 0 过渡到逐渐 converge 的 difficulty threshold 是模型真正需要 CoT 的起点，curriculum 应重点采样此区间。这将 ICG 从 "measurement paper" 提升为对 reasoning model training 有直接指导意义的工作，显著提升 significance ceiling。
- 价值: 命中 **Significance**。当前 framing 将 ICG 定位为分析工具；增加 training implications 将其定位为 potentially shaping how future reasoning models are trained——这是一个影响力量级的提升。注意：这里不是建议增加训练实验（那是补救 agent 的事），而是建议在 paper 的 significance framing 和 discussion section 中明确 articulate 这个 connection。
- 调研依据: 基于 Li et al. (2510.22362) 的 easy→decorative, hard→faithful finding。如果 RL training 不区分这两种模式，decorative CoT 会被错误 reinforce。ICG 的 G*(t) 直接 operationalize 了这个区分。同时参考 Gjølbye et al. (2605.15454) 的 domain-specific difficulty-geometry coupling，说明 "临界难度" 是 domain-dependent 的，进一步增强了 per-domain G*(t) profiling 的 training 价值。

【发掘点 4】
- 维度: 前提假设质疑（非致命，但需收紧论述）
- 内容: **P*(t) 的 "correctness awareness" 解释需要更紧的 interpretive bounds。** 当前 proposal 在 G*(t) >> 0 时解释为 "knows but doesn't use"。proposal 已经有 interpretive caveat（"does not entail the model 'decided to withhold'"），但还不够。更精确的问题是：P*(t) 测量的是 "linear probe on hidden states predicts correctness"，但这可能反映三种完全不同的东西——(a) 模型确实"知道"答案/答案正确性；(b) hidden states 编码了与 difficulty 相关的 features，而 difficulty 与 correctness 高度相关（easy problems → high P*(t) AND high correctness，但 P*(t) 反映的是 difficulty encoding 而非 answer knowledge）；(c) 计算副产品（Chun et al. MCT geometric pulse）。当前的 null-probe calibration 解决了 baseline noise，但不能排除 (b)。建议在论述中明确承认这一 confound，并利用已有设计中的 difficulty conditioning（Phase 2）部分缓解：在 same-difficulty bin 内比较 correct vs. incorrect 的 P*(t)，排除 difficulty-mediated confound。如果 P*(t) 在 same-difficulty bin 内仍然 discriminative，则 "correctness awareness" 解释更有根据。这不需要增加实验（difficulty conditioning 已在计划中），只需在理论论述中显式 connect the dots。
- 价值: 命中 **Novelty**（claim 的 precision），间接支持 **Significance**（更 defensible 的 claim 更有影响力）。审稿人如果发现这个 confound 未被讨论，可能会直接质疑整个 framework 的 interpretive validity。显式讨论并利用 existing experimental design 缓解，将 weakness 转化为 strength。
- 调研依据: 基于 David (2511.14773) 的 easy (0.84) vs. hard (0.76) probe AUROC split——这个 split 本身可能部分由 difficulty encoding 驱动而非 answer knowledge。同时参考 Ravichander et al. (2005.00719) 的发现："properties recoverable when unused"——probe 能 decode 的信息不代表模型实际使用或 "知道" 该信息。

Sources:
- [Monitoring the Internal Monologue: Probe Trajectories](https://arxiv.org/abs/2605.18549)
- [Hidden Error Awareness in Chain-of-Thought Reasoning](https://arxiv.org/abs/2605.09502)
- [Decoding Answers Before Chain-of-Thought](https://arxiv.org/abs/2603.01437)
- [Probing the Trajectories of Reasoning Traces](https://arxiv.org/abs/2601.23163)
- [LLM Reasoning Is Latent, Not the Chain of Thought](https://arxiv.org/abs/2604.15726)
- [LLMs Faithfully and Iteratively Compute Answers During CoT](https://aclanthology.org/2026.findings-eacl.59/)
- [FaithCoT-Bench (ICLR 2026)](https://arxiv.org/abs/2510.04040)
- [Reasoning Models Don't Just Think Longer, They Move Differently](https://arxiv.org/abs/2605.15454)
- [Thought Anchors: Which LLM Reasoning Steps Matter?](https://arxiv.org/abs/2506.19143)
- [Causal Bypass / CMI](https://arxiv.org/abs/2602.03994)
- [Temporal Predictors of Outcome](https://arxiv.org/abs/2511.14773)
- [Reasoning Models Know When They're Right](https://arxiv.org/abs/2504.05419)
- [Mechanistic Evidence for Faithfulness Decay / NLDD](https://arxiv.org/abs/2602.11201)
- [ICLR 2026 LIT Workshop](https://openreview.net/group?id=ICLR.cc%2F2026%2FWorkshop%2FLIT)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03a635b6-ccfb-4efa-afbf-a981d463aa12",
  "isSidechain": false,
  "requestId": "req_011CbDBbEy32tPLghDKL9TLf",
  "type": "assistant",
  "uuid": "8c9a7559-73d5-4b66-980b-32ae79c91364",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JG48ue16A2pa585SNFiryD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2413,
      "cache_read_input_tokens": 42706,
      "output_tokens": 6822,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2413,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6822,
          "cache_read_input_tokens": 42706,
          "cache_creation_input_tokens": 2413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2413
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

_source line 63_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness  ## Description When a reasoning model gets the right answer, is i…",
  "leafUuid": "8c9a7559-73d5-4b66-980b-32ae79c91364",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0"
}
```

---

### Runtime record

_source line 64_

```json
{
  "type": "ai-title",
  "aiTitle": "Information-Contribution Gap for reasoning faithfulness",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0"
}
```

---

### Runtime record

_source line 65_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness  ## Description When a reasoning model gets the right answer, is i…",
  "leafUuid": "8c9a7559-73d5-4b66-980b-32ae79c91364",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0"
}
```

---

### Runtime record

_source line 66_

```json
{
  "type": "ai-title",
  "aiTitle": "Information-Contribution Gap for reasoning faithfulness",
  "sessionId": "a8d3cc8a-d625-4edc-ba71-1318a72e9ef0"
}
```

---
