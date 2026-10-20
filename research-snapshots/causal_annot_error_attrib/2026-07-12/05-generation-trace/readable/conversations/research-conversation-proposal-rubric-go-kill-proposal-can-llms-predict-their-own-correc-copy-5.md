# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Can LLMs Predict Their Own Correc

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/fd340454-b3c3-4e14-b94c-a1c862bbde3e.jsonl`
- **Structured JSON:** [`0bac208a12c090438f0b.json`](../../sessions/0b/0bac208a12c090438f0b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T18:59:30.906Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T18:59:30.906Z",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction\n\n## Description\nWe investigate whether LLMs' internal representations can predict which of their errors are self-correctable, and whether this prediction enables selective correction that outperforms both ungated correction, the trivial 'Wait' baseline, and confidence-based routing. Prior work shows a faint correctability signal at the post-answer newline token (PANL) achieving only 0.614 AUROC with a single-layer linear probe — insufficient for reliable gating. We develop Enhanced Correctability Probes (ECP) that combine multi-layer ensemble stacking, multi-token features (PANL + last-answer-token + reasoning tokens), attention-entropy features, pre-Wait hidden-state features (informed by crosscoder analysis of Wait-token mechanisms, arXiv:2510.04128), and SAE-guided feature selection targeting the confounded feature intersection that bridges uncertainty and correctness (motivated by the functional dissociation finding of arXiv:2604.19974, where 68% of pure incorrectness features are causally inert). We begin with a Phase 0 pilot that directly tests whether multi-layer ensembling — which improved deception detection AUROC by up to 78% (arXiv:2604.13386, specifically on Harm-Pressure Knowledge in Llama-70B) — transfers to the fundamentally different task of correctability prediction. These probes gate a three-way decision: retain the original answer (likely correct), attempt correction including probe-selective Wait insertion (error detected, high correctability), or abstain (error detected, low correctability). This framework is distinguished from CoRefine's (arXiv:2602.08948) three-way routing — which uses output-level confidence, lacks genuine abstention, and is not correctability-aware — by using hidden-state probes, providing a genuine abstention option for unfixable errors, and explicitly predicting error fixability rather than confidence. Critically, we provide the first evaluation of the 'Wait' baseline on correct answers, measuring its previously-unknown overcorrection cost. We also conduct the first representational geometry and SAE feature decomposition analysis of correctability vs. correctness, testing whether correctability — a second-order property that depends not just on whether the model is wrong but on whether correction mechanisms can reach the right answer — shares the low-dimensional, linearly-separable structure that correctness exhibits (arXiv:2602.08159), requires higher dimensionality or non-linear boundaries, or depends disproportionately on the narrow confounded feature population identified by arXiv:2604.19974. This analysis, combined with error depth characterization (arXiv:2601.00828) and threshold analysis mapping probe quality to gating utility, ensures publishable contributions even if probe AUROC plateaus at marginal levels. We evaluate across Gemma-3-27B, Qwen-2.5-7B-Instruct, and Mistral-Small-3.2-24B on TriviaQA, MMLU, and GSM8K, comparing against eight baselines including ungated correction, Wait (universal and probe-selective), confidence-based routing (CoRefine-style and Reflective Confidence-style), PAG, and oracle gating. Our contributions are: (1) operationalizing correctability as a prediction target distinct from correctness, (2) the first pilot testing whether multi-layer ensembling transfers from deception to correctability, (3) the first hidden-state probe-based gating with genuine abstention for correctability-aware self-correction — distinguished from CoRefine's confidence-based routing by signal source, abstention capability, and correctability specificity, (4) the first representational geometry and SAE feature decomposition comparison of correctability vs. correctness, testing whether second-order properties have a different confounded-feature signature than first-order properties, and (5) establishing the conditions — including minimum probe quality thresholds — under which probe-gated correction outperforms simpler alternatives including confidence-based controllers.\n\n## Core Problem\nLLMs attempt correction on all detected errors equally, but ~64.5% of self-generated errors are uncorrectable. Recent work reveals a faint internal 'correctability' signal at the post-answer newline token (PANL), but it achieves only 0.614 AUROC on own-generated errors using a single-layer linear probe — barely actionable for reliable gating. Meanwhile, trivial interventions like appending 'Wait' reduce blind spots by 89.3% on known errors, but their overcorrection rate on correct answers is completely untested. Confidence-based controllers like CoRefine (arXiv:2602.08948) achieve efficient three-way routing (halt/rethink/explore-alternative) using output-level logprobs, but they do not distinguish between correctable and uncorrectable errors — treating all detected issues as potentially fixable. Critically, correctability is a second-order property — it depends not just on whether the model is wrong, but on whether the model's correction mechanism can reach the right answer — and recent SAE analysis (arXiv:2604.19974) reveals that uncertainty and correctness are encoded by functionally distinct feature populations, with only rare 'confounded' features bridging both signals. It is unknown whether correctability — which inherently requires engaging both axes — shares the favorable geometric properties (low dimensionality, linear separability) that correctness exhibits, or whether it requires targeting the narrow confounded feature intersection. Can enhanced multi-signal probes substantially improve correctability prediction, what is the representational relationship between correctability, correctness, and uncertainty at the feature level, and under what conditions does probe-gated correction with genuine abstention outperform both ungated correction and simpler confidence-based alternatives?\n\n## Opportunity\nThree converging findings create a clear research opportunity: (1) The PANL paper (arXiv:2604.22271) establishes that correctability is partially encoded in internal representations, but their single-layer, single-token linear probe barely exceeds chance (0.614 AUROC) on own-generated errors — leaving substantial room for improvement. For correctness prediction on adjacent tasks, Gnosis-style multi-signal fusion (arXiv:2512.20578) achieves 0.78–0.92 AUROC on hidden states alone (with the lower end on MMLU-Pro; ablation on Qwen3-1.7B only) and 0.80–0.95 with attention fusion, while attention-head entropy probes (arXiv:2602.13699) achieve +0.06 AUROC absolute improvement in OOD settings (0.70→0.76 average, 8.5% relative vs. Lookback Lens). Multi-layer probe ensembling (arXiv:2604.13386) has dramatically improved deception detection AUROC (0.510→0.910 on Harm-Pressure Knowledge in Llama-70B), though whether similar gains transfer to correctability — a fundamentally different property — is an open empirical question that motivates our pilot experiment. (2) The 'Wait' baseline from Self-Correction Bench (arXiv:2507.02778) is powerful but fundamentally non-selective: it was tested only on known errors, never on correct answers, so its overcorrection cost is unknown. QwQ-32B naturally generates 'Wait' as its first correction token 37.7–76.8% of the time depending on benchmark (SCLI5 to PRM800K-SC), but this behavior varies widely across models and is near-zero for non-reasoning models. Recent mechanistic work shows that internal states before Wait tokens causally modulate distinct reasoning patterns — restarting, recalling, uncertainty expression, and double-checking (arXiv:2510.04128, EMNLP 2025 Findings) — and that Wait token probabilities correlate with reasoning correctness in ways that vary by training strategy (arXiv:2601.17421). These findings suggest Wait's effectiveness is not uniform but depends on which reasoning pattern it triggers, creating an opportunity for probe-selective application. Reflective Confidence (arXiv:2512.18605) demonstrates a related approach, transforming low-confidence output signals into reflection triggers rather than stopping, achieving 83.3% accuracy on AIME 2025 vs. 70.0% for Self-Consistency — but uses only output-level logprobs, not internal representations. (3) Existing gating approaches occupy adjacent niches but leave a clear gap. CoRefine (arXiv:2602.08948) implements three-way routing (halt/rethink/alternative) via a 211K-parameter Conv1D controller on output-level confidence, achieving 92.6% halt precision — but its decisions are confidence-based rather than correctability-aware, and its ALTERNATIVE option explores different approaches rather than genuinely abstaining when errors are likely unfixable. Four concurrent probe-gating papers address correctness, early exit, abstention, or reflection control — but none probe for correctability (whether a specific error is fixable), and none combine hidden-state probes with genuine abstention in a correctability-aware framework. Moreover, the SAE dissociation paper (arXiv:2604.19974) reveals that uncertainty and correctness are encoded by functionally distinct feature populations — with 68% of pure incorrectness features being causally inert and only rare confounded features (102 out of 1,057 in Llama-3.1-8B) bridging both signals to achieve 0.79 AUROC with just 3 features. This finding directly challenges naive linear probing over broad activations and suggests correctability prediction may need to target the narrow confounded feature intersection, motivating our SAE-guided probe design and representational analysis.\n\n## Related Work / Landscape\nThe PANL paper (arXiv:2604.22271) establishes correctability prediction as a distinct task from error detection, achieving 0.986 AUROC for detection but only 0.614 for correctability on own-generated errors using single-layer logistic regression at one token position. This gap — high detectability but low correctability prediction — is the central technical challenge. Gnosis (arXiv:2512.20578) achieves 0.80–0.95 AUROC for correctness prediction by fusing final-layer hidden states with attention-map features via a ~5M-parameter architecture; notably, the hidden-state stream alone achieves 0.78–0.92 AUROC (with the lower end on MMLU-Pro; ablation only reported for Qwen3-1.7B), with attention fusion adding 0–3 points depending on the task. The multi-layer ensembling paper (arXiv:2604.13386) shows that logistic stacking across complementary layers can dramatically improve probe performance — achieving 0.510→0.910 AUROC on the hardest deception detection task (Harm-Pressure Knowledge, Llama-70B) — because informative directions rotate across layers and double-fault analysis reveals complementary error patterns between early and late layers. However, this result is specific to deception detection, which has different layer-wise encoding properties than correctness or correctability; whether analogous gains transfer is an empirical hypothesis we test via a Phase 0 pilot. For correctness prediction specifically, multi-signal approaches show more modest but consistent gains: attention-head entropy probes (arXiv:2602.13699) improve OOD AUROC by +0.06 absolute (0.70→0.76 average across 5 models, an 8.5% relative improvement over Lookback Lens), and perturbation-stability probes (arXiv:2505.21772) add +6 AUROC points via targeted adversarial perturbations to hidden states. SWIFT (arXiv:2505.12225) concatenates all-layer hidden states with learned gating weights to extract token-level quality signals.\n\nThe Self-Correction Bench (arXiv:2507.02778) documents the 64.5% blind spot and shows 'Wait' reduces it by 89.3%. QwQ-32B naturally generates 'Wait' as its first correction token at rates varying by benchmark (37.7% on SCLI5, 72.5% on GSM8K-SC, 76.8% on PRM800K-SC), but this behavior is model-specific — other reasoning models show different patterns and non-reasoning models rarely generate Wait spontaneously. The Wait baseline was never tested on correct answers, leaving the overcorrection cost unknown. Two recent papers provide mechanistic understanding of Wait tokens: arXiv:2510.04128 (EMNLP 2025 Findings) trains crosscoders on DeepSeek-R1-Distill-Llama-8B to identify features that promote or suppress Wait tokens, discovering causal features for distinct reasoning patterns (restarting, recalling, uncertainty expression, double-checking) via activation steering at layer 15; arXiv:2601.17421 systematically analyzes Wait and other discourse tokens across model scales and training strategies, finding that Wait token probabilities correlate with reasoning correctness but that models exploit this signal only partially. Reflective Confidence (arXiv:2512.18605) proposes a related approach, transforming low-confidence output-level logprob signals into reflection triggers rather than early stopping, achieving 83.3% accuracy on AIME 2025 (vs. 70.0% Self-Consistency, K=32) on Qwen3-8B — demonstrating that selective confidence-gated correction can significantly outperform non-selective baselines, though it uses output-level signals rather than internal representations and does not model correctability.\n\nCoRefine (arXiv:2602.08948) is the closest existing system to our three-way gating, implementing halt/rethink/alternative decisions via a 211K-parameter Conv1D controller that consumes output-level confidence traces from the frozen LLM. It achieves 92.6% halt precision, averages 2.7 refinement steps per problem, and reduces tokens ~190× relative to 512-sample baselines on mathematical reasoning benchmarks. However, CoRefine differs from our proposal in three fundamental ways: (a) it uses output-level logprobs rather than hidden-state probes, missing the richer internal signal that PANL demonstrates exists; (b) its HALT decision accepts the current answer — it never genuinely abstains or flags for external intervention when errors are likely unfixable; (c) its routing is confidence-based, not correctability-aware — it cannot distinguish correctable from uncorrectable errors, treating all low-confidence outputs as potentially improvable. Four concurrent probe-gating papers occupy adjacent niches: arXiv:2507.12379 probes for arithmetic errors and selectively re-prompts (only 6–12% of detected errors actually get corrected); arXiv:2504.05419 uses probes for early exit from reasoning chains (AUROC 0.77–0.91 for correctness, not correctability); arXiv:2604.18419 trains value-function probes for dynamic mid-generation abstention; arXiv:2506.12217 uses activation steering to modulate self-reflection frequency. None of these probe for correctability specifically, and none combine hidden-state probes with genuine abstention in a correctability-aware framework.\n\nA critical finding for our probing approach comes from arXiv:2604.19974, which uses sparse autoencoders to decompose LLM representations into functionally distinct feature populations. In Llama-3.1-8B, they identify 700 pure uncertainty features, 255 pure incorrectness features, and only 102 confounded features encoding both signals. The key insight is a functional dissociation: 68% of pure incorrectness features are causally inert (mean accuracy delta of -0.03% when suppressed), while pure uncertainty features are essential for model performance, and only confounded features bridging both axes are causally effective for correctness prediction — with just 3 confounded features from layer 18 achieving 0.79 AUROC. This has direct implications for correctability probing: correctability is inherently a joint uncertainty+correctness concept (the model must be wrong AND the correction mechanism must be able to reach the right answer), so probes targeting broad activation spaces risk relying on functionally inert incorrectness features. This motivates our SAE-guided feature analysis in Phase 3b and suggests that the confounded feature intersection — not the full activation space — may be the effective substrate for correctability prediction, potentially explaining why the single-layer PANL probe achieves only 0.614 AUROC.\n\nThe Confidence Manifold (arXiv:2602.08159) shows correctness occupies only 3–8 dimensions in activation space and is linearly separable with as few as 25 labeled examples. However, correctability is a second-order property: it depends not just on whether the model is wrong, but on whether the model's correction mechanism can reach the right answer given the model's knowledge state and reasoning pathways. The Interpretability-without-Actionability paper (arXiv:2603.18353) provides indirect evidence that this second-order property may be harder to capture: even with 98.2% detection AUROC, activation steering corrected only 20–24% of errors (concept-bottleneck steering) or 0% (SAE feature steering), revealing a 53-percentage-point knowledge-action gap. This suggests correctability may occupy a different — possibly higher-dimensional or non-linear — representational subspace than correctness, and the SAE dissociation finding (arXiv:2604.19974) provides a mechanistic explanation: correctability may require engaging the narrow confounded feature population rather than the broader (but functionally inert) incorrectness features. The Truth-as-a-Trajectory framework (arXiv:2603.01326) proposes that cross-layer displacement vectors capture properties that static single-layer probes miss, potentially relevant to second-order properties like correctability. The Accuracy-Correction Paradox (arXiv:2601.00828) shows weaker models achieve 1.6× higher correction rates and proposes the Error Depth Hypothesis — that stronger models make fewer but deeper errors that resist self-correction — providing a taxonomy of error correctable characteristics. The information-theoretic analysis of correlated errors (Preprints.org 202601.0892) formalizes bounds on self-correction when generator and evaluator share failure modes, motivating external probe-based gating as a mechanism to break the correlation. LLMs also encode problem difficulty as a linearly decodable property (arXiv:2510.18147, ρ ≈ 0.88), suggesting that related meta-cognitive properties may be extractable, though correctability's second-order nature makes direct analogy uncertain.\n\n## Approach\nWe propose a four-phase study of correctability prediction and selective self-correction, including an explicit pilot to validate the multi-layer ensemble transfer hypothesis, SAE-guided feature analysis informed by the uncertainty-correctness dissociation (arXiv:2604.19974), and a contribution plan that is robust to negative results.\n\n**Phase 0: Pilot Feasibility Study.** Before committing to the full experimental pipeline, we run a targeted pilot on the PANL paper's existing correctability labels (Gemma-3-27B, TriviaQA subset). We train independent logistic regression probes at each of the ~42 layers, identify complementary layers via double-fault analysis (following arXiv:2604.13386's methodology), and build a 3–5 layer stacked ensemble. This pilot directly tests whether the multi-layer ensembling technique that improved deception detection AUROC by up to 78% transfers to correctability prediction. Success criterion: if the ensemble achieves ≥0.70 AUROC (meaningful improvement over the 0.614 single-layer baseline), we proceed to Phase 1. If the ensemble plateaus below 0.70, we shift emphasis to the representational geometry and SAE feature analysis (Phase 3b), which remains a publishable contribution. Estimated cost: ~15 H100-hours (single model, single dataset, multi-layer extraction only).\n\n**Phase 1: Enhanced Correctability Probes (ECP).** We move beyond the PANL paper's single-layer, single-token linear probe by developing multi-signal correctability probes. (a) Multi-layer ensemble: train independent logistic regression probes at each layer, select 3–5 complementary layers via double-fault analysis, combine via logistic stacking (following arXiv:2604.13386, but with the explicit caveat that this technique was validated on deception detection — our Phase 0 tests transfer to correctability). (b) Multi-token features: concatenate hidden states from the post-answer newline token (PANL), the last answer token (LAT), and the last 2 reasoning tokens — the PANL paper's own causal analysis shows LAT carries complementary information at different layers. (c) Attention-based features: extract per-head entropy statistics across semantic sections (question, reasoning, answer), following the methodology of arXiv:2602.13699 which achieves +0.06 AUROC absolute improvement over Lookback Lens in OOD correctness prediction. (d) Wait-token features: inspired by the crosscoder analysis of arXiv:2510.04128, extract hidden-state features at the position immediately preceding natural Wait tokens (when present), capturing the causal features that modulate reasoning patterns (restarting, recalling, uncertainty expression, double-checking). The insight from arXiv:2601.17421 that Wait token probabilities correlate with reasoning correctness suggests these features encode meta-cognitive state relevant to correctability. (e) SAE-guided feature selection: motivated by arXiv:2604.19974's finding that only confounded features (encoding both uncertainty and correctness) are causally effective while pure incorrectness features are functionally inert, we train SAEs on our target models and identify confounded features relevant to correctability. We then compare probes trained on (i) full activation spaces, (ii) SAE-reconstructed activations from confounded features only, and (iii) SAE-reconstructed activations excluding pure incorrectness features. This tests whether the narrow confounded feature intersection — rather than broad activations — is the effective substrate for correctability prediction, and whether filtering out causally inert features improves probe AUROC. (f) Non-linear probe ablation: compare linear probes, 2-layer MLPs (hidden dim 16/32), and SWIFT-style all-layer gated aggregation — motivated by the possibility that correctability, as a second-order property, may require non-linear boundaries even if correctness is linearly separable in 3–8 dimensions (arXiv:2602.08159). All probes are trained on on-policy correctability labels generated by running the model's actual self-correction pipeline (multiple correction attempts per error to get calibrated fixability scores), avoiding the distribution mismatch of synthetic error injection documented in SCoRe (arXiv:2409.12917).\n\n**Phase 2: Three-Way Gated Self-Correction.** Use the ECP to implement a three-way decision at inference time: (i) if the error detection probe indicates the answer is likely correct, retain the original answer; (ii) if the error is detected AND the correctability probe predicts high fixability (above a calibrated threshold), attempt correction — either prompting-based correction or probe-selective Wait insertion (applying Wait only when the probe detects both an error and high correctability, leveraging the mechanistic finding from arXiv:2510.04128 that Wait triggers different reasoning patterns depending on internal state); (iii) if the error is detected but correctability is predicted as low, abstain or flag for external intervention. This design is distinguished from CoRefine's (arXiv:2602.08948) three-way routing in three key ways: we use hidden-state probes rather than output-level confidence, our third option is genuine abstention (declining to answer) rather than exploring alternative approaches, and our gating is explicitly correctability-aware — routing based on predicted fixability rather than confidence level. Where CoRefine optimizes compute efficiency (achieving ~190× token reduction), our framework optimizes decision quality by preventing wasted correction attempts on unfixable errors and avoiding overcorrection of correct answers.\n\n**Phase 3: Comprehensive Evaluation.** Evaluate across three dense models where probing is well-understood: Gemma-3-27B (same as PANL paper, validates signal transfer), Qwen-2.5-7B-Instruct (same as PANL paper, smaller scale), and Mistral-Small-3.2-24B (different architecture family, tests generalization). Use three benchmarks (TriviaQA, MMLU, GSM8K) with 10K+ questions each. Compare gated correction against eight baselines: (1) no correction, (2) ungated prompting-based correction, (3) Wait-appended correction applied to all answers — measuring the previously-untested overcorrection rate, (4) Wait-appended correction applied only to probe-detected errors, (5) confidence-threshold gating using log-probabilities (following Reflective Confidence's approach, arXiv:2512.18605), (6) CoRefine-style output-confidence routing (arXiv:2602.08948) — retrained on our models/benchmarks for fair comparison, (7) PAG-style generative verification (arXiv:2506.10406), (8) oracle gating (upper bound). Conduct ablations on: probe architecture (linear vs. MLP vs. ensemble vs. SAE-guided), feature sources (PANL-only vs. multi-token vs. +attention vs. +Wait-features vs. +SAE-confounded), layer selection, cross-task transferability, and threshold sensitivity analysis showing at what AUROC level gating begins to outperform ungated correction.\n\n**Phase 3b: Representational Geometry and Feature Decomposition of Correctability (Robust to Negative Probe Results).** Regardless of probe performance, we conduct a dedicated analysis of the representational relationship between correctability, correctness, and uncertainty at the feature population level. (a) Subspace comparison: compute the principal components of correctness and correctability representations separately (following arXiv:2602.08159's methodology) and measure subspace alignment via principal angle analysis — testing whether correctability occupies the same 3–8 dimensional subspace as correctness or requires distinct dimensions. (b) Dimensionality analysis: determine how many dimensions encode correctability vs. correctness at each layer, and whether correctability requires higher dimensionality (consistent with its second-order nature). (c) Non-linearity characterization: compare linear vs. non-linear probe AUROC gaps for correctability vs. correctness — a larger gap for correctability would indicate it occupies a more complex geometric region. (d) SAE feature decomposition: train SAEs on our target models and decompose correctability-predictive features into pure uncertainty, pure incorrectness, and confounded populations (following arXiv:2604.19974's 2×2 framework). Test whether confounded features are disproportionately important for correctability prediction compared to correctness prediction — which would provide mechanistic evidence that correctability requires simultaneously engaging both uncertainty and correctness axes. Measure the causal efficacy of each population via suppression experiments: if suppressing pure incorrectness features has minimal effect on correctability prediction (paralleling the functional inertness finding for correctness), this confirms the narrow confounded intersection hypothesis and explains the representational ceiling for broad-activation linear probes. (e) Error depth analysis: using the Error Depth Hypothesis framework (arXiv:2601.00828), characterize what makes errors correctable vs. uncorrectable — surface-level errors (calculation mistakes, recall failures) vs. deep errors (fundamental misunderstanding, missing knowledge) — and test whether this taxonomy is reflected in representational distance and SAE feature activation patterns. (f) Cross-layer trajectory analysis: inspired by Truth-as-a-Trajectory (arXiv:2603.01326), examine whether correctability is better captured by cross-layer displacement vectors than by static single-layer activations, which would explain why single-layer probes struggle. This phase yields publishable insights regardless of whether the ECP achieves high AUROC, providing the first empirical characterization of how correctability is (or is not) represented in LLM internal states and the first application of the SAE uncertainty-correctness dissociation framework to a second-order property.\n\n## Inspiration\nThe gap between 0.614 AUROC (single-layer PANL probe) and the consistently higher performance of multi-signal probes on correctness prediction (Gnosis hidden-only: 0.78–0.92; attention entropy: +0.06 AUROC absolute in OOD) suggests correctability prediction has room for improvement with better probing methodology — though the magnitude of potential gains is uncertain given correctability's second-order nature. The dramatic improvement from multi-layer ensembling on deception detection (0.510→0.910; arXiv:2604.13386) demonstrates that multi-layer stacking can rescue failing single-layer probes, but transferability to correctability is a hypothesis to test, not a guaranteed outcome. The SAE dissociation finding (arXiv:2604.19974) — that only rare confounded features bridging uncertainty and correctness are causally effective — provides both a challenge and an opportunity: correctability probes may need to target this narrow feature intersection, but successfully doing so could yield more principled and interpretable predictions than broad-activation probing. The untested overcorrection cost of the 'Wait' baseline, combined with new mechanistic understanding of Wait tokens' causal role in triggering distinct reasoning patterns (arXiv:2510.04128, arXiv:2601.17421), creates a clear opportunity for probe-selective Wait application. CoRefine (arXiv:2602.08948) demonstrates the viability of learned three-way routing for self-correction but uses output-level confidence without correctability awareness or genuine abstention — leaving a well-defined gap for hidden-state probe-based gating that distinguishes correctable from uncorrectable errors. Key untried combination: multi-signal enhanced probes for correctability prediction informed by SAE feature analysis + three-way gating with genuine abstention + comparison against Wait and confidence-based controllers, with explicit analysis of what makes correctability representationally distinct from correctness at the feature population level.\n\n## Key References\n- How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals (arXiv:2604.22271, 2026) — establishes PANL correctability signal, 0.614 AUROC baseline\n- Self-Correction Bench: Uncovering and Addressing the Self-Correction Blind Spot in LLMs (arXiv:2507.02778, NeurIPS 2025 Workshop) — 64.5% blind spot, Wait baseline achieving 89.3% reduction; QwQ-32B generates Wait first-token at 37.7–76.8% depending on benchmark\n- Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling (arXiv:2604.13386, 2026) — multi-layer stacking on deception detection: +29% on Insider Trading, +78% on Harm-Pressure Knowledge (0.510→0.910 in Llama-70B); transfer to correctability is a hypothesis we test\n- Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits — Gnosis (arXiv:2512.20578, 2025) — multi-signal fusion for correctness prediction: hidden-only 0.78–0.92 AUROC (ablation on Qwen3-1.7B), fusion 0.80–0.95 AUROC\n- Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders (arXiv:2604.19974, 2026) — SAE decomposition reveals functionally distinct feature populations: 68% of pure incorrectness features are causally inert; only rare confounded features (102/1,057 in Llama-3.1-8B) bridge uncertainty and correctness, achieving 0.79 AUROC with 3 features from layer 18; directly informs our probe design and Phase 3b analysis\n- CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute (arXiv:2602.08948, 2026) — three-way routing (halt/rethink/alternative) via 211K-parameter Conv1D controller on output-level confidence; 92.6% halt precision, ~190× token reduction; differs from our approach in signal source (output logprobs vs. hidden-state probes), decision type (no genuine abstention), and gating criterion (confidence vs. correctability)\n- Reflective Confidence: Correcting Reasoning Flaws via Online Self-Correction (arXiv:2512.18605, 2025) — transforms low-confidence output signals into reflection triggers; 83.3% on AIME 2025 vs. 70.0% Self-Consistency; uses output-level logprobs, no correctability modeling\n- Internal states before wait modulate reasoning patterns (arXiv:2510.04128, EMNLP 2025 Findings) — crosscoders identify causal features promoting/suppressing Wait tokens; distinct reasoning patterns (restarting, recalling, uncertainty expression, double-checking) triggered by pre-Wait internal states\n- Oops, Wait: Token-Level Signals as a Lens into LLM Reasoning (arXiv:2601.17421, Jan 2026) — Wait token probabilities correlate with reasoning correctness; models exploit Wait signals only partially; implications for token-level steering\n- Probing for Arithmetic Errors in Language Models (arXiv:2507.12379, 2025) — probe-guided selective re-prompting, 6–12% correction rate\n- Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification (arXiv:2504.05419, 2025) — probe-gated early exit, AUROC 0.77–0.91\n- Knowing When to Quit: A Principled Framework for Dynamic Abstention in LLM Reasoning (arXiv:2604.18419, 2026) — value-function probes for abstention gating\n- From Emergence to Control: Probing and Modulating Self-Reflection in Language Models (arXiv:2506.12217, 2025) — self-reflection vector steering\n- The Confidence Manifold (arXiv:2602.08159, 2026) — correctness in 3–8 dimensions, 25-example sufficiency, linearly separable\n- Attention Head Entropy of LLMs Predicts Answer Correctness (arXiv:2602.13699, 2026) — per-head 2-Rényi entropy achieves OOD AUROC 0.76 average (+0.06 absolute, 8.5% relative improvement over Lookback Lens)\n- PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier (arXiv:2506.10406, 2025)\n- Understanding the Dark Side of LLMs' Intrinsic Self-Correction (ACL 2025) — overcorrection and cognitive biases\n- Interpretability without Actionability (arXiv:2603.18353, 2026) — knowledge-action gap: 98.2% detection AUROC but only 20–24% correction via steering, 53-point gap\n- Mining Intrinsic Rewards from LLM Hidden States — SWIFT (arXiv:2505.12225, 2025) — all-layer gated aggregation\n- Between the Layers Lies the Truth (arXiv:2603.22299, 2026) — cross-layer agreement features\n- Truth as a Trajectory (arXiv:2603.01326, 2026) — cross-layer displacement vectors capture properties missed by static single-layer probes\n- Training Language Models to Self-Correct via Reinforcement Learning — SCoRe (arXiv:2409.12917, 2024) — on-policy training data importance\n- Large Language Models Cannot Self-Correct Reasoning Yet (ICLR 2024)\n- Decomposing LLM Self-Correction: The Accuracy-Correction Paradox (arXiv:2601.00828, 2026) — Error Depth Hypothesis: weaker models achieve 1.6× higher correction rates; deeper errors resist self-correction\n- No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes (arXiv:2509.10625, ICLR 2026 Workshop)\n- Calibrating LLM Confidence by Probing Perturbed Representation Stability (arXiv:2505.21772, 2025) — +6 AUROC points via adversarial perturbation stability\n- LLMs Encode How Difficult Problems Are (arXiv:2510.18147, 2025) — difficulty linearly decodable (ρ ≈ 0.88); meta-cognitive properties extractable but correctability's second-order nature makes transfer uncertain\n- Limits of Self-Correction in LLMs: An Information-Theoretic Analysis of Correlated Errors (Preprints.org 202601.0892, Feb 2026) — formalizes bounds on self-correction with correlated generator-evaluator errors\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '220–280 H100-hours (Phase 0 pilot: ~15 hrs; inference for 3 models × ~30K questions × 3 passes [initial + Wait + correction] + multi-layer hidden state extraction across ~10 layers + attention feature extraction + Wait-feature extraction + SAE training and feature decomposition + probe training + representational geometry analysis + ablations)', 'timeline': '11–13 weeks (includes pilot, SAE analysis, full experiments, geometry analysis, paper writing)', 'estimated_gpu_cost': '$550–700 (at ~$2.50/H100-hr on cloud providers)'}\n- **human_in_loop**: {'gpu_hours': '220–280 H100-hours (same compute, faster iteration via AI-assisted code/analysis)', 'timeline': '8–10 weeks', 'claude_api_cost': '$150–210 (experiment orchestration, SAE analysis notebooks, geometry visualization, paper drafting via Sonnet 4.6)', 'estimated_gpu_cost': '$550–700'}\n- **auto_research**: {'gpu_hours': '300–360 H100-hours (overhead from automated probe architecture sweeps, SAE training and decomposition, threshold optimization, representational geometry grid, and broader ablation grid)', 'timeline': '2–3 weeks wall-clock', 'claude_api_cost': '$420–580 (full pipeline orchestration, code generation, debugging, SAE analysis, statistical analysis, visualization, paper drafting)', 'estimated_gpu_cost': '$750–900', 'speed_bottleneck': 'Sequential multi-layer hidden state extraction over ~90K forward passes (3 models × 30K questions); extraction requires full-precision activations at 5–10 layers per pass and cannot be batched as aggressively as standard inference; SAE training adds ~20–30 H100-hours per model'}\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T18:59:30.909Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T18:59:30.909Z",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e"
}
```

---

## Round 1

46 recorded events

### User

_source line 3 · 2026-05-19T18:59:30.923Z_

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
  "promptId": "032757f9-b233-4ec3-9ca3-db9f978295b0",
  "type": "user",
  "uuid": "a35c9cb8-1302-49a7-89d2-8fd03de978e9",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T18:59:30.922Z_

```json
{
  "parentUuid": "a35c9cb8-1302-49a7-89d2-8fd03de978e9",
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
  "uuid": "8e695aef-8648-4cee-9cb9-5016c092ff5a",
  "timestamp": "2026-05-19T18:59:30.922Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T18:59:30.922Z_

```json
{
  "parentUuid": "8e695aef-8648-4cee-9cb9-5016c092ff5a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "693d8f20-3dc5-486a-ab85-1d270b728392",
  "timestamp": "2026-05-19T18:59:30.922Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
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
  "leafUuid": "693d8f20-3dc5-486a-ab85-1d270b728392",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Predict correctability of LLM self-corrections",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e"
}
```

---

### Assistant

_source line 8 · 2026-05-19T18:59:50.899Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for CoRL 2026 (Conference on Robot Learning). Let me first note something important: the proposal is about LLM self-correction and probing internal representations - this is an NLP/mechanistic interpretability topic, not a robotics topic. CoRL is a robotics conference. This is a significant mismatch that I should flag.

Wait, let me re-read the instructions. The user says "评估其投稿 CoRL 2026 主会的中稿潜力". CoRL = Conference on Robot Learning. 

But this proposal is entirely about LLM self-correction probing, which is an NLP/AI topic, not robotics. This is a critical issue. Actually, let me reconsider - maybe the user means a different conference? Let me check - CoRL could also be... no, CoRL is Conference on Robot Learning. But the proposal mentions NLP/CL领域. The evaluation rubric mentions "研究问题是否重要、对 NLP/CL 领域的影响力", so it's explicitly about NLP/CL impact. Maybe the user made a mistake about the venue, or they're using "CoRL" to mean something else. Either way, I should just proceed with the evaluation using the rubric they provided.

There's definitely a venue mismatch here - if this is truly CoRL, the proposal has essentially zero chance of acceptance since it's completely off-topic. But the system prompt clearly indicates an NLP conference context, so I'll proceed with the evaluation and flag this potential confusion. Before I make any judgments though, I need to do some web searches to understand the current landscape of LLM self-correction work.

I'm looking into recent developments in LLM self-correction and correctness prediction, the PANL paper specifically, multi-layer probing techniques for analyzing LLM internal states, SAE-based approaches to uncertainty and correctness detection, and confidence-based routing systems like CoRefine.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "693d8f20-3dc5-486a-ab85-1d270b728392",
  "isSidechain": false,
  "requestId": "req_011CbCSaS8DEhpmxXkg1z6zj",
  "type": "assistant",
  "uuid": "ca55e74f-0dd4-45b0-93dd-f789f71b4688",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8anZtzNrhoTbpeUD2RryY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 24620,
      "output_tokens": 705,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 705,
          "cache_read_input_tokens": 24620,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 9 · 2026-05-19T18:59:50.902Z_

我需要先进行领域调研，然后才能客观评估这个 proposal。让我先加载 WebSearch 工具，然后进行多次针对性搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca55e74f-0dd4-45b0-93dd-f789f71b4688",
  "isSidechain": false,
  "requestId": "req_011CbCSaS8DEhpmxXkg1z6zj",
  "type": "assistant",
  "uuid": "023398f1-504c-40f1-b63d-5d1b824123a2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8anZtzNrhoTbpeUD2RryY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 24620,
      "output_tokens": 705,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 705,
          "cache_read_input_tokens": 24620,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 10 · 2026-05-19T18:59:51.023Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016cS3z7pQnmwAAjQ8hNUkCN`</summary>

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
  "parentUuid": "023398f1-504c-40f1-b63d-5d1b824123a2",
  "isSidechain": false,
  "requestId": "req_011CbCSaS8DEhpmxXkg1z6zj",
  "type": "assistant",
  "uuid": "28d44271-1f5a-4bf6-a1d8-38537c229fb0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K8anZtzNrhoTbpeUD2RryY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 24620,
      "output_tokens": 705,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 705,
          "cache_read_input_tokens": 24620,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 11 · 2026-05-19T18:59:51.030Z_

<details><summary>↩ Tool result · `toolu_016cS3z7pQnmwAAjQ8hNUkCN`</summary>

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
  "parentUuid": "28d44271-1f5a-4bf6-a1d8-38537c229fb0",
  "isSidechain": false,
  "promptId": "032757f9-b233-4ec3-9ca3-db9f978295b0",
  "type": "user",
  "uuid": "d0d94913-bd26-47b9-8960-ab3010c873b2",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "28d44271-1f5a-4bf6-a1d8-38537c229fb0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T18:59:53.961Z_

<details><summary>Logged reasoning block</summary>

```text
Good, now let me conduct the required web searches. I'll do multiple targeted searches to understand the field landscape.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0d94913-bd26-47b9-8960-ab3010c873b2",
  "isSidechain": false,
  "requestId": "req_011CbCSbv3mUhtYAfEGFKQvz",
  "type": "assistant",
  "uuid": "a7477290-e69a-4204-8fcf-2c0be4665898",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QasiQFkQqncaALGR58acZA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1231,
      "cache_read_input_tokens": 24620,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1231,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 365,
          "cache_read_input_tokens": 24620,
          "cache_creation_input_tokens": 1231,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1231
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

_source line 13 · 2026-05-19T18:59:54.512Z_

现在开始进行领域调研。让我同时发起多个搜索请求。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7477290-e69a-4204-8fcf-2c0be4665898",
  "isSidechain": false,
  "requestId": "req_011CbCSbv3mUhtYAfEGFKQvz",
  "type": "assistant",
  "uuid": "958e3e2d-c55d-44a8-8d54-bd88733030d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QasiQFkQqncaALGR58acZA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1231,
      "cache_read_input_tokens": 24620,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1231,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 365,
          "cache_read_input_tokens": 24620,
          "cache_creation_input_tokens": 1231,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1231
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

_source line 14 · 2026-05-19T18:59:55.028Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HneQaP7T8qsRtvjuKyjC4J`</summary>

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
  "parentUuid": "958e3e2d-c55d-44a8-8d54-bd88733030d3",
  "isSidechain": false,
  "requestId": "req_011CbCSbv3mUhtYAfEGFKQvz",
  "type": "assistant",
  "uuid": "4dc04f5f-3145-44b1-b8f3-2349699cd551",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QasiQFkQqncaALGR58acZA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1231,
      "cache_read_input_tokens": 24620,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1231,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 365,
          "cache_read_input_tokens": 24620,
          "cache_creation_input_tokens": 1231,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1231
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

_source line 15 · 2026-05-19T18:59:55.535Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015xDwuSVQVJzFpCj8X5kWHZ`</summary>

```json
{
  "query": "arXiv 2604.22271 PANL correctability signal LLM internal confidence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dc04f5f-3145-44b1-b8f3-2349699cd551",
  "isSidechain": false,
  "requestId": "req_011CbCSbv3mUhtYAfEGFKQvz",
  "type": "assistant",
  "uuid": "da4440d2-5c17-44cc-ba60-b0298a08cb38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QasiQFkQqncaALGR58acZA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1231,
      "cache_read_input_tokens": 24620,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1231,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 365,
          "cache_read_input_tokens": 24620,
          "cache_creation_input_tokens": 1231,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1231
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

_source line 16 · 2026-05-19T18:59:56.453Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TV3K9dXEwrX1Fz1wmc9669`</summary>

```json
{
  "query": "multi-layer ensemble probing LLM deception detection arXiv 2604.13386 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da4440d2-5c17-44cc-ba60-b0298a08cb38",
  "isSidechain": false,
  "requestId": "req_011CbCSbv3mUhtYAfEGFKQvz",
  "type": "assistant",
  "uuid": "9a3eff72-c9ba-45cc-9e18-79ec4dc358bc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QasiQFkQqncaALGR58acZA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1231,
      "cache_read_input_tokens": 24620,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1231,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 365,
          "cache_read_input_tokens": 24620,
          "cache_creation_input_tokens": 1231,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1231
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

_source line 17 · 2026-05-19T18:59:56.991Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W2z9rAT3ahS69bxAYwXxNS`</summary>

```json
{
  "query": "CoRefine confidence-guided self-refinement arXiv 2602.08948 three-way routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a3eff72-c9ba-45cc-9e18-79ec4dc358bc",
  "isSidechain": false,
  "requestId": "req_011CbCSbv3mUhtYAfEGFKQvz",
  "type": "assistant",
  "uuid": "a0cc0b09-dd76-41b7-8bdc-ba0339d0fc25",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QasiQFkQqncaALGR58acZA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1231,
      "cache_read_input_tokens": 24620,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1231,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 365,
          "cache_read_input_tokens": 24620,
          "cache_creation_input_tokens": 1231,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1231
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

_source line 18 · 2026-05-19T18:59:57.327Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TmCLATdpH1wZWQkRAP4Ku6`</summary>

```json
{
  "query": "SAE sparse autoencoder uncertainty correctness dissociation LLM features arXiv 2604.19974"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0cc0b09-dd76-41b7-8bdc-ba0339d0fc25",
  "isSidechain": false,
  "requestId": "req_011CbCSbv3mUhtYAfEGFKQvz",
  "type": "assistant",
  "uuid": "7a0b3938-23f6-4031-8d51-a1943cad300d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QasiQFkQqncaALGR58acZA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1231,
      "cache_read_input_tokens": 24620,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1231,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 365,
          "cache_read_input_tokens": 24620,
          "cache_creation_input_tokens": 1231,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1231
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

_source line 19 · 2026-05-19T19:00:02.587Z_

<details><summary>↩ Tool result · `toolu_01HneQaP7T8qsRtvjuKyjC4J`</summary>

```text
Web search results for query: "LLM self-correction correctability prediction internal representations probing 2025 2026"

Links: [{"title":"Predicting LLM Answer Accuracy from Question-Only ...","url":"https://arxiv.org/pdf/2509.10625"},{"title":"Model-Agnostic Correctness Assessment for LLM-Generated Code via Dynamic Internal Representation Selection","url":"https://arxiv.org/pdf/2510.02934"},{"title":"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/pdf/2512.20578"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"},{"title":"Probing for Arithmetic Errors in Language Models","url":"https://arxiv.org/pdf/2507.12379"},{"title":"Internalized Self-Correction for Large Language Models","url":"https://arxiv.org/pdf/2412.16653"}]

Based on the search results, here are the key findings related to LLM self-correction, correctability prediction, and internal representation probing from 2025-2026:

## Recent Research Directions

**Correctness Prediction from Internal Representations:**

Research is investigating the structure of self-correctness representations in LLMs, with work testing the Linear Representation Hypothesis for correctness using residual stream activations.

**Model-Agnostic Correctness Assessment:**

AUTOPROBE is a novel model-agnostic approach that dynamically selects the most informative internal representations for code correctness assessment, employing an attention-based mechanism to learn importance scores for hidden states.

**Self-Awareness via Internal Circuits:**

Large language models remain unreliable at assessing the correctness of their own outputs. Research is exploring whether LLMs can anticipate their own failures by examining the internal dynamics that govern their generation process.

**Limitations of Self-Correction:**

LLMs cannot correct their own reasoning without external feedback—and correction attempts can actually make things worse. Additionally, self-correction sometimes flips correct answers to incorrect ones through prompt bias and cognitive-like biases.

**Probing for Error Detection:**

Arithmetic errors can be anticipated from internal activations alone, and simple probes offer a viable path toward lightweight model self-correction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4dc04f5f-3145-44b1-b8f3-2349699cd551",
  "isSidechain": false,
  "promptId": "032757f9-b233-4ec3-9ca3-db9f978295b0",
  "type": "user",
  "uuid": "44973ad8-602f-4005-a0e5-299b44728aca",
  "toolUseResult": {
    "query": "LLM self-correction correctability prediction internal representations probing 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KdVPuEiKseceGHmkVKPvaP",
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
      "Based on the search results, here are the key findings related to LLM self-correction, correctability prediction, and internal representation probing from 2025-2026:\n\n## Recent Research Directions\n\n**Correctness Prediction from Internal Representations:**\n\nResearch is investigating the structure of self-correctness representations in LLMs, with work testing the Linear Representation Hypothesis for correctness using residual stream activations.\n\n**Model-Agnostic Correctness Assessment:**\n\nAUTOPROBE is a novel model-agnostic approach that dynamically selects the most informative internal representations for code correctness assessment, employing an attention-based mechanism to learn importance scores for hidden states.\n\n**Self-Awareness via Internal Circuits:**\n\nLarge language models remain unreliable at assessing the correctness of their own outputs. Research is exploring whether LLMs can anticipate their own failures by examining the internal dynamics that govern their generation process.\n\n**Limitations of Self-Correction:**\n\nLLMs cannot correct their own reasoning without external feedback—and correction attempts can actually make things worse. Additionally, self-correction sometimes flips correct answers to incorrect ones through prompt bias and cognitive-like biases.\n\n**Probing for Error Detection:**\n\nArithmetic errors can be anticipated from internal activations alone, and simple probes offer a viable path toward lightweight model self-correction."
    ],
    "durationSeconds": 7.554090100000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4dc04f5f-3145-44b1-b8f3-2349699cd551",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T19:00:04.191Z_

<details><summary>↩ Tool result · `toolu_015xDwuSVQVJzFpCj8X5kWHZ`</summary>

```text
Web search results for query: "arXiv 2604.22271 PANL correctability signal LLM internal confidence"

Links: [{"title":"How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals","url":"https://arxiv.org/html/2604.22271v1"},{"title":"On LLMs' Internal Representation of Code Correctness","url":"https://arxiv.org/pdf/2512.07404"},{"title":"How do LLMs Compute Verbal Confidence?","url":"https://arxiv.org/html/2603.17839v1"},{"title":"Correctness Assessment of Code Generated by Large Language Models Using Internal Representations","url":"https://arxiv.org/pdf/2501.12934"},{"title":"Model-Agnostic Correctness Assessment for LLM-Generated Code via Dynamic Internal Representation Selection","url":"https://arxiv.org/pdf/2510.02934"},{"title":"Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders","url":"https://arxiv.org/html/2604.19974"},{"title":"No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes","url":"https://arxiv.org/pdf/2509.10625"},{"title":"Use of Retrieval-Augmented Large Language Model for COVID-19 Fact-Checking: Development and Usability Study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12079058/"}]

Based on the search results, I found the paper you're looking for. Here's what the research is about:

The paper investigates how large language models can detect their own errors and sometimes correct them without external feedback through the lens of second-order models of confidence from decision neuroscience.

**Key Findings:**

The research shows that verbal confidence predicts error detection far beyond token log-probabilities, PANL activations predict error detection beyond verbal confidence itself, and PANL predicts which errors the model can correct—where all behavioral signals fail.

Causal interventions confirm that PANL signals rescue error detection behavior when answer information is corrupted.

**What is PANL:**

PANL stands for post-answer newline—a token immediately following the answer that caches a confidence representation and causally drives verbal confidence while dissociating from log-probabilities.

**Main Contribution:**

The results reveal that LLMs naturally implement a second-order confidence architecture whose internal evaluative signal encodes not only whether an answer is likely wrong but whether the model has the knowledge to fix it.

All findings replicate across models (Gemma 3 27B and Qwen 2.5 7B) and tasks (TriviaQA and MNLI).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da4440d2-5c17-44cc-ba60-b0298a08cb38",
  "isSidechain": false,
  "promptId": "032757f9-b233-4ec3-9ca3-db9f978295b0",
  "type": "user",
  "uuid": "ebb6ef81-e166-4668-a006-e175173b2a30",
  "toolUseResult": {
    "query": "arXiv 2604.22271 PANL correctability signal LLM internal confidence",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JwM3M1ZYGAT1SX1vb7ePSu",
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
            "title": "How do LLMs Compute Verbal Confidence?",
            "url": "https://arxiv.org/html/2603.17839v1"
          },
          {
            "title": "Correctness Assessment of Code Generated by Large Language Models Using Internal Representations",
            "url": "https://arxiv.org/pdf/2501.12934"
          },
          {
            "title": "Model-Agnostic Correctness Assessment for LLM-Generated Code via Dynamic Internal Representation Selection",
            "url": "https://arxiv.org/pdf/2510.02934"
          },
          {
            "title": "Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders",
            "url": "https://arxiv.org/html/2604.19974"
          },
          {
            "title": "No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes",
            "url": "https://arxiv.org/pdf/2509.10625"
          },
          {
            "title": "Use of Retrieval-Augmented Large Language Model for COVID-19 Fact-Checking: Development and Usability Study",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12079058/"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's what the research is about:\n\nThe paper investigates how large language models can detect their own errors and sometimes correct them without external feedback through the lens of second-order models of confidence from decision neuroscience.\n\n**Key Findings:**\n\nThe research shows that verbal confidence predicts error detection far beyond token log-probabilities, PANL activations predict error detection beyond verbal confidence itself, and PANL predicts which errors the model can correct—where all behavioral signals fail.\n\nCausal interventions confirm that PANL signals rescue error detection behavior when answer information is corrupted.\n\n**What is PANL:**\n\nPANL stands for post-answer newline—a token immediately following the answer that caches a confidence representation and causally drives verbal confidence while dissociating from log-probabilities.\n\n**Main Contribution:**\n\nThe results reveal that LLMs naturally implement a second-order confidence architecture whose internal evaluative signal encodes not only whether an answer is likely wrong but whether the model has the knowledge to fix it.\n\nAll findings replicate across models (Gemma 3 27B and Qwen 2.5 7B) and tasks (TriviaQA and MNLI)."
    ],
    "durationSeconds": 8.652588045999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "da4440d2-5c17-44cc-ba60-b0298a08cb38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T19:00:04.935Z_

<details><summary>↩ Tool result · `toolu_01W2z9rAT3ahS69bxAYwXxNS`</summary>

```text
Web search results for query: "CoRefine confidence-guided self-refinement arXiv 2602.08948 three-way routing"

Links: [{"title":"[2602.08948] CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute","url":"https://arxiv.org/abs/2602.08948"},{"title":"CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute","url":"https://arxiv.org/pdf/2602.08948"},{"title":"Learning to Route with Confidence Tokens","url":"https://arxiv.org/html/2410.13284v1"},{"title":"Learning to Route LLMs with Confidence Tokens","url":"https://arxiv.org/pdf/2410.13284"},{"title":"Confidence-Guided Stepwise Model Routing for Cost-Efficient Reasoning","url":"https://arxiv.org/pdf/2511.06190"}]

Based on the search results, here's what I found about CoRefine (arXiv 2602.08948):

## CoRefine Overview

CoRefine is a confidence-guided self-refinement method that achieves competitive accuracy using a fraction of the tokens via a lightweight 211k-parameter Conv1D controller atop a frozen LLM.

## Three-Way Routing

The "three-way routing" you're asking about refers to the refinement decisions the controller makes. The controller consumes full-trace confidence features of the LLM decoded reasoning chain and decides: HALT (accept current answer), RETHINK (verify reasoning), or ALTERNATIVE (explore new approach).

## Key Components

CoRefine consists of three components: (1) full-trace confidence extraction from the model's logprobs, (2) a lightweight neural controller (~211K parameters) that maps confidence features to refinement decisions, and (3) targeted synthesis prompts that compact previous reasoning into high-signal context for self-correction.

## Performance Results

The controller enables targeted self-correction with an average of 2.7 refinement steps per problem and roughly 190-fold token reduction relative to 512-sample baselines. CoRefine achieves competitive or superior accuracy to 512-sample or 20-sample majority voting with ~190× fewer tokens.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0cc0b09-dd76-41b7-8bdc-ba0339d0fc25",
  "isSidechain": false,
  "promptId": "032757f9-b233-4ec3-9ca3-db9f978295b0",
  "type": "user",
  "uuid": "f212aa5c-8aac-4929-9dc9-16434159f4bc",
  "toolUseResult": {
    "query": "CoRefine confidence-guided self-refinement arXiv 2602.08948 three-way routing",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VddeapAuBDmiZZVnAXCrUv",
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
            "title": "Learning to Route with Confidence Tokens",
            "url": "https://arxiv.org/html/2410.13284v1"
          },
          {
            "title": "Learning to Route LLMs with Confidence Tokens",
            "url": "https://arxiv.org/pdf/2410.13284"
          },
          {
            "title": "Confidence-Guided Stepwise Model Routing for Cost-Efficient Reasoning",
            "url": "https://arxiv.org/pdf/2511.06190"
          }
        ]
      },
      "Based on the search results, here's what I found about CoRefine (arXiv 2602.08948):\n\n## CoRefine Overview\n\nCoRefine is a confidence-guided self-refinement method that achieves competitive accuracy using a fraction of the tokens via a lightweight 211k-parameter Conv1D controller atop a frozen LLM.\n\n## Three-Way Routing\n\nThe \"three-way routing\" you're asking about refers to the refinement decisions the controller makes. The controller consumes full-trace confidence features of the LLM decoded reasoning chain and decides: HALT (accept current answer), RETHINK (verify reasoning), or ALTERNATIVE (explore new approach).\n\n## Key Components\n\nCoRefine consists of three components: (1) full-trace confidence extraction from the model's logprobs, (2) a lightweight neural controller (~211K parameters) that maps confidence features to refinement decisions, and (3) targeted synthesis prompts that compact previous reasoning into high-signal context for self-correction.\n\n## Performance Results\n\nThe controller enables targeted self-correction with an average of 2.7 refinement steps per problem and roughly 190-fold token reduction relative to 512-sample baselines. CoRefine achieves competitive or superior accuracy to 512-sample or 20-sample majority voting with ~190× fewer tokens."
    ],
    "durationSeconds": 7.940123274999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a0cc0b09-dd76-41b7-8bdc-ba0339d0fc25",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "f212aa5c-8aac-4929-9dc9-16434159f4bc",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Predict correctability of LLM self-corrections",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e"
}
```

---

### Tool result

_source line 24 · 2026-05-19T19:00:05.376Z_

<details><summary>↩ Tool result · `toolu_01TmCLATdpH1wZWQkRAP4Ku6`</summary>

```text
Web search results for query: "SAE sparse autoencoder uncertainty correctness dissociation LLM features arXiv 2604.19974"

Links: [{"title":"Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders","url":"https://arxiv.org/html/2604.19974"},{"title":"[2604.19974] Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders","url":"https://arxiv.org/abs/2604.19974"},{"title":"Sparse but Wrong: Incorrect L0 Leads to Incorrect Features in Sparse Autoencoders","url":"https://arxiv.org/pdf/2508.16560"},{"title":"Mechanistic Interpretability of Code Correctness in LLMs via Sparse Autoencoders","url":"https://arxiv.org/pdf/2510.02917"},{"title":"AdaptiveK Sparse Autoencoders: Dynamic Sparsity Allocation for Interpretable LLM Representations","url":"https://arxiv.org/pdf/2508.17320"}]

I found the paper! Here's what the search revealed:

Large language models can be uncertain yet correct, or confident yet wrong, raising the question of whether their output-level uncertainty and their actual correctness are driven by the same internal mechanisms or by distinct feature populations.

The researchers introduce a 2x2 framework that partitions model predictions along correctness and confidence axes, and uses sparse autoencoders to identify features associated with each dimension independently. Applying this to Llama-3.1-8B and Gemma-2-9B, they identify three feature populations that play fundamentally different functional roles.

The key findings are:
- Pure uncertainty features are functionally essential: suppressing them severely degrades accuracy.
- Pure incorrectness features are functionally inert: despite showing statistically significant activation differences between correct and incorrect predictions, the majority produce near-zero change in accuracy when suppressed.

This paper (arXiv:2604.19974) was published on April 21, 2026, by Het Patel and colleagues, and demonstrates a functional dissociation between how LLMs encode uncertainty versus actual correctness in their internal representations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a0b3938-23f6-4031-8d51-a1943cad300d",
  "isSidechain": false,
  "promptId": "032757f9-b233-4ec3-9ca3-db9f978295b0",
  "type": "user",
  "uuid": "ce4ecd79-38c6-48e5-aad5-c4dc08e0e7ae",
  "toolUseResult": {
    "query": "SAE sparse autoencoder uncertainty correctness dissociation LLM features arXiv 2604.19974",
    "results": [
      {
        "tool_use_id": "srvtoolu_014SMw88qcezc2inQ1AN4Vqx",
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
            "title": "Sparse but Wrong: Incorrect L0 Leads to Incorrect Features in Sparse Autoencoders",
            "url": "https://arxiv.org/pdf/2508.16560"
          },
          {
            "title": "Mechanistic Interpretability of Code Correctness in LLMs via Sparse Autoencoders",
            "url": "https://arxiv.org/pdf/2510.02917"
          },
          {
            "title": "AdaptiveK Sparse Autoencoders: Dynamic Sparsity Allocation for Interpretable LLM Representations",
            "url": "https://arxiv.org/pdf/2508.17320"
          }
        ]
      },
      "I found the paper! Here's what the search revealed:\n\nLarge language models can be uncertain yet correct, or confident yet wrong, raising the question of whether their output-level uncertainty and their actual correctness are driven by the same internal mechanisms or by distinct feature populations.\n\nThe researchers introduce a 2x2 framework that partitions model predictions along correctness and confidence axes, and uses sparse autoencoders to identify features associated with each dimension independently. Applying this to Llama-3.1-8B and Gemma-2-9B, they identify three feature populations that play fundamentally different functional roles.\n\nThe key findings are:\n- Pure uncertainty features are functionally essential: suppressing them severely degrades accuracy.\n- Pure incorrectness features are functionally inert: despite showing statistically significant activation differences between correct and incorrect predictions, the majority produce near-zero change in accuracy when suppressed.\n\nThis paper (arXiv:2604.19974) was published on April 21, 2026, by Het Patel and colleagues, and demonstrates a functional dissociation between how LLMs encode uncertainty versus actual correctness in their internal representations."
    ],
    "durationSeconds": 8.046685850999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7a0b3938-23f6-4031-8d51-a1943cad300d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T19:00:05.867Z_

<details><summary>↩ Tool result · `toolu_01TV3K9dXEwrX1Fz1wmc9669`</summary>

```text
Web search results for query: "multi-layer ensemble probing LLM deception detection arXiv 2604.13386 2026"

Links: [{"title":"Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling","url":"https://arxiv.org/html/2604.13386v1"},{"title":"[2604.13386] Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling","url":"https://arxiv.org/abs/2604.13386"},{"title":"Caught in the Act: a mechanistic approach to detecting deception","url":"https://arxiv.org/pdf/2508.19505"},{"title":"Caught in the Act: a mechanistic approach to detecting deception","url":"https://arxiv.org/html/2508.19505v2"},{"title":"DeceptGuard :A Constitutional Oversight Framework For Detecting Deception in LLM Agents","url":"https://arxiv.org/pdf/2603.13791"},{"title":"Detecting Multi-Agent Collusion Through Multi-Agent Interpretability","url":"https://arxiv.org/pdf/2604.01151"}]

I found the paper you're looking for! Here are the key details:

**Title:** Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling

**arXiv ID:** 2604.13386 (Version 1, April 15, 2026)

**Authors:** Erik Nordby, Tasha Pais, and Aviel Parrack

**Main Findings:**

Linear probes can detect when language models produce outputs they "know" are wrong, a capability relevant to both deception and reward hacking. However, single-layer probes are fragile: the best layer varies across models and tasks, and probes fail entirely on some deception types.

The paper's key contribution is that combining probes from multiple layers into an ensemble recovers strong performance even where single-layer probes fail, improving AUROC by +29% on Insider Trading and +78% on Harm-Pressure Knowledge.

**Technical Insights:**

Across 12 models (0.5B–176B parameters), probe accuracy improves with scale: ~5% AUROC per 10x parameters (R=0.81). Geometrically, deception directions rotate gradually across layers rather than appearing at one location, explaining both why single-layer probes are brittle and why multi-layer ensembles succeed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a3eff72-c9ba-45cc-9e18-79ec4dc358bc",
  "isSidechain": false,
  "promptId": "032757f9-b233-4ec3-9ca3-db9f978295b0",
  "type": "user",
  "uuid": "28c7ecc9-2f5e-4d39-9513-a0726fad794d",
  "toolUseResult": {
    "query": "multi-layer ensemble probing LLM deception detection arXiv 2604.13386 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QjrLpoU2gksPLaGYYgqza6",
        "content": [
          {
            "title": "Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling",
            "url": "https://arxiv.org/html/2604.13386v1"
          },
          {
            "title": "[2604.13386] Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling",
            "url": "https://arxiv.org/abs/2604.13386"
          },
          {
            "title": "Caught in the Act: a mechanistic approach to detecting deception",
            "url": "https://arxiv.org/pdf/2508.19505"
          },
          {
            "title": "Caught in the Act: a mechanistic approach to detecting deception",
            "url": "https://arxiv.org/html/2508.19505v2"
          },
          {
            "title": "DeceptGuard :A Constitutional Oversight Framework For Detecting Deception in LLM Agents",
            "url": "https://arxiv.org/pdf/2603.13791"
          },
          {
            "title": "Detecting Multi-Agent Collusion Through Multi-Agent Interpretability",
            "url": "https://arxiv.org/pdf/2604.01151"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details:\n\n**Title:** Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling\n\n**arXiv ID:** 2604.13386 (Version 1, April 15, 2026)\n\n**Authors:** Erik Nordby, Tasha Pais, and Aviel Parrack\n\n**Main Findings:**\n\nLinear probes can detect when language models produce outputs they \"know\" are wrong, a capability relevant to both deception and reward hacking. However, single-layer probes are fragile: the best layer varies across models and tasks, and probes fail entirely on some deception types.\n\nThe paper's key contribution is that combining probes from multiple layers into an ensemble recovers strong performance even where single-layer probes fail, improving AUROC by +29% on Insider Trading and +78% on Harm-Pressure Knowledge.\n\n**Technical Insights:**\n\nAcross 12 models (0.5B–176B parameters), probe accuracy improves with scale: ~5% AUROC per 10x parameters (R=0.81). Geometrically, deception directions rotate gradually across layers rather than appearing at one location, explaining both why single-layer probes are brittle and why multi-layer ensembles succeed."
    ],
    "durationSeconds": 9.409907277000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9a3eff72-c9ba-45cc-9e18-79ec4dc358bc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-19T19:00:08.566Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've gathered substantial information. Let me do a couple more targeted searches to understand the competitive landscape better.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28c7ecc9-2f5e-4d39-9513-a0726fad794d",
  "isSidechain": false,
  "requestId": "req_011CbCSd1UDsQurtXW9ZeomT",
  "type": "assistant",
  "uuid": "9f4d338b-61a0-4f6a-970a-ce0012f0b0bd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UpPhJebYQWW8K1XBS34YC8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1162,
      "cache_creation_input_tokens": 2349,
      "cache_read_input_tokens": 25851,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2349,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1162,
          "output_tokens": 261,
          "cache_read_input_tokens": 25851,
          "cache_creation_input_tokens": 2349,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2349
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

_source line 27 · 2026-05-19T19:00:09.513Z_

让我继续搜索更多相关工作，特别是关于 probe-gated self-correction 和 representational geometry 方面的最新进展。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f4d338b-61a0-4f6a-970a-ce0012f0b0bd",
  "isSidechain": false,
  "requestId": "req_011CbCSd1UDsQurtXW9ZeomT",
  "type": "assistant",
  "uuid": "4ee44cc7-d31c-419d-87cf-6c1129d9a216",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UpPhJebYQWW8K1XBS34YC8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1162,
      "cache_creation_input_tokens": 2349,
      "cache_read_input_tokens": 25851,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2349,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1162,
          "output_tokens": 261,
          "cache_read_input_tokens": 25851,
          "cache_creation_input_tokens": 2349,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2349
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

_source line 28 · 2026-05-19T19:00:09.997Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CUZTH6RF5nGLvEDufsgdsA`</summary>

```json
{
  "query": "probe-gated LLM self-correction abstention hidden state 2025 2026 selective correction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ee44cc7-d31c-419d-87cf-6c1129d9a216",
  "isSidechain": false,
  "requestId": "req_011CbCSd1UDsQurtXW9ZeomT",
  "type": "assistant",
  "uuid": "837ede06-8fea-4c43-8c55-a10f8463ba64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UpPhJebYQWW8K1XBS34YC8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1162,
      "cache_creation_input_tokens": 2349,
      "cache_read_input_tokens": 25851,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2349,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1162,
          "output_tokens": 261,
          "cache_read_input_tokens": 25851,
          "cache_creation_input_tokens": 2349,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2349
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

_source line 29 · 2026-05-19T19:00:10.995Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WKfuCMouDuMi9dtDWehhrR`</summary>

```json
{
  "query": "Confidence Manifold LLM correctness low-dimensional linear separability arXiv 2602.08159"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "837ede06-8fea-4c43-8c55-a10f8463ba64",
  "isSidechain": false,
  "requestId": "req_011CbCSd1UDsQurtXW9ZeomT",
  "type": "assistant",
  "uuid": "fdc16ba2-456c-4dd2-aca2-17097d722d9a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UpPhJebYQWW8K1XBS34YC8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1162,
      "cache_creation_input_tokens": 2349,
      "cache_read_input_tokens": 25851,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2349,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1162,
          "output_tokens": 261,
          "cache_read_input_tokens": 25851,
          "cache_creation_input_tokens": 2349,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2349
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

_source line 30 · 2026-05-19T19:00:11.676Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NzcJkH8NPXxZmizntWm4MD`</summary>

```json
{
  "query": "CoRL 2026 conference on robot learning submission topics scope"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdc16ba2-456c-4dd2-aca2-17097d722d9a",
  "isSidechain": false,
  "requestId": "req_011CbCSd1UDsQurtXW9ZeomT",
  "type": "assistant",
  "uuid": "4010492a-5577-4594-a202-a31ac7a7e0f6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UpPhJebYQWW8K1XBS34YC8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1162,
      "cache_creation_input_tokens": 2349,
      "cache_read_input_tokens": 25851,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2349,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1162,
          "output_tokens": 261,
          "cache_read_input_tokens": 25851,
          "cache_creation_input_tokens": 2349,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2349
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

_source line 31 · 2026-05-19T19:00:17.276Z_

<details><summary>↩ Tool result · `toolu_01CUZTH6RF5nGLvEDufsgdsA`</summary>

```text
Web search results for query: "probe-gated LLM self-correction abstention hidden state 2025 2026 selective correction"

Links: [{"title":"Uncertainty-Based Abstention in LLMs Improves Safety and Reduces   Hallucinations","url":"https://arxiv.org/pdf/2404.10960"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"},{"title":"No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes","url":"https://arxiv.org/pdf/2509.10625"},{"title":"Probing LLM Hidden States","url":"https://apxml.com/courses/how-to-build-a-large-language-model/chapter-23-analyzing-model-behavior/probing-internal-representations"},{"title":"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/pdf/2512.20578"},{"title":"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/html/2512.20578"},{"title":"Temporal Predictors of Outcome in Reasoning Language Models","url":"https://arxiv.org/pdf/2511.14773"},{"title":"Self-correction is Not An Innate Capability in Language Models","url":"https://arxiv.org/pdf/2410.20513"}]

Here are the search results for your query about probe-gated LLM self-correction abstention hidden state:

## Key Findings:

**Hidden State Probing for Self-Assessment:**

Large language models internally encode information beyond what is immediately observable in their output, with studies showing that hidden activations can reveal concepts related to statement truthfulness, deception, and hallucination.

Research investigates the structure of self-correctness representations in LLMs, testing whether the residual stream activation contains a direction that linearly separates questions the model will answer correctly from those it will not.

**Abstention and Confidence:**

For models that answer "I don't know," doing so correlates with the question's position along the in-advance correctness direction, suggesting this vector captures an implicit confidence axis.

**Recent Methods (2025-2026):**

A mechanism called Gnosis enables frozen LLMs to predict the correctness of their own generations by decoding signals intrinsic to the inference process, leveraging hidden states and attention maps with only ~5 million extra parameters.

Recent work includes probing during chain-of-thought generation to predict answer correctness directly from hidden states while the chain-of-thought is being generated, not only after the initial question or final answer.

**Self-Correction in Hidden States:**

Studies have trained probing vectors to measure toxicity and bias levels through the self-correction trajectory, with recent work proving the interaction of uncertainty and latent concepts during self-correction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "837ede06-8fea-4c43-8c55-a10f8463ba64",
  "isSidechain": false,
  "promptId": "032757f9-b233-4ec3-9ca3-db9f978295b0",
  "type": "user",
  "uuid": "a5a0c1d5-a7ea-4055-9460-541ee88984ed",
  "toolUseResult": {
    "query": "probe-gated LLM self-correction abstention hidden state 2025 2026 selective correction",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FVzKfbskBhXVgGEk4T5vej",
        "content": [
          {
            "title": "Uncertainty-Based Abstention in LLMs Improves Safety and Reduces   Hallucinations",
            "url": "https://arxiv.org/pdf/2404.10960"
          },
          {
            "title": "Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs",
            "url": "https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"
          },
          {
            "title": "No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes",
            "url": "https://arxiv.org/pdf/2509.10625"
          },
          {
            "title": "Probing LLM Hidden States",
            "url": "https://apxml.com/courses/how-to-build-a-large-language-model/chapter-23-analyzing-model-behavior/probing-internal-representations"
          },
          {
            "title": "Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/pdf/2512.20578"
          },
          {
            "title": "Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/html/2512.20578"
          },
          {
            "title": "Temporal Predictors of Outcome in Reasoning Language Models",
            "url": "https://arxiv.org/pdf/2511.14773"
          },
          {
            "title": "Self-correction is Not An Innate Capability in Language Models",
            "url": "https://arxiv.org/pdf/2410.20513"
          }
        ]
      },
      "Here are the search results for your query about probe-gated LLM self-correction abstention hidden state:\n\n## Key Findings:\n\n**Hidden State Probing for Self-Assessment:**\n\nLarge language models internally encode information beyond what is immediately observable in their output, with studies showing that hidden activations can reveal concepts related to statement truthfulness, deception, and hallucination.\n\nResearch investigates the structure of self-correctness representations in LLMs, testing whether the residual stream activation contains a direction that linearly separates questions the model will answer correctly from those it will not.\n\n**Abstention and Confidence:**\n\nFor models that answer \"I don't know,\" doing so correlates with the question's position along the in-advance correctness direction, suggesting this vector captures an implicit confidence axis.\n\n**Recent Methods (2025-2026):**\n\nA mechanism called Gnosis enables frozen LLMs to predict the correctness of their own generations by decoding signals intrinsic to the inference process, leveraging hidden states and attention maps with only ~5 million extra parameters.\n\nRecent work includes probing during chain-of-thought generation to predict answer correctness directly from hidden states while the chain-of-thought is being generated, not only after the initial question or final answer.\n\n**Self-Correction in Hidden States:**\n\nStudies have trained probing vectors to measure toxicity and bias levels through the self-correction trajectory, with recent work proving the interaction of uncertainty and latent concepts during self-correction."
    ],
    "durationSeconds": 7.27525215,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "837ede06-8fea-4c43-8c55-a10f8463ba64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T19:00:19.357Z_

<details><summary>↩ Tool result · `toolu_01NzcJkH8NPXxZmizntWm4MD`</summary>

```text
Web search results for query: "CoRL 2026 conference on robot learning submission topics scope"

Links: [{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI","url":"https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"2025 Conference on Robot Learning - CoRL","url":"https://www.corl.org/home"},{"title":"CoRL 2026 - About CoRL","url":"https://www.corl.org/about-corl"},{"title":"System and method for robot learning from human demonstrations with formal logic","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12208521"}]

Based on the search results, here's what CoRL 2026 is looking for in submissions:

## Conference Overview

The Conference on Robot Learning (CoRL) is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics and its interaction with other areas of robotics.

## Submission Topics and Scope

The aim of CoRL 2026 is to publish significant original research at the intersection of robotics and machine learning. CoRL welcomes papers in areas such as learning representations for robotic perception and control, learning robot foundation models or general-purpose knowledge systems for robotics, imitation learning for robotics, reinforcement learning for control of physical robots, and video models and latent world models for robot learning.

CoRL covers topics including imitation learning, reinforcement learning for robots, sim-to-real transfer, robot perception through learning, learned manipulation and locomotion, and learning-based planning.

## Key Requirements for Submissions

- Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics.
- Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.
- Submissions without a robotics focus will be returned without review.
- All submissions should include a Limitations section, explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments.

The paper submission deadline is May 29, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4010492a-5577-4594-a202-a31ac7a7e0f6",
  "isSidechain": false,
  "promptId": "032757f9-b233-4ec3-9ca3-db9f978295b0",
  "type": "user",
  "uuid": "c3083b71-3261-4f1a-9255-5a5374f909b4",
  "toolUseResult": {
    "query": "CoRL 2026 conference on robot learning submission topics scope",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PFwqWemmAbCCcmdSaha4K8",
        "content": [
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "CoRL LaTeX Template | Robot Learning Conference Format | Underleaf",
            "url": "https://www.underleaf.ai/templates/corl"
          },
          {
            "title": "Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI",
            "url": "https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"
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
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "2025 Conference on Robot Learning - CoRL",
            "url": "https://www.corl.org/home"
          },
          {
            "title": "CoRL 2026 - About CoRL",
            "url": "https://www.corl.org/about-corl"
          },
          {
            "title": "System and method for robot learning from human demonstrations with formal logic",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12208521"
          }
        ]
      },
      "Based on the search results, here's what CoRL 2026 is looking for in submissions:\n\n## Conference Overview\n\nThe Conference on Robot Learning (CoRL) is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics and its interaction with other areas of robotics.\n\n## Submission Topics and Scope\n\nThe aim of CoRL 2026 is to publish significant original research at the intersection of robotics and machine learning. CoRL welcomes papers in areas such as learning representations for robotic perception and control, learning robot foundation models or general-purpose knowledge systems for robotics, imitation learning for robotics, reinforcement learning for control of physical robots, and video models and latent world models for robot learning.\n\nCoRL covers topics including imitation learning, reinforcement learning for robots, sim-to-real transfer, robot perception through learning, learned manipulation and locomotion, and learning-based planning.\n\n## Key Requirements for Submissions\n\n- Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics.\n- Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.\n- Submissions without a robotics focus will be returned without review.\n- All submissions should include a Limitations section, explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments.\n\nThe paper submission deadline is May 29, 2026."
    ],
    "durationSeconds": 7.678350265000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4010492a-5577-4594-a202-a31ac7a7e0f6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T19:00:22.291Z_

<details><summary>↩ Tool result · `toolu_01WKfuCMouDuMi9dtDWehhrR`</summary>

```text
Web search results for query: "Confidence Manifold LLM correctness low-dimensional linear separability arXiv 2602.08159"

Links: [{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/pdf/2602.08159"},{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/html/2602.08159v1"},{"title":"The Confidence Manifold:","url":"https://www.arxiv.org/pdf/2602.08159"},{"title":"Predicting LLM Answer Accuracy from Question-Only ...","url":"https://arxiv.org/pdf/2509.10625"},{"title":"The Confidence Manifold - Seongland","url":"https://seongland.com/article/confidence-manifold/"},{"title":"REMA: A Unified Reasoning Manifold Framework for Interpreting Large Language Model","url":"https://arxiv.org/html/2509.22518v1"}]

Based on the search results, here's information about the paper "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models" (arXiv 2602.08159):

## Overview

The paper characterizes the geometry of correctness representations across 9 models from 5 architecture families.

## Key Findings

The discriminative signal occupies 3–8 dimensions, performance degrades with additional dimensions, and no nonlinear classifier improves over linear separation. This demonstrates the low-dimensional linear separability of the correctness signal.

Centroid distance in the low-dimensional subspace matches trained probe performance (0.90 AUC), enabling few-shot detection: on GPT-2, 25 labeled examples achieve 89% of full-data accuracy.

## Internal vs. Output-Based Detection

Internal probes achieve 0.80-0.97 AUC; output-based methods (P(True), semantic entropy) achieve only 0.44–0.64 AUC. The correctness signal exists internally but is not expressed in outputs.

## Causal Validation

The learned direction produces 10.9 percentage point changes in error rates while random directions show no effect when validated through activation steering.

## Geometric Structure

Centroid distance matches probe performance indicates class separation is a mean shift, making detection geometric rather than learned.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdc16ba2-456c-4dd2-aca2-17097d722d9a",
  "isSidechain": false,
  "promptId": "032757f9-b233-4ec3-9ca3-db9f978295b0",
  "type": "user",
  "uuid": "e43d78bd-f5ac-405e-9bc3-5e0ebdf87daf",
  "toolUseResult": {
    "query": "Confidence Manifold LLM correctness low-dimensional linear separability arXiv 2602.08159",
    "results": [
      {
        "tool_use_id": "srvtoolu_015S631Kupjda9RAKZt5UHTp",
        "content": [
          {
            "title": "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models",
            "url": "https://arxiv.org/pdf/2602.08159"
          },
          {
            "title": "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models",
            "url": "https://arxiv.org/html/2602.08159v1"
          },
          {
            "title": "The Confidence Manifold:",
            "url": "https://www.arxiv.org/pdf/2602.08159"
          },
          {
            "title": "Predicting LLM Answer Accuracy from Question-Only ...",
            "url": "https://arxiv.org/pdf/2509.10625"
          },
          {
            "title": "The Confidence Manifold - Seongland",
            "url": "https://seongland.com/article/confidence-manifold/"
          },
          {
            "title": "REMA: A Unified Reasoning Manifold Framework for Interpreting Large Language Model",
            "url": "https://arxiv.org/html/2509.22518v1"
          }
        ]
      },
      "Based on the search results, here's information about the paper \"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models\" (arXiv 2602.08159):\n\n## Overview\n\nThe paper characterizes the geometry of correctness representations across 9 models from 5 architecture families.\n\n## Key Findings\n\nThe discriminative signal occupies 3–8 dimensions, performance degrades with additional dimensions, and no nonlinear classifier improves over linear separation. This demonstrates the low-dimensional linear separability of the correctness signal.\n\nCentroid distance in the low-dimensional subspace matches trained probe performance (0.90 AUC), enabling few-shot detection: on GPT-2, 25 labeled examples achieve 89% of full-data accuracy.\n\n## Internal vs. Output-Based Detection\n\nInternal probes achieve 0.80-0.97 AUC; output-based methods (P(True), semantic entropy) achieve only 0.44–0.64 AUC. The correctness signal exists internally but is not expressed in outputs.\n\n## Causal Validation\n\nThe learned direction produces 10.9 percentage point changes in error rates while random directions show no effect when validated through activation steering.\n\n## Geometric Structure\n\nCentroid distance matches probe performance indicates class separation is a mean shift, making detection geometric rather than learned."
    ],
    "durationSeconds": 11.292051564000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fdc16ba2-456c-4dd2-aca2-17097d722d9a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34 · 2026-05-19T19:00:22.297Z_

```json
{
  "parentUuid": "e43d78bd-f5ac-405e-9bc3-5e0ebdf87daf",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1f734148-b391-4e08-a78d-aa510fd94c57",
  "timestamp": "2026-05-19T19:00:22.297Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "1f734148-b391-4e08-a78d-aa510fd94c57",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Predict correctability of LLM self-corrections",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e"
}
```

---

### Assistant

_source line 37 · 2026-05-19T19:00:27.745Z_

<details><summary>Logged reasoning block</summary>

```text
This is very important. CoRL 2026 explicitly states: "Submissions without a robotics focus will be returned without review." This proposal is about LLM self-correction probing, which has absolutely nothing to do with robotics. This is a **fatal venue mismatch**.

The proposal would be desk-rejected at CoRL. It's an NLP/mechanistic interpretability paper that should be submitted to venues like ACL, EMNLP, NeurIPS, ICML, or ICLR.

Let me now do my final search to check if there's any concurrent work that directly competes with this proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f734148-b391-4e08-a78d-aa510fd94c57",
  "isSidechain": false,
  "requestId": "req_011CbCSeDejFHxtwetVSVtaR",
  "type": "assistant",
  "uuid": "28ada562-765f-404d-86ff-18c687578b47",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FQGoNkQJ19zmWr2Ro4KK7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 733,
      "cache_creation_input_tokens": 2899,
      "cache_read_input_tokens": 28200,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2899,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 733,
          "output_tokens": 315,
          "cache_read_input_tokens": 28200,
          "cache_creation_input_tokens": 2899,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2899
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

_source line 38 · 2026-05-19T19:00:28.219Z_

这是一个关键发现。让我再搜索一下是否有直接竞争的 concurrent work。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28ada562-765f-404d-86ff-18c687578b47",
  "isSidechain": false,
  "requestId": "req_011CbCSeDejFHxtwetVSVtaR",
  "type": "assistant",
  "uuid": "b3958873-4bb8-417a-a1a1-a45cf12d889a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FQGoNkQJ19zmWr2Ro4KK7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 733,
      "cache_creation_input_tokens": 2899,
      "cache_read_input_tokens": 28200,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2899,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 733,
          "output_tokens": 315,
          "cache_read_input_tokens": 28200,
          "cache_creation_input_tokens": 2899,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2899
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

_source line 39 · 2026-05-19T19:00:29.287Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TbdMKSBStCEe2j3eWtkEpm`</summary>

```json
{
  "query": "\"correctability prediction\" \"self-correction\" probe gating LLM 2026 selective"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3958873-4bb8-417a-a1a1-a45cf12d889a",
  "isSidechain": false,
  "requestId": "req_011CbCSeDejFHxtwetVSVtaR",
  "type": "assistant",
  "uuid": "97e99c4a-1310-4655-be3b-767af2a17032",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FQGoNkQJ19zmWr2Ro4KK7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 733,
      "cache_creation_input_tokens": 2899,
      "cache_read_input_tokens": 28200,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2899,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 733,
          "output_tokens": 315,
          "cache_read_input_tokens": 28200,
          "cache_creation_input_tokens": 2899,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2899
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

_source line 40 · 2026-05-19T19:00:30.171Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018p9u6V4Z2DqrFoGhf2D4Vf`</summary>

```json
{
  "query": "Reflective Confidence arXiv 2512.18605 self-correction output confidence trigger 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97e99c4a-1310-4655-be3b-767af2a17032",
  "isSidechain": false,
  "requestId": "req_011CbCSeDejFHxtwetVSVtaR",
  "type": "assistant",
  "uuid": "ef6d9195-4940-48da-99f0-967f9e7d678f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FQGoNkQJ19zmWr2Ro4KK7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 733,
      "cache_creation_input_tokens": 2899,
      "cache_read_input_tokens": 28200,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2899,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 733,
          "output_tokens": 315,
          "cache_read_input_tokens": 28200,
          "cache_creation_input_tokens": 2899,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2899
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

_source line 41 · 2026-05-19T19:00:37.172Z_

<details><summary>↩ Tool result · `toolu_01TbdMKSBStCEe2j3eWtkEpm`</summary>

```text
Web search results for query: ""correctability prediction" "self-correction" probe gating LLM 2026 selective"

Links: [{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"},{"title":"Concurrent Criterion Validation of a Validity Screen for LLM Confidence Signals via Selective Prediction","url":"https://arxiv.org/html/2604.17716"},{"title":"Towards Reliable LLM Grading Through Self-Consistency and Selective Human Review: Higher Accuracy, Less Work","url":"https://www.mdpi.com/2504-4990/8/3/74"},{"title":"Learning self-evaluation to improve selective prediction in LLMs","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12536388"},{"title":"Adaptation with Self-Evaluation to Improve Selective Prediction in LLMs","url":"https://arxiv.org/pdf/2310.11689"},{"title":"No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes","url":"https://arxiv.org/pdf/2509.10625"},{"title":"Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis","url":"https://arxiv.org/pdf/2601.00828"}]

I found several relevant research papers and articles related to your search query about correctability prediction, self-correction, and selective prediction in Large Language Models from 2026. Here are the key findings:

## Recent Research on LLM Correctability and Self-Correction

Research in 2026 showed that LLMs cache a confidence representation at a token immediately following the answer (post-answer newline: PANL) that causally drives verbal confidence and dissociates from log-probabilities.

Recent work on selective prediction examines whether confidence discriminates correctness, with validation screenings being used as interpretable checks for systems using LLM confidence for abstention.

Research investigates the structure of self-correctness representations in LLMs by testing whether the residual stream activation captured immediately after processing a query contains a direction that linearly separates questions the model will answer correctly from those it will not.

Studies systematically decompose self-correction into error detection, error localization, and error correction, uncovering an "Accuracy-Correction Paradox" where weaker models achieve higher intrinsic correction rates than stronger models.

The research also addresses practical applications like selective uncertainty-based re-evaluation pipelines that combine repeated LLM prompting, uncertainty-based flagging, and selective human regrading to improve reliability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97e99c4a-1310-4655-be3b-767af2a17032",
  "isSidechain": false,
  "promptId": "032757f9-b233-4ec3-9ca3-db9f978295b0",
  "type": "user",
  "uuid": "b4238dde-de4e-48db-b5c8-5021a15827ab",
  "toolUseResult": {
    "query": "\"correctability prediction\" \"self-correction\" probe gating LLM 2026 selective",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GXmwbmmucMzFvXDaLUr5cQ",
        "content": [
          {
            "title": "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs",
            "url": "https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"
          },
          {
            "title": "Concurrent Criterion Validation of a Validity Screen for LLM Confidence Signals via Selective Prediction",
            "url": "https://arxiv.org/html/2604.17716"
          },
          {
            "title": "Towards Reliable LLM Grading Through Self-Consistency and Selective Human Review: Higher Accuracy, Less Work",
            "url": "https://www.mdpi.com/2504-4990/8/3/74"
          },
          {
            "title": "Learning self-evaluation to improve selective prediction in LLMs",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12536388"
          },
          {
            "title": "Adaptation with Self-Evaluation to Improve Selective Prediction in LLMs",
            "url": "https://arxiv.org/pdf/2310.11689"
          },
          {
            "title": "No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes",
            "url": "https://arxiv.org/pdf/2509.10625"
          },
          {
            "title": "Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis",
            "url": "https://arxiv.org/pdf/2601.00828"
          }
        ]
      },
      "I found several relevant research papers and articles related to your search query about correctability prediction, self-correction, and selective prediction in Large Language Models from 2026. Here are the key findings:\n\n## Recent Research on LLM Correctability and Self-Correction\n\nResearch in 2026 showed that LLMs cache a confidence representation at a token immediately following the answer (post-answer newline: PANL) that causally drives verbal confidence and dissociates from log-probabilities.\n\nRecent work on selective prediction examines whether confidence discriminates correctness, with validation screenings being used as interpretable checks for systems using LLM confidence for abstention.\n\nResearch investigates the structure of self-correctness representations in LLMs by testing whether the residual stream activation captured immediately after processing a query contains a direction that linearly separates questions the model will answer correctly from those it will not.\n\nStudies systematically decompose self-correction into error detection, error localization, and error correction, uncovering an \"Accuracy-Correction Paradox\" where weaker models achieve higher intrinsic correction rates than stronger models.\n\nThe research also addresses practical applications like selective uncertainty-based re-evaluation pipelines that combine repeated LLM prompting, uncertainty-based flagging, and selective human regrading to improve reliability."
    ],
    "durationSeconds": 7.880758341999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "97e99c4a-1310-4655-be3b-767af2a17032",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T19:00:49.177Z_

<details><summary>↩ Tool result · `toolu_018p9u6V4Z2DqrFoGhf2D4Vf`</summary>

```text
Web search results for query: "Reflective Confidence arXiv 2512.18605 self-correction output confidence trigger 2025"

Links: [{"title":"[2512.18605] Reflective Confidence: Correcting Reasoning Flaws via Online Self-Correction","url":"https://arxiv.org/abs/2512.18605"},{"title":"Reflective Confidence: Correcting Reasoning Flaws via Online Self-Correction","url":"https://arxiv.org/html/2512.18605v1"},{"title":"Reflective Confidence: Correcting Reasoning Flaws via Online Self-Correction","url":"https://arxiv.org/pdf/2512.18605"},{"title":"Artificial Intelligence Dec 2025","url":"https://arxiv.org/list/cs.AI/2025-12?skip=550&show=500"},{"title":"Confidence v.s. Critique: A Decomposition of Self-Correction Capability   for LLMs","url":"https://arxiv.org/pdf/2412.19513"}]

Based on the search results, here's what I found about the paper:

## Reflective Confidence (arXiv 2512.18605)

Reflective Confidence is a novel reasoning framework that transforms low-confidence signals from termination indicators into reflection triggers.

**Key Concept:**
When confidence falls below a threshold, instead of stopping generation, the model produces a reflection prompt to analyze the current reasoning state, identify potential errors, and continue generation along a corrected trajectory.

**Problem Addressed:**
The paper addresses inefficiencies in ensemble-based reasoning approaches. Early stopping strategies such as DeepConf save resources by terminating low-confidence paths, yet this discards incomplete paths and wastes computation.

**Method:**
The proposed method, ReflectiveConf, triggers a reflect-and-correct procedure upon detecting a low-confidence signal.

**Results:**
Experiments on mathematical reasoning benchmarks, including AIME 2025, show significant accuracy gains over advanced early stopping strategies at comparable cost, validating the efficiency of proactive correction over passive discarding.

The paper was submitted to arXiv on December 21, 2025, by researchers from Sun Yat-sen University: Qinglin Zeng, Jing Yang, and Keze Wang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef6d9195-4940-48da-99f0-967f9e7d678f",
  "isSidechain": false,
  "promptId": "032757f9-b233-4ec3-9ca3-db9f978295b0",
  "type": "user",
  "uuid": "8e0318dc-9694-4a59-93de-800dcf121937",
  "toolUseResult": {
    "query": "Reflective Confidence arXiv 2512.18605 self-correction output confidence trigger 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DGZVCyU5Ce6SWZZFTX1p3A",
        "content": [
          {
            "title": "[2512.18605] Reflective Confidence: Correcting Reasoning Flaws via Online Self-Correction",
            "url": "https://arxiv.org/abs/2512.18605"
          },
          {
            "title": "Reflective Confidence: Correcting Reasoning Flaws via Online Self-Correction",
            "url": "https://arxiv.org/html/2512.18605v1"
          },
          {
            "title": "Reflective Confidence: Correcting Reasoning Flaws via Online Self-Correction",
            "url": "https://arxiv.org/pdf/2512.18605"
          },
          {
            "title": "Artificial Intelligence Dec 2025",
            "url": "https://arxiv.org/list/cs.AI/2025-12?skip=550&show=500"
          },
          {
            "title": "Confidence v.s. Critique: A Decomposition of Self-Correction Capability   for LLMs",
            "url": "https://arxiv.org/pdf/2412.19513"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper:\n\n## Reflective Confidence (arXiv 2512.18605)\n\nReflective Confidence is a novel reasoning framework that transforms low-confidence signals from termination indicators into reflection triggers.\n\n**Key Concept:**\nWhen confidence falls below a threshold, instead of stopping generation, the model produces a reflection prompt to analyze the current reasoning state, identify potential errors, and continue generation along a corrected trajectory.\n\n**Problem Addressed:**\nThe paper addresses inefficiencies in ensemble-based reasoning approaches. Early stopping strategies such as DeepConf save resources by terminating low-confidence paths, yet this discards incomplete paths and wastes computation.\n\n**Method:**\nThe proposed method, ReflectiveConf, triggers a reflect-and-correct procedure upon detecting a low-confidence signal.\n\n**Results:**\nExperiments on mathematical reasoning benchmarks, including AIME 2025, show significant accuracy gains over advanced early stopping strategies at comparable cost, validating the efficiency of proactive correction over passive discarding.\n\nThe paper was submitted to arXiv on December 21, 2025, by researchers from Sun Yat-sen University: Qinglin Zeng, Jing Yang, and Keze Wang."
    ],
    "durationSeconds": 19.002153015999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ef6d9195-4940-48da-99f0-967f9e7d678f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-19T19:01:40.724Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to make my assessment. Let me synthesize everything.

## Critical Issue: Venue Mismatch

The most important finding is that **CoRL 2026 explicitly states "Submissions without a robotics focus will be returned without review."** This proposal is about LLM self-correction and internal representation probing — it has absolutely nothing to do with robotics. It would be desk-rejected.

This is a **fatal** issue at the venue level, independent of idea quality.

## Now let me assess the idea quality itself (venue-agnostic):

### Trivial Alternative Check


The core concern is whether simpler baselines already solve this problem. Output-level confidence routing methods like CoRefine achieve 92.6% halt precision using just logprobs, so the proposal needs to demonstrate that hidden-state probes provide meaningful gains over these lightweight approaches. Similarly, averaging predictions from probes across multiple layers is a straightforward extension of existing work rather than a novel contribution. The "Wait" baseline overcorrection measurement is also fairly straightforward to implement.

Beyond that, there are some fundamental assumptions worth questioning. The PANL paper only achieved 0.614 AUROC for correctability detection, suggesting the signal might not be strongly encoded in the model's representations at all. The proposal also assumes that multi-layer ensembling techniques from deception detection will transfer to correctability, but these are quite different problems — deception involves the model knowing the truth, while correctability is about whether a correction mechanism can find the right answer. Finally, using SAE-guided feature selection assumes that features relevant to correctness will also be relevant to correctability, but the dissociation work was specifically on correctness, not correctability, so this transfer is uncertain.

Looking at the novelty claims, the core contributions feel incremental. Operationalizing correctability as a prediction target is already established by PANL. Multi-layer ensembling for correctability is essentially applying an existing technique to a new domain. The probe-based gating with abstention combines existing ideas in a new way, but there are already several papers on probe-gating approaches, so the conceptual advance is limited.

The representational geometry analysis is probably the strongest contribution—extending existing methodology to analyze correctability as a second-order property. SAE feature decomposition is another methodological transfer, applying an established framework to correctability. Overall, this feels like a solid engineering effort that combines multiple existing techniques around a new target, but the individual pieces aren't conceptually novel.

The practical significance hinges on whether the approach actually improves selective self-correction in real scenarios. the probes can substantially improve over 0.614 AUROC. If they can't, the practical contribution is limited.
- The representational analysis is more of a scientific contribution, but its significance depends on whether it reveals something surprising about how LLMs encode second-order properties.
- For a top venue, the "would a reviewer say 'surprising'?" test: if the multi-layer ensemble improves AUROC from 0.614 to 0.70+, would that be surprising? Not really — we'd expect combining more information to help. If it doesn't improve, is the negative result surprising? Also not really — correctability might simply not be well-encoded.

### Related Work Assessment
The proposal has exceptionally thorough related work coverage. It cites ~25+ relevant papers and articulates clear distinctions from each. This is a strength, but as I noted in the rubric, form ≠ quality.

### Overall Assessment
This is a well-crafted proposal that combines existing probing techniques and applies them to correctability, but the core contribution is fundamentally engineering-focused rather than conceptually novel. The dual-outcome structure suggests the authors anticipate the positive result may not materialize, and realistically the work will likely yield modest probe improvements in the 0.65-0.72 AUROC range alongside a representational analysis — a solid but unremarkable contribution. The real problem is that neither outcome would surprise a reviewer; they'd expect combining more information to help, and if it doesn't, that's unsurprising too.

### Venue Issue
CoRL 2026 is completely wrong for this work — it would face immediate desk rejection since it's not a robotics paper at all.

For appropriate NLP venues like ACL, EMNLP, or NeurIPS, I'd estimate 20-30% acceptance probability with solid execution, but the idea itself remains incremental.

I need to be direct about the venue mismatch since the user specified CoRL 2026, though I should still evaluate the idea quality as requested while flagging this as a pre-filtering issue that makes everything else secondary.

Looking at the assessment now: novelty is weak to medium since correctability as a prediction target was already established, multi-layer ensembling borrows from deception detection work, and SAE-guided feature selection comes from uncertainty-correctness research—the combination is novel but each component is borrowed, with the most original aspect being the representational geometry comparison of first-order versus second-order properties. Significance lands at medium because while selective self-correction is genuinely important, the approach is unlikely to shift how the field thinks about the problem, and practical impact depends entirely on whether probes can meaningfully improve results. The related work coverage is exceptionally thorough.

Given the venue mismatch, I'm looking at essentially 0-5% probability for CoRL 2026 due to desk rejection, but 20-30% for appropriate venues like ACL, EMNLP, or NeurIPS. I should flag the venue issue prominently while still providing the full quality assessment the user requested.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e0318dc-9694-4a59-93de-800dcf121937",
  "isSidechain": false,
  "requestId": "req_011CbCSgCfWJbibe7CfYTu9m",
  "type": "assistant",
  "uuid": "d791f984-73c7-4647-b21d-e1702559405d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U3bGkh5t4qnkSQRiMZiefG",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2363,
      "cache_read_input_tokens": 31099,
      "output_tokens": 6757,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2363,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6757,
          "cache_read_input_tokens": 31099,
          "cache_creation_input_tokens": 2363,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2363
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

_source line 44 · 2026-05-19T19:03:17.606Z_

调研完成。现在我有足够的信息进行客观评估。

---

```
【阶段】: Triage

【⚠️ 致命前置问题：投稿venue完全不匹配】

CoRL (Conference on Robot Learning) 2026 明确声明："Submissions without a robotics focus 
will be returned without review." 本 proposal 是一篇纯 NLP/mechanistic interpretability 论文
（LLM 内部表征探测 + 自我纠错门控），与机器人学习完全无关。

→ 投稿 CoRL 2026 的中稿概率：≈0%（desk reject，不进入审稿流程）。

适合的venue：ACL、EMNLP、NeurIPS、ICML、ICLR 的 NLP/interpretability track。
以下评估假设投稿至适当的 NLP/ML 主会（如 ACL/EMNLP 2026 或 NeurIPS 2026）。

═══════════════════════════════════════════════════════════════

【领域调研】:

- arXiv:2604.22271 "How LLMs Detect and Correct Their Own Errors" (2026): 
  本 proposal 的直接前驱。已建立 PANL（post-answer newline）token 处的 correctability 
  信号，在 own-generated errors 上达到 0.614 AUROC。该论文已将 correctability 作为一个
  distinct prediction target 从 error detection 中分离出来。proposal 的核心概念贡献
  （correctability as a prediction target）在此论文中已被 operationalize。

- arXiv:2604.13386 "Linear Probe Accuracy Scales with Model Size and Benefits from 
  Multi-Layer Ensembling" (2026): 
  proposal 的主要技术灵感来源。在 deception detection 上 multi-layer stacking 将 AUROC 
  从 0.510 提升至 0.910（+78%）。但该工作针对的是 deception，其 layer-wise encoding 
  特性与 correctability 可能有本质差异。

- arXiv:2604.19974 "Are LLM Uncertainty and Correctness Encoded by the Same Features?" 
  (2026): 
  SAE 分解发现 uncertainty 和 correctness 由功能上不同的 feature population 编码。
  proposal 将此框架 extend 至 correctability（二阶属性）。但原论文针对的是 correctness
  （一阶属性），transferability 是未经验证的假设。

- arXiv:2602.08948 "CoRefine" (2026): 
  已实现基于 output-level confidence 的三路由自修正，211K 参数控制器达到 92.6% halt 
  precision，~190× token reduction。proposal 声称的差异化（hidden-state vs. output 
  logprobs, 真正的 abstention, correctability-aware）是成立的，但 CoRefine 的实际效果
  已经相当强，增量价值需要实验证明。

- arXiv:2512.18605 "Reflective Confidence" (2025): 
  将低 confidence 信号转化为 reflection trigger，在 AIME 2025 上达 83.3%（vs. 70.0% 
  Self-Consistency）。使用 output-level logprobs，未建模 correctability。

- arXiv:2602.08159 "The Confidence Manifold" (2026): 
  correctness 在 activation space 中占据 3-8 维，线性可分。proposal 计划测试 
  correctability 是否共享此结构。这是 proposal 中最有潜在 insight 的部分。

- arXiv:2512.20578 "Gnosis" (2025): 
  multi-signal fusion for correctness prediction, hidden-only 0.78-0.92 AUROC。
  为 correctness 而非 correctability，但技术路线相似。

- arXiv:2507.12379 / arXiv:2504.05419 / arXiv:2604.18419 / arXiv:2506.12217 (2025-2026): 
  四篇 concurrent probe-gating 论文分别探测 arithmetic errors、early exit、dynamic 
  abstention、self-reflection。均未针对 correctability，但方法论上高度相似。

- 调研总结: 2025-2026年出现了一个快速增长的子领域——用 LLM 内部表征探测来辅助自修正
  决策。PANL paper 已将 correctability 概念化，多篇 probe-gating 论文已从不同角度实现
  了 probe→decision 的 pipeline。本 proposal 处于这个快速拥挤的 landscape 的自然延伸
  位置——将多种已有技术（multi-layer ensembling, SAE feature analysis, probe-gating）
  组合应用于 correctability 这个已被定义但未被充分探索的 target。


【Trivial Alternative 检验】:

存在多个 trivial/simpler alternatives：

1. **直接在 PANL probe 上做 multi-layer 扩展**：只需在 PANL paper 的代码基础上训练
   每层的 logistic regression 再 stack，无需任何新的 framework。这个 trivial baseline
   就能回答 proposal 的核心问题（multi-layer ensembling 是否提升 correctability AUROC）。
   Proposal 的 Phase 0 本质上就是这个 trivial experiment。

2. **Output-level confidence thresholding**：CoRefine 已证明 output logprobs 可以做
   有效的三路由，92.6% halt precision。如果 hidden-state probe 只比 logprobs 好 2-3 
   个 AUROC 点，其工程复杂度的增量价值很难justify。

3. **Wait baseline 的 overcorrection 测量**：只需在 correct answers 上跑一遍 Wait 
   baseline 即可，这是一个 weekend experiment，不需要整个 ECP framework。

增量价值在于：如果 ECP 能将 correctability AUROC 从 0.614 显著提升（如 >0.80），且
hidden-state probe 明确优于 output-level confidence，那么三路门控的实际效用才能被
justify。但这是一个 empirical bet，而非 conceptual advance。


【前提假设检验】:

核心逻辑链中有 3 个未经验证的关键假设：

1. **"Correctability 信息充分编码在 internal representations 中"** — PANL paper 
   仅达到 0.614 AUROC，这可能不是 probing 方法的问题，而是信息本身就不够。
   Correctability 是一个 second-order property（不仅要"错"，还要"能纠正"），
   模型可能根本没有在内部充分编码这个信息——因为它在训练中没有被优化来做这件事。
   这是一个 information-theoretic ceiling 问题，不是 extraction 问题。

2. **"Multi-layer ensembling 从 deception detection 可迁移至 correctability"** — 
   Deception 的 layer-wise encoding 有其独特性（模型"知道"真相但选择撒谎，不同层
   编码 ground truth vs. deceptive output），而 correctability 涉及模型自身纠错
   机制的能力判断，编码模式可能完全不同。Proposal 诚实地承认了这是 hypothesis，
   但整个 Phase 1 的前提就建立在这个迁移上。

3. **"SAE confounded features 是 correctability probing 的有效 substrate"** — 
   arXiv:2604.19974 的发现是关于 correctness（一阶属性），correctability 作为
   二阶属性是否也集中在 confounded features 中完全是推测性的。如果 correctability
   的信息分布模式与 correctness 不同，整个 SAE-guided approach 就失去了理论基础。


【3 维度打分】:

1. Novelty: 弱-中 (Weak-to-Medium)
   
   理由：Proposal 的 5 个 claimed contributions 逐一分析：
   
   (1) "Operationalizing correctability as a prediction target" — 已由 PANL paper 
   (arXiv:2604.22271) 完成。该论文明确将 correctability 从 error detection 中分离
   并建立了 baseline probe。Proposal 是在此基础上的改进，不是概念首创。
   
   (2) "Multi-layer ensembling transfer to correctability" — 这是 arXiv:2604.13386 
   的技术在新 domain 上的直接应用。方法本身无新意，novelty 仅在于"试了一下看行不行"。
   
   (3) "Hidden-state probe-based gating with abstention" — probe-gating 已有 4 篇 
   concurrent papers (arXiv:2507.12379, 2504.05419, 2604.18419, 2506.12217)。
   Abstention 是 arXiv:2604.18419 的核心贡献。Correctability-specificity 是新的
   组合点，但不是新方法。
   
   (4) "Representational geometry of correctability" — 这是 proposal 中真正有潜力
   的部分。将 Confidence Manifold (arXiv:2602.08159) 的方法论 extend 到 second-order 
   property 并与 SAE 分析结合，可能产生有意义的 insight（如发现 correctability 需要
   更高维度/非线性边界）。但方法论本身是已有的，新意在于分析对象。
   
   (5) "Threshold analysis" — 这是标准的 engineering analysis，不构成 novelty。
   
   总结：每个 component 都是已有技术的 transfer/组合，conceptual novelty 有限。
   最有新意的是 Phase 3b 的表征几何分析，但独立来看也是已有方法的 straightforward
   extension。整体是"组合创新"而非"概念创新"。

2. Significance: 中 (Medium)
   
   理由：Selective self-correction 是一个实际重要的问题，尤其在 LLM 部署场景中。
   但关键的 "surprising" 检验失败了：
   
   - 如果 ECP 成功提升 AUROC（如 0.614→0.75+），审稿人反应大概率是 "makes sense, 
     combining more features helps" 而非 "surprising"。
   - 如果 ECP 未能大幅提升，审稿人反应是 "correctability may simply not be well-encoded, 
     as the authors themselves anticipated"。
   - 表征几何分析如果发现 correctability 需要更高维度，审稿人反应是 "expected, given 
     it's a second-order property"。
   
   无论结果如何，都难以产生 "I didn't expect this" 的反应。这限制了 significance 的
   上限。此外，practical impact 取决于 probe AUROC 能否达到 actionable 水平（~0.80+），
   这是高度不确定的。

3. Related Work: 强 (Strong)
   
   理由：这是 proposal 最突出的优点。引用了 25+ 篇高度相关的论文，且对每篇的描述
   经我调研验证后是准确的（PANL 的 0.614 AUROC、arXiv:2604.13386 的 0.510→0.910、
   CoRefine 的 92.6% halt precision、arXiv:2604.19974 的 confounded features 等数据
   均与原文一致）。与 CoRefine 的三重差异化（signal source、abstention、correctability-
   awareness）定位清晰。与 4 篇 concurrent probe-gating papers 的差异化也合理。
   对自身假设的不确定性有诚实的 hedge（如反复强调 multi-layer ensembling 的迁移是
   hypothesis）。但需注意：thorough related work ≠ idea 本身有 novelty。


【概率估计】: 

⚠️ 投稿 CoRL 2026：0-5%（desk reject，venue 完全不匹配）

若投稿适当 NLP/ML venue（ACL/EMNLP/NeurIPS）：[18% - 28%] 中位 22%

【估计理由】: 

Idea 的核心是"把多种已有 probing 技术组合应用于 correctability 这个 adjacent target"。
这是一个方向正确、execution-heavy 但 conceptual contribution 偏薄的 proposal。

- Novelty 弱-中 是主要限制因素：5 个 contributions 中没有一个是 conceptual breakthrough，
  全部是 existing techniques 的 transfer/组合。最有 insight 潜力的 Phase 3b 表征几何
  分析只是 proposal 的一个 sub-component 而非主线。
  
- Significance 中 限制了上限：无论正负结果都不太可能让审稿人 "surprised"。这使得
  即使 execution 完美，也很难超过 30%。

- Related Work 强 提供了下限保障：如果 execution 优秀，thoroughness 可以防止直接被拒。

- Proposal 形式非常完善（dual-outcome design、8 baselines、Phase 0 pilot），但这
  恰恰体现了 proposal 的特点：工程完备性补偿了 conceptual thinness。一个真正 novel 
  的 idea 不需要这么多 hedging。

- 22% 中位概率对应 rubric 中 "idea 方向站得住脚但内核薄弱" 到 "有实质内核但发现不
  surprising" 之间的位置。

【主要风险】: 

1. **"Incremental combination" 批评**：审稿人最可能的拒稿理由是 "this combines existing
   probing methods (multi-layer ensembling, SAE features, attention entropy) and applies 
   them to a closely related target (correctability vs. correctness). Each component is 
   borrowed, and the combination lacks a unifying conceptual insight." 这不是 execution 
   能补救的——idea 层面的组合性 novelty 是结构性弱点。

2. **Information ceiling 风险**：如果 correctability 确实没有在 LLM internal representations
   中被充分编码（0.614 AUROC 可能就是接近 ceiling 而非 extraction 不足），那么无论
   用多复杂的 probe，AUROC 都不会大幅提升。此时 proposal 的主线 (Phase 1-2) 全部
   fail，只剩 Phase 3b 作为 negative-result contribution——但一个"发现 correctability
   不太可 probe"的 negative result 的 impact 有限。
```

---

**补充说明**：

关于 venue 选择，我必须明确指出：**这篇 proposal 投稿 CoRL 2026 会被直接 desk reject**。CoRL 官网 Call for Papers 明确要求 "submissions should focus on a core robotics problem" 且 "submissions without a robotics focus will be returned without review"。本 proposal 是纯粹的 NLP/mechanistic interpretability 工作，与机器人学习无任何关联。

如果要继续推进这个 idea，建议将目标 venue 调整为 **ACL 2026, EMNLP 2026, NeurIPS 2026, 或 ICLR 2027**（取决于 submission timeline）。在这些 venue 下，上述 18-28% 的概率估计才是有效的。

Sources:
- [How LLMs Detect and Correct Their Own Errors (PANL paper)](https://arxiv.org/html/2604.22271v1)
- [Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling](https://arxiv.org/abs/2604.13386)
- [Are LLM Uncertainty and Correctness Encoded by the Same Features?](https://arxiv.org/abs/2604.19974)
- [CoRefine: Confidence-Guided Self-Refinement](https://arxiv.org/abs/2602.08948)
- [Reflective Confidence: Correcting Reasoning Flaws via Online Self-Correction](https://arxiv.org/abs/2512.18605)
- [The Confidence Manifold](https://arxiv.org/pdf/2602.08159)
- [Can LLMs Predict Their Own Failures? (Gnosis)](https://arxiv.org/pdf/2512.20578)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Probing for Arithmetic Errors in Language Models](https://arxiv.org/pdf/2507.12379)
- [Decomposing LLM Self-Correction: The Accuracy-Correction Paradox](https://arxiv.org/pdf/2601.00828)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d791f984-73c7-4647-b21d-e1702559405d",
  "isSidechain": false,
  "requestId": "req_011CbCSgCfWJbibe7CfYTu9m",
  "type": "assistant",
  "uuid": "3ce0ff38-8e26-478d-a3aa-90ed04fb1ba1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U3bGkh5t4qnkSQRiMZiefG",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2363,
      "cache_read_input_tokens": 31099,
      "output_tokens": 6757,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2363,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6757,
          "cache_read_input_tokens": 31099,
          "cache_creation_input_tokens": 2363,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2363
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "3ce0ff38-8e26-478d-a3aa-90ed04fb1ba1",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Predict correctability of LLM self-corrections",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "3ce0ff38-8e26-478d-a3aa-90ed04fb1ba1",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Predict correctability of LLM self-corrections",
  "sessionId": "fd340454-b3c3-4e14-b94c-a1c862bbde3e"
}
```

---
