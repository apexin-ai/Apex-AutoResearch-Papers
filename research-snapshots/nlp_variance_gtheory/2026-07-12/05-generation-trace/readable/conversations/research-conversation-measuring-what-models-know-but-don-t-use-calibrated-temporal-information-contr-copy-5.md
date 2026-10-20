# Research conversation: Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought F

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-3/bf74d8b1-2e3a-4d06-8889-9a66e097ba2b.jsonl`
- **Structured JSON:** [`8c7b96a5377601ffcb06.json`](../../sessions/8c/8c7b96a5377601ffcb06.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T03:48:14.899Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T03:48:14.899Z",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "content": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness\n\n## Description\nWe propose the Information-Contribution Gap (ICG) framework, a calibrated temporal diagnostic for chain-of-thought faithfulness that exploits a robust empirical finding: linear probes on hidden states reliably diagnose answer correctness (0.82-0.95 AUROC across four independent groups) yet causal interventions based on these probes consistently fail on reasoning-trained models (Cox et al.: negligible flip rates; Yuan et al.: all four intervention strategies fail). Rather than treating this diagnostic-causal gap as an obstacle, we make it the primary object of study — the gap between what models internally know and what their CoT causally contributes IS the faithfulness signal.\n\nThe framework tracks two calibrated time-varying quantities across the full CoT trajectory: P*(t), null-probe-calibrated correctness awareness (explicitly targeting right/wrong prediction — justified over answer-content probes by broader applicability beyond binary tasks, grounding in the diagnostic-not-causal finding which is about correctness, and more direct faithfulness interpretation — with supplementary answer-content analysis on binary/MC subsets), and C(t), causal contribution estimated via three complementary methods (prefix truncation with Ballon et al.'s three control conditions validating sequential content matters, paraphrase perturbation, NLDD). Their divergence G*(t) = P*(t) − C(t) produces phenomenon-specific temporal fingerprints, operationalizing Wang's (2604.15726) H1/H2 distinction: G*(t) >> 0 is latent-mediated (H1-consistent), G*(t) ≈ 0 is CoT-mediated (H2-consistent).\n\nPositioned against the closest concurrent work — Chrabąszcz et al.'s (2605.18549) probe trajectories with 60+ signal-processing features achieving up to 17pp improvement over static probes across 4 reasoning models — our framework adds the entire causal contribution dimension, the calibrated gap metric, null-probe calibration with MCT geometric validation, phenomenon taxonomy, and task-difficulty conditioning. Their probe-trajectory methodology validates our P*(t) direction; we extend it to the dual-estimator gap that no existing framework provides.\n\nWe adopt honest scoping: 2-3 faithfulness phenomena (pre-CoT encoding, genuine reasoning, post-hoc rationalization) as the realistic classification target, with steganographic encoding and reasoning theater as stretch goals. A new empirical pilot phase (Phase 0b) constructs real G*(t) curves from the SAME model and dataset and tests whether at least 2 phenomena produce distinguishable trajectories (effect size d > 0.5) before committing to the full classification pipeline — addressing the concern that semi-synthetic simulation from cross-study measurements overestimates real-data accuracy. The semi-synthetic simulation is retained as hypothesis generation producing testable predictions, not as evidence.\n\nTask-difficulty conditioning — grounded in David's easy (0.84) vs. hard (0.76) probe splits, the ICLR 2026 Workshop finding, and Gjølbye et al.'s (2605.15454) demonstration that difficulty-geometry coupling is systematic (ρ⊥ = +0.41 on Codeforces) but domain-specific (weaker on MATH) — reveals the decorative→load-bearing transition with practical guidance on when chain-of-thought adds genuine value, applying length correction (residualizing on log(N)) to avoid generation-length confounds.\n\nThe paper focuses on four core contributions: (a) calibrated ICG diagnostic with explicitly justified correctness-probe target on 4 models × 4 benchmarks, positioned against Chrabąszcz et al. to demonstrate the value of the causal contribution dimension; (b) empirical pilot validating that 2-3 phenomena produce distinguishable G*(t) signatures on real data; (c) difficulty-conditioned gap analysis with domain-specific nuance; (d) probe-target analysis contrasting correctness vs. answer-content gaps. Total compute: ~830 H100-hours, with NLDD on 32B models (~250 hrs) as the primary bottleneck.\n\n## Core Problem\nA striking convergence of 2025-2026 findings reveals a fundamental disconnect in reasoning language models: their hidden states reliably encode information about answer correctness — with linear probes achieving 0.82-0.95 AUROC across multiple independent groups — yet causal interventions based on these probes consistently fail to influence model outputs. Cox et al. (2603.01437) find that steering via answer-content probes produces answer flip rates 'negligible against the orthogonal baseline' on reasoning models, despite >0.9 AUC on instruction-tuned models. Yuan et al. (2605.09502) systematically test four distinct intervention strategies (activation steering, probe-guided best-of-N, self-correction, activation patching) on models up to 72B parameters and report that ALL fail: 'RL training does not close the diagnostic–causal gap.' This diagnostic-causal gap — the divergence between what information is available in a model's hidden states and what information the chain-of-thought reasoning text causally contributes — is NOT a methodological obstacle to overcome; it IS the central phenomenon. Critically, the literature conflates two distinct probe targets: answer-content probes (Cox et al.: predicting the specific answer on binary tasks, models ≤9B + GPT-OSS-20B) and correctness probes (Yuan et al.: predicting right/wrong on models up to 72B; Zhang et al.: per-chunk correctness on 7B-70B). This distinction matters because the gap's interpretation differs: answer-content gaps mean 'the model has already decided but CoT doesn't derive the answer,' while correctness gaps mean 'the model knows it's right/wrong but CoT doesn't reflect this awareness.' Meanwhile, the temporal dynamics of this gap are now empirically grounded: David (2511.14773) shows probe accuracy stabilizes at 0.84 AUC by token 4, remaining ~0.8 through token 100, with task-difficulty conditioning revealing easy (0.84) vs. hard (0.76) signatures. Zhang et al. (2504.05419) report chunk-level probe trajectories rising from 65% at 10% of reasoning to 79% at 100% on R1-Distill. Esakkiraja et al. (2604.01202) find >90% pre-generation AUROC with a characteristic dip at 5-10% of reasoning followed by recovery. Chrabąszcz et al. (2605.18549) demonstrate that temporal probe trajectories with 60+ signal-processing features achieve up to 17pp improvement over static probes, showing that trajectory dynamics capture information invisible to single-timepoint measurements. These temporal profiles suggest that different modes of CoT unfaithfulness — pre-CoT encoding, post-hoc rationalization, reasoning theater, myopic planning, thinking-answer gap — produce distinguishable temporal divergence signatures. Yet no existing framework jointly tracks information availability AND causal contribution across the full CoT timeline: Chrabąszcz et al. provide the closest probe-trajectory methodology but lack any causal contribution component, gap metric, probe calibration, or phenomenon taxonomy; Ballon et al. (2601.23163) provide behavioral causal curves via truncation-reinjection but lack hidden-state measurement; the CMI framework provides layerwise causal audit on ~50 examples but no temporal resolution; Zhao et al.'s True Thinking Score provides per-step causal contribution but no probe-side measurement. The gap between diagnostic information availability and causal contribution IS the phenomenon of interest, not an obstacle.\n\n## Opportunity\nThe field has independently produced the measurement tools needed for a unified temporal framework, but these tools remain siloed. The opportunity is fourfold:\n\n(1) **Temporal gap measurement.** Despite rapid accumulation of probe measurements (David: 0.84 at t=4; Zhang: 0.82-0.91 on chunks; Yuan: 0.95 overall, 0.787 first-step; Esakkiraja: >90% pre-generation; Chrabąszcz et al.: 91-97% AUROC with max-pooling on trajectories), no work tracks the full-timeline divergence between probe-estimated information availability and intervention-estimated causal contribution. Chrabąszcz et al. (2605.18549) come closest on the probe side — extracting 60+ signal-processing features from probe trajectories across 4 reasoning models and 4 datasets, achieving up to 17pp improvement over static probes on GSM8K — but they target outcome prediction (correctness, harmfulness) rather than the faithfulness gap, and provide no causal contribution measurement. Their work validates that temporal probe trajectories capture dynamics invisible to static probes (confirming our P*(t) direction); our framework extends this via the dual-estimator gap G*(t) = P*(t) − C(t) that requires the additional causal contribution dimension, null-probe calibration, and phenomenon mapping. On the causal side, Ballon et al. (2601.23163) provide behavioral C(t) curves via truncation-reinjection at decile intervals on Qwen3/gpt-oss across GPQA-Diamond and MMLU-Pro — showing monotonic accuracy increase from 30.8-42.3% to 49.0-73.1% with control conditions validating that sequential content (not just context length) matters — but lack hidden-state measurement. The gap between these two measurement traditions IS the framework's niche.\n\n(2) **Phenomenon unification with honest scoping.** The CoT faithfulness literature treats each failure mode as separate: Reasoning Horizon (Ye et al. 2602.11201), pre-CoT encoding (Cox et al. 2603.01437; Esakkiraja et al. 2604.01202), Reasoning Theater (Boppana et al. 2603.05488), myopic planning (Xu et al. 2602.02103), thinking-answer gap. We propose that 2-3 of these are confidently distinguishable via trajectory-shape signatures in the information-contribution gap G*(t), with 4-5 as a stretch goal requiring additional features. The honest scoping — validated through an empirical pilot on real data before committing to full classification — is itself a contribution to a field prone to over-claiming.\n\n(3) **Task-difficulty conditioning.** The ICLR 2026 Workshop finding and Li et al.'s (2510.22362) corroboration show easy→decorative, hard→faithful. David's easy/hard splits (0.84 vs. 0.76 at t=32) provide probe-level evidence. Gjølbye et al. (2605.15454) demonstrate that difficulty is systematically coupled to hidden-state trajectory geometry even after length correction (ρ⊥ = +0.41 for reasoning models vs. −0.06 for baselines on competitive programming), with domain-specific strength. A difficulty-conditioned gap framework can answer the practical question: at what difficulty level does CoT transition from decorative to load-bearing?\n\n(4) **Probe target clarification.** The field has not confronted the distinction between answer-content probes (Cox et al.: binary tasks, ≤9B) and correctness probes (Yuan et al.: up to 72B). A framework that explicitly measures correctness awareness gap — and contrasts it with answer-content gap on applicable tasks — provides the first principled treatment of what 'knowing but not using' means.\n\nTwo prior works have combined probing with causal interventions: Kudo et al. (EACL 2026) on synthetic arithmetic, and the CMI framework (2602.03994) on ~50 examples. Wang (2604.15726) formalizes the need via competing hypotheses (H1: latent-mediated, H2: CoT-mediated, H0: serial compute) and proposes compute-audited designs — our ICG framework provides an empirical methodology to distinguish H1 from H2 at each token position. Neither Kudo et al. nor CMI provides: (a) full temporal-position coverage on natural benchmarks, (b) mapping to named faithfulness phenomena, (c) a standalone instance-level diagnostic, (d) systematic multi-model comparison, (e) robustness validation — a critical gap highlighted by Young's (2603.20172) finding that faithfulness measurements are classifier-sensitive (inter-classifier kappa as low as 0.06), or (f) an empirical pilot validating phenomenon separability on real data.\n\n## Landscape\n**Probe-based temporal measurement (foundational for our P*(t) component).** Chrabąszcz et al. (2605.18549) is the closest concurrent work: they introduce probe trajectories — tracking concept probability at each generated token — and extract 60+ signal-processing features (volatility, trend, steady-state, temporal segmentation, boundary transients, autocorrelation) via 3-layer MLP probes with Multi-Instance Learning meta-probe across layers. Key results: max-pooling achieves 91-97% AUROC on harmfulness detection (vs. 33-61% for average-pooling, demonstrating average/last-token pooling collapses to near-random); up to 17pp improvement over static probes on GSM8K mathematical error prediction across Llama-8B-R1-Distill and Qwen3-4B/8B/14B (~3000 GPU-hours total). Critical differentiators from our framework: (a) NO causal contribution component — they measure only probe accuracy trajectories, not whether CoT causally contributes; (b) NO gap metric — just trajectory vs. static comparison for outcome prediction; (c) NO null-probe calibration or MCT geometric validation — their 3-layer MLP probes are uncalibrated; (d) NO phenomenon taxonomy — they separate correct/incorrect or safe/harmful, not faithfulness modes; (e) NO task-difficulty conditioning. Their 60+ feature extraction methodology is complementary and could enhance our trajectory-shape classification. David (2511.14773) trains per-position probes on reasoning models, finding 0.84 AUC at t=4, stable ~0.8 through t≈100, with easy/hard splits of 0.84 vs. 0.76 at t=32 on Qwen3-8B. Zhang et al. (2504.05419) probe R1-Distill models (7B/32B/70B) for correctness at each reasoning chunk, achieving 0.82-0.91 AUROC on GSM8K/MATH/AIME, with a rising trajectory from 65% at 10% chunk to 79% at 100%, enabling 24% token reduction via early-exit. Yuan et al. (2605.09502) report 0.95 AUROC on Qwen-3B, 0.852 on DeepSeek-R1-7B, 0.787 from first-step hidden states alone, and a concealment gap of 0.197 AUROC between hidden-state (0.787) and text-surface (0.590) classifiers — using correctness probes (right/wrong), not answer-content probes. Esakkiraja et al. (2604.01202) find >90% AUROC pre-generation on Qwen3-4B and GLM-Z1-9B, with a characteristic dip at 5-10% of reasoning and recovery to near-100% by think_end. Cox et al. (2603.01437) use answer-content probes (predicting specific answer A/B on binary tasks: Anachronisms, Logical Deduction, Sports Understanding, Social Chemistry) achieving >0.9 AUC on instruction-tuned Gemma-2 (2B, 9B) and Qwen-2.5 (1.5B, 3B, 7B) models, with causal validation via steering (>50% flip rates) — but 'the answer flip rate is negligible against the orthogonal baseline' on the reasoning model GPT-OSS-20B. Additional probing work: Qian et al. (2506.02867, NeurIPS 2025); Lewis-Lim et al. (2508.19827, EMNLP 2025); Mirtaheri & Belkin (2603.17199); Occhipinti et al. (ICLR 2026 LIT Workshop, probing F1 90-100%, steering 46% recovery).\n\n**The diagnostic-not-causal evidence (motivating our framework).** Yuan et al. (2605.09502) is the decisive study: four interventions — activation steering (at most +4%), probe-guided best-of-N (matches random), self-correction (hurts accuracy −3%), activation patching (destroys coherence at α=0.5) — all fail. Tested on Qwen2.5 (1.5B-72B), Llama-3.1-8B, Phi-3.5-mini, DeepSeek-R1-7B. Key quote: 'The error signal is a diagnostic readout—a summary statistic of computation quality—not a causal component that can be edited.' Cox et al. (2603.01437) independently confirm: steering fails on reasoning models despite high probe accuracy. This establishes that probe accuracy ≠ causal potency on reasoning models, which is the foundational observation our framework exploits.\n\n**Behavioral trajectory probing (foundational for our C(t) component).** Ballon et al. (2601.23163) introduce the truncation-reinjection protocol: generate full reasoning traces on Qwen3-4B/8B/14B and gpt-oss-20B/120B, truncate at decile intervals (10-100%), reinject with early-stopping suffix, measure answer-choice probability distributions. Key results: accuracy increases monotonically from 30.8-42.3% (no reasoning) to 49.0-73.1% (full trace) on GPQA-Diamond; decision commitment tracks similarly. Three control conditions validate causal content: random tokens (+2.1-4.3%), swapped traces (+3.2-8.7%), and shuffled tokens (+0.3-10.8%) all substantially underperform intact truncated traces (+18.1-33.1%), confirming sequential content — not just context length — drives gains. Stronger models rescue weak-model errors at 43-68% rate with free continuation vs. 28-51% anchoring in base mode. Explicitly disclaims faithfulness-to-internal-computations analysis, making it a direct precursor to our prefix-truncation C(t) estimator. Zhao et al. (2510.24941) introduce the True Thinking Score (TTS), measuring per-step causal contribution via numerical perturbation and ATE computation on DeepSeek-R1-Distill-Qwen-7B/14B/Llama-8B across AIME/MATH/AMC/CommonsenseQA, finding only 2.3% of AIME steps have TTS≥0.7. Ye et al. (2602.11201) introduce NLDD, finding a Reasoning Horizon at 70-85% of chain length on 3 models across synthetic tasks. Basu & Chakraborty (2603.22816) propose a decorative/scaffolding/genuine taxonomy. FACT-E (Sun et al. 2604.10693, ACL Findings 2026) provides another causal measurement approach.\n\n**Probe-intervention combinations (closest prior work).** Kudo et al. (2412.01113, EACL 2026) train per-position linear probes and validate with sliding-window activation patching on 9 models across synthetic multi-step arithmetic. They find CoT IS faithful for arithmetic but explicitly note their synthetic setting may not generalize. The CMI framework (2602.03994) introduces the CoT Mediation Index via layerwise activation patching across Phi, Qwen, DialoGPT on StrategyQA (20), TruthfulQA (10), GSM8K (20), identifying 'bypass regimes' where CMI ≈ 0. Both are complementary precursors operating on small samples or synthetic tasks.\n\n**Latent-reasoning theory.** Wang (2604.15726) formalizes three competing hypotheses about LLM reasoning: H1 (reasoning is primarily mediated by latent-state trajectories), H2 (reasoning is primarily mediated by explicit surface CoT), H0 (most reasoning gains are better explained by generic serial compute). Proposes compute-audited designs with six experimental arms (baseline, surface manipulation, surface control, latent intervention, latent control, compute-only expansion) and evidence tiers (probe-only = suggestive, compute-matched causal = strongest). Our ICG framework operationalizes Wang's H1/H2 distinction: when G*(t) >> 0, hidden states encode correctness awareness that CoT doesn't contribute (H1-consistent); when G*(t) ≈ 0, CoT is mediating (H2-consistent).\n\n**Temporal hidden-state dynamics (concurrent complementary work).** Gjølbye et al. (2605.15454) study hidden-state trajectory geometry across 11 models (6 reasoning: R1-Distill-Qwen-7B/14B/32B, R1-Distill-Llama-8B, QwQ-32B, Phi-4-Reasoning; 5 instruction-tuned baselines) on competitive programming (500 Codeforces), math (500 MATH), and Boolean SAT (500 SATBench). After length correction (residualizing directness/curvature on log(N)), difficulty remains systematically coupled to trajectory geometry: reasoning models show ρ⊥^D = +0.41 on Codeforces vs. −0.06 for baselines (raw correlations reverse from −0.73 to +0.41), with weaker effects in math (+0.05 vs. −0.07) and non-specific effects in SAT (+0.27 vs. +0.23). Critically, prompt-stage linear probes do NOT mirror these geometric effects — reasoning dynamics manifest during generation, not at input. Their length correction methodology and domain-specificity finding are relevant for our temporal analysis and difficulty conditioning. Furuya & Tanimura (2605.01853) introduce StALT, a training-free trajectory statistic separating correct from incorrect reasoning trajectories. Herrmann et al. (2605.09159) study 'internal polylogue' dynamics: persona vectors tracked temporally across MMLU-Pro in four open-weight models. Li et al. (2510.22362, NeurIPS 2025 MechInterp Workshop) introduce Concept Walk, tracking concept-direction alignment per step on Qwen 3-4B; find easy→decorative, hard→faithful. Vilas et al. (2510.10494, ICLR 2026) define three latent-trajectory signals, achieving 14-70% token savings on R1-Distill/Phi-4/Qwen3.\n\n**Probe calibration and inflation (methodological foundation).** Hewitt & Liang (2019) show MLP probes achieve only 4.5 selectivity. Ravichander et al. (2020) demonstrate properties recoverable even when unused. Voita & Titov (2020) show MDL-based probing reveals accuracy doesn't substantially favor pretrained over random. Chun et al. (2602.20338) apply Manifold Capacity Theory to CoT reasoning: geometric separability peaks transiently as a 'geometric pulse' while probe accuracy remains high afterward — direct evidence that probe accuracy overestimates information availability. We address this via null-probe calibration: P*(t) = P(t) − P_null(t).\n\n**Trajectory-shape analysis (supporting our shape-based classification).** Entropy trajectory paper (2603.18940): monotonicity predicts reliability regardless of absolute levels (+5.8pp). RQA analysis (2602.06266): temporal features outperform aggregates 36.94% vs. 28.97%. Microsoft trajectory geometry (2604.05655): 0.852 AUC from shape features vs. 0.649 baseline. This literature validates trajectory shapes as diagnostic features.\n\n**Measurement sensitivity.** Young (2603.20172) shows inter-classifier kappa as low as 0.06, up to 30.6pp divergence. Task-difficulty moderation: ICLR 2026 Workshop and Li et al. (2510.22362).\n\n**Reasoning-model internal dynamics.** Internal States Before Wait (2510.04128): crosscoders on R1-Distill with confirmed causal interventions for backtracking, uncertainty, verification features. From Reasoning to Answer (2509.23676): activation patching on R1-Distill.\n\n**Benchmarks, surveys, pathology diagnostics.** FaithCoT-Bench (ICLR 2026). Jin et al.'s survey (ARR for ACL 2026). Liu et al. (2602.13904): text-level metrics for rationalization/encoded/internalized reasoning. Reasoning Theater (2603.05488). Young (2603.26410). 'Lie to Me' (2603.22582). Various early-exit methods: ESTAR, DTSR, NEAT, CoDE-Stop, FRIT.\n\n**What remains open.** No extant framework provides: (1) a full-timeline information-contribution gap curve pairing calibrated probe trajectories with causal contribution estimation — Chrabąszcz et al.'s probe trajectories are the closest but lack the entire C(t) dimension, gap metric, and calibration; (2) an empirically-validated phenomenon trajectory-shape taxonomy grounded in real within-model, within-dataset G*(t) curves rather than cross-study semi-synthetic assembly; (3) an instance-level diagnostic score derived from the temporal gap; (4) difficulty-conditioned gap analysis with domain-specific nuance (following Gjølbye et al.'s finding of domain-dependent coupling strength); or (5) a principled treatment of the probe-target distinction (correctness vs. answer-content) and its implications for gap interpretation. The calibrated temporal ICG framework is unique in combining all five.\n\n## Approach\nWe propose the Information-Contribution Gap (ICG) framework: a calibrated, temporally-resolved diagnostic that measures the divergence between information available in hidden states and information that causally contributes to model outputs, tracked across the full chain-of-thought generation trajectory.\n\n**Formal Framework.** Define two time-varying quantities at each token position t during CoT generation:\n\n(i) *Calibrated Information Availability* P*(t): Cross-validated AUROC of a linear probe on layer-l hidden states at position t, calibrated via null-probe normalization (P*(t) = P(t) − P_null(t), following Hewitt & Liang 2019 selectivity, where P_null is trained on shuffled labels). **Probe target: correctness (right/wrong).** We choose correctness over answer-content for three reasons: (a) broader applicability — correctness probes generalize beyond binary/MC tasks (Cox et al.'s answer-content probes are limited to binary A/B on 4 tasks), while correctness probes (Yuan et al.) work across model families up to 72B; (b) the 'diagnostic not causal' finding that motivates the entire framework is specifically about correctness probes (Yuan et al.'s four-intervention failure on correctness probes); (c) correctness gaps are more directly interpretable for faithfulness — G*(t) >> 0 means 'the model's hidden states encode awareness that its answer is right/wrong, but its CoT does not causally reflect this self-monitoring.' On binary/MC task subsets, we additionally train answer-content probes to test whether the 'what answer' gap differs from the 'whether correct' gap — a supplementary analysis testing whether pre-CoT encoding operates on content or meta-cognition. This measures excess correctness awareness above correlative features. We probe at layers L/4, L/2, 3L/4, L to capture layer-wise dynamics. MCT geometric validation (Chun et al. 2602.20338) on 500 examples confirms whether calibrated probe signal reflects geometrically organized information rather than mere retrievability. Note: Chrabąszcz et al. (2605.18549) demonstrate that probe trajectories with 60+ signal-processing features substantially outperform static probes (up to 17pp on GSM8K). We adopt their insight that temporal dynamics are essential, while adding null-probe calibration (which they lack) and extending to the dual-estimator gap. Where applicable, we incorporate their feature categories (volatility, trend, steady-state, boundary transients) as additional trajectory descriptors for phenomenon classification in Phase 3.\n\n(ii) *Causal Contribution* C(t): The causal contribution of CoT up to position t, estimated via three complementary methods: (a) prefix-truncation ablation — measuring P(correct | CoT[:t]) vs. P(correct | full CoT), following Ballon et al.'s (2601.23163) truncation-reinjection protocol with their three control conditions (random tokens, swapped traces, shuffled tokens) to validate that C(t) measures genuine sequential content contribution rather than context-length effects (their finding: shuffled tokens retain +0.3-10.8% vs. intact +18.1-33.1%); (b) paraphrase perturbation — replacing CoT segments with meaning-preserving paraphrases and measuring answer stability; (c) NLDD-based influence scoring (Ye et al. 2602.11201) — measuring how corruption at position t degrades the answer distribution. Using multiple C(t) estimators provides robustness against single-method artifacts, following Young's (2603.20172) finding that faithfulness measurements are classifier-sensitive.\n\n**The Information-Contribution Gap.** G*(t) = P*(t) − C(t). This gap is the primary diagnostic signal:\n- G*(t) ≈ 0: Correctness awareness and causal contribution are aligned (necessary for faithfulness)\n- G*(t) >> 0: The model encodes correctness awareness it does not causally use in its CoT (diagnostic excess — the model 'knows but doesn't use')\n- G*(t) < 0: The CoT contributes to correctness beyond what hidden states encode at that point (information assembled during reasoning)\n\nBecause P*(t) is null-probe-calibrated, uniform correlative inflation is removed. C(t) is not subject to probe inflation as it measures behavioral change under intervention. The gap G*(t) is interpretable as 'calibrated correctness awareness the model has but doesn't channel through its CoT at position t.' Following Wang's (2604.15726) H1/H2 framework: G*(t) >> 0 is H1-consistent (latent-mediated reasoning), G*(t) ≈ 0 is H2-consistent (CoT-mediated reasoning).\n\n**Phenomenon Signature Predictions (2-3 confident, 4-5 stretch).** We ground predictions in real probe data but adopt honest scoping informed by the concern that cross-study heterogeneity may overestimate separability:\n\n*Primary targets (HIGH confidence, validated in Phase 0b pilot):*\n(i) *Pre-CoT encoding*: G*(t) starts high and stays high. Grounded in: David's 0.84 AUC at t=4, Esakkiraja's >90% pre-generation AUROC, Cox's >0.9 pre-CoT AUC. P*(0) > 0.5 (after calibration), C(t) rises slowly. Shape: large constant gap.\n(ii) *Genuine multi-step reasoning*: G*(t) converges toward zero. Grounded in: Zhang et al.'s 65%→79% chunk trajectory, Li et al.'s finding that hard→faithful, Ballon et al.'s monotonic accuracy increase with reasoning length. P*(t) rises gradually, C(t) tracks P*(t). Shape: co-rising curves, small/decreasing gap.\n(iii) *Post-hoc rationalization*: G*(t) starts moderate, rises during CoT. P*(t) stable (David: ~0.80 from t=4 through t=100), C(t) remains flat despite token generation. Shape: widening gap.\n\n*Stretch targets (MODERATE confidence, require additional features):*\n(iv) *Steganographic encoding*: G*(t) dip-and-recovery. Potentially consistent with Esakkiraja's dip at 5-10%. May require multi-layer analysis to separate from noise.\n(v) *Reasoning Theater*: EMPIRICAL QUESTION. Under non-uniform inflation, may overlap with pre-CoT encoding or post-hoc rationalization. Additional features — layer-wise P*(t) distribution, C(t) variance under paraphrase perturbation, Chrabąszcz-style signal features (autocorrelation, boundary transients, dwell-time run-lengths) — may enable separation. Whether Theater is cleanly separable is reported honestly with confusion matrices.\n\n**Semi-Synthetic Simulation (hypothesis generation, NOT validation).** We construct semi-synthetic G*(t) curves grounded in real published data to generate testable predictions about trajectory-shape separability — but we do NOT treat this as evidence of real-data separability (published measurements come from different models, datasets, and setups, introducing heterogeneity that does not match within-dataset variance). Instead, the simulation identifies: (a) which trajectory features are most discriminative in principle, (b) what minimum effect sizes real-data classification needs to achieve, (c) where non-uniform inflation causes theoretical overlap between phenomena. I_probe(t) profiles drawn from published measurements (David, Zhang, Esakkiraja, Yuan), C(t) profiles modeled from NLDD (Ye et al.) and TTS (Zhao et al.) data, non-uniform inflation calibrated against Chun et al.'s MCT finding. The real validation comes from Phase 0b.\n\n**Phase 0a: Gap Characterization (Weeks 1-2.5).** Three objectives on 500 examples × 3 datasets (GSM8K, MATH-500, MMLU) × 3 models (DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct):\n(i) Construct empirical P*(t) and C(t) curves at token-level resolution\n(ii) Validate null-probe calibration: P_null(t) shows high accuracy (inflation exists) but P*(t) shows meaningful variance (calibration reveals structure)\n(iii) Characterize causal potency: following Cox et al.'s protocol, measure answer flip rates via probe-direction steering on reasoning vs. instruction-tuned models\n\nExpected outcome (base case): Causal potency is low on reasoning models, confirming the diagnostic-not-causal property and validating the ICG framework's interpretive power. If causal potency is unexpectedly high, this is an exciting upgrade. Either outcome is scientifically valuable.\n\n**Phase 0b: Empirical Pilot for Phenomenon Separability (Weeks 2.5-4).** This phase validates that trajectory-shape classification is feasible on real data before committing to the full pipeline. On the SAME model (R1-Distill-Qwen-7B) and datasets (GSM8K + MATH-500, 1000 examples), construct real G*(t) curves and test whether at least 2 phenomena produce distinguishable trajectories. Protocol: (i) partition examples by difficulty quintile and model behavior (easy-correct with high P*(0) → pre-CoT encoding candidates; hard-correct with rising P*(t) tracking C(t) → genuine reasoning candidates; incorrect with stable P*(t) and flat C(t) → post-hoc rationalization candidates); (ii) compute full G*(t) for each partition; (iii) test effect size d > 0.5 on at least 2 trajectory features between partitions. Apply Gjølbye et al.'s (2605.15454) length correction (residualizing trajectory features on log(N)) to ensure differences are not conflated with generation-length effects. Success criterion: d > 0.5 between at least 2 partitions on 2+ features. If d < 0.3 across all features, downscope to a characterization paper (gap exists and varies with difficulty, but trajectory shapes are not cleanly phenotypic) — still a strong contribution given no prior full-timeline G*(t) measurement exists.\n\n**Phase 1: Full ICG Construction (Weeks 4-9).** Conditional on Phase 0b showing separability (d > 0.5). Extend to 4 models (add QwQ-32B or R1-Distill-32B) × 4 benchmarks (add GPQA-Diamond or AIME). Full calibrated P*(t) with null-probe normalization + MCT concordance check on 500 examples. Three C(t) estimators with Ballon et al.-style controls (random, swap, shuffle baselines). Cross-reference with TTS (Zhao et al.) at step boundaries. Bootstrap confidence intervals on G*(t).\n\n**Phase 2: Task-Difficulty Conditioning (Weeks 7-11).** Partition each benchmark into difficulty quintiles (using model accuracy as proxy). Measure G*(t) per quintile. Hypothesis grounded in David's easy/hard data, Li et al.'s finding, and Gjølbye et al.'s difficulty-geometry coupling: easy problems show large persistent gap (decorative CoT), hard problems show converging gap (load-bearing CoT). Following Gjølbye et al., apply length correction and report domain-specific effects — expecting stronger effects on math/code benchmarks than MMLU, given their finding of ρ⊥ = +0.41 on Codeforces vs. +0.05 on MATH. The transition point — where G*(t) shifts from decorative to genuine — provides practical guidance on when CoT adds value.\n\n**Phase 3: Phenomenon Classification and Robustness (Weeks 9-14).** Apply trajectory-shape classification to real data. Target: 2-3 cleanly separable phenomena, with 4-5 reported honestly including overlap. Incorporate Chrabąszcz et al.'s feature categories (volatility, trend, boundary transients, autocorrelation) alongside our gap-specific features (initial G* value, G* slope, convergence rate, dC/dt locality). Six robustness ablations following Young (2603.20172): (a) probe architecture (linear vs. 2-layer MLP) with selectivity; (b) layer selection (single best vs. multi-layer); (c) C(t) estimator agreement (prefix vs. paraphrase vs. NLDD); (d) gap normalization method; (e) calibration method (shuffled-label vs. random-representation); (f) probe target (correctness vs. answer-content on binary/MC subsets). Report sensitivity ranges across all dimensions.\n\n**TIF Score.** Temporal Information-contribution Faithfulness score: normalized area under calibrated G*(t), benchmarked against FaithCoT-Bench and Liu et al.'s text-level metrics.\n\n**Paper Focus (Tightened).** Core contributions: (1) calibrated ICG diagnostic with explicitly justified correctness-probe target on 4 models × 4 benchmarks, positioned against Chrabąszcz et al.'s probe trajectories — demonstrating the value added by the causal contribution dimension and gap metric; (2) Phase 0b empirical pilot validating that 2-3 phenomena produce distinguishable G*(t) signatures on real within-model, within-dataset data; (3) task-difficulty conditioning revealing the decorative→load-bearing transition with domain-specific strength following Gjølbye et al.'s nuance. Supporting: robustness ablations (6 dimensions); TIF validation. Supplementary: 671B subset (500 examples, 3 layers); answer-content vs. correctness probe comparison; semi-synthetic simulation as hypothesis generation.\n\n**Experiments.** DeepSeek-R1-Distill-Qwen-7B/14B/32B, QwQ-32B across MMLU, GPQA-Diamond, GSM8K, AIME. 671B validation (500-example subset, 3 layers). Calibration checks: synthetic arithmetic (G* ≈ 0 expected), TTS cross-reference, MCT cross-reference. Gjølbye-style length correction on all temporal analyses.\n\n## Resource Estimate\n{'manual': {'gpu_hours': '~830 H100-hours (Phase 0a characterization: 80 hrs [3 models × 3 datasets, probe training + prefix ablation + steering tests]; Phase 0b empirical pilot: 30 hrs [1 model × 2 datasets, full G*(t) construction + partition analysis + length correction]; Phase 1 full ICG: 120 hrs [4 models × 4 benchmarks, multi-layer probes + 3 C(t) estimators]; Phase 2 difficulty conditioning: 50 hrs; Phase 3 phenomenon classification + robustness ablations: 50 hrs; NLDD on 32B model: 250 hrs [primary bottleneck — up to 20 perturbation positions × 5K examples × forward passes]; NLDD on 7B/14B models: 100 hrs; MCT geometric validation: 50 hrs; 671B subset: 50 hrs [8×H100]; semi-synthetic simulation: 50 hrs [mostly CPU, some GPU for validation])', 'timeline': '15-17 weeks (2 researchers: 4 weeks Phase 0a+0b characterization + pilot; 5 weeks Phase 1 full ICG; 4 weeks Phases 2-3 in parallel with NLDD; 2-3 weeks writing + ablations)', 'estimated_gpu_cost': '$2,500 at ~$3/H100-hour (cloud spot pricing)', 'storage': '3-5 TB (4 layers per model, fp16); reducible to ~1.5 TB via PCA'}, 'human_in_loop': {'gpu_hours': '~830 H100-hours', 'timeline': '13 weeks (1 researcher + Claude for experiment design and analysis)', 'claude_api_cost': '$350', 'estimated_gpu_cost': '$2,500'}, 'auto_research': {'gpu_hours': '~830 H100-hours', 'timeline': '11 weeks', 'claude_api_cost': '$700', 'estimated_gpu_cost': '$2,500', 'speed_bottleneck': 'NLDD on 32B (~250 H100-hours, ~30% of total compute) is the primary bottleneck. Each NLDD evaluation requires corrupting reasoning at multiple positions and measuring logit degradation — O(T × N) forward passes where T≈20 perturbation positions and N≈5K examples. For 32B models, this cannot be easily parallelized beyond 8-GPU data parallelism. Secondary: 671B subset (8×H100, ~50 hrs); MCT geometric validation (~50 hrs). Phase 0b pilot (30 hrs) provides early go/no-go signal before committing full Phase 1-3 compute.'}}\n\n## Inspired By\nThe convergence of five independent lines of evidence — (a) Cox et al.'s finding that answer-content probe steering fails on reasoning models despite high accuracy; (b) Yuan et al.'s systematic demonstration that four interventions all fail on correctness probes, establishing 'diagnostic not causal'; (c) the temporal probe dynamics now empirically characterized by David (0.84 AUC at t=4, stable ~0.8), Zhang et al. (chunk-level rising trajectory), Esakkiraja et al. (pre-generation >90% with dip-recovery), and Chrabąszcz et al. (60+ trajectory features capturing dynamics invisible to static probes, up to 17pp improvement); (d) Ballon et al.'s truncation-reinjection protocol demonstrating monotonic behavioral C(t) curves with rigorous controls (sequential content +18.1-33.1% vs. shuffled +0.3-10.8%) — all pointing to the same insight: the gap between diagnostic information availability and causal contribution IS the phenomenon of interest. Additionally inspired by: Wang's (2604.15726) formalization of H1/H2/H0 hypotheses providing the theoretical scaffold for what our framework empirically measures; Gjølbye et al.'s (2605.15454) finding that difficulty-geometry coupling is domain-specific and requires length correction; Herrmann et al.'s concurrent temporal persona-vector dynamics; and the trajectory-shape literature showing shapes can distinguish phenomena regardless of absolute-value calibration.\n\n## Target Venues\n- ICLR 2027 (abstract: Sep 19, full paper: Sep 24, 2026; conference: Apr/May 2027 — primary target, 4 months from now)\n- ICML 2027 (full paper: Jan 29, 2027; conference: Jul 2027 — comfortable fallback if additional experiments needed)\n\n## Key References\n- Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics (Chrabąszcz et al., arXiv 2605.18549)\n- Probing the Trajectories of Reasoning Traces in Large Language Models (Ballon et al., arXiv 2601.23163)\n- LLM Reasoning Is Latent, Not the Chain of Thought (Wang, arXiv 2604.15726)\n- Reasoning Models Don't Just Think Longer, They Move Differently (Gjølbye et al., arXiv 2605.15454)\n- Hidden Error Awareness: The Signal Is Diagnostic, Not Causal (Yuan et al., arXiv 2605.09502)\n- Decoding Answers Before Chain-of-Thought: Pre-CoT Probes and Activation Steering (Cox et al., arXiv 2603.01437)\n- Temporal Predictors of Outcome in Reasoning Language Models (David, arXiv 2511.14773)\n- Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification (Zhang et al., arXiv 2504.05419)\n- Therefore I am. I Think (Esakkiraja et al., arXiv 2604.01202)\n- Can Aha Moments Be Fake? True Thinking Score (Zhao et al., arXiv 2510.24941)\n- Mechanistic Evidence for Faithfulness Decay / NLDD (Ye et al., arXiv 2602.11201)\n- Do LLMs Experience an Internal Polylogue? (Herrmann et al., arXiv 2605.09159)\n- LLMs Faithfully and Iteratively Compute Answers During CoT (Kudo et al., EACL 2026, arXiv 2412.01113)\n- When Chains of Thought Don't Matter: Causal Bypass / CMI (Sathyanarayanan et al., arXiv 2602.03994)\n- Spatiotemporal Hidden-State Dynamics / StALT (Furuya & Tanimura, arXiv 2605.01853)\n- Mapping Faithful Reasoning / Concept Walk (Li et al., arXiv 2510.22362, NeurIPS 2025 MechInterp Workshop)\n- Task Difficulty Shapes CoT Faithfulness (ICLR 2026 Workshop)\n- Diagnosing Pathological CoT (Liu et al., arXiv 2602.13904)\n- Measuring Faithfulness Depends on How You Measure (Young, arXiv 2603.20172)\n- Emergent Manifold Separability / MCT (Chun et al., arXiv 2602.20338)\n- Tracing the Traces: Latent Temporal Signals (Vilas et al., ICLR 2026, arXiv 2510.10494)\n- Probing and Steering CoT Unfaithfulness (Occhipinti et al., ICLR 2026 LIT Workshop)\n- Designing and Interpreting Probes with Control Tasks (Hewitt & Liang, EMNLP 2019)\n- Information-Theoretic Probing with MDL (Voita & Titov, EMNLP 2020, arXiv 2003.12298)\n- Probing the Probing Paradigm (Ravichander et al., arXiv 2005.00719)\n- Shape-over-magnitude dissociation in entropy trajectories (arXiv 2603.18940)\n- Is My Model Mind Blurting? RQA of Reasoning Dynamics (arXiv 2602.06266)\n- LLM Reasoning as Trajectories (arXiv 2604.05655, Microsoft)\n- Internal States Before Wait Modulate Reasoning Patterns (arXiv 2510.04128)\n- FACT-E (Sun et al., ACL Findings 2026, arXiv 2604.10693)\n- Breaking the Chain (Somov et al., arXiv 2603.16475)\n- The Illusion of Reasoning (Basu & Chakraborty, arXiv 2603.22816)\n- FaithCoT-Bench (ICLR 2026, arXiv 2510.04040)\n- The Mirage of Explainability survey (Jin et al., ARR for ACL 2026)\n- Reasoning Theater (Boppana et al., arXiv 2603.05488)\n- No Global Plan in CoT (Xu et al., arXiv 2602.02103)\n- Catching Rationalization in the Act (Mirtaheri & Belkin, arXiv 2603.17199)\n- CoT Monitorability via Information Theory (Anwar et al., arXiv 2602.18297)\n- Understanding CoT via Information Theory (Ton et al., ICML 2025, arXiv 2411.11984)\n- Demystifying Reasoning Dynamics with MI (Qian et al., NeurIPS 2025, arXiv 2506.02867)\n- Analysing CoT Dynamics (Lewis-Lim et al., EMNLP 2025, arXiv 2508.19827)\n- Why Models Know But Don't Say (Young, arXiv 2603.26410)\n- Lie to Me (arXiv 2603.22582)\n- Step-Level Hallucination via Transport Geometry (Alvarez & Baheri, arXiv 2605.13772)\n- From Reasoning to Answer (arXiv 2509.23676)\n- SAE Reasoning Features (arXiv 2503.18878)\n- FRIT (Swaroop et al., arXiv 2509.13334)\n- Solution Hides in Hidden States (arXiv 2604.23351)\n- Knowing Before Saying (ACL Findings 2025, arXiv 2505.24362)\n- LEACE: Perfect Linear Concept Erasure (Belrose et al., NeurIPS 2023, arXiv 2306.03819)\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T03:48:14.902Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T03:48:14.902Z",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b"
}
```

---

## Round 1

57 recorded events

### User

_source line 3 · 2026-05-20T03:48:14.917Z_

# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness

## Description
We propose the Information-Contribution Gap (ICG) framework, a calibrated temporal diagnostic for chain-of-thought faithfulness that exploits a robust empirical finding: linear probes on hidden states reliably diagnose answer correctness (0.82-0.95 AUROC across four independent groups) yet causal interventions based on these probes consistently fail on reasoning-trained models (Cox et al.: negligible flip rates; Yuan et al.: all four intervention strategies fail). Rather than treating this diagnostic-causal gap as an obstacle, we make it the primary object of study — the gap between what models internally know and what their CoT causally contributes IS the faithfulness signal.

The framework tracks two calibrated time-varying quantities across the full CoT trajectory: P*(t), null-probe-calibrated correctness awareness (explicitly targeting right/wrong prediction — justified over answer-content probes by broader applicability beyond binary tasks, grounding in the diagnostic-not-causal finding which is about correctness, and more direct faithfulness interpretation — with supplementary answer-content analysis on binary/MC subsets), and C(t), causal contribution estimated via three complementary methods (prefix truncation with Ballon et al.'s three control conditions validating sequential content matters, paraphrase perturbation, NLDD). Their divergence G*(t) = P*(t) − C(t) produces phenomenon-specific temporal fingerprints, operationalizing Wang's (2604.15726) H1/H2 distinction: G*(t) >> 0 is latent-mediated (H1-consistent), G*(t) ≈ 0 is CoT-mediated (H2-consistent).

Positioned against the closest concurrent work — Chrabąszcz et al.'s (2605.18549) probe trajectories with 60+ signal-processing features achieving up to 17pp improvement over static probes across 4 reasoning models — our framework adds the entire causal contribution dimension, the calibrated gap metric, null-probe calibration with MCT geometric validation, phenomenon taxonomy, and task-difficulty conditioning. Their probe-trajectory methodology validates our P*(t) direction; we extend it to the dual-estimator gap that no existing framework provides.

We adopt honest scoping: 2-3 faithfulness phenomena (pre-CoT encoding, genuine reasoning, post-hoc rationalization) as the realistic classification target, with steganographic encoding and reasoning theater as stretch goals. A new empirical pilot phase (Phase 0b) constructs real G*(t) curves from the SAME model and dataset and tests whether at least 2 phenomena produce distinguishable trajectories (effect size d > 0.5) before committing to the full classification pipeline — addressing the concern that semi-synthetic simulation from cross-study measurements overestimates real-data accuracy. The semi-synthetic simulation is retained as hypothesis generation producing testable predictions, not as evidence.

Task-difficulty conditioning — grounded in David's easy (0.84) vs. hard (0.76) probe splits, the ICLR 2026 Workshop finding, and Gjølbye et al.'s (2605.15454) demonstration that difficulty-geometry coupling is systematic (ρ⊥ = +0.41 on Codeforces) but domain-specific (weaker on MATH) — reveals the decorative→load-bearing transition with practical guidance on when chain-of-thought adds genuine value, applying length correction (residualizing on log(N)) to avoid generation-length confounds.

The paper focuses on four core contributions: (a) calibrated ICG diagnostic with explicitly justified correctness-probe target on 4 models × 4 benchmarks, positioned against Chrabąszcz et al. to demonstrate the value of the causal contribution dimension; (b) empirical pilot validating that 2-3 phenomena produce distinguishable G*(t) signatures on real data; (c) difficulty-conditioned gap analysis with domain-specific nuance; (d) probe-target analysis contrasting correctness vs. answer-content gaps. Total compute: ~830 H100-hours, with NLDD on 32B models (~250 hrs) as the primary bottleneck.

## Core Problem
A striking convergence of 2025-2026 findings reveals a fundamental disconnect in reasoning language models: their hidden states reliably encode information about answer correctness — with linear probes achieving 0.82-0.95 AUROC across multiple independent groups — yet causal interventions based on these probes consistently fail to influence model outputs. Cox et al. (2603.01437) find that steering via answer-content probes produces answer flip rates 'negligible against the orthogonal baseline' on reasoning models, despite >0.9 AUC on instruction-tuned models. Yuan et al. (2605.09502) systematically test four distinct intervention strategies (activation steering, probe-guided best-of-N, self-correction, activation patching) on models up to 72B parameters and report that ALL fail: 'RL training does not close the diagnostic–causal gap.' This diagnostic-causal gap — the divergence between what information is available in a model's hidden states and what information the chain-of-thought reasoning text causally contributes — is NOT a methodological obstacle to overcome; it IS the central phenomenon. Critically, the literature conflates two distinct probe targets: answer-content probes (Cox et al.: predicting the specific answer on binary tasks, models ≤9B + GPT-OSS-20B) and correctness probes (Yuan et al.: predicting right/wrong on models up to 72B; Zhang et al.: per-chunk correctness on 7B-70B). This distinction matters because the gap's interpretation differs: answer-content gaps mean 'the model has already decided but CoT doesn't derive the answer,' while correctness gaps mean 'the model knows it's right/wrong but CoT doesn't reflect this awareness.' Meanwhile, the temporal dynamics of this gap are now empirically grounded: David (2511.14773) shows probe accuracy stabilizes at 0.84 AUC by token 4, remaining ~0.8 through token 100, with task-difficulty conditioning revealing easy (0.84) vs. hard (0.76) signatures. Zhang et al. (2504.05419) report chunk-level probe trajectories rising from 65% at 10% of reasoning to 79% at 100% on R1-Distill. Esakkiraja et al. (2604.01202) find >90% pre-generation AUROC with a characteristic dip at 5-10% of reasoning followed by recovery. Chrabąszcz et al. (2605.18549) demonstrate that temporal probe trajectories with 60+ signal-processing features achieve up to 17pp improvement over static probes, showing that trajectory dynamics capture information invisible to single-timepoint measurements. These temporal profiles suggest that different modes of CoT unfaithfulness — pre-CoT encoding, post-hoc rationalization, reasoning theater, myopic planning, thinking-answer gap — produce distinguishable temporal divergence signatures. Yet no existing framework jointly tracks information availability AND causal contribution across the full CoT timeline: Chrabąszcz et al. provide the closest probe-trajectory methodology but lack any causal contribution component, gap metric, probe calibration, or phenomenon taxonomy; Ballon et al. (2601.23163) provide behavioral causal curves via truncation-reinjection but lack hidden-state measurement; the CMI framework provides layerwise causal audit on ~50 examples but no temporal resolution; Zhao et al.'s True Thinking Score provides per-step causal contribution but no probe-side measurement. The gap between diagnostic information availability and causal contribution IS the phenomenon of interest, not an obstacle.

## Opportunity
The field has independently produced the measurement tools needed for a unified temporal framework, but these tools remain siloed. The opportunity is fourfold:

(1) **Temporal gap measurement.** Despite rapid accumulation of probe measurements (David: 0.84 at t=4; Zhang: 0.82-0.91 on chunks; Yuan: 0.95 overall, 0.787 first-step; Esakkiraja: >90% pre-generation; Chrabąszcz et al.: 91-97% AUROC with max-pooling on trajectories), no work tracks the full-timeline divergence between probe-estimated information availability and intervention-estimated causal contribution. Chrabąszcz et al. (2605.18549) come closest on the probe side — extracting 60+ signal-processing features from probe trajectories across 4 reasoning models and 4 datasets, achieving up to 17pp improvement over static probes on GSM8K — but they target outcome prediction (correctness, harmfulness) rather than the faithfulness gap, and provide no causal contribution measurement. Their work validates that temporal probe trajectories capture dynamics invisible to static probes (confirming our P*(t) direction); our framework extends this via the dual-estimator gap G*(t) = P*(t) − C(t) that requires the additional causal contribution dimension, null-probe calibration, and phenomenon mapping. On the causal side, Ballon et al. (2601.23163) provide behavioral C(t) curves via truncation-reinjection at decile intervals on Qwen3/gpt-oss across GPQA-Diamond and MMLU-Pro — showing monotonic accuracy increase from 30.8-42.3% to 49.0-73.1% with control conditions validating that sequential content (not just context length) matters — but lack hidden-state measurement. The gap between these two measurement traditions IS the framework's niche.

(2) **Phenomenon unification with honest scoping.** The CoT faithfulness literature treats each failure mode as separate: Reasoning Horizon (Ye et al. 2602.11201), pre-CoT encoding (Cox et al. 2603.01437; Esakkiraja et al. 2604.01202), Reasoning Theater (Boppana et al. 2603.05488), myopic planning (Xu et al. 2602.02103), thinking-answer gap. We propose that 2-3 of these are confidently distinguishable via trajectory-shape signatures in the information-contribution gap G*(t), with 4-5 as a stretch goal requiring additional features. The honest scoping — validated through an empirical pilot on real data before committing to full classification — is itself a contribution to a field prone to over-claiming.

(3) **Task-difficulty conditioning.** The ICLR 2026 Workshop finding and Li et al.'s (2510.22362) corroboration show easy→decorative, hard→faithful. David's easy/hard splits (0.84 vs. 0.76 at t=32) provide probe-level evidence. Gjølbye et al. (2605.15454) demonstrate that difficulty is systematically coupled to hidden-state trajectory geometry even after length correction (ρ⊥ = +0.41 for reasoning models vs. −0.06 for baselines on competitive programming), with domain-specific strength. A difficulty-conditioned gap framework can answer the practical question: at what difficulty level does CoT transition from decorative to load-bearing?

(4) **Probe target clarification.** The field has not confronted the distinction between answer-content probes (Cox et al.: binary tasks, ≤9B) and correctness probes (Yuan et al.: up to 72B). A framework that explicitly measures correctness awareness gap — and contrasts it with answer-content gap on applicable tasks — provides the first principled treatment of what 'knowing but not using' means.

Two prior works have combined probing with causal interventions: Kudo et al. (EACL 2026) on synthetic arithmetic, and the CMI framework (2602.03994) on ~50 examples. Wang (2604.15726) formalizes the need via competing hypotheses (H1: latent-mediated, H2: CoT-mediated, H0: serial compute) and proposes compute-audited designs — our ICG framework provides an empirical methodology to distinguish H1 from H2 at each token position. Neither Kudo et al. nor CMI provides: (a) full temporal-position coverage on natural benchmarks, (b) mapping to named faithfulness phenomena, (c) a standalone instance-level diagnostic, (d) systematic multi-model comparison, (e) robustness validation — a critical gap highlighted by Young's (2603.20172) finding that faithfulness measurements are classifier-sensitive (inter-classifier kappa as low as 0.06), or (f) an empirical pilot validating phenomenon separability on real data.

## Landscape
**Probe-based temporal measurement (foundational for our P*(t) component).** Chrabąszcz et al. (2605.18549) is the closest concurrent work: they introduce probe trajectories — tracking concept probability at each generated token — and extract 60+ signal-processing features (volatility, trend, steady-state, temporal segmentation, boundary transients, autocorrelation) via 3-layer MLP probes with Multi-Instance Learning meta-probe across layers. Key results: max-pooling achieves 91-97% AUROC on harmfulness detection (vs. 33-61% for average-pooling, demonstrating average/last-token pooling collapses to near-random); up to 17pp improvement over static probes on GSM8K mathematical error prediction across Llama-8B-R1-Distill and Qwen3-4B/8B/14B (~3000 GPU-hours total). Critical differentiators from our framework: (a) NO causal contribution component — they measure only probe accuracy trajectories, not whether CoT causally contributes; (b) NO gap metric — just trajectory vs. static comparison for outcome prediction; (c) NO null-probe calibration or MCT geometric validation — their 3-layer MLP probes are uncalibrated; (d) NO phenomenon taxonomy — they separate correct/incorrect or safe/harmful, not faithfulness modes; (e) NO task-difficulty conditioning. Their 60+ feature extraction methodology is complementary and could enhance our trajectory-shape classification. David (2511.14773) trains per-position probes on reasoning models, finding 0.84 AUC at t=4, stable ~0.8 through t≈100, with easy/hard splits of 0.84 vs. 0.76 at t=32 on Qwen3-8B. Zhang et al. (2504.05419) probe R1-Distill models (7B/32B/70B) for correctness at each reasoning chunk, achieving 0.82-0.91 AUROC on GSM8K/MATH/AIME, with a rising trajectory from 65% at 10% chunk to 79% at 100%, enabling 24% token reduction via early-exit. Yuan et al. (2605.09502) report 0.95 AUROC on Qwen-3B, 0.852 on DeepSeek-R1-7B, 0.787 from first-step hidden states alone, and a concealment gap of 0.197 AUROC between hidden-state (0.787) and text-surface (0.590) classifiers — using correctness probes (right/wrong), not answer-content probes. Esakkiraja et al. (2604.01202) find >90% AUROC pre-generation on Qwen3-4B and GLM-Z1-9B, with a characteristic dip at 5-10% of reasoning and recovery to near-100% by think_end. Cox et al. (2603.01437) use answer-content probes (predicting specific answer A/B on binary tasks: Anachronisms, Logical Deduction, Sports Understanding, Social Chemistry) achieving >0.9 AUC on instruction-tuned Gemma-2 (2B, 9B) and Qwen-2.5 (1.5B, 3B, 7B) models, with causal validation via steering (>50% flip rates) — but 'the answer flip rate is negligible against the orthogonal baseline' on the reasoning model GPT-OSS-20B. Additional probing work: Qian et al. (2506.02867, NeurIPS 2025); Lewis-Lim et al. (2508.19827, EMNLP 2025); Mirtaheri & Belkin (2603.17199); Occhipinti et al. (ICLR 2026 LIT Workshop, probing F1 90-100%, steering 46% recovery).

**The diagnostic-not-causal evidence (motivating our framework).** Yuan et al. (2605.09502) is the decisive study: four interventions — activation steering (at most +4%), probe-guided best-of-N (matches random), self-correction (hurts accuracy −3%), activation patching (destroys coherence at α=0.5) — all fail. Tested on Qwen2.5 (1.5B-72B), Llama-3.1-8B, Phi-3.5-mini, DeepSeek-R1-7B. Key quote: 'The error signal is a diagnostic readout—a summary statistic of computation quality—not a causal component that can be edited.' Cox et al. (2603.01437) independently confirm: steering fails on reasoning models despite high probe accuracy. This establishes that probe accuracy ≠ causal potency on reasoning models, which is the foundational observation our framework exploits.

**Behavioral trajectory probing (foundational for our C(t) component).** Ballon et al. (2601.23163) introduce the truncation-reinjection protocol: generate full reasoning traces on Qwen3-4B/8B/14B and gpt-oss-20B/120B, truncate at decile intervals (10-100%), reinject with early-stopping suffix, measure answer-choice probability distributions. Key results: accuracy increases monotonically from 30.8-42.3% (no reasoning) to 49.0-73.1% (full trace) on GPQA-Diamond; decision commitment tracks similarly. Three control conditions validate causal content: random tokens (+2.1-4.3%), swapped traces (+3.2-8.7%), and shuffled tokens (+0.3-10.8%) all substantially underperform intact truncated traces (+18.1-33.1%), confirming sequential content — not just context length — drives gains. Stronger models rescue weak-model errors at 43-68% rate with free continuation vs. 28-51% anchoring in base mode. Explicitly disclaims faithfulness-to-internal-computations analysis, making it a direct precursor to our prefix-truncation C(t) estimator. Zhao et al. (2510.24941) introduce the True Thinking Score (TTS), measuring per-step causal contribution via numerical perturbation and ATE computation on DeepSeek-R1-Distill-Qwen-7B/14B/Llama-8B across AIME/MATH/AMC/CommonsenseQA, finding only 2.3% of AIME steps have TTS≥0.7. Ye et al. (2602.11201) introduce NLDD, finding a Reasoning Horizon at 70-85% of chain length on 3 models across synthetic tasks. Basu & Chakraborty (2603.22816) propose a decorative/scaffolding/genuine taxonomy. FACT-E (Sun et al. 2604.10693, ACL Findings 2026) provides another causal measurement approach.

**Probe-intervention combinations (closest prior work).** Kudo et al. (2412.01113, EACL 2026) train per-position linear probes and validate with sliding-window activation patching on 9 models across synthetic multi-step arithmetic. They find CoT IS faithful for arithmetic but explicitly note their synthetic setting may not generalize. The CMI framework (2602.03994) introduces the CoT Mediation Index via layerwise activation patching across Phi, Qwen, DialoGPT on StrategyQA (20), TruthfulQA (10), GSM8K (20), identifying 'bypass regimes' where CMI ≈ 0. Both are complementary precursors operating on small samples or synthetic tasks.

**Latent-reasoning theory.** Wang (2604.15726) formalizes three competing hypotheses about LLM reasoning: H1 (reasoning is primarily mediated by latent-state trajectories), H2 (reasoning is primarily mediated by explicit surface CoT), H0 (most reasoning gains are better explained by generic serial compute). Proposes compute-audited designs with six experimental arms (baseline, surface manipulation, surface control, latent intervention, latent control, compute-only expansion) and evidence tiers (probe-only = suggestive, compute-matched causal = strongest). Our ICG framework operationalizes Wang's H1/H2 distinction: when G*(t) >> 0, hidden states encode correctness awareness that CoT doesn't contribute (H1-consistent); when G*(t) ≈ 0, CoT is mediating (H2-consistent).

**Temporal hidden-state dynamics (concurrent complementary work).** Gjølbye et al. (2605.15454) study hidden-state trajectory geometry across 11 models (6 reasoning: R1-Distill-Qwen-7B/14B/32B, R1-Distill-Llama-8B, QwQ-32B, Phi-4-Reasoning; 5 instruction-tuned baselines) on competitive programming (500 Codeforces), math (500 MATH), and Boolean SAT (500 SATBench). After length correction (residualizing directness/curvature on log(N)), difficulty remains systematically coupled to trajectory geometry: reasoning models show ρ⊥^D = +0.41 on Codeforces vs. −0.06 for baselines (raw correlations reverse from −0.73 to +0.41), with weaker effects in math (+0.05 vs. −0.07) and non-specific effects in SAT (+0.27 vs. +0.23). Critically, prompt-stage linear probes do NOT mirror these geometric effects — reasoning dynamics manifest during generation, not at input. Their length correction methodology and domain-specificity finding are relevant for our temporal analysis and difficulty conditioning. Furuya & Tanimura (2605.01853) introduce StALT, a training-free trajectory statistic separating correct from incorrect reasoning trajectories. Herrmann et al. (2605.09159) study 'internal polylogue' dynamics: persona vectors tracked temporally across MMLU-Pro in four open-weight models. Li et al. (2510.22362, NeurIPS 2025 MechInterp Workshop) introduce Concept Walk, tracking concept-direction alignment per step on Qwen 3-4B; find easy→decorative, hard→faithful. Vilas et al. (2510.10494, ICLR 2026) define three latent-trajectory signals, achieving 14-70% token savings on R1-Distill/Phi-4/Qwen3.

**Probe calibration and inflation (methodological foundation).** Hewitt & Liang (2019) show MLP probes achieve only 4.5 selectivity. Ravichander et al. (2020) demonstrate properties recoverable even when unused. Voita & Titov (2020) show MDL-based probing reveals accuracy doesn't substantially favor pretrained over random. Chun et al. (2602.20338) apply Manifold Capacity Theory to CoT reasoning: geometric separability peaks transiently as a 'geometric pulse' while probe accuracy remains high afterward — direct evidence that probe accuracy overestimates information availability. We address this via null-probe calibration: P*(t) = P(t) − P_null(t).

**Trajectory-shape analysis (supporting our shape-based classification).** Entropy trajectory paper (2603.18940): monotonicity predicts reliability regardless of absolute levels (+5.8pp). RQA analysis (2602.06266): temporal features outperform aggregates 36.94% vs. 28.97%. Microsoft trajectory geometry (2604.05655): 0.852 AUC from shape features vs. 0.649 baseline. This literature validates trajectory shapes as diagnostic features.

**Measurement sensitivity.** Young (2603.20172) shows inter-classifier kappa as low as 0.06, up to 30.6pp divergence. Task-difficulty moderation: ICLR 2026 Workshop and Li et al. (2510.22362).

**Reasoning-model internal dynamics.** Internal States Before Wait (2510.04128): crosscoders on R1-Distill with confirmed causal interventions for backtracking, uncertainty, verification features. From Reasoning to Answer (2509.23676): activation patching on R1-Distill.

**Benchmarks, surveys, pathology diagnostics.** FaithCoT-Bench (ICLR 2026). Jin et al.'s survey (ARR for ACL 2026). Liu et al. (2602.13904): text-level metrics for rationalization/encoded/internalized reasoning. Reasoning Theater (2603.05488). Young (2603.26410). 'Lie to Me' (2603.22582). Various early-exit methods: ESTAR, DTSR, NEAT, CoDE-Stop, FRIT.

**What remains open.** No extant framework provides: (1) a full-timeline information-contribution gap curve pairing calibrated probe trajectories with causal contribution estimation — Chrabąszcz et al.'s probe trajectories are the closest but lack the entire C(t) dimension, gap metric, and calibration; (2) an empirically-validated phenomenon trajectory-shape taxonomy grounded in real within-model, within-dataset G*(t) curves rather than cross-study semi-synthetic assembly; (3) an instance-level diagnostic score derived from the temporal gap; (4) difficulty-conditioned gap analysis with domain-specific nuance (following Gjølbye et al.'s finding of domain-dependent coupling strength); or (5) a principled treatment of the probe-target distinction (correctness vs. answer-content) and its implications for gap interpretation. The calibrated temporal ICG framework is unique in combining all five.

## Approach
We propose the Information-Contribution Gap (ICG) framework: a calibrated, temporally-resolved diagnostic that measures the divergence between information available in hidden states and information that causally contributes to model outputs, tracked across the full chain-of-thought generation trajectory.

**Formal Framework.** Define two time-varying quantities at each token position t during CoT generation:

(i) *Calibrated Information Availability* P*(t): Cross-validated AUROC of a linear probe on layer-l hidden states at position t, calibrated via null-probe normalization (P*(t) = P(t) − P_null(t), following Hewitt & Liang 2019 selectivity, where P_null is trained on shuffled labels). **Probe target: correctness (right/wrong).** We choose correctness over answer-content for three reasons: (a) broader applicability — correctness probes generalize beyond binary/MC tasks (Cox et al.'s answer-content probes are limited to binary A/B on 4 tasks), while correctness probes (Yuan et al.) work across model families up to 72B; (b) the 'diagnostic not causal' finding that motivates the entire framework is specifically about correctness probes (Yuan et al.'s four-intervention failure on correctness probes); (c) correctness gaps are more directly interpretable for faithfulness — G*(t) >> 0 means 'the model's hidden states encode awareness that its answer is right/wrong, but its CoT does not causally reflect this self-monitoring.' On binary/MC task subsets, we additionally train answer-content probes to test whether the 'what answer' gap differs from the 'whether correct' gap — a supplementary analysis testing whether pre-CoT encoding operates on content or meta-cognition. This measures excess correctness awareness above correlative features. We probe at layers L/4, L/2, 3L/4, L to capture layer-wise dynamics. MCT geometric validation (Chun et al. 2602.20338) on 500 examples confirms whether calibrated probe signal reflects geometrically organized information rather than mere retrievability. Note: Chrabąszcz et al. (2605.18549) demonstrate that probe trajectories with 60+ signal-processing features substantially outperform static probes (up to 17pp on GSM8K). We adopt their insight that temporal dynamics are essential, while adding null-probe calibration (which they lack) and extending to the dual-estimator gap. Where applicable, we incorporate their feature categories (volatility, trend, steady-state, boundary transients) as additional trajectory descriptors for phenomenon classification in Phase 3.

(ii) *Causal Contribution* C(t): The causal contribution of CoT up to position t, estimated via three complementary methods: (a) prefix-truncation ablation — measuring P(correct | CoT[:t]) vs. P(correct | full CoT), following Ballon et al.'s (2601.23163) truncation-reinjection protocol with their three control conditions (random tokens, swapped traces, shuffled tokens) to validate that C(t) measures genuine sequential content contribution rather than context-length effects (their finding: shuffled tokens retain +0.3-10.8% vs. intact +18.1-33.1%); (b) paraphrase perturbation — replacing CoT segments with meaning-preserving paraphrases and measuring answer stability; (c) NLDD-based influence scoring (Ye et al. 2602.11201) — measuring how corruption at position t degrades the answer distribution. Using multiple C(t) estimators provides robustness against single-method artifacts, following Young's (2603.20172) finding that faithfulness measurements are classifier-sensitive.

**The Information-Contribution Gap.** G*(t) = P*(t) − C(t). This gap is the primary diagnostic signal:
- G*(t) ≈ 0: Correctness awareness and causal contribution are aligned (necessary for faithfulness)
- G*(t) >> 0: The model encodes correctness awareness it does not causally use in its CoT (diagnostic excess — the model 'knows but doesn't use')
- G*(t) < 0: The CoT contributes to correctness beyond what hidden states encode at that point (information assembled during reasoning)

Because P*(t) is null-probe-calibrated, uniform correlative inflation is removed. C(t) is not subject to probe inflation as it measures behavioral change under intervention. The gap G*(t) is interpretable as 'calibrated correctness awareness the model has but doesn't channel through its CoT at position t.' Following Wang's (2604.15726) H1/H2 framework: G*(t) >> 0 is H1-consistent (latent-mediated reasoning), G*(t) ≈ 0 is H2-consistent (CoT-mediated reasoning).

**Phenomenon Signature Predictions (2-3 confident, 4-5 stretch).** We ground predictions in real probe data but adopt honest scoping informed by the concern that cross-study heterogeneity may overestimate separability:

*Primary targets (HIGH confidence, validated in Phase 0b pilot):*
(i) *Pre-CoT encoding*: G*(t) starts high and stays high. Grounded in: David's 0.84 AUC at t=4, Esakkiraja's >90% pre-generation AUROC, Cox's >0.9 pre-CoT AUC. P*(0) > 0.5 (after calibration), C(t) rises slowly. Shape: large constant gap.
(ii) *Genuine multi-step reasoning*: G*(t) converges toward zero. Grounded in: Zhang et al.'s 65%→79% chunk trajectory, Li et al.'s finding that hard→faithful, Ballon et al.'s monotonic accuracy increase with reasoning length. P*(t) rises gradually, C(t) tracks P*(t). Shape: co-rising curves, small/decreasing gap.
(iii) *Post-hoc rationalization*: G*(t) starts moderate, rises during CoT. P*(t) stable (David: ~0.80 from t=4 through t=100), C(t) remains flat despite token generation. Shape: widening gap.

*Stretch targets (MODERATE confidence, require additional features):*
(iv) *Steganographic encoding*: G*(t) dip-and-recovery. Potentially consistent with Esakkiraja's dip at 5-10%. May require multi-layer analysis to separate from noise.
(v) *Reasoning Theater*: EMPIRICAL QUESTION. Under non-uniform inflation, may overlap with pre-CoT encoding or post-hoc rationalization. Additional features — layer-wise P*(t) distribution, C(t) variance under paraphrase perturbation, Chrabąszcz-style signal features (autocorrelation, boundary transients, dwell-time run-lengths) — may enable separation. Whether Theater is cleanly separable is reported honestly with confusion matrices.

**Semi-Synthetic Simulation (hypothesis generation, NOT validation).** We construct semi-synthetic G*(t) curves grounded in real published data to generate testable predictions about trajectory-shape separability — but we do NOT treat this as evidence of real-data separability (published measurements come from different models, datasets, and setups, introducing heterogeneity that does not match within-dataset variance). Instead, the simulation identifies: (a) which trajectory features are most discriminative in principle, (b) what minimum effect sizes real-data classification needs to achieve, (c) where non-uniform inflation causes theoretical overlap between phenomena. I_probe(t) profiles drawn from published measurements (David, Zhang, Esakkiraja, Yuan), C(t) profiles modeled from NLDD (Ye et al.) and TTS (Zhao et al.) data, non-uniform inflation calibrated against Chun et al.'s MCT finding. The real validation comes from Phase 0b.

**Phase 0a: Gap Characterization (Weeks 1-2.5).** Three objectives on 500 examples × 3 datasets (GSM8K, MATH-500, MMLU) × 3 models (DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct):
(i) Construct empirical P*(t) and C(t) curves at token-level resolution
(ii) Validate null-probe calibration: P_null(t) shows high accuracy (inflation exists) but P*(t) shows meaningful variance (calibration reveals structure)
(iii) Characterize causal potency: following Cox et al.'s protocol, measure answer flip rates via probe-direction steering on reasoning vs. instruction-tuned models

Expected outcome (base case): Causal potency is low on reasoning models, confirming the diagnostic-not-causal property and validating the ICG framework's interpretive power. If causal potency is unexpectedly high, this is an exciting upgrade. Either outcome is scientifically valuable.

**Phase 0b: Empirical Pilot for Phenomenon Separability (Weeks 2.5-4).** This phase validates that trajectory-shape classification is feasible on real data before committing to the full pipeline. On the SAME model (R1-Distill-Qwen-7B) and datasets (GSM8K + MATH-500, 1000 examples), construct real G*(t) curves and test whether at least 2 phenomena produce distinguishable trajectories. Protocol: (i) partition examples by difficulty quintile and model behavior (easy-correct with high P*(0) → pre-CoT encoding candidates; hard-correct with rising P*(t) tracking C(t) → genuine reasoning candidates; incorrect with stable P*(t) and flat C(t) → post-hoc rationalization candidates); (ii) compute full G*(t) for each partition; (iii) test effect size d > 0.5 on at least 2 trajectory features between partitions. Apply Gjølbye et al.'s (2605.15454) length correction (residualizing trajectory features on log(N)) to ensure differences are not conflated with generation-length effects. Success criterion: d > 0.5 between at least 2 partitions on 2+ features. If d < 0.3 across all features, downscope to a characterization paper (gap exists and varies with difficulty, but trajectory shapes are not cleanly phenotypic) — still a strong contribution given no prior full-timeline G*(t) measurement exists.

**Phase 1: Full ICG Construction (Weeks 4-9).** Conditional on Phase 0b showing separability (d > 0.5). Extend to 4 models (add QwQ-32B or R1-Distill-32B) × 4 benchmarks (add GPQA-Diamond or AIME). Full calibrated P*(t) with null-probe normalization + MCT concordance check on 500 examples. Three C(t) estimators with Ballon et al.-style controls (random, swap, shuffle baselines). Cross-reference with TTS (Zhao et al.) at step boundaries. Bootstrap confidence intervals on G*(t).

**Phase 2: Task-Difficulty Conditioning (Weeks 7-11).** Partition each benchmark into difficulty quintiles (using model accuracy as proxy). Measure G*(t) per quintile. Hypothesis grounded in David's easy/hard data, Li et al.'s finding, and Gjølbye et al.'s difficulty-geometry coupling: easy problems show large persistent gap (decorative CoT), hard problems show converging gap (load-bearing CoT). Following Gjølbye et al., apply length correction and report domain-specific effects — expecting stronger effects on math/code benchmarks than MMLU, given their finding of ρ⊥ = +0.41 on Codeforces vs. +0.05 on MATH. The transition point — where G*(t) shifts from decorative to genuine — provides practical guidance on when CoT adds value.

**Phase 3: Phenomenon Classification and Robustness (Weeks 9-14).** Apply trajectory-shape classification to real data. Target: 2-3 cleanly separable phenomena, with 4-5 reported honestly including overlap. Incorporate Chrabąszcz et al.'s feature categories (volatility, trend, boundary transients, autocorrelation) alongside our gap-specific features (initial G* value, G* slope, convergence rate, dC/dt locality). Six robustness ablations following Young (2603.20172): (a) probe architecture (linear vs. 2-layer MLP) with selectivity; (b) layer selection (single best vs. multi-layer); (c) C(t) estimator agreement (prefix vs. paraphrase vs. NLDD); (d) gap normalization method; (e) calibration method (shuffled-label vs. random-representation); (f) probe target (correctness vs. answer-content on binary/MC subsets). Report sensitivity ranges across all dimensions.

**TIF Score.** Temporal Information-contribution Faithfulness score: normalized area under calibrated G*(t), benchmarked against FaithCoT-Bench and Liu et al.'s text-level metrics.

**Paper Focus (Tightened).** Core contributions: (1) calibrated ICG diagnostic with explicitly justified correctness-probe target on 4 models × 4 benchmarks, positioned against Chrabąszcz et al.'s probe trajectories — demonstrating the value added by the causal contribution dimension and gap metric; (2) Phase 0b empirical pilot validating that 2-3 phenomena produce distinguishable G*(t) signatures on real within-model, within-dataset data; (3) task-difficulty conditioning revealing the decorative→load-bearing transition with domain-specific strength following Gjølbye et al.'s nuance. Supporting: robustness ablations (6 dimensions); TIF validation. Supplementary: 671B subset (500 examples, 3 layers); answer-content vs. correctness probe comparison; semi-synthetic simulation as hypothesis generation.

**Experiments.** DeepSeek-R1-Distill-Qwen-7B/14B/32B, QwQ-32B across MMLU, GPQA-Diamond, GSM8K, AIME. 671B validation (500-example subset, 3 layers). Calibration checks: synthetic arithmetic (G* ≈ 0 expected), TTS cross-reference, MCT cross-reference. Gjølbye-style length correction on all temporal analyses.

## Resource Estimate
{'manual': {'gpu_hours': '~830 H100-hours (Phase 0a characterization: 80 hrs [3 models × 3 datasets, probe training + prefix ablation + steering tests]; Phase 0b empirical pilot: 30 hrs [1 model × 2 datasets, full G*(t) construction + partition analysis + length correction]; Phase 1 full ICG: 120 hrs [4 models × 4 benchmarks, multi-layer probes + 3 C(t) estimators]; Phase 2 difficulty conditioning: 50 hrs; Phase 3 phenomenon classification + robustness ablations: 50 hrs; NLDD on 32B model: 250 hrs [primary bottleneck — up to 20 perturbation positions × 5K examples × forward passes]; NLDD on 7B/14B models: 100 hrs; MCT geometric validation: 50 hrs; 671B subset: 50 hrs [8×H100]; semi-synthetic simulation: 50 hrs [mostly CPU, some GPU for validation])', 'timeline': '15-17 weeks (2 researchers: 4 weeks Phase 0a+0b characterization + pilot; 5 weeks Phase 1 full ICG; 4 weeks Phases 2-3 in parallel with NLDD; 2-3 weeks writing + ablations)', 'estimated_gpu_cost': '$2,500 at ~$3/H100-hour (cloud spot pricing)', 'storage': '3-5 TB (4 layers per model, fp16); reducible to ~1.5 TB via PCA'}, 'human_in_loop': {'gpu_hours': '~830 H100-hours', 'timeline': '13 weeks (1 researcher + Claude for experiment design and analysis)', 'claude_api_cost': '$350', 'estimated_gpu_cost': '$2,500'}, 'auto_research': {'gpu_hours': '~830 H100-hours', 'timeline': '11 weeks', 'claude_api_cost': '$700', 'estimated_gpu_cost': '$2,500', 'speed_bottleneck': 'NLDD on 32B (~250 H100-hours, ~30% of total compute) is the primary bottleneck. Each NLDD evaluation requires corrupting reasoning at multiple positions and measuring logit degradation — O(T × N) forward passes where T≈20 perturbation positions and N≈5K examples. For 32B models, this cannot be easily parallelized beyond 8-GPU data parallelism. Secondary: 671B subset (8×H100, ~50 hrs); MCT geometric validation (~50 hrs). Phase 0b pilot (30 hrs) provides early go/no-go signal before committing full Phase 1-3 compute.'}}

## Inspired By
The convergence of five independent lines of evidence — (a) Cox et al.'s finding that answer-content probe steering fails on reasoning models despite high accuracy; (b) Yuan et al.'s systematic demonstration that four interventions all fail on correctness probes, establishing 'diagnostic not causal'; (c) the temporal probe dynamics now empirically characterized by David (0.84 AUC at t=4, stable ~0.8), Zhang et al. (chunk-level rising trajectory), Esakkiraja et al. (pre-generation >90% with dip-recovery), and Chrabąszcz et al. (60+ trajectory features capturing dynamics invisible to static probes, up to 17pp improvement); (d) Ballon et al.'s truncation-reinjection protocol demonstrating monotonic behavioral C(t) curves with rigorous controls (sequential content +18.1-33.1% vs. shuffled +0.3-10.8%) — all pointing to the same insight: the gap between diagnostic information availability and causal contribution IS the phenomenon of interest. Additionally inspired by: Wang's (2604.15726) formalization of H1/H2/H0 hypotheses providing the theoretical scaffold for what our framework empirically measures; Gjølbye et al.'s (2605.15454) finding that difficulty-geometry coupling is domain-specific and requires length correction; Herrmann et al.'s concurrent temporal persona-vector dynamics; and the trajectory-shape literature showing shapes can distinguish phenomena regardless of absolute-value calibration.

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
  "promptId": "c0380e88-a16d-43cf-a4b7-4aee5f2af40b",
  "type": "user",
  "uuid": "54a6034f-5ebb-423b-b475-fc483c396122",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T03:48:14.914Z_

```json
{
  "parentUuid": "54a6034f-5ebb-423b-b475-fc483c396122",
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
  "uuid": "12b87278-281a-41e9-8b9d-81d17f587977",
  "timestamp": "2026-05-20T03:48:14.914Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T03:48:14.915Z_

```json
{
  "parentUuid": "12b87278-281a-41e9-8b9d-81d17f587977",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1ee880c9-cc5f-48b5-be98-eb6241badedf",
  "timestamp": "2026-05-20T03:48:14.915Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
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
  "leafUuid": "1ee880c9-cc5f-48b5-be98-eb6241badedf",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Measuring calibrated temporal information-contribution gaps in chain-of-thought reasoning",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b"
}
```

---

### Assistant

_source line 8 · 2026-05-20T03:48:26.103Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze this proposal as the "发掘 agent" (Discovery Agent). I need to:

1. First, do thorough literature searches to understand the current landscape
2. Assess the novelty, significance, and related work differentiation
3. Check for trivial alternatives and assumption validity
4. Provide concrete suggestions for strengthening the idea's ceiling

Let me start by reading the proposal carefully and then conducting targeted web searches.

The proposal is about measuring the "Information-Contribution Gap" (ICG) - the divergence between what models internally know (measured via probes on hidden states) and what their Chain-of-Thought (CoT) causally contributes. The key insight is that this gap IS the faithfulness signal.


The core findings show that linear probes can reliably detect answer correctness across a wide range of accuracy levels, but causal interventions on the same information don't produce corresponding effects. I'm tracking how this diagnostic-causal gap evolves over time as G*(t) = P*(t) - C(t), and different faithfulness phenomena appear to have distinct temporal patterns. The gap itself seems to be modulated by task difficulty—easier problems show decorative gaps while harder ones show load-bearing gaps. Now I need to search recent literature to properly contextualize these claims and identify what's genuinely novel here.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ee880c9-cc5f-48b5-be98-eb6241badedf",
  "isSidechain": false,
  "requestId": "req_011CbD8twtXDTzBcUWauCve9",
  "type": "assistant",
  "uuid": "6cfb719f-8d19-4e86-a3fd-3921d64768c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HqAWACRJAYBwN1NuRuPjL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16804,
      "cache_read_input_tokens": 11374,
      "output_tokens": 394,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16804,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 394,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 16804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16804
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

_source line 9 · 2026-05-20T03:48:26.108Z_

I'll start by carefully reading the proposal, then conduct targeted web searches to assess the novelty landscape before making any judgments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cfb719f-8d19-4e86-a3fd-3921d64768c0",
  "isSidechain": false,
  "requestId": "req_011CbD8twtXDTzBcUWauCve9",
  "type": "assistant",
  "uuid": "0b5f260b-3c8b-4817-83f8-a33c4883d971",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HqAWACRJAYBwN1NuRuPjL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16804,
      "cache_read_input_tokens": 11374,
      "output_tokens": 394,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16804,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 394,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 16804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16804
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

_source line 10 · 2026-05-20T03:48:26.116Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RvgqzdhhaacwjT9tVuoGie`</summary>

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
  "parentUuid": "0b5f260b-3c8b-4817-83f8-a33c4883d971",
  "isSidechain": false,
  "requestId": "req_011CbD8twtXDTzBcUWauCve9",
  "type": "assistant",
  "uuid": "2358af07-593c-4964-80e4-8a7548cd19c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HqAWACRJAYBwN1NuRuPjL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16804,
      "cache_read_input_tokens": 11374,
      "output_tokens": 394,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16804,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 394,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 16804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16804
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

_source line 11 · 2026-05-20T03:48:26.122Z_

<details><summary>↩ Tool result · `toolu_01RvgqzdhhaacwjT9tVuoGie`</summary>

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
  "parentUuid": "2358af07-593c-4964-80e4-8a7548cd19c7",
  "isSidechain": false,
  "promptId": "c0380e88-a16d-43cf-a4b7-4aee5f2af40b",
  "type": "user",
  "uuid": "19ead819-afdc-4e04-94ab-8fe2064ae761",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "2358af07-593c-4964-80e4-8a7548cd19c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-20T03:48:29.178Z_

Now let me conduct the required pre-research searches. I'll run multiple targeted searches in parallel to cover the key dimensions of this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19ead819-afdc-4e04-94ab-8fe2064ae761",
  "isSidechain": false,
  "requestId": "req_011CbD8umpZvbXgu7aSpijhU",
  "type": "assistant",
  "uuid": "1cac483c-7e0c-4852-bfb3-78bb5ef4f41d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A15VDrYzSm1N5Zq1dKXSMk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 921,
      "cache_read_input_tokens": 28178,
      "output_tokens": 100,
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
          "input_tokens": 3,
          "output_tokens": 100,
          "cache_read_input_tokens": 28178,
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

### Tool call

_source line 13 · 2026-05-20T03:48:29.814Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JA9hYLmBU1YJvccJc35k4C`</summary>

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
  "parentUuid": "1cac483c-7e0c-4852-bfb3-78bb5ef4f41d",
  "isSidechain": false,
  "requestId": "req_011CbD8umpZvbXgu7aSpijhU",
  "type": "assistant",
  "uuid": "83a66080-afcf-4deb-9f33-26ff9c240a70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A15VDrYzSm1N5Zq1dKXSMk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 921,
      "cache_read_input_tokens": 28178,
      "output_tokens": 100,
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
          "input_tokens": 3,
          "output_tokens": 100,
          "cache_read_input_tokens": 28178,
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

_source line 14 · 2026-05-20T03:48:37.457Z_

<details><summary>↩ Tool result · `toolu_01JA9hYLmBU1YJvccJc35k4C`</summary>

```text
Web search results for query: "chain-of-thought faithfulness probing causal intervention gap 2025 2026"

Links: [{"title":"Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models","url":"https://arxiv.org/html/2603.26410"},{"title":"Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING","url":"https://openreview.net/attachment?id=lN3yKqqzF1&name=pdf"},{"title":"Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning | Request PDF","url":"https://www.researchgate.net/publication/386203451_Making_Reasoning_Matter_Measuring_and_Improving_Faithfulness_of_Chain-of-Thought_Reasoning"},{"title":"FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness","url":"https://arxiv.org/pdf/2509.13334"},{"title":"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures","url":"https://arxiv.org/html/2603.16475v1"},{"title":"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps","url":"https://arxiv.org/html/2502.14829v3"},{"title":"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2602.11201v1"},{"title":"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures | OpenReview","url":"https://openreview.net/forum?id=yfqHr7l2tG"}]

Based on the search results, I found several recent papers addressing chain-of-thought (CoT) faithfulness, probing methods, and causal interventions from 2025-2026:

## Key Research Findings

**Causal Intervention Approaches:**
Studies have used causal interventions (truncating, corrupting, and paraphrasing CoTs) to show that models can arrive at correct answers even when their stated reasoning is disrupted, suggesting CoT can be post-hoc rationalization rather than genuine computation.

**Mechanistic Insights:**
Recent work identified a "Reasoning Horizon" at 70–85% of chain length, beyond which reasoning tokens have diminishing causal influence on the final answer. Additionally, models often commit to answers early in the reasoning chain, with subsequent tokens serving a performative rather than computational role.

**Systematic Gap in Faithfulness:**
Across nine models and four benchmarks with annotated intermediates, research reveals a systematic gap: while models rely on structures more than the original text (>60% consistency under interventions to original prompt), they fail to update under logically significant structural edits more than 50% of the time.

**Monitoring Frameworks:**
A complete monitoring pipeline requires at minimum three tiers: answer-text screening (catches transparent cases), thinking-token screening (catches the divergence-pattern cases), and activation-level or probe-based monitoring (needed for unacknowledged cases).

**Recent Methodological Work:**
Faithful Reasoning via Intervention Training (FRIT) is a scalable method for improving CoT faithfulness without human supervision that uses causality of CoT steps to fine-tune for more faithful outputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83a66080-afcf-4deb-9f33-26ff9c240a70",
  "isSidechain": false,
  "promptId": "c0380e88-a16d-43cf-a4b7-4aee5f2af40b",
  "type": "user",
  "uuid": "29e70314-166a-4057-a64b-e1e582cb2855",
  "toolUseResult": {
    "query": "chain-of-thought faithfulness probing causal intervention gap 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FfWHoyh4F6iiyLedjttEwi",
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
      "Based on the search results, I found several recent papers addressing chain-of-thought (CoT) faithfulness, probing methods, and causal interventions from 2025-2026:\n\n## Key Research Findings\n\n**Causal Intervention Approaches:**\nStudies have used causal interventions (truncating, corrupting, and paraphrasing CoTs) to show that models can arrive at correct answers even when their stated reasoning is disrupted, suggesting CoT can be post-hoc rationalization rather than genuine computation.\n\n**Mechanistic Insights:**\nRecent work identified a \"Reasoning Horizon\" at 70–85% of chain length, beyond which reasoning tokens have diminishing causal influence on the final answer. Additionally, models often commit to answers early in the reasoning chain, with subsequent tokens serving a performative rather than computational role.\n\n**Systematic Gap in Faithfulness:**\nAcross nine models and four benchmarks with annotated intermediates, research reveals a systematic gap: while models rely on structures more than the original text (>60% consistency under interventions to original prompt), they fail to update under logically significant structural edits more than 50% of the time.\n\n**Monitoring Frameworks:**\nA complete monitoring pipeline requires at minimum three tiers: answer-text screening (catches transparent cases), thinking-token screening (catches the divergence-pattern cases), and activation-level or probe-based monitoring (needed for unacknowledged cases).\n\n**Recent Methodological Work:**\nFaithful Reasoning via Intervention Training (FRIT) is a scalable method for improving CoT faithfulness without human supervision that uses causality of CoT steps to fine-tune for more faithful outputs."
    ],
    "durationSeconds": 7.6352823590000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "83a66080-afcf-4deb-9f33-26ff9c240a70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T03:48:43.288Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DhDwxRm43r69zcv1nGNWnC`</summary>

```json
{
  "query": "Chrabąszcz probe trajectories reasoning dynamics 2605.18549 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29e70314-166a-4057-a64b-e1e582cb2855",
  "isSidechain": false,
  "requestId": "req_011CbD8vc7wq3UzpbU5hMe4c",
  "type": "assistant",
  "uuid": "50d1c860-a8f3-420f-86f3-0a0e6d90621f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ry9yzZ4EeXiuWagdrSDwEj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 29099,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 951,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 29099,
          "cache_creation_input_tokens": 951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 951
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

_source line 16 · 2026-05-20T03:48:50.399Z_

<details><summary>↩ Tool result · `toolu_01DhDwxRm43r69zcv1nGNWnC`</summary>

```text
Web search results for query: "Chrabąszcz probe trajectories reasoning dynamics 2605.18549 2026"

Links: [{"title":"[2605.18549] Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics","url":"https://arxiv.org/abs/2605.18549"},{"title":"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics","url":"https://arxiv.org/html/2605.18549"},{"title":"Reasoning emerges from constrained inference manifolds in large language models","url":"https://arxiv.org/html/2605.08142"},{"title":"Spatiotemporal Hidden-State Dynamics as a Signature of Internal Reasoning in Large Language Models","url":"https://arxiv.org/html/2605.01853"},{"title":"[2605.01853] Spatiotemporal Hidden-State Dynamics as a Signature of Internal Reasoning in Large Language Models","url":"https://arxiv.org/abs/2605.01853"},{"title":"Trajectory sampling using spatial familiarity","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11435202"},{"title":"The Effect of Probe Dynamics on Galactic Exploration Timescales","url":"https://arxiv.org/pdf/1212.2371"}]

Based on the search results, I found the paper you're looking for:

arXiv paper 2605.18549, titled "Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics," was submitted on May 18, 2026, by authors including Maciej Chrabąszcz and colleagues.

The paper investigates hidden representations of Large Reasoning Models (LRMs) to determine whether future behavior can be predicted from prompt and Chain of Thought representations, and by evaluating a probe at each generated token, they construct a probe trajectory—the continuous evolution of a concept's probability across the reasoning process.

The key findings show that future model behavior is more distinguishable when examined over the full trajectory than from a single static prediction, and the authors extract signal-processing features that capture volatility, trend, and steady-state behavior to characterize these temporal dynamics.

Among their methodological insights, they found that the choice of pooling operation is critical: max-pooling achieves up to 95% AUROC and yields stable probe trajectories.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50d1c860-a8f3-420f-86f3-0a0e6d90621f",
  "isSidechain": false,
  "promptId": "c0380e88-a16d-43cf-a4b7-4aee5f2af40b",
  "type": "user",
  "uuid": "f880ae33-08b3-416e-96e2-8ce854f106b2",
  "toolUseResult": {
    "query": "Chrabąszcz probe trajectories reasoning dynamics 2605.18549 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KYTysU268dWCEBmRy5Vrro",
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
      "Based on the search results, I found the paper you're looking for:\n\narXiv paper 2605.18549, titled \"Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics,\" was submitted on May 18, 2026, by authors including Maciej Chrabąszcz and colleagues.\n\nThe paper investigates hidden representations of Large Reasoning Models (LRMs) to determine whether future behavior can be predicted from prompt and Chain of Thought representations, and by evaluating a probe at each generated token, they construct a probe trajectory—the continuous evolution of a concept's probability across the reasoning process.\n\nThe key findings show that future model behavior is more distinguishable when examined over the full trajectory than from a single static prediction, and the authors extract signal-processing features that capture volatility, trend, and steady-state behavior to characterize these temporal dynamics.\n\nAmong their methodological insights, they found that the choice of pooling operation is critical: max-pooling achieves up to 95% AUROC and yields stable probe trajectories."
    ],
    "durationSeconds": 7.105741622000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "50d1c860-a8f3-420f-86f3-0a0e6d90621f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T03:48:53.095Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FXYW1Q3rLjcSSJfKoBeac2`</summary>

```json
{
  "query": "Yuan et al \"diagnostic not causal\" hidden error awareness reasoning models intervention failure 2605.09502"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f880ae33-08b3-416e-96e2-8ce854f106b2",
  "isSidechain": false,
  "requestId": "req_011CbD8wZSVRZ1Ru4DbkFBTA",
  "type": "assistant",
  "uuid": "1a272ff9-3edf-45a8-84e3-1c26e47a87fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CyS1MYWmW274thXQmJ6FMT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 671,
      "cache_read_input_tokens": 30050,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 30050,
          "cache_creation_input_tokens": 671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 671
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

_source line 18 · 2026-05-20T03:49:01.282Z_

<details><summary>↩ Tool result · `toolu_01FXYW1Q3rLjcSSJfKoBeac2`</summary>

```text
Web search results for query: "Yuan et al "diagnostic not causal" hidden error awareness reasoning models intervention failure 2605.09502"

Links: [{"title":"[2605.09502] Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal","url":"https://arxiv.org/abs/2605.09502"},{"title":"Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal","url":"https://arxiv.org/html/2605.09502"},{"title":"[2605.06059] Correcting heterogeneous diagnostic bias when developing clinical prediction models using causal hidden Markov models","url":"https://arxiv.org/abs/2605.06059"},{"title":"Hop, Skip, and Overthink: Diagnosing Why Reasoning Models Fumble during Multi-Hop Analysis","url":"https://arxiv.org/pdf/2508.04699"},{"title":"Automation Bias in Large Language Model Assisted Diagnostic Reasoning Among AI-Trained Physicians","url":"https://www.medrxiv.org/content/10.1101/2025.08.23.25334280.full.pdf"},{"title":"How Well Can Reasoning Models Identify and Recover from Unhelpful Thoughts?","url":"https://arxiv.org/pdf/2506.10979"}]

I found the paper! Here's a summary of the key findings from Yuan et al. (arXiv:2605.09502):

## Hidden Error Awareness in Chain-of-Thought Reasoning

The paper challenges the assumption that chain-of-thought reasoning reflects a model's internal computation, showing that models internally detect their own reasoning errors but outwardly express confidence in them.

### Key Findings:

**Detection Without Expression:**
A linear probe on hidden states predicts trace correctness with 0.95 AUROC from the very first reasoning step (0.79), while verbalized confidence for wrong traces is 4.55/5, nearly identical to correct ones (4.87/5). A text-surface classifier achieves only 0.59 on the same data, confirming a gap invisible in the generated text.

**Generality Across Models:**
This hidden error awareness holds across three model families (Qwen, Llama, Phi), ranging from 1.5B-72B parameters, and RL-trained reasoning models (DeepSeek-R1, 0.852 AUROC).

**Intervention Failure:**
Four interventions—activation steering, probe-guided best-of-N, self-correction, and activation patching—all fail, and the signal is diagnostic, not causal: a readout of computation quality, not a lever to redirect it.

This delineates a boundary for mechanistic interpretability: error representations during reasoning are fundamentally different from the factual knowledge representations that prior work has successfully edited.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a272ff9-3edf-45a8-84e3-1c26e47a87fb",
  "isSidechain": false,
  "promptId": "c0380e88-a16d-43cf-a4b7-4aee5f2af40b",
  "type": "user",
  "uuid": "24227b17-600e-4f4c-af2f-10a4b42243ce",
  "toolUseResult": {
    "query": "Yuan et al \"diagnostic not causal\" hidden error awareness reasoning models intervention failure 2605.09502",
    "results": [
      {
        "tool_use_id": "srvtoolu_015cFeJJLSzuqsEGAQDvpwAT",
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
            "title": "[2605.06059] Correcting heterogeneous diagnostic bias when developing clinical prediction models using causal hidden Markov models",
            "url": "https://arxiv.org/abs/2605.06059"
          },
          {
            "title": "Hop, Skip, and Overthink: Diagnosing Why Reasoning Models Fumble during Multi-Hop Analysis",
            "url": "https://arxiv.org/pdf/2508.04699"
          },
          {
            "title": "Automation Bias in Large Language Model Assisted Diagnostic Reasoning Among AI-Trained Physicians",
            "url": "https://www.medrxiv.org/content/10.1101/2025.08.23.25334280.full.pdf"
          },
          {
            "title": "How Well Can Reasoning Models Identify and Recover from Unhelpful Thoughts?",
            "url": "https://arxiv.org/pdf/2506.10979"
          }
        ]
      },
      "I found the paper! Here's a summary of the key findings from Yuan et al. (arXiv:2605.09502):\n\n## Hidden Error Awareness in Chain-of-Thought Reasoning\n\nThe paper challenges the assumption that chain-of-thought reasoning reflects a model's internal computation, showing that models internally detect their own reasoning errors but outwardly express confidence in them.\n\n### Key Findings:\n\n**Detection Without Expression:**\nA linear probe on hidden states predicts trace correctness with 0.95 AUROC from the very first reasoning step (0.79), while verbalized confidence for wrong traces is 4.55/5, nearly identical to correct ones (4.87/5). A text-surface classifier achieves only 0.59 on the same data, confirming a gap invisible in the generated text.\n\n**Generality Across Models:**\nThis hidden error awareness holds across three model families (Qwen, Llama, Phi), ranging from 1.5B-72B parameters, and RL-trained reasoning models (DeepSeek-R1, 0.852 AUROC).\n\n**Intervention Failure:**\nFour interventions—activation steering, probe-guided best-of-N, self-correction, and activation patching—all fail, and the signal is diagnostic, not causal: a readout of computation quality, not a lever to redirect it.\n\nThis delineates a boundary for mechanistic interpretability: error representations during reasoning are fundamentally different from the factual knowledge representations that prior work has successfully edited."
    ],
    "durationSeconds": 8.183953878,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1a272ff9-3edf-45a8-84e3-1c26e47a87fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T03:49:03.847Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pp2XUGDedUCqMFB7Tbn6KA`</summary>

```json
{
  "query": "information contribution gap temporal probe causal faithfulness framework CoT 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24227b17-600e-4f4c-af2f-10a4b42243ce",
  "isSidechain": false,
  "requestId": "req_011CbD8xMvyGAJkVC14VbG9T",
  "type": "assistant",
  "uuid": "74a86e66-855b-4caf-97cb-215303cb188c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T4K52P7haU64j6XRcfemEt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 779,
      "cache_read_input_tokens": 30721,
      "output_tokens": 66,
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
          "output_tokens": 66,
          "cache_read_input_tokens": 30721,
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

_source line 20 · 2026-05-20T03:49:12.807Z_

<details><summary>↩ Tool result · `toolu_01Pp2XUGDedUCqMFB7Tbn6KA`</summary>

```text
Web search results for query: "information contribution gap temporal probe causal faithfulness framework CoT 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING","url":"https://arxiv.org/pdf/2510.04040"},{"title":"Evaluating Reasoning Faithfulness in Medical Vision-Language Models using Multimodal Perturbations","url":"https://arxiv.org/html/2510.11196"},{"title":"FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2510.04040v1"},{"title":"A Causal Lens for Evaluating Faithfulness Metrics","url":"https://arxiv.org/html/2502.18848v3"},{"title":"Bypassing the Rationale: Causal Auditing of Implicit Reasoning in Language Models","url":"https://arxiv.org/pdf/2602.03994"},{"title":"Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents","url":"https://arxiv.org/html/2601.02314v1"},{"title":"Causal AI Decision Intelligence: Why It Will Emerge in 2026 - theCUBE Research","url":"https://thecuberesearch.com/why-causal-ai-decision-intelligence-2026/"},{"title":"Causal-INSIGHT: Probing Temporal Models to Extract Causal Structure","url":"https://arxiv.org/pdf/2603.25473"}]

Based on the search results, I found several relevant research papers and frameworks from 2026 related to causal faithfulness and Chain-of-Thought (CoT) reasoning:

## Key Findings:

**FaithCoT-Bench and CoT Faithfulness Evaluation:**
Studies have examined the faithfulness of CoT, a key concept in interpretability that assesses whether an explanation aligns with the model's actual reasoning or decision-making process. Approaches probe CoT faithfulness by perturbing reasoning traces, for example by adding mistakes, removing steps, or forcing early answers, and then testing whether the final prediction changes accordingly, with such causal sensitivity treated as evidence of faithfulness since a faithful CoT should preserve a causal link between intermediate steps and the final answer.

**Logit-Based and Information Contribution Methods:**
Some studies leverage model-internal diagnostics, such as analyzing logit variations or measuring information gain to approximate causal alignment between CoTs and outputs.

**Causal Auditing Frameworks:**
A CoT-specific metric (CMI) was introduced to test whether models mechanistically rely on CoT, and a causal, layerwise auditing framework measures whether answers are mechanistically mediated by CoT-aligned internal representations, quantified using the CoT Mediation Index (CMI).

**Temporal Causal Analysis:**
Causal-INSIGHT is a model-agnostic, post-hoc interpretation framework for extracting model-implied, directed, time-lagged influence structure from trained temporal predictors.

The search results indicate this is an active research area in 2026, with multiple frameworks addressing the "faithfulness gap" in AI reasoning systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74a86e66-855b-4caf-97cb-215303cb188c",
  "isSidechain": false,
  "promptId": "c0380e88-a16d-43cf-a4b7-4aee5f2af40b",
  "type": "user",
  "uuid": "5e6df68a-522b-46a5-b0f6-d76ba75a6616",
  "toolUseResult": {
    "query": "information contribution gap temporal probe causal faithfulness framework CoT 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SpjaCF1zwBcsgUR4zXwKC5",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING",
            "url": "https://arxiv.org/pdf/2510.04040"
          },
          {
            "title": "Evaluating Reasoning Faithfulness in Medical Vision-Language Models using Multimodal Perturbations",
            "url": "https://arxiv.org/html/2510.11196"
          },
          {
            "title": "FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2510.04040v1"
          },
          {
            "title": "A Causal Lens for Evaluating Faithfulness Metrics",
            "url": "https://arxiv.org/html/2502.18848v3"
          },
          {
            "title": "Bypassing the Rationale: Causal Auditing of Implicit Reasoning in Language Models",
            "url": "https://arxiv.org/pdf/2602.03994"
          },
          {
            "title": "Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents",
            "url": "https://arxiv.org/html/2601.02314v1"
          },
          {
            "title": "Causal AI Decision Intelligence: Why It Will Emerge in 2026 - theCUBE Research",
            "url": "https://thecuberesearch.com/why-causal-ai-decision-intelligence-2026/"
          },
          {
            "title": "Causal-INSIGHT: Probing Temporal Models to Extract Causal Structure",
            "url": "https://arxiv.org/pdf/2603.25473"
          }
        ]
      },
      "Based on the search results, I found several relevant research papers and frameworks from 2026 related to causal faithfulness and Chain-of-Thought (CoT) reasoning:\n\n## Key Findings:\n\n**FaithCoT-Bench and CoT Faithfulness Evaluation:**\nStudies have examined the faithfulness of CoT, a key concept in interpretability that assesses whether an explanation aligns with the model's actual reasoning or decision-making process. Approaches probe CoT faithfulness by perturbing reasoning traces, for example by adding mistakes, removing steps, or forcing early answers, and then testing whether the final prediction changes accordingly, with such causal sensitivity treated as evidence of faithfulness since a faithful CoT should preserve a causal link between intermediate steps and the final answer.\n\n**Logit-Based and Information Contribution Methods:**\nSome studies leverage model-internal diagnostics, such as analyzing logit variations or measuring information gain to approximate causal alignment between CoTs and outputs.\n\n**Causal Auditing Frameworks:**\nA CoT-specific metric (CMI) was introduced to test whether models mechanistically rely on CoT, and a causal, layerwise auditing framework measures whether answers are mechanistically mediated by CoT-aligned internal representations, quantified using the CoT Mediation Index (CMI).\n\n**Temporal Causal Analysis:**\nCausal-INSIGHT is a model-agnostic, post-hoc interpretation framework for extracting model-implied, directed, time-lagged influence structure from trained temporal predictors.\n\nThe search results indicate this is an active research area in 2026, with multiple frameworks addressing the \"faithfulness gap\" in AI reasoning systems."
    ],
    "durationSeconds": 8.955733263000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "74a86e66-855b-4caf-97cb-215303cb188c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
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
  "leafUuid": "5e6df68a-522b-46a5-b0f6-d76ba75a6616",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Measuring calibrated temporal information-contribution gaps in chain-of-thought reasoning",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b"
}
```

---

### Tool call

_source line 23 · 2026-05-20T03:49:15.308Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Af5Apjzi7NGE3KaHNvHg9D`</summary>

```json
{
  "query": "combining probing hidden states causal contribution reasoning faithfulness temporal trajectory 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e6df68a-522b-46a5-b0f6-d76ba75a6616",
  "isSidechain": false,
  "requestId": "req_011CbD8yDLKXcHXKzuVSiKRv",
  "type": "assistant",
  "uuid": "367bb142-208c-4c33-acda-576eca75076f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MLdURfDaetPGzHkdvMvxBK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 866,
      "cache_read_input_tokens": 31500,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 866,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 31500,
          "cache_creation_input_tokens": 866,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 866
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

_source line 24 · 2026-05-20T03:49:23.557Z_

<details><summary>↩ Tool result · `toolu_01Af5Apjzi7NGE3KaHNvHg9D`</summary>

```text
Web search results for query: "combining probing hidden states causal contribution reasoning faithfulness temporal trajectory 2026 arxiv"

Links: [{"title":"Temporal Predictors of Outcome in Reasoning Language Models","url":"https://arxiv.org/html/2511.14773"},{"title":"Bypassing the Rationale: Causal Auditing of Implicit Reasoning in Language Models","url":"https://arxiv.org/pdf/2602.03994"},{"title":"Streaming Hallucination Detection in Long Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2601.02170"},{"title":"Beyond Patterns: Harnessing Causal Logic for Autonomous Driving Trajectory Prediction","url":"https://arxiv.org/pdf/2505.06856"},{"title":"LLMs Faithfully and Iteratively Compute Answers During CoT: A Systematic Analysis With Multi-step Arithmetics","url":"https://arxiv.org/html/2412.01113"},{"title":"Combining Causal Models for More Accurate Abstractions of Neural   Networks","url":"https://arxiv.org/pdf/2503.11429"},{"title":"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/html/2604.15400v1"},{"title":"[2508.15928] Transforming Causality: Transformer-Based Temporal Causal Discovery with Prior Knowledge Integration","url":"https://arxiv.org/abs/2508.15928"}]

Based on the search results, I found several relevant papers related to your query. Here are the most notable ones:

1. **"Temporal Predictors of Outcome in Reasoning Language Models"** (November 2025, arXiv:2511.14773): This paper directly probes the model's hidden trajectory during reasoning without requiring extra decoding passes, predicting answer correctness from hidden states while chain-of-thought is being generated.

2. **"Bypassing the Rationale: Causal Auditing of Implicit Reasoning in Language Models"** (arXiv:2602.03994): This work introduces causal, layerwise intervention methods to test whether models mechanistically rely on chain-of-thought, with a framework that measures whether answers are mechanistically mediated by chain-of-thought-aligned internal representations.

3. **"Streaming Hallucination Detection in Long Chain-of-Thought Reasoning"** (January 2026, arXiv:2601.02170): This paper views hallucination in long chain-of-thought reasoning as a temporally evolving latent state, tracking the trajectory of hidden states throughout the reasoning process rather than treating them as isolated local errors.

4. **"LLMs Faithfully and Iteratively Compute Answers During CoT: A Systematic Analysis With Multi-step Arithmetics"** (March 2026, arXiv:2412.01113): This study combines probing results with causal intervention analyses to clarify the causal relationship between the model's internal representations and answers.

5. **"Combining Causal Models for More Accurate Abstractions of Neural Networks"** (arXiv:2503.11429): This paper explores reasoning about the faithfulness of causal analyses by modifying partially faithful causal models based on input-provided information to become more faithful.

These papers collectively address the intersection of probing hidden states, causal interventions, reasoning, faithfulness evaluation, and temporal dynamics in language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "367bb142-208c-4c33-acda-576eca75076f",
  "isSidechain": false,
  "promptId": "c0380e88-a16d-43cf-a4b7-4aee5f2af40b",
  "type": "user",
  "uuid": "7a6cffc6-8816-45c5-bae8-b02431d96d9d",
  "toolUseResult": {
    "query": "combining probing hidden states causal contribution reasoning faithfulness temporal trajectory 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PTPh8Mx82cwRicZz5XC98o",
        "content": [
          {
            "title": "Temporal Predictors of Outcome in Reasoning Language Models",
            "url": "https://arxiv.org/html/2511.14773"
          },
          {
            "title": "Bypassing the Rationale: Causal Auditing of Implicit Reasoning in Language Models",
            "url": "https://arxiv.org/pdf/2602.03994"
          },
          {
            "title": "Streaming Hallucination Detection in Long Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2601.02170"
          },
          {
            "title": "Beyond Patterns: Harnessing Causal Logic for Autonomous Driving Trajectory Prediction",
            "url": "https://arxiv.org/pdf/2505.06856"
          },
          {
            "title": "LLMs Faithfully and Iteratively Compute Answers During CoT: A Systematic Analysis With Multi-step Arithmetics",
            "url": "https://arxiv.org/html/2412.01113"
          },
          {
            "title": "Combining Causal Models for More Accurate Abstractions of Neural   Networks",
            "url": "https://arxiv.org/pdf/2503.11429"
          },
          {
            "title": "Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation",
            "url": "https://arxiv.org/html/2604.15400v1"
          },
          {
            "title": "[2508.15928] Transforming Causality: Transformer-Based Temporal Causal Discovery with Prior Knowledge Integration",
            "url": "https://arxiv.org/abs/2508.15928"
          }
        ]
      },
      "Based on the search results, I found several relevant papers related to your query. Here are the most notable ones:\n\n1. **\"Temporal Predictors of Outcome in Reasoning Language Models\"** (November 2025, arXiv:2511.14773): This paper directly probes the model's hidden trajectory during reasoning without requiring extra decoding passes, predicting answer correctness from hidden states while chain-of-thought is being generated.\n\n2. **\"Bypassing the Rationale: Causal Auditing of Implicit Reasoning in Language Models\"** (arXiv:2602.03994): This work introduces causal, layerwise intervention methods to test whether models mechanistically rely on chain-of-thought, with a framework that measures whether answers are mechanistically mediated by chain-of-thought-aligned internal representations.\n\n3. **\"Streaming Hallucination Detection in Long Chain-of-Thought Reasoning\"** (January 2026, arXiv:2601.02170): This paper views hallucination in long chain-of-thought reasoning as a temporally evolving latent state, tracking the trajectory of hidden states throughout the reasoning process rather than treating them as isolated local errors.\n\n4. **\"LLMs Faithfully and Iteratively Compute Answers During CoT: A Systematic Analysis With Multi-step Arithmetics\"** (March 2026, arXiv:2412.01113): This study combines probing results with causal intervention analyses to clarify the causal relationship between the model's internal representations and answers.\n\n5. **\"Combining Causal Models for More Accurate Abstractions of Neural Networks\"** (arXiv:2503.11429): This paper explores reasoning about the faithfulness of causal analyses by modifying partially faithful causal models based on input-provided information to become more faithful.\n\nThese papers collectively address the intersection of probing hidden states, causal interventions, reasoning, faithfulness evaluation, and temporal dynamics in language models."
    ],
    "durationSeconds": 8.244648228000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "367bb142-208c-4c33-acda-576eca75076f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T03:49:26.076Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CSycCaD3UqKRSFSyh8tqCn`</summary>

```json
{
  "query": "Wang 2604.15726 \"latent reasoning\" \"chain of thought\" H1 H2 hypothesis competing 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a6cffc6-8816-45c5-bae8-b02431d96d9d",
  "isSidechain": false,
  "requestId": "req_011CbD8z1BbxuZgqUXnUHwv4",
  "type": "assistant",
  "uuid": "29d6c356-30d6-4be0-b283-71594b753d2e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcqQVsNzEqiptLC4shLfg7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 923,
      "cache_read_input_tokens": 32366,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 923,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 32366,
          "cache_creation_input_tokens": 923,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 923
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

_source line 26 · 2026-05-20T03:49:31.737Z_

<details><summary>↩ Tool result · `toolu_01CSycCaD3UqKRSFSyh8tqCn`</summary>

```text
Web search results for query: "Wang 2604.15726 "latent reasoning" "chain of thought" H1 H2 hypothesis competing 2026"

Links: [{"title":"[2604.15726] LLM Reasoning Is Latent, Not the Chain of Thought","url":"https://arxiv.org/abs/2604.15726"},{"title":"LLM Reasoning Is Latent, Not the Chain of Thought","url":"https://arxiv.org/html/2604.15726"},{"title":"The Illusion of Superposition? A Principled Analysis of Latent Thinking in Language Models","url":"https://arxiv.org/pdf/2604.06374"},{"title":"Reasoning Beyond Chain-of-Thought: A Latent Computational Mode in Large Language Models","url":"https://arxiv.org/pdf/2601.08058"},{"title":"Latent Chain-of-Thought as Planning: Decoupling Reasoning from Verbalization","url":"https://arxiv.org/pdf/2601.21358"},{"title":"A Survey on Latent Reasoning","url":"https://arxiv.org/pdf/2507.06203"}]

I found the paper! Here are the search results for Wang 2604.15726:

This position paper argues that large language model (LLM) reasoning should be studied as latent-state trajectory formation rather than as faithful surface chain-of-thought (CoT).

The paper formalizes three competing hypotheses: H1, reasoning is primarily mediated by latent-state trajectories; H2, reasoning is primarily mediated by explicit surface CoT; and H0, most apparent reasoning gains are better explained by generic serial compute than by any privileged representational object.

The paper argues this matters because claims about faithfulness, interpretability, reasoning benchmarks, and inference-time intervention all depend on what the field takes the primary object of reasoning to be.

The paper was submitted on April 17, 2026, by Wenshuo Wang from the School of Future Technology at South China University of Technology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29d6c356-30d6-4be0-b283-71594b753d2e",
  "isSidechain": false,
  "promptId": "c0380e88-a16d-43cf-a4b7-4aee5f2af40b",
  "type": "user",
  "uuid": "f5443f89-3f12-458e-acf5-26abae961c00",
  "toolUseResult": {
    "query": "Wang 2604.15726 \"latent reasoning\" \"chain of thought\" H1 H2 hypothesis competing 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PADhXMiBVpg77DQifXjo3F",
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
      "I found the paper! Here are the search results for Wang 2604.15726:\n\nThis position paper argues that large language model (LLM) reasoning should be studied as latent-state trajectory formation rather than as faithful surface chain-of-thought (CoT).\n\nThe paper formalizes three competing hypotheses: H1, reasoning is primarily mediated by latent-state trajectories; H2, reasoning is primarily mediated by explicit surface CoT; and H0, most apparent reasoning gains are better explained by generic serial compute than by any privileged representational object.\n\nThe paper argues this matters because claims about faithfulness, interpretability, reasoning benchmarks, and inference-time intervention all depend on what the field takes the primary object of reasoning to be.\n\nThe paper was submitted on April 17, 2026, by Wenshuo Wang from the School of Future Technology at South China University of Technology."
    ],
    "durationSeconds": 5.658843279000008,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "29d6c356-30d6-4be0-b283-71594b753d2e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T03:49:34.436Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014FxVE7RAHpcMQTsPgP7Vrq`</summary>

```json
{
  "query": "\"probe calibration\" \"null probe\" hidden states reasoning models faithfulness measurement 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5443f89-3f12-458e-acf5-26abae961c00",
  "isSidechain": false,
  "requestId": "req_011CbD8zc8JVRvf5WN2edUfo",
  "type": "assistant",
  "uuid": "beb1788b-ac53-45b6-8a5c-90080e0b636a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NhEtPdMe6f26Af6MSLJZek",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 590,
      "cache_read_input_tokens": 33289,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 590,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 33289,
          "cache_creation_input_tokens": 590,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 590
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

_source line 28 · 2026-05-20T03:49:41.002Z_

<details><summary>↩ Tool result · `toolu_014FxVE7RAHpcMQTsPgP7Vrq`</summary>

```text
Web search results for query: ""probe calibration" "null probe" hidden states reasoning models faithfulness measurement 2025 2026"

Links: [{"title":"Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification | OpenReview","url":"https://openreview.net/forum?id=O6I0Av7683"},{"title":"Reasoning Models Know When They're Right: Probing Hidden States for   Self-Verification","url":"https://arxiv.org/pdf/2504.05419"},{"title":"Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation","url":"https://arxiv.org/html/2512.22245v1"},{"title":"[2512.22245] Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation","url":"https://arxiv.org/abs/2512.22245"},{"title":"Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation","url":"https://arxiv.org/pdf/2512.22245"},{"title":"Cognitive Dissonance: Why Do Language Model Outputs Disagree with   Internal Representations of Truthfulness?","url":"https://arxiv.org/pdf/2312.03729"}]

I've found several highly relevant papers on probe calibration and hidden states in reasoning models from 2025-2026. Here are the key findings:

## Recent Research on Probe Calibration and Hidden States

**1. Reasoning Models Know When They're Right (2025)**

Research studies whether reasoning models encode information about answer correctness through probing the model's hidden states. The resulting probe can verify intermediate answers with high accuracy and produces highly calibrated scores. Models' hidden states encode correctness of future answers, enabling early prediction of the correctness before the intermediate answer is fully formulated.

**2. Calibrating LLM Judges (2025)**

Linear probes trained with a Brier score-based loss provide calibrated uncertainty estimates from reasoning judges' hidden states, requiring no additional model training. These probes achieve substantially better calibration than verbalized and multi-generation baselines across multiple model families and judging styles, while requiring an order of magnitude less compute.

**3. Faithfulness and Hidden States**

Even when language model outputs are factually incorrect, it is sometimes possible to assess the truth of statements by probing models' hidden states.

These papers demonstrate recent advances in using probes to extract calibrated uncertainty and correctness information from model hidden states, which is particularly important for reasoning models and LLM judges.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "beb1788b-ac53-45b6-8a5c-90080e0b636a",
  "isSidechain": false,
  "promptId": "c0380e88-a16d-43cf-a4b7-4aee5f2af40b",
  "type": "user",
  "uuid": "bb61e0d9-f4b6-4ddc-b8ab-1b6fc724f4ad",
  "toolUseResult": {
    "query": "\"probe calibration\" \"null probe\" hidden states reasoning models faithfulness measurement 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LaByxJBFBwJxfjfCfkpgab",
        "content": [
          {
            "title": "Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification | OpenReview",
            "url": "https://openreview.net/forum?id=O6I0Av7683"
          },
          {
            "title": "Reasoning Models Know When They're Right: Probing Hidden States for   Self-Verification",
            "url": "https://arxiv.org/pdf/2504.05419"
          },
          {
            "title": "Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation",
            "url": "https://arxiv.org/html/2512.22245v1"
          },
          {
            "title": "[2512.22245] Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation",
            "url": "https://arxiv.org/abs/2512.22245"
          },
          {
            "title": "Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation",
            "url": "https://arxiv.org/pdf/2512.22245"
          },
          {
            "title": "Cognitive Dissonance: Why Do Language Model Outputs Disagree with   Internal Representations of Truthfulness?",
            "url": "https://arxiv.org/pdf/2312.03729"
          }
        ]
      },
      "I've found several highly relevant papers on probe calibration and hidden states in reasoning models from 2025-2026. Here are the key findings:\n\n## Recent Research on Probe Calibration and Hidden States\n\n**1. Reasoning Models Know When They're Right (2025)**\n\nResearch studies whether reasoning models encode information about answer correctness through probing the model's hidden states. The resulting probe can verify intermediate answers with high accuracy and produces highly calibrated scores. Models' hidden states encode correctness of future answers, enabling early prediction of the correctness before the intermediate answer is fully formulated.\n\n**2. Calibrating LLM Judges (2025)**\n\nLinear probes trained with a Brier score-based loss provide calibrated uncertainty estimates from reasoning judges' hidden states, requiring no additional model training. These probes achieve substantially better calibration than verbalized and multi-generation baselines across multiple model families and judging styles, while requiring an order of magnitude less compute.\n\n**3. Faithfulness and Hidden States**\n\nEven when language model outputs are factually incorrect, it is sometimes possible to assess the truth of statements by probing models' hidden states.\n\nThese papers demonstrate recent advances in using probes to extract calibrated uncertainty and correctness information from model hidden states, which is particularly important for reasoning models and LLM judges."
    ],
    "durationSeconds": 6.560254597999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "beb1788b-ac53-45b6-8a5c-90080e0b636a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-20T03:49:41.008Z_

```json
{
  "parentUuid": "bb61e0d9-f4b6-4ddc-b8ab-1b6fc724f4ad",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "7a154125-0b7d-4437-9bb8-d04c6bd6bb07",
  "timestamp": "2026-05-20T03:49:41.008Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-20T03:49:43.625Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B96GbPtKDkLcyz2YHKtFhQ`</summary>

```json
{
  "query": "Gjølbye 2605.15454 \"reasoning models move differently\" trajectory geometry difficulty 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a154125-0b7d-4437-9bb8-d04c6bd6bb07",
  "isSidechain": false,
  "requestId": "req_011CbD91HnmBL35MrF9K1Tb1",
  "type": "assistant",
  "uuid": "ae076328-b9f9-40c5-9e96-4ae452cfac3d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Hs7FvwqGVAUnTCniVCEn8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 33879,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 33879,
          "cache_creation_input_tokens": 801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 801
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

_source line 31 · 2026-05-20T03:49:51.027Z_

<details><summary>↩ Tool result · `toolu_01B96GbPtKDkLcyz2YHKtFhQ`</summary>

```text
Web search results for query: "Gjølbye 2605.15454 "reasoning models move differently" trajectory geometry difficulty 2026"

Links: [{"title":"[2605.15454] Reasoning Models Don't Just Think Longer, They Move Differently","url":"https://arxiv.org/abs/2605.15454"},{"title":"Reasoning Models Don’t Just Think Longer, They Move Differently","url":"https://arxiv.org/html/2605.15454"},{"title":"LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals","url":"https://arxiv.org/pdf/2604.05655"},{"title":"The Geometry of Thought: How Scale Restructures Reasoning In Large Language Models","url":"https://arxiv.org/pdf/2601.13358"},{"title":"[2605.13772] Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry","url":"https://arxiv.org/abs/2605.13772"},{"title":"The Geometry of Reasoning: Flowing Logics in Representation Space","url":"https://arxiv.org/pdf/2510.09782"}]

Based on the search results, I found the paper you're looking for:

The arXiv paper 2605.15454, authored by Anders Gjølbye, Lars Kai Hansen, and Sanmi Koyejo, is titled "Reasoning Models Don't Just Think Longer, They Move Differently" and was submitted on May 14, 2026.

**Key findings of the paper:**

Reasoning-trained language models often spend more tokens on harder problems, but longer chains of thought do not show whether a model is merely computing for more steps or following a different internal trajectory.

The researchers study this distinction through hidden-state trajectories during chain-of-thought generation across competitive programming, mathematics, and Boolean satisfiability.

**Important methodological contribution:**

Raw trajectory geometry is strongly shaped by generation length: longer generations mechanically alter path statistics, so difficulty-dependent comparisons are misleading without adjustment. After residualizing trajectory statistics on length, difficulty remains systematically coupled to corrected trajectory geometry across all domains studied.

**Main results:**

The clearest reasoning-specific separation appears in the code domain, where harder problems show more direct corrected trajectories and less heterogeneous local curvature in reasoning-trained models than in matched instruction-tuned baselines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae076328-b9f9-40c5-9e96-4ae452cfac3d",
  "isSidechain": false,
  "promptId": "c0380e88-a16d-43cf-a4b7-4aee5f2af40b",
  "type": "user",
  "uuid": "034f2603-05a8-4e5c-b307-61246a0599b4",
  "toolUseResult": {
    "query": "Gjølbye 2605.15454 \"reasoning models move differently\" trajectory geometry difficulty 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XzPGh3rBUwnD5SocfdvzCG",
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
            "title": "LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals",
            "url": "https://arxiv.org/pdf/2604.05655"
          },
          {
            "title": "The Geometry of Thought: How Scale Restructures Reasoning In Large Language Models",
            "url": "https://arxiv.org/pdf/2601.13358"
          },
          {
            "title": "[2605.13772] Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry",
            "url": "https://arxiv.org/abs/2605.13772"
          },
          {
            "title": "The Geometry of Reasoning: Flowing Logics in Representation Space",
            "url": "https://arxiv.org/pdf/2510.09782"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe arXiv paper 2605.15454, authored by Anders Gjølbye, Lars Kai Hansen, and Sanmi Koyejo, is titled \"Reasoning Models Don't Just Think Longer, They Move Differently\" and was submitted on May 14, 2026.\n\n**Key findings of the paper:**\n\nReasoning-trained language models often spend more tokens on harder problems, but longer chains of thought do not show whether a model is merely computing for more steps or following a different internal trajectory.\n\nThe researchers study this distinction through hidden-state trajectories during chain-of-thought generation across competitive programming, mathematics, and Boolean satisfiability.\n\n**Important methodological contribution:**\n\nRaw trajectory geometry is strongly shaped by generation length: longer generations mechanically alter path statistics, so difficulty-dependent comparisons are misleading without adjustment. After residualizing trajectory statistics on length, difficulty remains systematically coupled to corrected trajectory geometry across all domains studied.\n\n**Main results:**\n\nThe clearest reasoning-specific separation appears in the code domain, where harder problems show more direct corrected trajectories and less heterogeneous local curvature in reasoning-trained models than in matched instruction-tuned baselines."
    ],
    "durationSeconds": 7.397824473999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ae076328-b9f9-40c5-9e96-4ae452cfac3d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T03:49:53.854Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0156wnKEta5dLUq7CP2Lhm1J`</summary>

```json
{
  "query": "CoT faithfulness temporal measurement \"information gap\" probe contribution divergence diagnostic causal 2026 new framework"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "034f2603-05a8-4e5c-b307-61246a0599b4",
  "isSidechain": false,
  "requestId": "req_011CbD922eTwK8oks2tp4rUj",
  "type": "assistant",
  "uuid": "bb95067e-5b82-4904-b8b0-f74fa0983db0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MV7YuwkYTWYwXQvnVNaRt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 664,
      "cache_read_input_tokens": 34680,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 664,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 34680,
          "cache_creation_input_tokens": 664,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 664
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

_source line 33 · 2026-05-20T03:50:01.626Z_

<details><summary>↩ Tool result · `toolu_0156wnKEta5dLUq7CP2Lhm1J`</summary>

```text
Web search results for query: "CoT faithfulness temporal measurement "information gap" probe contribution divergence diagnostic causal 2026 new framework"

Links: [{"title":"Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING","url":"https://arxiv.org/pdf/2510.04040"},{"title":"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2602.11201"},{"title":"3 Classifiers, 3 Answers: Why CoT Faithfulness Scores Are Meaningless - DEV Community","url":"https://dev.to/plasmon_imp/3-classifiers-3-answers-why-cot-faithfulness-scores-are-meaningless-5hfc"},{"title":"Bypassing the Rationale: Causal Auditing of Implicit Reasoning in Language Models","url":"https://arxiv.org/pdf/2602.03994"},{"title":"FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2510.04040v1"},{"title":"Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models","url":"https://arxiv.org/html/2603.26410"}]

Based on the search results, here are the key findings related to CoT (Chain-of-Thought) faithfulness research in 2026:

## CoT Faithfulness Evaluation Frameworks

Three main methodological approaches have emerged for evaluating CoT faithfulness: counterfactual-based methods that perturb reasoning traces, logit-based methods that measure information gain to approximate causal alignment, and LLM-as-Judge methods that use stronger language models to evaluate reasoning quality.

## Temporal and Mechanistic Insights

A new approach called NLDD (Neuron Layer Divergence Diagnostic) offers a way to measure when CoT matters, revealing different faithfulness regimes where models either depend on their reasoning chains or are distracted by them. Recent work has identified a "Reasoning Horizon" at 70–85% of chain length, beyond which reasoning tokens have diminishing causal influence on the final answer.

## Information Gap and Divergence Findings

At the instance level, correctness and faithfulness diverge, with nearly 40% of instances showing misalignment between correct answers and faithful reasoning—meaning correct answers are not sufficient evidence of faithful reasoning. Research using 10,276 reasoning traces from 12 open-weight models found that different classifiers produced faithfulness rates ranging from 74.4% to 82.6%, with gaps between classifiers reaching 13 percentage points.

## Causal Diagnostic Framework

New causal auditing approaches use layerwise activation patching to measure CoT-related representations, introducing the CoT Mediation Index (CMI) to test whether models mechanistically rely on CoT.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb95067e-5b82-4904-b8b0-f74fa0983db0",
  "isSidechain": false,
  "promptId": "c0380e88-a16d-43cf-a4b7-4aee5f2af40b",
  "type": "user",
  "uuid": "510a07f6-af27-40b7-9d71-3f8a87866476",
  "toolUseResult": {
    "query": "CoT faithfulness temporal measurement \"information gap\" probe contribution divergence diagnostic causal 2026 new framework",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UJGiBtti5Nw1fVd9T354Np",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING",
            "url": "https://arxiv.org/pdf/2510.04040"
          },
          {
            "title": "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2602.11201"
          },
          {
            "title": "3 Classifiers, 3 Answers: Why CoT Faithfulness Scores Are Meaningless - DEV Community",
            "url": "https://dev.to/plasmon_imp/3-classifiers-3-answers-why-cot-faithfulness-scores-are-meaningless-5hfc"
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
            "title": "Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models",
            "url": "https://arxiv.org/html/2603.26410"
          }
        ]
      },
      "Based on the search results, here are the key findings related to CoT (Chain-of-Thought) faithfulness research in 2026:\n\n## CoT Faithfulness Evaluation Frameworks\n\nThree main methodological approaches have emerged for evaluating CoT faithfulness: counterfactual-based methods that perturb reasoning traces, logit-based methods that measure information gain to approximate causal alignment, and LLM-as-Judge methods that use stronger language models to evaluate reasoning quality.\n\n## Temporal and Mechanistic Insights\n\nA new approach called NLDD (Neuron Layer Divergence Diagnostic) offers a way to measure when CoT matters, revealing different faithfulness regimes where models either depend on their reasoning chains or are distracted by them. Recent work has identified a \"Reasoning Horizon\" at 70–85% of chain length, beyond which reasoning tokens have diminishing causal influence on the final answer.\n\n## Information Gap and Divergence Findings\n\nAt the instance level, correctness and faithfulness diverge, with nearly 40% of instances showing misalignment between correct answers and faithful reasoning—meaning correct answers are not sufficient evidence of faithful reasoning. Research using 10,276 reasoning traces from 12 open-weight models found that different classifiers produced faithfulness rates ranging from 74.4% to 82.6%, with gaps between classifiers reaching 13 percentage points.\n\n## Causal Diagnostic Framework\n\nNew causal auditing approaches use layerwise activation patching to measure CoT-related representations, introducing the CoT Mediation Index (CMI) to test whether models mechanistically rely on CoT."
    ],
    "durationSeconds": 7.768357408999989,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bb95067e-5b82-4904-b8b0-f74fa0983db0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
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
  "leafUuid": "510a07f6-af27-40b7-9d71-3f8a87866476",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Measuring calibrated temporal information-contribution gaps in chain-of-thought reasoning",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b"
}
```

---

### Tool call

_source line 36 · 2026-05-20T03:50:04.502Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FNzKpeuDBEWvMDYFR25H16`</summary>

```json
{
  "query": "Ballon et al 2601.23163 truncation reinjection reasoning traces causal contribution 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "510a07f6-af27-40b7-9d71-3f8a87866476",
  "isSidechain": false,
  "requestId": "req_011CbD92ov2JuW6CeSVeTrdf",
  "type": "assistant",
  "uuid": "bfe6d540-d3ca-4f48-a1b4-528002c2d5ed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MNpJK8ouWr4QXagQhzoZmK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 813,
      "cache_read_input_tokens": 35344,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 813,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 35344,
          "cache_creation_input_tokens": 813,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 813
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

_source line 37 · 2026-05-20T03:50:11.139Z_

<details><summary>↩ Tool result · `toolu_01FNzKpeuDBEWvMDYFR25H16`</summary>

```text
Web search results for query: "Ballon et al 2601.23163 truncation reinjection reasoning traces causal contribution 2026"

Links: [{"title":"[2601.23163] Probing the Trajectories of Reasoning Traces in Large Language Models","url":"https://arxiv.org/abs/2601.23163"},{"title":"Probing the Trajectories of Reasoning Traces in Large Language Models","url":"https://arxiv.org/html/2601.23163"},{"title":"[2601.21210] Uncovering Hidden Correctness in LLM Causal Reasoning via Symbolic Verification","url":"https://arxiv.org/abs/2601.21210"},{"title":"Casper: Debugging Null Dereferences with Dynamic Causality Traces","url":"https://arxiv.org/pdf/1502.02004"},{"title":"Directional Reasoning Trajectory Change (DRTC): Identifying Critical Trace Segments in Reasoning Models","url":"https://arxiv.org/pdf/2602.15332"},{"title":"Uncovering Hidden Correctness in LLM Causal Reasoning via Symbolic Verification","url":"https://arxiv.org/html/2601.21210"},{"title":"Thought Anchors: Which LLM Reasoning Steps Matter?","url":"https://arxiv.org/pdf/2506.19143"}]

Based on the search results, I found the paper you're looking for:

The paper "Probing the Trajectories of Reasoning Traces in Large Language Models" by Marthe Ballon and 3 other authors (arXiv 2601.23163) examines how large language models increasingly solve difficult problems by producing "reasoning traces" before emitting a final response.

The researchers propose a protocol to systematically probe the trajectories of reasoning traces in LLMs by 1) generating a model's reasoning trace, 2) truncating it at fixed token-percentiles, and 3) injecting each partial trace back into the model (or a different model) to measure the induced distribution over answer choices via next-token probabilities.

The work addresses whether intermediate trace segments provide answer-relevant information beyond generic length or stylistic effects, and how accuracy and decision commitment evolve along a reasoning trajectory. They apply this protocol to the open-source Qwen3-4B/-8B/-14B and gpt-oss-20b/-120b models across the multiple-choice GPQA Diamond and MMLU-Pro benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfe6d540-d3ca-4f48-a1b4-528002c2d5ed",
  "isSidechain": false,
  "promptId": "c0380e88-a16d-43cf-a4b7-4aee5f2af40b",
  "type": "user",
  "uuid": "8929e93e-970f-4922-881d-ccf9ef78578a",
  "toolUseResult": {
    "query": "Ballon et al 2601.23163 truncation reinjection reasoning traces causal contribution 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018Bj6JrZs3mPoXkwmQ7bmd5",
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
            "title": "[2601.21210] Uncovering Hidden Correctness in LLM Causal Reasoning via Symbolic Verification",
            "url": "https://arxiv.org/abs/2601.21210"
          },
          {
            "title": "Casper: Debugging Null Dereferences with Dynamic Causality Traces",
            "url": "https://arxiv.org/pdf/1502.02004"
          },
          {
            "title": "Directional Reasoning Trajectory Change (DRTC): Identifying Critical Trace Segments in Reasoning Models",
            "url": "https://arxiv.org/pdf/2602.15332"
          },
          {
            "title": "Uncovering Hidden Correctness in LLM Causal Reasoning via Symbolic Verification",
            "url": "https://arxiv.org/html/2601.21210"
          },
          {
            "title": "Thought Anchors: Which LLM Reasoning Steps Matter?",
            "url": "https://arxiv.org/pdf/2506.19143"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper \"Probing the Trajectories of Reasoning Traces in Large Language Models\" by Marthe Ballon and 3 other authors (arXiv 2601.23163) examines how large language models increasingly solve difficult problems by producing \"reasoning traces\" before emitting a final response.\n\nThe researchers propose a protocol to systematically probe the trajectories of reasoning traces in LLMs by 1) generating a model's reasoning trace, 2) truncating it at fixed token-percentiles, and 3) injecting each partial trace back into the model (or a different model) to measure the induced distribution over answer choices via next-token probabilities.\n\nThe work addresses whether intermediate trace segments provide answer-relevant information beyond generic length or stylistic effects, and how accuracy and decision commitment evolve along a reasoning trajectory. They apply this protocol to the open-source Qwen3-4B/-8B/-14B and gpt-oss-20b/-120b models across the multiple-choice GPQA Diamond and MMLU-Pro benchmarks."
    ],
    "durationSeconds": 6.631260941000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bfe6d540-d3ca-4f48-a1b4-528002c2d5ed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-20T03:50:17.447Z_

Now let me search for whether anyone has already proposed a framework that specifically combines temporal probing with causal contribution measurement — the core claim of this proposal's novelty.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8929e93e-970f-4922-881d-ccf9ef78578a",
  "isSidechain": false,
  "requestId": "req_011CbD93WeEUWibipGkYtToF",
  "type": "assistant",
  "uuid": "e780444e-9799-458c-8d27-ff4bf0473627",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013viApn36mRzkzJ2MGX6Vkg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 692,
      "cache_read_input_tokens": 36157,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 110,
          "cache_read_input_tokens": 36157,
          "cache_creation_input_tokens": 692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 692
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

_source line 39 · 2026-05-20T03:50:17.636Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K9pr1CmfnaKi1sdSvX3xBC`</summary>

```json
{
  "query": "\"probe trajectory\" AND \"causal contribution\" OR \"causal intervention\" reasoning faithfulness combined framework 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e780444e-9799-458c-8d27-ff4bf0473627",
  "isSidechain": false,
  "requestId": "req_011CbD93WeEUWibipGkYtToF",
  "type": "assistant",
  "uuid": "b332c4c5-3ed1-4d8c-90e5-01c7a83cc1f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013viApn36mRzkzJ2MGX6Vkg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 692,
      "cache_read_input_tokens": 36157,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 110,
          "cache_read_input_tokens": 36157,
          "cache_creation_input_tokens": 692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 692
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

_source line 40 · 2026-05-20T03:50:26.339Z_

<details><summary>↩ Tool result · `toolu_01K9pr1CmfnaKi1sdSvX3xBC`</summary>

```text
Web search results for query: ""probe trajectory" AND "causal contribution" OR "causal intervention" reasoning faithfulness combined framework 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING","url":"https://arxiv.org/pdf/2510.04040"},{"title":"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2602.11201"},{"title":"Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning | Request PDF","url":"https://www.researchgate.net/publication/386203451_Making_Reasoning_Matter_Measuring_and_Improving_Faithfulness_of_Chain-of-Thought_Reasoning"},{"title":"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures","url":"https://arxiv.org/html/2603.16475"},{"title":"Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents","url":"https://arxiv.org/pdf/2601.02314"},{"title":"Causal Intervention and Counterfactual Reasoning for Multimodal Pedestrian Trajectory Prediction","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12653532/"}]

I found several highly relevant research papers from 2026 that address your query about probe trajectory, causal contribution/intervention, and reasoning faithfulness frameworks:

## Key Findings:

**Faithfulness in Chain-of-Thought Reasoning:**

Recent approaches probe CoT faithfulness by perturbing reasoning traces through adding mistakes, removing steps, or forcing early answers, treating causal sensitivity as evidence of faithfulness since a faithful CoT should preserve a causal link between intermediate steps and the final answer.

**Mechanistic Diagnostics:**

Research couples linear probes to track solution-relevant information evolution across layers, utilizing Trajectory Alignment Score (TAS) to quantify geometric drift of reasoning paths in latent space following counterfactual intervention.

**Counterfactual Intervention Methods:**

By performing counterfactual interventions that corrupt specific reasoning steps while maintaining surface coherence, researchers isolate the degree to which models causally depend on their generated reasoning.

**Structural Causal Frameworks:**

Project Ariadne utilizes Structural Causal Models (SCMs) and counterfactual logic, performing hard interventions on intermediate reasoning nodes to measure Causal Sensitivity of the terminal answer.

**Causal Evaluation Protocols:**

A causal evaluation protocol makes structural causality directly measurable: selecting tasks where a deterministic function maps intermediate structures to decisions, revealing that apparent faithfulness is fragile once the intermediate structure changes.

These papers represent the cutting edge of reasoning faithfulness evaluation combining probe trajectories with causal intervention methodologies in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b332c4c5-3ed1-4d8c-90e5-01c7a83cc1f7",
  "isSidechain": false,
  "promptId": "c0380e88-a16d-43cf-a4b7-4aee5f2af40b",
  "type": "user",
  "uuid": "47438f05-f202-428e-b3fe-8b3bbd3bb693",
  "toolUseResult": {
    "query": "\"probe trajectory\" AND \"causal contribution\" OR \"causal intervention\" reasoning faithfulness combined framework 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0168uV4k5sAUkaWXe5zPVcmP",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026 FAITHCOT-BENCH: BENCHMARKING",
            "url": "https://arxiv.org/pdf/2510.04040"
          },
          {
            "title": "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2602.11201"
          },
          {
            "title": "Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning | Request PDF",
            "url": "https://www.researchgate.net/publication/386203451_Making_Reasoning_Matter_Measuring_and_Improving_Faithfulness_of_Chain-of-Thought_Reasoning"
          },
          {
            "title": "Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures",
            "url": "https://arxiv.org/html/2603.16475"
          },
          {
            "title": "Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents",
            "url": "https://arxiv.org/pdf/2601.02314"
          },
          {
            "title": "Causal Intervention and Counterfactual Reasoning for Multimodal Pedestrian Trajectory Prediction",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12653532/"
          }
        ]
      },
      "I found several highly relevant research papers from 2026 that address your query about probe trajectory, causal contribution/intervention, and reasoning faithfulness frameworks:\n\n## Key Findings:\n\n**Faithfulness in Chain-of-Thought Reasoning:**\n\nRecent approaches probe CoT faithfulness by perturbing reasoning traces through adding mistakes, removing steps, or forcing early answers, treating causal sensitivity as evidence of faithfulness since a faithful CoT should preserve a causal link between intermediate steps and the final answer.\n\n**Mechanistic Diagnostics:**\n\nResearch couples linear probes to track solution-relevant information evolution across layers, utilizing Trajectory Alignment Score (TAS) to quantify geometric drift of reasoning paths in latent space following counterfactual intervention.\n\n**Counterfactual Intervention Methods:**\n\nBy performing counterfactual interventions that corrupt specific reasoning steps while maintaining surface coherence, researchers isolate the degree to which models causally depend on their generated reasoning.\n\n**Structural Causal Frameworks:**\n\nProject Ariadne utilizes Structural Causal Models (SCMs) and counterfactual logic, performing hard interventions on intermediate reasoning nodes to measure Causal Sensitivity of the terminal answer.\n\n**Causal Evaluation Protocols:**\n\nA causal evaluation protocol makes structural causality directly measurable: selecting tasks where a deterministic function maps intermediate structures to decisions, revealing that apparent faithfulness is fragile once the intermediate structure changes.\n\nThese papers represent the cutting edge of reasoning faithfulness evaluation combining probe trajectories with causal intervention methodologies in 2026."
    ],
    "durationSeconds": 8.698460927999985,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b332c4c5-3ed1-4d8c-90e5-01c7a83cc1f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T03:50:29.756Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TmgUEeNNi2osuXRsbtNPnE`</summary>

```json
{
  "query": "Cox et al 2603.01437 pre-CoT probes activation steering reasoning model failure answer flip rate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47438f05-f202-428e-b3fe-8b3bbd3bb693",
  "isSidechain": false,
  "requestId": "req_011CbD94dtpivHqZ7NL4yqU6",
  "type": "assistant",
  "uuid": "6e8c7ea7-d864-4a5d-adb4-545363d4150c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EfDB79RmnajxXt8WBGuG4f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 833,
      "cache_read_input_tokens": 36849,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 833,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 36849,
          "cache_creation_input_tokens": 833,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 833
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

_source line 42 · 2026-05-20T03:50:35.430Z_

<details><summary>↩ Tool result · `toolu_01TmgUEeNNi2osuXRsbtNPnE`</summary>

```text
Web search results for query: "Cox et al 2603.01437 pre-CoT probes activation steering reasoning model failure answer flip rate"

Links: [{"title":"[2603.01437] Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/abs/2603.01437"},{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/html/2603.01437"},{"title":"Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://arxiv.org/pdf/2603.01437"},{"title":"Post-Hoc Reasoning in Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering | OpenReview","url":"https://openreview.net/forum?id=UMUYpeXtJQ"},{"title":"[Literature Review] Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering","url":"https://www.themoonlight.io/en/review/decoding-answers-before-chain-of-thought-evidence-from-pre-cot-probes-and-activation-steering"}]

Based on the search results, here's what I found about the Cox et al. paper (arXiv:2603.01437):

## Pre-CoT Probes

Training linear probes on residual stream activations at the last token before CoT, the researchers can predict the model's final answer with >0.9 AUC on most tasks. This was tested across five language models (Gemma 2: 2B, 9B; Qwen 2.5: 1.5B, 3B, 7B) and four binary question answering tasks (Anachronisms, Logical Deduction, Social Chemistry, Sports Understanding).

## Activation Steering & Answer Flip Rate

Steering activations along the probe direction flips model answers in over 50% of cases, significantly exceeding orthogonal baselines. This demonstrates that the discovered directions are not only predictive but also causal in determining model outputs.

## Failure Modes

When steering induces incorrect answers, two distinct failure modes are observed: non-entailment (stating correct premises but drawing unsupported conclusions) and confabulation (fabricating false premises).

The paper provides mechanistic evidence that instruction-tuned models often determine their answer before generating CoT, suggesting that chain-of-thought reasoning may be post-hoc rather than faithfully reflecting the model's decision process.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e8c7ea7-d864-4a5d-adb4-545363d4150c",
  "isSidechain": false,
  "promptId": "c0380e88-a16d-43cf-a4b7-4aee5f2af40b",
  "type": "user",
  "uuid": "d8cf44a3-c9cc-4287-8c0d-168f223edceb",
  "toolUseResult": {
    "query": "Cox et al 2603.01437 pre-CoT probes activation steering reasoning model failure answer flip rate",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MWEeUG4K1Fp2M2QUJE6ZUo",
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
            "title": "Post-Hoc Reasoning in Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering | OpenReview",
            "url": "https://openreview.net/forum?id=UMUYpeXtJQ"
          },
          {
            "title": "[Literature Review] Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering",
            "url": "https://www.themoonlight.io/en/review/decoding-answers-before-chain-of-thought-evidence-from-pre-cot-probes-and-activation-steering"
          }
        ]
      },
      "Based on the search results, here's what I found about the Cox et al. paper (arXiv:2603.01437):\n\n## Pre-CoT Probes\n\nTraining linear probes on residual stream activations at the last token before CoT, the researchers can predict the model's final answer with >0.9 AUC on most tasks. This was tested across five language models (Gemma 2: 2B, 9B; Qwen 2.5: 1.5B, 3B, 7B) and four binary question answering tasks (Anachronisms, Logical Deduction, Social Chemistry, Sports Understanding).\n\n## Activation Steering & Answer Flip Rate\n\nSteering activations along the probe direction flips model answers in over 50% of cases, significantly exceeding orthogonal baselines. This demonstrates that the discovered directions are not only predictive but also causal in determining model outputs.\n\n## Failure Modes\n\nWhen steering induces incorrect answers, two distinct failure modes are observed: non-entailment (stating correct premises but drawing unsupported conclusions) and confabulation (fabricating false premises).\n\nThe paper provides mechanistic evidence that instruction-tuned models often determine their answer before generating CoT, suggesting that chain-of-thought reasoning may be post-hoc rather than faithfully reflecting the model's decision process."
    ],
    "durationSeconds": 5.669533018999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6e8c7ea7-d864-4a5d-adb4-545363d4150c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T03:50:38.244Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018wm4qksN4HkYThf7Wwpqp1`</summary>

```json
{
  "query": "reasoning models CoT faithfulness phenomenon taxonomy classification temporal signatures pre-CoT post-hoc rationalization 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8cf44a3-c9cc-4287-8c0d-168f223edceb",
  "isSidechain": false,
  "requestId": "req_011CbD95JUZ1ruUqxr8xxpgZ",
  "type": "assistant",
  "uuid": "9794abf0-cba4-41df-868d-251fe2b5db9f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTaac1Xkmt1fEgo7JimGbi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 743,
      "cache_read_input_tokens": 37682,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 743,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 37682,
          "cache_creation_input_tokens": 743,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 743
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

_source line 44 · 2026-05-20T03:50:47.666Z_

<details><summary>↩ Tool result · `toolu_018wm4qksN4HkYThf7Wwpqp1`</summary>

```text
Web search results for query: "reasoning models CoT faithfulness phenomenon taxonomy classification temporal signatures pre-CoT post-hoc rationalization 2026"

Links: [{"title":"Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models","url":"https://arxiv.org/html/2603.26410"},{"title":"[2603.22582] Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?","url":"https://arxiv.org/abs/2603.22582"},{"title":"Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?","url":"https://arxiv.org/html/2603.22582v1"},{"title":"Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?","url":"https://arxiv.org/pdf/2508.19827"},{"title":"Are DeepSeek R1 And Other Reasoning Models More Faithful?","url":"https://arxiv.org/pdf/2501.08156"},{"title":"Chain-of-Thought Reasoning In The Wild Is Not Always Faithful","url":"https://arxiv.org/pdf/2503.08679"},{"title":"Reasoning Models Don't Always Say What They Think","url":"https://arxiv.org/pdf/2505.05410"}]

Based on the web search results, I found several recent 2026 studies examining the faithfulness of chain-of-thought reasoning in modern reasoning models:

## Key Findings on CoT Faithfulness

Prior work has established that chain-of-thought reasoning is not always faithful. Recent research from 2026 reveals a striking phenomenon:

Keyword-based analysis reveals a striking gap between thinking-token acknowledgment (approximately 87.5%) and answer-text acknowledgment (approximately 28.6%), suggesting that models internally recognize hint influence but systematically suppress this acknowledgment in their outputs.

## Taxonomy and Classification

The analysis classifies cases into a four-quadrant taxonomy based on hint acknowledgment patterns in thinking tokens versus answer text. This taxonomy distinguishes cases where models do or don't acknowledge influencing cues in different channels.

## Temporal Signatures

Boppana et al. (2026) used activation probing to demonstrate "Reasoning Theater" (models that lock in answers early but continue generating performative reasoning tokens). This suggests temporal patterns where answers are determined before the reasoning output.

## Pre-CoT vs. Post-hoc Rationalization

Earlier non-reasoning models generate post-hoc CoT reasoning without mentioning cues at all. In contrast, unfaithful CoT reasoning can be found in both thinking and non-thinking frontier models, even without explicit prompting.

The research indicates that faithfulness is not a fixed property of reasoning models but varies systematically with architecture, training method, and the nature of the influencing cue.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9794abf0-cba4-41df-868d-251fe2b5db9f",
  "isSidechain": false,
  "promptId": "c0380e88-a16d-43cf-a4b7-4aee5f2af40b",
  "type": "user",
  "uuid": "6576ff68-57e5-446f-81a1-6bba31acad4a",
  "toolUseResult": {
    "query": "reasoning models CoT faithfulness phenomenon taxonomy classification temporal signatures pre-CoT post-hoc rationalization 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011JAzqgWKtXv9LoypwKnnWu",
        "content": [
          {
            "title": "Why Models Know But Don’t Say: Chain-of-Thought Faithfulness Divergence Between Thinking Tokens and Answers in Open-Weight Reasoning Models",
            "url": "https://arxiv.org/html/2603.26410"
          },
          {
            "title": "[2603.22582] Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?",
            "url": "https://arxiv.org/abs/2603.22582"
          },
          {
            "title": "Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Open-Weight Reasoning Models?",
            "url": "https://arxiv.org/html/2603.22582v1"
          },
          {
            "title": "Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?",
            "url": "https://arxiv.org/pdf/2508.19827"
          },
          {
            "title": "Are DeepSeek R1 And Other Reasoning Models More Faithful?",
            "url": "https://arxiv.org/pdf/2501.08156"
          },
          {
            "title": "Chain-of-Thought Reasoning In The Wild Is Not Always Faithful",
            "url": "https://arxiv.org/pdf/2503.08679"
          },
          {
            "title": "Reasoning Models Don't Always Say What They Think",
            "url": "https://arxiv.org/pdf/2505.05410"
          }
        ]
      },
      "Based on the web search results, I found several recent 2026 studies examining the faithfulness of chain-of-thought reasoning in modern reasoning models:\n\n## Key Findings on CoT Faithfulness\n\nPrior work has established that chain-of-thought reasoning is not always faithful. Recent research from 2026 reveals a striking phenomenon:\n\nKeyword-based analysis reveals a striking gap between thinking-token acknowledgment (approximately 87.5%) and answer-text acknowledgment (approximately 28.6%), suggesting that models internally recognize hint influence but systematically suppress this acknowledgment in their outputs.\n\n## Taxonomy and Classification\n\nThe analysis classifies cases into a four-quadrant taxonomy based on hint acknowledgment patterns in thinking tokens versus answer text. This taxonomy distinguishes cases where models do or don't acknowledge influencing cues in different channels.\n\n## Temporal Signatures\n\nBoppana et al. (2026) used activation probing to demonstrate \"Reasoning Theater\" (models that lock in answers early but continue generating performative reasoning tokens). This suggests temporal patterns where answers are determined before the reasoning output.\n\n## Pre-CoT vs. Post-hoc Rationalization\n\nEarlier non-reasoning models generate post-hoc CoT reasoning without mentioning cues at all. In contrast, unfaithful CoT reasoning can be found in both thinking and non-thinking frontier models, even without explicit prompting.\n\nThe research indicates that faithfulness is not a fixed property of reasoning models but varies systematically with architecture, training method, and the nature of the influencing cue."
    ],
    "durationSeconds": 9.417974979999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9794abf0-cba4-41df-868d-251fe2b5db9f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T03:50:50.893Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RQGrrNL83fxEatieHSV4Uh`</summary>

```json
{
  "query": "Chun et al 2602.20338 manifold capacity theory CoT reasoning geometric separability probe inflation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6576ff68-57e5-446f-81a1-6bba31acad4a",
  "isSidechain": false,
  "requestId": "req_011CbD96CpWJEaXYr5ZGR3r6",
  "type": "assistant",
  "uuid": "6f154a98-e600-49e4-8ffd-dabe41a1a769",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJDFhM2hKv4wkezRUAZAwq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 791,
      "cache_read_input_tokens": 38425,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 791,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 38425,
          "cache_creation_input_tokens": 791,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 791
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

_source line 46 · 2026-05-20T03:50:58.051Z_

<details><summary>↩ Tool result · `toolu_01RQGrrNL83fxEatieHSV4Uh`</summary>

```text
Web search results for query: "Chun et al 2602.20338 manifold capacity theory CoT reasoning geometric separability probe inflation"

Links: [{"title":"[2602.20338] Emergent Manifold Separability during Reasoning in Large Language Models","url":"https://arxiv.org/abs/2602.20338"},{"title":"Emergent Manifold Separability during Reasoning in Large Language Models","url":"https://arxiv.org/pdf/2602.20338"},{"title":"Emergent Manifold Separability during Reasoning in Large Language Models","url":"https://arxiv.org/html/2602.20338"},{"title":"CoT is Not True Reasoning, It Is Just a Tight Constraint to Imitate: A Theory Perspective","url":"https://arxiv.org/pdf/2506.02878"},{"title":"On the Representational Capacity of Neural Language Models with   Chain-of-Thought Reasoning","url":"https://arxiv.org/pdf/2406.14197"}]

Based on the search results, I found the paper you're looking for. Here's what the research contains:

The paper investigates Chain-of-Thought (CoT) prompting in Large Language Models by applying Manifold Capacity Theory (MCT) to a compositional Boolean logic task, allowing researchers to quantify the linear separability of latent representations without the confounding factors of probe training.

The key finding is that reasoning manifests as a transient geometric pulse, where concept manifolds are untangled into linearly separable subspaces immediately prior to computation and rapidly compressed thereafter.

This behavior diverges from standard linear probe accuracy, which remains high long after computation, suggesting a fundamental distinction between information that is merely retrievable and information that is geometrically prepared for processing.

The paper is titled "Emergent Manifold Separability during Reasoning in Large Language Models" and was authored by Alexandre Polo, Chanwoo Chun, and SueYeon Chung from Harvard University and affiliated institutions. It was submitted on February 23, 2026 (arXiv:2602.20338).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f154a98-e600-49e4-8ffd-dabe41a1a769",
  "isSidechain": false,
  "promptId": "c0380e88-a16d-43cf-a4b7-4aee5f2af40b",
  "type": "user",
  "uuid": "f73b6e4d-7ce4-4807-bcc9-28eb45a21153",
  "toolUseResult": {
    "query": "Chun et al 2602.20338 manifold capacity theory CoT reasoning geometric separability probe inflation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Wf79eUgtUD51Xki9avULTz",
        "content": [
          {
            "title": "[2602.20338] Emergent Manifold Separability during Reasoning in Large Language Models",
            "url": "https://arxiv.org/abs/2602.20338"
          },
          {
            "title": "Emergent Manifold Separability during Reasoning in Large Language Models",
            "url": "https://arxiv.org/pdf/2602.20338"
          },
          {
            "title": "Emergent Manifold Separability during Reasoning in Large Language Models",
            "url": "https://arxiv.org/html/2602.20338"
          },
          {
            "title": "CoT is Not True Reasoning, It Is Just a Tight Constraint to Imitate: A Theory Perspective",
            "url": "https://arxiv.org/pdf/2506.02878"
          },
          {
            "title": "On the Representational Capacity of Neural Language Models with   Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/pdf/2406.14197"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's what the research contains:\n\nThe paper investigates Chain-of-Thought (CoT) prompting in Large Language Models by applying Manifold Capacity Theory (MCT) to a compositional Boolean logic task, allowing researchers to quantify the linear separability of latent representations without the confounding factors of probe training.\n\nThe key finding is that reasoning manifests as a transient geometric pulse, where concept manifolds are untangled into linearly separable subspaces immediately prior to computation and rapidly compressed thereafter.\n\nThis behavior diverges from standard linear probe accuracy, which remains high long after computation, suggesting a fundamental distinction between information that is merely retrievable and information that is geometrically prepared for processing.\n\nThe paper is titled \"Emergent Manifold Separability during Reasoning in Large Language Models\" and was authored by Alexandre Polo, Chanwoo Chun, and SueYeon Chung from Harvard University and affiliated institutions. It was submitted on February 23, 2026 (arXiv:2602.20338)."
    ],
    "durationSeconds": 7.153340533999988,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6f154a98-e600-49e4-8ffd-dabe41a1a769",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
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
  "leafUuid": "f73b6e4d-7ce4-4807-bcc9-28eb45a21153",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Measuring calibrated temporal information-contribution gaps in chain-of-thought reasoning",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b"
}
```

---

### Assistant

_source line 49 · 2026-05-20T03:51:00.791Z_

Now I have sufficient research context. Let me synthesize my analysis of this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f73b6e4d-7ce4-4807-bcc9-28eb45a21153",
  "isSidechain": false,
  "requestId": "req_011CbD96yDEFYqY2m5Yqk7Vg",
  "type": "assistant",
  "uuid": "fd3302f1-c633-470b-b65b-58430c886d35",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNoqLc7QcY4XCrEq6bD6YK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 595,
      "cache_read_input_tokens": 39216,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 595,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 99,
          "cache_read_input_tokens": 39216,
          "cache_creation_input_tokens": 595,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 595
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

_source line 50 · 2026-05-20T03:51:01.719Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MumdscSjoTTrkDhEVWTvNs`</summary>

```json
{
  "query": "Esakkiraja 2604.01202 \"Therefore I am\" pre-generation AUROC dip recovery reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd3302f1-c633-470b-b65b-58430c886d35",
  "isSidechain": false,
  "requestId": "req_011CbD96yDEFYqY2m5Yqk7Vg",
  "type": "assistant",
  "uuid": "2bc7f0a4-8c17-4139-835f-48a1670a2325",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNoqLc7QcY4XCrEq6bD6YK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 595,
      "cache_read_input_tokens": 39216,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 595,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 99,
          "cache_read_input_tokens": 39216,
          "cache_creation_input_tokens": 595,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 595
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

_source line 51 · 2026-05-20T03:51:08.400Z_

<details><summary>↩ Tool result · `toolu_01MumdscSjoTTrkDhEVWTvNs`</summary>

```text
Web search results for query: "Esakkiraja 2604.01202 "Therefore I am" pre-generation AUROC dip recovery reasoning 2026"

Links: [{"title":"[2604.01202] Therefore I am. I Think","url":"https://arxiv.org/abs/2604.01202"},{"title":"Therefore I am. I Think.","url":"https://arxiv.org/html/2604.01202"},{"title":"Paper page - Therefore I am. I Think","url":"https://huggingface.co/papers/2604.01202"},{"title":"Esakkiraja Esakkidurai","url":"https://m.facebook.com/IndianKickboxerEsakkiraja/?profile_tab_item_selected=about"},{"title":"Esakki Raja (@actor_esakkiraja)","url":"https://www.instagram.com/actor_esakkiraja/"},{"title":"G4 & the balanced metric family – a novel approach to solving binary classification problems in medical device validation & verification studies","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11515465/"},{"title":"Recovery after stroke: not so proportional after all?","url":"https://www.biorxiv.org/content/10.1101/306514.full.pdf"},{"title":"Esakkiraja Esakkidurai (@indiankickboxeresakkirajadurai) • Instagram photos and videos","url":"https://www.instagram.com/indiankickboxeresakkirajadurai/"},{"title":"How to reduce the number of rating scale items without predictability loss?","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5400800/"}]

Based on the search results, I found information about the paper you're asking about:

"Therefore I am. I Think" is an arXiv paper (2604.01202) by Esakkivel Esakkiraja and 3 other authors that investigates when large language reasoning models make choices—whether they think first and then decide, or decide first and then think.

The paper shows that a simple linear probe successfully decodes tool-calling decisions from pre-generation activations with very high confidence, and in some cases, even before a single reasoning token is produced. Activation steering supports this causally: perturbing the decision direction leads to inflated deliberation and flips behavior in many examples, and when steering changes the decision, the chain-of-thought process often rationalizes the flip rather than resisting it.

The paper appears to have been published on arXiv on April 3, 2026, but the search results don't contain specific information about AUROC dip recovery or the specific reasoning mechanisms related to that metric. For more detailed technical information about those specific aspects, you might want to access the full PDF directly from the arXiv link.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2bc7f0a4-8c17-4139-835f-48a1670a2325",
  "isSidechain": false,
  "promptId": "c0380e88-a16d-43cf-a4b7-4aee5f2af40b",
  "type": "user",
  "uuid": "dedd8b98-5a54-47fb-9dc1-778260f9f7b8",
  "toolUseResult": {
    "query": "Esakkiraja 2604.01202 \"Therefore I am\" pre-generation AUROC dip recovery reasoning 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ELVrSnjPM9NFF7QfLcvu4N",
        "content": [
          {
            "title": "[2604.01202] Therefore I am. I Think",
            "url": "https://arxiv.org/abs/2604.01202"
          },
          {
            "title": "Therefore I am. I Think.",
            "url": "https://arxiv.org/html/2604.01202"
          },
          {
            "title": "Paper page - Therefore I am. I Think",
            "url": "https://huggingface.co/papers/2604.01202"
          },
          {
            "title": "Esakkiraja Esakkidurai",
            "url": "https://m.facebook.com/IndianKickboxerEsakkiraja/?profile_tab_item_selected=about"
          },
          {
            "title": "Esakki Raja (@actor_esakkiraja)",
            "url": "https://www.instagram.com/actor_esakkiraja/"
          },
          {
            "title": "G4 & the balanced metric family – a novel approach to solving binary classification problems in medical device validation & verification studies",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11515465/"
          },
          {
            "title": "Recovery after stroke: not so proportional after all?",
            "url": "https://www.biorxiv.org/content/10.1101/306514.full.pdf"
          },
          {
            "title": "Esakkiraja Esakkidurai (@indiankickboxeresakkirajadurai) • Instagram photos and videos",
            "url": "https://www.instagram.com/indiankickboxeresakkirajadurai/"
          },
          {
            "title": "How to reduce the number of rating scale items without predictability loss?",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5400800/"
          }
        ]
      },
      "Based on the search results, I found information about the paper you're asking about:\n\n\"Therefore I am. I Think\" is an arXiv paper (2604.01202) by Esakkivel Esakkiraja and 3 other authors that investigates when large language reasoning models make choices—whether they think first and then decide, or decide first and then think.\n\nThe paper shows that a simple linear probe successfully decodes tool-calling decisions from pre-generation activations with very high confidence, and in some cases, even before a single reasoning token is produced. Activation steering supports this causally: perturbing the decision direction leads to inflated deliberation and flips behavior in many examples, and when steering changes the decision, the chain-of-thought process often rationalizes the flip rather than resisting it.\n\nThe paper appears to have been published on arXiv on April 3, 2026, but the search results don't contain specific information about AUROC dip recovery or the specific reasoning mechanisms related to that metric. For more detailed technical information about those specific aspects, you might want to access the full PDF directly from the arXiv link."
    ],
    "durationSeconds": 6.676565323999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2bc7f0a4-8c17-4139-835f-48a1670a2325",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 52 · 2026-05-20T03:51:08.405Z_

```json
{
  "parentUuid": "dedd8b98-5a54-47fb-9dc1-778260f9f7b8",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f9757bcf-2ec6-40a2-afc0-bab96e3f87d1",
  "timestamp": "2026-05-20T03:51:08.405Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 53 · 2026-05-20T03:51:11.718Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015nmmQaHGFpDVvC1aAf55D6`</summary>

```json
{
  "query": "correctness probe vs answer content probe hidden states reasoning models distinction 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9757bcf-2ec6-40a2-afc0-bab96e3f87d1",
  "isSidechain": false,
  "requestId": "req_011CbD97jWzxFb2c7j7CFWzN",
  "type": "assistant",
  "uuid": "474230ae-0f62-448e-844e-58846768fac8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LeU6ZXpKJxGiwxMXCPJBbH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 897,
      "cache_read_input_tokens": 39811,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 897,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 39811,
          "cache_creation_input_tokens": 897,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 897
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

_source line 54 · 2026-05-20T03:51:21.599Z_

<details><summary>↩ Tool result · `toolu_015nmmQaHGFpDVvC1aAf55D6`</summary>

```text
Web search results for query: "correctness probe vs answer content probe hidden states reasoning models distinction 2026"

Links: [{"title":"Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification | OpenReview","url":"https://openreview.net/forum?id=O6I0Av7683"},{"title":"Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/html/2504.05419v1"},{"title":"Reasoning Models Know When They're Right: Probing Hidden States for   Self-Verification","url":"https://arxiv.org/pdf/2504.05419"},{"title":"They train a binary probe on hidden states from intermediate reasoning steps, which accurately predicts answer correctness before generation, enabling early-exit to reduce test-time compute without compromise. Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification https://arxiv.org/abs/2504.05419v1","url":"https://www.threads.com/@sung.kim.mw/post/DTxYmJ4EWAp/they-train-a-binary-probe-on-hidden-states-from-intermediate-reasoning-steps"},{"title":"[Literature Review] Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification","url":"https://www.themoonlight.io/en/review/reasoning-models-know-when-theyre-right-probing-hidden-states-for-self-verification"},{"title":"Reasoning Models Know When They’re Right: NYU Researchers Introduce a Hidden-State Probe That Enables Efficient Self-Verification and Reduces Token Usage by 24% - MarkTechPost","url":"https://www.marktechpost.com/2025/04/13/reasoning-models-know-when-theyre-right-nyu-researchers-introduce-a-hidden-state-probe-that-enables-efficient-self-verification-and-reduces-token-usage-by-24/"}]

The search results focus primarily on a specific paper about probing hidden states for correctness in reasoning models, but don't directly address a distinction between "correctness probe" and "answer content probe." Let me search more specifically for this distinction.

Links: [{"title":"Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/html/2504.05419v1"},{"title":"(PDF) Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification","url":"https://www.researchgate.net/publication/390601804_Reasoning_Models_Know_When_They're_Right_Probing_Hidden_States_for_Self-Verification"},{"title":"[2504.05419] Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/abs/2504.05419"},{"title":"Reasoning Models Know When They're Right: Probing Hidden States for   Self-Verification","url":"https://arxiv.org/pdf/2504.05419"},{"title":"[Literature Review] Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification","url":"https://www.themoonlight.io/en/review/reasoning-models-know-when-theyre-right-probing-hidden-states-for-self-verification"},{"title":"Reasoning Models Know When They’re Right: NYU Researchers Introduce a Hidden-State Probe That Enables Efficient Self-Verification and Reduces Token Usage by 24% - MarkTechPost","url":"https://www.marktechpost.com/2025/04/13/reasoning-models-know-when-theyre-right-nyu-researchers-introduce-a-hidden-state-probe-that-enables-efficient-self-verification-and-reduces-token-usage-by-24/"},{"title":"Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification | OpenReview","url":"https://openreview.net/forum?id=O6I0Av7683"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"}]

Based on my search results, I found relevant information about probing hidden states in reasoning models, though the specific distinction between "correctness probe" and "answer content probe" as separate concepts is not explicitly detailed in these sources. However, I can provide you with what the research shows:

## Key Findings on Probing Hidden States in Reasoning Models

Researchers segment long Chain-of-Thought (CoT) into chunks containing intermediate answers, and train a binary classifier to predict answer correctness from the model's hidden states at the answer positions. This represents the "correctness probe" approach.

Information about answer correctness is readily encoded in the model's internal representations, and a simple probe can reliably extract this information, performing accurately on both in-distribution and out-of-distribution examples.

### Look-Ahead Capabilities

The model's hidden states contain "look-ahead" information: correctness can be predicted even before the intermediate answer is fully articulated. This suggests that correctness signals are encoded at deeper levels of the hidden states.

### Differences from Non-Reasoning Models

When applying the same probing method to traditional short CoT models, there is a significant degradation in performance, suggesting that the encoded correctness information is likely acquired during long CoT training.

The search results don't explicitly contrast a separate "answer content probe" distinct from correctness probing. If you're looking for information about a specific paper or framework that makes this distinction, you may need to provide additional context or search terms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "474230ae-0f62-448e-844e-58846768fac8",
  "isSidechain": false,
  "promptId": "c0380e88-a16d-43cf-a4b7-4aee5f2af40b",
  "type": "user",
  "uuid": "7f5546d5-c01c-4c45-a433-09f83e1bb6f0",
  "toolUseResult": {
    "query": "correctness probe vs answer content probe hidden states reasoning models distinction 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01T9PRTLA2Dr5HtiwGiUV14S",
        "content": [
          {
            "title": "Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification | OpenReview",
            "url": "https://openreview.net/forum?id=O6I0Av7683"
          },
          {
            "title": "Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification",
            "url": "https://arxiv.org/html/2504.05419v1"
          },
          {
            "title": "Reasoning Models Know When They're Right: Probing Hidden States for   Self-Verification",
            "url": "https://arxiv.org/pdf/2504.05419"
          },
          {
            "title": "They train a binary probe on hidden states from intermediate reasoning steps, which accurately predicts answer correctness before generation, enabling early-exit to reduce test-time compute without compromise. Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification https://arxiv.org/abs/2504.05419v1",
            "url": "https://www.threads.com/@sung.kim.mw/post/DTxYmJ4EWAp/they-train-a-binary-probe-on-hidden-states-from-intermediate-reasoning-steps"
          },
          {
            "title": "[Literature Review] Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification",
            "url": "https://www.themoonlight.io/en/review/reasoning-models-know-when-theyre-right-probing-hidden-states-for-self-verification"
          },
          {
            "title": "Reasoning Models Know When They’re Right: NYU Researchers Introduce a Hidden-State Probe That Enables Efficient Self-Verification and Reduces Token Usage by 24% - MarkTechPost",
            "url": "https://www.marktechpost.com/2025/04/13/reasoning-models-know-when-theyre-right-nyu-researchers-introduce-a-hidden-state-probe-that-enables-efficient-self-verification-and-reduces-token-usage-by-24/"
          }
        ]
      },
      "The search results focus primarily on a specific paper about probing hidden states for correctness in reasoning models, but don't directly address a distinction between \"correctness probe\" and \"answer content probe.\" Let me search more specifically for this distinction.",
      {
        "tool_use_id": "srvtoolu_01HYaMExu6Zq9J4Lp9dJuEmv",
        "content": [
          {
            "title": "Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification",
            "url": "https://arxiv.org/html/2504.05419v1"
          },
          {
            "title": "(PDF) Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification",
            "url": "https://www.researchgate.net/publication/390601804_Reasoning_Models_Know_When_They're_Right_Probing_Hidden_States_for_Self-Verification"
          },
          {
            "title": "[2504.05419] Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification",
            "url": "https://arxiv.org/abs/2504.05419"
          },
          {
            "title": "Reasoning Models Know When They're Right: Probing Hidden States for   Self-Verification",
            "url": "https://arxiv.org/pdf/2504.05419"
          },
          {
            "title": "[Literature Review] Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification",
            "url": "https://www.themoonlight.io/en/review/reasoning-models-know-when-theyre-right-probing-hidden-states-for-self-verification"
          },
          {
            "title": "Reasoning Models Know When They’re Right: NYU Researchers Introduce a Hidden-State Probe That Enables Efficient Self-Verification and Reduces Token Usage by 24% - MarkTechPost",
            "url": "https://www.marktechpost.com/2025/04/13/reasoning-models-know-when-theyre-right-nyu-researchers-introduce-a-hidden-state-probe-that-enables-efficient-self-verification-and-reduces-token-usage-by-24/"
          },
          {
            "title": "Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification | OpenReview",
            "url": "https://openreview.net/forum?id=O6I0Av7683"
          },
          {
            "title": "Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs",
            "url": "https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"
          }
        ]
      },
      "Based on my search results, I found relevant information about probing hidden states in reasoning models, though the specific distinction between \"correctness probe\" and \"answer content probe\" as separate concepts is not explicitly detailed in these sources. However, I can provide you with what the research shows:\n\n## Key Findings on Probing Hidden States in Reasoning Models\n\nResearchers segment long Chain-of-Thought (CoT) into chunks containing intermediate answers, and train a binary classifier to predict answer correctness from the model's hidden states at the answer positions. This represents the \"correctness probe\" approach.\n\nInformation about answer correctness is readily encoded in the model's internal representations, and a simple probe can reliably extract this information, performing accurately on both in-distribution and out-of-distribution examples.\n\n### Look-Ahead Capabilities\n\nThe model's hidden states contain \"look-ahead\" information: correctness can be predicted even before the intermediate answer is fully articulated. This suggests that correctness signals are encoded at deeper levels of the hidden states.\n\n### Differences from Non-Reasoning Models\n\nWhen applying the same probing method to traditional short CoT models, there is a significant degradation in performance, suggesting that the encoded correctness information is likely acquired during long CoT training.\n\nThe search results don't explicitly contrast a separate \"answer content probe\" distinct from correctness probing. If you're looking for information about a specific paper or framework that makes this distinction, you may need to provide additional context or search terms."
    ],
    "durationSeconds": 9.875787245999993,
    "searchCount": 2
  },
  "sourceToolAssistantUUID": "474230ae-0f62-448e-844e-58846768fac8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-20T03:53:04.735Z_

I now have sufficient research context to provide a thorough analysis. Let me synthesize my findings.

---

【状态】: 有发掘空间

【前置调研发现】
- **Chrabąszcz et al. (2605.18549)**: The closest concurrent work on probe trajectories. Tracks temporal probe dynamics with 60+ signal-processing features, achieving up to 17pp improvement over static probes. Critically, NO causal contribution component, NO gap metric, NO probe calibration. This validates the probe-trajectory direction but leaves the entire C(t) dimension untouched — confirming the proposal's core niche is real.
- **Yuan et al. (2605.09502)**: Establishes the "diagnostic not causal" finding decisively across 4 intervention strategies, 6 model families, up to 72B. The intervention failure is comprehensive and model-scale-spanning. This is the strongest empirical anchor for the proposal's motivating observation.
- **Cox et al. (2603.01437)**: Answer-content probes on binary tasks succeed in steering instruction-tuned models (>50% flip rate) but fail on reasoning models. The instruction-tuned vs. reasoning-model contrast is sharp and well-documented.
- **Wang (2604.15726)**: Formalizes H1/H2/H0 hypotheses. A position/theory paper without empirical implementation — the ICG framework would be the first empirical operationalization of the H1/H2 distinction at token-level temporal resolution.
- **Gjølbye et al. (2605.15454)**: Demonstrates difficulty-geometry coupling with critical methodological contribution (length correction). Domain-specific effects (strong in code, weak in math) add important nuance.
- **Ballon et al. (2601.23163)**: Provides the C(t) measurement protocol via truncation-reinjection with rigorous controls. Explicitly disclaims faithfulness analysis — directly setting up the proposal's integration opportunity.
- **Chun et al. (2602.20338, MCT)**: "Geometric pulse" finding shows probe accuracy overestimates information availability — strong justification for null-probe calibration.
- **Kudo et al. (EACL 2026)** and **CMI framework (2602.03994)**: The only two prior works combining probing + causal intervention, but limited to synthetic arithmetic / ~50 examples. Neither provides temporal coverage, phenomenon mapping, or multi-model comparison.
- **调研总结**: The field is converging rapidly on the observation that probing and causal intervention tell different stories for reasoning models. Multiple groups have independently built components (probe trajectories, truncation protocols, intervention failure catalogs) but nobody has unified them into a temporal gap framework. The proposal occupies a genuine gap. However, the field is moving fast — the window for this contribution is narrowing.

---

【发掘点 1】
- 维度: 核心 claim 强化
- 内容: The proposal's core claim — "the gap IS the faithfulness signal" — is philosophically compelling but needs to be made more operationally precise to survive reviewer scrutiny. Currently, the gap G*(t) = P*(t) − C(t) subtracts two quantities measured on fundamentally different scales and via fundamentally different methods: P*(t) is a calibrated probe AUROC (a measure of linear separability in hidden-state space), while C(t) is a behavioral accuracy change under truncation/perturbation. Subtracting these is like subtracting temperature from humidity — they are both numbers, but the difference's meaning is not self-evident. The proposal should explicitly address why this subtraction is meaningful, not just algebraically possible. The strongest version of the claim would be: "We don't need the subtraction to be a calibrated scalar — we need the *temporal profile* of the gap (shape, convergence, divergence) to be the diagnostic signal." This reframes the contribution from "we measure a number G*(t)" to "we identify temporal trajectory signatures in the divergence between two independently meaningful measurement streams." This is actually what the proposal already does in practice (phenomenon signatures are about shapes, not absolute values), but the framing buries this insight under the algebra.
- 价值: This strengthens the core claim against the most predictable reviewer attack: "What does it mean to subtract AUROC from accuracy?" By front-loading the "shapes not magnitudes" framing, the paper preempts this criticism and actually elevates the contribution — trajectory-shape analysis is more robust than absolute-value comparison (as the entropy trajectory literature confirms: shape predicts reliability regardless of absolute levels).
- 调研依据: The entropy trajectory paper (2603.18940) and trajectory-shape literature (Microsoft 2604.05655) validate that shape features are more diagnostic than absolute values. This directly supports reframing G*(t) as a trajectory-shape diagnostic rather than a calibrated scalar metric.

【发掘点 2】
- 维度: novelty 锐化
- 内容: The proposal positions itself against Chrabąszcz et al. (2605.18549) by claiming "we add the causal contribution dimension." This is accurate but undersells the actual novelty differential. The deeper insight is: Chrabąszcz et al. answer "what does the model know over time?" while this framework answers "what does the model know over time AND fail to channel into its reasoning?" This is the difference between a diagnostic tool and a *faithfulness diagnostic* — a qualitative leap, not an incremental extension. The proposal should sharpen this distinction by explicitly noting: Chrabąszcz et al.'s probe trajectories can distinguish correct from incorrect reasoning (outcome prediction), but they cannot distinguish faithful-correct from unfaithful-correct reasoning (faithfulness diagnosis). A model that pre-encodes the answer and generates decorative CoT would look identical to a model that genuinely reasons in Chrabąszcz et al.'s framework (both have high probe accuracy throughout), but would look radically different in the ICG framework (the former has G*(t) >> 0 throughout, the latter has G*(t) converging to 0). This specific example should appear in the paper as the motivating illustration.
- 价值: This sharpens the novelty claim from "we add a component" (incremental) to "we can make a distinction that the closest prior work fundamentally cannot" (qualitative gap). This is a much stronger pitch to reviewers on the Novelty dimension.
- 调研依据: Directly based on Chrabąszcz et al. (2605.18549) — their framework explicitly targets outcome prediction (correctness, harmfulness), NOT faithfulness diagnosis. The faithful-correct vs. unfaithful-correct blindspot is structurally guaranteed by their single-stream (probe-only) design.

【发掘点 3】
- 维度: significance 提升
- 内容: The proposal currently frames significance primarily in terms of faithfulness measurement — understanding when models are being faithful vs. unfaithful. This is important but somewhat academic. There is a much stronger significance angle hiding in the difficulty-conditioning component: **the ICG framework can answer a practical question that the field urgently needs answered: "For this model, on this task type, at what difficulty threshold does CoT transition from decorative overhead to genuine cognitive contribution?"** This has direct implications for (a) inference-time compute allocation (don't generate CoT for easy problems where G*(t) >> 0 — it's wasted compute), (b) safety monitoring (if G*(t) >> 0, the model is concealing its actual reasoning process, which is an alignment concern), and (c) benchmark design (problems where all models show G*(t) >> 0 are not testing reasoning, regardless of accuracy scores). The safety angle is particularly compelling: Yuan et al.'s finding that the error signal is "diagnostic not causal" means models have an internal quality-monitoring system that is decoupled from their output — this is exactly the kind of hidden computation that alignment researchers worry about.
- 价值: This elevates the paper from "faithfulness measurement contribution" to "practical implications for compute efficiency, safety monitoring, AND benchmark validity." Hitting all three amplifies significance substantially.
- 调研依据: Based on the convergence of Li et al. (2510.22362, easy→decorative, hard→faithful), Gjølbye et al. (2605.15454, domain-specific difficulty coupling), and Yuan et al. (2605.09502, the alignment implication of decoupled internal monitoring). The safety/alignment framing is particularly timely given the field's growing concern about reasoning model opacity.

【发掘点 4】
- 维度: 前提假设质疑
- 内容: There is a non-trivial assumption in the framework that requires explicit acknowledgment: **P*(t) and C(t) are measuring the same latent quantity at different levels of abstraction.** The implicit claim is that when P*(t) > C(t), the "extra" information in P*(t) represents knowledge that *could have been* channeled through CoT but wasn't. However, this assumes that probe-detectable information is of the right *kind* to be expressible in CoT text. It's possible that some probe-detectable signals are computational byproducts (e.g., intermediate activations that correlate with correctness as a statistical regularity rather than representing "knowledge" in any semantically meaningful sense). Chun et al.'s MCT finding — that geometric separability peaks transiently while probe accuracy remains high — suggests exactly this: some of what probes detect may be residual activation patterns rather than actionable knowledge. The framework's null-probe calibration addresses inflation but not this deeper issue of *interpretability of the gap*. The proposal should add a brief section acknowledging this: "G*(t) >> 0 means correctness-correlated information is present but not causally used; it does not necessarily mean the model 'decided to withhold' this information — the information may not be in a form that the generation process can access." This honest caveat actually strengthens the paper by blocking a reviewer from raising it as a fatal flaw.
- 价值: Explicitly addressing this assumption converts a potential reviewer rejection point ("your gap might be meaningless because probes detect artifacts") into a nuanced discussion point ("we acknowledge this interpretive boundary and propose MCT validation as a partial mitigation"). This is Related Work/Soundness dimension.
- 调研依据: Chun et al. (2602.20338) — the geometric pulse finding directly demonstrates that probe-detectable information and geometrically organized (actionable) information can diverge. Hewitt & Liang (2019) and Ravichander et al. (2020) established the foundational concern about probe inflation. The proposal cites all of these but doesn't explicitly confront the *interpretive* implication for the gap metric.

【发掘点 5】
- 维度: trivial alternative 威胁
- 内容: A reviewer could ask: "Why not just measure the correlation between pre-CoT probe accuracy and final answer correctness? If the correlation is high, CoT is decorative; if low, CoT contributes. Why do we need the full temporal G*(t) framework?" This is a genuine trivial-alternative threat. The proposal needs to explicitly articulate why the temporal trajectory matters beyond the endpoint comparison. The strongest argument is: **the temporal shape reveals the *mechanism* of unfaithfulness, not just its presence.** Pre-CoT encoding and post-hoc rationalization both produce high probe accuracy + low causal contribution, but they produce different G*(t) shapes (constant-high vs. widening). This mechanistic discrimination is impossible from a single-timepoint comparison. Additionally, the "genuine reasoning with late failure" phenomenon (model reasons faithfully for 80% of the chain, then shortcuts at the end) would show G*(t) ≈ 0 then G*(t) spiking — invisible to any static measurement. The proposal partially makes this argument through the phenomenon signatures but should lead with it as the primary justification for temporal resolution.
- 价值: Preemptively defuses the "over-engineering" criticism. The temporal framework's value is not just measurement precision — it's the ability to distinguish between failure *modes*, which a simpler approach collapses into a single "unfaithful" label. This is core Novelty defense.
- 调研依据: Based on the overall architecture of the proposal's phenomenon signatures. The entropy trajectory paper (2603.18940) provides external validation that trajectory shapes carry information beyond endpoints. The RQA analysis (2602.06266, temporal features outperform aggregates 36.94% vs. 28.97%) provides quantitative evidence.

【发掘点 6】
- 维度: related work 差异化
- 内容: The proposal extensively positions against Chrabąszcz et al., but underplays a potentially important differentiator from the CMI framework (Sathyanarayanan et al., 2602.03994). CMI measures causal mediation via layerwise activation patching — it *does* combine probing with causal intervention, which partially overlaps with the ICG claim. The proposal dismisses CMI for operating on "~50 examples" and lacking temporal resolution, which is true but superficial. The deeper differentiation is: CMI measures whether the *answer's latent representation* passes through CoT-aligned layers (a structural/architectural question: "does the computational path go through CoT?"), while ICG measures whether the *information that the model possesses* is reflected in the *behavioral causal contribution* of CoT text (a functional question: "does the CoT text carry the model's knowledge?"). These are genuinely different questions — a model could have high CMI (answer representations pass through CoT-processing layers) but high G*(t) (the CoT text itself doesn't causally contribute to correctness), if the computational path through those layers uses the CoT as a timing scaffold rather than for its semantic content. This distinction should be sharpened.
- 价值: The CMI overlap is a likely reviewer concern. Clarifying the structural-vs-functional distinction preemptively closes this attack vector and further sharpens the novelty claim. This is Related Work dimension.
- 调研依据: CMI framework (2602.03994) — the paper proposes layerwise activation patching to compute a "CoT Mediation Index," which measures representation-level mediation. The functional distinction from ICG's behavioral-level measurement is implicit in both papers but not explicitly articulated anywhere.

Sources:
- [Monitoring the Internal Monologue: Probe Trajectories (Chrabąszcz et al.)](https://arxiv.org/abs/2605.18549)
- [Hidden Error Awareness (Yuan et al.)](https://arxiv.org/abs/2605.09502)
- [Decoding Answers Before CoT (Cox et al.)](https://arxiv.org/abs/2603.01437)
- [LLM Reasoning Is Latent (Wang)](https://arxiv.org/abs/2604.15726)
- [Reasoning Models Move Differently (Gjølbye et al.)](https://arxiv.org/abs/2605.15454)
- [Probing Trajectories of Reasoning Traces (Ballon et al.)](https://arxiv.org/abs/2601.23163)
- [Emergent Manifold Separability / MCT (Chun et al.)](https://arxiv.org/abs/2602.20338)
- [Therefore I am. I Think (Esakkiraja et al.)](https://arxiv.org/abs/2604.01202)
- [FaithCoT-Bench (ICLR 2026)](https://arxiv.org/abs/2510.04040)
- [Bypassing the Rationale / CMI Framework](https://arxiv.org/abs/2602.03994)
- [Mechanistic Evidence for Faithfulness Decay / NLDD (Ye et al.)](https://arxiv.org/abs/2602.11201)
- [Why Models Know But Don't Say (Young)](https://arxiv.org/abs/2603.26410)
- [Lie to Me (CoT Faithfulness)](https://arxiv.org/abs/2603.22582)
- [Reasoning Models Know When They're Right (Zhang et al.)](https://arxiv.org/abs/2504.05419)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f5546d5-c01c-4c45-a433-09f83e1bb6f0",
  "isSidechain": false,
  "requestId": "req_011CbD98huHrA6xDpDST8fyv",
  "type": "assistant",
  "uuid": "7c48613d-fad4-4d6b-8372-02b5161c9fcf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KjkMkTXod1mDfyq4W9mKvL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1458,
      "cache_read_input_tokens": 40708,
      "output_tokens": 3820,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1458,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3820,
          "cache_read_input_tokens": 40708,
          "cache_creation_input_tokens": 1458,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1458
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

_source line 56_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness  ## Description We propose the Information-Contribution Gap (ICG)…",
  "leafUuid": "7c48613d-fad4-4d6b-8372-02b5161c9fcf",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "ai-title",
  "aiTitle": "Measuring calibrated temporal information-contribution gaps in chain-of-thought reasoning",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b"
}
```

---

### Runtime record

_source line 58_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Measuring What Models Know But Don't Use: Calibrated Temporal Information-Contribution Divergence for Chain-of-Thought Faithfulness  ## Description We propose the Information-Contribution Gap (ICG)…",
  "leafUuid": "7c48613d-fad4-4d6b-8372-02b5161c9fcf",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b"
}
```

---

### Runtime record

_source line 59_

```json
{
  "type": "ai-title",
  "aiTitle": "Measuring calibrated temporal information-contribution gaps in chain-of-thought reasoning",
  "sessionId": "bf74d8b1-2e3a-4d06-8889-9a66e097ba2b"
}
```

---
