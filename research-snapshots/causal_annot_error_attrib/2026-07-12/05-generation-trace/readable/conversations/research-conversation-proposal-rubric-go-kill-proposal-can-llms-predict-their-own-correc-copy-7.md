# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Can LLMs Predict Their Own Correc

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/58000b7c-d081-4a2b-9c38-633829e0398d.jsonl`
- **Structured JSON:** [`6d4b0e3c5ade58c1ea25.json`](../../sessions/6d/6d4b0e3c5ade58c1ea25.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T21:12:35.908Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T21:12:35.908Z",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction\n\n## Description\nWe investigate whether LLMs' internal representations can predict which of their errors are self-correctable, and whether this prediction enables selective correction that outperforms both ungated correction, the trivial 'Wait' baseline, and confidence-based routing. Prior work shows a faint correctability signal at the post-answer newline token (PANL) achieving only 0.614 AUROC with a single-layer linear probe — insufficient for reliable gating. We develop Enhanced Correctability Probes (ECP) that combine multi-layer ensemble stacking, multi-token features (PANL + last-answer-token + reasoning tokens), attention-entropy features, pre-Wait hidden-state features (informed by crosscoder analysis of Wait-token mechanisms, arXiv:2510.04128), and SAE-guided feature selection targeting the confounded feature intersection that bridges uncertainty and correctness (motivated by the functional dissociation finding of arXiv:2604.19974, where 68% of pure incorrectness features are causally inert). We begin with a Phase 0 pilot that directly tests whether multi-layer ensembling — which improved deception detection AUROC by up to 78% (arXiv:2604.13386, specifically on Harm-Pressure Knowledge in Llama-70B) — transfers to the fundamentally different task of correctability prediction. These probes gate a three-way decision: retain the original answer (likely correct), attempt correction including probe-selective Wait insertion (error detected, high correctability), or abstain (error detected, low correctability). This framework is distinguished from CoRefine's (arXiv:2602.08948) three-way routing — which uses output-level confidence, lacks genuine abstention, and is not correctability-aware — by using hidden-state probes, providing a genuine abstention option for unfixable errors, and explicitly predicting error fixability rather than confidence. Critically, we provide the first evaluation of the 'Wait' baseline on correct answers, measuring its previously-unknown overcorrection cost. We also conduct the first representational geometry and SAE feature decomposition analysis of correctability vs. correctness, testing whether correctability — a second-order property that depends not just on whether the model is wrong but on whether correction mechanisms can reach the right answer — shares the low-dimensional, linearly-separable structure that correctness exhibits (arXiv:2602.08159), requires higher dimensionality or non-linear boundaries, or depends disproportionately on the narrow confounded feature population identified by arXiv:2604.19974. This analysis, combined with error depth characterization (arXiv:2601.00828) and threshold analysis mapping probe quality to gating utility, ensures publishable contributions even if probe AUROC plateaus at marginal levels. We evaluate across Gemma-3-27B, Qwen-2.5-7B-Instruct, and Mistral-Small-3.2-24B on TriviaQA, MMLU, and GSM8K, comparing against eight baselines including ungated correction, Wait (universal and probe-selective), confidence-based routing (CoRefine-style and Reflective Confidence-style), PAG, and oracle gating. Our contributions are: (1) operationalizing correctability as a prediction target distinct from correctness, (2) the first pilot testing whether multi-layer ensembling transfers from deception to correctability, (3) the first hidden-state probe-based gating with genuine abstention for correctability-aware self-correction — distinguished from CoRefine's confidence-based routing by signal source, abstention capability, and correctability specificity, (4) the first representational geometry and SAE feature decomposition comparison of correctability vs. correctness, testing whether second-order properties have a different confounded-feature signature than first-order properties, and (5) establishing the conditions — including minimum probe quality thresholds — under which probe-gated correction outperforms simpler alternatives including confidence-based controllers.\n\n## Core Problem\nLLMs attempt correction on all detected errors equally, but ~64.5% of self-generated errors are uncorrectable. Recent work reveals a faint internal 'correctability' signal at the post-answer newline token (PANL), but it achieves only 0.614 AUROC on own-generated errors using a single-layer linear probe — barely actionable for reliable gating. Meanwhile, trivial interventions like appending 'Wait' reduce blind spots by 89.3% on known errors, but their overcorrection rate on correct answers is completely untested. Confidence-based controllers like CoRefine (arXiv:2602.08948) achieve efficient three-way routing (halt/rethink/explore-alternative) using output-level logprobs, but they do not distinguish between correctable and uncorrectable errors — treating all detected issues as potentially fixable. Critically, correctability is a second-order property — it depends not just on whether the model is wrong, but on whether the model's correction mechanism can reach the right answer — and recent SAE analysis (arXiv:2604.19974) reveals that uncertainty and correctness are encoded by functionally distinct feature populations, with only rare 'confounded' features bridging both signals. It is unknown whether correctability — which inherently requires engaging both axes — shares the favorable geometric properties (low dimensionality, linear separability) that correctness exhibits, or whether it requires targeting the narrow confounded feature intersection. Can enhanced multi-signal probes substantially improve correctability prediction, what is the representational relationship between correctability, correctness, and uncertainty at the feature level, and under what conditions does probe-gated correction with genuine abstention outperform both ungated correction and simpler confidence-based alternatives?\n\n## Opportunity\nThree converging findings create a clear research opportunity: (1) The PANL paper (arXiv:2604.22271) establishes that correctability is partially encoded in internal representations, but their single-layer, single-token linear probe barely exceeds chance (0.614 AUROC) on own-generated errors — leaving substantial room for improvement. For correctness prediction on adjacent tasks, Gnosis-style multi-signal fusion (arXiv:2512.20578) achieves 0.78–0.92 AUROC on hidden states alone (with the lower end on MMLU-Pro; ablation on Qwen3-1.7B only) and 0.80–0.95 with attention fusion, while attention-head entropy probes (arXiv:2602.13699) achieve +0.06 AUROC absolute improvement in OOD settings (0.70→0.76 average, 8.5% relative vs. Lookback Lens). Multi-layer probe ensembling (arXiv:2604.13386) has dramatically improved deception detection AUROC (0.510→0.910 on Harm-Pressure Knowledge in Llama-70B), though whether similar gains transfer to correctability — a fundamentally different property — is an open empirical question that motivates our pilot experiment. (2) The 'Wait' baseline from Self-Correction Bench (arXiv:2507.02778) is powerful but fundamentally non-selective: it was tested only on known errors, never on correct answers, so its overcorrection cost is unknown. QwQ-32B naturally generates 'Wait' as its first correction token 37.7–76.8% of the time depending on benchmark (SCLI5 to PRM800K-SC), but this behavior varies widely across models and is near-zero for non-reasoning models. Recent mechanistic work shows that internal states before Wait tokens causally modulate distinct reasoning patterns — restarting, recalling, uncertainty expression, and double-checking (arXiv:2510.04128, EMNLP 2025 Findings) — and that Wait token probabilities correlate with reasoning correctness in ways that vary by training strategy (arXiv:2601.17421). These findings suggest Wait's effectiveness is not uniform but depends on which reasoning pattern it triggers, creating an opportunity for probe-selective application. Reflective Confidence (arXiv:2512.18605) demonstrates a related approach, transforming low-confidence output signals into reflection triggers rather than stopping, achieving 83.3% accuracy on AIME 2025 vs. 70.0% for Self-Consistency — but uses only output-level logprobs, not internal representations. (3) Existing gating approaches occupy adjacent niches but leave a clear gap. CoRefine (arXiv:2602.08948) implements three-way routing (halt/rethink/alternative) via a 211K-parameter Conv1D controller on output-level confidence, achieving 92.6% halt precision — but its decisions are confidence-based rather than correctability-aware, and its ALTERNATIVE option explores different approaches rather than genuinely abstaining when errors are likely unfixable. Four concurrent probe-gating papers address correctness, early exit, abstention, or reflection control — but none probe for correctability (whether a specific error is fixable), and none combine hidden-state probes with genuine abstention in a correctability-aware framework. Moreover, the SAE dissociation paper (arXiv:2604.19974) reveals that uncertainty and correctness are encoded by functionally distinct feature populations — with 68% of pure incorrectness features being causally inert and only rare confounded features (102 out of 1,057 in Llama-3.1-8B) bridging both signals to achieve 0.79 AUROC with just 3 features. This finding directly challenges naive linear probing over broad activations and suggests correctability prediction may need to target the narrow confounded feature intersection, motivating our SAE-guided probe design and representational analysis.\n\n## Related Work / Landscape\nThe PANL paper (arXiv:2604.22271) establishes correctability prediction as a distinct task from error detection, achieving 0.986 AUROC for detection but only 0.614 for correctability on own-generated errors using single-layer logistic regression at one token position. This gap — high detectability but low correctability prediction — is the central technical challenge. Gnosis (arXiv:2512.20578) achieves 0.80–0.95 AUROC for correctness prediction by fusing final-layer hidden states with attention-map features via a ~5M-parameter architecture; notably, the hidden-state stream alone achieves 0.78–0.92 AUROC (with the lower end on MMLU-Pro; ablation only reported for Qwen3-1.7B), with attention fusion adding 0–3 points depending on the task. The multi-layer ensembling paper (arXiv:2604.13386) shows that logistic stacking across complementary layers can dramatically improve probe performance — achieving 0.510→0.910 AUROC on the hardest deception detection task (Harm-Pressure Knowledge, Llama-70B) — because informative directions rotate across layers and double-fault analysis reveals complementary error patterns between early and late layers. However, this result is specific to deception detection, which has different layer-wise encoding properties than correctness or correctability; whether analogous gains transfer is an empirical hypothesis we test via a Phase 0 pilot. For correctness prediction specifically, multi-signal approaches show more modest but consistent gains: attention-head entropy probes (arXiv:2602.13699) improve OOD AUROC by +0.06 absolute (0.70→0.76 average across 5 models, an 8.5% relative improvement over Lookback Lens), and perturbation-stability probes (arXiv:2505.21772) add +6 AUROC points via targeted adversarial perturbations to hidden states. SWIFT (arXiv:2505.12225) concatenates all-layer hidden states with learned gating weights to extract token-level quality signals.\n\nThe Self-Correction Bench (arXiv:2507.02778) documents the 64.5% blind spot and shows 'Wait' reduces it by 89.3%. QwQ-32B naturally generates 'Wait' as its first correction token at rates varying by benchmark (37.7% on SCLI5, 72.5% on GSM8K-SC, 76.8% on PRM800K-SC), but this behavior is model-specific — other reasoning models show different patterns and non-reasoning models rarely generate Wait spontaneously. The Wait baseline was never tested on correct answers, leaving the overcorrection cost unknown. Two recent papers provide mechanistic understanding of Wait tokens: arXiv:2510.04128 (EMNLP 2025 Findings) trains crosscoders on DeepSeek-R1-Distill-Llama-8B to identify features that promote or suppress Wait tokens, discovering causal features for distinct reasoning patterns (restarting, recalling, uncertainty expression, double-checking) via activation steering at layer 15; arXiv:2601.17421 systematically analyzes Wait and other discourse tokens across model scales and training strategies, finding that Wait token probabilities correlate with reasoning correctness but that models exploit this signal only partially. Reflective Confidence (arXiv:2512.18605) proposes a related approach, transforming low-confidence output-level logprob signals into reflection triggers rather than early stopping, achieving 83.3% accuracy on AIME 2025 (vs. 70.0% Self-Consistency, K=32) on Qwen3-8B — demonstrating that selective confidence-gated correction can significantly outperform non-selective baselines, though it uses output-level signals rather than internal representations and does not model correctability.\n\nCoRefine (arXiv:2602.08948) is the closest existing system to our three-way gating, implementing halt/rethink/alternative decisions via a 211K-parameter Conv1D controller that consumes output-level confidence traces from the frozen LLM. It achieves 92.6% halt precision, averages 2.7 refinement steps per problem, and reduces tokens ~190× relative to 512-sample baselines on mathematical reasoning benchmarks. However, CoRefine differs from our proposal in three fundamental ways: (a) it uses output-level logprobs rather than hidden-state probes, missing the richer internal signal that PANL demonstrates exists; (b) its HALT decision accepts the current answer — it never genuinely abstains or flags for external intervention when errors are likely unfixable; (c) its routing is confidence-based, not correctability-aware — it cannot distinguish correctable from uncorrectable errors, treating all low-confidence outputs as potentially improvable. Four concurrent probe-gating papers occupy adjacent niches: arXiv:2507.12379 probes for arithmetic errors and selectively re-prompts (only 6–12% of detected errors actually get corrected); arXiv:2504.05419 uses probes for early exit from reasoning chains (AUROC 0.77–0.91 for correctness, not correctability); arXiv:2604.18419 trains value-function probes for dynamic mid-generation abstention; arXiv:2506.12217 uses activation steering to modulate self-reflection frequency. None of these probe for correctability specifically, and none combine hidden-state probes with genuine abstention in a correctability-aware framework.\n\nA critical finding for our probing approach comes from arXiv:2604.19974, which uses sparse autoencoders to decompose LLM representations into functionally distinct feature populations. In Llama-3.1-8B, they identify 700 pure uncertainty features, 255 pure incorrectness features, and only 102 confounded features encoding both signals. The key insight is a functional dissociation: 68% of pure incorrectness features are causally inert (mean accuracy delta of -0.03% when suppressed), while pure uncertainty features are essential for model performance, and only confounded features bridging both axes are causally effective for correctness prediction — with just 3 confounded features from layer 18 achieving 0.79 AUROC. This has direct implications for correctability probing: correctability is inherently a joint uncertainty+correctness concept (the model must be wrong AND the correction mechanism must be able to reach the right answer), so probes targeting broad activation spaces risk relying on functionally inert incorrectness features. This motivates our SAE-guided feature analysis in Phase 3b and suggests that the confounded feature intersection — not the full activation space — may be the effective substrate for correctability prediction, potentially explaining why the single-layer PANL probe achieves only 0.614 AUROC.\n\nThe Confidence Manifold (arXiv:2602.08159) shows correctness occupies only 3–8 dimensions in activation space and is linearly separable with as few as 25 labeled examples. However, correctability is a second-order property: it depends not just on whether the model is wrong, but on whether the model's correction mechanism can reach the right answer given the model's knowledge state and reasoning pathways. The Interpretability-without-Actionability paper (arXiv:2603.18353) provides indirect evidence that this second-order property may be harder to capture: even with 98.2% detection AUROC, activation steering corrected only 20–24% of errors (concept-bottleneck steering) or 0% (SAE feature steering), revealing a 53-percentage-point knowledge-action gap. This suggests correctability may occupy a different — possibly higher-dimensional or non-linear — representational subspace than correctness, and the SAE dissociation finding (arXiv:2604.19974) provides a mechanistic explanation: correctability may require engaging the narrow confounded feature population rather than the broader (but functionally inert) incorrectness features. The Truth-as-a-Trajectory framework (arXiv:2603.01326) proposes that cross-layer displacement vectors capture properties that static single-layer probes miss, potentially relevant to second-order properties like correctability. The Accuracy-Correction Paradox (arXiv:2601.00828) shows weaker models achieve 1.6× higher correction rates and proposes the Error Depth Hypothesis — that stronger models make fewer but deeper errors that resist self-correction — providing a taxonomy of error correctable characteristics. The information-theoretic analysis of correlated errors (Preprints.org 202601.0892) formalizes bounds on self-correction when generator and evaluator share failure modes, motivating external probe-based gating as a mechanism to break the correlation. LLMs also encode problem difficulty as a linearly decodable property (arXiv:2510.18147, ρ ≈ 0.88), suggesting that related meta-cognitive properties may be extractable, though correctability's second-order nature makes direct analogy uncertain.\n\n## Approach\nWe propose a four-phase study of correctability prediction and selective self-correction, including an explicit pilot to validate the multi-layer ensemble transfer hypothesis, SAE-guided feature analysis informed by the uncertainty-correctness dissociation (arXiv:2604.19974), and a contribution plan that is robust to negative results.\n\n**Phase 0: Pilot Feasibility Study.** Before committing to the full experimental pipeline, we run a targeted pilot on the PANL paper's existing correctability labels (Gemma-3-27B, TriviaQA subset). We train independent logistic regression probes at each of the ~42 layers, identify complementary layers via double-fault analysis (following arXiv:2604.13386's methodology), and build a 3–5 layer stacked ensemble. This pilot directly tests whether the multi-layer ensembling technique that improved deception detection AUROC by up to 78% transfers to correctability prediction. Success criterion: if the ensemble achieves ≥0.70 AUROC (meaningful improvement over the 0.614 single-layer baseline), we proceed to Phase 1. If the ensemble plateaus below 0.70, we shift emphasis to the representational geometry and SAE feature analysis (Phase 3b), which remains a publishable contribution. Estimated cost: ~15 H100-hours (single model, single dataset, multi-layer extraction only).\n\n**Phase 1: Enhanced Correctability Probes (ECP).** We move beyond the PANL paper's single-layer, single-token linear probe by developing multi-signal correctability probes. (a) Multi-layer ensemble: train independent logistic regression probes at each layer, select 3–5 complementary layers via double-fault analysis, combine via logistic stacking (following arXiv:2604.13386, but with the explicit caveat that this technique was validated on deception detection — our Phase 0 tests transfer to correctability). (b) Multi-token features: concatenate hidden states from the post-answer newline token (PANL), the last answer token (LAT), and the last 2 reasoning tokens — the PANL paper's own causal analysis shows LAT carries complementary information at different layers. (c) Attention-based features: extract per-head entropy statistics across semantic sections (question, reasoning, answer), following the methodology of arXiv:2602.13699 which achieves +0.06 AUROC absolute improvement over Lookback Lens in OOD correctness prediction. (d) Wait-token features: inspired by the crosscoder analysis of arXiv:2510.04128, extract hidden-state features at the position immediately preceding natural Wait tokens (when present), capturing the causal features that modulate reasoning patterns (restarting, recalling, uncertainty expression, double-checking). The insight from arXiv:2601.17421 that Wait token probabilities correlate with reasoning correctness suggests these features encode meta-cognitive state relevant to correctability. (e) SAE-guided feature selection: motivated by arXiv:2604.19974's finding that only confounded features (encoding both uncertainty and correctness) are causally effective while pure incorrectness features are functionally inert, we train SAEs on our target models and identify confounded features relevant to correctability. We then compare probes trained on (i) full activation spaces, (ii) SAE-reconstructed activations from confounded features only, and (iii) SAE-reconstructed activations excluding pure incorrectness features. This tests whether the narrow confounded feature intersection — rather than broad activations — is the effective substrate for correctability prediction, and whether filtering out causally inert features improves probe AUROC. (f) Non-linear probe ablation: compare linear probes, 2-layer MLPs (hidden dim 16/32), and SWIFT-style all-layer gated aggregation — motivated by the possibility that correctability, as a second-order property, may require non-linear boundaries even if correctness is linearly separable in 3–8 dimensions (arXiv:2602.08159). All probes are trained on on-policy correctability labels generated by running the model's actual self-correction pipeline (multiple correction attempts per error to get calibrated fixability scores), avoiding the distribution mismatch of synthetic error injection documented in SCoRe (arXiv:2409.12917).\n\n**Phase 2: Three-Way Gated Self-Correction.** Use the ECP to implement a three-way decision at inference time: (i) if the error detection probe indicates the answer is likely correct, retain the original answer; (ii) if the error is detected AND the correctability probe predicts high fixability (above a calibrated threshold), attempt correction — either prompting-based correction or probe-selective Wait insertion (applying Wait only when the probe detects both an error and high correctability, leveraging the mechanistic finding from arXiv:2510.04128 that Wait triggers different reasoning patterns depending on internal state); (iii) if the error is detected but correctability is predicted as low, abstain or flag for external intervention. This design is distinguished from CoRefine's (arXiv:2602.08948) three-way routing in three key ways: we use hidden-state probes rather than output-level confidence, our third option is genuine abstention (declining to answer) rather than exploring alternative approaches, and our gating is explicitly correctability-aware — routing based on predicted fixability rather than confidence level. Where CoRefine optimizes compute efficiency (achieving ~190× token reduction), our framework optimizes decision quality by preventing wasted correction attempts on unfixable errors and avoiding overcorrection of correct answers.\n\n**Phase 3: Comprehensive Evaluation.** Evaluate across three dense models where probing is well-understood: Gemma-3-27B (same as PANL paper, validates signal transfer), Qwen-2.5-7B-Instruct (same as PANL paper, smaller scale), and Mistral-Small-3.2-24B (different architecture family, tests generalization). Use three benchmarks (TriviaQA, MMLU, GSM8K) with 10K+ questions each. Compare gated correction against eight baselines: (1) no correction, (2) ungated prompting-based correction, (3) Wait-appended correction applied to all answers — measuring the previously-untested overcorrection rate, (4) Wait-appended correction applied only to probe-detected errors, (5) confidence-threshold gating using log-probabilities (following Reflective Confidence's approach, arXiv:2512.18605), (6) CoRefine-style output-confidence routing (arXiv:2602.08948) — retrained on our models/benchmarks for fair comparison, (7) PAG-style generative verification (arXiv:2506.10406), (8) oracle gating (upper bound). Conduct ablations on: probe architecture (linear vs. MLP vs. ensemble vs. SAE-guided), feature sources (PANL-only vs. multi-token vs. +attention vs. +Wait-features vs. +SAE-confounded), layer selection, cross-task transferability, and threshold sensitivity analysis showing at what AUROC level gating begins to outperform ungated correction.\n\n**Phase 3b: Representational Geometry and Feature Decomposition of Correctability (Robust to Negative Probe Results).** Regardless of probe performance, we conduct a dedicated analysis of the representational relationship between correctability, correctness, and uncertainty at the feature population level. (a) Subspace comparison: compute the principal components of correctness and correctability representations separately (following arXiv:2602.08159's methodology) and measure subspace alignment via principal angle analysis — testing whether correctability occupies the same 3–8 dimensional subspace as correctness or requires distinct dimensions. (b) Dimensionality analysis: determine how many dimensions encode correctability vs. correctness at each layer, and whether correctability requires higher dimensionality (consistent with its second-order nature). (c) Non-linearity characterization: compare linear vs. non-linear probe AUROC gaps for correctability vs. correctness — a larger gap for correctability would indicate it occupies a more complex geometric region. (d) SAE feature decomposition: train SAEs on our target models and decompose correctability-predictive features into pure uncertainty, pure incorrectness, and confounded populations (following arXiv:2604.19974's 2×2 framework). Test whether confounded features are disproportionately important for correctability prediction compared to correctness prediction — which would provide mechanistic evidence that correctability requires simultaneously engaging both uncertainty and correctness axes. Measure the causal efficacy of each population via suppression experiments: if suppressing pure incorrectness features has minimal effect on correctability prediction (paralleling the functional inertness finding for correctness), this confirms the narrow confounded intersection hypothesis and explains the representational ceiling for broad-activation linear probes. (e) Error depth analysis: using the Error Depth Hypothesis framework (arXiv:2601.00828), characterize what makes errors correctable vs. uncorrectable — surface-level errors (calculation mistakes, recall failures) vs. deep errors (fundamental misunderstanding, missing knowledge) — and test whether this taxonomy is reflected in representational distance and SAE feature activation patterns. (f) Cross-layer trajectory analysis: inspired by Truth-as-a-Trajectory (arXiv:2603.01326), examine whether correctability is better captured by cross-layer displacement vectors than by static single-layer activations, which would explain why single-layer probes struggle. This phase yields publishable insights regardless of whether the ECP achieves high AUROC, providing the first empirical characterization of how correctability is (or is not) represented in LLM internal states and the first application of the SAE uncertainty-correctness dissociation framework to a second-order property.\n\n## Inspiration\nThe gap between 0.614 AUROC (single-layer PANL probe) and the consistently higher performance of multi-signal probes on correctness prediction (Gnosis hidden-only: 0.78–0.92; attention entropy: +0.06 AUROC absolute in OOD) suggests correctability prediction has room for improvement with better probing methodology — though the magnitude of potential gains is uncertain given correctability's second-order nature. The dramatic improvement from multi-layer ensembling on deception detection (0.510→0.910; arXiv:2604.13386) demonstrates that multi-layer stacking can rescue failing single-layer probes, but transferability to correctability is a hypothesis to test, not a guaranteed outcome. The SAE dissociation finding (arXiv:2604.19974) — that only rare confounded features bridging uncertainty and correctness are causally effective — provides both a challenge and an opportunity: correctability probes may need to target this narrow feature intersection, but successfully doing so could yield more principled and interpretable predictions than broad-activation probing. The untested overcorrection cost of the 'Wait' baseline, combined with new mechanistic understanding of Wait tokens' causal role in triggering distinct reasoning patterns (arXiv:2510.04128, arXiv:2601.17421), creates a clear opportunity for probe-selective Wait application. CoRefine (arXiv:2602.08948) demonstrates the viability of learned three-way routing for self-correction but uses output-level confidence without correctability awareness or genuine abstention — leaving a well-defined gap for hidden-state probe-based gating that distinguishes correctable from uncorrectable errors. Key untried combination: multi-signal enhanced probes for correctability prediction informed by SAE feature analysis + three-way gating with genuine abstention + comparison against Wait and confidence-based controllers, with explicit analysis of what makes correctability representationally distinct from correctness at the feature population level.\n\n## Key References\n- How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals (arXiv:2604.22271, 2026) — establishes PANL correctability signal, 0.614 AUROC baseline\n- Self-Correction Bench: Uncovering and Addressing the Self-Correction Blind Spot in LLMs (arXiv:2507.02778, NeurIPS 2025 Workshop) — 64.5% blind spot, Wait baseline achieving 89.3% reduction; QwQ-32B generates Wait first-token at 37.7–76.8% depending on benchmark\n- Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling (arXiv:2604.13386, 2026) — multi-layer stacking on deception detection: +29% on Insider Trading, +78% on Harm-Pressure Knowledge (0.510→0.910 in Llama-70B); transfer to correctability is a hypothesis we test\n- Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits — Gnosis (arXiv:2512.20578, 2025) — multi-signal fusion for correctness prediction: hidden-only 0.78–0.92 AUROC (ablation on Qwen3-1.7B), fusion 0.80–0.95 AUROC\n- Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders (arXiv:2604.19974, 2026) — SAE decomposition reveals functionally distinct feature populations: 68% of pure incorrectness features are causally inert; only rare confounded features (102/1,057 in Llama-3.1-8B) bridge uncertainty and correctness, achieving 0.79 AUROC with 3 features from layer 18; directly informs our probe design and Phase 3b analysis\n- CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute (arXiv:2602.08948, 2026) — three-way routing (halt/rethink/alternative) via 211K-parameter Conv1D controller on output-level confidence; 92.6% halt precision, ~190× token reduction; differs from our approach in signal source (output logprobs vs. hidden-state probes), decision type (no genuine abstention), and gating criterion (confidence vs. correctability)\n- Reflective Confidence: Correcting Reasoning Flaws via Online Self-Correction (arXiv:2512.18605, 2025) — transforms low-confidence output signals into reflection triggers; 83.3% on AIME 2025 vs. 70.0% Self-Consistency; uses output-level logprobs, no correctability modeling\n- Internal states before wait modulate reasoning patterns (arXiv:2510.04128, EMNLP 2025 Findings) — crosscoders identify causal features promoting/suppressing Wait tokens; distinct reasoning patterns (restarting, recalling, uncertainty expression, double-checking) triggered by pre-Wait internal states\n- Oops, Wait: Token-Level Signals as a Lens into LLM Reasoning (arXiv:2601.17421, Jan 2026) — Wait token probabilities correlate with reasoning correctness; models exploit Wait signals only partially; implications for token-level steering\n- Probing for Arithmetic Errors in Language Models (arXiv:2507.12379, 2025) — probe-guided selective re-prompting, 6–12% correction rate\n- Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification (arXiv:2504.05419, 2025) — probe-gated early exit, AUROC 0.77–0.91\n- Knowing When to Quit: A Principled Framework for Dynamic Abstention in LLM Reasoning (arXiv:2604.18419, 2026) — value-function probes for abstention gating\n- From Emergence to Control: Probing and Modulating Self-Reflection in Language Models (arXiv:2506.12217, 2025) — self-reflection vector steering\n- The Confidence Manifold (arXiv:2602.08159, 2026) — correctness in 3–8 dimensions, 25-example sufficiency, linearly separable\n- Attention Head Entropy of LLMs Predicts Answer Correctness (arXiv:2602.13699, 2026) — per-head 2-Rényi entropy achieves OOD AUROC 0.76 average (+0.06 absolute, 8.5% relative improvement over Lookback Lens)\n- PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier (arXiv:2506.10406, 2025)\n- Understanding the Dark Side of LLMs' Intrinsic Self-Correction (ACL 2025) — overcorrection and cognitive biases\n- Interpretability without Actionability (arXiv:2603.18353, 2026) — knowledge-action gap: 98.2% detection AUROC but only 20–24% correction via steering, 53-point gap\n- Mining Intrinsic Rewards from LLM Hidden States — SWIFT (arXiv:2505.12225, 2025) — all-layer gated aggregation\n- Between the Layers Lies the Truth (arXiv:2603.22299, 2026) — cross-layer agreement features\n- Truth as a Trajectory (arXiv:2603.01326, 2026) — cross-layer displacement vectors capture properties missed by static single-layer probes\n- Training Language Models to Self-Correct via Reinforcement Learning — SCoRe (arXiv:2409.12917, 2024) — on-policy training data importance\n- Large Language Models Cannot Self-Correct Reasoning Yet (ICLR 2024)\n- Decomposing LLM Self-Correction: The Accuracy-Correction Paradox (arXiv:2601.00828, 2026) — Error Depth Hypothesis: weaker models achieve 1.6× higher correction rates; deeper errors resist self-correction\n- No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes (arXiv:2509.10625, ICLR 2026 Workshop)\n- Calibrating LLM Confidence by Probing Perturbed Representation Stability (arXiv:2505.21772, 2025) — +6 AUROC points via adversarial perturbation stability\n- LLMs Encode How Difficult Problems Are (arXiv:2510.18147, 2025) — difficulty linearly decodable (ρ ≈ 0.88); meta-cognitive properties extractable but correctability's second-order nature makes transfer uncertain\n- Limits of Self-Correction in LLMs: An Information-Theoretic Analysis of Correlated Errors (Preprints.org 202601.0892, Feb 2026) — formalizes bounds on self-correction with correlated generator-evaluator errors\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '220–280 H100-hours (Phase 0 pilot: ~15 hrs; inference for 3 models × ~30K questions × 3 passes [initial + Wait + correction] + multi-layer hidden state extraction across ~10 layers + attention feature extraction + Wait-feature extraction + SAE training and feature decomposition + probe training + representational geometry analysis + ablations)', 'timeline': '11–13 weeks (includes pilot, SAE analysis, full experiments, geometry analysis, paper writing)', 'estimated_gpu_cost': '$550–700 (at ~$2.50/H100-hr on cloud providers)'}\n- **human_in_loop**: {'gpu_hours': '220–280 H100-hours (same compute, faster iteration via AI-assisted code/analysis)', 'timeline': '8–10 weeks', 'claude_api_cost': '$150–210 (experiment orchestration, SAE analysis notebooks, geometry visualization, paper drafting via Sonnet 4.6)', 'estimated_gpu_cost': '$550–700'}\n- **auto_research**: {'gpu_hours': '300–360 H100-hours (overhead from automated probe architecture sweeps, SAE training and decomposition, threshold optimization, representational geometry grid, and broader ablation grid)', 'timeline': '2–3 weeks wall-clock', 'claude_api_cost': '$420–580 (full pipeline orchestration, code generation, debugging, SAE analysis, statistical analysis, visualization, paper drafting)', 'estimated_gpu_cost': '$750–900', 'speed_bottleneck': 'Sequential multi-layer hidden state extraction over ~90K forward passes (3 models × 30K questions); extraction requires full-precision activations at 5–10 layers per pass and cannot be batched as aggressively as standard inference; SAE training adds ~20–30 H100-hours per model'}\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T21:12:35.912Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T21:12:35.912Z",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d"
}
```

---

## Round 1

44 recorded events

### User

_source line 3 · 2026-05-19T21:12:35.927Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction

## Description
We investigate whether LLMs' internal representations can predict which of their errors are self-correctable, and whether this prediction enables selective correction that outperforms both ungated correction, the trivial 'Wait' baseline, and confidence-based routing. Prior work shows a faint correctability signal at the post-answer newline token (PANL) achieving only 0.614 AUROC with a single-layer linear probe — insufficient for reliable gating. We develop Enhanced Correctability Probes (ECP) that combine multi-layer ensemble stacking, multi-token features (PANL + last-answer-token + reasoning tokens), attention-entropy features, pre-Wait hidden-state features (informed by crosscoder analysis of Wait-token mechanisms, arXiv:2510.04128), and SAE-guided feature selection targeting the confounded feature intersection that bridges uncertainty and correctness (motivated by the functional dissociation finding of arXiv:2604.19974, where 68% of pure incorrectness features are causally inert). We begin with a Phase 0 pilot that directly tests whether multi-layer ensembling — which improved deception detection AUROC by up to 78% (arXiv:2604.13386, specifically on Harm-Pressure Knowledge in Llama-70B) — transfers to the fundamentally different task of correctability prediction. These probes gate a three-way decision: retain the original answer (likely correct), attempt correction including probe-selective Wait insertion (error detected, high correctability), or abstain (error detected, low correctability). This framework is distinguished from CoRefine's (arXiv:2602.08948) three-way routing — which uses output-level confidence, lacks genuine abstention, and is not correctability-aware — by using hidden-state probes, providing a genuine abstention option for unfixable errors, and explicitly predicting error fixability rather than confidence. Critically, we provide the first evaluation of the 'Wait' baseline on correct answers, measuring its previously-unknown overcorrection cost. We also conduct the first representational geometry and SAE feature decomposition analysis of correctability vs. correctness, testing whether correctability — a second-order property that depends not just on whether the model is wrong but on whether correction mechanisms can reach the right answer — shares the low-dimensional, linearly-separable structure that correctness exhibits (arXiv:2602.08159), requires higher dimensionality or non-linear boundaries, or depends disproportionately on the narrow confounded feature population identified by arXiv:2604.19974. This analysis, combined with error depth characterization (arXiv:2601.00828) and threshold analysis mapping probe quality to gating utility, ensures publishable contributions even if probe AUROC plateaus at marginal levels. We evaluate across Gemma-3-27B, Qwen-2.5-7B-Instruct, and Mistral-Small-3.2-24B on TriviaQA, MMLU, and GSM8K, comparing against eight baselines including ungated correction, Wait (universal and probe-selective), confidence-based routing (CoRefine-style and Reflective Confidence-style), PAG, and oracle gating. Our contributions are: (1) operationalizing correctability as a prediction target distinct from correctness, (2) the first pilot testing whether multi-layer ensembling transfers from deception to correctability, (3) the first hidden-state probe-based gating with genuine abstention for correctability-aware self-correction — distinguished from CoRefine's confidence-based routing by signal source, abstention capability, and correctability specificity, (4) the first representational geometry and SAE feature decomposition comparison of correctability vs. correctness, testing whether second-order properties have a different confounded-feature signature than first-order properties, and (5) establishing the conditions — including minimum probe quality thresholds — under which probe-gated correction outperforms simpler alternatives including confidence-based controllers.

## Core Problem
LLMs attempt correction on all detected errors equally, but ~64.5% of self-generated errors are uncorrectable. Recent work reveals a faint internal 'correctability' signal at the post-answer newline token (PANL), but it achieves only 0.614 AUROC on own-generated errors using a single-layer linear probe — barely actionable for reliable gating. Meanwhile, trivial interventions like appending 'Wait' reduce blind spots by 89.3% on known errors, but their overcorrection rate on correct answers is completely untested. Confidence-based controllers like CoRefine (arXiv:2602.08948) achieve efficient three-way routing (halt/rethink/explore-alternative) using output-level logprobs, but they do not distinguish between correctable and uncorrectable errors — treating all detected issues as potentially fixable. Critically, correctability is a second-order property — it depends not just on whether the model is wrong, but on whether the model's correction mechanism can reach the right answer — and recent SAE analysis (arXiv:2604.19974) reveals that uncertainty and correctness are encoded by functionally distinct feature populations, with only rare 'confounded' features bridging both signals. It is unknown whether correctability — which inherently requires engaging both axes — shares the favorable geometric properties (low dimensionality, linear separability) that correctness exhibits, or whether it requires targeting the narrow confounded feature intersection. Can enhanced multi-signal probes substantially improve correctability prediction, what is the representational relationship between correctability, correctness, and uncertainty at the feature level, and under what conditions does probe-gated correction with genuine abstention outperform both ungated correction and simpler confidence-based alternatives?

## Opportunity
Three converging findings create a clear research opportunity: (1) The PANL paper (arXiv:2604.22271) establishes that correctability is partially encoded in internal representations, but their single-layer, single-token linear probe barely exceeds chance (0.614 AUROC) on own-generated errors — leaving substantial room for improvement. For correctness prediction on adjacent tasks, Gnosis-style multi-signal fusion (arXiv:2512.20578) achieves 0.78–0.92 AUROC on hidden states alone (with the lower end on MMLU-Pro; ablation on Qwen3-1.7B only) and 0.80–0.95 with attention fusion, while attention-head entropy probes (arXiv:2602.13699) achieve +0.06 AUROC absolute improvement in OOD settings (0.70→0.76 average, 8.5% relative vs. Lookback Lens). Multi-layer probe ensembling (arXiv:2604.13386) has dramatically improved deception detection AUROC (0.510→0.910 on Harm-Pressure Knowledge in Llama-70B), though whether similar gains transfer to correctability — a fundamentally different property — is an open empirical question that motivates our pilot experiment. (2) The 'Wait' baseline from Self-Correction Bench (arXiv:2507.02778) is powerful but fundamentally non-selective: it was tested only on known errors, never on correct answers, so its overcorrection cost is unknown. QwQ-32B naturally generates 'Wait' as its first correction token 37.7–76.8% of the time depending on benchmark (SCLI5 to PRM800K-SC), but this behavior varies widely across models and is near-zero for non-reasoning models. Recent mechanistic work shows that internal states before Wait tokens causally modulate distinct reasoning patterns — restarting, recalling, uncertainty expression, and double-checking (arXiv:2510.04128, EMNLP 2025 Findings) — and that Wait token probabilities correlate with reasoning correctness in ways that vary by training strategy (arXiv:2601.17421). These findings suggest Wait's effectiveness is not uniform but depends on which reasoning pattern it triggers, creating an opportunity for probe-selective application. Reflective Confidence (arXiv:2512.18605) demonstrates a related approach, transforming low-confidence output signals into reflection triggers rather than stopping, achieving 83.3% accuracy on AIME 2025 vs. 70.0% for Self-Consistency — but uses only output-level logprobs, not internal representations. (3) Existing gating approaches occupy adjacent niches but leave a clear gap. CoRefine (arXiv:2602.08948) implements three-way routing (halt/rethink/alternative) via a 211K-parameter Conv1D controller on output-level confidence, achieving 92.6% halt precision — but its decisions are confidence-based rather than correctability-aware, and its ALTERNATIVE option explores different approaches rather than genuinely abstaining when errors are likely unfixable. Four concurrent probe-gating papers address correctness, early exit, abstention, or reflection control — but none probe for correctability (whether a specific error is fixable), and none combine hidden-state probes with genuine abstention in a correctability-aware framework. Moreover, the SAE dissociation paper (arXiv:2604.19974) reveals that uncertainty and correctness are encoded by functionally distinct feature populations — with 68% of pure incorrectness features being causally inert and only rare confounded features (102 out of 1,057 in Llama-3.1-8B) bridging both signals to achieve 0.79 AUROC with just 3 features. This finding directly challenges naive linear probing over broad activations and suggests correctability prediction may need to target the narrow confounded feature intersection, motivating our SAE-guided probe design and representational analysis.

## Related Work / Landscape
The PANL paper (arXiv:2604.22271) establishes correctability prediction as a distinct task from error detection, achieving 0.986 AUROC for detection but only 0.614 for correctability on own-generated errors using single-layer logistic regression at one token position. This gap — high detectability but low correctability prediction — is the central technical challenge. Gnosis (arXiv:2512.20578) achieves 0.80–0.95 AUROC for correctness prediction by fusing final-layer hidden states with attention-map features via a ~5M-parameter architecture; notably, the hidden-state stream alone achieves 0.78–0.92 AUROC (with the lower end on MMLU-Pro; ablation only reported for Qwen3-1.7B), with attention fusion adding 0–3 points depending on the task. The multi-layer ensembling paper (arXiv:2604.13386) shows that logistic stacking across complementary layers can dramatically improve probe performance — achieving 0.510→0.910 AUROC on the hardest deception detection task (Harm-Pressure Knowledge, Llama-70B) — because informative directions rotate across layers and double-fault analysis reveals complementary error patterns between early and late layers. However, this result is specific to deception detection, which has different layer-wise encoding properties than correctness or correctability; whether analogous gains transfer is an empirical hypothesis we test via a Phase 0 pilot. For correctness prediction specifically, multi-signal approaches show more modest but consistent gains: attention-head entropy probes (arXiv:2602.13699) improve OOD AUROC by +0.06 absolute (0.70→0.76 average across 5 models, an 8.5% relative improvement over Lookback Lens), and perturbation-stability probes (arXiv:2505.21772) add +6 AUROC points via targeted adversarial perturbations to hidden states. SWIFT (arXiv:2505.12225) concatenates all-layer hidden states with learned gating weights to extract token-level quality signals.

The Self-Correction Bench (arXiv:2507.02778) documents the 64.5% blind spot and shows 'Wait' reduces it by 89.3%. QwQ-32B naturally generates 'Wait' as its first correction token at rates varying by benchmark (37.7% on SCLI5, 72.5% on GSM8K-SC, 76.8% on PRM800K-SC), but this behavior is model-specific — other reasoning models show different patterns and non-reasoning models rarely generate Wait spontaneously. The Wait baseline was never tested on correct answers, leaving the overcorrection cost unknown. Two recent papers provide mechanistic understanding of Wait tokens: arXiv:2510.04128 (EMNLP 2025 Findings) trains crosscoders on DeepSeek-R1-Distill-Llama-8B to identify features that promote or suppress Wait tokens, discovering causal features for distinct reasoning patterns (restarting, recalling, uncertainty expression, double-checking) via activation steering at layer 15; arXiv:2601.17421 systematically analyzes Wait and other discourse tokens across model scales and training strategies, finding that Wait token probabilities correlate with reasoning correctness but that models exploit this signal only partially. Reflective Confidence (arXiv:2512.18605) proposes a related approach, transforming low-confidence output-level logprob signals into reflection triggers rather than early stopping, achieving 83.3% accuracy on AIME 2025 (vs. 70.0% Self-Consistency, K=32) on Qwen3-8B — demonstrating that selective confidence-gated correction can significantly outperform non-selective baselines, though it uses output-level signals rather than internal representations and does not model correctability.

CoRefine (arXiv:2602.08948) is the closest existing system to our three-way gating, implementing halt/rethink/alternative decisions via a 211K-parameter Conv1D controller that consumes output-level confidence traces from the frozen LLM. It achieves 92.6% halt precision, averages 2.7 refinement steps per problem, and reduces tokens ~190× relative to 512-sample baselines on mathematical reasoning benchmarks. However, CoRefine differs from our proposal in three fundamental ways: (a) it uses output-level logprobs rather than hidden-state probes, missing the richer internal signal that PANL demonstrates exists; (b) its HALT decision accepts the current answer — it never genuinely abstains or flags for external intervention when errors are likely unfixable; (c) its routing is confidence-based, not correctability-aware — it cannot distinguish correctable from uncorrectable errors, treating all low-confidence outputs as potentially improvable. Four concurrent probe-gating papers occupy adjacent niches: arXiv:2507.12379 probes for arithmetic errors and selectively re-prompts (only 6–12% of detected errors actually get corrected); arXiv:2504.05419 uses probes for early exit from reasoning chains (AUROC 0.77–0.91 for correctness, not correctability); arXiv:2604.18419 trains value-function probes for dynamic mid-generation abstention; arXiv:2506.12217 uses activation steering to modulate self-reflection frequency. None of these probe for correctability specifically, and none combine hidden-state probes with genuine abstention in a correctability-aware framework.

A critical finding for our probing approach comes from arXiv:2604.19974, which uses sparse autoencoders to decompose LLM representations into functionally distinct feature populations. In Llama-3.1-8B, they identify 700 pure uncertainty features, 255 pure incorrectness features, and only 102 confounded features encoding both signals. The key insight is a functional dissociation: 68% of pure incorrectness features are causally inert (mean accuracy delta of -0.03% when suppressed), while pure uncertainty features are essential for model performance, and only confounded features bridging both axes are causally effective for correctness prediction — with just 3 confounded features from layer 18 achieving 0.79 AUROC. This has direct implications for correctability probing: correctability is inherently a joint uncertainty+correctness concept (the model must be wrong AND the correction mechanism must be able to reach the right answer), so probes targeting broad activation spaces risk relying on functionally inert incorrectness features. This motivates our SAE-guided feature analysis in Phase 3b and suggests that the confounded feature intersection — not the full activation space — may be the effective substrate for correctability prediction, potentially explaining why the single-layer PANL probe achieves only 0.614 AUROC.

The Confidence Manifold (arXiv:2602.08159) shows correctness occupies only 3–8 dimensions in activation space and is linearly separable with as few as 25 labeled examples. However, correctability is a second-order property: it depends not just on whether the model is wrong, but on whether the model's correction mechanism can reach the right answer given the model's knowledge state and reasoning pathways. The Interpretability-without-Actionability paper (arXiv:2603.18353) provides indirect evidence that this second-order property may be harder to capture: even with 98.2% detection AUROC, activation steering corrected only 20–24% of errors (concept-bottleneck steering) or 0% (SAE feature steering), revealing a 53-percentage-point knowledge-action gap. This suggests correctability may occupy a different — possibly higher-dimensional or non-linear — representational subspace than correctness, and the SAE dissociation finding (arXiv:2604.19974) provides a mechanistic explanation: correctability may require engaging the narrow confounded feature population rather than the broader (but functionally inert) incorrectness features. The Truth-as-a-Trajectory framework (arXiv:2603.01326) proposes that cross-layer displacement vectors capture properties that static single-layer probes miss, potentially relevant to second-order properties like correctability. The Accuracy-Correction Paradox (arXiv:2601.00828) shows weaker models achieve 1.6× higher correction rates and proposes the Error Depth Hypothesis — that stronger models make fewer but deeper errors that resist self-correction — providing a taxonomy of error correctable characteristics. The information-theoretic analysis of correlated errors (Preprints.org 202601.0892) formalizes bounds on self-correction when generator and evaluator share failure modes, motivating external probe-based gating as a mechanism to break the correlation. LLMs also encode problem difficulty as a linearly decodable property (arXiv:2510.18147, ρ ≈ 0.88), suggesting that related meta-cognitive properties may be extractable, though correctability's second-order nature makes direct analogy uncertain.

## Approach
We propose a four-phase study of correctability prediction and selective self-correction, including an explicit pilot to validate the multi-layer ensemble transfer hypothesis, SAE-guided feature analysis informed by the uncertainty-correctness dissociation (arXiv:2604.19974), and a contribution plan that is robust to negative results.

**Phase 0: Pilot Feasibility Study.** Before committing to the full experimental pipeline, we run a targeted pilot on the PANL paper's existing correctability labels (Gemma-3-27B, TriviaQA subset). We train independent logistic regression probes at each of the ~42 layers, identify complementary layers via double-fault analysis (following arXiv:2604.13386's methodology), and build a 3–5 layer stacked ensemble. This pilot directly tests whether the multi-layer ensembling technique that improved deception detection AUROC by up to 78% transfers to correctability prediction. Success criterion: if the ensemble achieves ≥0.70 AUROC (meaningful improvement over the 0.614 single-layer baseline), we proceed to Phase 1. If the ensemble plateaus below 0.70, we shift emphasis to the representational geometry and SAE feature analysis (Phase 3b), which remains a publishable contribution. Estimated cost: ~15 H100-hours (single model, single dataset, multi-layer extraction only).

**Phase 1: Enhanced Correctability Probes (ECP).** We move beyond the PANL paper's single-layer, single-token linear probe by developing multi-signal correctability probes. (a) Multi-layer ensemble: train independent logistic regression probes at each layer, select 3–5 complementary layers via double-fault analysis, combine via logistic stacking (following arXiv:2604.13386, but with the explicit caveat that this technique was validated on deception detection — our Phase 0 tests transfer to correctability). (b) Multi-token features: concatenate hidden states from the post-answer newline token (PANL), the last answer token (LAT), and the last 2 reasoning tokens — the PANL paper's own causal analysis shows LAT carries complementary information at different layers. (c) Attention-based features: extract per-head entropy statistics across semantic sections (question, reasoning, answer), following the methodology of arXiv:2602.13699 which achieves +0.06 AUROC absolute improvement over Lookback Lens in OOD correctness prediction. (d) Wait-token features: inspired by the crosscoder analysis of arXiv:2510.04128, extract hidden-state features at the position immediately preceding natural Wait tokens (when present), capturing the causal features that modulate reasoning patterns (restarting, recalling, uncertainty expression, double-checking). The insight from arXiv:2601.17421 that Wait token probabilities correlate with reasoning correctness suggests these features encode meta-cognitive state relevant to correctability. (e) SAE-guided feature selection: motivated by arXiv:2604.19974's finding that only confounded features (encoding both uncertainty and correctness) are causally effective while pure incorrectness features are functionally inert, we train SAEs on our target models and identify confounded features relevant to correctability. We then compare probes trained on (i) full activation spaces, (ii) SAE-reconstructed activations from confounded features only, and (iii) SAE-reconstructed activations excluding pure incorrectness features. This tests whether the narrow confounded feature intersection — rather than broad activations — is the effective substrate for correctability prediction, and whether filtering out causally inert features improves probe AUROC. (f) Non-linear probe ablation: compare linear probes, 2-layer MLPs (hidden dim 16/32), and SWIFT-style all-layer gated aggregation — motivated by the possibility that correctability, as a second-order property, may require non-linear boundaries even if correctness is linearly separable in 3–8 dimensions (arXiv:2602.08159). All probes are trained on on-policy correctability labels generated by running the model's actual self-correction pipeline (multiple correction attempts per error to get calibrated fixability scores), avoiding the distribution mismatch of synthetic error injection documented in SCoRe (arXiv:2409.12917).

**Phase 2: Three-Way Gated Self-Correction.** Use the ECP to implement a three-way decision at inference time: (i) if the error detection probe indicates the answer is likely correct, retain the original answer; (ii) if the error is detected AND the correctability probe predicts high fixability (above a calibrated threshold), attempt correction — either prompting-based correction or probe-selective Wait insertion (applying Wait only when the probe detects both an error and high correctability, leveraging the mechanistic finding from arXiv:2510.04128 that Wait triggers different reasoning patterns depending on internal state); (iii) if the error is detected but correctability is predicted as low, abstain or flag for external intervention. This design is distinguished from CoRefine's (arXiv:2602.08948) three-way routing in three key ways: we use hidden-state probes rather than output-level confidence, our third option is genuine abstention (declining to answer) rather than exploring alternative approaches, and our gating is explicitly correctability-aware — routing based on predicted fixability rather than confidence level. Where CoRefine optimizes compute efficiency (achieving ~190× token reduction), our framework optimizes decision quality by preventing wasted correction attempts on unfixable errors and avoiding overcorrection of correct answers.

**Phase 3: Comprehensive Evaluation.** Evaluate across three dense models where probing is well-understood: Gemma-3-27B (same as PANL paper, validates signal transfer), Qwen-2.5-7B-Instruct (same as PANL paper, smaller scale), and Mistral-Small-3.2-24B (different architecture family, tests generalization). Use three benchmarks (TriviaQA, MMLU, GSM8K) with 10K+ questions each. Compare gated correction against eight baselines: (1) no correction, (2) ungated prompting-based correction, (3) Wait-appended correction applied to all answers — measuring the previously-untested overcorrection rate, (4) Wait-appended correction applied only to probe-detected errors, (5) confidence-threshold gating using log-probabilities (following Reflective Confidence's approach, arXiv:2512.18605), (6) CoRefine-style output-confidence routing (arXiv:2602.08948) — retrained on our models/benchmarks for fair comparison, (7) PAG-style generative verification (arXiv:2506.10406), (8) oracle gating (upper bound). Conduct ablations on: probe architecture (linear vs. MLP vs. ensemble vs. SAE-guided), feature sources (PANL-only vs. multi-token vs. +attention vs. +Wait-features vs. +SAE-confounded), layer selection, cross-task transferability, and threshold sensitivity analysis showing at what AUROC level gating begins to outperform ungated correction.

**Phase 3b: Representational Geometry and Feature Decomposition of Correctability (Robust to Negative Probe Results).** Regardless of probe performance, we conduct a dedicated analysis of the representational relationship between correctability, correctness, and uncertainty at the feature population level. (a) Subspace comparison: compute the principal components of correctness and correctability representations separately (following arXiv:2602.08159's methodology) and measure subspace alignment via principal angle analysis — testing whether correctability occupies the same 3–8 dimensional subspace as correctness or requires distinct dimensions. (b) Dimensionality analysis: determine how many dimensions encode correctability vs. correctness at each layer, and whether correctability requires higher dimensionality (consistent with its second-order nature). (c) Non-linearity characterization: compare linear vs. non-linear probe AUROC gaps for correctability vs. correctness — a larger gap for correctability would indicate it occupies a more complex geometric region. (d) SAE feature decomposition: train SAEs on our target models and decompose correctability-predictive features into pure uncertainty, pure incorrectness, and confounded populations (following arXiv:2604.19974's 2×2 framework). Test whether confounded features are disproportionately important for correctability prediction compared to correctness prediction — which would provide mechanistic evidence that correctability requires simultaneously engaging both uncertainty and correctness axes. Measure the causal efficacy of each population via suppression experiments: if suppressing pure incorrectness features has minimal effect on correctability prediction (paralleling the functional inertness finding for correctness), this confirms the narrow confounded intersection hypothesis and explains the representational ceiling for broad-activation linear probes. (e) Error depth analysis: using the Error Depth Hypothesis framework (arXiv:2601.00828), characterize what makes errors correctable vs. uncorrectable — surface-level errors (calculation mistakes, recall failures) vs. deep errors (fundamental misunderstanding, missing knowledge) — and test whether this taxonomy is reflected in representational distance and SAE feature activation patterns. (f) Cross-layer trajectory analysis: inspired by Truth-as-a-Trajectory (arXiv:2603.01326), examine whether correctability is better captured by cross-layer displacement vectors than by static single-layer activations, which would explain why single-layer probes struggle. This phase yields publishable insights regardless of whether the ECP achieves high AUROC, providing the first empirical characterization of how correctability is (or is not) represented in LLM internal states and the first application of the SAE uncertainty-correctness dissociation framework to a second-order property.

## Inspiration
The gap between 0.614 AUROC (single-layer PANL probe) and the consistently higher performance of multi-signal probes on correctness prediction (Gnosis hidden-only: 0.78–0.92; attention entropy: +0.06 AUROC absolute in OOD) suggests correctability prediction has room for improvement with better probing methodology — though the magnitude of potential gains is uncertain given correctability's second-order nature. The dramatic improvement from multi-layer ensembling on deception detection (0.510→0.910; arXiv:2604.13386) demonstrates that multi-layer stacking can rescue failing single-layer probes, but transferability to correctability is a hypothesis to test, not a guaranteed outcome. The SAE dissociation finding (arXiv:2604.19974) — that only rare confounded features bridging uncertainty and correctness are causally effective — provides both a challenge and an opportunity: correctability probes may need to target this narrow feature intersection, but successfully doing so could yield more principled and interpretable predictions than broad-activation probing. The untested overcorrection cost of the 'Wait' baseline, combined with new mechanistic understanding of Wait tokens' causal role in triggering distinct reasoning patterns (arXiv:2510.04128, arXiv:2601.17421), creates a clear opportunity for probe-selective Wait application. CoRefine (arXiv:2602.08948) demonstrates the viability of learned three-way routing for self-correction but uses output-level confidence without correctability awareness or genuine abstention — leaving a well-defined gap for hidden-state probe-based gating that distinguishes correctable from uncorrectable errors. Key untried combination: multi-signal enhanced probes for correctability prediction informed by SAE feature analysis + three-way gating with genuine abstention + comparison against Wait and confidence-based controllers, with explicit analysis of what makes correctability representationally distinct from correctness at the feature population level.

## Key References
- How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals (arXiv:2604.22271, 2026) — establishes PANL correctability signal, 0.614 AUROC baseline
- Self-Correction Bench: Uncovering and Addressing the Self-Correction Blind Spot in LLMs (arXiv:2507.02778, NeurIPS 2025 Workshop) — 64.5% blind spot, Wait baseline achieving 89.3% reduction; QwQ-32B generates Wait first-token at 37.7–76.8% depending on benchmark
- Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling (arXiv:2604.13386, 2026) — multi-layer stacking on deception detection: +29% on Insider Trading, +78% on Harm-Pressure Knowledge (0.510→0.910 in Llama-70B); transfer to correctability is a hypothesis we test
- Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits — Gnosis (arXiv:2512.20578, 2025) — multi-signal fusion for correctness prediction: hidden-only 0.78–0.92 AUROC (ablation on Qwen3-1.7B), fusion 0.80–0.95 AUROC
- Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders (arXiv:2604.19974, 2026) — SAE decomposition reveals functionally distinct feature populations: 68% of pure incorrectness features are causally inert; only rare confounded features (102/1,057 in Llama-3.1-8B) bridge uncertainty and correctness, achieving 0.79 AUROC with 3 features from layer 18; directly informs our probe design and Phase 3b analysis
- CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute (arXiv:2602.08948, 2026) — three-way routing (halt/rethink/alternative) via 211K-parameter Conv1D controller on output-level confidence; 92.6% halt precision, ~190× token reduction; differs from our approach in signal source (output logprobs vs. hidden-state probes), decision type (no genuine abstention), and gating criterion (confidence vs. correctability)
- Reflective Confidence: Correcting Reasoning Flaws via Online Self-Correction (arXiv:2512.18605, 2025) — transforms low-confidence output signals into reflection triggers; 83.3% on AIME 2025 vs. 70.0% Self-Consistency; uses output-level logprobs, no correctability modeling
- Internal states before wait modulate reasoning patterns (arXiv:2510.04128, EMNLP 2025 Findings) — crosscoders identify causal features promoting/suppressing Wait tokens; distinct reasoning patterns (restarting, recalling, uncertainty expression, double-checking) triggered by pre-Wait internal states
- Oops, Wait: Token-Level Signals as a Lens into LLM Reasoning (arXiv:2601.17421, Jan 2026) — Wait token probabilities correlate with reasoning correctness; models exploit Wait signals only partially; implications for token-level steering
- Probing for Arithmetic Errors in Language Models (arXiv:2507.12379, 2025) — probe-guided selective re-prompting, 6–12% correction rate
- Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification (arXiv:2504.05419, 2025) — probe-gated early exit, AUROC 0.77–0.91
- Knowing When to Quit: A Principled Framework for Dynamic Abstention in LLM Reasoning (arXiv:2604.18419, 2026) — value-function probes for abstention gating
- From Emergence to Control: Probing and Modulating Self-Reflection in Language Models (arXiv:2506.12217, 2025) — self-reflection vector steering
- The Confidence Manifold (arXiv:2602.08159, 2026) — correctness in 3–8 dimensions, 25-example sufficiency, linearly separable
- Attention Head Entropy of LLMs Predicts Answer Correctness (arXiv:2602.13699, 2026) — per-head 2-Rényi entropy achieves OOD AUROC 0.76 average (+0.06 absolute, 8.5% relative improvement over Lookback Lens)
- PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier (arXiv:2506.10406, 2025)
- Understanding the Dark Side of LLMs' Intrinsic Self-Correction (ACL 2025) — overcorrection and cognitive biases
- Interpretability without Actionability (arXiv:2603.18353, 2026) — knowledge-action gap: 98.2% detection AUROC but only 20–24% correction via steering, 53-point gap
- Mining Intrinsic Rewards from LLM Hidden States — SWIFT (arXiv:2505.12225, 2025) — all-layer gated aggregation
- Between the Layers Lies the Truth (arXiv:2603.22299, 2026) — cross-layer agreement features
- Truth as a Trajectory (arXiv:2603.01326, 2026) — cross-layer displacement vectors capture properties missed by static single-layer probes
- Training Language Models to Self-Correct via Reinforcement Learning — SCoRe (arXiv:2409.12917, 2024) — on-policy training data importance
- Large Language Models Cannot Self-Correct Reasoning Yet (ICLR 2024)
- Decomposing LLM Self-Correction: The Accuracy-Correction Paradox (arXiv:2601.00828, 2026) — Error Depth Hypothesis: weaker models achieve 1.6× higher correction rates; deeper errors resist self-correction
- No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes (arXiv:2509.10625, ICLR 2026 Workshop)
- Calibrating LLM Confidence by Probing Perturbed Representation Stability (arXiv:2505.21772, 2025) — +6 AUROC points via adversarial perturbation stability
- LLMs Encode How Difficult Problems Are (arXiv:2510.18147, 2025) — difficulty linearly decodable (ρ ≈ 0.88); meta-cognitive properties extractable but correctability's second-order nature makes transfer uncertain
- Limits of Self-Correction in LLMs: An Information-Theoretic Analysis of Correlated Errors (Preprints.org 202601.0892, Feb 2026) — formalizes bounds on self-correction with correlated generator-evaluator errors

## Resource Estimate
- **manual**: {'gpu_hours': '220–280 H100-hours (Phase 0 pilot: ~15 hrs; inference for 3 models × ~30K questions × 3 passes [initial + Wait + correction] + multi-layer hidden state extraction across ~10 layers + attention feature extraction + Wait-feature extraction + SAE training and feature decomposition + probe training + representational geometry analysis + ablations)', 'timeline': '11–13 weeks (includes pilot, SAE analysis, full experiments, geometry analysis, paper writing)', 'estimated_gpu_cost': '$550–700 (at ~$2.50/H100-hr on cloud providers)'}
- **human_in_loop**: {'gpu_hours': '220–280 H100-hours (same compute, faster iteration via AI-assisted code/analysis)', 'timeline': '8–10 weeks', 'claude_api_cost': '$150–210 (experiment orchestration, SAE analysis notebooks, geometry visualization, paper drafting via Sonnet 4.6)', 'estimated_gpu_cost': '$550–700'}
- **auto_research**: {'gpu_hours': '300–360 H100-hours (overhead from automated probe architecture sweeps, SAE training and decomposition, threshold optimization, representational geometry grid, and broader ablation grid)', 'timeline': '2–3 weeks wall-clock', 'claude_api_cost': '$420–580 (full pipeline orchestration, code generation, debugging, SAE analysis, statistical analysis, visualization, paper drafting)', 'estimated_gpu_cost': '$750–900', 'speed_bottleneck': 'Sequential multi-layer hidden state extraction over ~90K forward passes (3 models × 30K questions); extraction requires full-precision activations at 5–10 layers per pass and cannot be batched as aggressively as standard inference; SAE training adds ~20–30 H100-hours per model'}


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "8aba1f0b-4089-45b9-b00b-017d1ec192b1",
  "type": "user",
  "uuid": "79a273c8-2aef-41a1-9704-5bb05d820b86",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T21:12:35.925Z_

```json
{
  "parentUuid": "79a273c8-2aef-41a1-9704-5bb05d820b86",
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
  "uuid": "fd39e259-719b-40e0-88c0-8ce60ba85ee6",
  "timestamp": "2026-05-19T21:12:35.925Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T21:12:35.925Z_

```json
{
  "parentUuid": "fd39e259-719b-40e0-88c0-8ce60ba85ee6",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "40088f12-81ee-43f1-9748-eb3a8554957c",
  "timestamp": "2026-05-19T21:12:35.925Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "40088f12-81ee-43f1-9748-eb3a8554957c",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Predict LLM error correctability via multi-signal probes",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d"
}
```

---

### Assistant

_source line 8 · 2026-05-19T21:12:50.439Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for CoRL 2026 submission. Let me first carefully read the proposal, then conduct web searches to understand the current landscape before making my assessment.

Wait - CoRL is Conference on Robot Learning. This proposal is about LLM self-correction and probing internal representations. This seems more like an NLP/ML interpretability paper rather than a robotics paper. Let me re-read the task description...

The task says "评估其投稿 CoRL 2026 主会的中稿潜力" - evaluating its potential for acceptance at CoRL 2026 main conference. 

There's a clear mismatch here - the proposal focuses on LLM internal representations for self-correction, which is fundamentally an NLP/interpretability problem, not robotics. But the system prompt indicates this is a general idea review process without venue constraints, and the rubric explicitly mentions "NLP/CL 领域的影响力". So I should evaluate the idea quality itself rather than getting hung up on the venue mismatch.

Let me search the literature to understand the current state of work on LLM self-correction and internal representations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40088f12-81ee-43f1-9748-eb3a8554957c",
  "isSidechain": false,
  "requestId": "req_011CbCcjCYJzeqRcgYAtyCsQ",
  "type": "assistant",
  "uuid": "ebbbd12e-cee7-4231-8886-2e5f79d61f8d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018fvuSYu2we3aKE7sBnRP3R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10635,
      "cache_read_input_tokens": 13985,
      "output_tokens": 469,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10635,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 469,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 10635,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10635
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

_source line 9 · 2026-05-19T21:12:50.736Z_

I need to conduct thorough field research before evaluating this proposal. Let me search for the key papers and current landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebbbd12e-cee7-4231-8886-2e5f79d61f8d",
  "isSidechain": false,
  "requestId": "req_011CbCcjCYJzeqRcgYAtyCsQ",
  "type": "assistant",
  "uuid": "4e5e76fb-8967-4714-83b4-0e8c84f62bc9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018fvuSYu2we3aKE7sBnRP3R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10635,
      "cache_read_input_tokens": 13985,
      "output_tokens": 469,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10635,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 469,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 10635,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10635
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

_source line 10 · 2026-05-19T21:12:50.937Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VoZKdXPYz5eqcYBkYZc1CX`</summary>

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
  "parentUuid": "4e5e76fb-8967-4714-83b4-0e8c84f62bc9",
  "isSidechain": false,
  "requestId": "req_011CbCcjCYJzeqRcgYAtyCsQ",
  "type": "assistant",
  "uuid": "8e38f729-0975-4194-b900-1f4a428d0e98",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018fvuSYu2we3aKE7sBnRP3R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10635,
      "cache_read_input_tokens": 13985,
      "output_tokens": 469,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10635,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 469,
          "cache_read_input_tokens": 13985,
          "cache_creation_input_tokens": 10635,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10635
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

_source line 11 · 2026-05-19T21:12:50.945Z_

<details><summary>↩ Tool result · `toolu_01VoZKdXPYz5eqcYBkYZc1CX`</summary>

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
  "parentUuid": "8e38f729-0975-4194-b900-1f4a428d0e98",
  "isSidechain": false,
  "promptId": "8aba1f0b-4089-45b9-b00b-017d1ec192b1",
  "type": "user",
  "uuid": "5865f3a0-b100-4b21-807c-f1c0df1bf45a",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "8e38f729-0975-4194-b900-1f4a428d0e98",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T21:12:53.745Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me conduct the required web searches to understand the landscape. I'll search for the key papers and topics mentioned in the proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5865f3a0-b100-4b21-807c-f1c0df1bf45a",
  "isSidechain": false,
  "requestId": "req_011CbCck9mefyDRdnM5X5QwE",
  "type": "assistant",
  "uuid": "f34dd581-eb7d-4864-993b-ff15cbc2c830",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013kz3Mu5G2JAJnVrs1aXtE8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 996,
      "cache_read_input_tokens": 24620,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 996,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 129,
          "cache_read_input_tokens": 24620,
          "cache_creation_input_tokens": 996,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 996
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

_source line 13 · 2026-05-19T21:12:54.247Z_

Let me conduct multiple targeted searches to understand the current landscape before evaluating.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f34dd581-eb7d-4864-993b-ff15cbc2c830",
  "isSidechain": false,
  "requestId": "req_011CbCck9mefyDRdnM5X5QwE",
  "type": "assistant",
  "uuid": "5c17b88a-f11b-48d7-984e-5bf95897c3e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013kz3Mu5G2JAJnVrs1aXtE8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 996,
      "cache_read_input_tokens": 24620,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 996,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 129,
          "cache_read_input_tokens": 24620,
          "cache_creation_input_tokens": 996,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 996
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

_source line 14 · 2026-05-19T21:12:54.512Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GtxgtxXSyLFhAT6ctE7mgM`</summary>

```json
{
  "query": "LLM self-correction correctability prediction internal representations probing 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c17b88a-f11b-48d7-984e-5bf95897c3e4",
  "isSidechain": false,
  "requestId": "req_011CbCck9mefyDRdnM5X5QwE",
  "type": "assistant",
  "uuid": "125e6601-5ea3-40c1-b861-f9fc47c25924",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013kz3Mu5G2JAJnVrs1aXtE8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 996,
      "cache_read_input_tokens": 24620,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 996,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 129,
          "cache_read_input_tokens": 24620,
          "cache_creation_input_tokens": 996,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 996
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

_source line 15 · 2026-05-19T21:13:01.141Z_

<details><summary>↩ Tool result · `toolu_01GtxgtxXSyLFhAT6ctE7mgM`</summary>

```text
Web search results for query: "LLM self-correction correctability prediction internal representations probing 2025 2026"

Links: [{"title":"Predicting LLM Answer Accuracy from Question-Only ...","url":"https://arxiv.org/pdf/2509.10625"},{"title":"Model-Agnostic Correctness Assessment for LLM-Generated Code via Dynamic Internal Representation Selection","url":"https://arxiv.org/pdf/2510.02934"},{"title":"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/pdf/2512.20578"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"},{"title":"Probing for Arithmetic Errors in Language Models","url":"https://arxiv.org/pdf/2507.12379"},{"title":"Internalized Self-Correction for Large Language Models","url":"https://arxiv.org/pdf/2412.16653"}]

I found several relevant research papers on this topic. Here are the key findings:

## Recent Research on LLM Self-Correction and Correctability Prediction

**Correctability Prediction from Internal Representations:**

Research investigates the structure of self-correctness representations in LLMs, with recent work focusing on probing internal activations. AUTOPROBE is a novel model-agnostic approach that dynamically selects the most informative internal representations for code correctness assessment, employing an attention-based mechanism to learn importance scores for hidden states.

**Challenges in Self-Correction:**

Large language models remain unreliable at assessing the correctness of their own outputs, frequently producing confident but incorrect answers and failing to detect reasoning errors or hallucinations. More specifically, no prior work shows successful intrinsic self-correction using only the model's own feedback, though self-correction sometimes flips correct answers to incorrect ones through prompt bias and cognitive-like biases.

**Probing for Error Detection:**

Arithmetic errors can be anticipated from internal activations alone, and simple probes offer a viable path toward lightweight model self-correction. This suggests that examining internal representations may enable better correctability prediction.

The research indicates an emerging focus on using internal representation probing to predict whether models will produce correct answers and potentially guide self-correction mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "125e6601-5ea3-40c1-b861-f9fc47c25924",
  "isSidechain": false,
  "promptId": "8aba1f0b-4089-45b9-b00b-017d1ec192b1",
  "type": "user",
  "uuid": "08bffce9-ac94-4066-9233-28e3150ea94c",
  "toolUseResult": {
    "query": "LLM self-correction correctability prediction internal representations probing 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013khtYavWXY7MZS8UvX5ydL",
        "content": [
          {
            "title": "Predicting LLM Answer Accuracy from Question-Only ...",
            "url": "https://arxiv.org/pdf/2509.10625"
          },
          {
            "title": "Model-Agnostic Correctness Assessment for LLM-Generated Code via Dynamic Internal Representation Selection",
            "url": "https://arxiv.org/pdf/2510.02934"
          },
          {
            "title": "Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/pdf/2512.20578"
          },
          {
            "title": "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs",
            "url": "https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"
          },
          {
            "title": "Probing for Arithmetic Errors in Language Models",
            "url": "https://arxiv.org/pdf/2507.12379"
          },
          {
            "title": "Internalized Self-Correction for Large Language Models",
            "url": "https://arxiv.org/pdf/2412.16653"
          }
        ]
      },
      "I found several relevant research papers on this topic. Here are the key findings:\n\n## Recent Research on LLM Self-Correction and Correctability Prediction\n\n**Correctability Prediction from Internal Representations:**\n\nResearch investigates the structure of self-correctness representations in LLMs, with recent work focusing on probing internal activations. AUTOPROBE is a novel model-agnostic approach that dynamically selects the most informative internal representations for code correctness assessment, employing an attention-based mechanism to learn importance scores for hidden states.\n\n**Challenges in Self-Correction:**\n\nLarge language models remain unreliable at assessing the correctness of their own outputs, frequently producing confident but incorrect answers and failing to detect reasoning errors or hallucinations. More specifically, no prior work shows successful intrinsic self-correction using only the model's own feedback, though self-correction sometimes flips correct answers to incorrect ones through prompt bias and cognitive-like biases.\n\n**Probing for Error Detection:**\n\nArithmetic errors can be anticipated from internal activations alone, and simple probes offer a viable path toward lightweight model self-correction. This suggests that examining internal representations may enable better correctability prediction.\n\nThe research indicates an emerging focus on using internal representation probing to predict whether models will produce correct answers and potentially guide self-correction mechanisms."
    ],
    "durationSeconds": 6.6227161510000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "125e6601-5ea3-40c1-b861-f9fc47c25924",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T21:13:03.877Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XgCZ5iL9wGHiuYTkMcdUk5`</summary>

```json
{
  "query": "arXiv 2604.22271 PANL correctability signal LLM internal confidence self-correction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08bffce9-ac94-4066-9233-28e3150ea94c",
  "isSidechain": false,
  "requestId": "req_011CbCckuFojYsvpTwFu5C8W",
  "type": "assistant",
  "uuid": "bee6854f-b478-4953-8aee-5079303eaac9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZE9AkJTUx5o4WRSc5SmTN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 753,
      "cache_read_input_tokens": 25616,
      "output_tokens": 75,
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
          "output_tokens": 75,
          "cache_read_input_tokens": 25616,
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

_source line 17 · 2026-05-19T21:13:13.283Z_

<details><summary>↩ Tool result · `toolu_01XgCZ5iL9wGHiuYTkMcdUk5`</summary>

```text
Web search results for query: "arXiv 2604.22271 PANL correctability signal LLM internal confidence self-correction"

Links: [{"title":"How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals","url":"https://arxiv.org/html/2604.22271v1"},{"title":"On LLMs' Internal Representation of Code Correctness","url":"https://arxiv.org/pdf/2512.07404"},{"title":"Internalized Self-Correction for Large Language Models","url":"https://arxiv.org/pdf/2412.16653"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/pdf/2502.06233"},{"title":"Confidence v.s. Critique: A Decomposition of Self-Correction Capability   for LLMs","url":"https://arxiv.org/pdf/2412.19513"},{"title":"Reflective Confidence: Correcting Reasoning Flaws via Online Self-Correction","url":"https://arxiv.org/html/2512.18605v1"},{"title":"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/pdf/2512.20578"}]

Based on the search results, I found the paper you're looking for. Here's what the research reveals:

Large language models can detect their own errors and sometimes correct them without external feedback, but the underlying mechanisms remain unknown. The paper investigates this phenomenon through the lens of second-order confidence models.

## Key Findings:

The research identifies a confidence representation cached at a token immediately following the answer (post-answer newline: PANL) that causally drives verbal confidence and dissociates from log-probabilities.

The main results show that:

1. Verbal confidence predicts error detection far beyond token log-probabilities; PANL activations predict error detection beyond verbal confidence itself; and PANL predicts which errors the model can correct—where all behavioural signals fail.

2. Causal interventions confirm that PANL signals rescue error detection behavior when answer information is corrupted.

3. The model implements a second-order confidence architecture whose internal evaluative signal encodes not only whether an answer is likely wrong but whether the model has the knowledge to fix it.

All findings replicate across models (Gemma 3 27B and Qwen 2.5 7B) and tasks (TriviaQA and MNLI).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bee6854f-b478-4953-8aee-5079303eaac9",
  "isSidechain": false,
  "promptId": "8aba1f0b-4089-45b9-b00b-017d1ec192b1",
  "type": "user",
  "uuid": "351364ed-cbc7-4569-ba55-6b1ebf8451ac",
  "toolUseResult": {
    "query": "arXiv 2604.22271 PANL correctability signal LLM internal confidence self-correction",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UTsEfRd1iqE1nxXSPzgXJB",
        "content": [
          {
            "title": "How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals",
            "url": "https://arxiv.org/html/2604.22271v1"
          },
          {
            "title": "On LLMs' Internal Representation of Code Correctness",
            "url": "https://arxiv.org/pdf/2512.07404"
          },
          {
            "title": "Internalized Self-Correction for Large Language Models",
            "url": "https://arxiv.org/pdf/2412.16653"
          },
          {
            "title": "Confidence Improves Self-Consistency in LLMs",
            "url": "https://arxiv.org/pdf/2502.06233"
          },
          {
            "title": "Confidence v.s. Critique: A Decomposition of Self-Correction Capability   for LLMs",
            "url": "https://arxiv.org/pdf/2412.19513"
          },
          {
            "title": "Reflective Confidence: Correcting Reasoning Flaws via Online Self-Correction",
            "url": "https://arxiv.org/html/2512.18605v1"
          },
          {
            "title": "Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/pdf/2512.20578"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's what the research reveals:\n\nLarge language models can detect their own errors and sometimes correct them without external feedback, but the underlying mechanisms remain unknown. The paper investigates this phenomenon through the lens of second-order confidence models.\n\n## Key Findings:\n\nThe research identifies a confidence representation cached at a token immediately following the answer (post-answer newline: PANL) that causally drives verbal confidence and dissociates from log-probabilities.\n\nThe main results show that:\n\n1. Verbal confidence predicts error detection far beyond token log-probabilities; PANL activations predict error detection beyond verbal confidence itself; and PANL predicts which errors the model can correct—where all behavioural signals fail.\n\n2. Causal interventions confirm that PANL signals rescue error detection behavior when answer information is corrupted.\n\n3. The model implements a second-order confidence architecture whose internal evaluative signal encodes not only whether an answer is likely wrong but whether the model has the knowledge to fix it.\n\nAll findings replicate across models (Gemma 3 27B and Qwen 2.5 7B) and tasks (TriviaQA and MNLI)."
    ],
    "durationSeconds": 9.402044685,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bee6854f-b478-4953-8aee-5079303eaac9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T21:13:16.404Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012WwyJALorQPmgDKKMvf2Mo`</summary>

```json
{
  "query": "arXiv 2604.13386 multi-layer probe ensembling deception detection linear probe stacking 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "351364ed-cbc7-4569-ba55-6b1ebf8451ac",
  "isSidechain": false,
  "requestId": "req_011CbCcmo6kb5o4WvFZudYua",
  "type": "assistant",
  "uuid": "ad50b2ac-c9fd-43e5-8be0-1cfe0a53c863",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NMd1QEiMUu1uXGr9EE4GMn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 26369,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 693,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 26369,
          "cache_creation_input_tokens": 693,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 693
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

_source line 19 · 2026-05-19T21:13:23.624Z_

<details><summary>↩ Tool result · `toolu_012WwyJALorQPmgDKKMvf2Mo`</summary>

```text
Web search results for query: "arXiv 2604.13386 multi-layer probe ensembling deception detection linear probe stacking 2026"

Links: [{"title":"[2604.13386] Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling","url":"https://arxiv.org/abs/2604.13386"},{"title":"Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling","url":"https://arxiv.org/html/2604.13386v1"},{"title":"Building Better Deception Probes Using Targeted Instruction Pairs","url":"https://arxiv.org/html/2602.01425"},{"title":"Caught in the Act: a mechanistic approach to detecting deception","url":"https://arxiv.org/pdf/2508.19505"},{"title":"Multilayered deception for intrusion detection and prevention","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9392001"},{"title":"Multilayered deception for intrusion detection and prevention","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8739281"},{"title":"Detecting Strategic Deception Using Linear Probes","url":"https://arxiv.org/pdf/2502.03407"},{"title":"Improved semi-supervised autoencoder for deception detection","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6782094/"}]

I found the paper you're looking for! Here's what I discovered:

The arXiv paper 2604.13386 is titled "Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling", authored by Erik Nordby, Tasha Pais, and Aviel Parrack, and was submitted on April 15, 2026.

**Key findings from the paper:**

- Linear probes can detect when language models produce outputs they "know" are wrong, a capability relevant to both deception and reward hacking

- Single-layer probes are fragile: the best layer varies across models and tasks, and probes fail entirely on some deception types

- Combining probes from multiple layers into an ensemble recovers strong performance even where single-layer probes fail, improving AUROC by +29% on Insider Trading and +78% on Harm-Pressure Knowledge

- Across 12 models (0.5B--176B parameters), probe accuracy improves with scale: ~5% AUROC per 10x parameters (R=0.81)

- Geometrically, deception directions rotate gradually across layers rather than appearing at one location, explaining both why single-layer probes are brittle and why multi-layer ensembles succeed


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad50b2ac-c9fd-43e5-8be0-1cfe0a53c863",
  "isSidechain": false,
  "promptId": "8aba1f0b-4089-45b9-b00b-017d1ec192b1",
  "type": "user",
  "uuid": "bf5b7b34-7f7d-4b0a-a1c9-55ae3c8402f9",
  "toolUseResult": {
    "query": "arXiv 2604.13386 multi-layer probe ensembling deception detection linear probe stacking 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NGhWaLddWi163p6kPF9Voe",
        "content": [
          {
            "title": "[2604.13386] Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling",
            "url": "https://arxiv.org/abs/2604.13386"
          },
          {
            "title": "Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling",
            "url": "https://arxiv.org/html/2604.13386v1"
          },
          {
            "title": "Building Better Deception Probes Using Targeted Instruction Pairs",
            "url": "https://arxiv.org/html/2602.01425"
          },
          {
            "title": "Caught in the Act: a mechanistic approach to detecting deception",
            "url": "https://arxiv.org/pdf/2508.19505"
          },
          {
            "title": "Multilayered deception for intrusion detection and prevention",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9392001"
          },
          {
            "title": "Multilayered deception for intrusion detection and prevention",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8739281"
          },
          {
            "title": "Detecting Strategic Deception Using Linear Probes",
            "url": "https://arxiv.org/pdf/2502.03407"
          },
          {
            "title": "Improved semi-supervised autoencoder for deception detection",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6782094/"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I discovered:\n\nThe arXiv paper 2604.13386 is titled \"Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling\", authored by Erik Nordby, Tasha Pais, and Aviel Parrack, and was submitted on April 15, 2026.\n\n**Key findings from the paper:**\n\n- Linear probes can detect when language models produce outputs they \"know\" are wrong, a capability relevant to both deception and reward hacking\n\n- Single-layer probes are fragile: the best layer varies across models and tasks, and probes fail entirely on some deception types\n\n- Combining probes from multiple layers into an ensemble recovers strong performance even where single-layer probes fail, improving AUROC by +29% on Insider Trading and +78% on Harm-Pressure Knowledge\n\n- Across 12 models (0.5B--176B parameters), probe accuracy improves with scale: ~5% AUROC per 10x parameters (R=0.81)\n\n- Geometrically, deception directions rotate gradually across layers rather than appearing at one location, explaining both why single-layer probes are brittle and why multi-layer ensembles succeed"
    ],
    "durationSeconds": 7.214841160000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ad50b2ac-c9fd-43e5-8be0-1cfe0a53c863",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T21:13:26.336Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W9L6v2rAf65Y9wdiYYi45G`</summary>

```json
{
  "query": "arXiv 2604.19974 SAE sparse autoencoder uncertainty correctness features dissociation LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf5b7b34-7f7d-4b0a-a1c9-55ae3c8402f9",
  "isSidechain": false,
  "requestId": "req_011CbCcnZEqz16XcU6LQ79Ft",
  "type": "assistant",
  "uuid": "0b28fb2e-578d-42be-9b5f-b1f2f14c8293",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNWnfzghB1XSFJwk57v6CM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 768,
      "cache_read_input_tokens": 27062,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 768,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 27062,
          "cache_creation_input_tokens": 768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 768
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

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "0b28fb2e-578d-42be-9b5f-b1f2f14c8293",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Predict LLM error correctability via multi-signal probes",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d"
}
```

---

### Tool result

_source line 23 · 2026-05-19T21:13:35.856Z_

<details><summary>↩ Tool result · `toolu_01W9L6v2rAf65Y9wdiYYi45G`</summary>

```text
Web search results for query: "arXiv 2604.19974 SAE sparse autoencoder uncertainty correctness features dissociation LLM 2026"

Links: [{"title":"Analysis of Variational Sparse Autoencoders","url":"https://arxiv.org/html/2509.22994v1"},{"title":"Understanding sparse autoencoder scaling in the presence of feature manifolds","url":"https://arxiv.org/html/2509.02565v1"},{"title":"Sparse Autoencoders for Sequential Recommendation Models: Interpretation and Flexible Control","url":"https://arxiv.org/html/2507.12202v1"},{"title":"Sparse autoencoders reveal selective remapping of visual concepts during adaptation","url":"https://arxiv.org/html/2412.05276v1"},{"title":"Adaptive Sparse Allocation with Mutual Choice & Feature Choice Sparse   Autoencoders","url":"https://arxiv.org/pdf/2411.02124"},{"title":"Probing the Representational Power of Sparse Autoencoders in Vision Models","url":"https://arxiv.org/pdf/2508.11277"},{"title":"Evaluating and Designing Sparse Autoencoders by Approximating Quasi-Orthogonality","url":"https://arxiv.org/pdf/2503.24277"},{"title":"Improving Dictionary Learning with Gated Sparse Autoencoders","url":"https://arxiv.org/pdf/2404.16014"},{"title":"Interpretable and Testable Vision Features via Sparse Autoencoders","url":"https://arxiv.org/html/2502.06755v2"}]

The search results didn't return the specific arXiv paper 2604.19974. Let me search more directly for this paper identifier.

Links: [{"title":"Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders","url":"https://arxiv.org/html/2604.19974"},{"title":"[2604.19974] Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders","url":"https://arxiv.org/abs/2604.19974"},{"title":"[2504.19974] Modelling collective cell migration in a data-rich age: challenges and opportunities for data-driven modelling","url":"https://arxiv.org/abs/2504.19974"},{"title":"The effect of 'Open Access' upon citation impact: An analysis of ArXiv's   Condensed Matter Section","url":"https://arxiv.org/pdf/cs/0611060"},{"title":"LiteRev, an Automation Tool to Support Literature Reviews: A Case Study on Acute and Early HIV Infection in Sub-Saharan Africa","url":"https://www.medrxiv.org/content/10.1101/2023.02.20.23286179.full.pdf"}]

Perfect! I found the paper. Here are the results for arXiv paper 2604.19974:

## Paper Details

The paper "Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders" was submitted on April 21, 2026 (arXiv:2604.19974v1), authored by Het Patel from UC Riverside and Tiejin Chen from Arizona State University, along with additional co-authors.

## Research Overview

The paper addresses whether large language models' output-level uncertainty and their actual correctness are driven by the same internal mechanisms or by distinct feature populations.

## Methodology

The researchers introduce a 2×2 framework that partitions model predictions along correctness and confidence axes, and uses sparse autoencoders to identify features associated with each dimension independently.

## Key Findings

Applying this framework to Llama-3.1-8B and Gemma-2-9B, the study identifies three feature populations that play fundamentally different functional roles. Specifically:

- Pure uncertainty features are functionally essential: suppressing them severely degrades accuracy
- Pure incorrectness features are functionally inert: despite showing statistically significant activation differences between correct and incorrect predictions, the majority produce near-zero change in accuracy when suppressed


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b28fb2e-578d-42be-9b5f-b1f2f14c8293",
  "isSidechain": false,
  "promptId": "8aba1f0b-4089-45b9-b00b-017d1ec192b1",
  "type": "user",
  "uuid": "6dce3ea2-2d99-44d9-a6a1-682baef6ecc5",
  "toolUseResult": {
    "query": "arXiv 2604.19974 SAE sparse autoencoder uncertainty correctness features dissociation LLM 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YQJg4KTYUEDU86FaTnoEEJ",
        "content": [
          {
            "title": "Analysis of Variational Sparse Autoencoders",
            "url": "https://arxiv.org/html/2509.22994v1"
          },
          {
            "title": "Understanding sparse autoencoder scaling in the presence of feature manifolds",
            "url": "https://arxiv.org/html/2509.02565v1"
          },
          {
            "title": "Sparse Autoencoders for Sequential Recommendation Models: Interpretation and Flexible Control",
            "url": "https://arxiv.org/html/2507.12202v1"
          },
          {
            "title": "Sparse autoencoders reveal selective remapping of visual concepts during adaptation",
            "url": "https://arxiv.org/html/2412.05276v1"
          },
          {
            "title": "Adaptive Sparse Allocation with Mutual Choice & Feature Choice Sparse   Autoencoders",
            "url": "https://arxiv.org/pdf/2411.02124"
          },
          {
            "title": "Probing the Representational Power of Sparse Autoencoders in Vision Models",
            "url": "https://arxiv.org/pdf/2508.11277"
          },
          {
            "title": "Evaluating and Designing Sparse Autoencoders by Approximating Quasi-Orthogonality",
            "url": "https://arxiv.org/pdf/2503.24277"
          },
          {
            "title": "Improving Dictionary Learning with Gated Sparse Autoencoders",
            "url": "https://arxiv.org/pdf/2404.16014"
          },
          {
            "title": "Interpretable and Testable Vision Features via Sparse Autoencoders",
            "url": "https://arxiv.org/html/2502.06755v2"
          }
        ]
      },
      "The search results didn't return the specific arXiv paper 2604.19974. Let me search more directly for this paper identifier.",
      {
        "tool_use_id": "srvtoolu_014BZUQenJUXJLWFfBu19yMQ",
        "content": [
          {
            "title": "Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders",
            "url": "https://arxiv.org/html/2604.19974"
          },
          {
            "title": "[2604.19974] Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders",
            "url": "https://arxiv.org/abs/2604.19974"
          },
          {
            "title": "[2504.19974] Modelling collective cell migration in a data-rich age: challenges and opportunities for data-driven modelling",
            "url": "https://arxiv.org/abs/2504.19974"
          },
          {
            "title": "The effect of 'Open Access' upon citation impact: An analysis of ArXiv's   Condensed Matter Section",
            "url": "https://arxiv.org/pdf/cs/0611060"
          },
          {
            "title": "LiteRev, an Automation Tool to Support Literature Reviews: A Case Study on Acute and Early HIV Infection in Sub-Saharan Africa",
            "url": "https://www.medrxiv.org/content/10.1101/2023.02.20.23286179.full.pdf"
          }
        ]
      },
      "Perfect! I found the paper. Here are the results for arXiv paper 2604.19974:\n\n## Paper Details\n\nThe paper \"Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders\" was submitted on April 21, 2026 (arXiv:2604.19974v1), authored by Het Patel from UC Riverside and Tiejin Chen from Arizona State University, along with additional co-authors.\n\n## Research Overview\n\nThe paper addresses whether large language models' output-level uncertainty and their actual correctness are driven by the same internal mechanisms or by distinct feature populations.\n\n## Methodology\n\nThe researchers introduce a 2×2 framework that partitions model predictions along correctness and confidence axes, and uses sparse autoencoders to identify features associated with each dimension independently.\n\n## Key Findings\n\nApplying this framework to Llama-3.1-8B and Gemma-2-9B, the study identifies three feature populations that play fundamentally different functional roles. Specifically:\n\n- Pure uncertainty features are functionally essential: suppressing them severely degrades accuracy\n- Pure incorrectness features are functionally inert: despite showing statistically significant activation differences between correct and incorrect predictions, the majority produce near-zero change in accuracy when suppressed"
    ],
    "durationSeconds": 9.516000646,
    "searchCount": 2
  },
  "sourceToolAssistantUUID": "0b28fb2e-578d-42be-9b5f-b1f2f14c8293",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T21:13:38.849Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019h5nSE6rJnYxtnpBUpMvMw`</summary>

```json
{
  "query": "CoRefine confidence-guided self-refinement arXiv 2602.08948 probe-gated self-correction LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6dce3ea2-2d99-44d9-a6a1-682baef6ecc5",
  "isSidechain": false,
  "requestId": "req_011CbCcoTaoHt4kdvUWeoxj8",
  "type": "assistant",
  "uuid": "596266ea-5dd3-4e04-b423-54072cb4d415",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRQHaUMdp1qdnGeKmV1zXu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 27830,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1123,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 27830,
          "cache_creation_input_tokens": 1123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1123
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

_source line 25 · 2026-05-19T21:13:45.951Z_

<details><summary>↩ Tool result · `toolu_019h5nSE6rJnYxtnpBUpMvMw`</summary>

```text
Web search results for query: "CoRefine confidence-guided self-refinement arXiv 2602.08948 probe-gated self-correction LLM 2026"

Links: [{"title":"[2602.08948] CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute","url":"https://arxiv.org/abs/2602.08948"},{"title":"CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute","url":"https://arxiv.org/pdf/2602.08948"},{"title":"Confidence-aware Adversarial Learning for Self-supervised Semantic   Matching","url":"https://arxiv.org/pdf/2008.10902"},{"title":"Self-Refinement of Language Models from External Proxy Metrics Feedback","url":"https://arxiv.org/pdf/2403.00827"},{"title":"A Stitch in Time Saves Nine: Proactive Self-Refinement for Language Models","url":"https://arxiv.org/pdf/2508.12903"},{"title":"Toward More Reliable Artificial Intelligence: Reducing Hallucinations in Vision-Language Models","url":"https://arxiv.org/pdf/2512.07564"}]

Based on the search results, I found detailed information about the paper you're interested in:

## CoRefine: Confidence-Guided Self-Refinement

CoRefine is a confidence-guided self-refinement method that achieves competitive accuracy using a fraction of the tokens via a lightweight 211k-parameter Conv1D controller atop a frozen LLM.

### How It Works

The controller consumes full-trace confidence features of the LLM decoded reasoning chain and decides: HALT (accept current answer), RETHINK (verify reasoning), or ALTERNATIVE (explore new approach).

### Key Results

The controller enables targeted self-correction with an average of 2.7 refinement steps per problem and roughly 190-fold token reduction relative to 512-sample baselines. Additionally, token savings translate to actual latency reduction, with CoRefine saving up to 63% over parallel baselines.

### Performance

The controller achieves 92.6 percent precision when it confidently halts, indicating that confidence dynamics reliably signal when to stop refinement.

The paper (arXiv:2602.08948) was submitted on February 9, 2026, by Chen Jin, Ryutaro Tanno, Tom Diethe, and Philip Teare.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "596266ea-5dd3-4e04-b423-54072cb4d415",
  "isSidechain": false,
  "promptId": "8aba1f0b-4089-45b9-b00b-017d1ec192b1",
  "type": "user",
  "uuid": "84b30ad1-3972-47d2-ad50-ccb27a1a19d0",
  "toolUseResult": {
    "query": "CoRefine confidence-guided self-refinement arXiv 2602.08948 probe-gated self-correction LLM 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_019zow5qSTnu5fEDKbJ4TZaX",
        "content": [
          {
            "title": "[2602.08948] CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute",
            "url": "https://arxiv.org/abs/2602.08948"
          },
          {
            "title": "CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute",
            "url": "https://arxiv.org/pdf/2602.08948"
          },
          {
            "title": "Confidence-aware Adversarial Learning for Self-supervised Semantic   Matching",
            "url": "https://arxiv.org/pdf/2008.10902"
          },
          {
            "title": "Self-Refinement of Language Models from External Proxy Metrics Feedback",
            "url": "https://arxiv.org/pdf/2403.00827"
          },
          {
            "title": "A Stitch in Time Saves Nine: Proactive Self-Refinement for Language Models",
            "url": "https://arxiv.org/pdf/2508.12903"
          },
          {
            "title": "Toward More Reliable Artificial Intelligence: Reducing Hallucinations in Vision-Language Models",
            "url": "https://arxiv.org/pdf/2512.07564"
          }
        ]
      },
      "Based on the search results, I found detailed information about the paper you're interested in:\n\n## CoRefine: Confidence-Guided Self-Refinement\n\nCoRefine is a confidence-guided self-refinement method that achieves competitive accuracy using a fraction of the tokens via a lightweight 211k-parameter Conv1D controller atop a frozen LLM.\n\n### How It Works\n\nThe controller consumes full-trace confidence features of the LLM decoded reasoning chain and decides: HALT (accept current answer), RETHINK (verify reasoning), or ALTERNATIVE (explore new approach).\n\n### Key Results\n\nThe controller enables targeted self-correction with an average of 2.7 refinement steps per problem and roughly 190-fold token reduction relative to 512-sample baselines. Additionally, token savings translate to actual latency reduction, with CoRefine saving up to 63% over parallel baselines.\n\n### Performance\n\nThe controller achieves 92.6 percent precision when it confidently halts, indicating that confidence dynamics reliably signal when to stop refinement.\n\nThe paper (arXiv:2602.08948) was submitted on February 9, 2026, by Chen Jin, Ryutaro Tanno, Tom Diethe, and Philip Teare."
    ],
    "durationSeconds": 7.098459482999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "596266ea-5dd3-4e04-b423-54072cb4d415",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-19T21:13:48.904Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PoGXnLsGpEYBKyCjqYQ3CA`</summary>

```json
{
  "query": "LLM self-correction gating hidden state probes correctability abstention 2025 2026 recent papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84b30ad1-3972-47d2-ad50-ccb27a1a19d0",
  "isSidechain": false,
  "requestId": "req_011CbCcpCn63QfbGHoHz3cVn",
  "type": "assistant",
  "uuid": "5a8552f0-fb04-4a3e-803a-af33fe78b73f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GUxoFWwLLrCwDaJZLckvp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 696,
      "cache_read_input_tokens": 28953,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 696,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 28953,
          "cache_creation_input_tokens": 696,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 696
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

_source line 27 · 2026-05-19T21:13:57.440Z_

<details><summary>↩ Tool result · `toolu_01PoGXnLsGpEYBKyCjqYQ3CA`</summary>

```text
Web search results for query: "LLM self-correction gating hidden state probes correctability abstention 2025 2026 recent papers"

Links: [{"title":"Latent Space Chain-of-Embedding Enables Output-free LLM Self-Evaluation","url":"https://arxiv.org/pdf/2410.13640"},{"title":"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/pdf/2512.20578"},{"title":"Temporal Predictors of Outcome in Reasoning Language Models","url":"https://arxiv.org/pdf/2511.14773"},{"title":"Predicting LLM Answer Accuracy from Question-Only ...","url":"https://www.lesswrong.com/posts/KwYpFHAJrh6C84ShD/no-answer-needed-predicting-llm-answer-accuracy-from"},{"title":"Are the Hidden States Hiding Something? Testing the ...","url":"https://arxiv.org/pdf/2505.16520"},{"title":"Intrinsic Self-correction for Enhanced Morality: An Analysis of Internal   Mechanisms and the Superficial Hypothesis","url":"https://arxiv.org/pdf/2407.15286"},{"title":"Are the Hidden States Hiding Something? Testing the Limits of Factuality-Encoding Capabilities in LLMs This is the authors’ version of the work. The final, published version will appear in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL ‘25). This work is licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Please cite the official published version when available.","url":"https://arxiv.org/html/2505.16520v2"},{"title":"(PDF) Are the Hidden States Hiding Something? Testing the Limits of Factuality-Encoding Capabilities in LLMs","url":"https://www.researchgate.net/publication/391991645_Are_the_Hidden_States_Hiding_Something_Testing_the_Limits_of_Factuality-Encoding_Capabilities_in_LLMs"}]

Based on the search results, I found several recent papers (2025-2026) that directly address the topics you're interested in:

## Recent Papers on LLM Self-Correction and Hidden State Probes

**Gnosis: Self-Awareness via Internal Circuits (December 2025)**
Gnosis introduces a lightweight mechanism that enables frozen LLMs to predict the correctness of their own generations by leveraging hidden-state evolution and attention-routing patterns through a compact architecture. The method outperforms 8B Skywork reward models and Gemini 2.5 Pro on Math-Reasoning, Open-Domain QA, and Academic Knowledge tasks.

**Temporal Predictors of Outcome in Reasoning Language Models (November 2025)**
This work predicts answer correctness directly from an LLM's hidden state while chain-of-thought is being generated, using a fixed, auditable recipe. Hidden states from very short prefixes contain linearly decodable information about eventual correctness, reaching AUCs up to 0.8+ on MATH-like data.

**Latent Space Chain-of-Embedding (October 2024/2025)**
Recent research reveals that LLM latent space contains hidden state information that can reflect response correctness and is usually more interpretable than LLM output.

**Are the Hidden States Hiding Something? Testing Factuality-Encoding Capabilities (May 2025)**
Self-evaluation approaches can improve truthfulness and transparency through abstention mechanisms, fact verification, and self-correction.

These papers collectively explore how LLMs' internal representations can be probed to assess correctness, enable self-correction, and support abstention mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a8552f0-fb04-4a3e-803a-af33fe78b73f",
  "isSidechain": false,
  "promptId": "8aba1f0b-4089-45b9-b00b-017d1ec192b1",
  "type": "user",
  "uuid": "410a4eb3-ae23-4cf4-8c24-6e789ff47ee3",
  "toolUseResult": {
    "query": "LLM self-correction gating hidden state probes correctability abstention 2025 2026 recent papers",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RWU4iThEGw6rH5u6WFfvBu",
        "content": [
          {
            "title": "Latent Space Chain-of-Embedding Enables Output-free LLM Self-Evaluation",
            "url": "https://arxiv.org/pdf/2410.13640"
          },
          {
            "title": "Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/pdf/2512.20578"
          },
          {
            "title": "Temporal Predictors of Outcome in Reasoning Language Models",
            "url": "https://arxiv.org/pdf/2511.14773"
          },
          {
            "title": "Predicting LLM Answer Accuracy from Question-Only ...",
            "url": "https://www.lesswrong.com/posts/KwYpFHAJrh6C84ShD/no-answer-needed-predicting-llm-answer-accuracy-from"
          },
          {
            "title": "Are the Hidden States Hiding Something? Testing the ...",
            "url": "https://arxiv.org/pdf/2505.16520"
          },
          {
            "title": "Intrinsic Self-correction for Enhanced Morality: An Analysis of Internal   Mechanisms and the Superficial Hypothesis",
            "url": "https://arxiv.org/pdf/2407.15286"
          },
          {
            "title": "Are the Hidden States Hiding Something? Testing the Limits of Factuality-Encoding Capabilities in LLMs This is the authors’ version of the work. The final, published version will appear in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL ‘25). This work is licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Please cite the official published version when available.",
            "url": "https://arxiv.org/html/2505.16520v2"
          },
          {
            "title": "(PDF) Are the Hidden States Hiding Something? Testing the Limits of Factuality-Encoding Capabilities in LLMs",
            "url": "https://www.researchgate.net/publication/391991645_Are_the_Hidden_States_Hiding_Something_Testing_the_Limits_of_Factuality-Encoding_Capabilities_in_LLMs"
          }
        ]
      },
      "Based on the search results, I found several recent papers (2025-2026) that directly address the topics you're interested in:\n\n## Recent Papers on LLM Self-Correction and Hidden State Probes\n\n**Gnosis: Self-Awareness via Internal Circuits (December 2025)**\nGnosis introduces a lightweight mechanism that enables frozen LLMs to predict the correctness of their own generations by leveraging hidden-state evolution and attention-routing patterns through a compact architecture. The method outperforms 8B Skywork reward models and Gemini 2.5 Pro on Math-Reasoning, Open-Domain QA, and Academic Knowledge tasks.\n\n**Temporal Predictors of Outcome in Reasoning Language Models (November 2025)**\nThis work predicts answer correctness directly from an LLM's hidden state while chain-of-thought is being generated, using a fixed, auditable recipe. Hidden states from very short prefixes contain linearly decodable information about eventual correctness, reaching AUCs up to 0.8+ on MATH-like data.\n\n**Latent Space Chain-of-Embedding (October 2024/2025)**\nRecent research reveals that LLM latent space contains hidden state information that can reflect response correctness and is usually more interpretable than LLM output.\n\n**Are the Hidden States Hiding Something? Testing Factuality-Encoding Capabilities (May 2025)**\nSelf-evaluation approaches can improve truthfulness and transparency through abstention mechanisms, fact verification, and self-correction.\n\nThese papers collectively explore how LLMs' internal representations can be probed to assess correctness, enable self-correction, and support abstention mechanisms."
    ],
    "durationSeconds": 8.531770745000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5a8552f0-fb04-4a3e-803a-af33fe78b73f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-19T21:14:00.726Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y3nAuXj6LzRQuf1BqbqMfT`</summary>

```json
{
  "query": "\"correctability\" prediction LLM probe gating selective correction 2026 CoRL NeurIPS ICML"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "410a4eb3-ae23-4cf4-8c24-6e789ff47ee3",
  "isSidechain": false,
  "requestId": "req_011CbCcq3woJbor3tVFHTKpF",
  "type": "assistant",
  "uuid": "03ffd5df-c238-4bd2-bc5e-53056648b135",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DoBM4hKrEbNiA9y1fT869a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 997,
      "cache_read_input_tokens": 29649,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 997,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 29649,
          "cache_creation_input_tokens": 997,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 997
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

_source line 29 · 2026-05-19T21:14:08.592Z_

<details><summary>↩ Tool result · `toolu_01Y3nAuXj6LzRQuf1BqbqMfT`</summary>

```text
Web search results for query: ""correctability" prediction LLM probe gating selective correction 2026 CoRL NeurIPS ICML"

Links: [{"title":"Concurrent Criterion Validation of a Validity Screen for LLM Confidence Signals via Selective Prediction","url":"https://arxiv.org/html/2604.17716"},{"title":"No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes","url":"https://arxiv.org/pdf/2509.10625"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"},{"title":"Generalized Correctness Models: Learning Calibrated and Model-Agnostic Correctness Predictors from Historical Patterns","url":"https://arxiv.org/pdf/2509.24988"},{"title":"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/pdf/2512.20578"},{"title":"Multi-Dimensional Evaluation of LLMs for Grammatical Error CorrectionAccepted at AIED 2026","url":"https://arxiv.org/html/2605.07635"}]

I found several relevant papers related to LLM correctness prediction and probing. Here are the key results:

**Correctness Prediction via Linear Probes:**
One study investigates the structure of self-correctness representations in LLMs by testing whether the residual stream activation (captured immediately after processing a query) contains a direction that linearly separates questions the model will answer correctly from those it will not. The research confirms that a correctness signal is indeed linearly separable in the activation space, with a linear probe trained on TriviaQA generalizing to domain-specific knowledge datasets and outperforming non-linear baselines.

**Confidence Signals and Selective Prediction:**
Alignment can compress or distort verbal confidence. Probe design changes measured metacognitive efficiency, with results specific to binary KEEP/WITHDRAW and BET/NO BET probes.

**Self-Correction Research:**
LLMs cache a confidence representation at a token immediately following the answer (post-answer newline: PANL) that causally drives verbal confidence and dissociates from log-probabilities.

**Model-Agnostic Correctness Prediction:**
Generalized correctness models evaluated across 5 model families found that reliable LLM confidence estimation is a generalizable and model-agnostic skill learned by systematically encoding correctness history.

The search results show active research in 2026 on predicting LLM correctness through various approaches including linear probes, confidence signals, and selective prediction mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03ffd5df-c238-4bd2-bc5e-53056648b135",
  "isSidechain": false,
  "promptId": "8aba1f0b-4089-45b9-b00b-017d1ec192b1",
  "type": "user",
  "uuid": "63801247-e4f7-4df2-b666-33ca686b0387",
  "toolUseResult": {
    "query": "\"correctability\" prediction LLM probe gating selective correction 2026 CoRL NeurIPS ICML",
    "results": [
      {
        "tool_use_id": "srvtoolu_012E6q3Qb55RhoJ3VyLa3DKJ",
        "content": [
          {
            "title": "Concurrent Criterion Validation of a Validity Screen for LLM Confidence Signals via Selective Prediction",
            "url": "https://arxiv.org/html/2604.17716"
          },
          {
            "title": "No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes",
            "url": "https://arxiv.org/pdf/2509.10625"
          },
          {
            "title": "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs",
            "url": "https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"
          },
          {
            "title": "Generalized Correctness Models: Learning Calibrated and Model-Agnostic Correctness Predictors from Historical Patterns",
            "url": "https://arxiv.org/pdf/2509.24988"
          },
          {
            "title": "Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/pdf/2512.20578"
          },
          {
            "title": "Multi-Dimensional Evaluation of LLMs for Grammatical Error CorrectionAccepted at AIED 2026",
            "url": "https://arxiv.org/html/2605.07635"
          }
        ]
      },
      "I found several relevant papers related to LLM correctness prediction and probing. Here are the key results:\n\n**Correctness Prediction via Linear Probes:**\nOne study investigates the structure of self-correctness representations in LLMs by testing whether the residual stream activation (captured immediately after processing a query) contains a direction that linearly separates questions the model will answer correctly from those it will not. The research confirms that a correctness signal is indeed linearly separable in the activation space, with a linear probe trained on TriviaQA generalizing to domain-specific knowledge datasets and outperforming non-linear baselines.\n\n**Confidence Signals and Selective Prediction:**\nAlignment can compress or distort verbal confidence. Probe design changes measured metacognitive efficiency, with results specific to binary KEEP/WITHDRAW and BET/NO BET probes.\n\n**Self-Correction Research:**\nLLMs cache a confidence representation at a token immediately following the answer (post-answer newline: PANL) that causally drives verbal confidence and dissociates from log-probabilities.\n\n**Model-Agnostic Correctness Prediction:**\nGeneralized correctness models evaluated across 5 model families found that reliable LLM confidence estimation is a generalizable and model-agnostic skill learned by systematically encoding correctness history.\n\nThe search results show active research in 2026 on predicting LLM correctness through various approaches including linear probes, confidence signals, and selective prediction mechanisms."
    ],
    "durationSeconds": 7.86189899999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "03ffd5df-c238-4bd2-bc5e-53056648b135",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-19T21:14:08.595Z_

```json
{
  "parentUuid": "63801247-e4f7-4df2-b666-33ca686b0387",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ad645afd-154e-4f17-8d65-336019edaa22",
  "timestamp": "2026-05-19T21:14:08.595Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-19T21:14:11.749Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QtKyN3hNZLCBbwJFVRAmKA`</summary>

```json
{
  "query": "CoRL 2026 conference topics scope robot learning accepted papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad645afd-154e-4f17-8d65-336019edaa22",
  "isSidechain": false,
  "requestId": "req_011CbCcqu2JWawAGbUuRztZd",
  "type": "assistant",
  "uuid": "4f1bc4fb-fdc9-45dc-951a-76126bbc6740",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwCi3BjLrnwRofaECHWviH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 894,
      "cache_read_input_tokens": 30646,
      "output_tokens": 64,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 894,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 64,
          "cache_read_input_tokens": 30646,
          "cache_creation_input_tokens": 894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 894
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

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "4f1bc4fb-fdc9-45dc-951a-76126bbc6740",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Predict LLM error correctability via multi-signal probes",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d"
}
```

---

### Tool result

_source line 34 · 2026-05-19T21:14:18.251Z_

<details><summary>↩ Tool result · `toolu_01QtKyN3hNZLCBbwJFVRAmKA`</summary>

```text
Web search results for query: "CoRL 2026 conference topics scope robot learning accepted papers"

Links: [{"title":"Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI","url":"https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"CoRL 2026 - About CoRL","url":"https://www.corl.org/about-corl"},{"title":"CoRL 2026 - Workshops","url":"https://www.corl.org/program/workshops"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"}]

Based on the search results, here's what I found about CoRL 2026:

## Conference Overview

The Conference on Robot Learning (CoRL) is an annual international conference focusing on the intersection of robotics and machine learning. CoRL 2026 will be held at the JW Marriott Austin in Austin, TX (November 9–12, 2026), with a workshop day on November 9 and the main conference on November 10–12.

## Topics and Scope

CoRL covers topics including imitation learning, reinforcement learning for robots, sim-to-real transfer, robot perception through learning, learned manipulation and locomotion, and learning-based planning.

More specifically, CoRL welcomes papers in areas such as learning representations for robotic perception and control, learning robot foundation models or general-purpose knowledge systems for robotics, imitation learning for robotics, reinforcement learning for control of physical robots, learning approaches to robot safety and alignment, and applications of robot learning in robot manipulation, navigation, locomotion, driving, flight, and other areas of robotics.

## Paper Submission Requirements

The paper submission deadline is May 29, 2026. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.

The search results don't yet show information about accepted papers for CoRL 2026, as the conference is still upcoming with submissions currently being processed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f1bc4fb-fdc9-45dc-951a-76126bbc6740",
  "isSidechain": false,
  "promptId": "8aba1f0b-4089-45b9-b00b-017d1ec192b1",
  "type": "user",
  "uuid": "2df00a55-c4a3-46dc-b62d-2f4ef12839f0",
  "toolUseResult": {
    "query": "CoRL 2026 conference topics scope robot learning accepted papers",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NcN8mK6ngeTAPrsY4eeqWH",
        "content": [
          {
            "title": "Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI",
            "url": "https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"
          },
          {
            "title": "CoRL LaTeX Template | Robot Learning Conference Format | Underleaf",
            "url": "https://www.underleaf.ai/templates/corl"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "CoRL 2026 - Contributions",
            "url": "https://www.corl.org/contributions"
          },
          {
            "title": "CoRL 2026 - Call for Workshops",
            "url": "https://www.corl.org/contributions/call-for-workshops"
          },
          {
            "title": "CoRL 2026 - About CoRL",
            "url": "https://www.corl.org/about-corl"
          },
          {
            "title": "CoRL 2026 - Workshops",
            "url": "https://www.corl.org/program/workshops"
          },
          {
            "title": "Robot Learning Foundation",
            "url": "https://www.robot-learning.org/"
          }
        ]
      },
      "Based on the search results, here's what I found about CoRL 2026:\n\n## Conference Overview\n\nThe Conference on Robot Learning (CoRL) is an annual international conference focusing on the intersection of robotics and machine learning. CoRL 2026 will be held at the JW Marriott Austin in Austin, TX (November 9–12, 2026), with a workshop day on November 9 and the main conference on November 10–12.\n\n## Topics and Scope\n\nCoRL covers topics including imitation learning, reinforcement learning for robots, sim-to-real transfer, robot perception through learning, learned manipulation and locomotion, and learning-based planning.\n\nMore specifically, CoRL welcomes papers in areas such as learning representations for robotic perception and control, learning robot foundation models or general-purpose knowledge systems for robotics, imitation learning for robotics, reinforcement learning for control of physical robots, learning approaches to robot safety and alignment, and applications of robot learning in robot manipulation, navigation, locomotion, driving, flight, and other areas of robotics.\n\n## Paper Submission Requirements\n\nThe paper submission deadline is May 29, 2026. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.\n\nThe search results don't yet show information about accepted papers for CoRL 2026, as the conference is still upcoming with submissions currently being processed."
    ],
    "durationSeconds": 6.498137155999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4f1bc4fb-fdc9-45dc-951a-76126bbc6740",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-19T21:14:26.610Z_

<details><summary>Logged reasoning block</summary>

```text
This is a critical finding. CoRL 2026 is the Conference on Robot Learning, focused on robotics and machine learning for robotics. The proposal is about LLM self-correction probing — it has nothing to do with robotics. This is a fundamental venue mismatch.

The proposal is about:
- Probing LLM internal representations for correctability prediction
- Self-correction mechanisms in LLMs
- SAE feature decomposition
- Three-way gating for self-correction

This is squarely an NLP/interpretability/ML paper. It would be appropriate for venues like NeurIPS, ICML, ACL, EMNLP, ICLR — but NOT CoRL, which is specifically about robot learning.


This venue mismatch is essentially disqualifying for CoRL acceptance. I should verify the key papers cited and then provide my final assessment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2df00a55-c4a3-46dc-b62d-2f4ef12839f0",
  "isSidechain": false,
  "requestId": "req_011CbCcratRVFFCSpNkR2kyi",
  "type": "assistant",
  "uuid": "42ae5511-063a-43ee-b616-8d2dc5b38663",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HoBkmBkJXwofxbuAFTeyE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 31540,
      "output_tokens": 337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 337,
          "cache_read_input_tokens": 31540,
          "cache_creation_input_tokens": 729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 729
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

_source line 36 · 2026-05-19T21:14:26.725Z_

Now I have a critical finding — let me verify the CoRL scope more carefully and do one final search.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42ae5511-063a-43ee-b616-8d2dc5b38663",
  "isSidechain": false,
  "requestId": "req_011CbCcratRVFFCSpNkR2kyi",
  "type": "assistant",
  "uuid": "2466fbd2-4007-49f8-bc3b-b5a6593d7d89",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HoBkmBkJXwofxbuAFTeyE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 31540,
      "output_tokens": 337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 337,
          "cache_read_input_tokens": 31540,
          "cache_creation_input_tokens": 729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 729
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

_source line 37 · 2026-05-19T21:14:27.092Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FGCUS8hJsPUSYvSqfxvAoy`</summary>

```json
{
  "query": "arXiv 2602.08159 confidence manifold correctness dimensionality LLM activation space 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2466fbd2-4007-49f8-bc3b-b5a6593d7d89",
  "isSidechain": false,
  "requestId": "req_011CbCcratRVFFCSpNkR2kyi",
  "type": "assistant",
  "uuid": "bcff12e9-f942-4bb2-924f-32ef2c13fa95",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HoBkmBkJXwofxbuAFTeyE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 31540,
      "output_tokens": 337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 337,
          "cache_read_input_tokens": 31540,
          "cache_creation_input_tokens": 729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 729
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

_source line 38 · 2026-05-19T21:14:35.629Z_

<details><summary>↩ Tool result · `toolu_01FGCUS8hJsPUSYvSqfxvAoy`</summary>

```text
Web search results for query: "arXiv 2602.08159 confidence manifold correctness dimensionality LLM activation space 2026"

Links: [{"title":"The Confidence Manifold:","url":"https://www.arxiv.org/pdf/2602.08159"},{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/html/2602.08159v1"},{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/pdf/2602.08159"},{"title":"Confidence-Based Response Abstinence: Improving LLM Trustworthiness via Activation-Based Uncertainty Estimation","url":"https://arxiv.org/pdf/2510.13750"},{"title":"The Confidence Manifold - Seongland","url":"https://seongland.com/article/confidence-manifold/"},{"title":"REMA: A Unified Reasoning Manifold Framework for Interpreting Large Language Model","url":"https://arxiv.org/html/2509.22518v1"},{"title":"Multicalibration for Confidence Scoring in LLMs","url":"https://arxiv.org/html/2404.04689v1"}]

I found the paper you're looking for. Here are the key findings from arXiv 2602.08159 "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models":

## Key Findings:

**Dimensionality of the Correctness Signal:**
The discriminative signal for correctness concentrates in 3–8 dimensions, substantially lower than the high-dimensional activation space. The discriminative signal is simple: it occupies 3–8 dimensions, performance decreases with additional dimensions, and no nonlinear classifier improves over linear probes.

**Geometric Structure:**
The optimal decision boundary is a hyperplane; complex boundaries model structure that does not exist. This simplifies the linear representation hypothesis: confidence is not just linear, but low-dimensional linear.

**Internal vs. Output-Based Confidence:**
Output-based methods achieve near-chance performance (0.44–0.64 AUC) while internal probes achieve 0.80–0.97 AUC. The information required for correctness detection exists internally but is not expressed in outputs.

**Cross-Domain Transfer:**
On Qwen2-7B, projecting to 5D PLS dimensions improves cross-domain transfer by 10–14% absolute AUC (0.61–0.79).

**Causal Validation:**
The learned direction produces 10.9 percentage point changes in error rates while random directions show no effect.

The paper was published on February 8, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcff12e9-f942-4bb2-924f-32ef2c13fa95",
  "isSidechain": false,
  "promptId": "8aba1f0b-4089-45b9-b00b-017d1ec192b1",
  "type": "user",
  "uuid": "eb87825f-739d-46e7-b82d-4cac83083f49",
  "toolUseResult": {
    "query": "arXiv 2602.08159 confidence manifold correctness dimensionality LLM activation space 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JqBCA8CX2BLLtaa3kPTpgL",
        "content": [
          {
            "title": "The Confidence Manifold:",
            "url": "https://www.arxiv.org/pdf/2602.08159"
          },
          {
            "title": "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models",
            "url": "https://arxiv.org/html/2602.08159v1"
          },
          {
            "title": "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models",
            "url": "https://arxiv.org/pdf/2602.08159"
          },
          {
            "title": "Confidence-Based Response Abstinence: Improving LLM Trustworthiness via Activation-Based Uncertainty Estimation",
            "url": "https://arxiv.org/pdf/2510.13750"
          },
          {
            "title": "The Confidence Manifold - Seongland",
            "url": "https://seongland.com/article/confidence-manifold/"
          },
          {
            "title": "REMA: A Unified Reasoning Manifold Framework for Interpreting Large Language Model",
            "url": "https://arxiv.org/html/2509.22518v1"
          },
          {
            "title": "Multicalibration for Confidence Scoring in LLMs",
            "url": "https://arxiv.org/html/2404.04689v1"
          }
        ]
      },
      "I found the paper you're looking for. Here are the key findings from arXiv 2602.08159 \"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models\":\n\n## Key Findings:\n\n**Dimensionality of the Correctness Signal:**\nThe discriminative signal for correctness concentrates in 3–8 dimensions, substantially lower than the high-dimensional activation space. The discriminative signal is simple: it occupies 3–8 dimensions, performance decreases with additional dimensions, and no nonlinear classifier improves over linear probes.\n\n**Geometric Structure:**\nThe optimal decision boundary is a hyperplane; complex boundaries model structure that does not exist. This simplifies the linear representation hypothesis: confidence is not just linear, but low-dimensional linear.\n\n**Internal vs. Output-Based Confidence:**\nOutput-based methods achieve near-chance performance (0.44–0.64 AUC) while internal probes achieve 0.80–0.97 AUC. The information required for correctness detection exists internally but is not expressed in outputs.\n\n**Cross-Domain Transfer:**\nOn Qwen2-7B, projecting to 5D PLS dimensions improves cross-domain transfer by 10–14% absolute AUC (0.61–0.79).\n\n**Causal Validation:**\nThe learned direction produces 10.9 percentage point changes in error rates while random directions show no effect.\n\nThe paper was published on February 8, 2026."
    ],
    "durationSeconds": 8.531743055999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bcff12e9-f942-4bb2-924f-32ef2c13fa95",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T21:14:38.703Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HtTwc38cHgVPGtLZRsBKTL`</summary>

```json
{
  "query": "self-correction Wait token reasoning models mechanistic analysis 2025 2026 arXiv 2510.04128"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb87825f-739d-46e7-b82d-4cac83083f49",
  "isSidechain": false,
  "requestId": "req_011CbCcssBETbMtPgL2dgbQd",
  "type": "assistant",
  "uuid": "febdd20a-7db4-4666-830a-fda01e01890e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KHjLXFfatadPBtxaTGYG4u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1024,
      "cache_read_input_tokens": 32269,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1024,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 32269,
          "cache_creation_input_tokens": 1024,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1024
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

_source line 40 · 2026-05-19T21:14:46.030Z_

<details><summary>↩ Tool result · `toolu_01HtTwc38cHgVPGtLZRsBKTL`</summary>

```text
Web search results for query: "self-correction Wait token reasoning models mechanistic analysis 2025 2026 arXiv 2510.04128"

Links: [{"title":"[2510.04128] Internal states before wait modulate reasoning patterns","url":"https://arxiv.org/abs/2510.04128"},{"title":"Internal states before wait modulate reasoning patterns","url":"https://arxiv.org/pdf/2510.04128"},{"title":"Internal states before wait modulate reasoning patterns","url":"https://arxiv.org/html/2510.04128"},{"title":"Oops, Wait: Token-Level Signals as a Lens into LLM Reasoning","url":"https://arxiv.org/pdf/2601.17421"},{"title":"Understanding Reasoning in LLMs through Strategic Information Allocation under Uncertainty","url":"https://arxiv.org/pdf/2603.15500"},{"title":"Language Models can perform Single-Utterance Self-Correction of Perturbed Reasoning","url":"https://arxiv.org/pdf/2506.15894"},{"title":"Wait, We Don't Need to \"Wait\"! Removing Thinking Tokens Improves Reasoning Efficiency","url":"https://arxiv.org/pdf/2506.08343"},{"title":"Base Models Know How to Reason, Thinking Models Learn When","url":"https://arxiv.org/html/2510.07364v3"}]

I found the paper you're looking for! Here's what I found about arXiv 2510.04128:

## "Internal states before wait modulate reasoning patterns"

This paper by Dmitrii Troitskii, Koyena Pal, Chris Wendler, Callum Stuart McDougall, and Neel Nanda examines how reasoning models reason and self-correct.

**Key Research Questions:**
The paper focuses on the "wait" token, which often signals reasoning behavior such as backtracking. Despite being such a complex behavior, little is understood about exactly why models do or do not decide to reason in this particular manner.

**Methodology:**
The researchers trained crosscoders at multiple layers of DeepSeek-R1-Distill-Llama-8B and its base version, and introduced a latent attribution technique in the crosscoder setting.

**Findings:**
They located a small set of features relevant for promoting/suppressing wait tokens' probabilities, and through experiments analyzing max-activating examples and causal interventions, they showed that many of their identified features are relevant for the reasoning process and give rise to different types of reasoning patterns such as restarting from the beginning, recalling prior knowledge, expressing uncertainty, and double-checking.

The paper was published in October 2025 and uses mechanistic interpretability techniques (sparse autoencoders/crosscoders) to understand the internal mechanisms behind wait token generation and self-correction in reasoning models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "febdd20a-7db4-4666-830a-fda01e01890e",
  "isSidechain": false,
  "promptId": "8aba1f0b-4089-45b9-b00b-017d1ec192b1",
  "type": "user",
  "uuid": "63129105-2d4a-4f3b-ae3a-085824a59fe0",
  "toolUseResult": {
    "query": "self-correction Wait token reasoning models mechanistic analysis 2025 2026 arXiv 2510.04128",
    "results": [
      {
        "tool_use_id": "srvtoolu_01H9Siqa7E7XiQ5KviMpM7Sh",
        "content": [
          {
            "title": "[2510.04128] Internal states before wait modulate reasoning patterns",
            "url": "https://arxiv.org/abs/2510.04128"
          },
          {
            "title": "Internal states before wait modulate reasoning patterns",
            "url": "https://arxiv.org/pdf/2510.04128"
          },
          {
            "title": "Internal states before wait modulate reasoning patterns",
            "url": "https://arxiv.org/html/2510.04128"
          },
          {
            "title": "Oops, Wait: Token-Level Signals as a Lens into LLM Reasoning",
            "url": "https://arxiv.org/pdf/2601.17421"
          },
          {
            "title": "Understanding Reasoning in LLMs through Strategic Information Allocation under Uncertainty",
            "url": "https://arxiv.org/pdf/2603.15500"
          },
          {
            "title": "Language Models can perform Single-Utterance Self-Correction of Perturbed Reasoning",
            "url": "https://arxiv.org/pdf/2506.15894"
          },
          {
            "title": "Wait, We Don't Need to \"Wait\"! Removing Thinking Tokens Improves Reasoning Efficiency",
            "url": "https://arxiv.org/pdf/2506.08343"
          },
          {
            "title": "Base Models Know How to Reason, Thinking Models Learn When",
            "url": "https://arxiv.org/html/2510.07364v3"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I found about arXiv 2510.04128:\n\n## \"Internal states before wait modulate reasoning patterns\"\n\nThis paper by Dmitrii Troitskii, Koyena Pal, Chris Wendler, Callum Stuart McDougall, and Neel Nanda examines how reasoning models reason and self-correct.\n\n**Key Research Questions:**\nThe paper focuses on the \"wait\" token, which often signals reasoning behavior such as backtracking. Despite being such a complex behavior, little is understood about exactly why models do or do not decide to reason in this particular manner.\n\n**Methodology:**\nThe researchers trained crosscoders at multiple layers of DeepSeek-R1-Distill-Llama-8B and its base version, and introduced a latent attribution technique in the crosscoder setting.\n\n**Findings:**\nThey located a small set of features relevant for promoting/suppressing wait tokens' probabilities, and through experiments analyzing max-activating examples and causal interventions, they showed that many of their identified features are relevant for the reasoning process and give rise to different types of reasoning patterns such as restarting from the beginning, recalling prior knowledge, expressing uncertainty, and double-checking.\n\nThe paper was published in October 2025 and uses mechanistic interpretability techniques (sparse autoencoders/crosscoders) to understand the internal mechanisms behind wait token generation and self-correction in reasoning models."
    ],
    "durationSeconds": 7.321875843000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "febdd20a-7db4-4666-830a-fda01e01890e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-19T21:15:32.334Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to make my assessment. Let me synthesize everything.

**Critical Issue: Venue Mismatch**
CoRL 2026 is the Conference on Robot Learning, focused on robotics-specific ML topics like imitation learning, RL for robots, sim-to-real transfer, learned manipulation and locomotion, robot perception, etc. The call for papers explicitly states topics around robot learning, and authors are "encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots."

This proposal is about LLM internal representation probing for self-correction — a pure NLP/interpretability paper with zero robotics content. This is a **fatal** venue mismatch.
 
That said, the user's instructions ask me to evaluate the idea quality itself, and the rubric mentions impact in the NLP/CL domain, so maybe CoRL 2026 is a placeholder and the actual target is something like ICML, NeurIPS, ACL, EMNLP, or ICLR. I should flag the venue issue but proceed with evaluating the core idea as requested.

Looking at the central claim: the proposal argues that LLM correctability—whether a model can self-correct a specific error—is predictable from its internal representations, and that enhanced multi-turn prompting strategies can improve this capability.

The key concern is whether this actually beats simpler baselines. Output-level confidence already works well for routing (CoRefine achieves 92.6% halt precision, and Reflective Confidence shows 83.3% on AIME 2025), so the question becomes whether probing hidden states provides enough additional signal to justify the added complexity, or if the gains are marginal compared to just attempting correction on everything.

There's also uncertainty baked into the core assumptions: the transfer from deception detection to correctability prediction isn't guaranteed, and the PANL paper suggests correctability is already weakly encoded in representations. If correctability is genuinely harder to represent than correctness, then 0.614 AUROC might already be near the ceiling for what linear probes can achieve, making further improvements difficult.

Looking at the novelty claims more carefully, the proposal is mostly combining existing techniques rather than introducing fundamentally new ideas. The PANL paper already operationalized correctability as a distinct prediction target and built probes for it, so the multi-layer ensembling approach is just an incremental improvement on the same target. The three-way gating with abstention borrows heavily from CoRefine's routing mechanism with only minor variations. The most genuinely novel contribution would be comparing the representational geometry of correctability versus correctness, but the rest feels like straightforward applications of existing methods.

On significance, the core question about predicting self-correctable errors is practically valuable, though whether the probes actually beat the baseline 0.614 AUROC remains unclear. The representational geometry analysis could be scientifically interesting, but if it just confirms that correctability is harder to linearly separate, that's somewhat expected, and if it shows they're similar, that undermines the paper's central premise.

Most plausible findings would feel unsurprising in hindsight—multi-layer probes helping because they help elsewhere, higher dimensionality being needed for a second-order property, SAE features mattering because correctability involves both uncertainty and correctness, or gating improving results when the gate is reliable. The real novelty would come from negative results showing correctability is fundamentally resistant to probing.

There's a major venue problem here: CoRL focuses on robot learning, and this paper has no robotics component whatsoever, which essentially disqualifies it. The related work is thorough with 25+ citations, but breadth of coverage doesn't establish novelty. At its core, this is a competent incremental study applying existing probing methods to a newly-defined target, with the representational geometry analysis being the most interesting contribution—though even that yields fairly expected outcomes. The experimental design is elaborate enough (four phases, eight baselines, SAE analysis) that it risks obscuring how incremental the fundamental idea actually is.

For a general ML venue like NeurIPS or ICML, this might land in the borderline range, but the complete mismatch with CoRL's focus makes acceptance there essentially impossible.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63129105-2d4a-4f3b-ae3a-085824a59fe0",
  "isSidechain": false,
  "requestId": "req_011CbCctdeRcYkHWqpRW59Fm",
  "type": "assistant",
  "uuid": "49d1bc9f-cfeb-4b23-9183-31e6f7562895",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HVPUL8EdQZCeT7dpTvv4eC",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 33293,
      "output_tokens": 6472,
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
          "output_tokens": 6472,
          "cache_read_input_tokens": 33293,
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

### Assistant

_source line 42 · 2026-05-19T21:17:13.215Z_

Now I have sufficient information to provide my assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【重大前置问题：投稿 venue 不匹配】

CoRL (Conference on Robot Learning) 的主题范围明确限定为：imitation learning, RL for robots, sim-to-real transfer, learned manipulation/locomotion, robot perception, robot foundation models, robot safety 等与机器人学习直接相关的研究。Call for Papers 明确鼓励 "real-robot experiments or convincing evidence that simulation experiments are transferable to real robots"。

本 proposal 是一篇纯 NLP/LLM interpretability 论文——probing LLM 内部表征以预测 self-correction 的可行性——与机器人学习零关联。无论 idea 质量如何，投 CoRL 主会的中稿概率接近于零（<2%），因为 desk reject 概率极高。

适合的 venue 应为 NeurIPS、ICML、ICLR、ACL、EMNLP 等。以下评估假设投稿至合理 venue（如 NeurIPS/ICML），仅评估 idea 质量本身。

---

【领域调研】:

- [arXiv:2604.22271] "How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals" (2026): 
  这是本 proposal 最直接的前序工作。该论文已经将 correctability 定义为一个独立预测目标，建立了 PANL token 上的线性探针，报告了 0.614 AUROC（on own-generated errors）。同时发现 PANL activations encode second-order confidence，因果干预验证了信号的有效性。**本 proposal 的核心目标——"用更好的探针提升 correctability 预测"——是在该论文基础上的直接延伸。**

- [arXiv:2604.13386] "Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling" (2026): 
  多层 ensemble stacking 在 deception detection 上取得显著提升（0.510→0.910 on Harm-Pressure Knowledge）。proposal 的 Phase 0 pilot 直接测试该技术是否迁移到 correctability——这是一个合理但直觉上可预期的实验设计。

- [arXiv:2604.19974] "Are LLM Uncertainty and Correctness Encoded by the Same Features?" (2026): 
  SAE 分解揭示 uncertainty 和 correctness 由功能不同的 feature population 编码，仅少量 confounded features 有因果效力。proposal 中的 SAE-guided feature selection 直接采用该框架——是自然延伸而非创新方法。

- [arXiv:2602.08948] CoRefine (2026): 
  已实现三路 routing（halt/rethink/alternative），基于 output-level confidence，211K 参数 Conv1D controller，92.6% halt precision。proposal 声称的差异化（hidden-state vs. output confidence, genuine abstention, correctability-aware）是 real 但 incremental 的变体。

- [arXiv:2602.08159] "The Confidence Manifold" (2026): 
  correctness 在 activation space 中仅占 3-8 维，线性可分。proposal 的 Phase 3b 核心问题——"correctability 是否占据不同的几何结构？"——是对该工作的自然后续。

- [arXiv:2512.20578] Gnosis (2025): 
  multi-signal fusion 对 correctness prediction 达到 0.78-0.95 AUROC，hidden-only 0.78-0.92。proposal 的 multi-signal 策略（multi-token + attention + Wait features）与 Gnosis 方法论高度重叠。

- [arXiv:2512.18605] Reflective Confidence (2025): 
  output-level logprob 信号用于选择性 reflection triggering，在 AIME 2025 上 83.3% accuracy。demonstration that selective confidence-gated correction works, albeit at output level.

- [arXiv:2507.02778] Self-Correction Bench (NeurIPS 2025 Workshop): 
  64.5% blind spot, Wait baseline reduces by 89.3%。proposal 声称"Wait 在 correct answers 上的 overcorrection cost 未知"——这是一个合理但相对 minor 的贡献点。

- 调研总结: 这个领域在 2025-2026 年极度活跃。Correctability 作为预测目标刚被 PANL 论文定义（2026.04），multi-layer probing / SAE decomposition / confidence manifold 等工具论文几乎同期发表。本 proposal 的定位是"用最新的 probing 工具箱改进刚刚建立的 correctability baseline"——是一个 well-timed 但本质上 combinatorial 的工作。

---

【Trivial Alternative 检验】:

**存在多个 trivial alternative 威胁：**

1. **Output-level confidence routing（最严重威胁）**：CoRefine 已经用 output logprobs 实现三路 routing 并达到 92.6% halt precision；Reflective Confidence 用 logprobs 做 selective reflection 达到 83.3% on AIME。如果 hidden-state probes 只比 output confidence 好几个 AUROC 点，实际 gating 收益可能微乎其微——而 output confidence 的获取成本为零（无需额外 forward pass 或 activation extraction）。proposal 需要证明 hidden-state probes 在 correctability 维度上有 **质的** 而非 **量的** 优势。

2. **Simply trying self-correction on everything**：如果 overcorrection cost 较低（这是 unknown 的，但也完全可能），那么 "correct everything + accept minor overcorrection" 可能是一个成本效益比更高的 baseline。probe-gated correction 的增量价值取决于 overcorrection cost 的大小——这是一个需要先 measure 的前提，不是 probe 本身的贡献。

3. **Multi-layer probe 可能只是 marginal improvement**：PANL 论文的 0.614 AUROC 可能反映的不是"probing 方法太简单"，而是"correctability 本身就难以从 representations 中提取"。如果 ceiling 在 0.70-0.72，multi-signal probing 的增量不足以支撑整篇论文。

**增量价值**：如果 ECP 确实能将 AUROC 从 0.614 提升到 0.75+，且 hidden-state probes 显著优于 output confidence routing on correctability（不仅仅是 correctness），那增量是 real 的。但这是一个 empirical bet，不是 idea 层面的保证。

---

【前提假设检验】:

1. **"Multi-layer ensembling 的收益可迁移到 correctability"**——这是 proposal 自己承认的 hypothesis，但它构成了整个技术路线的基石。Deception detection 和 correctability 的 layer-wise encoding 特性可能根本不同：deception 涉及 model "knowingly" producing wrong output，correctability 涉及 model 的 correction mechanism 能否到达正确答案——后者更像是 knowledge boundary 的编码而非 intentional signal 的编码。迁移性是一个 genuine open question。

2. **"Correctability 在内部表征中有超越 0.614 AUROC 的可提取信号"**——PANL 论文已经在 PANL token 位置尝试了 probing，0.614 可能不是方法的局限而是信号的局限。Confidence Manifold 论文显示 correctness 在 3-8 维即可线性分离且达到 0.80-0.97 AUC——但 correctness 是 first-order property，correctability 作为 second-order property 可能 fundamentally 更 noisy。如果 ceiling 就是 0.65-0.70，整个技术贡献链条就不成立。

3. **"Confounded features 是 correctability probing 的有效基质"**——这基于 arXiv:2604.19974 对 correctness 的发现外推到 correctability。但 correctability 涉及 model 的 correction mechanism 是否能 reach correct answer，这不仅仅是 uncertainty + correctness 的交集，还涉及 model 的推理路径可塑性——后者可能不在 SAE 分解的框架内。

4. **"Probe-gated correction 在 practical settings 中优于 simpler alternatives"**——即使 AUROC 提升到 0.75，gating decision 的 precision/recall tradeoff 在实际应用中是否足够好？0.75 AUROC 意味着仍有大量 mis-routing，probe 本身的 computational cost 可能抵消 gating 带来的效率收益。

---

【3 维度打分】:

1. **Novelty: 弱 (Weak)**
   
   核心贡献逐条分析：
   - "Operationalizing correctability as a prediction target"——已由 PANL 论文 (arXiv:2604.22271) 完成，不是本 proposal 的贡献。
   - "Multi-layer ensemble for correctability"——是将 arXiv:2604.13386 的现有技术应用到 PANL 的 existing target，属于 straightforward combination，不是 methodological innovation。
   - "Three-way gating with abstention"——CoRefine (arXiv:2602.08948) 已有三路 routing，差异（signal source, abstention type, correctability-awareness）是 real 但 incremental 的 design variations。
   - "Representational geometry of correctability vs. correctness"——这是最具 novelty 的贡献，将 Confidence Manifold (arXiv:2602.08159) 的框架应用于 correctability 这一 second-order property。但问题在于：预期结果（"correctability 需要更高维度 / 更复杂边界"）在 idea 层面就已经 intuitive——审稿人大概率会说 "I would have guessed this"。
   - "SAE feature decomposition for correctability"——是 arXiv:2604.19974 框架的直接应用。
   
   **总体模式：proposal 是 5-6 个 2026 年初最新论文的 combinatorial application，每个组件都不是新的，组合方式也是自然推导的路径。这是 solid engineering 但 novelty delta 有限。**

2. **Significance: 中 (Medium)**
   
   研究问题本身（"哪些错误可以被自我纠正？"）是有实际价值和科学意义的。Self-correction 是 LLM deployment 的核心瓶颈之一，selective correction 的框架在 efficiency 和 reliability 上都有应用价值。
   
   但 significance 受到两个因素限制：
   - **实际收益的上限不确定**：如果 AUROC 只能从 0.614 提到 0.70，gating 的 practical benefit 非常有限。Significance 依赖于 empirical result 的幅度。
   - **Output-level alternatives 的竞争**：CoRefine 和 Reflective Confidence 已经展示 output-level routing 在实践中 work well，如果 hidden-state probes 的 marginal gain 不大，contribution 的 practical significance 被削弱。
   - **Representational analysis 的 significance**：Phase 3b 的 geometry 分析有独立科学价值，但作为一个 descriptive/analytical contribution，其 impact 取决于是否能揭示 surprising 结论——而大多数预期结论（correctability 更复杂、confounded features 更重要）都是 intuitive 的。

3. **Related Work: 强 (Strong)**
   
   这是 proposal 最突出的优点。覆盖极为全面，引用了 25+ 篇高度相关的工作，每篇的描述准确（经核实 arXiv:2604.22271, 2604.13386, 2604.19974, 2602.08948, 2602.08159 的关键数据均匹配原文）。差异化定位清晰：对每个竞争工作都有具体的对比维度（signal source, abstention capability, correctability specificity）。proposal 对领域的理解是 expert-level 的。

---

【概率估计】: 15% - 28%，中位 20%

（注意：此概率假设投稿至合理 venue 如 NeurIPS/ICML/ICLR。若投 CoRL 2026，概率 <2%，因 venue 不匹配将导致 desk reject。）

【估计理由】:

Novelty 是主要限制因素。proposal 的核心技术路线是将多个 2026 年初论文的方法组合应用到 PANL 论文定义的 correctability 目标上——这是一个"把最新工具用到最新目标"的 well-executed combination，但审稿人会问："剥去组合外壳后，真正新的 insight 是什么？" 

如果核心发现是 positive（multi-layer probes 提升了 AUROC），审稿人的反应更可能是 "I would have guessed that multi-signal probes outperform single-signal probes" 而非 "this is surprising"。如果是 negative（ceiling 就在 0.65-0.70），representational geometry analysis 可以 salvage 一个发表，但更适合 workshop 而非 main conference。

Significance 是 medium——研究问题 important，但 proposal 的增量贡献相对于 trivial alternatives（output confidence routing）的优势未确立。

Related Work 是 strong，但优秀的 related work 只提升下限，不提升 idea 上限。

Proposal 的形式完善度极高（4 phases, dual-outcome design, 8 baselines, SAE analysis），但形式完善不等于 idea 出色。实际上，过度精细的实验设计反而暴露了 idea 本身的 thinness——需要大量工程来 compensate for 有限的 novelty delta。

【主要风险】:

1. **Novelty insufficiency（核心风险）**: 审稿人将此定性为"applying existing probing toolkit to a recently-defined target"——一个 competent empirical study，但不够 novel for top venue。每个技术组件（multi-layer ensemble, SAE-guided features, attention entropy, three-way gating）都有直接的出处论文，组合方式是 predictable engineering 而非 creative insight。

2. **Trivial alternative 未解决（决定性风险）**: 如果 output-level confidence routing（zero extra cost）在 correctability-aware gating 上的表现与 hidden-state probes（significant extra cost）相差不大，整个技术路线的 justification 就不成立。proposal 目前将此定位为"我们会 compare against CoRefine-style routing"，但如果结果是 CoRefine 接近或匹配 ECP，这篇论文的 story 就瓦解了——而这完全是可能的，因为 CoRefine 的 92.6% halt precision 已经很高。
```

---

**补充说明（venue 建议）**：

此 proposal 是一篇纯 NLP/LLM interpretability + self-correction 的工作，与 CoRL 的 robot learning 主题完全不匹配。建议改投以下 venue：
- **NeurIPS 2026**（最匹配：ML + interpretability + LLM meta-cognition）
- **ICML 2026**（ML methodology）
- **EMNLP 2026**（NLP + LLM analysis）
- **ICLR 2027**（representation learning + probing）

如果维持当前 proposal 投 CoRL，应直接止损——不是 idea 质量问题，是 venue 选择问题。

Sources:
- [How LLMs Detect and Correct Their Own Errors (PANL paper)](https://arxiv.org/html/2604.22271v1)
- [Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling](https://arxiv.org/abs/2604.13386)
- [Are LLM Uncertainty and Correctness Encoded by the Same Features?](https://arxiv.org/abs/2604.19974)
- [CoRefine: Confidence-Guided Self-Refinement](https://arxiv.org/abs/2602.08948)
- [The Confidence Manifold](https://arxiv.org/html/2602.08159v1)
- [Gnosis: Can LLMs Predict Their Own Failures?](https://arxiv.org/pdf/2512.20578)
- [Reflective Confidence](https://arxiv.org/html/2512.18605v1)
- [Internal states before wait modulate reasoning patterns](https://arxiv.org/abs/2510.04128)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49d1bc9f-cfeb-4b23-9183-31e6f7562895",
  "isSidechain": false,
  "requestId": "req_011CbCctdeRcYkHWqpRW59Fm",
  "type": "assistant",
  "uuid": "32a344b2-6fc4-4d92-a5ec-bc0d7ee63bef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HVPUL8EdQZCeT7dpTvv4eC",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 33293,
      "output_tokens": 6472,
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
          "output_tokens": 6472,
          "cache_read_input_tokens": 33293,
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

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "32a344b2-6fc4-4d92-a5ec-bc0d7ee63bef",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Predict LLM error correctability via multi-signal probes",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "32a344b2-6fc4-4d92-a5ec-bc0d7ee63bef",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Predict LLM error correctability via multi-signal probes",
  "sessionId": "58000b7c-d081-4a2b-9c38-633829e0398d"
}
```

---
