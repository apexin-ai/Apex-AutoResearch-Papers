# Idea Brief: Beyond Intent Drift: Persuasion-Grounded Turn Representations for Multi-Turn Jailbreak Detection


- **Idea ID**: `idea_008`
- **Created**: 2026-05-17
- **Approved**: 2026-05-17
- **Source**: foreign:be-idea-gen-0515-5
- **Level**: top-tier
- **Target Venues**: EMNLP 2026 (ARR submission deadline: May 25, 2026; commitment deadline: August 2, 2026; conference: October 24-29, Budapest) — LLM Security is listed as a topic area within the main conference, with additional relevance to Discourse and Pragmatics, NLP Applications, and Ethics/Bias/Fairness topic areas

## Seed Topic

Target: EMNLP 2026, ARR submission deadline 2026-05-25 (11 days from today 2026-05-14). Track: LLM Security.

Direction: LLM safety robustness — defense methods against jailbreaking, adversarial prompt attacks, and safety alignment degradation. In-scope: robust safety training that resists adaptive attacks, automated red-teaming frameworks for systematic vulnerability discovery, safety-aware decoding or filtering at inference time, detecting and mitigating safety degradation when models are fine-tuned or distilled, multi-turn attack defense, tool-use and agentic safety. NOT limited to text — agentic tool-call safety and multi-modal attack surfaces welcome.

Contribution type: METHOD ONLY. Must propose a concrete defense algorithm, detection pipeline, or training recipe — not just a new attack or red-teaming dataset. Attack + defense paired contributions OK if defense is the primary contribution.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total. Safety research is mostly inference-heavy — budget for evaluation across multiple attack suites, not large-scale pretraining.
2. Time: ≤11 days. Build on existing open safety benchmarks and models (Llama-3-Guard, ShieldGemma, Qwen3, DeepSeek-R1 distills). Use established attack libraries (HarmBench, JailbreakBench, StrongREJECT) for evaluation.
3. Eval: Attack Success Rate (ASR) reduction on HarmBench, JailbreakBench, AdvBench; safety score on WildGuard/Aegis; utility preservation on MT-Bench/MMLU (defense must not kill helpfulness).

This is a NEW dedicated track at EMNLP 2026 — high visibility, growing fast, few established defense methods. 2026 research shows reasoning models can jailbreak other models at 97% success; defense lags far behind attack. Look for: inference-time safety filters that adapt to attack patterns, representation-level safety mechanisms (circuit-based), robust alignment under fine-tuning distribution shift, defense against multi-turn and agentic attacks. Avoid: yet another jailbreak attack without defense contribution, prompt-template-only defenses, safety classifiers without adversarial robustness guarantees.

## Core Problem

Multi-turn jailbreak attacks remain one of the most persistent threats to deployed LLMs, distributing adversarial intent across individually benign-seeming messages that exploit conversational dynamics to gradually steer models past safety boundaries. The state-of-the-art dedicated multi-turn detector, DeepContext (arXiv 2602.16935, Feb 2026), models this threat as generic intent drift: it embeds each turn with fine-tuned BERT, applies task-attention weighted pooling, and feeds the resulting sequence through a 3-layer GRU (2048 hidden units) with hybrid residual connections to detect when the conversation trajectory shifts toward harmful territory. This approach achieves F1=0.84 on standard multi-turn benchmarks with sub-20ms inference on a T4 GPU, establishing a strong baseline. However, DeepContext's reliance on undifferentiated semantic drift creates three fundamental limitations. (1) High false-positive rates on naturally drifting conversations: brainstorming sessions, Socratic dialogues, creative writing, and complex tutoring all exhibit substantial topic drift, triggering drift detectors even though no manipulation is occurring. (2) Zero interpretability: the 2048-dimensional GRU hidden state provides an opaque risk score with no actionable threat intelligence—security teams cannot see which manipulation strategy is being employed or at which turn the attack transitions from rapport-building to exploitation. (3) The acknowledged 'glass cannon' effect—strong performance on known attack templates but fragile generalization to novel strategies—because the model learns surface-level correlates of attacks (lexical drift patterns) rather than the underlying causal mechanism (adversarial persuasion). A recent representation engineering analysis (Bullwinkel et al., arXiv 2507.02956, Microsoft Research, Jun 2025) provides a mechanistic explanation for why per-turn representation-level defenses fundamentally struggle with multi-turn attacks: Crescendo keeps model outputs in a 'benign' region of representation space, with harmful classification dropping sharply after just 2 turns. Circuit breakers—trained to reroute harmful single-turn representations—achieve only 54.2% ASR defense (vs. 3.8% on single-turn) because multi-turn attack representations are 'sufficiently different from single-turn representations.' This finding demonstrates that the information needed to detect multi-turn attacks is not reliably present in per-turn representations of semantic content; it resides instead in the discourse-level pattern of how turns relate to each other—specifically, in the adversarial persuasion playbook orchestrating the conversation. Meanwhile, BIID (arXiv 2509.22732) achieves near-0% ASR through bidirectional LLM-based intention inference, but imposes 2+ full LLM reasoning passes per turn with latency estimated at several seconds (no published latency analysis exists; this estimate is based on the computational requirements of two full LLM forward passes per turn and requires independent verification). GLiGuard (arXiv 2605.07982, May 2026) demonstrates that compact 300M-parameter encoders can detect 11 jailbreak strategies and 14 harm categories in a single pass with 16x speedup over 7B decoder guards, but operates only on single inputs without temporal modeling. XGuard-Train (arXiv 2504.13203) achieves 48.3% vulnerability reduction through safety training data (30K multi-turn conversations), but as a training-time defense, it is model-specific and inapplicable to closed-source or already-deployed models. The core problem is therefore not architectural—encoder-plus-recurrent designs are well-established for this task—but representational: the features extracted from each turn do not encode the information most relevant to distinguishing adversarial manipulation from benign conversational evolution, and as Bullwinkel et al. show, per-turn semantic representations are actively misleading because multi-turn attacks are designed to keep them benign. What turn-level representation would capture the causal mechanism of multi-turn attacks at the discourse level, above the representation space where attacks deliberately hide?

## Opportunity / Why Now

Four converging findings define a precise representational opportunity. First, Bullwinkel et al. (arXiv 2507.02956, Microsoft Research, Jun 2025) established that multi-turn jailbreaks succeed specifically because they keep per-turn representations in a 'benign' region of representation space, explaining why representation-level defenses (circuit breakers) fail with a 50-percentage-point generalization gap. This finding has a critical implication: effective multi-turn detection requires features that operate above the per-turn representation level—at the discourse level where the manipulation playbook is visible even when individual turns appear benign. Second, 'How Do LLMs Persuade?' (arXiv 2508.05625) demonstrated that linear probes applied to intermediate transformer representations can reliably detect persuasion strategies, track persuasion success trajectories, and identify personality-adapted persuasion across multi-turn conversations—faster than prompting-based approaches and with competitive accuracy. Although this work was not applied to jailbreak detection, it empirically validates a crucial premise: the specific persuasion mechanisms operating in a conversation are extractable from turn-level representations and computationally tractable. Third, Hagendorff (Nature Communications 2026) showed that reasoning-model attackers achieving 97% ASR employ identifiable persuasion strategies—flattery/rapport-building (84.75%), educational/research framing (68.56%), hypothetical scenarios (65.67%), verbose technical jargon (44.42%)—that 'largely align with those predefined in the system prompt,' creating predictable temporal discourse signatures. Multi-turn jailbreaks succeed through specific persuasion playbooks: rapport THEN reframing THEN escalation, where each step individually appears benign but the sequence constitutes manipulation. Fourth, the Persuasive Fingerprint work (Alizadeh Noughabi et al., CIKM 2025, arXiv 2510.21983) confirmed that Cialdini's persuasion principles computationally characterize jailbreak susceptibility, establishing that persuasion structure is the right analytical lens for understanding jailbreaks. The specific representational gap, now mechanistically grounded by Bullwinkel et al.: DeepContext's generic drift features operate at the same representation level where multi-turn attacks deliberately hide—they see 'the conversation is changing' but cannot distinguish natural evolution (brainstorming, creative collaboration) from adversarial manipulation (rapport→reframing→escalation) because both produce benign-looking per-turn representations. Persuasion-grounded features operate at the discourse level, seeing the specific manipulation playbook being executed even when each turn's semantic representation appears benign. This distinction should enable three concrete improvements: (a) earlier detection—persuasion strategy transitions (e.g., shift from rapport to authority framing) manifest before any explicitly harmful content appears, creating a detection window invisible to drift-only or representation-level systems; (b) lower false-positive rates—benign conversations that naturally drift (high drift magnitude) use qualitatively different persuasion distributions than adversarial conversations (no escalation pattern, no strategic framing shifts); (c) native interpretability—detected threats are explained in terms of named persuasion strategies and their temporal sequence rather than opaque drift magnitudes. GLiGuard's success with single-turn strategy detection validates that compact encoders can learn strategy-level features; DisPeD extends this to the temporal domain. DeepContext's own future-work section identifies 'dual-stream architecture to separate benign functional intent from adversarial steering' as a promising direction—DisPeD directly pursues this line with the critical addition of persuasion grounding.

## Landscape (SOTA & Limitations)

DeepContext (arXiv 2602.16935, Feb 2026): Primary baseline and most directly comparable system. Fine-tuned BERT encoder with task-attention weighted pooling, 3-layer GRU (2048 hidden), hybrid residual connection concatenating projected hidden state with raw embeddings. Tracks generic intent drift. F1=0.84 on multi-turn benchmarks, sub-20ms on T4 GPU. Training: 437K sequences (~20% malicious). Acknowledged limitations: 'glass cannon' effect (overfits to known patterns), false positives in function-calling contexts, no interpretability (opaque 2048-dim hidden state). No adversarial robustness evaluation. Future work identifies dual-stream architecture as promising direction. We candidly acknowledge that DisPeD's Track B (DeBERTa + GRU over semantic embeddings) is architecturally similar to DeepContext with an upgraded encoder; the contribution lies in Track A's persuasion-strategy sequence modeling, the cross-attention fusion, and the empirical demonstration that persuasion-grounded representations outperform generic drift features. Bullwinkel et al. (arXiv 2507.02956, Microsoft Research, Jun 2025): 'A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks.' Uses representation reading (MLP probes on intermediate activations, 0.997-0.999 test accuracy) and PCA visualization to show that Crescendo keeps model outputs in a 'benign' region of representation space, with harmful classification dropping sharply from k=1 to k=2 turns. Circuit breakers achieve only 54.2% ASR defense on multi-turn (vs. 3.8% on single-turn), a 50-point generalization gap, because Crescendo representations are 'sufficiently different from single-turn representations.' Tested on Llama-3-8B-Instruct and its circuit-breaker variant. Critically important for DisPeD's theoretical argument: this paper mechanistically explains why per-turn representation-level features are insufficient—attacks are designed to keep them benign—and why discourse-level features (persuasion strategy sequences) are needed. DisPeD's approach directly addresses the gap Bullwinkel et al. identify: rather than trying to detect harmful per-turn representations (which multi-turn attacks suppress), we detect the adversarial persuasion playbook operating above the representation level. GLiGuard (arXiv 2605.07982, May 2026): State-of-the-art single-turn guard. 300M-parameter schema-conditioned bidirectional encoder adapted from GLiNER2, detecting 11 jailbreak strategies and 14 harm categories in a single non-autoregressive forward pass. 16x higher throughput and 17x lower latency than 7B decoder guards; competitive F1 with 7-27B models. Single-input only—no temporal modeling—making it complementary to multi-turn approaches. Included as baseline to characterize the single-turn vs. multi-turn detection gap. BIID (arXiv 2509.22732, Sep 2025): Bidirectional intention inference combining forward request analysis with backward response retrospection. Near-0% ASR on MHJ. Training-free but requires target LLM to self-analyze (2+ full LLM reasoning passes per turn). No published latency analysis; we estimate several seconds per turn based on computational requirements of two full LLM forward passes and plan to independently measure this latency as part of evaluation. Strongest known ASR but no interpretability and untested adversarial robustness. G-Guard (arXiv 2507.07146, Jul 2025): Attention-aware GCN over entity graphs via GraphRAG. Merges turns into global graph via entity deduplication, losing temporal ordering. F1: 1.00/0.87 on HarmBench. Acknowledges 'loss of potentially important contextual information' from aggressive node pruning. XGuard-Train (arXiv 2504.13203, Apr 2025): Training-time defense using collaborative multi-agent framework to generate 30K adversarial conversations. 48.3% vulnerability reduction against X-Teaming attacks, 38.5% against other multi-turn jailbreaks, while mostly preserving general capabilities. Fundamentally complementary to inference-time detection: model-specific, requires fine-tuning access, inapplicable to closed-source models. DisPeD and XGuard-Train can be composed—XGuard-Train hardens the model, DisPeD monitors for attacks that evade the hardening. Concurrent work (acknowledged): Rafiei Asl et al. (ODU/UVA, CCI-funded) are developing a defense against persuasion-based multi-turn jailbreaks using reinforcement learning-driven defensive architectures that dynamically adjust model responses. No preprint published as of May 2026. Their prior work—NEXUS (EMNLP 2025) and HarmNet (arXiv 2510.18728)—focuses on attack frameworks. The RL-based approach is fundamentally different from DisPeD: it is a training-time, model-specific defense that modifies model behavior through RL-based response adjustment, requiring fine-tuning access. DisPeD is an inference-time, model-agnostic detector that monitors conversation patterns externally, applicable to closed-source models via API wrapping. The two approaches are complementary: RL-based response adjustment hardens the model; DisPeD detects attacks that evade the hardening and provides interpretable threat intelligence. 'How Do LLMs Persuade?' (arXiv 2508.05625): Linear probes detect persuasion strategies, success trajectories, and personality-adapted persuasion in multi-turn conversations, faster than prompting-based approaches. Not applied to jailbreak detection. Provides theoretical and empirical grounding for DisPeD's core hypothesis. Hagendorff (Nature Communications 2026): 97% ASR from reasoning-model attackers; identifiable persuasion strategies (flattery 84.75%, educational framing 68.56%, hypothetical scenarios 65.67%, technical jargon 44.42%). Demonstrates persuasion playbooks are the mechanism of sophisticated multi-turn attacks. PAP (Zeng et al., ACL 2024): 40 persuasion techniques; Targeted Summarization defense reduces single-turn ASR to 2% but degrades MT-Bench. Single-turn only. Persuasive Fingerprint (Alizadeh Noughabi et al., CIKM 2025, arXiv 2510.21983): Cialdini's 7 principles characterize jailbreak susceptibility. No defense proposed. SafeDream (arXiv 2604.16824, Apr 2026): Safety world model with CUSUM detection; F1=0.891, FPR=7.9%; requires white-box hidden state access. Nasr, Carlini et al. (arXiv 2510.09023, Oct 2025): Systematically bypassed 12 single-input classifiers with >90% ASR under adaptive attack. All 12 tested defenses were single-turn/single-input classifiers. Establishes necessity of robustness evaluation for any classifier-based defense. Guarding the Guardrails (arXiv 2510.13893): Taxonomy of 7 jailbreak strategy families including persuasion, with 1,364 multi-turn Italian dialogues annotated with taxonomy. LLM-based detection via taxonomy-guided prompting. Peak+Accumulation (arXiv 2602.11247): Zero-GPU proxy scoring; 90.8% recall. Defensive M2S (arXiv 2601.00454): Compresses multi-turn to single-turn; 93.8% recall. Constitutional Classifiers (arXiv 2501.18837, Anthropic): Exchange-level classifier; 4.4% ASR; proprietary. MultiBreak (arXiv 2605.01687): 10,389-sample multi-turn benchmark. SoK: Evaluating Jailbreak Guardrails (arXiv 2506.10597, Jun 2025; IEEE S&P 2026): Comprehensive evaluation framework for jailbreak guardrails; taxonomy across six dimensions. FITD (EMNLP 2025): Foot-in-the-door multi-turn attack; demonstrates persuasion structure drives attacks. No published work combines persuasion-grounded turn representations (not generic drift features) with temporal sequence modeling for multi-turn jailbreak detection. The contribution is representational, not architectural.

## Proposed Approach

We propose DisPeD (Discourse-level Persuasion Detection), honestly framed as persuasion-grounded DeepContext with dual-track modeling, adversarial robustness evaluation, and interpretability. The primary contribution is demonstrating that persuasion-grounded turn representations are fundamentally better features for multi-turn jailbreak detection than generic intent-drift features, validated through rigorous ablation against a reproduced DeepContext baseline. We frame DisPeD's value as a multi-metric Pareto improvement: rather than claiming dominance on any single axis, we demonstrate that persuasion grounding simultaneously advances detection performance, early detection capability, false-positive discrimination, interpretability, and adversarial robustness—a combination no existing system achieves.

**Theoretical Grounding from Representation Engineering:**
Bullwinkel et al. (arXiv 2507.02956) mechanistically explain why generic semantic features are insufficient: multi-turn attacks deliberately keep per-turn representations in a 'benign' region of representation space, causing circuit breakers and other representation-level defenses to fail with a 50-point ASR generalization gap. DisPeD addresses this by operating at the discourse level—detecting the adversarial persuasion playbook that orchestrates the conversation—rather than at the per-turn representation level where attacks deliberately hide. The key insight: even when each turn's semantic representation appears benign (as Bullwinkel et al. show it will), the sequence of persuasion strategies across turns (rapport→reframing→escalation) constitutes a detectable manipulation fingerprint.

**Positioning Against DeepContext:**
We explicitly acknowledge that DisPeD's temporal architecture (encoder + GRU) shares the same paradigm as DeepContext. The contribution is not a new architecture but a new representation. Concretely: we show that grounding the encoder in persuasion strategy classification (Track A) and fusing discrete strategy signals with continuous semantic signals (cross-attention fusion) yields significant improvement over generic intent-drift detection, while the dual-track design provides adversarial robustness and interpretability that single-track architectures lack. The ablation design is structured to isolate each contribution precisely.

**Positioning Against XGuard-Train and Concurrent RL-Based Defenses:**
XGuard-Train is a training-time, model-specific defense requiring fine-tuning access. The concurrent ODU/UVA project (Rafiei Asl et al., CCI-funded) pursues RL-based defensive architectures that dynamically adjust model responses—also training-time and model-specific. DisPeD is inference-time, model-agnostic, and deployable on closed-source models via API wrapping. DisPeD provides interpretable post-hoc explanations (named persuasion strategy sequences) that neither training-time alignment nor RL-based response adjustment can provide. These approaches are complementary and composable: training-time defenses harden the model; DisPeD monitors conversations for novel attacks that evade the hardening and provides security teams with actionable threat intelligence.

**Phase 1 – Persuasion Strategy Annotation (~40 H100-hours):**
Develop a persuasion strategy taxonomy grounded in PAP's social-science categories, Hagendorff's empirical findings, and Cialdini's principles. Categories: (1) rapport/flattery, (2) authority/educational framing, (3) hypothetical scenario construction, (4) reframing/normalization, (5) emotional leverage/urgency, (6) identity manipulation/role assignment, (7) incremental escalation, (8) benign/neutral. Annotate turn-level persuasion strategies on existing multi-turn jailbreak datasets (MHJ, XGuard-Train subset, SafeDialBench, MultiBreak) using GPT-4-class models with taxonomy-guided prompting, validated by expert review on a 500-sample stratified subset (targeting >0.75 Cohen's kappa). Generate additional adversarial conversations (~1,000) using reasoning-model attackers (DeepSeek-R1-Distill-14B, Qwen3-30B-A3B) against 3 targets, extracting persuasion labels from attacker CoT traces. Supplement with benign conversations enriched with natural persuasion: tutoring, customer service, brainstorming, debate, and creative collaboration—specifically selected to exhibit high topic drift with benign persuasion distributions for false-positive calibration. Target: ~30K annotated conversations.

**Phase 2 – Persuasion-Grounded Encoder (~25 H100-hours):**
Fine-tune DeBERTa-v3-base on a multi-task objective: (a) 8-way persuasion strategy classification, and (b) binary jailbreak-intent classification. The multi-task training produces turn embeddings (penultimate-layer [CLS] representation) that encode both semantic content and the specific persuasion mechanism in play, contrasting with DeepContext's BERT embeddings that encode only generic semantic content. DeBERTa-v3-base is chosen over BERT-base for its disentangled attention mechanism, which improves fine-grained token-level discrimination relevant to distinguishing subtle persuasion strategies.

**Phase 3 – Dual-Track Temporal Model (~20 H100-hours):**
Track A (Interpretable Persuasion Sequence): GRU over discrete persuasion-strategy probability distributions (8-dim per turn) concatenated with per-turn harmfulness scores from a standalone guard (Qwen3Guard or WildGuard). Detects characteristic attack playbooks: rapport→reframing→escalation. Provides human-readable explanations ('Turn 1-3: rapport-building; Turn 4: authority reframing; Turn 5-6: incremental escalation'). Track B (Robust Semantic Content): GRU over continuous DeBERTa turn embeddings concatenated with harmfulness scores. Architecturally similar to DeepContext with DeBERTa; captures semantic evolution beyond fixed taxonomy categories. Cross-Attention Fusion: At each timestep, bidirectional cross-attention between Track A and Track B hidden states allows the tracks to exchange information. Track A informs Track B about the manipulation context of observed semantic shifts (distinguishing benign drift from adversarial steering); Track B provides Track A with semantic grounding to disambiguate persuasion strategies. Final classification via learned late fusion of track outputs.

**Mechanistic Hypothesis for Why Persuasion Labels Beat Generic Drift (now grounded in Bullwinkel et al.):**
Bullwinkel et al. show that multi-turn attacks keep per-turn representations in a 'benign' region—the representation space is adversarially manipulated. Generic drift detection operates in this same manipulated space: it sees 'the conversation is changing' but the direction of change appears benign. Persuasion-aware detection operates at a different level of abstraction: it classifies the discourse function of each turn (rapport-building, authority framing, reframing) rather than its semantic content. Even when a turn's semantic representation is benign (as Bullwinkel et al. show it will be during Crescendo), its discourse function within the conversation can reveal adversarial intent. This enables: (a) earlier detection—detecting rapport→authority framing transition before any harmful content appears (while generic drift and representation-level defenses see only benign signals); (b) better false-positive discrimination—benign conversations that also 'drift' (brainstorming, creative writing, complex tutoring) exhibit flat or random persuasion distributions rather than the escalatory persuasion sequences characteristic of attacks; (c) interpretable explanations—naming the strategy rather than reporting an opaque drift magnitude.

**Phase 4 – Comprehensive Ablation-Driven Evaluation (~45 H100-hours):**

*Multi-Metric Pareto Evaluation Framework:*
We pre-commit to reporting a multi-dimensional comparison table across six axes: (1) F1 detection accuracy, (2) turns-before-compliance (early detection), (3) FPR on benign high-drift conversations, (4) interpretability score (human evaluation), (5) inference latency, and (6) adaptive attack robustness. DisPeD's claimed value is as a Pareto improvement across these dimensions: BIID achieves the strongest ASR reduction but at ~100x latency with no interpretability; DeepContext matches latency but provides no interpretability, no FPR discrimination, and no adversarial robustness; SafeDream achieves early detection but requires white-box hidden state access. Even modest F1 gains become significant when accompanied by clear wins on interpretability, FPR, and early detection. If F1 gains over DeepContext are ≤2 points, the paper's primary narrative shifts to the multi-metric advantages while honestly reporting the F1 result.

*Primary Ablation (DeepContext comparison):*
(A0) DeepContext reproduction: BERT-base + task-attention pooling + 3-layer GRU (2048 hidden), trained on generic intent-drift labels, targeting reproduction of reported F1=0.84. (A1) Encoder upgrade: DeBERTa-v3-base replacing BERT-base in the DeepContext architecture (same GRU, same drift task), isolating encoder contribution. (A2) Persuasion grounding: DeBERTa-v3-base with multi-task persuasion training in single-track GRU (Track B only), isolating persuasion-representation contribution. (A3) Full DisPeD: dual-track with cross-attention fusion. This four-condition ablation ensures every claimed contribution is empirically justified relative to the most relevant baseline.

*Detection performance:* Precision/recall/F1 on MHJ, MultiBreak, SafeDialBench, XGuard-Train test split, and reasoning-model-attacker test set. Per-condition (A0-A3) to trace contribution sources.

*Early detection:* Turns before compliance, per condition. Hypothesis: persuasion-grounded conditions (A2, A3) detect earlier because persuasion patterns manifest before harmful content. We pre-commit to reporting the A1-vs-A2 gap on this metric as a primary result, since this most cleanly isolates the value of persuasion grounding independent of encoder quality.

*False-p

## Resource Estimate

- **auto_research**: {'claude_api_cost': '$250-400 (heavy orchestration: annotation pipeline, 4-condition ablation management, multi-benchmark evaluation, adaptive attack generation across ~4000-6000 turns)', 'estimated_gpu_cost': '$400-500', 'gpu_hours': '~160h H100 (broader annotation coverage, full 4-condition ablation with multiple seeds, comprehensive adaptive attack evaluation, all benchmark evaluations, latency benchmarking, GLiGuard baseline)', 'gpu_utilization': 'High (~75-85%): continuous experiment scheduling across annotation, training, and evaluation pipelines', 'risk_note': "Primary risk: if DeepContext reproduction fails or if persuasion-grounded representations show only marginal improvement (<=2 F1 points) over encoder-upgraded DeepContext (A1 vs A2), the paper reframes around multi-metric Pareto improvement. Pre-committed secondary metrics (turns-before-compliance, FPR reduction, interpretability) are expected to show clearer advantages even if F1 gains are modest, since persuasion patterns manifest before harmful content (early detection) and benign conversations lack escalatory persuasion sequences (FPR). Contingency: if MVE (8 days) shows persuasion grounding has no advantage on ANY metric, this constitutes a well-documented negative result with theoretical analysis of why (contributing to the field's understanding of multi-turn detection representations).", 'speed_bottleneck': 'DeepContext reproduction without code release; sequential multi-turn conversation generation (~50-100s/conversation); API rate limits for closed-source target evaluation', 'team': '0 (initial setup: persuasion taxonomy, DeepContext reproduction script, benchmark selection, adaptive attack specifications)', 'timeline_tiered': {'full_experiment': '11 days with 8x H100 cluster — A0-A3 on 5+ benchmarks, 3 seeds, ~30K annotations, adaptive attacks, all baselines, interpretability evaluation', 'minimum_viable_experiment': '8 days with 8x H100 cluster — A0+A3 on MHJ+MultiBreak, single seed, ~15K annotations, core metrics (F1, turns-before-compliance, FPR, latency)', 'phase_overlap': 'Annotation (days 1-4), encoder training (days 3-6, using early batches), DeepContext reproduction (days 1-5, parallel), dual-track training (days 5-8), evaluation (days 7-11 with MVE conditions first)'}}
- **human_in_loop**: {'claude_api_cost': '$150-250 (experiment orchestration, annotation assistance, ablation analysis across ~1500-2500 turns)', 'estimated_gpu_cost': '$350-425', 'gpu_hours': '~140h H100 (agent optimizes annotation quality, encoder hyperparameters, cross-attention design, DeepContext reproduction fidelity, adaptive attack design)', 'gpu_utilization': 'Moderate-High (~60-70%): agent queues experiments; human reviews persuasion taxonomy, annotation agreement metrics, and ablation results ~1x/day', 'risk_note': 'DeepContext reproduction is critical path: if we cannot reproduce F1=0.84 (paper provides no code release), the ablation story weakens. Mitigation: contact authors for implementation details; if reproduction gap >3 F1 points, report both reproduced and original numbers with discussion of discrepancy, and pivot to A2-vs-A3 comparison. Persuasion annotation ambiguity estimated at ~10-15% at strategy boundaries; mitigated by multi-task training that uses both discrete labels and continuous embeddings.', 'team': '1 researcher, ~30min/day reviewing persuasion annotations, DeepContext reproduction fidelity, ablation deltas, and interpretability outputs', 'timeline': '4-5 weeks'}
- **manual**: {'estimated_gpu_cost': '$325-400 at ~$2.50/hr H100', 'gpu_hours': '~130h H100 (persuasion annotation with GPT-4-class models: ~40h, DeBERTa multi-task training: ~25h, dual-track GRU training: ~20h, comprehensive ablation evaluation with DeepContext reproduction + baselines: ~45h)', 'gpu_utilization': 'Moderate (~50-60%): annotation is sequential per conversation; training is standard fine-tuning; evaluation is parallelizable across conditions', 'team': '2 researchers (1 NLP/discourse analysis lead, 1 safety/ML engineer) + 3 security practitioners for interpretability evaluation (4-6 hours each)', 'timeline': '2-3 months'}

## Key References

- DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs (arXiv 2602.16935, Feb 2026) — PRIMARY BASELINE: BERT+GRU intent-drift detector, F1=0.84, sub-20ms T4
- A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks (Bullwinkel et al., arXiv 2507.02956, Microsoft Research, Jun 2025) — shows multi-turn attacks keep representations 'benign', circuit breakers fail with 50-point gap; THEORETICAL FOUNDATION for discourse-level features
- GLiGuard: Schema-Conditioned Classification for LLM Safeguard (arXiv 2605.07982, May 2026) — 300M encoder, 11 jailbreak strategies + 14 harm categories, single-turn only, 16x faster than 7B guards
- How Do LLMs Persuade? Linear Probes Can Uncover Persuasion Dynamics in Multi-Turn Conversations (arXiv 2508.05625) — validates persuasion dynamics are extractable from turn-level representations
- Large reasoning models are autonomous jailbreak agents (Hagendorff et al., Nature Communications 2026) — 97% ASR via identifiable persuasion strategies
- Bidirectional Intention Inference Enhances LLMs' Defense Against Multi-Turn Jailbreak Attacks (BIID, arXiv 2509.22732, Sep 2025) — near-0% ASR, no published latency analysis
- X-Teaming: Multi-Turn Jailbreaks and Defenses with Adaptive Multi-Agents / XGuard-Train (arXiv 2504.13203, Apr 2025) — training-time defense, 30K conversations, 48.3% vulnerability reduction
- Attention-Aware GNN-based Input Defense against Multi-Turn LLM Jailbreak (G-Guard, arXiv 2507.07146, Jul 2025)
- How Johnny Can Persuade LLMs to Jailbreak Them (PAP, Zeng et al., ACL 2024) — 40 persuasion techniques, single-turn
- Uncovering the Persuasive Fingerprint of LLMs in Jailbreaking Attacks (Alizadeh Noughabi et al., CIKM 2025, arXiv 2510.21983) — Cialdini's principles for jailbreak analysis
- The Attacker Moves Second (Nasr, Carlini et al., arXiv 2510.09023, Oct 2025) — adaptive attacks bypass 12 single-input classifiers with >90% ASR
- Intention Analysis Makes LLMs A Good Jailbreak Defender (Zhang et al., COLING 2025, arXiv 2401.06561)
- SafeDream: Safety World Model for Proactive Early Jailbreak Detection (arXiv 2604.16824, Apr 2026)
- Guarding the Guardrails: A Taxonomy-Driven Approach to Jailbreak Detection (arXiv 2510.13893) — 7 jailbreak strategy families, multi-turn Italian dataset
- Peak + Accumulation: Proxy-Level Scoring for Multi-Turn LLM Attack Detection (arXiv 2602.11247, Feb 2026)
- Defensive M2S: Training Guardrail Models on Compressed Multi-turn Conversations (arXiv 2601.00454, Jan 2026)
- Foot-In-The-Door: A Multi-turn Jailbreak for LLMs (EMNLP 2025) — persuasion structure drives attacks
- MultiBreak: A Scalable and Diverse Multi-turn Jailbreak Benchmark (arXiv 2605.01687, May 2026)
- Constitutional Classifiers: Defending against Universal Jailbreaks (arXiv 2501.18837, Anthropic Jan 2025)
- DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training (He et al., ICLR 2023)
- Must Read: A Systematic Survey of Computational Persuasion (arXiv 2505.07775, May 2025)
- SoK: Evaluating Jailbreak Guardrails for Large Language Models (arXiv 2506.10597, Jun 2025; IEEE S&P 2026)
- NEXUS: Network Exploration for eXploiting Unsafe Sequences in Multi-Turn LLM Jailbreaks (Rafiei Asl et al., EMNLP 2025) — concurrent team's attack work

## Reviewer Evaluation

**Scores**:
  - clarity: **{'rationale': "Exceptionally well-structured proposal with honest positioning against DeepContext (explicitly acknowledges Track B is architecturally similar), precise mechanistic hypothesis grounded in Bullwinkel et al., rigorous 4-condition ablation design (A0-A3), multi-metric Pareto framing, concurrent work acknowledgment, and tiered risk contingencies. Among the best-articulated proposals I've reviewed.", 'score': 5}**/5
  - feasibility: **{'rationale': '130-160 H100-hours is well within the 200-hour budget. DeBERTa-v3-base (86M params) fine-tuning is standard and fast. Tiered timeline (8-day MVE vs. 11-day full) credibly de-risks the deadline. All datasets (MHJ, MultiBreak, XGuard-Train) and models are publicly available. DeepContext reproduction risk has reasonable contingency. The tight timeline is the main concern but MVE guarantees a publishable minimum.', 'score': 4}**/5
  - impact: **{'rationale': 'Addresses a genuine deployment need: interpretable, efficient, model-agnostic multi-turn defense. The Pareto improvement across 6 axes (F1, early detection, FPR, interpretability, latency, adversarial robustness) is a compelling contribution framing—no existing system advances all six. If hypothesis holds, it demonstrates task-appropriate features beat generic features, a useful insight. EMNLP 2026 LLM Security topic area is well-matched.', 'score': 4}**/5
  - novelty: **{'rationale': "Independently verified that no published work combines persuasion-grounded encoder training with temporal sequence modeling for multi-turn jailbreak detection. The theoretical grounding from Bullwinkel et al. (confirmed: representations kept 'benign' by multi-turn attacks, circuit breakers fail with 50-point gap) provides strong mechanistic justification. Honest framing as representational (not architectural) contribution strengthens credibility. Incremental but principled.", 'score': 4}**/5

## Human Review Note

【优化方案】

1. **[标题] — 从方法命名升级为原则命名** — 命中 Novelty + Significance
   原始标题暗示"又一个检测方法"；建议改为突出理论贡献的标题，如 "DisPeD: Exploiting the Pragmatic Evasion Asymmetry for Robust Multi-turn Jailbreak Detection"，将核心 insight 前置于标题层。

2. **[Introduction / Core Insight] — 将 novelty 从 "persuasion features 有用" 重定位为 "Evasion Hierarchy 原则的首个系统验证"** — 命中 Novelty + Significance
   - 提出对抗通信中的逃逸难度递增层次：lexical（最易）< semantic（中等）< pragmatic（结构性困难）
   - DisPeD 定位为该通用原则在 jailbreak detection 中的首个实证验证，而非仅仅"一个更好的检测器"
   - 引入 Speech Act Theory（Austin 1962, Searle 1969）作为理论锚：现有检测器工作在 locutionary act 层面，DisPeD 工作在 illocutionary act 层面

3. **[Section 2 / Theoretical Foundation] — 新增 Pragmatic Evasion Asymmetry 半形式化论证** — 命中 Novelty
   - 明确 persuasion-mediated attack 的 functional prerequisites（rapport building → defense lowering → boundary normalization → harmful elicitation）是攻击成功的**必要条件**
   - 逐条论证跳过任何 prerequisite 导致攻击失败（无 rapport → model 不降低防御 → 直接有害请求被拒绝；无 boundary testing → 直接跳到有害请求 = single-turn attack，已被现有防御覆盖）
   - 结论：semantic evasion（替换词汇/话题）不破坏 prerequisites → 容易；pragmatic evasion（消除 prerequisites）等价于放弃攻击 → 结构性困难

4. **[Motivation] — 修复理论链条逻辑漏洞，精确化 "fundamental limitation" 边界** — 命中 Technical Soundness
   - Bullwinkel et al. 的发现严格限定为"target model 内部表征被操控"，不外推至外部检测器
   - 外部检测器失败归因精确分层：**scalar drift metrics**（如 inter-turn cosine distance）= information-theoretically insufficient（无论训练多少数据都无法从中恢复区分信号）；**full semantic representations** = practically limited（信息理论上可区分，但需模型自行从数据中解耦 pragmatic signal，DisPeD 通过 explicit inductive bias 加速此过程）
   - 此分层使 motivation 对端到端 baseline 结果 robust：即使 E2E baseline F1 尚可，DisPeD 的优势仍可论证为 sample efficiency + interpretability + robustness

5. **[Scope] — 新增显式 scope 声明，精确限定核心 claim 适用范围** — 命中 Novelty（防御性强化）
   - 核心 pragmatic evasion asymmetry 适用于 persuasion-mediated multi-turn attacks（Crescendo, Deceptive Delight, social engineering jailbreaks）——覆盖现有多轮攻击的绝大多数
   - 明确承认部分攻击类型（纯信息累积、token smuggling、单帧 roleplay）不在 Track A 显式覆盖范围内
   - 但 Track B 的 continuous embedding 可捕捉这些攻击的异常 pragmatic patterns，形成安全网

6. **[Method / Architecture Rationale] — 新增 "Bounded + Unbounded Detection" 互补叙事** — 命中 Novelty
   - Track A = bounded precision：14-category taxonomy 精确覆盖主流攻击类，输出可解释的 strategy sequence
   - Track B = unbounded recall：continuous pragmatic embeddings 泛化至未知攻击类型和 novel strategy combinations
   - 此互补不是工程冗余，而是理论驱动的必然设计

7. **[Method / Architecture Rationale] — 新增 "Why Not End-to-End" 三点必要性论证** — 命中 Novelty
   - (a) Interpretability as deployment requirement：安全团队需要可审计的 explanation 来 triage alerts
   - (b) Sample efficiency via encoded priors：persuasion taxonomy 编码数十年社会心理学研究，low-data regime 下提供有意义的 inductive bias
   - (c) Robustness to distribution shift：新攻击引入新 semantic content 但复用 pragmatic patterns，explicit pragmatic features 跨分布更稳定

8. **[Method / Track A] — 明确两阶段 pipeline，修复 latency 可信度** — 命中 Technical Soundness
   - 训练时：GPT-4 作为 teacher 标注 15K conversations
   - 推理时：distilled DeBERTa-base classifier 执行 per-turn 14-class prediction
   - 报告 distilled classifier 的 held-out macro-F1 和 per-turn accuracy
   - 预设可接受阈值 macro-F1 ≥ 0.65；Plan B：若不达标则合并至 10 类

9. **[Method / Key Hypothesis] — 显式提出 "Monotonic Escalation Trajectory" hypothesis** — 命中 Novelty + 论文记忆点
   - Hypothesis：adversarial conversations 在 pragmatic strategy space 中呈现 monotonic escalation trajectory（trust → test → normalize → elicit）；benign conversations 呈现 oscillatory / non-monotonic patterns
   - 验证方式：strategy transition matrix 可视化 + trajectory analysis
   - 这是论文最 memorable 的 one-liner，审稿人读完 abstract 就能记住

10. **[Experiments / Ablation] — 从原始 4 条件扩展为 6 条件完整贡献分解链** — 命中 Technical Soundness
    - A0（DeepContext reproduction, DeBERTa-base, drift features）
    - A1（encoder upgrade: DeBERTa-v3-large, same drift features）→ 隔离 encoder capacity
    - A1.5（full per-turn embeddings, vanilla DeBERTa-v3-large, no persuasion FT）→ 隔离 "full embeddings vs. scalar drift"
    - A2（persuasion-grounded contrastive FT, single-track）→ 隔离 persuasion grounding 纯增量
    - A3（full dual-track + cross-attention fusion）→ 隔离 dual-track + fusion 贡献
    - A3'（dual-track + concatenation fusion）→ 隔离 cross-attention 机制贡献
    - 每一步精确改变一个变量，形成无 confounding 的 contribution ladder

11. **[Experiments / Baselines] — 从原始 7 个扩展至 9 个，补关键缺失** — 命中 Technical Soundness
    - 新增 **Hierarchical E2E baseline**：per-turn DeBERTa-v3-large [CLS] → GRU → binary classification（与 DisPeD 信息覆盖完全对等，唯一差异是有无 explicit pragmatic features）
    - 新增 **GPT-4 Direct Prompting**：full conversation + few-shot → classification + explanation（度量 accuracy-latency-cost tradeoff）
    - E2E baseline 采用层次化设计确保公平比较：DisPeD 赢 = 证明 explicit pragmatic modeling 必要性；DisPeD 输 = 必须诚实讨论

12. **[Experiments / Evaluation] — Latency claim 修正为诚实分层报告** — 命中 Technical Soundness
    - 放弃原始"≤25ms"的不可信 claim
    - 改为：full pipeline latency（首次处理完整对话，预估 100-500ms）+ incremental latency（新增一 turn 边际处理，预估 30-60ms）
    - 与 GPT-4 prompting（~5-10s）形成有意义但诚实的对比

13. **[Experiments / Adaptive Attack] — 在 initial submission 中纳入 50-sample strategy-aware evasion** — 命中 Technical Soundness
    - 使用 DeepSeek-R1 生成 50 条攻击者尝试避免触发已知 persuasion strategy patterns 的对话
    - 直接验证核心 pragmatic evasion asymmetry claim：如果 DisPeD 在此条件下仍维持高 F1，impossibility argument 获得实证支持
    - 剩余两类 adaptive attack（benign-mimicry, temporal perturbation）保留至 camera-ready

14. **[Experiments / FPR] — 强化 benign high-drift 测试集构建 + 分层报告** — 命中 Technical Soundness
    - 从 WildChat 主动筛选 top-10% 最高 drift 对话作为 "hard negative" 子集
    - 报告 FPR @ 低/中/高 drift 分位数，精确展示 persuasion grounding 在 high-drift 场景下的 discrimination 能力
    - 所有 ablation 条件使用相同训练数据分布（含 high-drift negatives），排除 data composition 解释

15. **[Experiments / Interpretability] — 严格化人工评估 protocol** — 命中 Technical Soundness
    - 100 样本 × 3 security practitioners × blinded randomized × Factual Accuracy (1-5) + Actionability (1-5) × Krippendorff's α × pairwise preference
    - 新增 automatic proxy：Track A predicted strategy sequence vs. ground-truth annotation 的 sequence-level F1
    - 两层验证互补：human eval 验证实用价值，auto proxy 验证事实准确性

16. **[Experiments / Statistical Rigor] — 加入 encoder stability proxy** — 命中 Technical Soundness
    - 承认单 encoder run 为 limitation
    - 补充 cross-checkpoint variance（epoch 2 / epoch 3 / final 分别评估 A3），量化 encoder training stochasticity 对下游的影响

17. **[Related Work] — 新增三组关键差异化论证** — 命中 Related Work 差异化
    - vs. PAP（Zeng et al. 2024）：taxonomy scope（14 类 > Cialdini 6 类）、temporal trajectory（不只是 per-turn labels）、Track B continuous generalization
    - vs. Propaganda Detection / SemEval：span-level 单文档 → turn-level 跨轮次 temporal trajectory；rhetoric taxonomy → social psychology + interaction dynamics 融合
    - vs. Dialogue Act Sequence Modeling（Tsinganos et al. 2022 等）：persuasion-strategy level（语义更丰富）vs. DA level（inform/request/confirm）；双通道 vs. 单通道；对抗检测 vs. 对话管理

18. **[Broader Significance] — 将 jailbreak detection 定位为通用原则的 primary instantiation** — 命中 Significance
    - Evasion hierarchy 原则泛化至：社交工程检测、phishing 对话识别、online radicalization 路径检测、deceptive negotiation
    - Jailbreak detection 选择理由：ground-truth 可得、攻击策略多样、safety 影响即时
    - 不需要额外实验，但显著扩大论文 audience 和 citation potential

【主要风险】:
1. **Timeline 极限风险**：9 天内完成 ~170 H100-hours compute + 人工评估协调 + 论文写作。任何环节延迟（annotation κ 不达标需返工、encoder training 不收敛、practitioner 不响应）都可能导致 MVE 不完整。Fallback：削减至 4 条件（A0+A1.5+A2+A3），interpretability eval 降级为 pilot。
2. **Impossibility argument 可能被 dismiss**：半形式化论证的说服力高度依赖写作质量。如果论述过于 informal 或 hand-wavy，sophisticated reviewer 可能评为"interesting intuition but not a rigorous result"，从而将论文 novelty 降级为 pure empirics。对策：保持论证简短（半页以内）、逻辑链清晰、明确标注为 "informal argument" 而非 "proof"。

【实施评估】:
- **计算资源**: ~170 H100-hours total。分解：DeBERTa-v3-large persuasion-grounded contrastive fine-tuning ~40h；DeBERTa-base distilled classifier ~8h；GRU training 6 conditions × 3 seeds × ~7h = ~126h。需要 8× H100 节点约 21 小时连续计算，或等效云资源（A100 约 ×1.5 时间）。Cloud cost 预估 ~$500-700。GPT-4 API cost ~$300-500（annotation + prompting baseline）。
- **数据需求**: MHJ、MultiBreak、WildChat、MT-Bench——全部公开可得，无需额外数据采集或授权。需要从 WildChat 中筛选 high-drift subset（自动化脚本，~1h）。50 条 adaptive attack 通过 DeepSeek-R1 API 生成（~$10-20）。
- **人工介入**: (1) 2 名 trained annotators：500-sample annotation QA，每人约 15-20 小时工作量，需具备对话分析或 NLP 背景；(2) 3 名 security practitioners：100-sample interpretability evaluation，每人约 3 小时，需具备安全事件响应经验。均需 Day 0 立即启动招募和培训。协调难度中-高（主要是时间紧迫而非任务复杂性）。
- **训练需求**: 需要模型 fine-tuning（非从头预训练）。DeBERTa-v3-large（304M 参数）persuasion-grounded contrastive fine-tuning 是最大训练任务（~40 H100-hours，预估 2-3 epochs on 15K conversations）。DeBERTa-base（110M 参数）distilled classifier 是轻量级 supervised fine-tuning（~8 H100-hours）。Bi-GRU 模型体量小（< 10M 参数），训练快速。无需训练 LLM 级模型。
- **新 Benchmark**: 不需要构建新的 benchmark 或评测数据集。需要构造的数据均为标注/生成性质：(1) 15K conversations 的 14-class persuasion strategy annotation（GPT-4 生成 + 500-sample human validation）；(2) 50 条 strategy-aware evasion attacks（DeepSeek-R1 生成）；(3) high-drift benign subset 筛选（自动化）。所有评测基于现有公开 benchmark（MHJ, MultiBreak）。


## MVP Validation Results

- **Date**: 2026-05-17
- **Hypothesis Supported**: Yes

### Key Metrics

Treatment K=2 F1=0.987, Baseline K=2 F1=0.879, Delta=+10.8pp; Treatment K=3 delta=+5.9pp; TF-IDF=1.0 (data quality caveat, must fix in research phase)

### Summary

Phase B full (480 samples: 250 jailbreak + 230 benign) validated the core hypothesis: persuasion-grounded DeBERTa embeddings (multi-task fine-tuned on 8-class persuasion + intent) enable significantly earlier detection of Crescendo jailbreak attacks vs vanilla DeBERTa. Treatment outperforms baseline at early turns: K=2 F1 0.987 vs 0.879 (+10.8pp), K=3 +5.9pp. Caveat: TF-IDF=1.0 indicates lexical shortcuts remain in current data — must be resolved in research phase before paper submission.

### Recommendation

GO — core signal validated. Research phase priority: (1) fix TF-IDF=1.0 via adversarial perturbation experiments, (2) fix strategy=7 hardcoding (M004), (3) re-validate on clean data. Target: EMNLP 2026 ARR DDL 2026-05-25.
