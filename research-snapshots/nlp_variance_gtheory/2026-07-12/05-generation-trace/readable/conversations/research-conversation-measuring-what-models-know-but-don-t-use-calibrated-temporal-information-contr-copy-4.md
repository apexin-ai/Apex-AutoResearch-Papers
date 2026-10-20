# Research conversation: Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought F

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-3/e23dd0d5-f3b9-4a43-8fe0-00654e6600fd.jsonl`
- **Structured JSON:** [`2f042669fcc96f1d4cd5.json`](../../sessions/2f/2f042669fcc96f1d4cd5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:05:12.439Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:05:12.439Z",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "content": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness\n\n## Description\nWe propose the Information-Contribution Gap (ICG) framework, a calibrated temporal diagnostic for chain-of-thought faithfulness that exploits a robust empirical finding: linear probes on hidden states reliably diagnose answer correctness (0.82-0.95 AUROC across four independent groups) yet causal interventions based on these probes consistently fail on reasoning-trained models (Cox et al.: negligible flip rates; Yuan et al.: all four intervention strategies fail). Rather than treating this diagnostic-causal gap as an obstacle, we make it the primary object of study — the gap between what models internally know and what their CoT causally contributes IS the faithfulness signal.\n\nThe framework tracks two calibrated time-varying quantities across the full CoT trajectory: P*(t), null-probe-calibrated correctness awareness, and C(t), causal contribution estimated via three complementary methods (prefix truncation with Ballon et al.'s three control conditions, paraphrase perturbation, NLDD). Their divergence G*(t) = P*(t) − C(t) produces phenomenon-specific temporal fingerprints, operationalizing Wang's (2604.15726) H1/H2 distinction: G*(t) >> 0 is latent-mediated (H1-consistent), G*(t) ≈ 0 is CoT-mediated (H2-consistent).\n\n**Core insight: the diagnostic contribution of G*(t) is its temporal trajectory shape — not its absolute magnitude.** Because P*(t) and C(t) are measured via fundamentally different methods (probe AUROC vs. behavioral accuracy change), their absolute scales are not directly commensurable. We address this via rank-based normalization as primary scheme, but more fundamentally, we show that the trajectory-shape profile of G*(t) — its initial value regime, slope dynamics, convergence/divergence patterns — carries the diagnostic signal. A model that pre-encodes the answer shows a constant-high shape regardless of absolute scale; a model that genuinely reasons shows a converging shape; post-hoc rationalization shows a widening shape. This shapes-over-magnitudes approach is validated by the trajectory-shape literature: entropy trajectory monotonicity predicts reliability regardless of absolute levels (+5.8pp, arXiv 2603.18940); RQA temporal features outperform aggregates (36.94% vs. 28.97%, arXiv 2602.06266); Microsoft trajectory geometry achieves 0.852 AUC from shape features vs. 0.649 baseline (arXiv 2604.05655).\n\n**Why temporal trajectories, not just endpoint comparison?** A reviewer might ask: \"Why not just correlate pre-CoT probe accuracy with final correctness?\" The answer: endpoint comparison detects the *presence* of unfaithfulness but collapses distinct failure *mechanisms* into a single label. Pre-CoT encoding and post-hoc rationalization both produce \"high probe accuracy + low causal contribution\" at endpoints, but yield distinct G*(t) shapes (constant-high vs. widening). \"Genuine reasoning with late failure\" (model reasons faithfully for 80% of the chain, then shortcuts) shows G*(t) ≈ 0 then spiking — invisible to any static measurement. The temporal framework's value is mechanistic discrimination, not just detection.\n\nPositioned against the closest concurrent work — Chrabąszcz et al.'s (2605.18549) probe trajectories with 60+ signal-processing features achieving up to 17pp improvement over static probes — our framework addresses a qualitative blindspot in their single-stream design: Chrabąszcz et al. answer \"what does the model know over time?\" (outcome prediction), but cannot distinguish *faithful-correct* from *unfaithful-correct* reasoning. A model that pre-encodes the answer and generates decorative CoT looks identical to a model that genuinely reasons in their framework (both show high probe accuracy throughout), but looks radically different in ICG (the former has persistent G*(t) >> 0, the latter has G*(t) converging to 0). This faithful-vs-unfaithful distinction is structurally impossible from probe trajectories alone — it requires the causal contribution dimension.\n\nWe further differentiate from the CMI framework (Sathyanarayanan et al., 2602.03994), which measures whether answer representations pass through CoT-aligned layers via layerwise activation patching — a *structural* question (\"does the computational path go through CoT?\"). ICG answers a *functional* question (\"does the CoT text causally contribute to correctness?\"). A model could have high CMI (representations routed through CoT-processing layers) but high G*(t) (the CoT text serves as a timing scaffold rather than contributing semantic content). This structural-vs-functional distinction is novel.\n\n**Interpretive boundary.** We explicitly acknowledge: G*(t) >> 0 means correctness-correlated information is present in hidden states but not causally channeled through CoT text. It does not necessarily mean the model \"decided to withhold\" — the information may exist as computational byproducts (statistical regularities in activations) rather than semantically actionable knowledge. Chun et al.'s MCT finding (2602.20338) — geometric separability peaks transiently while probe accuracy remains high — provides direct evidence of this possibility. Null-probe calibration addresses uniform inflation but not this deeper question. We use MCT concordance as supplementary validation and report G*(t) interpretations with this caveat.\n\n**Practical significance beyond faithfulness measurement.** The ICG framework addresses questions the field urgently needs answered: (a) *Inference-time compute allocation*: when G*(t) >> 0 for easy problems, CoT is decorative overhead — don't generate it; (b) *Benchmark validity*: problems where all models show persistent G*(t) >> 0 are not testing reasoning regardless of accuracy scores; (c) *Safety monitoring*: the decoupled internal quality-monitoring system identified by Yuan et al. (the model internally knows it's wrong but doesn't course-correct) is exactly the kind of hidden computation alignment researchers worry about.\n\nWe adopt honest scoping: 2-3 faithfulness phenomena (pre-CoT encoding, genuine reasoning, post-hoc rationalization) as the realistic classification target, with steganographic encoding and reasoning theater as stretch goals. A new empirical pilot phase (Phase 0b) validates phenomenon separability on real data using external classification standards (difficulty-based partition and FaithCoT-Bench ground truth) before committing to the full pipeline. Task-difficulty conditioning — grounded in David's easy (0.84) vs. hard (0.76) probe splits and Gjølbye et al.'s (2605.15454) demonstration that difficulty-geometry coupling is systematic (ρ⊥ = +0.41 on Codeforces) but domain-specific — reveals the decorative→load-bearing transition with length correction (residualizing on log(N)).\n\nThe paper focuses on four core contributions: (a) calibrated ICG diagnostic with shape-based trajectory analysis on 4 models × 4 benchmarks, positioned against Chrabąszcz et al. and CMI to demonstrate the value of the dual-stream functional gap; (b) empirical pilot validating that 2-3 phenomena produce distinguishable G*(t) trajectory shapes on real data using external validation standards; (c) difficulty-conditioned gap analysis with domain-specific nuance; (d) head-to-head comparison against TTS, FaithCoT-Bench methods, and probe-only trajectories demonstrating the incremental value of the causal contribution dimension. Total compute: ~830 H100-hours, with NLDD on 32B models (~250 hrs, conditional on Phase 0a feasibility) as the primary bottleneck.\n\n## Core Problem\nA striking convergence of 2025-2026 findings reveals a fundamental disconnect in reasoning language models: their hidden states reliably encode information about answer correctness — with linear probes achieving 0.82-0.95 AUROC across multiple independent groups — yet causal interventions based on these probes consistently fail to influence model outputs. Cox et al. (2603.01437) find that steering via answer-content probes produces answer flip rates 'negligible against the orthogonal baseline' on reasoning models, despite >0.9 AUC on instruction-tuned models. Yuan et al. (2605.09502) systematically test four distinct intervention strategies (activation steering, probe-guided best-of-N, self-correction, activation patching) on models up to 72B parameters and report that ALL fail: 'RL training does not close the diagnostic–causal gap.' This diagnostic-causal gap — the divergence between what information is available in a model's hidden states and what information the chain-of-thought reasoning text causally contributes — is NOT a methodological obstacle to overcome; it IS the central phenomenon. Critically, the literature conflates two distinct probe targets: answer-content probes (Cox et al.: predicting the specific answer on binary tasks, models ≤9B + GPT-OSS-20B) and correctness probes (Yuan et al.: predicting right/wrong on models up to 72B; Zhang et al.: per-chunk correctness on 7B-70B). This distinction matters because the gap's interpretation differs: answer-content gaps mean 'the model has already decided but CoT doesn't derive the answer,' while correctness gaps mean 'the model knows it's right/wrong but CoT doesn't reflect this awareness.' Meanwhile, the temporal dynamics of this gap are now empirically grounded: David (2511.14773) shows probe accuracy stabilizes at 0.84 AUC by token 4, remaining ~0.8 through token 100, with task-difficulty conditioning revealing easy (0.84) vs. hard (0.76) signatures. Zhang et al. (2504.05419) report chunk-level probe trajectories rising from 65% at 10% of reasoning to 79% at 100% on R1-Distill. Esakkiraja et al. (2604.01202) find >90% pre-generation AUROC with a characteristic dip at 5-10% of reasoning followed by recovery. Chrabąszcz et al. (2605.18549) demonstrate that temporal probe trajectories with 60+ signal-processing features achieve up to 17pp improvement over static probes, showing that trajectory dynamics capture information invisible to single-timepoint measurements. These temporal profiles suggest that different modes of CoT unfaithfulness — pre-CoT encoding, post-hoc rationalization, reasoning theater, myopic planning, thinking-answer gap — produce distinguishable temporal divergence signatures. Yet no existing framework jointly tracks information availability AND causal contribution across the full CoT timeline: Chrabąszcz et al. provide the closest probe-trajectory methodology but lack any causal contribution component, gap metric, probe calibration, or phenomenon taxonomy; Ballon et al. (2601.23163) provide behavioral causal curves via truncation-reinjection but lack hidden-state measurement; the CMI framework provides layerwise causal audit on ~50 examples but measures structural mediation (whether representations route through CoT layers) rather than functional contribution (whether CoT text causally affects correctness); Zhao et al.'s True Thinking Score provides per-step causal contribution but no probe-side measurement. The gap between diagnostic information availability and causal contribution IS the phenomenon of interest, not an obstacle.\n\n## Opportunity\nThe field has independently produced the measurement tools needed for a unified temporal framework, but these tools remain siloed. The opportunity is fourfold:\n\n(1) **Temporal gap measurement.** Despite rapid accumulation of probe measurements (David: 0.84 at t=4; Zhang: 0.82-0.91 on chunks; Yuan: 0.95 overall, 0.787 first-step; Esakkiraja: >90% pre-generation; Chrabąszcz et al.: 91-97% AUROC with max-pooling on trajectories), no work tracks the full-timeline divergence between probe-estimated information availability and intervention-estimated causal contribution. Chrabąszcz et al. (2605.18549) come closest on the probe side — extracting 60+ signal-processing features from probe trajectories across 4 reasoning models and 4 datasets, achieving up to 17pp improvement over static probes on GSM8K — but they target outcome prediction (correctness, harmfulness) rather than the faithfulness gap, and provide no causal contribution measurement. Critically, their framework is structurally blind to the faithful-correct vs. unfaithful-correct distinction: a model that pre-encodes answers and a model that genuinely reasons look identical in their single-stream design. Our framework extends this via the dual-estimator gap G*(t) = P*(t) − C(t) that enables this distinction. On the causal side, Ballon et al. (2601.23163) provide behavioral C(t) curves via truncation-reinjection at decile intervals on Qwen3/gpt-oss across GPQA-Diamond and MMLU-Pro — showing monotonic accuracy increase from 30.8-42.3% to 49.0-73.1% with control conditions validating that sequential content (not just context length) matters — but lack hidden-state measurement.\n\n(2) **Phenomenon unification with honest scoping.** The CoT faithfulness literature treats each failure mode as separate: Reasoning Horizon (Ye et al. 2602.11201), pre-CoT encoding (Cox et al. 2603.01437; Esakkiraja et al. 2604.01202), Reasoning Theater (Boppana et al. 2603.05488), myopic planning (Xu et al. 2602.02103), thinking-answer gap. We propose that 2-3 of these are confidently distinguishable via trajectory-shape signatures in G*(t), with 4-5 as a stretch goal. The honest scoping — validated through an empirical pilot on real data with external classification standards before committing to full classification — is itself a contribution to a field prone to over-claiming.\n\n(3) **Task-difficulty conditioning.** The ICLR 2026 Workshop finding and Li et al.'s (2510.22362) corroboration show easy→decorative, hard→faithful. David's easy/hard splits (0.84 vs. 0.76 at t=32) provide probe-level evidence. Gjølbye et al. (2605.15454) demonstrate that difficulty is systematically coupled to hidden-state trajectory geometry even after length correction (ρ⊥ = +0.41 for reasoning models vs. −0.06 for baselines on competitive programming), with domain-specific strength. A difficulty-conditioned gap framework answers the practical question: at what difficulty level does CoT transition from decorative to load-bearing? This has direct implications for inference-time compute allocation (skip CoT on easy problems) and benchmark validity (problems where all models show G*(t) >> 0 are not testing reasoning).\n\n(4) **Probe target clarification.** The field has not confronted the distinction between answer-content probes (Cox et al.: binary tasks, ≤9B) and correctness probes (Yuan et al.: up to 72B). A framework that explicitly measures correctness awareness gap — and contrasts it with answer-content gap on applicable tasks — provides the first principled treatment of what 'knowing but not using' means.\n\nTwo prior works have combined probing with causal interventions: Kudo et al. (EACL 2026) on synthetic arithmetic, and the CMI framework (2602.03994) on ~50 examples. The CMI framework provides *structural* causal mediation (layerwise activation patching measuring whether representations route through CoT layers), while our framework provides *functional* causal assessment (whether the CoT text itself causally contributes to behavioral correctness). Wang (2604.15726) formalizes the need via competing hypotheses (H1: latent-mediated, H2: CoT-mediated, H0: serial compute) — our ICG framework provides an empirical methodology to distinguish H1 from H2 at each temporal position. Neither Kudo et al. nor CMI provides: (a) full temporal-position coverage on natural benchmarks, (b) mapping to named faithfulness phenomena, (c) a standalone instance-level diagnostic, (d) systematic multi-model comparison, (e) robustness validation — a critical gap highlighted by Young's (2603.20172) finding that faithfulness measurements are classifier-sensitive (inter-classifier kappa as low as 0.06), or (f) an empirical pilot with external validation standards.\n\n## Landscape\n**Probe-based temporal measurement (foundational for our P*(t) component).** Chrabąszcz et al. (2605.18549) is the closest concurrent work: they introduce probe trajectories — tracking concept probability at each generated token — and extract 60+ signal-processing features (volatility, trend, steady-state, temporal segmentation, boundary transients, autocorrelation) via 3-layer MLP probes with Multi-Instance Learning meta-probe across layers. Key results: max-pooling achieves 91-97% AUROC on harmfulness detection (vs. 33-61% for average-pooling); up to 17pp improvement over static probes on GSM8K across Llama-8B-R1-Distill and Qwen3-4B/8B/14B (~3000 GPU-hours total). Critical differentiators from our framework: (a) NO causal contribution component; (b) NO gap metric; (c) NO null-probe calibration or MCT validation; (d) NO phenomenon taxonomy — they separate correct/incorrect or safe/harmful, not faithfulness modes; (e) NO task-difficulty conditioning; (f) structurally cannot distinguish faithful-correct from unfaithful-correct reasoning (both produce high probe accuracy, but only the dual-stream ICG can separate them via the C(t) dimension). Their 60+ feature extraction methodology is complementary and could enhance our trajectory-shape classification. David (2511.14773) trains per-position probes on reasoning models, finding 0.84 AUC at t=4, stable ~0.8 through t≈100, with easy/hard splits of 0.84 vs. 0.76 at t=32 on Qwen3-8B. Zhang et al. (2504.05419) probe R1-Distill models (7B/32B/70B) for correctness at each reasoning chunk, achieving 0.82-0.91 AUROC on GSM8K/MATH/AIME, with a rising trajectory from 65% at 10% chunk to 79% at 100%, enabling 24% token reduction via early-exit. Yuan et al. (2605.09502) report 0.95 AUROC on Qwen-3B, 0.852 on DeepSeek-R1-7B, 0.787 from first-step hidden states alone, and a concealment gap of 0.197 AUROC between hidden-state (0.787) and text-surface (0.590) classifiers — using correctness probes (right/wrong). Esakkiraja et al. (2604.01202) find >90% AUROC pre-generation on Qwen3-4B and GLM-Z1-9B, with a characteristic dip at 5-10% of reasoning and recovery to near-100% by think_end. Cox et al. (2603.01437) use answer-content probes achieving >0.9 AUC on instruction-tuned Gemma-2 (2B, 9B) and Qwen-2.5 (1.5B, 3B, 7B) models, but 'the answer flip rate is negligible against the orthogonal baseline' on the reasoning model GPT-OSS-20B. Additional probing work: Qian et al. (2506.02867, NeurIPS 2025); Lewis-Lim et al. (2508.19827, EMNLP 2025); Mirtaheri & Belkin (2603.17199); Occhipinti et al. (ICLR 2026 LIT Workshop, probing F1 90-100%, steering 46% recovery).\n\n**The diagnostic-not-causal evidence (motivating our framework).** Yuan et al. (2605.09502) is the decisive study: four interventions — activation steering (at most +4%), probe-guided best-of-N (matches random), self-correction (hurts accuracy −3%), activation patching (destroys coherence at α=0.5) — all fail. Tested on Qwen2.5 (1.5B-72B), Llama-3.1-8B, Phi-3.5-mini, DeepSeek-R1-7B. Key quote: 'The error signal is a diagnostic readout—a summary statistic of computation quality—not a causal component that can be edited.' Cox et al. (2603.01437) independently confirm: steering fails on reasoning models despite high probe accuracy. This establishes that probe accuracy ≠ causal potency on reasoning models.\n\n**Behavioral trajectory probing (foundational for our C(t) component).** Ballon et al. (2601.23163) introduce the truncation-reinjection protocol: generate full reasoning traces on Qwen3-4B/8B/14B and gpt-oss-20B/120B, truncate at decile intervals (10-100%), reinject with early-stopping suffix, measure answer-choice probability distributions. Key results: accuracy increases monotonically from 30.8-42.3% to 49.0-73.1% on GPQA-Diamond; three control conditions validate causal content: random tokens (+2.1-4.3%), swapped traces (+3.2-8.7%), and shuffled tokens (+0.3-10.8%) all substantially underperform intact truncated traces (+18.1-33.1%). Explicitly disclaims faithfulness-to-internal-computations analysis. Zhao et al. (2510.24941) introduce the True Thinking Score (TTS), measuring per-step causal contribution via numerical perturbation and ATE computation on DeepSeek-R1-Distill-Qwen-7B/14B/Llama-8B across AIME/MATH/AMC/CommonsenseQA, finding only 2.3% of AIME steps have TTS≥0.7. Ye et al. (2602.11201) introduce NLDD, finding a Reasoning Horizon at 70-85% of chain length on 3 models across synthetic tasks (syntactic, logical, arithmetic — natural benchmark generalizability remains unvalidated). Basu & Chakraborty (2603.22816) propose a decorative/scaffolding/genuine taxonomy. FACT-E (Sun et al. 2604.10693, ACL Findings 2026) provides another causal measurement approach.\n\n**Probe-intervention combinations (closest prior work).** Kudo et al. (2412.01113, EACL 2026) train per-position linear probes and validate with sliding-window activation patching on 9 models across synthetic multi-step arithmetic — CoT IS faithful for arithmetic but explicitly note their synthetic setting may not generalize. The CMI framework (2602.03994) introduces the CoT Mediation Index via layerwise activation patching across Phi, Qwen, DialoGPT on StrategyQA (20), TruthfulQA (10), GSM8K (20), identifying 'bypass regimes' where CMI ≈ 0. CMI measures *structural mediation* — whether the answer's latent representation passes through CoT-aligned layers — which is a different question from ICG's *functional contribution* — whether the CoT text itself causally contributes to behavioral correctness. A model could have high CMI (representations routed through CoT layers) but high G*(t) (the CoT text serves as a timing scaffold without semantic contribution). Both are complementary precursors operating on small samples or synthetic tasks.\n\n**Latent-reasoning theory.** Wang (2604.15726) formalizes three competing hypotheses: H1 (latent-mediated), H2 (CoT-mediated), H0 (serial compute). Proposes compute-audited designs with six experimental arms and evidence tiers. Our ICG framework operationalizes Wang's H1/H2 distinction: G*(t) >> 0 is H1-consistent, G*(t) ≈ 0 is H2-consistent.\n\n**Temporal hidden-state dynamics (concurrent complementary work).** Gjølbye et al. (2605.15454) study hidden-state trajectory geometry across 11 models (6 reasoning, 5 instruction-tuned baselines) on competitive programming (500 Codeforces), math (500 MATH), and Boolean SAT (500 SATBench). After length correction, difficulty remains systematically coupled to trajectory geometry: ρ⊥^D = +0.41 on Codeforces vs. −0.06 for baselines, with weaker effects in math (+0.05). Prompt-stage linear probes do NOT mirror these geometric effects — dynamics manifest during generation. Furuya & Tanimura (2605.01853) introduce StALT, a training-free trajectory statistic. Herrmann et al. (2605.09159) study 'internal polylogue' dynamics: persona vectors tracked temporally across MMLU-Pro. Li et al. (2510.22362, NeurIPS 2025 MechInterp Workshop) introduce Concept Walk, tracking concept-direction alignment per step on Qwen 3-4B; find easy→decorative, hard→faithful. Vilas et al. (2510.10494, ICLR 2026) define three latent-trajectory signals, achieving 14-70% token savings on R1-Distill/Phi-4/Qwen3.\n\n**Probe calibration and inflation (methodological foundation).** Hewitt & Liang (2019) show MLP probes achieve only 4.5 selectivity. Ravichander et al. (2020) demonstrate properties recoverable even when unused. Voita & Titov (2020) show MDL-based probing reveals accuracy doesn't substantially favor pretrained over random. Chun et al. (2602.20338) apply Manifold Capacity Theory to CoT reasoning: geometric separability peaks transiently as a 'geometric pulse' while probe accuracy remains high afterward — evidence that probe accuracy can overestimate geometrically organized (actionable) information availability. We address uniform inflation via null-probe calibration: P*(t) = P(t) − P_null(t), and use MCT as supplementary concordance check.\n\n**Trajectory-shape analysis (supporting our shape-based classification).** Entropy trajectory paper (2603.18940): monotonicity predicts reliability regardless of absolute levels (+5.8pp). RQA analysis (2602.06266): temporal features outperform aggregates 36.94% vs. 28.97%. Microsoft trajectory geometry (2604.05655): 0.852 AUC from shape features vs. 0.649 baseline. This literature validates trajectory shapes as diagnostic features — supporting our shapes-over-magnitudes approach to G*(t).\n\n**Measurement sensitivity.** Young (2603.20172) shows inter-classifier kappa as low as 0.06, up to 30.6pp divergence. Task-difficulty moderation: ICLR 2026 Workshop and Li et al. (2510.22362).\n\n**Reasoning-model internal dynamics.** Internal States Before Wait (2510.04128): crosscoders on R1-Distill with confirmed causal interventions for backtracking, uncertainty, verification features. From Reasoning to Answer (2509.23676): activation patching on R1-Distill.\n\n**Benchmarks, surveys, pathology diagnostics.** FaithCoT-Bench (ICLR 2026, arXiv 2510.04040): 1000+ expert-annotated trajectories providing instance-level faithfulness ground truth across 4 models × 4 domains, with 11 detection methods across 4 paradigms — serves as both external validation standard and evaluation benchmark for our TIF score. Jin et al.'s survey (ARR for ACL 2026). Liu et al. (2602.13904): text-level metrics for rationalization/encoded/internalized reasoning. Reasoning Theater (2603.05488). Young (2603.26410). 'Lie to Me' (2603.22582). Various early-exit methods: ESTAR, DTSR, NEAT, CoDE-Stop, FRIT (Swaroop et al., arXiv 2509.13334).\n\n**What remains open.** No extant framework provides: (1) a full-timeline information-contribution gap curve pairing calibrated probe trajectories with causal contribution estimation — Chrabąszcz et al. are closest but lack the entire C(t) dimension, gap metric, calibration, and the structural capacity to distinguish faithful from unfaithful correct reasoning; (2) empirically-validated phenomenon taxonomy using external classification standards; (3) an instance-level diagnostic score from the temporal gap; (4) difficulty-conditioned gap analysis with domain-specific nuance; (5) principled probe-target distinction treatment; or (6) head-to-head comparison against existing causal faithfulness methods (TTS, FaithCoT-Bench methods) demonstrating the incremental value of the dual-stream temporal approach.\n\n## Approach\nWe propose the Information-Contribution Gap (ICG) framework: a calibrated, temporally-resolved diagnostic that measures the divergence between information available in hidden states and information that causally contributes to model outputs, tracked across the full chain-of-thought generation trajectory.\n\n**Formal Framework.** Define two time-varying quantities at equally-spaced positions across CoT generation (primary resolution: 20-50 positions via percentile-based sampling; token-level as supplementary on smaller subsets):\n\n(i) *Calibrated Information Availability* P*(t): Cross-validated AUROC of a linear probe on layer-l hidden states at position t, calibrated via null-probe normalization (P*(t) = P(t) − P_null(t), following Hewitt & Liang 2019 selectivity). A single shared probe is trained and evaluated at each position (following Chrabąszcz et al.'s per-token evaluation approach, avoiding computationally prohibitive per-position probe training). **Probe target: correctness (right/wrong).** Correctness over answer-content for three reasons: (a) broader applicability beyond binary/MC tasks; (b) the 'diagnostic not causal' finding motivating the framework is specifically about correctness probes (Yuan et al.'s four-intervention failure); (c) more direct faithfulness interpretation — G*(t) >> 0 means 'the model's hidden states encode awareness that its answer is right/wrong, but its CoT does not causally reflect this self-monitoring.' On binary/MC subsets, supplementary answer-content probes test whether the 'what answer' gap differs from the 'whether correct' gap. We probe at layers L/4, L/2, 3L/4, L. MCT geometric validation (Chun et al. 2602.20338) on 500 examples serves as supplementary concordance check: if MCT capacity tracks P*(t), null-probe calibration is validated; if MCT shows geometric pulse while P*(t) remains high, this identifies positions where probe signal may reflect retrievability rather than geometrically organized information, informing interpretation of G*(t) at those positions. MCT results do not alter the core framework but enrich the interpretive layer.\n\n(ii) *Causal Contribution* C(t): Estimated via three complementary methods, aggregated into a composite C_agg(t) before gap computation: (a) **prefix-truncation ablation** — following Ballon et al.'s (2601.23163) truncation-reinjection protocol with their three control conditions (random tokens, swapped traces, shuffled tokens), measuring P(correct | CoT[:t]) vs. P(correct | full CoT); (b) **paraphrase perturbation** — replacing CoT segments (sentence-level, aligned with NLDD step segmentation) with meaning-preserving paraphrases generated by an external model (Claude or GPT-4, avoiding self-paraphrase bias), 3-5 variants per segment, with NLI-based semantic preservation verification. Answer stability measured as P(same answer | paraphrased CoT), reporting both exact match and logit-space KL. Protocol follows FaithCoT-Bench's (ICLR 2026) paraphrasing paradigm as operational reference; (c) **NLDD-based influence scoring** (Ye et al. 2602.11201, conditional on Phase 0a feasibility check) — measuring logit degradation under corruption at position t. Step segmentation for natural reasoning traces uses sentence-level boundaries (aligned with Zhao et al.'s TTS sentence-level approach). Using multiple C(t) estimators provides robustness against single-method artifacts, following Young's (2603.20172) finding that faithfulness measurements are classifier-sensitive.\n\n**C(t) Aggregation and Gap Normalization.** The three C(t) estimators operate on different scales. Primary normalization: rank-based — convert each estimator to instance-level percentile ranks within each model-benchmark cell, then average ranks to produce C_agg(t). Similarly rank-normalize P*(t). G*(t) = rank(P*)(t) − rank(C_agg)(t) operates in a unified dimensionless space. Alternative normalizations (min-max per estimator, z-score) reported as robustness ablation. As argued above, the primary diagnostic value lies in G*(t) trajectory shapes, not absolute magnitudes, so normalization choice affects scale but not the shape-based phenomenon signatures.\n\n**The Information-Contribution Gap.** G*(t) = P*(t) − C(t) [or rank-normalized equivalent]. Primary diagnostic signal:\n- G*(t) ≈ 0: Correctness awareness and causal contribution aligned (necessary for faithfulness)\n- G*(t) >> 0: Model encodes correctness awareness it does not causally use (diagnostic excess — 'knows but doesn't use')\n- G*(t) < 0: CoT contributes beyond what hidden states encode at that point (information assembled during reasoning)\n\nBecause P*(t) is null-probe-calibrated, uniform correlative inflation is removed. C(t) is not subject to probe inflation as it measures behavioral change under intervention. Following Wang's (2604.15726) H1/H2 framework: G*(t) >> 0 is H1-consistent, G*(t) ≈ 0 is H2-consistent.\n\n**Interpretive caveat.** G*(t) >> 0 indicates correctness-correlated information is present but not causally channeled through CoT. This does not entail the model \"decided to withhold\" — some probe-detectable signals may be computational byproducts (statistical regularities correlating with correctness) rather than semantically actionable knowledge accessible to the generation process. Chun et al.'s MCT geometric pulse finding provides evidence that probe-detectable and geometrically organized information can diverge. We report this boundary explicitly and use MCT concordance as partial validation.\n\n**Phenomenon Signature Predictions (2-3 confident, 4-5 stretch).** Grounded in real probe data with honest scoping:\n\n*Primary targets (HIGH confidence, validated in Phase 0b):*\n(i) *Pre-CoT encoding*: G*(t) starts high, stays high. Grounded in: David's 0.84 AUC at t=4, Esakkiraja's >90% pre-generation AUROC, Cox's >0.9 pre-CoT AUC. Shape: large constant gap.\n(ii) *Genuine multi-step reasoning*: G*(t) converges toward zero. Grounded in: Zhang et al.'s 65%→79% chunk trajectory, Li et al.'s hard→faithful, Ballon et al.'s monotonic accuracy increase. Shape: co-rising curves, small/decreasing gap.\n(iii) *Post-hoc rationalization*: G*(t) starts moderate, rises during CoT. P*(t) stable (David: ~0.80 from t=4 through t=100), C(t) remains flat. Shape: widening gap.\n\n*Stretch targets (MODERATE confidence, require additional features):*\n(iv) *Steganographic encoding*: G*(t) dip-and-recovery. Potentially consistent with Esakkiraja's dip at 5-10%. May require multi-layer analysis.\n(v) *Reasoning Theater*: EMPIRICAL QUESTION. May overlap with pre-CoT encoding or rationalization. Additional features — Chrabąszcz-style signal features (autocorrelation, boundary transients, dwell-time run-lengths) — may enable separation. Reported honestly with confusion matrices.\n\n**Semi-Synthetic Simulation (hypothesis generation, NOT validation).** Constructed from real published data to generate testable predictions about trajectory-shape separability. I_probe(t) profiles from David, Zhang, Esakkiraja, Yuan; C(t) profiles from NLDD (Ye et al.) and TTS (Zhao et al.); non-uniform inflation calibrated against Chun et al.'s MCT finding. Real validation comes from Phase 0b.\n\n**Phase 0a: Gap Characterization + NLDD Feasibility (Weeks 1-2.5).** Four objectives on 500 examples × 3 datasets (GSM8K, MATH-500, MMLU) × 3 models (DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct):\n(i) Construct empirical P*(t) and C(t) curves at chunk-level resolution (20-50 positions)\n(ii) Validate null-probe calibration: P_null(t) shows high accuracy (inflation exists) but P*(t) shows meaningful variance\n(iii) Characterize causal potency: following Cox et al.'s protocol, measure answer flip rates via probe-direction steering on reasoning vs. instruction-tuned models\n(iv) **NLDD feasibility check**: test NLDD on 7B model × 100 examples on GSM8K (clear step structure) and MMLU (ambiguous step structure). Evaluate signal-to-noise ratio and step segmentation quality. If NLDD signal is uninformative on MMLU (SNR < threshold), restrict NLDD to math/code benchmarks or replace with TTS-style per-step perturbation. This check costs <10 GPU-hrs and gates the 250+ hrs NLDD investment on 32B.\n\n**Phase 0b: Empirical Pilot for Phenomenon Separability (Weeks 2.5-4).** Validates trajectory-shape classification feasibility on real data before full pipeline commitment. On R1-Distill-Qwen-7B × GSM8K + MATH-500 (1000 examples):\n\n*Primary validation (external classification standards — avoids circularity):*\n(i) **Difficulty-only partition**: classify examples solely by model-independent difficulty (benchmark-provided difficulty level or multi-model consensus accuracy) into easy/medium/hard bins, without using P*(t) or C(t) features. Test whether G*(t) trajectory shapes differ significantly across difficulty bins (effect size d > 0.5 on 2+ trajectory-shape features).\n(ii) **FaithCoT-Bench external validation**: on the subset of examples overlapping with FaithCoT-Bench (ICLR 2026) annotations, test correlation between G*(t) trajectory features and expert-annotated faithfulness labels. If overlap is insufficient, use FaithCoT-Bench's task types as proxy.\n(iii) **TTS cross-reference**: compute Zhao et al.'s True Thinking Score on the same examples; test whether high-TTS examples (genuine reasoning candidates) vs. low-TTS examples (decorative candidates) produce distinguishable G*(t) shapes.\n\n*Supplementary (self-consistency check, NOT primary evidence):* Partition by P*(t) and C(t) features (as originally proposed) and verify consistency with external-standard results.\n\nApply Gjølbye et al.'s (2605.15454) length correction (residualizing on log(N)). Success criterion: d > 0.5 between at least 2 externally-defined partitions on 2+ features. If d < 0.3, downscope to characterization paper.\n\n**Phase 1: Full ICG Construction (Weeks 4-9).** Conditional on Phase 0b d > 0.5. Extend to 4 models (add QwQ-32B or R1-Distill-32B) × 4 benchmarks (add GPQA-Diamond or AIME). Full calibrated P*(t) with null-probe normalization + MCT supplementary concordance on 500 examples. Three C(t) estimators (NLDD on 32B conditional on Phase 0a feasibility) with Ballon et al.-style controls. Cross-reference with TTS at step boundaries. Bootstrap confidence intervals on G*(t). Primary resolution: 20-50 equally-spaced positions; token-level on 200-example subset for fine-grained analysis.\n\n**Phase 2: Task-Difficulty Conditioning (Weeks 7-11).** Partition each benchmark into difficulty quintiles. Measure G*(t) per quintile. Hypothesis: easy → large persistent gap (decorative CoT), hard → converging gap (load-bearing CoT). Following Gjølbye et al., apply length correction and report domain-specific effects — expecting stronger effects on math/code than MMLU, given ρ⊥ = +0.41 on Codeforces vs. +0.05 on MATH.\n\n**Phase 3: Phenomenon Classification, Baselines, and Robustness (Weeks 9-14).**\n\n*Classification framework:* Apply trajectory-shape classification to real data using G*(t) features (initial value, slope, convergence rate, dC/dt locality) + Chrabąszcz-style features (volatility, trend, boundary transients, autocorrelation). Classifier gradient: logistic regression → random forest → simple MLP; report all results to avoid cherry-picking. Evaluation: macro-F1 (primary, handles class imbalance) + confusion matrix + calibrated probability (reliability diagram). Cross-validation: 5-fold random + cross-model generalization (train on model A, test on model B) + cross-benchmark generalization (train on GSM8K, test on MATH).\n\n*Baselines for phenomenon classification:* (a) Random classifier + majority-class classifier; (b) Difficulty-only classifier (predict phenomenon from difficulty quintile alone — verifies that G*(t) features provide information beyond simple difficulty stratification); (c) **Chrabąszcz probe-trajectory-only features** — use only P*(t) trajectory features without C(t), as a \"no causal dimension\" ablation quantifying the incremental contribution of the dual-stream design; (d) **TTS-based classification** — use Zhao et al.'s per-step TTS values for the same examples, testing whether per-step causal contribution alone (without the probe dimension) achieves comparable phenomenon discrimination.\n\n*Head-to-head TIF validation:* Benchmark TIF score against: (a) FaithCoT-Bench's 11 detection methods (at minimum: Adding Mistakes, Removing Steps, Early Answering from counterfactual paradigm; paraphrasing method) on overlapping examples, comparing instance-level correlation with expert ground truth; (b) TTS as a per-step causal contribution baseline, comparing correlation with faithfulness labels.\n\n*Robustness ablations (6 dimensions):* (a) probe architecture (linear vs. 2-layer MLP) with selectivity; (b) layer selection (single best vs. multi-layer); (c) C(t) estimator agreement (prefix vs. paraphrase vs. NLDD); (d) gap normalization method (rank-based vs. min-max vs. z-score); (e) calibration method (shuffled-label vs. random-representation); (f) probe target (correctness vs. answer-content on binary/MC subsets). Report sensitivity ranges across all dimensions.\n\n**TIF Score.** Temporal Information-contribution Faithfulness score: normalized area under calibrated G*(t), benchmarked against FaithCoT-Bench and Liu et al.'s (2602.13904) text-level metrics.\n\n**Paper Focus (Tightened).** Core contributions: (1) calibrated ICG diagnostic with shape-based trajectory analysis on 4 models × 4 benchmarks, introducing the dual-stream gap that enables faithful-vs-unfaithful distinction impossible from probe trajectories alone; (2) Phase 0b empirical pilot with external validation standards (difficulty partition, FaithCoT-Bench, TTS cross-reference) demonstrating 2-3 distinguishable G*(t) phenomenon signatures; (3) task-difficulty conditioning revealing the decorative→load-bearing transition with domain-specific strength; (4) head-to-head comparison showing ICG's incremental value over probe-only trajectories, TTS, and FaithCoT-Bench methods. Supporting: robustness ablations (6 dimensions); TIF validation. Supplementary: 671B subset (500 examples, 3 layers); answer-content vs. correctness probe comparison; semi-synthetic simulation as hypothesis generation.\n\n**Experiments.** DeepSeek-R1-Distill-Qwen-7B/14B/32B, QwQ-32B across MMLU, GPQA-Diamond, GSM8K, AIME. 671B validation (500-example subset, 3 layers). Calibration checks: synthetic arithmetic (G* ≈ 0 expected), TTS cross-reference, MCT supplementary concordance. Gjølbye-style length correction on all temporal analyses.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '~830 H100-hours (Phase 0a characterization + NLDD feasibility: 90 hrs [3 models × 3 datasets, probe training + prefix ablation + steering tests + NLDD feasibility on 7B]; Phase 0b empirical pilot: 30 hrs [1 model × 2 datasets, full G*(t) construction + external validation]; Phase 1 full ICG: 120 hrs [4 models × 4 benchmarks, multi-layer probes + 3 C(t) estimators]; Phase 2 difficulty conditioning: 50 hrs; Phase 3 phenomenon classification + baselines + robustness: 60 hrs; NLDD on 32B model: 250 hrs [conditional on Phase 0a feasibility — primary bottleneck]; NLDD on 7B/14B models: 100 hrs; MCT geometric validation: 50 hrs [supplementary]; 671B subset: 50 hrs [8×H100]; semi-synthetic simulation: 30 hrs [mostly CPU])', 'timeline': '15-17 weeks (2 researchers: 4 weeks Phase 0a+0b; 5 weeks Phase 1; 4 weeks Phases 2-3 in parallel with NLDD; 2-3 weeks writing + ablations)', 'estimated_gpu_cost': '$2,500 at ~$3/H100-hour (cloud spot pricing)', 'storage': '3-5 TB (4 layers per model, fp16); reducible to ~1.5 TB via PCA or on-the-fly evaluation'}, 'human_in_loop': {'gpu_hours': '~830 H100-hours', 'timeline': '13 weeks (1 researcher + Claude for experiment design and analysis)', 'claude_api_cost': '$350', 'estimated_gpu_cost': '$2,500'}, 'auto_research': {'gpu_hours': '~830 H100-hours', 'timeline': '11 weeks', 'claude_api_cost': '$700', 'estimated_gpu_cost': '$2,500', 'speed_bottleneck': 'NLDD on 32B (~250 H100-hours, conditional on Phase 0a feasibility, ~30% of total compute) is the primary bottleneck. Phase 0b pilot (30 hrs) provides early go/no-go signal before committing full Phase 1-3 compute.'}}\n\n## Inspired By\nThe convergence of five independent lines of evidence — (a) Cox et al.'s finding that answer-content probe steering fails on reasoning models despite high accuracy; (b) Yuan et al.'s systematic demonstration that four interventions all fail on correctness probes, establishing 'diagnostic not causal'; (c) the temporal probe dynamics now empirically characterized by David (0.84 AUC at t=4, stable ~0.8), Zhang et al. (chunk-level rising trajectory), Esakkiraja et al. (pre-generation >90% with dip-recovery), and Chrabąszcz et al. (60+ trajectory features capturing dynamics invisible to static probes, up to 17pp improvement); (d) Ballon et al.'s truncation-reinjection protocol demonstrating monotonic behavioral C(t) curves with rigorous controls; (e) the trajectory-shape literature (arXiv 2603.18940, 2602.06266, 2604.05655) showing that shape features carry diagnostic information beyond absolute values — all pointing to the same insight: the gap between diagnostic information availability and causal contribution IS the phenomenon of interest, and its temporal trajectory shape reveals the mechanism of faithfulness or unfaithfulness. Additionally inspired by: Wang's (2604.15726) H1/H2/H0 hypotheses; Gjølbye et al.'s (2605.15454) domain-specific difficulty-geometry coupling; Chun et al.'s (2602.20338) MCT geometric pulse; and the CMI framework's (2602.03994) structural mediation approach, which our functional gap methodology complements.\n\n## Target Venues\n- ICLR 2027 (abstract: Sep 19, full paper: Sep 24, 2026; conference: Apr/May 2027 — primary target, 4 months from now)\n- ICML 2027 (full paper: Jan 29, 2027; conference: Jul 2027 — comfortable fallback if additional experiments needed)\n\n## Key References\n- Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics (Chrabąszcz et al., arXiv 2605.18549)\n- Probing the Trajectories of Reasoning Traces in Large Language Models (Ballon et al., arXiv 2601.23163)\n- LLM Reasoning Is Latent, Not the Chain of Thought (Wang, arXiv 2604.15726)\n- Reasoning Models Don't Just Think Longer, They Move Differently (Gjølbye et al., arXiv 2605.15454)\n- Hidden Error Awareness: The Signal Is Diagnostic, Not Causal (Yuan et al., arXiv 2605.09502)\n- Decoding Answers Before Chain-of-Thought: Pre-CoT Probes and Activation Steering (Cox et al., arXiv 2603.01437)\n- Temporal Predictors of Outcome in Reasoning Language Models (David, arXiv 2511.14773)\n- Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification (Zhang et al., arXiv 2504.05419)\n- Therefore I am. I Think (Esakkiraja et al., arXiv 2604.01202)\n- Can Aha Moments Be Fake? True Thinking Score (Zhao et al., arXiv 2510.24941)\n- Mechanistic Evidence for Faithfulness Decay / NLDD (Ye et al., arXiv 2602.11201)\n- Do LLMs Experience an Internal Polylogue? (Herrmann et al., arXiv 2605.09159)\n- LLMs Faithfully and Iteratively Compute Answers During CoT (Kudo et al., EACL 2026, arXiv 2412.01113)\n- When Chains of Thought Don't Matter: Causal Bypass / CMI (Sathyanarayanan et al., arXiv 2602.03994)\n- Spatiotemporal Hidden-State Dynamics / StALT (Furuya & Tanimura, arXiv 2605.01853)\n- Mapping Faithful Reasoning / Concept Walk (Li et al., arXiv 2510.22362, NeurIPS 2025 MechInterp Workshop)\n- Task Difficulty Shapes CoT Faithfulness (ICLR 2026 Workshop)\n- Diagnosing Pathological CoT (Liu et al., arXiv 2602.13904)\n- Measuring Faithfulness Depends on How You Measure (Young, arXiv 2603.20172)\n- Emergent Manifold Separability / MCT (Chun et al., arXiv 2602.20338)\n- Tracing the Traces: Latent Temporal Signals (Vilas et al., ICLR 2026, arXiv 2510.10494)\n- Probing and Steering CoT Unfaithfulness (Occhipinti et al., ICLR 2026 LIT Workshop)\n- Designing and Interpreting Probes with Control Tasks (Hewitt & Liang, EMNLP 2019)\n- Information-Theoretic Probing with MDL (Voita & Titov, EMNLP 2020, arXiv 2003.12298)\n- Probing the Probing Paradigm (Ravichander et al., arXiv 2005.00719)\n- Shape-over-magnitude dissociation in entropy trajectories (arXiv 2603.18940)\n- Is My Model Mind Blurting? RQA of Reasoning Dynamics (arXiv 2602.06266)\n- LLM Reasoning as Trajectories (arXiv 2604.05655, Microsoft)\n- Internal States Before Wait Modulate Reasoning Patterns (arXiv 2510.04128)\n- FACT-E (Sun et al., ACL Findings 2026, arXiv 2604.10693)\n- Breaking the Chain (Somov et al., arXiv 2603.16475)\n- The Illusion of Reasoning (Basu & Chakraborty, arXiv 2603.22816)\n- FaithCoT-Bench (ICLR 2026, arXiv 2510.04040)\n- The Mirage of Explainability survey (Jin et al., ARR for ACL 2026)\n- Reasoning Theater (Boppana et al., arXiv 2603.05488)\n- No Global Plan in CoT (Xu et al., arXiv 2602.02103)\n- Catching Rationalization in the Act (Mirtaheri & Belkin, arXiv 2603.17199)\n- CoT Monitorability via Information Theory (Anwar et al., arXiv 2602.18297)\n- Understanding CoT via Information Theory (Ton et al., ICML 2025, arXiv 2411.11984)\n- Demystifying Reasoning Dynamics with MI (Qian et al., NeurIPS 2025, arXiv 2506.02867)\n- Analysing CoT Dynamics (Lewis-Lim et al., EMNLP 2025, arXiv 2508.19827)\n- Why Models Know But Don't Say (Young, arXiv 2603.26410)\n- Lie to Me (arXiv 2603.22582)\n- Step-Level Hallucination via Transport Geometry (Alvarez & Baheri, arXiv 2605.13772)\n- From Reasoning to Answer (arXiv 2509.23676)\n- SAE Reasoning Features (arXiv 2503.18878)\n- FRIT (Swaroop et al., arXiv 2509.13334)\n- Solution Hides in Hidden States (arXiv 2604.23351)\n- Knowing Before Saying (ACL Findings 2025, arXiv 2505.24362)\n- LEACE: Perfect Linear Concept Erasure (Belrose et al., NeurIPS 2023, arXiv 2306.03819)"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T04:05:12.443Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:05:12.443Z",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd"
}
```

---

## Round 1

55 recorded events

### User

_source line 3 · 2026-05-20T04:05:12.468Z_

# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness

## Description
We propose the Information-Contribution Gap (ICG) framework, a calibrated temporal diagnostic for chain-of-thought faithfulness that exploits a robust empirical finding: linear probes on hidden states reliably diagnose answer correctness (0.82-0.95 AUROC across four independent groups) yet causal interventions based on these probes consistently fail on reasoning-trained models (Cox et al.: negligible flip rates; Yuan et al.: all four intervention strategies fail). Rather than treating this diagnostic-causal gap as an obstacle, we make it the primary object of study — the gap between what models internally know and what their CoT causally contributes IS the faithfulness signal.

The framework tracks two calibrated time-varying quantities across the full CoT trajectory: P*(t), null-probe-calibrated correctness awareness, and C(t), causal contribution estimated via three complementary methods (prefix truncation with Ballon et al.'s three control conditions, paraphrase perturbation, NLDD). Their divergence G*(t) = P*(t) − C(t) produces phenomenon-specific temporal fingerprints, operationalizing Wang's (2604.15726) H1/H2 distinction: G*(t) >> 0 is latent-mediated (H1-consistent), G*(t) ≈ 0 is CoT-mediated (H2-consistent).

**Core insight: the diagnostic contribution of G*(t) is its temporal trajectory shape — not its absolute magnitude.** Because P*(t) and C(t) are measured via fundamentally different methods (probe AUROC vs. behavioral accuracy change), their absolute scales are not directly commensurable. We address this via rank-based normalization as primary scheme, but more fundamentally, we show that the trajectory-shape profile of G*(t) — its initial value regime, slope dynamics, convergence/divergence patterns — carries the diagnostic signal. A model that pre-encodes the answer shows a constant-high shape regardless of absolute scale; a model that genuinely reasons shows a converging shape; post-hoc rationalization shows a widening shape. This shapes-over-magnitudes approach is validated by the trajectory-shape literature: entropy trajectory monotonicity predicts reliability regardless of absolute levels (+5.8pp, arXiv 2603.18940); RQA temporal features outperform aggregates (36.94% vs. 28.97%, arXiv 2602.06266); Microsoft trajectory geometry achieves 0.852 AUC from shape features vs. 0.649 baseline (arXiv 2604.05655).

**Why temporal trajectories, not just endpoint comparison?** A reviewer might ask: "Why not just correlate pre-CoT probe accuracy with final correctness?" The answer: endpoint comparison detects the *presence* of unfaithfulness but collapses distinct failure *mechanisms* into a single label. Pre-CoT encoding and post-hoc rationalization both produce "high probe accuracy + low causal contribution" at endpoints, but yield distinct G*(t) shapes (constant-high vs. widening). "Genuine reasoning with late failure" (model reasons faithfully for 80% of the chain, then shortcuts) shows G*(t) ≈ 0 then spiking — invisible to any static measurement. The temporal framework's value is mechanistic discrimination, not just detection.

Positioned against the closest concurrent work — Chrabąszcz et al.'s (2605.18549) probe trajectories with 60+ signal-processing features achieving up to 17pp improvement over static probes — our framework addresses a qualitative blindspot in their single-stream design: Chrabąszcz et al. answer "what does the model know over time?" (outcome prediction), but cannot distinguish *faithful-correct* from *unfaithful-correct* reasoning. A model that pre-encodes the answer and generates decorative CoT looks identical to a model that genuinely reasons in their framework (both show high probe accuracy throughout), but looks radically different in ICG (the former has persistent G*(t) >> 0, the latter has G*(t) converging to 0). This faithful-vs-unfaithful distinction is structurally impossible from probe trajectories alone — it requires the causal contribution dimension.

We further differentiate from the CMI framework (Sathyanarayanan et al., 2602.03994), which measures whether answer representations pass through CoT-aligned layers via layerwise activation patching — a *structural* question ("does the computational path go through CoT?"). ICG answers a *functional* question ("does the CoT text causally contribute to correctness?"). A model could have high CMI (representations routed through CoT-processing layers) but high G*(t) (the CoT text serves as a timing scaffold rather than contributing semantic content). This structural-vs-functional distinction is novel.

**Interpretive boundary.** We explicitly acknowledge: G*(t) >> 0 means correctness-correlated information is present in hidden states but not causally channeled through CoT text. It does not necessarily mean the model "decided to withhold" — the information may exist as computational byproducts (statistical regularities in activations) rather than semantically actionable knowledge. Chun et al.'s MCT finding (2602.20338) — geometric separability peaks transiently while probe accuracy remains high — provides direct evidence of this possibility. Null-probe calibration addresses uniform inflation but not this deeper question. We use MCT concordance as supplementary validation and report G*(t) interpretations with this caveat.

**Practical significance beyond faithfulness measurement.** The ICG framework addresses questions the field urgently needs answered: (a) *Inference-time compute allocation*: when G*(t) >> 0 for easy problems, CoT is decorative overhead — don't generate it; (b) *Benchmark validity*: problems where all models show persistent G*(t) >> 0 are not testing reasoning regardless of accuracy scores; (c) *Safety monitoring*: the decoupled internal quality-monitoring system identified by Yuan et al. (the model internally knows it's wrong but doesn't course-correct) is exactly the kind of hidden computation alignment researchers worry about.

We adopt honest scoping: 2-3 faithfulness phenomena (pre-CoT encoding, genuine reasoning, post-hoc rationalization) as the realistic classification target, with steganographic encoding and reasoning theater as stretch goals. A new empirical pilot phase (Phase 0b) validates phenomenon separability on real data using external classification standards (difficulty-based partition and FaithCoT-Bench ground truth) before committing to the full pipeline. Task-difficulty conditioning — grounded in David's easy (0.84) vs. hard (0.76) probe splits and Gjølbye et al.'s (2605.15454) demonstration that difficulty-geometry coupling is systematic (ρ⊥ = +0.41 on Codeforces) but domain-specific — reveals the decorative→load-bearing transition with length correction (residualizing on log(N)).

The paper focuses on four core contributions: (a) calibrated ICG diagnostic with shape-based trajectory analysis on 4 models × 4 benchmarks, positioned against Chrabąszcz et al. and CMI to demonstrate the value of the dual-stream functional gap; (b) empirical pilot validating that 2-3 phenomena produce distinguishable G*(t) trajectory shapes on real data using external validation standards; (c) difficulty-conditioned gap analysis with domain-specific nuance; (d) head-to-head comparison against TTS, FaithCoT-Bench methods, and probe-only trajectories demonstrating the incremental value of the causal contribution dimension. Total compute: ~830 H100-hours, with NLDD on 32B models (~250 hrs, conditional on Phase 0a feasibility) as the primary bottleneck.

## Core Problem
A striking convergence of 2025-2026 findings reveals a fundamental disconnect in reasoning language models: their hidden states reliably encode information about answer correctness — with linear probes achieving 0.82-0.95 AUROC across multiple independent groups — yet causal interventions based on these probes consistently fail to influence model outputs. Cox et al. (2603.01437) find that steering via answer-content probes produces answer flip rates 'negligible against the orthogonal baseline' on reasoning models, despite >0.9 AUC on instruction-tuned models. Yuan et al. (2605.09502) systematically test four distinct intervention strategies (activation steering, probe-guided best-of-N, self-correction, activation patching) on models up to 72B parameters and report that ALL fail: 'RL training does not close the diagnostic–causal gap.' This diagnostic-causal gap — the divergence between what information is available in a model's hidden states and what information the chain-of-thought reasoning text causally contributes — is NOT a methodological obstacle to overcome; it IS the central phenomenon. Critically, the literature conflates two distinct probe targets: answer-content probes (Cox et al.: predicting the specific answer on binary tasks, models ≤9B + GPT-OSS-20B) and correctness probes (Yuan et al.: predicting right/wrong on models up to 72B; Zhang et al.: per-chunk correctness on 7B-70B). This distinction matters because the gap's interpretation differs: answer-content gaps mean 'the model has already decided but CoT doesn't derive the answer,' while correctness gaps mean 'the model knows it's right/wrong but CoT doesn't reflect this awareness.' Meanwhile, the temporal dynamics of this gap are now empirically grounded: David (2511.14773) shows probe accuracy stabilizes at 0.84 AUC by token 4, remaining ~0.8 through token 100, with task-difficulty conditioning revealing easy (0.84) vs. hard (0.76) signatures. Zhang et al. (2504.05419) report chunk-level probe trajectories rising from 65% at 10% of reasoning to 79% at 100% on R1-Distill. Esakkiraja et al. (2604.01202) find >90% pre-generation AUROC with a characteristic dip at 5-10% of reasoning followed by recovery. Chrabąszcz et al. (2605.18549) demonstrate that temporal probe trajectories with 60+ signal-processing features achieve up to 17pp improvement over static probes, showing that trajectory dynamics capture information invisible to single-timepoint measurements. These temporal profiles suggest that different modes of CoT unfaithfulness — pre-CoT encoding, post-hoc rationalization, reasoning theater, myopic planning, thinking-answer gap — produce distinguishable temporal divergence signatures. Yet no existing framework jointly tracks information availability AND causal contribution across the full CoT timeline: Chrabąszcz et al. provide the closest probe-trajectory methodology but lack any causal contribution component, gap metric, probe calibration, or phenomenon taxonomy; Ballon et al. (2601.23163) provide behavioral causal curves via truncation-reinjection but lack hidden-state measurement; the CMI framework provides layerwise causal audit on ~50 examples but measures structural mediation (whether representations route through CoT layers) rather than functional contribution (whether CoT text causally affects correctness); Zhao et al.'s True Thinking Score provides per-step causal contribution but no probe-side measurement. The gap between diagnostic information availability and causal contribution IS the phenomenon of interest, not an obstacle.

## Opportunity
The field has independently produced the measurement tools needed for a unified temporal framework, but these tools remain siloed. The opportunity is fourfold:

(1) **Temporal gap measurement.** Despite rapid accumulation of probe measurements (David: 0.84 at t=4; Zhang: 0.82-0.91 on chunks; Yuan: 0.95 overall, 0.787 first-step; Esakkiraja: >90% pre-generation; Chrabąszcz et al.: 91-97% AUROC with max-pooling on trajectories), no work tracks the full-timeline divergence between probe-estimated information availability and intervention-estimated causal contribution. Chrabąszcz et al. (2605.18549) come closest on the probe side — extracting 60+ signal-processing features from probe trajectories across 4 reasoning models and 4 datasets, achieving up to 17pp improvement over static probes on GSM8K — but they target outcome prediction (correctness, harmfulness) rather than the faithfulness gap, and provide no causal contribution measurement. Critically, their framework is structurally blind to the faithful-correct vs. unfaithful-correct distinction: a model that pre-encodes answers and a model that genuinely reasons look identical in their single-stream design. Our framework extends this via the dual-estimator gap G*(t) = P*(t) − C(t) that enables this distinction. On the causal side, Ballon et al. (2601.23163) provide behavioral C(t) curves via truncation-reinjection at decile intervals on Qwen3/gpt-oss across GPQA-Diamond and MMLU-Pro — showing monotonic accuracy increase from 30.8-42.3% to 49.0-73.1% with control conditions validating that sequential content (not just context length) matters — but lack hidden-state measurement.

(2) **Phenomenon unification with honest scoping.** The CoT faithfulness literature treats each failure mode as separate: Reasoning Horizon (Ye et al. 2602.11201), pre-CoT encoding (Cox et al. 2603.01437; Esakkiraja et al. 2604.01202), Reasoning Theater (Boppana et al. 2603.05488), myopic planning (Xu et al. 2602.02103), thinking-answer gap. We propose that 2-3 of these are confidently distinguishable via trajectory-shape signatures in G*(t), with 4-5 as a stretch goal. The honest scoping — validated through an empirical pilot on real data with external classification standards before committing to full classification — is itself a contribution to a field prone to over-claiming.

(3) **Task-difficulty conditioning.** The ICLR 2026 Workshop finding and Li et al.'s (2510.22362) corroboration show easy→decorative, hard→faithful. David's easy/hard splits (0.84 vs. 0.76 at t=32) provide probe-level evidence. Gjølbye et al. (2605.15454) demonstrate that difficulty is systematically coupled to hidden-state trajectory geometry even after length correction (ρ⊥ = +0.41 for reasoning models vs. −0.06 for baselines on competitive programming), with domain-specific strength. A difficulty-conditioned gap framework answers the practical question: at what difficulty level does CoT transition from decorative to load-bearing? This has direct implications for inference-time compute allocation (skip CoT on easy problems) and benchmark validity (problems where all models show G*(t) >> 0 are not testing reasoning).

(4) **Probe target clarification.** The field has not confronted the distinction between answer-content probes (Cox et al.: binary tasks, ≤9B) and correctness probes (Yuan et al.: up to 72B). A framework that explicitly measures correctness awareness gap — and contrasts it with answer-content gap on applicable tasks — provides the first principled treatment of what 'knowing but not using' means.

Two prior works have combined probing with causal interventions: Kudo et al. (EACL 2026) on synthetic arithmetic, and the CMI framework (2602.03994) on ~50 examples. The CMI framework provides *structural* causal mediation (layerwise activation patching measuring whether representations route through CoT layers), while our framework provides *functional* causal assessment (whether the CoT text itself causally contributes to behavioral correctness). Wang (2604.15726) formalizes the need via competing hypotheses (H1: latent-mediated, H2: CoT-mediated, H0: serial compute) — our ICG framework provides an empirical methodology to distinguish H1 from H2 at each temporal position. Neither Kudo et al. nor CMI provides: (a) full temporal-position coverage on natural benchmarks, (b) mapping to named faithfulness phenomena, (c) a standalone instance-level diagnostic, (d) systematic multi-model comparison, (e) robustness validation — a critical gap highlighted by Young's (2603.20172) finding that faithfulness measurements are classifier-sensitive (inter-classifier kappa as low as 0.06), or (f) an empirical pilot with external validation standards.

## Landscape
**Probe-based temporal measurement (foundational for our P*(t) component).** Chrabąszcz et al. (2605.18549) is the closest concurrent work: they introduce probe trajectories — tracking concept probability at each generated token — and extract 60+ signal-processing features (volatility, trend, steady-state, temporal segmentation, boundary transients, autocorrelation) via 3-layer MLP probes with Multi-Instance Learning meta-probe across layers. Key results: max-pooling achieves 91-97% AUROC on harmfulness detection (vs. 33-61% for average-pooling); up to 17pp improvement over static probes on GSM8K across Llama-8B-R1-Distill and Qwen3-4B/8B/14B (~3000 GPU-hours total). Critical differentiators from our framework: (a) NO causal contribution component; (b) NO gap metric; (c) NO null-probe calibration or MCT validation; (d) NO phenomenon taxonomy — they separate correct/incorrect or safe/harmful, not faithfulness modes; (e) NO task-difficulty conditioning; (f) structurally cannot distinguish faithful-correct from unfaithful-correct reasoning (both produce high probe accuracy, but only the dual-stream ICG can separate them via the C(t) dimension). Their 60+ feature extraction methodology is complementary and could enhance our trajectory-shape classification. David (2511.14773) trains per-position probes on reasoning models, finding 0.84 AUC at t=4, stable ~0.8 through t≈100, with easy/hard splits of 0.84 vs. 0.76 at t=32 on Qwen3-8B. Zhang et al. (2504.05419) probe R1-Distill models (7B/32B/70B) for correctness at each reasoning chunk, achieving 0.82-0.91 AUROC on GSM8K/MATH/AIME, with a rising trajectory from 65% at 10% chunk to 79% at 100%, enabling 24% token reduction via early-exit. Yuan et al. (2605.09502) report 0.95 AUROC on Qwen-3B, 0.852 on DeepSeek-R1-7B, 0.787 from first-step hidden states alone, and a concealment gap of 0.197 AUROC between hidden-state (0.787) and text-surface (0.590) classifiers — using correctness probes (right/wrong). Esakkiraja et al. (2604.01202) find >90% AUROC pre-generation on Qwen3-4B and GLM-Z1-9B, with a characteristic dip at 5-10% of reasoning and recovery to near-100% by think_end. Cox et al. (2603.01437) use answer-content probes achieving >0.9 AUC on instruction-tuned Gemma-2 (2B, 9B) and Qwen-2.5 (1.5B, 3B, 7B) models, but 'the answer flip rate is negligible against the orthogonal baseline' on the reasoning model GPT-OSS-20B. Additional probing work: Qian et al. (2506.02867, NeurIPS 2025); Lewis-Lim et al. (2508.19827, EMNLP 2025); Mirtaheri & Belkin (2603.17199); Occhipinti et al. (ICLR 2026 LIT Workshop, probing F1 90-100%, steering 46% recovery).

**The diagnostic-not-causal evidence (motivating our framework).** Yuan et al. (2605.09502) is the decisive study: four interventions — activation steering (at most +4%), probe-guided best-of-N (matches random), self-correction (hurts accuracy −3%), activation patching (destroys coherence at α=0.5) — all fail. Tested on Qwen2.5 (1.5B-72B), Llama-3.1-8B, Phi-3.5-mini, DeepSeek-R1-7B. Key quote: 'The error signal is a diagnostic readout—a summary statistic of computation quality—not a causal component that can be edited.' Cox et al. (2603.01437) independently confirm: steering fails on reasoning models despite high probe accuracy. This establishes that probe accuracy ≠ causal potency on reasoning models.

**Behavioral trajectory probing (foundational for our C(t) component).** Ballon et al. (2601.23163) introduce the truncation-reinjection protocol: generate full reasoning traces on Qwen3-4B/8B/14B and gpt-oss-20B/120B, truncate at decile intervals (10-100%), reinject with early-stopping suffix, measure answer-choice probability distributions. Key results: accuracy increases monotonically from 30.8-42.3% to 49.0-73.1% on GPQA-Diamond; three control conditions validate causal content: random tokens (+2.1-4.3%), swapped traces (+3.2-8.7%), and shuffled tokens (+0.3-10.8%) all substantially underperform intact truncated traces (+18.1-33.1%). Explicitly disclaims faithfulness-to-internal-computations analysis. Zhao et al. (2510.24941) introduce the True Thinking Score (TTS), measuring per-step causal contribution via numerical perturbation and ATE computation on DeepSeek-R1-Distill-Qwen-7B/14B/Llama-8B across AIME/MATH/AMC/CommonsenseQA, finding only 2.3% of AIME steps have TTS≥0.7. Ye et al. (2602.11201) introduce NLDD, finding a Reasoning Horizon at 70-85% of chain length on 3 models across synthetic tasks (syntactic, logical, arithmetic — natural benchmark generalizability remains unvalidated). Basu & Chakraborty (2603.22816) propose a decorative/scaffolding/genuine taxonomy. FACT-E (Sun et al. 2604.10693, ACL Findings 2026) provides another causal measurement approach.

**Probe-intervention combinations (closest prior work).** Kudo et al. (2412.01113, EACL 2026) train per-position linear probes and validate with sliding-window activation patching on 9 models across synthetic multi-step arithmetic — CoT IS faithful for arithmetic but explicitly note their synthetic setting may not generalize. The CMI framework (2602.03994) introduces the CoT Mediation Index via layerwise activation patching across Phi, Qwen, DialoGPT on StrategyQA (20), TruthfulQA (10), GSM8K (20), identifying 'bypass regimes' where CMI ≈ 0. CMI measures *structural mediation* — whether the answer's latent representation passes through CoT-aligned layers — which is a different question from ICG's *functional contribution* — whether the CoT text itself causally contributes to behavioral correctness. A model could have high CMI (representations routed through CoT layers) but high G*(t) (the CoT text serves as a timing scaffold without semantic contribution). Both are complementary precursors operating on small samples or synthetic tasks.

**Latent-reasoning theory.** Wang (2604.15726) formalizes three competing hypotheses: H1 (latent-mediated), H2 (CoT-mediated), H0 (serial compute). Proposes compute-audited designs with six experimental arms and evidence tiers. Our ICG framework operationalizes Wang's H1/H2 distinction: G*(t) >> 0 is H1-consistent, G*(t) ≈ 0 is H2-consistent.

**Temporal hidden-state dynamics (concurrent complementary work).** Gjølbye et al. (2605.15454) study hidden-state trajectory geometry across 11 models (6 reasoning, 5 instruction-tuned baselines) on competitive programming (500 Codeforces), math (500 MATH), and Boolean SAT (500 SATBench). After length correction, difficulty remains systematically coupled to trajectory geometry: ρ⊥^D = +0.41 on Codeforces vs. −0.06 for baselines, with weaker effects in math (+0.05). Prompt-stage linear probes do NOT mirror these geometric effects — dynamics manifest during generation. Furuya & Tanimura (2605.01853) introduce StALT, a training-free trajectory statistic. Herrmann et al. (2605.09159) study 'internal polylogue' dynamics: persona vectors tracked temporally across MMLU-Pro. Li et al. (2510.22362, NeurIPS 2025 MechInterp Workshop) introduce Concept Walk, tracking concept-direction alignment per step on Qwen 3-4B; find easy→decorative, hard→faithful. Vilas et al. (2510.10494, ICLR 2026) define three latent-trajectory signals, achieving 14-70% token savings on R1-Distill/Phi-4/Qwen3.

**Probe calibration and inflation (methodological foundation).** Hewitt & Liang (2019) show MLP probes achieve only 4.5 selectivity. Ravichander et al. (2020) demonstrate properties recoverable even when unused. Voita & Titov (2020) show MDL-based probing reveals accuracy doesn't substantially favor pretrained over random. Chun et al. (2602.20338) apply Manifold Capacity Theory to CoT reasoning: geometric separability peaks transiently as a 'geometric pulse' while probe accuracy remains high afterward — evidence that probe accuracy can overestimate geometrically organized (actionable) information availability. We address uniform inflation via null-probe calibration: P*(t) = P(t) − P_null(t), and use MCT as supplementary concordance check.

**Trajectory-shape analysis (supporting our shape-based classification).** Entropy trajectory paper (2603.18940): monotonicity predicts reliability regardless of absolute levels (+5.8pp). RQA analysis (2602.06266): temporal features outperform aggregates 36.94% vs. 28.97%. Microsoft trajectory geometry (2604.05655): 0.852 AUC from shape features vs. 0.649 baseline. This literature validates trajectory shapes as diagnostic features — supporting our shapes-over-magnitudes approach to G*(t).

**Measurement sensitivity.** Young (2603.20172) shows inter-classifier kappa as low as 0.06, up to 30.6pp divergence. Task-difficulty moderation: ICLR 2026 Workshop and Li et al. (2510.22362).

**Reasoning-model internal dynamics.** Internal States Before Wait (2510.04128): crosscoders on R1-Distill with confirmed causal interventions for backtracking, uncertainty, verification features. From Reasoning to Answer (2509.23676): activation patching on R1-Distill.

**Benchmarks, surveys, pathology diagnostics.** FaithCoT-Bench (ICLR 2026, arXiv 2510.04040): 1000+ expert-annotated trajectories providing instance-level faithfulness ground truth across 4 models × 4 domains, with 11 detection methods across 4 paradigms — serves as both external validation standard and evaluation benchmark for our TIF score. Jin et al.'s survey (ARR for ACL 2026). Liu et al. (2602.13904): text-level metrics for rationalization/encoded/internalized reasoning. Reasoning Theater (2603.05488). Young (2603.26410). 'Lie to Me' (2603.22582). Various early-exit methods: ESTAR, DTSR, NEAT, CoDE-Stop, FRIT (Swaroop et al., arXiv 2509.13334).

**What remains open.** No extant framework provides: (1) a full-timeline information-contribution gap curve pairing calibrated probe trajectories with causal contribution estimation — Chrabąszcz et al. are closest but lack the entire C(t) dimension, gap metric, calibration, and the structural capacity to distinguish faithful from unfaithful correct reasoning; (2) empirically-validated phenomenon taxonomy using external classification standards; (3) an instance-level diagnostic score from the temporal gap; (4) difficulty-conditioned gap analysis with domain-specific nuance; (5) principled probe-target distinction treatment; or (6) head-to-head comparison against existing causal faithfulness methods (TTS, FaithCoT-Bench methods) demonstrating the incremental value of the dual-stream temporal approach.

## Approach
We propose the Information-Contribution Gap (ICG) framework: a calibrated, temporally-resolved diagnostic that measures the divergence between information available in hidden states and information that causally contributes to model outputs, tracked across the full chain-of-thought generation trajectory.

**Formal Framework.** Define two time-varying quantities at equally-spaced positions across CoT generation (primary resolution: 20-50 positions via percentile-based sampling; token-level as supplementary on smaller subsets):

(i) *Calibrated Information Availability* P*(t): Cross-validated AUROC of a linear probe on layer-l hidden states at position t, calibrated via null-probe normalization (P*(t) = P(t) − P_null(t), following Hewitt & Liang 2019 selectivity). A single shared probe is trained and evaluated at each position (following Chrabąszcz et al.'s per-token evaluation approach, avoiding computationally prohibitive per-position probe training). **Probe target: correctness (right/wrong).** Correctness over answer-content for three reasons: (a) broader applicability beyond binary/MC tasks; (b) the 'diagnostic not causal' finding motivating the framework is specifically about correctness probes (Yuan et al.'s four-intervention failure); (c) more direct faithfulness interpretation — G*(t) >> 0 means 'the model's hidden states encode awareness that its answer is right/wrong, but its CoT does not causally reflect this self-monitoring.' On binary/MC subsets, supplementary answer-content probes test whether the 'what answer' gap differs from the 'whether correct' gap. We probe at layers L/4, L/2, 3L/4, L. MCT geometric validation (Chun et al. 2602.20338) on 500 examples serves as supplementary concordance check: if MCT capacity tracks P*(t), null-probe calibration is validated; if MCT shows geometric pulse while P*(t) remains high, this identifies positions where probe signal may reflect retrievability rather than geometrically organized information, informing interpretation of G*(t) at those positions. MCT results do not alter the core framework but enrich the interpretive layer.

(ii) *Causal Contribution* C(t): Estimated via three complementary methods, aggregated into a composite C_agg(t) before gap computation: (a) **prefix-truncation ablation** — following Ballon et al.'s (2601.23163) truncation-reinjection protocol with their three control conditions (random tokens, swapped traces, shuffled tokens), measuring P(correct | CoT[:t]) vs. P(correct | full CoT); (b) **paraphrase perturbation** — replacing CoT segments (sentence-level, aligned with NLDD step segmentation) with meaning-preserving paraphrases generated by an external model (Claude or GPT-4, avoiding self-paraphrase bias), 3-5 variants per segment, with NLI-based semantic preservation verification. Answer stability measured as P(same answer | paraphrased CoT), reporting both exact match and logit-space KL. Protocol follows FaithCoT-Bench's (ICLR 2026) paraphrasing paradigm as operational reference; (c) **NLDD-based influence scoring** (Ye et al. 2602.11201, conditional on Phase 0a feasibility check) — measuring logit degradation under corruption at position t. Step segmentation for natural reasoning traces uses sentence-level boundaries (aligned with Zhao et al.'s TTS sentence-level approach). Using multiple C(t) estimators provides robustness against single-method artifacts, following Young's (2603.20172) finding that faithfulness measurements are classifier-sensitive.

**C(t) Aggregation and Gap Normalization.** The three C(t) estimators operate on different scales. Primary normalization: rank-based — convert each estimator to instance-level percentile ranks within each model-benchmark cell, then average ranks to produce C_agg(t). Similarly rank-normalize P*(t). G*(t) = rank(P*)(t) − rank(C_agg)(t) operates in a unified dimensionless space. Alternative normalizations (min-max per estimator, z-score) reported as robustness ablation. As argued above, the primary diagnostic value lies in G*(t) trajectory shapes, not absolute magnitudes, so normalization choice affects scale but not the shape-based phenomenon signatures.

**The Information-Contribution Gap.** G*(t) = P*(t) − C(t) [or rank-normalized equivalent]. Primary diagnostic signal:
- G*(t) ≈ 0: Correctness awareness and causal contribution aligned (necessary for faithfulness)
- G*(t) >> 0: Model encodes correctness awareness it does not causally use (diagnostic excess — 'knows but doesn't use')
- G*(t) < 0: CoT contributes beyond what hidden states encode at that point (information assembled during reasoning)

Because P*(t) is null-probe-calibrated, uniform correlative inflation is removed. C(t) is not subject to probe inflation as it measures behavioral change under intervention. Following Wang's (2604.15726) H1/H2 framework: G*(t) >> 0 is H1-consistent, G*(t) ≈ 0 is H2-consistent.

**Interpretive caveat.** G*(t) >> 0 indicates correctness-correlated information is present but not causally channeled through CoT. This does not entail the model "decided to withhold" — some probe-detectable signals may be computational byproducts (statistical regularities correlating with correctness) rather than semantically actionable knowledge accessible to the generation process. Chun et al.'s MCT geometric pulse finding provides evidence that probe-detectable and geometrically organized information can diverge. We report this boundary explicitly and use MCT concordance as partial validation.

**Phenomenon Signature Predictions (2-3 confident, 4-5 stretch).** Grounded in real probe data with honest scoping:

*Primary targets (HIGH confidence, validated in Phase 0b):*
(i) *Pre-CoT encoding*: G*(t) starts high, stays high. Grounded in: David's 0.84 AUC at t=4, Esakkiraja's >90% pre-generation AUROC, Cox's >0.9 pre-CoT AUC. Shape: large constant gap.
(ii) *Genuine multi-step reasoning*: G*(t) converges toward zero. Grounded in: Zhang et al.'s 65%→79% chunk trajectory, Li et al.'s hard→faithful, Ballon et al.'s monotonic accuracy increase. Shape: co-rising curves, small/decreasing gap.
(iii) *Post-hoc rationalization*: G*(t) starts moderate, rises during CoT. P*(t) stable (David: ~0.80 from t=4 through t=100), C(t) remains flat. Shape: widening gap.

*Stretch targets (MODERATE confidence, require additional features):*
(iv) *Steganographic encoding*: G*(t) dip-and-recovery. Potentially consistent with Esakkiraja's dip at 5-10%. May require multi-layer analysis.
(v) *Reasoning Theater*: EMPIRICAL QUESTION. May overlap with pre-CoT encoding or rationalization. Additional features — Chrabąszcz-style signal features (autocorrelation, boundary transients, dwell-time run-lengths) — may enable separation. Reported honestly with confusion matrices.

**Semi-Synthetic Simulation (hypothesis generation, NOT validation).** Constructed from real published data to generate testable predictions about trajectory-shape separability. I_probe(t) profiles from David, Zhang, Esakkiraja, Yuan; C(t) profiles from NLDD (Ye et al.) and TTS (Zhao et al.); non-uniform inflation calibrated against Chun et al.'s MCT finding. Real validation comes from Phase 0b.

**Phase 0a: Gap Characterization + NLDD Feasibility (Weeks 1-2.5).** Four objectives on 500 examples × 3 datasets (GSM8K, MATH-500, MMLU) × 3 models (DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct):
(i) Construct empirical P*(t) and C(t) curves at chunk-level resolution (20-50 positions)
(ii) Validate null-probe calibration: P_null(t) shows high accuracy (inflation exists) but P*(t) shows meaningful variance
(iii) Characterize causal potency: following Cox et al.'s protocol, measure answer flip rates via probe-direction steering on reasoning vs. instruction-tuned models
(iv) **NLDD feasibility check**: test NLDD on 7B model × 100 examples on GSM8K (clear step structure) and MMLU (ambiguous step structure). Evaluate signal-to-noise ratio and step segmentation quality. If NLDD signal is uninformative on MMLU (SNR < threshold), restrict NLDD to math/code benchmarks or replace with TTS-style per-step perturbation. This check costs <10 GPU-hrs and gates the 250+ hrs NLDD investment on 32B.

**Phase 0b: Empirical Pilot for Phenomenon Separability (Weeks 2.5-4).** Validates trajectory-shape classification feasibility on real data before full pipeline commitment. On R1-Distill-Qwen-7B × GSM8K + MATH-500 (1000 examples):

*Primary validation (external classification standards — avoids circularity):*
(i) **Difficulty-only partition**: classify examples solely by model-independent difficulty (benchmark-provided difficulty level or multi-model consensus accuracy) into easy/medium/hard bins, without using P*(t) or C(t) features. Test whether G*(t) trajectory shapes differ significantly across difficulty bins (effect size d > 0.5 on 2+ trajectory-shape features).
(ii) **FaithCoT-Bench external validation**: on the subset of examples overlapping with FaithCoT-Bench (ICLR 2026) annotations, test correlation between G*(t) trajectory features and expert-annotated faithfulness labels. If overlap is insufficient, use FaithCoT-Bench's task types as proxy.
(iii) **TTS cross-reference**: compute Zhao et al.'s True Thinking Score on the same examples; test whether high-TTS examples (genuine reasoning candidates) vs. low-TTS examples (decorative candidates) produce distinguishable G*(t) shapes.

*Supplementary (self-consistency check, NOT primary evidence):* Partition by P*(t) and C(t) features (as originally proposed) and verify consistency with external-standard results.

Apply Gjølbye et al.'s (2605.15454) length correction (residualizing on log(N)). Success criterion: d > 0.5 between at least 2 externally-defined partitions on 2+ features. If d < 0.3, downscope to characterization paper.

**Phase 1: Full ICG Construction (Weeks 4-9).** Conditional on Phase 0b d > 0.5. Extend to 4 models (add QwQ-32B or R1-Distill-32B) × 4 benchmarks (add GPQA-Diamond or AIME). Full calibrated P*(t) with null-probe normalization + MCT supplementary concordance on 500 examples. Three C(t) estimators (NLDD on 32B conditional on Phase 0a feasibility) with Ballon et al.-style controls. Cross-reference with TTS at step boundaries. Bootstrap confidence intervals on G*(t). Primary resolution: 20-50 equally-spaced positions; token-level on 200-example subset for fine-grained analysis.

**Phase 2: Task-Difficulty Conditioning (Weeks 7-11).** Partition each benchmark into difficulty quintiles. Measure G*(t) per quintile. Hypothesis: easy → large persistent gap (decorative CoT), hard → converging gap (load-bearing CoT). Following Gjølbye et al., apply length correction and report domain-specific effects — expecting stronger effects on math/code than MMLU, given ρ⊥ = +0.41 on Codeforces vs. +0.05 on MATH.

**Phase 3: Phenomenon Classification, Baselines, and Robustness (Weeks 9-14).**

*Classification framework:* Apply trajectory-shape classification to real data using G*(t) features (initial value, slope, convergence rate, dC/dt locality) + Chrabąszcz-style features (volatility, trend, boundary transients, autocorrelation). Classifier gradient: logistic regression → random forest → simple MLP; report all results to avoid cherry-picking. Evaluation: macro-F1 (primary, handles class imbalance) + confusion matrix + calibrated probability (reliability diagram). Cross-validation: 5-fold random + cross-model generalization (train on model A, test on model B) + cross-benchmark generalization (train on GSM8K, test on MATH).

*Baselines for phenomenon classification:* (a) Random classifier + majority-class classifier; (b) Difficulty-only classifier (predict phenomenon from difficulty quintile alone — verifies that G*(t) features provide information beyond simple difficulty stratification); (c) **Chrabąszcz probe-trajectory-only features** — use only P*(t) trajectory features without C(t), as a "no causal dimension" ablation quantifying the incremental contribution of the dual-stream design; (d) **TTS-based classification** — use Zhao et al.'s per-step TTS values for the same examples, testing whether per-step causal contribution alone (without the probe dimension) achieves comparable phenomenon discrimination.

*Head-to-head TIF validation:* Benchmark TIF score against: (a) FaithCoT-Bench's 11 detection methods (at minimum: Adding Mistakes, Removing Steps, Early Answering from counterfactual paradigm; paraphrasing method) on overlapping examples, comparing instance-level correlation with expert ground truth; (b) TTS as a per-step causal contribution baseline, comparing correlation with faithfulness labels.

*Robustness ablations (6 dimensions):* (a) probe architecture (linear vs. 2-layer MLP) with selectivity; (b) layer selection (single best vs. multi-layer); (c) C(t) estimator agreement (prefix vs. paraphrase vs. NLDD); (d) gap normalization method (rank-based vs. min-max vs. z-score); (e) calibration method (shuffled-label vs. random-representation); (f) probe target (correctness vs. answer-content on binary/MC subsets). Report sensitivity ranges across all dimensions.

**TIF Score.** Temporal Information-contribution Faithfulness score: normalized area under calibrated G*(t), benchmarked against FaithCoT-Bench and Liu et al.'s (2602.13904) text-level metrics.

**Paper Focus (Tightened).** Core contributions: (1) calibrated ICG diagnostic with shape-based trajectory analysis on 4 models × 4 benchmarks, introducing the dual-stream gap that enables faithful-vs-unfaithful distinction impossible from probe trajectories alone; (2) Phase 0b empirical pilot with external validation standards (difficulty partition, FaithCoT-Bench, TTS cross-reference) demonstrating 2-3 distinguishable G*(t) phenomenon signatures; (3) task-difficulty conditioning revealing the decorative→load-bearing transition with domain-specific strength; (4) head-to-head comparison showing ICG's incremental value over probe-only trajectories, TTS, and FaithCoT-Bench methods. Supporting: robustness ablations (6 dimensions); TIF validation. Supplementary: 671B subset (500 examples, 3 layers); answer-content vs. correctness probe comparison; semi-synthetic simulation as hypothesis generation.

**Experiments.** DeepSeek-R1-Distill-Qwen-7B/14B/32B, QwQ-32B across MMLU, GPQA-Diamond, GSM8K, AIME. 671B validation (500-example subset, 3 layers). Calibration checks: synthetic arithmetic (G* ≈ 0 expected), TTS cross-reference, MCT supplementary concordance. Gjølbye-style length correction on all temporal analyses.

## Resource Estimate
{'manual': {'gpu_hours': '~830 H100-hours (Phase 0a characterization + NLDD feasibility: 90 hrs [3 models × 3 datasets, probe training + prefix ablation + steering tests + NLDD feasibility on 7B]; Phase 0b empirical pilot: 30 hrs [1 model × 2 datasets, full G*(t) construction + external validation]; Phase 1 full ICG: 120 hrs [4 models × 4 benchmarks, multi-layer probes + 3 C(t) estimators]; Phase 2 difficulty conditioning: 50 hrs; Phase 3 phenomenon classification + baselines + robustness: 60 hrs; NLDD on 32B model: 250 hrs [conditional on Phase 0a feasibility — primary bottleneck]; NLDD on 7B/14B models: 100 hrs; MCT geometric validation: 50 hrs [supplementary]; 671B subset: 50 hrs [8×H100]; semi-synthetic simulation: 30 hrs [mostly CPU])', 'timeline': '15-17 weeks (2 researchers: 4 weeks Phase 0a+0b; 5 weeks Phase 1; 4 weeks Phases 2-3 in parallel with NLDD; 2-3 weeks writing + ablations)', 'estimated_gpu_cost': '$2,500 at ~$3/H100-hour (cloud spot pricing)', 'storage': '3-5 TB (4 layers per model, fp16); reducible to ~1.5 TB via PCA or on-the-fly evaluation'}, 'human_in_loop': {'gpu_hours': '~830 H100-hours', 'timeline': '13 weeks (1 researcher + Claude for experiment design and analysis)', 'claude_api_cost': '$350', 'estimated_gpu_cost': '$2,500'}, 'auto_research': {'gpu_hours': '~830 H100-hours', 'timeline': '11 weeks', 'claude_api_cost': '$700', 'estimated_gpu_cost': '$2,500', 'speed_bottleneck': 'NLDD on 32B (~250 H100-hours, conditional on Phase 0a feasibility, ~30% of total compute) is the primary bottleneck. Phase 0b pilot (30 hrs) provides early go/no-go signal before committing full Phase 1-3 compute.'}}

## Inspired By
The convergence of five independent lines of evidence — (a) Cox et al.'s finding that answer-content probe steering fails on reasoning models despite high accuracy; (b) Yuan et al.'s systematic demonstration that four interventions all fail on correctness probes, establishing 'diagnostic not causal'; (c) the temporal probe dynamics now empirically characterized by David (0.84 AUC at t=4, stable ~0.8), Zhang et al. (chunk-level rising trajectory), Esakkiraja et al. (pre-generation >90% with dip-recovery), and Chrabąszcz et al. (60+ trajectory features capturing dynamics invisible to static probes, up to 17pp improvement); (d) Ballon et al.'s truncation-reinjection protocol demonstrating monotonic behavioral C(t) curves with rigorous controls; (e) the trajectory-shape literature (arXiv 2603.18940, 2602.06266, 2604.05655) showing that shape features carry diagnostic information beyond absolute values — all pointing to the same insight: the gap between diagnostic information availability and causal contribution IS the phenomenon of interest, and its temporal trajectory shape reveals the mechanism of faithfulness or unfaithfulness. Additionally inspired by: Wang's (2604.15726) H1/H2/H0 hypotheses; Gjølbye et al.'s (2605.15454) domain-specific difficulty-geometry coupling; Chun et al.'s (2602.20338) MCT geometric pulse; and the CMI framework's (2602.03994) structural mediation approach, which our functional gap methodology complements.

## Target Venues
- ICLR 2027 (abstract: Sep 19, full paper: Sep 24, 2026; conference: Apr/May 2027 — primary target, 4 months from now)
- ICML 2027 (full paper: Jan 29, 2027; conference: Jul 2027 — comfortable fallback if additional experiments needed)

## Key References
- Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics (Chrabąszcz et al., arXiv 2605.18549)
- Probing the Trajectories of Reasoning Traces in Large Language Models (Ballon et al., arXiv 2601.23163)
- LLM Reasoning Is Latent, Not the Chain of Thought (Wang, arXiv 2604.15726)
- Reasoning Models Don't Just Think Longer, They Move Differently (Gjølbye et al., arXiv 2605.15454)
- Hidden Error Awareness: The Signal Is Diagnostic, Not Causal (Yuan et al., arXiv 2605.09502)
- Decoding Answers Before Chain-of-Thought: Pre-CoT Probes and Activation Steering (Cox et al., arXiv 2603.01437)
- Temporal Predictors of Outcome in Reasoning Language Models (David, arXiv 2511.14773)
- Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification (Zhang et al., arXiv 2504.05419)
- Therefore I am. I Think (Esakkiraja et al., arXiv 2604.01202)
- Can Aha Moments Be Fake? True Thinking Score (Zhao et al., arXiv 2510.24941)
- Mechanistic Evidence for Faithfulness Decay / NLDD (Ye et al., arXiv 2602.11201)
- Do LLMs Experience an Internal Polylogue? (Herrmann et al., arXiv 2605.09159)
- LLMs Faithfully and Iteratively Compute Answers During CoT (Kudo et al., EACL 2026, arXiv 2412.01113)
- When Chains of Thought Don't Matter: Causal Bypass / CMI (Sathyanarayanan et al., arXiv 2602.03994)
- Spatiotemporal Hidden-State Dynamics / StALT (Furuya & Tanimura, arXiv 2605.01853)
- Mapping Faithful Reasoning / Concept Walk (Li et al., arXiv 2510.22362, NeurIPS 2025 MechInterp Workshop)
- Task Difficulty Shapes CoT Faithfulness (ICLR 2026 Workshop)
- Diagnosing Pathological CoT (Liu et al., arXiv 2602.13904)
- Measuring Faithfulness Depends on How You Measure (Young, arXiv 2603.20172)
- Emergent Manifold Separability / MCT (Chun et al., arXiv 2602.20338)
- Tracing the Traces: Latent Temporal Signals (Vilas et al., ICLR 2026, arXiv 2510.10494)
- Probing and Steering CoT Unfaithfulness (Occhipinti et al., ICLR 2026 LIT Workshop)
- Designing and Interpreting Probes with Control Tasks (Hewitt & Liang, EMNLP 2019)
- Information-Theoretic Probing with MDL (Voita & Titov, EMNLP 2020, arXiv 2003.12298)
- Probing the Probing Paradigm (Ravichander et al., arXiv 2005.00719)
- Shape-over-magnitude dissociation in entropy trajectories (arXiv 2603.18940)
- Is My Model Mind Blurting? RQA of Reasoning Dynamics (arXiv 2602.06266)
- LLM Reasoning as Trajectories (arXiv 2604.05655, Microsoft)
- Internal States Before Wait Modulate Reasoning Patterns (arXiv 2510.04128)
- FACT-E (Sun et al., ACL Findings 2026, arXiv 2604.10693)
- Breaking the Chain (Somov et al., arXiv 2603.16475)
- The Illusion of Reasoning (Basu & Chakraborty, arXiv 2603.22816)
- FaithCoT-Bench (ICLR 2026, arXiv 2510.04040)
- The Mirage of Explainability survey (Jin et al., ARR for ACL 2026)
- Reasoning Theater (Boppana et al., arXiv 2603.05488)
- No Global Plan in CoT (Xu et al., arXiv 2602.02103)
- Catching Rationalization in the Act (Mirtaheri & Belkin, arXiv 2603.17199)
- CoT Monitorability via Information Theory (Anwar et al., arXiv 2602.18297)
- Understanding CoT via Information Theory (Ton et al., ICML 2025, arXiv 2411.11984)
- Demystifying Reasoning Dynamics with MI (Qian et al., NeurIPS 2025, arXiv 2506.02867)
- Analysing CoT Dynamics (Lewis-Lim et al., EMNLP 2025, arXiv 2508.19827)
- Why Models Know But Don't Say (Young, arXiv 2603.26410)
- Lie to Me (arXiv 2603.22582)
- Step-Level Hallucination via Transport Geometry (Alvarez & Baheri, arXiv 2605.13772)
- From Reasoning to Answer (arXiv 2509.23676)
- SAE Reasoning Features (arXiv 2503.18878)
- FRIT (Swaroop et al., arXiv 2509.13334)
- Solution Hides in Hidden States (arXiv 2604.23351)
- Knowing Before Saying (ACL Findings 2025, arXiv 2505.24362)
- LEACE: Perfect Linear Concept Erasure (Belrose et al., NeurIPS 2023, arXiv 2306.03819)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "b15418e1-7e26-425c-8335-7273c8cf23f6",
  "type": "user",
  "uuid": "5dba601c-6142-40cd-a92d-70378289bf31",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:05:12.466Z_

```json
{
  "parentUuid": "5dba601c-6142-40cd-a92d-70378289bf31",
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
  "uuid": "9792eeb9-bea4-4d02-9049-63a5913de193",
  "timestamp": "2026-05-20T04:05:12.466Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:05:12.466Z_

```json
{
  "parentUuid": "9792eeb9-bea4-4d02-9049-63a5913de193",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "769bbc57-afe3-4e72-9a16-4b98ace53562",
  "timestamp": "2026-05-20T04:05:12.466Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
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
  "lastPrompt": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness  ## Description We propose the Information-Contribution Gap (ICG)…",
  "leafUuid": "769bbc57-afe3-4e72-9a16-4b98ace53562",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Measuring models' knowledge-action gaps in reasoning with temporal probes",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd"
}
```

---

### Assistant

_source line 8 · 2026-05-20T04:05:20.445Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully read and analyze this proposal. It's about measuring the gap between what language models internally know (via probes on hidden states) and what their chain-of-thought (CoT) reasoning actually contributes causally to their outputs. The framework is called ICG (Information-Contribution Gap).

Let me first do thorough web searches to understand the current landscape before making any judgments.

Key things I need to search for:
1. The most recent work on CoT faithfulness measurement (2025-2026)
2. Probe trajectory analysis work (Chrabąszcz et al., and others)
3. The diagnostic-causal gap literature


4. Whether existing work already explores similar ideas about trajectory shape and reasoning patterns
5. Any recent studies on how reasoning traces evolve through model layers

Let me start with targeted searches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "769bbc57-afe3-4e72-9a16-4b98ace53562",
  "isSidechain": false,
  "requestId": "req_011CbDABxNdkracU9d48wqky",
  "type": "assistant",
  "uuid": "5ed29cac-532e-4109-8140-5d28087a0398",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EQL8arTyd4Z2vdNqBKPBVp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14864,
      "cache_read_input_tokens": 14549,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14864,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 300,
          "cache_read_input_tokens": 14549,
          "cache_creation_input_tokens": 14864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14864
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

_source line 9 · 2026-05-20T04:05:20.447Z_

I'll start by reading the proposal carefully and then conducting thorough web searches before making any judgments. Let me do the pre-research first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ed29cac-532e-4109-8140-5d28087a0398",
  "isSidechain": false,
  "requestId": "req_011CbDABxNdkracU9d48wqky",
  "type": "assistant",
  "uuid": "33c308ba-12df-4998-b9fa-a800dc0d5707",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EQL8arTyd4Z2vdNqBKPBVp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14864,
      "cache_read_input_tokens": 14549,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14864,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 300,
          "cache_read_input_tokens": 14549,
          "cache_creation_input_tokens": 14864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14864
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

_source line 10 · 2026-05-20T04:05:20.454Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MhYj8jPHFamuWh4r93utdc`</summary>

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
  "parentUuid": "33c308ba-12df-4998-b9fa-a800dc0d5707",
  "isSidechain": false,
  "requestId": "req_011CbDABxNdkracU9d48wqky",
  "type": "assistant",
  "uuid": "b612a49e-1126-4f22-bb5e-bb1e9f8e7dd9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EQL8arTyd4Z2vdNqBKPBVp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14864,
      "cache_read_input_tokens": 14549,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14864,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 300,
          "cache_read_input_tokens": 14549,
          "cache_creation_input_tokens": 14864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14864
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

_source line 11 · 2026-05-20T04:05:20.460Z_

<details><summary>↩ Tool result · `toolu_01MhYj8jPHFamuWh4r93utdc`</summary>

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
  "parentUuid": "b612a49e-1126-4f22-bb5e-bb1e9f8e7dd9",
  "isSidechain": false,
  "promptId": "b15418e1-7e26-425c-8335-7273c8cf23f6",
  "type": "user",
  "uuid": "3a5fe187-2a30-4c3c-a554-75be9ce94b25",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "b612a49e-1126-4f22-bb5e-bb1e9f8e7dd9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T04:05:23.288Z_

Now let me conduct the pre-research searches. I'll run multiple searches in parallel to cover the key areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a5fe187-2a30-4c3c-a554-75be9ce94b25",
  "isSidechain": false,
  "requestId": "req_011CbDACYaRxDfSYMNFXfXRN",
  "type": "assistant",
  "uuid": "6a900bbd-be0d-4681-8205-90f1b6a0c156",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyJNAcTuzo6YHtZbWMfRkW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 828,
      "cache_read_input_tokens": 29413,
      "output_tokens": 94,
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
          "input_tokens": 3,
          "output_tokens": 94,
          "cache_read_input_tokens": 29413,
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

_source line 13 · 2026-05-20T04:05:23.578Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EcFPXQeQSnx5UVm8sHS51Y`</summary>

```json
{
  "query": "chain-of-thought faithfulness measurement probe causal gap 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a900bbd-be0d-4681-8205-90f1b6a0c156",
  "isSidechain": false,
  "requestId": "req_011CbDACYaRxDfSYMNFXfXRN",
  "type": "assistant",
  "uuid": "772d4a0c-7985-4b29-bc96-9e3f945f2c04",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyJNAcTuzo6YHtZbWMfRkW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 828,
      "cache_read_input_tokens": 29413,
      "output_tokens": 94,
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
          "input_tokens": 3,
          "output_tokens": 94,
          "cache_read_input_tokens": 29413,
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

_source line 14 · 2026-05-20T04:05:31.661Z_

<details><summary>↩ Tool result · `toolu_01EcFPXQeQSnx5UVm8sHS51Y`</summary>

```text
Web search results for query: "chain-of-thought faithfulness measurement probe causal gap 2025 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING","url":"https://openreview.net/attachment?id=lN3yKqqzF1&name=pdf"},{"title":"faithcot-bench: benchmarking instance- level faithfulness of ...","url":"https://arxiv.org/pdf/2510.04040"},{"title":"Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning | Request PDF","url":"https://www.researchgate.net/publication/386203451_Making_Reasoning_Matter_Measuring_and_Improving_Faithfulness_of_Chain-of-Thought_Reasoning"},{"title":"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures","url":"https://arxiv.org/html/2603.16475v1"},{"title":"FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2510.04040v1"},{"title":"Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models","url":"https://arxiv.org/html/2603.26410"},{"title":"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2602.11201v1"},{"title":"FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness","url":"https://arxiv.org/pdf/2509.13334"}]

Based on the search results, here's what I found about chain-of-thought faithfulness measurement and causal gap research from 2025-2026:

## Recent Research on CoT Faithfulness and Causal Measurement

The FaithCoT-Bench benchmark provides the first instance-level dataset for detecting unfaithful reasoning in Chain-of-Thought outputs, addressing a gap in instance-level CoT unfaithfulness evaluation.

### Approaches to Measuring Faithfulness

Counterfactual-based methods probe CoT faithfulness by perturbing reasoning traces (adding mistakes, removing steps, or forcing early answers), testing whether the final prediction changes, treating such causal sensitivity as evidence of faithfulness since a faithful CoT should preserve a causal link between intermediate steps and the final answer.

Logit-based methods leverage model-internal diagnostics, such as analyzing logit variations or measuring information gain to approximate causal alignment between CoTs and outputs.

### Causal Probing and the Mechanistic Gap

While current benchmarks focus on observable signals, future work will investigate whether these signals align with the model's actual decision process using emerging mechanistic tools such as causal probing, circuit analysis, and hidden-state inspection.

Recent mechanistic evidence identified a "Reasoning Horizon" at 70–85% of chain length, beyond which reasoning tokens have diminishing causal influence on the final answer.

Recent research complements causal measurements with representational similarity analysis (RSA) to track when intermediate representations lose semantic distinctiveness, proposing a framework to quantify CoT faithfulness through behavioral, representational, and geometric perspectives.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "772d4a0c-7985-4b29-bc96-9e3f945f2c04",
  "isSidechain": false,
  "promptId": "b15418e1-7e26-425c-8335-7273c8cf23f6",
  "type": "user",
  "uuid": "0b488bf5-56fc-4007-97c9-ad648fd4b18a",
  "toolUseResult": {
    "query": "chain-of-thought faithfulness measurement probe causal gap 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_019NDgHeF7Nrc4FwJvf6rxbE",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING",
            "url": "https://openreview.net/attachment?id=lN3yKqqzF1&name=pdf"
          },
          {
            "title": "faithcot-bench: benchmarking instance- level faithfulness of ...",
            "url": "https://arxiv.org/pdf/2510.04040"
          },
          {
            "title": "Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning | Request PDF",
            "url": "https://www.researchgate.net/publication/386203451_Making_Reasoning_Matter_Measuring_and_Improving_Faithfulness_of_Chain-of-Thought_Reasoning"
          },
          {
            "title": "Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures",
            "url": "https://arxiv.org/html/2603.16475v1"
          },
          {
            "title": "FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2510.04040v1"
          },
          {
            "title": "Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models",
            "url": "https://arxiv.org/html/2603.26410"
          },
          {
            "title": "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2602.11201v1"
          },
          {
            "title": "FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness",
            "url": "https://arxiv.org/pdf/2509.13334"
          }
        ]
      },
      "Based on the search results, here's what I found about chain-of-thought faithfulness measurement and causal gap research from 2025-2026:\n\n## Recent Research on CoT Faithfulness and Causal Measurement\n\nThe FaithCoT-Bench benchmark provides the first instance-level dataset for detecting unfaithful reasoning in Chain-of-Thought outputs, addressing a gap in instance-level CoT unfaithfulness evaluation.\n\n### Approaches to Measuring Faithfulness\n\nCounterfactual-based methods probe CoT faithfulness by perturbing reasoning traces (adding mistakes, removing steps, or forcing early answers), testing whether the final prediction changes, treating such causal sensitivity as evidence of faithfulness since a faithful CoT should preserve a causal link between intermediate steps and the final answer.\n\nLogit-based methods leverage model-internal diagnostics, such as analyzing logit variations or measuring information gain to approximate causal alignment between CoTs and outputs.\n\n### Causal Probing and the Mechanistic Gap\n\nWhile current benchmarks focus on observable signals, future work will investigate whether these signals align with the model's actual decision process using emerging mechanistic tools such as causal probing, circuit analysis, and hidden-state inspection.\n\nRecent mechanistic evidence identified a \"Reasoning Horizon\" at 70–85% of chain length, beyond which reasoning tokens have diminishing causal influence on the final answer.\n\nRecent research complements causal measurements with representational similarity analysis (RSA) to track when intermediate representations lose semantic distinctiveness, proposing a framework to quantify CoT faithfulness through behavioral, representational, and geometric perspectives."
    ],
    "durationSeconds": 8.077577425000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "772d4a0c-7985-4b29-bc96-9e3f945f2c04",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T04:05:34.012Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Uzi7jfxkrYBsMp2X3xUNR8`</summary>

```json
{
  "query": "Chrabąszcz probe trajectories reasoning dynamics 2605.18549 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b488bf5-56fc-4007-97c9-ad648fd4b18a",
  "isSidechain": false,
  "requestId": "req_011CbDADNHqGmXQW5MbsRhtp",
  "type": "assistant",
  "uuid": "43f78240-aa53-4ee0-8abe-da30f710f2dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FxuPAangzh6g6K5zm55Lqz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 926,
      "cache_read_input_tokens": 30241,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 926,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 30241,
          "cache_creation_input_tokens": 926,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 926
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

_source line 16 · 2026-05-20T04:05:42.261Z_

<details><summary>↩ Tool result · `toolu_01Uzi7jfxkrYBsMp2X3xUNR8`</summary>

```text
Web search results for query: "Chrabąszcz probe trajectories reasoning dynamics 2605.18549 2025"

Links: [{"title":"[2605.18549] Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics","url":"https://arxiv.org/abs/2605.18549"},{"title":"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics","url":"https://arxiv.org/html/2605.18549"},{"title":"Reasoning emerges from constrained inference manifolds in large language models","url":"https://arxiv.org/html/2605.08142"},{"title":"Spatiotemporal Hidden-State Dynamics as a Signature of Internal Reasoning in Large Language Models","url":"https://arxiv.org/html/2605.01853"},{"title":"[2605.01853] Spatiotemporal Hidden-State Dynamics as a Signature of Internal Reasoning in Large Language Models","url":"https://arxiv.org/abs/2605.01853"},{"title":"Trajectory sampling using spatial familiarity","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11435202"},{"title":"The Effect of Probe Dynamics on Galactic Exploration Timescales","url":"https://arxiv.org/pdf/1212.2371"}]

Based on the search results, I found the paper you're looking for:

## Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics

The paper (arXiv:2605.18549) was submitted on May 18, 2026, and authored by Maciej Chrabąszcz, Aleksander Szymczyk, Marcin Sendera, Tomasz Trzciński, and Sebastian Cygert.

**Overview:**
The research investigates Large Reasoning Models (LRMs) and introduces new opportunities for safety monitoring through their Chain of Thought (CoT) reasoning. The authors investigate the hidden representations of LRMs to determine whether future behavior can be predicted from prompt and CoT representations.

**Key Methodology:**
By evaluating a probe at each generated token, the researchers construct a probe trajectory, which is the continuous evolution of a concept's probability across the reasoning process. They find that future model behavior is more distinguishable when examined over the full trajectory than from a single static prediction.

**Important Findings:**
To characterize temporal dynamics, the authors extract signal-processing features that capture volatility, trend, and steady-state behavior, significantly improving the separation of future model states. The choice of pooling operation is critical: average-pooling and last-token methods collapse to near-random performance, while max-pooling achieves up to 95% AUROC.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43f78240-aa53-4ee0-8abe-da30f710f2dd",
  "isSidechain": false,
  "promptId": "b15418e1-7e26-425c-8335-7273c8cf23f6",
  "type": "user",
  "uuid": "a2ed7b80-ab89-4a00-a2e1-d2b3b78e9112",
  "toolUseResult": {
    "query": "Chrabąszcz probe trajectories reasoning dynamics 2605.18549 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CyPaRP6jxwc5djr7WqndLD",
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
            "title": "Reasoning emerges from constrained inference manifolds in large language models",
            "url": "https://arxiv.org/html/2605.08142"
          },
          {
            "title": "Spatiotemporal Hidden-State Dynamics as a Signature of Internal Reasoning in Large Language Models",
            "url": "https://arxiv.org/html/2605.01853"
          },
          {
            "title": "[2605.01853] Spatiotemporal Hidden-State Dynamics as a Signature of Internal Reasoning in Large Language Models",
            "url": "https://arxiv.org/abs/2605.01853"
          },
          {
            "title": "Trajectory sampling using spatial familiarity",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11435202"
          },
          {
            "title": "The Effect of Probe Dynamics on Galactic Exploration Timescales",
            "url": "https://arxiv.org/pdf/1212.2371"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n## Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics\n\nThe paper (arXiv:2605.18549) was submitted on May 18, 2026, and authored by Maciej Chrabąszcz, Aleksander Szymczyk, Marcin Sendera, Tomasz Trzciński, and Sebastian Cygert.\n\n**Overview:**\nThe research investigates Large Reasoning Models (LRMs) and introduces new opportunities for safety monitoring through their Chain of Thought (CoT) reasoning. The authors investigate the hidden representations of LRMs to determine whether future behavior can be predicted from prompt and CoT representations.\n\n**Key Methodology:**\nBy evaluating a probe at each generated token, the researchers construct a probe trajectory, which is the continuous evolution of a concept's probability across the reasoning process. They find that future model behavior is more distinguishable when examined over the full trajectory than from a single static prediction.\n\n**Important Findings:**\nTo characterize temporal dynamics, the authors extract signal-processing features that capture volatility, trend, and steady-state behavior, significantly improving the separation of future model states. The choice of pooling operation is critical: average-pooling and last-token methods collapse to near-random performance, while max-pooling achieves up to 95% AUROC."
    ],
    "durationSeconds": 8.244840814,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "43f78240-aa53-4ee0-8abe-da30f710f2dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T04:05:44.963Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GbDHkJUmnbjZD8zhAdEx5T`</summary>

```json
{
  "query": "Yuan et al \"hidden error awareness\" \"diagnostic not causal\" reasoning models intervention failure 2605.09502"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2ed7b80-ab89-4a00-a2e1-d2b3b78e9112",
  "isSidechain": false,
  "requestId": "req_011CbDAE9bdFYf5Mg3XdnP1L",
  "type": "assistant",
  "uuid": "04f926b1-956c-4895-a0cc-142d69eccd68",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jrc7hS2mCsSgGijhtYjwew",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 751,
      "cache_read_input_tokens": 31167,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 751,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 31167,
          "cache_creation_input_tokens": 751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 751
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

_source line 18 · 2026-05-20T04:05:53.196Z_

<details><summary>↩ Tool result · `toolu_01GbDHkJUmnbjZD8zhAdEx5T`</summary>

```text
Web search results for query: "Yuan et al "hidden error awareness" "diagnostic not causal" reasoning models intervention failure 2605.09502"

Links: [{"title":"[2605.09502] Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal","url":"https://arxiv.org/abs/2605.09502"},{"title":"Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal","url":"https://arxiv.org/html/2605.09502"},{"title":"Error awareness as evidence accumulation: effects of speed-accuracy trade-off on error signaling","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3417303/"},{"title":"Hide and Seek with LLMs: An Adversarial Game for Sneaky Error Generation and Self-Improving Diagnosis","url":"https://arxiv.org/pdf/2508.03396"},{"title":"Hop, Skip, and Overthink: Diagnosing Why Reasoning Models Fumble during Multi-Hop Analysis","url":"https://arxiv.org/pdf/2508.04699"},{"title":"Automation Bias in Large Language Model Assisted Diagnostic Reasoning Among AI-Trained Physicians","url":"https://www.medrxiv.org/content/10.1101/2025.08.23.25334280.full.pdf"}]

I found the paper you're looking for! Here's what the search reveals about the arXiv paper 2605.09502:

## Paper Overview

The paper "Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal" by Aojie Yuan and colleagues shows that models internally detect their own reasoning errors but outwardly express confidence in them.

## Key Findings

A linear probe on hidden states predicts trace correctness with 0.95 AUROC from the very first reasoning step (0.79), while verbalized confidence for wrong traces is 4.55/5, nearly identical to correct ones (4.87/5). A text-surface classifier achieves only 0.59 on the same data, confirming a gap invisible in the generated text.

## Intervention Failure

Regarding your specific interest in intervention failure: The signal cannot fix the errors it detects; four interventions—activation steering, probe-guided best-of-N, self-correction, and activation patching—all fail; patching destroys output coherence entirely. The signal is diagnostic, not causal: a readout of computation quality, not a lever to redirect it.

## Model Coverage

This hidden error awareness holds across three model families (Qwen, Llama, Phi), 1.5B-72B parameters, and RL-trained reasoning models (DeepSeek-R1, 0.852 AUROC).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04f926b1-956c-4895-a0cc-142d69eccd68",
  "isSidechain": false,
  "promptId": "b15418e1-7e26-425c-8335-7273c8cf23f6",
  "type": "user",
  "uuid": "db08c1ac-771d-4803-a93b-2f9283bbd65f",
  "toolUseResult": {
    "query": "Yuan et al \"hidden error awareness\" \"diagnostic not causal\" reasoning models intervention failure 2605.09502",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WkFh92jABhp8FrygHh3G9C",
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
            "title": "Error awareness as evidence accumulation: effects of speed-accuracy trade-off on error signaling",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3417303/"
          },
          {
            "title": "Hide and Seek with LLMs: An Adversarial Game for Sneaky Error Generation and Self-Improving Diagnosis",
            "url": "https://arxiv.org/pdf/2508.03396"
          },
          {
            "title": "Hop, Skip, and Overthink: Diagnosing Why Reasoning Models Fumble during Multi-Hop Analysis",
            "url": "https://arxiv.org/pdf/2508.04699"
          },
          {
            "title": "Automation Bias in Large Language Model Assisted Diagnostic Reasoning Among AI-Trained Physicians",
            "url": "https://www.medrxiv.org/content/10.1101/2025.08.23.25334280.full.pdf"
          }
        ]
      },
      "I found the paper you're looking for! Here's what the search reveals about the arXiv paper 2605.09502:\n\n## Paper Overview\n\nThe paper \"Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal\" by Aojie Yuan and colleagues shows that models internally detect their own reasoning errors but outwardly express confidence in them.\n\n## Key Findings\n\nA linear probe on hidden states predicts trace correctness with 0.95 AUROC from the very first reasoning step (0.79), while verbalized confidence for wrong traces is 4.55/5, nearly identical to correct ones (4.87/5). A text-surface classifier achieves only 0.59 on the same data, confirming a gap invisible in the generated text.\n\n## Intervention Failure\n\nRegarding your specific interest in intervention failure: The signal cannot fix the errors it detects; four interventions—activation steering, probe-guided best-of-N, self-correction, and activation patching—all fail; patching destroys output coherence entirely. The signal is diagnostic, not causal: a readout of computation quality, not a lever to redirect it.\n\n## Model Coverage\n\nThis hidden error awareness holds across three model families (Qwen, Llama, Phi), 1.5B-72B parameters, and RL-trained reasoning models (DeepSeek-R1, 0.852 AUROC)."
    ],
    "durationSeconds": 8.229348165000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "04f926b1-956c-4895-a0cc-142d69eccd68",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T04:05:56.002Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FEvtthW4g1JLq2XKQmRBTm`</summary>

```json
{
  "query": "\"information contribution gap\" OR \"probe causal contribution divergence\" chain-of-thought temporal trajectory faithfulness 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db08c1ac-771d-4803-a93b-2f9283bbd65f",
  "isSidechain": false,
  "requestId": "req_011CbDAExKzE86rKGeobZ6Z8",
  "type": "assistant",
  "uuid": "21c95933-8657-4dc7-b346-5565b4b771cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAutEBeQvUeJvgDQUUKfRc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 778,
      "cache_read_input_tokens": 31918,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 778,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 31918,
          "cache_creation_input_tokens": 778,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 778
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

_source line 20 · 2026-05-20T04:06:03.640Z_

<details><summary>↩ Tool result · `toolu_01FEvtthW4g1JLq2XKQmRBTm`</summary>

```text
Web search results for query: ""information contribution gap" OR "probe causal contribution divergence" chain-of-thought temporal trajectory faithfulness 2026"

Links: [{"title":"Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models","url":"https://arxiv.org/html/2603.26410v1"},{"title":"Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought","url":"https://arxiv.org/pdf/2510.24941"},{"title":"On the Causal Identifiability of Chain-of-Thought in Language Models","url":"https://www.techrxiv.org/users/973828/articles/1348183/master/file/data/On%20the%20Causal%20Identifiability%20of%20Chain%20of%20Thought%20in%20Language%20Models/On%20the%20Causal%20Identifiability%20of%20Chain%20of%20Thought%20in%20Language%20Models.pdf?inline=true"},{"title":"The Gradient-Causal Gap: Why Gradient Importance Fails on Complex Tasks","url":"https://arxiv.org/html/2602.01442"},{"title":"Under review THE GRADIENT-CAUSAL GAP: WHY GRADIENT","url":"https://arxiv.org/pdf/2602.01442"},{"title":"Analyzing and Improving Chain-of-Thought Monitorability Through Information Theory","url":"https://arxiv.org/pdf/2602.18297"},{"title":"How does Chain of Thought Think? Mechanistic ...","url":"https://arxiv.org/pdf/2507.22928"},{"title":"Verifying Chain-of-Thought Reasoning via Its Computational Graph","url":"https://arxiv.org/html/2510.09312v1"}]

Based on the search results, I found highly relevant research addressing your query topics. Here are the key findings:

## Chain-of-Thought Faithfulness Divergence

Recent research shows that divergence between thinking tokens and final answers is not a byproduct of reasoning length, with no practically meaningful association between reasoning chain length and divergence rate observed.

## Causal Contribution Analysis

Studies propose metrics like the True Thinking Score (TTS) to quantify the causal contribution of each step in chain-of-thought reasoning, revealing that LLMs often interleave between true-thinking steps (which causally drive the final output) and decorative-thinking steps (which have minimal causal influence). Research shows that only a small subset of reasoning steps causally drive the model's prediction—for example, on AIME, only an average of 2.3% of reasoning steps have high causal contribution for Qwen-2.5.

## Temporal Patterns in Reasoning

A "Reasoning Horizon" exists at 70–85% of chain length, beyond which reasoning tokens have diminishing causal influence on the final answer. Models often commit to answers early in the reasoning chain, with subsequent tokens serving a performative rather than computational role.

## Related Work on Gaps

The Gradient-Causal Gap has been formalized, representing the divergence between what gradients signal as important and what causally matters for out-of-distribution generalization.

The search results contain multiple 2026 publications addressing these themes of causal contribution analysis and chain-of-thought faithfulness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21c95933-8657-4dc7-b346-5565b4b771cc",
  "isSidechain": false,
  "promptId": "b15418e1-7e26-425c-8335-7273c8cf23f6",
  "type": "user",
  "uuid": "1388b086-d3fa-4753-9981-2b78bfa1807e",
  "toolUseResult": {
    "query": "\"information contribution gap\" OR \"probe causal contribution divergence\" chain-of-thought temporal trajectory faithfulness 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0161VJbKkkXVnhjjnbhvXsoq",
        "content": [
          {
            "title": "Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models",
            "url": "https://arxiv.org/html/2603.26410v1"
          },
          {
            "title": "Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought",
            "url": "https://arxiv.org/pdf/2510.24941"
          },
          {
            "title": "On the Causal Identifiability of Chain-of-Thought in Language Models",
            "url": "https://www.techrxiv.org/users/973828/articles/1348183/master/file/data/On%20the%20Causal%20Identifiability%20of%20Chain%20of%20Thought%20in%20Language%20Models/On%20the%20Causal%20Identifiability%20of%20Chain%20of%20Thought%20in%20Language%20Models.pdf?inline=true"
          },
          {
            "title": "The Gradient-Causal Gap: Why Gradient Importance Fails on Complex Tasks",
            "url": "https://arxiv.org/html/2602.01442"
          },
          {
            "title": "Under review THE GRADIENT-CAUSAL GAP: WHY GRADIENT",
            "url": "https://arxiv.org/pdf/2602.01442"
          },
          {
            "title": "Analyzing and Improving Chain-of-Thought Monitorability Through Information Theory",
            "url": "https://arxiv.org/pdf/2602.18297"
          },
          {
            "title": "How does Chain of Thought Think? Mechanistic ...",
            "url": "https://arxiv.org/pdf/2507.22928"
          },
          {
            "title": "Verifying Chain-of-Thought Reasoning via Its Computational Graph",
            "url": "https://arxiv.org/html/2510.09312v1"
          }
        ]
      },
      "Based on the search results, I found highly relevant research addressing your query topics. Here are the key findings:\n\n## Chain-of-Thought Faithfulness Divergence\n\nRecent research shows that divergence between thinking tokens and final answers is not a byproduct of reasoning length, with no practically meaningful association between reasoning chain length and divergence rate observed.\n\n## Causal Contribution Analysis\n\nStudies propose metrics like the True Thinking Score (TTS) to quantify the causal contribution of each step in chain-of-thought reasoning, revealing that LLMs often interleave between true-thinking steps (which causally drive the final output) and decorative-thinking steps (which have minimal causal influence). Research shows that only a small subset of reasoning steps causally drive the model's prediction—for example, on AIME, only an average of 2.3% of reasoning steps have high causal contribution for Qwen-2.5.\n\n## Temporal Patterns in Reasoning\n\nA \"Reasoning Horizon\" exists at 70–85% of chain length, beyond which reasoning tokens have diminishing causal influence on the final answer. Models often commit to answers early in the reasoning chain, with subsequent tokens serving a performative rather than computational role.\n\n## Related Work on Gaps\n\nThe Gradient-Causal Gap has been formalized, representing the divergence between what gradients signal as important and what causally matters for out-of-distribution generalization.\n\nThe search results contain multiple 2026 publications addressing these themes of causal contribution analysis and chain-of-thought faithfulness."
    ],
    "durationSeconds": 7.634738001999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "21c95933-8657-4dc7-b346-5565b4b771cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
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
  "lastPrompt": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness  ## Description We propose the Information-Contribution Gap (ICG)…",
  "leafUuid": "1388b086-d3fa-4753-9981-2b78bfa1807e",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Measuring models' knowledge-action gaps in reasoning with temporal probes",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd"
}
```

---

### Tool call

_source line 23 · 2026-05-20T04:06:08.138Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013PsjpzYfzFv5k28nZf2zUM`</summary>

```json
{
  "query": "combining probing hidden states causal intervention chain-of-thought dual stream temporal framework 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1388b086-d3fa-4753-9981-2b78bfa1807e",
  "isSidechain": false,
  "requestId": "req_011CbDAFj3ZdtrGz5WGAec9N",
  "type": "assistant",
  "uuid": "0e046efe-d875-4655-bcb8-c62e8e76e898",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PuuRvQLAjH9nN4oPNVgJ9a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 921,
      "cache_read_input_tokens": 32696,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 921,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 32696,
          "cache_creation_input_tokens": 921,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 921
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

_source line 24 · 2026-05-20T04:06:16.050Z_

<details><summary>↩ Tool result · `toolu_013PsjpzYfzFv5k28nZf2zUM`</summary>

```text
Web search results for query: "combining probing hidden states causal intervention chain-of-thought dual stream temporal framework 2026"

Links: [{"title":"When Chain-of-Thought Fails, the Solution Hides in the Hidden States","url":"https://arxiv.org/html/2604.23351v1"},{"title":"time2time: Causal Intervention in Hidden States to Simulate Rare Events in Time Series Foundation Models","url":"https://arxiv.org/html/2509.05801v1"},{"title":"time2time: Causal Intervention in Hidden States to Simulate Rare Events in Time Series Foundation Models","url":"https://arxiv.org/pdf/2509.05801"},{"title":"Dynamics Within Latent Chain-of-Thought: An Empirical Study of Causal Structure","url":"https://arxiv.org/pdf/2602.08783"},{"title":"Causal-INSIGHT: Probing Temporal Models to Extract Causal Structure","url":"https://arxiv.org/pdf/2603.25473"},{"title":"Think-as-You-See: Streaming Chain-of-Thought Reasoning for Large Vision-Language Models","url":"https://arxiv.org/pdf/2603.02872"}]

Based on the web search results, I found several recent papers (from 2025-2026) that combine elements of your query related to probing hidden states, causal intervention, and chain-of-thought reasoning:

1. **"When Chain-of-Thought Fails, the Solution Hides in the Hidden States"** - This work uses a causal intervention framework that patches hidden states from individual tokens in a CoT generation into the same layer of a direct-answer run for arithmetic problems, measuring the effect on final-answer accuracy.

2. **"time2time: Causal Intervention in Hidden States to Simulate Rare Events in Time Series Foundation Models"** - This paper extracts statistical moments of hidden activations from a style event and re-standardizes them, implanting the dynamics of one event (e.g., a market crash) into another, steering the model's forecast accordingly.

3. **"Dynamics Within Latent Chain-of-Thought: An Empirical Study of Causal Structure"** - This work conceptualizes latent CoT as a causal system and evaluates it with intervention-based causal analysis, performing step-wise do-interventions that modify an intermediate state while keeping downstream computation unchanged.

4. **"Think-as-You-See: Streaming Chain-of-Thought Reasoning for Large Vision-Language Models"** - This framework introduces a streaming attention mask to enforce temporal causality, a decoupled positional encoding strategy, and a parallel dual KV-cache mechanism that decouples visual encoding from reasoning generation.

5. **"Causal-INSIGHT: Probing Temporal Models to Extract Causal Structure"** - Causal-INSIGHT is a model-agnostic, post-hoc interpretation framework that extracts model-implied causal structure from trained temporal predictors through systematic, intervention-inspired input clamping applied at inference time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e046efe-d875-4655-bcb8-c62e8e76e898",
  "isSidechain": false,
  "promptId": "b15418e1-7e26-425c-8335-7273c8cf23f6",
  "type": "user",
  "uuid": "7a02dbc0-8366-4c27-b2e3-f82f23cffb80",
  "toolUseResult": {
    "query": "combining probing hidden states causal intervention chain-of-thought dual stream temporal framework 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018rhReLyhUTVzGdzXMRRhLo",
        "content": [
          {
            "title": "When Chain-of-Thought Fails, the Solution Hides in the Hidden States",
            "url": "https://arxiv.org/html/2604.23351v1"
          },
          {
            "title": "time2time: Causal Intervention in Hidden States to Simulate Rare Events in Time Series Foundation Models",
            "url": "https://arxiv.org/html/2509.05801v1"
          },
          {
            "title": "time2time: Causal Intervention in Hidden States to Simulate Rare Events in Time Series Foundation Models",
            "url": "https://arxiv.org/pdf/2509.05801"
          },
          {
            "title": "Dynamics Within Latent Chain-of-Thought: An Empirical Study of Causal Structure",
            "url": "https://arxiv.org/pdf/2602.08783"
          },
          {
            "title": "Causal-INSIGHT: Probing Temporal Models to Extract Causal Structure",
            "url": "https://arxiv.org/pdf/2603.25473"
          },
          {
            "title": "Think-as-You-See: Streaming Chain-of-Thought Reasoning for Large Vision-Language Models",
            "url": "https://arxiv.org/pdf/2603.02872"
          }
        ]
      },
      "Based on the web search results, I found several recent papers (from 2025-2026) that combine elements of your query related to probing hidden states, causal intervention, and chain-of-thought reasoning:\n\n1. **\"When Chain-of-Thought Fails, the Solution Hides in the Hidden States\"** - This work uses a causal intervention framework that patches hidden states from individual tokens in a CoT generation into the same layer of a direct-answer run for arithmetic problems, measuring the effect on final-answer accuracy.\n\n2. **\"time2time: Causal Intervention in Hidden States to Simulate Rare Events in Time Series Foundation Models\"** - This paper extracts statistical moments of hidden activations from a style event and re-standardizes them, implanting the dynamics of one event (e.g., a market crash) into another, steering the model's forecast accordingly.\n\n3. **\"Dynamics Within Latent Chain-of-Thought: An Empirical Study of Causal Structure\"** - This work conceptualizes latent CoT as a causal system and evaluates it with intervention-based causal analysis, performing step-wise do-interventions that modify an intermediate state while keeping downstream computation unchanged.\n\n4. **\"Think-as-You-See: Streaming Chain-of-Thought Reasoning for Large Vision-Language Models\"** - This framework introduces a streaming attention mask to enforce temporal causality, a decoupled positional encoding strategy, and a parallel dual KV-cache mechanism that decouples visual encoding from reasoning generation.\n\n5. **\"Causal-INSIGHT: Probing Temporal Models to Extract Causal Structure\"** - Causal-INSIGHT is a model-agnostic, post-hoc interpretation framework that extracts model-implied causal structure from trained temporal predictors through systematic, intervention-inspired input clamping applied at inference time."
    ],
    "durationSeconds": 7.907778027,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0e046efe-d875-4655-bcb8-c62e8e76e898",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T04:06:18.836Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014DmXuyJrUEicxVb2bRktip`</summary>

```json
{
  "query": "CoT faithfulness \"probe trajectory\" \"causal contribution\" gap measurement reasoning model 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a02dbc0-8366-4c27-b2e3-f82f23cffb80",
  "isSidechain": false,
  "requestId": "req_011CbDAGe5BwBiNf3YexoNEN",
  "type": "assistant",
  "uuid": "0f91683f-4ff7-4d03-9877-6faa347e14b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FnprL9yFsR69XGHtnZUBXg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 818,
      "cache_read_input_tokens": 33617,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 818,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 33617,
          "cache_creation_input_tokens": 818,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 818
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

_source line 26 · 2026-05-20T04:06:26.473Z_

<details><summary>↩ Tool result · `toolu_014DmXuyJrUEicxVb2bRktip`</summary>

```text
Web search results for query: "CoT faithfulness "probe trajectory" "causal contribution" gap measurement reasoning model 2025 2026 arxiv"

Links: [{"title":"Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING","url":"https://arxiv.org/pdf/2510.04040"},{"title":"Under review as a conference paper at ICLR 2026 THOUGHT ANCHORS: WHICH LLM","url":"https://arxiv.org/pdf/2506.19143"},{"title":"Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2402.13950v3"},{"title":"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2602.11201"},{"title":"Bypassing the Rationale: Causal Auditing of Implicit Reasoning in Language Models","url":"https://arxiv.org/pdf/2602.03994"},{"title":"FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2510.04040v1"},{"title":"Evaluating Reasoning Faithfulness in Medical Vision-Language Models using Multimodal Perturbations","url":"https://arxiv.org/html/2510.11196v1"},{"title":"Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?","url":"https://arxiv.org/pdf/2508.19827"}]

The search results contain several relevant papers on CoT (Chain-of-Thought) faithfulness from 2025-2026. Here are the key findings:

## Recent Research on CoT Faithfulness Measurement

Recent approaches probe CoT faithfulness by perturbing reasoning traces (adding mistakes, removing steps, or forcing early answers) and testing whether final predictions change accordingly, with causal sensitivity treated as evidence of faithfulness since a faithful CoT should preserve a causal link between intermediate steps and the final answer.

One emerging approach proposes understanding reasoning traces through "thought anchors" (critical reasoning steps guiding the trajectory of reasoning) and measuring causal dependencies between sentences via masking approaches to interpret a CoT's wider computational structure.

A metric called NLDD has been introduced to quantify step-level faithfulness by measuring how a model's confidence changes when reasoning steps are corrupted, operating in logit space and normalizing for cross-model comparison.

Complementary structural diagnostics include Representational Similarity Analysis (RSA) to measure alignment between clean and counterfactually corrupted reasoning trajectories, linear probes to track solution-relevant information across layers, and Trajectory Alignment Score (TAS) to quantify geometric drift of reasoning paths in latent space following counterfactual intervention.

Another causal auditing framework measures whether answers are mechanistically mediated by CoT-aligned internal representations using the CoT Mediation Index (CMI) to quantify this dependence and localize where in the network CoT-specific influence arises.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f91683f-4ff7-4d03-9877-6faa347e14b7",
  "isSidechain": false,
  "promptId": "b15418e1-7e26-425c-8335-7273c8cf23f6",
  "type": "user",
  "uuid": "fec14959-6675-4902-b306-a31d02c79e3c",
  "toolUseResult": {
    "query": "CoT faithfulness \"probe trajectory\" \"causal contribution\" gap measurement reasoning model 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XqoUDf6hkapVfCzsoJWpgc",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING",
            "url": "https://arxiv.org/pdf/2510.04040"
          },
          {
            "title": "Under review as a conference paper at ICLR 2026 THOUGHT ANCHORS: WHICH LLM",
            "url": "https://arxiv.org/pdf/2506.19143"
          },
          {
            "title": "Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2402.13950v3"
          },
          {
            "title": "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2602.11201"
          },
          {
            "title": "Bypassing the Rationale: Causal Auditing of Implicit Reasoning in Language Models",
            "url": "https://arxiv.org/pdf/2602.03994"
          },
          {
            "title": "FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2510.04040v1"
          },
          {
            "title": "Evaluating Reasoning Faithfulness in Medical Vision-Language Models using Multimodal Perturbations",
            "url": "https://arxiv.org/html/2510.11196v1"
          },
          {
            "title": "Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?",
            "url": "https://arxiv.org/pdf/2508.19827"
          }
        ]
      },
      "The search results contain several relevant papers on CoT (Chain-of-Thought) faithfulness from 2025-2026. Here are the key findings:\n\n## Recent Research on CoT Faithfulness Measurement\n\nRecent approaches probe CoT faithfulness by perturbing reasoning traces (adding mistakes, removing steps, or forcing early answers) and testing whether final predictions change accordingly, with causal sensitivity treated as evidence of faithfulness since a faithful CoT should preserve a causal link between intermediate steps and the final answer.\n\nOne emerging approach proposes understanding reasoning traces through \"thought anchors\" (critical reasoning steps guiding the trajectory of reasoning) and measuring causal dependencies between sentences via masking approaches to interpret a CoT's wider computational structure.\n\nA metric called NLDD has been introduced to quantify step-level faithfulness by measuring how a model's confidence changes when reasoning steps are corrupted, operating in logit space and normalizing for cross-model comparison.\n\nComplementary structural diagnostics include Representational Similarity Analysis (RSA) to measure alignment between clean and counterfactually corrupted reasoning trajectories, linear probes to track solution-relevant information across layers, and Trajectory Alignment Score (TAS) to quantify geometric drift of reasoning paths in latent space following counterfactual intervention.\n\nAnother causal auditing framework measures whether answers are mechanistically mediated by CoT-aligned internal representations using the CoT Mediation Index (CMI) to quantify this dependence and localize where in the network CoT-specific influence arises."
    ],
    "durationSeconds": 7.632905448999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0f91683f-4ff7-4d03-9877-6faa347e14b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T04:06:29.493Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ru1v9wN1cKu3pzweAaiqmv`</summary>

```json
{
  "query": "Wang 2604.15726 \"latent reasoning\" \"not the chain of thought\" H1 H2 hypotheses"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fec14959-6675-4902-b306-a31d02c79e3c",
  "isSidechain": false,
  "requestId": "req_011CbDAHQbMUqTiLgvkSd2DY",
  "type": "assistant",
  "uuid": "3d51ee06-177b-4a99-97db-58cab093c359",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KWaao8oYuUKSU2GGj78aXw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 851,
      "cache_read_input_tokens": 34435,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 851,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 34435,
          "cache_creation_input_tokens": 851,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 851
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

_source line 28 · 2026-05-20T04:06:36.970Z_

<details><summary>↩ Tool result · `toolu_01Ru1v9wN1cKu3pzweAaiqmv`</summary>

```text
Web search results for query: "Wang 2604.15726 "latent reasoning" "not the chain of thought" H1 H2 hypotheses"

Links: [{"title":"[2604.15726] LLM Reasoning Is Latent, Not the Chain of Thought","url":"https://arxiv.org/abs/2604.15726"},{"title":"LLM Reasoning Is Latent, Not the Chain of Thought","url":"https://arxiv.org/html/2604.15726"},{"title":"The Illusion of Superposition? A Principled Analysis of Latent Thinking in Language Models","url":"https://arxiv.org/pdf/2604.06374"},{"title":"Reasoning Beyond Chain-of-Thought: A Latent Computational Mode in Large Language Models","url":"https://arxiv.org/pdf/2601.08058"},{"title":"Latent Chain-of-Thought as Planning: Decoupling Reasoning from Verbalization","url":"https://arxiv.org/pdf/2601.21358"},{"title":"A Survey on Latent Reasoning","url":"https://arxiv.org/pdf/2507.06203"}]

Based on the search results, I found the paper you're looking for:

The paper "LLM Reasoning Is Latent, Not the Chain of Thought" (arXiv:2604.15726) by Wenshuo Wang argues that large language model reasoning should be studied as latent-state trajectory formation rather than as faithful surface chain-of-thought (CoT).

The paper formalizes three competing hypotheses: H1, reasoning is primarily mediated by latent-state trajectories; H2, reasoning is primarily mediated by explicit surface CoT; and H0, most apparent reasoning gains are better explained by generic serial compute than by any privileged representational object.

The paper emphasizes that this matters because claims about faithfulness, interpretability, reasoning benchmarks, and inference-time intervention all depend on what the field takes the primary object of reasoning to be. The paper was submitted on April 17, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d51ee06-177b-4a99-97db-58cab093c359",
  "isSidechain": false,
  "promptId": "b15418e1-7e26-425c-8335-7273c8cf23f6",
  "type": "user",
  "uuid": "3c32e82d-310a-4630-9690-6dc21072e4c6",
  "toolUseResult": {
    "query": "Wang 2604.15726 \"latent reasoning\" \"not the chain of thought\" H1 H2 hypotheses",
    "results": [
      {
        "tool_use_id": "srvtoolu_01A4eX2zHH5yQkCtE78L2WY7",
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
            "title": "The Illusion of Superposition? A Principled Analysis of Latent Thinking in Language Models",
            "url": "https://arxiv.org/pdf/2604.06374"
          },
          {
            "title": "Reasoning Beyond Chain-of-Thought: A Latent Computational Mode in Large Language Models",
            "url": "https://arxiv.org/pdf/2601.08058"
          },
          {
            "title": "Latent Chain-of-Thought as Planning: Decoupling Reasoning from Verbalization",
            "url": "https://arxiv.org/pdf/2601.21358"
          },
          {
            "title": "A Survey on Latent Reasoning",
            "url": "https://arxiv.org/pdf/2507.06203"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper \"LLM Reasoning Is Latent, Not the Chain of Thought\" (arXiv:2604.15726) by Wenshuo Wang argues that large language model reasoning should be studied as latent-state trajectory formation rather than as faithful surface chain-of-thought (CoT).\n\nThe paper formalizes three competing hypotheses: H1, reasoning is primarily mediated by latent-state trajectories; H2, reasoning is primarily mediated by explicit surface CoT; and H0, most apparent reasoning gains are better explained by generic serial compute than by any privileged representational object.\n\nThe paper emphasizes that this matters because claims about faithfulness, interpretability, reasoning benchmarks, and inference-time intervention all depend on what the field takes the primary object of reasoning to be. The paper was submitted on April 17, 2026."
    ],
    "durationSeconds": 7.472461087000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3d51ee06-177b-4a99-97db-58cab093c359",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-20T04:06:36.974Z_

```json
{
  "parentUuid": "3c32e82d-310a-4630-9690-6dc21072e4c6",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "42d0825f-5dd5-422b-b2b0-b253ffe5b35d",
  "timestamp": "2026-05-20T04:06:36.974Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-20T04:06:40.159Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KRSXnH8z1ax1sDjbAQhidz`</summary>

```json
{
  "query": "Gjølbye 2605.15454 \"reasoning models\" \"move differently\" hidden state trajectory geometry difficulty 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42d0825f-5dd5-422b-b2b0-b253ffe5b35d",
  "isSidechain": false,
  "requestId": "req_011CbDAJBW5m37qqiuzgzgbx",
  "type": "assistant",
  "uuid": "582d85b2-52b9-42ef-a17d-90ce025f7607",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AmGTTBPMUVBkw9jeLuikf8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 694,
      "cache_read_input_tokens": 35286,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 694,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 35286,
          "cache_creation_input_tokens": 694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 694
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

_source line 31 · 2026-05-20T04:06:47.030Z_

<details><summary>↩ Tool result · `toolu_01KRSXnH8z1ax1sDjbAQhidz`</summary>

```text
Web search results for query: "Gjølbye 2605.15454 "reasoning models" "move differently" hidden state trajectory geometry difficulty 2026"

Links: [{"title":"[2605.15454] Reasoning Models Don't Just Think Longer, They Move Differently","url":"https://arxiv.org/abs/2605.15454"},{"title":"Reasoning Models Don’t Just Think Longer, They Move Differently","url":"https://arxiv.org/html/2605.15454"},{"title":"Spatiotemporal Hidden-State Dynamics as a Signature of Internal Reasoning in Large Language Models","url":"https://arxiv.org/html/2605.01853"},{"title":"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry","url":"https://arxiv.org/html/2605.13772"},{"title":"A Statistical Physics of Language Model Reasoning","url":"https://arxiv.org/pdf/2506.04374"},{"title":"[2605.01853] Spatiotemporal Hidden-State Dynamics as a Signature of Internal Reasoning in Large Language Models","url":"https://arxiv.org/abs/2605.01853"},{"title":"Emergent Search and Backtracking in Latent Reasoning Models","url":"https://arxiv.org/pdf/2602.08100"},{"title":"PRISM: A Dual View of LLM Reasoning through Semantic Flow and Latent Computation","url":"https://arxiv.org/pdf/2603.22754"},{"title":"The Geometry of Thought: How Scale Restructures Reasoning In Large Language Models","url":"https://arxiv.org/pdf/2601.13358"}]

Based on the search results, I found the paper you're looking for:

The paper "Reasoning Models Don't Just Think Longer, They Move Differently" (arXiv:2605.15454) by Anders Gjølbye, Lars Kai Hansen, and Sanmi Koyejo (from Technical University of Denmark and Stanford University) was published on May 14, 2026.

**Main findings:**

The paper examines whether reasoning-trained language models are merely computing for more steps or following different internal trajectories when spending more tokens on harder problems. The researchers study this distinction through hidden-state trajectories during chain-of-thought generation across competitive programming, mathematics, and Boolean satisfiability.

**Key insights about trajectory geometry and difficulty:**

Raw trajectory geometry is strongly shaped by generation length, so difficulty-dependent comparisons are misleading without adjustment. After residualizing trajectory statistics on length, difficulty remains systematically coupled to corrected trajectory geometry across all domains studied.

The clearest reasoning-specific separation appears in the code domain, where harder problems show more direct corrected trajectories and less heterogeneous local curvature in reasoning-trained models than in matched instruction-tuned baselines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "582d85b2-52b9-42ef-a17d-90ce025f7607",
  "isSidechain": false,
  "promptId": "b15418e1-7e26-425c-8335-7273c8cf23f6",
  "type": "user",
  "uuid": "05481f67-b9f1-40f4-b8f1-1b58043c84dc",
  "toolUseResult": {
    "query": "Gjølbye 2605.15454 \"reasoning models\" \"move differently\" hidden state trajectory geometry difficulty 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012pPwNvjm4SYugSnMB7QhGd",
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
            "title": "Spatiotemporal Hidden-State Dynamics as a Signature of Internal Reasoning in Large Language Models",
            "url": "https://arxiv.org/html/2605.01853"
          },
          {
            "title": "Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry",
            "url": "https://arxiv.org/html/2605.13772"
          },
          {
            "title": "A Statistical Physics of Language Model Reasoning",
            "url": "https://arxiv.org/pdf/2506.04374"
          },
          {
            "title": "[2605.01853] Spatiotemporal Hidden-State Dynamics as a Signature of Internal Reasoning in Large Language Models",
            "url": "https://arxiv.org/abs/2605.01853"
          },
          {
            "title": "Emergent Search and Backtracking in Latent Reasoning Models",
            "url": "https://arxiv.org/pdf/2602.08100"
          },
          {
            "title": "PRISM: A Dual View of LLM Reasoning through Semantic Flow and Latent Computation",
            "url": "https://arxiv.org/pdf/2603.22754"
          },
          {
            "title": "The Geometry of Thought: How Scale Restructures Reasoning In Large Language Models",
            "url": "https://arxiv.org/pdf/2601.13358"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper \"Reasoning Models Don't Just Think Longer, They Move Differently\" (arXiv:2605.15454) by Anders Gjølbye, Lars Kai Hansen, and Sanmi Koyejo (from Technical University of Denmark and Stanford University) was published on May 14, 2026.\n\n**Main findings:**\n\nThe paper examines whether reasoning-trained language models are merely computing for more steps or following different internal trajectories when spending more tokens on harder problems. The researchers study this distinction through hidden-state trajectories during chain-of-thought generation across competitive programming, mathematics, and Boolean satisfiability.\n\n**Key insights about trajectory geometry and difficulty:**\n\nRaw trajectory geometry is strongly shaped by generation length, so difficulty-dependent comparisons are misleading without adjustment. After residualizing trajectory statistics on length, difficulty remains systematically coupled to corrected trajectory geometry across all domains studied.\n\nThe clearest reasoning-specific separation appears in the code domain, where harder problems show more direct corrected trajectories and less heterogeneous local curvature in reasoning-trained models than in matched instruction-tuned baselines."
    ],
    "durationSeconds": 6.865806207999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "582d85b2-52b9-42ef-a17d-90ce025f7607",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T04:06:49.613Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019yLScnkizzBuUtDNiVGSyR`</summary>

```json
{
  "query": "\"dual stream\" OR \"two-stream\" probe intervention reasoning faithfulness temporal measurement framework 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05481f67-b9f1-40f4-b8f1-1b58043c84dc",
  "isSidechain": false,
  "requestId": "req_011CbDAJvXxGYS2hxJvZiSxY",
  "type": "assistant",
  "uuid": "e2ce477e-eda4-41da-982e-184a7f3c7b92",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fyq2j7oke49LCaghr5ucEU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 35980,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 771,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 35980,
          "cache_creation_input_tokens": 771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 771
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

_source line 33 · 2026-05-20T04:06:56.150Z_

<details><summary>↩ Tool result · `toolu_019yLScnkizzBuUtDNiVGSyR`</summary>

```text
Web search results for query: ""dual stream" OR "two-stream" probe intervention reasoning faithfulness temporal measurement framework 2025 2026"

Links: [{"title":"Dual-Stream Time Series Prediction Algorithm Based on Inter-scale Interaction | Springer Nature Link","url":"https://link.springer.com/10.1007/978-981-95-5696-0_35"},{"title":"Downloads 2025","url":"https://neurips.cc/Downloads/2025"},{"title":"Dual-Stream Attention-Enhanced Memory Networks for Video Anomaly Detection - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12431475/"},{"title":"A Survey of Reasoning and Agentic Systems in Time Series with Large Language Models","url":"https://arxiv.org/html/2509.11575v1"},{"title":"ProAct: A Dual-System Framework for Proactive Embodied Social Agents","url":"https://arxiv.org/pdf/2602.14048"},{"title":"CircuitProbe: Tracing Visual Temporal Evidence Flow in Video Language Models","url":"https://arxiv.org/pdf/2507.19420"}]

I've performed a web search for your query. Here are the results:

The search returned several relevant papers from 2025-2026:

1. **Dual-Stream Time Series Prediction** - A dual-stream network architecture was proposed to address scale heterogeneity in multivariate time series, using LSTM networks and linear layers to capture different temporal characteristics, with a cross-scale attention mechanism for multi-scale information fusion.

2. **Causality and Intervention in AI Systems** - The NeurIPS 2025 downloads page includes papers on intervention-based approaches, including works on causal reasoning and debiasing LLMs through intervention methods.

3. **Dual-Stream Attention for Video Analysis** - A hierarchical multi-scale temporal encoder and position-aware global relation network were employed to capture both local and long-range dependencies for video anomaly detection.

4. **Time Series Reasoning with LLMs** - Recent work in 2025-2026 includes LLM-based agents for anomaly detection and hierarchical multi-agent frameworks for interpretable anomaly explanations.

5. **CircuitProbe for Video Language Models** - Analysis-driven intervention yielded improvements on temporal understanding benchmarks in large vision-language models.

The results suggest active research in dual-stream architectures, temporal reasoning, and probe-based intervention methods for evaluating model faithfulness and temporal understanding in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2ce477e-eda4-41da-982e-184a7f3c7b92",
  "isSidechain": false,
  "promptId": "b15418e1-7e26-425c-8335-7273c8cf23f6",
  "type": "user",
  "uuid": "35677131-843e-44c9-aa65-eef6fd4f18d2",
  "toolUseResult": {
    "query": "\"dual stream\" OR \"two-stream\" probe intervention reasoning faithfulness temporal measurement framework 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QRoBdBTiewkXuEB9pJAnhe",
        "content": [
          {
            "title": "Dual-Stream Time Series Prediction Algorithm Based on Inter-scale Interaction | Springer Nature Link",
            "url": "https://link.springer.com/10.1007/978-981-95-5696-0_35"
          },
          {
            "title": "Downloads 2025",
            "url": "https://neurips.cc/Downloads/2025"
          },
          {
            "title": "Dual-Stream Attention-Enhanced Memory Networks for Video Anomaly Detection - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12431475/"
          },
          {
            "title": "A Survey of Reasoning and Agentic Systems in Time Series with Large Language Models",
            "url": "https://arxiv.org/html/2509.11575v1"
          },
          {
            "title": "ProAct: A Dual-System Framework for Proactive Embodied Social Agents",
            "url": "https://arxiv.org/pdf/2602.14048"
          },
          {
            "title": "CircuitProbe: Tracing Visual Temporal Evidence Flow in Video Language Models",
            "url": "https://arxiv.org/pdf/2507.19420"
          }
        ]
      },
      "I've performed a web search for your query. Here are the results:\n\nThe search returned several relevant papers from 2025-2026:\n\n1. **Dual-Stream Time Series Prediction** - A dual-stream network architecture was proposed to address scale heterogeneity in multivariate time series, using LSTM networks and linear layers to capture different temporal characteristics, with a cross-scale attention mechanism for multi-scale information fusion.\n\n2. **Causality and Intervention in AI Systems** - The NeurIPS 2025 downloads page includes papers on intervention-based approaches, including works on causal reasoning and debiasing LLMs through intervention methods.\n\n3. **Dual-Stream Attention for Video Analysis** - A hierarchical multi-scale temporal encoder and position-aware global relation network were employed to capture both local and long-range dependencies for video anomaly detection.\n\n4. **Time Series Reasoning with LLMs** - Recent work in 2025-2026 includes LLM-based agents for anomaly detection and hierarchical multi-agent frameworks for interpretable anomaly explanations.\n\n5. **CircuitProbe for Video Language Models** - Analysis-driven intervention yielded improvements on temporal understanding benchmarks in large vision-language models.\n\nThe results suggest active research in dual-stream architectures, temporal reasoning, and probe-based intervention methods for evaluating model faithfulness and temporal understanding in 2025-2026."
    ],
    "durationSeconds": 6.533564560999992,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e2ce477e-eda4-41da-982e-184a7f3c7b92",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness  ## Description We propose the Information-Contribution Gap (ICG)…",
  "leafUuid": "35677131-843e-44c9-aa65-eef6fd4f18d2",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Measuring models' knowledge-action gaps in reasoning with temporal probes",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd"
}
```

---

### Tool call

_source line 36 · 2026-05-20T04:06:59.013Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L9THQhWeo932w4yASGjFxg`</summary>

```json
{
  "query": "arxiv 2026 \"probe accuracy\" \"causal intervention\" reasoning LLM \"hidden states\" faithfulness gap temporal dynamics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35677131-843e-44c9-aa65-eef6fd4f18d2",
  "isSidechain": false,
  "requestId": "req_011CbDAKbUkbN2NHQTh5MZC8",
  "type": "assistant",
  "uuid": "bc522207-a591-4975-8f57-d65b72ac9ddd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bk2wwS4WNAFxhwgwJ5YMxw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 703,
      "cache_read_input_tokens": 36751,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 36751,
          "cache_creation_input_tokens": 703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 703
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

_source line 37 · 2026-05-20T04:07:06.676Z_

<details><summary>↩ Tool result · `toolu_01L9THQhWeo932w4yASGjFxg`</summary>

```text
Web search results for query: "arxiv 2026 "probe accuracy" "causal intervention" reasoning LLM "hidden states" faithfulness gap temporal dynamics"

Links: [{"title":"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures","url":"https://arxiv.org/html/2603.16475v1"},{"title":"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures | OpenReview","url":"https://openreview.net/forum?id=yfqHr7l2tG"},{"title":"Do LLMs Experience an Internal Polylogue? Investigating Reasoning through the Lens of Personas","url":"https://arxiv.org/html/2605.09159v1"},{"title":"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures","url":"https://arxiv.org/pdf/2603.16475"},{"title":"Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents","url":"https://arxiv.org/pdf/2601.02314"},{"title":"Mathematical Reasoning via Intervention-Based Time-Series Causal Discovery Using LLMs as Concept Mastery Simulators","url":"https://arxiv.org/html/2605.07600v1"}]

The search returned several highly relevant arxiv papers from 2025-2026 that address your query about causal interventions, reasoning in LLMs, faithfulness gaps, and related topics:

## Key Results:

1. **"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures"** (arxiv 2603.16475, March 2026)
   - Tests whether models rely on intermediate structures through causal interventions, revealing models fail to update under logically significant structural edits more than 50% of the time
   - Finds that intermediate structures function as influential context rather than stable causal mediators

2. **"Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents"** (arxiv 2601.02314)
   - Uses hard interventions on intermediate reasoning nodes to measure causal sensitivity of terminal answers
   - Reveals a persistent faithfulness gap and detects causal decoupling with violation density up to 0.77 in factual and scientific domains

3. **"Do LLMs Experience an Internal Polylogue? Investigating Reasoning through the Lens of Personas"** (arxiv 2605.09159)
   - Addresses semantic, functional, and causal faithfulness of internal representations
   - Examines whether features are actionable as steering targets through causal faithfulness testing

4. **"Mathematical Reasoning via Intervention-Based Time-Series Causal Discovery Using LLMs as Concept Mastery Simulators"** (arxiv 2605.07600)
   - Focuses on causal discovery and intervention methods for LLM reasoning

These papers directly address your interest in probe accuracy, causal interventions, hidden states, faithfulness gaps, and temporal dynamics in LLM reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc522207-a591-4975-8f57-d65b72ac9ddd",
  "isSidechain": false,
  "promptId": "b15418e1-7e26-425c-8335-7273c8cf23f6",
  "type": "user",
  "uuid": "5285ab31-abed-4ab5-a38a-af266a17dc1a",
  "toolUseResult": {
    "query": "arxiv 2026 \"probe accuracy\" \"causal intervention\" reasoning LLM \"hidden states\" faithfulness gap temporal dynamics",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WcjDrg4Zm5C54oUkCw13kd",
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
            "title": "Do LLMs Experience an Internal Polylogue? Investigating Reasoning through the Lens of Personas",
            "url": "https://arxiv.org/html/2605.09159v1"
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
            "title": "Mathematical Reasoning via Intervention-Based Time-Series Causal Discovery Using LLMs as Concept Mastery Simulators",
            "url": "https://arxiv.org/html/2605.07600v1"
          }
        ]
      },
      "The search returned several highly relevant arxiv papers from 2025-2026 that address your query about causal interventions, reasoning in LLMs, faithfulness gaps, and related topics:\n\n## Key Results:\n\n1. **\"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures\"** (arxiv 2603.16475, March 2026)\n   - Tests whether models rely on intermediate structures through causal interventions, revealing models fail to update under logically significant structural edits more than 50% of the time\n   - Finds that intermediate structures function as influential context rather than stable causal mediators\n\n2. **\"Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents\"** (arxiv 2601.02314)\n   - Uses hard interventions on intermediate reasoning nodes to measure causal sensitivity of terminal answers\n   - Reveals a persistent faithfulness gap and detects causal decoupling with violation density up to 0.77 in factual and scientific domains\n\n3. **\"Do LLMs Experience an Internal Polylogue? Investigating Reasoning through the Lens of Personas\"** (arxiv 2605.09159)\n   - Addresses semantic, functional, and causal faithfulness of internal representations\n   - Examines whether features are actionable as steering targets through causal faithfulness testing\n\n4. **\"Mathematical Reasoning via Intervention-Based Time-Series Causal Discovery Using LLMs as Concept Mastery Simulators\"** (arxiv 2605.07600)\n   - Focuses on causal discovery and intervention methods for LLM reasoning\n\nThese papers directly address your interest in probe accuracy, causal interventions, hidden states, faithfulness gaps, and temporal dynamics in LLM reasoning."
    ],
    "durationSeconds": 7.658512755000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bc522207-a591-4975-8f57-d65b72ac9ddd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T04:07:10.067Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C9FGVBpJi9KtMRybRs2e3m`</summary>

```json
{
  "query": "Sathyanarayanan \"causal bypass\" \"CMI\" \"CoT mediation index\" chain-of-thought 2602.03994"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5285ab31-abed-4ab5-a38a-af266a17dc1a",
  "isSidechain": false,
  "requestId": "req_011CbDALNZuGNcTgPASqCekb",
  "type": "assistant",
  "uuid": "32dbac5e-7820-47b8-be63-926f737120db",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q69RkAvPKWAAZ98UEEaFRj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 849,
      "cache_read_input_tokens": 37454,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 849,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 85,
          "cache_read_input_tokens": 37454,
          "cache_creation_input_tokens": 849,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 849
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

_source line 39 · 2026-05-20T04:07:17.303Z_

<details><summary>↩ Tool result · `toolu_01C9FGVBpJi9KtMRybRs2e3m`</summary>

```text
Web search results for query: "Sathyanarayanan "causal bypass" "CMI" "CoT mediation index" chain-of-thought 2602.03994"

Links: [{"title":"When Chains of Thought Don’t Matter: Causal Bypass in Large Language Models","url":"https://arxiv.org/html/2602.03994"},{"title":"Bypassing the Rationale: Causal Auditing of Implicit Reasoning in Language Models","url":"https://arxiv.org/pdf/2602.03994"},{"title":"[2602.03994] When Chains of Thought Don't Matter: Causal Bypass in Large Language Models","url":"https://arxiv.org/abs/2602.03994"},{"title":"Association of cardiometabolic index with all-cause and cause-specific mortality among overweight and obese adults: a cohort study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12222087/"},{"title":"Is systemic inflammation a missing link between cardiometabolic index with mortality? Evidence from a large population-based study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11191290/"}]

Perfect! I found the paper. Here are the results for your query:

## Paper: "When Chains of Thought Don't Matter: Causal Bypass in Large Language Models"

**Authors:** Anish Sathyanarayanan, Aditya Nagarsekar, and Aarush Rathore from Birla Institute of Technology and Science, Pilani, K. K. Birla Goa Campus

**ArXiv ID:** 2602.03994 (Published February 3, 2026)

**Key Findings:**

Even when CoT is verbose, strategic, and flagged by surface-level manipulation detectors, model answers are often causally independent of the CoT content.

**Core Methodology:**

The key metric, the CoT Mediation Index (CMI), isolates CoT-specific causal influence by comparing performance degradation from patching CoT-token hidden states against matched control patches. The bypass score is calculated as (1 - CMI).

**Main Results:**

CoT-specific influence is typically depth-localized into narrow "reasoning windows," and bypass regimes exist where CMI is near-zero despite plausible CoT text. Additionally, models tuned explicitly for reasoning tend to exhibit stronger and more structured mediation than larger untuned counterparts, while Mixture-of-Experts models show more distributed mediation consistent with routing-based computation.

The paper is available at: https://arxiv.org/abs/2602.03994


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32dbac5e-7820-47b8-be63-926f737120db",
  "isSidechain": false,
  "promptId": "b15418e1-7e26-425c-8335-7273c8cf23f6",
  "type": "user",
  "uuid": "8ad566fe-f14f-489f-9e01-c740d07e78c8",
  "toolUseResult": {
    "query": "Sathyanarayanan \"causal bypass\" \"CMI\" \"CoT mediation index\" chain-of-thought 2602.03994",
    "results": [
      {
        "tool_use_id": "srvtoolu_019cnWuvaWmQMRYGMDaiU9je",
        "content": [
          {
            "title": "When Chains of Thought Don’t Matter: Causal Bypass in Large Language Models",
            "url": "https://arxiv.org/html/2602.03994"
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
            "title": "Association of cardiometabolic index with all-cause and cause-specific mortality among overweight and obese adults: a cohort study",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12222087/"
          },
          {
            "title": "Is systemic inflammation a missing link between cardiometabolic index with mortality? Evidence from a large population-based study",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11191290/"
          }
        ]
      },
      "Perfect! I found the paper. Here are the results for your query:\n\n## Paper: \"When Chains of Thought Don't Matter: Causal Bypass in Large Language Models\"\n\n**Authors:** Anish Sathyanarayanan, Aditya Nagarsekar, and Aarush Rathore from Birla Institute of Technology and Science, Pilani, K. K. Birla Goa Campus\n\n**ArXiv ID:** 2602.03994 (Published February 3, 2026)\n\n**Key Findings:**\n\nEven when CoT is verbose, strategic, and flagged by surface-level manipulation detectors, model answers are often causally independent of the CoT content.\n\n**Core Methodology:**\n\nThe key metric, the CoT Mediation Index (CMI), isolates CoT-specific causal influence by comparing performance degradation from patching CoT-token hidden states against matched control patches. The bypass score is calculated as (1 - CMI).\n\n**Main Results:**\n\nCoT-specific influence is typically depth-localized into narrow \"reasoning windows,\" and bypass regimes exist where CMI is near-zero despite plausible CoT text. Additionally, models tuned explicitly for reasoning tend to exhibit stronger and more structured mediation than larger untuned counterparts, while Mixture-of-Experts models show more distributed mediation consistent with routing-based computation.\n\nThe paper is available at: https://arxiv.org/abs/2602.03994"
    ],
    "durationSeconds": 7.231714418999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "32dbac5e-7820-47b8-be63-926f737120db",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-20T04:07:19.855Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YA1ZPYaPDrFbiY15qD1GSJ`</summary>

```json
{
  "query": "\"trajectory shape\" OR \"trajectory profile\" hidden state reasoning LLM faithfulness classification 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ad566fe-f14f-489f-9e01-c740d07e78c8",
  "isSidechain": false,
  "requestId": "req_011CbDAM9uRe78ieoy96b46y",
  "type": "assistant",
  "uuid": "f6c02897-2d9e-42d8-a484-08689879b74e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcyLH6SX39xUdenqB3dUQJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 752,
      "cache_read_input_tokens": 38303,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 752,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 38303,
          "cache_creation_input_tokens": 752,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 752
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

_source line 41 · 2026-05-20T04:07:26.850Z_

<details><summary>↩ Tool result · `toolu_01YA1ZPYaPDrFbiY15qD1GSJ`</summary>

```text
Web search results for query: ""trajectory shape" OR "trajectory profile" hidden state reasoning LLM faithfulness classification 2025 2026"

Links: [{"title":"Entropy trajectory shape predicts LLM reasoning reliability: A diagnostic study of uncertainty dynamics in chain-of-thought","url":"https://arxiv.org/pdf/2603.18940"},{"title":"Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing","url":"https://arxiv.org/pdf/2604.08401"},{"title":"Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning","url":"https://arxiv.org/pdf/2603.01326"},{"title":"Beyond Scalars: Evaluating and Understanding LLM Reasoning via Geometric Progress and Stability","url":"https://arxiv.org/pdf/2603.10384"},{"title":"LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals","url":"https://arxiv.org/pdf/2604.05655"},{"title":"Probing the Trajectories of Reasoning Traces in Large Language Models","url":"https://arxiv.org/html/2601.23163v1"},{"title":"CLUE: Non-parametric Verification from Experience via Hidden-State Clustering","url":"https://arxiv.org/pdf/2510.01591"}]

I found several highly relevant papers from 2025-2026 on trajectory shapes, hidden states, and LLM reasoning. Here are the key results:

## Key Findings:

A recent study investigates whether the shape of uncertainty dynamics across reasoning steps—captured by sampling answer completions at each step—predicts whether the final answer is correct. The research introduces "entropy-trajectory monotonicity," where a chain is monotone if its per-step answer-distribution entropy decreases at every step, reflecting consistent uncertainty reduction. Monotone chains are significantly more accurate than non-monotone chains.

Another study plots layerwise hidden states as trajectories in activation space, finding that correct generations follow smoother paths, while incorrect ones exhibit sharp deviations.

Research examining whether LLM reasoning steps form a structured trajectory through representation space found that steps unfold as structured geometric motion in representation space, and these trajectories contain linear signals about the phase of reasoning and the model's proximity to correct or incorrect conclusions.

One approach proposes that correctness manifests as a geometrically separable pattern in hidden-state trajectories that distinguishes success from failure, with trajectories for correct and incorrect solutions consistently clustering apart across tasks and model scales.

These papers collectively demonstrate an emerging research direction connecting trajectory shapes in hidden state space to LLM reasoning reliability and faithfulness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6c02897-2d9e-42d8-a484-08689879b74e",
  "isSidechain": false,
  "promptId": "b15418e1-7e26-425c-8335-7273c8cf23f6",
  "type": "user",
  "uuid": "00979522-1b00-4e3f-bb9a-d84a2e0e77f7",
  "toolUseResult": {
    "query": "\"trajectory shape\" OR \"trajectory profile\" hidden state reasoning LLM faithfulness classification 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018rjsdyGn39w9aFXAiWQWyE",
        "content": [
          {
            "title": "Entropy trajectory shape predicts LLM reasoning reliability: A diagnostic study of uncertainty dynamics in chain-of-thought",
            "url": "https://arxiv.org/pdf/2603.18940"
          },
          {
            "title": "Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing",
            "url": "https://arxiv.org/pdf/2604.08401"
          },
          {
            "title": "Truth as a Trajectory: What Internal Representations Reveal About Large Language Model Reasoning",
            "url": "https://arxiv.org/pdf/2603.01326"
          },
          {
            "title": "Beyond Scalars: Evaluating and Understanding LLM Reasoning via Geometric Progress and Stability",
            "url": "https://arxiv.org/pdf/2603.10384"
          },
          {
            "title": "LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals",
            "url": "https://arxiv.org/pdf/2604.05655"
          },
          {
            "title": "Probing the Trajectories of Reasoning Traces in Large Language Models",
            "url": "https://arxiv.org/html/2601.23163v1"
          },
          {
            "title": "CLUE: Non-parametric Verification from Experience via Hidden-State Clustering",
            "url": "https://arxiv.org/pdf/2510.01591"
          }
        ]
      },
      "I found several highly relevant papers from 2025-2026 on trajectory shapes, hidden states, and LLM reasoning. Here are the key results:\n\n## Key Findings:\n\nA recent study investigates whether the shape of uncertainty dynamics across reasoning steps—captured by sampling answer completions at each step—predicts whether the final answer is correct. The research introduces \"entropy-trajectory monotonicity,\" where a chain is monotone if its per-step answer-distribution entropy decreases at every step, reflecting consistent uncertainty reduction. Monotone chains are significantly more accurate than non-monotone chains.\n\nAnother study plots layerwise hidden states as trajectories in activation space, finding that correct generations follow smoother paths, while incorrect ones exhibit sharp deviations.\n\nResearch examining whether LLM reasoning steps form a structured trajectory through representation space found that steps unfold as structured geometric motion in representation space, and these trajectories contain linear signals about the phase of reasoning and the model's proximity to correct or incorrect conclusions.\n\nOne approach proposes that correctness manifests as a geometrically separable pattern in hidden-state trajectories that distinguishes success from failure, with trajectories for correct and incorrect solutions consistently clustering apart across tasks and model scales.\n\nThese papers collectively demonstrate an emerging research direction connecting trajectory shapes in hidden state space to LLM reasoning reliability and faithfulness."
    ],
    "durationSeconds": 6.990402620999986,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f6c02897-2d9e-42d8-a484-08689879b74e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T04:07:29.713Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012Y1xh8urcDudS82UUm4Yn2`</summary>

```json
{
  "query": "\"knowing but not using\" OR \"knows but doesn't use\" OR \"pre-CoT encoding\" probe steering reasoning model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00979522-1b00-4e3f-bb9a-d84a2e0e77f7",
  "isSidechain": false,
  "requestId": "req_011CbDAMri6mdhGHHAmVwigp",
  "type": "assistant",
  "uuid": "6e7b71a6-c87e-4c24-a954-3697ffa8178c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gk8CwjTLqk22G6J3WG2hbZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 727,
      "cache_read_input_tokens": 39055,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 39055,
          "cache_creation_input_tokens": 727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 727
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

_source line 43 · 2026-05-20T04:07:35.353Z_

<details><summary>↩ Tool result · `toolu_012Y1xh8urcDudS82UUm4Yn2`</summary>

```text
Web search results for query: ""knowing but not using" OR "knows but doesn't use" OR "pre-CoT encoding" probe steering reasoning model 2026"

Links: [{"title":"[2603.01437] Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/abs/2603.01437"},{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/html/2603.01437"},{"title":"Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"},{"title":"Knowing Before Saying: LLM Representations Encode Information About Chain-of-Thought Success Before Completion","url":"https://arxiv.org/html/2505.24362v2"},{"title":"Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification | OpenReview","url":"https://openreview.net/forum?id=O6I0Av7683"},{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/pdf/2603.01437"}]

I found relevant research on this topic. The most directly applicable work is:

"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering," published on arXiv in March 2026, by Kyle Cox and colleagues.

**Key Findings:**

The research shows that on some reasoning tasks, models may "know" the answer prior to CoT and perform reasoning post-hoc, such as responding correctly when CoT is removed or replaced with misleading CoT.

**Method - Pre-CoT Probes:**

The researchers found that probe directions are not only predictive, but also causal: steering activations along the probe direction flips model answers in over 50% of cases, significantly exceeding orthogonal baselines.

**Failure Modes:**

When steering induces incorrect answers, two distinct failure modes are observed: non-entailment (stating correct premises but drawing unsupported conclusions) and confabulation (fabricating false premises).

**Implications:**

While post-hoc reasoning may be instrumentally useful when the model has a correct pre-CoT belief, these failure modes suggest it can result in undesirable behaviors when reasoning from a false belief.

This research demonstrates the phenomenon where models "know" answers before generating chain-of-thought reasoning, which has important implications for understanding model interpretability and the faithfulness of reasoning explanations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e7b71a6-c87e-4c24-a954-3697ffa8178c",
  "isSidechain": false,
  "promptId": "b15418e1-7e26-425c-8335-7273c8cf23f6",
  "type": "user",
  "uuid": "d9456784-f7e0-4357-9713-99a3ed70d372",
  "toolUseResult": {
    "query": "\"knowing but not using\" OR \"knows but doesn't use\" OR \"pre-CoT encoding\" probe steering reasoning model 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XHRkupmMqwRAUFqhQM3bxB",
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
            "title": "Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra",
            "url": "https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"
          },
          {
            "title": "Knowing Before Saying: LLM Representations Encode Information About Chain-of-Thought Success Before Completion",
            "url": "https://arxiv.org/html/2505.24362v2"
          },
          {
            "title": "Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification | OpenReview",
            "url": "https://openreview.net/forum?id=O6I0Av7683"
          },
          {
            "title": "Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering",
            "url": "https://arxiv.org/pdf/2603.01437"
          }
        ]
      },
      "I found relevant research on this topic. The most directly applicable work is:\n\n\"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering,\" published on arXiv in March 2026, by Kyle Cox and colleagues.\n\n**Key Findings:**\n\nThe research shows that on some reasoning tasks, models may \"know\" the answer prior to CoT and perform reasoning post-hoc, such as responding correctly when CoT is removed or replaced with misleading CoT.\n\n**Method - Pre-CoT Probes:**\n\nThe researchers found that probe directions are not only predictive, but also causal: steering activations along the probe direction flips model answers in over 50% of cases, significantly exceeding orthogonal baselines.\n\n**Failure Modes:**\n\nWhen steering induces incorrect answers, two distinct failure modes are observed: non-entailment (stating correct premises but drawing unsupported conclusions) and confabulation (fabricating false premises).\n\n**Implications:**\n\nWhile post-hoc reasoning may be instrumentally useful when the model has a correct pre-CoT belief, these failure modes suggest it can result in undesirable behaviors when reasoning from a false belief.\n\nThis research demonstrates the phenomenon where models \"know\" answers before generating chain-of-thought reasoning, which has important implications for understanding model interpretability and the faithfulness of reasoning explanations."
    ],
    "durationSeconds": 5.635855767000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6e7b71a6-c87e-4c24-a954-3697ffa8178c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-20T04:09:18.102Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the landscape. Let me synthesize my findings and provide my analysis as the "发掘 agent."

Key things I've found from my research:

1. **Chrabąszcz et al. (2605.18549)**: Probe trajectories with 60+ features, but NO causal dimension. This is the closest concurrent work and the proposal correctly identifies the gap.

2. **Yuan et al. (2605.09502)**: Confirms the diagnostic-not-causal finding with 4 failed interventions. This is a solid motivation.


3. **Cox et al. (2603.01437)**: Pre-CoT probes and steering approaches fail on reasoning models, which validates the need for a different approach.
4. **Wang (2604.15726)**: The H1/H2/H0 framework is well-operationalized in the proposal.
5. **Gjølbye et al. (2605.15454)**: Their work on trajectory geometry and difficulty coupling complements this research nicely.
6. **CMI (2602.03994)**: The proposal correctly distinguishes between structural mediation and ICG's functional contribution.
7. **FaithCoT-Bench (ICLR 2026)**: Provides instance-level ground truth for evaluation.
8. **Entropy trajectory shape (2603.18940)**: The entropy patterns validate the trajectory shape analysis.
9. **Microsoft trajectory geometry (2604.05655)**: They extract AUC metrics from shape features, which is relevant here.

Looking at whether there's a simpler approach—comparing probe accuracy at the start versus end plus TTS would seem like it should work, but the proposal makes a solid case that endpoint comparison alone can't distinguish between pre-CoT encoding and post-hoc rationalization. The temporal trajectory shape is what actually differentiates these phenomena. The core assumption that P*(t) and C(t) trajectories will produce distinguishable shapes for different faithfulness scenarios is testable in Phase 0b, and the null-probe calibration seems like a reasonable way to handle inflation concerns, though there's still some uncertainty about whether it fully addresses all the issues.

The real novelty here is combining the dual-stream temporal gap—merging probe trajectories with causal contribution trajectories and analyzing the gap between them. Prior work has tackled pieces of this (probe-only approaches, causal-only approaches, structural mediation, per-step causal analysis) but nobody's put both streams together temporally before. The practical payoff is clear too—this directly addresses inference-time compute tradeoffs, benchmark validity, and safety monitoring in a way the field has been implicitly looking for.

Now I'm thinking about what actually needs sharpening at the conceptual level. The current framing says the gap itself signals faithfulness, but the stronger insight is that the *shape* of the gap's temporal trajectory acts as a fingerprint for different faithfulness failure modes. That's the real contribution—being able to discriminate between failure types based on how G*(t) evolves. The paper buries this under methodological layers when it should be the headline. The title is descriptive but not compelling; the core claim should be front-loaded: different faithfulness breakdowns produce distinct G*(t) signatures, and this is the first framework that can tell them apart.

The shapes-over-magnitudes insight is actually the deepest contribution but gets treated as a technical fix rather than a theoretical principle. Using rank normalization to handle scale differences is smart, but the real discovery is that trajectory shapes carry diagnostic power independent of absolute magnitude—that's a measurement theory insight worth elevating. And there's an underexplored distinction between information that's computationally present versus information the model actually uses for decisions. The proposal acknowledges this honestly but could flip it into a positive contribution: figuring out *when* probe-detected information becomes actionable knowledge is itself a valuable research question, and the MCT concordance check hints at this but could be developed further.

Compared to Chrabąszcz et al., there's a sharper framing available: their work answers what the model knows over time, while ICG answers what knowing costs the model in reasoning—the gap G*(t) is essentially measuring the price of knowledge in unused internal information. But stepping back, the proposal is actually quite mature and addresses most of the natural objections already. The real question is whether the 2-3 phenomenon taxonomy is pitched at the right level of ambition.

The predicted signatures for these phenomena rest on specific assumptions that haven't been empirically validated yet. For post-hoc rationalization specifically, the theory predicts a widening gap with stable P*(t) and flat C(t), but there's a tension here: if the model is genuinely rationalizing, wouldn't the chain-of-thought actually increase C(t) since plausible reasoning could causally influence the answer? That's a potential crack in the signature predictions. Let me think through what post-hoc rationalization actually looks like—the model already has the answer locked in, so P*(t) stays high while the generated reasoning is just window dressing.

But here's where it gets tricky: pre-CoT encoding looks almost identical on the surface, with high P*(t) and low C(t). The proposal's distinction hinges on the temporal shape—pre-CoT encoding should show a constant-high gap while post-hoc rationalization shows widening. Yet this distinction feels fragile because both mechanisms could produce similar patterns depending on how the model's confidence actually evolves over time. the answer but pretends to reason," then P*(t) should also be high from the start (like pre-CoT encoding). The distinction between pre-CoT encoding and post-hoc rationalization via trajectory shapes is not as clean as the proposal suggests.

Actually, I need to be more careful here. The proposal distinguishes between pre-CoT encoding—where G*(t) starts high and stays high because both P* is consistently high and C(t) consistently low—versus post-hoc rationalization, where G*(t) starts moderate but rises during CoT while P*(t) stays stable and C(t) remains flat.

The key insight is that in post-hoc rationalization, the model doesn't start with maximum probe accuracy. Instead, P*(t) rises as the model commits to an answer during reasoning, but C(t) doesn't rise because the CoT isn't actually driving that commitment—it's just justifying it after the fact. This creates a widening gap. The real question is whether probe accuracy can actually distinguish between "the model had the answer beforehand" and "the model committed to an answer mid-reasoning."

This is getting into experimental design territory, which isn't really my focus here. Let me think about what conceptual contributions I can actually make.

The structural versus functional distinction with CMI is genuinely sharp—the idea that a model could have high CMI but high G*(t), meaning the CoT is structurally mediating but not functionally contributing, is novel and testable. If that holds up, it's a significant insight about how reasoning models actually work.

There's also a connection to inference-time compute allocation that could be sharpened. The proposal mentions that G*(t) >> 0 for easy problems means CoT is decorative overhead, which ties into active research on when and how long to think. But instead of just being a diagnostic tool, ICG could be framed as providing the theoretical foundation for adaptive compute allocation—a principled framework for understanding when additional reasoning tokens are actually decorative, which current early-exit methods like ESTAR and DTSR approach only through heuristics.

The probe target distinction—between answer-content probes and correctness probes—deserves elevation as its own contribution. The finding that diagnostic-not-causal may mean different things depending on which probe you're using is itself a novel conceptual insight that the proposal currently treats as secondary.

Now checking whether this has a trivial alternative: using TTS per step gives C(t) but not P*(t), so you can't distinguish different types of faithfulness failure. Chrabąszcz probe trajectories give P*(t) but not C(t), missing the distinction between faithful-correct and unfaithful-correct. Simple endpoint comparisons between pre-CoT and final accuracy don't capture the temporal dynamics at all.  FaithCoT-Bench methods provide instance-level labels but lack temporal resolution and mechanism discrimination. None of these can do what ICG claims—the dual-stream temporal approach is genuinely necessary.

For the premise check: linear probes reliably diagnose answer correctness (0.82-0.95 AUROC), and causal interventions on reasoning models do fail as documented. But the key untested hypothesis is whether different faithfulness phenomena actually produce distinguishable G*(t) shapes—and the proposal is transparent that this needs Phase 0b validation.

Trajectory shapes carrying more diagnostic information than absolute magnitudes is supported by the literature, and null-probe calibration addresses inflation concerns, though with acknowledged limitations. The real risk hinges on Premise 3, but the go/no-go structure is sound.

Now I'm thinking about how to frame my assessment. This feels like a mature proposal with genuine novelty, but there are a few conceptual points that could be sharpened—particularly around leading with the faithful-correct versus unfaithful-correct distinction as the core claim rather than treating it as secondary.

The dual-stream gap is actually the key insight here: existing methods can tell you whether a model gets the right answer and whether it "knows" the answer, but only this approach reveals whether it got the right answer for the right reasons. That's the fundamental faithfulness question and should anchor the entire framing. The CMI structural-versus-functional distinction is also underexplored theoretically—the possibility that high CMI coexists with high G*(t) would genuinely reshape how we understand mechanistic interpretability of reasoning. And the connection between trajectory shapes and deeper theoretical properties deserves more development. I'm realizing that point 3 about introducing a unifying theoretical framework is promising, while point 4 might be stretching too far. Now I need to think through a potential vulnerability: what if someone just combines existing methods like Chrabąszcz's probe trajectories with token-level causal scores? That would technically be a dual-stream approach too, but the key difference is that my proposal uses cumulative causal contribution rather than per-step scores, which better captures how reasoning unfolds over time—though I should make this distinction explicit in the proposal rather than leaving it implicit. ulation (C(t) as "causal contribution of CoT[:t]") is preferred. The answer is: the cumulative formulation directly captures whether the model is "building up" reasoning (convergent) vs. "already done" (flat), which is the key mechanistic distinction.

Hmm, but this is getting into a subtlety that might be more methodological than idea-level. Let me check: is this a novelty concern (someone could trivially combine existing methods) or an experimental design concern? I think it's a novelty concern — if someone could get similar discrimination by combining existing methods in a straightforward way, the novelty is reduced. So it is my domain.

Let me think about whether Chrabąszcz + step-level TTS would achieve the same thing. Chrabąszcz gives you the P(t) trajectory with many features, and TTS gives you per-step causal contribution, so you could compute a gap between probe accuracy and causal contribution at each step to get something similar to G*(t). The key differences would be that TTS is specific to numerical perturbation while my approach uses three complementary methods, TTS measures step-level contribution versus my prefix truncation measuring cumulative contribution, and I include null-probe calibration. But the core insight of comparing what the model knows with what the CoT contributes over time would be captured by this simpler combination, so I need to address this more explicitly in the proposal.

I think I have enough for my analysis now. Let me also consider whether the framing could be stronger — instead of just "making the diagnostic-causal gap the primary object of study," I could emphasize what this actually enables.

The stronger framing would be that this is the first framework that can discriminate between a model that got the right answer through faithful reasoning versus one that got the right answer despite unfaithful reasoning, which connects directly to fundamental AI safety and reliability questions.

Before I write this up, let me do one more search to check if there's recent work similar to ICG that the proposal might be missing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9456784-f7e0-4357-9713-99a3ed70d372",
  "isSidechain": false,
  "requestId": "req_011CbDANV67TMxvGKUy7kd4i",
  "type": "assistant",
  "uuid": "f2af5b33-5ae1-4e5c-ab83-f93ac74c88e1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ShJvrfXAxvtV8YnX5AqKbH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 765,
      "cache_read_input_tokens": 39782,
      "output_tokens": 4296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 765,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4296,
          "cache_read_input_tokens": 39782,
          "cache_creation_input_tokens": 765,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 765
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

_source line 45 · 2026-05-20T04:09:18.104Z_

Let me do one more targeted search to check for any very recent work that might overlap with the dual-stream gap idea.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2af5b33-5ae1-4e5c-ab83-f93ac74c88e1",
  "isSidechain": false,
  "requestId": "req_011CbDANV67TMxvGKUy7kd4i",
  "type": "assistant",
  "uuid": "515b855c-5578-4aa9-92ef-11ae3259c030",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ShJvrfXAxvtV8YnX5AqKbH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 765,
      "cache_read_input_tokens": 39782,
      "output_tokens": 4296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 765,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4296,
          "cache_read_input_tokens": 39782,
          "cache_creation_input_tokens": 765,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 765
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

_source line 46 · 2026-05-20T04:09:18.107Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Hn4x7kxBY2SUupXhHtFkHV`</summary>

```json
{
  "query": "measuring \"what models know\" vs \"what CoT contributes\" faithfulness diagnostic temporal divergence 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "515b855c-5578-4aa9-92ef-11ae3259c030",
  "isSidechain": false,
  "requestId": "req_011CbDANV67TMxvGKUy7kd4i",
  "type": "assistant",
  "uuid": "28aaae0b-d424-44e2-8ec2-20570c9198c4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ShJvrfXAxvtV8YnX5AqKbH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 765,
      "cache_read_input_tokens": 39782,
      "output_tokens": 4296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 765,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4296,
          "cache_read_input_tokens": 39782,
          "cache_creation_input_tokens": 765,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 765
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

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness  ## Description We propose the Information-Contribution Gap (ICG)…",
  "leafUuid": "28aaae0b-d424-44e2-8ec2-20570c9198c4",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Measuring models' knowledge-action gaps in reasoning with temporal probes",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd"
}
```

---

### Tool result

_source line 49 · 2026-05-20T04:09:25.899Z_

<details><summary>↩ Tool result · `toolu_01Hn4x7kxBY2SUupXhHtFkHV`</summary>

```text
Web search results for query: "measuring "what models know" vs "what CoT contributes" faithfulness diagnostic temporal divergence 2026"

Links: [{"title":"Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models","url":"https://arxiv.org/html/2603.26410"},{"title":"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2602.11201v1"},{"title":"(PDF) Why Models Know But Don't Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models","url":"https://www.researchgate.net/publication/403262878_Why_Models_Know_But_Don't_Say_Chain-of-Thought_Faithfulness_Divergence_Between_Thinking_Tokens_and_Answers_in_Open-Weight_Reasoning_Models"},{"title":"Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING","url":"https://arxiv.org/pdf/2510.04040"},{"title":"Chain-of-Thought Unfaithfulness as Disguised Accuracy","url":"https://arxiv.org/pdf/2402.14897"},{"title":"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning","url":"https://arxiv.org/pdf/2602.11201"},{"title":"Measuring Faithfulness Depends on How You Measure: Classifier Sensitivity in LLM Chain-of-Thought Evaluation","url":"https://arxiv.org/pdf/2603.20172"}]

I found several highly relevant recent papers (from 2026) on this topic. Here are the key findings:

## Main Research Works

**1. "Why Models Know But Don't Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models"**

This paper asks whether, when a model follows a misleading hint, its visible answer acknowledges the same influences that its thinking tokens do. The research found that for consistency and unethical hints, models' thinking tokens contain hint-related keywords, but the corresponding answer text omits them. The study demonstrates that classifier choice alone can shift measured faithfulness by up to 30 percentage points.

**2. "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning"**

This work proposes Normalized Logit Difference Decay (NLDD), a metric that measures whether individual reasoning steps are faithful to the model's decision-making process. The research reveals divergent faithfulness regimes: in faithful cases, the final prediction depends on the reasoning chain, while in anti-faithful cases, CoT distracts from pre-computed answers.

**3. "Measuring Faithfulness Depends on How You Measure: Classifier Sensitivity in LLM Chain-of-Thought Evaluation"**

This study argues that faithfulness admits multiple valid formalizations depending on the intended guarantee, and different operationalizations of the same concept yield divergent measurements.

These papers collectively address the diagnostic problem of measuring what models know (internal representations) versus what Chain-of-Thought reasoning contributes to their outputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28aaae0b-d424-44e2-8ec2-20570c9198c4",
  "isSidechain": false,
  "promptId": "b15418e1-7e26-425c-8335-7273c8cf23f6",
  "type": "user",
  "uuid": "0d14ba9a-feeb-4596-aba5-5d18b67e4c9b",
  "toolUseResult": {
    "query": "measuring \"what models know\" vs \"what CoT contributes\" faithfulness diagnostic temporal divergence 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SjHWHdXn2XSktgRqJFRyWx",
        "content": [
          {
            "title": "Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models",
            "url": "https://arxiv.org/html/2603.26410"
          },
          {
            "title": "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2602.11201v1"
          },
          {
            "title": "(PDF) Why Models Know But Don't Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models",
            "url": "https://www.researchgate.net/publication/403262878_Why_Models_Know_But_Don't_Say_Chain-of-Thought_Faithfulness_Divergence_Between_Thinking_Tokens_and_Answers_in_Open-Weight_Reasoning_Models"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING",
            "url": "https://arxiv.org/pdf/2510.04040"
          },
          {
            "title": "Chain-of-Thought Unfaithfulness as Disguised Accuracy",
            "url": "https://arxiv.org/pdf/2402.14897"
          },
          {
            "title": "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/pdf/2602.11201"
          },
          {
            "title": "Measuring Faithfulness Depends on How You Measure: Classifier Sensitivity in LLM Chain-of-Thought Evaluation",
            "url": "https://arxiv.org/pdf/2603.20172"
          }
        ]
      },
      "I found several highly relevant recent papers (from 2026) on this topic. Here are the key findings:\n\n## Main Research Works\n\n**1. \"Why Models Know But Don't Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models\"**\n\nThis paper asks whether, when a model follows a misleading hint, its visible answer acknowledges the same influences that its thinking tokens do. The research found that for consistency and unethical hints, models' thinking tokens contain hint-related keywords, but the corresponding answer text omits them. The study demonstrates that classifier choice alone can shift measured faithfulness by up to 30 percentage points.\n\n**2. \"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning\"**\n\nThis work proposes Normalized Logit Difference Decay (NLDD), a metric that measures whether individual reasoning steps are faithful to the model's decision-making process. The research reveals divergent faithfulness regimes: in faithful cases, the final prediction depends on the reasoning chain, while in anti-faithful cases, CoT distracts from pre-computed answers.\n\n**3. \"Measuring Faithfulness Depends on How You Measure: Classifier Sensitivity in LLM Chain-of-Thought Evaluation\"**\n\nThis study argues that faithfulness admits multiple valid formalizations depending on the intended guarantee, and different operationalizations of the same concept yield divergent measurements.\n\nThese papers collectively address the diagnostic problem of measuring what models know (internal representations) versus what Chain-of-Thought reasoning contributes to their outputs."
    ],
    "durationSeconds": 7.7877099929999964,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "28aaae0b-d424-44e2-8ec2-20570c9198c4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-20T04:09:28.819Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y3QBWTio1Vp62nKCp9ttHq`</summary>

```json
{
  "query": "\"Thought Anchors\" 2506.19143 causal dependency CoT reasoning step ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d14ba9a-feeb-4596-aba5-5d18b67e4c9b",
  "isSidechain": false,
  "requestId": "req_011CbDAWdmUh8fChYBk9zaV9",
  "type": "assistant",
  "uuid": "2028c9c4-18fc-44ba-9d58-22a6f800d5ff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011pnvEeQyDpNBFqwCv5iDk4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5104,
      "cache_read_input_tokens": 40547,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5104,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 40547,
          "cache_creation_input_tokens": 5104,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5104
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

_source line 51 · 2026-05-20T04:09:34.385Z_

<details><summary>↩ Tool result · `toolu_01Y3QBWTio1Vp62nKCp9ttHq`</summary>

```text
Web search results for query: ""Thought Anchors" 2506.19143 causal dependency CoT reasoning step ICLR 2026"

Links: [{"title":"[2506.19143] Thought Anchors: Which LLM Reasoning Steps Matter?","url":"https://arxiv.org/abs/2506.19143"},{"title":"Under review as a conference paper at ICLR 2026 THOUGHT ANCHORS: WHICH LLM","url":"https://arxiv.org/pdf/2506.19143"},{"title":"Unveiling and Causalizing CoT: A Causal Pespective","url":"https://arxiv.org/pdf/2502.18239"},{"title":"Bypassing the Rationale: Causal Auditing of Implicit Reasoning in Language Models","url":"https://arxiv.org/pdf/2602.03994"},{"title":"Causal Sufficiency and Necessity Improves Chain-of-Thought Reasoning","url":"https://arxiv.org/pdf/2506.09853"},{"title":"The Curse of CoT: On the Limitations of Chain-of-Thought in In-Context Learning","url":"https://arxiv.org/pdf/2504.05081"},{"title":"KisMATH: Do LLMs Have Knowledge of Implicit Structures in Mathematical Reasoning?","url":"https://arxiv.org/pdf/2507.11408"},{"title":"Graph-of-Causal Evolution: Challenging Chain-of-Model for Reasoning","url":"https://arxiv.org/pdf/2506.07501"}]

Based on the search results, here's what I found about "Thought Anchors":

The paper introduces "thought anchors" - sentences that are generally planning or uncertainty management sentences, with specialized attention heads consistently attending from subsequent sentences to thought anchors.

The method measures each sentence's counterfactual importance by repeatedly sampling replacement sentences from the model, filtering for semantically different ones, and continuing the chain of thought from that point onwards to quantify the sentence's impact on the distribution of final answers.

The research discovers that certain sentences can have an outsized impact on the trajectory of the reasoning trace and final answer.

Examining sentence-sentence causal links within a reasoning trace gives insight into a model's behavior.

The paper (arXiv:2506.19143) is under review as a conference paper at ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2028c9c4-18fc-44ba-9d58-22a6f800d5ff",
  "isSidechain": false,
  "promptId": "b15418e1-7e26-425c-8335-7273c8cf23f6",
  "type": "user",
  "uuid": "b9cd66dd-fe88-4765-9c13-8a0f3a84a920",
  "toolUseResult": {
    "query": "\"Thought Anchors\" 2506.19143 causal dependency CoT reasoning step ICLR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CNzrDKEwHXDZ9Jg4wjBUBy",
        "content": [
          {
            "title": "[2506.19143] Thought Anchors: Which LLM Reasoning Steps Matter?",
            "url": "https://arxiv.org/abs/2506.19143"
          },
          {
            "title": "Under review as a conference paper at ICLR 2026 THOUGHT ANCHORS: WHICH LLM",
            "url": "https://arxiv.org/pdf/2506.19143"
          },
          {
            "title": "Unveiling and Causalizing CoT: A Causal Pespective",
            "url": "https://arxiv.org/pdf/2502.18239"
          },
          {
            "title": "Bypassing the Rationale: Causal Auditing of Implicit Reasoning in Language Models",
            "url": "https://arxiv.org/pdf/2602.03994"
          },
          {
            "title": "Causal Sufficiency and Necessity Improves Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/pdf/2506.09853"
          },
          {
            "title": "The Curse of CoT: On the Limitations of Chain-of-Thought in In-Context Learning",
            "url": "https://arxiv.org/pdf/2504.05081"
          },
          {
            "title": "KisMATH: Do LLMs Have Knowledge of Implicit Structures in Mathematical Reasoning?",
            "url": "https://arxiv.org/pdf/2507.11408"
          },
          {
            "title": "Graph-of-Causal Evolution: Challenging Chain-of-Model for Reasoning",
            "url": "https://arxiv.org/pdf/2506.07501"
          }
        ]
      },
      "Based on the search results, here's what I found about \"Thought Anchors\":\n\nThe paper introduces \"thought anchors\" - sentences that are generally planning or uncertainty management sentences, with specialized attention heads consistently attending from subsequent sentences to thought anchors.\n\nThe method measures each sentence's counterfactual importance by repeatedly sampling replacement sentences from the model, filtering for semantically different ones, and continuing the chain of thought from that point onwards to quantify the sentence's impact on the distribution of final answers.\n\nThe research discovers that certain sentences can have an outsized impact on the trajectory of the reasoning trace and final answer.\n\nExamining sentence-sentence causal links within a reasoning trace gives insight into a model's behavior.\n\nThe paper (arXiv:2506.19143) is under review as a conference paper at ICLR 2026."
    ],
    "durationSeconds": 5.562401474999992,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2028c9c4-18fc-44ba-9d58-22a6f800d5ff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-20T04:09:50.343Z_

<details><summary>Logged reasoning block</summary>

```text
OK, this "Thought Anchors" paper (2506.19143) is actually quite relevant and the proposal doesn't cite it. It measures per-sentence causal importance via counterfactual replacement, which is essentially a more sophisticated version of the paraphrase perturbation component of C(t). The proposal should be aware of this work.

Let me also think about whether the "PRISM" paper I saw earlier is relevant.

Now let me synthesize everything and write my analysis.

Key findings from my research:

1. **No existing work combines both probe trajectories and causal contribution trajectories in a dual-stream framework** — the core novelty claim holds.


2. Chrabąszcz et al. comes closest but only implements the probe stream, while "Thought Anchors" measures per-sentence causal importance in chain-of-thought reasoning—overlapping with the C(t) component but not the full dual-stream approach.
3. The trajectory-shape literature around entropy and geometric analysis supports prioritizing shape patterns over raw magnitudes, and the distinction between structural CMI and functional ICG contributions is well-motivated.
4. The "faithful-correct vs. unfaithful-correct" distinction seems like the most compelling angle for the analysis.
5. I should address whether step-level causal scores from existing methods could approximate the cumulative C(t) formulation, and clarify why the full dual-stream approach is necessary rather than a trivial combination of existing techniques.
6. The "computation utilization efficiency" framing could tie the three applications together more cohesively, and I need stronger theoretical grounding for why P*(t) signatures would differ between post-hoc rationalization and pre-CoT encoding scenarios.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9cd66dd-fe88-4765-9c13-8a0f3a84a920",
  "isSidechain": false,
  "requestId": "req_011CbDAXG14YqsGbdQge3nEJ",
  "type": "assistant",
  "uuid": "9bcadbf1-3bc9-40a1-9285-0cf991a27df1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011G9C24wA9rnSdcQAHxEigw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 674,
      "cache_read_input_tokens": 45651,
      "output_tokens": 4639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 674,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4639,
          "cache_read_input_tokens": 45651,
          "cache_creation_input_tokens": 674,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 674
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

_source line 53 · 2026-05-20T04:11:26.589Z_

Now I have sufficient background to provide my analysis. Let me compile my findings.

---

【状态】: 有发掘空间

【前置调研发现】
- **Chrabąszcz et al. (2605.18549)**: Probe trajectories with 60+ signal-processing features, up to 17pp over static probes; max-pooling critical (91-97% AUROC for harmfulness). Confirmed: NO causal dimension, NO gap metric, NO calibration, NO faithfulness-mode discrimination. The proposal's characterization is accurate.
- **Yuan et al. (2605.09502)**: Four interventions all fail; 0.95 AUROC from probes, 0.787 from first step alone; "diagnostic not causal" is firmly established across 1.5B-72B, three model families. The motivating phenomenon is robust.
- **Cox et al. (2603.01437)**: Probe-direction steering flips answers on instruction-tuned models (>50%) but fails on reasoning models. Confirms pre-CoT encoding and the diagnostic-causal split specifically for answer-content probes.
- **Wang (2604.15726)**: H1 (latent-mediated), H2 (CoT-mediated), H0 (serial compute) framework. Proposes compute-audited experimental designs but no empirical implementation. ICG operationalizes this directly.
- **CMI / Sathyanarayanan et al. (2602.03994)**: Layerwise activation patching; bypass regimes where CMI ≈ 0 despite plausible CoT; structural mediation is depth-localized into narrow "reasoning windows." Confirmed: structural question, not functional.
- **Gjølbye et al. (2605.15454)**: After length correction, difficulty-geometry coupling is domain-specific (ρ⊥ = +0.41 on code, +0.05 on MATH). Important: prompt-stage probes do NOT mirror these geometric effects — dynamics manifest during generation.
- **"Thought Anchors" (arXiv 2506.19143, under review ICLR 2026)**: Measures per-sentence counterfactual importance in CoT via replacement sampling; identifies "thought anchor" sentences with outsized causal influence on reasoning trajectory and final answer. **NOT cited in proposal** — overlaps with the paraphrase perturbation component of C(t).
- **Young (2603.26410)**: Thinking tokens contain hint-related keywords that answer text omits; classifier choice shifts measured faithfulness by up to 30pp. Reinforces the need for multi-method C(t) estimation.
- **Entropy trajectory monotonicity (2603.18940)**: Monotone entropy decrease → more accurate; shape predicts reliability regardless of absolute levels. Directly validates shapes-over-magnitudes.
- **Microsoft trajectory geometry (2604.05655)**: Step-level representation geometry, correct/incorrect trajectories cluster apart; 0.852 AUC from shape features. Validates geometric trajectory approach.
- **调研总结**: The field has converged on two independent measurement streams — probe-based internal state monitoring and behavioral causal testing — but they remain completely siloed. Every group either tracks what the model "knows" (probes) OR what the CoT "does" (interventions), never both temporally. The dual-stream temporal gap is a genuine vacuum. The closest threat to novelty comes not from any single paper but from a trivial combination of Chrabąszcz's probe trajectories with TTS step-level causal scores — the proposal must preempt this.

---

【发掘点 1】
- 维度: 核心 claim 强化
- 内容: **The "faithful-correct vs. unfaithful-correct" discrimination should be the LEAD framing of the paper, not a differentiator from Chrabąszcz.** Currently, the proposal opens with "the diagnostic-causal gap IS the faithfulness signal" — which is true but abstract. The killer concrete claim is: *this is the first framework that can distinguish a model that got the right answer for the right reasons from a model that got the right answer despite unfaithful reasoning.* This is the question alignment researchers, benchmark designers, and practitioners all urgently need answered. Probe-only methods (Chrabąszcz) can tell you what the model knows; causal-only methods (TTS, NLDD, Ballon) can tell you what the CoT does; but ONLY the dual-stream gap tells you whether the CoT is the *reason* the model succeeds. Reframing the paper around this concrete question — rather than the more abstract "gap as phenomenon" — immediately elevates both novelty and significance claims because it connects directly to a problem the field recognizes but has no tool for.
- 价值: Sharpens significance (the "so what?" becomes immediately obvious to reviewers) and novelty (the claim becomes structurally unthreatened by any single-stream method). Moves the paper from "we measure an interesting quantity" to "we solve a problem no one else can solve."
- 调研依据: Based on confirmed gap between Chrabąszcz et al. (probe-only, structurally cannot make this distinction) and the field's lack of any existing faithful-vs-unfaithful discrimination tool for correct instances.

【发掘点 2】
- 维度: trivial alternative 威胁
- 内容: **The proposal needs to preemptively address the "Chrabąszcz + TTS" trivial combination.** A reviewer could reasonably ask: "Why not just take Chrabąszcz's probe trajectory features and Zhao et al.'s per-step TTS values, compute a per-step 'gap,' and call it done?" This combination would give you both streams at step granularity without the ICG framework's overhead (null-probe calibration, three C(t) estimators, rank normalization). The proposal must explain why its CUMULATIVE formulation of C(t) — "causal contribution of CoT[:t]" — captures information that step-level TTS cannot. The key argument: TTS measures whether removing step *s* changes the answer (marginal contribution), while prefix-truncation C(t) measures whether the CoT *up to position t* is sufficient (cumulative sufficiency). These answer different questions. A chain where every individual step has low TTS (each is individually replaceable) could still have high cumulative C(t) (the chain as a whole is necessary — no single step is critical but the ensemble matters). This cumulative-vs-marginal distinction is the theoretical reason ICG needs its own formulation rather than being a trivial combination. Making this explicit strengthens the novelty claim considerably.
- 价值: Preempts the most dangerous reviewer objection — "incremental combination of existing methods" — by articulating a theoretical distinction (cumulative sufficiency vs. marginal contribution) that makes ICG non-reducible to existing components. Hits the novelty dimension directly.
- 调研依据: Chrabąszcz et al. (2605.18549) for probe trajectories + Zhao et al.'s TTS (2510.24941) for step-level causal scores. The cumulative-vs-marginal distinction is inspired by the difference between Ballon et al.'s (2601.23163) monotonic prefix-truncation curves (cumulative) and TTS's per-step ATE (marginal).

【发掘点 3】
- 维度: related work 差异化
- 内容: **"Thought Anchors" (arXiv 2506.19143, under review ICLR 2026) is a missing related work that partially overlaps with C(t) and should be cited and differentiated.** Thought Anchors measures per-sentence counterfactual importance in CoT via replacement sampling — identifying "anchor" sentences with outsized causal influence on the reasoning trajectory. This directly overlaps with the paraphrase perturbation component of C(t). The differentiation: Thought Anchors provides a *within-CoT structural analysis* (which sentences matter to each other) but no *external reference* (no probe-side measurement of what the model already knows). A thought anchor could be causally critical within the CoT but entirely redundant relative to the model's internal state — a distinction only ICG can make. Citing and differentiating this work preempts a reviewer who knows the paper from raising an uncited-overlap concern.
- 价值: Strengthens related work completeness and preempts a reviewer attack on novelty via an uncited overlapping method. Hits the related work 差异化 dimension.
- 调研依据: "Thought Anchors" (2506.19143), discovered in web search — measures per-sentence counterfactual importance via replacement sampling, with causal dependency analysis within CoT.

【发掘点 4】
- 维度: 前提假设质疑
- 内容: **The predicted G*(t) signature for post-hoc rationalization vs. pre-CoT encoding needs stronger theoretical grounding — the current distinction is fragile.** The proposal predicts pre-CoT encoding shows "constant-high" G*(t) (P* high from start, C(t) low throughout) while post-hoc rationalization shows "widening" G*(t) (P* starts "moderate," C(t) stays flat). But the theoretical basis for P*(t) starting "moderate" in post-hoc rationalization is unclear. If the model is rationalizing post-hoc, it has already committed to an answer — so P*(t) should ALSO be high from the start, making it indistinguishable from pre-CoT encoding in the probe dimension. The real distinction may need to come from the C(t) dimension instead: in pre-CoT encoding, C(t) is flat-low (CoT doesn't matter at any point); in post-hoc rationalization, C(t) might show spurious increases (the rationalization is crafted to be plausible and might happen to be locally consistent, leading to partial causal contribution detected by paraphrase perturbation). This is a non-trivial theoretical question that Phase 0b should specifically test. If pre-CoT encoding and post-hoc rationalization turn out to be empirically inseparable via G*(t) shapes, the phenomenon taxonomy should honestly collapse to 2 categories (pre-committed vs. genuinely reasoning), which is still a strong result but requires adjusting the claims now. Acknowledging this possibility upfront is more credible than asserting 3-category separation.
- 价值: Identifies a soft spot in the theoretical predictions that a careful reviewer would probe. Addressing it proactively (either by strengthening the theoretical argument or by honestly pre-registering the possibility of collapse) significantly improves credibility. Hits the novelty dimension (the claimed 3-phenomenon discrimination may actually be 2-phenomenon, which changes the contribution framing).
- 调研依据: Based on Cox et al. (2603.01437) showing pre-CoT probes already at >0.9 AUC (suggesting high P* from the start regardless of faithfulness mode) and the general logic of post-hoc rationalization as articulated in the proposal's own phenomenon definitions.

【发掘点 5】
- 维度: significance 提升
- 内容: **Unify the three practical applications under a single conceptual frame: "reasoning utilization efficiency."** The proposal lists three practical applications (inference-time compute allocation, benchmark validity, safety monitoring) as separate points. These are all instances of a single deeper question: *how efficiently does the model convert its internal knowledge into externally-verifiable reasoning?* G*(t) ≈ 0 means full utilization (knowledge is channeled through CoT); G*(t) >> 0 means waste (knowledge exists but CoT doesn't use it); G*(t) < 0 means productive computation (CoT assembles information the model didn't start with). Framing G*(t) as a "reasoning utilization" metric — analogous to GPU utilization in computing — makes the practical significance story more cohesive and memorable. It also opens a connection to the emerging "adaptive compute" literature (when to think, how long to think): ICG provides the PRINCIPLED DIAGNOSTIC that tells you when additional compute is being utilized vs. wasted, replacing the heuristics that current early-exit methods rely on (ESTAR, DTSR, CoDE-Stop, FRIT). This positioning — ICG as the theoretical foundation for adaptive reasoning compute — is a more impactful significance claim than three disconnected applications.
- 价值: Elevates significance from "three use cases" to "foundational diagnostic for an entire emerging research direction (adaptive reasoning compute)." Makes the paper relevant to a broader audience (not just faithfulness researchers but also efficiency/deployment researchers). Hits the significance dimension.
- 调研依据: Based on the landscape of early-exit and adaptive compute methods cited in the proposal (ESTAR, DTSR, FRIT, CoDE-Stop) and the growing inference-time compute allocation literature (e.g., Vilas et al. 2510.10494 achieving 14-70% token savings via latent trajectory signals). ICG would provide the principled framework these methods currently lack.

【发掘点 6】
- 维度: novelty 锐化
- 内容: **The structural (CMI) vs. functional (ICG) distinction deserves elevation to a testable prediction, not just a positioning statement.** The proposal claims that "a model could have high CMI but high G*(t)" — meaning CoT representations are structurally mediating (passing through CoT-aligned layers) but the CoT text isn't functionally contributing to correctness. This is currently framed as a theoretical possibility for related-work differentiation. But it is actually a NOVEL EMPIRICAL PREDICTION that, if confirmed, would be a genuinely surprising finding. It would mean that the computational path goes "through" the CoT but the CoT acts as a timing scaffold or routing mechanism rather than contributing semantic content. This prediction connects to the open question of whether RL-trained reasoning models use CoT as a genuine reasoning medium or as a structured computation timer. If ICG can empirically demonstrate cases where CMI is high but G*(t) >> 0 — even on a small number of examples — this would be one of the paper's most cited findings. Elevate this from "theoretical differentiation" to "testable prediction + empirical test" (even as a small supplementary experiment on a few examples from CMI's own datasets).
- 价值: Transforms a related-work positioning statement into a novel empirical contribution. If confirmed, the "high CMI + high G*(t)" finding would be surprising (审稿人 would NOT have guessed this) and would open a new research direction on the distinction between structural and functional mediation in reasoning. Hits the novelty dimension with high expected impact.
- 调研依据: CMI framework (Sathyanarayanan et al., 2602.03994) — confirmed that CMI measures structural mediation via layerwise activation patching. The structural-vs-functional divergence prediction is a direct consequence of the ICG framework's design but is not tested by any existing work.

Sources:
- [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics (Chrabąszcz et al.)](https://arxiv.org/abs/2605.18549)
- [Hidden Error Awareness in Chain-of-Thought Reasoning (Yuan et al.)](https://arxiv.org/abs/2605.09502)
- [Decoding Answers Before Chain-of-Thought (Cox et al.)](https://arxiv.org/abs/2603.01437)
- [LLM Reasoning Is Latent, Not the Chain of Thought (Wang)](https://arxiv.org/abs/2604.15726)
- [When Chains of Thought Don't Matter: Causal Bypass / CMI (Sathyanarayanan et al.)](https://arxiv.org/abs/2602.03994)
- [Reasoning Models Don't Just Think Longer, They Move Differently (Gjølbye et al.)](https://arxiv.org/abs/2605.15454)
- [Thought Anchors: Which LLM Reasoning Steps Matter?](https://arxiv.org/abs/2506.19143)
- [Why Models Know But Don't Say (Young)](https://arxiv.org/html/2603.26410)
- [Entropy trajectory shape predicts LLM reasoning reliability](https://arxiv.org/pdf/2603.18940)
- [LLM Reasoning as Trajectories (Microsoft)](https://arxiv.org/pdf/2604.05655)
- [FaithCoT-Bench (ICLR 2026)](https://arxiv.org/abs/2510.04040)
- [Can Aha Moments Be Fake? True Thinking Score (Zhao et al.)](https://arxiv.org/pdf/2510.24941)
- [Mechanistic Evidence for Faithfulness Decay / NLDD (Ye et al.)](https://arxiv.org/html/2602.11201)
- [Measuring Faithfulness Depends on How You Measure (Young)](https://arxiv.org/pdf/2603.20172)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bcadbf1-3bc9-40a1-9285-0cf991a27df1",
  "isSidechain": false,
  "requestId": "req_011CbDAXG14YqsGbdQge3nEJ",
  "type": "assistant",
  "uuid": "e95c9740-a43c-43dd-8157-046ee626cc26",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011G9C24wA9rnSdcQAHxEigw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 674,
      "cache_read_input_tokens": 45651,
      "output_tokens": 4639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 674,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4639,
          "cache_read_input_tokens": 45651,
          "cache_creation_input_tokens": 674,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 674
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

_source line 54_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness  ## Description We propose the Information-Contribution Gap (ICG)…",
  "leafUuid": "e95c9740-a43c-43dd-8157-046ee626cc26",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Measuring models' knowledge-action gaps in reasoning with temporal probes",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness  ## Description We propose the Information-Contribution Gap (ICG)…",
  "leafUuid": "e95c9740-a43c-43dd-8157-046ee626cc26",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "ai-title",
  "aiTitle": "Measuring models' knowledge-action gaps in reasoning with temporal probes",
  "sessionId": "e23dd0d5-f3b9-4a43-8fe0-00654e6600fd"
}
```

---
