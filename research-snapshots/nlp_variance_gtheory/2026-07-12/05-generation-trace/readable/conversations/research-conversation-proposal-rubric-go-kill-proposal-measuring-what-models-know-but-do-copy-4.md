# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Measuring What Models Know But Do

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/d2fe3289-ab28-432b-9391-57de9a76f3e4.jsonl`
- **Structured JSON:** [`52ab23dda4f9aac54fff.json`](../../sessions/52/52ab23dda4f9aac54fff.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:35:22.708Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:35:22.708Z",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness\n\n## Description\nWhen a reasoning model gets the right answer, is its chain-of-thought the reason it succeeded — or did it already know the answer and generate decorative reasoning? No existing method can answer this question. Probe-only approaches (Chrabąszcz et al., 2605.18549) reveal what the model knows over time but are structurally blind to whether CoT caused the correct output. Causal-only approaches (TTS, Zhao et al. 2510.24941; NLDD, Ye et al. 2602.11201; Ballon et al. 2601.23163) measure what CoT does but cannot assess what the model already knew internally. Only a dual-stream framework — jointly tracking information availability AND causal contribution — can distinguish faithful-correct from unfaithful-correct reasoning. The Information-Contribution Gap (ICG) framework provides this.\n\nICG exploits a robust empirical finding: linear probes on hidden states reliably diagnose answer correctness (0.82-0.95 AUROC across four independent groups) yet causal interventions based on these probes consistently fail on reasoning-trained models (Cox et al. 2603.01437: negligible flip rates; Yuan et al. 2605.09502: all four intervention strategies fail). Rather than treating this diagnostic-causal gap as an obstacle, we make it the primary object of study.\n\nThe framework tracks two calibrated time-varying quantities across the CoT trajectory: P*(t), null-probe-calibrated correctness awareness, and C(t), causal contribution estimated via three complementary methods (prefix truncation following Ballon et al.'s three control conditions, paraphrase perturbation, NLDD). Their divergence G*(t) = P*(t) − C(t) produces phenomenon-specific temporal fingerprints, operationalizing Wang's (2604.15726) H1/H2 distinction: G*(t) >> 0 is latent-mediated (H1-consistent), G*(t) ≈ 0 is CoT-mediated (H2-consistent).\n\n**Core insight: the diagnostic contribution of G*(t) is its temporal trajectory shape, not its absolute magnitude.** P*(t) (probe AUROC) and C(t) (behavioral accuracy change) are measured via fundamentally different methods with non-commensurable scales. We address this via rank-based normalization as primary scheme, but more fundamentally, trajectory-shape profiles carry the diagnostic signal: a model that pre-encodes the answer shows a constant-high shape; genuine reasoning shows convergence toward zero; post-hoc rationalization shows widening. The shapes-over-magnitudes approach is validated by: entropy trajectory monotonicity predicting reliability regardless of absolute levels (+5.8pp, arXiv 2603.18940); RQA temporal features outperforming aggregates (36.94% vs. 28.97%, arXiv 2602.06266); Microsoft trajectory geometry achieving 0.852 AUC from shape features vs. 0.649 baseline (arXiv 2604.05655).\n\n**Why not just endpoint comparison or trivial combination?** Two reviewer objections are preempted: (1) \"Why not correlate pre-CoT probe accuracy with final correctness?\" — endpoint comparison detects unfaithfulness presence but collapses distinct failure *mechanisms* (pre-CoT encoding vs. rationalization vs. late shortcutting produce identical endpoints but distinct G*(t) shapes). (2) \"Why not just pair Chrabąszcz's probe trajectories with TTS step scores?\" — TTS measures *marginal* contribution (removing step *s* changes the answer), while prefix-truncation C(t) measures *cumulative sufficiency* (CoT[:t] is sufficient for correctness). A chain where every individual step has low TTS (each individually replaceable) could still have high cumulative C(t) (the ensemble is necessary). This cumulative-vs-marginal distinction is theoretically non-reducible and empirically grounded in the difference between Ballon et al.'s monotonic prefix curves and TTS's per-step ATE.\n\n**Structural vs. functional differentiation from CMI.** The CMI framework (Sathyanarayanan et al., 2602.03994) measures whether answer representations pass through CoT-aligned layers via layerwise activation patching — a *structural* question. ICG answers a *functional* question: does the CoT text causally contribute to behavioral correctness? This generates a testable prediction: models could show high CMI (representations routed through CoT-processing layers) but high G*(t) (CoT serves as timing scaffold rather than contributing semantic content). If confirmed, this would reveal a novel structural-functional dissociation in reasoning models.\n\n**Differentiation from Thought Anchors.** Thought Anchors (arXiv 2506.19143) measures per-sentence counterfactual importance via replacement sampling — identifying sentences with outsized causal influence on reasoning trajectory. This provides *within-CoT structural analysis* (which sentences matter to each other) but no *external reference* to the model's internal state. A thought anchor could be causally critical within the CoT but entirely redundant relative to what the model already knows — a distinction only ICG can make via the probe dimension.\n\n**Interpretive boundary.** G*(t) >> 0 means correctness-correlated information is present but not causally channeled through CoT. It does not entail the model \"decided to withhold\" — the information may exist as computational byproducts rather than semantically actionable knowledge. Chun et al.'s MCT geometric pulse finding (2602.20338) provides evidence of this possibility. We report interpretations with this caveat.\n\n**Practical significance: reasoning utilization efficiency.** G*(t) provides a unified diagnostic for reasoning utilization: G*(t) ≈ 0 means full utilization (knowledge channeled through CoT); G*(t) >> 0 means waste (CoT is decorative overhead); G*(t) < 0 means productive computation (CoT assembles new information). This framing connects to three practical domains: (a) *inference-time compute allocation* — skip CoT generation when G*(t) >> 0 for easy problems, providing the principled diagnostic that current early-exit heuristics (ESTAR, DTSR, FRIT, CoDE-Stop) lack; (b) *benchmark validity* — problems where all models show persistent G*(t) >> 0 are not testing reasoning; (c) *safety monitoring* — the decoupled internal quality-monitoring system (Yuan et al.) is the kind of hidden computation alignment researchers worry about.\n\nWe adopt honest scoping: 2-3 faithfulness phenomena as the realistic classification target, with steganographic encoding and reasoning theater as stretch goals. The boundary between pre-CoT encoding and post-hoc rationalization may be empirically blurred (in both cases, the model may have committed to an answer before CoT begins, so P*(t) starts high in both), potentially collapsing the taxonomy to 2 primary categories (pre-committed vs. genuinely reasoning). Phase 0b explicitly tests 2-category vs. 3-category separability; either outcome is a strong contribution. Task-difficulty conditioning — grounded in David's easy (0.84) vs. hard (0.76) probe splits and Gjølbye et al.'s (2605.15454) domain-specific difficulty-geometry coupling (ρ⊥ = +0.41 on Codeforces) — reveals the decorative→load-bearing transition with length correction.\n\nCore contributions: (a) calibrated ICG diagnostic with shape-based trajectory analysis on 5 models (4 reasoning + 1 instruction-tuned control) × 4 benchmarks, the first framework capable of distinguishing faithful-correct from unfaithful-correct reasoning; (b) empirical pilot with external validation (TTS cross-reference, difficulty partition, FaithCoT-Bench supplementary) demonstrating 2-3 distinguishable G*(t) phenomenon signatures; (c) difficulty-conditioned gap analysis with domain-specific nuance; (d) head-to-head comparison against TTS, FaithCoT-Bench methods, and probe-only trajectories. Total compute: ~1050 H100-hours.\n\n## Core Problem\nA striking convergence of 2025-2026 findings reveals a fundamental disconnect in reasoning language models: their hidden states reliably encode information about answer correctness — linear probes achieving 0.82-0.95 AUROC across multiple independent groups — yet causal interventions based on these probes consistently fail to influence model outputs. Cox et al. (2603.01437) find steering via answer-content probes produces answer flip rates 'negligible against the orthogonal baseline' on reasoning models, despite >0.9 AUC on instruction-tuned models. Yuan et al. (2605.09502) systematically test four interventions (activation steering, probe-guided best-of-N, self-correction, activation patching) on models up to 72B and report ALL fail. This diagnostic-causal gap is NOT an obstacle; it IS the central phenomenon.\n\nThe literature conflates two probe targets: answer-content probes (Cox et al.: specific answer on binary tasks, ≤9B + GPT-OSS-20B) and correctness probes (Yuan et al.: right/wrong on models up to 72B; Zhang et al. 2504.05419: per-chunk correctness on 7B-70B). Answer-content gaps mean 'the model has decided but CoT doesn't derive the answer'; correctness gaps mean 'the model knows it's right/wrong but CoT doesn't reflect this awareness.'\n\nTemporal dynamics are empirically grounded: David (2511.14773) finds probe accuracy at 0.84 AUC by token 4, stable ~0.8 through token 100, with easy (0.84) vs. hard (0.76) splits. Zhang et al. (2504.05419) report 65%→79% chunk trajectories on R1-Distill. Esakkiraja et al. (2604.01202) find >90% pre-generation AUROC with characteristic dip at 5-10%. Chrabąszcz et al. (2605.18549) demonstrate 60+ signal-processing features achieving up to 17pp over static probes. Yet no framework jointly tracks information availability AND causal contribution: Chrabąszcz et al. lack any causal component; Ballon et al. (2601.23163) provide behavioral C(t) but no hidden-state measurement; CMI (2602.03994) provides structural layerwise audit on ~50 examples but measures representation routing, not functional text contribution; TTS provides per-step marginal causal contribution but no probe-side measurement and no cumulative sufficiency assessment; Thought Anchors (2506.19143) provide within-CoT causal structure but no external probe reference.\n\n## Opportunity\n(1) **Temporal gap measurement.** Multiple groups have independently built the measurement components — probe trajectories (Chrabąszcz: 60+ features, 91-97% AUROC; David: per-token; Zhang: per-chunk; Yuan: 0.95 overall; Esakkiraja: >90% pre-generation) and behavioral causal curves (Ballon: truncation-reinjection; TTS: per-step ATE; NLDD: per-position degradation) — but no one has unified them into a dual-stream temporal gap. Chrabąszcz et al. are structurally blind to the faithful-correct vs. unfaithful-correct distinction; Ballon et al. lack hidden-state measurement. The gap between these traditions IS the framework's niche.\n\n(2) **Phenomenon unification with honest scoping.** CoT faithfulness failures are studied in isolation: Reasoning Horizon (Ye et al. 2602.11201), pre-CoT encoding (Cox et al.; Esakkiraja et al.), Reasoning Theater (Boppana et al. 2603.05488), myopic planning (Xu et al. 2602.02103). We propose 2-3 are distinguishable via G*(t) trajectory shapes, honestly pre-registering that pre-CoT encoding and rationalization may collapse to a single \"pre-committed\" category.\n\n(3) **Task-difficulty conditioning.** ICLR 2026 Workshop finding, Li et al. (2510.22362): easy→decorative, hard→faithful. Gjølbye et al. (2605.15454): difficulty-geometry coupling domain-specific (ρ⊥ = +0.41 code, +0.05 math). ICG answers: at what difficulty does CoT transition from decorative to load-bearing?\n\n(4) **Probe target clarification.** First principled treatment contrasting correctness awareness gap vs. answer-content gap on applicable tasks.\n\nTwo prior works combine probing with causal intervention: Kudo et al. (EACL 2026, 2412.01113) on synthetic arithmetic, and CMI (2602.03994) on ~50 examples — CMI measures *structural mediation* (representation routing through layers) while ICG measures *functional contribution* (whether CoT text causally contributes to behavioral correctness). Wang (2604.15726) formalizes H1/H2/H0 hypotheses; ICG operationalizes the H1/H2 distinction empirically. Neither Kudo et al. nor CMI provides: (a) temporal coverage on natural benchmarks, (b) phenomenon mapping, (c) instance-level diagnostic, (d) multi-model comparison across model families, (e) robustness validation per Young's (2603.20172) classifier-sensitivity finding (kappa as low as 0.06), or (f) empirical pilot with external validation standards.\n\n## Landscape\n**Probe-based temporal measurement (P*(t) foundation).** Chrabąszcz et al. (2605.18549): probe trajectories with 60+ signal-processing features (volatility, trend, steady-state, boundary transients, autocorrelation) via 3-layer MLP + Multi-Instance Learning. Max-pooling: 91-97% AUROC harmfulness (vs. 33-61% average-pooling); up to 17pp over static on GSM8K across Llama-8B-R1-Distill and Qwen3-4B/8B/14B (~3000 GPU-hours). Critical: (a) NO causal component, (b) NO gap metric, (c) NO calibration, (d) NO faithfulness-mode taxonomy, (e) NO difficulty conditioning, (f) structurally cannot distinguish faithful-correct from unfaithful-correct. David (2511.14773): 0.84 AUC at t=4, stable ~0.8, easy/hard 0.84/0.76 on Qwen3-8B. Zhang et al. (2504.05419): 0.82-0.91 AUROC on GSM8K/MATH/AIME, 65%→79% trajectory, 24% token reduction via early-exit. Yuan et al. (2605.09502): 0.95 AUROC on Qwen-3B, 0.852 on R1-7B, 0.787 first-step, concealment gap 0.197 AUROC. Esakkiraja et al. (2604.01202): >90% pre-generation, dip at 5-10%, recovery to near-100%. Cox et al. (2603.01437): answer-content probes >0.9 AUC on instruction-tuned Gemma-2/Qwen-2.5, negligible flip on reasoning GPT-OSS-20B. Additional: Qian et al. (2506.02867, NeurIPS 2025); Lewis-Lim et al. (2508.19827, EMNLP 2025); Mirtaheri & Belkin (2603.17199); Occhipinti et al. (ICLR 2026 LIT Workshop).\n\n**Diagnostic-not-causal evidence.** Yuan et al. (2605.09502): four interventions all fail on Qwen2.5 (1.5B-72B), Llama-3.1-8B, Phi-3.5-mini, DeepSeek-R1-7B. 'The error signal is a diagnostic readout, not a causal component that can be edited.' Cox et al. independently confirm. Probe accuracy ≠ causal potency on reasoning models.\n\n**Behavioral C(t) measurement.** Ballon et al. (2601.23163): truncation-reinjection on Qwen3-4B/8B/14B and gpt-oss-20B/120B, decile intervals. Accuracy: 30.8-42.3% → 49.0-73.1% on GPQA-Diamond. Controls validate sequential content (intact +18.1-33.1% vs. shuffled +0.3-10.8%). Disclaims faithfulness analysis. Zhao et al. (2510.24941, TTS): per-step ATE on R1-Distill-Qwen-7B/14B/Llama-8B, only 2.3% AIME steps TTS≥0.7. Ye et al. (2602.11201, NLDD): Reasoning Horizon at 70-85% on synthetic tasks (natural benchmark generalizability unvalidated). Thought Anchors (2506.19143): per-sentence counterfactual importance via 100-rollout replacement sampling; identifies \"anchor\" sentences steering reasoning trajectory — provides within-CoT causal structure but no probe reference for assessing redundancy relative to internal state. Basu & Chakraborty (2603.22816): decorative/scaffolding/genuine taxonomy. FACT-E (Sun et al. 2604.10693, ACL Findings 2026).\n\n**Probe-intervention combinations.** Kudo et al. (2412.01113, EACL 2026): per-position probes + activation patching on synthetic arithmetic, 9 models. CMI (2602.03994): layerwise activation patching on Phi/Qwen/DialoGPT, ~50 examples. CMI measures *structural mediation* (representation routing); ICG measures *functional contribution* (behavioral text causation). Both complementary precursors on small/synthetic samples.\n\n**Latent-reasoning theory.** Wang (2604.15726): H1/H2/H0 hypotheses with compute-audited designs. ICG operationalizes H1/H2 distinction.\n\n**Temporal hidden-state dynamics.** Gjølbye et al. (2605.15454): 11 models, 3 domains, length correction. ρ⊥^D = +0.41 Codeforces vs. −0.06 baselines; weaker on MATH (+0.05). Prompt-stage probes don't mirror generation-time dynamics. Furuya & Tanimura (2605.01853, StALT). Herrmann et al. (2605.09159): internal polylogue dynamics. Li et al. (2510.22362, NeurIPS 2025 MechInterp Workshop, Concept Walk): easy→decorative, hard→faithful. Vilas et al. (2510.10494, ICLR 2026): 14-70% token savings.\n\n**Probe calibration.** Hewitt & Liang (EMNLP 2019): 4.5 selectivity. Ravichander et al. (2005.00719): properties recoverable when unused. Voita & Titov (EMNLP 2020, 2003.12298): MDL probing. Chun et al. (2602.20338, MCT): geometric pulse — separability peaks transiently while probe accuracy persists. Validates null-probe calibration need.\n\n**Trajectory-shape analysis.** Entropy trajectories (2603.18940): +5.8pp from monotonicity. RQA (2602.06266): temporal 36.94% vs. aggregates 28.97%. Microsoft (2604.05655): 0.852 vs. 0.649 AUC.\n\n**Measurement sensitivity.** Young (2603.20172): kappa as low as 0.06, up to 30.6pp divergence. Young (2603.26410). 'Lie to Me' (2603.22582).\n\n**Additional.** Internal States Before Wait (2510.04128). From Reasoning to Answer (2509.23676). FaithCoT-Bench (ICLR 2026, 2510.04040): 1000+ expert-annotated trajectories, 11 methods, 4 paradigms. Jin et al. survey (ARR for ACL 2026). Liu et al. (2602.13904). Reasoning Theater (2603.05488). Early-exit: ESTAR, DTSR, NEAT, CoDE-Stop, FRIT (Swaroop et al., 2509.13334). Breaking the Chain (Somov et al., 2603.16475). Step-Level Hallucination (Alvarez & Baheri, 2605.13772). SAE Reasoning Features (2503.18878). Solution Hides in Hidden States (2604.23351). Knowing Before Saying (ACL Findings 2025, 2505.24362). LEACE (Belrose et al., NeurIPS 2023, 2306.03819). CoT Monitorability (Anwar et al., 2602.18297). Understanding CoT via Information Theory (Ton et al., ICML 2025, 2411.11984).\n\n**What remains open.** No framework provides: (1) dual-stream temporal gap enabling faithful-vs-unfaithful discrimination for correct instances; (2) empirically-validated phenomenon taxonomy with external validation; (3) instance-level diagnostic from temporal gap; (4) difficulty-conditioned gap with domain nuance; (5) head-to-head comparison against existing causal faithfulness methods; (6) instruction-tuned vs. reasoning model control comparison within the same framework.\n\n## Approach\n**Formal Framework.** Two time-varying quantities at equally-spaced positions (primary: 20-50 percentile-based positions; token-level supplementary on subsets):\n\n(i) *P*(t)*: Cross-validated AUROC of linear probe on layer-l hidden states, calibrated via null-probe (P*(t) = P(t) − P_null(t), Hewitt & Liang 2019). Shared probe evaluated at each position (following Chrabąszcz's per-token evaluation, avoiding per-position training). **Target: correctness (right/wrong)** — broader applicability than answer-content probes, directly tied to the diagnostic-not-causal finding (Yuan et al.), more interpretable for faithfulness. Supplementary answer-content probes on binary/MC subsets. Probed at layers L/4, L/2, 3L/4, L. MCT (Chun et al. 2602.20338) supplementary concordance on 500 examples: if MCT capacity diverges from P*(t), identifies positions where probe signal may reflect retrievability rather than geometrically organized information.\n\n(ii) *C(t)*: Three estimators aggregated into C_agg(t): (a) **Prefix truncation** — Ballon et al.'s (2601.23163) protocol with three controls (random, swapped, shuffled tokens), measuring P(correct | CoT[:t]) vs. P(correct | full CoT). This measures *cumulative sufficiency* — whether CoT up to position t is sufficient for correctness — which is theoretically distinct from per-step *marginal contribution* (TTS); (b) **Paraphrase perturbation** — sentence-level segments paraphrased by external model (Claude Haiku or GPT-4o-mini for cost efficiency), 2-3 variants per segment, NLI-based semantic preservation verification. Answer stability: P(same answer | paraphrased CoT). Protocol follows FaithCoT-Bench (ICLR 2026) paraphrasing paradigm. Applied to stratified subset (~40% of examples per cell) for cost control, with full prefix truncation on all examples; (c) **NLDD** (Ye et al. 2602.11201, conditional on Phase 0a feasibility) — logit degradation under corruption. Sentence-level segmentation aligned with TTS approach (Zhao et al.). Multiple estimators provide robustness per Young's (2603.20172) classifier-sensitivity finding.\n\n**C(t) Aggregation and Gap Normalization.** Primary: rank-based normalization — each estimator converted to instance-level percentile ranks within model-benchmark cell, then combined. If NLDD underperforms on specific benchmarks (Phase 0a), two-estimator C_agg(t) (prefix + paraphrase) is primary for those benchmarks; three-estimator as supplementary. Ablation reports: (a) per-estimator G*(t) for phenomenon classification; (b) inverse-variance weighting vs. equal-weight; (c) pairwise Spearman correlation and Cohen's kappa between estimators. Diagnostic value lies in trajectory shapes, not magnitudes, so normalization affects scale but not shape-based signatures.\n\n**G*(t) = P*(t) − C(t).** Primary signal:\n- G*(t) ≈ 0: Aligned (necessary for faithfulness; H2-consistent per Wang 2604.15726)\n- G*(t) >> 0: Diagnostic excess — 'knows but doesn't use' (H1-consistent)\n- G*(t) < 0: Information assembled during reasoning\n\n**Interpretive caveat.** G*(t) >> 0 indicates correctness-correlated information not causally channeled through CoT, but does not entail intentional withholding — some signals may be computational byproducts rather than actionable knowledge. MCT concordance provides partial validation of this boundary.\n\n**Phenomenon Predictions (honestly scoped).**\n*Primary (HIGH confidence):*\n(i) *Pre-committed reasoning* (encompasses pre-CoT encoding and potentially post-hoc rationalization): G*(t) starts high, stays high or widens. P*(t) high from start (David: 0.84 at t=4; Esakkiraja: >90% pre-generation; Cox: >0.9 pre-CoT), C(t) low or flat.\n(ii) *Genuine multi-step reasoning*: G*(t) converges toward zero. P*(t) rises gradually, C(t) tracks P*(t). Zhang et al.'s 65%→79%, Li et al.'s hard→faithful, Ballon et al.'s monotonic accuracy increase.\n\n*Secondary (MODERATE confidence — Phase 0b tests whether separable from pre-committed):*\n(iii) *Post-hoc rationalization as distinct from pre-CoT encoding*: If distinguishable, the separation should manifest primarily in C(t) dynamics (rationalization may show spurious partial C(t) increases as the model crafts locally-consistent reasoning, while pre-CoT encoding shows flat-zero C(t)) rather than P*(t). Phase 0b explicitly tests 2-category vs. 3-category separability; 2-category (pre-committed vs. genuine) is pre-registered as an acceptable outcome.\n\n*Stretch (require additional features):*\n(iv) *Steganographic encoding*: Dip-and-recovery, consistent with Esakkiraja's 5-10% dip.\n(v) *Reasoning Theater*: May overlap with pre-committed. Chrabąszcz-style features may enable separation. Reported with confusion matrices.\n\n**Semi-Synthetic Simulation (hypothesis generation, NOT validation).** Constructed from published data (David, Zhang, Esakkiraja, Yuan for probes; NLDD, TTS for causal; Chun et al. MCT for inflation). Real validation in Phase 0b.\n\n**Phase 0a: Gap Characterization + NLDD Feasibility (Weeks 1-2.5).** 500 examples × 3 datasets (GSM8K, MATH-500, MMLU) × 3 models (DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct):\n(i) Construct P*(t) and C(t) curves at 20-50 position resolution\n(ii) Validate null-probe calibration\n(iii) Characterize causal potency (Cox et al. protocol: steering on reasoning vs. instruction-tuned)\n(iv) **NLDD feasibility**: 7B × 100 examples on GSM8K (clear steps) + MMLU (ambiguous steps). If SNR uninformative on MMLU, restrict NLDD to math/code or replace with TTS-style perturbation. Cost: <10 GPU-hrs; gates 250+ hrs NLDD investment.\n\n**Phase 0b: Empirical Pilot (Weeks 2.5-4).** R1-Distill-Qwen-7B × GSM8K + MATH-500, 1000 examples.\n\n*Primary validation (external standards):*\n(i) **Difficulty-only partition**: model-independent difficulty bins (easy/medium/hard), no P*/C features used. Test G*(t) shape differences: d > 0.5 AND p < 0.01 (Bonferroni-corrected) on 2+ trajectory features.\n(ii) **TTS cross-reference** (primary external validation): compute Zhao et al.'s TTS on same examples; test whether high-TTS (genuine reasoning) vs. low-TTS (decorative) produce distinguishable G*(t) shapes.\n(iii) **2-category vs. 3-category test**: explicitly test whether pre-CoT encoding and post-hoc rationalization are separable or collapse to single \"pre-committed\" category.\n(iv) **FaithCoT-Bench** (supplementary): if instance-level overlap available, test correlation with expert labels; otherwise dataset-level validation.\n\n*Supplementary*: P*/C-based partition as self-consistency check.\nLength correction per Gjølbye et al. (2605.15454). Success: d > 0.5 between 2+ externally-defined partitions. If d < 0.3, downscope to characterization paper.\n\n**Phase 1: Full ICG (Weeks 4-9).** Conditional on Phase 0b d > 0.5. **5 models**: DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Llama-8B, DeepSeek-R1-Distill-Qwen-14B, QwQ-32B (reasoning models spanning 2 architecture families) + Qwen2.5-7B-Instruct (instruction-tuned control — expected G*(t) ≈ 0 as sanity check). **4 benchmarks**: GSM8K (500 examples), MATH-500 (500), GPQA-Diamond (~198 full), AIME (~90 full). Per-cell: ~1288 examples × 5 models. Full calibrated P*(t) + MCT supplementary + three C(t) estimators (NLDD conditional, paraphrase on ~40% stratified subset) + Ballon-style controls. Cross-reference with TTS at step boundaries. Bootstrap 95% CI on G*(t). ~250 H100-hours.\n\n**Phase 2: Difficulty Conditioning (Weeks 7-11).** Difficulty quintiles per benchmark. G*(t) per quintile. Expected: easy → persistent gap, hard → converging gap. Length correction; domain-specific reporting (stronger on math/code per Gjølbye et al.'s ρ⊥ = +0.41 code vs. +0.05 math).\n\n**Phase 3: Classification, Baselines, Robustness (Weeks 9-14).**\n\n*Classification framework:* G*(t) features (initial value, slope, convergence rate, dC/dt locality) + Chrabąszcz-style features (volatility, trend, boundary transients, autocorrelation). Classifier gradient: logistic regression → RF → MLP; report all. Metric: macro-F1 (primary) + confusion matrix + reliability diagram. Validation: 5-fold + cross-model (train A → test B, reporting within-family vs. cross-family separately) + cross-benchmark generalization. Paired permutation tests with Bonferroni correction for all head-to-head comparisons.\n\n*Baselines:* (a) Random + majority-class; (b) Difficulty-only classifier; (c) **Probe-trajectory-only** (Chrabąszcz-style P*(t) features, no C(t)) — \"no causal dimension\" ablation; (d) **TTS-only** — per-step marginal causal contribution without probe dimension.\n\n*Head-to-head TIF validation:* TIF score vs. FaithCoT-Bench detection methods (Adding Mistakes, Removing Steps, Early Answering, Paraphrasing) and TTS on overlapping examples, comparing instance-level correlation with ground truth.\n\n*Robustness ablations (7 dimensions):* (a) probe architecture (linear vs. 2-layer MLP); (b) layer selection; (c) C(t) estimator agreement + per-estimator performance + weighting schemes; (d) gap normalization (rank vs. min-max vs. z-score); (e) calibration method (shuffled-label vs. random-representation); (f) probe target (correctness vs. answer-content); (g) **temporal resolution** (5/10/20/35/50 positions + token-level — reporting resolution vs. macro-F1 curve and saturation point).\n\n**TIF Score.** Normalized area under calibrated G*(t), benchmarked against FaithCoT-Bench and Liu et al.'s (2602.13904) text-level metrics.\n\n**Paper Focus.** Core contributions: (1) ICG diagnostic — first framework distinguishing faithful-correct from unfaithful-correct reasoning via dual-stream temporal gap, with instruction-tuned control validating the framework; (2) Phase 0b pilot with external validation demonstrating 2-3 distinguishable G*(t) signatures (or honestly reporting 2-category outcome); (3) difficulty-conditioned gap revealing decorative→load-bearing transition; (4) head-to-head showing ICG's value over probe-only, TTS-only, and FaithCoT-Bench methods. Supporting: 7-dimension ablations; TIF validation. Supplementary: 671B subset (500 examples, 3 layers); answer-content vs. correctness comparison; semi-synthetic simulation; CMI structural-functional prediction if resources allow.\n\n**Experiments.** DeepSeek-R1-Distill-Qwen-7B/14B, DeepSeek-R1-Distill-Llama-8B, QwQ-32B, Qwen2.5-7B-Instruct across GSM8K, MATH-500, GPQA-Diamond, AIME. 671B validation (500-example subset). Calibration: synthetic arithmetic (G* ≈ 0 expected), TTS cross-reference, MCT supplementary. Gjølbye-style length correction throughout.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '~1050 H100-hours (Phase 0a: 90 hrs [3 models × 3 datasets + NLDD feasibility]; Phase 0b: 30 hrs [pilot]; Phase 1: 250 hrs [5 models × 4 benchmarks, probes + 3 C(t) estimators + controls]; Phase 2: 50 hrs [difficulty conditioning]; Phase 3: 70 hrs [classification + 7-dim ablations + baselines]; NLDD 32B conditional: 250 hrs [primary bottleneck]; NLDD 7B/14B: 100 hrs; MCT supplementary: 50 hrs; 671B subset: 50 hrs [8×H100]; semi-synthetic: 30 hrs; paraphrase model: ~80 hrs inference on target models for stability checks)', 'paraphrase_api_cost': '~$800-1500 (Claude Haiku/GPT-4o-mini on stratified ~40% subset, 2-3 variants)', 'timeline': '15-17 weeks (2 researchers)', 'estimated_gpu_cost': '$3,200 at ~$3/H100-hour', 'storage': '3-5 TB (4 layers, fp16); ~1.5 TB with PCA/on-the-fly'}, 'human_in_loop': {'gpu_hours': '~1050 H100-hours', 'timeline': '14 weeks (1 researcher + Claude)', 'claude_api_cost': '$500 (experiment design) + $800-1500 (paraphrase generation)', 'estimated_gpu_cost': '$3,200'}, 'auto_research': {'gpu_hours': '~1050 H100-hours', 'timeline': '12 weeks', 'claude_api_cost': '$900 + $800-1500 (paraphrase)', 'estimated_gpu_cost': '$3,200', 'speed_bottleneck': 'NLDD on 32B (~250 hrs, conditional on Phase 0a) is primary bottleneck. Phase 0b pilot (30 hrs) provides early go/no-go.'}}\n\n## Inspired By\nThe convergence of five independent lines of evidence — (a) Cox et al.'s steering failure on reasoning models despite high probe accuracy; (b) Yuan et al.'s four-intervention failure establishing 'diagnostic not causal'; (c) temporal probe dynamics (David, Zhang, Esakkiraja, Chrabąszcz: 60+ features, up to 17pp improvement); (d) Ballon et al.'s truncation-reinjection demonstrating monotonic behavioral C(t) with controls; (e) trajectory-shape literature (arXiv 2603.18940, 2602.06266, 2604.05655) showing shapes carry diagnostic information — all pointing to: the gap between diagnostic availability and causal contribution IS the phenomenon, and its temporal shape reveals the mechanism. Additionally: Wang's (2604.15726) H1/H2/H0; Gjølbye et al.'s (2605.15454) domain-specific coupling; Chun et al.'s (2602.20338) MCT geometric pulse; CMI's (2602.03994) structural mediation; Thought Anchors' (2506.19143) within-CoT causal structure.\n\n## Target Venues\n- ICLR 2027 (abstract: Sep 19, full paper: Sep 24, 2026; primary target)\n- ICML 2027 (full paper: Jan 29, 2027; fallback)\n\n## Key References\n- Monitoring the Internal Monologue: Probe Trajectories (Chrabąszcz et al., arXiv 2605.18549)\n- Probing the Trajectories of Reasoning Traces (Ballon et al., arXiv 2601.23163)\n- LLM Reasoning Is Latent (Wang, arXiv 2604.15726)\n- Reasoning Models Move Differently (Gjølbye et al., arXiv 2605.15454)\n- Hidden Error Awareness (Yuan et al., arXiv 2605.09502)\n- Decoding Answers Before CoT (Cox et al., arXiv 2603.01437)\n- Temporal Predictors of Outcome (David, arXiv 2511.14773)\n- Reasoning Models Know When They're Right (Zhang et al., arXiv 2504.05419)\n- Therefore I am. I Think (Esakkiraja et al., arXiv 2604.01202)\n- True Thinking Score (Zhao et al., arXiv 2510.24941)\n- Mechanistic Evidence for Faithfulness Decay / NLDD (Ye et al., arXiv 2602.11201)\n- Internal Polylogue (Herrmann et al., arXiv 2605.09159)\n- Faithfully Compute Answers During CoT (Kudo et al., EACL 2026, arXiv 2412.01113)\n- Causal Bypass / CMI (Sathyanarayanan et al., arXiv 2602.03994)\n- StALT (Furuya & Tanimura, arXiv 2605.01853)\n- Concept Walk (Li et al., arXiv 2510.22362, NeurIPS 2025 MechInterp Workshop)\n- Task Difficulty Shapes CoT Faithfulness (ICLR 2026 Workshop)\n- Diagnosing Pathological CoT (Liu et al., arXiv 2602.13904)\n- Measuring Faithfulness Depends on How You Measure (Young, arXiv 2603.20172)\n- MCT / Emergent Manifold Separability (Chun et al., arXiv 2602.20338)\n- Latent Temporal Signals (Vilas et al., ICLR 2026, arXiv 2510.10494)\n- Probing and Steering CoT Unfaithfulness (Occhipinti et al., ICLR 2026 LIT Workshop)\n- Designing and Interpreting Probes (Hewitt & Liang, EMNLP 2019)\n- Information-Theoretic Probing with MDL (Voita & Titov, EMNLP 2020, arXiv 2003.12298)\n- Probing the Probing Paradigm (Ravichander et al., arXiv 2005.00719)\n- Entropy trajectory shapes (arXiv 2603.18940)\n- RQA of Reasoning Dynamics (arXiv 2602.06266)\n- LLM Reasoning as Trajectories (arXiv 2604.05655, Microsoft)\n- Internal States Before Wait (arXiv 2510.04128)\n- FACT-E (Sun et al., ACL Findings 2026, arXiv 2604.10693)\n- Breaking the Chain (Somov et al., arXiv 2603.16475)\n- The Illusion of Reasoning (Basu & Chakraborty, arXiv 2603.22816)\n- FaithCoT-Bench (ICLR 2026, arXiv 2510.04040)\n- The Mirage of Explainability survey (Jin et al., ARR for ACL 2026)\n- Reasoning Theater (Boppana et al., arXiv 2603.05488)\n- No Global Plan in CoT (Xu et al., arXiv 2602.02103)\n- Catching Rationalization in the Act (Mirtaheri & Belkin, arXiv 2603.17199)\n- CoT Monitorability (Anwar et al., arXiv 2602.18297)\n- Understanding CoT via Information Theory (Ton et al., ICML 2025, arXiv 2411.11984)\n- Demystifying Reasoning Dynamics (Qian et al., NeurIPS 2025, arXiv 2506.02867)\n- Analysing CoT Dynamics (Lewis-Lim et al., EMNLP 2025, arXiv 2508.19827)\n- Why Models Know But Don't Say (Young, arXiv 2603.26410)\n- Lie to Me (arXiv 2603.22582)\n- Step-Level Hallucination (Alvarez & Baheri, arXiv 2605.13772)\n- From Reasoning to Answer (arXiv 2509.23676)\n- SAE Reasoning Features (arXiv 2503.18878)\n- FRIT (Swaroop et al., arXiv 2509.13334)\n- Solution Hides in Hidden States (arXiv 2604.23351)\n- Knowing Before Saying (ACL Findings 2025, arXiv 2505.24362)\n- LEACE (Belrose et al., NeurIPS 2023, arXiv 2306.03819)\n- Thought Anchors (arXiv 2506.19143)"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T04:35:22.711Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:35:22.711Z",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4"
}
```

---

## Round 1

39 recorded events

### User

_source line 3 · 2026-05-20T04:35:22.723Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
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
  "promptId": "1e462d9b-9458-4a67-ae07-9e2cab1e57dc",
  "type": "user",
  "uuid": "4af98f74-2619-4f8d-a2a0-7c039ceb5229",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:35:22.721Z_

```json
{
  "parentUuid": "4af98f74-2619-4f8d-a2a0-7c039ceb5229",
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
  "uuid": "f6d35ea9-bb13-4679-b1a0-a94ac7b6bc93",
  "timestamp": "2026-05-20T04:35:22.721Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:35:22.721Z_

```json
{
  "parentUuid": "f6d35ea9-bb13-4679-b1a0-a94ac7b6bc93",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "73f641f5-e0d4-4567-8ebb-1f36f64eaf49",
  "timestamp": "2026-05-20T04:35:22.721Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-T…",
  "leafUuid": "73f641f5-e0d4-4567-8ebb-1f36f64eaf49",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Measuring chain-of-thought faithfulness via temporal gaps",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4"
}
```

---

### Assistant

_source line 8 · 2026-05-20T04:35:30.285Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this proposal carefully. It's about measuring CoT faithfulness in reasoning models by combining probe-based information tracking with causal contribution measurement. I need to do thorough research on the current state of this field before providing my assessment.

Let me start by searching for the key papers and recent developments in this area.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73f641f5-e0d4-4567-8ebb-1f36f64eaf49",
  "isSidechain": false,
  "requestId": "req_011CbDCVPxE5ba4bNT2iHbGf",
  "type": "assistant",
  "uuid": "74a01aa1-004f-43f1-bb8c-3b74820537b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NLFFNZ21eJuSvMRANRhsiC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14678,
      "cache_read_input_tokens": 11374,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 186,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 14678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14678
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

_source line 9 · 2026-05-20T04:35:30.406Z_

I'll start by conducting thorough research on the field before making any assessment. Let me search for the key topics and competing works.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74a01aa1-004f-43f1-bb8c-3b74820537b3",
  "isSidechain": false,
  "requestId": "req_011CbDCVPxE5ba4bNT2iHbGf",
  "type": "assistant",
  "uuid": "eeb210f3-5188-43f8-b51a-a5b9f7154a02",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NLFFNZ21eJuSvMRANRhsiC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14678,
      "cache_read_input_tokens": 11374,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 186,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 14678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14678
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

_source line 10 · 2026-05-20T04:35:30.565Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0172J1QSNzRCuN4omqaTWDrB`</summary>

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
  "parentUuid": "eeb210f3-5188-43f8-b51a-a5b9f7154a02",
  "isSidechain": false,
  "requestId": "req_011CbDCVPxE5ba4bNT2iHbGf",
  "type": "assistant",
  "uuid": "4bf8325c-ea15-4a06-9db8-4e0b64cb7c80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NLFFNZ21eJuSvMRANRhsiC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14678,
      "cache_read_input_tokens": 11374,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 186,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 14678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14678
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

_source line 11 · 2026-05-20T04:35:30.572Z_

<details><summary>↩ Tool result · `toolu_0172J1QSNzRCuN4omqaTWDrB`</summary>

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
  "parentUuid": "4bf8325c-ea15-4a06-9db8-4e0b64cb7c80",
  "isSidechain": false,
  "promptId": "1e462d9b-9458-4a67-ae07-9e2cab1e57dc",
  "type": "user",
  "uuid": "15e4fba4-485e-462f-8e26-b8d92f7b14e3",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "4bf8325c-ea15-4a06-9db8-4e0b64cb7c80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T04:35:35.487Z_

Now let me conduct the required research. I'll run multiple searches in parallel to cover the key aspects of this proposal's field.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15e4fba4-485e-462f-8e26-b8d92f7b14e3",
  "isSidechain": false,
  "requestId": "req_011CbDCVz35faC1knfpWFte7",
  "type": "assistant",
  "uuid": "7c456dc1-c2a0-44e4-a398-cae3e987894a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSWCvgR482evC39SSeSye8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 714,
      "cache_read_input_tokens": 26052,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 714,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 99,
          "cache_read_input_tokens": 26052,
          "cache_creation_input_tokens": 714,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 714
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

_source line 13 · 2026-05-20T04:35:35.956Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LuFhjVix6TJ6NirSRqx5sv`</summary>

```json
{
  "query": "chain-of-thought faithfulness probing causal intervention reasoning models 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c456dc1-c2a0-44e4-a398-cae3e987894a",
  "isSidechain": false,
  "requestId": "req_011CbDCVz35faC1knfpWFte7",
  "type": "assistant",
  "uuid": "70630b0e-a9cb-4079-8c02-586b9da93427",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSWCvgR482evC39SSeSye8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 714,
      "cache_read_input_tokens": 26052,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 714,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 99,
          "cache_read_input_tokens": 26052,
          "cache_creation_input_tokens": 714,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 714
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

_source line 14 · 2026-05-20T04:35:43.883Z_

<details><summary>↩ Tool result · `toolu_01LuFhjVix6TJ6NirSRqx5sv`</summary>

```text
Web search results for query: "chain-of-thought faithfulness probing causal intervention reasoning models 2025 2026"

Links: [{"title":"Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models","url":"https://arxiv.org/html/2603.26410"},{"title":"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures","url":"https://arxiv.org/html/2603.16475v1"},{"title":"Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning | Request PDF","url":"https://www.researchgate.net/publication/386203451_Making_Reasoning_Matter_Measuring_and_Improving_Faithfulness_of_Chain-of-Thought_Reasoning"},{"title":"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2602.11201v1"},{"title":"FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness","url":"https://arxiv.org/pdf/2509.13334"},{"title":"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps","url":"https://arxiv.org/html/2502.14829v3"},{"title":"How does Chain of Thought Think? Mechanistic ...","url":"https://arxiv.org/pdf/2507.22928"},{"title":"How does Chain of Thought Think? Mechanistic Interpretability of Chain-of-Thought Reasoning with Sparse Autoencoding","url":"https://arxiv.org/html/2507.22928v1"}]

I found relevant research on chain-of-thought faithfulness, probing, and causal intervention methods in reasoning models from 2025-2026. Here are the key findings:

## Recent Research on CoT Faithfulness

Chen et al. (2025) introduced a hint-injection methodology to test whether models verbalize the influence of misleading hints, finding that faithfulness varies dramatically by model and hint type.

Ye et al. (2026) identified a "Reasoning Horizon" at 70–85% of chain length, beyond which reasoning tokens have diminishing causal influence on the final answer. Additionally, Boppana et al. (2026) used activation probes to show that models often commit to answers early in the reasoning chain, with subsequent tokens serving a performative rather than computational role.

## Causal Intervention Methods

Reasoning intervention approaches evaluate faithfulness by modifying reasoning traces or introducing perturbations to the input and measuring whether the model's prediction changes accordingly, including trace perturbation protocols that edit or truncate chain-of-thought reasoning to test whether the final answer depends on the generated reasoning steps.

FRIT (Faithful Reasoning via Intervention Training) is a scalable method for improving CoT faithfulness without human supervision that uses causality of CoT steps to fine-tune for more faithful outputs.

## Mechanistic Analysis Approaches

A framework to quantify CoT faithfulness uses three complementary perspectives: behavioral NLDD, representational (RSA), and geometric (TAS). Matton et al. (2025) introduce interventions at the semantic concept level, elevating faithfulness analysis to a higher abstraction level.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70630b0e-a9cb-4079-8c02-586b9da93427",
  "isSidechain": false,
  "promptId": "1e462d9b-9458-4a67-ae07-9e2cab1e57dc",
  "type": "user",
  "uuid": "6a547d03-ca36-4aaa-be25-eebddbc9d702",
  "toolUseResult": {
    "query": "chain-of-thought faithfulness probing causal intervention reasoning models 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EPGTgx6Xe2efp3cGzmmkLS",
        "content": [
          {
            "title": "Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models",
            "url": "https://arxiv.org/html/2603.26410"
          },
          {
            "title": "Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures",
            "url": "https://arxiv.org/html/2603.16475v1"
          },
          {
            "title": "Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning | Request PDF",
            "url": "https://www.researchgate.net/publication/386203451_Making_Reasoning_Matter_Measuring_and_Improving_Faithfulness_of_Chain-of-Thought_Reasoning"
          },
          {
            "title": "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2602.11201v1"
          },
          {
            "title": "FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness",
            "url": "https://arxiv.org/pdf/2509.13334"
          },
          {
            "title": "Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps",
            "url": "https://arxiv.org/html/2502.14829v3"
          },
          {
            "title": "How does Chain of Thought Think? Mechanistic ...",
            "url": "https://arxiv.org/pdf/2507.22928"
          },
          {
            "title": "How does Chain of Thought Think? Mechanistic Interpretability of Chain-of-Thought Reasoning with Sparse Autoencoding",
            "url": "https://arxiv.org/html/2507.22928v1"
          }
        ]
      },
      "I found relevant research on chain-of-thought faithfulness, probing, and causal intervention methods in reasoning models from 2025-2026. Here are the key findings:\n\n## Recent Research on CoT Faithfulness\n\nChen et al. (2025) introduced a hint-injection methodology to test whether models verbalize the influence of misleading hints, finding that faithfulness varies dramatically by model and hint type.\n\nYe et al. (2026) identified a \"Reasoning Horizon\" at 70–85% of chain length, beyond which reasoning tokens have diminishing causal influence on the final answer. Additionally, Boppana et al. (2026) used activation probes to show that models often commit to answers early in the reasoning chain, with subsequent tokens serving a performative rather than computational role.\n\n## Causal Intervention Methods\n\nReasoning intervention approaches evaluate faithfulness by modifying reasoning traces or introducing perturbations to the input and measuring whether the model's prediction changes accordingly, including trace perturbation protocols that edit or truncate chain-of-thought reasoning to test whether the final answer depends on the generated reasoning steps.\n\nFRIT (Faithful Reasoning via Intervention Training) is a scalable method for improving CoT faithfulness without human supervision that uses causality of CoT steps to fine-tune for more faithful outputs.\n\n## Mechanistic Analysis Approaches\n\nA framework to quantify CoT faithfulness uses three complementary perspectives: behavioral NLDD, representational (RSA), and geometric (TAS). Matton et al. (2025) introduce interventions at the semantic concept level, elevating faithfulness analysis to a higher abstraction level."
    ],
    "durationSeconds": 7.919682576,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "70630b0e-a9cb-4079-8c02-586b9da93427",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T04:35:47.000Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0189kVrrijiAtDnEo3s9qVWY`</summary>

```json
{
  "query": "probe trajectory hidden states reasoning LLM diagnostic causal gap 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a547d03-ca36-4aaa-be25-eebddbc9d702",
  "isSidechain": false,
  "requestId": "req_011CbDCWxbJ7WV26zcoKnyhR",
  "type": "assistant",
  "uuid": "6d95e63d-d2c1-4955-a330-53c3b395265e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nss2hYnykxwaFUArA99fYG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 916,
      "cache_read_input_tokens": 26766,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 916,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 26766,
          "cache_creation_input_tokens": 916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 916
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

_source line 16 · 2026-05-20T04:35:55.942Z_

<details><summary>↩ Tool result · `toolu_0189kVrrijiAtDnEo3s9qVWY`</summary>

```text
Web search results for query: "probe trajectory hidden states reasoning LLM diagnostic causal gap 2025 2026 arxiv"

Links: [{"title":"Probing the Trajectories of Reasoning Traces in Large Language Models","url":"https://arxiv.org/html/2601.23163v1"},{"title":"Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning","url":"https://arxiv.org/pdf/2603.01326"},{"title":"Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING","url":"https://arxiv.org/pdf/2510.04040"},{"title":"No Global Plan in Chain-of-Thought: Uncover the Latent Planning Horizon of LLMs","url":"https://arxiv.org/pdf/2602.02103"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs | medRxiv","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"}]

Based on the web search results, here are the most relevant papers addressing probe trajectory, hidden states, reasoning, and related topics from 2025-2026 on arXiv:

## Key Papers Found:

1. **"Probing the Trajectories of Reasoning Traces in Large Language Models"** (January 30, 2026)
   - Uses a trajectory-probing protocol to detect model-specific failure modes and find that accuracy increases along the reasoning trajectory
   - Observes "lost" trajectories where models go from right to wrong answers, and notes that longer reasoning does not guarantee better calibration

2. **"Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning"** (2026)
   - Proposes "Truth as a Trajectory" (TaT), which reframes LLM inference as a dynamical process rather than a collection of static layer snapshots
   - Plots layerwise hidden states as trajectories in activation space, where correct generations follow smoother paths while incorrect ones exhibit sharp deviations

3. **"No Global Plan in Chain-of-Thought: Uncover the Latent Planning Horizon of LLMs"** (February 3, 2026)
   - Observes that hidden states at the beginning of CoT can reliably predict total reasoning steps and key attributes with high correlation to realized trajectories
   - Presents probing experiments using a method called "Tele-Lens" to dissect LLM hidden states and evaluate internal planning

4. **"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs"** (September 2025)
   - Presents PING (Probing INternal states of Generative models), a framework that trains lightweight probes on frozen transformers to deliver structured predictions

5. **"FaithCoT-Bench: Benchmarking"** (Published at ICLR 2026)
   - Addresses approximating causal alignment between chain-of-thoughts and outputs


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d95e63d-d2c1-4955-a330-53c3b395265e",
  "isSidechain": false,
  "promptId": "1e462d9b-9458-4a67-ae07-9e2cab1e57dc",
  "type": "user",
  "uuid": "467ddc6f-1061-439c-83a8-622f2c3abf24",
  "toolUseResult": {
    "query": "probe trajectory hidden states reasoning LLM diagnostic causal gap 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ev2hxdrtj57ZWY2f5RPhLA",
        "content": [
          {
            "title": "Probing the Trajectories of Reasoning Traces in Large Language Models",
            "url": "https://arxiv.org/html/2601.23163v1"
          },
          {
            "title": "Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning",
            "url": "https://arxiv.org/pdf/2603.01326"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING",
            "url": "https://arxiv.org/pdf/2510.04040"
          },
          {
            "title": "No Global Plan in Chain-of-Thought: Uncover the Latent Planning Horizon of LLMs",
            "url": "https://arxiv.org/pdf/2602.02103"
          },
          {
            "title": "Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs | medRxiv",
            "url": "https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full"
          },
          {
            "title": "Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs",
            "url": "https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"
          }
        ]
      },
      "Based on the web search results, here are the most relevant papers addressing probe trajectory, hidden states, reasoning, and related topics from 2025-2026 on arXiv:\n\n## Key Papers Found:\n\n1. **\"Probing the Trajectories of Reasoning Traces in Large Language Models\"** (January 30, 2026)\n   - Uses a trajectory-probing protocol to detect model-specific failure modes and find that accuracy increases along the reasoning trajectory\n   - Observes \"lost\" trajectories where models go from right to wrong answers, and notes that longer reasoning does not guarantee better calibration\n\n2. **\"Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning\"** (2026)\n   - Proposes \"Truth as a Trajectory\" (TaT), which reframes LLM inference as a dynamical process rather than a collection of static layer snapshots\n   - Plots layerwise hidden states as trajectories in activation space, where correct generations follow smoother paths while incorrect ones exhibit sharp deviations\n\n3. **\"No Global Plan in Chain-of-Thought: Uncover the Latent Planning Horizon of LLMs\"** (February 3, 2026)\n   - Observes that hidden states at the beginning of CoT can reliably predict total reasoning steps and key attributes with high correlation to realized trajectories\n   - Presents probing experiments using a method called \"Tele-Lens\" to dissect LLM hidden states and evaluate internal planning\n\n4. **\"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs\"** (September 2025)\n   - Presents PING (Probing INternal states of Generative models), a framework that trains lightweight probes on frozen transformers to deliver structured predictions\n\n5. **\"FaithCoT-Bench: Benchmarking\"** (Published at ICLR 2026)\n   - Addresses approximating causal alignment between chain-of-thoughts and outputs"
    ],
    "durationSeconds": 8.932781495000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6d95e63d-d2c1-4955-a330-53c3b395265e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T04:35:58.363Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BKg6gBpvcE3syyYmVFFMVw`</summary>

```json
{
  "query": "Yuan et al 2605.09502 hidden error awareness intervention failure reasoning models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "467ddc6f-1061-439c-83a8-622f2c3abf24",
  "isSidechain": false,
  "requestId": "req_011CbDCXqsW5veHhhp5UTLCJ",
  "type": "assistant",
  "uuid": "b63e71de-49d3-4f13-aa20-5a79d3b0cefb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CkK1415W6mFSbEL8q74jje",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 895,
      "cache_read_input_tokens": 27682,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 895,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 27682,
          "cache_creation_input_tokens": 895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 895
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

_source line 18 · 2026-05-20T04:36:06.685Z_

<details><summary>↩ Tool result · `toolu_01BKg6gBpvcE3syyYmVFFMVw`</summary>

```text
Web search results for query: "Yuan et al 2605.09502 hidden error awareness intervention failure reasoning models"

Links: [{"title":"[2605.09502] Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal","url":"https://arxiv.org/abs/2605.09502"},{"title":"Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal","url":"https://arxiv.org/html/2605.09502"},{"title":"Stop Before You Fail: Operational Capability Boundaries for Mitigating Unproductive Reasoning in Large Reasoning Models","url":"https://arxiv.org/pdf/2509.24711"},{"title":"Hop, Skip, and Overthink: Diagnosing Why Reasoning Models Fumble during Multi-Hop Analysis","url":"https://arxiv.org/pdf/2508.04699"},{"title":"Fail Fast, or Ask: Mitigating the Deficiencies of Reasoning LLMs with Human-in-the-Loop Systems Engineering","url":"https://arxiv.org/pdf/2507.14406"},{"title":"Hidden in Plain Sight: Reasoning in Underspecified and Misspecified Scenarios for Multimodal LLMs","url":"https://arxiv.org/pdf/2506.00258"},{"title":"Are Reasoning LLMs Robust to Interventions on Their Chain-of-Thought?","url":"https://arxiv.org/pdf/2602.07470"}]

Based on the search results, I found the paper you're looking for. Here's information about the Yuan et al. 2605.09502 paper:

## Hidden Error Awareness in Chain-of-Thought Reasoning

The paper demonstrates that models internally detect their own reasoning errors but outwardly express confidence in them, challenging the assumption that generated reasoning reflects a model's internal computation.

**Key Findings:**

A linear probe on hidden states predicts trace correctness with 0.95 AUROC — from the very first reasoning step (0.79) — while verbalized confidence for wrong traces is 4.55/5, nearly identical to correct ones (4.87/5).

A text-surface classifier achieves only 0.59 on the same data, confirming a 0.20-point gap invisible in the generated text.

This hidden error awareness holds across three model families (Qwen, Llama, Phi), 1.5B-72B parameters, and RL-trained reasoning models (DeepSeek-R1, 0.852 AUROC).

**Intervention Attempts:**

Four interventions — activation steering, probe-guided best-of-N, self-correction, and activation patching — all fail; patching destroys output coherence entirely. The signal is diagnostic, not causal: a readout of computation quality, not a lever to redirect it.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b63e71de-49d3-4f13-aa20-5a79d3b0cefb",
  "isSidechain": false,
  "promptId": "1e462d9b-9458-4a67-ae07-9e2cab1e57dc",
  "type": "user",
  "uuid": "9e0db409-20b3-4742-8f98-2f4fe2b9f460",
  "toolUseResult": {
    "query": "Yuan et al 2605.09502 hidden error awareness intervention failure reasoning models",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RwhNeZMEHYbd8ALAETiGyw",
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
            "title": "Stop Before You Fail: Operational Capability Boundaries for Mitigating Unproductive Reasoning in Large Reasoning Models",
            "url": "https://arxiv.org/pdf/2509.24711"
          },
          {
            "title": "Hop, Skip, and Overthink: Diagnosing Why Reasoning Models Fumble during Multi-Hop Analysis",
            "url": "https://arxiv.org/pdf/2508.04699"
          },
          {
            "title": "Fail Fast, or Ask: Mitigating the Deficiencies of Reasoning LLMs with Human-in-the-Loop Systems Engineering",
            "url": "https://arxiv.org/pdf/2507.14406"
          },
          {
            "title": "Hidden in Plain Sight: Reasoning in Underspecified and Misspecified Scenarios for Multimodal LLMs",
            "url": "https://arxiv.org/pdf/2506.00258"
          },
          {
            "title": "Are Reasoning LLMs Robust to Interventions on Their Chain-of-Thought?",
            "url": "https://arxiv.org/pdf/2602.07470"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's information about the Yuan et al. 2605.09502 paper:\n\n## Hidden Error Awareness in Chain-of-Thought Reasoning\n\nThe paper demonstrates that models internally detect their own reasoning errors but outwardly express confidence in them, challenging the assumption that generated reasoning reflects a model's internal computation.\n\n**Key Findings:**\n\nA linear probe on hidden states predicts trace correctness with 0.95 AUROC — from the very first reasoning step (0.79) — while verbalized confidence for wrong traces is 4.55/5, nearly identical to correct ones (4.87/5).\n\nA text-surface classifier achieves only 0.59 on the same data, confirming a 0.20-point gap invisible in the generated text.\n\nThis hidden error awareness holds across three model families (Qwen, Llama, Phi), 1.5B-72B parameters, and RL-trained reasoning models (DeepSeek-R1, 0.852 AUROC).\n\n**Intervention Attempts:**\n\nFour interventions — activation steering, probe-guided best-of-N, self-correction, and activation patching — all fail; patching destroys output coherence entirely. The signal is diagnostic, not causal: a readout of computation quality, not a lever to redirect it."
    ],
    "durationSeconds": 8.318304012,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b63e71de-49d3-4f13-aa20-5a79d3b0cefb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T04:36:10.179Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YU5v2T4upbg8hXn2dXgJ2A`</summary>

```json
{
  "query": "Chrabąszcz probe trajectories monitoring internal monologue 2605.18549 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e0db409-20b3-4742-8f98-2f4fe2b9f460",
  "isSidechain": false,
  "requestId": "req_011CbDCYdn1f6Ggyo1Yy6XkG",
  "type": "assistant",
  "uuid": "747b7342-4bee-4478-9619-6b22085b97e1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0126LAuiBs8XZz7th2gvFUuE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 779,
      "cache_read_input_tokens": 28577,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 779,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 28577,
          "cache_creation_input_tokens": 779,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 779
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

_source line 20 · 2026-05-20T04:36:15.683Z_

<details><summary>↩ Tool result · `toolu_01YU5v2T4upbg8hXn2dXgJ2A`</summary>

```text
Web search results for query: "Chrabąszcz probe trajectories monitoring internal monologue 2605.18549 2026"

Links: [{"title":"[2605.18549] Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics","url":"https://arxiv.org/abs/2605.18549"},{"title":"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics","url":"https://arxiv.org/html/2605.18549"},{"title":"Inner Monologue Statistics: 2026 Verified Report","url":"https://wifitalents.com/inner-monologue-statistics/"},{"title":"Internal Monologue: Data Reports 2026","url":"https://wifitalents.com/internal-monologue-statistics/"},{"title":"Spectroscopic Active Probes for Investigation of Lipid Transformation in Cells and Membranes | The Journal of Physical Chemistry B","url":"https://pubs.acs.org/doi/10.1021/acs.jpcb.5c05981"},{"title":"(PDF) Internal Monologue","url":"https://www.academia.edu/68121407/Internal_Monologue"},{"title":"Trajectory sampling using spatial familiarity","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11435202"},{"title":"Method, apparatus, and computer program product for anonymizing trajectories","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11662215"}]

Based on the search results, I found the paper you're looking for:

The paper "Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics" (arXiv:2605.18549) was submitted on May 18, 2026, with authors Maciej Chrabąszcz, Aleksander Szymczyk, Marcin Sendera, Tomasz Trzciński, and Sebastian Cygert.

The paper addresses Large Reasoning Models (LRMs) and their Chain of Thought (CoT) reasoning for safety monitoring. The research investigates hidden representations of LRMs to predict future behavior from prompt and CoT representations, using a probe trajectory—the continuous evolution of a concept's probability across the reasoning process—constructed by evaluating a probe at each generated token.

You can access the full paper at https://arxiv.org/abs/2605.18549.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "747b7342-4bee-4478-9619-6b22085b97e1",
  "isSidechain": false,
  "promptId": "1e462d9b-9458-4a67-ae07-9e2cab1e57dc",
  "type": "user",
  "uuid": "7630f11c-2efc-45ce-a871-56e5b76c6162",
  "toolUseResult": {
    "query": "Chrabąszcz probe trajectories monitoring internal monologue 2605.18549 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YJHJFWFb8pByQ33HiH1P5Q",
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
            "title": "Inner Monologue Statistics: 2026 Verified Report",
            "url": "https://wifitalents.com/inner-monologue-statistics/"
          },
          {
            "title": "Internal Monologue: Data Reports 2026",
            "url": "https://wifitalents.com/internal-monologue-statistics/"
          },
          {
            "title": "Spectroscopic Active Probes for Investigation of Lipid Transformation in Cells and Membranes | The Journal of Physical Chemistry B",
            "url": "https://pubs.acs.org/doi/10.1021/acs.jpcb.5c05981"
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
            "title": "Method, apparatus, and computer program product for anonymizing trajectories",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11662215"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper \"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics\" (arXiv:2605.18549) was submitted on May 18, 2026, with authors Maciej Chrabąszcz, Aleksander Szymczyk, Marcin Sendera, Tomasz Trzciński, and Sebastian Cygert.\n\nThe paper addresses Large Reasoning Models (LRMs) and their Chain of Thought (CoT) reasoning for safety monitoring. The research investigates hidden representations of LRMs to predict future behavior from prompt and CoT representations, using a probe trajectory—the continuous evolution of a concept's probability across the reasoning process—constructed by evaluating a probe at each generated token.\n\nYou can access the full paper at https://arxiv.org/abs/2605.18549."
    ],
    "durationSeconds": 5.499744040000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "747b7342-4bee-4478-9619-6b22085b97e1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-T…",
  "leafUuid": "7630f11c-2efc-45ce-a871-56e5b76c6162",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Measuring chain-of-thought faithfulness via temporal gaps",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4"
}
```

---

### Tool call

_source line 23 · 2026-05-20T04:36:18.403Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016BhXzxg5WcgFETdSmuQyQM`</summary>

```json
{
  "query": "CoT faithfulness benchmark FaithCoT-Bench ICLR 2026 causal mediation reasoning dual stream 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7630f11c-2efc-45ce-a871-56e5b76c6162",
  "isSidechain": false,
  "requestId": "req_011CbDCZJGXtT1yurUHoh5dv",
  "type": "assistant",
  "uuid": "c25c6e85-26a1-40bf-8ee7-4b049adaab2f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019KDRCkNDskQYUmgGwzzV4B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 701,
      "cache_read_input_tokens": 29356,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 701,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 29356,
          "cache_creation_input_tokens": 701,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 701
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

_source line 24 · 2026-05-20T04:36:25.186Z_

<details><summary>↩ Tool result · `toolu_016BhXzxg5WcgFETdSmuQyQM`</summary>

```text
Web search results for query: "CoT faithfulness benchmark FaithCoT-Bench ICLR 2026 causal mediation reasoning dual stream 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING","url":"https://arxiv.org/pdf/2510.04040"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2505.11839"},{"title":"FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2510.04040v1"},{"title":"[2510.04040] FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning","url":"https://arxiv.org/abs/2510.04040"},{"title":"FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning | OpenReview","url":"https://openreview.net/forum?id=lN3yKqqzF1"},{"title":"Reasoning Faithfulness","url":"https://akhil.bio/CoT"}]

Based on the search results, here's what I found about FaithCoT-Bench:

## FaithCoT-Bench Overview

FaithCoT-Bench is a unified benchmark for instance-level CoT unfaithfulness detection. The framework provides FINE-CoT, an expert-annotated collection of over 1,000 trajectories generated by four representative LLMs across four domains, including more than 300 unfaithful instances with fine-grained causes and step-level evidence.

## Key Findings on CoT Faithfulness

The research reveals several important observations about chain-of-thought reasoning:

- Plausibility signals alone are insufficient to distinguish faithful from unfaithful reasoning, and counterfactual-based methods are effective only when interventions target causally critical steps.

- CoT reasoning errors do not necessarily imply unfaithfulness - a CoT may contain incorrect reasoning steps yet remain faithful if it truthfully exposes the model's internal process.

## Evaluation Methods

The paper conducts a systematic evaluation of eleven representative detection methods spanning counterfactual, logit-based, and LLM-as-judge paradigms.

## Important Distinction

FaithCoT-Bench categorizes each CoT as faithful or unfaithful via expert annotation, finding that around 15–20% of correct answers are paired with unfaithful CoTs, and similarly many wrong answers are paired with faithful CoTs, showing that accuracy and faithfulness are partially independent axes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c25c6e85-26a1-40bf-8ee7-4b049adaab2f",
  "isSidechain": false,
  "promptId": "1e462d9b-9458-4a67-ae07-9e2cab1e57dc",
  "type": "user",
  "uuid": "71452b5f-cb17-4f07-9184-34f6be804aaf",
  "toolUseResult": {
    "query": "CoT faithfulness benchmark FaithCoT-Bench ICLR 2026 causal mediation reasoning dual stream 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BTJK2Gh2E9ateLCwfah8TV",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING",
            "url": "https://arxiv.org/pdf/2510.04040"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2505.11839"
          },
          {
            "title": "FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2510.04040v1"
          },
          {
            "title": "[2510.04040] FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/abs/2510.04040"
          },
          {
            "title": "FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=lN3yKqqzF1"
          },
          {
            "title": "Reasoning Faithfulness",
            "url": "https://akhil.bio/CoT"
          }
        ]
      },
      "Based on the search results, here's what I found about FaithCoT-Bench:\n\n## FaithCoT-Bench Overview\n\nFaithCoT-Bench is a unified benchmark for instance-level CoT unfaithfulness detection. The framework provides FINE-CoT, an expert-annotated collection of over 1,000 trajectories generated by four representative LLMs across four domains, including more than 300 unfaithful instances with fine-grained causes and step-level evidence.\n\n## Key Findings on CoT Faithfulness\n\nThe research reveals several important observations about chain-of-thought reasoning:\n\n- Plausibility signals alone are insufficient to distinguish faithful from unfaithful reasoning, and counterfactual-based methods are effective only when interventions target causally critical steps.\n\n- CoT reasoning errors do not necessarily imply unfaithfulness - a CoT may contain incorrect reasoning steps yet remain faithful if it truthfully exposes the model's internal process.\n\n## Evaluation Methods\n\nThe paper conducts a systematic evaluation of eleven representative detection methods spanning counterfactual, logit-based, and LLM-as-judge paradigms.\n\n## Important Distinction\n\nFaithCoT-Bench categorizes each CoT as faithful or unfaithful via expert annotation, finding that around 15–20% of correct answers are paired with unfaithful CoTs, and similarly many wrong answers are paired with faithful CoTs, showing that accuracy and faithfulness are partially independent axes."
    ],
    "durationSeconds": 6.780081621999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c25c6e85-26a1-40bf-8ee7-4b049adaab2f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T04:36:28.834Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011XRDS5csPQN24PMzSYDxcN`</summary>

```json
{
  "query": "\"information contribution gap\" OR \"dual stream\" probe causal faithfulness reasoning LLM temporal gap 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71452b5f-cb17-4f07-9184-34f6be804aaf",
  "isSidechain": false,
  "requestId": "req_011CbDCZzv2fmgps2fxWfp9h",
  "type": "assistant",
  "uuid": "f21a8a6e-c7c2-4fd0-8a49-00692c733f66",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EPtLCjR6USW4ct2sGAzgc6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 764,
      "cache_read_input_tokens": 30057,
      "output_tokens": 75,
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
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 30057,
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

_source line 26 · 2026-05-20T04:36:39.989Z_

<details><summary>↩ Tool result · `toolu_011XRDS5csPQN24PMzSYDxcN`</summary>

```text
Web search results for query: ""information contribution gap" OR "dual stream" probe causal faithfulness reasoning LLM temporal gap 2026"

Links: [{"title":"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures","url":"https://arxiv.org/html/2603.16475v1"},{"title":"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures | OpenReview","url":"https://openreview.net/forum?id=yfqHr7l2tG"},{"title":"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures","url":"https://arxiv.org/pdf/2603.16475"},{"title":"Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents","url":"https://arxiv.org/pdf/2601.02314"},{"title":"C2-Faith: Benchmarking LLM Judges for Causal and Coverage Faithfulness in Chain-of-Thought Reasoning","url":"https://arxiv.org/pdf/2603.05167"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf?id=1oGQCCmydB"}]

Based on my search results, I found several relevant papers from 2026 addressing causal faithfulness and reasoning in LLMs:

## Key Findings:

**"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures"** appears to be a prominent paper on this topic. The protocol reveals a systematic gap: while models rely on structures more than the original text (>60% consistency under interventions to original prompt), they fail to update under logically significant structural edits more than 50% of the time. Models are more faithful to their self-generated structures than to gold ones, and the study provides evidence that current LLMs treat intermediate structures as context rather than true mediators of decision making.

**"Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents"** (January 2026) addresses related concerns. The empirical evaluation reveals a persistent Faithfulness Gap and detects a widespread failure mode termed Causal Decoupling, where agents exhibit violation density up to 0.77 in factual and scientific domains.

**"C2-Faith: Benchmarking LLM Judges for Causal and Coverage Faithfulness in Chain-of-Thought Reasoning"** decomposes faithfulness into causal and coverage dimensions. Causality examines whether each reasoning step logically follows from preceding steps, while Coverage addresses whether critical intermediate inferences are actually present—capturing complementary failure modes.

These papers collectively investigate gaps between models' apparent reasoning faithfulness and actual causal dependence on their stated reasoning processes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f21a8a6e-c7c2-4fd0-8a49-00692c733f66",
  "isSidechain": false,
  "promptId": "1e462d9b-9458-4a67-ae07-9e2cab1e57dc",
  "type": "user",
  "uuid": "c17b5e72-f379-4838-a149-787d89731e09",
  "toolUseResult": {
    "query": "\"information contribution gap\" OR \"dual stream\" probe causal faithfulness reasoning LLM temporal gap 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0147Fs6qKNVDS3KqDxqJi8Hk",
        "content": [
          {
            "title": "Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures",
            "url": "https://arxiv.org/html/2603.16475v1"
          },
          {
            "title": "Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures | OpenReview",
            "url": "https://openreview.net/forum?id=yfqHr7l2tG"
          },
          {
            "title": "Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures",
            "url": "https://arxiv.org/pdf/2603.16475"
          },
          {
            "title": "Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents",
            "url": "https://arxiv.org/pdf/2601.02314"
          },
          {
            "title": "C2-Faith: Benchmarking LLM Judges for Causal and Coverage Faithfulness in Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/pdf/2603.05167"
          },
          {
            "title": "000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019",
            "url": "https://openreview.net/pdf?id=1oGQCCmydB"
          }
        ]
      },
      "Based on my search results, I found several relevant papers from 2026 addressing causal faithfulness and reasoning in LLMs:\n\n## Key Findings:\n\n**\"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures\"** appears to be a prominent paper on this topic. The protocol reveals a systematic gap: while models rely on structures more than the original text (>60% consistency under interventions to original prompt), they fail to update under logically significant structural edits more than 50% of the time. Models are more faithful to their self-generated structures than to gold ones, and the study provides evidence that current LLMs treat intermediate structures as context rather than true mediators of decision making.\n\n**\"Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents\"** (January 2026) addresses related concerns. The empirical evaluation reveals a persistent Faithfulness Gap and detects a widespread failure mode termed Causal Decoupling, where agents exhibit violation density up to 0.77 in factual and scientific domains.\n\n**\"C2-Faith: Benchmarking LLM Judges for Causal and Coverage Faithfulness in Chain-of-Thought Reasoning\"** decomposes faithfulness into causal and coverage dimensions. Causality examines whether each reasoning step logically follows from preceding steps, while Coverage addresses whether critical intermediate inferences are actually present—capturing complementary failure modes.\n\nThese papers collectively investigate gaps between models' apparent reasoning faithfulness and actual causal dependence on their stated reasoning processes."
    ],
    "durationSeconds": 11.149303883,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f21a8a6e-c7c2-4fd0-8a49-00692c733f66",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T04:36:42.799Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013fs9tiRZRzCiqiocQdpbWJ`</summary>

```json
{
  "query": "Thought Anchors 2506.19143 counterfactual importance reasoning CoT 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c17b5e72-f379-4838-a149-787d89731e09",
  "isSidechain": false,
  "requestId": "req_011CbDCb6CJQDGLyXWgfYr3k",
  "type": "assistant",
  "uuid": "6810b7e2-ced4-4c34-a4c3-628bae84c8d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GtUneQstZN7ZwNsRvaNw4Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 30821,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 805,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 30821,
          "cache_creation_input_tokens": 805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 805
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

_source line 28 · 2026-05-20T04:36:48.206Z_

<details><summary>↩ Tool result · `toolu_013fs9tiRZRzCiqiocQdpbWJ`</summary>

```text
Web search results for query: "Thought Anchors 2506.19143 counterfactual importance reasoning CoT 2025"

Links: [{"title":"[Literature Review] Thought Anchors: Which LLM Reasoning Steps Matter?","url":"https://www.themoonlight.io/en/review/thought-anchors-which-llm-reasoning-steps-matter"},{"title":"Thought Anchors: Which LLM Reasoning Steps Matter?","url":"https://www.alignmentforum.org/posts/iLHe3vLur3NgrFPFy/thought-anchors-which-llm-reasoning-steps-matter"},{"title":"[2506.19143] Thought Anchors: Which LLM Reasoning Steps Matter?","url":"https://arxiv.org/abs/2506.19143"},{"title":"Thought Anchors: Which LLM Reasoning Steps Matter?","url":"https://arxiv.org/html/2506.19143"},{"title":"Thought Anchors: Which LLM Reasoning Steps Matter? | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/thought-anchors-which-llm-reasoning-steps-matter"},{"title":"Under review as a conference paper at ICLR 2026 THOUGHT ANCHORS: WHICH LLM","url":"https://arxiv.org/pdf/2506.19143"},{"title":"GitHub - interp-reasoning/thought-anchors: ⚓️ Repository for the \"Thought Anchors: Which LLM Reasoning Steps Matter?\" paper.","url":"https://github.com/interp-reasoning/thought-anchors"},{"title":"AI Safety Diary: August 28, 2025 | Serhat Giydiren","url":"https://serhatgiydiren.com/ai-safety-diary-august-28-2025/"},{"title":"Thought Anchors in LLM Reasoning","url":"https://www.emergentmind.com/papers/2506.19143"},{"title":"Paper page - Thought Anchors: Which LLM Reasoning Steps Matter?","url":"https://huggingface.co/papers/2506.19143"}]

Based on the search results, here's what I found about the "Thought Anchors" paper (arXiv 2506.19143):

## Overview

The paper "Thought Anchors: Which LLM Reasoning Steps Matter?" introduces a sentence-level approach to understanding and interpreting chain-of-thought (CoT) reasoning in large language models (LLMs).

## Key Concepts

The paper introduces "thought anchors," key reasoning steps in chain-of-thought (CoT) processes that significantly influence subsequent reasoning.

## Methodology

The paper proposes three complementary attribution methods: (1) a black-box method measuring each sentence's counterfactual importance by comparing final answers across 100 rollouts; (2) a white-box method of aggregating attention patterns between pairs of sentences; (3) a causal attribution method measuring logical connections between sentences by suppressing attention toward one sentence.

## Counterfactual Importance Method

The counterfactual importance method measures each sentence's counterfactual importance by repeatedly sampling replacement sentences from the model, filtering for semantically different ones, and continuing the chain of thought from that point onwards to quantify the sentence's impact on the distribution of final answers.

## Key Findings

Plan generation and uncertainty management sentences consistently exhibit higher counterfactual importance than other categories, and these sentences, often related to backtracking, appear to anchor and steer the reasoning trajectory.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6810b7e2-ced4-4c34-a4c3-628bae84c8d1",
  "isSidechain": false,
  "promptId": "1e462d9b-9458-4a67-ae07-9e2cab1e57dc",
  "type": "user",
  "uuid": "2707a914-9042-4f65-a3d5-19743a10221d",
  "toolUseResult": {
    "query": "Thought Anchors 2506.19143 counterfactual importance reasoning CoT 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_012sYHhQbKbj16LQmSZ7oEfQ",
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
            "url": "https://arxiv.org/html/2506.19143"
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
            "title": "GitHub - interp-reasoning/thought-anchors: ⚓️ Repository for the \"Thought Anchors: Which LLM Reasoning Steps Matter?\" paper.",
            "url": "https://github.com/interp-reasoning/thought-anchors"
          },
          {
            "title": "AI Safety Diary: August 28, 2025 | Serhat Giydiren",
            "url": "https://serhatgiydiren.com/ai-safety-diary-august-28-2025/"
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
      "Based on the search results, here's what I found about the \"Thought Anchors\" paper (arXiv 2506.19143):\n\n## Overview\n\nThe paper \"Thought Anchors: Which LLM Reasoning Steps Matter?\" introduces a sentence-level approach to understanding and interpreting chain-of-thought (CoT) reasoning in large language models (LLMs).\n\n## Key Concepts\n\nThe paper introduces \"thought anchors,\" key reasoning steps in chain-of-thought (CoT) processes that significantly influence subsequent reasoning.\n\n## Methodology\n\nThe paper proposes three complementary attribution methods: (1) a black-box method measuring each sentence's counterfactual importance by comparing final answers across 100 rollouts; (2) a white-box method of aggregating attention patterns between pairs of sentences; (3) a causal attribution method measuring logical connections between sentences by suppressing attention toward one sentence.\n\n## Counterfactual Importance Method\n\nThe counterfactual importance method measures each sentence's counterfactual importance by repeatedly sampling replacement sentences from the model, filtering for semantically different ones, and continuing the chain of thought from that point onwards to quantify the sentence's impact on the distribution of final answers.\n\n## Key Findings\n\nPlan generation and uncertainty management sentences consistently exhibit higher counterfactual importance than other categories, and these sentences, often related to backtracking, appear to anchor and steer the reasoning trajectory."
    ],
    "durationSeconds": 5.398439775999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6810b7e2-ced4-4c34-a4c3-628bae84c8d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-20T04:36:48.209Z_

```json
{
  "parentUuid": "2707a914-9042-4f65-a3d5-19743a10221d",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1dd9c5ff-6e8f-4b2e-b545-751de8996a7c",
  "timestamp": "2026-05-20T04:36:48.209Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 30 · 2026-05-20T04:36:50.666Z_

Now let me do a couple more targeted searches to understand the competitive landscape better.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dd9c5ff-6e8f-4b2e-b545-751de8996a7c",
  "isSidechain": false,
  "requestId": "req_011CbDCbhJRadEkznirj8kyA",
  "type": "assistant",
  "uuid": "8c2203c5-618c-4d9c-9270-e8dd2042ddd3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012x32r3RaEMdWcKkHmKUbf9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1050,
      "cache_read_input_tokens": 31626,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1050,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 31626,
          "cache_creation_input_tokens": 1050,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1050
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

_source line 31 · 2026-05-20T04:36:51.336Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J8qemkecEKZ2catKAHckPt`</summary>

```json
{
  "query": "Cox 2603.01437 decoding answers before CoT probe steering failure reasoning models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c2203c5-618c-4d9c-9270-e8dd2042ddd3",
  "isSidechain": false,
  "requestId": "req_011CbDCbhJRadEkznirj8kyA",
  "type": "assistant",
  "uuid": "1c300a52-4e5c-4231-8f89-9f2af4704b1f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012x32r3RaEMdWcKkHmKUbf9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1050,
      "cache_read_input_tokens": 31626,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1050,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 31626,
          "cache_creation_input_tokens": 1050,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1050
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

_source line 32 · 2026-05-20T04:36:57.658Z_

<details><summary>↩ Tool result · `toolu_01J8qemkecEKZ2catKAHckPt`</summary>

```text
Web search results for query: "Cox 2603.01437 decoding answers before CoT probe steering failure reasoning models"

Links: [{"title":"[2603.01437] Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/abs/2603.01437"},{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/html/2603.01437"},{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/pdf/2603.01437"},{"title":"[Literature Review] Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://www.themoonlight.io/en/review/decoding-answers-before-chain-of-thought-evidence-from-pre-cot-probes-and-activation-steering"},{"title":"Post-Hoc Reasoning in Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering | OpenReview","url":"https://openreview.net/forum?id=UMUYpeXtJQ"}]

Based on the search results, here's what I found about the arXiv paper 2603.01437:

## Overview

The paper "Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering" by Kyle Cox, Darius Kianersi, and Adrià Garriga-Alonso investigates whether large language models' chain-of-thought reasoning truly reflects their decision process.

## Key Findings

The paper provides mechanistic evidence that instruction-tuned models often determine their answer before generating CoT. 

The researchers used two main approaches:

1. **Pre-CoT Probes**: By training linear probes on residual stream activations at the last token before CoT, they can predict the model's final answer with 0.9 AUC on most tasks.

2. **Activation Steering**: The probe directions are not only predictive, but also causal: steering activations along the probe direction flips model answers in over 50% of cases, significantly exceeding orthogonal baselines.

## Failure Modes

When steering induces incorrect answers, two distinct failure modes are observed: non-entailment (stating correct premises but drawing unsupported conclusions) and confabulation (fabricating false premises).

The paper was submitted on March 2, 2026, and examines this phenomenon across multiple instruction-tuned models on various reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c300a52-4e5c-4231-8f89-9f2af4704b1f",
  "isSidechain": false,
  "promptId": "1e462d9b-9458-4a67-ae07-9e2cab1e57dc",
  "type": "user",
  "uuid": "8a45fc3a-f39d-432e-b562-832ebc73d585",
  "toolUseResult": {
    "query": "Cox 2603.01437 decoding answers before CoT probe steering failure reasoning models",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GbS3hJDi6AMrZ8oe2D3BZB",
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
            "title": "[Literature Review] Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering",
            "url": "https://www.themoonlight.io/en/review/decoding-answers-before-chain-of-thought-evidence-from-pre-cot-probes-and-activation-steering"
          },
          {
            "title": "Post-Hoc Reasoning in Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering | OpenReview",
            "url": "https://openreview.net/forum?id=UMUYpeXtJQ"
          }
        ]
      },
      "Based on the search results, here's what I found about the arXiv paper 2603.01437:\n\n## Overview\n\nThe paper \"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering\" by Kyle Cox, Darius Kianersi, and Adrià Garriga-Alonso investigates whether large language models' chain-of-thought reasoning truly reflects their decision process.\n\n## Key Findings\n\nThe paper provides mechanistic evidence that instruction-tuned models often determine their answer before generating CoT. \n\nThe researchers used two main approaches:\n\n1. **Pre-CoT Probes**: By training linear probes on residual stream activations at the last token before CoT, they can predict the model's final answer with 0.9 AUC on most tasks.\n\n2. **Activation Steering**: The probe directions are not only predictive, but also causal: steering activations along the probe direction flips model answers in over 50% of cases, significantly exceeding orthogonal baselines.\n\n## Failure Modes\n\nWhen steering induces incorrect answers, two distinct failure modes are observed: non-entailment (stating correct premises but drawing unsupported conclusions) and confabulation (fabricating false premises).\n\nThe paper was submitted on March 2, 2026, and examines this phenomenon across multiple instruction-tuned models on various reasoning tasks."
    ],
    "durationSeconds": 6.317958864,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1c300a52-4e5c-4231-8f89-9f2af4704b1f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T04:37:00.821Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FT7mgoSnHk457zv24S1mdb`</summary>

```json
{
  "query": "CMI causal mediation index Sathyanarayanan 2602.03994 causal bypass reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a45fc3a-f39d-432e-b562-832ebc73d585",
  "isSidechain": false,
  "requestId": "req_011CbDCcPpjeMsZWXTs58HMg",
  "type": "assistant",
  "uuid": "8e455071-bed8-4888-9797-cf8909a12c95",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KZmBY5jYgoV58sTLJwf5Qq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 766,
      "cache_read_input_tokens": 32676,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 766,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 32676,
          "cache_creation_input_tokens": 766,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 766
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

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-T…",
  "leafUuid": "8e455071-bed8-4888-9797-cf8909a12c95",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Measuring chain-of-thought faithfulness via temporal gaps",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4"
}
```

---

### Tool result

_source line 36 · 2026-05-20T04:37:08.047Z_

<details><summary>↩ Tool result · `toolu_01FT7mgoSnHk457zv24S1mdb`</summary>

```text
Web search results for query: "CMI causal mediation index Sathyanarayanan 2602.03994 causal bypass reasoning 2026"

Links: [{"title":"[2602.03994] When Chains of Thought Don't Matter: Causal Bypass in Large Language Models","url":"https://arxiv.org/abs/2602.03994"},{"title":"Causal Bypass in Large Language Models","url":"https://www.arxiv.org/pdf/2602.03994"},{"title":"When Chains of Thought Don’t Matter: Causal Bypass in Large Language Models","url":"https://arxiv.org/html/2602.03994"},{"title":"The Stata Journal (2011) 11, Number 4, pp. 605–619 Causal mediation analysis","url":"https://journals.sagepub.com/doi/pdf/10.1177/1536867X1201100407"},{"title":"Identification of causal direct-indirect effects without untestable   assumptions","url":"https://arxiv.org/pdf/2009.12528"},{"title":"A general approach to causal mediation analysis","url":"https://pubmed.ncbi.nlm.nih.gov/20954780/"},{"title":"Statistical Mediation Analysis for Models with a Binary Mediator and a Binary Outcome: the Differences Between Causal and Traditional Mediation Analysis","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9108123/"}]

Based on the search results, I found relevant information about the paper you're looking for:

The paper "When Chains of Thought Don't Matter: Causal Bypass in Large Language Models" is authored by Anish Sathyanarayanan, Aditya Nagarsekar, and Aarush Rathore, and it was posted on February 3, 2026.

The central finding is that even when chain-of-thought (CoT) is verbose, strategic, and flagged by surface-level manipulation detectors, model answers are often causally independent of the CoT content. The paper presents a diagnostic framework that includes a causal probe measuring CoT-mediated influence (CMI) via hidden-state patching and reports a bypass score (1−CMI), quantifying the degree to which the answer is produced by a bypass circuit independent of the rationale.

In pilot evaluations, audit-aware prompting increases detectable manipulation signals, yet causal probes reveal task-dependent mediation: many QA items exhibit near-total bypass (CMI ≈ 0), while some logic problems show stronger mediation (CMI up to 0.56).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e455071-bed8-4888-9797-cf8909a12c95",
  "isSidechain": false,
  "promptId": "1e462d9b-9458-4a67-ae07-9e2cab1e57dc",
  "type": "user",
  "uuid": "f2c98022-1fb9-4d64-92d6-082c5b3eecfc",
  "toolUseResult": {
    "query": "CMI causal mediation index Sathyanarayanan 2602.03994 causal bypass reasoning 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DKWdTNcRUCfJL8Ny13tEYb",
        "content": [
          {
            "title": "[2602.03994] When Chains of Thought Don't Matter: Causal Bypass in Large Language Models",
            "url": "https://arxiv.org/abs/2602.03994"
          },
          {
            "title": "Causal Bypass in Large Language Models",
            "url": "https://www.arxiv.org/pdf/2602.03994"
          },
          {
            "title": "When Chains of Thought Don’t Matter: Causal Bypass in Large Language Models",
            "url": "https://arxiv.org/html/2602.03994"
          },
          {
            "title": "The Stata Journal (2011) 11, Number 4, pp. 605–619 Causal mediation analysis",
            "url": "https://journals.sagepub.com/doi/pdf/10.1177/1536867X1201100407"
          },
          {
            "title": "Identification of causal direct-indirect effects without untestable   assumptions",
            "url": "https://arxiv.org/pdf/2009.12528"
          },
          {
            "title": "A general approach to causal mediation analysis",
            "url": "https://pubmed.ncbi.nlm.nih.gov/20954780/"
          },
          {
            "title": "Statistical Mediation Analysis for Models with a Binary Mediator and a Binary Outcome: the Differences Between Causal and Traditional Mediation Analysis",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9108123/"
          }
        ]
      },
      "Based on the search results, I found relevant information about the paper you're looking for:\n\nThe paper \"When Chains of Thought Don't Matter: Causal Bypass in Large Language Models\" is authored by Anish Sathyanarayanan, Aditya Nagarsekar, and Aarush Rathore, and it was posted on February 3, 2026.\n\nThe central finding is that even when chain-of-thought (CoT) is verbose, strategic, and flagged by surface-level manipulation detectors, model answers are often causally independent of the CoT content. The paper presents a diagnostic framework that includes a causal probe measuring CoT-mediated influence (CMI) via hidden-state patching and reports a bypass score (1−CMI), quantifying the degree to which the answer is produced by a bypass circuit independent of the rationale.\n\nIn pilot evaluations, audit-aware prompting increases detectable manipulation signals, yet causal probes reveal task-dependent mediation: many QA items exhibit near-total bypass (CMI ≈ 0), while some logic problems show stronger mediation (CMI up to 0.56)."
    ],
    "durationSeconds": 7.222401466000011,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8e455071-bed8-4888-9797-cf8909a12c95",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T04:37:10.854Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CskoLNX3KcSRmm5nR4HAZb`</summary>

```json
{
  "query": "Wang 2604.15726 \"LLM reasoning is latent\" H1 H2 hypothesis reasoning faithfulness 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2c98022-1fb9-4d64-92d6-082c5b3eecfc",
  "isSidechain": false,
  "requestId": "req_011CbDCdAAEXYi2znXhNrLgo",
  "type": "assistant",
  "uuid": "90983320-7cfc-497e-b832-0122a523886b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZCwQkNsi9Dee5A2SDKMHf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 733,
      "cache_read_input_tokens": 33442,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 733,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 33442,
          "cache_creation_input_tokens": 733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 733
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

_source line 38 · 2026-05-20T04:37:16.689Z_

<details><summary>↩ Tool result · `toolu_01CskoLNX3KcSRmm5nR4HAZb`</summary>

```text
Web search results for query: "Wang 2604.15726 "LLM reasoning is latent" H1 H2 hypothesis reasoning faithfulness 2026"

Links: [{"title":"[2604.15726] LLM Reasoning Is Latent, Not the Chain of Thought","url":"https://arxiv.org/abs/2604.15726"},{"title":"LLM Reasoning Is Latent, Not the Chain of Thought","url":"https://arxiv.org/html/2604.15726"},{"title":"Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing","url":"https://arxiv.org/pdf/2604.08401"},{"title":"A Comprehensive Survey on Trustworthiness in Reasoning with Large Language Models","url":"https://arxiv.org/html/2509.03871v1"},{"title":"A CAUSAL ANALYSIS OF LLM FAITHFULNESS TO ...","url":"https://openreview.net/pdf/ad24ecf6de7a98b8765c4d43ac9cc793d585260f.pdf"},{"title":"Worries about latent reasoning in LLMs — EA Forum","url":"https://forum.effectivealtruism.org/posts/sNkua636jSni6Jftt/worries-about-latent-reasoning-in-llms"},{"title":"Measuring Faithfulness in Chain-of-Thought Reasoning","url":"https://arxiv.org/pdf/2307.13702"}]

Based on the search results, I found the paper you're looking for:

The paper "LLM Reasoning Is Latent, Not the Chain of Thought" (arXiv:2604.15726) argues that large language model reasoning should be studied as latent-state trajectory formation rather than as faithful surface chain-of-thought (CoT).

The paper formalizes three competing hypotheses: H1, reasoning is primarily mediated by latent-state trajectories; H2, reasoning is primarily mediated by explicit surface CoT; and H0, most apparent reasoning gains are better explained by generic serial compute than by any privileged representational object.

The paper emphasizes that this matters because claims about faithfulness, interpretability, reasoning benchmarks, and inference-time intervention all depend on what the field takes the primary object of reasoning to be.

The paper was authored by Wenshuo Wang from the School of Future Technology at South China University of Technology and was published on April 17, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90983320-7cfc-497e-b832-0122a523886b",
  "isSidechain": false,
  "promptId": "1e462d9b-9458-4a67-ae07-9e2cab1e57dc",
  "type": "user",
  "uuid": "88165120-202a-434b-bd81-4ea4b7dcde7d",
  "toolUseResult": {
    "query": "Wang 2604.15726 \"LLM reasoning is latent\" H1 H2 hypothesis reasoning faithfulness 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HZNg5p7LmQSwybmhdtuKh6",
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
            "title": "Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing",
            "url": "https://arxiv.org/pdf/2604.08401"
          },
          {
            "title": "A Comprehensive Survey on Trustworthiness in Reasoning with Large Language Models",
            "url": "https://arxiv.org/html/2509.03871v1"
          },
          {
            "title": "A CAUSAL ANALYSIS OF LLM FAITHFULNESS TO ...",
            "url": "https://openreview.net/pdf/ad24ecf6de7a98b8765c4d43ac9cc793d585260f.pdf"
          },
          {
            "title": "Worries about latent reasoning in LLMs — EA Forum",
            "url": "https://forum.effectivealtruism.org/posts/sNkua636jSni6Jftt/worries-about-latent-reasoning-in-llms"
          },
          {
            "title": "Measuring Faithfulness in Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/pdf/2307.13702"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper \"LLM Reasoning Is Latent, Not the Chain of Thought\" (arXiv:2604.15726) argues that large language model reasoning should be studied as latent-state trajectory formation rather than as faithful surface chain-of-thought (CoT).\n\nThe paper formalizes three competing hypotheses: H1, reasoning is primarily mediated by latent-state trajectories; H2, reasoning is primarily mediated by explicit surface CoT; and H0, most apparent reasoning gains are better explained by generic serial compute than by any privileged representational object.\n\nThe paper emphasizes that this matters because claims about faithfulness, interpretability, reasoning benchmarks, and inference-time intervention all depend on what the field takes the primary object of reasoning to be.\n\nThe paper was authored by Wenshuo Wang from the School of Future Technology at South China University of Technology and was published on April 17, 2026."
    ],
    "durationSeconds": 5.831235486000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "90983320-7cfc-497e-b832-0122a523886b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-20T04:39:16.958Z_

Now I have sufficient context to provide a thorough assessment. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [Chrabąszcz et al., arXiv 2605.18549](https://arxiv.org/abs/2605.18549) (May 2026): 最直接的竞争工作。60+ signal-processing features on probe trajectories, 91-97% AUROC。但完全没有 causal component——这正是本 proposal 声称要填补的空白。该工作发表仅 2 天前（5月18日），说明该领域极度活跃。
- [Yuan et al., arXiv 2605.09502](https://arxiv.org/abs/2605.09502) (May 2026): 核心 empirical foundation。证明 probe 可诊断但 4 种 causal intervention 全部失败，"diagnostic not causal"。本 proposal 将该发现从 obstacle 重新定义为 phenomenon，立意精准。
- [Cox et al., arXiv 2603.01437](https://arxiv.org/abs/2603.01437) (March 2026): Pre-CoT probes predict answer with >0.9 AUC; steering works on instruction-tuned but fails on reasoning models。独立验证了 diagnostic-causal gap。
- [Ballon et al., arXiv 2601.23163](https://arxiv.org/abs/2601.23163) (Jan 2026): Truncation-reinjection protocol providing behavioral C(t) curves。本 proposal 直接采用其方法作为 C(t) estimator 之一。
- [FaithCoT-Bench, ICLR 2026](https://arxiv.org/abs/2510.04040): 1000+ expert-annotated trajectories, 11 detection methods。已被接收为 ICLR 2026 conference paper。本 proposal 将其作为 external validation 和 comparison baseline。
- [Wang, arXiv 2604.15726](https://arxiv.org/abs/2604.15726) (April 2026): 形式化 H1 (latent-mediated) vs H2 (CoT-mediated) 假设。本 proposal 声称 ICG 可 operationalize 该区分。
- [CMI / Sathyanarayanan et al., arXiv 2602.03994](https://arxiv.org/abs/2602.03994) (Feb 2026): Causal bypass via hidden-state patching, ~50 examples, structural mediation。本 proposal 正确区分了 structural vs functional faithfulness。
- [Thought Anchors, arXiv 2506.19143](https://arxiv.org/abs/2506.19143) (June 2025): Per-sentence counterfactual importance via 100-rollout replacement。Within-CoT causal analysis 但无 probe reference。
- [Kudo et al., EACL 2026](https://arxiv.org/abs/2412.01113): 最接近的先驱——per-position probes + activation patching，但限于 synthetic arithmetic。
- [TTS / Zhao et al., arXiv 2510.24941](https://arxiv.org/abs/2510.24941): Per-step marginal ATE, only 2.3% AIME steps TTS≥0.7。提供 marginal causal contribution 但无 probe 维度。

- 调研总结: CoT faithfulness 是 2025-2026 年 interpretability/alignment 领域最活跃的方向之一，已有大量 probe-only 和 causal-only 的工作，但确实没有已发表工作将 probe trajectories 与 causal contribution 统一到一个 temporal gap framework 中。该 proposal 的 niche（dual-stream temporal gap）在文献中确实是空白。但该领域极度拥挤且快速移动，window of opportunity 非常窄。

【整体印象】:
作为审稿人，我的第一反应是：这是一个 **极其 well-researched、positioning 精准的分析型 proposal**，对领域理解极深，literature coverage 几乎无遗漏。核心直觉——"将 diagnostic-causal gap 本身作为研究对象，而非视其为障碍"——是一个真正有洞察力的 reframing。

但我同时有几个严重担忧：
1. **Framework 复杂度过高**：ICG 涉及 P*(t)（多层 probe + null calibration + MCT concordance）和 C(t)（3种 estimator + aggregation + normalization），加上 7 个 ablation 维度、5 个模型、4 个 benchmark。这对一篇 8 页论文来说信息密度过大，有沦为"measurement study"的风险。
2. **核心 contribution 的 novelty 边界模糊**：ICG 本质上是"用已有方法 A 的输出减去已有方法 B 的输出"。P*(t) 来自 Chrabąszcz/David/Zhang 等的 probe 方法，C(t) 来自 Ballon/TTS/NLDD。创新点在于 combination + temporal gap analysis，但 reviewer 可能质疑这是否是"trivial combination"。Proposal 自己预见了这个 objection 并给出了 cumulative vs marginal 的论证，但说服力取决于 empirical results。
3. **Shape-based classification 的可靠性**：将 faithfulness phenomena 分类寄托于 G*(t) trajectory shapes（constant-high vs convergence vs widening），但 Phase 0b 的 success criterion 是 d > 0.5 between partitions。如果 d < 0.5，proposal 预注册降级为 characterization paper——这说明作者自己也不确定核心 claim 是否成立。

倾向：**borderline accept**。如果实验结果强，有 accept 的可能；如果 Phase 0b 的 effect sizes 不够强或分类只有 2 categories，可能掉到 weak reject。

【核心贡献】:
1. 首次提出 dual-stream temporal gap framework (ICG)，将 probe-based information availability 和 causal contribution 统一到时间轴上，能够区分 faithful-correct 和 unfaithful-correct reasoning。
2. G*(t) trajectory shape 作为 phenomenon fingerprint 的概念，可以 operationalize Wang 的 H1/H2 区分。
3. Difficulty-conditioned gap analysis，回答"在什么难度下 CoT 从 decorative 过渡到 load-bearing"。
4. 对 reasoning utilization efficiency 的实用意义（early-exit、benchmark validity、safety monitoring）。

价值评估：如果 empirical results 强（d > 0.5，3 categories separable），这是一个高价值的 diagnostic tool，对 interpretability 和 alignment 社区有实质性贡献。如果 results 弱，价值降为"又一个 measurement framework"。

【方法合理性】:
方法在逻辑上是合理的——分别测量 information availability 和 causal contribution 然后计算 gap——但有几个 concerns：

1. **P*(t) 和 C(t) 的可比性**：Proposal 承认两者"measured via fundamentally different methods with non-commensurable scales"，并采用 rank-based normalization。但 rank normalization 会丢失 magnitude 信息，而 proposal 又声称 shapes 才是关键。这个 tension 是否真的被 resolved 值得审视。
2. **C(t) 的 aggregation**：三种 estimator（prefix truncation, paraphrase, NLDD）测量的是不同的东西——cumulative sufficiency、content independence、positional degradation。将它们 aggregate 的理论依据不够强。Young (2603.20172) 已证明不同 faithfulness metrics 之间 kappa 可低至 0.06，说明 aggregation 可能掩盖而非增强信号。
3. **更简单的替代方案**：直接用 Chrabąszcz 的 probe trajectory features + Ballon 的 truncation accuracy，不做 gap 计算，而是做 multi-feature classification，可能达到类似甚至更好的效果。Proposal 需要证明 gap formulation 提供了超越 simple feature concatenation 的 insight。

【5 维度打分】:

1. 研究问题: [强] — "模型知道答案但 CoT 并未使用这个知识"是 2025-2026 年被多组独立验证的核心现象（Yuan et al., Cox et al., Esakkiraja et al.）。将 diagnostic-causal gap 本身作为研究对象而非障碍是一个有价值的 reframing。FaithCoT-Bench (ICLR 2026) 已确认 15-20% correct answers 配对 unfaithful CoTs，验证了问题的实际存在。这个问题对 AI safety（monitoring hidden reasoning）和 efficiency（early-exit compute）都有直接影响。

2. 方法与创新: [中] — ICG 的 novelty 在于 combination 和 temporal gap formulation，而非底层方法（probe 来自多组前人工作，C(t) 来自 Ballon/TTS/NLDD）。与 Chrabąszcz et al. (2605.18549) 相比，ICG 增加了 causal 维度；与 CMI (2602.03994) 相比，ICG 是 functional 而非 structural。区分是清晰的，但 reviewer 可能质疑 gap = P*(t) - C(t) 是否比 feature concatenation 更有信息量。Proposal 对 cumulative vs marginal 的论证（对标 TTS vs Ballon）是一个合理的 preemption，但最终需要 empirical 支撑。Kudo et al. (EACL 2026) 已在 synthetic data 上做了 probe + causal combination，ICG 的增量在于 natural benchmarks + temporal gap formulation。

3. 实验设计: [强] — 这是 proposal 最出色的部分。Phase 0a/0b 的 go/no-go 设计非常成熟；external validation 通过 difficulty partition 和 TTS cross-reference（而非仅依赖 P*/C 自身的 partition）是方法论上的亮点；7 维 ablation 覆盖了几乎所有合理的 robustness concern；head-to-head 比较 probe-only、TTS-only、FaithCoT-Bench 方法提供了清晰的 contribution 量化。5 models × 4 benchmarks（含 instruction-tuned control 作 sanity check）的规模对分析型工作来说充分。与 Young (2603.20172) 的 measurement sensitivity 发现直接对话（报告 inter-estimator kappa）也是加分项。唯一的 concern 是规模可能导致论文过于 dense。

4. 可行性: [中] — ~1050 H100-hours 和 15-17 周在学术组可行但不轻松。主要风险在于：(a) NLDD 在 32B 上的 250 hrs bottleneck 且 Phase 0a 可能判其不可行；(b) paraphrase perturbation 的 API cost（$800-1500）和质量控制；(c) 3-5 TB hidden state 存储需要 engineering。好的方面是 Phase 0a 的早期 go/no-go 设计降低了 sunk cost 风险。如果 NLDD 在 Phase 0a 被 gated out，C(t) 只剩两个 estimator，可能削弱 robustness claim。

5. 写作与呈现: [中] — Proposal 的 literature positioning 极其精准，每个 related work 的区分都有清晰论证。但写作上存在几个问题：(a) 信息过载——一篇 8 页论文要呈现 dual-stream framework + 3 C(t) estimators + 7 ablation + 5 models × 4 benchmarks + difficulty conditioning + TIF score + classification + head-to-head + 671B subset + MCT supplementary + semi-synthetic simulation，几乎不可能在有限篇幅内清晰呈现；(b) framing 偏向 measurement framework，缺少 actionable insight 的前置承诺（beyond "we can classify phenomena"，so what？）；(c) phenomenon taxonomy 的 honest scoping（2 vs 3 categories）虽然诚实但也传递了不确定性。

【概率估计】: [28% - 42%] 中位 35%

【估计理由】:
上界理由 (42%): 如果 Phase 0b 验证成功（d > 0.5, 3 categories separable），shape-based classification 显著优于 probe-only 和 TTS-only baselines，且论文成功聚焦核心 contribution 而非 exhaustive ablation，这将是一篇 solid 的 analysis paper。研究问题的 timeliness（2025-2026 最热话题之一）和实验设计的 rigor 是明确加分项。EMNLP 历来接收高质量的 analysis/interpretability 工作。

下界理由 (28%): (1) 最大风险是 novelty 争议——"已有方法 A 的输出减已有方法 B 的输出"可能被 reviewer 视为 incremental combination 而非 fundamental contribution；(2) 如果 Phase 0b effect sizes 不强或 phenomenon taxonomy 坍缩为 2 categories，核心 claim 被削弱；(3) 论文信息密度过高可能导致关键 insight 被淹没；(4) 该领域极度拥挤且快速移动（Chrabąszcz 5月18日才出，Thought Anchors 6月出），在 submission 前可能出现更直接的竞争工作。

中位 35%: 方向正确、实验设计 solid、但 novelty 有争议性且 execution risk 不低。属于"如果结果强则有希望，但需要 empirical results 来证明 gap formulation 的 added value"的 proposal。

【主要风险】:
1. **Novelty 被质疑为 trivial combination**: 审稿人可能认为 ICG = probe trajectory (existing) + causal measurement (existing) 的简单拼接，gap subtraction 不构成足够的方法论创新。Proposal 预见了这一点并给出了 cumulative vs marginal 论证，但如果 ablation 显示 feature concatenation（不做 gap）效果类似或更好，核心 claim 就不成立。
2. **Phenomenon classification 结果弱**: 如果 G*(t) trajectory shapes 在不同 faithfulness phenomena 之间没有足够大的 effect size（d < 0.5），或 3-category 分类坍缩为 2-category，论文从"diagnostic framework"降级为"characterization study"，显著降低 impact。在这个竞争激烈的领域，一篇"我们看了这个 gap 但它没有特别能区分什么"的论文很难被接收。

【实施评估】:
  - 计算资源: ~1050 H100-hours (~$3,200)，中等规模，学术组可负担但需要稳定 GPU 集群。NLDD 32B (250 hrs) 是单项最大开销，Phase 0a 可 gate。
  - 数据需求: 使用现有公开 benchmark（GSM8K, MATH-500, GPQA-Diamond, AIME），无需构建新数据集。FaithCoT-Bench 的 instance-level labels 如可获取将显著增强 validation。
  - 人工介入: 低。Probe training、C(t) estimation、classification 均可自动化。Paraphrase 需要 NLI-based 质量验证。主要人工投入在实验设计和论文写作。
  - 训练需求: 轻量级——仅训练 linear probes 和浅层 classifiers（LR/RF/MLP），不涉及 LLM fine-tuning。
  - 新 Benchmark: 不需要。TIF score 作为 derived metric 但不构成独立 benchmark。
  - 预估周期: 15-17 周（2 researchers）/ 14 周（1 researcher + Claude）。Phase 0b 在第 4 周提供 early go/no-go。整体 timeline 紧凑但可行。
```

Sources:
- [Monitoring the Internal Monologue: Probe Trajectories (Chrabąszcz et al.)](https://arxiv.org/abs/2605.18549)
- [Hidden Error Awareness (Yuan et al.)](https://arxiv.org/abs/2605.09502)
- [Decoding Answers Before CoT (Cox et al.)](https://arxiv.org/abs/2603.01437)
- [Probing the Trajectories of Reasoning Traces (Ballon et al.)](https://arxiv.org/abs/2601.23163)
- [FaithCoT-Bench (ICLR 2026)](https://arxiv.org/abs/2510.04040)
- [LLM Reasoning Is Latent (Wang)](https://arxiv.org/abs/2604.15726)
- [When Chains of Thought Don't Matter: Causal Bypass / CMI](https://arxiv.org/abs/2602.03994)
- [Thought Anchors](https://arxiv.org/abs/2506.19143)
- [Breaking the Chain (Somov et al.)](https://arxiv.org/abs/2603.16475)
- [Measuring Faithfulness Depends on How You Measure (Young)](https://arxiv.org/abs/2603.20172)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88165120-202a-434b-bd81-4ea4b7dcde7d",
  "isSidechain": false,
  "requestId": "req_011CbDCdo6jPLfa6a4Qq5bN7",
  "type": "assistant",
  "uuid": "4f75b2e7-4eef-430f-8acd-45a037ab427e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q4VZYtUJKGNFae7gQauNsd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 34175,
      "output_tokens": 4913,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 699,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4913,
          "cache_read_input_tokens": 34175,
          "cache_creation_input_tokens": 699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 699
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

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-T…",
  "leafUuid": "4f75b2e7-4eef-430f-8acd-45a037ab427e",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Measuring chain-of-thought faithfulness via temporal gaps",
  "sessionId": "d2fe3289-ab28-432b-9391-57de9a76f3e4"
}
```

---
