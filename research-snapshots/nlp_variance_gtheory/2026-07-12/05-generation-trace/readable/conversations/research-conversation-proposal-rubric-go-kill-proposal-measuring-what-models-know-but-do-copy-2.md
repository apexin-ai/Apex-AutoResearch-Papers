# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Measuring What Models Know But Do

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-3/9f054eab-0d77-4538-b834-27b44a1162e3.jsonl`
- **Structured JSON:** [`db06963a9a3fc20a46a7.json`](../../sessions/db/db06963a9a3fc20a46a7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:35:22.764Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:35:22.764Z",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness\n\n## Description\nWhen a reasoning model gets the right answer, is its chain-of-thought the reason it succeeded — or did it already know the answer and generate decorative reasoning? No existing method can answer this question. Probe-only approaches (Chrabąszcz et al., 2605.18549) reveal what the model knows over time but are structurally blind to whether CoT caused the correct output. Causal-only approaches (TTS, Zhao et al. 2510.24941; NLDD, Ye et al. 2602.11201; Ballon et al. 2601.23163) measure what CoT does but cannot assess what the model already knew internally. Only a dual-stream framework — jointly tracking information availability AND causal contribution — can distinguish faithful-correct from unfaithful-correct reasoning. The Information-Contribution Gap (ICG) framework provides this.\n\nICG exploits a robust empirical finding: linear probes on hidden states reliably diagnose answer correctness (0.82-0.95 AUROC across four independent groups) yet causal interventions based on these probes consistently fail on reasoning-trained models (Cox et al. 2603.01437: negligible flip rates; Yuan et al. 2605.09502: all four intervention strategies fail). Rather than treating this diagnostic-causal gap as an obstacle, we make it the primary object of study.\n\nThe framework tracks two calibrated time-varying quantities across the CoT trajectory: P*(t), null-probe-calibrated correctness awareness, and C(t), causal contribution estimated via three complementary methods (prefix truncation following Ballon et al.'s three control conditions, paraphrase perturbation, NLDD). Their divergence G*(t) = P*(t) − C(t) produces phenomenon-specific temporal fingerprints, operationalizing Wang's (2604.15726) H1/H2 distinction: G*(t) >> 0 is latent-mediated (H1-consistent), G*(t) ≈ 0 is CoT-mediated (H2-consistent).\n\n**Core insight: the diagnostic contribution of G*(t) is its temporal trajectory shape, not its absolute magnitude.** P*(t) (probe AUROC) and C(t) (behavioral accuracy change) are measured via fundamentally different methods with non-commensurable scales. We address this via rank-based normalization as primary scheme, but more fundamentally, trajectory-shape profiles carry the diagnostic signal: a model that pre-encodes the answer shows a constant-high shape; genuine reasoning shows convergence toward zero; post-hoc rationalization shows widening. The shapes-over-magnitudes approach is validated by: entropy trajectory monotonicity predicting reliability regardless of absolute levels (+5.8pp, arXiv 2603.18940); RQA temporal features outperforming aggregates (36.94% vs. 28.97%, arXiv 2602.06266); Microsoft trajectory geometry achieving 0.852 AUC from shape features vs. 0.649 baseline (arXiv 2604.05655).\n\n**Why not just endpoint comparison or trivial combination?** Two reviewer objections are preempted: (1) \"Why not correlate pre-CoT probe accuracy with final correctness?\" — endpoint comparison detects unfaithfulness presence but collapses distinct failure *mechanisms* (pre-CoT encoding vs. rationalization vs. late shortcutting produce identical endpoints but distinct G*(t) shapes). (2) \"Why not just pair Chrabąszcz's probe trajectories with TTS step scores?\" — TTS measures *marginal* contribution (removing step *s* changes the answer), while prefix-truncation C(t) measures *cumulative sufficiency* (CoT[:t] is sufficient for correctness). A chain where every individual step has low TTS (each individually replaceable) could still have high cumulative C(t) (the ensemble is necessary). This cumulative-vs-marginal distinction is theoretically non-reducible and empirically grounded in the difference between Ballon et al.'s monotonic prefix curves and TTS's per-step ATE.\n\n**Structural vs. functional differentiation from CMI.** The CMI framework (Sathyanarayanan et al., 2602.03994) measures whether answer representations pass through CoT-aligned layers via layerwise activation patching — a *structural* question. ICG answers a *functional* question: does the CoT text causally contribute to behavioral correctness? This generates a testable prediction: models could show high CMI (representations routed through CoT-processing layers) but high G*(t) (CoT serves as timing scaffold rather than contributing semantic content). If confirmed, this would reveal a novel structural-functional dissociation in reasoning models.\n\n**Differentiation from Thought Anchors.** Thought Anchors (arXiv 2506.19143) measures per-sentence counterfactual importance via replacement sampling — identifying sentences with outsized causal influence on reasoning trajectory. This provides *within-CoT structural analysis* (which sentences matter to each other) but no *external reference* to the model's internal state. A thought anchor could be causally critical within the CoT but entirely redundant relative to what the model already knows — a distinction only ICG can make via the probe dimension.\n\n**Interpretive boundary.** G*(t) >> 0 means correctness-correlated information is present but not causally channeled through CoT. It does not entail the model \"decided to withhold\" — the information may exist as computational byproducts rather than semantically actionable knowledge. Chun et al.'s MCT geometric pulse finding (2602.20338) provides evidence of this possibility. We report interpretations with this caveat.\n\n**Practical significance: reasoning utilization efficiency.** G*(t) provides a unified diagnostic for reasoning utilization: G*(t) ≈ 0 means full utilization (knowledge channeled through CoT); G*(t) >> 0 means waste (CoT is decorative overhead); G*(t) < 0 means productive computation (CoT assembles new information). This framing connects to three practical domains: (a) *inference-time compute allocation* — skip CoT generation when G*(t) >> 0 for easy problems, providing the principled diagnostic that current early-exit heuristics (ESTAR, DTSR, FRIT, CoDE-Stop) lack; (b) *benchmark validity* — problems where all models show persistent G*(t) >> 0 are not testing reasoning; (c) *safety monitoring* — the decoupled internal quality-monitoring system (Yuan et al.) is the kind of hidden computation alignment researchers worry about.\n\nWe adopt honest scoping: 2-3 faithfulness phenomena as the realistic classification target, with steganographic encoding and reasoning theater as stretch goals. The boundary between pre-CoT encoding and post-hoc rationalization may be empirically blurred (in both cases, the model may have committed to an answer before CoT begins, so P*(t) starts high in both), potentially collapsing the taxonomy to 2 primary categories (pre-committed vs. genuinely reasoning). Phase 0b explicitly tests 2-category vs. 3-category separability; either outcome is a strong contribution. Task-difficulty conditioning — grounded in David's easy (0.84) vs. hard (0.76) probe splits and Gjølbye et al.'s (2605.15454) domain-specific difficulty-geometry coupling (ρ⊥ = +0.41 on Codeforces) — reveals the decorative→load-bearing transition with length correction.\n\nCore contributions: (a) calibrated ICG diagnostic with shape-based trajectory analysis on 5 models (4 reasoning + 1 instruction-tuned control) × 4 benchmarks, the first framework capable of distinguishing faithful-correct from unfaithful-correct reasoning; (b) empirical pilot with external validation (TTS cross-reference, difficulty partition, FaithCoT-Bench supplementary) demonstrating 2-3 distinguishable G*(t) phenomenon signatures; (c) difficulty-conditioned gap analysis with domain-specific nuance; (d) head-to-head comparison against TTS, FaithCoT-Bench methods, and probe-only trajectories. Total compute: ~1050 H100-hours.\n\n## Core Problem\nA striking convergence of 2025-2026 findings reveals a fundamental disconnect in reasoning language models: their hidden states reliably encode information about answer correctness — linear probes achieving 0.82-0.95 AUROC across multiple independent groups — yet causal interventions based on these probes consistently fail to influence model outputs. Cox et al. (2603.01437) find steering via answer-content probes produces answer flip rates 'negligible against the orthogonal baseline' on reasoning models, despite >0.9 AUC on instruction-tuned models. Yuan et al. (2605.09502) systematically test four interventions (activation steering, probe-guided best-of-N, self-correction, activation patching) on models up to 72B and report ALL fail. This diagnostic-causal gap is NOT an obstacle; it IS the central phenomenon.\n\nThe literature conflates two probe targets: answer-content probes (Cox et al.: specific answer on binary tasks, ≤9B + GPT-OSS-20B) and correctness probes (Yuan et al.: right/wrong on models up to 72B; Zhang et al. 2504.05419: per-chunk correctness on 7B-70B). Answer-content gaps mean 'the model has decided but CoT doesn't derive the answer'; correctness gaps mean 'the model knows it's right/wrong but CoT doesn't reflect this awareness.'\n\nTemporal dynamics are empirically grounded: David (2511.14773) finds probe accuracy at 0.84 AUC by token 4, stable ~0.8 through token 100, with easy (0.84) vs. hard (0.76) splits. Zhang et al. (2504.05419) report 65%→79% chunk trajectories on R1-Distill. Esakkiraja et al. (2604.01202) find >90% pre-generation AUROC with characteristic dip at 5-10%. Chrabąszcz et al. (2605.18549) demonstrate 60+ signal-processing features achieving up to 17pp over static probes. Yet no framework jointly tracks information availability AND causal contribution: Chrabąszcz et al. lack any causal component; Ballon et al. (2601.23163) provide behavioral C(t) but no hidden-state measurement; CMI (2602.03994) provides structural layerwise audit on ~50 examples but measures representation routing, not functional text contribution; TTS provides per-step marginal causal contribution but no probe-side measurement and no cumulative sufficiency assessment; Thought Anchors (2506.19143) provide within-CoT causal structure but no external probe reference.\n\n## Opportunity\n(1) **Temporal gap measurement.** Multiple groups have independently built the measurement components — probe trajectories (Chrabąszcz: 60+ features, 91-97% AUROC; David: per-token; Zhang: per-chunk; Yuan: 0.95 overall; Esakkiraja: >90% pre-generation) and behavioral causal curves (Ballon: truncation-reinjection; TTS: per-step ATE; NLDD: per-position degradation) — but no one has unified them into a dual-stream temporal gap. Chrabąszcz et al. are structurally blind to the faithful-correct vs. unfaithful-correct distinction; Ballon et al. lack hidden-state measurement. The gap between these traditions IS the framework's niche.\n\n(2) **Phenomenon unification with honest scoping.** CoT faithfulness failures are studied in isolation: Reasoning Horizon (Ye et al. 2602.11201), pre-CoT encoding (Cox et al.; Esakkiraja et al.), Reasoning Theater (Boppana et al. 2603.05488), myopic planning (Xu et al. 2602.02103). We propose 2-3 are distinguishable via G*(t) trajectory shapes, honestly pre-registering that pre-CoT encoding and rationalization may collapse to a single \"pre-committed\" category.\n\n(3) **Task-difficulty conditioning.** ICLR 2026 Workshop finding, Li et al. (2510.22362): easy→decorative, hard→faithful. Gjølbye et al. (2605.15454): difficulty-geometry coupling domain-specific (ρ⊥ = +0.41 code, +0.05 math). ICG answers: at what difficulty does CoT transition from decorative to load-bearing?\n\n(4) **Probe target clarification.** First principled treatment contrasting correctness awareness gap vs. answer-content gap on applicable tasks.\n\nTwo prior works combine probing with causal intervention: Kudo et al. (EACL 2026, 2412.01113) on synthetic arithmetic, and CMI (2602.03994) on ~50 examples — CMI measures *structural mediation* (representation routing through layers) while ICG measures *functional contribution* (whether CoT text causally contributes to behavioral correctness). Wang (2604.15726) formalizes H1/H2/H0 hypotheses; ICG operationalizes the H1/H2 distinction empirically. Neither Kudo et al. nor CMI provides: (a) temporal coverage on natural benchmarks, (b) phenomenon mapping, (c) instance-level diagnostic, (d) multi-model comparison across model families, (e) robustness validation per Young's (2603.20172) classifier-sensitivity finding (kappa as low as 0.06), or (f) empirical pilot with external validation standards.\n\n## Landscape\n**Probe-based temporal measurement (P*(t) foundation).** Chrabąszcz et al. (2605.18549): probe trajectories with 60+ signal-processing features (volatility, trend, steady-state, boundary transients, autocorrelation) via 3-layer MLP + Multi-Instance Learning. Max-pooling: 91-97% AUROC harmfulness (vs. 33-61% average-pooling); up to 17pp over static on GSM8K across Llama-8B-R1-Distill and Qwen3-4B/8B/14B (~3000 GPU-hours). Critical: (a) NO causal component, (b) NO gap metric, (c) NO calibration, (d) NO faithfulness-mode taxonomy, (e) NO difficulty conditioning, (f) structurally cannot distinguish faithful-correct from unfaithful-correct. David (2511.14773): 0.84 AUC at t=4, stable ~0.8, easy/hard 0.84/0.76 on Qwen3-8B. Zhang et al. (2504.05419): 0.82-0.91 AUROC on GSM8K/MATH/AIME, 65%→79% trajectory, 24% token reduction via early-exit. Yuan et al. (2605.09502): 0.95 AUROC on Qwen-3B, 0.852 on R1-7B, 0.787 first-step, concealment gap 0.197 AUROC. Esakkiraja et al. (2604.01202): >90% pre-generation, dip at 5-10%, recovery to near-100%. Cox et al. (2603.01437): answer-content probes >0.9 AUC on instruction-tuned Gemma-2/Qwen-2.5, negligible flip on reasoning GPT-OSS-20B. Additional: Qian et al. (2506.02867, NeurIPS 2025); Lewis-Lim et al. (2508.19827, EMNLP 2025); Mirtaheri & Belkin (2603.17199); Occhipinti et al. (ICLR 2026 LIT Workshop).\n\n**Diagnostic-not-causal evidence.** Yuan et al. (2605.09502): four interventions all fail on Qwen2.5 (1.5B-72B), Llama-3.1-8B, Phi-3.5-mini, DeepSeek-R1-7B. 'The error signal is a diagnostic readout, not a causal component that can be edited.' Cox et al. independently confirm. Probe accuracy ≠ causal potency on reasoning models.\n\n**Behavioral C(t) measurement.** Ballon et al. (2601.23163): truncation-reinjection on Qwen3-4B/8B/14B and gpt-oss-20B/120B, decile intervals. Accuracy: 30.8-42.3% → 49.0-73.1% on GPQA-Diamond. Controls validate sequential content (intact +18.1-33.1% vs. shuffled +0.3-10.8%). Disclaims faithfulness analysis. Zhao et al. (2510.24941, TTS): per-step ATE on R1-Distill-Qwen-7B/14B/Llama-8B, only 2.3% AIME steps TTS≥0.7. Ye et al. (2602.11201, NLDD): Reasoning Horizon at 70-85% on synthetic tasks (natural benchmark generalizability unvalidated). Thought Anchors (2506.19143): per-sentence counterfactual importance via 100-rollout replacement sampling; identifies \"anchor\" sentences steering reasoning trajectory — provides within-CoT causal structure but no probe reference for assessing redundancy relative to internal state. Basu & Chakraborty (2603.22816): decorative/scaffolding/genuine taxonomy. FACT-E (Sun et al. 2604.10693, ACL Findings 2026).\n\n**Probe-intervention combinations.** Kudo et al. (2412.01113, EACL 2026): per-position probes + activation patching on synthetic arithmetic, 9 models. CMI (2602.03994): layerwise activation patching on Phi/Qwen/DialoGPT, ~50 examples. CMI measures *structural mediation* (representation routing); ICG measures *functional contribution* (behavioral text causation). Both complementary precursors on small/synthetic samples.\n\n**Latent-reasoning theory.** Wang (2604.15726): H1/H2/H0 hypotheses with compute-audited designs. ICG operationalizes H1/H2 distinction.\n\n**Temporal hidden-state dynamics.** Gjølbye et al. (2605.15454): 11 models, 3 domains, length correction. ρ⊥^D = +0.41 Codeforces vs. −0.06 baselines; weaker on MATH (+0.05). Prompt-stage probes don't mirror generation-time dynamics. Furuya & Tanimura (2605.01853, StALT). Herrmann et al. (2605.09159): internal polylogue dynamics. Li et al. (2510.22362, NeurIPS 2025 MechInterp Workshop, Concept Walk): easy→decorative, hard→faithful. Vilas et al. (2510.10494, ICLR 2026): 14-70% token savings.\n\n**Probe calibration.** Hewitt & Liang (EMNLP 2019): 4.5 selectivity. Ravichander et al. (2005.00719): properties recoverable when unused. Voita & Titov (EMNLP 2020, 2003.12298): MDL probing. Chun et al. (2602.20338, MCT): geometric pulse — separability peaks transiently while probe accuracy persists. Validates null-probe calibration need.\n\n**Trajectory-shape analysis.** Entropy trajectories (2603.18940): +5.8pp from monotonicity. RQA (2602.06266): temporal 36.94% vs. aggregates 28.97%. Microsoft (2604.05655): 0.852 vs. 0.649 AUC.\n\n**Measurement sensitivity.** Young (2603.20172): kappa as low as 0.06, up to 30.6pp divergence. Young (2603.26410). 'Lie to Me' (2603.22582).\n\n**Additional.** Internal States Before Wait (2510.04128). From Reasoning to Answer (2509.23676). FaithCoT-Bench (ICLR 2026, 2510.04040): 1000+ expert-annotated trajectories, 11 methods, 4 paradigms. Jin et al. survey (ARR for ACL 2026). Liu et al. (2602.13904). Reasoning Theater (2603.05488). Early-exit: ESTAR, DTSR, NEAT, CoDE-Stop, FRIT (Swaroop et al., 2509.13334). Breaking the Chain (Somov et al., 2603.16475). Step-Level Hallucination (Alvarez & Baheri, 2605.13772). SAE Reasoning Features (2503.18878). Solution Hides in Hidden States (2604.23351). Knowing Before Saying (ACL Findings 2025, 2505.24362). LEACE (Belrose et al., NeurIPS 2023, 2306.03819). CoT Monitorability (Anwar et al., 2602.18297). Understanding CoT via Information Theory (Ton et al., ICML 2025, 2411.11984).\n\n**What remains open.** No framework provides: (1) dual-stream temporal gap enabling faithful-vs-unfaithful discrimination for correct instances; (2) empirically-validated phenomenon taxonomy with external validation; (3) instance-level diagnostic from temporal gap; (4) difficulty-conditioned gap with domain nuance; (5) head-to-head comparison against existing causal faithfulness methods; (6) instruction-tuned vs. reasoning model control comparison within the same framework.\n\n## Approach\n**Formal Framework.** Two time-varying quantities at equally-spaced positions (primary: 20-50 percentile-based positions; token-level supplementary on subsets):\n\n(i) *P*(t)*: Cross-validated AUROC of linear probe on layer-l hidden states, calibrated via null-probe (P*(t) = P(t) − P_null(t), Hewitt & Liang 2019). Shared probe evaluated at each position (following Chrabąszcz's per-token evaluation, avoiding per-position training). **Target: correctness (right/wrong)** — broader applicability than answer-content probes, directly tied to the diagnostic-not-causal finding (Yuan et al.), more interpretable for faithfulness. Supplementary answer-content probes on binary/MC subsets. Probed at layers L/4, L/2, 3L/4, L. MCT (Chun et al. 2602.20338) supplementary concordance on 500 examples: if MCT capacity diverges from P*(t), identifies positions where probe signal may reflect retrievability rather than geometrically organized information.\n\n(ii) *C(t)*: Three estimators aggregated into C_agg(t): (a) **Prefix truncation** — Ballon et al.'s (2601.23163) protocol with three controls (random, swapped, shuffled tokens), measuring P(correct | CoT[:t]) vs. P(correct | full CoT). This measures *cumulative sufficiency* — whether CoT up to position t is sufficient for correctness — which is theoretically distinct from per-step *marginal contribution* (TTS); (b) **Paraphrase perturbation** — sentence-level segments paraphrased by external model (Claude Haiku or GPT-4o-mini for cost efficiency), 2-3 variants per segment, NLI-based semantic preservation verification. Answer stability: P(same answer | paraphrased CoT). Protocol follows FaithCoT-Bench (ICLR 2026) paraphrasing paradigm. Applied to stratified subset (~40% of examples per cell) for cost control, with full prefix truncation on all examples; (c) **NLDD** (Ye et al. 2602.11201, conditional on Phase 0a feasibility) — logit degradation under corruption. Sentence-level segmentation aligned with TTS approach (Zhao et al.). Multiple estimators provide robustness per Young's (2603.20172) classifier-sensitivity finding.\n\n**C(t) Aggregation and Gap Normalization.** Primary: rank-based normalization — each estimator converted to instance-level percentile ranks within model-benchmark cell, then combined. If NLDD underperforms on specific benchmarks (Phase 0a), two-estimator C_agg(t) (prefix + paraphrase) is primary for those benchmarks; three-estimator as supplementary. Ablation reports: (a) per-estimator G*(t) for phenomenon classification; (b) inverse-variance weighting vs. equal-weight; (c) pairwise Spearman correlation and Cohen's kappa between estimators. Diagnostic value lies in trajectory shapes, not magnitudes, so normalization affects scale but not shape-based signatures.\n\n**G*(t) = P*(t) − C(t).** Primary signal:\n- G*(t) ≈ 0: Aligned (necessary for faithfulness; H2-consistent per Wang 2604.15726)\n- G*(t) >> 0: Diagnostic excess — 'knows but doesn't use' (H1-consistent)\n- G*(t) < 0: Information assembled during reasoning\n\n**Interpretive caveat.** G*(t) >> 0 indicates correctness-correlated information not causally channeled through CoT, but does not entail intentional withholding — some signals may be computational byproducts rather than actionable knowledge. MCT concordance provides partial validation of this boundary.\n\n**Phenomenon Predictions (honestly scoped).**\n*Primary (HIGH confidence):*\n(i) *Pre-committed reasoning* (encompasses pre-CoT encoding and potentially post-hoc rationalization): G*(t) starts high, stays high or widens. P*(t) high from start (David: 0.84 at t=4; Esakkiraja: >90% pre-generation; Cox: >0.9 pre-CoT), C(t) low or flat.\n(ii) *Genuine multi-step reasoning*: G*(t) converges toward zero. P*(t) rises gradually, C(t) tracks P*(t). Zhang et al.'s 65%→79%, Li et al.'s hard→faithful, Ballon et al.'s monotonic accuracy increase.\n\n*Secondary (MODERATE confidence — Phase 0b tests whether separable from pre-committed):*\n(iii) *Post-hoc rationalization as distinct from pre-CoT encoding*: If distinguishable, the separation should manifest primarily in C(t) dynamics (rationalization may show spurious partial C(t) increases as the model crafts locally-consistent reasoning, while pre-CoT encoding shows flat-zero C(t)) rather than P*(t). Phase 0b explicitly tests 2-category vs. 3-category separability; 2-category (pre-committed vs. genuine) is pre-registered as an acceptable outcome.\n\n*Stretch (require additional features):*\n(iv) *Steganographic encoding*: Dip-and-recovery, consistent with Esakkiraja's 5-10% dip.\n(v) *Reasoning Theater*: May overlap with pre-committed. Chrabąszcz-style features may enable separation. Reported with confusion matrices.\n\n**Semi-Synthetic Simulation (hypothesis generation, NOT validation).** Constructed from published data (David, Zhang, Esakkiraja, Yuan for probes; NLDD, TTS for causal; Chun et al. MCT for inflation). Real validation in Phase 0b.\n\n**Phase 0a: Gap Characterization + NLDD Feasibility (Weeks 1-2.5).** 500 examples × 3 datasets (GSM8K, MATH-500, MMLU) × 3 models (DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct):\n(i) Construct P*(t) and C(t) curves at 20-50 position resolution\n(ii) Validate null-probe calibration\n(iii) Characterize causal potency (Cox et al. protocol: steering on reasoning vs. instruction-tuned)\n(iv) **NLDD feasibility**: 7B × 100 examples on GSM8K (clear steps) + MMLU (ambiguous steps). If SNR uninformative on MMLU, restrict NLDD to math/code or replace with TTS-style perturbation. Cost: <10 GPU-hrs; gates 250+ hrs NLDD investment.\n\n**Phase 0b: Empirical Pilot (Weeks 2.5-4).** R1-Distill-Qwen-7B × GSM8K + MATH-500, 1000 examples.\n\n*Primary validation (external standards):*\n(i) **Difficulty-only partition**: model-independent difficulty bins (easy/medium/hard), no P*/C features used. Test G*(t) shape differences: d > 0.5 AND p < 0.01 (Bonferroni-corrected) on 2+ trajectory features.\n(ii) **TTS cross-reference** (primary external validation): compute Zhao et al.'s TTS on same examples; test whether high-TTS (genuine reasoning) vs. low-TTS (decorative) produce distinguishable G*(t) shapes.\n(iii) **2-category vs. 3-category test**: explicitly test whether pre-CoT encoding and post-hoc rationalization are separable or collapse to single \"pre-committed\" category.\n(iv) **FaithCoT-Bench** (supplementary): if instance-level overlap available, test correlation with expert labels; otherwise dataset-level validation.\n\n*Supplementary*: P*/C-based partition as self-consistency check.\nLength correction per Gjølbye et al. (2605.15454). Success: d > 0.5 between 2+ externally-defined partitions. If d < 0.3, downscope to characterization paper.\n\n**Phase 1: Full ICG (Weeks 4-9).** Conditional on Phase 0b d > 0.5. **5 models**: DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Llama-8B, DeepSeek-R1-Distill-Qwen-14B, QwQ-32B (reasoning models spanning 2 architecture families) + Qwen2.5-7B-Instruct (instruction-tuned control — expected G*(t) ≈ 0 as sanity check). **4 benchmarks**: GSM8K (500 examples), MATH-500 (500), GPQA-Diamond (~198 full), AIME (~90 full). Per-cell: ~1288 examples × 5 models. Full calibrated P*(t) + MCT supplementary + three C(t) estimators (NLDD conditional, paraphrase on ~40% stratified subset) + Ballon-style controls. Cross-reference with TTS at step boundaries. Bootstrap 95% CI on G*(t). ~250 H100-hours.\n\n**Phase 2: Difficulty Conditioning (Weeks 7-11).** Difficulty quintiles per benchmark. G*(t) per quintile. Expected: easy → persistent gap, hard → converging gap. Length correction; domain-specific reporting (stronger on math/code per Gjølbye et al.'s ρ⊥ = +0.41 code vs. +0.05 math).\n\n**Phase 3: Classification, Baselines, Robustness (Weeks 9-14).**\n\n*Classification framework:* G*(t) features (initial value, slope, convergence rate, dC/dt locality) + Chrabąszcz-style features (volatility, trend, boundary transients, autocorrelation). Classifier gradient: logistic regression → RF → MLP; report all. Metric: macro-F1 (primary) + confusion matrix + reliability diagram. Validation: 5-fold + cross-model (train A → test B, reporting within-family vs. cross-family separately) + cross-benchmark generalization. Paired permutation tests with Bonferroni correction for all head-to-head comparisons.\n\n*Baselines:* (a) Random + majority-class; (b) Difficulty-only classifier; (c) **Probe-trajectory-only** (Chrabąszcz-style P*(t) features, no C(t)) — \"no causal dimension\" ablation; (d) **TTS-only** — per-step marginal causal contribution without probe dimension.\n\n*Head-to-head TIF validation:* TIF score vs. FaithCoT-Bench detection methods (Adding Mistakes, Removing Steps, Early Answering, Paraphrasing) and TTS on overlapping examples, comparing instance-level correlation with ground truth.\n\n*Robustness ablations (7 dimensions):* (a) probe architecture (linear vs. 2-layer MLP); (b) layer selection; (c) C(t) estimator agreement + per-estimator performance + weighting schemes; (d) gap normalization (rank vs. min-max vs. z-score); (e) calibration method (shuffled-label vs. random-representation); (f) probe target (correctness vs. answer-content); (g) **temporal resolution** (5/10/20/35/50 positions + token-level — reporting resolution vs. macro-F1 curve and saturation point).\n\n**TIF Score.** Normalized area under calibrated G*(t), benchmarked against FaithCoT-Bench and Liu et al.'s (2602.13904) text-level metrics.\n\n**Paper Focus.** Core contributions: (1) ICG diagnostic — first framework distinguishing faithful-correct from unfaithful-correct reasoning via dual-stream temporal gap, with instruction-tuned control validating the framework; (2) Phase 0b pilot with external validation demonstrating 2-3 distinguishable G*(t) signatures (or honestly reporting 2-category outcome); (3) difficulty-conditioned gap revealing decorative→load-bearing transition; (4) head-to-head showing ICG's value over probe-only, TTS-only, and FaithCoT-Bench methods. Supporting: 7-dimension ablations; TIF validation. Supplementary: 671B subset (500 examples, 3 layers); answer-content vs. correctness comparison; semi-synthetic simulation; CMI structural-functional prediction if resources allow.\n\n**Experiments.** DeepSeek-R1-Distill-Qwen-7B/14B, DeepSeek-R1-Distill-Llama-8B, QwQ-32B, Qwen2.5-7B-Instruct across GSM8K, MATH-500, GPQA-Diamond, AIME. 671B validation (500-example subset). Calibration: synthetic arithmetic (G* ≈ 0 expected), TTS cross-reference, MCT supplementary. Gjølbye-style length correction throughout.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '~1050 H100-hours (Phase 0a: 90 hrs [3 models × 3 datasets + NLDD feasibility]; Phase 0b: 30 hrs [pilot]; Phase 1: 250 hrs [5 models × 4 benchmarks, probes + 3 C(t) estimators + controls]; Phase 2: 50 hrs [difficulty conditioning]; Phase 3: 70 hrs [classification + 7-dim ablations + baselines]; NLDD 32B conditional: 250 hrs [primary bottleneck]; NLDD 7B/14B: 100 hrs; MCT supplementary: 50 hrs; 671B subset: 50 hrs [8×H100]; semi-synthetic: 30 hrs; paraphrase model: ~80 hrs inference on target models for stability checks)', 'paraphrase_api_cost': '~$800-1500 (Claude Haiku/GPT-4o-mini on stratified ~40% subset, 2-3 variants)', 'timeline': '15-17 weeks (2 researchers)', 'estimated_gpu_cost': '$3,200 at ~$3/H100-hour', 'storage': '3-5 TB (4 layers, fp16); ~1.5 TB with PCA/on-the-fly'}, 'human_in_loop': {'gpu_hours': '~1050 H100-hours', 'timeline': '14 weeks (1 researcher + Claude)', 'claude_api_cost': '$500 (experiment design) + $800-1500 (paraphrase generation)', 'estimated_gpu_cost': '$3,200'}, 'auto_research': {'gpu_hours': '~1050 H100-hours', 'timeline': '12 weeks', 'claude_api_cost': '$900 + $800-1500 (paraphrase)', 'estimated_gpu_cost': '$3,200', 'speed_bottleneck': 'NLDD on 32B (~250 hrs, conditional on Phase 0a) is primary bottleneck. Phase 0b pilot (30 hrs) provides early go/no-go.'}}\n\n## Inspired By\nThe convergence of five independent lines of evidence — (a) Cox et al.'s steering failure on reasoning models despite high probe accuracy; (b) Yuan et al.'s four-intervention failure establishing 'diagnostic not causal'; (c) temporal probe dynamics (David, Zhang, Esakkiraja, Chrabąszcz: 60+ features, up to 17pp improvement); (d) Ballon et al.'s truncation-reinjection demonstrating monotonic behavioral C(t) with controls; (e) trajectory-shape literature (arXiv 2603.18940, 2602.06266, 2604.05655) showing shapes carry diagnostic information — all pointing to: the gap between diagnostic availability and causal contribution IS the phenomenon, and its temporal shape reveals the mechanism. Additionally: Wang's (2604.15726) H1/H2/H0; Gjølbye et al.'s (2605.15454) domain-specific coupling; Chun et al.'s (2602.20338) MCT geometric pulse; CMI's (2602.03994) structural mediation; Thought Anchors' (2506.19143) within-CoT causal structure.\n\n## Target Venues\n- ICLR 2027 (abstract: Sep 19, full paper: Sep 24, 2026; primary target)\n- ICML 2027 (full paper: Jan 29, 2027; fallback)\n\n## Key References\n- Monitoring the Internal Monologue: Probe Trajectories (Chrabąszcz et al., arXiv 2605.18549)\n- Probing the Trajectories of Reasoning Traces (Ballon et al., arXiv 2601.23163)\n- LLM Reasoning Is Latent (Wang, arXiv 2604.15726)\n- Reasoning Models Move Differently (Gjølbye et al., arXiv 2605.15454)\n- Hidden Error Awareness (Yuan et al., arXiv 2605.09502)\n- Decoding Answers Before CoT (Cox et al., arXiv 2603.01437)\n- Temporal Predictors of Outcome (David, arXiv 2511.14773)\n- Reasoning Models Know When They're Right (Zhang et al., arXiv 2504.05419)\n- Therefore I am. I Think (Esakkiraja et al., arXiv 2604.01202)\n- True Thinking Score (Zhao et al., arXiv 2510.24941)\n- Mechanistic Evidence for Faithfulness Decay / NLDD (Ye et al., arXiv 2602.11201)\n- Internal Polylogue (Herrmann et al., arXiv 2605.09159)\n- Faithfully Compute Answers During CoT (Kudo et al., EACL 2026, arXiv 2412.01113)\n- Causal Bypass / CMI (Sathyanarayanan et al., arXiv 2602.03994)\n- StALT (Furuya & Tanimura, arXiv 2605.01853)\n- Concept Walk (Li et al., arXiv 2510.22362, NeurIPS 2025 MechInterp Workshop)\n- Task Difficulty Shapes CoT Faithfulness (ICLR 2026 Workshop)\n- Diagnosing Pathological CoT (Liu et al., arXiv 2602.13904)\n- Measuring Faithfulness Depends on How You Measure (Young, arXiv 2603.20172)\n- MCT / Emergent Manifold Separability (Chun et al., arXiv 2602.20338)\n- Latent Temporal Signals (Vilas et al., ICLR 2026, arXiv 2510.10494)\n- Probing and Steering CoT Unfaithfulness (Occhipinti et al., ICLR 2026 LIT Workshop)\n- Designing and Interpreting Probes (Hewitt & Liang, EMNLP 2019)\n- Information-Theoretic Probing with MDL (Voita & Titov, EMNLP 2020, arXiv 2003.12298)\n- Probing the Probing Paradigm (Ravichander et al., arXiv 2005.00719)\n- Entropy trajectory shapes (arXiv 2603.18940)\n- RQA of Reasoning Dynamics (arXiv 2602.06266)\n- LLM Reasoning as Trajectories (arXiv 2604.05655, Microsoft)\n- Internal States Before Wait (arXiv 2510.04128)\n- FACT-E (Sun et al., ACL Findings 2026, arXiv 2604.10693)\n- Breaking the Chain (Somov et al., arXiv 2603.16475)\n- The Illusion of Reasoning (Basu & Chakraborty, arXiv 2603.22816)\n- FaithCoT-Bench (ICLR 2026, arXiv 2510.04040)\n- The Mirage of Explainability survey (Jin et al., ARR for ACL 2026)\n- Reasoning Theater (Boppana et al., arXiv 2603.05488)\n- No Global Plan in CoT (Xu et al., arXiv 2602.02103)\n- Catching Rationalization in the Act (Mirtaheri & Belkin, arXiv 2603.17199)\n- CoT Monitorability (Anwar et al., arXiv 2602.18297)\n- Understanding CoT via Information Theory (Ton et al., ICML 2025, arXiv 2411.11984)\n- Demystifying Reasoning Dynamics (Qian et al., NeurIPS 2025, arXiv 2506.02867)\n- Analysing CoT Dynamics (Lewis-Lim et al., EMNLP 2025, arXiv 2508.19827)\n- Why Models Know But Don't Say (Young, arXiv 2603.26410)\n- Lie to Me (arXiv 2603.22582)\n- Step-Level Hallucination (Alvarez & Baheri, arXiv 2605.13772)\n- From Reasoning to Answer (arXiv 2509.23676)\n- SAE Reasoning Features (arXiv 2503.18878)\n- FRIT (Swaroop et al., arXiv 2509.13334)\n- Solution Hides in Hidden States (arXiv 2604.23351)\n- Knowing Before Saying (ACL Findings 2025, arXiv 2505.24362)\n- LEACE (Belrose et al., NeurIPS 2023, arXiv 2306.03819)\n- Thought Anchors (arXiv 2506.19143)"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T04:35:22.767Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:35:22.767Z",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3"
}
```

---

## Round 1

44 recorded events

### User

_source line 3 · 2026-05-20T04:35:22.779Z_

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
  "promptId": "91ae5899-f812-4435-ba43-3aeb1b84ea98",
  "type": "user",
  "uuid": "23adf1ec-1964-4934-913c-813a3ee9599a",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:35:22.777Z_

```json
{
  "parentUuid": "23adf1ec-1964-4934-913c-813a3ee9599a",
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
  "uuid": "96a1e5ab-e42f-4069-8218-c0d7c0de3c3d",
  "timestamp": "2026-05-20T04:35:22.777Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:35:22.777Z_

```json
{
  "parentUuid": "96a1e5ab-e42f-4069-8218-c0d7c0de3c3d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c9cc6d63-0eec-4cae-baa6-846037b625ee",
  "timestamp": "2026-05-20T04:35:22.777Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
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
  "leafUuid": "c9cc6d63-0eec-4cae-baa6-846037b625ee",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Temporal information-contribution gap analysis for reasoning faithfulness",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3"
}
```

---

### Assistant

_source line 8 · 2026-05-20T04:35:30.035Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this proposal carefully. It's about measuring Chain-of-Thought (CoT) faithfulness in reasoning models by combining probe-based information availability with causal contribution measurements. I need to do thorough research on the current state of this field before making my assessment.

Let me start by searching for the key related works and the current landscape.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9cc6d63-0eec-4cae-baa6-846037b625ee",
  "isSidechain": false,
  "requestId": "req_011CbDCVQ89QQreMKo4a1WZ8",
  "type": "assistant",
  "uuid": "23e2afb3-e70b-46dd-b594-bb0009b397c1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EqsGeEn6WVDsE5aokBzLkc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14678,
      "cache_read_input_tokens": 11374,
      "output_tokens": 191,
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
          "output_tokens": 191,
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

_source line 9 · 2026-05-20T04:35:30.079Z_

I'll begin by conducting thorough field research before making any assessment. Let me search for the key topics in this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23e2afb3-e70b-46dd-b594-bb0009b397c1",
  "isSidechain": false,
  "requestId": "req_011CbDCVQ89QQreMKo4a1WZ8",
  "type": "assistant",
  "uuid": "d6915e4e-2b80-41de-a53a-02359fdc1295",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EqsGeEn6WVDsE5aokBzLkc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14678,
      "cache_read_input_tokens": 11374,
      "output_tokens": 191,
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
          "output_tokens": 191,
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

_source line 10 · 2026-05-20T04:35:30.186Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EtE4B1JqRjdAen1Kc3bG1L`</summary>

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
  "parentUuid": "d6915e4e-2b80-41de-a53a-02359fdc1295",
  "isSidechain": false,
  "requestId": "req_011CbDCVQ89QQreMKo4a1WZ8",
  "type": "assistant",
  "uuid": "ea2e6203-5836-4822-aa11-2c51a3d0012d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EqsGeEn6WVDsE5aokBzLkc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14678,
      "cache_read_input_tokens": 11374,
      "output_tokens": 191,
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
          "output_tokens": 191,
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

_source line 11 · 2026-05-20T04:35:30.192Z_

<details><summary>↩ Tool result · `toolu_01EtE4B1JqRjdAen1Kc3bG1L`</summary>

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
  "parentUuid": "ea2e6203-5836-4822-aa11-2c51a3d0012d",
  "isSidechain": false,
  "promptId": "91ae5899-f812-4435-ba43-3aeb1b84ea98",
  "type": "user",
  "uuid": "ae049f68-0f04-4c87-909c-78a477ec7d48",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "ea2e6203-5836-4822-aa11-2c51a3d0012d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T04:35:32.980Z_

<details><summary>Logged reasoning block</summary>

```text
Let me conduct multiple searches to understand the current landscape of CoT faithfulness research, probe-based methods, and the specific works cited in this proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae049f68-0f04-4c87-909c-78a477ec7d48",
  "isSidechain": false,
  "requestId": "req_011CbDCVyExUMxvpfMQw8QKU",
  "type": "assistant",
  "uuid": "3a6ed61b-685d-4fba-a1d8-a10f7e18598e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AgKnjk8HaC6gjZbrSTbaM3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 26052,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 719,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 290,
          "cache_read_input_tokens": 26052,
          "cache_creation_input_tokens": 719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 719
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

_source line 13 · 2026-05-20T04:35:33.931Z_

Now let me conduct the required field research with multiple targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a6ed61b-685d-4fba-a1d8-a10f7e18598e",
  "isSidechain": false,
  "requestId": "req_011CbDCVyExUMxvpfMQw8QKU",
  "type": "assistant",
  "uuid": "49bc82d9-8bb8-4473-a5ff-9e03f051250e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AgKnjk8HaC6gjZbrSTbaM3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 26052,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 719,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 290,
          "cache_read_input_tokens": 26052,
          "cache_creation_input_tokens": 719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 719
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

_source line 14 · 2026-05-20T04:35:34.476Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BPZQoVraJzkvRaVFH6aEgG`</summary>

```json
{
  "query": "chain-of-thought faithfulness measurement probing causal intervention 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49bc82d9-8bb8-4473-a5ff-9e03f051250e",
  "isSidechain": false,
  "requestId": "req_011CbDCVyExUMxvpfMQw8QKU",
  "type": "assistant",
  "uuid": "c60717c9-d07e-4f98-bfa8-cafc36845e65",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AgKnjk8HaC6gjZbrSTbaM3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 26052,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 719,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 290,
          "cache_read_input_tokens": 26052,
          "cache_creation_input_tokens": 719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 719
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

_source line 15 · 2026-05-20T04:35:35.479Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U46yyHZhgD4uwUF46yh3i8`</summary>

```json
{
  "query": "probe trajectories hidden states reasoning models diagnostic causal gap 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c60717c9-d07e-4f98-bfa8-cafc36845e65",
  "isSidechain": false,
  "requestId": "req_011CbDCVyExUMxvpfMQw8QKU",
  "type": "assistant",
  "uuid": "8ef552e7-ebb0-40e8-80c7-30d40becbf2b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AgKnjk8HaC6gjZbrSTbaM3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 26052,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 719,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 290,
          "cache_read_input_tokens": 26052,
          "cache_creation_input_tokens": 719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 719
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

_source line 16 · 2026-05-20T04:35:36.009Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R1SztMU96xLFH4HbK1sEGK`</summary>

```json
{
  "query": "Chrabąszcz probe trajectories internal monologue arXiv 2605.18549"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ef552e7-ebb0-40e8-80c7-30d40becbf2b",
  "isSidechain": false,
  "requestId": "req_011CbDCVyExUMxvpfMQw8QKU",
  "type": "assistant",
  "uuid": "2b613607-9435-4368-a50c-34aef266c459",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AgKnjk8HaC6gjZbrSTbaM3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 26052,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 719,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 290,
          "cache_read_input_tokens": 26052,
          "cache_creation_input_tokens": 719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 719
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

_source line 17 · 2026-05-20T04:35:36.877Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P2RYaSXxL3F7Qyeyn3Vx69`</summary>

```json
{
  "query": "Yuan hidden error awareness intervention failure reasoning models arXiv 2605.09502"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b613607-9435-4368-a50c-34aef266c459",
  "isSidechain": false,
  "requestId": "req_011CbDCVyExUMxvpfMQw8QKU",
  "type": "assistant",
  "uuid": "9536cc10-e60f-4a77-986b-d40b72a069a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AgKnjk8HaC6gjZbrSTbaM3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 26052,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 719,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 290,
          "cache_read_input_tokens": 26052,
          "cache_creation_input_tokens": 719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 719
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

_source line 18 · 2026-05-20T04:35:41.380Z_

<details><summary>↩ Tool result · `toolu_01BPZQoVraJzkvRaVFH6aEgG`</summary>

```text
Web search results for query: "chain-of-thought faithfulness measurement probing causal intervention 2025 2026"

Links: [{"title":"Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models","url":"https://arxiv.org/html/2603.26410v1"},{"title":"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps","url":"https://arxiv.org/html/2502.14829v3"},{"title":"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures","url":"https://arxiv.org/html/2603.16475"},{"title":"Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning | Request PDF","url":"https://www.researchgate.net/publication/386203451_Making_Reasoning_Matter_Measuring_and_Improving_Faithfulness_of_Chain-of-Thought_Reasoning"},{"title":"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2602.11201v1"},{"title":"On the Faithfulness of Visual Thinking: Measurement and Enhancement","url":"https://arxiv.org/html/2510.23482v1"},{"title":"FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness","url":"https://arxiv.org/pdf/2509.13334"},{"title":"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps","url":"https://aclanthology.org/2025.emnlp-main.504.pdf"}]

I found several recent papers (2025-2026) on this topic. Here are the key results:

## Recent Research on Chain-of-Thought Faithfulness

**Major Studies:**

Chen et al. (2025) introduced a hint-injection methodology to test whether models verbalize the influence of misleading hints, finding that faithfulness varies dramatically by model and hint type.

Han et al. (2026) use counterfactual interventions on reasoning traces to evaluate causal influence.

**Measurement Methods:**

Researchers employ Representational Similarity Analysis (RSA) to measure the alignment between clean and counterfactually corrupted reasoning trajectories, coupled with linear probes to track the evolution of solution-relevant information across layers.

Parameter intervention approaches prompt models to produce answers and reasoning chains, then segment the reasoning chain and unlearn content tokens from single reasoning steps, measuring faithfulness as the adverse effect of unlearning onto the models' initial prediction.

**Key Findings:**

Even with thinking-token access, 11.8% of influenced cases show no acknowledgment in either channel; the influence operates below the level of verbalization.

A complete monitoring pipeline requires at minimum three tiers: answer-text screening, thinking-token screening, and activation-level or probe-based monitoring.

**Improving Faithfulness:**

FRIT (Faithful Reasoning via Intervention Training) is a scalable method for improving CoT faithfulness without human supervision that uses causality of CoT steps to fine-tune for more faithful outputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c60717c9-d07e-4f98-bfa8-cafc36845e65",
  "isSidechain": false,
  "promptId": "91ae5899-f812-4435-ba43-3aeb1b84ea98",
  "type": "user",
  "uuid": "264aec1f-5241-44be-be7e-9d973d85df0f",
  "toolUseResult": {
    "query": "chain-of-thought faithfulness measurement probing causal intervention 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01U63yyDdp5aPZcR98uKk56s",
        "content": [
          {
            "title": "Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models",
            "url": "https://arxiv.org/html/2603.26410v1"
          },
          {
            "title": "Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps",
            "url": "https://arxiv.org/html/2502.14829v3"
          },
          {
            "title": "Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures",
            "url": "https://arxiv.org/html/2603.16475"
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
            "title": "On the Faithfulness of Visual Thinking: Measurement and Enhancement",
            "url": "https://arxiv.org/html/2510.23482v1"
          },
          {
            "title": "FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness",
            "url": "https://arxiv.org/pdf/2509.13334"
          },
          {
            "title": "Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps",
            "url": "https://aclanthology.org/2025.emnlp-main.504.pdf"
          }
        ]
      },
      "I found several recent papers (2025-2026) on this topic. Here are the key results:\n\n## Recent Research on Chain-of-Thought Faithfulness\n\n**Major Studies:**\n\nChen et al. (2025) introduced a hint-injection methodology to test whether models verbalize the influence of misleading hints, finding that faithfulness varies dramatically by model and hint type.\n\nHan et al. (2026) use counterfactual interventions on reasoning traces to evaluate causal influence.\n\n**Measurement Methods:**\n\nResearchers employ Representational Similarity Analysis (RSA) to measure the alignment between clean and counterfactually corrupted reasoning trajectories, coupled with linear probes to track the evolution of solution-relevant information across layers.\n\nParameter intervention approaches prompt models to produce answers and reasoning chains, then segment the reasoning chain and unlearn content tokens from single reasoning steps, measuring faithfulness as the adverse effect of unlearning onto the models' initial prediction.\n\n**Key Findings:**\n\nEven with thinking-token access, 11.8% of influenced cases show no acknowledgment in either channel; the influence operates below the level of verbalization.\n\nA complete monitoring pipeline requires at minimum three tiers: answer-text screening, thinking-token screening, and activation-level or probe-based monitoring.\n\n**Improving Faithfulness:**\n\nFRIT (Faithful Reasoning via Intervention Training) is a scalable method for improving CoT faithfulness without human supervision that uses causality of CoT steps to fine-tune for more faithful outputs."
    ],
    "durationSeconds": 6.8999204549999975,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c60717c9-d07e-4f98-bfa8-cafc36845e65",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T04:35:43.691Z_

<details><summary>↩ Tool result · `toolu_01R1SztMU96xLFH4HbK1sEGK`</summary>

```text
Web search results for query: "Chrabąszcz probe trajectories internal monologue arXiv 2605.18549"

Links: [{"title":"[2605.18549] Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics","url":"https://arxiv.org/abs/2605.18549"},{"title":"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics","url":"https://arxiv.org/html/2605.18549"},{"title":"Beyond the Black Box: Interpretability of Agentic AI Tool Use","url":"https://arxiv.org/html/2605.06890"},{"title":"Inner Monologue: Embodied Reasoning through Planning ...","url":"https://arxiv.org/pdf/2207.05608"},{"title":"Trajectory sampling using spatial familiarity","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11435202"},{"title":"Computing Feasible Trajectories for an Articulated Probe in Three   Dimensions","url":"https://arxiv.org/pdf/2011.11685"}]

I found the paper! Here are the search results for arXiv 2605.18549:

**Paper Title:** Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics

**Authors:** Maciej Chrabąszcz, Aleksander Szymczyk, Marcin Sendera, Tomasz Trzciński, and Sebastian Cygert from institutions in Poland including NASK - National Research Institute, Warsaw University of Technology, Jagiellonian University, Tooploox, IDEAS Research Institute, and Gdańsk University of Technology

**Main Focus:** The paper addresses safety monitoring of Large Reasoning Models (LRMs) through their Chain of Thought (CoT) reasoning, though CoT is not always faithful to the model's final output, undermining its reliability as a monitoring tool.

**Key Methodology:** The researchers investigate the hidden representations of LRMs to determine whether future behavior can be predicted from prompt and CoT representations by evaluating a probe at each generated token to construct a probe trajectory, the continuous evolution of a concept's probability across the reasoning process.

**Key Findings:** Future model behavior is more distinguishable when examined over the full trajectory than from a single static prediction, and max-pooling achieves up to 95% AUROC and yields stable probe trajectories.

The paper was submitted on May 18, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b613607-9435-4368-a50c-34aef266c459",
  "isSidechain": false,
  "promptId": "91ae5899-f812-4435-ba43-3aeb1b84ea98",
  "type": "user",
  "uuid": "5bd0c66c-e55b-496f-b44f-981f1c27a7a9",
  "toolUseResult": {
    "query": "Chrabąszcz probe trajectories internal monologue arXiv 2605.18549",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KuG93mghDxK7VbBXUyGdRv",
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
            "title": "Inner Monologue: Embodied Reasoning through Planning ...",
            "url": "https://arxiv.org/pdf/2207.05608"
          },
          {
            "title": "Trajectory sampling using spatial familiarity",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11435202"
          },
          {
            "title": "Computing Feasible Trajectories for an Articulated Probe in Three   Dimensions",
            "url": "https://arxiv.org/pdf/2011.11685"
          }
        ]
      },
      "I found the paper! Here are the search results for arXiv 2605.18549:\n\n**Paper Title:** Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics\n\n**Authors:** Maciej Chrabąszcz, Aleksander Szymczyk, Marcin Sendera, Tomasz Trzciński, and Sebastian Cygert from institutions in Poland including NASK - National Research Institute, Warsaw University of Technology, Jagiellonian University, Tooploox, IDEAS Research Institute, and Gdańsk University of Technology\n\n**Main Focus:** The paper addresses safety monitoring of Large Reasoning Models (LRMs) through their Chain of Thought (CoT) reasoning, though CoT is not always faithful to the model's final output, undermining its reliability as a monitoring tool.\n\n**Key Methodology:** The researchers investigate the hidden representations of LRMs to determine whether future behavior can be predicted from prompt and CoT representations by evaluating a probe at each generated token to construct a probe trajectory, the continuous evolution of a concept's probability across the reasoning process.\n\n**Key Findings:** Future model behavior is more distinguishable when examined over the full trajectory than from a single static prediction, and max-pooling achieves up to 95% AUROC and yields stable probe trajectories.\n\nThe paper was submitted on May 18, 2026."
    ],
    "durationSeconds": 7.679538653,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2b613607-9435-4368-a50c-34aef266c459",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T04:35:43.940Z_

<details><summary>↩ Tool result · `toolu_01P2RYaSXxL3F7Qyeyn3Vx69`</summary>

```text
Web search results for query: "Yuan hidden error awareness intervention failure reasoning models arXiv 2605.09502"

Links: [{"title":"[2605.09502] Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal","url":"https://arxiv.org/abs/2605.09502"},{"title":"Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal","url":"https://arxiv.org/html/2605.09502"},{"title":"Stop Before You Fail: Operational Capability Boundaries for Mitigating Unproductive Reasoning in Large Reasoning Models","url":"https://arxiv.org/pdf/2509.24711"},{"title":"Hop, Skip, and Overthink: Diagnosing Why Reasoning Models Fumble during Multi-Hop Analysis","url":"https://arxiv.org/pdf/2508.04699"},{"title":"Mathematical Proof as a Litmus Test: Revealing Failure Modes of Advanced Large Reasoning Models","url":"https://arxiv.org/pdf/2506.17114"},{"title":"Fail Fast, or Ask: Mitigating the Deficiencies of Reasoning LLMs with Human-in-the-Loop Systems Engineering","url":"https://arxiv.org/pdf/2507.14406"},{"title":"Are Reasoning LLMs Robust to Interventions on Their Chain-of-Thought?","url":"https://arxiv.org/pdf/2602.07470"}]

Based on the search results, here's information about the arXiv paper 2605.09502:

## Hidden Error Awareness in Chain-of-Thought Reasoning

The paper shows that the assumption that chain-of-thought reasoning reflects a model's internal computation is wrong in a specific way: models internally detect their own reasoning errors but outwardly express confidence in them.

### Key Findings

A linear probe on hidden states predicts trace correctness with 0.95 AUROC from the very first reasoning step (0.79), while verbalized confidence for wrong traces is 4.55/5, nearly identical to correct ones (4.87/5). A text-surface classifier achieves only 0.59 on the same data, confirming a 0.20-point gap invisible in the generated text.

This hidden error awareness holds across three model families (Qwen, Llama, Phi), 1.5B-72B parameters, and RL-trained reasoning models (DeepSeek-R1, 0.852 AUROC).

### Intervention Failure

Four interventions—activation steering, probe-guided best-of-N, self-correction, and activation patching—all fail; patching destroys output coherence entirely. The signal is diagnostic, not causal: a readout of computation quality, not a lever to redirect it.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9536cc10-e60f-4a77-986b-d40b72a069a8",
  "isSidechain": false,
  "promptId": "91ae5899-f812-4435-ba43-3aeb1b84ea98",
  "type": "user",
  "uuid": "c25d5a98-ec69-458f-9816-e75cebd01807",
  "toolUseResult": {
    "query": "Yuan hidden error awareness intervention failure reasoning models arXiv 2605.09502",
    "results": [
      {
        "tool_use_id": "srvtoolu_013ibGcYw3GWePbM75mMsAmz",
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
            "title": "Mathematical Proof as a Litmus Test: Revealing Failure Modes of Advanced Large Reasoning Models",
            "url": "https://arxiv.org/pdf/2506.17114"
          },
          {
            "title": "Fail Fast, or Ask: Mitigating the Deficiencies of Reasoning LLMs with Human-in-the-Loop Systems Engineering",
            "url": "https://arxiv.org/pdf/2507.14406"
          },
          {
            "title": "Are Reasoning LLMs Robust to Interventions on Their Chain-of-Thought?",
            "url": "https://arxiv.org/pdf/2602.07470"
          }
        ]
      },
      "Based on the search results, here's information about the arXiv paper 2605.09502:\n\n## Hidden Error Awareness in Chain-of-Thought Reasoning\n\nThe paper shows that the assumption that chain-of-thought reasoning reflects a model's internal computation is wrong in a specific way: models internally detect their own reasoning errors but outwardly express confidence in them.\n\n### Key Findings\n\nA linear probe on hidden states predicts trace correctness with 0.95 AUROC from the very first reasoning step (0.79), while verbalized confidence for wrong traces is 4.55/5, nearly identical to correct ones (4.87/5). A text-surface classifier achieves only 0.59 on the same data, confirming a 0.20-point gap invisible in the generated text.\n\nThis hidden error awareness holds across three model families (Qwen, Llama, Phi), 1.5B-72B parameters, and RL-trained reasoning models (DeepSeek-R1, 0.852 AUROC).\n\n### Intervention Failure\n\nFour interventions—activation steering, probe-guided best-of-N, self-correction, and activation patching—all fail; patching destroys output coherence entirely. The signal is diagnostic, not causal: a readout of computation quality, not a lever to redirect it."
    ],
    "durationSeconds": 7.059830032999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9536cc10-e60f-4a77-986b-d40b72a069a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T04:35:44.097Z_

<details><summary>↩ Tool result · `toolu_01U46yyHZhgD4uwUF46yh3i8`</summary>

```text
Web search results for query: "probe trajectories hidden states reasoning models diagnostic causal gap 2025 2026"

Links: [{"title":"Published at Latent & Implicit Thinking Workshop @ ICLR 2026","url":"https://openreview.net/pdf/d14277b6518be41dfa71a1cd3224d4de191e2b8a.pdf"},{"title":"Preprint. February 2026. DYNAMICS WITHIN LATENT CHAIN-OF-THOUGHT:","url":"https://arxiv.org/pdf/2602.08783"},{"title":"Reasoning Models Know When They're Right: Probing Hidden States for   Self-Verification","url":"https://arxiv.org/pdf/2504.05419"},{"title":"Hidden States as Early Signals: Step-level Trace Evaluation and","url":"https://www.arxiv.org/pdf/2601.09093"},{"title":"More Than Meets the Eye? Uncovering the Reasoning-Planning Disconnect in Training Vision-Language Driving Models","url":"https://arxiv.org/pdf/2510.04532"},{"title":"Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning","url":"https://arxiv.org/pdf/2603.01326"}]

Based on the search results, I found several recent papers from 2025-2026 addressing probe trajectories, hidden states, reasoning models, and causal diagnostics:

## Key Research Areas

**Latent Reasoning and Causal Analysis:**
Research instantiates causal evaluation frameworks on latent-reasoning paradigms like Coconut and CODI, across both mathematical and general reasoning tasks. Key causal questions include step-wise necessity (whether final decisions depend on intermediate states) and latent-budget sufficiency (how many latent steps are required before answers become decodable).

**Hidden States and Correctness Detection:**
Hidden states encode correctness of future answers, enabling early prediction before intermediate answers are fully formulated, and probes can be used as verifiers to decide whether to exit reasoning at intermediate answers during inference, reducing inference tokens by 24% without compromising performance.

**Diagnostic Causal Methods:**
A "Causal Probe" is a novel, training-free diagnostic method that detects shortcut reliance, providing a tool for evaluating causal robustness. Research analyzes layerwise hidden states as trajectories in activation space, with correct generations following smoother paths while incorrect ones exhibit sharp deviations.

**The Reasoning-Decision Gap:**
A consistent pattern shows that causal leverage is highly heterogeneous across latent steps with a small subset exerting outsized influence, step-to-step effects are often non-local indicating routed propagation rather than purely chain-like transmission, and output-level preference can emerge earlier than representational consolidation, revealing a persistent gap between early bias and later confirmation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ef552e7-ebb0-40e8-80c7-30d40becbf2b",
  "isSidechain": false,
  "promptId": "91ae5899-f812-4435-ba43-3aeb1b84ea98",
  "type": "user",
  "uuid": "fcc9b2a6-d3ed-44a5-93ec-fb401c5b6c62",
  "toolUseResult": {
    "query": "probe trajectories hidden states reasoning models diagnostic causal gap 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014vGAeWsJXEC1pDEMz9QT51",
        "content": [
          {
            "title": "Published at Latent & Implicit Thinking Workshop @ ICLR 2026",
            "url": "https://openreview.net/pdf/d14277b6518be41dfa71a1cd3224d4de191e2b8a.pdf"
          },
          {
            "title": "Preprint. February 2026. DYNAMICS WITHIN LATENT CHAIN-OF-THOUGHT:",
            "url": "https://arxiv.org/pdf/2602.08783"
          },
          {
            "title": "Reasoning Models Know When They're Right: Probing Hidden States for   Self-Verification",
            "url": "https://arxiv.org/pdf/2504.05419"
          },
          {
            "title": "Hidden States as Early Signals: Step-level Trace Evaluation and",
            "url": "https://www.arxiv.org/pdf/2601.09093"
          },
          {
            "title": "More Than Meets the Eye? Uncovering the Reasoning-Planning Disconnect in Training Vision-Language Driving Models",
            "url": "https://arxiv.org/pdf/2510.04532"
          },
          {
            "title": "Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning",
            "url": "https://arxiv.org/pdf/2603.01326"
          }
        ]
      },
      "Based on the search results, I found several recent papers from 2025-2026 addressing probe trajectories, hidden states, reasoning models, and causal diagnostics:\n\n## Key Research Areas\n\n**Latent Reasoning and Causal Analysis:**\nResearch instantiates causal evaluation frameworks on latent-reasoning paradigms like Coconut and CODI, across both mathematical and general reasoning tasks. Key causal questions include step-wise necessity (whether final decisions depend on intermediate states) and latent-budget sufficiency (how many latent steps are required before answers become decodable).\n\n**Hidden States and Correctness Detection:**\nHidden states encode correctness of future answers, enabling early prediction before intermediate answers are fully formulated, and probes can be used as verifiers to decide whether to exit reasoning at intermediate answers during inference, reducing inference tokens by 24% without compromising performance.\n\n**Diagnostic Causal Methods:**\nA \"Causal Probe\" is a novel, training-free diagnostic method that detects shortcut reliance, providing a tool for evaluating causal robustness. Research analyzes layerwise hidden states as trajectories in activation space, with correct generations following smoother paths while incorrect ones exhibit sharp deviations.\n\n**The Reasoning-Decision Gap:**\nA consistent pattern shows that causal leverage is highly heterogeneous across latent steps with a small subset exerting outsized influence, step-to-step effects are often non-local indicating routed propagation rather than purely chain-like transmission, and output-level preference can emerge earlier than representational consolidation, revealing a persistent gap between early bias and later confirmation."
    ],
    "durationSeconds": 8.615784459000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8ef552e7-ebb0-40e8-80c7-30d40becbf2b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-T…",
  "leafUuid": "fcc9b2a6-d3ed-44a5-93ec-fb401c5b6c62",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Temporal information-contribution gap analysis for reasoning faithfulness",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3"
}
```

---

### Tool call

_source line 24 · 2026-05-20T04:35:48.431Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011qHpD6Q4HaggEEceHzcbhT`</summary>

```json
{
  "query": "FaithCoT-Bench faithfulness benchmark ICLR 2026 arXiv 2510.04040"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcc9b2a6-d3ed-44a5-93ec-fb401c5b6c62",
  "isSidechain": false,
  "requestId": "req_011CbDCWyDFdyrq84c8UsqPK",
  "type": "assistant",
  "uuid": "db9e8537-e376-4b05-bd65-96a23c869801",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zqSbFZppb9WPbypsxPuhH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1351,
      "cache_creation_input_tokens": 1798,
      "cache_read_input_tokens": 26771,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1798,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1351,
          "output_tokens": 193,
          "cache_read_input_tokens": 26771,
          "cache_creation_input_tokens": 1798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1798
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

_source line 25 · 2026-05-20T04:35:48.970Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EwzN67oAuHN9HeXWHu2w62`</summary>

```json
{
  "query": "Ballon probing trajectories reasoning traces truncation reinjection arXiv 2601.23163"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db9e8537-e376-4b05-bd65-96a23c869801",
  "isSidechain": false,
  "requestId": "req_011CbDCWyDFdyrq84c8UsqPK",
  "type": "assistant",
  "uuid": "ab5442b3-a84d-462a-9d8a-03d3e0ec2278",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zqSbFZppb9WPbypsxPuhH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1351,
      "cache_creation_input_tokens": 1798,
      "cache_read_input_tokens": 26771,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1798,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1351,
          "output_tokens": 193,
          "cache_read_input_tokens": 26771,
          "cache_creation_input_tokens": 1798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1798
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

_source line 26 · 2026-05-20T04:35:49.621Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017XzGTKfzxtTuDY6zzWNHtF`</summary>

```json
{
  "query": "Cox decoding answers before chain-of-thought steering failure reasoning models arXiv 2603.01437"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab5442b3-a84d-462a-9d8a-03d3e0ec2278",
  "isSidechain": false,
  "requestId": "req_011CbDCWyDFdyrq84c8UsqPK",
  "type": "assistant",
  "uuid": "fb92b1a6-25a1-4fbe-a5dc-68d810637dae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zqSbFZppb9WPbypsxPuhH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1351,
      "cache_creation_input_tokens": 1798,
      "cache_read_input_tokens": 26771,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1798,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1351,
          "output_tokens": 193,
          "cache_read_input_tokens": 26771,
          "cache_creation_input_tokens": 1798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1798
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

_source line 27 · 2026-05-20T04:35:54.559Z_

<details><summary>↩ Tool result · `toolu_01EwzN67oAuHN9HeXWHu2w62`</summary>

```text
Web search results for query: "Ballon probing trajectories reasoning traces truncation reinjection arXiv 2601.23163"

Links: [{"title":"[2601.23163] Probing the Trajectories of Reasoning Traces in Large Language Models","url":"https://arxiv.org/abs/2601.23163"},{"title":"Probing the Trajectories of Reasoning Traces in Large Language Models","url":"https://arxiv.org/html/2601.23163v1"},{"title":"Harnessing Reasoning Trajectories for Hallucination Detection via Answer-agreement Representation Shaping","url":"https://arxiv.org/pdf/2601.17467"},{"title":"Harnessing Reasoning Trajectories for Hallucination Detection via Answer-agreement Representation Shaping","url":"https://arxiv.org/html/2601.17467v1"},{"title":"[2601.17467] Harnessing Reasoning Trajectories for Hallucination Detection via Answer-agreement Representation Shaping","url":"https://arxiv.org/abs/2601.17467"},{"title":"[2601.21494] The Path of Least Resistance: Guiding LLM Reasoning Trajectories with Prefix Consensus","url":"https://arxiv.org/abs/2601.21494"}]

Based on the search results, I found the paper you're looking for:

**"Probing the Trajectories of Reasoning Traces in Large Language Models"** (arXiv 2601.23163)

This paper by Marthe Ballon and 3 other authors addresses how Large Language Models (LLMs) increasingly solve difficult problems by producing "reasoning traces" before emitting a final response.

The research investigates how accuracy and decision commitment evolve along a reasoning trajectory, and whether intermediate trace segments provide answer-relevant information beyond generic length or stylistic effects.

The authors propose a protocol to systematically probe the trajectories of reasoning traces in LLMs by: 1) generating a model's reasoning trace, 2) truncating it at fixed token-percentiles, and 3) injecting each partial trace back into the model (or a different model) to measure the induced distribution over answer choices via next-token probabilities.

The paper was published on January 30, 2026. You can access the full paper directly on arXiv at https://arxiv.org/abs/2601.23163.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab5442b3-a84d-462a-9d8a-03d3e0ec2278",
  "isSidechain": false,
  "promptId": "91ae5899-f812-4435-ba43-3aeb1b84ea98",
  "type": "user",
  "uuid": "0567c962-e720-46ab-937f-66868c0f6433",
  "toolUseResult": {
    "query": "Ballon probing trajectories reasoning traces truncation reinjection arXiv 2601.23163",
    "results": [
      {
        "tool_use_id": "srvtoolu_0121uPdPZAjA51oRCfdUjXcC",
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
            "title": "Harnessing Reasoning Trajectories for Hallucination Detection via Answer-agreement Representation Shaping",
            "url": "https://arxiv.org/pdf/2601.17467"
          },
          {
            "title": "Harnessing Reasoning Trajectories for Hallucination Detection via Answer-agreement Representation Shaping",
            "url": "https://arxiv.org/html/2601.17467v1"
          },
          {
            "title": "[2601.17467] Harnessing Reasoning Trajectories for Hallucination Detection via Answer-agreement Representation Shaping",
            "url": "https://arxiv.org/abs/2601.17467"
          },
          {
            "title": "[2601.21494] The Path of Least Resistance: Guiding LLM Reasoning Trajectories with Prefix Consensus",
            "url": "https://arxiv.org/abs/2601.21494"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**\"Probing the Trajectories of Reasoning Traces in Large Language Models\"** (arXiv 2601.23163)\n\nThis paper by Marthe Ballon and 3 other authors addresses how Large Language Models (LLMs) increasingly solve difficult problems by producing \"reasoning traces\" before emitting a final response.\n\nThe research investigates how accuracy and decision commitment evolve along a reasoning trajectory, and whether intermediate trace segments provide answer-relevant information beyond generic length or stylistic effects.\n\nThe authors propose a protocol to systematically probe the trajectories of reasoning traces in LLMs by: 1) generating a model's reasoning trace, 2) truncating it at fixed token-percentiles, and 3) injecting each partial trace back into the model (or a different model) to measure the induced distribution over answer choices via next-token probabilities.\n\nThe paper was published on January 30, 2026. You can access the full paper directly on arXiv at https://arxiv.org/abs/2601.23163."
    ],
    "durationSeconds": 5.585355479000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ab5442b3-a84d-462a-9d8a-03d3e0ec2278",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T04:35:55.226Z_

<details><summary>↩ Tool result · `toolu_011qHpD6Q4HaggEEceHzcbhT`</summary>

```text
Web search results for query: "FaithCoT-Bench faithfulness benchmark ICLR 2026 arXiv 2510.04040"

Links: [{"title":"IAI Researchers Have 23 Papers Accepted in ICLR 2026 - Institute of Artificial Intelligence","url":"https://ai.ucf.edu/iai-researchers-have-23-papers-accepted-in-iclr-2026/"},{"title":"Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING","url":"https://arxiv.org/pdf/2510.04040"},{"title":"[2510.04040] FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning","url":"https://arxiv.org/abs/2510.04040"},{"title":"Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING","url":"https://openreview.net/pdf?id=lN3yKqqzF1"},{"title":"SPD-Faith Bench: Diagnosing and Improving Faithfulness in Chain-of-Thought for Multimodal Large Language Models","url":"https://arxiv.org/html/2602.07833v1"},{"title":"Reasoning Faithfulness","url":"https://akhil.bio/CoT"},{"title":"Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?","url":"https://arxiv.org/html/2603.22582v1"}]

Based on the search results, here's what I found about FaithCoT-Bench:

## Overview
FaithCoT-Bench is a unified benchmark for instance-level CoT unfaithfulness detection. The paper was published at the Fourteenth International Conference on Learning Representations (ICLR) in 2026.

## Motivation
Large language models (LLMs) increasingly rely on Chain-of-Thought (CoT) prompting to improve problem-solving and provide seemingly transparent explanations, however, growing evidence shows that CoT often fail to faithfully represent the underlying reasoning process, raising concerns about their reliability in high-risk applications.

## Key Components
FaithCoT-Bench provides FINE-CoT (Faithfulness instance evaluation for Chain-of-Thought), an expert-annotated collection of over 1,000 trajectories generated by four representative LLMs across four domains, including more than 300 unfaithful instances with fine-grained causes and step-level evidence.

## Methodology
The authors collected CoT traces from four domains and four LLMs, annotated them through a multi-stage human pipeline to build the FINE-CoT dataset, and benchmarked existing detection methods across counterfactual, logit-based, and LLM-as-Judge paradigms.

## Evaluation
FaithCoT-Bench provides a unified reference for fair assessment of counterfactual, logit-based, and LLM-as-judge approaches, and allows us to uncover their respective strengths and limitations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db9e8537-e376-4b05-bd65-96a23c869801",
  "isSidechain": false,
  "promptId": "91ae5899-f812-4435-ba43-3aeb1b84ea98",
  "type": "user",
  "uuid": "e0a5d30b-9f08-4b30-b5e9-b873ec407a35",
  "toolUseResult": {
    "query": "FaithCoT-Bench faithfulness benchmark ICLR 2026 arXiv 2510.04040",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QEhJRAvvT3kyWxXKzAzceU",
        "content": [
          {
            "title": "IAI Researchers Have 23 Papers Accepted in ICLR 2026 - Institute of Artificial Intelligence",
            "url": "https://ai.ucf.edu/iai-researchers-have-23-papers-accepted-in-iclr-2026/"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING",
            "url": "https://arxiv.org/pdf/2510.04040"
          },
          {
            "title": "[2510.04040] FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/abs/2510.04040"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING",
            "url": "https://openreview.net/pdf?id=lN3yKqqzF1"
          },
          {
            "title": "SPD-Faith Bench: Diagnosing and Improving Faithfulness in Chain-of-Thought for Multimodal Large Language Models",
            "url": "https://arxiv.org/html/2602.07833v1"
          },
          {
            "title": "Reasoning Faithfulness",
            "url": "https://akhil.bio/CoT"
          },
          {
            "title": "Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?",
            "url": "https://arxiv.org/html/2603.22582v1"
          }
        ]
      },
      "Based on the search results, here's what I found about FaithCoT-Bench:\n\n## Overview\nFaithCoT-Bench is a unified benchmark for instance-level CoT unfaithfulness detection. The paper was published at the Fourteenth International Conference on Learning Representations (ICLR) in 2026.\n\n## Motivation\nLarge language models (LLMs) increasingly rely on Chain-of-Thought (CoT) prompting to improve problem-solving and provide seemingly transparent explanations, however, growing evidence shows that CoT often fail to faithfully represent the underlying reasoning process, raising concerns about their reliability in high-risk applications.\n\n## Key Components\nFaithCoT-Bench provides FINE-CoT (Faithfulness instance evaluation for Chain-of-Thought), an expert-annotated collection of over 1,000 trajectories generated by four representative LLMs across four domains, including more than 300 unfaithful instances with fine-grained causes and step-level evidence.\n\n## Methodology\nThe authors collected CoT traces from four domains and four LLMs, annotated them through a multi-stage human pipeline to build the FINE-CoT dataset, and benchmarked existing detection methods across counterfactual, logit-based, and LLM-as-Judge paradigms.\n\n## Evaluation\nFaithCoT-Bench provides a unified reference for fair assessment of counterfactual, logit-based, and LLM-as-judge approaches, and allows us to uncover their respective strengths and limitations."
    ],
    "durationSeconds": 6.791034135000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "db9e8537-e376-4b05-bd65-96a23c869801",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T04:35:55.587Z_

<details><summary>↩ Tool result · `toolu_017XzGTKfzxtTuDY6zzWNHtF`</summary>

```text
Web search results for query: "Cox decoding answers before chain-of-thought steering failure reasoning models arXiv 2603.01437"

Links: [{"title":"[2603.01437] Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/abs/2603.01437"},{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/html/2603.01437"},{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/pdf/2603.01437"},{"title":"Nudging Hidden States: Training-Free Model Steering for Chain-of-Thought Reasoning in Large Audio-Language Models","url":"https://arxiv.org/pdf/2603.14636"},{"title":"[2603.16331v1] Decoding the Critique Mechanism in Large Reasoning Models","url":"https://arxiv.org/abs/2603.16331v1"}]

I found the paper! Here's information about the arXiv paper 2603.01437:

**Title:** Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering

**Authors:** Kyle Cox, Darius Kianersi, and Adrià Garriga-Alonso

**Key Findings:**

Instruction-tuned models often determine their answer before generating chain-of-thought. The researchers demonstrated this through two methods:

1. **Predictive Analysis:** Training linear probes on residual stream activations at the last token before CoT, they can predict the model's final answer with 0.9 AUC on most tasks.

2. **Causal Evidence:** Steering activations along the probe direction flips model answers in over 50% of cases, significantly exceeding orthogonal baselines.

**Failure Modes:** When steering induces incorrect answers, there are two distinct failure modes: non-entailment (stating correct premises but drawing unsupported conclusions) and confabulation (fabricating false premises).

The paper was posted on March 2, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb92b1a6-25a1-4fbe-a5dc-68d810637dae",
  "isSidechain": false,
  "promptId": "91ae5899-f812-4435-ba43-3aeb1b84ea98",
  "type": "user",
  "uuid": "2e9b6e7e-bf63-4339-aeee-aaed90fbd9c5",
  "toolUseResult": {
    "query": "Cox decoding answers before chain-of-thought steering failure reasoning models arXiv 2603.01437",
    "results": [
      {
        "tool_use_id": "srvtoolu_018pokoA9BDzbdW5RFaR2qEN",
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
            "title": "Nudging Hidden States: Training-Free Model Steering for Chain-of-Thought Reasoning in Large Audio-Language Models",
            "url": "https://arxiv.org/pdf/2603.14636"
          },
          {
            "title": "[2603.16331v1] Decoding the Critique Mechanism in Large Reasoning Models",
            "url": "https://arxiv.org/abs/2603.16331v1"
          }
        ]
      },
      "I found the paper! Here's information about the arXiv paper 2603.01437:\n\n**Title:** Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering\n\n**Authors:** Kyle Cox, Darius Kianersi, and Adrià Garriga-Alonso\n\n**Key Findings:**\n\nInstruction-tuned models often determine their answer before generating chain-of-thought. The researchers demonstrated this through two methods:\n\n1. **Predictive Analysis:** Training linear probes on residual stream activations at the last token before CoT, they can predict the model's final answer with 0.9 AUC on most tasks.\n\n2. **Causal Evidence:** Steering activations along the probe direction flips model answers in over 50% of cases, significantly exceeding orthogonal baselines.\n\n**Failure Modes:** When steering induces incorrect answers, there are two distinct failure modes: non-entailment (stating correct premises but drawing unsupported conclusions) and confabulation (fabricating false premises).\n\nThe paper was posted on March 2, 2026."
    ],
    "durationSeconds": 5.963479810000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fb92b1a6-25a1-4fbe-a5dc-68d810637dae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-20T04:35:55.591Z_

```json
{
  "parentUuid": "2e9b6e7e-bf63-4339-aeee-aaed90fbd9c5",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "d28d2e6e-8af2-44e8-9257-089c467f6521",
  "timestamp": "2026-05-20T04:35:55.591Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-20T04:35:59.154Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019W8yJFYatvVJNkRMkkHArG`</summary>

```json
{
  "query": "Wang \"LLM reasoning is latent\" H1 H2 hypothesis arXiv 2604.15726"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d28d2e6e-8af2-44e8-9257-089c467f6521",
  "isSidechain": false,
  "requestId": "req_011CbDCXpNDiztp9y1X3aynj",
  "type": "assistant",
  "uuid": "bf198adf-e22a-4bce-8825-65c6f7e0d448",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUJ9BpuPYjdS8a99BWo9G3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3629,
      "cache_read_input_tokens": 28569,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 28569,
          "cache_creation_input_tokens": 3629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3629
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

_source line 32 · 2026-05-20T04:36:00.101Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GMg3PDAaVFQPcEbrbJo9it`</summary>

```json
{
  "query": "causal mediation information CoT faithfulness CMI Sathyanarayanan arXiv 2602.03994"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf198adf-e22a-4bce-8825-65c6f7e0d448",
  "isSidechain": false,
  "requestId": "req_011CbDCXpNDiztp9y1X3aynj",
  "type": "assistant",
  "uuid": "7cf62f1e-0b52-41d4-9b65-f4ebe2e47b7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUJ9BpuPYjdS8a99BWo9G3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3629,
      "cache_read_input_tokens": 28569,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 28569,
          "cache_creation_input_tokens": 3629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3629
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

_source line 33 · 2026-05-20T04:36:05.115Z_

<details><summary>↩ Tool result · `toolu_019W8yJFYatvVJNkRMkkHArG`</summary>

```text
Web search results for query: "Wang "LLM reasoning is latent" H1 H2 hypothesis arXiv 2604.15726"

Links: [{"title":"LLM Reasoning Is Latent, Not the Chain of Thought","url":"https://arxiv.org/html/2604.15726"},{"title":"[2604.15726] LLM Reasoning Is Latent, Not the Chain of Thought","url":"https://arxiv.org/abs/2604.15726"},{"title":"Reasoning Beyond Chain-of-Thought: A Latent Computational Mode in Large Language Models","url":"https://arxiv.org/pdf/2601.08058"},{"title":"Training Large Language Models to Reason in a Continuous Latent Space","url":"https://arxiv.org/html/2412.06769v1"},{"title":"Do Large Language Models Latently Perform Multi-Hop Reasoning?","url":"https://arxiv.org/pdf/2402.16837"},{"title":"Emergent Hierarchical Reasoning in LLMs through Reinforcement Learning","url":"https://arxiv.org/pdf/2509.03646"}]

I found the paper! Here are the key details:

The paper is titled "LLM Reasoning Is Latent, Not the Chain of Thought" by Wenshuo Wang from the School of Future Technology at South China University of Technology, published on arXiv as 2604.15726 on April 17, 2026.

The paper formalizes three competing hypotheses: H1, reasoning is primarily mediated by latent-state trajectories; H2, reasoning is primarily mediated by explicit surface CoT; and H0, most apparent reasoning gains are better explained by generic serial compute than by any privileged representational object.

The paper finds that current evidence most strongly supports H1 as a default working hypothesis.

You can access the full paper at: https://arxiv.org/html/2604.15726 or https://arxiv.org/abs/2604.15726


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf198adf-e22a-4bce-8825-65c6f7e0d448",
  "isSidechain": false,
  "promptId": "91ae5899-f812-4435-ba43-3aeb1b84ea98",
  "type": "user",
  "uuid": "1a775e06-337d-4abd-947e-033c1f2164c9",
  "toolUseResult": {
    "query": "Wang \"LLM reasoning is latent\" H1 H2 hypothesis arXiv 2604.15726",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Euqgb1NjZyXAa4HbHYk3kd",
        "content": [
          {
            "title": "LLM Reasoning Is Latent, Not the Chain of Thought",
            "url": "https://arxiv.org/html/2604.15726"
          },
          {
            "title": "[2604.15726] LLM Reasoning Is Latent, Not the Chain of Thought",
            "url": "https://arxiv.org/abs/2604.15726"
          },
          {
            "title": "Reasoning Beyond Chain-of-Thought: A Latent Computational Mode in Large Language Models",
            "url": "https://arxiv.org/pdf/2601.08058"
          },
          {
            "title": "Training Large Language Models to Reason in a Continuous Latent Space",
            "url": "https://arxiv.org/html/2412.06769v1"
          },
          {
            "title": "Do Large Language Models Latently Perform Multi-Hop Reasoning?",
            "url": "https://arxiv.org/pdf/2402.16837"
          },
          {
            "title": "Emergent Hierarchical Reasoning in LLMs through Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2509.03646"
          }
        ]
      },
      "I found the paper! Here are the key details:\n\nThe paper is titled \"LLM Reasoning Is Latent, Not the Chain of Thought\" by Wenshuo Wang from the School of Future Technology at South China University of Technology, published on arXiv as 2604.15726 on April 17, 2026.\n\nThe paper formalizes three competing hypotheses: H1, reasoning is primarily mediated by latent-state trajectories; H2, reasoning is primarily mediated by explicit surface CoT; and H0, most apparent reasoning gains are better explained by generic serial compute than by any privileged representational object.\n\nThe paper finds that current evidence most strongly supports H1 as a default working hypothesis.\n\nYou can access the full paper at: https://arxiv.org/html/2604.15726 or https://arxiv.org/abs/2604.15726"
    ],
    "durationSeconds": 5.957886498,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bf198adf-e22a-4bce-8825-65c6f7e0d448",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T04:36:07.094Z_

<details><summary>↩ Tool result · `toolu_01GMg3PDAaVFQPcEbrbJo9it`</summary>

```text
Web search results for query: "causal mediation information CoT faithfulness CMI Sathyanarayanan arXiv 2602.03994"

Links: [{"title":"BYPASSING THE RATIONALE: CAUSAL AUDITING OF","url":"https://www.arxiv.org/pdf/2602.03994"},{"title":"[2602.03994] When Chains of Thought Don't Matter: Causal Bypass in Large Language Models","url":"https://arxiv.org/abs/2602.03994"},{"title":"When Chains of Thought Don’t Matter: Causal Bypass in Large Language Models","url":"https://arxiv.org/html/2602.03994"},{"title":"[2203.10665] Shaking the causal tree: On the faithfulness and minimality assumptions beyond pairwise interactions","url":"https://arxiv.org/abs/2203.10665"},{"title":"arXiv:2203.10665v2 [cond-mat.stat-mech] 6 Aug 2022","url":"https://arxiv.org/pdf/2203.10665"},{"title":"Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2402.13950v3"},{"title":"When causation does not imply correlation: robust violations of the   Faithfulness axiom","url":"https://arxiv.org/pdf/1505.03118"}]

Based on the search results, I found information about the arXiv paper 2602.03994:

**Title:** "When Chains of Thought Don't Matter: Causal Bypass in Large Language Models" by Anish Sathyanarayanan, Aditya Nagarsekar, and Aarush Rathore

**Key Concepts:**

The CoT Mediation Index (CMI) isolates CoT-specific causal influence by comparing performance degradation from patching CoT-token hidden states against matched control patches.

**Main Findings:**

Even when CoT is verbose, strategic, and flagged by surface-level manipulation detectors, model answers are often causally independent of the CoT content. CMI is highly localized in depth, with only a small subset of layers carrying most of the CoT-specific causal effect.

**Methodology:**

The diagnostic framework combines an interpretable behavioral module that scores manipulation-relevant signals in CoT text and a causal probe that measures CoT-mediated influence via hidden-state patching.

The paper presents evidence that while language models may produce reasoning traces, they often don't mechanistically rely on them during computation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cf62f1e-0b52-41d4-9b65-f4ebe2e47b7d",
  "isSidechain": false,
  "promptId": "91ae5899-f812-4435-ba43-3aeb1b84ea98",
  "type": "user",
  "uuid": "f1570992-644a-4d03-bc00-aa54df3c7e1c",
  "toolUseResult": {
    "query": "causal mediation information CoT faithfulness CMI Sathyanarayanan arXiv 2602.03994",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QJ2PWN17QtiK92H6PuaSZo",
        "content": [
          {
            "title": "BYPASSING THE RATIONALE: CAUSAL AUDITING OF",
            "url": "https://www.arxiv.org/pdf/2602.03994"
          },
          {
            "title": "[2602.03994] When Chains of Thought Don't Matter: Causal Bypass in Large Language Models",
            "url": "https://arxiv.org/abs/2602.03994"
          },
          {
            "title": "When Chains of Thought Don’t Matter: Causal Bypass in Large Language Models",
            "url": "https://arxiv.org/html/2602.03994"
          },
          {
            "title": "[2203.10665] Shaking the causal tree: On the faithfulness and minimality assumptions beyond pairwise interactions",
            "url": "https://arxiv.org/abs/2203.10665"
          },
          {
            "title": "arXiv:2203.10665v2 [cond-mat.stat-mech] 6 Aug 2022",
            "url": "https://arxiv.org/pdf/2203.10665"
          },
          {
            "title": "Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2402.13950v3"
          },
          {
            "title": "When causation does not imply correlation: robust violations of the   Faithfulness axiom",
            "url": "https://arxiv.org/pdf/1505.03118"
          }
        ]
      },
      "Based on the search results, I found information about the arXiv paper 2602.03994:\n\n**Title:** \"When Chains of Thought Don't Matter: Causal Bypass in Large Language Models\" by Anish Sathyanarayanan, Aditya Nagarsekar, and Aarush Rathore\n\n**Key Concepts:**\n\nThe CoT Mediation Index (CMI) isolates CoT-specific causal influence by comparing performance degradation from patching CoT-token hidden states against matched control patches.\n\n**Main Findings:**\n\nEven when CoT is verbose, strategic, and flagged by surface-level manipulation detectors, model answers are often causally independent of the CoT content. CMI is highly localized in depth, with only a small subset of layers carrying most of the CoT-specific causal effect.\n\n**Methodology:**\n\nThe diagnostic framework combines an interpretable behavioral module that scores manipulation-relevant signals in CoT text and a causal probe that measures CoT-mediated influence via hidden-state patching.\n\nThe paper presents evidence that while language models may produce reasoning traces, they often don't mechanistically rely on them during computation."
    ],
    "durationSeconds": 6.9909685559999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7cf62f1e-0b52-41d4-9b65-f4ebe2e47b7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T04:36:10.231Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012YAy1McfQmtUAWECtnhTYd`</summary>

```json
{
  "query": "Thought Anchors counterfactual reasoning chain-of-thought arXiv 2506.19143 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1570992-644a-4d03-bc00-aa54df3c7e1c",
  "isSidechain": false,
  "requestId": "req_011CbDCYfYRm37dBxA1P1HA8",
  "type": "assistant",
  "uuid": "6cb29312-5d61-42b9-b585-74239aceb25c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YreVqmJgFrioQSuMY9g8g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1329,
      "cache_read_input_tokens": 32198,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1329,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 32198,
          "cache_creation_input_tokens": 1329,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1329
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

_source line 36 · 2026-05-20T04:36:10.860Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015rJA3qeedbDfz9sLH168UX`</summary>

```json
{
  "query": "True Thinking Score TTS Zhao per-step causal contribution reasoning arXiv 2510.24941"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cb29312-5d61-42b9-b585-74239aceb25c",
  "isSidechain": false,
  "requestId": "req_011CbDCYfYRm37dBxA1P1HA8",
  "type": "assistant",
  "uuid": "f62515ec-685e-470c-bbde-e22fb25e075c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YreVqmJgFrioQSuMY9g8g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1329,
      "cache_read_input_tokens": 32198,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1329,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 32198,
          "cache_creation_input_tokens": 1329,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1329
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-T…",
  "leafUuid": "f62515ec-685e-470c-bbde-e22fb25e075c",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Temporal information-contribution gap analysis for reasoning faithfulness",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3"
}
```

---

### Tool result

_source line 39 · 2026-05-20T04:36:17.094Z_

<details><summary>↩ Tool result · `toolu_015rJA3qeedbDfz9sLH168UX`</summary>

```text
Web search results for query: "True Thinking Score TTS Zhao per-step causal contribution reasoning arXiv 2510.24941"

Links: [{"title":"[2510.24941] Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought","url":"https://arxiv.org/abs/2510.24941"},{"title":"Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought","url":"https://arxiv.org/html/2510.24941"},{"title":"Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought","url":"https://arxiv.org/pdf/2510.24941"},{"title":"[2510.07745] Parallel Test-Time Scaling for Latent Reasoning Models","url":"https://arxiv.org/abs/2510.07745"},{"title":"Making Reasoning Matter: Measuring and Improving Faithfulness of   Chain-of-Thought Reasoning","url":"https://arxiv.org/pdf/2402.13950"},{"title":"Decomposing the True Score Variance in Rated Responses to Divergent Thinking-Tasks for Assessing Creativity: A Multitrait–Multimethod Analysis","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11508196/"}]

I found relevant information about the paper you're searching for. Here are the key findings:

The paper "Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought" is authored by Jiachen Zhao, Yiyou Sun, Weiyan Shi, and Dawn Song.

The True Thinking Score (TTS) is proposed to quantify the causal contribution of each step in chain-of-thought (CoT) to the model's final prediction. The experiments show that large language models often interleave between true-thinking steps (which are genuinely used to compute the final output) and decorative-thinking steps (which give the appearance of reasoning but have minimal causal influence).

The research reveals that only a small subset of the total reasoning steps causally drive the model's prediction—for example, on AIME, only an average of 2.3% of reasoning steps in CoT have a TTS ≥ 0.7 (with a range of 0-1) for Qwen-2.5.

The paper is available on arXiv at: https://arxiv.org/abs/2510.24941


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f62515ec-685e-470c-bbde-e22fb25e075c",
  "isSidechain": false,
  "promptId": "91ae5899-f812-4435-ba43-3aeb1b84ea98",
  "type": "user",
  "uuid": "4a95fafc-eac8-45ff-8e7f-d68f491b23e9",
  "toolUseResult": {
    "query": "True Thinking Score TTS Zhao per-step causal contribution reasoning arXiv 2510.24941",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HKQRenEsSVpWqgLBZQCUeD",
        "content": [
          {
            "title": "[2510.24941] Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought",
            "url": "https://arxiv.org/abs/2510.24941"
          },
          {
            "title": "Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought",
            "url": "https://arxiv.org/html/2510.24941"
          },
          {
            "title": "Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought",
            "url": "https://arxiv.org/pdf/2510.24941"
          },
          {
            "title": "[2510.07745] Parallel Test-Time Scaling for Latent Reasoning Models",
            "url": "https://arxiv.org/abs/2510.07745"
          },
          {
            "title": "Making Reasoning Matter: Measuring and Improving Faithfulness of   Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/pdf/2402.13950"
          },
          {
            "title": "Decomposing the True Score Variance in Rated Responses to Divergent Thinking-Tasks for Assessing Creativity: A Multitrait–Multimethod Analysis",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11508196/"
          }
        ]
      },
      "I found relevant information about the paper you're searching for. Here are the key findings:\n\nThe paper \"Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought\" is authored by Jiachen Zhao, Yiyou Sun, Weiyan Shi, and Dawn Song.\n\nThe True Thinking Score (TTS) is proposed to quantify the causal contribution of each step in chain-of-thought (CoT) to the model's final prediction. The experiments show that large language models often interleave between true-thinking steps (which are genuinely used to compute the final output) and decorative-thinking steps (which give the appearance of reasoning but have minimal causal influence).\n\nThe research reveals that only a small subset of the total reasoning steps causally drive the model's prediction—for example, on AIME, only an average of 2.3% of reasoning steps in CoT have a TTS ≥ 0.7 (with a range of 0-1) for Qwen-2.5.\n\nThe paper is available on arXiv at: https://arxiv.org/abs/2510.24941"
    ],
    "durationSeconds": 6.2301660960000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f62515ec-685e-470c-bbde-e22fb25e075c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T04:36:17.925Z_

<details><summary>↩ Tool result · `toolu_012YAy1McfQmtUAWECtnhTYd`</summary>

```text
Web search results for query: "Thought Anchors counterfactual reasoning chain-of-thought arXiv 2506.19143 2025"

Links: [{"title":"[2506.19143] Thought Anchors: Which LLM Reasoning Steps Matter?","url":"https://arxiv.org/abs/2506.19143"},{"title":"[2506.19143v2] Thought Anchors: Which LLM Reasoning Steps Matter?","url":"https://arxiv.org/abs/2506.19143v2"},{"title":"[Literature Review] Thought Anchors: Which LLM Reasoning Steps Matter?","url":"https://www.themoonlight.io/en/review/thought-anchors-which-llm-reasoning-steps-matter"},{"title":"Thought Anchors: Which LLM Reasoning Steps Matter? | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/thought-anchors-which-llm-reasoning-steps-matter"},{"title":"Thought Anchors: Which LLM Reasoning Steps Matter?","url":"https://www.alignmentforum.org/posts/iLHe3vLur3NgrFPFy/thought-anchors-which-llm-reasoning-steps-matter"},{"title":"Thought Anchors in LLM Reasoning","url":"https://www.emergentmind.com/papers/2506.19143"},{"title":"Paper page - Thought Anchors: Which LLM Reasoning Steps Matter?","url":"https://huggingface.co/papers/2506.19143"},{"title":"Thought Anchors: Which LLM Reasoning Steps Matter?","url":"https://arxiv.org/html/2506.19143v1"},{"title":"GitHub - interp-reasoning/thought-anchors: ⚓️ Repository for the \"Thought Anchors: Which LLM Reasoning Steps Matter?\" paper.","url":"https://github.com/interp-reasoning/thought-anchors"},{"title":"Under review as a conference paper at ICLR 2026 THOUGHT ANCHORS: WHICH LLM","url":"https://arxiv.org/pdf/2506.19143"}]

I found comprehensive information about the "Thought Anchors" paper. Here's what the research is about:

## Overview

"Thought Anchors: Which LLM Reasoning Steps Matter?" introduces a sentence-level approach to understanding and interpreting chain-of-thought (CoT) reasoning in large language models (LLMs).

## The Problem

Long-form chain-of-thought reasoning creates interpretability challenges as each generated token depends on all previous ones, making the computation harder to decompose, so analyzing reasoning traces at the sentence level is a promising approach to understanding reasoning processes.

## Key Methods

The paper presents three complementary attribution methods: (1) a black-box method measuring each sentence's counterfactual importance by comparing final answers across 100 rollouts conditioned on the model generating that sentence or one with a different meaning; (2) a white-box method of aggregating attention patterns between pairs of sentences, which identified "broadcasting" sentences that receive disproportionate attention from all future sentences via "receiver" attention heads; (3) a causal attribution method measuring logical connections between sentences by suppressing attention toward one sentence and measuring the effect on each future sentence's tokens.

## Key Findings

Plan generation, uncertainty management, and self-checking sentences consistently received the most attention via receiver heads, while active computation sentences received minimal attention, with this pattern aligning with the counterfactual importance findings, reinforcing the idea that high-level organizational sentences are more critical than computational steps.

The paper is available on arXiv at https://arxiv.org/abs/2506.19143, with code and datasets also publicly available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cb29312-5d61-42b9-b585-74239aceb25c",
  "isSidechain": false,
  "promptId": "91ae5899-f812-4435-ba43-3aeb1b84ea98",
  "type": "user",
  "uuid": "7fa73463-142c-4a5c-9a1b-7daf9def91a0",
  "toolUseResult": {
    "query": "Thought Anchors counterfactual reasoning chain-of-thought arXiv 2506.19143 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01D3B5eGtQtVXPuat1Cj5K2P",
        "content": [
          {
            "title": "[2506.19143] Thought Anchors: Which LLM Reasoning Steps Matter?",
            "url": "https://arxiv.org/abs/2506.19143"
          },
          {
            "title": "[2506.19143v2] Thought Anchors: Which LLM Reasoning Steps Matter?",
            "url": "https://arxiv.org/abs/2506.19143v2"
          },
          {
            "title": "[Literature Review] Thought Anchors: Which LLM Reasoning Steps Matter?",
            "url": "https://www.themoonlight.io/en/review/thought-anchors-which-llm-reasoning-steps-matter"
          },
          {
            "title": "Thought Anchors: Which LLM Reasoning Steps Matter? | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/thought-anchors-which-llm-reasoning-steps-matter"
          },
          {
            "title": "Thought Anchors: Which LLM Reasoning Steps Matter?",
            "url": "https://www.alignmentforum.org/posts/iLHe3vLur3NgrFPFy/thought-anchors-which-llm-reasoning-steps-matter"
          },
          {
            "title": "Thought Anchors in LLM Reasoning",
            "url": "https://www.emergentmind.com/papers/2506.19143"
          },
          {
            "title": "Paper page - Thought Anchors: Which LLM Reasoning Steps Matter?",
            "url": "https://huggingface.co/papers/2506.19143"
          },
          {
            "title": "Thought Anchors: Which LLM Reasoning Steps Matter?",
            "url": "https://arxiv.org/html/2506.19143v1"
          },
          {
            "title": "GitHub - interp-reasoning/thought-anchors: ⚓️ Repository for the \"Thought Anchors: Which LLM Reasoning Steps Matter?\" paper.",
            "url": "https://github.com/interp-reasoning/thought-anchors"
          },
          {
            "title": "Under review as a conference paper at ICLR 2026 THOUGHT ANCHORS: WHICH LLM",
            "url": "https://arxiv.org/pdf/2506.19143"
          }
        ]
      },
      "I found comprehensive information about the \"Thought Anchors\" paper. Here's what the research is about:\n\n## Overview\n\n\"Thought Anchors: Which LLM Reasoning Steps Matter?\" introduces a sentence-level approach to understanding and interpreting chain-of-thought (CoT) reasoning in large language models (LLMs).\n\n## The Problem\n\nLong-form chain-of-thought reasoning creates interpretability challenges as each generated token depends on all previous ones, making the computation harder to decompose, so analyzing reasoning traces at the sentence level is a promising approach to understanding reasoning processes.\n\n## Key Methods\n\nThe paper presents three complementary attribution methods: (1) a black-box method measuring each sentence's counterfactual importance by comparing final answers across 100 rollouts conditioned on the model generating that sentence or one with a different meaning; (2) a white-box method of aggregating attention patterns between pairs of sentences, which identified \"broadcasting\" sentences that receive disproportionate attention from all future sentences via \"receiver\" attention heads; (3) a causal attribution method measuring logical connections between sentences by suppressing attention toward one sentence and measuring the effect on each future sentence's tokens.\n\n## Key Findings\n\nPlan generation, uncertainty management, and self-checking sentences consistently received the most attention via receiver heads, while active computation sentences received minimal attention, with this pattern aligning with the counterfactual importance findings, reinforcing the idea that high-level organizational sentences are more critical than computational steps.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2506.19143, with code and datasets also publicly available."
    ],
    "durationSeconds": 7.690113369999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6cb29312-5d61-42b9-b585-74239aceb25c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-20T04:37:07.108Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have sufficient research to make my assessment. Let me synthesize everything and produce the final evaluation.

Let me think carefully about this proposal:

**What it proposes:** A dual-stream framework (ICG) that jointly tracks:
1. P*(t): Probe-based correctness awareness over time (calibrated)
2. C(t): Causal contribution of CoT text to correctness over time (via prefix truncation, paraphrase perturbation, NLDD)

The gap G*(t) = P*(t) - C(t) is the main diagnostic, and its temporal trajectory shape is the key signal.


The research question is well-grounded in documented phenomena like the diagnostic-causal gap, and the proposal distinguishes itself by making this gap the central focus rather than studying probes or causal methods in isolation. The literature review is comprehensive, positioning the work against probe-only approaches, causal-only methods, structural analyses, and within-CoT techniques to show why a dual-stream framework is necessary.

The experimental design is solid with multiple phases, clear decision gates, external validation through cross-referencing and difficulty partitions, and seven dimensions of ablation studies across multiple baselines. The compute budget of roughly 1050 H100-hours is realistic, and the proposal anticipates common reviewer concerns by directly addressing why endpoint comparison or naive combination wouldn't suffice.

The main vulnerability I'm seeing is whether P*(t) and C(t) are truly commensurable—P*(t) measures probe discrimination via AUROC while C(t) operates on a different scale entirely, which could undermine the core comparison. ), while C(t) is behavioral accuracy change under intervention. These are fundamentally different quantities. The proposal acknowledges this and proposes rank-based normalization and shape-based analysis, but a reviewer could still argue the subtraction G*(t) = P*(t) - C(t) is conceptually ill-defined. The shapes-over-magnitudes defense is partially convincing but doesn't fully resolve the issue — shape features like "convergence toward zero" still require some notion of comparability.

2. **Complexity and over-engineering**: The framework has many moving parts — 3 C(t) estimators, 4 probe layers, rank normalization, MCT concordance, multiple aggregation schemes, 7 ablation dimensions. A reviewer might ask: is this complexity necessary, or is a simpler approach sufficient?

3. **Validation challenge**: The core problem is grounding what "faithful" reasoning actually means. I'm relying on external validators like TTS and FaithCoT-Bench, but these are indirect proxies. The semi-synthetic simulation helps generate hypotheses but can't definitively establish ground truth — a fundamental limitation in faithfulness research.

4. **Novelty concern**: A skeptical reviewer might see this as engineering existing components together rather than introducing a fundamentally new insight. The dual-stream architecture is conceptually clean, but probes, truncation, and perturbation are all established techniques.

5. **Scalability**: The work focuses on 7B-32B models, and reviewers will likely question how this scales to 70B+ models. The 671B subset only has 500 examples across 3 layers, which is quite limited.

6. **Diagnostic signal claim**: While I cite evidence that shape features carry signal in other domains, applying this specifically to G*(t) shapes for faithfulness detection is a leap that needs stronger empirical grounding.

7. **Presentation density**: The proposal is extremely dense and would need significant streamlining for a paper to be accessible to reviewers.

The proposal is well-researched and addresses a genuine gap — no existing method combines probe awareness with temporal causal contribution. The experimental design is thorough with appropriate gates. But the core issue of whether the dual streams are truly commensurable remains unresolved, and the validation challenge is real since there's no ground truth for faithfulness.

I'm noticing the venue mismatch — the proposal targets ICLR/ICML 2027, not EMNLP 2026 as stated, though it does fit EMNLP's scope as an interpretability paper. Weighing the strong research question and phased approach against the methodological concerns and complexity, I'm thinking this lands around 30-42% acceptance probability. It's solid work that hinges on strong empirical results, but the commensurability question is a real obstacle. Actually, stepping back — the proposal is remarkably thorough. The phased gates are excellent, the literature positioning is outstanding, and the differentiation from competitors is crystal clear and well-argued.

But a real reviewer would likely push back on the conceptual soundness of subtracting probe AUROC from behavioral accuracy, question whether all these moving parts justify the complexity, and worry that the validation relies too heavily on indirect proxies. There's also the fundamental risk that the shapes could just be noise. Balancing the genuine strengths against these legitimate methodological concerns, I'm settling on 28-40%, with a median around 34%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fa73463-142c-4a5c-9a1b-7daf9def91a0",
  "isSidechain": false,
  "requestId": "req_011CbDCZU39zRzysfEoJbbo8",
  "type": "assistant",
  "uuid": "36ffc147-b8d6-4084-bc8e-3cbf038e58bc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XWjUZ6SYbyvAKtxhDSPg7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 664,
      "cache_creation_input_tokens": 1075,
      "cache_read_input_tokens": 33527,
      "output_tokens": 6476,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1075,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 664,
          "output_tokens": 6476,
          "cache_read_input_tokens": 33527,
          "cache_creation_input_tokens": 1075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1075
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

_source line 42 · 2026-05-20T04:38:55.990Z_

Now I have sufficient research to make a thorough assessment. Let me compile my evaluation.

```
【阶段】: Triage

【领域调研】:
- [Monitoring the Internal Monologue: Probe Trajectories (Chrabąszcz et al., arXiv 2605.18549)](https://arxiv.org/abs/2605.18549) (May 2026): 最直接的竞争者之一。在 reasoning model 上用 per-token probe 构建轨迹，60+ 信号处理特征，max-pooling 达 91-97% AUROC。关键限制：完全没有 causal 维度，无法区分 faithful-correct vs. unfaithful-correct。ICG 的 probe 端正是要站在这个工作的肩上。
- [Hidden Error Awareness (Yuan et al., arXiv 2605.09502)](https://arxiv.org/abs/2605.09502) (May 2026): 系统验证了 diagnostic-not-causal 现象——0.95 AUROC probe 准确率，但四种 intervention 全部失败。这是 ICG 框架立论的核心经验基础之一。非常新的工作，ICG 的 research question 直接建立在此发现之上。
- [Decoding Answers Before CoT (Cox et al., arXiv 2603.01437)](https://arxiv.org/abs/2603.01437) (March 2026): 发现 instruction-tuned model 上 steering 可以翻转答案 (>50%)，但 reasoning model 上翻转率 negligible。与 Yuan et al. 互相印证了 diagnostic-causal gap 在 reasoning model 上的独特性。
- [Probing the Trajectories of Reasoning Traces (Ballon et al., arXiv 2601.23163)](https://arxiv.org/abs/2601.23163) (Jan 2026): 提出 truncation-reinjection 协议测量 behavioral C(t)，在 Qwen/GPT-OSS 上实验，accuracy 从 30-42% 升到 49-73%。关键限制：没有 hidden-state 测量，且明确 disclaims faithfulness 分析。ICG 的 C(t) 端直接继承此方法。
- [FaithCoT-Bench (ICLR 2026, arXiv 2510.04040)](https://arxiv.org/abs/2510.04040): 1000+ expert-annotated 轨迹，11 种检测方法的统一 benchmark。这是 ICG 的主要外部验证标准之一，也是头对头比较的关键对手。
- [True Thinking Score / TTS (Zhao et al., arXiv 2510.24941)](https://arxiv.org/abs/2510.24941): per-step marginal causal contribution，AIME 上只有 2.3% 的步骤 TTS≥0.7。ICG 明确区分了 cumulative sufficiency (自己的 C(t)) vs. marginal contribution (TTS)。
- [LLM Reasoning Is Latent (Wang, arXiv 2604.15726)](https://arxiv.org/abs/2604.15726) (April 2026): 形式化 H1(latent-mediated)/H2(CoT-mediated)/H0 假设，结论倾向 H1。ICG 声称可以操作化 H1/H2 区分。
- [When Chains of Thought Don't Matter / CMI (Sathyanarayanan et al., arXiv 2602.03994)](https://arxiv.org/abs/2602.03994) (Feb 2026): layerwise activation patching 衡量 CoT 结构介导，~50 examples。ICG 区分了 structural mediation (CMI) vs. functional contribution (自己)。
- [Thought Anchors (arXiv 2506.19143)](https://arxiv.org/abs/2506.19143): sentence-level counterfactual importance via 100-rollout replacement sampling，识别对推理轨迹有重大影响的 "anchor" 句子。提供 within-CoT 因果结构，但无 probe 外部参照。

- **调研总结**: CoT faithfulness 是 2025-2026 年 NLP 可解释性最活跃的方向之一，probe 端和 causal 端各有大量独立工作，但确实没有人将二者在时间维度上统一。ICG 的 niche（dual-stream temporal gap）在文献中确实是空白的。但该领域竞争激烈、工作密集，多个同期竞争者可能在 proposal 完成前填补类似空白。

【整体印象】:
如果我是审稿人，第一反应是：这是一份学术功底极深、文献调研极其扎实的 proposal，研究问题真实且有价值。但第二反应是：(1) 框架核心操作——P*(t) 与 C(t) 的相减——在概念层面存在不可通约性问题；(2) 系统整体复杂度非常高，可能过度工程化；(3) faithfulness ground truth 的缺失使验证只能依赖间接代理。我会倾向 borderline，需要看实验结果才能决定 accept 或 reject。如果 Phase 0b 的效果量显著 (d > 0.5)，这会是一篇 solid 的贡献；如果效果量不够，整个框架的说服力会大打折扣。

【核心贡献】:
核心贡献是提出第一个能区分 "faithful-correct" vs. "unfaithful-correct" 推理的诊断框架：通过同时追踪模型内部的信息可用性 (probe) 和 CoT 文本的因果贡献 (behavioral intervention)，用二者的时间轨迹差异（G*(t) 形状）来分类不同的 faithfulness 现象。这个贡献对领域有中等偏高的价值——它试图将分散的 probe 和 causal 两大研究传统统一起来，如果成功，可以为 CoT faithfulness 提供一个更精细的诊断工具。但其价值很大程度上取决于 G*(t) 形状是否真的能稳健地区分不同现象。

【方法合理性】:
方法的整体设计方向是合理的——probe 端继承 Chrabąszcz/David/Yuan 的成熟方法，causal 端继承 Ballon 的 truncation-reinjection + 扰动方法，都有坚实的先验支撑。但存在三个核心问题：

(1) **不可通约性**：P*(t) 是 AUROC（分类判别能力），C(t) 是 accuracy change（行为差异）。这两个量纲根本不同，直接相减在数学上没有意义。Proposal 承认了这一点并用 rank normalization + "shapes over magnitudes" 来辩护，但 rank normalization 后的轨迹形状仍然受到两个流各自 noise profile 和 granularity 的影响。如果 P*(t) 在 20 个 position 上平滑缓变，而 C(t) 因为 truncation 点数量有限而呈阶梯状，那么 G*(t) 的形状主要反映 C(t) 的离散化伪影，而非真正的 faithfulness 信号。这是一个比 proposal 承认的更严重的问题。

(2) **更简单的替代方案**：一个显然的替代方案是不做减法，而是直接用 P*(t) 和 C(t) 各自的轨迹特征作为联合特征输入分类器。这避免了不可通约性问题，且可能获得类似甚至更好的分类性能。Proposal 确实在 ablation 中对比了 probe-only 和 TTS-only，但没有测试"联合特征但不做 gap"这个自然基线——审稿人几乎一定会问这个问题。

(3) **Ground truth 缺失**：Faithfulness 本身缺乏可靠的 ground truth。FaithCoT-Bench 的 expert annotations 是目前最好的，但覆盖有限且主观性不可忽视。Proposal 使用 difficulty partition 和 TTS 作为外部验证，但这些都是间接代理——difficulty 和 faithfulness 的关系是 assumed 而非 proven 的。

【5 维度打分】:
  1. 研究问题: 【强】— Diagnostic-causal gap 是一个真实的、被多个独立团队验证的现象 (Yuan et al. 2605.09502, Cox et al. 2603.01437)，将其从 "obstacle" 转为 "object of study" 是一个有洞察力的 reframing。问题的重要性和时效性都很高。CoT faithfulness 是当前 NLP 可解释性的核心问题，对 AI safety 有直接意义。

  2. 方法与创新: 【中】— Dual-stream 的概念框架是清晰的且填补了真实的文献空白（Chrabąszcz 无 causal，Ballon 无 probe，CMI 是 structural 而非 functional，Thought Anchors 无外部参照）。但创新主要在框架层面而非方法层面——个体组件 (linear probe, truncation-reinjection, paraphrase perturbation, NLDD) 全部是现有工具的组合。P*(t) 与 C(t) 的不可通约性是核心方法论弱点，shapes-over-magnitudes 的辩护虽有 trajectory 文献支撑 (arXiv 2603.18940, 2602.06266, 2604.05655)，但这些支撑来自不同上下文，对本场景的 transferability 未经验证。缺少"联合特征但不做 gap"这个自然消融基线。

  3. 实验设计: 【强】— 这是 proposal 最突出的优点之一。5 models × 4 benchmarks 的覆盖面充分；Phase 0a/0b 的 go/no-go 门控是成熟的研究实践；7 维消融非常全面；多个外部验证标准 (TTS cross-reference, difficulty partition, FaithCoT-Bench)；cross-model 泛化测试 (train A → test B)；统计严谨性 (bootstrap CI, Bonferroni correction, permutation tests)。与领域标准 (FaithCoT-Bench 的 4 种方法, TTS) 的 head-to-head 对比也是该有的。但缺少"P*(t)+C(t) 联合特征不做减法"作为 baseline。instruction-tuned control (Qwen2.5-7B-Instruct) 作为 sanity check 也是好设计。

  4. 可行性: 【中】— ~1050 H100-hours 在学术实验室可承受范围内；15-17 周时间线合理但紧张。主要风险：(a) NLDD 在自然 benchmark 上的可行性未验证（Phase 0a 测试，但如果失败需要调整方案）；(b) paraphrase perturbation 的语义保持验证 (NLI-based) 可能引入 noise；(c) 32B 模型上的 NLDD 是计算瓶颈 (250 hrs)；(d) 整个框架依赖 Phase 0b 的 d > 0.5 结果，如果不成立需要大幅降级。Phase 0b 的 go/no-go 设计是明智的，但也意味着有非零概率整个项目需要 pivot。

  5. 写作与呈现: 【中】— Proposal 的逻辑结构清晰，文献定位极其精确（每个竞争者的优势和不足都有细致对比），预判并回应审稿人 objection 的做法非常专业。但过于密集——实际论文需要大幅精简，否则审稿人会因信息过载而降低好感。某些地方有 over-claim 风险（如 "the first framework capable of distinguishing faithful-correct from unfaithful-correct reasoning"——这在 P*(t)-C(t) 不可通约性未完全解决前是 aggressive 的 claim）。

【概率估计】: [28% - 42%] 中位 35%

【估计理由】:
**向上因素**：(1) 研究问题真实、重要、时效性强；(2) 文献空白是真实存在的——确实没有 dual-stream temporal 框架；(3) 实验设计非常完备，go/no-go 门控、7 维消融、多重外部验证；(4) honest scoping（2 vs 3 category）是加分项；(5) 与 Thought Anchors、CMI、TTS、Chrabąszcz 的差异化论证清晰有力。

**向下因素**：(1) P*(t) 与 C(t) 的不可通约性是核心方法论弱点，rank normalization + shapes 的辩护可能不足以说服严格审稿人；(2) 创新主要在"框架组合"而非"方法突破"——所有组件都是现有工具，审稿人可能判定为 engineering contribution；(3) ground truth 缺失，验证只能依赖间接代理，分类的 "正确性" 无法严格确认；(4) 该领域竞争极度激烈（2025-2026 已有 30+ 篇相关工作），提交时可能已有类似思路的工作出现；(5) 缺少"联合特征不做 gap"这个自然基线，审稿人大概率会指出。

中位 35% 反映了这是一篇方向正确、设计扎实但存在核心方法论争议的 proposal。如果 Phase 0b 效果量优异且能补上"不做 gap"的消融，概率可上探 40%+。如果 G*(t) 形状的区分能力不够 robust，或审稿人对不可通约性严厉批评，概率会降到 28% 以下。

【主要风险】:
1. **P*(t)-C(t) 不可通约性遭到 fundamental objection**：审稿人认为 AUROC 与 accuracy change 的相减在概念上不成立，rank normalization 不足以解决问题，且"shapes over magnitudes"的辩护缺乏在本具体场景的直接验证。这可能被视为方法论的 fatal flaw。
2. **"组合而非创新" 的评判**：审稿人认为框架只是将 Chrabąszcz 的 probe + Ballon 的 truncation 简单拼接，没有引入根本性的新洞察或新方法，核心贡献不足以达到 venue 标准。尤其是如果"联合特征不做 gap"的 baseline 表现与 G*(t) 相当或更好，会严重削弱框架的存在价值。

【实施评估】:
  - 计算资源: ~1050 H100-hours，约 $3,200（按 $3/hr），学术可承受。32B NLDD 是瓶颈 (250 hrs)。
  - 数据需求: 公开 benchmark (GSM8K, MATH-500, GPQA-Diamond, AIME)，无需新数据收集。FaithCoT-Bench (ICLR 2026) 作为外部验证标准需确认 instance-level 数据可获取性。
  - 人工介入: 无需人工标注（依赖已有 benchmark 和自动化方法）。Paraphrase 生成由 API 完成。
  - 训练需求: 无大规模模型训练。需训练 linear probes（轻量）和小型分类器 (logistic regression/RF/MLP)。所有目标模型使用现有权重。
  - 新 Benchmark: 不构建新 benchmark。TIF Score 是新指标但不是 benchmark。
  - 预估周期: 15-17 周 (2 researchers) 或 12-14 周 (1 researcher + Claude)。Phase 0b 在第 4 周提供 go/no-go 信号。
```

Sources:
- [Monitoring the Internal Monologue: Probe Trajectories (Chrabąszcz et al.)](https://arxiv.org/abs/2605.18549)
- [Hidden Error Awareness (Yuan et al.)](https://arxiv.org/abs/2605.09502)
- [Decoding Answers Before CoT (Cox et al.)](https://arxiv.org/abs/2603.01437)
- [Probing the Trajectories of Reasoning Traces (Ballon et al.)](https://arxiv.org/abs/2601.23163)
- [FaithCoT-Bench (ICLR 2026)](https://arxiv.org/abs/2510.04040)
- [True Thinking Score / TTS (Zhao et al.)](https://arxiv.org/abs/2510.24941)
- [LLM Reasoning Is Latent (Wang)](https://arxiv.org/abs/2604.15726)
- [When Chains of Thought Don't Matter / CMI (Sathyanarayanan et al.)](https://arxiv.org/abs/2602.03994)
- [Thought Anchors](https://arxiv.org/abs/2506.19143)
- [Mechanistic Evidence for Faithfulness Decay / NLDD (Ye et al.)](https://arxiv.org/abs/2602.11201)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36ffc147-b8d6-4084-bc8e-3cbf038e58bc",
  "isSidechain": false,
  "requestId": "req_011CbDCZU39zRzysfEoJbbo8",
  "type": "assistant",
  "uuid": "6a5ac71f-43c2-4d80-8ef3-404f4f2531b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XWjUZ6SYbyvAKtxhDSPg7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 664,
      "cache_creation_input_tokens": 1075,
      "cache_read_input_tokens": 33527,
      "output_tokens": 6476,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1075,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 664,
          "output_tokens": 6476,
          "cache_read_input_tokens": 33527,
          "cache_creation_input_tokens": 1075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1075
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

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-T…",
  "leafUuid": "6a5ac71f-43c2-4d80-8ef3-404f4f2531b3",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Temporal information-contribution gap analysis for reasoning faithfulness",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-T…",
  "leafUuid": "6a5ac71f-43c2-4d80-8ef3-404f4f2531b3",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Temporal information-contribution gap analysis for reasoning faithfulness",
  "sessionId": "9f054eab-0d77-4538-b834-27b44a1162e3"
}
```

---
