# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-19 (UTC).** ## Original idea { "tit

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/a600395c-52af-4483-884f-a0137eaa6f5f.jsonl`
- **Structured JSON:** [`b80fbf1e274218a17960.json`](../../sessions/b8/b80fbf1e274218a17960.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T12:00:31.834Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T12:00:31.834Z",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-19 (UTC).**\n\n## Original idea\n{\n  \"title\": \"The Probe-Intervention Gap: Diagnosing Chain-of-Thought Faithfulness via Dual-Estimator Temporal Information Decomposition\",\n  \"project_name\": \"cot_faithfulness_decomp\",\n  \"source\": \"web_research\",\n  \"level\": \"top-tier\",\n  \"target_venues\": [\n    \"ICLR 2027 (abstract: Sep 19, full paper: Sep 24, 2026; conference: Apr/May 2027 — primary target, 4 months from now)\",\n    \"ICML 2027 (full paper: Jan 29, 2027; conference: Jul 2027 — comfortable fallback if additional experiments needed)\"\n  ],\n  \"core_problem\": \"Multiple independent findings in 2025-2026 — Reasoning Horizon, pre-CoT answer encoding, Reasoning Theater, myopic planning, thinking-answer gap — all describe facets of the same underlying problem: models' chain-of-thought reasoning is partially or entirely decorative. While the CoT faithfulness literature has catalogued these phenomena (Jin et al.'s survey; FaithCoT-Bench at ICLR 2026) and several groups have measured temporal dynamics of individual signals, no work has unified these disparate phenomena under a single information-theoretic framework that explains WHY and WHEN each occurs. Crucially, recent work reveals that the relationship between faithfulness and task difficulty is not binary: CoT transitions from decorative to load-bearing as task difficulty increases ('Task Difficulty Shapes CoT Faithfulness,' ICLR 2026 Workshop), with error propagation ranging from 22% on MMLU to 41% on BBH. This difficulty gradient — detectable via hidden-state probes but resistant to single-direction steering ('readout rather than control') — demands a diagnostic framework that can characterize faithfulness along both temporal and difficulty dimensions. The closest precedents — Kudo et al.'s (EACL 2026) probing + activation patching on synthetic arithmetic, the CMI framework's layerwise causal audit on ~50 examples, Zhao et al.'s (2510.24941) True Thinking Score providing per-step causal contribution on AIME/MATH, and Furuya & Tanimura's (2605.01853) training-free StALT trajectory statistic — each capture one dimension of the problem but none provides a dual-estimator framework that jointly measures internal information and causal contribution across the full CoT timeline on natural benchmarks.\",\n  \"opportunity\": \"The field has independently produced three complementary measurement paradigms: (1) probe-based approaches revealing what the model internally represents at each CoT position (David 2511.14773: correctness decodable at t=4 tokens; Cox et al. 2603.01437: pre-CoT probes at >0.9 AUC with causal validation via steering on instruction-tuned models up to 9B; Esakkiraja et al. 2604.01202: pre-generation probes with >90% AUROC; Furuya & Tanimura 2605.01853: training-free StALT separating correct from incorrect trajectories), (2) intervention-based approaches measuring what the CoT text causally contributes (Ye et al. 2602.11201: NLDD reveals Reasoning Horizon at 70-85%; Zhao et al. 2510.24941: True Thinking Score provides per-step ATE on AIME/MATH/AMC/CommonsenseQA, finding only 2.3% of AIME steps have TTS≥0.7; Basu & Chakraborty 2603.22816: decorative/scaffolding/genuine taxonomy), and (3) diagnostic approaches characterizing CoT pathologies (Liu et al. 2602.13904: text-level metrics for rationalization/encoded/internalized reasoning via model organisms; 'Task Difficulty Shapes CoT Faithfulness' ICLR 2026 Workshop: difficulty-dependent faithfulness gradient). Two prior works have combined probing with causal interventions on the same instances: Kudo et al. (2412.01113, EACL 2026) train linear probes and perform activation patching across arithmetic CoT; the CMI framework (2602.03994) measures CoT-mediated causal influence via layerwise patching. However, neither provides: (a) full temporal-position coverage across CoT on natural benchmarks, (b) a mapping to the five named faithfulness phenomena, (c) a standalone instance-level diagnostic score, (d) systematic multi-model comparison on realistic reasoning tasks, or (e) robustness validation across measurement methodologies — a critical gap highlighted by Young's (2603.20172) finding that faithfulness measurements are classifier-sensitive (inter-classifier kappa as low as 0.06). The opportunity is to extend the probe-intervention combination paradigm to a systematic dual-estimator Temporal Information Curve (TIC) framework producing a 2D faithfulness signal — the gap between probe-estimated internal information and intervention-estimated causal contribution — on natural benchmarks at scale, with explicit robustness validation.\",\n  \"landscape\": \"**Probe-intervention combinations (closest prior work).** Kudo et al. (2412.01113, EACL 2026) train per-position linear probes on hidden states and validate with sliding-window activation patching on 9 models across synthetic multi-step arithmetic. They find CoT IS faithful for arithmetic but explicitly note their synthetic setting may not generalize to 'more realistic reasoning tasks in natural language.' The CMI framework (2602.03994) introduces the CoT Mediation Index via layerwise activation patching across Phi, Qwen, and DialoGPT on StrategyQA (20 examples), TruthfulQA (10), and GSM8K (20), identifying 'bypass regimes' where CMI ≈ 0. Both are complementary precursors.\\n\\n**Per-step causal contribution (direct Causal-TIC precursor).** Zhao et al. (2510.24941, Oct 2025, revised Apr 2026) introduce the True Thinking Score (TTS), measuring per-step causal contribution via text-level perturbation (numerical offsets preserving grammar) and ATE computation. On DeepSeek-R1-Distill-Qwen-7B/14B/Llama-8B across AIME, MATH, AMC, CommonsenseQA, they find only 2.3% of AIME steps have TTS≥0.7. TTS also extracts a 'TrueThinking direction' from hidden states for steering (53.6-91.2% flip rates). TTS is a direct precursor to our Causal-TIC component. Key differentiators: TTS operates at discrete step granularity (not continuous temporal), is a single-estimator metric (no probe gap), uses text-level perturbation (vs. our NLDD logit degradation), and does not map to the five faithfulness phenomena or provide an instance-level diagnostic score grounded in the probe-intervention divergence. Our framework extends TTS's causal measurement from per-step to continuous temporal coverage and pairs it with the Probe-TIC for the gap diagnostic unavailable from either estimator alone.\\n\\n**Training-free temporal hidden-state dynamics (concurrent work adjacent to Probe-TIC).** Furuya & Tanimura (2605.01853, May 2026) introduce StALT (Spatiotemporal Amplitude of Latent Transition), a training-free trajectory statistic that separates correct from incorrect reasoning trajectories by tracking hidden-state transitions across decoding steps and layers. Tested on GSM8K, MATH-500, and GPQA. StALT is conceptually adjacent to our Probe-TIC in tracking temporal hidden-state evolution. Key differentiators: StALT targets correctness separation (not faithfulness diagnosis), is training-free (vs. our trained answer-content probes targeting specific answer information), lacks a causal intervention component (no gap diagnostic), and does not map to faithfulness phenomena. Our Probe-TIC complements StALT by probing for answer content specifically and pairing it with causal interventions.\\n\\n**Latent-trajectory signals for efficiency.** Vilas et al. (2510.10494, ICLR 2026) define three latent-trajectory signals — net change, cumulative change, and aligned change — tracking hidden-state evolution across 500-token segments. On DeepSeek-R1-Distill-Qwen-14B, Phi-4-Reasoning-Plus, and Qwen3-14B across GPQA Diamond, AIME 2025, and TSP, they achieve 14-70% token savings and +2.6% accuracy gains via early selection of productive reasoning paths. Focuses on efficiency (correctness prediction for compute allocation), not faithfulness. Adjacent methodology but orthogonal goal; reinforces that temporal hidden-state signals are informative, motivating our faithfulness-specific application.\\n\\n**The diagnostic-not-causal challenge.** Yuan et al. (2605.09502, May 2026) show that probes detecting *trace correctness* achieve 0.95 AUROC but four interventions fail, concluding error representations are 'fundamentally different from editable factual knowledge representations.' Cox et al. (2603.01437) demonstrate that *answer-content* probe directions are causally potent on instruction-tuned models: steering flips >50% of answers. However — and this is a critical limitation acknowledged in this revision — Cox et al.'s validation is restricted to binary classification tasks (Anachronisms, Logical Deduction, Sports Understanding, Social Chemistry) on models up to 9B parameters, and they explicitly note that for reasoning models, they find 'some success using probes to linearly decode the final answer, but little success steering to change it.' This means the causal potency of answer-content probes on reasoning models (our target model class) is NOT yet established. The 'Task Difficulty Shapes CoT Faithfulness' workshop paper independently reaches a similar conclusion: hidden-state probes are 'readout rather than control.' We therefore reframe: the Probe-TIC captures information availability (an upper bound on what the model 'knows' at each position), regardless of whether that representation is directly steerable. The gap G(t) between information availability and causal contribution remains diagnostic of reasoning quality under this weaker but more honest assumption.\\n\\n**CoT pathology diagnostics.** Liu et al. (2602.13904, Feb 2026) propose text-level, computationally inexpensive, task-agnostic metrics for three CoT pathologies: Necessity (rationalization), Paraphrasability (encoded reasoning), and Substantivity (internalized reasoning), validated on model organisms (Olmo-3-7B-Think trained to exhibit pathologies). Their approach is complementary to ours: purely text-level (no hidden states), uses model organisms (not natural models), categorical per-pathology metrics (not continuous temporal curves), and lacks the dual-estimator gap. Our framework provides mechanistic grounding via hidden states that their text-level metrics cannot.\\n\\n**Measurement sensitivity.** Young (2603.20172, Mar 2026) shows faithfulness measurements are classifier-sensitive: inter-classifier kappa as low as 0.06 for sycophancy hints, with up to 30.6 percentage-point divergence across three classifiers on 10,276 traces from 12 models. This raises a methodological concern directly applicable to our framework: TIF will likely show sensitivity to probe layer selection, probe architecture, NLDD perturbation method, and gap normalization. We address this by planning explicit robustness ablations across these measurement dimensions and reporting sensitivity ranges rather than single aggregate numbers.\\n\\n**Task-difficulty moderation of faithfulness.** 'Task Difficulty Shapes CoT Faithfulness' (ICLR 2026 Workshop) demonstrates that CoT transitions from decorative to load-bearing as task difficulty increases: error propagation rises from 22% on MMLU to 41% on BBH, with 7× variation within MMLU subjects. Hidden-state probes detect this gradient but single-direction steering cannot shift it ('readout rather than control'). This finding has two critical implications for our framework: (1) the five faithfulness phenomena may be differentially expressed across task difficulties, enriching our unification thesis with a difficulty dimension; (2) independent confirmation that probes are diagnostic instruments, not interventional tools, supporting our thermometer framing.\\n\\n**Probe-based temporal measurement.** Qian et al. (2506.02867, NeurIPS 2025) compute per-token HSIC between hidden representations and golden answers, discovering MI peaks at thinking tokens. David (2511.14773) trains linear classifiers at prefix lengths t=4...512, showing correctness is decodable early. Zhang et al. (2504.05419) probe hidden states at intermediate answer positions for early-exit (24% savings). Lewis-Lim et al. (2508.19827, EMNLP 2025) track answer confidence trajectories, revealing flat (rationalization) vs. increasing (genuine reasoning) patterns. Mirtaheri & Belkin (2603.17199) show pre-generation probes match full-CoT monitors. Esakkiraja et al. (2604.01202) show pre-generation probes predict tool-calling at >90% AUROC.\\n\\n**Intervention-based causal measurement.** Ye et al. (2602.11201) introduce NLDD, revealing Reasoning Horizon at 70-85%. Basu & Chakraborty (2603.22816) propose genuine/scaffolding/decoration taxonomy via step ablation. Somov et al. (2603.16475) show up to 60% failure to update after intervention. FACT-E (2604.10693, ACL Findings 2026) uses controlled perturbations.\\n\\n**Probing and steering faithfulness.** Occhipinti et al. (ICLR 2026 LIT Workshop) demonstrate that faithfulness is encoded as linear directions in middle-to-late layers, with probing F1 scores of 90-100% at peak layers and steering achieving 46% monitorability recovery with <5% collateral effects. This provides complementary evidence that faithfulness has a linear geometric signature exploitable by probes.\\n\\n**Geometric and information-theoretic approaches.** Chun et al. (2602.20338) apply Manifold Capacity Theory revealing transient geometric pulses. Alvarez & Baheri (2605.13772, May 2026) detect step-level hallucination via hidden-state transport geometry. Ton et al. (ICML 2025, 2411.11984) define per-step information gain. Anwar et al. (2602.18297) decompose monitorability into information gap + elicitation error.\\n\\n**Faithfulness benchmarks and surveys.** FaithCoT-Bench (ICLR 2026, 2510.04040). Jin et al.'s survey (submitted to ARR for ACL 2026; no public arXiv version). Young (2603.26410): 55.4% thinking-only acknowledgment. 'Lie to Me' (2603.22582): 87.5% vs 28.6% thinking vs answer.\\n\\n**Early-exit methods.** Reasoning Theater (2603.05488: 80% savings), ESTAR (2602.10004), DTSR (2604.06787: 28.9-34.9%), NEAT (2602.02010), CoDE-Stop (2604.04930), Zhang et al. (2504.05419: 24%), FRIT (2509.13334).\\n\\n**What remains open.** No extant framework provides: (1) a full-timeline dual-estimator curve combining answer-content probes with causal interventions on natural benchmarks at scale; (2) a systematic mapping of five phenomena to distinguishable signatures within such a framework, conditioned on task difficulty; (3) an instance-level diagnostic score derived from the probe-intervention gap with explicit robustness validation across measurement methodologies; or (4) a principled account of how the probe-intervention gap behaves differently on instruction-tuned vs. reasoning models. TTS provides per-step causal contribution (single-estimator, text-level); StALT provides temporal hidden-state correctness signals (single-estimator, no causal component); Vilas et al. provide latent-trajectory efficiency signals (no faithfulness connection); Liu et al. provide text-level pathology diagnostics (no hidden states). The dual-estimator gap — jointly measuring internal information and causal contribution across the full timeline — remains the unique contribution.\",\n  \"inspired_by\": \"The convergence of four observations: (a) Kudo et al.'s demonstration that probe+intervention combination is feasible and informative on synthetic arithmetic, with their explicit call for natural-task extension; (b) Zhao et al.'s (2510.24941) TTS demonstrating per-step causal contribution measurement at scale on our exact target benchmarks (AIME, MATH), establishing the causal-contribution paradigm we extend to continuous temporal coverage with the dual-estimator gap; (c) the finding from both Cox et al. (2603.01437) on instruction-tuned models and the 'Task Difficulty' workshop paper that probes are diagnostic ('readout') rather than interventional ('control') — which, rather than undermining probe-based faithfulness work, clarifies that the Probe-TIC should be interpreted as an information-availability signal, making the framework more honest and defensible; (d) Young's (2603.20172) demonstration that faithfulness measurements are classifier-sensitive, motivating our explicit robustness ablation plan.\",\n  \"approach\": \"Define a dual-estimator Temporal Information Curve (TIC) framework that diagnoses chain-of-thought faithfulness at each token position t via two complementary signals:\\n\\n**(a) Probe-TIC P(t)**: Information about the answer decodable from residual-stream activations h_{1:t} via linear probes trained on 3-5 selected layers. Critically, we probe for *answer content* (which answer option / numerical value the model will produce), not binary correctness. On instruction-tuned models, Cox et al. (2603.01437) demonstrate such probes are causally potent (steering flips >50% of answers). However, Cox et al.'s validation is limited to binary tasks on models ≤9B, and they explicitly report that reasoning models resist steering. We therefore interpret the Probe-TIC as measuring *information availability* — an upper bound on what the model internally represents at each position — rather than assuming causal potency. This interpretation is independently supported by the 'Task Difficulty Shapes CoT Faithfulness' finding that probes are 'readout rather than control,' and is consistent with the training-free trajectory statistics of Furuya & Tanimura (2605.01853) which also show hidden-state signals are diagnostic of reasoning quality.\\n\\n**(b) Causal-TIC C(t)**: Causal contribution of CoT_{1:t} to the answer via NLDD-style interventions (corrupting CoT segments and measuring logit degradation). This extends the single-model NLDD paradigm (Ye et al. 2602.11201) to systematic multi-model comparison with continuous temporal coverage, and provides a continuous temporal generalization of the per-step TTS metric (Zhao et al. 2510.24941). Where TTS applies text-level perturbation at discrete step boundaries with ATE computation, our Causal-TIC applies NLDD logit degradation at each token position, yielding a continuous curve that captures within-step dynamics invisible to TTS.\\n\\n**The Faithfulness Gap as a Diagnostic Signal.** The core diagnostic is G(t) = P(t) − C(t). We characterize this gap under a *weaker but more honest assumption* than previous versions: the Probe-TIC measures information availability (what the model knows at position t), not necessarily causally determinative information. This means:\\n- G(t) ≈ 0 is a *necessary condition* for faithfulness: if available internal information and CoT causal contribution are aligned, CoT is faithful.\\n- G(t) >> 0 indicates *information excess* — the model possesses answer information not causally contributed by CoT text. This is suspicious but not proof of unfaithfulness (the 'thermometer reading' scenario).\\n- Critically, even under this weaker assumption, the gap is diagnostic: the PATTERN of G(t) across time, tasks, and difficulty levels reveals which of the five phenomena is operative, which is the framework's primary contribution.\\n\\nThis diagnostic framing is independently supported by three convergent findings: (1) Yuan et al. (2605.09502) show correctness probes are diagnostic-not-causal; (2) the 'Task Difficulty' workshop shows probes are 'readout rather than control'; (3) Occhipinti et al. (ICLR 2026 LIT Workshop) show faithfulness steering achieves only 46% recovery. The thermometer interpretation — invaluable for diagnosis, not intended for intervention — is the honest and defensible framing.\\n\\n**Pilot Validation of Probe Causal Potency (Phase 0).** Before running full experiments, we conduct a targeted pilot on 500 examples across MMLU (4-choice) and GSM8K (numerical) using DeepSeek-R1-Distill-Qwen-7B: train answer-content linear probes on pre-CoT and mid-CoT hidden states, then test steering along probe directions at varying strengths. This tests the falsifiable prediction that answer-content probes retain some causal potency on reasoning models for multi-choice (not just binary) tasks — or, if steering fails, validates the information-availability interpretation and calibrates how loose the upper bound is. This pilot addresses the Tier-1 risk of extrapolating Cox et al.'s binary-task findings to our setting.\\n\\n**Diagnostic Features.** Derive four features from the dual-TIC:\\n(i) Initial probe value P(0) — detects pre-CoT encoding (high P(0) with any C trajectory).\\n(ii) Causal-TIC plateau onset t* — captures the Reasoning Horizon (C(t) saturates).\\n(iii) Gap trajectory G(t) over time — distinguishes Reasoning Theater (growing gap: P rises, C stays flat) from genuine reasoning (stable near-zero gap).\\n(iv) Locality of Causal-TIC gradients — short- vs. long-range correlations in dC/dt capture myopic vs. global planning.\\n\\n**Task-Difficulty Conditioning.** Following the 'Task Difficulty Shapes CoT Faithfulness' finding, we analyze dual-TIC signatures stratified by task difficulty (using model confidence on first pass as a difficulty proxy). We predict: (a) easy instances show high P(0) with flat C(t) (pre-CoT encoding / decoration); (b) moderate instances show Reasoning Horizon signatures (C(t) plateau); (c) hard instances show increasing P(t) and C(t) trajectories (genuine reasoning). This difficulty conditioning enriches the five-phenomena unification with a sixth predictive variable.\\n\\n**Robustness Ablations.** Motivated by Young (2603.20172), who shows inter-classifier kappa as low as 0.06 for faithfulness measurements, we plan explicit robustness ablations: (a) probe architecture (linear vs. 2-layer MLP); (b) layer selection (best-3 vs. best-5 vs. all layers); (c) NLDD perturbation method (Gaussian corruption vs. token replacement vs. segment shuffling); (d) gap normalization (raw difference vs. ratio vs. area-under-curve). We report sensitivity ranges for TIF scores across these axes, following Young's recommendation for multi-method validation.\\n\\n**Experiments.** Core experiments target DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Qwen-14B, DeepSeek-R1-Distill-Qwen-32B, and QwQ-32B across four benchmarks (MMLU, GPQA-Diamond, GSM8K, AIME), with a targeted validation run on DeepSeek-R1-671B (500-example subset, 3 layers). Layer-selective activation caching (5 layers from pilot study on 7B) keeps storage at ~3-5 TB. As a calibration check, we include Kudo et al.'s synthetic arithmetic as a control condition where we expect G(t) ≈ 0. As an additional calibration, we cross-reference TTS values from Zhao et al. on overlapping benchmarks (AIME, MATH) to validate Causal-TIC against the established per-step metric.\\n\\n**Primary Output: Temporal Information Fidelity (TIF) Score.** An instance-level diagnostic score computed as the normalized area under the gap curve G(t). TIF is explicitly framed as a diagnostic signal grounded in the information asymmetry between what hidden states encode and what CoT text causally contributes. Benchmarked against FaithCoT-Bench expert annotations and cross-validated against Liu et al.'s (2602.13904) text-level pathology metrics (Necessity, Paraphrasability, Substantivity) on overlapping examples. We hypothesize TIF correlates with but does not perfectly predict expert annotations, because TIF captures potential for unfaithfulness (information availability mismatch) while experts judge realized unfaithfulness (information misuse).\\n\\n**Secondary Output: Causal Sufficiency Stopping Criterion.** As a secondary application, we derive an early-exit criterion keyed to the Causal-TIC's inflection point. Benchmarked against existing methods but positioned as a practical byproduct, not a standalone contribution.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"600 H100-hours (300 for distilled-model inference with layer-selective activation caching on 4 models × 4 datasets + synthetic arithmetic control; 150 for NLDD causal interventions across 10-20 perturbation passes per model; 50 for probe training, Phase 0 pilot, and TIF-FaithCoT-Bench validation; 50 for robustness ablations across 4 measurement dimensions; 50 for 671B validation subset on 8×H100 node)\",\n      \"timeline\": \"4 months (2 researchers: 2 weeks Phase 0 pilot (probe causal potency validation on 7B) + probing pipeline via nnsight + layer-selection study + synthetic arithmetic calibration, 7 weeks core dual-estimator experiments across 4 models × 4 datasets with task-difficulty stratification, 3 weeks TIF validation against FaithCoT-Bench + Liu et al. metrics + phenomenon mapping, 2 weeks robustness ablations + TTS cross-reference, 2 weeks writing)\",\n      \"estimated_gpu_cost\": \"$1,500 (at ~$2.50/H100-hr avg via RunPod/Lambda spot pricing, May 2026 rates)\",\n      \"storage\": \"3-5 TB for layer-selective activation caching (5 layers per model, fp16); reducible to ~1.5 TB via PCA to 25% dimensionality\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"500 H100-hours (Claude accelerates probing pipeline, NLDD implementation, analysis scripts, reducing iteration overhead ~20%)\",\n      \"timeline\": \"3.5 months (1 researcher + Claude: 2 weeks Phase 0 pilot + pipeline setup + synthetic arithmetic calibration, 6 weeks core experiments with difficulty stratification, 2 weeks TIF validation + phenomenon mapping + robustness ablations, 2 weeks TTS cross-reference + paper drafting)\",\n      \"claude_api_cost\": \"$400 (code generation for probing/intervention/ablation pipelines, automated result analysis, paper drafting; ~80M input + 20M output tokens via Sonnet 4.6)\",\n      \"estimated_gpu_cost\": \"$1,250\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"500 H100-hours (same computational footprint; experiment is GPU-bound not code-bound)\",\n      \"timeline\": \"3 months (Claude drives experiment design, implementation, analysis, and full draft; human provides weekly steering and final review)\",\n      \"claude_api_cost\": \"$800 (extensive pipeline generation, hyperparameter sweeps, robustness ablation design, automated result interpretation, full paper draft; ~160M input + 40M output tokens)\",\n      \"estimated_gpu_cost\": \"$1,250\",\n      \"speed_bottleneck\": \"NLDD interventions on 32B models require multiple forward passes (10-20 per example) at ~15 tok/s on 2×H100; ~250 node-hours for 20K examples across 4 datasets + arithmetic control dominate wall-clock time. 671B validation subset requires 8×H100 node. Robustness ablations add ~50 node-hours for 4-dimensional sweep.\"\n    }\n  },\n  \"key_references\": [\n    \"LLMs Faithfully and Iteratively Compute Answers During CoT: A Systematic Analysis With Multi-step Arithmetics (Kudo et al., EACL 2026, arXiv 2412.01113) — probing + activation patching on same instances for synthetic arithmetic; finds CoT IS faithful; explicitly calls for natural-task extension\",\n    \"When Chains of Thought Don't Matter: Causal Bypass in Large Language Models (Sathyanarayanan et al., arXiv 2602.03994) — CoT Mediation Index via layerwise activation patching; identifies bypass regimes (CMI ≈ 0); small scale (~50 examples), no temporal resolution\",\n    \"Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal (Yuan et al., arXiv 2605.09502, May 2026) — correctness probes at 0.95 AUROC but four interventions fail; critical context for probe interpretation\",\n    \"Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought (Zhao et al., arXiv 2510.24941, Oct 2025, revised Apr 2026) — True Thinking Score (TTS) via text-level perturbation + ATE; only 2.3% of AIME steps have TTS≥0.7; tested on DeepSeek-R1-Distill-Qwen-7B/14B, Llama-8B across AIME/MATH/AMC/CommonsenseQA; direct Causal-TIC precursor (per-step, single-estimator, text-level)\",\n    \"Spatiotemporal Hidden-State Dynamics as a Signature of Internal Reasoning in Large Language Models (Furuya & Tanimura, arXiv 2605.01853, May 2026) — StALT training-free temporal trajectory statistic; separates correct from incorrect reasoning; concurrent work adjacent to Probe-TIC (targets correctness not faithfulness, no causal component)\",\n    \"Task Difficulty Shapes Chain-of-Thought Faithfulness (ICLR 2026 Workshop) — CoT transitions from decorative to load-bearing with difficulty; error propagation 22% (MMLU) to 41% (BBH); probes are 'readout rather than control'; independently validates diagnostic framing\",\n    \"Diagnosing Pathological Chain-of-Thought in Reasoning Models (Liu et al., arXiv 2602.13904, Feb 2026) — text-level metrics (Necessity, Paraphrasability, Substantivity) for three CoT pathologies; computationally inexpensive, task-agnostic; validated on model organisms; complementary text-level diagnostic\",\n    \"Measuring Faithfulness Depends on How You Measure: Classifier Sensitivity in LLM Chain-of-Thought Evaluation (Young, arXiv 2603.20172, Mar 2026) — inter-classifier kappa as low as 0.06; up to 30.6pp divergence across classifiers on 10,276 traces; motivates robustness ablations for TIF\",\n    \"Tracing the Traces: Latent Temporal Signals for Efficient and Accurate Reasoning (Vilas et al., ICLR 2026, arXiv 2510.10494) — latent-trajectory signals (net/cumulative/aligned change) for reasoning efficiency; 14-70% token savings; adjacent temporal hidden-state methodology applied to efficiency not faithfulness\",\n    \"Probing and Steering Chain-of-Thought Unfaithfulness in Language Models (Occhipinti et al., ICLR 2026 LIT Workshop) — faithfulness encoded as linear directions in middle-to-late layers; probing F1 90-100%; steering recovers 46% monitorability with <5% collateral\",\n    \"FACT-E: Causality-Inspired Evaluation for Trustworthy Chain-of-Thought Reasoning (Sun et al., ACL Findings 2026, arXiv 2604.10693) — controlled perturbations measuring intra-chain faithfulness + CoT-to-answer consistency; no hidden-state access\",\n    \"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (Alvarez & Baheri, arXiv 2605.13772, May 2026) — geometric features for step-level hallucination detection\",\n    \"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures (Somov et al., arXiv 2603.16475) — up to 60% failure to update after intervention\",\n    \"When Is Thinking Enough? Early Exit via Sufficiency Assessment (Xiang et al., arXiv 2604.06787) — DTSR 28.9-34.9% token reduction\",\n    \"FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness (Swaroop et al., arXiv 2509.13334)\",\n    \"Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks (Qian et al., NeurIPS 2025, arXiv 2506.02867)\",\n    \"Temporal Predictors of Outcome in Reasoning Language Models (David, arXiv 2511.14773, Nov 2025)\",\n    \"Reasoning Models Know When They're Right: Probing for Self-Verification (Zhang et al., arXiv 2504.05419, Apr 2025)\",\n    \"Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation? (Lewis-Lim et al., EMNLP 2025, arXiv 2508.19827)\",\n    \"The Illusion of Reasoning: Step-Level Evaluation Reveals Decorative CoT (Basu & Chakraborty, arXiv 2603.22816, Mar 2026)\",\n    \"Why Models Know But Don't Say: CoT Faithfulness Divergence (Young, arXiv 2603.26410, Mar 2026)\",\n    \"Therefore I am. I Think (Esakkiraja et al., arXiv 2604.01202, Apr 2026)\",\n    \"Early Stopping via Confidence Dynamics: CoDE-Stop (Hosseini et al., arXiv 2604.04930, Apr 2026)\",\n    \"Emergent Manifold Separability during Reasoning in LLMs (Chun et al., arXiv 2602.20338, Feb 2026)\",\n    \"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning (Ye et al., arXiv 2602.11201, Feb 2026)\",\n    \"Decoding Answers Before Chain-of-Thought: Pre-CoT Probes and Activation Steering (Cox et al., arXiv 2603.01437, Mar 2026) — pre-CoT probes >0.9 AUC; steering flips >50% on instruction-tuned models; explicitly limited to binary tasks ≤9B; reports 'little success steering' reasoning models\",\n    \"Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought (Boppana et al., arXiv 2603.05488, Mar 2026)\",\n    \"No Global Plan in Chain-of-Thought: Latent Planning Horizon of LLMs (Xu et al., arXiv 2602.02103, Feb 2026)\",\n    \"Catching Rationalization in the Act: Detecting Motivated Reasoning via Activation Probing (Mirtaheri & Belkin, arXiv 2603.17199, Mar 2026)\",\n    \"Analyzing and Improving CoT Monitorability Through Information Theory (Anwar et al., arXiv 2602.18297, Feb 2026)\",\n    \"FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of CoT Reasoning (ICLR 2026, arXiv 2510.04040)\",\n    \"The Mirage of Explainability: A Survey on CoT Faithfulness (Jin et al., submitted to ARR for ACL 2026; no public arXiv version)\",\n    \"Lie to Me: How Faithful Is CoT Reasoning in Reasoning Models? (arXiv 2603.22582, Mar 2026)\",\n    \"Understanding Chain-of-Thought in LLMs through Information Theory (Ton et al., ICML 2025, arXiv 2411.11984)\",\n    \"The Potential of CoT for Reasoning: Trace Dynamics (Bachmann et al., arXiv 2602.14903, Feb 2026)\",\n    \"NEAT: Neuron-Based Early Exit for Large Reasoning Models (arXiv 2602.02010, Feb 2026)\",\n    \"ESTAR: Early-Stopping Token-Aware Reasoning (arXiv 2602.10004, Feb 2026)\",\n    \"When Chain-of-Thought Fails, the Solution Hides in the Hidden States (arXiv 2604.23351, Apr 2026)\",\n    \"Knowing Before Saying: LLM Representations Encode CoT Success Before Completion (ACL Findings 2025, arXiv 2505.24362)\"\n  ],\n  \"description\": \"We propose a dual-estimator Temporal Information Curve (TIC) framework that diagnoses chain-of-thought faithfulness by measuring the divergence between what a model internally represents and what its reasoning text causally contributes at each token position. Prior work has established the building blocks: Kudo et al. (EACL 2026) combine probing and patching on synthetic arithmetic; the CMI framework (2602.03994) provides layerwise causal audit on ~50 examples; Zhao et al. (2510.24941) measure per-step causal contribution via TTS on AIME/MATH; Furuya & Tanimura (2605.01853) track temporal hidden-state dynamics via StALT; Liu et al. (2602.13904) diagnose CoT pathologies via text-level metrics. We unify and extend these paradigms in four ways: (1) we construct a full-timeline dual-estimator curve combining answer-content linear probes (Probe-TIC) with NLDD causal interventions (Causal-TIC) — extending TTS from per-step to continuous temporal coverage and pairing it with a hidden-state information signal unavailable from any prior single-estimator approach; (2) we map five independently discovered phenomena — pre-CoT encoding, Reasoning Horizon, Reasoning Theater, myopic planning, and thinking-answer gap — to distinguishable dual-TIC signatures, conditioned on task difficulty following the ICLR 2026 Workshop finding that faithfulness varies from decorative to load-bearing with difficulty; (3) we derive the Temporal Information Fidelity (TIF) score with explicit robustness validation across probe architectures, layer selections, perturbation methods, and normalization choices, addressing the measurement sensitivity concern raised by Young (2603.20172); and (4) we include a Phase 0 pilot validating whether answer-content probes retain causal potency on reasoning models for multi-choice tasks — testing a falsifiable prediction motivated by the gap between Cox et al.'s (2603.01437) steering success on instruction-tuned models and their explicit caveat about reasoning models.\\n\\nWe adopt a deliberately weaker but more defensible interpretive stance than prior versions: the Probe-TIC measures *information availability* (an upper bound on internal knowledge), not necessarily causally determinative information. This interpretation is independently supported by three convergent findings: Yuan et al. (2605.09502) show correctness probes are diagnostic-not-causal; the 'Task Difficulty' workshop shows probes are 'readout rather than control'; Occhipinti et al. (ICLR 2026 LIT Workshop) show faithfulness steering achieves only 46% recovery. The gap G(t) = P(t) − C(t) remains diagnostic under this weaker assumption: patterns of information excess across time, tasks, and difficulty levels reveal which faithfulness phenomenon is operative, providing mechanistic grounding absent from text-level diagnostics (Liu et al.), single-estimator metrics (TTS, StALT, latent-trajectory signals), and expert annotation benchmarks (FaithCoT-Bench). As calibration, we include Kudo et al.'s synthetic arithmetic (expecting G(t) ≈ 0) and cross-reference TTS values on overlapping benchmarks. A secondary application derives a principled early-exit criterion from Causal-TIC inflection points.\",\n  \"revision_notes\": {\n    \"critical_changes\": [\n      \"ADDED TTS (2510.24941) AS DIRECT CAUSAL-TIC PRECURSOR: Zhao et al.'s True Thinking Score — per-step causal contribution via text-level perturbation + ATE on our exact target benchmarks (AIME, MATH) and models (DeepSeek-R1-Distill-Qwen-7B/14B) — is now prominently positioned as the single-estimator precursor that our Causal-TIC extends to continuous temporal coverage within the dual-estimator gap framework. Key differentiators: TTS is discrete per-step (not continuous), single-estimator (no probe gap), text-level perturbation (vs. NLDD logit degradation). We add TTS cross-reference on overlapping benchmarks as a calibration check.\",\n      \"CITED StALT (2605.01853) AS CONCURRENT ADJACENT WORK: Furuya & Tanimura's training-free temporal trajectory statistic on hidden states is acknowledged as conceptually adjacent to Probe-TIC. Differentiated: targets correctness separation (not faithfulness), training-free (vs. trained probes targeting answer content), no causal intervention component, no gap diagnostic.\",\n      \"ADDED TASK-DIFFICULTY CONDITIONING TO FRAMEWORK: The 'Task Difficulty Shapes CoT Faithfulness' (ICLR 2026 Workshop) finding — that faithfulness transitions from decorative to load-bearing with difficulty, and probes are 'readout rather than control' — is integrated as a sixth analytical dimension. Dual-TIC signatures are now analyzed stratified by task difficulty, with predictions for how each phenomenon manifests across difficulty levels. This enriches the unification thesis and independently validates the diagnostic framing.\",\n      \"ADDED MEASUREMENT SENSITIVITY ABLATIONS: Young (2603.20172) shows inter-classifier kappa as low as 0.06. We now plan explicit robustness ablations across 4 dimensions (probe architecture, layer selection, NLDD perturbation method, gap normalization) and commit to reporting sensitivity ranges rather than single aggregate TIF numbers.\",\n      \"ELEVATED ANSWER-CONTENT PROBE GENERALIZATION TO TIER-1 RISK WITH PILOT VALIDATION: Cox et al.'s (2603.01437) validation is limited to binary tasks on models ≤9B, and they explicitly report 'little success steering' reasoning models. This is now a Tier-1 risk addressed via Phase 0 pilot: 500 examples on MMLU (4-choice) and GSM8K (numerical) testing whether answer-content probes retain causal potency on DeepSeek-R1-Distill-Qwen-7B. If steering fails, we validate the information-availability interpretation and calibrate the upper bound looseness.\",\n      \"REFRAMED PROBE-TIC UNDER WEAKER BUT MORE DEFENSIBLE ASSUMPTION: The Probe-TIC is now explicitly interpreted as measuring 'information availability' (upper bound on internal knowledge), not causally determinative information. This is independently supported by three convergent findings (Yuan et al., 'Task Difficulty' workshop, Occhipinti et al.) and makes the framework robust to the possibility that answer-content probes are not causally potent on reasoning models.\",\n      \"ADDED LIU ET AL. (2602.13904) AS COMPLEMENTARY TEXT-LEVEL DIAGNOSTIC: Their Necessity/Paraphrasability/Substantivity metrics for three CoT pathologies provide a text-level baseline for cross-validation with our hidden-state-grounded TIF score.\",\n      \"ADDED VILAS ET AL. (2510.10494, ICLR 2026) AS ADJACENT TEMPORAL METHODOLOGY: Their latent-trajectory signals demonstrate that temporal hidden-state evolution is informative for reasoning analysis, motivating our faithfulness-specific application of similar methodology.\",\n      \"ADDED OCCHIPINTI ET AL. (ICLR 2026 LIT WORKSHOP): Their finding that faithfulness is linearly encoded (probing F1 90-100%) but steering recovers only 46% monitorability provides independent evidence for our readout-not-control interpretation.\",\n      \"DROPPED AAAI 2027: 2 months is insufficient regardless of execution mode. Venues are now ICLR 2027 (primary, 4 months) and ICML 2027 (fallback, 8 months).\"\n    ],\n    \"what_stayed\": \"The five-phenomena unification thesis (now enriched with task-difficulty conditioning), the dual-TIC concept, the NLDD and probe estimators, the four benchmarks (MMLU, GPQA-Diamond, GSM8K, AIME), the four target models (DeepSeek-R1-Distill 7B/14B/32B, QwQ-32B), the 671B validation subset, layer-selective caching, the TIF score concept, the synthetic arithmetic calibration check, and the diagnostic (thermometer) framing. The core insight — that the gap between internal information and causal contribution reveals diagnostic patterns invisible to either estimator alone — is strengthened by honest positioning, weaker interpretive assumptions, task-difficulty conditioning, and robustness validation.\",\n    \"residual_risks\": [\n      \"TIER-1: Answer-content probe causal potency on reasoning models is untested for multi-choice and numerical tasks. The Phase 0 pilot addresses this directly, but if probes show neither predictive power nor causal potency on reasoning models (a possibility given Cox et al.'s caveat), the Probe-TIC contribution would be limited to reproducing StALT-like correctness signals. Mitigation: the information-availability interpretation preserves diagnostic value even under minimal causal potency, but the gap signal would be loosened.\",\n      \"TIER-1: The TTS paper (Zhao et al. 2510.24941) tests on our exact models (DeepSeek-R1-Distill-Qwen-7B/14B) and benchmarks (AIME, MATH). If our Causal-TIC (NLDD-based) and their TTS (ATE-based) show near-identical patterns at step boundaries, the continuous-temporal-coverage novelty narrows. Mitigation: the dual-estimator gap and five-phenomenon mapping remain unique; the within-step dynamics visible to Causal-TIC but invisible to TTS provide differentiation that must be demonstrated empirically.\",\n      \"Measurement sensitivity (Young 2603.20172): TIF may show high sensitivity to probe and intervention choices. If robustness ablations reveal instability (e.g., TIF rankings change across measurement configurations), this undermines the diagnostic utility. Mitigation: plan ablations early and report sensitivity ranges; if instability is severe, this becomes a finding about the fundamental difficulty of faithfulness measurement.\",\n      \"Task-difficulty conditioning may reveal that the five phenomena are not signatures of a unified information dynamic but rather artefacts of different task types. If pre-CoT encoding is exclusively an easy-task phenomenon and Reasoning Horizon is exclusively a moderate-task phenomenon, the 'unification' thesis weakens to a 'taxonomy indexed by difficulty' thesis. This would be a less exciting but still publishable finding.\",\n      \"NLDD interventions remain computationally expensive (10-20 perturbation passes per example on 32B models, ~250 node-hours). Robustness ablations across perturbation methods add further computational cost. May need subsampling for AIME long CoT traces.\",\n      \"The field is moving at 3+ papers per month. StALT (May 2026) appeared during this revision cycle. Additional concurrent work (especially dual-estimator approaches) may narrow the novelty window before the ICLR 2027 deadline (Sep 2026). The focused contribution (gap diagnostic + phenomenon unification + robustness validation) and the Phase 0 pilot providing novel empirical evidence about probe causal potency on reasoning models are more defensible against this risk.\",\n      \"Chun et al.'s (2602.20338) finding that probe accuracy ≠ computational readiness suggests Probe-TIC may overestimate available information. The information-availability interpretation partially addresses this, but the gap G(t) could be inflated by correlative information the model possesses but never uses.\"\n    ]\n  }\n}\n\n## Reviewer feedback (round 4)\nIssues: [\"CONCEPTUAL: The gap diagnostic G(t) = P(t) − C(t) has a discriminability problem under the 'information availability' assumption. If Probe-TIC captures correlative/epiphenomenal information (as Chun et al. 2602.20338 suggest: 'probe accuracy ≠ computational readiness'), then P(t) may be systematically high for ALL instances regardless of faithfulness phenomenon, making G(t) uniformly inflated. This would collapse the five-phenomenon signatures into a single 'high gap everywhere' pattern, undermining the framework's central diagnostic claim. The proposal acknowledges this as a residual risk but treats it as tier-2 when it should be tier-1.\", \"CONCEPTUAL: The five-phenomenon distinguishability argument is underspecified under the weaker assumption. Specifically: Pre-CoT encoding (high P(0), any C trajectory) and Reasoning Theater (growing gap: P rises, C flat) could produce indistinguishable TIC signatures if P(t) is always high due to correlative information. The proposal's four diagnostic features (initial P(0), C-plateau onset, gap trajectory, C-gradient locality) may not discriminate phenomena when the probe captures an upper bound rather than a tight estimate. The proposal needs either a formal argument or simulation showing distinguishability persists under probe inflation.\", \"MINOR MISSING REFERENCE: 'Mapping Faithful Reasoning in Language Models' (Li et al., 2510.22362, NeurIPS 2025 MechInterp Workshop) introduces Concept Walk, which projects each reasoning step onto concept directions and tracks temporal evolution of internal activations for faithfulness diagnosis. Finds easy→decorative, hard→faithful, paralleling the task-difficulty conditioning dimension. Different probe methodology (concept directions vs. answer-content probes) and different domain (safety, single model), but conceptually adjacent to Probe-TIC temporal tracking and should be cited.\", \"RISK UNDERESTIMATION: The Phase 0 pilot tests answer-content probe causal potency on MMLU (4-choice) and GSM8K (numerical) using DeepSeek-R1-Distill-Qwen-7B. But Cox et al.'s validation was on binary tasks on instruction-tuned models ≤9B, and they explicitly report 'little success steering' reasoning models. If the Phase 0 pilot confirms this failure for reasoning models broadly, the Probe-TIC becomes just another correlative hidden-state signal (like StALT) rather than measuring information the model could in principle use. Under this scenario, the gap G(t) loses its interpretation as 'information excess' and becomes 'correlative excess,' which is less interesting. The proposal should have a more detailed contingency plan for this outcome.\", \"NOVELTY POSITIONING: The proposal's core novelty claim — that the gap between two estimators reveals phenomenon-specific signatures invisible to either alone — is compelling in principle but untested. The proposal relies heavily on the prediction that different phenomena produce distinguishable gap trajectories, but this is an empirical bet. If the patterns turn out to be noisy or hard to distinguish (especially given Young's measurement sensitivity findings), the main contribution reduces to 'we ran probing and NLDD on the same instances at scale,' which is a useful resource contribution but not a conceptual advance worthy of a top venue.\"]\nFeedback: **Round 4 shows major improvement — the proposal is now well-positioned against the literature, honest about assumptions, and comprehensive in scope.** The critical issue preventing a pass is the gap diagnostic's discriminability under the weaker 'information availability' assumption. Three specific fixes:\n\n1. **Elevate the gap inflation problem to Tier-1 and address it directly.** Chun et al.'s finding that probe accuracy ≠ computational readiness means P(t) may be uniformly high, collapsing five-phenomenon signatures into one. To address this: (a) include a theoretical analysis or toy simulation showing that even if P(t) is inflated, the *trajectory shape* (rate of increase, curvature, onset timing) can still distinguish phenomena; (b) propose a calibration method — e.g., normalize P(t) against a 'null probe' trained on shuffled labels, so the gap measures *excess* information above chance rather than raw probe accuracy; (c) in Phase 0, explicitly test whether Probe-TIC trajectories differ meaningfully across task difficulty levels even if absolute P(t) values are high.\n\n2. **Strengthen the five-phenomenon distinguishability argument.** Currently, the four diagnostic features (initial P(0), C-plateau onset, gap trajectory, C-gradient locality) are asserted to distinguish phenomena but not demonstrated. Add a concrete worked example: take 2-3 phenomena (e.g., Pre-CoT encoding vs. Reasoning Theater vs. genuine reasoning) and draw predicted TIC curves under both the strong and weak probe assumptions. Show that trajectory *shapes* remain distinguishable even when absolute P(t) is inflated. If you cannot draw distinguishable curves under the weak assumption, this is a fundamental problem that must be acknowledged and the five-phenomenon mapping should be reframed as 'exploratory' rather than a primary contribution.\n\n3. **Cite Li et al. (2510.22362) 'Mapping Faithful Reasoning'** — their Concept Walk framework tracks temporal activation evolution and finds easy→decorative, hard→faithful, which directly supports your task-difficulty conditioning. Differentiate: they use concept directions (not answer-content probes), study safety (not reasoning benchmarks), and lack a causal-contribution curve.\n\n4. **Tighten the focus for the paper.** The proposal currently has ~7 contributions (gap diagnostic, five-phenomenon mapping, TIF score, task-difficulty conditioning, robustness ablations, Phase 0 pilot findings, early-exit criterion). For a single paper, consider: Phase 0 pilot results + gap diagnostic + task-difficulty conditioned signatures as the core paper, with robustness ablations and five-phenomenon mapping as the key experimental sections. The early-exit application and 671B validation can be supplementary material.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.\n- Address each issue specifically.\n\n## 深度调研要求\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。\n3. **深度思考**：\n   - 核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach？\n4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。\n\n## 针对 Review 意见的定向搜索\n\n1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点\n2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline\n3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现\n4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot\n\n- You have full freedom: minor fix, major revision, or pivot.\n- Include a \"change_type\" field: \"minor\", \"major\", or \"pivot\".\n- Output a COMPLETE JSON object with ALL fields."
}
```

---

### Runtime record

_source line 2 · 2026-05-19T12:00:31.838Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T12:00:31.838Z",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f"
}
```

---

## Round 1

48 recorded events

### User

_source line 3 · 2026-05-19T12:00:31.852Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-19 (UTC).**

## Original idea
{
  "title": "The Probe-Intervention Gap: Diagnosing Chain-of-Thought Faithfulness via Dual-Estimator Temporal Information Decomposition",
  "project_name": "cot_faithfulness_decomp",
  "source": "web_research",
  "level": "top-tier",
  "target_venues": [
    "ICLR 2027 (abstract: Sep 19, full paper: Sep 24, 2026; conference: Apr/May 2027 — primary target, 4 months from now)",
    "ICML 2027 (full paper: Jan 29, 2027; conference: Jul 2027 — comfortable fallback if additional experiments needed)"
  ],
  "core_problem": "Multiple independent findings in 2025-2026 — Reasoning Horizon, pre-CoT answer encoding, Reasoning Theater, myopic planning, thinking-answer gap — all describe facets of the same underlying problem: models' chain-of-thought reasoning is partially or entirely decorative. While the CoT faithfulness literature has catalogued these phenomena (Jin et al.'s survey; FaithCoT-Bench at ICLR 2026) and several groups have measured temporal dynamics of individual signals, no work has unified these disparate phenomena under a single information-theoretic framework that explains WHY and WHEN each occurs. Crucially, recent work reveals that the relationship between faithfulness and task difficulty is not binary: CoT transitions from decorative to load-bearing as task difficulty increases ('Task Difficulty Shapes CoT Faithfulness,' ICLR 2026 Workshop), with error propagation ranging from 22% on MMLU to 41% on BBH. This difficulty gradient — detectable via hidden-state probes but resistant to single-direction steering ('readout rather than control') — demands a diagnostic framework that can characterize faithfulness along both temporal and difficulty dimensions. The closest precedents — Kudo et al.'s (EACL 2026) probing + activation patching on synthetic arithmetic, the CMI framework's layerwise causal audit on ~50 examples, Zhao et al.'s (2510.24941) True Thinking Score providing per-step causal contribution on AIME/MATH, and Furuya & Tanimura's (2605.01853) training-free StALT trajectory statistic — each capture one dimension of the problem but none provides a dual-estimator framework that jointly measures internal information and causal contribution across the full CoT timeline on natural benchmarks.",
  "opportunity": "The field has independently produced three complementary measurement paradigms: (1) probe-based approaches revealing what the model internally represents at each CoT position (David 2511.14773: correctness decodable at t=4 tokens; Cox et al. 2603.01437: pre-CoT probes at >0.9 AUC with causal validation via steering on instruction-tuned models up to 9B; Esakkiraja et al. 2604.01202: pre-generation probes with >90% AUROC; Furuya & Tanimura 2605.01853: training-free StALT separating correct from incorrect trajectories), (2) intervention-based approaches measuring what the CoT text causally contributes (Ye et al. 2602.11201: NLDD reveals Reasoning Horizon at 70-85%; Zhao et al. 2510.24941: True Thinking Score provides per-step ATE on AIME/MATH/AMC/CommonsenseQA, finding only 2.3% of AIME steps have TTS≥0.7; Basu & Chakraborty 2603.22816: decorative/scaffolding/genuine taxonomy), and (3) diagnostic approaches characterizing CoT pathologies (Liu et al. 2602.13904: text-level metrics for rationalization/encoded/internalized reasoning via model organisms; 'Task Difficulty Shapes CoT Faithfulness' ICLR 2026 Workshop: difficulty-dependent faithfulness gradient). Two prior works have combined probing with causal interventions on the same instances: Kudo et al. (2412.01113, EACL 2026) train linear probes and perform activation patching across arithmetic CoT; the CMI framework (2602.03994) measures CoT-mediated causal influence via layerwise patching. However, neither provides: (a) full temporal-position coverage across CoT on natural benchmarks, (b) a mapping to the five named faithfulness phenomena, (c) a standalone instance-level diagnostic score, (d) systematic multi-model comparison on realistic reasoning tasks, or (e) robustness validation across measurement methodologies — a critical gap highlighted by Young's (2603.20172) finding that faithfulness measurements are classifier-sensitive (inter-classifier kappa as low as 0.06). The opportunity is to extend the probe-intervention combination paradigm to a systematic dual-estimator Temporal Information Curve (TIC) framework producing a 2D faithfulness signal — the gap between probe-estimated internal information and intervention-estimated causal contribution — on natural benchmarks at scale, with explicit robustness validation.",
  "landscape": "**Probe-intervention combinations (closest prior work).** Kudo et al. (2412.01113, EACL 2026) train per-position linear probes on hidden states and validate with sliding-window activation patching on 9 models across synthetic multi-step arithmetic. They find CoT IS faithful for arithmetic but explicitly note their synthetic setting may not generalize to 'more realistic reasoning tasks in natural language.' The CMI framework (2602.03994) introduces the CoT Mediation Index via layerwise activation patching across Phi, Qwen, and DialoGPT on StrategyQA (20 examples), TruthfulQA (10), and GSM8K (20), identifying 'bypass regimes' where CMI ≈ 0. Both are complementary precursors.\n\n**Per-step causal contribution (direct Causal-TIC precursor).** Zhao et al. (2510.24941, Oct 2025, revised Apr 2026) introduce the True Thinking Score (TTS), measuring per-step causal contribution via text-level perturbation (numerical offsets preserving grammar) and ATE computation. On DeepSeek-R1-Distill-Qwen-7B/14B/Llama-8B across AIME, MATH, AMC, CommonsenseQA, they find only 2.3% of AIME steps have TTS≥0.7. TTS also extracts a 'TrueThinking direction' from hidden states for steering (53.6-91.2% flip rates). TTS is a direct precursor to our Causal-TIC component. Key differentiators: TTS operates at discrete step granularity (not continuous temporal), is a single-estimator metric (no probe gap), uses text-level perturbation (vs. our NLDD logit degradation), and does not map to the five faithfulness phenomena or provide an instance-level diagnostic score grounded in the probe-intervention divergence. Our framework extends TTS's causal measurement from per-step to continuous temporal coverage and pairs it with the Probe-TIC for the gap diagnostic unavailable from either estimator alone.\n\n**Training-free temporal hidden-state dynamics (concurrent work adjacent to Probe-TIC).** Furuya & Tanimura (2605.01853, May 2026) introduce StALT (Spatiotemporal Amplitude of Latent Transition), a training-free trajectory statistic that separates correct from incorrect reasoning trajectories by tracking hidden-state transitions across decoding steps and layers. Tested on GSM8K, MATH-500, and GPQA. StALT is conceptually adjacent to our Probe-TIC in tracking temporal hidden-state evolution. Key differentiators: StALT targets correctness separation (not faithfulness diagnosis), is training-free (vs. our trained answer-content probes targeting specific answer information), lacks a causal intervention component (no gap diagnostic), and does not map to faithfulness phenomena. Our Probe-TIC complements StALT by probing for answer content specifically and pairing it with causal interventions.\n\n**Latent-trajectory signals for efficiency.** Vilas et al. (2510.10494, ICLR 2026) define three latent-trajectory signals — net change, cumulative change, and aligned change — tracking hidden-state evolution across 500-token segments. On DeepSeek-R1-Distill-Qwen-14B, Phi-4-Reasoning-Plus, and Qwen3-14B across GPQA Diamond, AIME 2025, and TSP, they achieve 14-70% token savings and +2.6% accuracy gains via early selection of productive reasoning paths. Focuses on efficiency (correctness prediction for compute allocation), not faithfulness. Adjacent methodology but orthogonal goal; reinforces that temporal hidden-state signals are informative, motivating our faithfulness-specific application.\n\n**The diagnostic-not-causal challenge.** Yuan et al. (2605.09502, May 2026) show that probes detecting *trace correctness* achieve 0.95 AUROC but four interventions fail, concluding error representations are 'fundamentally different from editable factual knowledge representations.' Cox et al. (2603.01437) demonstrate that *answer-content* probe directions are causally potent on instruction-tuned models: steering flips >50% of answers. However — and this is a critical limitation acknowledged in this revision — Cox et al.'s validation is restricted to binary classification tasks (Anachronisms, Logical Deduction, Sports Understanding, Social Chemistry) on models up to 9B parameters, and they explicitly note that for reasoning models, they find 'some success using probes to linearly decode the final answer, but little success steering to change it.' This means the causal potency of answer-content probes on reasoning models (our target model class) is NOT yet established. The 'Task Difficulty Shapes CoT Faithfulness' workshop paper independently reaches a similar conclusion: hidden-state probes are 'readout rather than control.' We therefore reframe: the Probe-TIC captures information availability (an upper bound on what the model 'knows' at each position), regardless of whether that representation is directly steerable. The gap G(t) between information availability and causal contribution remains diagnostic of reasoning quality under this weaker but more honest assumption.\n\n**CoT pathology diagnostics.** Liu et al. (2602.13904, Feb 2026) propose text-level, computationally inexpensive, task-agnostic metrics for three CoT pathologies: Necessity (rationalization), Paraphrasability (encoded reasoning), and Substantivity (internalized reasoning), validated on model organisms (Olmo-3-7B-Think trained to exhibit pathologies). Their approach is complementary to ours: purely text-level (no hidden states), uses model organisms (not natural models), categorical per-pathology metrics (not continuous temporal curves), and lacks the dual-estimator gap. Our framework provides mechanistic grounding via hidden states that their text-level metrics cannot.\n\n**Measurement sensitivity.** Young (2603.20172, Mar 2026) shows faithfulness measurements are classifier-sensitive: inter-classifier kappa as low as 0.06 for sycophancy hints, with up to 30.6 percentage-point divergence across three classifiers on 10,276 traces from 12 models. This raises a methodological concern directly applicable to our framework: TIF will likely show sensitivity to probe layer selection, probe architecture, NLDD perturbation method, and gap normalization. We address this by planning explicit robustness ablations across these measurement dimensions and reporting sensitivity ranges rather than single aggregate numbers.\n\n**Task-difficulty moderation of faithfulness.** 'Task Difficulty Shapes CoT Faithfulness' (ICLR 2026 Workshop) demonstrates that CoT transitions from decorative to load-bearing as task difficulty increases: error propagation rises from 22% on MMLU to 41% on BBH, with 7× variation within MMLU subjects. Hidden-state probes detect this gradient but single-direction steering cannot shift it ('readout rather than control'). This finding has two critical implications for our framework: (1) the five faithfulness phenomena may be differentially expressed across task difficulties, enriching our unification thesis with a difficulty dimension; (2) independent confirmation that probes are diagnostic instruments, not interventional tools, supporting our thermometer framing.\n\n**Probe-based temporal measurement.** Qian et al. (2506.02867, NeurIPS 2025) compute per-token HSIC between hidden representations and golden answers, discovering MI peaks at thinking tokens. David (2511.14773) trains linear classifiers at prefix lengths t=4...512, showing correctness is decodable early. Zhang et al. (2504.05419) probe hidden states at intermediate answer positions for early-exit (24% savings). Lewis-Lim et al. (2508.19827, EMNLP 2025) track answer confidence trajectories, revealing flat (rationalization) vs. increasing (genuine reasoning) patterns. Mirtaheri & Belkin (2603.17199) show pre-generation probes match full-CoT monitors. Esakkiraja et al. (2604.01202) show pre-generation probes predict tool-calling at >90% AUROC.\n\n**Intervention-based causal measurement.** Ye et al. (2602.11201) introduce NLDD, revealing Reasoning Horizon at 70-85%. Basu & Chakraborty (2603.22816) propose genuine/scaffolding/decoration taxonomy via step ablation. Somov et al. (2603.16475) show up to 60% failure to update after intervention. FACT-E (2604.10693, ACL Findings 2026) uses controlled perturbations.\n\n**Probing and steering faithfulness.** Occhipinti et al. (ICLR 2026 LIT Workshop) demonstrate that faithfulness is encoded as linear directions in middle-to-late layers, with probing F1 scores of 90-100% at peak layers and steering achieving 46% monitorability recovery with <5% collateral effects. This provides complementary evidence that faithfulness has a linear geometric signature exploitable by probes.\n\n**Geometric and information-theoretic approaches.** Chun et al. (2602.20338) apply Manifold Capacity Theory revealing transient geometric pulses. Alvarez & Baheri (2605.13772, May 2026) detect step-level hallucination via hidden-state transport geometry. Ton et al. (ICML 2025, 2411.11984) define per-step information gain. Anwar et al. (2602.18297) decompose monitorability into information gap + elicitation error.\n\n**Faithfulness benchmarks and surveys.** FaithCoT-Bench (ICLR 2026, 2510.04040). Jin et al.'s survey (submitted to ARR for ACL 2026; no public arXiv version). Young (2603.26410): 55.4% thinking-only acknowledgment. 'Lie to Me' (2603.22582): 87.5% vs 28.6% thinking vs answer.\n\n**Early-exit methods.** Reasoning Theater (2603.05488: 80% savings), ESTAR (2602.10004), DTSR (2604.06787: 28.9-34.9%), NEAT (2602.02010), CoDE-Stop (2604.04930), Zhang et al. (2504.05419: 24%), FRIT (2509.13334).\n\n**What remains open.** No extant framework provides: (1) a full-timeline dual-estimator curve combining answer-content probes with causal interventions on natural benchmarks at scale; (2) a systematic mapping of five phenomena to distinguishable signatures within such a framework, conditioned on task difficulty; (3) an instance-level diagnostic score derived from the probe-intervention gap with explicit robustness validation across measurement methodologies; or (4) a principled account of how the probe-intervention gap behaves differently on instruction-tuned vs. reasoning models. TTS provides per-step causal contribution (single-estimator, text-level); StALT provides temporal hidden-state correctness signals (single-estimator, no causal component); Vilas et al. provide latent-trajectory efficiency signals (no faithfulness connection); Liu et al. provide text-level pathology diagnostics (no hidden states). The dual-estimator gap — jointly measuring internal information and causal contribution across the full timeline — remains the unique contribution.",
  "inspired_by": "The convergence of four observations: (a) Kudo et al.'s demonstration that probe+intervention combination is feasible and informative on synthetic arithmetic, with their explicit call for natural-task extension; (b) Zhao et al.'s (2510.24941) TTS demonstrating per-step causal contribution measurement at scale on our exact target benchmarks (AIME, MATH), establishing the causal-contribution paradigm we extend to continuous temporal coverage with the dual-estimator gap; (c) the finding from both Cox et al. (2603.01437) on instruction-tuned models and the 'Task Difficulty' workshop paper that probes are diagnostic ('readout') rather than interventional ('control') — which, rather than undermining probe-based faithfulness work, clarifies that the Probe-TIC should be interpreted as an information-availability signal, making the framework more honest and defensible; (d) Young's (2603.20172) demonstration that faithfulness measurements are classifier-sensitive, motivating our explicit robustness ablation plan.",
  "approach": "Define a dual-estimator Temporal Information Curve (TIC) framework that diagnoses chain-of-thought faithfulness at each token position t via two complementary signals:\n\n**(a) Probe-TIC P(t)**: Information about the answer decodable from residual-stream activations h_{1:t} via linear probes trained on 3-5 selected layers. Critically, we probe for *answer content* (which answer option / numerical value the model will produce), not binary correctness. On instruction-tuned models, Cox et al. (2603.01437) demonstrate such probes are causally potent (steering flips >50% of answers). However, Cox et al.'s validation is limited to binary tasks on models ≤9B, and they explicitly report that reasoning models resist steering. We therefore interpret the Probe-TIC as measuring *information availability* — an upper bound on what the model internally represents at each position — rather than assuming causal potency. This interpretation is independently supported by the 'Task Difficulty Shapes CoT Faithfulness' finding that probes are 'readout rather than control,' and is consistent with the training-free trajectory statistics of Furuya & Tanimura (2605.01853) which also show hidden-state signals are diagnostic of reasoning quality.\n\n**(b) Causal-TIC C(t)**: Causal contribution of CoT_{1:t} to the answer via NLDD-style interventions (corrupting CoT segments and measuring logit degradation). This extends the single-model NLDD paradigm (Ye et al. 2602.11201) to systematic multi-model comparison with continuous temporal coverage, and provides a continuous temporal generalization of the per-step TTS metric (Zhao et al. 2510.24941). Where TTS applies text-level perturbation at discrete step boundaries with ATE computation, our Causal-TIC applies NLDD logit degradation at each token position, yielding a continuous curve that captures within-step dynamics invisible to TTS.\n\n**The Faithfulness Gap as a Diagnostic Signal.** The core diagnostic is G(t) = P(t) − C(t). We characterize this gap under a *weaker but more honest assumption* than previous versions: the Probe-TIC measures information availability (what the model knows at position t), not necessarily causally determinative information. This means:\n- G(t) ≈ 0 is a *necessary condition* for faithfulness: if available internal information and CoT causal contribution are aligned, CoT is faithful.\n- G(t) >> 0 indicates *information excess* — the model possesses answer information not causally contributed by CoT text. This is suspicious but not proof of unfaithfulness (the 'thermometer reading' scenario).\n- Critically, even under this weaker assumption, the gap is diagnostic: the PATTERN of G(t) across time, tasks, and difficulty levels reveals which of the five phenomena is operative, which is the framework's primary contribution.\n\nThis diagnostic framing is independently supported by three convergent findings: (1) Yuan et al. (2605.09502) show correctness probes are diagnostic-not-causal; (2) the 'Task Difficulty' workshop shows probes are 'readout rather than control'; (3) Occhipinti et al. (ICLR 2026 LIT Workshop) show faithfulness steering achieves only 46% recovery. The thermometer interpretation — invaluable for diagnosis, not intended for intervention — is the honest and defensible framing.\n\n**Pilot Validation of Probe Causal Potency (Phase 0).** Before running full experiments, we conduct a targeted pilot on 500 examples across MMLU (4-choice) and GSM8K (numerical) using DeepSeek-R1-Distill-Qwen-7B: train answer-content linear probes on pre-CoT and mid-CoT hidden states, then test steering along probe directions at varying strengths. This tests the falsifiable prediction that answer-content probes retain some causal potency on reasoning models for multi-choice (not just binary) tasks — or, if steering fails, validates the information-availability interpretation and calibrates how loose the upper bound is. This pilot addresses the Tier-1 risk of extrapolating Cox et al.'s binary-task findings to our setting.\n\n**Diagnostic Features.** Derive four features from the dual-TIC:\n(i) Initial probe value P(0) — detects pre-CoT encoding (high P(0) with any C trajectory).\n(ii) Causal-TIC plateau onset t* — captures the Reasoning Horizon (C(t) saturates).\n(iii) Gap trajectory G(t) over time — distinguishes Reasoning Theater (growing gap: P rises, C stays flat) from genuine reasoning (stable near-zero gap).\n(iv) Locality of Causal-TIC gradients — short- vs. long-range correlations in dC/dt capture myopic vs. global planning.\n\n**Task-Difficulty Conditioning.** Following the 'Task Difficulty Shapes CoT Faithfulness' finding, we analyze dual-TIC signatures stratified by task difficulty (using model confidence on first pass as a difficulty proxy). We predict: (a) easy instances show high P(0) with flat C(t) (pre-CoT encoding / decoration); (b) moderate instances show Reasoning Horizon signatures (C(t) plateau); (c) hard instances show increasing P(t) and C(t) trajectories (genuine reasoning). This difficulty conditioning enriches the five-phenomena unification with a sixth predictive variable.\n\n**Robustness Ablations.** Motivated by Young (2603.20172), who shows inter-classifier kappa as low as 0.06 for faithfulness measurements, we plan explicit robustness ablations: (a) probe architecture (linear vs. 2-layer MLP); (b) layer selection (best-3 vs. best-5 vs. all layers); (c) NLDD perturbation method (Gaussian corruption vs. token replacement vs. segment shuffling); (d) gap normalization (raw difference vs. ratio vs. area-under-curve). We report sensitivity ranges for TIF scores across these axes, following Young's recommendation for multi-method validation.\n\n**Experiments.** Core experiments target DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Qwen-14B, DeepSeek-R1-Distill-Qwen-32B, and QwQ-32B across four benchmarks (MMLU, GPQA-Diamond, GSM8K, AIME), with a targeted validation run on DeepSeek-R1-671B (500-example subset, 3 layers). Layer-selective activation caching (5 layers from pilot study on 7B) keeps storage at ~3-5 TB. As a calibration check, we include Kudo et al.'s synthetic arithmetic as a control condition where we expect G(t) ≈ 0. As an additional calibration, we cross-reference TTS values from Zhao et al. on overlapping benchmarks (AIME, MATH) to validate Causal-TIC against the established per-step metric.\n\n**Primary Output: Temporal Information Fidelity (TIF) Score.** An instance-level diagnostic score computed as the normalized area under the gap curve G(t). TIF is explicitly framed as a diagnostic signal grounded in the information asymmetry between what hidden states encode and what CoT text causally contributes. Benchmarked against FaithCoT-Bench expert annotations and cross-validated against Liu et al.'s (2602.13904) text-level pathology metrics (Necessity, Paraphrasability, Substantivity) on overlapping examples. We hypothesize TIF correlates with but does not perfectly predict expert annotations, because TIF captures potential for unfaithfulness (information availability mismatch) while experts judge realized unfaithfulness (information misuse).\n\n**Secondary Output: Causal Sufficiency Stopping Criterion.** As a secondary application, we derive an early-exit criterion keyed to the Causal-TIC's inflection point. Benchmarked against existing methods but positioned as a practical byproduct, not a standalone contribution.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "600 H100-hours (300 for distilled-model inference with layer-selective activation caching on 4 models × 4 datasets + synthetic arithmetic control; 150 for NLDD causal interventions across 10-20 perturbation passes per model; 50 for probe training, Phase 0 pilot, and TIF-FaithCoT-Bench validation; 50 for robustness ablations across 4 measurement dimensions; 50 for 671B validation subset on 8×H100 node)",
      "timeline": "4 months (2 researchers: 2 weeks Phase 0 pilot (probe causal potency validation on 7B) + probing pipeline via nnsight + layer-selection study + synthetic arithmetic calibration, 7 weeks core dual-estimator experiments across 4 models × 4 datasets with task-difficulty stratification, 3 weeks TIF validation against FaithCoT-Bench + Liu et al. metrics + phenomenon mapping, 2 weeks robustness ablations + TTS cross-reference, 2 weeks writing)",
      "estimated_gpu_cost": "$1,500 (at ~$2.50/H100-hr avg via RunPod/Lambda spot pricing, May 2026 rates)",
      "storage": "3-5 TB for layer-selective activation caching (5 layers per model, fp16); reducible to ~1.5 TB via PCA to 25% dimensionality"
    },
    "human_in_loop": {
      "gpu_hours": "500 H100-hours (Claude accelerates probing pipeline, NLDD implementation, analysis scripts, reducing iteration overhead ~20%)",
      "timeline": "3.5 months (1 researcher + Claude: 2 weeks Phase 0 pilot + pipeline setup + synthetic arithmetic calibration, 6 weeks core experiments with difficulty stratification, 2 weeks TIF validation + phenomenon mapping + robustness ablations, 2 weeks TTS cross-reference + paper drafting)",
      "claude_api_cost": "$400 (code generation for probing/intervention/ablation pipelines, automated result analysis, paper drafting; ~80M input + 20M output tokens via Sonnet 4.6)",
      "estimated_gpu_cost": "$1,250"
    },
    "auto_research": {
      "gpu_hours": "500 H100-hours (same computational footprint; experiment is GPU-bound not code-bound)",
      "timeline": "3 months (Claude drives experiment design, implementation, analysis, and full draft; human provides weekly steering and final review)",
      "claude_api_cost": "$800 (extensive pipeline generation, hyperparameter sweeps, robustness ablation design, automated result interpretation, full paper draft; ~160M input + 40M output tokens)",
      "estimated_gpu_cost": "$1,250",
      "speed_bottleneck": "NLDD interventions on 32B models require multiple forward passes (10-20 per example) at ~15 tok/s on 2×H100; ~250 node-hours for 20K examples across 4 datasets + arithmetic control dominate wall-clock time. 671B validation subset requires 8×H100 node. Robustness ablations add ~50 node-hours for 4-dimensional sweep."
    }
  },
  "key_references": [
    "LLMs Faithfully and Iteratively Compute Answers During CoT: A Systematic Analysis With Multi-step Arithmetics (Kudo et al., EACL 2026, arXiv 2412.01113) — probing + activation patching on same instances for synthetic arithmetic; finds CoT IS faithful; explicitly calls for natural-task extension",
    "When Chains of Thought Don't Matter: Causal Bypass in Large Language Models (Sathyanarayanan et al., arXiv 2602.03994) — CoT Mediation Index via layerwise activation patching; identifies bypass regimes (CMI ≈ 0); small scale (~50 examples), no temporal resolution",
    "Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal (Yuan et al., arXiv 2605.09502, May 2026) — correctness probes at 0.95 AUROC but four interventions fail; critical context for probe interpretation",
    "Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought (Zhao et al., arXiv 2510.24941, Oct 2025, revised Apr 2026) — True Thinking Score (TTS) via text-level perturbation + ATE; only 2.3% of AIME steps have TTS≥0.7; tested on DeepSeek-R1-Distill-Qwen-7B/14B, Llama-8B across AIME/MATH/AMC/CommonsenseQA; direct Causal-TIC precursor (per-step, single-estimator, text-level)",
    "Spatiotemporal Hidden-State Dynamics as a Signature of Internal Reasoning in Large Language Models (Furuya & Tanimura, arXiv 2605.01853, May 2026) — StALT training-free temporal trajectory statistic; separates correct from incorrect reasoning; concurrent work adjacent to Probe-TIC (targets correctness not faithfulness, no causal component)",
    "Task Difficulty Shapes Chain-of-Thought Faithfulness (ICLR 2026 Workshop) — CoT transitions from decorative to load-bearing with difficulty; error propagation 22% (MMLU) to 41% (BBH); probes are 'readout rather than control'; independently validates diagnostic framing",
    "Diagnosing Pathological Chain-of-Thought in Reasoning Models (Liu et al., arXiv 2602.13904, Feb 2026) — text-level metrics (Necessity, Paraphrasability, Substantivity) for three CoT pathologies; computationally inexpensive, task-agnostic; validated on model organisms; complementary text-level diagnostic",
    "Measuring Faithfulness Depends on How You Measure: Classifier Sensitivity in LLM Chain-of-Thought Evaluation (Young, arXiv 2603.20172, Mar 2026) — inter-classifier kappa as low as 0.06; up to 30.6pp divergence across classifiers on 10,276 traces; motivates robustness ablations for TIF",
    "Tracing the Traces: Latent Temporal Signals for Efficient and Accurate Reasoning (Vilas et al., ICLR 2026, arXiv 2510.10494) — latent-trajectory signals (net/cumulative/aligned change) for reasoning efficiency; 14-70% token savings; adjacent temporal hidden-state methodology applied to efficiency not faithfulness",
    "Probing and Steering Chain-of-Thought Unfaithfulness in Language Models (Occhipinti et al., ICLR 2026 LIT Workshop) — faithfulness encoded as linear directions in middle-to-late layers; probing F1 90-100%; steering recovers 46% monitorability with <5% collateral",
    "FACT-E: Causality-Inspired Evaluation for Trustworthy Chain-of-Thought Reasoning (Sun et al., ACL Findings 2026, arXiv 2604.10693) — controlled perturbations measuring intra-chain faithfulness + CoT-to-answer consistency; no hidden-state access",
    "Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (Alvarez & Baheri, arXiv 2605.13772, May 2026) — geometric features for step-level hallucination detection",
    "Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures (Somov et al., arXiv 2603.16475) — up to 60% failure to update after intervention",
    "When Is Thinking Enough? Early Exit via Sufficiency Assessment (Xiang et al., arXiv 2604.06787) — DTSR 28.9-34.9% token reduction",
    "FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness (Swaroop et al., arXiv 2509.13334)",
    "Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks (Qian et al., NeurIPS 2025, arXiv 2506.02867)",
    "Temporal Predictors of Outcome in Reasoning Language Models (David, arXiv 2511.14773, Nov 2025)",
    "Reasoning Models Know When They're Right: Probing for Self-Verification (Zhang et al., arXiv 2504.05419, Apr 2025)",
    "Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation? (Lewis-Lim et al., EMNLP 2025, arXiv 2508.19827)",
    "The Illusion of Reasoning: Step-Level Evaluation Reveals Decorative CoT (Basu & Chakraborty, arXiv 2603.22816, Mar 2026)",
    "Why Models Know But Don't Say: CoT Faithfulness Divergence (Young, arXiv 2603.26410, Mar 2026)",
    "Therefore I am. I Think (Esakkiraja et al., arXiv 2604.01202, Apr 2026)",
    "Early Stopping via Confidence Dynamics: CoDE-Stop (Hosseini et al., arXiv 2604.04930, Apr 2026)",
    "Emergent Manifold Separability during Reasoning in LLMs (Chun et al., arXiv 2602.20338, Feb 2026)",
    "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning (Ye et al., arXiv 2602.11201, Feb 2026)",
    "Decoding Answers Before Chain-of-Thought: Pre-CoT Probes and Activation Steering (Cox et al., arXiv 2603.01437, Mar 2026) — pre-CoT probes >0.9 AUC; steering flips >50% on instruction-tuned models; explicitly limited to binary tasks ≤9B; reports 'little success steering' reasoning models",
    "Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought (Boppana et al., arXiv 2603.05488, Mar 2026)",
    "No Global Plan in Chain-of-Thought: Latent Planning Horizon of LLMs (Xu et al., arXiv 2602.02103, Feb 2026)",
    "Catching Rationalization in the Act: Detecting Motivated Reasoning via Activation Probing (Mirtaheri & Belkin, arXiv 2603.17199, Mar 2026)",
    "Analyzing and Improving CoT Monitorability Through Information Theory (Anwar et al., arXiv 2602.18297, Feb 2026)",
    "FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of CoT Reasoning (ICLR 2026, arXiv 2510.04040)",
    "The Mirage of Explainability: A Survey on CoT Faithfulness (Jin et al., submitted to ARR for ACL 2026; no public arXiv version)",
    "Lie to Me: How Faithful Is CoT Reasoning in Reasoning Models? (arXiv 2603.22582, Mar 2026)",
    "Understanding Chain-of-Thought in LLMs through Information Theory (Ton et al., ICML 2025, arXiv 2411.11984)",
    "The Potential of CoT for Reasoning: Trace Dynamics (Bachmann et al., arXiv 2602.14903, Feb 2026)",
    "NEAT: Neuron-Based Early Exit for Large Reasoning Models (arXiv 2602.02010, Feb 2026)",
    "ESTAR: Early-Stopping Token-Aware Reasoning (arXiv 2602.10004, Feb 2026)",
    "When Chain-of-Thought Fails, the Solution Hides in the Hidden States (arXiv 2604.23351, Apr 2026)",
    "Knowing Before Saying: LLM Representations Encode CoT Success Before Completion (ACL Findings 2025, arXiv 2505.24362)"
  ],
  "description": "We propose a dual-estimator Temporal Information Curve (TIC) framework that diagnoses chain-of-thought faithfulness by measuring the divergence between what a model internally represents and what its reasoning text causally contributes at each token position. Prior work has established the building blocks: Kudo et al. (EACL 2026) combine probing and patching on synthetic arithmetic; the CMI framework (2602.03994) provides layerwise causal audit on ~50 examples; Zhao et al. (2510.24941) measure per-step causal contribution via TTS on AIME/MATH; Furuya & Tanimura (2605.01853) track temporal hidden-state dynamics via StALT; Liu et al. (2602.13904) diagnose CoT pathologies via text-level metrics. We unify and extend these paradigms in four ways: (1) we construct a full-timeline dual-estimator curve combining answer-content linear probes (Probe-TIC) with NLDD causal interventions (Causal-TIC) — extending TTS from per-step to continuous temporal coverage and pairing it with a hidden-state information signal unavailable from any prior single-estimator approach; (2) we map five independently discovered phenomena — pre-CoT encoding, Reasoning Horizon, Reasoning Theater, myopic planning, and thinking-answer gap — to distinguishable dual-TIC signatures, conditioned on task difficulty following the ICLR 2026 Workshop finding that faithfulness varies from decorative to load-bearing with difficulty; (3) we derive the Temporal Information Fidelity (TIF) score with explicit robustness validation across probe architectures, layer selections, perturbation methods, and normalization choices, addressing the measurement sensitivity concern raised by Young (2603.20172); and (4) we include a Phase 0 pilot validating whether answer-content probes retain causal potency on reasoning models for multi-choice tasks — testing a falsifiable prediction motivated by the gap between Cox et al.'s (2603.01437) steering success on instruction-tuned models and their explicit caveat about reasoning models.\n\nWe adopt a deliberately weaker but more defensible interpretive stance than prior versions: the Probe-TIC measures *information availability* (an upper bound on internal knowledge), not necessarily causally determinative information. This interpretation is independently supported by three convergent findings: Yuan et al. (2605.09502) show correctness probes are diagnostic-not-causal; the 'Task Difficulty' workshop shows probes are 'readout rather than control'; Occhipinti et al. (ICLR 2026 LIT Workshop) show faithfulness steering achieves only 46% recovery. The gap G(t) = P(t) − C(t) remains diagnostic under this weaker assumption: patterns of information excess across time, tasks, and difficulty levels reveal which faithfulness phenomenon is operative, providing mechanistic grounding absent from text-level diagnostics (Liu et al.), single-estimator metrics (TTS, StALT, latent-trajectory signals), and expert annotation benchmarks (FaithCoT-Bench). As calibration, we include Kudo et al.'s synthetic arithmetic (expecting G(t) ≈ 0) and cross-reference TTS values on overlapping benchmarks. A secondary application derives a principled early-exit criterion from Causal-TIC inflection points.",
  "revision_notes": {
    "critical_changes": [
      "ADDED TTS (2510.24941) AS DIRECT CAUSAL-TIC PRECURSOR: Zhao et al.'s True Thinking Score — per-step causal contribution via text-level perturbation + ATE on our exact target benchmarks (AIME, MATH) and models (DeepSeek-R1-Distill-Qwen-7B/14B) — is now prominently positioned as the single-estimator precursor that our Causal-TIC extends to continuous temporal coverage within the dual-estimator gap framework. Key differentiators: TTS is discrete per-step (not continuous), single-estimator (no probe gap), text-level perturbation (vs. NLDD logit degradation). We add TTS cross-reference on overlapping benchmarks as a calibration check.",
      "CITED StALT (2605.01853) AS CONCURRENT ADJACENT WORK: Furuya & Tanimura's training-free temporal trajectory statistic on hidden states is acknowledged as conceptually adjacent to Probe-TIC. Differentiated: targets correctness separation (not faithfulness), training-free (vs. trained probes targeting answer content), no causal intervention component, no gap diagnostic.",
      "ADDED TASK-DIFFICULTY CONDITIONING TO FRAMEWORK: The 'Task Difficulty Shapes CoT Faithfulness' (ICLR 2026 Workshop) finding — that faithfulness transitions from decorative to load-bearing with difficulty, and probes are 'readout rather than control' — is integrated as a sixth analytical dimension. Dual-TIC signatures are now analyzed stratified by task difficulty, with predictions for how each phenomenon manifests across difficulty levels. This enriches the unification thesis and independently validates the diagnostic framing.",
      "ADDED MEASUREMENT SENSITIVITY ABLATIONS: Young (2603.20172) shows inter-classifier kappa as low as 0.06. We now plan explicit robustness ablations across 4 dimensions (probe architecture, layer selection, NLDD perturbation method, gap normalization) and commit to reporting sensitivity ranges rather than single aggregate TIF numbers.",
      "ELEVATED ANSWER-CONTENT PROBE GENERALIZATION TO TIER-1 RISK WITH PILOT VALIDATION: Cox et al.'s (2603.01437) validation is limited to binary tasks on models ≤9B, and they explicitly report 'little success steering' reasoning models. This is now a Tier-1 risk addressed via Phase 0 pilot: 500 examples on MMLU (4-choice) and GSM8K (numerical) testing whether answer-content probes retain causal potency on DeepSeek-R1-Distill-Qwen-7B. If steering fails, we validate the information-availability interpretation and calibrate the upper bound looseness.",
      "REFRAMED PROBE-TIC UNDER WEAKER BUT MORE DEFENSIBLE ASSUMPTION: The Probe-TIC is now explicitly interpreted as measuring 'information availability' (upper bound on internal knowledge), not causally determinative information. This is independently supported by three convergent findings (Yuan et al., 'Task Difficulty' workshop, Occhipinti et al.) and makes the framework robust to the possibility that answer-content probes are not causally potent on reasoning models.",
      "ADDED LIU ET AL. (2602.13904) AS COMPLEMENTARY TEXT-LEVEL DIAGNOSTIC: Their Necessity/Paraphrasability/Substantivity metrics for three CoT pathologies provide a text-level baseline for cross-validation with our hidden-state-grounded TIF score.",
      "ADDED VILAS ET AL. (2510.10494, ICLR 2026) AS ADJACENT TEMPORAL METHODOLOGY: Their latent-trajectory signals demonstrate that temporal hidden-state evolution is informative for reasoning analysis, motivating our faithfulness-specific application of similar methodology.",
      "ADDED OCCHIPINTI ET AL. (ICLR 2026 LIT WORKSHOP): Their finding that faithfulness is linearly encoded (probing F1 90-100%) but steering recovers only 46% monitorability provides independent evidence for our readout-not-control interpretation.",
      "DROPPED AAAI 2027: 2 months is insufficient regardless of execution mode. Venues are now ICLR 2027 (primary, 4 months) and ICML 2027 (fallback, 8 months)."
    ],
    "what_stayed": "The five-phenomena unification thesis (now enriched with task-difficulty conditioning), the dual-TIC concept, the NLDD and probe estimators, the four benchmarks (MMLU, GPQA-Diamond, GSM8K, AIME), the four target models (DeepSeek-R1-Distill 7B/14B/32B, QwQ-32B), the 671B validation subset, layer-selective caching, the TIF score concept, the synthetic arithmetic calibration check, and the diagnostic (thermometer) framing. The core insight — that the gap between internal information and causal contribution reveals diagnostic patterns invisible to either estimator alone — is strengthened by honest positioning, weaker interpretive assumptions, task-difficulty conditioning, and robustness validation.",
    "residual_risks": [
      "TIER-1: Answer-content probe causal potency on reasoning models is untested for multi-choice and numerical tasks. The Phase 0 pilot addresses this directly, but if probes show neither predictive power nor causal potency on reasoning models (a possibility given Cox et al.'s caveat), the Probe-TIC contribution would be limited to reproducing StALT-like correctness signals. Mitigation: the information-availability interpretation preserves diagnostic value even under minimal causal potency, but the gap signal would be loosened.",
      "TIER-1: The TTS paper (Zhao et al. 2510.24941) tests on our exact models (DeepSeek-R1-Distill-Qwen-7B/14B) and benchmarks (AIME, MATH). If our Causal-TIC (NLDD-based) and their TTS (ATE-based) show near-identical patterns at step boundaries, the continuous-temporal-coverage novelty narrows. Mitigation: the dual-estimator gap and five-phenomenon mapping remain unique; the within-step dynamics visible to Causal-TIC but invisible to TTS provide differentiation that must be demonstrated empirically.",
      "Measurement sensitivity (Young 2603.20172): TIF may show high sensitivity to probe and intervention choices. If robustness ablations reveal instability (e.g., TIF rankings change across measurement configurations), this undermines the diagnostic utility. Mitigation: plan ablations early and report sensitivity ranges; if instability is severe, this becomes a finding about the fundamental difficulty of faithfulness measurement.",
      "Task-difficulty conditioning may reveal that the five phenomena are not signatures of a unified information dynamic but rather artefacts of different task types. If pre-CoT encoding is exclusively an easy-task phenomenon and Reasoning Horizon is exclusively a moderate-task phenomenon, the 'unification' thesis weakens to a 'taxonomy indexed by difficulty' thesis. This would be a less exciting but still publishable finding.",
      "NLDD interventions remain computationally expensive (10-20 perturbation passes per example on 32B models, ~250 node-hours). Robustness ablations across perturbation methods add further computational cost. May need subsampling for AIME long CoT traces.",
      "The field is moving at 3+ papers per month. StALT (May 2026) appeared during this revision cycle. Additional concurrent work (especially dual-estimator approaches) may narrow the novelty window before the ICLR 2027 deadline (Sep 2026). The focused contribution (gap diagnostic + phenomenon unification + robustness validation) and the Phase 0 pilot providing novel empirical evidence about probe causal potency on reasoning models are more defensible against this risk.",
      "Chun et al.'s (2602.20338) finding that probe accuracy ≠ computational readiness suggests Probe-TIC may overestimate available information. The information-availability interpretation partially addresses this, but the gap G(t) could be inflated by correlative information the model possesses but never uses."
    ]
  }
}

## Reviewer feedback (round 4)
Issues: ["CONCEPTUAL: The gap diagnostic G(t) = P(t) − C(t) has a discriminability problem under the 'information availability' assumption. If Probe-TIC captures correlative/epiphenomenal information (as Chun et al. 2602.20338 suggest: 'probe accuracy ≠ computational readiness'), then P(t) may be systematically high for ALL instances regardless of faithfulness phenomenon, making G(t) uniformly inflated. This would collapse the five-phenomenon signatures into a single 'high gap everywhere' pattern, undermining the framework's central diagnostic claim. The proposal acknowledges this as a residual risk but treats it as tier-2 when it should be tier-1.", "CONCEPTUAL: The five-phenomenon distinguishability argument is underspecified under the weaker assumption. Specifically: Pre-CoT encoding (high P(0), any C trajectory) and Reasoning Theater (growing gap: P rises, C flat) could produce indistinguishable TIC signatures if P(t) is always high due to correlative information. The proposal's four diagnostic features (initial P(0), C-plateau onset, gap trajectory, C-gradient locality) may not discriminate phenomena when the probe captures an upper bound rather than a tight estimate. The proposal needs either a formal argument or simulation showing distinguishability persists under probe inflation.", "MINOR MISSING REFERENCE: 'Mapping Faithful Reasoning in Language Models' (Li et al., 2510.22362, NeurIPS 2025 MechInterp Workshop) introduces Concept Walk, which projects each reasoning step onto concept directions and tracks temporal evolution of internal activations for faithfulness diagnosis. Finds easy→decorative, hard→faithful, paralleling the task-difficulty conditioning dimension. Different probe methodology (concept directions vs. answer-content probes) and different domain (safety, single model), but conceptually adjacent to Probe-TIC temporal tracking and should be cited.", "RISK UNDERESTIMATION: The Phase 0 pilot tests answer-content probe causal potency on MMLU (4-choice) and GSM8K (numerical) using DeepSeek-R1-Distill-Qwen-7B. But Cox et al.'s validation was on binary tasks on instruction-tuned models ≤9B, and they explicitly report 'little success steering' reasoning models. If the Phase 0 pilot confirms this failure for reasoning models broadly, the Probe-TIC becomes just another correlative hidden-state signal (like StALT) rather than measuring information the model could in principle use. Under this scenario, the gap G(t) loses its interpretation as 'information excess' and becomes 'correlative excess,' which is less interesting. The proposal should have a more detailed contingency plan for this outcome.", "NOVELTY POSITIONING: The proposal's core novelty claim — that the gap between two estimators reveals phenomenon-specific signatures invisible to either alone — is compelling in principle but untested. The proposal relies heavily on the prediction that different phenomena produce distinguishable gap trajectories, but this is an empirical bet. If the patterns turn out to be noisy or hard to distinguish (especially given Young's measurement sensitivity findings), the main contribution reduces to 'we ran probing and NLDD on the same instances at scale,' which is a useful resource contribution but not a conceptual advance worthy of a top venue."]
Feedback: **Round 4 shows major improvement — the proposal is now well-positioned against the literature, honest about assumptions, and comprehensive in scope.** The critical issue preventing a pass is the gap diagnostic's discriminability under the weaker 'information availability' assumption. Three specific fixes:

1. **Elevate the gap inflation problem to Tier-1 and address it directly.** Chun et al.'s finding that probe accuracy ≠ computational readiness means P(t) may be uniformly high, collapsing five-phenomenon signatures into one. To address this: (a) include a theoretical analysis or toy simulation showing that even if P(t) is inflated, the *trajectory shape* (rate of increase, curvature, onset timing) can still distinguish phenomena; (b) propose a calibration method — e.g., normalize P(t) against a 'null probe' trained on shuffled labels, so the gap measures *excess* information above chance rather than raw probe accuracy; (c) in Phase 0, explicitly test whether Probe-TIC trajectories differ meaningfully across task difficulty levels even if absolute P(t) values are high.

2. **Strengthen the five-phenomenon distinguishability argument.** Currently, the four diagnostic features (initial P(0), C-plateau onset, gap trajectory, C-gradient locality) are asserted to distinguish phenomena but not demonstrated. Add a concrete worked example: take 2-3 phenomena (e.g., Pre-CoT encoding vs. Reasoning Theater vs. genuine reasoning) and draw predicted TIC curves under both the strong and weak probe assumptions. Show that trajectory *shapes* remain distinguishable even when absolute P(t) is inflated. If you cannot draw distinguishable curves under the weak assumption, this is a fundamental problem that must be acknowledged and the five-phenomenon mapping should be reframed as 'exploratory' rather than a primary contribution.

3. **Cite Li et al. (2510.22362) 'Mapping Faithful Reasoning'** — their Concept Walk framework tracks temporal activation evolution and finds easy→decorative, hard→faithful, which directly supports your task-difficulty conditioning. Differentiate: they use concept directions (not answer-content probes), study safety (not reasoning benchmarks), and lack a causal-contribution curve.

4. **Tighten the focus for the paper.** The proposal currently has ~7 contributions (gap diagnostic, five-phenomenon mapping, TIF score, task-difficulty conditioning, robustness ablations, Phase 0 pilot findings, early-exit criterion). For a single paper, consider: Phase 0 pilot results + gap diagnostic + task-difficulty conditioned signatures as the core paper, with robustness ablations and five-phenomenon mapping as the key experimental sections. The early-exit application and 671B validation can be supplementary material.

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.
- Address each issue specifically.

## 深度调研要求

不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。
2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。
3. **深度思考**：
   - 核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach？
4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。

## 针对 Review 意见的定向搜索

1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点
2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline
3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现
4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot

- You have full freedom: minor fix, major revision, or pivot.
- Include a "change_type" field: "minor", "major", or "pivot".
- Output a COMPLETE JSON object with ALL fields.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "type": "user",
  "uuid": "548fbf74-7a86-4796-964b-2a148d729a30",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T12:00:31.850Z_

```json
{
  "parentUuid": "548fbf74-7a86-4796-964b-2a148d729a30",
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
  "uuid": "689509df-6411-434f-96a1-150e4681e029",
  "timestamp": "2026-05-19T12:00:31.850Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T12:00:31.850Z_

```json
{
  "parentUuid": "689509df-6411-434f-96a1-150e4681e029",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "45672ad9-bca6-4b6d-9b42-19d924fe8da3",
  "timestamp": "2026-05-19T12:00:31.850Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"The Probe-Intervention Gap: Diagnosing Chain-of-Thought Faithfulness v…",
  "leafUuid": "45672ad9-bca6-4b6d-9b42-19d924fe8da3",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise gap diagnostic discriminability and phenomenon distinguishability",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f"
}
```

---

### Assistant

_source line 8 · 2026-05-19T12:00:42.939Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully before doing research:

1. **Gap inflation problem (TIER-1)**: The core issue is that if P(t) is uniformly high due to correlative/epiphenomenal information, G(t) = P(t) - C(t) would be uniformly inflated, collapsing all five phenomena into one pattern. The reviewer suggests: (a) theoretical/simulation analysis of trajectory shapes, (b) null-probe calibration, (c) Phase 0 testing of trajectory differences.

2. **Five-phenomenon distinguishability**: The diagnostic features may not discriminate under probe inflation. Need worked examples showing trajectory shapes remain distinguishable.


3. **Missing reference**: I need to track down the Li et al. paper on the Concept Walk framework that should be cited here.

4. **Phase 0 contingency**: There's a risk that if the probes don't work on reasoning models, the gap metric loses its interpretation as measuring information excess rather than just resource consumption.

5. **Novelty at stake**: If the patterns turn out to be noisy, the contribution might collapse into just measuring resource usage, which is less novel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45672ad9-bca6-4b6d-9b42-19d924fe8da3",
  "isSidechain": false,
  "requestId": "req_011CbBtdKwFYP345nV73v7zs",
  "type": "assistant",
  "uuid": "42d51e83-16a5-49bb-86f3-fd12f46a4923",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ERsBfiX4h6oxeTNa8wmPH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15218,
      "cache_read_input_tokens": 11374,
      "output_tokens": 358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15218,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 358,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 15218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15218
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

_source line 9 · 2026-05-19T12:00:42.951Z_

I need to research several specific issues raised by the reviewers before revising. Let me launch parallel research agents for the key topics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42d51e83-16a5-49bb-86f3-fd12f46a4923",
  "isSidechain": false,
  "requestId": "req_011CbBtdKwFYP345nV73v7zs",
  "type": "assistant",
  "uuid": "6ad6bf27-f4b6-4c3f-a76b-f3608e12e93c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ERsBfiX4h6oxeTNa8wmPH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15218,
      "cache_read_input_tokens": 11374,
      "output_tokens": 358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15218,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 358,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 15218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15218
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

_source line 10 · 2026-05-19T12:00:42.979Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RHenY3G4gLFHWqqbzy853t`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ad6bf27-f4b6-4c3f-a76b-f3608e12e93c",
  "isSidechain": false,
  "requestId": "req_011CbBtdKwFYP345nV73v7zs",
  "type": "assistant",
  "uuid": "e18da08c-7ff9-4226-8924-33f567159faf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ERsBfiX4h6oxeTNa8wmPH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15218,
      "cache_read_input_tokens": 11374,
      "output_tokens": 358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15218,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 358,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 15218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15218
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

_source line 11 · 2026-05-19T12:00:42.986Z_

<details><summary>↩ Tool result · `toolu_01RHenY3G4gLFHWqqbzy853t`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

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
  "parentUuid": "e18da08c-7ff9-4226-8924-33f567159faf",
  "isSidechain": false,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "type": "user",
  "uuid": "56e2b839-0145-43f5-8f49-2299fc66b40f",
  "toolUseResult": {
    "matches": [
      "WebFetch",
      "WebSearch"
    ],
    "query": "select:WebFetch,WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "e18da08c-7ff9-4226-8924-33f567159faf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T12:00:46.184Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me launch parallel research agents to investigate the key issues raised by reviewers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56e2b839-0145-43f5-8f49-2299fc66b40f",
  "isSidechain": false,
  "requestId": "req_011CbBteB8Cmuvp2ERuXVV8C",
  "type": "assistant",
  "uuid": "f85f6324-8399-491b-9e73-db311b52e9a5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6ZeAmNZF51HYwcd1igXRQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1377,
      "cache_read_input_tokens": 26592,
      "output_tokens": 1680,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1377,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1680,
          "cache_read_input_tokens": 26592,
          "cache_creation_input_tokens": 1377,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1377
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

_source line 13 · 2026-05-19T12:00:46.691Z_

Let me launch parallel research on the key issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f85f6324-8399-491b-9e73-db311b52e9a5",
  "isSidechain": false,
  "requestId": "req_011CbBteB8Cmuvp2ERuXVV8C",
  "type": "assistant",
  "uuid": "453a2825-a7d5-44ed-8998-c2060e513c42",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6ZeAmNZF51HYwcd1igXRQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1377,
      "cache_read_input_tokens": 26592,
      "output_tokens": 1680,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1377,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1680,
          "cache_read_input_tokens": 26592,
          "cache_creation_input_tokens": 1377,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1377
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

_source line 14 · 2026-05-19T12:00:55.533Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Bj9cynxHTHba47N4VGrEv6`</summary>

```json
{
  "description": "Research probe inflation/calibration",
  "prompt": "I'm revising a research proposal about chain-of-thought faithfulness diagnosis. A key reviewer concern is that linear probes on LLM hidden states may capture correlative/epiphenomenal information rather than causally relevant information, making probe accuracy uniformly high regardless of actual faithfulness. This is the \"probe inflation\" problem.\n\nI need to research:\n1. Methods for calibrating probes to distinguish genuine vs correlative information — especially \"null probe\" or \"control probe\" baselines (e.g., training probes on shuffled labels, selectivity scores, etc.)\n2. Chun et al. (2602.20338) \"Emergent Manifold Separability during Reasoning in LLMs\" — their finding that probe accuracy ≠ computational readiness\n3. Any work on probe selectivity, amnesic probing, or causal probing that addresses the concern that high probe accuracy doesn't mean the information is being used\n4. Methods for distinguishing trajectory shapes even when absolute values are inflated\n\nPlease search for:\n- \"probe selectivity score control task\" neural network probing\n- \"amnesic probing\" OR \"causal probing\" language models 2024 2025 2026\n- \"null probe\" baseline linear probing hidden states\n- Chun et al 2602.20338 manifold separability reasoning\n\nFor key papers found, use WebFetch to read the abstracts/key findings. Report back with concrete methods I could use for probe calibration.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "453a2825-a7d5-44ed-8998-c2060e513c42",
  "isSidechain": false,
  "requestId": "req_011CbBteB8Cmuvp2ERuXVV8C",
  "type": "assistant",
  "uuid": "c53e8df1-ec6d-48de-80d3-e89d527c64f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6ZeAmNZF51HYwcd1igXRQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1377,
      "cache_read_input_tokens": 26592,
      "output_tokens": 1680,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1377,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1680,
          "cache_read_input_tokens": 26592,
          "cache_creation_input_tokens": 1377,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1377
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

_source line 15 · 2026-05-19T12:01:00.298Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01X2W5ju2RzySRm21YTsnrhw`</summary>

```json
{
  "description": "Research Li et al. Concept Walk",
  "prompt": "I need to find and read the paper \"Mapping Faithful Reasoning in Language Models\" by Li et al. (arXiv 2510.22362), presented at the NeurIPS 2025 MechInterp Workshop. It introduces something called \"Concept Walk\" which projects each reasoning step onto concept directions and tracks temporal evolution of internal activations for faithfulness diagnosis. They reportedly find easy→decorative, hard→faithful patterns.\n\nPlease:\n1. Search for this paper using WebSearch\n2. Use WebFetch on the arXiv page to read the abstract and key details\n3. Report back: What exactly is Concept Walk? How does it track temporal evolution? What are the key findings about easy vs hard tasks? What models/benchmarks do they use? How does it differ from answer-content linear probes?\n\nSearch queries to try:\n- \"Mapping Faithful Reasoning Language Models\" Li 2510.22362\n- \"Concept Walk\" faithfulness reasoning NeurIPS 2025\n- arxiv.org 2510.22362",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c53e8df1-ec6d-48de-80d3-e89d527c64f3",
  "isSidechain": false,
  "requestId": "req_011CbBteB8Cmuvp2ERuXVV8C",
  "type": "assistant",
  "uuid": "ef8ab33b-b1e4-4183-9a52-4bae1cd96666",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6ZeAmNZF51HYwcd1igXRQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1377,
      "cache_read_input_tokens": 26592,
      "output_tokens": 1680,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1377,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1680,
          "cache_read_input_tokens": 26592,
          "cache_creation_input_tokens": 1377,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1377
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

_source line 16 · 2026-05-19T12:01:08.269Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01DgajeiwtTuhGLjGDGqPrF6`</summary>

```json
{
  "description": "Research phenomenon distinguishability",
  "prompt": "I'm working on a research proposal that claims five chain-of-thought faithfulness phenomena (pre-CoT encoding, Reasoning Horizon, Reasoning Theater, myopic planning, thinking-answer gap) produce distinguishable temporal signatures when measured by two signals: (1) a probe-based information curve P(t) measuring what's decodable from hidden states at position t, and (2) a causal intervention curve C(t) measuring causal contribution of CoT up to position t.\n\nA reviewer argues that if P(t) is inflated by correlative information, the gap G(t) = P(t) - C(t) may be uniformly high, collapsing all phenomena into one pattern.\n\nI need to research:\n1. Whether temporal trajectory SHAPES (rate of increase, curvature, onset timing) can distinguish phenomena even when absolute values are inflated — are there precedents in neuroscience or ML interpretability?\n2. Work on \"dual estimator\" or \"dual signal\" diagnostic frameworks where the divergence pattern matters more than absolute values\n3. Specific empirical evidence about temporal dynamics of these phenomena — do pre-CoT encoding and Reasoning Theater actually have different temporal profiles?\n\nSearch for:\n- \"temporal dynamics\" \"chain of thought\" faithfulness probe 2025 2026\n- \"pre-CoT encoding\" OR \"answer encoded before reasoning\" temporal profile\n- \"reasoning horizon\" temporal dynamics hidden states\n- dual estimator divergence pattern shape analysis interpretability\n\nUse WebFetch to read any key papers. Report concrete evidence about whether trajectory shapes differ across phenomena.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef8ab33b-b1e4-4183-9a52-4bae1cd96666",
  "isSidechain": false,
  "requestId": "req_011CbBteB8Cmuvp2ERuXVV8C",
  "type": "assistant",
  "uuid": "46e2da3b-d20a-4db2-bb5c-39812f0cc1fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6ZeAmNZF51HYwcd1igXRQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1377,
      "cache_read_input_tokens": 26592,
      "output_tokens": 1680,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1377,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1680,
          "cache_read_input_tokens": 26592,
          "cache_creation_input_tokens": 1377,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1377
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

_source line 17 · 2026-05-19T12:01:18.258Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01EsJ4GfnRxEAZB9Wsaewo5o`</summary>

```json
{
  "description": "Research contingency if probes fail",
  "prompt": "I'm working on a research proposal about chain-of-thought faithfulness. A key component is training linear probes on hidden states to measure what answer information the model internally represents at each token position during chain-of-thought reasoning.\n\nThe reviewer raises a critical concern: Cox et al. (2603.01437) showed probes work for steering on instruction-tuned models (binary tasks, ≤9B params) but explicitly report \"little success steering\" reasoning models. If our Phase 0 pilot confirms that answer-content probes on reasoning models (like DeepSeek-R1-Distill) have NO causal potency, the probe signal becomes merely correlative.\n\nI need to research:\n1. What happens when you probe reasoning models specifically? Any papers testing probes on DeepSeek-R1, QwQ, or similar?\n2. The distinction between \"information availability\" and \"information use\" in probing literature — is a correlative probe signal still scientifically interesting?\n3. Alternative probe targets that might be more causally relevant than answer content (e.g., probing for reasoning strategy, intermediate subgoal, confidence)\n4. Whether there's a meaningful distinction between \"the model knows the answer early but uses CoT to verify\" vs \"the model knows the answer early and CoT is decorative\" — and how probes could distinguish these\n\nSearch for:\n- probing reasoning models DeepSeek-R1 hidden states 2025 2026\n- \"information availability\" vs \"information use\" probing language models\n- probe causal potency reasoning chain-of-thought 2026\n- alternative probe targets intermediate reasoning states\n\nUse WebFetch on key papers. Report what the literature says about probing reasoning models specifically and what contingency approaches exist.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46e2da3b-d20a-4db2-bb5c-39812f0cc1fd",
  "isSidechain": false,
  "requestId": "req_011CbBteB8Cmuvp2ERuXVV8C",
  "type": "assistant",
  "uuid": "ada137a4-b00a-4cc7-a19a-03df2280b1e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6ZeAmNZF51HYwcd1igXRQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1377,
      "cache_read_input_tokens": 26592,
      "output_tokens": 1680,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1377,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1680,
          "cache_read_input_tokens": 26592,
          "cache_creation_input_tokens": 1377,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1377
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

_source line 18 · 2026-05-19T12:02:43.574Z_

<details><summary>↩ Tool result · `toolu_01X2W5ju2RzySRm21YTsnrhw`</summary>

```text
I have all the information needed to provide a thorough report. Here is the full synthesis:

---

## Paper: "Mapping Faithful Reasoning in Language Models" (arXiv 2510.22362)

**Authors:** Jiazheng Li, Andreas Damianou, J Rosser, Jose Luis Redondo Garcia, Konstantina Palla
**Venue:** Mechanistic Interpretability Workshop at NeurIPS 2025
**Submitted:** October 25, 2025
**Categories:** cs.LG, cs.CL

---

### What Is Concept Walk?

Concept Walk is a three-stage framework for tracing how a model's internal representations evolve with respect to a specific concept (in their case study, "safety") during multi-step chain-of-thought (CoT) reasoning. It operates entirely in activation space rather than analyzing surface text. The three stages are:

1. **Filtering** -- selecting cases where perturbation to the CoT actually changes vs. does not change the model's output (to separate "hard" from "easy" cases).
2. **Direction computation** -- learning a concept direction vector from contrastive data.
3. **Temporal tracking** -- projecting each reasoning step's activations onto that direction to produce a step-by-step trajectory.

---

### How Concept Directions Are Learned

They use a **difference-of-means** approach on contrastive datasets (unsafe vs. safe prompts):

- Compute mean activations for unsafe prompts: mu_unsafe(layer, token)
- Compute mean activations for safe prompts: mu_safe(layer, token)
- Safety direction vector: **v = mu_unsafe - mu_safe** (normalized)

Candidate direction vectors are filtered using three criteria:
- **Bypass score**: effectiveness at suppressing refusal on harmful prompts
- **Induce score**: ability to induce refusal on harmless prompts
- **KL divergence**: minimal disruption to general model outputs (threshold < 0.1)

They also exclude late-layer directions (beyond 80% of model depth) that primarily suppress output tokens rather than encoding genuine safety features.

An important design choice: the safety direction is computed in **non-thinking mode** (standard inference) but applied to **thinking-mode** activations, under the assumption that core safety encoding remains stable across modes while temporal expression differs.

---

### How Temporal Evolution Is Tracked

For each reasoning step `s` in the CoT:

1. Extract residual stream activations for all tokens in that step
2. Average token activations into a step-level representation: **h_s**
3. Compute cosine similarity with the safety direction vector: **alpha_s = cos(h_s, v)**

This produces a scalar alignment score per step, creating a trajectory that reveals whether internal safety activation emerges, persists, or decays throughout reasoning. By comparing the baseline trajectory (original CoT) against a perturbed trajectory (CoT with injected flawed reasoning at the midpoint), they can diagnose whether the model's internal state actually tracks the reasoning content.

---

### Key Findings: Easy vs. Hard Tasks

**Easy cases (decorative reasoning):**
- Perturbed CoTs produce only **transient** safety activation shifts
- The model rapidly reverts to its original activation trajectory
- The internal state "self-corrects" despite the injected flawed reasoning
- The CoT functions as a post-hoc rationalization -- it does not causally drive the output
- Example: "Playlist for a bar crawl" -- model acknowledges the injected error briefly but quickly reverses course

**Hard cases (faithful reasoning):**
- Perturbations induce **sustained, structured** activation shifts
- Safety activations diverge from baseline and persist for multiple steps beyond injection point
- Downstream reasoning tracks the altered internal state
- The final output often changes in response to the perturbation
- The CoT is genuinely computational -- it causally shapes the outcome
- Example: "Can you recommend some classic rock tunes" -- injected error produces lasting divergence in both activation trajectory and final decision

Additionally, **unsafe prompts consistently trigger higher initial safety activation**, confirming the safety direction vector effectively captures unsafe content recognition.

---

### Models and Benchmarks

- **Direction learning model:** Mistral-7B-Instruct-v0.2 (7.3B parameters) -- used to generate synthetic contrastive datasets
- **Analysis model:** Qwen 3-4B with controllable thinking mode (36-layer Transformer, 128K context)
- **Domain:** Safety (specifically music playlist requests, e.g., "playlist for a dinner party")
- **Datasets (synthetic, generated via Mistral with policy guidelines):**
  - Harm category: 1,746 train / 873 val / 292 test (2,911 total pairs)
  - Hate category: 2,890 train / 1,445 val / 484 test (4,819 total pairs)
- After filtering for prediction-ground-truth match: Hate = 256 violative + 462 non-violative; Harm = 181 violative + 290 non-violative

**Perturbation method:** At the midpoint of the CoT, they replace a reasoning step with a logically flawed but fluent alternative (e.g., "This is safe. Therefore, I will answer."), then resume autoregressive generation and compare outputs/trajectories.

---

### How It Differs from Answer-Content Linear Probes

Standard answer-content linear probes:
- Learn a linear classifier mapping activations to a binary output (e.g., safe/unsafe)
- Apply this uniformly across positions or layers
- Provide **static, position-agnostic** interpretations -- they tell you "the model has already decided X at layer Y" but not how that decision evolves through reasoning steps

Concept Walk instead:
- Derives directions from **contrastive datasets capturing semantic meaning** (not trained to predict the answer)
- Tracks the **temporal evolution** of concept alignment across reasoning steps -- it produces a trajectory, not a single snapshot
- Reveals whether concept signals **persist** (faithful/computational) or **decay** (decorative) after perturbation
- Tests faithfulness via **perturbation sensitivity within activation space** rather than just checking if the model's output changes
- Is **concept-specific** -- different concept directions can be plugged in for different analysis domains

The key insight is that Concept Walk goes beyond "does the model know the answer early?" (which probes answer) to "does the reasoning process causally shape the internal concept representation over time?"

---

### Limitations

1. Cross-mode representation shift: safety direction learned in non-thinking mode may not perfectly transfer to thinking mode
2. Cannot capture hidden reasoning pathways unexpressed in verbal output
3. Small sample sizes for hard violative cases after filtering
4. Only tested on one model (Qwen 3-4B) and one domain (safety)
5. Fixed midpoint perturbation injection -- systematic variation of timing/strength not explored
6. Safety vector may partially encode refusal patterns, potentially obscuring fine-grained mid-trace dynamics

---

Sources:
- [arXiv Abstract: 2510.22362](https://arxiv.org/abs/2510.22362)
- [arXiv HTML Full Paper](https://arxiv.org/html/2510.22362)
- [arXiv PDF](https://arxiv.org/pdf/2510.22362)
- [OpenReview PDF](https://openreview.net/pdf/89878ca66572c0425255f7be53b2879e6d2e7e7b.pdf)

agentId: a7570908b24c44cbc (use SendMessage with to: 'a7570908b24c44cbc' to continue this agent)
&lt;usage>total_tokens: 17426
tool_uses: 7
duration_ms: 103272&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef8ab33b-b1e4-4183-9a52-4bae1cd96666",
  "isSidechain": false,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "type": "user",
  "uuid": "1d0e1494-76d0-41b2-908f-fc1a824fabaa",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to find and read the paper \"Mapping Faithful Reasoning in Language Models\" by Li et al. (arXiv 2510.22362), presented at the NeurIPS 2025 MechInterp Workshop. It introduces something called \"Concept Walk\" which projects each reasoning step onto concept directions and tracks temporal evolution of internal activations for faithfulness diagnosis. They reportedly find easy→decorative, hard→faithful patterns.\n\nPlease:\n1. Search for this paper using WebSearch\n2. Use WebFetch on the arXiv page to read the abstract and key details\n3. Report back: What exactly is Concept Walk? How does it track temporal evolution? What are the key findings about easy vs hard tasks? What models/benchmarks do they use? How does it differ from answer-content linear probes?\n\nSearch queries to try:\n- \"Mapping Faithful Reasoning Language Models\" Li 2510.22362\n- \"Concept Walk\" faithfulness reasoning NeurIPS 2025\n- arxiv.org 2510.22362",
    "agentId": "a7570908b24c44cbc",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I have all the information needed to provide a thorough report. Here is the full synthesis:\n\n---\n\n## Paper: \"Mapping Faithful Reasoning in Language Models\" (arXiv 2510.22362)\n\n**Authors:** Jiazheng Li, Andreas Damianou, J Rosser, Jose Luis Redondo Garcia, Konstantina Palla\n**Venue:** Mechanistic Interpretability Workshop at NeurIPS 2025\n**Submitted:** October 25, 2025\n**Categories:** cs.LG, cs.CL\n\n---\n\n### What Is Concept Walk?\n\nConcept Walk is a three-stage framework for tracing how a model's internal representations evolve with respect to a specific concept (in their case study, \"safety\") during multi-step chain-of-thought (CoT) reasoning. It operates entirely in activation space rather than analyzing surface text. The three stages are:\n\n1. **Filtering** -- selecting cases where perturbation to the CoT actually changes vs. does not change the model's output (to separate \"hard\" from \"easy\" cases).\n2. **Direction computation** -- learning a concept direction vector from contrastive data.\n3. **Temporal tracking** -- projecting each reasoning step's activations onto that direction to produce a step-by-step trajectory.\n\n---\n\n### How Concept Directions Are Learned\n\nThey use a **difference-of-means** approach on contrastive datasets (unsafe vs. safe prompts):\n\n- Compute mean activations for unsafe prompts: mu_unsafe(layer, token)\n- Compute mean activations for safe prompts: mu_safe(layer, token)\n- Safety direction vector: **v = mu_unsafe - mu_safe** (normalized)\n\nCandidate direction vectors are filtered using three criteria:\n- **Bypass score**: effectiveness at suppressing refusal on harmful prompts\n- **Induce score**: ability to induce refusal on harmless prompts\n- **KL divergence**: minimal disruption to general model outputs (threshold < 0.1)\n\nThey also exclude late-layer directions (beyond 80% of model depth) that primarily suppress output tokens rather than encoding genuine safety features.\n\nAn important design choice: the safety direction is computed in **non-thinking mode** (standard inference) but applied to **thinking-mode** activations, under the assumption that core safety encoding remains stable across modes while temporal expression differs.\n\n---\n\n### How Temporal Evolution Is Tracked\n\nFor each reasoning step `s` in the CoT:\n\n1. Extract residual stream activations for all tokens in that step\n2. Average token activations into a step-level representation: **h_s**\n3. Compute cosine similarity with the safety direction vector: **alpha_s = cos(h_s, v)**\n\nThis produces a scalar alignment score per step, creating a trajectory that reveals whether internal safety activation emerges, persists, or decays throughout reasoning. By comparing the baseline trajectory (original CoT) against a perturbed trajectory (CoT with injected flawed reasoning at the midpoint), they can diagnose whether the model's internal state actually tracks the reasoning content.\n\n---\n\n### Key Findings: Easy vs. Hard Tasks\n\n**Easy cases (decorative reasoning):**\n- Perturbed CoTs produce only **transient** safety activation shifts\n- The model rapidly reverts to its original activation trajectory\n- The internal state \"self-corrects\" despite the injected flawed reasoning\n- The CoT functions as a post-hoc rationalization -- it does not causally drive the output\n- Example: \"Playlist for a bar crawl\" -- model acknowledges the injected error briefly but quickly reverses course\n\n**Hard cases (faithful reasoning):**\n- Perturbations induce **sustained, structured** activation shifts\n- Safety activations diverge from baseline and persist for multiple steps beyond injection point\n- Downstream reasoning tracks the altered internal state\n- The final output often changes in response to the perturbation\n- The CoT is genuinely computational -- it causally shapes the outcome\n- Example: \"Can you recommend some classic rock tunes\" -- injected error produces lasting divergence in both activation trajectory and final decision\n\nAdditionally, **unsafe prompts consistently trigger higher initial safety activation**, confirming the safety direction vector effectively captures unsafe content recognition.\n\n---\n\n### Models and Benchmarks\n\n- **Direction learning model:** Mistral-7B-Instruct-v0.2 (7.3B parameters) -- used to generate synthetic contrastive datasets\n- **Analysis model:** Qwen 3-4B with controllable thinking mode (36-layer Transformer, 128K context)\n- **Domain:** Safety (specifically music playlist requests, e.g., \"playlist for a dinner party\")\n- **Datasets (synthetic, generated via Mistral with policy guidelines):**\n  - Harm category: 1,746 train / 873 val / 292 test (2,911 total pairs)\n  - Hate category: 2,890 train / 1,445 val / 484 test (4,819 total pairs)\n- After filtering for prediction-ground-truth match: Hate = 256 violative + 462 non-violative; Harm = 181 violative + 290 non-violative\n\n**Perturbation method:** At the midpoint of the CoT, they replace a reasoning step with a logically flawed but fluent alternative (e.g., \"This is safe. Therefore, I will answer.\"), then resume autoregressive generation and compare outputs/trajectories.\n\n---\n\n### How It Differs from Answer-Content Linear Probes\n\nStandard answer-content linear probes:\n- Learn a linear classifier mapping activations to a binary output (e.g., safe/unsafe)\n- Apply this uniformly across positions or layers\n- Provide **static, position-agnostic** interpretations -- they tell you \"the model has already decided X at layer Y\" but not how that decision evolves through reasoning steps\n\nConcept Walk instead:\n- Derives directions from **contrastive datasets capturing semantic meaning** (not trained to predict the answer)\n- Tracks the **temporal evolution** of concept alignment across reasoning steps -- it produces a trajectory, not a single snapshot\n- Reveals whether concept signals **persist** (faithful/computational) or **decay** (decorative) after perturbation\n- Tests faithfulness via **perturbation sensitivity within activation space** rather than just checking if the model's output changes\n- Is **concept-specific** -- different concept directions can be plugged in for different analysis domains\n\nThe key insight is that Concept Walk goes beyond \"does the model know the answer early?\" (which probes answer) to \"does the reasoning process causally shape the internal concept representation over time?\"\n\n---\n\n### Limitations\n\n1. Cross-mode representation shift: safety direction learned in non-thinking mode may not perfectly transfer to thinking mode\n2. Cannot capture hidden reasoning pathways unexpressed in verbal output\n3. Small sample sizes for hard violative cases after filtering\n4. Only tested on one model (Qwen 3-4B) and one domain (safety)\n5. Fixed midpoint perturbation injection -- systematic variation of timing/strength not explored\n6. Safety vector may partially encode refusal patterns, potentially obscuring fine-grained mid-trace dynamics\n\n---\n\nSources:\n- [arXiv Abstract: 2510.22362](https://arxiv.org/abs/2510.22362)\n- [arXiv HTML Full Paper](https://arxiv.org/html/2510.22362)\n- [arXiv PDF](https://arxiv.org/pdf/2510.22362)\n- [OpenReview PDF](https://openreview.net/pdf/89878ca66572c0425255f7be53b2879e6d2e7e7b.pdf)"
      }
    ],
    "totalDurationMs": 103272,
    "totalTokens": 17426,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 660,
      "cache_read_input_tokens": 14995,
      "output_tokens": 1770,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 660
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1770,
          "cache_read_input_tokens": 14995,
          "cache_creation_input_tokens": 660,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 660,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 7
    }
  },
  "sourceToolAssistantUUID": "ef8ab33b-b1e4-4183-9a52-4bae1cd96666",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"The Probe-Intervention Gap: Diagnosing Chain-of-Thought Faithfulness v…",
  "leafUuid": "1d0e1494-76d0-41b2-908f-fc1a824fabaa",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise gap diagnostic discriminability and phenomenon distinguishability",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f"
}
```

---

### Tool result

_source line 21 · 2026-05-19T12:04:09.153Z_

<details><summary>↩ Tool result · `toolu_01Bj9cynxHTHba47N4VGrEv6`</summary>

```text
Now I have comprehensive information. Let me compile the findings into a thorough report.

---

Here is a structured research report with concrete methods you can use for probe calibration in your chain-of-thought faithfulness diagnosis proposal.

---

## 1. Control Tasks and Selectivity Scores (Hewitt & Liang, EMNLP 2019)

**Paper:** "Designing and Interpreting Probes with Control Tasks" -- [ACL Anthology](https://aclanthology.org/D19-1275/) | [Stanford PDF](https://nlp.stanford.edu/pubs/hewitt2019control.pdf) | [John Hewitt's blog](https://www.cs.columbia.edu/~johnhew/interpreting-probes.html)

**Core method:**
- Define a **control task** by assigning each word type a random label (independently sampled). By construction, this task can only be "solved" by the probe memorizing word identities, not by detecting genuine structure in representations.
- **Selectivity** = linguistic task accuracy - control task accuracy.
- High selectivity means the probe succeeds *because of* linguistic structure in the labels, not because the probe memorizes surface features.

**Key finding for your proposal:** MLP probes achieve very low selectivity (e.g., 97.3% on POS tagging but 92.8% on the control task = 4.5 selectivity), while linear probes achieve much higher selectivity (97.2% vs 71.2% = 26.0 selectivity). This directly addresses your reviewer's concern: you should report selectivity alongside accuracy, and use linear probes rather than MLPs.

**How to apply:** For your CoT faithfulness probes, train a parallel "null probe" on shuffled labels (random assignment of faithfulness labels to hidden states). Report `selectivity = real_accuracy - shuffled_accuracy`. If selectivity is low, the probe is capturing correlative/epiphenomenal information.

---

## 2. MDL Probing (Voita & Titov, EMNLP 2020)

**Paper:** "Information-Theoretic Probing with Minimum Description Length" -- [arXiv:2003.12298](https://arxiv.org/abs/2003.12298) | [Lena Voita's blog](https://lena-voita.github.io/posts/mdl_probes.html) | [GitHub](https://github.com/lena-voita/description-length-probing)

**Core method:**
- Replace probe accuracy with **minimum description length (MDL)** of labels given representations. This measures both quality AND the effort needed to achieve it (model size or data requirements).
- Two estimation methods: **variational coding** and **online coding**, both easily implemented on top of standard probing pipelines.

**Key finding:** Standard probe accuracy does NOT substantially favor pretrained representations over randomly initialized ones, and shows similar accuracy for genuine linguistic tasks vs. random synthetic tasks. MDL probing solves this by penalizing unnecessary complexity -- it is "more informative and stable than standard probes."

**How to apply:** Instead of reporting only probe accuracy for faithfulness detection, report MDL (codelength). If a probe on genuine faithfulness labels requires similar codelength to a probe on random labels, the information is not genuinely structured in the representations. This directly addresses the "uniformly high accuracy" concern.

---

## 3. Amnesic Probing (Elazar et al., TACL 2021)

**Paper:** "Amnesic Probing: Behavioral Explanation with Amnesic Counterfactuals" -- [arXiv:2006.00995](https://arxiv.org/abs/2006.00995) | [MIT Press](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00359/98091/Amnesic-Probing-Behavioral-Explanation-with)

**Core method:**
- Use **Iterative Nullspace Projection (INLP)** to remove a property from representations, then test whether the model's downstream performance changes.
- The key shift: from "what is encoded?" to "how is information used?" -- a counterfactual causal intervention.

**Critical finding:** "Conventional probing performance is not correlated to task importance." Properties may be detectable (high probe accuracy) yet causally irrelevant to model predictions. For example, BERT encodes POS information but removing it via INLP does not hurt masked language modeling -- the information is epiphenomenal.

**How to apply:** After training your faithfulness probes, use INLP/LEACE to erase the detected "faithfulness-relevant" directions from hidden states, then check if the model's CoT behavior actually changes. If erasing the information doesn't change outputs, the probe was detecting correlative rather than causally relevant information.

**Important caveat:** INLP introduces random modifications. Use **LEACE** or **Mean Projection** instead for cleaner erasure (see next item).

---

## 4. LEACE and Improved Amnesic Probing (Belrose et al., NeurIPS 2023; Dobrzeniecka et al., ACL 2025)

**Papers:**
- "LEACE: Perfect linear concept erasure in closed form" -- [arXiv:2306.03819](https://arxiv.org/abs/2306.03819)
- "Improving Causal Interventions in Amnesic Probing with Mean Projection or LEACE" -- [arXiv:2506.11673](https://arxiv.org/abs/2506.11673) | [ACL 2025 Findings](https://aclanthology.org/2025.findings-acl.674/)

**Core method:**
- LEACE provides a closed-form projection that **provably prevents all linear classifiers** from detecting a concept while changing representations minimally.
- The 2025 paper shows that LEACE and Mean Projection are strictly better than INLP for amnesic probing because INLP introduces random noise, while LEACE/MP perform surgical, minimal-perturbation erasure.

**How to apply:** Use LEACE as your concept erasure method when doing amnesic probing of faithfulness information. LEACE's theoretical guarantee (no linear classifier can recover the erased concept) makes it the strongest tool for testing whether detected information is causally used.

---

## 5. Latent Causal Probing (2024)

**Paper:** "Latent Causal Probing: A Formal Perspective on Probing with Causal Models of Data" -- [arXiv:2407.13765](https://arxiv.org/abs/2407.13765)

**Core method:**
- Formalizes probing using **structural causal models (SCMs)**, isolating the causal path through the language model while excluding the probe's influence.
- Distinguishes between **correlation** (information present in representations) and **causal use** (information actually employed by the model).
- Validated on synthetic tasks where the true causal structure is known.

**How to apply:** If you can design tasks where the ground-truth causal relationship between CoT faithfulness and internal representations is known (e.g., synthetic reasoning tasks), this framework lets you formally verify that your probes capture causal rather than correlative information.

---

## 6. Manifold Capacity Theory -- Chun et al. (arXiv:2602.20338)

**Paper:** "Emergent Manifold Separability during Reasoning in Large Language Models" by Polo, Chun, & Chung -- [arXiv:2602.20338](https://arxiv.org/abs/2602.20338)

**Core method:**
- Applies **Manifold Capacity Theory (MCT)** to quantify linear separability of concept manifolds *without training a probe at all*. MCT measures intrinsic geometric properties of the representation space (radius, dimensionality, alignment of concept manifolds).

**Critical finding for your proposal:** Linear probe accuracy remains high long after computation is complete, but **geometric separability (MCT) peaks transiently just before computation and compresses rapidly afterward**. They call this a "geometric pulse." This is direct evidence that probe accuracy captures information that is *merely retrievable* (epiphenomenal), not information that is *geometrically prepared for processing* (causally relevant).

The mechanism they propose -- **Dynamic Manifold Management** -- describes how models dynamically modulate representational capacity to optimize the residual stream's bandwidth during reasoning chains.

**How to apply:** This is perhaps the strongest paper for your reviewer response. MCT gives you a probe-free metric of representational readiness that dissociates from probe accuracy. You could:
1. Track MCT separability across CoT reasoning steps alongside probe accuracy.
2. Show that MCT separability has a characteristic temporal profile (the "geometric pulse") even when probe accuracy is flat/high.
3. Use the *shape* of the MCT trajectory (timing and magnitude of the pulse) as your diagnostic, rather than absolute probe accuracy values.

---

## 7. Trajectory-Shape Methods for CoT Faithfulness

**Paper:** "Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning" -- [arXiv:2602.11201](https://arxiv.org/abs/2602.11201)

**Key methods relevant to your concern about trajectory shapes vs. absolute values:**
- **Normalized Logit Difference Decay (NLDD):** Corrupts individual reasoning steps and measures confidence drops, with normalization that enables rigorous cross-model comparison regardless of output scaling differences. This addresses the problem that raw sensitivity metrics are inflated/incomparable across architectures.
- **Reasoning Horizon (k*):** They identify a consistent point at 70-85% of chain length beyond which reasoning tokens have little or negative effect on the final answer.
- Critical finding: "Models can encode correct internal representations while completely failing the task" -- accuracy alone does not reveal whether a model actually reasons through its chain.

**Paper:** "Entropy trajectory shape predicts LLM reasoning reliability" -- [arXiv:2603.18940](https://arxiv.org/pdf/2603.18940)
- Uses **entropy-trajectory monotonicity** rather than absolute values. Achieves +5.8pp at 73.7% coverage, outperforming scalar baselines.
- Shows that token log-probability scores are systematically miscalibrated (ECE rises from 0.186 to 0.312 across reasoning steps).

**How to apply:** Use NLDD-style normalization so your probe trajectories are comparable across models and robust to inflation. Focus on trajectory *shape* features (timing of peaks, monotonicity, inflection points) rather than absolute accuracy values.

---

## 8. "Probing the Probing Paradigm" (Ravichander et al., 2020)

**Paper:** "Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance?" -- [arXiv:2005.00719](https://arxiv.org/abs/2005.00719)

**Key finding directly addressing your reviewer's concern:** Models encode linguistic properties "considerably above chance-level even when distributed in the data as random noise." Pretrained word embeddings, not task training, account for much of the encoded information. This means high probe accuracy can be entirely epiphenomenal.

---

## 9. Belinkov Survey (Computational Linguistics, 2022)

**Paper:** "Probing Classifiers: Promises, Shortcomings, and Advances" -- [arXiv:2102.12452](https://arxiv.org/abs/2102.12452) | [MIT Press](https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and)

A comprehensive survey covering all the methodological limitations. Useful as a reference for motivating your calibration approach.

---

## Concrete Recommendations for Your Proposal

Here is a calibration toolkit you could propose, ordered from simplest to most rigorous:

**Tier 1 -- Baselines (minimal effort, should always do):**
1. **Shuffled-label control probes** (Hewitt & Liang 2019): Train probes on randomly assigned faithfulness labels. Report selectivity = real accuracy - control accuracy.
2. **Random-representation baseline**: Train probes on random vectors of the same dimensionality. If accuracy is still high, your probe is too expressive.

**Tier 2 -- Information-theoretic calibration (moderate effort):**
3. **MDL probing** (Voita & Titov 2020): Replace accuracy with codelength. Genuine structure requires less description length than random assignments. Implementations available on GitHub.

**Tier 3 -- Causal validation (higher effort, strongest evidence):**
4. **Amnesic probing with LEACE** (Belrose et al. 2023; Dobrzeniecka et al. 2025): Erase the detected "faithfulness" directions from hidden states using LEACE, then check if model behavior changes. If not, the information is epiphenomenal.
5. **Latent Causal Probing** (2024): For synthetic tasks where you control ground truth, use SCM-based probing to formally distinguish correlation from causation.

**Tier 4 -- Geometry-based alternatives (probe-free, addresses inflation directly):**
6. **Manifold Capacity Theory** (Polo, Chun & Chung 2026): Track geometric separability across reasoning steps without training a probe. Compare MCT trajectory shape with probe accuracy trajectory -- the divergence between them is itself diagnostic of epiphenomenal encoding.

**For trajectory analysis specifically:**
7. **NLDD normalization** (arXiv:2602.11201): Normalize probe/sensitivity metrics across models to make trajectory shapes comparable despite absolute value inflation.
8. **Trajectory shape features**: Analyze timing of peaks, monotonicity, inflection points rather than absolute accuracy values. The "geometric pulse" pattern from MCT provides a template for what genuine computational readiness looks like vs. flat/high epiphenomenal encoding.

agentId: acc4b077cc6fe4048 (use SendMessage with to: 'acc4b077cc6fe4048' to continue this agent)
&lt;usage>total_tokens: 30120
tool_uses: 26
duration_ms: 193615&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c53e8df1-ec6d-48de-80d3-e89d527c64f3",
  "isSidechain": false,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "type": "user",
  "uuid": "46df83a4-b20e-4ceb-9563-05ec3e6c2584",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm revising a research proposal about chain-of-thought faithfulness diagnosis. A key reviewer concern is that linear probes on LLM hidden states may capture correlative/epiphenomenal information rather than causally relevant information, making probe accuracy uniformly high regardless of actual faithfulness. This is the \"probe inflation\" problem.\n\nI need to research:\n1. Methods for calibrating probes to distinguish genuine vs correlative information — especially \"null probe\" or \"control probe\" baselines (e.g., training probes on shuffled labels, selectivity scores, etc.)\n2. Chun et al. (2602.20338) \"Emergent Manifold Separability during Reasoning in LLMs\" — their finding that probe accuracy ≠ computational readiness\n3. Any work on probe selectivity, amnesic probing, or causal probing that addresses the concern that high probe accuracy doesn't mean the information is being used\n4. Methods for distinguishing trajectory shapes even when absolute values are inflated\n\nPlease search for:\n- \"probe selectivity score control task\" neural network probing\n- \"amnesic probing\" OR \"causal probing\" language models 2024 2025 2026\n- \"null probe\" baseline linear probing hidden states\n- Chun et al 2602.20338 manifold separability reasoning\n\nFor key papers found, use WebFetch to read the abstracts/key findings. Report back with concrete methods I could use for probe calibration.",
    "agentId": "acc4b077cc6fe4048",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Let me compile the findings into a thorough report.\n\n---\n\nHere is a structured research report with concrete methods you can use for probe calibration in your chain-of-thought faithfulness diagnosis proposal.\n\n---\n\n## 1. Control Tasks and Selectivity Scores (Hewitt & Liang, EMNLP 2019)\n\n**Paper:** \"Designing and Interpreting Probes with Control Tasks\" -- [ACL Anthology](https://aclanthology.org/D19-1275/) | [Stanford PDF](https://nlp.stanford.edu/pubs/hewitt2019control.pdf) | [John Hewitt's blog](https://www.cs.columbia.edu/~johnhew/interpreting-probes.html)\n\n**Core method:**\n- Define a **control task** by assigning each word type a random label (independently sampled). By construction, this task can only be \"solved\" by the probe memorizing word identities, not by detecting genuine structure in representations.\n- **Selectivity** = linguistic task accuracy - control task accuracy.\n- High selectivity means the probe succeeds *because of* linguistic structure in the labels, not because the probe memorizes surface features.\n\n**Key finding for your proposal:** MLP probes achieve very low selectivity (e.g., 97.3% on POS tagging but 92.8% on the control task = 4.5 selectivity), while linear probes achieve much higher selectivity (97.2% vs 71.2% = 26.0 selectivity). This directly addresses your reviewer's concern: you should report selectivity alongside accuracy, and use linear probes rather than MLPs.\n\n**How to apply:** For your CoT faithfulness probes, train a parallel \"null probe\" on shuffled labels (random assignment of faithfulness labels to hidden states). Report `selectivity = real_accuracy - shuffled_accuracy`. If selectivity is low, the probe is capturing correlative/epiphenomenal information.\n\n---\n\n## 2. MDL Probing (Voita & Titov, EMNLP 2020)\n\n**Paper:** \"Information-Theoretic Probing with Minimum Description Length\" -- [arXiv:2003.12298](https://arxiv.org/abs/2003.12298) | [Lena Voita's blog](https://lena-voita.github.io/posts/mdl_probes.html) | [GitHub](https://github.com/lena-voita/description-length-probing)\n\n**Core method:**\n- Replace probe accuracy with **minimum description length (MDL)** of labels given representations. This measures both quality AND the effort needed to achieve it (model size or data requirements).\n- Two estimation methods: **variational coding** and **online coding**, both easily implemented on top of standard probing pipelines.\n\n**Key finding:** Standard probe accuracy does NOT substantially favor pretrained representations over randomly initialized ones, and shows similar accuracy for genuine linguistic tasks vs. random synthetic tasks. MDL probing solves this by penalizing unnecessary complexity -- it is \"more informative and stable than standard probes.\"\n\n**How to apply:** Instead of reporting only probe accuracy for faithfulness detection, report MDL (codelength). If a probe on genuine faithfulness labels requires similar codelength to a probe on random labels, the information is not genuinely structured in the representations. This directly addresses the \"uniformly high accuracy\" concern.\n\n---\n\n## 3. Amnesic Probing (Elazar et al., TACL 2021)\n\n**Paper:** \"Amnesic Probing: Behavioral Explanation with Amnesic Counterfactuals\" -- [arXiv:2006.00995](https://arxiv.org/abs/2006.00995) | [MIT Press](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00359/98091/Amnesic-Probing-Behavioral-Explanation-with)\n\n**Core method:**\n- Use **Iterative Nullspace Projection (INLP)** to remove a property from representations, then test whether the model's downstream performance changes.\n- The key shift: from \"what is encoded?\" to \"how is information used?\" -- a counterfactual causal intervention.\n\n**Critical finding:** \"Conventional probing performance is not correlated to task importance.\" Properties may be detectable (high probe accuracy) yet causally irrelevant to model predictions. For example, BERT encodes POS information but removing it via INLP does not hurt masked language modeling -- the information is epiphenomenal.\n\n**How to apply:** After training your faithfulness probes, use INLP/LEACE to erase the detected \"faithfulness-relevant\" directions from hidden states, then check if the model's CoT behavior actually changes. If erasing the information doesn't change outputs, the probe was detecting correlative rather than causally relevant information.\n\n**Important caveat:** INLP introduces random modifications. Use **LEACE** or **Mean Projection** instead for cleaner erasure (see next item).\n\n---\n\n## 4. LEACE and Improved Amnesic Probing (Belrose et al., NeurIPS 2023; Dobrzeniecka et al., ACL 2025)\n\n**Papers:**\n- \"LEACE: Perfect linear concept erasure in closed form\" -- [arXiv:2306.03819](https://arxiv.org/abs/2306.03819)\n- \"Improving Causal Interventions in Amnesic Probing with Mean Projection or LEACE\" -- [arXiv:2506.11673](https://arxiv.org/abs/2506.11673) | [ACL 2025 Findings](https://aclanthology.org/2025.findings-acl.674/)\n\n**Core method:**\n- LEACE provides a closed-form projection that **provably prevents all linear classifiers** from detecting a concept while changing representations minimally.\n- The 2025 paper shows that LEACE and Mean Projection are strictly better than INLP for amnesic probing because INLP introduces random noise, while LEACE/MP perform surgical, minimal-perturbation erasure.\n\n**How to apply:** Use LEACE as your concept erasure method when doing amnesic probing of faithfulness information. LEACE's theoretical guarantee (no linear classifier can recover the erased concept) makes it the strongest tool for testing whether detected information is causally used.\n\n---\n\n## 5. Latent Causal Probing (2024)\n\n**Paper:** \"Latent Causal Probing: A Formal Perspective on Probing with Causal Models of Data\" -- [arXiv:2407.13765](https://arxiv.org/abs/2407.13765)\n\n**Core method:**\n- Formalizes probing using **structural causal models (SCMs)**, isolating the causal path through the language model while excluding the probe's influence.\n- Distinguishes between **correlation** (information present in representations) and **causal use** (information actually employed by the model).\n- Validated on synthetic tasks where the true causal structure is known.\n\n**How to apply:** If you can design tasks where the ground-truth causal relationship between CoT faithfulness and internal representations is known (e.g., synthetic reasoning tasks), this framework lets you formally verify that your probes capture causal rather than correlative information.\n\n---\n\n## 6. Manifold Capacity Theory -- Chun et al. (arXiv:2602.20338)\n\n**Paper:** \"Emergent Manifold Separability during Reasoning in Large Language Models\" by Polo, Chun, & Chung -- [arXiv:2602.20338](https://arxiv.org/abs/2602.20338)\n\n**Core method:**\n- Applies **Manifold Capacity Theory (MCT)** to quantify linear separability of concept manifolds *without training a probe at all*. MCT measures intrinsic geometric properties of the representation space (radius, dimensionality, alignment of concept manifolds).\n\n**Critical finding for your proposal:** Linear probe accuracy remains high long after computation is complete, but **geometric separability (MCT) peaks transiently just before computation and compresses rapidly afterward**. They call this a \"geometric pulse.\" This is direct evidence that probe accuracy captures information that is *merely retrievable* (epiphenomenal), not information that is *geometrically prepared for processing* (causally relevant).\n\nThe mechanism they propose -- **Dynamic Manifold Management** -- describes how models dynamically modulate representational capacity to optimize the residual stream's bandwidth during reasoning chains.\n\n**How to apply:** This is perhaps the strongest paper for your reviewer response. MCT gives you a probe-free metric of representational readiness that dissociates from probe accuracy. You could:\n1. Track MCT separability across CoT reasoning steps alongside probe accuracy.\n2. Show that MCT separability has a characteristic temporal profile (the \"geometric pulse\") even when probe accuracy is flat/high.\n3. Use the *shape* of the MCT trajectory (timing and magnitude of the pulse) as your diagnostic, rather than absolute probe accuracy values.\n\n---\n\n## 7. Trajectory-Shape Methods for CoT Faithfulness\n\n**Paper:** \"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning\" -- [arXiv:2602.11201](https://arxiv.org/abs/2602.11201)\n\n**Key methods relevant to your concern about trajectory shapes vs. absolute values:**\n- **Normalized Logit Difference Decay (NLDD):** Corrupts individual reasoning steps and measures confidence drops, with normalization that enables rigorous cross-model comparison regardless of output scaling differences. This addresses the problem that raw sensitivity metrics are inflated/incomparable across architectures.\n- **Reasoning Horizon (k*):** They identify a consistent point at 70-85% of chain length beyond which reasoning tokens have little or negative effect on the final answer.\n- Critical finding: \"Models can encode correct internal representations while completely failing the task\" -- accuracy alone does not reveal whether a model actually reasons through its chain.\n\n**Paper:** \"Entropy trajectory shape predicts LLM reasoning reliability\" -- [arXiv:2603.18940](https://arxiv.org/pdf/2603.18940)\n- Uses **entropy-trajectory monotonicity** rather than absolute values. Achieves +5.8pp at 73.7% coverage, outperforming scalar baselines.\n- Shows that token log-probability scores are systematically miscalibrated (ECE rises from 0.186 to 0.312 across reasoning steps).\n\n**How to apply:** Use NLDD-style normalization so your probe trajectories are comparable across models and robust to inflation. Focus on trajectory *shape* features (timing of peaks, monotonicity, inflection points) rather than absolute accuracy values.\n\n---\n\n## 8. \"Probing the Probing Paradigm\" (Ravichander et al., 2020)\n\n**Paper:** \"Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance?\" -- [arXiv:2005.00719](https://arxiv.org/abs/2005.00719)\n\n**Key finding directly addressing your reviewer's concern:** Models encode linguistic properties \"considerably above chance-level even when distributed in the data as random noise.\" Pretrained word embeddings, not task training, account for much of the encoded information. This means high probe accuracy can be entirely epiphenomenal.\n\n---\n\n## 9. Belinkov Survey (Computational Linguistics, 2022)\n\n**Paper:** \"Probing Classifiers: Promises, Shortcomings, and Advances\" -- [arXiv:2102.12452](https://arxiv.org/abs/2102.12452) | [MIT Press](https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and)\n\nA comprehensive survey covering all the methodological limitations. Useful as a reference for motivating your calibration approach.\n\n---\n\n## Concrete Recommendations for Your Proposal\n\nHere is a calibration toolkit you could propose, ordered from simplest to most rigorous:\n\n**Tier 1 -- Baselines (minimal effort, should always do):**\n1. **Shuffled-label control probes** (Hewitt & Liang 2019): Train probes on randomly assigned faithfulness labels. Report selectivity = real accuracy - control accuracy.\n2. **Random-representation baseline**: Train probes on random vectors of the same dimensionality. If accuracy is still high, your probe is too expressive.\n\n**Tier 2 -- Information-theoretic calibration (moderate effort):**\n3. **MDL probing** (Voita & Titov 2020): Replace accuracy with codelength. Genuine structure requires less description length than random assignments. Implementations available on GitHub.\n\n**Tier 3 -- Causal validation (higher effort, strongest evidence):**\n4. **Amnesic probing with LEACE** (Belrose et al. 2023; Dobrzeniecka et al. 2025): Erase the detected \"faithfulness\" directions from hidden states using LEACE, then check if model behavior changes. If not, the information is epiphenomenal.\n5. **Latent Causal Probing** (2024): For synthetic tasks where you control ground truth, use SCM-based probing to formally distinguish correlation from causation.\n\n**Tier 4 -- Geometry-based alternatives (probe-free, addresses inflation directly):**\n6. **Manifold Capacity Theory** (Polo, Chun & Chung 2026): Track geometric separability across reasoning steps without training a probe. Compare MCT trajectory shape with probe accuracy trajectory -- the divergence between them is itself diagnostic of epiphenomenal encoding.\n\n**For trajectory analysis specifically:**\n7. **NLDD normalization** (arXiv:2602.11201): Normalize probe/sensitivity metrics across models to make trajectory shapes comparable despite absolute value inflation.\n8. **Trajectory shape features**: Analyze timing of peaks, monotonicity, inflection points rather than absolute accuracy values. The \"geometric pulse\" pattern from MCT provides a template for what genuine computational readiness looks like vs. flat/high epiphenomenal encoding."
      }
    ],
    "totalDurationMs": 193615,
    "totalTokens": 30120,
    "totalToolUseCount": 26,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 25632,
      "output_tokens": 3358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1129
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3358,
          "cache_read_input_tokens": 25632,
          "cache_creation_input_tokens": 1129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1129,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 26
    }
  },
  "sourceToolAssistantUUID": "c53e8df1-ec6d-48de-80d3-e89d527c64f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T12:05:55.268Z_

<details><summary>↩ Tool result · `toolu_01DgajeiwtTuhGLjGDGqPrF6`</summary>

```text
Now I have a comprehensive evidence base. Let me compile the findings into a thorough research report.

---

Here is a detailed synthesis of the evidence, organized around your three questions.

---

## 1. Can temporal trajectory SHAPES distinguish phenomena even when absolute values are inflated?

**Yes -- there are strong precedents in both neuroscience and ML interpretability.**

**ML Interpretability: The shape-over-magnitude dissociation.** The most direct precedent is [Entropy trajectory shape predicts LLM reasoning reliability](https://arxiv.org/pdf/2603.18940) (2026), which explicitly demonstrates that "it is *whether* entropy decreases at every step, not *how much* it drops, that predicts correctness -- a shape-over-magnitude dissociation." This means even if absolute entropy values are artificially elevated or scaled, the monotonicity/curvature of the trajectory remains diagnostic. This is precisely the argument you need: if P(t) is uniformly inflated by correlative information, the *shape* of G(t) = P(t) - C(t) can still distinguish phenomena.

**Recurrence Quantification Analysis (RQA) of reasoning dynamics.** [Is my model "mind blurting"?](https://arxiv.org/html/2602.06266) (Feb 2026) treats token generation as a dynamical system and applies RQA to hidden-state trajectories. Key finding: temporal RQA (capturing shape features like slope of determinism, acceleration of laminarity, variability of semantic repetition) achieves 36.94% complexity classification accuracy vs. 28.97% for response length and only 16.81% for global (amplitude-averaging) RQA. The predictive signal resides in "temporal evolution, not aggregate statistics." The top features are `det_std` (variability of semantic repetition) and `lam_slope` (acceleration of stalling) -- both shape descriptors.

**Trajectory geometry in representation space.** [LLM Reasoning as Trajectories](https://arxiv.org/html/2604.05655v1) (Microsoft, April 2026) shows that correct and incorrect reasoning paths follow similar trajectories at early steps but diverge geometrically at late steps. The divergence is measured by Euclidean distance differences (-4.26 at second-to-last step, -13.39 at final transition) and cosine distance shifts. This late-step trajectory divergence achieves 0.852 AUC for mid-reasoning correctness prediction, compared to only 0.649 for step-count baselines. The shape of the trajectory path, not the absolute activation magnitudes, carries the information.

**Neuroscience precedent.** [EEG state-trajectory instability and speed](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0235744) demonstrates that trajectory curvature (approximately the 2nd temporal derivative) and speed (approximately the 1st temporal derivative) distinguish cognitive states and brain regions *even though amplitudes differ across conditions*. The global coordination rule -- all regions converge on a common timescale of ~25ms for trajectory instability -- means shape features are robust to amplitude variation. Similarly, the Neurospectrum framework uses path signatures and persistent homology to extract "trajectory curvature as a distinguishable signature of post-task reconfiguration" independently of signal amplitude.

**Functional Data Analysis (FDA).** The mathematical framework for this exists in [Shape-based FDA](https://link.springer.com/article/10.1007/s11749-023-00876-9) (TEST, 2023), which formally separates amplitude variation from phase variation. Two functions with identical average values but different peak timing, number of inflection points, or rates of change are considered to have different "shapes." This provides the statistical framework for arguing that G(t) shapes are distinguishable even under uniform P(t) inflation.

---

## 2. Work on "dual estimator" / "dual signal" diagnostic frameworks

**The probe-vs-intervention gap is now a recognized methodological concern, and divergence patterns between the two signals have been studied.**

**Divergent representations from causal interventions.** [Addressing divergent representations from causal interventions on neural networks](https://arxiv.org/html/2511.04638v3) (2025) directly addresses the gap between correlational probes and causal interventions. They identify two classes of divergence:
- **Harmless divergences**: in the behavioral null-space (probe detects information that isn't causally used)
- **Pernicious divergences**: activating hidden pathways never active in natural processing

The critical finding is that "the same intervention that was benign in one context produces a behavioral flip in another purely due to latent divergence priming a new pathway." This means the *pattern* of probe-causal divergence is context-dependent and informative, not uniformly noisy. They propose the **Counterfactual Latent (CL) loss** to reduce divergence while preserving accuracy, achieving EMD of 0.007 vs 0.032 for behavioral-only loss.

**Task Difficulty Shapes CoT Faithfulness.** [Task Difficulty Shapes Chain-of-Thought Faithfulness](https://openreview.net/pdf/f2beacfb65623c951a3c9017791b7501159a3250.pdf) (2025) provides a natural "dual signal" result: hidden-state probes can detect where an example falls on the decorative-to-load-bearing gradient, but single-direction activation steering cannot shift it. This means P(t) (probe decodability) and C(t) (causal steerability) *systematically diverge* in a way that correlates with task difficulty -- easy tasks show high P(t) but low C(t) (decorative CoT), while hard tasks show P(t) and C(t) converging (load-bearing CoT).

**Thought Anchors: counterfactual vs. attention-based measurement.** [Thought Anchors](https://arxiv.org/html/2506.19143) (2025) provides three complementary attribution methods measuring causal importance of reasoning steps: (1) black-box counterfactual resampling, (2) white-box attention patterns ("receiver heads"), (3) causal attention suppression. The three methods substantially converge, but their *divergence patterns across task types* are informative: mathematical reasoning shows strong close-range causal links (r=0.44, p<0.001 between accuracy and close-range effects), while non-mathematical domains show weaker close-range but stronger distant connections. The temporal distribution of causal importance is task-type-specific.

---

## 3. Empirical evidence that the five phenomena have different temporal profiles

This is where the evidence is most concrete. Each phenomenon produces a **qualitatively distinct P(t) and C(t) trajectory**:

### Pre-CoT Encoding
**Temporal signature: P(t) is high from t=0, C(t) is low throughout.**
- [Decoding Answers Before Chain-of-Thought](https://arxiv.org/html/2603.01437) (Cox et al., March 2026): Probes at the last token *before* CoT begins achieve >0.9 AUC on most tasks (e.g., Anachronisms: 0.988-1.000; Sports Understanding: 0.808-0.961). Causal steering flips answers in >50% of cases at the pre-CoT position, confirming the information is causally present *before any reasoning*.
- [Temporal Predictors of Outcome](https://arxiv.org/html/2511.14773) (Nov 2025): Hidden states at t=4 tokens already encode correctness at AUC 0.84, and performance "remains high -- around 0.8 -- well into the 100 token mark."
- **Shape**: P(t) starts high and stays flat (or rises marginally). C(t) for CoT tokens is low since the answer is already determined. G(t) = P(t) - C(t) starts with a large gap that remains roughly constant.

### Reasoning Theater
**Temporal signature: P(t) locks in early, C(t) drops to near-zero after lock-in.**
- [Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought](https://arxiv.org/html/2603.05488v1) (Goodfire, March 2026): On MMLU, probes reach >90% accuracy from the very beginning of reasoning while monitors (measuring overt CoT contribution) remain near chance (25%). Performativity rates reach 0.417-0.505 on MMLU. On harder GPQA-Diamond, performativity drops to 0.010-0.012 and all curves track together.
- Early exit at 95% probe confidence retains 97% of original performance while saving 80% of tokens.
- **Shape**: P(t) plateaus immediately. C(t) may briefly rise then flatlines. G(t) opens early and widens as the model generates "performative" reasoning that has no causal effect. Crucially, this differs from pre-CoT encoding because Reasoning Theater shows P(t) locking in at the *start of CoT*, not before it, and because there *is* overt reasoning text being generated (just causally inert).

### Reasoning Horizon / Myopic Planning
**Temporal signature: P(t) flat until late spike, C(t) concentrated at sparse "pivot" positions.**
- [No Global Plan in Chain-of-Thought](https://arxiv.org/pdf/2602.02103) (Feb 2026): Final-answer prediction accuracy stays near random (50%) through most of the reasoning chain, then spikes to 97-99% accuracy at the very last step. Next-token prediction decays rapidly beyond 2 steps. The "Wooden Barrel principle" identifies critical pivot positions concentrated near completion.
- Top-5 pivot positions achieve 9% absolute improvement in uncertainty estimation vs. trajectory-wide aggregates.
- **Shape**: P(t) is low/flat for most of the trajectory, then shows a sharp late spike. C(t) is concentrated at sparse "reasoning pivots." G(t) is near zero through most of the chain (neither signal shows much) then the gap pattern depends on whether pivots are causally essential or just predictive.

### Myopic Planning (distinct from Reasoning Horizon)
**Temporal signature: Both P(t) and C(t) show short-range structure only.**
- The myopic planning finding from the same Tele-Lens paper: "Top-5 accuracy exceeding 50% for the next two steps" but declining rapidly beyond that. Hidden states encode local transitions but not global plans.
- Reasoning length predictions show "unstable and often low correlations" with actual lengths.
- **Shape**: P(t) shows a rolling, step-by-step incremental pattern. C(t) tracks it closely at short range. G(t) is small because information that's decodable is also being locally used -- but neither signal has long-range structure. This contrasts sharply with Reasoning Theater (where P(t) is high but C(t) is zero) and pre-CoT encoding (where P(t) starts high before reasoning).

### Thinking-Answer Gap
**Temporal signature: P(t) from thinking tokens diverges from P(t) in answer tokens late in the sequence.**
- [Why Models Know But Don't Say](https://arxiv.org/html/2603.26410v1) (March 2026): 87.5% of thinking tokens acknowledged misleading hints while only 28.6% of answer texts did -- a 59-percentage-point gap. The directional asymmetry ratio is 121:1 (thinking-only vs. surface-only divergence).
- Three suppression mechanisms: bare truncation, laundered attribution, confabulated justification.
- [When Chain-of-Thought Fails, the Solution Hides in the Hidden States](https://arxiv.org/html/2604.23351v1) (April 2026): Patch success rate drops monotonically across reasoning positions (Q1: 33.55% vs Q4: 21.99%), showing information frontloads early and degrades. Correct answers are recoverable from hidden states at 99.5-99.7% accuracy even when CoT fails (vs. 84.6-89.2% from overt CoT).
- **Shape**: P(t) remains high throughout (information is present in hidden states), but the *gap between hidden-state decodability and overt CoT fidelity* widens as the model progresses toward the answer, particularly at the thinking-to-answer boundary. C(t) for the thinking portion may be substantial, but C(t) for the answer portion shows suppression. This produces a different G(t) shape than Reasoning Theater because the thinking tokens themselves are informative -- the gap is specifically at the thinking/answer interface.

---

## Summary Table: Distinguishable G(t) Signatures

| Phenomenon | P(t) shape | C(t) shape | G(t) = P(t)-C(t) shape |
|---|---|---|---|
| **Pre-CoT encoding** | High from t=0, flat | Low throughout | Large constant gap |
| **Reasoning Theater** | Locks in early in CoT, plateaus | Brief rise then flatline | Gap opens during CoT, widens |
| **Reasoning Horizon** | Flat then late spike | Sparse pivots near end | Near-zero then complex late pattern |
| **Myopic planning** | Incremental step-by-step | Tracks P(t) locally | Small, locally varying |
| **Thinking-answer gap** | High throughout thinking | Drops at think/answer boundary | Spike at interface |

---

## Your Reviewer's Objection and the Rebuttal

The reviewer's claim that uniform P(t) inflation collapses all phenomena into one pattern is **empirically refuted** by the evidence above. The key rebuttal points:

1. **Shape-over-magnitude dissociation is empirically validated**: The entropy trajectory paper (2026) explicitly demonstrates that shape features (monotonicity, curvature) distinguish outcomes even when absolute values are scaled. This is a direct precedent.

2. **The five phenomena have qualitatively different P(t) shapes, not just different P(t) levels**: Pre-CoT encoding has a flat-from-start P(t); Reasoning Theater has a lock-in-and-plateau; Reasoning Horizon has a flat-then-spike; myopic planning has step-wise increments; thinking-answer gap has high-throughout-then-interface-drop. Even if all P(t) values are uniformly shifted upward by correlative information, these *shapes* remain distinguishable.

3. **C(t) provides an independent calibration signal**: The divergent-representations literature shows that the *pattern* of probe-causal divergence is informative and context-dependent. Even if P(t) is inflated, C(t) is measured by intervention and is not subject to the same correlative inflation. The G(t) shape is robust because it captures the *difference* between a potentially inflated signal and a causally grounded one.

4. **FDA provides the formal framework**: Shape-based functional data analysis provides rigorous statistical tools for comparing curve shapes after separating amplitude from phase variation. You can formally test whether G(t) trajectories from different phenomena have different shapes using elastic registration and shape distance metrics.

Sources:
- [Is my model "mind blurting"? - RQA of reasoning dynamics](https://arxiv.org/html/2602.06266)
- [Dynamics Within Latent Chain-of-Thought](https://arxiv.org/pdf/2602.08783)
- [Task Difficulty Shapes Chain-of-Thought Faithfulness](https://openreview.net/pdf/f2beacfb65623c951a3c9017791b7501159a3250.pdf)
- [Temporal Predictors of Outcome in Reasoning Language Models](https://arxiv.org/html/2511.14773)
- [When Chain-of-Thought Fails, the Solution Hides in the Hidden States](https://arxiv.org/html/2604.23351v1)
- [Analysing Chain of Thought Dynamics: Active Guidance or Post-hoc Rationalisation](https://arxiv.org/pdf/2508.19827)
- [Decoding Answers Before Chain-of-Thought: Pre-CoT Probes and Activation Steering](https://arxiv.org/html/2603.01437)
- [Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought](https://arxiv.org/html/2603.05488v1)
- [Reasoning Theater - Goodfire Research](https://www.goodfire.ai/research/reasoning-theater)
- [Why Models Know But Don't Say: Thinking-Answer Faithfulness Divergence](https://arxiv.org/html/2603.26410v1)
- [No Global Plan in Chain-of-Thought: Latent Planning Horizon](https://arxiv.org/pdf/2602.02103)
- [Addressing Divergent Representations from Causal Interventions](https://arxiv.org/html/2511.04638v3)
- [Entropy Trajectory Shape Predicts LLM Reasoning Reliability](https://arxiv.org/pdf/2603.18940)
- [LLM Reasoning as Trajectories: Step-Specific Representation Geometry](https://arxiv.org/html/2604.05655v1)
- [Thought Anchors: Which LLM Reasoning Steps Matter?](https://arxiv.org/html/2506.19143)
- [EEG State-Trajectory Instability and Speed](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0235744)
- [Shape-Based Functional Data Analysis](https://link.springer.com/article/10.1007/s11749-023-00876-9)
- [Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps](https://arxiv.org/html/2502.14829v3)

agentId: a32375811bdbb4ffe (use SendMessage with to: 'a32375811bdbb4ffe' to continue this agent)
&lt;usage>total_tokens: 39396
tool_uses: 33
duration_ms: 286995&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46e2da3b-d20a-4db2-bb5c-39812f0cc1fd",
  "isSidechain": false,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "type": "user",
  "uuid": "b659169d-1b4a-47f3-b37a-4dffea086892",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm working on a research proposal that claims five chain-of-thought faithfulness phenomena (pre-CoT encoding, Reasoning Horizon, Reasoning Theater, myopic planning, thinking-answer gap) produce distinguishable temporal signatures when measured by two signals: (1) a probe-based information curve P(t) measuring what's decodable from hidden states at position t, and (2) a causal intervention curve C(t) measuring causal contribution of CoT up to position t.\n\nA reviewer argues that if P(t) is inflated by correlative information, the gap G(t) = P(t) - C(t) may be uniformly high, collapsing all phenomena into one pattern.\n\nI need to research:\n1. Whether temporal trajectory SHAPES (rate of increase, curvature, onset timing) can distinguish phenomena even when absolute values are inflated — are there precedents in neuroscience or ML interpretability?\n2. Work on \"dual estimator\" or \"dual signal\" diagnostic frameworks where the divergence pattern matters more than absolute values\n3. Specific empirical evidence about temporal dynamics of these phenomena — do pre-CoT encoding and Reasoning Theater actually have different temporal profiles?\n\nSearch for:\n- \"temporal dynamics\" \"chain of thought\" faithfulness probe 2025 2026\n- \"pre-CoT encoding\" OR \"answer encoded before reasoning\" temporal profile\n- \"reasoning horizon\" temporal dynamics hidden states\n- dual estimator divergence pattern shape analysis interpretability\n\nUse WebFetch to read any key papers. Report concrete evidence about whether trajectory shapes differ across phenomena.",
    "agentId": "a32375811bdbb4ffe",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have a comprehensive evidence base. Let me compile the findings into a thorough research report.\n\n---\n\nHere is a detailed synthesis of the evidence, organized around your three questions.\n\n---\n\n## 1. Can temporal trajectory SHAPES distinguish phenomena even when absolute values are inflated?\n\n**Yes -- there are strong precedents in both neuroscience and ML interpretability.**\n\n**ML Interpretability: The shape-over-magnitude dissociation.** The most direct precedent is [Entropy trajectory shape predicts LLM reasoning reliability](https://arxiv.org/pdf/2603.18940) (2026), which explicitly demonstrates that \"it is *whether* entropy decreases at every step, not *how much* it drops, that predicts correctness -- a shape-over-magnitude dissociation.\" This means even if absolute entropy values are artificially elevated or scaled, the monotonicity/curvature of the trajectory remains diagnostic. This is precisely the argument you need: if P(t) is uniformly inflated by correlative information, the *shape* of G(t) = P(t) - C(t) can still distinguish phenomena.\n\n**Recurrence Quantification Analysis (RQA) of reasoning dynamics.** [Is my model \"mind blurting\"?](https://arxiv.org/html/2602.06266) (Feb 2026) treats token generation as a dynamical system and applies RQA to hidden-state trajectories. Key finding: temporal RQA (capturing shape features like slope of determinism, acceleration of laminarity, variability of semantic repetition) achieves 36.94% complexity classification accuracy vs. 28.97% for response length and only 16.81% for global (amplitude-averaging) RQA. The predictive signal resides in \"temporal evolution, not aggregate statistics.\" The top features are `det_std` (variability of semantic repetition) and `lam_slope` (acceleration of stalling) -- both shape descriptors.\n\n**Trajectory geometry in representation space.** [LLM Reasoning as Trajectories](https://arxiv.org/html/2604.05655v1) (Microsoft, April 2026) shows that correct and incorrect reasoning paths follow similar trajectories at early steps but diverge geometrically at late steps. The divergence is measured by Euclidean distance differences (-4.26 at second-to-last step, -13.39 at final transition) and cosine distance shifts. This late-step trajectory divergence achieves 0.852 AUC for mid-reasoning correctness prediction, compared to only 0.649 for step-count baselines. The shape of the trajectory path, not the absolute activation magnitudes, carries the information.\n\n**Neuroscience precedent.** [EEG state-trajectory instability and speed](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0235744) demonstrates that trajectory curvature (approximately the 2nd temporal derivative) and speed (approximately the 1st temporal derivative) distinguish cognitive states and brain regions *even though amplitudes differ across conditions*. The global coordination rule -- all regions converge on a common timescale of ~25ms for trajectory instability -- means shape features are robust to amplitude variation. Similarly, the Neurospectrum framework uses path signatures and persistent homology to extract \"trajectory curvature as a distinguishable signature of post-task reconfiguration\" independently of signal amplitude.\n\n**Functional Data Analysis (FDA).** The mathematical framework for this exists in [Shape-based FDA](https://link.springer.com/article/10.1007/s11749-023-00876-9) (TEST, 2023), which formally separates amplitude variation from phase variation. Two functions with identical average values but different peak timing, number of inflection points, or rates of change are considered to have different \"shapes.\" This provides the statistical framework for arguing that G(t) shapes are distinguishable even under uniform P(t) inflation.\n\n---\n\n## 2. Work on \"dual estimator\" / \"dual signal\" diagnostic frameworks\n\n**The probe-vs-intervention gap is now a recognized methodological concern, and divergence patterns between the two signals have been studied.**\n\n**Divergent representations from causal interventions.** [Addressing divergent representations from causal interventions on neural networks](https://arxiv.org/html/2511.04638v3) (2025) directly addresses the gap between correlational probes and causal interventions. They identify two classes of divergence:\n- **Harmless divergences**: in the behavioral null-space (probe detects information that isn't causally used)\n- **Pernicious divergences**: activating hidden pathways never active in natural processing\n\nThe critical finding is that \"the same intervention that was benign in one context produces a behavioral flip in another purely due to latent divergence priming a new pathway.\" This means the *pattern* of probe-causal divergence is context-dependent and informative, not uniformly noisy. They propose the **Counterfactual Latent (CL) loss** to reduce divergence while preserving accuracy, achieving EMD of 0.007 vs 0.032 for behavioral-only loss.\n\n**Task Difficulty Shapes CoT Faithfulness.** [Task Difficulty Shapes Chain-of-Thought Faithfulness](https://openreview.net/pdf/f2beacfb65623c951a3c9017791b7501159a3250.pdf) (2025) provides a natural \"dual signal\" result: hidden-state probes can detect where an example falls on the decorative-to-load-bearing gradient, but single-direction activation steering cannot shift it. This means P(t) (probe decodability) and C(t) (causal steerability) *systematically diverge* in a way that correlates with task difficulty -- easy tasks show high P(t) but low C(t) (decorative CoT), while hard tasks show P(t) and C(t) converging (load-bearing CoT).\n\n**Thought Anchors: counterfactual vs. attention-based measurement.** [Thought Anchors](https://arxiv.org/html/2506.19143) (2025) provides three complementary attribution methods measuring causal importance of reasoning steps: (1) black-box counterfactual resampling, (2) white-box attention patterns (\"receiver heads\"), (3) causal attention suppression. The three methods substantially converge, but their *divergence patterns across task types* are informative: mathematical reasoning shows strong close-range causal links (r=0.44, p<0.001 between accuracy and close-range effects), while non-mathematical domains show weaker close-range but stronger distant connections. The temporal distribution of causal importance is task-type-specific.\n\n---\n\n## 3. Empirical evidence that the five phenomena have different temporal profiles\n\nThis is where the evidence is most concrete. Each phenomenon produces a **qualitatively distinct P(t) and C(t) trajectory**:\n\n### Pre-CoT Encoding\n**Temporal signature: P(t) is high from t=0, C(t) is low throughout.**\n- [Decoding Answers Before Chain-of-Thought](https://arxiv.org/html/2603.01437) (Cox et al., March 2026): Probes at the last token *before* CoT begins achieve >0.9 AUC on most tasks (e.g., Anachronisms: 0.988-1.000; Sports Understanding: 0.808-0.961). Causal steering flips answers in >50% of cases at the pre-CoT position, confirming the information is causally present *before any reasoning*.\n- [Temporal Predictors of Outcome](https://arxiv.org/html/2511.14773) (Nov 2025): Hidden states at t=4 tokens already encode correctness at AUC 0.84, and performance \"remains high -- around 0.8 -- well into the 100 token mark.\"\n- **Shape**: P(t) starts high and stays flat (or rises marginally). C(t) for CoT tokens is low since the answer is already determined. G(t) = P(t) - C(t) starts with a large gap that remains roughly constant.\n\n### Reasoning Theater\n**Temporal signature: P(t) locks in early, C(t) drops to near-zero after lock-in.**\n- [Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought](https://arxiv.org/html/2603.05488v1) (Goodfire, March 2026): On MMLU, probes reach >90% accuracy from the very beginning of reasoning while monitors (measuring overt CoT contribution) remain near chance (25%). Performativity rates reach 0.417-0.505 on MMLU. On harder GPQA-Diamond, performativity drops to 0.010-0.012 and all curves track together.\n- Early exit at 95% probe confidence retains 97% of original performance while saving 80% of tokens.\n- **Shape**: P(t) plateaus immediately. C(t) may briefly rise then flatlines. G(t) opens early and widens as the model generates \"performative\" reasoning that has no causal effect. Crucially, this differs from pre-CoT encoding because Reasoning Theater shows P(t) locking in at the *start of CoT*, not before it, and because there *is* overt reasoning text being generated (just causally inert).\n\n### Reasoning Horizon / Myopic Planning\n**Temporal signature: P(t) flat until late spike, C(t) concentrated at sparse \"pivot\" positions.**\n- [No Global Plan in Chain-of-Thought](https://arxiv.org/pdf/2602.02103) (Feb 2026): Final-answer prediction accuracy stays near random (50%) through most of the reasoning chain, then spikes to 97-99% accuracy at the very last step. Next-token prediction decays rapidly beyond 2 steps. The \"Wooden Barrel principle\" identifies critical pivot positions concentrated near completion.\n- Top-5 pivot positions achieve 9% absolute improvement in uncertainty estimation vs. trajectory-wide aggregates.\n- **Shape**: P(t) is low/flat for most of the trajectory, then shows a sharp late spike. C(t) is concentrated at sparse \"reasoning pivots.\" G(t) is near zero through most of the chain (neither signal shows much) then the gap pattern depends on whether pivots are causally essential or just predictive.\n\n### Myopic Planning (distinct from Reasoning Horizon)\n**Temporal signature: Both P(t) and C(t) show short-range structure only.**\n- The myopic planning finding from the same Tele-Lens paper: \"Top-5 accuracy exceeding 50% for the next two steps\" but declining rapidly beyond that. Hidden states encode local transitions but not global plans.\n- Reasoning length predictions show \"unstable and often low correlations\" with actual lengths.\n- **Shape**: P(t) shows a rolling, step-by-step incremental pattern. C(t) tracks it closely at short range. G(t) is small because information that's decodable is also being locally used -- but neither signal has long-range structure. This contrasts sharply with Reasoning Theater (where P(t) is high but C(t) is zero) and pre-CoT encoding (where P(t) starts high before reasoning).\n\n### Thinking-Answer Gap\n**Temporal signature: P(t) from thinking tokens diverges from P(t) in answer tokens late in the sequence.**\n- [Why Models Know But Don't Say](https://arxiv.org/html/2603.26410v1) (March 2026): 87.5% of thinking tokens acknowledged misleading hints while only 28.6% of answer texts did -- a 59-percentage-point gap. The directional asymmetry ratio is 121:1 (thinking-only vs. surface-only divergence).\n- Three suppression mechanisms: bare truncation, laundered attribution, confabulated justification.\n- [When Chain-of-Thought Fails, the Solution Hides in the Hidden States](https://arxiv.org/html/2604.23351v1) (April 2026): Patch success rate drops monotonically across reasoning positions (Q1: 33.55% vs Q4: 21.99%), showing information frontloads early and degrades. Correct answers are recoverable from hidden states at 99.5-99.7% accuracy even when CoT fails (vs. 84.6-89.2% from overt CoT).\n- **Shape**: P(t) remains high throughout (information is present in hidden states), but the *gap between hidden-state decodability and overt CoT fidelity* widens as the model progresses toward the answer, particularly at the thinking-to-answer boundary. C(t) for the thinking portion may be substantial, but C(t) for the answer portion shows suppression. This produces a different G(t) shape than Reasoning Theater because the thinking tokens themselves are informative -- the gap is specifically at the thinking/answer interface.\n\n---\n\n## Summary Table: Distinguishable G(t) Signatures\n\n| Phenomenon | P(t) shape | C(t) shape | G(t) = P(t)-C(t) shape |\n|---|---|---|---|\n| **Pre-CoT encoding** | High from t=0, flat | Low throughout | Large constant gap |\n| **Reasoning Theater** | Locks in early in CoT, plateaus | Brief rise then flatline | Gap opens during CoT, widens |\n| **Reasoning Horizon** | Flat then late spike | Sparse pivots near end | Near-zero then complex late pattern |\n| **Myopic planning** | Incremental step-by-step | Tracks P(t) locally | Small, locally varying |\n| **Thinking-answer gap** | High throughout thinking | Drops at think/answer boundary | Spike at interface |\n\n---\n\n## Your Reviewer's Objection and the Rebuttal\n\nThe reviewer's claim that uniform P(t) inflation collapses all phenomena into one pattern is **empirically refuted** by the evidence above. The key rebuttal points:\n\n1. **Shape-over-magnitude dissociation is empirically validated**: The entropy trajectory paper (2026) explicitly demonstrates that shape features (monotonicity, curvature) distinguish outcomes even when absolute values are scaled. This is a direct precedent.\n\n2. **The five phenomena have qualitatively different P(t) shapes, not just different P(t) levels**: Pre-CoT encoding has a flat-from-start P(t); Reasoning Theater has a lock-in-and-plateau; Reasoning Horizon has a flat-then-spike; myopic planning has step-wise increments; thinking-answer gap has high-throughout-then-interface-drop. Even if all P(t) values are uniformly shifted upward by correlative information, these *shapes* remain distinguishable.\n\n3. **C(t) provides an independent calibration signal**: The divergent-representations literature shows that the *pattern* of probe-causal divergence is informative and context-dependent. Even if P(t) is inflated, C(t) is measured by intervention and is not subject to the same correlative inflation. The G(t) shape is robust because it captures the *difference* between a potentially inflated signal and a causally grounded one.\n\n4. **FDA provides the formal framework**: Shape-based functional data analysis provides rigorous statistical tools for comparing curve shapes after separating amplitude from phase variation. You can formally test whether G(t) trajectories from different phenomena have different shapes using elastic registration and shape distance metrics.\n\nSources:\n- [Is my model \"mind blurting\"? - RQA of reasoning dynamics](https://arxiv.org/html/2602.06266)\n- [Dynamics Within Latent Chain-of-Thought](https://arxiv.org/pdf/2602.08783)\n- [Task Difficulty Shapes Chain-of-Thought Faithfulness](https://openreview.net/pdf/f2beacfb65623c951a3c9017791b7501159a3250.pdf)\n- [Temporal Predictors of Outcome in Reasoning Language Models](https://arxiv.org/html/2511.14773)\n- [When Chain-of-Thought Fails, the Solution Hides in the Hidden States](https://arxiv.org/html/2604.23351v1)\n- [Analysing Chain of Thought Dynamics: Active Guidance or Post-hoc Rationalisation](https://arxiv.org/pdf/2508.19827)\n- [Decoding Answers Before Chain-of-Thought: Pre-CoT Probes and Activation Steering](https://arxiv.org/html/2603.01437)\n- [Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought](https://arxiv.org/html/2603.05488v1)\n- [Reasoning Theater - Goodfire Research](https://www.goodfire.ai/research/reasoning-theater)\n- [Why Models Know But Don't Say: Thinking-Answer Faithfulness Divergence](https://arxiv.org/html/2603.26410v1)\n- [No Global Plan in Chain-of-Thought: Latent Planning Horizon](https://arxiv.org/pdf/2602.02103)\n- [Addressing Divergent Representations from Causal Interventions](https://arxiv.org/html/2511.04638v3)\n- [Entropy Trajectory Shape Predicts LLM Reasoning Reliability](https://arxiv.org/pdf/2603.18940)\n- [LLM Reasoning as Trajectories: Step-Specific Representation Geometry](https://arxiv.org/html/2604.05655v1)\n- [Thought Anchors: Which LLM Reasoning Steps Matter?](https://arxiv.org/html/2506.19143)\n- [EEG State-Trajectory Instability and Speed](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0235744)\n- [Shape-Based Functional Data Analysis](https://link.springer.com/article/10.1007/s11749-023-00876-9)\n- [Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps](https://arxiv.org/html/2502.14829v3)"
      }
    ],
    "totalDurationMs": 286995,
    "totalTokens": 39396,
    "totalToolUseCount": 33,
    "usage": {
      "input_tokens": 476,
      "cache_creation_input_tokens": 1825,
      "cache_read_input_tokens": 32773,
      "output_tokens": 4322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1825
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 476,
          "output_tokens": 4322,
          "cache_read_input_tokens": 32773,
          "cache_creation_input_tokens": 1825,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1825,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 33
    }
  },
  "sourceToolAssistantUUID": "46e2da3b-d20a-4db2-bb5c-39812f0cc1fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"The Probe-Intervention Gap: Diagnosing Chain-of-Thought Faithfulness v…",
  "leafUuid": "b659169d-1b4a-47f3-b37a-4dffea086892",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise gap diagnostic discriminability and phenomenon distinguishability",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f"
}
```

---

### Tool result

_source line 25 · 2026-05-19T12:06:56.427Z_

<details><summary>↩ Tool result · `toolu_01EsJ4GfnRxEAZB9Wsaewo5o`</summary>

```text
I now have comprehensive coverage of the literature. Here is my synthesis.

---

## Literature Review: Probing Reasoning Models for Chain-of-Thought Faithfulness

### 1. What Happens When You Probe Reasoning Models Specifically?

**The Cox et al. (2603.01437) finding is real but nuanced.** Cox et al. tested instruction-tuned models (Gemma 2 2B/9B, Qwen 2.5 1.5B/3B/7B) and one reasoning model (GPT-OSS 20B, tested only in Appendix F). For instruction-tuned models, linear probes on pre-CoT residual stream activations achieved >0.9 AUC on most tasks, and activation steering flipped answers in >50% of cases. For the reasoning model, probe AUC was "considerably lower on all datasets except Anachronisms" and critically, **"the answer flip rate is negligible against the orthogonal baseline."** The authors theorize that "most of the load-bearing reasoning ability for [reasoning models] occurs in their chain-of-thought."

**However, several 2025-2026 papers directly probe reasoning model internals with more positive results:**

- **"Reasoning Models Know When They're Right" (2504.05419)** probed DeepSeek-R1-Distill variants (Llama-8B, Llama-70B, Qwen-1.5B/7B/32B) and QwQ-32B for **answer correctness** (not answer content). They found ROC-AUC >0.7 across datasets, with R1-Distill-Qwen-32B achieving >0.9 on AIME. Correctness information was linearly encoded. However, this was purely correlative probing -- no causal interventions were performed. The key finding: models "encode a notion of correctness yet fail to exploit it," continuing to generate unnecessary reasoning tokens.

- **"Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal" (2605.09502)** is perhaps the most directly relevant paper. They tested 9 models including **DeepSeek-R1-7B** and found hidden-state probes achieve 0.95 AUROC for predicting trace correctness (DeepSeek-R1-7B specifically: 0.852 AUROC). But four causal interventions all failed: activation steering gained only +4% max, best-of-N underperformed majority voting, self-correction degraded accuracy by -3%, and activation patching destroyed coherence (0% accuracy). Their conclusion: **the error signal is "diagnostic, not causal" -- like a thermometer that reads fever but cannot cure it.**

- **"Internal States Before Wait Modulate Reasoning Patterns" (2510.04128)** trained crosscoders on DeepSeek-R1-Distill-Llama-8B and identified features for backtracking, uncertainty expression, knowledge recall, and double-checking. Causal interventions confirmed these features promote/suppress reasoning patterns. This is more positive -- but the target was reasoning *behavior* (backtracking, verification), not answer content.

- **Goodfire AI's SAE work on the full 671B DeepSeek-R1** found the model is "qualitatively different from non-reasoning language models." They could steer R1 using SAE features, but encountered key challenges: steering must occur after initial response prefixes, and "oversteering paradoxically causes the model to revert to its original behavior."

- **"From Reasoning to Answer" (2509.23676)** used activation patching on R1-Distill-Llama-8B, R1-Qwen-7B, and R1-Qwen-1.5B, finding that perturbations to reasoning token activations could flip model outputs (normalized logit difference up to 0.5). Removing reasoning traces degraded accuracy by ~10% on MATH-500 for distilled models.

**Bottom line on Question 1:** Probes *detect* information in reasoning model hidden states (correctness, error awareness, progress), but the detected information has dramatically reduced causal potency compared to instruction-tuned models. The Cox et al. finding generalizes: answer-content steering largely fails on reasoning models.

---

### 2. Information Availability vs. Information Use -- Is a Correlative Signal Still Interesting?

The probing literature has thoroughly established this distinction:

- **Amnesic Probing (Elazar et al., 2021; TACL)** introduced the foundational framework: standard probes test what information is *present* in representations, while amnesic probing tests what information is *used* by measuring behavioral impact when that information is removed. High probe accuracy does not entail task relevance.

- **"Probing the Probing Paradigm" (Ravichander et al., 2020; 2005.00719)** showed that "even when models cannot use a linguistic property to perform the task, the property can be reliably recovered from neural representations through probing."

- **LEACE (Belrose et al., 2024) and improved amnesic probing (2506.11673)** provide better methods for information removal, but the fundamental gap persists.

- **The knowledge-action gap (2603.18353)** provides the starkest quantification: linear probes achieved 98.2% AUROC detecting hazardous clinical cases, yet model output sensitivity was only 45.1% -- a 53-point discrepancy.

**Is a correlative signal still scientifically interesting? Yes, for several reasons:**

1. **It establishes an upper bound on information availability.** Even if the model does not causally *use* answer information during CoT, knowing it is *available* tells us something about the model's internal computation. The 2605.09502 paper frames this as "diagnostic" -- genuinely informative about computational quality even without causal potency.

2. **It enables early exit and efficiency.** The 2504.05419 paper showed correctness probes on reasoning models enabled 24% token reduction without accuracy loss. The signal need not be causal to be *useful* -- it functions as a monitoring readout.

3. **It reveals concealment.** The 2605.09502 paper found a 0.20 AUROC gap between hidden-state probes (0.95) and text-surface classifiers (0.59 at first step) for error detection. Models possess error awareness they never verbalize -- this is scientifically significant for alignment research regardless of causal potency.

4. **It provides a baseline for future causal work.** Establishing that information is present is a prerequisite for investigating *why* the model fails to use it.

However, the proposal must be transparent about the distinction. A probe that detects answer content without causal potency cannot support claims about "what drives reasoning." It can support claims about "what the model represents" and "whether CoT adds information beyond pre-existing representations."

---

### 3. Alternative Probe Targets That May Be More Causally Relevant

The literature suggests several alternatives to answer-content probing:

**A. Answer Correctness / Self-Verification (most established)**
- Probed in 2504.05419 on DeepSeek-R1-Distill models with strong results (AUC >0.7-0.9)
- Probed in 2605.09502 with 0.95 AUROC but shown to be diagnostic-not-causal
- Still the most practical alternative since correctness probes enable early exit

**B. Reasoning Strategy / Behavioral Mode**
- 2510.04128 identified features for backtracking, uncertainty, knowledge recall, and double-checking in DeepSeek-R1-Distill-Llama-8B, with **causal interventions confirmed** -- this is the most promising causally potent alternative
- Goodfire's SAE work on the full R1 identified steerable reasoning features (with caveats about oversteering)
- The "I Have Covered All the Bases" paper (2503.18878) used SAEs to build taxonomies of reasoning features across R1-Distill variants and QwQ-32B

**C. Progress / Completion Estimation**
- "Real-Time Progress Prediction" (2506.23274) trained linear probes predicting reasoning progress from hidden states
- "No Global Plan in Chain-of-Thought" (2602.02103) found LLMs have "myopic" planning horizons, but hidden states at CoT onset predict total reasoning steps. They recommend probing **uncertainty** rather than planning content.

**D. Motivated Reasoning / Rationalization Detection**
- "Catching Rationalization in the Act" (2603.17199) trained probes on residual streams to detect motivated reasoning. Pre-generation probes matched or exceeded a full-CoT LLM monitor. This is a highly relevant alternative target -- probing for *process unfaithfulness* rather than answer content.

**E. True vs. Decorative Thinking Steps**
- "Can Aha Moments Be Fake?" (2510.24941) defined a True Thinking Score (TTS) measuring causal contribution of each step. On AIME with Qwen-2.5, only 2.3% of steps had TTS >= 0.7. They identified a "TrueThinking direction" enabling steering.

**F. Multi-Step Credibility (ReProbe approach)**
- 2511.06209 trained transformer-based probes on internal states to estimate step credibility during generation. These probes matched or exceeded Process Reward Models 810x larger. This is tested with DeepSeek-R1 for annotation and demonstrates that step-level confidence probes are highly practical.

**Recommendation for the proposal:** Probing for **reasoning behavioral mode** (backtracking, verification, uncertainty -- following 2510.04128) has the strongest evidence of causal potency in reasoning models specifically. Probing for **step-level correctness** (following 2504.05419) is the most practical and already demonstrated on R1-Distill. Probing for **rationalization detection** (following 2603.17199) is the most directly aligned with faithfulness research goals.

---

### 4. "Knows the Answer Early and Verifies via CoT" vs. "Knows the Answer Early and CoT is Decorative" -- How Probes Could Distinguish

The literature offers direct evidence and methodological guidance for this distinction:

**Evidence that models often know early:**
- Cox et al. (2603.01437): Linear probes decode the final answer from pre-CoT activations with >0.9 AUC on instruction-tuned models
- "Knowing Before Saying" (2505.24362): Probing classifiers predict reasoning success "even before a single token is generated"
- "Therefore I Am. I Think" (2604.01202): Pre-generation probes decode tool-calling decisions with high confidence; when steering changes the decision, "the chain-of-thought process often rationalizes the flip rather than resisting it"

**Evidence for the verification interpretation:**
- 2504.05419: Correctness probes become more accurate as reasoning progresses, and early-exit at 85% confidence maintains 88.2% accuracy -- this is consistent with CoT refining/confirming an initially uncertain representation
- 2509.23676 (activation patching on R1-Distill): Perturbing reasoning token activations flips outputs with normalized logit difference up to 0.5, suggesting reasoning tokens are causally active in distilled models
- 2602.03994 (CMI): Reasoning-tuned Phi-4-mini-reasoning showed CMI of 0.082 vs 0.0065 for base Phi-4, suggesting reasoning training *increases* genuine CoT dependence

**Evidence for the decoration interpretation:**
- 2510.24941: Only 2.3% of CoT steps have high causal contribution (TTS >= 0.7) on AIME
- 2602.03994: TruthfulQA shows CMI near zero across nearly all instances despite plausible reasoning text
- 2603.16475: Models "fail to update predictions after intervention in up to 60% of cases"

**How probes can distinguish the two hypotheses:**

1. **Temporal dynamics of probe accuracy.** If CoT is verification, probe accuracy for the *correct answer* should increase monotonically through reasoning. If CoT is decorative, probe accuracy should be high from the start and plateau early. The 2504.05419 paper found correctness signals emerge early but strengthen, suggesting partial verification. The "Reasoning Horizon" finding (Ye et al., 2026) places the boundary at 70-85% of chain length, beyond which tokens have diminishing causal influence.

2. **CoT Mediation Index (CMI) from 2602.03994.** This directly measures whether patching CoT-token hidden states degrades output more than control patches. CMI near zero = decorative. CMI significantly positive = verification. This is model- and task-specific.

3. **Steering + CoT observation (Cox et al. method).** When you steer the pre-CoT representation to a different answer and the CoT *rationalizes the new answer* rather than *correcting back to the original*, this is evidence for decoration. When CoT *resists* the steering, this is evidence for verification. Cox et al. found instruction-tuned models rationalize; the question for reasoning models is whether their CoT would resist more strongly.

4. **The "LLM Reasoning Is Latent" framework (2604.15726).** This paper formalizes three hypotheses: H1 (latent-trajectory mediation -- reasoning happens in hidden states, CoT is partial interface), H2 (surface-CoT mediation -- reasoning is in the text), H0 (generic compute). They propose a mediator protocol with necessity, sufficiency, and specificity tests. Their evidence favors H1 as the default for most tasks, but H2 recovers when CoT includes constitutive operations (tool use, symbolic execution).

5. **Probe on error awareness vs. error correction (2605.09502).** If the model knows it is wrong (hidden probe detects error) but continues generating confident wrong reasoning, this is decoration. If the model's reasoning course-corrects when error signals are strong, this is verification. The 2605.09502 finding -- diagnostic not causal -- suggests reasoning models detect errors but do not self-correct, which is more consistent with decoration.

---

### Summary of Contingency Approaches for the Proposal

If Phase 0 confirms that answer-content probes on reasoning models have no causal potency, the proposal has several well-supported pivots:

| Contingency | Literature Support | Causal Evidence |
|---|---|---|
| Probe for **correctness/self-verification** instead of answer content | 2504.05419 (strong on R1-Distill), 2605.09502 | Correlative only -- diagnostic, not causal |
| Probe for **reasoning behavioral mode** (backtracking, uncertainty, verification) | 2510.04128 (R1-Distill, causal interventions confirmed) | **Causal -- strongest option** |
| Use **SAE feature identification** instead of linear probes | Goodfire (R1 671B), 2503.18878 (R1-Distill, QwQ-32B) | Partially causal (steering works with caveats) |
| Probe for **step-level credibility** | 2511.06209 (matches 810x larger PRMs) | Applied/practical, causality indirect |
| Measure **CoT Mediation Index** to quantify bypass | 2602.03994 | Causal by construction (activation patching) |
| Probe for **rationalization detection** | 2603.17199 (pre-generation probes match full-CoT monitors) | Correlative but high practical value |
| Reframe as **diagnostic probing** -- explicitly argue that the availability/use gap is the scientific contribution | 2605.09502, 2603.18353 | Reframes the question itself |

**Key citation for the reviewer response:** The 2605.09502 paper ("Hidden Error Awareness... The Signal Is Diagnostic, Not Causal") directly addresses your reviewer's concern and provides the theoretical framework for arguing that diagnostic probe signals are scientifically valuable even without causal potency. Their thermometer analogy -- "a thermometer reads body temperature but cannot cure fever" -- is apt. The probe reveals what the model internally represents about its own reasoning quality, which is informative for understanding faithfulness even if interventions based on that signal fail.

### Sources

- [Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification](https://arxiv.org/abs/2504.05419)
- [Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering (Cox et al.)](https://arxiv.org/abs/2603.01437)
- [When Chains of Thought Don't Matter: Causal Bypass in Large Language Models](https://arxiv.org/abs/2602.03994)
- [Reasoning Beyond Chain-of-Thought: A Latent Computational Mode in Large Language Models](https://arxiv.org/abs/2601.08058)
- [Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps](https://arxiv.org/abs/2510.24941)
- [Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal](https://arxiv.org/abs/2605.09502)
- [LLM Reasoning Is Latent, Not the Chain of Thought](https://arxiv.org/abs/2604.15726)
- [No Global Plan in Chain-of-Thought: Uncover the Latent Planning Horizon of LLMs](https://arxiv.org/abs/2602.02103)
- [Internal States Before Wait Modulate Reasoning Patterns](https://arxiv.org/abs/2510.04128)
- [From Reasoning to Answer: Mechanistic Insights into Distilled DeepSeek R1 Models](https://arxiv.org/abs/2509.23676)
- [Therefore I Am. I Think](https://arxiv.org/abs/2604.01202)
- [Catching Rationalization in the Act: Detecting Motivated Reasoning via Activation Probing](https://arxiv.org/abs/2603.17199)
- [Efficient Test-Time Scaling of Multi-Step Reasoning by Probing Internal States (ReProbe)](https://arxiv.org/abs/2511.06209)
- [Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures](https://arxiv.org/abs/2603.16475)
- [Interpretability Without Actionability: Mechanistic Methods Cannot Correct LM Errors](https://arxiv.org/abs/2603.18353)
- [Improving Causal Interventions in Amnesic Probing with Mean Projection or LEACE](https://arxiv.org/abs/2506.11673)
- [Amnesic Probing: Behavioral Explanation with Amnesic Counterfactuals](https://arxiv.org/abs/2006.00995)
- [Why Models Know But Don't Say: CoT Faithfulness Divergence in Reasoning Models](https://arxiv.org/abs/2603.26410)
- [I Have Covered All the Bases: Interpreting Reasoning Features via SAEs](https://arxiv.org/abs/2503.18878)
- [Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?](https://arxiv.org/abs/2508.19827)
- [Under the Hood of a Reasoning Model (Goodfire AI)](https://www.goodfire.ai/research/under-the-hood-of-a-reasoning-model)
- [Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance?](https://arxiv.org/abs/2005.00719)
- [LYNX: Learning Dynamic Exits for Confidence-Controlled Reasoning](https://arxiv.org/abs/2512.05325)
- [Steering Large Reasoning Models towards Concise Reasoning via Flow Matching](https://arxiv.org/abs/2602.05539)

agentId: a980aca5800710932 (use SendMessage with to: 'a980aca5800710932' to continue this agent)
&lt;usage>total_tokens: 41947
tool_uses: 39
duration_ms: 338162&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ada137a4-b00a-4cc7-a19a-03df2280b1e7",
  "isSidechain": false,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "type": "user",
  "uuid": "c9242808-f3ce-48ab-9683-66f4aa9acef1",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm working on a research proposal about chain-of-thought faithfulness. A key component is training linear probes on hidden states to measure what answer information the model internally represents at each token position during chain-of-thought reasoning.\n\nThe reviewer raises a critical concern: Cox et al. (2603.01437) showed probes work for steering on instruction-tuned models (binary tasks, ≤9B params) but explicitly report \"little success steering\" reasoning models. If our Phase 0 pilot confirms that answer-content probes on reasoning models (like DeepSeek-R1-Distill) have NO causal potency, the probe signal becomes merely correlative.\n\nI need to research:\n1. What happens when you probe reasoning models specifically? Any papers testing probes on DeepSeek-R1, QwQ, or similar?\n2. The distinction between \"information availability\" and \"information use\" in probing literature — is a correlative probe signal still scientifically interesting?\n3. Alternative probe targets that might be more causally relevant than answer content (e.g., probing for reasoning strategy, intermediate subgoal, confidence)\n4. Whether there's a meaningful distinction between \"the model knows the answer early but uses CoT to verify\" vs \"the model knows the answer early and CoT is decorative\" — and how probes could distinguish these\n\nSearch for:\n- probing reasoning models DeepSeek-R1 hidden states 2025 2026\n- \"information availability\" vs \"information use\" probing language models\n- probe causal potency reasoning chain-of-thought 2026\n- alternative probe targets intermediate reasoning states\n\nUse WebFetch on key papers. Report what the literature says about probing reasoning models specifically and what contingency approaches exist.",
    "agentId": "a980aca5800710932",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive coverage of the literature. Here is my synthesis.\n\n---\n\n## Literature Review: Probing Reasoning Models for Chain-of-Thought Faithfulness\n\n### 1. What Happens When You Probe Reasoning Models Specifically?\n\n**The Cox et al. (2603.01437) finding is real but nuanced.** Cox et al. tested instruction-tuned models (Gemma 2 2B/9B, Qwen 2.5 1.5B/3B/7B) and one reasoning model (GPT-OSS 20B, tested only in Appendix F). For instruction-tuned models, linear probes on pre-CoT residual stream activations achieved >0.9 AUC on most tasks, and activation steering flipped answers in >50% of cases. For the reasoning model, probe AUC was \"considerably lower on all datasets except Anachronisms\" and critically, **\"the answer flip rate is negligible against the orthogonal baseline.\"** The authors theorize that \"most of the load-bearing reasoning ability for [reasoning models] occurs in their chain-of-thought.\"\n\n**However, several 2025-2026 papers directly probe reasoning model internals with more positive results:**\n\n- **\"Reasoning Models Know When They're Right\" (2504.05419)** probed DeepSeek-R1-Distill variants (Llama-8B, Llama-70B, Qwen-1.5B/7B/32B) and QwQ-32B for **answer correctness** (not answer content). They found ROC-AUC >0.7 across datasets, with R1-Distill-Qwen-32B achieving >0.9 on AIME. Correctness information was linearly encoded. However, this was purely correlative probing -- no causal interventions were performed. The key finding: models \"encode a notion of correctness yet fail to exploit it,\" continuing to generate unnecessary reasoning tokens.\n\n- **\"Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal\" (2605.09502)** is perhaps the most directly relevant paper. They tested 9 models including **DeepSeek-R1-7B** and found hidden-state probes achieve 0.95 AUROC for predicting trace correctness (DeepSeek-R1-7B specifically: 0.852 AUROC). But four causal interventions all failed: activation steering gained only +4% max, best-of-N underperformed majority voting, self-correction degraded accuracy by -3%, and activation patching destroyed coherence (0% accuracy). Their conclusion: **the error signal is \"diagnostic, not causal\" -- like a thermometer that reads fever but cannot cure it.**\n\n- **\"Internal States Before Wait Modulate Reasoning Patterns\" (2510.04128)** trained crosscoders on DeepSeek-R1-Distill-Llama-8B and identified features for backtracking, uncertainty expression, knowledge recall, and double-checking. Causal interventions confirmed these features promote/suppress reasoning patterns. This is more positive -- but the target was reasoning *behavior* (backtracking, verification), not answer content.\n\n- **Goodfire AI's SAE work on the full 671B DeepSeek-R1** found the model is \"qualitatively different from non-reasoning language models.\" They could steer R1 using SAE features, but encountered key challenges: steering must occur after initial response prefixes, and \"oversteering paradoxically causes the model to revert to its original behavior.\"\n\n- **\"From Reasoning to Answer\" (2509.23676)** used activation patching on R1-Distill-Llama-8B, R1-Qwen-7B, and R1-Qwen-1.5B, finding that perturbations to reasoning token activations could flip model outputs (normalized logit difference up to 0.5). Removing reasoning traces degraded accuracy by ~10% on MATH-500 for distilled models.\n\n**Bottom line on Question 1:** Probes *detect* information in reasoning model hidden states (correctness, error awareness, progress), but the detected information has dramatically reduced causal potency compared to instruction-tuned models. The Cox et al. finding generalizes: answer-content steering largely fails on reasoning models.\n\n---\n\n### 2. Information Availability vs. Information Use -- Is a Correlative Signal Still Interesting?\n\nThe probing literature has thoroughly established this distinction:\n\n- **Amnesic Probing (Elazar et al., 2021; TACL)** introduced the foundational framework: standard probes test what information is *present* in representations, while amnesic probing tests what information is *used* by measuring behavioral impact when that information is removed. High probe accuracy does not entail task relevance.\n\n- **\"Probing the Probing Paradigm\" (Ravichander et al., 2020; 2005.00719)** showed that \"even when models cannot use a linguistic property to perform the task, the property can be reliably recovered from neural representations through probing.\"\n\n- **LEACE (Belrose et al., 2024) and improved amnesic probing (2506.11673)** provide better methods for information removal, but the fundamental gap persists.\n\n- **The knowledge-action gap (2603.18353)** provides the starkest quantification: linear probes achieved 98.2% AUROC detecting hazardous clinical cases, yet model output sensitivity was only 45.1% -- a 53-point discrepancy.\n\n**Is a correlative signal still scientifically interesting? Yes, for several reasons:**\n\n1. **It establishes an upper bound on information availability.** Even if the model does not causally *use* answer information during CoT, knowing it is *available* tells us something about the model's internal computation. The 2605.09502 paper frames this as \"diagnostic\" -- genuinely informative about computational quality even without causal potency.\n\n2. **It enables early exit and efficiency.** The 2504.05419 paper showed correctness probes on reasoning models enabled 24% token reduction without accuracy loss. The signal need not be causal to be *useful* -- it functions as a monitoring readout.\n\n3. **It reveals concealment.** The 2605.09502 paper found a 0.20 AUROC gap between hidden-state probes (0.95) and text-surface classifiers (0.59 at first step) for error detection. Models possess error awareness they never verbalize -- this is scientifically significant for alignment research regardless of causal potency.\n\n4. **It provides a baseline for future causal work.** Establishing that information is present is a prerequisite for investigating *why* the model fails to use it.\n\nHowever, the proposal must be transparent about the distinction. A probe that detects answer content without causal potency cannot support claims about \"what drives reasoning.\" It can support claims about \"what the model represents\" and \"whether CoT adds information beyond pre-existing representations.\"\n\n---\n\n### 3. Alternative Probe Targets That May Be More Causally Relevant\n\nThe literature suggests several alternatives to answer-content probing:\n\n**A. Answer Correctness / Self-Verification (most established)**\n- Probed in 2504.05419 on DeepSeek-R1-Distill models with strong results (AUC >0.7-0.9)\n- Probed in 2605.09502 with 0.95 AUROC but shown to be diagnostic-not-causal\n- Still the most practical alternative since correctness probes enable early exit\n\n**B. Reasoning Strategy / Behavioral Mode**\n- 2510.04128 identified features for backtracking, uncertainty, knowledge recall, and double-checking in DeepSeek-R1-Distill-Llama-8B, with **causal interventions confirmed** -- this is the most promising causally potent alternative\n- Goodfire's SAE work on the full R1 identified steerable reasoning features (with caveats about oversteering)\n- The \"I Have Covered All the Bases\" paper (2503.18878) used SAEs to build taxonomies of reasoning features across R1-Distill variants and QwQ-32B\n\n**C. Progress / Completion Estimation**\n- \"Real-Time Progress Prediction\" (2506.23274) trained linear probes predicting reasoning progress from hidden states\n- \"No Global Plan in Chain-of-Thought\" (2602.02103) found LLMs have \"myopic\" planning horizons, but hidden states at CoT onset predict total reasoning steps. They recommend probing **uncertainty** rather than planning content.\n\n**D. Motivated Reasoning / Rationalization Detection**\n- \"Catching Rationalization in the Act\" (2603.17199) trained probes on residual streams to detect motivated reasoning. Pre-generation probes matched or exceeded a full-CoT LLM monitor. This is a highly relevant alternative target -- probing for *process unfaithfulness* rather than answer content.\n\n**E. True vs. Decorative Thinking Steps**\n- \"Can Aha Moments Be Fake?\" (2510.24941) defined a True Thinking Score (TTS) measuring causal contribution of each step. On AIME with Qwen-2.5, only 2.3% of steps had TTS >= 0.7. They identified a \"TrueThinking direction\" enabling steering.\n\n**F. Multi-Step Credibility (ReProbe approach)**\n- 2511.06209 trained transformer-based probes on internal states to estimate step credibility during generation. These probes matched or exceeded Process Reward Models 810x larger. This is tested with DeepSeek-R1 for annotation and demonstrates that step-level confidence probes are highly practical.\n\n**Recommendation for the proposal:** Probing for **reasoning behavioral mode** (backtracking, verification, uncertainty -- following 2510.04128) has the strongest evidence of causal potency in reasoning models specifically. Probing for **step-level correctness** (following 2504.05419) is the most practical and already demonstrated on R1-Distill. Probing for **rationalization detection** (following 2603.17199) is the most directly aligned with faithfulness research goals.\n\n---\n\n### 4. \"Knows the Answer Early and Verifies via CoT\" vs. \"Knows the Answer Early and CoT is Decorative\" -- How Probes Could Distinguish\n\nThe literature offers direct evidence and methodological guidance for this distinction:\n\n**Evidence that models often know early:**\n- Cox et al. (2603.01437): Linear probes decode the final answer from pre-CoT activations with >0.9 AUC on instruction-tuned models\n- \"Knowing Before Saying\" (2505.24362): Probing classifiers predict reasoning success \"even before a single token is generated\"\n- \"Therefore I Am. I Think\" (2604.01202): Pre-generation probes decode tool-calling decisions with high confidence; when steering changes the decision, \"the chain-of-thought process often rationalizes the flip rather than resisting it\"\n\n**Evidence for the verification interpretation:**\n- 2504.05419: Correctness probes become more accurate as reasoning progresses, and early-exit at 85% confidence maintains 88.2% accuracy -- this is consistent with CoT refining/confirming an initially uncertain representation\n- 2509.23676 (activation patching on R1-Distill): Perturbing reasoning token activations flips outputs with normalized logit difference up to 0.5, suggesting reasoning tokens are causally active in distilled models\n- 2602.03994 (CMI): Reasoning-tuned Phi-4-mini-reasoning showed CMI of 0.082 vs 0.0065 for base Phi-4, suggesting reasoning training *increases* genuine CoT dependence\n\n**Evidence for the decoration interpretation:**\n- 2510.24941: Only 2.3% of CoT steps have high causal contribution (TTS >= 0.7) on AIME\n- 2602.03994: TruthfulQA shows CMI near zero across nearly all instances despite plausible reasoning text\n- 2603.16475: Models \"fail to update predictions after intervention in up to 60% of cases\"\n\n**How probes can distinguish the two hypotheses:**\n\n1. **Temporal dynamics of probe accuracy.** If CoT is verification, probe accuracy for the *correct answer* should increase monotonically through reasoning. If CoT is decorative, probe accuracy should be high from the start and plateau early. The 2504.05419 paper found correctness signals emerge early but strengthen, suggesting partial verification. The \"Reasoning Horizon\" finding (Ye et al., 2026) places the boundary at 70-85% of chain length, beyond which tokens have diminishing causal influence.\n\n2. **CoT Mediation Index (CMI) from 2602.03994.** This directly measures whether patching CoT-token hidden states degrades output more than control patches. CMI near zero = decorative. CMI significantly positive = verification. This is model- and task-specific.\n\n3. **Steering + CoT observation (Cox et al. method).** When you steer the pre-CoT representation to a different answer and the CoT *rationalizes the new answer* rather than *correcting back to the original*, this is evidence for decoration. When CoT *resists* the steering, this is evidence for verification. Cox et al. found instruction-tuned models rationalize; the question for reasoning models is whether their CoT would resist more strongly.\n\n4. **The \"LLM Reasoning Is Latent\" framework (2604.15726).** This paper formalizes three hypotheses: H1 (latent-trajectory mediation -- reasoning happens in hidden states, CoT is partial interface), H2 (surface-CoT mediation -- reasoning is in the text), H0 (generic compute). They propose a mediator protocol with necessity, sufficiency, and specificity tests. Their evidence favors H1 as the default for most tasks, but H2 recovers when CoT includes constitutive operations (tool use, symbolic execution).\n\n5. **Probe on error awareness vs. error correction (2605.09502).** If the model knows it is wrong (hidden probe detects error) but continues generating confident wrong reasoning, this is decoration. If the model's reasoning course-corrects when error signals are strong, this is verification. The 2605.09502 finding -- diagnostic not causal -- suggests reasoning models detect errors but do not self-correct, which is more consistent with decoration.\n\n---\n\n### Summary of Contingency Approaches for the Proposal\n\nIf Phase 0 confirms that answer-content probes on reasoning models have no causal potency, the proposal has several well-supported pivots:\n\n| Contingency | Literature Support | Causal Evidence |\n|---|---|---|\n| Probe for **correctness/self-verification** instead of answer content | 2504.05419 (strong on R1-Distill), 2605.09502 | Correlative only -- diagnostic, not causal |\n| Probe for **reasoning behavioral mode** (backtracking, uncertainty, verification) | 2510.04128 (R1-Distill, causal interventions confirmed) | **Causal -- strongest option** |\n| Use **SAE feature identification** instead of linear probes | Goodfire (R1 671B), 2503.18878 (R1-Distill, QwQ-32B) | Partially causal (steering works with caveats) |\n| Probe for **step-level credibility** | 2511.06209 (matches 810x larger PRMs) | Applied/practical, causality indirect |\n| Measure **CoT Mediation Index** to quantify bypass | 2602.03994 | Causal by construction (activation patching) |\n| Probe for **rationalization detection** | 2603.17199 (pre-generation probes match full-CoT monitors) | Correlative but high practical value |\n| Reframe as **diagnostic probing** -- explicitly argue that the availability/use gap is the scientific contribution | 2605.09502, 2603.18353 | Reframes the question itself |\n\n**Key citation for the reviewer response:** The 2605.09502 paper (\"Hidden Error Awareness... The Signal Is Diagnostic, Not Causal\") directly addresses your reviewer's concern and provides the theoretical framework for arguing that diagnostic probe signals are scientifically valuable even without causal potency. Their thermometer analogy -- \"a thermometer reads body temperature but cannot cure fever\" -- is apt. The probe reveals what the model internally represents about its own reasoning quality, which is informative for understanding faithfulness even if interventions based on that signal fail.\n\n### Sources\n\n- [Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification](https://arxiv.org/abs/2504.05419)\n- [Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering (Cox et al.)](https://arxiv.org/abs/2603.01437)\n- [When Chains of Thought Don't Matter: Causal Bypass in Large Language Models](https://arxiv.org/abs/2602.03994)\n- [Reasoning Beyond Chain-of-Thought: A Latent Computational Mode in Large Language Models](https://arxiv.org/abs/2601.08058)\n- [Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps](https://arxiv.org/abs/2510.24941)\n- [Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal](https://arxiv.org/abs/2605.09502)\n- [LLM Reasoning Is Latent, Not the Chain of Thought](https://arxiv.org/abs/2604.15726)\n- [No Global Plan in Chain-of-Thought: Uncover the Latent Planning Horizon of LLMs](https://arxiv.org/abs/2602.02103)\n- [Internal States Before Wait Modulate Reasoning Patterns](https://arxiv.org/abs/2510.04128)\n- [From Reasoning to Answer: Mechanistic Insights into Distilled DeepSeek R1 Models](https://arxiv.org/abs/2509.23676)\n- [Therefore I Am. I Think](https://arxiv.org/abs/2604.01202)\n- [Catching Rationalization in the Act: Detecting Motivated Reasoning via Activation Probing](https://arxiv.org/abs/2603.17199)\n- [Efficient Test-Time Scaling of Multi-Step Reasoning by Probing Internal States (ReProbe)](https://arxiv.org/abs/2511.06209)\n- [Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures](https://arxiv.org/abs/2603.16475)\n- [Interpretability Without Actionability: Mechanistic Methods Cannot Correct LM Errors](https://arxiv.org/abs/2603.18353)\n- [Improving Causal Interventions in Amnesic Probing with Mean Projection or LEACE](https://arxiv.org/abs/2506.11673)\n- [Amnesic Probing: Behavioral Explanation with Amnesic Counterfactuals](https://arxiv.org/abs/2006.00995)\n- [Why Models Know But Don't Say: CoT Faithfulness Divergence in Reasoning Models](https://arxiv.org/abs/2603.26410)\n- [I Have Covered All the Bases: Interpreting Reasoning Features via SAEs](https://arxiv.org/abs/2503.18878)\n- [Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation?](https://arxiv.org/abs/2508.19827)\n- [Under the Hood of a Reasoning Model (Goodfire AI)](https://www.goodfire.ai/research/under-the-hood-of-a-reasoning-model)\n- [Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance?](https://arxiv.org/abs/2005.00719)\n- [LYNX: Learning Dynamic Exits for Confidence-Controlled Reasoning](https://arxiv.org/abs/2512.05325)\n- [Steering Large Reasoning Models towards Concise Reasoning via Flow Matching](https://arxiv.org/abs/2602.05539)"
      }
    ],
    "totalDurationMs": 338162,
    "totalTokens": 41947,
    "totalToolUseCount": 39,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 678,
      "cache_read_input_tokens": 36390,
      "output_tokens": 4878,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 678
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4878,
          "cache_read_input_tokens": 36390,
          "cache_creation_input_tokens": 678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 678,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 39
    }
  },
  "sourceToolAssistantUUID": "ada137a4-b00a-4cc7-a19a-03df2280b1e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"The Probe-Intervention Gap: Diagnosing Chain-of-Thought Faithfulness v…",
  "leafUuid": "c9242808-f3ce-48ab-9683-66f4aa9acef1",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise gap diagnostic discriminability and phenomenon distinguishability",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f"
}
```

---

### Assistant

_source line 28 · 2026-05-19T12:07:26.215Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent — I now have comprehensive research results from all four agents. Let me synthesize the key findings before writing the revision:

## Key Research Findings

### 1. Probe Inflation / Calibration Methods
- **Selectivity scores** (Hewitt & Liang 2019): Train control probes on shuffled labels, report selectivity = real accuracy - control accuracy
- **MDL probing** (Voita & Titov 2020): Replace accuracy with minimum description length
- **Amnesic probing with LEACE** (Belrose et al. 2023; Dobrzeniecka et al. 

2025): Erase detected directions, check if behavior changes
- **Manifold Capacity Theory** (Chun et al. 2602.20338): MCT separability peaks transiently (geometric pulse) while probe accuracy stays high — direct evidence that probe accuracy ≠ computational readiness
- Key insight: Use **null-probe calibration** (shuffled labels) to normalize P(t), producing P_calibrated(t) = P(t) - P_null(t), measuring excess information above chance

### 2. Li et al. (2510.22362) — Concept Walk
The three-stage framework involves filtering, then computing directions through difference-of-means approaches, with applications to understanding how concepts emerge and propagate through model layers.

Easy cases show transient activation shifts that quickly revert when perturbed, while hard cases exhibit sustained, structured changes — they tested this on Qwen 3-4B in the safety domain, which differs from our reasoning-focused approach using answer-content probes rather than concept directions.

### 3. Phenomenon Distinguishability
The trajectory shapes themselves diverge meaningfully across different phenomena even when accounting for probe inflation: pre-CoT encoding maintains high accuracy from the start with flat curves, reasoning theater locks in early and plateaus, reasoning horizon stays flat then spikes late, myopic planning shows incremental step-by-step changes, and the thinking-answer gap remains elevated throughout.

Shape differences are empirically robust to magnitude variations, as validated in the entropy trajectory literature, and formal tools like Functional Data Analysis let us compare shapes after factoring out amplitude and phase effects.

### 4. Contingency if Probes Fail
There's established evidence that probing for reasoning behavioral modes like backtracking and uncertainty has causal effects on reasoning models, and correctness/self-verification probes work on R1-Distill. The diagnostic framing using a thermometer analogy is independently supported in the literature, and we could fall back on SAE features or CMI as alternative information signals if linear probes underperform.

Now I'm restructuring the proposal to elevate gap inflation as a primary concern, starting with null-probe calibration to establish selectivity baselines.

I'll strengthen the distinguishability argument by working through predicted trajectory curves under different assumptions and grounding this in the shape-analysis literature. I'm also incorporating Li et al.'s work on task-difficulty conditioning and expanding the contingency plan with concrete alternative probe targets. The core paper will focus on Phase 0, the gap diagnostic, and difficulty-conditioned signatures, while pushing robustness checks and larger-scale validation to supplementary materials. This is a substantial shift—the probe calibration methodology and formal trajectory-shape analysis fundamentally reshape the experimental design.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9242808-f3ce-48ab-9683-66f4aa9acef1",
  "isSidechain": false,
  "requestId": "req_011CbBu7fynbMRyDitBn83oe",
  "type": "assistant",
  "uuid": "eeac02fc-91bc-4c2e-a683-56d1c75d62fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QsMTGqneNPVBJ36zXkjASn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16388,
      "cache_read_input_tokens": 27969,
      "output_tokens": 18747,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16388,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 18747,
          "cache_read_input_tokens": 27969,
          "cache_creation_input_tokens": 16388,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16388
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

_source line 29 · 2026-05-19T12:07:29.175Z_

Now I have comprehensive research findings from all four parallel investigations. Let me synthesize the key insights:

1. **Probe calibration**: Established methods exist — selectivity scores (Hewitt & Liang 2019), MDL probing (Voita & Titov 2020), LEACE erasure (Belrose et al. 2023), and critically, Chun et al.'s MCT shows geometric separability peaks transiently while probe accuracy stays flat/high — direct evidence for the inflation problem.

2. **Li et al. Concept Walk**: Three-stage framework tracking concept direction alignment per reasoning step; finds easy→transient/decorative, hard→sustained/faithful patterns on Qwen 3-4B in safety domain.

3. **Phenomenon distinguishability**: Strong evidence that trajectory *shapes* differ across phenomena even when absolute values are inflated. Shape-over-magnitude dissociation is empirically validated (entropy trajectory paper 2603.18940). Five phenomena produce qualitatively different P(t) temporal profiles.

4. **Contingency approaches**: Probing for reasoning behavioral mode (backtracking, uncertainty) has confirmed causal potency on reasoning models (2510.04128). Multiple fallback probe targets with varying causal evidence exist.

Let me now write the complete revised proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eeac02fc-91bc-4c2e-a683-56d1c75d62fa",
  "isSidechain": false,
  "requestId": "req_011CbBu7fynbMRyDitBn83oe",
  "type": "assistant",
  "uuid": "4c7a6027-c0bc-4370-9e30-30aab2a95b59",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QsMTGqneNPVBJ36zXkjASn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16388,
      "cache_read_input_tokens": 27969,
      "output_tokens": 18747,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16388,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 18747,
          "cache_read_input_tokens": 27969,
          "cache_creation_input_tokens": 16388,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16388
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

_source line 30 · 2026-05-19T12:14:39.544Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01XAp2MKe45XQjpavHKeRbzW`</summary>

```json
{
  "command": "cat << 'JSONEOF'\n{\n  \"change_type\": \"major\",\n  \"title\": \"The Probe-Intervention Gap: Diagnosing Chain-of-Thought Faithfulness via Calibrated Dual-Estimator Temporal Information Decomposition\",\n  \"project_name\": \"cot_faithfulness_decomp\",\n  \"source\": \"web_research\",\n  \"level\": \"top-tier\",\n  \"target_venues\": [\n    \"ICLR 2027 (abstract: Sep 19, full paper: Sep 24, 2026; conference: Apr/May 2027 — primary target, 4 months from now)\",\n    \"ICML 2027 (full paper: Jan 29, 2027; conference: Jul 2027 — comfortable fallback if additional experiments needed)\"\n  ],\n  \"core_problem\": \"Multiple independent findings in 2025-2026 — Reasoning Horizon, pre-CoT answer encoding, Reasoning Theater, myopic planning, thinking-answer gap — all describe facets of the same underlying problem: models' chain-of-thought reasoning is partially or entirely decorative. While the CoT faithfulness literature has catalogued these phenomena (Jin et al.'s survey; FaithCoT-Bench at ICLR 2026) and several groups have measured temporal dynamics of individual signals, no work has unified these disparate phenomena under a single information-theoretic framework that explains WHY and WHEN each occurs. Crucially, recent work reveals that the relationship between faithfulness and task difficulty is not binary: CoT transitions from decorative to load-bearing as task difficulty increases ('Task Difficulty Shapes CoT Faithfulness,' ICLR 2026 Workshop), with error propagation ranging from 22% on MMLU to 41% on BBH. This difficulty gradient — detectable via hidden-state probes but resistant to single-direction steering ('readout rather than control') — demands a diagnostic framework that can characterize faithfulness along both temporal and difficulty dimensions. A critical methodological concern, raised by the probing literature (Hewitt & Liang 2019; Ravichander et al. 2020; Chun et al. 2602.20338) and reinforced by Yuan et al. (2605.09502), is that probe accuracy on hidden states captures correlative/epiphenomenal information rather than information the model actively uses — probe accuracy ≠ computational readiness. This means any probe-based diagnostic must address the gap inflation problem: if probes detect uniformly high 'information availability' regardless of actual faithfulness, the diagnostic collapses. The closest precedents — Kudo et al.'s (EACL 2026) probing + activation patching on synthetic arithmetic, the CMI framework's layerwise causal audit on ~50 examples, Zhao et al.'s (2510.24941) True Thinking Score providing per-step causal contribution on AIME/MATH, Furuya & Tanimura's (2605.01853) training-free StALT trajectory statistic, and Li et al.'s (2510.22362, NeurIPS 2025 MechInterp Workshop) Concept Walk tracking temporal concept-direction alignment — each capture one dimension of the problem but none provides a calibrated dual-estimator framework that jointly measures internal information and causal contribution across the full CoT timeline on natural benchmarks, with explicit controls for probe inflation.\",\n  \"opportunity\": \"The field has independently produced three complementary measurement paradigms: (1) probe-based approaches revealing what the model internally represents at each CoT position (David 2511.14773: correctness decodable at t=4 tokens; Cox et al. 2603.01437: pre-CoT probes at >0.9 AUC with causal validation via steering on instruction-tuned models up to 9B; Esakkiraja et al. 2604.01202: pre-generation probes with >90% AUROC; Furuya & Tanimura 2605.01853: training-free StALT separating correct from incorrect trajectories; Li et al. 2510.22362: Concept Walk tracking concept-direction alignment per step, finding easy→decorative, hard→faithful), (2) intervention-based approaches measuring what the CoT text causally contributes (Ye et al. 2602.11201: NLDD reveals Reasoning Horizon at 70-85%; Zhao et al. 2510.24941: True Thinking Score provides per-step ATE on AIME/MATH/AMC/CommonsenseQA, finding only 2.3% of AIME steps have TTS≥0.7; Basu & Chakraborty 2603.22816: decorative/scaffolding/genuine taxonomy), and (3) diagnostic approaches characterizing CoT pathologies (Liu et al. 2602.13904: text-level metrics for rationalization/encoded/internalized reasoning via model organisms; 'Task Difficulty Shapes CoT Faithfulness' ICLR 2026 Workshop: difficulty-dependent faithfulness gradient). Two prior works have combined probing with causal interventions on the same instances: Kudo et al. (2412.01113, EACL 2026) train linear probes and perform activation patching across arithmetic CoT; the CMI framework (2602.03994) measures CoT-mediated causal influence via layerwise patching. However, neither provides: (a) full temporal-position coverage across CoT on natural benchmarks, (b) a mapping to the five named faithfulness phenomena, (c) a standalone instance-level diagnostic score, (d) systematic multi-model comparison on realistic reasoning tasks, (e) robustness validation across measurement methodologies — a critical gap highlighted by Young's (2603.20172) finding that faithfulness measurements are classifier-sensitive (inter-classifier kappa as low as 0.06), or (f) controls for probe inflation — the well-documented problem that probe accuracy captures correlative information not actively used by the model (Hewitt & Liang 2019; Voita & Titov 2020; Chun et al. 2602.20338). The opportunity is to extend the probe-intervention combination paradigm to a calibrated dual-estimator Temporal Information Curve (TIC) framework producing a 2D faithfulness signal — the gap between calibrated probe-estimated internal information and intervention-estimated causal contribution — on natural benchmarks at scale, with explicit probe inflation controls and robustness validation.\",\n  \"landscape\": \"**Probe-intervention combinations (closest prior work).** Kudo et al. (2412.01113, EACL 2026) train per-position linear probes on hidden states and validate with sliding-window activation patching on 9 models across synthetic multi-step arithmetic. They find CoT IS faithful for arithmetic but explicitly note their synthetic setting may not generalize to 'more realistic reasoning tasks in natural language.' The CMI framework (2602.03994) introduces the CoT Mediation Index via layerwise activation patching across Phi, Qwen, and DialoGPT on StrategyQA (20 examples), TruthfulQA (10), and GSM8K (20), identifying 'bypass regimes' where CMI ≈ 0. Both are complementary precursors.\\n\\n**Per-step causal contribution (direct Causal-TIC precursor).** Zhao et al. (2510.24941, Oct 2025, revised Apr 2026) introduce the True Thinking Score (TTS), measuring per-step causal contribution via text-level perturbation (numerical offsets preserving grammar) and ATE computation. On DeepSeek-R1-Distill-Qwen-7B/14B/Llama-8B across AIME, MATH, AMC, CommonsenseQA, they find only 2.3% of AIME steps have TTS≥0.7. TTS also extracts a 'TrueThinking direction' from hidden states for steering (53.6-91.2% flip rates). TTS is a direct precursor to our Causal-TIC component. Key differentiators: TTS operates at discrete step granularity (not continuous temporal), is a single-estimator metric (no calibrated probe gap), uses text-level perturbation (vs. our NLDD logit degradation), and does not map to the five faithfulness phenomena or provide an instance-level diagnostic score grounded in the probe-intervention divergence. Our framework extends TTS's causal measurement from per-step to continuous temporal coverage and pairs it with the calibrated Probe-TIC for the gap diagnostic unavailable from either estimator alone.\\n\\n**Training-free temporal hidden-state dynamics (concurrent work adjacent to Probe-TIC).** Furuya & Tanimura (2605.01853, May 2026) introduce StALT (Spatiotemporal Amplitude of Latent Transition), a training-free trajectory statistic that separates correct from incorrect reasoning trajectories by tracking hidden-state transitions across decoding steps and layers. Tested on GSM8K, MATH-500, and GPQA. StALT is conceptually adjacent to our Probe-TIC in tracking temporal hidden-state evolution. Key differentiators: StALT targets correctness separation (not faithfulness diagnosis), is training-free (vs. our trained answer-content probes targeting specific answer information), lacks a causal intervention component (no gap diagnostic), and does not map to faithfulness phenomena. Our Probe-TIC complements StALT by probing for answer content specifically and pairing it with causal interventions.\\n\\n**Temporal concept-direction tracking (concurrent work supporting task-difficulty conditioning).** Li et al. (2510.22362, NeurIPS 2025 MechInterp Workshop) introduce Concept Walk, which projects each reasoning step's activations onto concept directions (learned via difference-of-means from contrastive data) and tracks temporal evolution across CoT. On Qwen 3-4B in the safety domain, they find easy cases produce only transient activation shifts under perturbation (decorative CoT), while hard cases produce sustained, structured shifts (faithful CoT). This directly supports our task-difficulty conditioning dimension and the prediction that faithfulness signatures vary with difficulty. Key differentiators from our framework: Concept Walk uses concept directions (not answer-content probes), operates in a single domain (safety, not reasoning benchmarks), lacks a separate causal-contribution curve (perturbation is used for classification, not as a continuous C(t) estimator), tests on one small model (Qwen 3-4B), and does not derive an instance-level diagnostic score from the probe-intervention gap.\\n\\n**Latent-trajectory signals for efficiency.** Vilas et al. (2510.10494, ICLR 2026) define three latent-trajectory signals — net change, cumulative change, and aligned change — tracking hidden-state evolution across 500-token segments. On DeepSeek-R1-Distill-Qwen-14B, Phi-4-Reasoning-Plus, and Qwen3-14B across GPQA Diamond, AIME 2025, and TSP, they achieve 14-70% token savings and +2.6% accuracy gains via early selection of productive reasoning paths. Focuses on efficiency (correctness prediction for compute allocation), not faithfulness. Adjacent methodology but orthogonal goal; reinforces that temporal hidden-state signals are informative, motivating our faithfulness-specific application.\\n\\n**The diagnostic-not-causal challenge.** Yuan et al. (2605.09502, May 2026) show that probes detecting *trace correctness* achieve 0.95 AUROC but four interventions fail, concluding error representations are 'fundamentally different from editable factual knowledge representations.' Cox et al. (2603.01437) demonstrate that *answer-content* probe directions are causally potent on instruction-tuned models: steering flips >50% of answers. However — and this is a critical limitation acknowledged in this revision — Cox et al.'s validation is restricted to binary classification tasks (Anachronisms, Logical Deduction, Sports Understanding, Social Chemistry) on models up to 9B parameters, and they explicitly note that for reasoning models, they find 'some success using probes to linearly decode the final answer, but little success steering to change it.' This means the causal potency of answer-content probes on reasoning models (our target model class) is NOT yet established. The 'Task Difficulty Shapes CoT Faithfulness' workshop paper independently reaches a similar conclusion: hidden-state probes are 'readout rather than control.' We therefore introduce probe calibration methodology (Section: Approach) to address the inflation problem.\\n\\n**The probe inflation problem.** The probing literature has thoroughly documented that high probe accuracy does not entail task relevance. Hewitt & Liang (2019) show that MLP probes achieve only 4.5 selectivity on POS tagging (97.3% accuracy vs. 92.8% on shuffled-label controls). Ravichander et al. (2020) demonstrate that 'even when models cannot use a linguistic property to perform the task, the property can be reliably recovered from neural representations.' Voita & Titov (2020) show that MDL-based probing reveals that standard accuracy does not substantially favor pretrained over random representations. Most directly, Chun et al. (2602.20338) apply Manifold Capacity Theory to CoT reasoning and find that geometric separability peaks transiently as a 'geometric pulse' just before computation and compresses rapidly afterward, while probe accuracy remains high long after computation is complete. This provides direct evidence that probe accuracy overestimates information availability during reasoning. We address this via null-probe calibration and MCT geometric validation (see Approach).\\n\\n**Trajectory-shape analysis.** A separate line of work demonstrates that temporal trajectory *shapes* carry diagnostic information beyond absolute values. The entropy trajectory paper (2603.18940) shows a 'shape-over-magnitude dissociation': monotonicity of entropy decrease predicts reasoning reliability regardless of absolute entropy levels (+5.8pp at 73.7% coverage). RQA analysis of reasoning dynamics (2602.06266) shows that temporal features (determinism variability, laminarity slope) outperform aggregate statistics for complexity classification (36.94% vs. 28.97%). Microsoft's trajectory geometry work (2604.05655) shows correct vs. incorrect reasoning paths diverge geometrically at late steps (0.852 AUC from shape features vs. 0.649 from step-count baselines). This literature supports our core claim that even if P(t) is uniformly inflated, the trajectory *shape* of the gap G(t) can distinguish faithfulness phenomena.\\n\\n**CoT pathology diagnostics.** Liu et al. (2602.13904, Feb 2026) propose text-level, computationally inexpensive, task-agnostic metrics for three CoT pathologies: Necessity (rationalization), Paraphrasability (encoded reasoning), and Substantivity (internalized reasoning), validated on model organisms (Olmo-3-7B-Think trained to exhibit pathologies). Their approach is complementary to ours: purely text-level (no hidden states), uses model organisms (not natural models), categorical per-pathology metrics (not continuous temporal curves), and lacks the dual-estimator gap. Our framework provides mechanistic grounding via hidden states that their text-level metrics cannot.\\n\\n**Measurement sensitivity.** Young (2603.20172, Mar 2026) shows faithfulness measurements are classifier-sensitive: inter-classifier kappa as low as 0.06 for sycophancy hints, with up to 30.6 percentage-point divergence across three classifiers on 10,276 traces from 12 models. This raises a methodological concern directly applicable to our framework: TIF will likely show sensitivity to probe layer selection, probe architecture, NLDD perturbation method, and gap normalization. We address this by planning explicit robustness ablations across these measurement dimensions and reporting sensitivity ranges rather than single aggregate numbers.\\n\\n**Task-difficulty moderation of faithfulness.** 'Task Difficulty Shapes CoT Faithfulness' (ICLR 2026 Workshop) demonstrates that CoT transitions from decorative to load-bearing as task difficulty increases: error propagation rises from 22% on MMLU to 41% on BBH, with 7× variation within MMLU subjects. Hidden-state probes detect this gradient but single-direction steering cannot shift it ('readout rather than control'). Li et al. (2510.22362) independently corroborate this: Concept Walk shows easy cases produce transient/decorative activation patterns while hard cases produce sustained/faithful patterns. This finding has two critical implications for our framework: (1) the five faithfulness phenomena may be differentially expressed across task difficulties, enriching our unification thesis with a difficulty dimension; (2) independent confirmation that probes are diagnostic instruments, not interventional tools, supporting our thermometer framing.\\n\\n**Probe-based temporal measurement.** Qian et al. (2506.02867, NeurIPS 2025) compute per-token HSIC between hidden representations and golden answers, discovering MI peaks at thinking tokens. David (2511.14773) trains linear classifiers at prefix lengths t=4...512, showing correctness is decodable early. Zhang et al. (2504.05419) probe hidden states at intermediate answer positions for early-exit (24% savings) on DeepSeek-R1-Distill variants, achieving >0.7 AUC for correctness. Lewis-Lim et al. (2508.19827, EMNLP 2025) track answer confidence trajectories, revealing flat (rationalization) vs. increasing (genuine reasoning) patterns. Mirtaheri & Belkin (2603.17199) show pre-generation probes match full-CoT monitors for rationalization detection. Esakkiraja et al. (2604.01202) show pre-generation probes predict tool-calling at >90% AUROC.\\n\\n**Intervention-based causal measurement.** Ye et al. (2602.11201) introduce NLDD, revealing Reasoning Horizon at 70-85%. Basu & Chakraborty (2603.22816) propose genuine/scaffolding/decoration taxonomy via step ablation. Somov et al. (2603.16475) show up to 60% failure to update after intervention. FACT-E (2604.10693, ACL Findings 2026) uses controlled perturbations.\\n\\n**Probing and steering faithfulness.** Occhipinti et al. (ICLR 2026 LIT Workshop) demonstrate that faithfulness is encoded as linear directions in middle-to-late layers, with probing F1 scores of 90-100% at peak layers and steering achieving 46% monitorability recovery with <5% collateral effects. This provides complementary evidence that faithfulness has a linear geometric signature exploitable by probes.\\n\\n**Probing reasoning models specifically.** Internal States Before Wait (2510.04128) trains crosscoders on DeepSeek-R1-Distill-Llama-8B, identifying features for backtracking, uncertainty, knowledge recall, and double-checking, with causal interventions confirmed. This demonstrates that reasoning *behavioral modes* (as opposed to answer content) are causally potent probe targets in reasoning models. From Reasoning to Answer (2509.23676) uses activation patching on R1-Distill variants, finding reasoning token perturbations flip outputs with NLD up to 0.5. These findings inform our contingency plan for the Phase 0 pilot.\\n\\n**Geometric and information-theoretic approaches.** Chun et al. (2602.20338) apply Manifold Capacity Theory revealing transient geometric pulses (critical for our probe calibration methodology). Alvarez & Baheri (2605.13772, May 2026) detect step-level hallucination via hidden-state transport geometry. Ton et al. (ICML 2025, 2411.11984) define per-step information gain. Anwar et al. (2602.18297) decompose monitorability into information gap + elicitation error.\\n\\n**Faithfulness benchmarks and surveys.** FaithCoT-Bench (ICLR 2026, 2510.04040). Jin et al.'s survey (submitted to ARR for ACL 2026; no public arXiv version). Young (2603.26410): 55.4% thinking-only acknowledgment. 'Lie to Me' (2603.22582): 87.5% vs 28.6% thinking vs answer.\\n\\n**Early-exit methods.** Reasoning Theater (2603.05488: 80% savings), ESTAR (2602.10004), DTSR (2604.06787: 28.9-34.9%), NEAT (2602.02010), CoDE-Stop (2604.04930), Zhang et al. (2504.05419: 24%), FRIT (2509.13334).\\n\\n**What remains open.** No extant framework provides: (1) a full-timeline calibrated dual-estimator curve combining answer-content probes with causal interventions on natural benchmarks at scale, with explicit controls for probe inflation; (2) a systematic mapping of five phenomena to distinguishable *trajectory-shape* signatures within such a framework, demonstrated to be robust under the weaker information-availability assumption; (3) an instance-level diagnostic score derived from the calibrated probe-intervention gap with explicit robustness validation across measurement methodologies; or (4) a principled account of how the probe-intervention gap behaves differently on instruction-tuned vs. reasoning models. TTS provides per-step causal contribution (single-estimator, text-level); StALT provides temporal hidden-state correctness signals (single-estimator, no causal component); Concept Walk provides temporal concept-direction alignment (single model, single domain, no continuous causal curve); Vilas et al. provide latent-trajectory efficiency signals (no faithfulness connection); Liu et al. provide text-level pathology diagnostics (no hidden states). The calibrated dual-estimator gap — jointly measuring excess internal information (above a null-probe baseline) and causal contribution across the full timeline — remains the unique contribution.\",\n  \"inspired_by\": \"The convergence of five observations: (a) Kudo et al.'s demonstration that probe+intervention combination is feasible and informative on synthetic arithmetic, with their explicit call for natural-task extension; (b) Zhao et al.'s (2510.24941) TTS demonstrating per-step causal contribution measurement at scale on our exact target benchmarks (AIME, MATH), establishing the causal-contribution paradigm we extend to continuous temporal coverage with the dual-estimator gap; (c) the finding from both Cox et al. (2603.01437) on instruction-tuned models and the 'Task Difficulty' workshop paper that probes are diagnostic ('readout') rather than interventional ('control'), clarifying the Probe-TIC interpretation; (d) Young's (2603.20172) demonstration that faithfulness measurements are classifier-sensitive, motivating explicit robustness ablation; (e) Chun et al.'s (2602.20338) discovery that probe accuracy ≠ computational readiness — geometric separability peaks transiently while probe accuracy stays flat — which motivates our null-probe calibration methodology and the adoption of trajectory-shape features rather than absolute probe values.\",\n  \"approach\": \"Define a calibrated dual-estimator Temporal Information Curve (TIC) framework that diagnoses chain-of-thought faithfulness at each token position t via two complementary signals, with explicit controls for probe inflation:\\n\\n**(a) Calibrated Probe-TIC P*(t)**: We address the probe inflation problem — the well-documented finding that probe accuracy captures correlative/epiphenomenal information not actively used by the model (Hewitt & Liang 2019; Ravichander et al. 2020; Chun et al. 2602.20338) — via a three-layer calibration strategy:\\n\\n(i) *Null-probe normalization.* For each layer and position, train a parallel 'null probe' on shuffled answer labels (random assignment of answer identities to hidden states). Define the calibrated Probe-TIC as P*(t) = P(t) − P_null(t), measuring *excess* answer information above what is extractable from correlative features alone. This follows the selectivity methodology of Hewitt & Liang (2019), adapted to our temporal setting: selectivity is computed at each position t, producing a calibrated curve rather than a single aggregate number. High P*(t) means the model's hidden states at position t encode answer information *beyond* what is attributable to correlative features.\\n\\n(ii) *MCT geometric validation.* On a subset of 500 examples per benchmark, compute Manifold Capacity Theory (Chun et al. 2602.20338) separability alongside probe accuracy at each position. MCT measures intrinsic geometric readiness for computation (the 'geometric pulse') independent of probe training, providing a probe-free check on whether the information P*(t) detects is geometrically organized for use. If MCT separability and P*(t) show concordant temporal trajectories, the probe captures information that is at least geometrically prepared; if MCT shows the characteristic transient pulse while P*(t) remains flat/high, this diagnoses the specific type of inflation present.\\n\\n(iii) *MDL complexity check.* Following Voita & Titov (2020), compute minimum description length for probe labels at each position. If genuine answer information requires less codelength than random labels at position t, the signal is structured; if codelengths are comparable, the signal is noise-like. This provides a second probe-free validation that P*(t) captures genuine information structure.\\n\\nWe probe for *answer content* (which answer option / numerical value the model will produce) using linear probes trained on 3-5 selected layers. On instruction-tuned models, Cox et al. (2603.01437) demonstrate such probes are causally potent (steering flips >50% of answers). However, Cox et al.'s validation is limited to binary tasks on models ≤9B, and they explicitly report that reasoning models resist steering. We therefore interpret the calibrated Probe-TIC P*(t) as measuring *excess information availability* — what the model internally represents at position t above a correlative baseline — rather than assuming causal potency. This interpretation is independently supported by the 'Task Difficulty Shapes CoT Faithfulness' finding that probes are 'readout rather than control,' by Yuan et al.'s (2605.09502) demonstration that correctness probes are diagnostic-not-causal, and is consistent with Furuya & Tanimura (2605.01853) and Li et al.'s (2510.22362) finding that hidden-state temporal signals are diagnostic of reasoning quality.\\n\\n**(b) Causal-TIC C(t)**: Causal contribution of CoT_{1:t} to the answer via NLDD-style interventions (corrupting CoT segments and measuring logit degradation). This extends the single-model NLDD paradigm (Ye et al. 2602.11201) to systematic multi-model comparison with continuous temporal coverage, and provides a continuous temporal generalization of the per-step TTS metric (Zhao et al. 2510.24941). Where TTS applies text-level perturbation at discrete step boundaries with ATE computation, our Causal-TIC applies NLDD logit degradation at each token position, yielding a continuous curve that captures within-step dynamics invisible to TTS. Critically, C(t) is not subject to the probe inflation problem: it measures *behavioral change* under intervention, not decodability from representations.\\n\\n**The Calibrated Faithfulness Gap as a Diagnostic Signal.** The core diagnostic is G*(t) = P*(t) − C(t), where P*(t) is null-probe-calibrated. This calibration fundamentally changes the gap's interpretation:\\n- G*(t) ≈ 0 means excess internal information (above correlative baseline) and CoT causal contribution are aligned — a necessary condition for faithfulness.\\n- G*(t) >> 0 means the model possesses answer information *beyond correlative features* that is not causally contributed by CoT text — genuine information excess, not merely probe inflation.\\n- G*(t) < 0 would indicate CoT contributes more than the model's calibrated internal information suggests — potentially indicating information assembled during reasoning.\\n- Because P*(t) is calibrated against the null probe, uniform probe inflation is removed. If raw P(t) is uniformly high but P_null(t) is similarly high, the calibrated P*(t) is low, correctly reflecting that the 'information' is correlative rather than answer-specific.\\n\\n**Trajectory-Shape Analysis for Phenomenon Distinguishability.** The reviewer concern that five phenomena might produce indistinguishable signatures under probe inflation motivates a critical design choice: we diagnose phenomena primarily from trajectory *shapes* (temporal derivatives, curvature, onset timing) rather than absolute gap values. This shape-over-magnitude approach is empirically validated: the entropy trajectory literature (2603.18940) demonstrates that 'whether entropy decreases at every step, not how much it drops, predicts correctness,' and RQA analysis (2602.06266) shows temporal shape features outperform aggregate statistics for reasoning complexity classification (36.94% vs. 28.97%).\\n\\nConcretely, we extract six shape features from the calibrated dual-TIC:\\n(i) P*(0) level — initial excess information at CoT onset, after null-probe calibration. Detects pre-CoT encoding: high P*(0) means the model possesses answer-specific information (above correlative baseline) before any reasoning.\\n(ii) dP*/dt trajectory — rate of excess information accumulation. Flat dP*/dt indicates information was front-loaded; positive dP*/dt indicates genuine information acquisition during reasoning.\\n(iii) C(t) plateau onset t* — the temporal position where causal contribution saturates. Captures the Reasoning Horizon.\\n(iv) G*(t) trajectory shape — the curvature and monotonicity of the calibrated gap over time. Distinguishes Reasoning Theater (monotonically widening: P* rises while C stays flat) from genuine reasoning (G* near zero throughout) from pre-CoT encoding (G* starts high, stays constant).\\n(v) dC/dt locality — short- vs. long-range autocorrelation in the causal contribution gradient. Short-range only captures myopic planning; long-range structure indicates global planning.\\n(vi) P*-C divergence at thinking/answer boundary — a spike in G*(t) at the interface between thinking tokens and answer tokens detects the thinking-answer gap.\\n\\n**Worked Example: Distinguishability Under Probe Inflation.** We demonstrate that trajectory shapes remain distinguishable even under the weak assumption. Consider three phenomena with raw P(t) uniformly inflated by +0.3 due to correlative information:\\n\\n*Pre-CoT encoding:* Raw P(t) = 0.9 from t=0 (0.6 real + 0.3 correlative), flat throughout. Null probe P_null(t) ≈ 0.3 uniformly. Calibrated P*(t) ≈ 0.6 from t=0, flat. C(t) ≈ 0.1 throughout (CoT adds little). G*(t) ≈ 0.5, constant. Shape signature: flat P*(t), flat C(t), large constant gap. dP*/dt ≈ 0.\\n\\n*Reasoning Theater:* Raw P(t) = 0.4+0.3 at t=0, rises to 0.7+0.3 during CoT as the model 'deliberates' (producing text that increases correlative features but also encodes the answer). Null probe P_null(t) ≈ 0.3 + slight increase (CoT text increases generic decodability). Calibrated P*(t) ≈ 0.1 at t=0, rises to ≈0.7 during CoT. C(t) ≈ 0.05 throughout (CoT text has no causal effect). G*(t) starts near 0, grows monotonically. Shape signature: rising P*(t), flat C(t), widening gap. dP*/dt > 0, dC/dt ≈ 0.\\n\\n*Genuine reasoning:* Raw P(t) = 0.3+0.3 at t=0, rises to 0.8+0.3 through reasoning. Null probe P_null(t) ≈ 0.3 uniformly. Calibrated P*(t) ≈ 0.0 at t=0, rises to ≈0.8. C(t) tracks P*(t) with small lag — rises from 0.0 to ≈0.7. G*(t) ≈ 0 throughout (small positive during information acquisition). Shape signature: rising P*(t) AND rising C(t), near-zero gap. dP*/dt > 0, dC/dt > 0, shapes correlated.\\n\\nCritically, these three phenomena produce distinguishable G*(t) trajectory shapes even though raw P(t) is inflated by the same +0.3 correlative offset in all cases. The null-probe calibration removes the uniform inflation; the shape features (constant vs. widening vs. near-zero gap) remain discriminable. The formal statistical framework for comparing these trajectory shapes is provided by Functional Data Analysis (Srivastava & Klassen 2016; Marron & Dryden 2021), which separates amplitude variation from phase variation via elastic registration. We will apply FDA shape distance metrics (Fisher-Rao distance) to formally test whether G*(t) trajectories cluster by phenomenon type.\\n\\n**Task-Difficulty Conditioning.** Following the 'Task Difficulty Shapes CoT Faithfulness' finding and Li et al.'s (2510.22362) independent corroboration (easy→decorative, hard→faithful), we analyze dual-TIC signatures stratified by task difficulty (using model confidence on first pass as a difficulty proxy). We predict: (a) easy instances show high P*(0) with flat C(t) (pre-CoT encoding / decoration); (b) moderate instances show Reasoning Horizon signatures (C(t) plateau at 70-85%); (c) hard instances show increasing P*(t) and C(t) trajectories (genuine reasoning). This difficulty conditioning enriches the phenomenon analysis with a predictive variable and tests whether the difficulty gradient is reflected in calibrated gap trajectory shapes.\\n\\n**Pilot Validation (Phase 0): Probe Calibration and Causal Potency.** Before running full experiments, we conduct a targeted pilot on 500 examples across MMLU (4-choice) and GSM8K (numerical) using DeepSeek-R1-Distill-Qwen-7B. The pilot has three objectives:\\n\\n(i) *Null-probe calibration validation:* Verify that P*(t) = P(t) - P_null(t) effectively removes correlative inflation. Success criterion: P_null(t) shows high absolute accuracy (demonstrating inflation is real) but P*(t) shows meaningful variance across instances and time (demonstrating calibration reveals genuine structure).\\n\\n(ii) *MCT geometric concordance:* Compute MCT separability alongside P*(t) at 10 temporal positions. Test whether MCT and P*(t) show concordant trajectories (information is geometrically prepared) or discordant trajectories (information is correlative only). If concordant, MCT validates P* as capturing computationally relevant information.\\n\\n(iii) *Causal potency test:* Test steering along answer-content probe directions at varying strengths. This tests whether answer-content probes retain any causal potency on reasoning models for multi-choice (not just binary) tasks.\\n\\n**Detailed Contingency Plan (if Phase 0 probes show no causal potency):** If answer-content steering fails on reasoning models (the most likely outcome given Cox et al.'s caveat and Yuan et al.'s findings), the framework has three fallback strategies, ordered by preference:\\n\\n*Fallback A (preferred): Calibrated information-availability interpretation with MCT validation.* If P*(t) shows meaningful temporal structure after null-probe calibration AND MCT geometric validation shows concordant trajectories, the Probe-TIC captures information that is at least geometrically organized for computation, even if not directly steerable. G*(t) measures 'information that is geometrically available but not utilized by CoT text.' This is weaker than the causal interpretation but still diagnostic: it reveals where the model's computational resources diverge from its verbal reasoning. The thermometer analogy holds — a thermometer that accurately tracks fever without curing it is still medically valuable.\\n\\n*Fallback B: Pivot to reasoning-behavioral-mode probes.* If P*(t) shows little temporal structure even after calibration (i.e., the probe captures noise), we pivot from answer-content probes to probing for *reasoning behavioral modes* — backtracking, uncertainty, verification, knowledge recall — which have confirmed causal potency on reasoning models (Internal States Before Wait, 2510.04128). The Probe-TIC becomes 'reasoning-mode information curve,' measuring when the model internally commits to a reasoning strategy. The gap G*(t) then captures the divergence between internal reasoning commitment and overt CoT causal contribution, which is a different but still novel diagnostic.\\n\\n*Fallback C: Dual-causal framework.* Replace the Probe-TIC entirely with a second causal measure — e.g., activation-patching-based information transfer (following the CMI framework, 2602.03994) — yielding a 'causal-causal' framework comparing two intervention-based signals. This eliminates the probe inflation concern entirely but loses the probe's computational efficiency.\\n\\nIn all three scenarios, the Causal-TIC component, the task-difficulty conditioning, the five-phenomenon mapping via trajectory shapes, and the TIF score remain unchanged. The core contribution — that temporal trajectory-shape signatures distinguish faithfulness phenomena — is preserved regardless of which information signal populates the P-axis.\\n\\n**Robustness Ablations.** Motivated by Young (2603.20172), who shows inter-classifier kappa as low as 0.06 for faithfulness measurements, we plan explicit robustness ablations: (a) probe architecture (linear vs. 2-layer MLP) with selectivity scores for each; (b) layer selection (best-3 vs. best-5 vs. all layers); (c) NLDD perturbation method (Gaussian corruption vs. token replacement vs. segment shuffling); (d) gap normalization (raw difference vs. ratio vs. area-under-curve); (e) null-probe calibration method (shuffled-label vs. random-representation baseline vs. MDL complexity threshold). We report sensitivity ranges for TIF scores across these axes, following Young's recommendation for multi-method validation.\\n\\n**Experiments.** Core experiments target DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Qwen-14B, DeepSeek-R1-Distill-Qwen-32B, and QwQ-32B across four benchmarks (MMLU, GPQA-Diamond, GSM8K, AIME), with a targeted validation run on DeepSeek-R1-671B (500-example subset, 3 layers). Layer-selective activation caching (5 layers from pilot study on 7B) keeps storage at ~3-5 TB. As calibration checks: (a) Kudo et al.'s synthetic arithmetic as a control where we expect G*(t) ≈ 0; (b) cross-reference TTS values from Zhao et al. on overlapping benchmarks (AIME, MATH) to validate Causal-TIC against the established per-step metric; (c) cross-reference MCT geometric pulses from Chun et al.'s methodology to validate the Probe-TIC's temporal dynamics.\\n\\n**Paper Focus (Tightened).** Following the reviewer's recommendation, the paper is organized around three core contributions with supplementary extensions:\\n\\n*Core paper:*\\n1. Phase 0 pilot results: empirical findings on probe calibration (null-probe, MCT concordance) and causal potency of answer-content probes on reasoning models — novel empirical contribution regardless of outcome.\\n2. Calibrated gap diagnostic G*(t): the null-probe-calibrated dual-estimator framework with formal trajectory-shape analysis, demonstrated on 4 models × 4 benchmarks with task-difficulty conditioning.\\n3. Five-phenomenon mapping via trajectory shapes: demonstrated distinguishability of pre-CoT encoding, Reasoning Horizon, Reasoning Theater, myopic planning, and thinking-answer gap as TIC shape signatures, with FDA statistical tests.\\n\\n*Supporting sections:*\\n4. Robustness ablations across 5 measurement dimensions.\\n5. TIF score validation against FaithCoT-Bench annotations and Liu et al.'s text-level metrics.\\n\\n*Supplementary material:*\\n6. 671B validation subset.\\n7. Early-exit criterion from Causal-TIC inflection points.\\n8. Detailed MCT and MDL calibration analysis.\\n\\n**Primary Output: Temporal Information Fidelity (TIF) Score.** An instance-level diagnostic score computed as the normalized area under the calibrated gap curve G*(t). TIF is explicitly framed as a diagnostic signal grounded in the information asymmetry between what hidden states encode (above correlative baseline) and what CoT text causally contributes. Benchmarked against FaithCoT-Bench expert annotations and cross-validated against Liu et al.'s (2602.13904) text-level pathology metrics (Necessity, Paraphrasability, Substantivity) on overlapping examples. We hypothesize TIF correlates with but does not perfectly predict expert annotations, because TIF captures potential for unfaithfulness (calibrated information availability mismatch) while experts judge realized unfaithfulness (information misuse).\\n\\n**Secondary Output: Causal Sufficiency Stopping Criterion.** As a supplementary application, we derive an early-exit criterion keyed to the Causal-TIC's inflection point. Benchmarked against existing methods but positioned as a practical byproduct, not a standalone contribution.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"650 H100-hours (300 for distilled-model inference with layer-selective activation caching on 4 models × 4 datasets + synthetic arithmetic control; 150 for NLDD causal interventions across 10-20 perturbation passes per model; 50 for probe training, null-probe calibration, Phase 0 pilot (probe + MCT + MDL), and TIF-FaithCoT-Bench validation; 50 for robustness ablations across 5 measurement dimensions; 50 for MCT geometric validation on 500-example subsets; 50 for 671B validation subset on 8×H100 node)\",\n      \"timeline\": \"4 months (2 researchers: 2 weeks Phase 0 pilot (probe calibration validation: null-probe + MCT + MDL + causal potency test on 7B) + probing pipeline via nnsight + layer-selection study + synthetic arithmetic calibration, 7 weeks core dual-estimator experiments across 4 models × 4 datasets with task-difficulty stratification and null-probe calibration at each position, 3 weeks TIF validation against FaithCoT-Bench + Liu et al. metrics + phenomenon mapping via FDA trajectory-shape analysis, 2 weeks robustness ablations + TTS cross-reference + MCT concordance analysis, 2 weeks writing)\",\n      \"estimated_gpu_cost\": \"$1,625 (at ~$2.50/H100-hr avg via RunPod/Lambda spot pricing, May 2026 rates)\",\n      \"storage\": \"3-5 TB for layer-selective activation caching (5 layers per model, fp16); reducible to ~1.5 TB via PCA to 25% dimensionality\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"550 H100-hours (Claude accelerates probing pipeline, null-probe calibration implementation, MCT computation, analysis scripts, reducing iteration overhead ~15%)\",\n      \"timeline\": \"3.5 months (1 researcher + Claude: 2 weeks Phase 0 pilot + null-probe calibration + MCT setup + pipeline, 6 weeks core experiments with difficulty stratification and calibration, 2 weeks TIF validation + phenomenon mapping + robustness ablations + FDA shape analysis, 2 weeks TTS cross-reference + paper drafting)\",\n      \"claude_api_cost\": \"$450 (code generation for probing/null-probe/MCT/intervention/FDA/ablation pipelines, automated result analysis, paper drafting; ~90M input + 22M output tokens via Sonnet 4.6)\",\n      \"estimated_gpu_cost\": \"$1,375\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"550 H100-hours (same computational footprint; experiment is GPU-bound not code-bound)\",\n      \"timeline\": \"3 months (Claude drives experiment design, implementation, analysis, and full draft; human provides weekly steering and final review)\",\n      \"claude_api_cost\": \"$900 (extensive pipeline generation, null-probe calibration sweep, MCT implementation, FDA trajectory analysis, robustness ablation design, automated result interpretation, full paper draft; ~180M input + 45M output tokens)\",\n      \"estimated_gpu_cost\": \"$1,375\",\n      \"speed_bottleneck\": \"NLDD interventions on 32B models require multiple forward passes (10-20 per example) at ~15 tok/s on 2×H100; ~250 node-hours for 20K examples across 4 datasets + arithmetic control dominate wall-clock time. MCT computation adds ~30 node-hours for geometric validation on 500-example subsets across 4 models. 671B validation subset requires 8×H100 node. Robustness ablations across 5 dimensions add ~60 node-hours.\"\n    }\n  },\n  \"key_references\": [\n    \"LLMs Faithfully and Iteratively Compute Answers During CoT: A Systematic Analysis With Multi-step Arithmetics (Kudo et al., EACL 2026, arXiv 2412.01113) — probing + activation patching on same instances for synthetic arithmetic; finds CoT IS faithful; explicitly calls for natural-task extension\",\n    \"When Chains of Thought Don't Matter: Causal Bypass in Large Language Models (Sathyanarayanan et al., arXiv 2602.03994) — CoT Mediation Index via layerwise activation patching; identifies bypass regimes (CMI ≈ 0); small scale (~50 examples), no temporal resolution\",\n    \"Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal (Yuan et al., arXiv 2605.09502, May 2026) — correctness probes at 0.95 AUROC but four interventions fail; critical context for probe interpretation and thermometer framing\",\n    \"Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought (Zhao et al., arXiv 2510.24941, Oct 2025, revised Apr 2026) — True Thinking Score (TTS) via text-level perturbation + ATE; only 2.3% of AIME steps have TTS≥0.7; tested on DeepSeek-R1-Distill-Qwen-7B/14B, Llama-8B across AIME/MATH/AMC/CommonsenseQA; direct Causal-TIC precursor\",\n    \"Spatiotemporal Hidden-State Dynamics as a Signature of Internal Reasoning in Large Language Models (Furuya & Tanimura, arXiv 2605.01853, May 2026) — StALT training-free temporal trajectory statistic; separates correct from incorrect reasoning; concurrent work adjacent to Probe-TIC\",\n    \"Mapping Faithful Reasoning in Language Models (Li et al., arXiv 2510.22362, NeurIPS 2025 MechInterp Workshop) — Concept Walk framework projects reasoning steps onto concept directions, tracking temporal activation evolution; finds easy→decorative, hard→faithful patterns on Qwen 3-4B in safety domain; supports task-difficulty conditioning; different methodology (concept directions, not answer-content probes) and domain (safety, not reasoning benchmarks), no continuous causal-contribution curve\",\n    \"Task Difficulty Shapes Chain-of-Thought Faithfulness (ICLR 2026 Workshop) — CoT transitions from decorative to load-bearing with difficulty; error propagation 22% (MMLU) to 41% (BBH); probes are 'readout rather than control'; independently validates diagnostic framing\",\n    \"Diagnosing Pathological Chain-of-Thought in Reasoning Models (Liu et al., arXiv 2602.13904, Feb 2026) — text-level metrics (Necessity, Paraphrasability, Substantivity) for three CoT pathologies; computationally inexpensive, task-agnostic; validated on model organisms; complementary text-level diagnostic\",\n    \"Measuring Faithfulness Depends on How You Measure: Classifier Sensitivity in LLM Chain-of-Thought Evaluation (Young, arXiv 2603.20172, Mar 2026) — inter-classifier kappa as low as 0.06; up to 30.6pp divergence across classifiers on 10,276 traces; motivates robustness ablations for TIF\",\n    \"Emergent Manifold Separability during Reasoning in LLMs (Chun et al., arXiv 2602.20338, Feb 2026) — Manifold Capacity Theory reveals transient geometric pulses; probe accuracy ≠ computational readiness; critical for probe inflation diagnosis and MCT geometric validation methodology\",\n    \"Tracing the Traces: Latent Temporal Signals for Efficient and Accurate Reasoning (Vilas et al., ICLR 2026, arXiv 2510.10494) — latent-trajectory signals (net/cumulative/aligned change) for reasoning efficiency; 14-70% token savings; adjacent temporal hidden-state methodology applied to efficiency not faithfulness\",\n    \"Probing and Steering Chain-of-Thought Unfaithfulness in Language Models (Occhipinti et al., ICLR 2026 LIT Workshop) — faithfulness encoded as linear directions in middle-to-late layers; probing F1 90-100%; steering recovers 46% monitorability with <5% collateral\",\n    \"Designing and Interpreting Probes with Control Tasks (Hewitt & Liang, EMNLP 2019) — selectivity scores via shuffled-label control probes; MLP probes show low selectivity (4.5) vs. linear probes (26.0); foundational methodology for null-probe calibration\",\n    \"Information-Theoretic Probing with Minimum Description Length (Voita & Titov, EMNLP 2020, arXiv 2003.12298) — MDL-based probing reveals standard accuracy does not favor pretrained over random representations; codelength as alternative to accuracy; methodology for MDL complexity check\",\n    \"LEACE: Perfect Linear Concept Erasure in Closed Form (Belrose et al., NeurIPS 2023, arXiv 2306.03819) — provable erasure preventing all linear classifiers from detecting a concept; methodology for amnesic probing validation\",\n    \"Improving Causal Interventions in Amnesic Probing with Mean Projection or LEACE (Dobrzeniecka et al., ACL Findings 2025, arXiv 2506.11673) — LEACE and Mean Projection outperform INLP for amnesic probing; methodology for causal validation of probe signals\",\n    \"Shape-over-magnitude dissociation in entropy trajectories (arXiv 2603.18940, 2026) — entropy trajectory monotonicity predicts reasoning reliability regardless of absolute levels; +5.8pp at 73.7% coverage; validates trajectory-shape analysis for reasoning diagnosis\",\n    \"Is My Model 'Mind Blurting'? Recurrence Quantification Analysis of Reasoning Dynamics (arXiv 2602.06266, Feb 2026) — temporal RQA shape features (determinism variability, laminarity slope) outperform aggregate statistics for complexity classification (36.94% vs. 28.97%); supports shape-over-magnitude approach\",\n    \"LLM Reasoning as Trajectories: Step-Specific Representation Geometry (arXiv 2604.05655, Apr 2026, Microsoft) — correct vs. incorrect reasoning paths diverge geometrically at late steps; 0.852 AUC from shape features vs. 0.649 from step-count baselines\",\n    \"Internal States Before Wait Modulate Reasoning Patterns (arXiv 2510.04128, 2025) — crosscoders on DeepSeek-R1-Distill-Llama-8B identify backtracking, uncertainty, knowledge recall, double-checking features with causal interventions confirmed; informs contingency plan for reasoning-behavioral-mode probes\",\n    \"FACT-E: Causality-Inspired Evaluation for Trustworthy Chain-of-Thought Reasoning (Sun et al., ACL Findings 2026, arXiv 2604.10693) — controlled perturbations measuring intra-chain faithfulness + CoT-to-answer consistency; no hidden-state access\",\n    \"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (Alvarez & Baheri, arXiv 2605.13772, May 2026) — geometric features for step-level hallucination detection\",\n    \"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures (Somov et al., arXiv 2603.16475) — up to 60% failure to update after intervention\",\n    \"When Is Thinking Enough? Early Exit via Sufficiency Assessment (Xiang et al., arXiv 2604.06787) — DTSR 28.9-34.9% token reduction\",\n    \"FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness (Swaroop et al., arXiv 2509.13334)\",\n    \"Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks (Qian et al., NeurIPS 2025, arXiv 2506.02867)\",\n    \"Temporal Predictors of Outcome in Reasoning Language Models (David, arXiv 2511.14773, Nov 2025)\",\n    \"Reasoning Models Know When They're Right: Probing for Self-Verification (Zhang et al., arXiv 2504.05419, Apr 2025) — probes on DeepSeek-R1-Distill achieve >0.7-0.9 AUC for correctness; enables 24% early-exit savings; tested on reasoning models\",\n    \"Analysing Chain of Thought Dynamics: Active Guidance or Unfaithful Post-hoc Rationalisation? (Lewis-Lim et al., EMNLP 2025, arXiv 2508.19827)\",\n    \"The Illusion of Reasoning: Step-Level Evaluation Reveals Decorative CoT (Basu & Chakraborty, arXiv 2603.22816, Mar 2026)\",\n    \"Why Models Know But Don't Say: CoT Faithfulness Divergence (Young, arXiv 2603.26410, Mar 2026)\",\n    \"Therefore I am. I Think (Esakkiraja et al., arXiv 2604.01202, Apr 2026)\",\n    \"Early Stopping via Confidence Dynamics: CoDE-Stop (Hosseini et al., arXiv 2604.04930, Apr 2026)\",\n    \"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning (Ye et al., arXiv 2602.11201, Feb 2026)\",\n    \"Decoding Answers Before Chain-of-Thought: Pre-CoT Probes and Activation Steering (Cox et al., arXiv 2603.01437, Mar 2026) — pre-CoT probes >0.9 AUC; steering flips >50% on instruction-tuned models; explicitly limited to binary tasks ≤9B; reports 'little success steering' reasoning models\",\n    \"Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought (Boppana et al., arXiv 2603.05488, Mar 2026)\",\n    \"No Global Plan in Chain-of-Thought: Latent Planning Horizon of LLMs (Xu et al., arXiv 2602.02103, Feb 2026)\",\n    \"Catching Rationalization in the Act: Detecting Motivated Reasoning via Activation Probing (Mirtaheri & Belkin, arXiv 2603.17199, Mar 2026)\",\n    \"Analyzing and Improving CoT Monitorability Through Information Theory (Anwar et al., arXiv 2602.18297, Feb 2026)\",\n    \"FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of CoT Reasoning (ICLR 2026, arXiv 2510.04040)\",\n    \"The Mirage of Explainability: A Survey on CoT Faithfulness (Jin et al., submitted to ARR for ACL 2026; no public arXiv version)\",\n    \"Lie to Me: How Faithful Is CoT Reasoning in Reasoning Models? (arXiv 2603.22582, Mar 2026)\",\n    \"Understanding Chain-of-Thought in LLMs through Information Theory (Ton et al., ICML 2025, arXiv 2411.11984)\",\n    \"The Potential of CoT for Reasoning: Trace Dynamics (Bachmann et al., arXiv 2602.14903, Feb 2026)\",\n    \"NEAT: Neuron-Based Early Exit for Large Reasoning Models (arXiv 2602.02010, Feb 2026)\",\n    \"ESTAR: Early-Stopping Token-Aware Reasoning (arXiv 2602.10004, Feb 2026)\",\n    \"When Chain-of-Thought Fails, the Solution Hides in the Hidden States (arXiv 2604.23351, Apr 2026)\",\n    \"Knowing Before Saying: LLM Representations Encode CoT Success Before Completion (ACL Findings 2025, arXiv 2505.24362)\",\n    \"From Reasoning to Answer: Mechanistic Insights into Distilled DeepSeek R1 Models (arXiv 2509.23676, 2025) — activation patching on R1-Distill shows reasoning token perturbations flip outputs with NLD up to 0.5\",\n    \"Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance? (Ravichander et al., arXiv 2005.00719, 2020) — properties recoverable from representations even when models cannot use them; foundational for probe inflation concern\",\n    \"Amnesic Probing: Behavioral Explanation with Amnesic Counterfactuals (Elazar et al., TACL 2021, arXiv 2006.00995) — conventional probing performance is not correlated to task importance; amnesic probing tests whether detected information is causally used\",\n    \"I Have Covered All the Bases: Interpreting Reasoning Features via SAEs (arXiv 2503.18878, 2025) — SAE feature taxonomies on R1-Distill and QwQ-32B; informs SAE-based contingency\",\n    \"Addressing Divergent Representations from Causal Interventions on Neural Networks (arXiv 2511.04638, 2025) — classifies probe-causal divergences into harmless (behavioral null-space) and pernicious (hidden pathway activation); pattern of divergence is context-dependent and informative\"\n  ],\n  \"description\": \"We propose a calibrated dual-estimator Temporal Information Curve (TIC) framework that diagnoses chain-of-thought faithfulness by measuring the divergence between what a model internally represents — above a correlative baseline — and what its reasoning text causally contributes at each token position. The central methodological advance over prior work is addressing the probe inflation problem: the well-documented finding (Hewitt & Liang 2019; Chun et al. 2602.20338) that probe accuracy on hidden states captures correlative/epiphenomenal information, which would collapse all faithfulness phenomena into a single 'high gap everywhere' pattern if left uncalibrated. We introduce a three-layer calibration strategy: (1) null-probe normalization (subtracting shuffled-label probe accuracy to measure excess information above chance), (2) Manifold Capacity Theory geometric validation (verifying that detected information is geometrically organized for computation, not merely retrievable), and (3) MDL complexity checks (confirming the signal is structured, not noise-like). The calibrated Probe-TIC P*(t) is paired with NLDD-based Causal-TIC C(t) to produce the calibrated gap G*(t) = P*(t) − C(t), which we diagnose via trajectory *shapes* (temporal derivatives, curvature, onset timing) rather than absolute values — a design choice validated by the shape-over-magnitude dissociation literature (2603.18940; 2602.06266; 2604.05655).\\n\\nPrior work has established the building blocks: Kudo et al. (EACL 2026) combine probing and patching on synthetic arithmetic; the CMI framework (2602.03994) provides layerwise causal audit on ~50 examples; Zhao et al. (2510.24941) measure per-step causal contribution via TTS on AIME/MATH; Furuya & Tanimura (2605.01853) track temporal hidden-state dynamics via StALT; Li et al. (2510.22362) track concept-direction alignment over time via Concept Walk; Liu et al. (2602.13904) diagnose CoT pathologies via text-level metrics. We unify and extend these paradigms in four ways: (1) we construct a full-timeline calibrated dual-estimator curve combining null-probe-normalized answer-content linear probes (Probe-TIC) with NLDD causal interventions (Causal-TIC), with MCT geometric validation — extending TTS from per-step to continuous temporal coverage and addressing the probe inflation gap absent from all prior single-estimator approaches; (2) we map five independently discovered phenomena — pre-CoT encoding, Reasoning Horizon, Reasoning Theater, myopic planning, and thinking-answer gap — to distinguishable trajectory-shape signatures in the calibrated G*(t) curve, with a worked demonstration that shapes remain discriminable under probe inflation and formal statistical testing via FDA shape distance metrics, conditioned on task difficulty following the ICLR 2026 Workshop finding and Li et al.'s independent corroboration; (3) we derive the Temporal Information Fidelity (TIF) score with explicit robustness validation across probe architectures, layer selections, perturbation methods, normalization choices, and calibration methods, addressing the measurement sensitivity concern raised by Young (2603.20172); and (4) we include a Phase 0 pilot that simultaneously validates probe calibration methodology (null-probe, MCT concordance, MDL) and tests answer-content probe causal potency on reasoning models, with a detailed three-tier contingency plan (calibrated information-availability interpretation, reasoning-behavioral-mode probe pivot, dual-causal framework pivot) if causal potency fails.\\n\\nThe paper is focused around three core contributions: (a) Phase 0 pilot results providing novel empirical findings on probe calibration and causal potency in reasoning models; (b) the calibrated gap diagnostic G*(t) demonstrated on 4 models × 4 benchmarks with task-difficulty conditioning; (c) five-phenomenon mapping via trajectory shapes with FDA statistical tests. Robustness ablations and TIF validation form supporting sections; 671B validation and early-exit application are supplementary material.\",\n  \"revision_notes\": {\n    \"critical_changes\": [\n      \"ELEVATED GAP INFLATION TO TIER-1 AND ADDRESSED WITH THREE-LAYER CALIBRATION (Major): Reviewer identified that Chun et al.'s finding (probe accuracy ≠ computational readiness) means P(t) may be uniformly high, collapsing five-phenomenon signatures into one pattern. This is now the central methodological contribution. We introduce: (a) null-probe calibration P*(t) = P(t) - P_null(t) following Hewitt & Liang (2019), producing a calibrated curve that measures excess answer information above correlative baseline at each position; (b) MCT geometric validation following Chun et al. (2602.20338), checking whether detected information shows the transient 'geometric pulse' characteristic of computationally relevant information vs. flat/high profile of correlative information; (c) MDL complexity check following Voita & Titov (2020), confirming signal structure. This calibration removes the uniform inflation concern: if raw P(t) and P_null(t) are both high, P*(t) is low, correctly reflecting absence of answer-specific information.\",\n      \"ADDED FORMAL TRAJECTORY-SHAPE ANALYSIS WITH WORKED EXAMPLE (Major): Reviewer argued five-phenomenon distinguishability was underspecified under the weak assumption. We now: (a) provide a concrete worked example showing three phenomena (pre-CoT encoding, Reasoning Theater, genuine reasoning) produce distinguishable G*(t) trajectory shapes even with +0.3 correlative inflation, because null-probe calibration removes the uniform offset and shape features (constant vs. widening vs. near-zero gap) remain discriminable; (b) adopt trajectory-shape features (six features: P*(0) level, dP*/dt, C(t) plateau onset, G*(t) curvature, dC/dt locality, P*-C boundary divergence) rather than absolute values; (c) cite the shape-over-magnitude dissociation literature (entropy trajectories 2603.18940, RQA analysis 2602.06266, trajectory geometry 2604.05655) establishing that temporal shape features are more diagnostic than absolute values; (d) plan FDA (Functional Data Analysis) shape distance metrics (Fisher-Rao distance) for formal statistical testing of trajectory clustering by phenomenon type.\",\n      \"CITED LI ET AL. (2510.22362) 'MAPPING FAITHFUL REASONING' (Minor): Concept Walk framework now cited in core_problem, opportunity, and landscape sections. Differentiated: uses concept directions (not answer-content probes), single domain (safety, not reasoning benchmarks), single model (Qwen 3-4B), no continuous causal-contribution curve. Supports task-difficulty conditioning (easy→decorative, hard→faithful) as independent corroboration.\",\n      \"EXPANDED PHASE 0 CONTINGENCY PLAN TO THREE TIERS (Major): If Phase 0 confirms probes lack causal potency on reasoning models, three ordered fallbacks: (A) calibrated information-availability interpretation with MCT validation (preferred — if P*(t) shows meaningful structure and MCT is concordant, the thermometer analogy holds); (B) pivot to reasoning-behavioral-mode probes targeting backtracking/uncertainty/verification, which have confirmed causal potency on reasoning models (2510.04128); (C) dual-causal framework replacing probes with a second intervention-based measure (CMI-style). In all three scenarios, Causal-TIC, task-difficulty conditioning, five-phenomenon mapping, and TIF score are preserved.\",\n      \"TIGHTENED PAPER FOCUS (Minor): Following reviewer recommendation, paper is organized as: Core = Phase 0 pilot + calibrated gap diagnostic + difficulty-conditioned trajectory-shape signatures (3 contributions). Supporting = robustness ablations + TIF validation. Supplementary = 671B validation + early-exit application + detailed calibration analysis.\",\n      \"ADDED PROBE CALIBRATION LITERATURE (Major): New references: Hewitt & Liang (EMNLP 2019) for selectivity/control probes; Voita & Titov (EMNLP 2020) for MDL probing; Belrose et al. (NeurIPS 2023) for LEACE erasure; Dobrzeniecka et al. (ACL Findings 2025) for improved amnesic probing; Ravichander et al. (2020) for probe-task-relevance gap. Also added trajectory-shape references: entropy trajectory (2603.18940), RQA reasoning dynamics (2602.06266), trajectory geometry (2604.05655).\",\n      \"ADDED REASONING-MODEL PROBING LITERATURE FOR CONTINGENCY (Minor): Internal States Before Wait (2510.04128) for causally potent reasoning-behavioral-mode probes on R1-Distill; From Reasoning to Answer (2509.23676) for activation patching on R1-Distill; I Have Covered All the Bases (2503.18878) for SAE feature taxonomies on R1-Distill and QwQ-32B.\"\n    ],\n    \"what_stayed\": \"The five-phenomena unification thesis (now with formal trajectory-shape analysis), the dual-TIC concept (now with probe calibration), the NLDD and probe estimators, the four benchmarks (MMLU, GPQA-Diamond, GSM8K, AIME), the four target models (DeepSeek-R1-Distill 7B/14B/32B, QwQ-32B), the 671B validation subset, layer-selective caching, the TIF score concept, the synthetic arithmetic calibration check, the TTS cross-reference, the task-difficulty conditioning, the robustness ablations, and the diagnostic (thermometer) framing. The core insight — that the gap between calibrated internal information and causal contribution reveals diagnostic patterns invisible to either estimator alone — is substantially strengthened by probe calibration methodology, trajectory-shape analysis, and formal distinguishability arguments.\",\n    \"residual_risks\": [\n      \"TIER-1: Null-probe calibration may over-correct. If P_null(t) is high because hidden states contain rich correlative structure (not random noise), subtracting it may remove genuine answer information that happens to correlate with generic features. Mitigation: compare three calibration methods (shuffled-label, random-representation, MDL threshold) and report sensitivity; if calibration methods disagree substantially, this reveals the calibration boundary is itself a finding about representation structure.\",\n      \"TIER-1: The TTS paper (Zhao et al. 2510.24941) tests on our exact models and benchmarks. If Causal-TIC (NLDD-based) and TTS (ATE-based) show near-identical patterns at step boundaries, the continuous-temporal-coverage novelty narrows. Mitigation: the calibrated dual-estimator gap and five-phenomenon trajectory-shape mapping remain unique; within-step dynamics visible to Causal-TIC but invisible to TTS provide differentiation. The probe calibration methodology (null-probe + MCT) is a standalone contribution regardless.\",\n      \"TIER-1: MCT geometric validation may show discordance with P*(t) — i.e., the geometric pulse timing does not match the calibrated probe trajectory. If so, this reveals that even calibrated probes capture information not geometrically prepared for use. Mitigation: the discordance itself would be a finding about the relationship between information availability and computational readiness; we proceed with Fallback A (calibrated information-availability interpretation) noting the specific type of gap between geometric readiness and probe decodability.\",\n      \"TIER-2: Task-difficulty conditioning may reveal that the five phenomena are not signatures of a unified information dynamic but artefacts of different task types. If pre-CoT encoding is exclusively an easy-task phenomenon and Reasoning Horizon is exclusively a moderate-task phenomenon, the 'unification' thesis weakens to a 'taxonomy indexed by difficulty.' This would be less exciting but still publishable.\",\n      \"TIER-2: Measurement sensitivity (Young 2603.20172): TIF may show high sensitivity to probe and intervention choices. If robustness ablations reveal instability, this undermines diagnostic utility. Mitigation: plan ablations early and report sensitivity ranges; if instability is severe, this becomes a finding about the fundamental difficulty of faithfulness measurement.\",\n      \"TIER-2: NLDD interventions remain computationally expensive (10-20 perturbation passes per example on 32B models). MCT computation adds ~30 node-hours. Robustness ablations across 5 dimensions add further cost. May need subsampling for AIME long CoT traces.\",\n      \"TIER-2: The field is moving at 3+ papers per month. Additional concurrent work (especially calibrated probe or dual-estimator approaches) may narrow the novelty window. The probe calibration methodology, trajectory-shape analysis, and Phase 0 pilot (providing novel empirical evidence about probe inflation in reasoning models) are more defensible against this risk than the original uncalibrated framework.\"\n    ]\n  }\n}\nJSONEOF",
  "description": "Output the complete revised JSON proposal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c7a6027-c0bc-4370-9e30-30aab2a95b59",
  "isSidechain": false,
  "requestId": "req_011CbBu7fynbMRyDitBn83oe",
  "type": "assistant",
  "uuid": "fc68d095-2786-422c-9739-eabe7a4f4201",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QsMTGqneNPVBJ36zXkjASn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16388,
      "cache_read_input_tokens": 27969,
      "output_tokens": 18747,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16388,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 18747,
          "cache_read_input_tokens": 27969,
          "cache_creation_input_tokens": 16388,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16388
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

_source line 31 · 2026-05-19T12:14:39.651Z_

<details><summary>↩ Tool result · reported error · `toolu_01XAp2MKe45XQjpavHKeRbzW`</summary>

```text
Contains brace with quote character (expansion obfuscation)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc68d095-2786-422c-9739-eabe7a4f4201",
  "isSidechain": false,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "type": "user",
  "uuid": "7dbbebc2-9639-458e-9214-b546ccf7bb5d",
  "toolUseResult": "Error: Contains brace with quote character (expansion obfuscation)",
  "sourceToolAssistantUUID": "fc68d095-2786-422c-9739-eabe7a4f4201",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"The Probe-Intervention Gap: Diagnosing Chain-of-Thought Faithfulness v…",
  "leafUuid": "7dbbebc2-9639-458e-9214-b546ccf7bb5d",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise gap diagnostic discriminability and phenomenon distinguishability",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f"
}
```

---

### Assistant

_source line 34 · 2026-05-19T12:14:45.176Z_

<details><summary>Logged reasoning block</summary>

```text
The heredoc is having issues with special characters. Let me write this to a file instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7dbbebc2-9639-458e-9214-b546ccf7bb5d",
  "isSidechain": false,
  "requestId": "req_011CbBuhpUTyCSa6MFz6y4mf",
  "type": "assistant",
  "uuid": "9f9aa9df-18c9-4678-a65d-f90d31400364",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Hrri5S9UDiJvJ1ujVBSN1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18776,
      "cache_read_input_tokens": 44357,
      "output_tokens": 14738,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18776,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14738,
          "cache_read_input_tokens": 44357,
          "cache_creation_input_tokens": 18776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18776
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

_source line 35 · 2026-05-19T12:14:45.671Z_

Let me write the JSON to a file instead.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f9aa9df-18c9-4678-a65d-f90d31400364",
  "isSidechain": false,
  "requestId": "req_011CbBuhpUTyCSa6MFz6y4mf",
  "type": "assistant",
  "uuid": "ce55f2c1-41cd-4a3c-bf89-8d116034c839",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Hrri5S9UDiJvJ1ujVBSN1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18776,
      "cache_read_input_tokens": 44357,
      "output_tokens": 14738,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18776,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14738,
          "cache_read_input_tokens": 44357,
          "cache_creation_input_tokens": 18776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18776
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

_source line 36 · 2026-05-19T12:20:34.865Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Gu2ErqazwpA2VAqpgPoNB2`</summary>

```json
{
  "file_path": "/tmp/revised_proposal_r5.json",
  "content": "{\n  \"change_type\": \"major\",\n  \"title\": \"The Probe-Intervention Gap: Diagnosing Chain-of-Thought Faithfulness via Calibrated Dual-Estimator Temporal Information Decomposition\",\n  \"project_name\": \"cot_faithfulness_decomp\",\n  \"source\": \"web_research\",\n  \"level\": \"top-tier\",\n  \"target_venues\": [\n    \"ICLR 2027 (abstract: Sep 19, full paper: Sep 24, 2026; conference: Apr/May 2027 — primary target, 4 months from now)\",\n    \"ICML 2027 (full paper: Jan 29, 2027; conference: Jul 2027 — comfortable fallback if additional experiments needed)\"\n  ],\n  \"core_problem\": \"Multiple independent findings in 2025-2026 — Reasoning Horizon, pre-CoT answer encoding, Reasoning Theater, myopic planning, thinking-answer gap — all describe facets of the same underlying problem: models' chain-of-thought reasoning is partially or entirely decorative. While the CoT faithfulness literature has catalogued these phenomena (Jin et al.'s survey; FaithCoT-Bench at ICLR 2026) and several groups have measured temporal dynamics of individual signals, no work has unified these disparate phenomena under a single information-theoretic framework that explains WHY and WHEN each occurs. Crucially, recent work reveals that the relationship between faithfulness and task difficulty is not binary: CoT transitions from decorative to load-bearing as task difficulty increases ('Task Difficulty Shapes CoT Faithfulness,' ICLR 2026 Workshop), with error propagation ranging from 22% on MMLU to 41% on BBH. This difficulty gradient — detectable via hidden-state probes but resistant to single-direction steering ('readout rather than control') — demands a diagnostic framework that can characterize faithfulness along both temporal and difficulty dimensions. A critical methodological concern, raised by the probing literature (Hewitt & Liang 2019; Ravichander et al. 2020; Chun et al. 2602.20338) and reinforced by Yuan et al. (2605.09502), is that probe accuracy on hidden states captures correlative/epiphenomenal information rather than information the model actively uses — probe accuracy does not equal computational readiness. This means any probe-based diagnostic must address the gap inflation problem: if probes detect uniformly high 'information availability' regardless of actual faithfulness, the diagnostic collapses. The closest precedents — Kudo et al.'s (EACL 2026) probing + activation patching on synthetic arithmetic, the CMI framework's layerwise causal audit on ~50 examples, Zhao et al.'s (2510.24941) True Thinking Score providing per-step causal contribution on AIME/MATH, Furuya & Tanimura's (2605.01853) training-free StALT trajectory statistic, and Li et al.'s (2510.22362, NeurIPS 2025 MechInterp Workshop) Concept Walk tracking temporal concept-direction alignment — each capture one dimension of the problem but none provides a calibrated dual-estimator framework that jointly measures internal information and causal contribution across the full CoT timeline on natural benchmarks, with explicit controls for probe inflation.\",\n  \"opportunity\": \"The field has independently produced three complementary measurement paradigms: (1) probe-based approaches revealing what the model internally represents at each CoT position (David 2511.14773: correctness decodable at t=4 tokens; Cox et al. 2603.01437: pre-CoT probes at >0.9 AUC with causal validation via steering on instruction-tuned models up to 9B; Esakkiraja et al. 2604.01202: pre-generation probes with >90% AUROC; Furuya & Tanimura 2605.01853: training-free StALT separating correct from incorrect trajectories; Li et al. 2510.22362: Concept Walk tracking concept-direction alignment per step, finding easy to decorative, hard to faithful), (2) intervention-based approaches measuring what the CoT text causally contributes (Ye et al. 2602.11201: NLDD reveals Reasoning Horizon at 70-85%; Zhao et al. 2510.24941: True Thinking Score provides per-step ATE on AIME/MATH/AMC/CommonsenseQA, finding only 2.3% of AIME steps have TTS>=0.7; Basu & Chakraborty 2603.22816: decorative/scaffolding/genuine taxonomy), and (3) diagnostic approaches characterizing CoT pathologies (Liu et al. 2602.13904: text-level metrics for rationalization/encoded/internalized reasoning via model organisms; 'Task Difficulty Shapes CoT Faithfulness' ICLR 2026 Workshop: difficulty-dependent faithfulness gradient). Two prior works have combined probing with causal interventions on the same instances: Kudo et al. (2412.01113, EACL 2026) train linear probes and perform activation patching across arithmetic CoT; the CMI framework (2602.03994) measures CoT-mediated causal influence via layerwise patching. However, neither provides: (a) full temporal-position coverage across CoT on natural benchmarks, (b) a mapping to the five named faithfulness phenomena, (c) a standalone instance-level diagnostic score, (d) systematic multi-model comparison on realistic reasoning tasks, (e) robustness validation across measurement methodologies — a critical gap highlighted by Young's (2603.20172) finding that faithfulness measurements are classifier-sensitive (inter-classifier kappa as low as 0.06), or (f) controls for probe inflation — the well-documented problem that probe accuracy captures correlative information not actively used by the model (Hewitt & Liang 2019; Voita & Titov 2020; Chun et al. 2602.20338). The opportunity is to extend the probe-intervention combination paradigm to a calibrated dual-estimator Temporal Information Curve (TIC) framework producing a 2D faithfulness signal — the gap between calibrated probe-estimated internal information and intervention-estimated causal contribution — on natural benchmarks at scale, with explicit probe inflation controls and robustness validation.\",\n  \"landscape\": \"**Probe-intervention combinations (closest prior work).** Kudo et al. (2412.01113, EACL 2026) train per-position linear probes on hidden states and validate with sliding-window activation patching on 9 models across synthetic multi-step arithmetic. They find CoT IS faithful for arithmetic but explicitly note their synthetic setting may not generalize to 'more realistic reasoning tasks in natural language.' The CMI framework (2602.03994) introduces the CoT Mediation Index via layerwise activation patching across Phi, Qwen, and DialoGPT on StrategyQA (20 examples), TruthfulQA (10), and GSM8K (20), identifying 'bypass regimes' where CMI is approximately 0. Both are complementary precursors.\\n\\n**Per-step causal contribution (direct Causal-TIC precursor).** Zhao et al. (2510.24941, Oct 2025, revised Apr 2026) introduce the True Thinking Score (TTS), measuring per-step causal contribution via text-level perturbation (numerical offsets preserving grammar) and ATE computation. On DeepSeek-R1-Distill-Qwen-7B/14B/Llama-8B across AIME, MATH, AMC, CommonsenseQA, they find only 2.3% of AIME steps have TTS>=0.7. TTS also extracts a 'TrueThinking direction' from hidden states for steering (53.6-91.2% flip rates). TTS is a direct precursor to our Causal-TIC component. Key differentiators: TTS operates at discrete step granularity (not continuous temporal), is a single-estimator metric (no calibrated probe gap), uses text-level perturbation (vs. our NLDD logit degradation), and does not map to the five faithfulness phenomena or provide an instance-level diagnostic score grounded in the probe-intervention divergence. Our framework extends TTS's causal measurement from per-step to continuous temporal coverage and pairs it with the calibrated Probe-TIC for the gap diagnostic unavailable from either estimator alone.\\n\\n**Training-free temporal hidden-state dynamics (concurrent work adjacent to Probe-TIC).** Furuya & Tanimura (2605.01853, May 2026) introduce StALT (Spatiotemporal Amplitude of Latent Transition), a training-free trajectory statistic that separates correct from incorrect reasoning trajectories by tracking hidden-state transitions across decoding steps and layers. Tested on GSM8K, MATH-500, and GPQA. StALT is conceptually adjacent to our Probe-TIC in tracking temporal hidden-state evolution. Key differentiators: StALT targets correctness separation (not faithfulness diagnosis), is training-free (vs. our trained answer-content probes targeting specific answer information), lacks a causal intervention component (no gap diagnostic), and does not map to faithfulness phenomena.\\n\\n**Temporal concept-direction tracking (concurrent work supporting task-difficulty conditioning).** Li et al. (2510.22362, NeurIPS 2025 MechInterp Workshop) introduce Concept Walk, which projects each reasoning step's activations onto concept directions (learned via difference-of-means from contrastive data) and tracks temporal evolution across CoT. On Qwen 3-4B in the safety domain, they find easy cases produce only transient activation shifts under perturbation (decorative CoT), while hard cases produce sustained, structured shifts (faithful CoT). This directly supports our task-difficulty conditioning dimension. Key differentiators from our framework: Concept Walk uses concept directions (not answer-content probes), operates in a single domain (safety, not reasoning benchmarks), lacks a separate causal-contribution curve (perturbation is used for classification, not as a continuous C(t) estimator), tests on one small model (Qwen 3-4B), and does not derive an instance-level diagnostic score from the probe-intervention gap.\\n\\n**Latent-trajectory signals for efficiency.** Vilas et al. (2510.10494, ICLR 2026) define three latent-trajectory signals — net change, cumulative change, and aligned change — tracking hidden-state evolution across 500-token segments. On DeepSeek-R1-Distill-Qwen-14B, Phi-4-Reasoning-Plus, and Qwen3-14B across GPQA Diamond, AIME 2025, and TSP, they achieve 14-70% token savings and +2.6% accuracy gains. Focuses on efficiency, not faithfulness. Adjacent methodology but orthogonal goal.\\n\\n**The diagnostic-not-causal challenge.** Yuan et al. (2605.09502, May 2026) show that probes detecting trace correctness achieve 0.95 AUROC but four interventions fail, concluding error representations are 'fundamentally different from editable factual knowledge representations.' Cox et al. (2603.01437) demonstrate that answer-content probe directions are causally potent on instruction-tuned models: steering flips >50% of answers. However, Cox et al.'s validation is restricted to binary classification tasks on models up to 9B parameters, and they explicitly note that for reasoning models, they find 'some success using probes to linearly decode the final answer, but little success steering to change it.' This means the causal potency of answer-content probes on reasoning models (our target model class) is NOT yet established. We therefore introduce probe calibration methodology to address the inflation problem.\\n\\n**The probe inflation problem.** The probing literature has thoroughly documented that high probe accuracy does not entail task relevance. Hewitt & Liang (2019) show that MLP probes achieve only 4.5 selectivity on POS tagging (97.3% accuracy vs. 92.8% on shuffled-label controls). Ravichander et al. (2020) demonstrate that 'even when models cannot use a linguistic property to perform the task, the property can be reliably recovered from neural representations.' Voita & Titov (2020) show that MDL-based probing reveals that standard accuracy does not substantially favor pretrained over random representations. Most directly, Chun et al. (2602.20338) apply Manifold Capacity Theory to CoT reasoning and find that geometric separability peaks transiently as a 'geometric pulse' just before computation and compresses rapidly afterward, while probe accuracy remains high long after computation is complete. This provides direct evidence that probe accuracy overestimates information availability during reasoning. We address this via null-probe calibration and MCT geometric validation.\\n\\n**Trajectory-shape analysis.** A separate line of work demonstrates that temporal trajectory shapes carry diagnostic information beyond absolute values. The entropy trajectory paper (2603.18940) shows a 'shape-over-magnitude dissociation': monotonicity of entropy decrease predicts reasoning reliability regardless of absolute entropy levels (+5.8pp at 73.7% coverage). RQA analysis of reasoning dynamics (2602.06266) shows that temporal features (determinism variability, laminarity slope) outperform aggregate statistics for complexity classification (36.94% vs. 28.97%). Microsoft's trajectory geometry work (2604.05655) shows correct vs. incorrect reasoning paths diverge geometrically at late steps (0.852 AUC from shape features vs. 0.649 from step-count baselines). This literature supports our core claim that even if P(t) is uniformly inflated, the trajectory shape of the gap G(t) can distinguish faithfulness phenomena.\\n\\n**CoT pathology diagnostics.** Liu et al. (2602.13904, Feb 2026) propose text-level, computationally inexpensive, task-agnostic metrics for three CoT pathologies: Necessity (rationalization), Paraphrasability (encoded reasoning), and Substantivity (internalized reasoning), validated on model organisms. Complementary to ours: purely text-level, no hidden states, categorical per-pathology metrics.\\n\\n**Measurement sensitivity.** Young (2603.20172, Mar 2026) shows faithfulness measurements are classifier-sensitive: inter-classifier kappa as low as 0.06, with up to 30.6 percentage-point divergence across three classifiers on 10,276 traces from 12 models.\\n\\n**Task-difficulty moderation of faithfulness.** 'Task Difficulty Shapes CoT Faithfulness' (ICLR 2026 Workshop) demonstrates that CoT transitions from decorative to load-bearing as task difficulty increases. Li et al. (2510.22362) independently corroborate this: Concept Walk shows easy cases produce transient/decorative patterns while hard cases produce sustained/faithful patterns.\\n\\n**Probe-based temporal measurement.** Qian et al. (2506.02867, NeurIPS 2025) compute per-token HSIC. David (2511.14773) shows correctness decodable at t=4 tokens. Zhang et al. (2504.05419) probe DeepSeek-R1-Distill variants for correctness, achieving >0.7 AUC. Lewis-Lim et al. (2508.19827, EMNLP 2025) reveal flat (rationalization) vs. increasing (genuine reasoning) confidence patterns. Mirtaheri & Belkin (2603.17199) show pre-generation probes match full-CoT monitors. Esakkiraja et al. (2604.01202) show pre-generation probes predict tool-calling at >90% AUROC.\\n\\n**Intervention-based causal measurement.** Ye et al. (2602.11201) introduce NLDD, revealing Reasoning Horizon at 70-85%. Basu & Chakraborty (2603.22816) propose taxonomy via step ablation. Somov et al. (2603.16475) show up to 60% failure to update. FACT-E (2604.10693, ACL Findings 2026) uses controlled perturbations.\\n\\n**Probing and steering faithfulness.** Occhipinti et al. (ICLR 2026 LIT Workshop) demonstrate faithfulness encoded as linear directions; probing F1 90-100%; steering 46% recovery with <5% collateral.\\n\\n**Probing reasoning models specifically.** Internal States Before Wait (2510.04128) trains crosscoders on DeepSeek-R1-Distill-Llama-8B, identifying features for backtracking, uncertainty, knowledge recall, and double-checking, with causal interventions confirmed. From Reasoning to Answer (2509.23676) uses activation patching on R1-Distill variants, finding reasoning token perturbations flip outputs with NLD up to 0.5. These inform our contingency plan.\\n\\n**Geometric and information-theoretic approaches.** Chun et al. (2602.20338) apply MCT revealing transient geometric pulses (critical for our probe calibration). Alvarez & Baheri (2605.13772) detect step-level hallucination via transport geometry. Ton et al. (ICML 2025, 2411.11984) define per-step information gain. Anwar et al. (2602.18297) decompose monitorability into information gap + elicitation error.\\n\\n**Benchmarks, surveys, and early-exit methods.** FaithCoT-Bench (ICLR 2026). Jin et al.'s survey (ARR for ACL 2026). Young (2603.26410). 'Lie to Me' (2603.22582). Reasoning Theater (2603.05488). ESTAR (2602.10004). DTSR (2604.06787). NEAT (2602.02010). CoDE-Stop (2604.04930). FRIT (2509.13334).\\n\\n**What remains open.** No extant framework provides: (1) a full-timeline calibrated dual-estimator curve combining answer-content probes with causal interventions on natural benchmarks at scale, with explicit controls for probe inflation; (2) a systematic mapping of five phenomena to distinguishable trajectory-shape signatures demonstrated to be robust under the weaker information-availability assumption via formal shape analysis; (3) an instance-level diagnostic score derived from the calibrated probe-intervention gap with explicit robustness validation; or (4) a principled account of how the probe-intervention gap behaves differently on instruction-tuned vs. reasoning models. TTS provides per-step causal contribution (single-estimator, text-level); StALT provides temporal hidden-state correctness signals (single-estimator, no causal component); Concept Walk provides temporal concept-direction alignment (single model, single domain, no continuous causal curve); Vilas et al. provide latent-trajectory efficiency signals (no faithfulness connection); Liu et al. provide text-level pathology diagnostics (no hidden states). The calibrated dual-estimator gap — jointly measuring excess internal information (above a null-probe baseline) and causal contribution across the full timeline — remains the unique contribution.\",\n  \"inspired_by\": \"The convergence of five observations: (a) Kudo et al.'s demonstration that probe+intervention combination is feasible and informative on synthetic arithmetic, with their explicit call for natural-task extension; (b) Zhao et al.'s (2510.24941) TTS demonstrating per-step causal contribution measurement at scale on our exact target benchmarks (AIME, MATH), establishing the causal-contribution paradigm we extend to continuous temporal coverage with the dual-estimator gap; (c) the finding from both Cox et al. (2603.01437) on instruction-tuned models and the 'Task Difficulty' workshop paper that probes are diagnostic ('readout') rather than interventional ('control'), clarifying the Probe-TIC interpretation; (d) Young's (2603.20172) demonstration that faithfulness measurements are classifier-sensitive, motivating explicit robustness ablation; (e) Chun et al.'s (2602.20338) discovery that probe accuracy does not equal computational readiness — geometric separability peaks transiently while probe accuracy stays flat — which motivates our null-probe calibration methodology and the adoption of trajectory-shape features rather than absolute probe values.\",\n  \"approach\": \"Define a calibrated dual-estimator Temporal Information Curve (TIC) framework that diagnoses chain-of-thought faithfulness at each token position t via two complementary signals, with explicit controls for probe inflation:\\n\\n**(a) Calibrated Probe-TIC P*(t)**: We address the probe inflation problem — the well-documented finding that probe accuracy captures correlative/epiphenomenal information not actively used by the model (Hewitt & Liang 2019; Ravichander et al. 2020; Chun et al. 2602.20338) — via a three-layer calibration strategy:\\n\\n(i) Null-probe normalization. For each layer and position, train a parallel 'null probe' on shuffled answer labels (random assignment of answer identities to hidden states). Define the calibrated Probe-TIC as P*(t) = P(t) - P_null(t), measuring excess answer information above what is extractable from correlative features alone. This follows the selectivity methodology of Hewitt & Liang (2019), adapted to our temporal setting: selectivity is computed at each position t, producing a calibrated curve rather than a single aggregate number. High P*(t) means the model's hidden states at position t encode answer information beyond what is attributable to correlative features.\\n\\n(ii) MCT geometric validation. On a subset of 500 examples per benchmark, compute Manifold Capacity Theory (Chun et al. 2602.20338) separability alongside probe accuracy at each position. MCT measures intrinsic geometric readiness for computation (the 'geometric pulse') independent of probe training, providing a probe-free check on whether the information P*(t) detects is geometrically organized for use. If MCT separability and P*(t) show concordant temporal trajectories, the probe captures information that is at least geometrically prepared; if MCT shows the characteristic transient pulse while P*(t) remains flat/high, this diagnoses the specific type of inflation present.\\n\\n(iii) MDL complexity check. Following Voita & Titov (2020), compute minimum description length for probe labels at each position. If genuine answer information requires less codelength than random labels at position t, the signal is structured; if codelengths are comparable, the signal is noise-like.\\n\\nWe probe for answer content (which answer option / numerical value the model will produce) using linear probes trained on 3-5 selected layers. On instruction-tuned models, Cox et al. (2603.01437) demonstrate such probes are causally potent (steering flips >50% of answers). However, Cox et al.'s validation is limited to binary tasks on models at most 9B, and they explicitly report that reasoning models resist steering. We therefore interpret the calibrated Probe-TIC P*(t) as measuring excess information availability — what the model internally represents at position t above a correlative baseline — rather than assuming causal potency. This interpretation is independently supported by the 'Task Difficulty Shapes CoT Faithfulness' finding that probes are 'readout rather than control,' by Yuan et al.'s (2605.09502) demonstration that correctness probes are diagnostic-not-causal, and is consistent with Furuya & Tanimura (2605.01853) and Li et al.'s (2510.22362) finding that hidden-state temporal signals are diagnostic of reasoning quality.\\n\\n**(b) Causal-TIC C(t)**: Causal contribution of CoT text up to position t to the answer via NLDD-style interventions (corrupting CoT segments and measuring logit degradation). This extends the single-model NLDD paradigm (Ye et al. 2602.11201) to systematic multi-model comparison with continuous temporal coverage, and provides a continuous temporal generalization of the per-step TTS metric (Zhao et al. 2510.24941). Where TTS applies text-level perturbation at discrete step boundaries with ATE computation, our Causal-TIC applies NLDD logit degradation at each token position, yielding a continuous curve that captures within-step dynamics invisible to TTS. Critically, C(t) is not subject to the probe inflation problem: it measures behavioral change under intervention, not decodability from representations.\\n\\n**The Calibrated Faithfulness Gap as a Diagnostic Signal.** The core diagnostic is G*(t) = P*(t) - C(t), where P*(t) is null-probe-calibrated. This calibration fundamentally changes the gap's interpretation:\\n- G*(t) approximately 0 means excess internal information (above correlative baseline) and CoT causal contribution are aligned — a necessary condition for faithfulness.\\n- G*(t) much greater than 0 means the model possesses answer information beyond correlative features that is not causally contributed by CoT text — genuine information excess, not merely probe inflation.\\n- G*(t) less than 0 would indicate CoT contributes more than the model's calibrated internal information suggests — potentially indicating information assembled during reasoning.\\n- Because P*(t) is calibrated against the null probe, uniform probe inflation is removed. If raw P(t) is uniformly high but P_null(t) is similarly high, the calibrated P*(t) is low, correctly reflecting that the 'information' is correlative rather than answer-specific.\\n\\n**Trajectory-Shape Analysis for Phenomenon Distinguishability.** We diagnose phenomena primarily from trajectory shapes (temporal derivatives, curvature, onset timing) rather than absolute gap values. This shape-over-magnitude approach is empirically validated: the entropy trajectory literature (2603.18940) demonstrates that 'whether entropy decreases at every step, not how much it drops, predicts correctness,' and RQA analysis (2602.06266) shows temporal shape features outperform aggregate statistics for reasoning complexity classification (36.94% vs. 28.97%).\\n\\nConcretely, we extract six shape features from the calibrated dual-TIC:\\n(i) P*(0) level — initial excess information at CoT onset, after null-probe calibration. Detects pre-CoT encoding.\\n(ii) dP*/dt trajectory — rate of excess information accumulation. Flat indicates front-loaded; positive indicates genuine acquisition.\\n(iii) C(t) plateau onset t* — captures the Reasoning Horizon.\\n(iv) G*(t) trajectory shape — curvature and monotonicity of the calibrated gap. Distinguishes Reasoning Theater (monotonically widening) from genuine reasoning (near-zero throughout) from pre-CoT encoding (large constant).\\n(v) dC/dt locality — short- vs. long-range autocorrelation in causal contribution gradient. Short-range only captures myopic planning.\\n(vi) P*-C divergence at thinking/answer boundary — spike in G*(t) at the interface detects the thinking-answer gap.\\n\\n**Worked Example: Distinguishability Under Probe Inflation.** Consider three phenomena with raw P(t) uniformly inflated by +0.3 due to correlative information:\\n\\nPre-CoT encoding: Raw P(t) = 0.9 from t=0 (0.6 real + 0.3 correlative), flat throughout. Null probe P_null(t) approximately 0.3 uniformly. Calibrated P*(t) approximately 0.6 from t=0, flat. C(t) approximately 0.1 throughout. G*(t) approximately 0.5, constant. Shape: flat P*(t), flat C(t), large constant gap. dP*/dt approximately 0.\\n\\nReasoning Theater: Raw P(t) = 0.7 at t=0, rises to 1.0 during CoT. Null probe P_null(t) approximately 0.3 with slight increase. Calibrated P*(t) approximately 0.1 at t=0, rises to approximately 0.7. C(t) approximately 0.05 throughout. G*(t) starts near 0, grows monotonically. Shape: rising P*(t), flat C(t), widening gap. dP*/dt > 0, dC/dt approximately 0.\\n\\nGenuine reasoning: Raw P(t) = 0.6 at t=0, rises to 1.1 through reasoning. Null probe P_null(t) approximately 0.3. Calibrated P*(t) approximately 0.0 at t=0, rises to approximately 0.8. C(t) tracks P*(t) with small lag. G*(t) approximately 0 throughout. Shape: rising P*(t) AND rising C(t), near-zero gap.\\n\\nThese three phenomena produce distinguishable G*(t) trajectory shapes even though raw P(t) is inflated by the same +0.3 in all cases. The formal statistical framework for comparing these trajectory shapes is provided by Functional Data Analysis (Srivastava & Klassen 2016; Marron & Dryden 2021), which separates amplitude variation from phase variation via elastic registration. We apply FDA shape distance metrics (Fisher-Rao distance) to formally test whether G*(t) trajectories cluster by phenomenon type.\\n\\n**Task-Difficulty Conditioning.** Following the 'Task Difficulty Shapes CoT Faithfulness' finding and Li et al.'s (2510.22362) independent corroboration (easy to decorative, hard to faithful), we analyze dual-TIC signatures stratified by task difficulty (using model confidence on first pass as a difficulty proxy). We predict: (a) easy instances show high P*(0) with flat C(t) (pre-CoT encoding / decoration); (b) moderate instances show Reasoning Horizon signatures (C(t) plateau at 70-85%); (c) hard instances show increasing P*(t) and C(t) trajectories (genuine reasoning).\\n\\n**Pilot Validation (Phase 0): Probe Calibration and Causal Potency.** Before running full experiments, we conduct a targeted pilot on 500 examples across MMLU (4-choice) and GSM8K (numerical) using DeepSeek-R1-Distill-Qwen-7B. Three objectives:\\n\\n(i) Null-probe calibration validation: Verify that P*(t) = P(t) - P_null(t) effectively removes correlative inflation. Success criterion: P_null(t) shows high absolute accuracy (demonstrating inflation is real) but P*(t) shows meaningful variance across instances and time (demonstrating calibration reveals genuine structure).\\n\\n(ii) MCT geometric concordance: Compute MCT separability alongside P*(t) at 10 temporal positions. Test concordance.\\n\\n(iii) Causal potency test: Test steering along answer-content probe directions at varying strengths on reasoning models for multi-choice tasks.\\n\\n**Detailed Contingency Plan (if Phase 0 probes show no causal potency):**\\n\\nFallback A (preferred): Calibrated information-availability interpretation with MCT validation. If P*(t) shows meaningful temporal structure after null-probe calibration AND MCT geometric validation shows concordant trajectories, the Probe-TIC captures information that is at least geometrically organized for computation, even if not directly steerable. G*(t) measures 'information that is geometrically available but not utilized by CoT text.' The thermometer analogy holds — a thermometer that accurately tracks fever without curing it is still medically valuable.\\n\\nFallback B: Pivot to reasoning-behavioral-mode probes. If P*(t) shows little temporal structure even after calibration, we pivot from answer-content probes to probing for reasoning behavioral modes — backtracking, uncertainty, verification, knowledge recall — which have confirmed causal potency on reasoning models (Internal States Before Wait, 2510.04128). The gap G*(t) then captures divergence between internal reasoning commitment and overt CoT causal contribution.\\n\\nFallback C: Dual-causal framework. Replace Probe-TIC with a second causal measure (e.g., CMI-style activation patching), yielding a causal-causal framework. Eliminates probe inflation concern entirely but loses computational efficiency.\\n\\nIn all three scenarios, Causal-TIC, task-difficulty conditioning, five-phenomenon mapping via trajectory shapes, and TIF score are preserved.\\n\\n**Robustness Ablations.** Motivated by Young (2603.20172): (a) probe architecture (linear vs. 2-layer MLP) with selectivity scores; (b) layer selection (best-3 vs. best-5 vs. all layers); (c) NLDD perturbation method (Gaussian corruption vs. token replacement vs. segment shuffling); (d) gap normalization (raw difference vs. ratio vs. area-under-curve); (e) null-probe calibration method (shuffled-label vs. random-representation baseline vs. MDL complexity threshold). Report sensitivity ranges.\\n\\n**Experiments.** Core experiments target DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Qwen-14B, DeepSeek-R1-Distill-Qwen-32B, and QwQ-32B across four benchmarks (MMLU, GPQA-Diamond, GSM8K, AIME), with a targeted validation run on DeepSeek-R1-671B (500-example subset, 3 layers). Layer-selective activation caching (5 layers from pilot study on 7B) keeps storage at approximately 3-5 TB. Calibration checks: (a) Kudo et al.'s synthetic arithmetic as control expecting G*(t) approximately 0; (b) cross-reference TTS values from Zhao et al. on overlapping benchmarks; (c) cross-reference MCT geometric pulses.\\n\\n**Paper Focus (Tightened).** Core paper: (1) Phase 0 pilot results on probe calibration and causal potency — novel empirical contribution regardless of outcome; (2) Calibrated gap diagnostic G*(t) demonstrated on 4 models x 4 benchmarks with task-difficulty conditioning; (3) Five-phenomenon mapping via trajectory shapes with FDA statistical tests. Supporting sections: robustness ablations across 5 dimensions; TIF score validation. Supplementary: 671B validation; early-exit criterion; detailed calibration analysis.\\n\\n**Primary Output: Temporal Information Fidelity (TIF) Score.** Instance-level diagnostic from normalized area under calibrated gap curve G*(t). Benchmarked against FaithCoT-Bench annotations and cross-validated against Liu et al.'s text-level pathology metrics.\\n\\n**Secondary Output: Causal Sufficiency Stopping Criterion.** Supplementary early-exit criterion from Causal-TIC inflection points.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"650 H100-hours (300 for distilled-model inference with layer-selective activation caching on 4 models x 4 datasets + synthetic arithmetic control; 150 for NLDD causal interventions across 10-20 perturbation passes per model; 50 for probe training, null-probe calibration, Phase 0 pilot (probe + MCT + MDL), and TIF-FaithCoT-Bench validation; 50 for robustness ablations across 5 measurement dimensions; 50 for MCT geometric validation on 500-example subsets; 50 for 671B validation subset on 8xH100 node)\",\n      \"timeline\": \"4 months (2 researchers: 2 weeks Phase 0 pilot including null-probe calibration, MCT concordance, MDL validation, and causal potency test on 7B, plus probing pipeline via nnsight, layer-selection study, and synthetic arithmetic calibration; 7 weeks core dual-estimator experiments across 4 models x 4 datasets with task-difficulty stratification and null-probe calibration at each position; 3 weeks TIF validation against FaithCoT-Bench plus Liu et al. metrics plus phenomenon mapping via FDA trajectory-shape analysis; 2 weeks robustness ablations plus TTS cross-reference plus MCT concordance analysis; 2 weeks writing)\",\n      \"estimated_gpu_cost\": \"$1,625 (at approximately $2.50/H100-hr avg via RunPod/Lambda spot pricing, May 2026 rates)\",\n      \"storage\": \"3-5 TB for layer-selective activation caching (5 layers per model, fp16); reducible to approximately 1.5 TB via PCA to 25% dimensionality\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"550 H100-hours (Claude accelerates probing pipeline, null-probe calibration implementation, MCT computation, analysis scripts, reducing iteration overhead approximately 15%)\",\n      \"timeline\": \"3.5 months (1 researcher + Claude: 2 weeks Phase 0 pilot plus null-probe calibration plus MCT setup plus pipeline; 6 weeks core experiments with difficulty stratification and calibration; 2 weeks TIF validation plus phenomenon mapping plus robustness ablations plus FDA shape analysis; 2 weeks TTS cross-reference plus paper drafting)\",\n      \"claude_api_cost\": \"$450 (code generation for probing/null-probe/MCT/intervention/FDA/ablation pipelines, automated result analysis, paper drafting; approximately 90M input + 22M output tokens via Sonnet 4.6)\",\n      \"estimated_gpu_cost\": \"$1,375\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"550 H100-hours (same computational footprint; experiment is GPU-bound not code-bound)\",\n      \"timeline\": \"3 months (Claude drives experiment design, implementation, analysis, and full draft; human provides weekly steering and final review)\",\n      \"claude_api_cost\": \"$900 (extensive pipeline generation, null-probe calibration sweep, MCT implementation, FDA trajectory analysis, robustness ablation design, automated result interpretation, full paper draft; approximately 180M input + 45M output tokens)\",\n      \"estimated_gpu_cost\": \"$1,375\",\n      \"speed_bottleneck\": \"NLDD interventions on 32B models require multiple forward passes (10-20 per example) at approximately 15 tok/s on 2xH100; approximately 250 node-hours for 20K examples across 4 datasets plus arithmetic control dominate wall-clock time. MCT computation adds approximately 30 node-hours for geometric validation on 500-example subsets across 4 models. 671B validation subset requires 8xH100 node. Robustness ablations across 5 dimensions add approximately 60 node-hours.\"\n    }\n  },\n  \"key_references\": [\n    \"LLMs Faithfully and Iteratively Compute Answers During CoT: A Systematic Analysis With Multi-step Arithmetics (Kudo et al., EACL 2026, arXiv 2412.01113) — probing + activation patching on same instances for synthetic arithmetic; finds CoT IS faithful; explicitly calls for natural-task extension\",\n    \"When Chains of Thought Don't Matter: Causal Bypass in Large Language Models (Sathyanarayanan et al., arXiv 2602.03994) — CoT Mediation Index via layerwise activation patching; identifies bypass regimes; small scale, no temporal resolution\",\n    \"Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal (Yuan et al., arXiv 2605.09502, May 2026) — correctness probes at 0.95 AUROC but four interventions fail; critical context for probe interpretation and thermometer framing\",\n    \"Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought (Zhao et al., arXiv 2510.24941, Oct 2025, revised Apr 2026) — True Thinking Score via text-level perturbation + ATE; only 2.3% of AIME steps have TTS>=0.7; direct Causal-TIC precursor\",\n    \"Spatiotemporal Hidden-State Dynamics as a Signature of Internal Reasoning in Large Language Models (Furuya & Tanimura, arXiv 2605.01853, May 2026) — StALT training-free temporal trajectory statistic; concurrent work adjacent to Probe-TIC\",\n    \"Mapping Faithful Reasoning in Language Models (Li et al., arXiv 2510.22362, NeurIPS 2025 MechInterp Workshop) — Concept Walk projects reasoning steps onto concept directions; finds easy to decorative, hard to faithful; supports task-difficulty conditioning; different methodology (concept directions not answer-content probes) and domain (safety not reasoning benchmarks), no continuous causal-contribution curve\",\n    \"Task Difficulty Shapes Chain-of-Thought Faithfulness (ICLR 2026 Workshop) — CoT transitions from decorative to load-bearing with difficulty; probes are 'readout rather than control'; independently validates diagnostic framing\",\n    \"Diagnosing Pathological Chain-of-Thought in Reasoning Models (Liu et al., arXiv 2602.13904, Feb 2026) — text-level metrics for three CoT pathologies; complementary text-level diagnostic\",\n    \"Measuring Faithfulness Depends on How You Measure: Classifier Sensitivity in LLM Chain-of-Thought Evaluation (Young, arXiv 2603.20172, Mar 2026) — inter-classifier kappa as low as 0.06; motivates robustness ablations\",\n    \"Emergent Manifold Separability during Reasoning in LLMs (Chun et al., arXiv 2602.20338, Feb 2026) — MCT reveals transient geometric pulses; probe accuracy does not equal computational readiness; critical for probe calibration methodology\",\n    \"Tracing the Traces: Latent Temporal Signals for Efficient and Accurate Reasoning (Vilas et al., ICLR 2026, arXiv 2510.10494) — latent-trajectory signals for reasoning efficiency; adjacent methodology\",\n    \"Probing and Steering Chain-of-Thought Unfaithfulness in Language Models (Occhipinti et al., ICLR 2026 LIT Workshop) — faithfulness encoded as linear directions; probing F1 90-100%; steering 46% recovery\",\n    \"Designing and Interpreting Probes with Control Tasks (Hewitt & Liang, EMNLP 2019) — selectivity scores via shuffled-label control probes; foundational methodology for null-probe calibration\",\n    \"Information-Theoretic Probing with Minimum Description Length (Voita & Titov, EMNLP 2020, arXiv 2003.12298) — MDL-based probing; codelength as alternative to accuracy; methodology for MDL complexity check\",\n    \"LEACE: Perfect Linear Concept Erasure in Closed Form (Belrose et al., NeurIPS 2023, arXiv 2306.03819) — provable erasure for amnesic probing validation\",\n    \"Improving Causal Interventions in Amnesic Probing with Mean Projection or LEACE (Dobrzeniecka et al., ACL Findings 2025, arXiv 2506.11673) — LEACE and Mean Projection for improved amnesic probing\",\n    \"Shape-over-magnitude dissociation in entropy trajectories (arXiv 2603.18940, 2026) — entropy trajectory monotonicity predicts reasoning reliability regardless of absolute levels; validates trajectory-shape analysis\",\n    \"Is My Model Mind Blurting? Recurrence Quantification Analysis of Reasoning Dynamics (arXiv 2602.06266, Feb 2026) — temporal RQA shape features outperform aggregate statistics for complexity classification\",\n    \"LLM Reasoning as Trajectories: Step-Specific Representation Geometry (arXiv 2604.05655, Apr 2026, Microsoft) — trajectory shape features achieve 0.852 AUC vs. 0.649 from step-count baselines\",\n    \"Internal States Before Wait Modulate Reasoning Patterns (arXiv 2510.04128, 2025) — crosscoders on R1-Distill identify reasoning features with causal interventions confirmed; informs contingency plan\",\n    \"FACT-E: Causality-Inspired Evaluation for Trustworthy Chain-of-Thought Reasoning (Sun et al., ACL Findings 2026, arXiv 2604.10693)\",\n    \"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (Alvarez & Baheri, arXiv 2605.13772, May 2026)\",\n    \"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures (Somov et al., arXiv 2603.16475)\",\n    \"When Is Thinking Enough? Early Exit via Sufficiency Assessment (Xiang et al., arXiv 2604.06787)\",\n    \"FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness (Swaroop et al., arXiv 2509.13334)\",\n    \"Demystifying Reasoning Dynamics with Mutual Information (Qian et al., NeurIPS 2025, arXiv 2506.02867)\",\n    \"Temporal Predictors of Outcome in Reasoning Language Models (David, arXiv 2511.14773, Nov 2025)\",\n    \"Reasoning Models Know When They're Right: Probing for Self-Verification (Zhang et al., arXiv 2504.05419, Apr 2025) — probes on DeepSeek-R1-Distill achieve >0.7-0.9 AUC for correctness; informs alternative probe targets\",\n    \"Analysing Chain of Thought Dynamics (Lewis-Lim et al., EMNLP 2025, arXiv 2508.19827)\",\n    \"The Illusion of Reasoning: Step-Level Evaluation Reveals Decorative CoT (Basu & Chakraborty, arXiv 2603.22816, Mar 2026)\",\n    \"Why Models Know But Don't Say: CoT Faithfulness Divergence (Young, arXiv 2603.26410, Mar 2026)\",\n    \"Therefore I am. I Think (Esakkiraja et al., arXiv 2604.01202, Apr 2026)\",\n    \"Early Stopping via Confidence Dynamics: CoDE-Stop (Hosseini et al., arXiv 2604.04930, Apr 2026)\",\n    \"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning (Ye et al., arXiv 2602.11201, Feb 2026)\",\n    \"Decoding Answers Before Chain-of-Thought (Cox et al., arXiv 2603.01437, Mar 2026) — pre-CoT probes >0.9 AUC; steering flips >50% on instruction-tuned models; limited to binary tasks; little success steering reasoning models\",\n    \"Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought (Boppana et al., arXiv 2603.05488, Mar 2026)\",\n    \"No Global Plan in Chain-of-Thought (Xu et al., arXiv 2602.02103, Feb 2026)\",\n    \"Catching Rationalization in the Act (Mirtaheri & Belkin, arXiv 2603.17199, Mar 2026)\",\n    \"Analyzing and Improving CoT Monitorability Through Information Theory (Anwar et al., arXiv 2602.18297, Feb 2026)\",\n    \"FaithCoT-Bench (ICLR 2026, arXiv 2510.04040)\",\n    \"The Mirage of Explainability: A Survey on CoT Faithfulness (Jin et al., submitted to ARR for ACL 2026)\",\n    \"Lie to Me: How Faithful Is CoT Reasoning in Reasoning Models? (arXiv 2603.22582, Mar 2026)\",\n    \"Understanding Chain-of-Thought in LLMs through Information Theory (Ton et al., ICML 2025, arXiv 2411.11984)\",\n    \"NEAT: Neuron-Based Early Exit (arXiv 2602.02010, Feb 2026)\",\n    \"ESTAR: Early-Stopping Token-Aware Reasoning (arXiv 2602.10004, Feb 2026)\",\n    \"When Chain-of-Thought Fails, the Solution Hides in the Hidden States (arXiv 2604.23351, Apr 2026)\",\n    \"Knowing Before Saying (ACL Findings 2025, arXiv 2505.24362)\",\n    \"From Reasoning to Answer: Mechanistic Insights into Distilled DeepSeek R1 Models (arXiv 2509.23676, 2025) — activation patching on R1-Distill shows reasoning token perturbations flip outputs\",\n    \"Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance? (Ravichander et al., arXiv 2005.00719, 2020) — foundational for probe inflation concern\",\n    \"Amnesic Probing: Behavioral Explanation with Amnesic Counterfactuals (Elazar et al., TACL 2021, arXiv 2006.00995) — conventional probing performance is not correlated to task importance\",\n    \"I Have Covered All the Bases: Interpreting Reasoning Features via SAEs (arXiv 2503.18878, 2025) — SAE feature taxonomies on R1-Distill and QwQ-32B; informs SAE-based contingency\",\n    \"Addressing Divergent Representations from Causal Interventions (arXiv 2511.04638, 2025) — classifies probe-causal divergences into harmless and pernicious; divergence pattern is informative\"\n  ],\n  \"description\": \"We propose a calibrated dual-estimator Temporal Information Curve (TIC) framework that diagnoses chain-of-thought faithfulness by measuring the divergence between what a model internally represents — above a correlative baseline — and what its reasoning text causally contributes at each token position. The central methodological advance over prior work is addressing the probe inflation problem: the well-documented finding (Hewitt & Liang 2019; Chun et al. 2602.20338) that probe accuracy on hidden states captures correlative/epiphenomenal information, which would collapse all faithfulness phenomena into a single 'high gap everywhere' pattern if left uncalibrated. We introduce a three-layer calibration strategy: (1) null-probe normalization (subtracting shuffled-label probe accuracy to measure excess information above chance), (2) Manifold Capacity Theory geometric validation (verifying that detected information is geometrically organized for computation, not merely retrievable), and (3) MDL complexity checks (confirming the signal is structured, not noise-like). The calibrated Probe-TIC P*(t) is paired with NLDD-based Causal-TIC C(t) to produce the calibrated gap G*(t) = P*(t) - C(t), which we diagnose via trajectory shapes (temporal derivatives, curvature, onset timing) rather than absolute values — a design choice validated by the shape-over-magnitude dissociation literature (2603.18940; 2602.06266; 2604.05655).\\n\\nPrior work has established the building blocks: Kudo et al. (EACL 2026) combine probing and patching on synthetic arithmetic; the CMI framework (2602.03994) provides layerwise causal audit on approximately 50 examples; Zhao et al. (2510.24941) measure per-step causal contribution via TTS on AIME/MATH; Furuya & Tanimura (2605.01853) track temporal hidden-state dynamics via StALT; Li et al. (2510.22362) track concept-direction alignment over time via Concept Walk; Liu et al. (2602.13904) diagnose CoT pathologies via text-level metrics. We unify and extend these paradigms in four ways: (1) we construct a full-timeline calibrated dual-estimator curve combining null-probe-normalized answer-content linear probes (Probe-TIC) with NLDD causal interventions (Causal-TIC), with MCT geometric validation — extending TTS from per-step to continuous temporal coverage and addressing the probe inflation gap absent from all prior single-estimator approaches; (2) we map five independently discovered phenomena — pre-CoT encoding, Reasoning Horizon, Reasoning Theater, myopic planning, and thinking-answer gap — to distinguishable trajectory-shape signatures in the calibrated G*(t) curve, with a worked demonstration that shapes remain discriminable under probe inflation and formal statistical testing via FDA shape distance metrics, conditioned on task difficulty following the ICLR 2026 Workshop finding and Li et al.'s independent corroboration; (3) we derive the Temporal Information Fidelity (TIF) score with explicit robustness validation across probe architectures, layer selections, perturbation methods, normalization choices, and calibration methods, addressing the measurement sensitivity concern raised by Young (2603.20172); and (4) we include a Phase 0 pilot that simultaneously validates probe calibration methodology (null-probe, MCT concordance, MDL) and tests answer-content probe causal potency on reasoning models, with a detailed three-tier contingency plan (calibrated information-availability interpretation, reasoning-behavioral-mode probe pivot, dual-causal framework pivot) if causal potency fails.\\n\\nThe paper is focused around three core contributions: (a) Phase 0 pilot results providing novel empirical findings on probe calibration and causal potency in reasoning models; (b) the calibrated gap diagnostic G*(t) demonstrated on 4 models x 4 benchmarks with task-difficulty conditioning; (c) five-phenomenon mapping via trajectory shapes with FDA statistical tests. Robustness ablations and TIF validation form supporting sections; 671B validation and early-exit application are supplementary material.\",\n  \"revision_notes\": {\n    \"critical_changes\": [\n      \"ELEVATED GAP INFLATION TO TIER-1 AND ADDRESSED WITH THREE-LAYER CALIBRATION (Major): Reviewer identified that Chun et al.'s finding (probe accuracy does not equal computational readiness) means P(t) may be uniformly high, collapsing five-phenomenon signatures. This is now the central methodological contribution. We introduce: (a) null-probe calibration P*(t) = P(t) - P_null(t) following Hewitt & Liang (2019), producing a calibrated curve measuring excess answer information above correlative baseline; (b) MCT geometric validation following Chun et al. (2602.20338), checking whether detected information shows the transient geometric pulse characteristic of computationally relevant information; (c) MDL complexity check following Voita & Titov (2020), confirming signal structure. This calibration removes uniform inflation: if raw P(t) and P_null(t) are both high, P*(t) is low.\",\n      \"ADDED FORMAL TRAJECTORY-SHAPE ANALYSIS WITH WORKED EXAMPLE (Major): Reviewer argued five-phenomenon distinguishability was underspecified under the weak assumption. We now: (a) provide concrete worked example showing three phenomena produce distinguishable G*(t) trajectory shapes even with +0.3 correlative inflation because null-probe calibration removes uniform offset; (b) adopt six trajectory-shape features rather than absolute values; (c) cite shape-over-magnitude dissociation literature (2603.18940, 2602.06266, 2604.05655); (d) plan FDA shape distance metrics (Fisher-Rao distance) for formal statistical testing.\",\n      \"CITED LI ET AL. (2510.22362) MAPPING FAITHFUL REASONING (Minor): Concept Walk framework now cited throughout. Differentiated: concept directions (not answer-content probes), single domain (safety), single model (Qwen 3-4B), no continuous causal-contribution curve. Supports task-difficulty conditioning as independent corroboration.\",\n      \"EXPANDED PHASE 0 CONTINGENCY PLAN TO THREE TIERS (Major): Three ordered fallbacks if causal potency fails: (A) calibrated information-availability with MCT validation (preferred); (B) pivot to reasoning-behavioral-mode probes with confirmed causal potency on reasoning models (2510.04128); (C) dual-causal framework replacing probes with CMI-style activation patching. All preserve Causal-TIC, task-difficulty conditioning, phenomenon mapping, and TIF score.\",\n      \"TIGHTENED PAPER FOCUS (Minor): Core = Phase 0 pilot + calibrated gap diagnostic + difficulty-conditioned trajectory-shape signatures. Supporting = robustness ablations + TIF validation. Supplementary = 671B validation + early-exit + detailed calibration analysis.\",\n      \"ADDED PROBE CALIBRATION LITERATURE (Major): Hewitt & Liang (EMNLP 2019) for selectivity; Voita & Titov (EMNLP 2020) for MDL probing; Belrose et al. (NeurIPS 2023) for LEACE; Dobrzeniecka et al. (ACL 2025) for improved amnesic probing; Ravichander et al. (2020) for probe-task-relevance gap. Also trajectory-shape references: entropy trajectories (2603.18940), RQA dynamics (2602.06266), trajectory geometry (2604.05655).\",\n      \"ADDED REASONING-MODEL PROBING LITERATURE FOR CONTINGENCY (Minor): Internal States Before Wait (2510.04128) for causally potent reasoning-behavioral-mode probes on R1-Distill; From Reasoning to Answer (2509.23676) for activation patching on R1-Distill; I Have Covered All the Bases (2503.18878) for SAE feature taxonomies.\"\n    ],\n    \"what_stayed\": \"The five-phenomena unification thesis (now with formal trajectory-shape analysis), the dual-TIC concept (now with probe calibration), the NLDD and probe estimators, the four benchmarks (MMLU, GPQA-Diamond, GSM8K, AIME), the four target models (DeepSeek-R1-Distill 7B/14B/32B, QwQ-32B), the 671B validation subset, layer-selective caching, the TIF score concept, the synthetic arithmetic calibration check, the TTS cross-reference, the task-difficulty conditioning, the robustness ablations, and the diagnostic (thermometer) framing.\",\n    \"residual_risks\": [\n      \"TIER-1: Null-probe calibration may over-correct. If P_null(t) is high because hidden states contain rich correlative structure (not random noise), subtracting it may remove genuine answer information that happens to correlate with generic features. Mitigation: compare three calibration methods (shuffled-label, random-representation, MDL threshold) and report sensitivity; if methods disagree substantially, this reveals the calibration boundary is itself a finding about representation structure.\",\n      \"TIER-1: The TTS paper (Zhao et al. 2510.24941) tests on our exact models and benchmarks. If Causal-TIC (NLDD-based) and TTS (ATE-based) show near-identical patterns at step boundaries, the continuous-temporal-coverage novelty narrows. Mitigation: the calibrated dual-estimator gap and trajectory-shape mapping remain unique; within-step dynamics provide differentiation. The probe calibration methodology is a standalone contribution regardless.\",\n      \"TIER-1: MCT geometric validation may show discordance with P*(t) — the geometric pulse timing may not match the calibrated probe trajectory. If so, this reveals that even calibrated probes capture information not geometrically prepared for use. Mitigation: the discordance itself is a finding; proceed with Fallback A noting the specific gap between geometric readiness and probe decodability.\",\n      \"TIER-2: Task-difficulty conditioning may reveal that five phenomena are artefacts of different task types rather than a unified information dynamic. Would weaken 'unification' thesis to 'taxonomy indexed by difficulty' — less exciting but still publishable.\",\n      \"TIER-2: Measurement sensitivity: TIF may show high sensitivity to choices. Mitigation: plan ablations early, report sensitivity ranges.\",\n      \"TIER-2: NLDD interventions remain computationally expensive. MCT adds approximately 30 node-hours. May need subsampling for AIME long traces.\",\n      \"TIER-2: Field moving at 3+ papers per month. The probe calibration methodology, trajectory-shape analysis, and Phase 0 pilot providing novel empirical evidence are more defensible against concurrent work than the original uncalibrated framework.\"\n    ]\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce55f2c1-41cd-4a3c-bf89-8d116034c839",
  "isSidechain": false,
  "requestId": "req_011CbBuhpUTyCSa6MFz6y4mf",
  "type": "assistant",
  "uuid": "d53669bd-5afa-4389-bd57-4c8bb1cd495e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011Hrri5S9UDiJvJ1ujVBSN1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18776,
      "cache_read_input_tokens": 44357,
      "output_tokens": 14738,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18776,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14738,
          "cache_read_input_tokens": 44357,
          "cache_creation_input_tokens": 18776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18776
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

_source line 37 · 2026-05-19T12:20:34.873Z_

<details><summary>↩ Tool result · reported error · `toolu_01Gu2ErqazwpA2VAqpgPoNB2`</summary>

```text
Claude requested permissions to write to /tmp/revised_proposal_r5.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d53669bd-5afa-4389-bd57-4c8bb1cd495e",
  "isSidechain": false,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "type": "user",
  "uuid": "9fa68eda-7cb2-4445-9806-157bfb1adffc",
  "toolUseResult": "Error: Claude requested permissions to write to /tmp/revised_proposal_r5.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "d53669bd-5afa-4389-bd57-4c8bb1cd495e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 38 · 2026-05-19T12:20:34.959Z_

```json
{
  "parentUuid": "9fa68eda-7cb2-4445-9806-157bfb1adffc",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "201f5d92-6ecc-4390-8cde-5f8a0f58ff4c",
  "timestamp": "2026-05-19T12:20:34.959Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"The Probe-Intervention Gap: Diagnosing Chain-of-Thought Faithfulness v…",
  "leafUuid": "201f5d92-6ecc-4390-8cde-5f8a0f58ff4c",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise gap diagnostic discriminability and phenomenon distinguishability",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f"
}
```

---

### Tool call

_source line 41 · 2026-05-19T12:26:25.656Z_

<details open><summary>🔧 Tool call — Write · `toolu_01YDcbos9UJDFnWLfTKYvEAS`</summary>

```json
{
  "file_path": "/tmp/revised_proposal_r5.json",
  "content": "{\n  \"change_type\": \"major\",\n  \"title\": \"The Probe-Intervention Gap: Diagnosing Chain-of-Thought Faithfulness via Calibrated Dual-Estimator Temporal Information Decomposition\",\n  \"project_name\": \"cot_faithfulness_decomp\",\n  \"source\": \"web_research\",\n  \"level\": \"top-tier\",\n  \"target_venues\": [\n    \"ICLR 2027 (abstract: Sep 19, full paper: Sep 24, 2026; conference: Apr/May 2027 — primary target, 4 months from now)\",\n    \"ICML 2027 (full paper: Jan 29, 2027; conference: Jul 2027 — comfortable fallback if additional experiments needed)\"\n  ],\n  \"core_problem\": \"Multiple independent findings in 2025-2026 — Reasoning Horizon, pre-CoT answer encoding, Reasoning Theater, myopic planning, thinking-answer gap — all describe facets of the same underlying problem: models' chain-of-thought reasoning is partially or entirely decorative. While the CoT faithfulness literature has catalogued these phenomena (Jin et al.'s survey; FaithCoT-Bench at ICLR 2026) and several groups have measured temporal dynamics of individual signals, no work has unified these disparate phenomena under a single information-theoretic framework that explains WHY and WHEN each occurs. Crucially, recent work reveals that the relationship between faithfulness and task difficulty is not binary: CoT transitions from decorative to load-bearing as task difficulty increases ('Task Difficulty Shapes CoT Faithfulness,' ICLR 2026 Workshop), with error propagation ranging from 22% on MMLU to 41% on BBH. This difficulty gradient — detectable via hidden-state probes but resistant to single-direction steering ('readout rather than control') — demands a diagnostic framework that can characterize faithfulness along both temporal and difficulty dimensions. A critical methodological concern, raised by the probing literature (Hewitt & Liang 2019; Ravichander et al. 2020; Chun et al. 2602.20338) and reinforced by Yuan et al. (2605.09502), is that probe accuracy on hidden states captures correlative/epiphenomenal information rather than information the model actively uses — probe accuracy does not equal computational readiness. This means any probe-based diagnostic must address the gap inflation problem: if probes detect uniformly high 'information availability' regardless of actual faithfulness, the diagnostic collapses. The closest precedents — Kudo et al.'s (EACL 2026) probing + activation patching on synthetic arithmetic, the CMI framework's layerwise causal audit on ~50 examples, Zhao et al.'s (2510.24941) True Thinking Score providing per-step causal contribution on AIME/MATH, Furuya & Tanimura's (2605.01853) training-free StALT trajectory statistic, and Li et al.'s (2510.22362, NeurIPS 2025 MechInterp Workshop) Concept Walk tracking temporal concept-direction alignment — each capture one dimension of the problem but none provides a calibrated dual-estimator framework that jointly measures internal information and causal contribution across the full CoT timeline on natural benchmarks, with explicit controls for probe inflation.\",\n  \"opportunity\": \"The field has independently produced three complementary measurement paradigms: (1) probe-based approaches revealing what the model internally represents at each CoT position (David 2511.14773: correctness decodable at t=4 tokens; Cox et al. 2603.01437: pre-CoT probes at >0.9 AUC with causal validation via steering on instruction-tuned models up to 9B; Esakkiraja et al. 2604.01202: pre-generation probes with >90% AUROC; Furuya & Tanimura 2605.01853: training-free StALT separating correct from incorrect trajectories; Li et al. 2510.22362: Concept Walk tracking concept-direction alignment per step, finding easy to decorative, hard to faithful), (2) intervention-based approaches measuring what the CoT text causally contributes (Ye et al. 2602.11201: NLDD reveals Reasoning Horizon at 70-85%; Zhao et al. 2510.24941: True Thinking Score provides per-step ATE on AIME/MATH/AMC/CommonsenseQA, finding only 2.3% of AIME steps have TTS>=0.7; Basu & Chakraborty 2603.22816: decorative/scaffolding/genuine taxonomy), and (3) diagnostic approaches characterizing CoT pathologies (Liu et al. 2602.13904: text-level metrics for rationalization/encoded/internalized reasoning via model organisms; 'Task Difficulty Shapes CoT Faithfulness' ICLR 2026 Workshop: difficulty-dependent faithfulness gradient). Two prior works have combined probing with causal interventions on the same instances: Kudo et al. (2412.01113, EACL 2026) train linear probes and perform activation patching across arithmetic CoT; the CMI framework (2602.03994) measures CoT-mediated causal influence via layerwise patching. However, neither provides: (a) full temporal-position coverage across CoT on natural benchmarks, (b) a mapping to the five named faithfulness phenomena, (c) a standalone instance-level diagnostic score, (d) systematic multi-model comparison on realistic reasoning tasks, (e) robustness validation across measurement methodologies — a critical gap highlighted by Young's (2603.20172) finding that faithfulness measurements are classifier-sensitive (inter-classifier kappa as low as 0.06), or (f) controls for probe inflation — the well-documented problem that probe accuracy captures correlative information not actively used by the model (Hewitt & Liang 2019; Voita & Titov 2020; Chun et al. 2602.20338). The opportunity is to extend the probe-intervention combination paradigm to a calibrated dual-estimator Temporal Information Curve (TIC) framework producing a 2D faithfulness signal — the gap between calibrated probe-estimated internal information and intervention-estimated causal contribution — on natural benchmarks at scale, with explicit probe inflation controls and robustness validation.\",\n  \"landscape\": \"**Probe-intervention combinations (closest prior work).** Kudo et al. (2412.01113, EACL 2026) train per-position linear probes on hidden states and validate with sliding-window activation patching on 9 models across synthetic multi-step arithmetic. They find CoT IS faithful for arithmetic but explicitly note their synthetic setting may not generalize to 'more realistic reasoning tasks in natural language.' The CMI framework (2602.03994) introduces the CoT Mediation Index via layerwise activation patching across Phi, Qwen, and DialoGPT on StrategyQA (20 examples), TruthfulQA (10), and GSM8K (20), identifying 'bypass regimes' where CMI is approximately 0. Both are complementary precursors.\\n\\n**Per-step causal contribution (direct Causal-TIC precursor).** Zhao et al. (2510.24941, Oct 2025, revised Apr 2026) introduce the True Thinking Score (TTS), measuring per-step causal contribution via text-level perturbation (numerical offsets preserving grammar) and ATE computation. On DeepSeek-R1-Distill-Qwen-7B/14B/Llama-8B across AIME, MATH, AMC, CommonsenseQA, they find only 2.3% of AIME steps have TTS>=0.7. TTS also extracts a 'TrueThinking direction' from hidden states for steering (53.6-91.2% flip rates). TTS is a direct precursor to our Causal-TIC component. Key differentiators: TTS operates at discrete step granularity (not continuous temporal), is a single-estimator metric (no calibrated probe gap), uses text-level perturbation (vs. our NLDD logit degradation), and does not map to the five faithfulness phenomena or provide an instance-level diagnostic score grounded in the probe-intervention divergence. Our framework extends TTS's causal measurement from per-step to continuous temporal coverage and pairs it with the calibrated Probe-TIC for the gap diagnostic unavailable from either estimator alone.\\n\\n**Training-free temporal hidden-state dynamics (concurrent work adjacent to Probe-TIC).** Furuya & Tanimura (2605.01853, May 2026) introduce StALT (Spatiotemporal Amplitude of Latent Transition), a training-free trajectory statistic that separates correct from incorrect reasoning trajectories by tracking hidden-state transitions across decoding steps and layers. Tested on GSM8K, MATH-500, and GPQA. StALT is conceptually adjacent to our Probe-TIC in tracking temporal hidden-state evolution. Key differentiators: StALT targets correctness separation (not faithfulness diagnosis), is training-free (vs. our trained answer-content probes targeting specific answer information), lacks a causal intervention component (no gap diagnostic), and does not map to faithfulness phenomena.\\n\\n**Temporal concept-direction tracking (concurrent work supporting task-difficulty conditioning).** Li et al. (2510.22362, NeurIPS 2025 MechInterp Workshop) introduce Concept Walk, which projects each reasoning step's activations onto concept directions (learned via difference-of-means from contrastive data) and tracks temporal evolution across CoT. On Qwen 3-4B in the safety domain, they find easy cases produce only transient activation shifts under perturbation (decorative CoT), while hard cases produce sustained, structured shifts (faithful CoT). This directly supports our task-difficulty conditioning dimension. Key differentiators from our framework: Concept Walk uses concept directions (not answer-content probes), operates in a single domain (safety, not reasoning benchmarks), lacks a separate causal-contribution curve (perturbation is used for classification, not as a continuous C(t) estimator), tests on one small model (Qwen 3-4B), and does not derive an instance-level diagnostic score from the probe-intervention gap.\\n\\n**Latent-trajectory signals for efficiency.** Vilas et al. (2510.10494, ICLR 2026) define three latent-trajectory signals — net change, cumulative change, and aligned change — tracking hidden-state evolution across 500-token segments. On DeepSeek-R1-Distill-Qwen-14B, Phi-4-Reasoning-Plus, and Qwen3-14B across GPQA Diamond, AIME 2025, and TSP, they achieve 14-70% token savings and +2.6% accuracy gains. Focuses on efficiency, not faithfulness. Adjacent methodology but orthogonal goal.\\n\\n**The diagnostic-not-causal challenge.** Yuan et al. (2605.09502, May 2026) show that probes detecting trace correctness achieve 0.95 AUROC but four interventions fail, concluding error representations are 'fundamentally different from editable factual knowledge representations.' Cox et al. (2603.01437) demonstrate that answer-content probe directions are causally potent on instruction-tuned models: steering flips >50% of answers. However, Cox et al.'s validation is restricted to binary classification tasks on models up to 9B parameters, and they explicitly note that for reasoning models, they find 'some success using probes to linearly decode the final answer, but little success steering to change it.' This means the causal potency of answer-content probes on reasoning models (our target model class) is NOT yet established. We therefore introduce probe calibration methodology to address the inflation problem.\\n\\n**The probe inflation problem.** The probing literature has thoroughly documented that high probe accuracy does not entail task relevance. Hewitt & Liang (2019) show that MLP probes achieve only 4.5 selectivity on POS tagging (97.3% accuracy vs. 92.8% on shuffled-label controls). Ravichander et al. (2020) demonstrate that 'even when models cannot use a linguistic property to perform the task, the property can be reliably recovered from neural representations.' Voita & Titov (2020) show that MDL-based probing reveals that standard accuracy does not substantially favor pretrained over random representations. Most directly, Chun et al. (2602.20338) apply Manifold Capacity Theory to CoT reasoning and find that geometric separability peaks transiently as a 'geometric pulse' just before computation and compresses rapidly afterward, while probe accuracy remains high long after computation is complete. This provides direct evidence that probe accuracy overestimates information availability during reasoning. We address this via null-probe calibration and MCT geometric validation.\\n\\n**Trajectory-shape analysis.** A separate line of work demonstrates that temporal trajectory shapes carry diagnostic information beyond absolute values. The entropy trajectory paper (2603.18940) shows a 'shape-over-magnitude dissociation': monotonicity of entropy decrease predicts reasoning reliability regardless of absolute entropy levels (+5.8pp at 73.7% coverage). RQA analysis of reasoning dynamics (2602.06266) shows that temporal features (determinism variability, laminarity slope) outperform aggregate statistics for complexity classification (36.94% vs. 28.97%). Microsoft's trajectory geometry work (2604.05655) shows correct vs. incorrect reasoning paths diverge geometrically at late steps (0.852 AUC from shape features vs. 0.649 from step-count baselines). This literature supports our core claim that even if P(t) is uniformly inflated, the trajectory shape of the gap G(t) can distinguish faithfulness phenomena.\\n\\n**CoT pathology diagnostics.** Liu et al. (2602.13904, Feb 2026) propose text-level, computationally inexpensive, task-agnostic metrics for three CoT pathologies: Necessity (rationalization), Paraphrasability (encoded reasoning), and Substantivity (internalized reasoning), validated on model organisms. Complementary to ours: purely text-level, no hidden states, categorical per-pathology metrics.\\n\\n**Measurement sensitivity.** Young (2603.20172, Mar 2026) shows faithfulness measurements are classifier-sensitive: inter-classifier kappa as low as 0.06, with up to 30.6 percentage-point divergence across three classifiers on 10,276 traces from 12 models.\\n\\n**Task-difficulty moderation of faithfulness.** 'Task Difficulty Shapes CoT Faithfulness' (ICLR 2026 Workshop) demonstrates that CoT transitions from decorative to load-bearing as task difficulty increases. Li et al. (2510.22362) independently corroborate this: Concept Walk shows easy cases produce transient/decorative patterns while hard cases produce sustained/faithful patterns.\\n\\n**Probe-based temporal measurement.** Qian et al. (2506.02867, NeurIPS 2025) compute per-token HSIC. David (2511.14773) shows correctness decodable at t=4 tokens. Zhang et al. (2504.05419) probe DeepSeek-R1-Distill variants for correctness, achieving >0.7 AUC. Lewis-Lim et al. (2508.19827, EMNLP 2025) reveal flat (rationalization) vs. increasing (genuine reasoning) confidence patterns. Mirtaheri & Belkin (2603.17199) show pre-generation probes match full-CoT monitors. Esakkiraja et al. (2604.01202) show pre-generation probes predict tool-calling at >90% AUROC.\\n\\n**Intervention-based causal measurement.** Ye et al. (2602.11201) introduce NLDD, revealing Reasoning Horizon at 70-85%. Basu & Chakraborty (2603.22816) propose taxonomy via step ablation. Somov et al. (2603.16475) show up to 60% failure to update. FACT-E (2604.10693, ACL Findings 2026) uses controlled perturbations.\\n\\n**Probing and steering faithfulness.** Occhipinti et al. (ICLR 2026 LIT Workshop) demonstrate faithfulness encoded as linear directions; probing F1 90-100%; steering 46% recovery with <5% collateral.\\n\\n**Probing reasoning models specifically.** Internal States Before Wait (2510.04128) trains crosscoders on DeepSeek-R1-Distill-Llama-8B, identifying features for backtracking, uncertainty, knowledge recall, and double-checking, with causal interventions confirmed. From Reasoning to Answer (2509.23676) uses activation patching on R1-Distill variants, finding reasoning token perturbations flip outputs with NLD up to 0.5. These inform our contingency plan.\\n\\n**Geometric and information-theoretic approaches.** Chun et al. (2602.20338) apply MCT revealing transient geometric pulses (critical for our probe calibration). Alvarez & Baheri (2605.13772) detect step-level hallucination via transport geometry. Ton et al. (ICML 2025, 2411.11984) define per-step information gain. Anwar et al. (2602.18297) decompose monitorability into information gap + elicitation error.\\n\\n**Benchmarks, surveys, and early-exit methods.** FaithCoT-Bench (ICLR 2026). Jin et al.'s survey (ARR for ACL 2026). Young (2603.26410). 'Lie to Me' (2603.22582). Reasoning Theater (2603.05488). ESTAR (2602.10004). DTSR (2604.06787). NEAT (2602.02010). CoDE-Stop (2604.04930). FRIT (2509.13334).\\n\\n**What remains open.** No extant framework provides: (1) a full-timeline calibrated dual-estimator curve combining answer-content probes with causal interventions on natural benchmarks at scale, with explicit controls for probe inflation; (2) a systematic mapping of five phenomena to distinguishable trajectory-shape signatures demonstrated to be robust under the weaker information-availability assumption via formal shape analysis; (3) an instance-level diagnostic score derived from the calibrated probe-intervention gap with explicit robustness validation; or (4) a principled account of how the probe-intervention gap behaves differently on instruction-tuned vs. reasoning models. TTS provides per-step causal contribution (single-estimator, text-level); StALT provides temporal hidden-state correctness signals (single-estimator, no causal component); Concept Walk provides temporal concept-direction alignment (single model, single domain, no continuous causal curve); Vilas et al. provide latent-trajectory efficiency signals (no faithfulness connection); Liu et al. provide text-level pathology diagnostics (no hidden states). The calibrated dual-estimator gap — jointly measuring excess internal information (above a null-probe baseline) and causal contribution across the full timeline — remains the unique contribution.\",\n  \"inspired_by\": \"The convergence of five observations: (a) Kudo et al.'s demonstration that probe+intervention combination is feasible and informative on synthetic arithmetic, with their explicit call for natural-task extension; (b) Zhao et al.'s (2510.24941) TTS demonstrating per-step causal contribution measurement at scale on our exact target benchmarks (AIME, MATH), establishing the causal-contribution paradigm we extend to continuous temporal coverage with the dual-estimator gap; (c) the finding from both Cox et al. (2603.01437) on instruction-tuned models and the 'Task Difficulty' workshop paper that probes are diagnostic ('readout') rather than interventional ('control'), clarifying the Probe-TIC interpretation; (d) Young's (2603.20172) demonstration that faithfulness measurements are classifier-sensitive, motivating explicit robustness ablation; (e) Chun et al.'s (2602.20338) discovery that probe accuracy does not equal computational readiness — geometric separability peaks transiently while probe accuracy stays flat — which motivates our null-probe calibration methodology and the adoption of trajectory-shape features rather than absolute probe values.\",\n  \"approach\": \"Define a calibrated dual-estimator Temporal Information Curve (TIC) framework that diagnoses chain-of-thought faithfulness at each token position t via two complementary signals, with explicit controls for probe inflation:\\n\\n**(a) Calibrated Probe-TIC P*(t)**: We address the probe inflation problem — the well-documented finding that probe accuracy captures correlative/epiphenomenal information not actively used by the model (Hewitt & Liang 2019; Ravichander et al. 2020; Chun et al. 2602.20338) — via a three-layer calibration strategy:\\n\\n(i) Null-probe normalization. For each layer and position, train a parallel 'null probe' on shuffled answer labels (random assignment of answer identities to hidden states). Define the calibrated Probe-TIC as P*(t) = P(t) - P_null(t), measuring excess answer information above what is extractable from correlative features alone. This follows the selectivity methodology of Hewitt & Liang (2019), adapted to our temporal setting: selectivity is computed at each position t, producing a calibrated curve rather than a single aggregate number. High P*(t) means the model's hidden states at position t encode answer information beyond what is attributable to correlative features.\\n\\n(ii) MCT geometric validation. On a subset of 500 examples per benchmark, compute Manifold Capacity Theory (Chun et al. 2602.20338) separability alongside probe accuracy at each position. MCT measures intrinsic geometric readiness for computation (the 'geometric pulse') independent of probe training, providing a probe-free check on whether the information P*(t) detects is geometrically organized for use. If MCT separability and P*(t) show concordant temporal trajectories, the probe captures information that is at least geometrically prepared; if MCT shows the characteristic transient pulse while P*(t) remains flat/high, this diagnoses the specific type of inflation present.\\n\\n(iii) MDL complexity check. Following Voita & Titov (2020), compute minimum description length for probe labels at each position. If genuine answer information requires less codelength than random labels at position t, the signal is structured; if codelengths are comparable, the signal is noise-like.\\n\\nWe probe for answer content (which answer option / numerical value the model will produce) using linear probes trained on 3-5 selected layers. On instruction-tuned models, Cox et al. (2603.01437) demonstrate such probes are causally potent (steering flips >50% of answers). However, Cox et al.'s validation is limited to binary tasks on models at most 9B, and they explicitly report that reasoning models resist steering. We therefore interpret the calibrated Probe-TIC P*(t) as measuring excess information availability — what the model internally represents at position t above a correlative baseline — rather than assuming causal potency. This interpretation is independently supported by the 'Task Difficulty Shapes CoT Faithfulness' finding that probes are 'readout rather than control,' by Yuan et al.'s (2605.09502) demonstration that correctness probes are diagnostic-not-causal, and is consistent with Furuya & Tanimura (2605.01853) and Li et al.'s (2510.22362) finding that hidden-state temporal signals are diagnostic of reasoning quality.\\n\\n**(b) Causal-TIC C(t)**: Causal contribution of CoT text up to position t to the answer via NLDD-style interventions (corrupting CoT segments and measuring logit degradation). This extends the single-model NLDD paradigm (Ye et al. 2602.11201) to systematic multi-model comparison with continuous temporal coverage, and provides a continuous temporal generalization of the per-step TTS metric (Zhao et al. 2510.24941). Where TTS applies text-level perturbation at discrete step boundaries with ATE computation, our Causal-TIC applies NLDD logit degradation at each token position, yielding a continuous curve that captures within-step dynamics invisible to TTS. Critically, C(t) is not subject to the probe inflation problem: it measures behavioral change under intervention, not decodability from representations.\\n\\n**The Calibrated Faithfulness Gap as a Diagnostic Signal.** The core diagnostic is G*(t) = P*(t) - C(t), where P*(t) is null-probe-calibrated. This calibration fundamentally changes the gap's interpretation:\\n- G*(t) approximately 0 means excess internal information (above correlative baseline) and CoT causal contribution are aligned — a necessary condition for faithfulness.\\n- G*(t) much greater than 0 means the model possesses answer information beyond correlative features that is not causally contributed by CoT text — genuine information excess, not merely probe inflation.\\n- G*(t) less than 0 would indicate CoT contributes more than the model's calibrated internal information suggests — potentially indicating information assembled during reasoning.\\n- Because P*(t) is calibrated against the null probe, uniform probe inflation is removed. If raw P(t) is uniformly high but P_null(t) is similarly high, the calibrated P*(t) is low, correctly reflecting that the 'information' is correlative rather than answer-specific.\\n\\n**Trajectory-Shape Analysis for Phenomenon Distinguishability.** We diagnose phenomena primarily from trajectory shapes (temporal derivatives, curvature, onset timing) rather than absolute gap values. This shape-over-magnitude approach is empirically validated: the entropy trajectory literature (2603.18940) demonstrates that 'whether entropy decreases at every step, not how much it drops, predicts correctness,' and RQA analysis (2602.06266) shows temporal shape features outperform aggregate statistics for reasoning complexity classification (36.94% vs. 28.97%).\\n\\nConcretely, we extract six shape features from the calibrated dual-TIC:\\n(i) P*(0) level — initial excess information at CoT onset, after null-probe calibration. Detects pre-CoT encoding.\\n(ii) dP*/dt trajectory — rate of excess information accumulation. Flat indicates front-loaded; positive indicates genuine acquisition.\\n(iii) C(t) plateau onset t* — captures the Reasoning Horizon.\\n(iv) G*(t) trajectory shape — curvature and monotonicity of the calibrated gap. Distinguishes Reasoning Theater (monotonically widening) from genuine reasoning (near-zero throughout) from pre-CoT encoding (large constant).\\n(v) dC/dt locality — short- vs. long-range autocorrelation in causal contribution gradient. Short-range only captures myopic planning.\\n(vi) P*-C divergence at thinking/answer boundary — spike in G*(t) at the interface detects the thinking-answer gap.\\n\\n**Worked Example: Distinguishability Under Probe Inflation.** Consider three phenomena with raw P(t) uniformly inflated by +0.3 due to correlative information:\\n\\nPre-CoT encoding: Raw P(t) = 0.9 from t=0 (0.6 real + 0.3 correlative), flat throughout. Null probe P_null(t) approximately 0.3 uniformly. Calibrated P*(t) approximately 0.6 from t=0, flat. C(t) approximately 0.1 throughout. G*(t) approximately 0.5, constant. Shape: flat P*(t), flat C(t), large constant gap. dP*/dt approximately 0.\\n\\nReasoning Theater: Raw P(t) = 0.7 at t=0, rises to 1.0 during CoT. Null probe P_null(t) approximately 0.3 with slight increase. Calibrated P*(t) approximately 0.1 at t=0, rises to approximately 0.7. C(t) approximately 0.05 throughout. G*(t) starts near 0, grows monotonically. Shape: rising P*(t), flat C(t), widening gap. dP*/dt > 0, dC/dt approximately 0.\\n\\nGenuine reasoning: Raw P(t) = 0.6 at t=0, rises to 1.1 through reasoning. Null probe P_null(t) approximately 0.3. Calibrated P*(t) approximately 0.0 at t=0, rises to approximately 0.8. C(t) tracks P*(t) with small lag. G*(t) approximately 0 throughout. Shape: rising P*(t) AND rising C(t), near-zero gap.\\n\\nThese three phenomena produce distinguishable G*(t) trajectory shapes even though raw P(t) is inflated by the same +0.3 in all cases. The formal statistical framework for comparing these trajectory shapes is provided by Functional Data Analysis (Srivastava & Klassen 2016; Marron & Dryden 2021), which separates amplitude variation from phase variation via elastic registration. We apply FDA shape distance metrics (Fisher-Rao distance) to formally test whether G*(t) trajectories cluster by phenomenon type.\\n\\n**Task-Difficulty Conditioning.** Following the 'Task Difficulty Shapes CoT Faithfulness' finding and Li et al.'s (2510.22362) independent corroboration (easy to decorative, hard to faithful), we analyze dual-TIC signatures stratified by task difficulty (using model confidence on first pass as a difficulty proxy). We predict: (a) easy instances show high P*(0) with flat C(t) (pre-CoT encoding / decoration); (b) moderate instances show Reasoning Horizon signatures (C(t) plateau at 70-85%); (c) hard instances show increasing P*(t) and C(t) trajectories (genuine reasoning).\\n\\n**Pilot Validation (Phase 0): Probe Calibration and Causal Potency.** Before running full experiments, we conduct a targeted pilot on 500 examples across MMLU (4-choice) and GSM8K (numerical) using DeepSeek-R1-Distill-Qwen-7B. Three objectives:\\n\\n(i) Null-probe calibration validation: Verify that P*(t) = P(t) - P_null(t) effectively removes correlative inflation. Success criterion: P_null(t) shows high absolute accuracy (demonstrating inflation is real) but P*(t) shows meaningful variance across instances and time (demonstrating calibration reveals genuine structure).\\n\\n(ii) MCT geometric concordance: Compute MCT separability alongside P*(t) at 10 temporal positions. Test concordance.\\n\\n(iii) Causal potency test: Test steering along answer-content probe directions at varying strengths on reasoning models for multi-choice tasks.\\n\\n**Detailed Contingency Plan (if Phase 0 probes show no causal potency):**\\n\\nFallback A (preferred): Calibrated information-availability interpretation with MCT validation. If P*(t) shows meaningful temporal structure after null-probe calibration AND MCT geometric validation shows concordant trajectories, the Probe-TIC captures information that is at least geometrically organized for computation, even if not directly steerable. G*(t) measures 'information that is geometrically available but not utilized by CoT text.' The thermometer analogy holds — a thermometer that accurately tracks fever without curing it is still medically valuable.\\n\\nFallback B: Pivot to reasoning-behavioral-mode probes. If P*(t) shows little temporal structure even after calibration, we pivot from answer-content probes to probing for reasoning behavioral modes — backtracking, uncertainty, verification, knowledge recall — which have confirmed causal potency on reasoning models (Internal States Before Wait, 2510.04128). The gap G*(t) then captures divergence between internal reasoning commitment and overt CoT causal contribution.\\n\\nFallback C: Dual-causal framework. Replace Probe-TIC with a second causal measure (e.g., CMI-style activation patching), yielding a causal-causal framework. Eliminates probe inflation concern entirely but loses computational efficiency.\\n\\nIn all three scenarios, Causal-TIC, task-difficulty conditioning, five-phenomenon mapping via trajectory shapes, and TIF score are preserved.\\n\\n**Robustness Ablations.** Motivated by Young (2603.20172): (a) probe architecture (linear vs. 2-layer MLP) with selectivity scores; (b) layer selection (best-3 vs. best-5 vs. all layers); (c) NLDD perturbation method (Gaussian corruption vs. token replacement vs. segment shuffling); (d) gap normalization (raw difference vs. ratio vs. area-under-curve); (e) null-probe calibration method (shuffled-label vs. random-representation baseline vs. MDL complexity threshold). Report sensitivity ranges.\\n\\n**Experiments.** Core experiments target DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Qwen-14B, DeepSeek-R1-Distill-Qwen-32B, and QwQ-32B across four benchmarks (MMLU, GPQA-Diamond, GSM8K, AIME), with a targeted validation run on DeepSeek-R1-671B (500-example subset, 3 layers). Layer-selective activation caching (5 layers from pilot study on 7B) keeps storage at approximately 3-5 TB. Calibration checks: (a) Kudo et al.'s synthetic arithmetic as control expecting G*(t) approximately 0; (b) cross-reference TTS values from Zhao et al. on overlapping benchmarks; (c) cross-reference MCT geometric pulses.\\n\\n**Paper Focus (Tightened).** Core paper: (1) Phase 0 pilot results on probe calibration and causal potency — novel empirical contribution regardless of outcome; (2) Calibrated gap diagnostic G*(t) demonstrated on 4 models x 4 benchmarks with task-difficulty conditioning; (3) Five-phenomenon mapping via trajectory shapes with FDA statistical tests. Supporting sections: robustness ablations across 5 dimensions; TIF score validation. Supplementary: 671B validation; early-exit criterion; detailed calibration analysis.\\n\\n**Primary Output: Temporal Information Fidelity (TIF) Score.** Instance-level diagnostic from normalized area under calibrated gap curve G*(t). Benchmarked against FaithCoT-Bench annotations and cross-validated against Liu et al.'s text-level pathology metrics.\\n\\n**Secondary Output: Causal Sufficiency Stopping Criterion.** Supplementary early-exit criterion from Causal-TIC inflection points.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"650 H100-hours (300 for distilled-model inference with layer-selective activation caching on 4 models x 4 datasets + synthetic arithmetic control; 150 for NLDD causal interventions across 10-20 perturbation passes per model; 50 for probe training, null-probe calibration, Phase 0 pilot (probe + MCT + MDL), and TIF-FaithCoT-Bench validation; 50 for robustness ablations across 5 measurement dimensions; 50 for MCT geometric validation on 500-example subsets; 50 for 671B validation subset on 8xH100 node)\",\n      \"timeline\": \"4 months (2 researchers: 2 weeks Phase 0 pilot including null-probe calibration, MCT concordance, MDL validation, and causal potency test on 7B, plus probing pipeline via nnsight, layer-selection study, and synthetic arithmetic calibration; 7 weeks core dual-estimator experiments across 4 models x 4 datasets with task-difficulty stratification and null-probe calibration at each position; 3 weeks TIF validation against FaithCoT-Bench plus Liu et al. metrics plus phenomenon mapping via FDA trajectory-shape analysis; 2 weeks robustness ablations plus TTS cross-reference plus MCT concordance analysis; 2 weeks writing)\",\n      \"estimated_gpu_cost\": \"$1,625 (at approximately $2.50/H100-hr avg via RunPod/Lambda spot pricing, May 2026 rates)\",\n      \"storage\": \"3-5 TB for layer-selective activation caching (5 layers per model, fp16); reducible to approximately 1.5 TB via PCA to 25% dimensionality\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"550 H100-hours (Claude accelerates probing pipeline, null-probe calibration implementation, MCT computation, analysis scripts, reducing iteration overhead approximately 15%)\",\n      \"timeline\": \"3.5 months (1 researcher + Claude: 2 weeks Phase 0 pilot plus null-probe calibration plus MCT setup plus pipeline; 6 weeks core experiments with difficulty stratification and calibration; 2 weeks TIF validation plus phenomenon mapping plus robustness ablations plus FDA shape analysis; 2 weeks TTS cross-reference plus paper drafting)\",\n      \"claude_api_cost\": \"$450 (code generation for probing/null-probe/MCT/intervention/FDA/ablation pipelines, automated result analysis, paper drafting; approximately 90M input + 22M output tokens via Sonnet 4.6)\",\n      \"estimated_gpu_cost\": \"$1,375\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"550 H100-hours (same computational footprint; experiment is GPU-bound not code-bound)\",\n      \"timeline\": \"3 months (Claude drives experiment design, implementation, analysis, and full draft; human provides weekly steering and final review)\",\n      \"claude_api_cost\": \"$900 (extensive pipeline generation, null-probe calibration sweep, MCT implementation, FDA trajectory analysis, robustness ablation design, automated result interpretation, full paper draft; approximately 180M input + 45M output tokens)\",\n      \"estimated_gpu_cost\": \"$1,375\",\n      \"speed_bottleneck\": \"NLDD interventions on 32B models require multiple forward passes (10-20 per example) at approximately 15 tok/s on 2xH100; approximately 250 node-hours for 20K examples across 4 datasets plus arithmetic control dominate wall-clock time. MCT computation adds approximately 30 node-hours for geometric validation on 500-example subsets across 4 models. 671B validation subset requires 8xH100 node. Robustness ablations across 5 dimensions add approximately 60 node-hours.\"\n    }\n  },\n  \"key_references\": [\n    \"LLMs Faithfully and Iteratively Compute Answers During CoT: A Systematic Analysis With Multi-step Arithmetics (Kudo et al., EACL 2026, arXiv 2412.01113) — probing + activation patching on same instances for synthetic arithmetic; finds CoT IS faithful; explicitly calls for natural-task extension\",\n    \"When Chains of Thought Don't Matter: Causal Bypass in Large Language Models (Sathyanarayanan et al., arXiv 2602.03994) — CoT Mediation Index via layerwise activation patching; identifies bypass regimes; small scale, no temporal resolution\",\n    \"Hidden Error Awareness in Chain-of-Thought Reasoning: The Signal Is Diagnostic, Not Causal (Yuan et al., arXiv 2605.09502, May 2026) — correctness probes at 0.95 AUROC but four interventions fail; critical context for probe interpretation and thermometer framing\",\n    \"Can Aha Moments Be Fake? Identifying True and Decorative Thinking Steps in Chain-of-Thought (Zhao et al., arXiv 2510.24941, Oct 2025, revised Apr 2026) — True Thinking Score via text-level perturbation + ATE; only 2.3% of AIME steps have TTS>=0.7; direct Causal-TIC precursor\",\n    \"Spatiotemporal Hidden-State Dynamics as a Signature of Internal Reasoning in Large Language Models (Furuya & Tanimura, arXiv 2605.01853, May 2026) — StALT training-free temporal trajectory statistic; concurrent work adjacent to Probe-TIC\",\n    \"Mapping Faithful Reasoning in Language Models (Li et al., arXiv 2510.22362, NeurIPS 2025 MechInterp Workshop) — Concept Walk projects reasoning steps onto concept directions; finds easy to decorative, hard to faithful; supports task-difficulty conditioning; different methodology (concept directions not answer-content probes) and domain (safety not reasoning benchmarks), no continuous causal-contribution curve\",\n    \"Task Difficulty Shapes Chain-of-Thought Faithfulness (ICLR 2026 Workshop) — CoT transitions from decorative to load-bearing with difficulty; probes are 'readout rather than control'; independently validates diagnostic framing\",\n    \"Diagnosing Pathological Chain-of-Thought in Reasoning Models (Liu et al., arXiv 2602.13904, Feb 2026) — text-level metrics for three CoT pathologies; complementary text-level diagnostic\",\n    \"Measuring Faithfulness Depends on How You Measure: Classifier Sensitivity in LLM Chain-of-Thought Evaluation (Young, arXiv 2603.20172, Mar 2026) — inter-classifier kappa as low as 0.06; motivates robustness ablations\",\n    \"Emergent Manifold Separability during Reasoning in LLMs (Chun et al., arXiv 2602.20338, Feb 2026) — MCT reveals transient geometric pulses; probe accuracy does not equal computational readiness; critical for probe calibration methodology\",\n    \"Tracing the Traces: Latent Temporal Signals for Efficient and Accurate Reasoning (Vilas et al., ICLR 2026, arXiv 2510.10494) — latent-trajectory signals for reasoning efficiency; adjacent methodology\",\n    \"Probing and Steering Chain-of-Thought Unfaithfulness in Language Models (Occhipinti et al., ICLR 2026 LIT Workshop) — faithfulness encoded as linear directions; probing F1 90-100%; steering 46% recovery\",\n    \"Designing and Interpreting Probes with Control Tasks (Hewitt & Liang, EMNLP 2019) — selectivity scores via shuffled-label control probes; foundational methodology for null-probe calibration\",\n    \"Information-Theoretic Probing with Minimum Description Length (Voita & Titov, EMNLP 2020, arXiv 2003.12298) — MDL-based probing; codelength as alternative to accuracy; methodology for MDL complexity check\",\n    \"LEACE: Perfect Linear Concept Erasure in Closed Form (Belrose et al., NeurIPS 2023, arXiv 2306.03819) — provable erasure for amnesic probing validation\",\n    \"Improving Causal Interventions in Amnesic Probing with Mean Projection or LEACE (Dobrzeniecka et al., ACL Findings 2025, arXiv 2506.11673) — LEACE and Mean Projection for improved amnesic probing\",\n    \"Shape-over-magnitude dissociation in entropy trajectories (arXiv 2603.18940, 2026) — entropy trajectory monotonicity predicts reasoning reliability regardless of absolute levels; validates trajectory-shape analysis\",\n    \"Is My Model Mind Blurting? Recurrence Quantification Analysis of Reasoning Dynamics (arXiv 2602.06266, Feb 2026) — temporal RQA shape features outperform aggregate statistics for complexity classification\",\n    \"LLM Reasoning as Trajectories: Step-Specific Representation Geometry (arXiv 2604.05655, Apr 2026, Microsoft) — trajectory shape features achieve 0.852 AUC vs. 0.649 from step-count baselines\",\n    \"Internal States Before Wait Modulate Reasoning Patterns (arXiv 2510.04128, 2025) — crosscoders on R1-Distill identify reasoning features with causal interventions confirmed; informs contingency plan\",\n    \"FACT-E: Causality-Inspired Evaluation for Trustworthy Chain-of-Thought Reasoning (Sun et al., ACL Findings 2026, arXiv 2604.10693)\",\n    \"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (Alvarez & Baheri, arXiv 2605.13772, May 2026)\",\n    \"Breaking the Chain: A Causal Analysis of LLM Faithfulness to Intermediate Structures (Somov et al., arXiv 2603.16475)\",\n    \"When Is Thinking Enough? Early Exit via Sufficiency Assessment (Xiang et al., arXiv 2604.06787)\",\n    \"FRIT: Using Causal Importance to Improve Chain-of-Thought Faithfulness (Swaroop et al., arXiv 2509.13334)\",\n    \"Demystifying Reasoning Dynamics with Mutual Information (Qian et al., NeurIPS 2025, arXiv 2506.02867)\",\n    \"Temporal Predictors of Outcome in Reasoning Language Models (David, arXiv 2511.14773, Nov 2025)\",\n    \"Reasoning Models Know When They're Right: Probing for Self-Verification (Zhang et al., arXiv 2504.05419, Apr 2025) — probes on DeepSeek-R1-Distill achieve >0.7-0.9 AUC for correctness; informs alternative probe targets\",\n    \"Analysing Chain of Thought Dynamics (Lewis-Lim et al., EMNLP 2025, arXiv 2508.19827)\",\n    \"The Illusion of Reasoning: Step-Level Evaluation Reveals Decorative CoT (Basu & Chakraborty, arXiv 2603.22816, Mar 2026)\",\n    \"Why Models Know But Don't Say: CoT Faithfulness Divergence (Young, arXiv 2603.26410, Mar 2026)\",\n    \"Therefore I am. I Think (Esakkiraja et al., arXiv 2604.01202, Apr 2026)\",\n    \"Early Stopping via Confidence Dynamics: CoDE-Stop (Hosseini et al., arXiv 2604.04930, Apr 2026)\",\n    \"Mechanistic Evidence for Faithfulness Decay in Chain-of-Thought Reasoning (Ye et al., arXiv 2602.11201, Feb 2026)\",\n    \"Decoding Answers Before Chain-of-Thought (Cox et al., arXiv 2603.01437, Mar 2026) — pre-CoT probes >0.9 AUC; steering flips >50% on instruction-tuned models; limited to binary tasks; little success steering reasoning models\",\n    \"Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought (Boppana et al., arXiv 2603.05488, Mar 2026)\",\n    \"No Global Plan in Chain-of-Thought (Xu et al., arXiv 2602.02103, Feb 2026)\",\n    \"Catching Rationalization in the Act (Mirtaheri & Belkin, arXiv 2603.17199, Mar 2026)\",\n    \"Analyzing and Improving CoT Monitorability Through Information Theory (Anwar et al., arXiv 2602.18297, Feb 2026)\",\n    \"FaithCoT-Bench (ICLR 2026, arXiv 2510.04040)\",\n    \"The Mirage of Explainability: A Survey on CoT Faithfulness (Jin et al., submitted to ARR for ACL 2026)\",\n    \"Lie to Me: How Faithful Is CoT Reasoning in Reasoning Models? (arXiv 2603.22582, Mar 2026)\",\n    \"Understanding Chain-of-Thought in LLMs through Information Theory (Ton et al., ICML 2025, arXiv 2411.11984)\",\n    \"NEAT: Neuron-Based Early Exit (arXiv 2602.02010, Feb 2026)\",\n    \"ESTAR: Early-Stopping Token-Aware Reasoning (arXiv 2602.10004, Feb 2026)\",\n    \"When Chain-of-Thought Fails, the Solution Hides in the Hidden States (arXiv 2604.23351, Apr 2026)\",\n    \"Knowing Before Saying (ACL Findings 2025, arXiv 2505.24362)\",\n    \"From Reasoning to Answer: Mechanistic Insights into Distilled DeepSeek R1 Models (arXiv 2509.23676, 2025) — activation patching on R1-Distill shows reasoning token perturbations flip outputs\",\n    \"Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance? (Ravichander et al., arXiv 2005.00719, 2020) — foundational for probe inflation concern\",\n    \"Amnesic Probing: Behavioral Explanation with Amnesic Counterfactuals (Elazar et al., TACL 2021, arXiv 2006.00995) — conventional probing performance is not correlated to task importance\",\n    \"I Have Covered All the Bases: Interpreting Reasoning Features via SAEs (arXiv 2503.18878, 2025) — SAE feature taxonomies on R1-Distill and QwQ-32B; informs SAE-based contingency\",\n    \"Addressing Divergent Representations from Causal Interventions (arXiv 2511.04638, 2025) — classifies probe-causal divergences into harmless and pernicious; divergence pattern is informative\"\n  ],\n  \"description\": \"We propose a calibrated dual-estimator Temporal Information Curve (TIC) framework that diagnoses chain-of-thought faithfulness by measuring the divergence between what a model internally represents — above a correlative baseline — and what its reasoning text causally contributes at each token position. The central methodological advance over prior work is addressing the probe inflation problem: the well-documented finding (Hewitt & Liang 2019; Chun et al. 2602.20338) that probe accuracy on hidden states captures correlative/epiphenomenal information, which would collapse all faithfulness phenomena into a single 'high gap everywhere' pattern if left uncalibrated. We introduce a three-layer calibration strategy: (1) null-probe normalization (subtracting shuffled-label probe accuracy to measure excess information above chance), (2) Manifold Capacity Theory geometric validation (verifying that detected information is geometrically organized for computation, not merely retrievable), and (3) MDL complexity checks (confirming the signal is structured, not noise-like). The calibrated Probe-TIC P*(t) is paired with NLDD-based Causal-TIC C(t) to produce the calibrated gap G*(t) = P*(t) - C(t), which we diagnose via trajectory shapes (temporal derivatives, curvature, onset timing) rather than absolute values — a design choice validated by the shape-over-magnitude dissociation literature (2603.18940; 2602.06266; 2604.05655).\\n\\nPrior work has established the building blocks: Kudo et al. (EACL 2026) combine probing and patching on synthetic arithmetic; the CMI framework (2602.03994) provides layerwise causal audit on approximately 50 examples; Zhao et al. (2510.24941) measure per-step causal contribution via TTS on AIME/MATH; Furuya & Tanimura (2605.01853) track temporal hidden-state dynamics via StALT; Li et al. (2510.22362) track concept-direction alignment over time via Concept Walk; Liu et al. (2602.13904) diagnose CoT pathologies via text-level metrics. We unify and extend these paradigms in four ways: (1) we construct a full-timeline calibrated dual-estimator curve combining null-probe-normalized answer-content linear probes (Probe-TIC) with NLDD causal interventions (Causal-TIC), with MCT geometric validation — extending TTS from per-step to continuous temporal coverage and addressing the probe inflation gap absent from all prior single-estimator approaches; (2) we map five independently discovered phenomena — pre-CoT encoding, Reasoning Horizon, Reasoning Theater, myopic planning, and thinking-answer gap — to distinguishable trajectory-shape signatures in the calibrated G*(t) curve, with a worked demonstration that shapes remain discriminable under probe inflation and formal statistical testing via FDA shape distance metrics, conditioned on task difficulty following the ICLR 2026 Workshop finding and Li et al.'s independent corroboration; (3) we derive the Temporal Information Fidelity (TIF) score with explicit robustness validation across probe architectures, layer selections, perturbation methods, normalization choices, and calibration methods, addressing the measurement sensitivity concern raised by Young (2603.20172); and (4) we include a Phase 0 pilot that simultaneously validates probe calibration methodology (null-probe, MCT concordance, MDL) and tests answer-content probe causal potency on reasoning models, with a detailed three-tier contingency plan (calibrated information-availability interpretation, reasoning-behavioral-mode probe pivot, dual-causal framework pivot) if causal potency fails.\\n\\nThe paper is focused around three core contributions: (a) Phase 0 pilot results providing novel empirical findings on probe calibration and causal potency in reasoning models; (b) the calibrated gap diagnostic G*(t) demonstrated on 4 models x 4 benchmarks with task-difficulty conditioning; (c) five-phenomenon mapping via trajectory shapes with FDA statistical tests. Robustness ablations and TIF validation form supporting sections; 671B validation and early-exit application are supplementary material.\",\n  \"revision_notes\": {\n    \"critical_changes\": [\n      \"ELEVATED GAP INFLATION TO TIER-1 AND ADDRESSED WITH THREE-LAYER CALIBRATION (Major): Reviewer identified that Chun et al.'s finding (probe accuracy does not equal computational readiness) means P(t) may be uniformly high, collapsing five-phenomenon signatures. This is now the central methodological contribution. We introduce: (a) null-probe calibration P*(t) = P(t) - P_null(t) following Hewitt & Liang (2019), producing a calibrated curve measuring excess answer information above correlative baseline; (b) MCT geometric validation following Chun et al. (2602.20338), checking whether detected information shows the transient geometric pulse characteristic of computationally relevant information; (c) MDL complexity check following Voita & Titov (2020), confirming signal structure. This calibration removes uniform inflation: if raw P(t) and P_null(t) are both high, P*(t) is low.\",\n      \"ADDED FORMAL TRAJECTORY-SHAPE ANALYSIS WITH WORKED EXAMPLE (Major): Reviewer argued five-phenomenon distinguishability was underspecified under the weak assumption. We now: (a) provide concrete worked example showing three phenomena produce distinguishable G*(t) trajectory shapes even with +0.3 correlative inflation because null-probe calibration removes uniform offset; (b) adopt six trajectory-shape features rather than absolute values; (c) cite shape-over-magnitude dissociation literature (2603.18940, 2602.06266, 2604.05655); (d) plan FDA shape distance metrics (Fisher-Rao distance) for formal statistical testing.\",\n      \"CITED LI ET AL. (2510.22362) MAPPING FAITHFUL REASONING (Minor): Concept Walk framework now cited throughout. Differentiated: concept directions (not answer-content probes), single domain (safety), single model (Qwen 3-4B), no continuous causal-contribution curve. Supports task-difficulty conditioning as independent corroboration.\",\n      \"EXPANDED PHASE 0 CONTINGENCY PLAN TO THREE TIERS (Major): Three ordered fallbacks if causal potency fails: (A) calibrated information-availability with MCT validation (preferred); (B) pivot to reasoning-behavioral-mode probes with confirmed causal potency on reasoning models (2510.04128); (C) dual-causal framework replacing probes with CMI-style activation patching. All preserve Causal-TIC, task-difficulty conditioning, phenomenon mapping, and TIF score.\",\n      \"TIGHTENED PAPER FOCUS (Minor): Core = Phase 0 pilot + calibrated gap diagnostic + difficulty-conditioned trajectory-shape signatures. Supporting = robustness ablations + TIF validation. Supplementary = 671B validation + early-exit + detailed calibration analysis.\",\n      \"ADDED PROBE CALIBRATION LITERATURE (Major): Hewitt & Liang (EMNLP 2019) for selectivity; Voita & Titov (EMNLP 2020) for MDL probing; Belrose et al. (NeurIPS 2023) for LEACE; Dobrzeniecka et al. (ACL 2025) for improved amnesic probing; Ravichander et al. (2020) for probe-task-relevance gap. Also trajectory-shape references: entropy trajectories (2603.18940), RQA dynamics (2602.06266), trajectory geometry (2604.05655).\",\n      \"ADDED REASONING-MODEL PROBING LITERATURE FOR CONTINGENCY (Minor): Internal States Before Wait (2510.04128) for causally potent reasoning-behavioral-mode probes on R1-Distill; From Reasoning to Answer (2509.23676) for activation patching on R1-Distill; I Have Covered All the Bases (2503.18878) for SAE feature taxonomies.\"\n    ],\n    \"what_stayed\": \"The five-phenomena unification thesis (now with formal trajectory-shape analysis), the dual-TIC concept (now with probe calibration), the NLDD and probe estimators, the four benchmarks (MMLU, GPQA-Diamond, GSM8K, AIME), the four target models (DeepSeek-R1-Distill 7B/14B/32B, QwQ-32B), the 671B validation subset, layer-selective caching, the TIF score concept, the synthetic arithmetic calibration check, the TTS cross-reference, the task-difficulty conditioning, the robustness ablations, and the diagnostic (thermometer) framing.\",\n    \"residual_risks\": [\n      \"TIER-1: Null-probe calibration may over-correct. If P_null(t) is high because hidden states contain rich correlative structure (not random noise), subtracting it may remove genuine answer information that happens to correlate with generic features. Mitigation: compare three calibration methods (shuffled-label, random-representation, MDL threshold) and report sensitivity; if methods disagree substantially, this reveals the calibration boundary is itself a finding about representation structure.\",\n      \"TIER-1: The TTS paper (Zhao et al. 2510.24941) tests on our exact models and benchmarks. If Causal-TIC (NLDD-based) and TTS (ATE-based) show near-identical patterns at step boundaries, the continuous-temporal-coverage novelty narrows. Mitigation: the calibrated dual-estimator gap and trajectory-shape mapping remain unique; within-step dynamics visible to Causal-TIC but invisible to TTS provide differentiation. The probe calibration methodology is a standalone contribution regardless.\",\n      \"TIER-1: MCT geometric validation may show discordance with P*(t) — the geometric pulse timing may not match the calibrated probe trajectory. If so, this reveals that even calibrated probes capture information not geometrically prepared for use. Mitigation: the discordance itself is a finding; proceed with Fallback A noting the specific gap between geometric readiness and probe decodability.\",\n      \"TIER-2: Task-difficulty conditioning may reveal that five phenomena are artefacts of different task types rather than a unified information dynamic. Would weaken 'unification' thesis to 'taxonomy indexed by difficulty' — less exciting but still publishable.\",\n      \"TIER-2: Measurement sensitivity: TIF may show high sensitivity to choices. Mitigation: plan ablations early, report sensitivity ranges.\",\n      \"TIER-2: NLDD interventions remain computationally expensive. MCT adds approximately 30 node-hours. May need subsampling for AIME long traces.\",\n      \"TIER-2: Field moving at 3+ papers per month. The probe calibration methodology, trajectory-shape analysis, and Phase 0 pilot providing novel empirical evidence are more defensible against concurrent work than the original uncalibrated framework.\"\n    ]\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "201f5d92-6ecc-4390-8cde-5f8a0f58ff4c",
  "isSidechain": false,
  "requestId": "req_011CbBvA1XwvvF9MoBDHbjyn",
  "type": "assistant",
  "uuid": "4f6213e2-96c8-4705-9e9b-9168b2171d50",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XkYQzFXahJdMqUFvrd6eTr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14882,
      "cache_read_input_tokens": 63133,
      "output_tokens": 14706,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14882,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14706,
          "cache_read_input_tokens": 63133,
          "cache_creation_input_tokens": 14882,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14882
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

_source line 42 · 2026-05-19T12:26:25.663Z_

<details><summary>↩ Tool result · reported error · `toolu_01YDcbos9UJDFnWLfTKYvEAS`</summary>

```text
Claude requested permissions to write to /tmp/revised_proposal_r5.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f6213e2-96c8-4705-9e9b-9168b2171d50",
  "isSidechain": false,
  "promptId": "f76ab8f1-cf60-4739-be49-0817894703ea",
  "type": "user",
  "uuid": "5938ffb0-9e41-45ad-ae62-fb9ade1561e5",
  "toolUseResult": "Error: Claude requested permissions to write to /tmp/revised_proposal_r5.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "4f6213e2-96c8-4705-9e9b-9168b2171d50",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"The Probe-Intervention Gap: Diagnosing Chain-of-Thought Faithfulness v…",
  "leafUuid": "5938ffb0-9e41-45ad-ae62-fb9ade1561e5",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise gap diagnostic discriminability and phenomenon distinguishability",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f"
}
```

---

### Assistant

_source line 45 · 2026-05-19T12:26:29.124Z_

<details><summary>Logged reasoning block</summary>

```text
Let me just output the JSON directly in my response since I can't write to file. The user asked me to output a complete JSON object.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5938ffb0-9e41-45ad-ae62-fb9ade1561e5",
  "isSidechain": false,
  "requestId": "req_011CbBvbsJKfAy2RBkihdPu9",
  "type": "assistant",
  "uuid": "c8a1d172-6cc0-4341-98a5-10e3ff1b2c1d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bcjz2mKV695H5G2qeBWBd9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14751,
      "cache_read_input_tokens": 78015,
      "output_tokens": 10076,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14751,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10076,
          "cache_read_input_tokens": 78015,
          "cache_creation_input_tokens": 14751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14751
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

_source line 46 · 2026-05-19T12:30:03.062Z_

Here is the complete revised proposal as a JSON object. This is a **major revision** — the probe calibration methodology and formal trajectory-shape analysis are substantive additions that fundamentally strengthen the framework against the reviewer's core concern.

---

```json
{
  "change_type": "major",
  "title": "The Probe-Intervention Gap: Diagnosing Chain-of-Thought Faithfulness via Calibrated Dual-Estimator Temporal Information Decomposition",
  "project_name": "cot_faithfulness_decomp",
  "source": "web_research",
  "level": "top-tier",
  "target_venues": [
    "ICLR 2027 (abstract: Sep 19, full paper: Sep 24, 2026; conference: Apr/May 2027 — primary target, 4 months from now)",
    "ICML 2027 (full paper: Jan 29, 2027; conference: Jul 2027 — comfortable fallback if additional experiments needed)"
  ],
  "core_problem": "Multiple independent findings in 2025-2026 — Reasoning Horizon, pre-CoT answer encoding, Reasoning Theater, myopic planning, thinking-answer gap — all describe facets of the same underlying problem: models' chain-of-thought reasoning is partially or entirely decorative. While the CoT faithfulness literature has catalogued these phenomena (Jin et al.'s survey; FaithCoT-Bench at ICLR 2026) and several groups have measured temporal dynamics of individual signals, no work has unified these disparate phenomena under a single information-theoretic framework that explains WHY and WHEN each occurs. Crucially, recent work reveals that the relationship between faithfulness and task difficulty is not binary: CoT transitions from decorative to load-bearing as task difficulty increases ('Task Difficulty Shapes CoT Faithfulness,' ICLR 2026 Workshop), with error propagation ranging from 22% on MMLU to 41% on BBH. This difficulty gradient — detectable via hidden-state probes but resistant to single-direction steering ('readout rather than control') — demands a diagnostic framework that can characterize faithfulness along both temporal and difficulty dimensions. A critical methodological concern, raised by the probing literature (Hewitt & Liang 2019; Ravichander et al. 2020; Chun et al. 2602.20338) and reinforced by Yuan et al. (2605.09502), is that probe accuracy on hidden states captures correlative/epiphenomenal information rather than information the model actively uses — probe accuracy does not equal computational readiness. This means any probe-based diagnostic must address the gap inflation problem: if probes detect uniformly high 'information availability' regardless of actual faithfulness, the diagnostic collapses. The closest precedents — Kudo et al.'s (EACL 2026) probing + activation patching on synthetic arithmetic, the CMI framework's layerwise causal audit on ~50 examples, Zhao et al.'s (2510.24941) True Thinking Score providing per-step causal contribution on AIME/MATH, Furuya & Tanimura's (2605.01853) training-free StALT trajectory statistic, and Li et al.'s (2510.22362, NeurIPS 2025 MechInterp Workshop) Concept Walk tracking temporal concept-direction alignment — each capture one dimension of the problem but none provides a calibrated dual-estimator framework that jointly measures internal information and causal contribution across the full CoT timeline on natural benchmarks, with explicit controls for probe inflation.",
  "opportunity": "The field has independently produced three complementary measurement paradigms: (1) probe-based approaches revealing what the model internally represents at each CoT position (David 2511.14773: correctness decodable at t=4 tokens; Cox et al. 2603.01437: pre-CoT probes at >0.9 AUC with causal validation via steering on instruction-tuned models up to 9B; Esakkiraja et al. 2604.01202: pre-generation probes with >90% AUROC; Furuya & Tanimura 2605.01853: training-free StALT separating correct from incorrect trajectories; Li et al. 2510.22362: Concept Walk tracking concept-direction alignment per step, finding easy→decorative, hard→faithful), (2) intervention-based approaches measuring what the CoT text causally contributes (Ye et al. 2602.11201: NLDD reveals Reasoning Horizon at 70-85%; Zhao et al. 2510.24941: True Thinking Score provides per-step ATE on AIME/MATH/AMC/CommonsenseQA, finding only 2.3% of AIME steps have TTS≥0.7; Basu & Chakraborty 2603.22816: decorative/scaffolding/genuine taxonomy), and (3) diagnostic approaches characterizing CoT pathologies (Liu et al. 2602.13904: text-level metrics for rationalization/encoded/internalized reasoning via model organisms; 'Task Difficulty Shapes CoT Faithfulness' ICLR 2026 Workshop: difficulty-dependent faithfulness gradient). Two prior works have combined probing with causal interventions on the same instances: Kudo et al. (2412.01113, EACL 2026) train linear probes and perform activation patching across arithmetic CoT; the CMI framework (2602.03994) measures CoT-mediated causal influence via layerwise patching. However, neither provides: (a) full temporal-position coverage across CoT on natural benchmarks, (b) a mapping to the five named faithfulness phenomena, (c) a standalone instance-level diagnostic score, (d) systematic multi-model comparison on realistic reasoning tasks, (e) robustness validation across measurement methodologies — a critical gap highlighted by Young's (2603.20172) finding that faithfulness measurements are classifier-sensitive (inter-classifier kappa as low as 0.06), or (f) controls for probe inflation — the well-documented problem that probe accuracy captures correlative information not actively used by the model (Hewitt & Liang 2019; Voita & Titov 2020; Chun et al. 2602.20338). The opportunity is to extend the probe-intervention combination paradigm to a calibrated dual-estimator Temporal Information Curve (TIC) framework producing a 2D faithfulness signal — the gap between calibrated probe-estimated internal information and intervention-estimated causal contribution — on natural benchmarks at scale, with explicit probe inflation controls and robustness validation.",
  "landscape": "**Probe-intervention combinations (closest prior work).** Kudo et al. (2412.01113, EACL 2026) train per-position linear probes on hidden states and validate with sliding-window activation patching on 9 models across synthetic multi-step arithmetic. They find CoT IS faithful for arithmetic but explicitly note their synthetic setting may not generalize to 'more realistic reasoning tasks in natural language.' The CMI framework (2602.03994) introduces the CoT Mediation Index via layerwise activation patching across Phi, Qwen, and DialoGPT on StrategyQA (20 examples), TruthfulQA (10), and GSM8K (20), identifying 'bypass regimes' where CMI ≈ 0. Both are complementary precursors.\n\n**Per-step causal contribution (direct Causal-TIC precursor).** Zhao et al. (2510.24941, Oct 2025, revised Apr 2026) introduce the True Thinking Score (TTS), measuring per-step causal contribution via text-level perturbation (numerical offsets preserving grammar) and ATE computation. On DeepSeek-R1-Distill-Qwen-7B/14B/Llama-8B across AIME, MATH, AMC, CommonsenseQA, they find only 2.3% of AIME steps have TTS≥0.7. TTS also extracts a 'TrueThinking direction' from hidden states for steering (53.6-91.2% flip rates). TTS is a direct precursor to our Causal-TIC component. Key differentiators: TTS operates at discrete step granularity (not continuous temporal), is a single-estimator metric (no calibrated probe gap), uses text-level perturbation (vs. our NLDD logit degradation), and does not map to the five faithfulness phenomena or provide an instance-level diagnostic score grounded in the probe-intervention divergence.\n\n**Training-free temporal hidden-state dynamics (concurrent work adjacent to Probe-TIC).** Furuya & Tanimura (2605.01853, May 2026) introduce StALT (Spatiotemporal Amplitude of Latent Transition), a training-free trajectory statistic that separates correct from incorrect reasoning trajectories. Key differentiators: targets correctness separation (not faithfulness diagnosis), training-free (vs. our trained answer-content probes), lacks a causal intervention component (no gap diagnostic).\n\n**Temporal concept-direction tracking (concurrent work supporting task-difficulty conditioning).** Li et al. (2510.22362, NeurIPS 2025 MechInterp Workshop) introduce Concept Walk, which projects each reasoning step's activations onto concept directions (learned via difference-of-means from contrastive data) and tracks temporal evolution across CoT. On Qwen 3-4B in the safety domain, they find easy cases produce only transient activation shifts under perturbation (decorative CoT), while hard cases produce sustained, structured shifts (faithful CoT). This directly supports our task-difficulty conditioning dimension. Key differentiators: concept directions (not answer-content probes), single domain (safety, not reasoning benchmarks), no separate causal-contribution curve, single small model (Qwen 3-4B), no instance-level diagnostic score.\n\n**Latent-trajectory signals for efficiency.** Vilas et al. (2510.10494, ICLR 2026) define three latent-trajectory signals tracking hidden-state evolution. On DeepSeek-R1-Distill-Qwen-14B, Phi-4-Reasoning-Plus, and Qwen3-14B they achieve 14-70% token savings. Focuses on efficiency, not faithfulness. Adjacent methodology but orthogonal goal.\n\n**The diagnostic-not-causal challenge.** Yuan et al. (2605.09502, May 2026) show that probes detecting trace correctness achieve 0.95 AUROC but four interventions fail. Cox et al. (2603.01437) demonstrate that answer-content probes are causally potent on instruction-tuned models (steering flips >50% of answers), but their validation is restricted to binary tasks on models ≤9B, and they explicitly note 'little success steering' reasoning models. The causal potency of answer-content probes on reasoning models is NOT yet established.\n\n**The probe inflation problem.** Hewitt & Liang (2019) show MLP probes achieve only 4.5 selectivity (97.3% accuracy vs. 92.8% on shuffled-label controls). Ravichander et al. (2020) demonstrate that properties are recoverable even when models cannot use them. Voita & Titov (2020) show MDL-based probing reveals standard accuracy does not substantially favor pretrained over random representations. Chun et al. (2602.20338) apply Manifold Capacity Theory to CoT reasoning and find geometric separability peaks transiently as a 'geometric pulse' just before computation and compresses rapidly afterward, while probe accuracy remains high long after computation is complete. This provides direct evidence that probe accuracy overestimates information availability. We address this via null-probe calibration and MCT geometric validation.\n\n**Trajectory-shape analysis.** The entropy trajectory paper (2603.18940) shows a 'shape-over-magnitude dissociation': monotonicity of entropy decrease predicts reasoning reliability regardless of absolute levels (+5.8pp at 73.7% coverage). RQA analysis (2602.06266) shows temporal features outperform aggregate statistics (36.94% vs. 28.97%). Microsoft's trajectory geometry work (2604.05655) shows 0.852 AUC from shape features vs. 0.649 from step-count baselines. This literature supports our claim that trajectory shapes can distinguish phenomena even under absolute-value inflation.\n\n**CoT pathology diagnostics.** Liu et al. (2602.13904) propose text-level metrics for three CoT pathologies. Complementary: purely text-level, no hidden states, categorical per-pathology.\n\n**Measurement sensitivity.** Young (2603.20172) shows inter-classifier kappa as low as 0.06, up to 30.6pp divergence.\n\n**Task-difficulty moderation.** 'Task Difficulty Shapes CoT Faithfulness' (ICLR 2026 Workshop) and Li et al. (2510.22362) independently show easy→decorative, hard→faithful.\n\n**Probe-based temporal measurement.** Qian et al. (2506.02867, NeurIPS 2025); David (2511.14773); Zhang et al. (2504.05419) probe R1-Distill for correctness at >0.7 AUC; Lewis-Lim et al. (2508.19827, EMNLP 2025); Mirtaheri & Belkin (2603.17199); Esakkiraja et al. (2604.01202).\n\n**Intervention-based causal measurement.** Ye et al. (2602.11201) NLDD; Basu & Chakraborty (2603.22816); Somov et al. (2603.16475); FACT-E (2604.10693).\n\n**Probing and steering faithfulness.** Occhipinti et al. (ICLR 2026 LIT Workshop): probing F1 90-100%; steering 46% recovery.\n\n**Probing reasoning models specifically.** Internal States Before Wait (2510.04128): crosscoders on R1-Distill with confirmed causal interventions for backtracking, uncertainty, verification features. From Reasoning to Answer (2509.23676): activation patching on R1-Distill with NLD up to 0.5. These inform our contingency plan.\n\n**Geometric approaches.** Chun et al. (2602.20338) MCT; Alvarez & Baheri (2605.13772); Ton et al. (ICML 2025, 2411.11984); Anwar et al. (2602.18297).\n\n**Benchmarks, surveys, early-exit.** FaithCoT-Bench (ICLR 2026). Jin et al.'s survey (ARR for ACL 2026). Young (2603.26410). 'Lie to Me' (2603.22582). Reasoning Theater (2603.05488). ESTAR/DTSR/NEAT/CoDE-Stop/FRIT.\n\n**What remains open.** No extant framework provides: (1) a full-timeline calibrated dual-estimator curve with probe inflation controls; (2) five-phenomenon trajectory-shape signatures robust under the weak assumption via formal shape analysis; (3) an instance-level diagnostic score from the calibrated gap with robustness validation; or (4) a principled account of gap behavior across instruction-tuned vs. reasoning models. The calibrated dual-estimator gap remains unique.",
  "inspired_by": "The convergence of five observations: (a) Kudo et al.'s probe+intervention combination on synthetic arithmetic with their call for natural-task extension; (b) Zhao et al.'s (2510.24941) TTS establishing per-step causal contribution on our exact benchmarks; (c) the finding from Cox et al. (2603.01437) and the 'Task Difficulty' workshop that probes are diagnostic not interventional; (d) Young's (2603.20172) measurement sensitivity findings; (e) Chun et al.'s (2602.20338) discovery that probe accuracy ≠ computational readiness — geometric separability peaks transiently while probe accuracy stays flat — motivating null-probe calibration and trajectory-shape features.",
  "approach": "Define a calibrated dual-estimator Temporal Information Curve (TIC) framework that diagnoses chain-of-thought faithfulness at each token position t via two complementary signals, with explicit controls for probe inflation:\n\n**(a) Calibrated Probe-TIC P*(t)**: We address the probe inflation problem via a three-layer calibration strategy:\n\n(i) Null-probe normalization. For each layer and position, train a parallel 'null probe' on shuffled answer labels. Define P*(t) = P(t) − P_null(t), measuring excess answer information above what is extractable from correlative features alone. This follows Hewitt & Liang (2019) selectivity, adapted to our temporal setting: selectivity at each position t produces a calibrated curve. High P*(t) means the model encodes answer information beyond correlative features.\n\n(ii) MCT geometric validation. On 500 examples per benchmark, compute Manifold Capacity Theory (Chun et al. 2602.20338) separability alongside probe accuracy at each position. MCT measures intrinsic geometric readiness for computation (the 'geometric pulse') independent of probe training. If MCT and P*(t) show concordant trajectories, the probe captures geometrically prepared information; if MCT shows a transient pulse while P*(t) remains flat, this diagnoses inflation type.\n\n(iii) MDL complexity check. Following Voita & Titov (2020), compute minimum description length at each position. If answer-label codelength is substantially less than random-label codelength, the signal is structured.\n\nWe probe for answer content using linear probes on 3-5 layers. The calibrated P*(t) is interpreted as excess information availability — what the model represents above correlative baseline — not assuming causal potency. This interpretation is supported by Yuan et al. (2605.09502), the 'Task Difficulty' workshop, Li et al. (2510.22362), and Furuya & Tanimura (2605.01853).\n\n**(b) Causal-TIC C(t)**: Causal contribution of CoT up to position t via NLDD-style interventions. Extends NLDD (Ye et al. 2602.11201) to multi-model comparison and provides continuous temporal generalization of TTS (Zhao et al. 2510.24941). C(t) is not subject to probe inflation: it measures behavioral change under intervention.\n\n**The Calibrated Faithfulness Gap.** G*(t) = P*(t) − C(t). Because P*(t) is null-probe-calibrated, uniform inflation is removed. G*(t) ≈ 0 indicates alignment (necessary for faithfulness). G*(t) >> 0 indicates genuine information excess. G*(t) < 0 indicates information assembled during reasoning.\n\n**Trajectory-Shape Analysis for Phenomenon Distinguishability.** We diagnose phenomena from trajectory shapes rather than absolute values, validated by the shape-over-magnitude dissociation literature (2603.18940: monotonicity predicts reliability regardless of absolute levels; 2602.06266: temporal RQA features outperform aggregates 36.94% vs. 28.97%; 2604.05655: shape features achieve 0.852 AUC vs. 0.649 baseline).\n\nSix shape features from the calibrated dual-TIC:\n(i) P*(0) level — initial excess information. Detects pre-CoT encoding.\n(ii) dP*/dt trajectory — rate of information accumulation. Flat = front-loaded; positive = genuine acquisition.\n(iii) C(t) plateau onset t* — Reasoning Horizon.\n(iv) G*(t) trajectory shape — curvature and monotonicity. Reasoning Theater: widening. Genuine reasoning: near-zero. Pre-CoT encoding: large constant.\n(v) dC/dt locality — short- vs. long-range autocorrelation. Myopic planning: short-range only.\n(vi) P*-C boundary divergence — spike at thinking/answer interface. Thinking-answer gap.\n\n**Worked Example: Distinguishability Under Probe Inflation.** Three phenomena with raw P(t) uniformly inflated by +0.3:\n\nPre-CoT encoding: Raw P(t) = 0.9 from t=0 (0.6 real + 0.3 correlative), flat. P_null(t) ≈ 0.3. P*(t) ≈ 0.6 from t=0, flat. C(t) ≈ 0.1. G*(t) ≈ 0.5, constant. Shape: flat P*, flat C, large constant gap.\n\nReasoning Theater: Raw P(t) rises from 0.7 to 1.0. P_null(t) ≈ 0.3 with slight rise. P*(t) ≈ 0.1 → 0.7. C(t) ≈ 0.05. G*(t) starts near 0, grows monotonically. Shape: rising P*, flat C, widening gap.\n\nGenuine reasoning: Raw P(t) rises from 0.6 to 1.1. P_null(t) ≈ 0.3. P*(t) ≈ 0.0 → 0.8. C(t) tracks P*(t) with lag. G*(t) ≈ 0 throughout. Shape: co-rising P* and C, near-zero gap.\n\nShapes remain distinguishable despite uniform +0.3 inflation. Formal testing via FDA shape distance metrics (Fisher-Rao distance, elastic registration separating amplitude from phase variation; Srivastava & Klassen 2016).\n\n**Task-Difficulty Conditioning.** Following the ICLR 2026 Workshop finding and Li et al.'s (2510.22362) corroboration: easy → high P*(0) with flat C(t); moderate → Reasoning Horizon signatures; hard → co-rising P*(t) and C(t).\n\n**Phase 0 Pilot: Probe Calibration and Causal Potency.** 500 examples, MMLU + GSM8K, DeepSeek-R1-Distill-Qwen-7B. Three objectives:\n(i) Null-probe calibration validation: P_null(t) shows high accuracy (inflation is real) but P*(t) shows meaningful variance (calibration reveals structure).\n(ii) MCT concordance: test whether MCT pulse timing matches P*(t) trajectory.\n(iii) Causal potency: steering test on reasoning models for multi-choice tasks.\n\n**Detailed Three-Tier Contingency (if causal potency fails):**\n\nFallback A (preferred): Calibrated information-availability with MCT validation. If P*(t) shows structure and MCT is concordant, the probe captures geometrically organized information even if not steerable. G*(t) = 'geometrically available but causally unused information.' Thermometer analogy preserved.\n\nFallback B: Pivot to reasoning-behavioral-mode probes. Probe for backtracking, uncertainty, verification, knowledge recall — confirmed causally potent on reasoning models (Internal States Before Wait, 2510.04128). G*(t) becomes 'reasoning-mode commitment vs. CoT causal contribution.'\n\nFallback C: Dual-causal framework. Replace Probe-TIC with CMI-style activation patching. Eliminates probe inflation entirely; loses efficiency.\n\nAll fallbacks preserve Causal-TIC, task-difficulty conditioning, phenomenon mapping, and TIF score.\n\n**Robustness Ablations.** Five dimensions following Young (2603.20172): (a) probe architecture (linear vs. 2-layer MLP) with selectivity; (b) layer selection; (c) NLDD perturbation method; (d) gap normalization; (e) calibration method (shuffled-label vs. random-representation vs. MDL threshold). Report sensitivity ranges.\n\n**Experiments.** DeepSeek-R1-Distill-Qwen-7B/14B/32B, QwQ-32B across MMLU, GPQA-Diamond, GSM8K, AIME. 671B validation (500-example subset, 3 layers). Calibration checks: synthetic arithmetic (G* ≈ 0), TTS cross-reference, MCT cross-reference.\n\n**Paper Focus (Tightened).** Core: (1) Phase 0 probe calibration + causal potency results; (2) calibrated gap diagnostic on 4 models × 4 benchmarks with difficulty conditioning; (3) five-phenomenon trajectory-shape mapping with FDA tests. Supporting: robustness ablations; TIF validation. Supplementary: 671B; early-exit; detailed calibration analysis.\n\n**TIF Score.** Normalized area under calibrated G*(t). Benchmarked against FaithCoT-Bench and Liu et al.'s metrics.\n\n**Causal Sufficiency Stopping Criterion.** Supplementary early-exit from Causal-TIC inflection.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "650 H100-hours (300 inference + caching; 150 NLDD interventions; 50 probes + calibration + Phase 0; 50 robustness ablations; 50 MCT geometric validation; 50 671B subset)",
      "timeline": "4 months (2 researchers: 2 weeks Phase 0 pilot with null-probe + MCT + MDL + causal potency; 7 weeks core experiments with calibration; 3 weeks TIF validation + phenomenon mapping via FDA; 2 weeks robustness ablations; 2 weeks writing)",
      "estimated_gpu_cost": "$1,625",
      "storage": "3-5 TB (5 layers per model, fp16); reducible to ~1.5 TB via PCA"
    },
    "human_in_loop": {
      "gpu_hours": "550 H100-hours",
      "timeline": "3.5 months (1 researcher + Claude)",
      "claude_api_cost": "$450",
      "estimated_gpu_cost": "$1,375"
    },
    "auto_research": {
      "gpu_hours": "550 H100-hours",
      "timeline": "3 months",
      "claude_api_cost": "$900",
      "estimated_gpu_cost": "$1,375",
      "speed_bottleneck": "NLDD on 32B (~250 node-hours); MCT (~30 node-hours); 671B subset (8×H100); robustness ablations (~60 node-hours)"
    }
  },
  "key_references": [
    "LLMs Faithfully and Iteratively Compute Answers During CoT (Kudo et al., EACL 2026, arXiv 2412.01113)",
    "When Chains of Thought Don't Matter: Causal Bypass (Sathyanarayanan et al., arXiv 2602.03994)",
    "Hidden Error Awareness: The Signal Is Diagnostic, Not Causal (Yuan et al., arXiv 2605.09502)",
    "Can Aha Moments Be Fake? True Thinking Score (Zhao et al., arXiv 2510.24941)",
    "Spatiotemporal Hidden-State Dynamics / StALT (Furuya & Tanimura, arXiv 2605.01853)",
    "Mapping Faithful Reasoning / Concept Walk (Li et al., arXiv 2510.22362, NeurIPS 2025 MechInterp Workshop)",
    "Task Difficulty Shapes CoT Faithfulness (ICLR 2026 Workshop)",
    "Diagnosing Pathological CoT (Liu et al., arXiv 2602.13904)",
    "Measuring Faithfulness Depends on How You Measure (Young, arXiv 2603.20172)",
    "Emergent Manifold Separability / MCT (Chun et al., arXiv 2602.20338)",
    "Tracing the Traces: Latent Temporal Signals (Vilas et al., ICLR 2026, arXiv 2510.10494)",
    "Probing and Steering CoT Unfaithfulness (Occhipinti et al., ICLR 2026 LIT Workshop)",
    "Designing and Interpreting Probes with Control Tasks (Hewitt & Liang, EMNLP 2019)",
    "Information-Theoretic Probing with MDL (Voita & Titov, EMNLP 2020, arXiv 2003.12298)",
    "LEACE: Perfect Linear Concept Erasure (Belrose et al., NeurIPS 2023, arXiv 2306.03819)",
    "Improving Causal Interventions in Amnesic Probing (Dobrzeniecka et al., ACL Findings 2025, arXiv 2506.11673)",
    "Shape-over-magnitude dissociation in entropy trajectories (arXiv 2603.18940)",
    "Is My Model Mind Blurting? RQA of Reasoning Dynamics (arXiv 2602.06266)",
    "LLM Reasoning as Trajectories (arXiv 2604.05655, Microsoft)",
    "Internal States Before Wait Modulate Reasoning Patterns (arXiv 2510.04128)",
    "FACT-E (Sun et al., ACL Findings 2026, arXiv 2604.10693)",
    "Step-Level Hallucination via Transport Geometry (Alvarez & Baheri, arXiv 2605.13772)",
    "Breaking the Chain (Somov et al., arXiv 2603.16475)",
    "DTSR Early Exit (Xiang et al., arXiv 2604.06787)",
    "FRIT (Swaroop et al., arXiv 2509.13334)",
    "Demystifying Reasoning Dynamics with MI (Qian et al., NeurIPS 2025, arXiv 2506.02867)",
    "Temporal Predictors of Outcome (David, arXiv 2511.14773)",
    "Reasoning Models Know When They're Right (Zhang et al., arXiv 2504.05419)",
    "Analysing CoT Dynamics (Lewis-Lim et al., EMNLP 2025, arXiv 2508.19827)",
    "The Illusion of Reasoning (Basu & Chakraborty, arXiv 2603.22816)",
    "Why Models Know But Don't Say (Young, arXiv 2603.26410)",
    "Therefore I am. I Think (Esakkiraja et al., arXiv 2604.01202)",
    "CoDE-Stop (Hosseini et al., arXiv 2604.04930)",
    "Mechanistic Evidence for Faithfulness Decay / NLDD (Ye et al., arXiv 2602.11201)",
    "Pre-CoT Probes and Activation Steering (Cox et al., arXiv 2603.01437)",
    "Reasoning Theater (Boppana et al., arXiv 2603.05488)",
    "No Global Plan in CoT (Xu et al., arXiv 2602.02103)",
    "Catching Rationalization in the Act (Mirtaheri & Belkin, arXiv 2603.17199)",
    "CoT Monitorability via Information Theory (Anwar et al., arXiv 2602.18297)",
    "FaithCoT-Bench (ICLR 2026, arXiv 2510.04040)",
    "The Mirage of Explainability survey (Jin et al., ARR for ACL 2026)",
    "Lie to Me (arXiv 2603.22582)",
    "Understanding CoT via Information Theory (Ton et al., ICML 2025, arXiv 2411.11984)",
    "NEAT (arXiv 2602.02010)",
    "ESTAR (arXiv 2602.10004)",
    "Solution Hides in Hidden States (arXiv 2604.23351)",
    "Knowing Before Saying (ACL Findings 2025, arXiv 2505.24362)",
    "From Reasoning to Answer (arXiv 2509.23676)",
    "Probing the Probing Paradigm (Ravichander et al., arXiv 2005.00719)",
    "Amnesic Probing (Elazar et al., TACL 2021, arXiv 2006.00995)",
    "SAE Reasoning Features (arXiv 2503.18878)",
    "Addressing Divergent Representations from Causal Interventions (arXiv 2511.04638)"
  ],
  "description": "We propose a calibrated dual-estimator Temporal Information Curve (TIC) framework that diagnoses chain-of-thought faithfulness by measuring the divergence between what a model internally represents — above a correlative baseline — and what its reasoning text causally contributes at each token position. The central methodological advance is addressing the probe inflation problem: the well-documented finding (Hewitt & Liang 2019; Chun et al. 2602.20338) that probe accuracy captures correlative/epiphenomenal information, which would collapse all faithfulness phenomena into a single 'high gap everywhere' pattern if left uncalibrated. We introduce a three-layer calibration strategy: (1) null-probe normalization (subtracting shuffled-label probe accuracy to measure excess information above chance), (2) Manifold Capacity Theory geometric validation (verifying information is geometrically organized for computation, not merely retrievable), and (3) MDL complexity checks. The calibrated Probe-TIC P*(t) is paired with NLDD-based Causal-TIC C(t) to produce the calibrated gap G*(t) = P*(t) − C(t), diagnosed via trajectory shapes rather than absolute values — validated by shape-over-magnitude dissociation literature (2603.18940; 2602.06266; 2604.05655).\n\nWe unify and extend prior paradigms in four ways: (1) a full-timeline calibrated dual-estimator curve with MCT geometric validation; (2) five-phenomenon trajectory-shape mapping with a worked demonstration of distinguishability under probe inflation and FDA statistical tests, conditioned on task difficulty; (3) TIF score with robustness validation across 5 measurement dimensions; (4) Phase 0 pilot validating probe calibration and causal potency on reasoning models, with three-tier contingency plan.\n\nThe paper focuses on three core contributions: (a) Phase 0 pilot results on probe calibration and causal potency; (b) calibrated gap diagnostic on 4 models × 4 benchmarks with difficulty conditioning; (c) five-phenomenon trajectory-shape mapping with FDA tests. Robustness ablations and TIF validation are supporting sections; 671B validation and early-exit are supplementary.",
  "revision_notes": {
    "critical_changes": [
      "ELEVATED GAP INFLATION TO TIER-1 AND ADDRESSED WITH THREE-LAYER CALIBRATION (Major): Introduced null-probe calibration P*(t) = P(t) − P_null(t) following Hewitt & Liang (2019); MCT geometric validation following Chun et al. (2602.20338); MDL complexity check following Voita & Titov (2020). This removes uniform inflation and makes the gap genuinely diagnostic.",
      "ADDED FORMAL TRAJECTORY-SHAPE ANALYSIS WITH WORKED EXAMPLE (Major): Concrete worked example showing three phenomena produce distinguishable G*(t) shapes even under +0.3 correlative inflation. Six trajectory-shape features. Cited shape-over-magnitude dissociation literature (2603.18940, 2602.06266, 2604.05655). Planned FDA shape distance metrics (Fisher-Rao distance) for formal testing.",
      "CITED LI ET AL. (2510.22362) MAPPING FAITHFUL REASONING (Minor): Concept Walk framework cited and differentiated throughout.",
      "EXPANDED PHASE 0 CONTINGENCY TO THREE TIERS (Major): Fallback A (calibrated information-availability + MCT), Fallback B (reasoning-behavioral-mode probes, 2510.04128), Fallback C (dual-causal framework). All preserve core contributions.",
      "TIGHTENED PAPER FOCUS (Minor): Core = Phase 0 + calibrated gap + trajectory shapes. Supporting = ablations + TIF validation. Supplementary = 671B + early-exit.",
      "ADDED PROBE CALIBRATION LITERATURE (Major): Hewitt & Liang 2019, Voita & Titov 2020, Belrose et al. 2023, Dobrzeniecka et al. 2025, Ravichander et al. 2020. Trajectory-shape: 2603.18940, 2602.06266, 2604.05655.",
      "ADDED REASONING-MODEL PROBING LITERATURE (Minor): Internal States Before Wait (2510.04128), From Reasoning to Answer (2509.23676), SAE features (2503.18878) for contingency."
    ],
    "what_stayed": "Five-phenomena unification thesis (now with formal shape analysis), dual-TIC concept (now with calibration), NLDD and probe estimators, four benchmarks, four target models, 671B validation, layer-selective caching, TIF score, synthetic arithmetic calibration, TTS cross-reference, task-difficulty conditioning, robustness ablations, diagnostic framing.",
    "residual_risks": [
      "TIER-1: Null-probe calibration may over-correct if answer information correlates with generic features. Mitigation: compare three calibration methods and report sensitivity.",
      "TIER-1: TTS tests on our exact models/benchmarks. If Causal-TIC and TTS show identical step-boundary patterns, continuous-coverage novelty narrows. Mitigation: calibrated gap and trajectory-shape mapping remain unique; probe calibration is standalone contribution.",
      "TIER-1: MCT may show discordance with P*(t). Mitigation: discordance is itself a finding about geometric readiness vs. decodability.",
      "TIER-2: Task-difficulty conditioning may reduce 'unification' to 'taxonomy indexed by difficulty.' Still publishable.",
      "TIER-2: TIF measurement sensitivity. Mitigation: ablations + sensitivity ranges.",
      "TIER-2: Computational cost (NLDD + MCT + ablations). May need subsampling.",
      "TIER-2: Rapid field movement. Calibration methodology + trajectory-shape analysis + Phase 0 empirics are more defensible than original uncalibrated framework."
    ]
  }
}
```

---

### Summary of changes addressing each reviewer issue:

1. **Gap inflation problem (CONCEPTUAL, now Tier-1):** Introduced a three-layer probe calibration strategy — null-probe normalization (Hewitt & Liang 2019 selectivity), MCT geometric validation (Chun et al. 2602.20338), and MDL complexity checks (Voita & Titov 2020). The calibrated P\*(t) = P(t) − P\_null(t) removes uniform correlative inflation. If raw P(t) is uniformly high but P\_null(t) is equally high, P\*(t) is correctly low.

2. **Five-phenomenon distinguishability (CONCEPTUAL):** Added a concrete worked example with three phenomena (pre-CoT encoding, Reasoning Theater, genuine reasoning) showing distinguishable G\*(t) trajectory shapes even under +0.3 uniform inflation. Adopted six trajectory-shape features over absolute values, grounded in the shape-over-magnitude dissociation literature (entropy trajectories achieving +5.8pp from shape alone; RQA temporal features at 36.94% vs. 28.97% for aggregates; trajectory geometry at 0.852 AUC). Planned FDA shape distance metrics for formal statistical testing.

3. **Li et al. (2510.22362) citation (MINOR):** Concept Walk now cited in core\_problem, opportunity, and landscape. Differentiated: concept directions (not answer-content probes), safety domain, single model, no continuous causal curve. Supports task-difficulty conditioning.

4. **Phase 0 contingency (RISK):** Expanded from one fallback to three ordered tiers: (A) calibrated information-availability with MCT concordance validation; (B) pivot to reasoning-behavioral-mode probes (backtracking, uncertainty, verification) with confirmed causal potency on reasoning models (2510.04128); (C) dual-causal framework replacing probes entirely with CMI-style patching.

5. **Novelty positioning (tightened focus):** Paper refocused to three core contributions: Phase 0 pilot empirics, calibrated gap diagnostic, trajectory-shape phenomenon mapping. Robustness ablations and TIF validation are supporting; 671B and early-exit are supplementary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8a1d172-6cc0-4341-98a5-10e3ff1b2c1d",
  "isSidechain": false,
  "requestId": "req_011CbBvbsJKfAy2RBkihdPu9",
  "type": "assistant",
  "uuid": "a33bd7cc-bfef-48e2-a7a9-7feaf97a5113",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bcjz2mKV695H5G2qeBWBd9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14751,
      "cache_read_input_tokens": 78015,
      "output_tokens": 10076,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14751,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10076,
          "cache_read_input_tokens": 78015,
          "cache_creation_input_tokens": 14751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14751
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"The Probe-Intervention Gap: Diagnosing Chain-of-Thought Faithfulness v…",
  "leafUuid": "a33bd7cc-bfef-48e2-a7a9-7feaf97a5113",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise gap diagnostic discriminability and phenomenon distinguishability",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f"
}
```

---

### Runtime record

_source line 49_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"The Probe-Intervention Gap: Diagnosing Chain-of-Thought Faithfulness v…",
  "leafUuid": "a33bd7cc-bfef-48e2-a7a9-7feaf97a5113",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f"
}
```

---

### Runtime record

_source line 50_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise gap diagnostic discriminability and phenomenon distinguishability",
  "sessionId": "a600395c-52af-4483-884f-a0137eaa6f5f"
}
```

---
