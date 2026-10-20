# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Can LLMs Predict Their Own Correc

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/b45d5360-28f0-406a-af8b-d7e8e5f62908.jsonl`
- **Structured JSON:** [`38b7f66abb3cf2305348.json`](../../sessions/38/38b7f66abb3cf2305348.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T18:55:59.769Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T18:55:59.769Z",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction\n\n## Description\nWe investigate whether LLMs' internal representations can predict which of their errors are self-correctable, and whether this prediction enables selective correction that outperforms both ungated correction, the trivial 'Wait' baseline, and confidence-based routing. Prior work shows a faint correctability signal at the post-answer newline token (PANL) achieving only 0.614 AUROC with a single-layer linear probe — insufficient for reliable gating. We develop Enhanced Correctability Probes (ECP) that combine multi-layer ensemble stacking, multi-token features (PANL + last-answer-token + reasoning tokens), attention-entropy features, pre-Wait hidden-state features (informed by crosscoder analysis of Wait-token mechanisms, arXiv:2510.04128), and SAE-guided feature selection targeting the confounded feature intersection that bridges uncertainty and correctness (motivated by the functional dissociation finding of arXiv:2604.19974, where 68% of pure incorrectness features are causally inert). We begin with a Phase 0 pilot that directly tests whether multi-layer ensembling — which improved deception detection AUROC by up to 78% (arXiv:2604.13386, specifically on Harm-Pressure Knowledge in Llama-70B) — transfers to the fundamentally different task of correctability prediction. These probes gate a three-way decision: retain the original answer (likely correct), attempt correction including probe-selective Wait insertion (error detected, high correctability), or abstain (error detected, low correctability). This framework is distinguished from CoRefine's (arXiv:2602.08948) three-way routing — which uses output-level confidence, lacks genuine abstention, and is not correctability-aware — by using hidden-state probes, providing a genuine abstention option for unfixable errors, and explicitly predicting error fixability rather than confidence. Critically, we provide the first evaluation of the 'Wait' baseline on correct answers, measuring its previously-unknown overcorrection cost. We also conduct the first representational geometry and SAE feature decomposition analysis of correctability vs. correctness, testing whether correctability — a second-order property that depends not just on whether the model is wrong but on whether correction mechanisms can reach the right answer — shares the low-dimensional, linearly-separable structure that correctness exhibits (arXiv:2602.08159), requires higher dimensionality or non-linear boundaries, or depends disproportionately on the narrow confounded feature population identified by arXiv:2604.19974. This analysis, combined with error depth characterization (arXiv:2601.00828) and threshold analysis mapping probe quality to gating utility, ensures publishable contributions even if probe AUROC plateaus at marginal levels. We evaluate across Gemma-3-27B, Qwen-2.5-7B-Instruct, and Mistral-Small-3.2-24B on TriviaQA, MMLU, and GSM8K, comparing against eight baselines including ungated correction, Wait (universal and probe-selective), confidence-based routing (CoRefine-style and Reflective Confidence-style), PAG, and oracle gating. Our contributions are: (1) operationalizing correctability as a prediction target distinct from correctness, (2) the first pilot testing whether multi-layer ensembling transfers from deception to correctability, (3) the first hidden-state probe-based gating with genuine abstention for correctability-aware self-correction — distinguished from CoRefine's confidence-based routing by signal source, abstention capability, and correctability specificity, (4) the first representational geometry and SAE feature decomposition comparison of correctability vs. correctness, testing whether second-order properties have a different confounded-feature signature than first-order properties, and (5) establishing the conditions — including minimum probe quality thresholds — under which probe-gated correction outperforms simpler alternatives including confidence-based controllers.\n\n## Core Problem\nLLMs attempt correction on all detected errors equally, but ~64.5% of self-generated errors are uncorrectable. Recent work reveals a faint internal 'correctability' signal at the post-answer newline token (PANL), but it achieves only 0.614 AUROC on own-generated errors using a single-layer linear probe — barely actionable for reliable gating. Meanwhile, trivial interventions like appending 'Wait' reduce blind spots by 89.3% on known errors, but their overcorrection rate on correct answers is completely untested. Confidence-based controllers like CoRefine (arXiv:2602.08948) achieve efficient three-way routing (halt/rethink/explore-alternative) using output-level logprobs, but they do not distinguish between correctable and uncorrectable errors — treating all detected issues as potentially fixable. Critically, correctability is a second-order property — it depends not just on whether the model is wrong, but on whether the model's correction mechanism can reach the right answer — and recent SAE analysis (arXiv:2604.19974) reveals that uncertainty and correctness are encoded by functionally distinct feature populations, with only rare 'confounded' features bridging both signals. It is unknown whether correctability — which inherently requires engaging both axes — shares the favorable geometric properties (low dimensionality, linear separability) that correctness exhibits, or whether it requires targeting the narrow confounded feature intersection. Can enhanced multi-signal probes substantially improve correctability prediction, what is the representational relationship between correctability, correctness, and uncertainty at the feature level, and under what conditions does probe-gated correction with genuine abstention outperform both ungated correction and simpler confidence-based alternatives?\n\n## Opportunity\nThree converging findings create a clear research opportunity: (1) The PANL paper (arXiv:2604.22271) establishes that correctability is partially encoded in internal representations, but their single-layer, single-token linear probe barely exceeds chance (0.614 AUROC) on own-generated errors — leaving substantial room for improvement. For correctness prediction on adjacent tasks, Gnosis-style multi-signal fusion (arXiv:2512.20578) achieves 0.78–0.92 AUROC on hidden states alone (with the lower end on MMLU-Pro; ablation on Qwen3-1.7B only) and 0.80–0.95 with attention fusion, while attention-head entropy probes (arXiv:2602.13699) achieve +0.06 AUROC absolute improvement in OOD settings (0.70→0.76 average, 8.5% relative vs. Lookback Lens). Multi-layer probe ensembling (arXiv:2604.13386) has dramatically improved deception detection AUROC (0.510→0.910 on Harm-Pressure Knowledge in Llama-70B), though whether similar gains transfer to correctability — a fundamentally different property — is an open empirical question that motivates our pilot experiment. (2) The 'Wait' baseline from Self-Correction Bench (arXiv:2507.02778) is powerful but fundamentally non-selective: it was tested only on known errors, never on correct answers, so its overcorrection cost is unknown. QwQ-32B naturally generates 'Wait' as its first correction token 37.7–76.8% of the time depending on benchmark (SCLI5 to PRM800K-SC), but this behavior varies widely across models and is near-zero for non-reasoning models. Recent mechanistic work shows that internal states before Wait tokens causally modulate distinct reasoning patterns — restarting, recalling, uncertainty expression, and double-checking (arXiv:2510.04128, EMNLP 2025 Findings) — and that Wait token probabilities correlate with reasoning correctness in ways that vary by training strategy (arXiv:2601.17421). These findings suggest Wait's effectiveness is not uniform but depends on which reasoning pattern it triggers, creating an opportunity for probe-selective application. Reflective Confidence (arXiv:2512.18605) demonstrates a related approach, transforming low-confidence output signals into reflection triggers rather than stopping, achieving 83.3% accuracy on AIME 2025 vs. 70.0% for Self-Consistency — but uses only output-level logprobs, not internal representations. (3) Existing gating approaches occupy adjacent niches but leave a clear gap. CoRefine (arXiv:2602.08948) implements three-way routing (halt/rethink/alternative) via a 211K-parameter Conv1D controller on output-level confidence, achieving 92.6% halt precision — but its decisions are confidence-based rather than correctability-aware, and its ALTERNATIVE option explores different approaches rather than genuinely abstaining when errors are likely unfixable. Four concurrent probe-gating papers address correctness, early exit, abstention, or reflection control — but none probe for correctability (whether a specific error is fixable), and none combine hidden-state probes with genuine abstention in a correctability-aware framework. Moreover, the SAE dissociation paper (arXiv:2604.19974) reveals that uncertainty and correctness are encoded by functionally distinct feature populations — with 68% of pure incorrectness features being causally inert and only rare confounded features (102 out of 1,057 in Llama-3.1-8B) bridging both signals to achieve 0.79 AUROC with just 3 features. This finding directly challenges naive linear probing over broad activations and suggests correctability prediction may need to target the narrow confounded feature intersection, motivating our SAE-guided probe design and representational analysis.\n\n## Related Work / Landscape\nThe PANL paper (arXiv:2604.22271) establishes correctability prediction as a distinct task from error detection, achieving 0.986 AUROC for detection but only 0.614 for correctability on own-generated errors using single-layer logistic regression at one token position. This gap — high detectability but low correctability prediction — is the central technical challenge. Gnosis (arXiv:2512.20578) achieves 0.80–0.95 AUROC for correctness prediction by fusing final-layer hidden states with attention-map features via a ~5M-parameter architecture; notably, the hidden-state stream alone achieves 0.78–0.92 AUROC (with the lower end on MMLU-Pro; ablation only reported for Qwen3-1.7B), with attention fusion adding 0–3 points depending on the task. The multi-layer ensembling paper (arXiv:2604.13386) shows that logistic stacking across complementary layers can dramatically improve probe performance — achieving 0.510→0.910 AUROC on the hardest deception detection task (Harm-Pressure Knowledge, Llama-70B) — because informative directions rotate across layers and double-fault analysis reveals complementary error patterns between early and late layers. However, this result is specific to deception detection, which has different layer-wise encoding properties than correctness or correctability; whether analogous gains transfer is an empirical hypothesis we test via a Phase 0 pilot. For correctness prediction specifically, multi-signal approaches show more modest but consistent gains: attention-head entropy probes (arXiv:2602.13699) improve OOD AUROC by +0.06 absolute (0.70→0.76 average across 5 models, an 8.5% relative improvement over Lookback Lens), and perturbation-stability probes (arXiv:2505.21772) add +6 AUROC points via targeted adversarial perturbations to hidden states. SWIFT (arXiv:2505.12225) concatenates all-layer hidden states with learned gating weights to extract token-level quality signals.\n\nThe Self-Correction Bench (arXiv:2507.02778) documents the 64.5% blind spot and shows 'Wait' reduces it by 89.3%. QwQ-32B naturally generates 'Wait' as its first correction token at rates varying by benchmark (37.7% on SCLI5, 72.5% on GSM8K-SC, 76.8% on PRM800K-SC), but this behavior is model-specific — other reasoning models show different patterns and non-reasoning models rarely generate Wait spontaneously. The Wait baseline was never tested on correct answers, leaving the overcorrection cost unknown. Two recent papers provide mechanistic understanding of Wait tokens: arXiv:2510.04128 (EMNLP 2025 Findings) trains crosscoders on DeepSeek-R1-Distill-Llama-8B to identify features that promote or suppress Wait tokens, discovering causal features for distinct reasoning patterns (restarting, recalling, uncertainty expression, double-checking) via activation steering at layer 15; arXiv:2601.17421 systematically analyzes Wait and other discourse tokens across model scales and training strategies, finding that Wait token probabilities correlate with reasoning correctness but that models exploit this signal only partially. Reflective Confidence (arXiv:2512.18605) proposes a related approach, transforming low-confidence output-level logprob signals into reflection triggers rather than early stopping, achieving 83.3% accuracy on AIME 2025 (vs. 70.0% Self-Consistency, K=32) on Qwen3-8B — demonstrating that selective confidence-gated correction can significantly outperform non-selective baselines, though it uses output-level signals rather than internal representations and does not model correctability.\n\nCoRefine (arXiv:2602.08948) is the closest existing system to our three-way gating, implementing halt/rethink/alternative decisions via a 211K-parameter Conv1D controller that consumes output-level confidence traces from the frozen LLM. It achieves 92.6% halt precision, averages 2.7 refinement steps per problem, and reduces tokens ~190× relative to 512-sample baselines on mathematical reasoning benchmarks. However, CoRefine differs from our proposal in three fundamental ways: (a) it uses output-level logprobs rather than hidden-state probes, missing the richer internal signal that PANL demonstrates exists; (b) its HALT decision accepts the current answer — it never genuinely abstains or flags for external intervention when errors are likely unfixable; (c) its routing is confidence-based, not correctability-aware — it cannot distinguish correctable from uncorrectable errors, treating all low-confidence outputs as potentially improvable. Four concurrent probe-gating papers occupy adjacent niches: arXiv:2507.12379 probes for arithmetic errors and selectively re-prompts (only 6–12% of detected errors actually get corrected); arXiv:2504.05419 uses probes for early exit from reasoning chains (AUROC 0.77–0.91 for correctness, not correctability); arXiv:2604.18419 trains value-function probes for dynamic mid-generation abstention; arXiv:2506.12217 uses activation steering to modulate self-reflection frequency. None of these probe for correctability specifically, and none combine hidden-state probes with genuine abstention in a correctability-aware framework.\n\nA critical finding for our probing approach comes from arXiv:2604.19974, which uses sparse autoencoders to decompose LLM representations into functionally distinct feature populations. In Llama-3.1-8B, they identify 700 pure uncertainty features, 255 pure incorrectness features, and only 102 confounded features encoding both signals. The key insight is a functional dissociation: 68% of pure incorrectness features are causally inert (mean accuracy delta of -0.03% when suppressed), while pure uncertainty features are essential for model performance, and only confounded features bridging both axes are causally effective for correctness prediction — with just 3 confounded features from layer 18 achieving 0.79 AUROC. This has direct implications for correctability probing: correctability is inherently a joint uncertainty+correctness concept (the model must be wrong AND the correction mechanism must be able to reach the right answer), so probes targeting broad activation spaces risk relying on functionally inert incorrectness features. This motivates our SAE-guided feature analysis in Phase 3b and suggests that the confounded feature intersection — not the full activation space — may be the effective substrate for correctability prediction, potentially explaining why the single-layer PANL probe achieves only 0.614 AUROC.\n\nThe Confidence Manifold (arXiv:2602.08159) shows correctness occupies only 3–8 dimensions in activation space and is linearly separable with as few as 25 labeled examples. However, correctability is a second-order property: it depends not just on whether the model is wrong, but on whether the model's correction mechanism can reach the right answer given the model's knowledge state and reasoning pathways. The Interpretability-without-Actionability paper (arXiv:2603.18353) provides indirect evidence that this second-order property may be harder to capture: even with 98.2% detection AUROC, activation steering corrected only 20–24% of errors (concept-bottleneck steering) or 0% (SAE feature steering), revealing a 53-percentage-point knowledge-action gap. This suggests correctability may occupy a different — possibly higher-dimensional or non-linear — representational subspace than correctness, and the SAE dissociation finding (arXiv:2604.19974) provides a mechanistic explanation: correctability may require engaging the narrow confounded feature population rather than the broader (but functionally inert) incorrectness features. The Truth-as-a-Trajectory framework (arXiv:2603.01326) proposes that cross-layer displacement vectors capture properties that static single-layer probes miss, potentially relevant to second-order properties like correctability. The Accuracy-Correction Paradox (arXiv:2601.00828) shows weaker models achieve 1.6× higher correction rates and proposes the Error Depth Hypothesis — that stronger models make fewer but deeper errors that resist self-correction — providing a taxonomy of error correctable characteristics. The information-theoretic analysis of correlated errors (Preprints.org 202601.0892) formalizes bounds on self-correction when generator and evaluator share failure modes, motivating external probe-based gating as a mechanism to break the correlation. LLMs also encode problem difficulty as a linearly decodable property (arXiv:2510.18147, ρ ≈ 0.88), suggesting that related meta-cognitive properties may be extractable, though correctability's second-order nature makes direct analogy uncertain.\n\n## Approach\nWe propose a four-phase study of correctability prediction and selective self-correction, including an explicit pilot to validate the multi-layer ensemble transfer hypothesis, SAE-guided feature analysis informed by the uncertainty-correctness dissociation (arXiv:2604.19974), and a contribution plan that is robust to negative results.\n\n**Phase 0: Pilot Feasibility Study.** Before committing to the full experimental pipeline, we run a targeted pilot on the PANL paper's existing correctability labels (Gemma-3-27B, TriviaQA subset). We train independent logistic regression probes at each of the ~42 layers, identify complementary layers via double-fault analysis (following arXiv:2604.13386's methodology), and build a 3–5 layer stacked ensemble. This pilot directly tests whether the multi-layer ensembling technique that improved deception detection AUROC by up to 78% transfers to correctability prediction. Success criterion: if the ensemble achieves ≥0.70 AUROC (meaningful improvement over the 0.614 single-layer baseline), we proceed to Phase 1. If the ensemble plateaus below 0.70, we shift emphasis to the representational geometry and SAE feature analysis (Phase 3b), which remains a publishable contribution. Estimated cost: ~15 H100-hours (single model, single dataset, multi-layer extraction only).\n\n**Phase 1: Enhanced Correctability Probes (ECP).** We move beyond the PANL paper's single-layer, single-token linear probe by developing multi-signal correctability probes. (a) Multi-layer ensemble: train independent logistic regression probes at each layer, select 3–5 complementary layers via double-fault analysis, combine via logistic stacking (following arXiv:2604.13386, but with the explicit caveat that this technique was validated on deception detection — our Phase 0 tests transfer to correctability). (b) Multi-token features: concatenate hidden states from the post-answer newline token (PANL), the last answer token (LAT), and the last 2 reasoning tokens — the PANL paper's own causal analysis shows LAT carries complementary information at different layers. (c) Attention-based features: extract per-head entropy statistics across semantic sections (question, reasoning, answer), following the methodology of arXiv:2602.13699 which achieves +0.06 AUROC absolute improvement over Lookback Lens in OOD correctness prediction. (d) Wait-token features: inspired by the crosscoder analysis of arXiv:2510.04128, extract hidden-state features at the position immediately preceding natural Wait tokens (when present), capturing the causal features that modulate reasoning patterns (restarting, recalling, uncertainty expression, double-checking). The insight from arXiv:2601.17421 that Wait token probabilities correlate with reasoning correctness suggests these features encode meta-cognitive state relevant to correctability. (e) SAE-guided feature selection: motivated by arXiv:2604.19974's finding that only confounded features (encoding both uncertainty and correctness) are causally effective while pure incorrectness features are functionally inert, we train SAEs on our target models and identify confounded features relevant to correctability. We then compare probes trained on (i) full activation spaces, (ii) SAE-reconstructed activations from confounded features only, and (iii) SAE-reconstructed activations excluding pure incorrectness features. This tests whether the narrow confounded feature intersection — rather than broad activations — is the effective substrate for correctability prediction, and whether filtering out causally inert features improves probe AUROC. (f) Non-linear probe ablation: compare linear probes, 2-layer MLPs (hidden dim 16/32), and SWIFT-style all-layer gated aggregation — motivated by the possibility that correctability, as a second-order property, may require non-linear boundaries even if correctness is linearly separable in 3–8 dimensions (arXiv:2602.08159). All probes are trained on on-policy correctability labels generated by running the model's actual self-correction pipeline (multiple correction attempts per error to get calibrated fixability scores), avoiding the distribution mismatch of synthetic error injection documented in SCoRe (arXiv:2409.12917).\n\n**Phase 2: Three-Way Gated Self-Correction.** Use the ECP to implement a three-way decision at inference time: (i) if the error detection probe indicates the answer is likely correct, retain the original answer; (ii) if the error is detected AND the correctability probe predicts high fixability (above a calibrated threshold), attempt correction — either prompting-based correction or probe-selective Wait insertion (applying Wait only when the probe detects both an error and high correctability, leveraging the mechanistic finding from arXiv:2510.04128 that Wait triggers different reasoning patterns depending on internal state); (iii) if the error is detected but correctability is predicted as low, abstain or flag for external intervention. This design is distinguished from CoRefine's (arXiv:2602.08948) three-way routing in three key ways: we use hidden-state probes rather than output-level confidence, our third option is genuine abstention (declining to answer) rather than exploring alternative approaches, and our gating is explicitly correctability-aware — routing based on predicted fixability rather than confidence level. Where CoRefine optimizes compute efficiency (achieving ~190× token reduction), our framework optimizes decision quality by preventing wasted correction attempts on unfixable errors and avoiding overcorrection of correct answers.\n\n**Phase 3: Comprehensive Evaluation.** Evaluate across three dense models where probing is well-understood: Gemma-3-27B (same as PANL paper, validates signal transfer), Qwen-2.5-7B-Instruct (same as PANL paper, smaller scale), and Mistral-Small-3.2-24B (different architecture family, tests generalization). Use three benchmarks (TriviaQA, MMLU, GSM8K) with 10K+ questions each. Compare gated correction against eight baselines: (1) no correction, (2) ungated prompting-based correction, (3) Wait-appended correction applied to all answers — measuring the previously-untested overcorrection rate, (4) Wait-appended correction applied only to probe-detected errors, (5) confidence-threshold gating using log-probabilities (following Reflective Confidence's approach, arXiv:2512.18605), (6) CoRefine-style output-confidence routing (arXiv:2602.08948) — retrained on our models/benchmarks for fair comparison, (7) PAG-style generative verification (arXiv:2506.10406), (8) oracle gating (upper bound). Conduct ablations on: probe architecture (linear vs. MLP vs. ensemble vs. SAE-guided), feature sources (PANL-only vs. multi-token vs. +attention vs. +Wait-features vs. +SAE-confounded), layer selection, cross-task transferability, and threshold sensitivity analysis showing at what AUROC level gating begins to outperform ungated correction.\n\n**Phase 3b: Representational Geometry and Feature Decomposition of Correctability (Robust to Negative Probe Results).** Regardless of probe performance, we conduct a dedicated analysis of the representational relationship between correctability, correctness, and uncertainty at the feature population level. (a) Subspace comparison: compute the principal components of correctness and correctability representations separately (following arXiv:2602.08159's methodology) and measure subspace alignment via principal angle analysis — testing whether correctability occupies the same 3–8 dimensional subspace as correctness or requires distinct dimensions. (b) Dimensionality analysis: determine how many dimensions encode correctability vs. correctness at each layer, and whether correctability requires higher dimensionality (consistent with its second-order nature). (c) Non-linearity characterization: compare linear vs. non-linear probe AUROC gaps for correctability vs. correctness — a larger gap for correctability would indicate it occupies a more complex geometric region. (d) SAE feature decomposition: train SAEs on our target models and decompose correctability-predictive features into pure uncertainty, pure incorrectness, and confounded populations (following arXiv:2604.19974's 2×2 framework). Test whether confounded features are disproportionately important for correctability prediction compared to correctness prediction — which would provide mechanistic evidence that correctability requires simultaneously engaging both uncertainty and correctness axes. Measure the causal efficacy of each population via suppression experiments: if suppressing pure incorrectness features has minimal effect on correctability prediction (paralleling the functional inertness finding for correctness), this confirms the narrow confounded intersection hypothesis and explains the representational ceiling for broad-activation linear probes. (e) Error depth analysis: using the Error Depth Hypothesis framework (arXiv:2601.00828), characterize what makes errors correctable vs. uncorrectable — surface-level errors (calculation mistakes, recall failures) vs. deep errors (fundamental misunderstanding, missing knowledge) — and test whether this taxonomy is reflected in representational distance and SAE feature activation patterns. (f) Cross-layer trajectory analysis: inspired by Truth-as-a-Trajectory (arXiv:2603.01326), examine whether correctability is better captured by cross-layer displacement vectors than by static single-layer activations, which would explain why single-layer probes struggle. This phase yields publishable insights regardless of whether the ECP achieves high AUROC, providing the first empirical characterization of how correctability is (or is not) represented in LLM internal states and the first application of the SAE uncertainty-correctness dissociation framework to a second-order property.\n\n## Inspiration\nThe gap between 0.614 AUROC (single-layer PANL probe) and the consistently higher performance of multi-signal probes on correctness prediction (Gnosis hidden-only: 0.78–0.92; attention entropy: +0.06 AUROC absolute in OOD) suggests correctability prediction has room for improvement with better probing methodology — though the magnitude of potential gains is uncertain given correctability's second-order nature. The dramatic improvement from multi-layer ensembling on deception detection (0.510→0.910; arXiv:2604.13386) demonstrates that multi-layer stacking can rescue failing single-layer probes, but transferability to correctability is a hypothesis to test, not a guaranteed outcome. The SAE dissociation finding (arXiv:2604.19974) — that only rare confounded features bridging uncertainty and correctness are causally effective — provides both a challenge and an opportunity: correctability probes may need to target this narrow feature intersection, but successfully doing so could yield more principled and interpretable predictions than broad-activation probing. The untested overcorrection cost of the 'Wait' baseline, combined with new mechanistic understanding of Wait tokens' causal role in triggering distinct reasoning patterns (arXiv:2510.04128, arXiv:2601.17421), creates a clear opportunity for probe-selective Wait application. CoRefine (arXiv:2602.08948) demonstrates the viability of learned three-way routing for self-correction but uses output-level confidence without correctability awareness or genuine abstention — leaving a well-defined gap for hidden-state probe-based gating that distinguishes correctable from uncorrectable errors. Key untried combination: multi-signal enhanced probes for correctability prediction informed by SAE feature analysis + three-way gating with genuine abstention + comparison against Wait and confidence-based controllers, with explicit analysis of what makes correctability representationally distinct from correctness at the feature population level.\n\n## Key References\n- How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals (arXiv:2604.22271, 2026) — establishes PANL correctability signal, 0.614 AUROC baseline\n- Self-Correction Bench: Uncovering and Addressing the Self-Correction Blind Spot in LLMs (arXiv:2507.02778, NeurIPS 2025 Workshop) — 64.5% blind spot, Wait baseline achieving 89.3% reduction; QwQ-32B generates Wait first-token at 37.7–76.8% depending on benchmark\n- Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling (arXiv:2604.13386, 2026) — multi-layer stacking on deception detection: +29% on Insider Trading, +78% on Harm-Pressure Knowledge (0.510→0.910 in Llama-70B); transfer to correctability is a hypothesis we test\n- Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits — Gnosis (arXiv:2512.20578, 2025) — multi-signal fusion for correctness prediction: hidden-only 0.78–0.92 AUROC (ablation on Qwen3-1.7B), fusion 0.80–0.95 AUROC\n- Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders (arXiv:2604.19974, 2026) — SAE decomposition reveals functionally distinct feature populations: 68% of pure incorrectness features are causally inert; only rare confounded features (102/1,057 in Llama-3.1-8B) bridge uncertainty and correctness, achieving 0.79 AUROC with 3 features from layer 18; directly informs our probe design and Phase 3b analysis\n- CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute (arXiv:2602.08948, 2026) — three-way routing (halt/rethink/alternative) via 211K-parameter Conv1D controller on output-level confidence; 92.6% halt precision, ~190× token reduction; differs from our approach in signal source (output logprobs vs. hidden-state probes), decision type (no genuine abstention), and gating criterion (confidence vs. correctability)\n- Reflective Confidence: Correcting Reasoning Flaws via Online Self-Correction (arXiv:2512.18605, 2025) — transforms low-confidence output signals into reflection triggers; 83.3% on AIME 2025 vs. 70.0% Self-Consistency; uses output-level logprobs, no correctability modeling\n- Internal states before wait modulate reasoning patterns (arXiv:2510.04128, EMNLP 2025 Findings) — crosscoders identify causal features promoting/suppressing Wait tokens; distinct reasoning patterns (restarting, recalling, uncertainty expression, double-checking) triggered by pre-Wait internal states\n- Oops, Wait: Token-Level Signals as a Lens into LLM Reasoning (arXiv:2601.17421, Jan 2026) — Wait token probabilities correlate with reasoning correctness; models exploit Wait signals only partially; implications for token-level steering\n- Probing for Arithmetic Errors in Language Models (arXiv:2507.12379, 2025) — probe-guided selective re-prompting, 6–12% correction rate\n- Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification (arXiv:2504.05419, 2025) — probe-gated early exit, AUROC 0.77–0.91\n- Knowing When to Quit: A Principled Framework for Dynamic Abstention in LLM Reasoning (arXiv:2604.18419, 2026) — value-function probes for abstention gating\n- From Emergence to Control: Probing and Modulating Self-Reflection in Language Models (arXiv:2506.12217, 2025) — self-reflection vector steering\n- The Confidence Manifold (arXiv:2602.08159, 2026) — correctness in 3–8 dimensions, 25-example sufficiency, linearly separable\n- Attention Head Entropy of LLMs Predicts Answer Correctness (arXiv:2602.13699, 2026) — per-head 2-Rényi entropy achieves OOD AUROC 0.76 average (+0.06 absolute, 8.5% relative improvement over Lookback Lens)\n- PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier (arXiv:2506.10406, 2025)\n- Understanding the Dark Side of LLMs' Intrinsic Self-Correction (ACL 2025) — overcorrection and cognitive biases\n- Interpretability without Actionability (arXiv:2603.18353, 2026) — knowledge-action gap: 98.2% detection AUROC but only 20–24% correction via steering, 53-point gap\n- Mining Intrinsic Rewards from LLM Hidden States — SWIFT (arXiv:2505.12225, 2025) — all-layer gated aggregation\n- Between the Layers Lies the Truth (arXiv:2603.22299, 2026) — cross-layer agreement features\n- Truth as a Trajectory (arXiv:2603.01326, 2026) — cross-layer displacement vectors capture properties missed by static single-layer probes\n- Training Language Models to Self-Correct via Reinforcement Learning — SCoRe (arXiv:2409.12917, 2024) — on-policy training data importance\n- Large Language Models Cannot Self-Correct Reasoning Yet (ICLR 2024)\n- Decomposing LLM Self-Correction: The Accuracy-Correction Paradox (arXiv:2601.00828, 2026) — Error Depth Hypothesis: weaker models achieve 1.6× higher correction rates; deeper errors resist self-correction\n- No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes (arXiv:2509.10625, ICLR 2026 Workshop)\n- Calibrating LLM Confidence by Probing Perturbed Representation Stability (arXiv:2505.21772, 2025) — +6 AUROC points via adversarial perturbation stability\n- LLMs Encode How Difficult Problems Are (arXiv:2510.18147, 2025) — difficulty linearly decodable (ρ ≈ 0.88); meta-cognitive properties extractable but correctability's second-order nature makes transfer uncertain\n- Limits of Self-Correction in LLMs: An Information-Theoretic Analysis of Correlated Errors (Preprints.org 202601.0892, Feb 2026) — formalizes bounds on self-correction with correlated generator-evaluator errors\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '220–280 H100-hours (Phase 0 pilot: ~15 hrs; inference for 3 models × ~30K questions × 3 passes [initial + Wait + correction] + multi-layer hidden state extraction across ~10 layers + attention feature extraction + Wait-feature extraction + SAE training and feature decomposition + probe training + representational geometry analysis + ablations)', 'timeline': '11–13 weeks (includes pilot, SAE analysis, full experiments, geometry analysis, paper writing)', 'estimated_gpu_cost': '$550–700 (at ~$2.50/H100-hr on cloud providers)'}\n- **human_in_loop**: {'gpu_hours': '220–280 H100-hours (same compute, faster iteration via AI-assisted code/analysis)', 'timeline': '8–10 weeks', 'claude_api_cost': '$150–210 (experiment orchestration, SAE analysis notebooks, geometry visualization, paper drafting via Sonnet 4.6)', 'estimated_gpu_cost': '$550–700'}\n- **auto_research**: {'gpu_hours': '300–360 H100-hours (overhead from automated probe architecture sweeps, SAE training and decomposition, threshold optimization, representational geometry grid, and broader ablation grid)', 'timeline': '2–3 weeks wall-clock', 'claude_api_cost': '$420–580 (full pipeline orchestration, code generation, debugging, SAE analysis, statistical analysis, visualization, paper drafting)', 'estimated_gpu_cost': '$750–900', 'speed_bottleneck': 'Sequential multi-layer hidden state extraction over ~90K forward passes (3 models × 30K questions); extraction requires full-precision activations at 5–10 layers per pass and cannot be batched as aggressively as standard inference; SAE training adds ~20–30 H100-hours per model'}\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T18:55:59.775Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T18:55:59.775Z",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908"
}
```

---

## Round 1

35 recorded events

### User

_source line 3 · 2026-05-19T18:55:59.791Z_

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
  "promptId": "8256411a-5d7a-47b0-8825-6efc21691ae1",
  "type": "user",
  "uuid": "e2098710-083b-481d-9c4c-5bb8869ae5bc",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T18:55:59.789Z_

```json
{
  "parentUuid": "e2098710-083b-481d-9c4c-5bb8869ae5bc",
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
  "uuid": "5e97212b-1770-4a7f-8459-43d592fe2d38",
  "timestamp": "2026-05-19T18:55:59.789Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T18:55:59.789Z_

```json
{
  "parentUuid": "5e97212b-1770-4a7f-8459-43d592fe2d38",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8efb69f7-c74e-411c-ac98-2eebdd6e7555",
  "timestamp": "2026-05-19T18:55:59.789Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
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
  "leafUuid": "8efb69f7-c74e-411c-ac98-2eebdd6e7555",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Predict LLM error correctability with enhanced probes",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908"
}
```

---

### Assistant

_source line 8 · 2026-05-19T18:56:12.594Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for CoRL 2026 submission. Let me first carefully read the proposal, then conduct web searches to understand the current landscape before making my assessment.

Wait - CoRL is Conference on Robot Learning. This proposal is about LLM self-correction and probing internal representations. This seems like it would be more appropriate for NLP/ML venues like ACL, EMNLP, NeurIPS, ICML, ICLR rather than CoRL. Let me note this but focus on the idea quality assessment as requested.

Actually, let me re-read the instructions. 

The user is submitting to CoRL 2026, but this proposal is purely about LLM internal representations and self-correction mechanisms - there's no robotics component at all. That's a fundamental venue mismatch I should flag. But first, let me search for the referenced papers to understand what's already been done in this space.

I need to look up several recent papers on correctability prediction, multi-layer probing ensembles, SAE dissociation, and self-correction gating to see where this work fits in the landscape and what's novel here.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8efb69f7-c74e-411c-ac98-2eebdd6e7555",
  "isSidechain": false,
  "requestId": "req_011CbCSJsXyjpTybtAYWAb7A",
  "type": "assistant",
  "uuid": "3814300f-6849-41cf-9dc4-ca6fed5bf525",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUGKf5VPF1qN73qmXZjqF7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10635,
      "cache_read_input_tokens": 13985,
      "output_tokens": 462,
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
          "output_tokens": 462,
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

_source line 9 · 2026-05-19T18:56:12.598Z_

我先进行前置调研，然后再打分。让我搜索几个关键方向。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3814300f-6849-41cf-9dc4-ca6fed5bf525",
  "isSidechain": false,
  "requestId": "req_011CbCSJsXyjpTybtAYWAb7A",
  "type": "assistant",
  "uuid": "c10060b6-0dd8-4c05-9e4e-2b3d61cc020c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUGKf5VPF1qN73qmXZjqF7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10635,
      "cache_read_input_tokens": 13985,
      "output_tokens": 462,
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
          "output_tokens": 462,
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

_source line 10 · 2026-05-19T18:56:12.795Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012Wmw18LazWUfDuGWwHMept`</summary>

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
  "parentUuid": "c10060b6-0dd8-4c05-9e4e-2b3d61cc020c",
  "isSidechain": false,
  "requestId": "req_011CbCSJsXyjpTybtAYWAb7A",
  "type": "assistant",
  "uuid": "2691e9a3-b85b-4155-99ae-ee6288ce5cc0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUGKf5VPF1qN73qmXZjqF7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10635,
      "cache_read_input_tokens": 13985,
      "output_tokens": 462,
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
          "output_tokens": 462,
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

_source line 11 · 2026-05-19T18:56:12.802Z_

<details><summary>↩ Tool result · `toolu_012Wmw18LazWUfDuGWwHMept`</summary>

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
  "parentUuid": "2691e9a3-b85b-4155-99ae-ee6288ce5cc0",
  "isSidechain": false,
  "promptId": "8256411a-5d7a-47b0-8825-6efc21691ae1",
  "type": "user",
  "uuid": "45b11c04-0503-413e-8dfd-0da5a17113c9",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "2691e9a3-b85b-4155-99ae-ee6288ce5cc0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T18:56:15.643Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do the web searches. I'll search for multiple things in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45b11c04-0503-413e-8dfd-0da5a17113c9",
  "isSidechain": false,
  "requestId": "req_011CbCSKqfeJa3h7yd8Mg58a",
  "type": "assistant",
  "uuid": "8c512db0-ca67-4f89-b2fa-a6b8a73c1fad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wz9TfiMGrxgkhT1K9Fw4yY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 986,
      "cache_read_input_tokens": 24620,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 986,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 118,
          "cache_read_input_tokens": 24620,
          "cache_creation_input_tokens": 986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 986
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

_source line 13 · 2026-05-19T18:56:16.191Z_

Let me conduct the required literature searches before evaluating.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c512db0-ca67-4f89-b2fa-a6b8a73c1fad",
  "isSidechain": false,
  "requestId": "req_011CbCSKqfeJa3h7yd8Mg58a",
  "type": "assistant",
  "uuid": "5b827e01-4e2f-46a0-bc7b-78d3d89000d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wz9TfiMGrxgkhT1K9Fw4yY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 986,
      "cache_read_input_tokens": 24620,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 986,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 118,
          "cache_read_input_tokens": 24620,
          "cache_creation_input_tokens": 986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 986
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

_source line 14 · 2026-05-19T18:56:16.730Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GLExUevAkeZnWexkRmM72m`</summary>

```json
{
  "query": "arXiv 2604.22271 LLM correctability prediction PANL internal confidence signals"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b827e01-4e2f-46a0-bc7b-78d3d89000d5",
  "isSidechain": false,
  "requestId": "req_011CbCSKqfeJa3h7yd8Mg58a",
  "type": "assistant",
  "uuid": "6ee77e2a-5b09-42ea-b297-8cb66b2cdeab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wz9TfiMGrxgkhT1K9Fw4yY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 986,
      "cache_read_input_tokens": 24620,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 986,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 118,
          "cache_read_input_tokens": 24620,
          "cache_creation_input_tokens": 986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 986
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

_source line 15 · 2026-05-19T18:56:23.768Z_

<details><summary>↩ Tool result · `toolu_01GLExUevAkeZnWexkRmM72m`</summary>

```text
Web search results for query: "arXiv 2604.22271 LLM correctability prediction PANL internal confidence signals"

Links: [{"title":"How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals","url":"https://arxiv.org/html/2604.22271v1"},{"title":"How do LLMs Compute Verbal Confidence?","url":"https://arxiv.org/html/2603.17839v1"},{"title":"Factual Confidence of LLMs: on Reliability and Robustness of Current   Estimators","url":"https://arxiv.org/pdf/2406.13415"},{"title":"Graph-based Confidence Calibration for Large Language Models","url":"https://arxiv.org/pdf/2411.02454"},{"title":"When to Trust LLMs: Aligning Confidence with Response Quality","url":"https://arxiv.org/pdf/2404.17287"},{"title":"Confidence v.s. Critique: A Decomposition of Self-Correction Capability   for LLMs","url":"https://arxiv.org/pdf/2412.19513"}]

Based on the search results, I found the paper you're looking for. Here's what I found:

## arXiv 2604.22271: "How LLMs Detect and Correct Their Own Errors"

This paper investigates how large language models can detect their own errors and sometimes correct them without external feedback, revealing that LLMs naturally implement a second-order confidence architecture whose internal evaluative signal encodes not only whether an answer is likely wrong but whether the model has the knowledge to fix it.

### Key Findings:

The research shows that: (i) verbal confidence predicts error detection far beyond token log-probabilities; (ii) PANL activations predict error detection beyond verbal confidence itself; and (iii) PANL predicts which errors the model can correct—where all behavioral signals fail.

### PANL (Post-Answer NewLine) Signal:

The PANL signal is a confidence representation cached at a token immediately following the answer (the post-answer newline) that causally drives verbal confidence and dissociates from log-probabilities. Causal interventions confirm that PANL signals rescue error detection behavior when answer information is corrupted.

### Validation:

All findings replicate across models (Gemma 3 27B and Qwen 2.5 7B) and tasks (TriviaQA and MNLI).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ee77e2a-5b09-42ea-b297-8cb66b2cdeab",
  "isSidechain": false,
  "promptId": "8256411a-5d7a-47b0-8825-6efc21691ae1",
  "type": "user",
  "uuid": "9b0c0735-084b-47fc-aad1-77f145b20f47",
  "toolUseResult": {
    "query": "arXiv 2604.22271 LLM correctability prediction PANL internal confidence signals",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Nj82dkYwuLboTTCyY8Jyv3",
        "content": [
          {
            "title": "How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals",
            "url": "https://arxiv.org/html/2604.22271v1"
          },
          {
            "title": "How do LLMs Compute Verbal Confidence?",
            "url": "https://arxiv.org/html/2603.17839v1"
          },
          {
            "title": "Factual Confidence of LLMs: on Reliability and Robustness of Current   Estimators",
            "url": "https://arxiv.org/pdf/2406.13415"
          },
          {
            "title": "Graph-based Confidence Calibration for Large Language Models",
            "url": "https://arxiv.org/pdf/2411.02454"
          },
          {
            "title": "When to Trust LLMs: Aligning Confidence with Response Quality",
            "url": "https://arxiv.org/pdf/2404.17287"
          },
          {
            "title": "Confidence v.s. Critique: A Decomposition of Self-Correction Capability   for LLMs",
            "url": "https://arxiv.org/pdf/2412.19513"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's what I found:\n\n## arXiv 2604.22271: \"How LLMs Detect and Correct Their Own Errors\"\n\nThis paper investigates how large language models can detect their own errors and sometimes correct them without external feedback, revealing that LLMs naturally implement a second-order confidence architecture whose internal evaluative signal encodes not only whether an answer is likely wrong but whether the model has the knowledge to fix it.\n\n### Key Findings:\n\nThe research shows that: (i) verbal confidence predicts error detection far beyond token log-probabilities; (ii) PANL activations predict error detection beyond verbal confidence itself; and (iii) PANL predicts which errors the model can correct—where all behavioral signals fail.\n\n### PANL (Post-Answer NewLine) Signal:\n\nThe PANL signal is a confidence representation cached at a token immediately following the answer (the post-answer newline) that causally drives verbal confidence and dissociates from log-probabilities. Causal interventions confirm that PANL signals rescue error detection behavior when answer information is corrupted.\n\n### Validation:\n\nAll findings replicate across models (Gemma 3 27B and Qwen 2.5 7B) and tasks (TriviaQA and MNLI)."
    ],
    "durationSeconds": 7.031057218999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6ee77e2a-5b09-42ea-b297-8cb66b2cdeab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T18:56:26.317Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012ZeWdD6rq5gpAbkKuU45ji`</summary>

```json
{
  "query": "arXiv 2604.13386 multi-layer ensembling linear probe deception detection AUROC"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b0c0735-084b-47fc-aad1-77f145b20f47",
  "isSidechain": false,
  "requestId": "req_011CbCSLduVgvugGm6eBoLnd",
  "type": "assistant",
  "uuid": "7f45488f-f21e-44bc-a698-572a6883d7e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQCEe7Ju8N7zu4Q5iyvrcD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 25606,
      "output_tokens": 75,
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
          "output_tokens": 75,
          "cache_read_input_tokens": 25606,
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

_source line 17 · 2026-05-19T18:56:33.596Z_

<details><summary>↩ Tool result · `toolu_012ZeWdD6rq5gpAbkKuU45ji`</summary>

```text
Web search results for query: "arXiv 2604.13386 multi-layer ensembling linear probe deception detection AUROC"

Links: [{"title":"[2604.13386] Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling","url":"https://arxiv.org/abs/2604.13386"},{"title":"Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling","url":"https://arxiv.org/html/2604.13386v1"},{"title":"Detecting Strategic Deception Using Linear Probes","url":"https://arxiv.org/pdf/2502.03407"},{"title":"[2502.03407] Detecting Strategic Deception Using Linear Probes","url":"https://arxiv.org/abs/2502.03407"},{"title":"Detecting Strategic Deception Using Linear Probes - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2502.03407"},{"title":"Caught in the Act: a mechanistic approach to detecting deception","url":"https://arxiv.org/html/2508.19505v2"},{"title":"Detecting Multi-Agent Collusion Through Multi-Agent Interpretability","url":"https://arxiv.org/html/2604.01151v1"},{"title":"Caught in the Act: a mechanistic approach to detecting deception","url":"https://arxiv.org/pdf/2508.19505"},{"title":"Building Better Deception Probes Using Targeted Instruction Pairs","url":"https://arxiv.org/pdf/2602.01425"}]

Based on the search results, I found the paper you're looking for. Here's what the research on arXiv 2604.13386 reveals:

## Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling

Linear probes can detect when language models produce outputs they "know" are wrong, a capability relevant to both deception and reward hacking. However, single-layer probes are fragile: the best layer varies across models and tasks, and probes fail entirely on some deception types.

### Key Findings on Multi-Layer Ensembling:

Combining probes from multiple layers into an ensemble recovers strong performance even where single-layer probes fail, improving AUROC by +29% on Insider Trading and +78% on Harm-Pressure Knowledge.

### Scaling Results:

Across 12 models (0.5B--176B parameters), probe accuracy improves with scale: ~5% AUROC per 10x parameters (R=0.81).

### Geometric Explanation:

Deception directions rotate gradually across layers rather than appearing at one location, explaining both why single-layer probes are brittle and why multi-layer ensembles succeed.

The paper was submitted to arXiv on April 15, 2026, by Erik Nordby, Tasha Pais, and Aviel Parrack.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f45488f-f21e-44bc-a698-572a6883d7e4",
  "isSidechain": false,
  "promptId": "8256411a-5d7a-47b0-8825-6efc21691ae1",
  "type": "user",
  "uuid": "11edb556-2231-4db7-9009-322293c70b70",
  "toolUseResult": {
    "query": "arXiv 2604.13386 multi-layer ensembling linear probe deception detection AUROC",
    "results": [
      {
        "tool_use_id": "srvtoolu_01StVD2evTx3WgkK63Sw2e1R",
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
            "title": "Detecting Strategic Deception Using Linear Probes",
            "url": "https://arxiv.org/pdf/2502.03407"
          },
          {
            "title": "[2502.03407] Detecting Strategic Deception Using Linear Probes",
            "url": "https://arxiv.org/abs/2502.03407"
          },
          {
            "title": "Detecting Strategic Deception Using Linear Probes - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/arXiv:2502.03407"
          },
          {
            "title": "Caught in the Act: a mechanistic approach to detecting deception",
            "url": "https://arxiv.org/html/2508.19505v2"
          },
          {
            "title": "Detecting Multi-Agent Collusion Through Multi-Agent Interpretability",
            "url": "https://arxiv.org/html/2604.01151v1"
          },
          {
            "title": "Caught in the Act: a mechanistic approach to detecting deception",
            "url": "https://arxiv.org/pdf/2508.19505"
          },
          {
            "title": "Building Better Deception Probes Using Targeted Instruction Pairs",
            "url": "https://arxiv.org/pdf/2602.01425"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's what the research on arXiv 2604.13386 reveals:\n\n## Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling\n\nLinear probes can detect when language models produce outputs they \"know\" are wrong, a capability relevant to both deception and reward hacking. However, single-layer probes are fragile: the best layer varies across models and tasks, and probes fail entirely on some deception types.\n\n### Key Findings on Multi-Layer Ensembling:\n\nCombining probes from multiple layers into an ensemble recovers strong performance even where single-layer probes fail, improving AUROC by +29% on Insider Trading and +78% on Harm-Pressure Knowledge.\n\n### Scaling Results:\n\nAcross 12 models (0.5B--176B parameters), probe accuracy improves with scale: ~5% AUROC per 10x parameters (R=0.81).\n\n### Geometric Explanation:\n\nDeception directions rotate gradually across layers rather than appearing at one location, explaining both why single-layer probes are brittle and why multi-layer ensembles succeed.\n\nThe paper was submitted to arXiv on April 15, 2026, by Erik Nordby, Tasha Pais, and Aviel Parrack."
    ],
    "durationSeconds": 7.273661408999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7f45488f-f21e-44bc-a698-572a6883d7e4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T18:56:36.667Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L1RDW3t5UzEYGSMxQxaNU7`</summary>

```json
{
  "query": "arXiv 2604.19974 SAE sparse autoencoder uncertainty correctness features dissociation LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11edb556-2231-4db7-9009-322293c70b70",
  "isSidechain": false,
  "requestId": "req_011CbCSMMvLxHz3VUrAaTnLc",
  "type": "assistant",
  "uuid": "b0116e16-d0e3-4655-8f48-53d0e4cf0d4f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N8VLKfX27cfiWk5Su3ebTC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 26335,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 26335,
          "cache_creation_input_tokens": 808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 808
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

_source line 19 · 2026-05-19T18:56:44.439Z_

<details><summary>↩ Tool result · `toolu_01L1RDW3t5UzEYGSMxQxaNU7`</summary>

```text
Web search results for query: "arXiv 2604.19974 SAE sparse autoencoder uncertainty correctness features dissociation LLM"

Links: [{"title":"Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders","url":"https://arxiv.org/html/2604.19974v1"},{"title":"[2604.19974] Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders","url":"https://arxiv.org/abs/2604.19974"},{"title":"Sparse but Wrong: Incorrect L0 Leads to Incorrect Features in Sparse Autoencoders","url":"https://arxiv.org/pdf/2508.16560"},{"title":"Mechanistic Interpretability of Code Correctness in LLMs via Sparse Autoencoders","url":"https://arxiv.org/pdf/2510.02917"},{"title":"Sparse Autoencoder Features for Classifications and Transferability","url":"https://arxiv.org/html/2502.11367"},{"title":"Mechanistic Interpretability of Code Correctness in LLMs via Sparse Autoencoders","url":"https://arxiv.org/html/2510.02917v1"}]

Based on the search results, here's what I found about arXiv paper 2604.19974:

## Paper Summary

Large language models can be uncertain yet correct, or confident yet wrong, raising the question of whether their output-level uncertainty and their actual correctness are driven by the same internal mechanisms or by distinct feature populations.

The paper addresses this question by using sparse autoencoders (SAEs) to decompose LLM internal representations into individual features and testing whether uncertainty and correctness are encoded by distinct or overlapping feature populations.

## Methodology

The authors introduce a 2x2 framework that partitions model predictions along correctness and confidence axes, and uses sparse autoencoders to identify features associated with each dimension independently. Applying this to Llama-3.1-8B and Gemma-2-9B, they identify three feature populations that play fundamentally different functional roles.

## Key Findings

The procedure yields three distinct feature populations: pure uncertainty features, pure incorrectness features, and confounded features associated with both signals. 

Pure uncertainty features are functionally essential: suppressing them severely degrades accuracy. Pure incorrectness features are functionally inert: despite showing statistically significant activation differences between correct and incorrect predictions, the majority produce near-zero change in accuracy when suppressed.

The paper was published on April 21, 2026, with authors including Het Patel, Tiejin Chen, and others.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0116e16-d0e3-4655-8f48-53d0e4cf0d4f",
  "isSidechain": false,
  "promptId": "8256411a-5d7a-47b0-8825-6efc21691ae1",
  "type": "user",
  "uuid": "99139862-4020-4e82-8823-abca3e581d51",
  "toolUseResult": {
    "query": "arXiv 2604.19974 SAE sparse autoencoder uncertainty correctness features dissociation LLM",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FvZkSBWRprFNewsL77AtRT",
        "content": [
          {
            "title": "Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders",
            "url": "https://arxiv.org/html/2604.19974v1"
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
            "title": "Sparse Autoencoder Features for Classifications and Transferability",
            "url": "https://arxiv.org/html/2502.11367"
          },
          {
            "title": "Mechanistic Interpretability of Code Correctness in LLMs via Sparse Autoencoders",
            "url": "https://arxiv.org/html/2510.02917v1"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2604.19974:\n\n## Paper Summary\n\nLarge language models can be uncertain yet correct, or confident yet wrong, raising the question of whether their output-level uncertainty and their actual correctness are driven by the same internal mechanisms or by distinct feature populations.\n\nThe paper addresses this question by using sparse autoencoders (SAEs) to decompose LLM internal representations into individual features and testing whether uncertainty and correctness are encoded by distinct or overlapping feature populations.\n\n## Methodology\n\nThe authors introduce a 2x2 framework that partitions model predictions along correctness and confidence axes, and uses sparse autoencoders to identify features associated with each dimension independently. Applying this to Llama-3.1-8B and Gemma-2-9B, they identify three feature populations that play fundamentally different functional roles.\n\n## Key Findings\n\nThe procedure yields three distinct feature populations: pure uncertainty features, pure incorrectness features, and confounded features associated with both signals. \n\nPure uncertainty features are functionally essential: suppressing them severely degrades accuracy. Pure incorrectness features are functionally inert: despite showing statistically significant activation differences between correct and incorrect predictions, the majority produce near-zero change in accuracy when suppressed.\n\nThe paper was published on April 21, 2026, with authors including Het Patel, Tiejin Chen, and others."
    ],
    "durationSeconds": 7.767185559000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b0116e16-d0e3-4655-8f48-53d0e4cf0d4f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T18:56:47.825Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AZnuMeiRFLUPpcAbVCwjB1`</summary>

```json
{
  "query": "LLM self-correction gating probe correctability 2025 2026 selective correction hidden states"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99139862-4020-4e82-8823-abca3e581d51",
  "isSidechain": false,
  "requestId": "req_011CbCSNAnQ4XNwnh9ehfaGL",
  "type": "assistant",
  "uuid": "03ca58f0-04ed-465d-bf68-1b69f3862293",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FfzTZVmjQi1ye3xNazRtHa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 748,
      "cache_read_input_tokens": 27143,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 748,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 27143,
          "cache_creation_input_tokens": 748,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 748
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
  "leafUuid": "03ca58f0-04ed-465d-bf68-1b69f3862293",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Predict LLM error correctability with enhanced probes",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908"
}
```

---

### Tool result

_source line 23 · 2026-05-19T18:56:55.661Z_

<details><summary>↩ Tool result · `toolu_01AZnuMeiRFLUPpcAbVCwjB1`</summary>

```text
Web search results for query: "LLM self-correction gating probe correctability 2025 2026 selective correction hidden states"

Links: [{"title":"Understanding the Dark Side of LLMs’ Intrinsic Self-Correction","url":"https://arxiv.org/html/2412.14959v1"},{"title":"Temporal Predictors of Outcome in Reasoning Language Models","url":"https://arxiv.org/pdf/2511.14773"},{"title":"Self-correction is Not An Innate Capability in Language Models","url":"https://arxiv.org/pdf/2410.20513"},{"title":"Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification","url":"https://arxiv.org/html/2504.05419v1"},{"title":"Intrinsic Self-correction for Enhanced Morality: An Analysis of Internal   Mechanisms and the Superficial Hypothesis","url":"https://arxiv.org/pdf/2407.15286"},{"title":"Latent Space Chain-of-Embedding Enables Output-free LLM Self-Evaluation","url":"https://arxiv.org/pdf/2410.13640"},{"title":"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/pdf/2512.20578"}]

Based on the search results, here are relevant papers and findings related to LLM self-correction, gating, probing, correctability, and hidden states:

## Key Papers Found:

1. **Understanding the Dark Side of LLMs' Intrinsic Self-Correction** (December 2024)
   Uses a binary classification probing experiment with tuned lens to probe LLM's internal token representations at each layer. This allows tracking of LLM's internal answer evolution by computing the difference of confidence score between correct and incorrect answers.

2. **Temporal Predictors of Outcome in Reasoning Language Models** (2025)
   Predicts answer correctness directly from an LLM's hidden state while the chain-of-thought is being generated, not only after initial question or the final answer. Shows that hidden states from very short prefixes already contain linearly decodable information about eventual correctness, reaching AUCs up to 0.8+ on MATH-like data.

3. **Self-correction is Not An Innate Capability in Language Models** (2024)
   Conducts a mechanistic analysis of the hidden states to examine how key components of self-correction, such as Chain-of-Thought and external feedback, interact to facilitate moral self-correction.

4. **Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification** (April 2025)
   Focuses on probing hidden states to verify intermediate answers during reasoning chains.

5. **Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits** (December 2025)
   Proposes Gnosis, which taps hidden states and attention maps from a frozen LLM and predicts a scalar correctness score.

These papers address selective correction based on correctability prediction from hidden states, which aligns with your query about gating mechanisms for self-correction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03ca58f0-04ed-465d-bf68-1b69f3862293",
  "isSidechain": false,
  "promptId": "8256411a-5d7a-47b0-8825-6efc21691ae1",
  "type": "user",
  "uuid": "6737bddb-25cd-4964-bf9f-1c977f48c337",
  "toolUseResult": {
    "query": "LLM self-correction gating probe correctability 2025 2026 selective correction hidden states",
    "results": [
      {
        "tool_use_id": "srvtoolu_013PbYFHZzqfpZ5JAC9erU1B",
        "content": [
          {
            "title": "Understanding the Dark Side of LLMs’ Intrinsic Self-Correction",
            "url": "https://arxiv.org/html/2412.14959v1"
          },
          {
            "title": "Temporal Predictors of Outcome in Reasoning Language Models",
            "url": "https://arxiv.org/pdf/2511.14773"
          },
          {
            "title": "Self-correction is Not An Innate Capability in Language Models",
            "url": "https://arxiv.org/pdf/2410.20513"
          },
          {
            "title": "Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification",
            "url": "https://arxiv.org/html/2504.05419v1"
          },
          {
            "title": "Intrinsic Self-correction for Enhanced Morality: An Analysis of Internal   Mechanisms and the Superficial Hypothesis",
            "url": "https://arxiv.org/pdf/2407.15286"
          },
          {
            "title": "Latent Space Chain-of-Embedding Enables Output-free LLM Self-Evaluation",
            "url": "https://arxiv.org/pdf/2410.13640"
          },
          {
            "title": "Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/pdf/2512.20578"
          }
        ]
      },
      "Based on the search results, here are relevant papers and findings related to LLM self-correction, gating, probing, correctability, and hidden states:\n\n## Key Papers Found:\n\n1. **Understanding the Dark Side of LLMs' Intrinsic Self-Correction** (December 2024)\n   Uses a binary classification probing experiment with tuned lens to probe LLM's internal token representations at each layer. This allows tracking of LLM's internal answer evolution by computing the difference of confidence score between correct and incorrect answers.\n\n2. **Temporal Predictors of Outcome in Reasoning Language Models** (2025)\n   Predicts answer correctness directly from an LLM's hidden state while the chain-of-thought is being generated, not only after initial question or the final answer. Shows that hidden states from very short prefixes already contain linearly decodable information about eventual correctness, reaching AUCs up to 0.8+ on MATH-like data.\n\n3. **Self-correction is Not An Innate Capability in Language Models** (2024)\n   Conducts a mechanistic analysis of the hidden states to examine how key components of self-correction, such as Chain-of-Thought and external feedback, interact to facilitate moral self-correction.\n\n4. **Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification** (April 2025)\n   Focuses on probing hidden states to verify intermediate answers during reasoning chains.\n\n5. **Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits** (December 2025)\n   Proposes Gnosis, which taps hidden states and attention maps from a frozen LLM and predicts a scalar correctness score.\n\nThese papers address selective correction based on correctability prediction from hidden states, which aligns with your query about gating mechanisms for self-correction."
    ],
    "durationSeconds": 7.831752800000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "03ca58f0-04ed-465d-bf68-1b69f3862293",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T18:56:58.339Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016zbNwKsEDNKMsjpbchv3eT`</summary>

```json
{
  "query": "CoRefine confidence-guided self-refinement arXiv 2602.08948 three-way routing self-correction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6737bddb-25cd-4964-bf9f-1c977f48c337",
  "isSidechain": false,
  "requestId": "req_011CbCSNzGA2cqfoBURA9gZb",
  "type": "assistant",
  "uuid": "08461341-563d-444a-8f84-7bdc5314b868",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bgfm22dp1boim5cJPniKvn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 27891,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 847,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 27891,
          "cache_creation_input_tokens": 847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 847
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

_source line 25 · 2026-05-19T18:57:05.868Z_

<details><summary>↩ Tool result · `toolu_016zbNwKsEDNKMsjpbchv3eT`</summary>

```text
Web search results for query: "CoRefine confidence-guided self-refinement arXiv 2602.08948 three-way routing self-correction"

Links: [{"title":"[2602.08948] CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute","url":"https://arxiv.org/abs/2602.08948"},{"title":"CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute","url":"https://arxiv.org/pdf/2602.08948"},{"title":"Confidence-aware Adversarial Learning for Self-supervised Semantic   Matching","url":"https://arxiv.org/pdf/2008.10902"},{"title":"Self-Refinement of Language Models from External Proxy Metrics Feedback","url":"https://arxiv.org/pdf/2403.00827"},{"title":"A Stitch in Time Saves Nine: Proactive Self-Refinement for Language Models","url":"https://arxiv.org/pdf/2508.12903"},{"title":"Toward More Reliable Artificial Intelligence: Reducing Hallucinations in Vision-Language Models","url":"https://arxiv.org/pdf/2512.07564"}]

Based on the search results, here's what I found about CoRefine:

CoRefine is a confidence-guided self-refinement method that achieves competitive accuracy using a fraction of the tokens via a lightweight 211k-parameter Conv1D controller atop a frozen LLM.

The three-way routing you mentioned is reflected in the system's decision mechanism: The controller consumes full-trace confidence features of the LLM decoded reasoning chain and decides: HALT (accept current answer), RETHINK (verify reasoning), or ALTERNATIVE (explore new approach).

The controller enables targeted self-correction with an average of 2.7 refinement steps per problem and roughly 190-fold token reduction relative to 512-sample baselines. Additionally, token savings translate to actual latency reduction, with CoRefine saving up to 63% over parallel baselines.

This represents an adaptive test-time compute approach where the system intelligently decides whether to continue with the current answer, reconsider the reasoning, or try an entirely different approach based on confidence signals in the reasoning process.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08461341-563d-444a-8f84-7bdc5314b868",
  "isSidechain": false,
  "promptId": "8256411a-5d7a-47b0-8825-6efc21691ae1",
  "type": "user",
  "uuid": "c256ec82-72aa-401a-8de8-48197abee901",
  "toolUseResult": {
    "query": "CoRefine confidence-guided self-refinement arXiv 2602.08948 three-way routing self-correction",
    "results": [
      {
        "tool_use_id": "srvtoolu_017WXBCcihiZtJgnxcV9Pd58",
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
      "Based on the search results, here's what I found about CoRefine:\n\nCoRefine is a confidence-guided self-refinement method that achieves competitive accuracy using a fraction of the tokens via a lightweight 211k-parameter Conv1D controller atop a frozen LLM.\n\nThe three-way routing you mentioned is reflected in the system's decision mechanism: The controller consumes full-trace confidence features of the LLM decoded reasoning chain and decides: HALT (accept current answer), RETHINK (verify reasoning), or ALTERNATIVE (explore new approach).\n\nThe controller enables targeted self-correction with an average of 2.7 refinement steps per problem and roughly 190-fold token reduction relative to 512-sample baselines. Additionally, token savings translate to actual latency reduction, with CoRefine saving up to 63% over parallel baselines.\n\nThis represents an adaptive test-time compute approach where the system intelligently decides whether to continue with the current answer, reconsider the reasoning, or try an entirely different approach based on confidence signals in the reasoning process."
    ],
    "durationSeconds": 7.524250651000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "08461341-563d-444a-8f84-7bdc5314b868",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-19T18:57:09.100Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012XoYCPSP9CmxTYNeJJsWEk`</summary>

```json
{
  "query": "CoRL 2026 conference topics scope robot learning submission guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c256ec82-72aa-401a-8de8-48197abee901",
  "isSidechain": false,
  "requestId": "req_011CbCSPjs1SRdpa9KyboJJJ",
  "type": "assistant",
  "uuid": "dfbaac34-d0a5-4af4-8036-fde2b852b6eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0197LdFmMNpx7XG24D47Jjgt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 635,
      "cache_read_input_tokens": 28738,
      "output_tokens": 64,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 635,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 64,
          "cache_read_input_tokens": 28738,
          "cache_creation_input_tokens": 635,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 635
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

_source line 27 · 2026-05-19T18:57:18.012Z_

<details><summary>↩ Tool result · `toolu_012XoYCPSP9CmxTYNeJJsWEk`</summary>

```text
Web search results for query: "CoRL 2026 conference topics scope robot learning submission guidelines"

Links: [{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf"}]

Based on the search results, here's comprehensive information about CoRL 2026 conference topics, scope, and submission guidelines:

## Conference Overview

The Conference on Robot Learning (CoRL) is an annual international conference aiming to bring together the robotics and machine learning research communities and focuses on the increasingly important role of learning in robotics and its interaction with other areas of robotics.

## Topics and Scope

The aim of CoRL 2026 is to publish significant original research at the intersection of robotics and machine learning. CoRL welcomes papers in areas such as: Learning representations for robotic perception and control · Learning robot foundation models or general-purpose knowledge systems for robotics · Imitation learning for robotics, e.g. by behavioral cloning and/or inverse reinforcement learning · Reinforcement learning for control of physical robots, as well as video models and latent world models for robot learning.

## Key Submission Requirements

- **Format**: Papers are limited to 8 pages of content plus unlimited references.
- **Robotics Focus**: Submissions without a robotics focus will be returned without review.
- **Real-Robot Emphasis**: Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.
- **Limitations Section**: All submissions should include a Limitations section, explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments and how these might be addressed in the future.
- **Supplementary Materials**: Authors are also encouraged to submit video, code and data as supplementary materials.

## Reviewer Requirements

All submissions must include at least one author who agrees to serve as a CoRL reviewer.

## Important Deadlines

The paper submission deadline is May 29, 2026. CoRL 2026 will be held in Austin, Texas, US.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfbaac34-d0a5-4af4-8036-fde2b852b6eb",
  "isSidechain": false,
  "promptId": "8256411a-5d7a-47b0-8825-6efc21691ae1",
  "type": "user",
  "uuid": "b7bc3812-309a-486a-83c9-df3a5881e527",
  "toolUseResult": {
    "query": "CoRL 2026 conference topics scope robot learning submission guidelines",
    "results": [
      {
        "tool_use_id": "srvtoolu_017867wcbRLFeQ3sft6nnDU1",
        "content": [
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "CoRL 2026 - Instruction for Authors",
            "url": "https://www.corl.org/contributions/instruction-for-authors"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "CoRL 2026 Conference | OpenReview",
            "url": "https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"
          },
          {
            "title": "CoRL 2026 - Call for Workshops",
            "url": "https://www.corl.org/contributions/call-for-workshops"
          },
          {
            "title": "CoRL LaTeX Template | Robot Learning Conference Format | Underleaf",
            "url": "https://www.underleaf.ai/templates/corl"
          },
          {
            "title": "CoRL 2026 - Contributions",
            "url": "https://www.corl.org/contributions"
          },
          {
            "title": "Robot Learning Foundation",
            "url": "https://www.robot-learning.org/"
          },
          {
            "title": "Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"
          },
          {
            "title": "Conference on Robot Learning (@corl_conf) / Posts / X",
            "url": "https://x.com/corl_conf"
          }
        ]
      },
      "Based on the search results, here's comprehensive information about CoRL 2026 conference topics, scope, and submission guidelines:\n\n## Conference Overview\n\nThe Conference on Robot Learning (CoRL) is an annual international conference aiming to bring together the robotics and machine learning research communities and focuses on the increasingly important role of learning in robotics and its interaction with other areas of robotics.\n\n## Topics and Scope\n\nThe aim of CoRL 2026 is to publish significant original research at the intersection of robotics and machine learning. CoRL welcomes papers in areas such as: Learning representations for robotic perception and control · Learning robot foundation models or general-purpose knowledge systems for robotics · Imitation learning for robotics, e.g. by behavioral cloning and/or inverse reinforcement learning · Reinforcement learning for control of physical robots, as well as video models and latent world models for robot learning.\n\n## Key Submission Requirements\n\n- **Format**: Papers are limited to 8 pages of content plus unlimited references.\n- **Robotics Focus**: Submissions without a robotics focus will be returned without review.\n- **Real-Robot Emphasis**: Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.\n- **Limitations Section**: All submissions should include a Limitations section, explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments and how these might be addressed in the future.\n- **Supplementary Materials**: Authors are also encouraged to submit video, code and data as supplementary materials.\n\n## Reviewer Requirements\n\nAll submissions must include at least one author who agrees to serve as a CoRL reviewer.\n\n## Important Deadlines\n\nThe paper submission deadline is May 29, 2026. CoRL 2026 will be held in Austin, Texas, US."
    ],
    "durationSeconds": 8.906439337999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "dfbaac34-d0a5-4af4-8036-fde2b852b6eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-19T18:57:25.526Z_

<details><summary>Logged reasoning block</summary>

```text
This is very important. CoRL 2026 explicitly states: "Submissions without a robotics focus will be returned without review." This proposal is entirely about LLM internal representations and self-correction - it has absolutely zero robotics content. This is a fatal venue mismatch.

Let me also search for one more thing to complete my literature review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7bc3812-309a-486a-83c9-df3a5881e527",
  "isSidechain": false,
  "requestId": "req_011CbCSQdrsrnSp93wbUcQVX",
  "type": "assistant",
  "uuid": "ea1a1ed3-28f4-42f8-9eae-5653669dbb50",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMJC4oaMsdEB41eBwJ8ia6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 886,
      "cache_read_input_tokens": 29373,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 886,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 29373,
          "cache_creation_input_tokens": 886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 886
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

_source line 29 · 2026-05-19T18:57:26.201Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G8BAddipKUcwN6ACqNHKup`</summary>

```json
{
  "query": "\"correctability prediction\" LLM probe self-correction selective gating 2026 hidden state"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea1a1ed3-28f4-42f8-9eae-5653669dbb50",
  "isSidechain": false,
  "requestId": "req_011CbCSQdrsrnSp93wbUcQVX",
  "type": "assistant",
  "uuid": "05f48520-779b-4e3f-aa55-6ef814a94727",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMJC4oaMsdEB41eBwJ8ia6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 886,
      "cache_read_input_tokens": 29373,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 886,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 29373,
          "cache_creation_input_tokens": 886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 886
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

_source line 30 · 2026-05-19T18:57:34.006Z_

<details><summary>↩ Tool result · `toolu_01G8BAddipKUcwN6ACqNHKup`</summary>

```text
Web search results for query: ""correctability prediction" LLM probe self-correction selective gating 2026 hidden state"

Links: [{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"},{"title":"Learning self-evaluation to improve selective prediction in LLMs","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12536388"},{"title":"Towards Reliable LLM Grading Through Self-Consistency and Selective Human Review: Higher Accuracy, Less Work","url":"https://www.mdpi.com/2504-4990/8/3/74"},{"title":"No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes","url":"https://arxiv.org/pdf/2509.10625"},{"title":"Adaptation with Self-Evaluation to Improve Selective Prediction in LLMs","url":"https://arxiv.org/pdf/2310.11689"},{"title":"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/pdf/2512.20578"},{"title":"Confidence v.s. Critique: A Decomposition of Self-Correction Capability   for LLMs","url":"https://arxiv.org/pdf/2412.19513"}]

I found several relevant papers on correctability prediction, self-correction, and hidden state analysis in LLMs from 2024-2026. Here are the key findings:

**Recent Research on Correctability Prediction:**

Recent work advances understanding of how LLMs encode self-assessment, providing evidence for a general "Factual Correctness" direction while highlighting structural distinctness of reasoning capabilities, with research available on GitHub examining question-only linear probes.

**Hidden State Analysis for Error Detection:**

Hidden activations diverge between correct and hallucinated outputs, with factuality cues concentrated in middle/deep layers yet sensitive to domain shift. Additionally, token-wise hidden-state entropy and information density can outperform perplexity-based failure prediction.

**Confidence Representation and Self-Correction:**

LLMs cache a confidence representation at a token immediately following the answer (post-answer newline: PANL) that causally drives verbal confidence and dissociates from log-probabilities. Research tests whether this PANL signal supports error detection and self-correction, deriving predictions from the second-order framework.

**Linear Probe Approaches:**

A complementary line trains simple probes (shallow MLPs) on final-token states, though these approaches consistently yield low accuracy across diverse benchmarks.

These recent papers explore the intersection of correctability prediction, probing mechanisms, and self-correction capabilities in modern LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05f48520-779b-4e3f-aa55-6ef814a94727",
  "isSidechain": false,
  "promptId": "8256411a-5d7a-47b0-8825-6efc21691ae1",
  "type": "user",
  "uuid": "591bf81d-09e6-4f6e-a2dd-a26b25af0c0b",
  "toolUseResult": {
    "query": "\"correctability prediction\" LLM probe self-correction selective gating 2026 hidden state",
    "results": [
      {
        "tool_use_id": "srvtoolu_011TD6E1f7SdFDTwAFqP23sy",
        "content": [
          {
            "title": "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs",
            "url": "https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"
          },
          {
            "title": "Learning self-evaluation to improve selective prediction in LLMs",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12536388"
          },
          {
            "title": "Towards Reliable LLM Grading Through Self-Consistency and Selective Human Review: Higher Accuracy, Less Work",
            "url": "https://www.mdpi.com/2504-4990/8/3/74"
          },
          {
            "title": "No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes",
            "url": "https://arxiv.org/pdf/2509.10625"
          },
          {
            "title": "Adaptation with Self-Evaluation to Improve Selective Prediction in LLMs",
            "url": "https://arxiv.org/pdf/2310.11689"
          },
          {
            "title": "Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/pdf/2512.20578"
          },
          {
            "title": "Confidence v.s. Critique: A Decomposition of Self-Correction Capability   for LLMs",
            "url": "https://arxiv.org/pdf/2412.19513"
          }
        ]
      },
      "I found several relevant papers on correctability prediction, self-correction, and hidden state analysis in LLMs from 2024-2026. Here are the key findings:\n\n**Recent Research on Correctability Prediction:**\n\nRecent work advances understanding of how LLMs encode self-assessment, providing evidence for a general \"Factual Correctness\" direction while highlighting structural distinctness of reasoning capabilities, with research available on GitHub examining question-only linear probes.\n\n**Hidden State Analysis for Error Detection:**\n\nHidden activations diverge between correct and hallucinated outputs, with factuality cues concentrated in middle/deep layers yet sensitive to domain shift. Additionally, token-wise hidden-state entropy and information density can outperform perplexity-based failure prediction.\n\n**Confidence Representation and Self-Correction:**\n\nLLMs cache a confidence representation at a token immediately following the answer (post-answer newline: PANL) that causally drives verbal confidence and dissociates from log-probabilities. Research tests whether this PANL signal supports error detection and self-correction, deriving predictions from the second-order framework.\n\n**Linear Probe Approaches:**\n\nA complementary line trains simple probes (shallow MLPs) on final-token states, though these approaches consistently yield low accuracy across diverse benchmarks.\n\nThese recent papers explore the intersection of correctability prediction, probing mechanisms, and self-correction capabilities in modern LLMs."
    ],
    "durationSeconds": 7.799411422999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "05f48520-779b-4e3f-aa55-6ef814a94727",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-19T18:57:34.035Z_

```json
{
  "parentUuid": "591bf81d-09e6-4f6e-a2dd-a26b25af0c0b",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "03b4742a-9440-45fa-ad73-969c7fe974e7",
  "timestamp": "2026-05-19T18:57:34.035Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-19T18:58:06.589Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to make my assessment. Let me synthesize everything.

Key observations:

1. **VENUE MISMATCH - FATAL**: CoRL 2026 explicitly states "Submissions without a robotics focus will be returned without review." This proposal is entirely about LLM internal representations, probing, self-correction, and representational geometry - it has ZERO robotics content. This is not a borderline case; this is a complete mismatch. The paper would be desk-rejected without review.

2. **Idea Quality Analysis**:
   - The core idea is about improving correctability prediction from LLM hidden states using multi-signal probes, and using this for selective self-correction gating with genuine abstention.
   - I'm verifying the cited papers - the PANL baseline establishing 0.614 AUROC, the multi-layer ensembling work showing strong deception detection gains, the SAE dissociation paper, and CoRefine all check out as real work.

3. **Novelty Assessment**:
   - The fundamental novelty claim - that correctability is a distinct prediction target from correctness itself - was already established by PANL. This proposal is essentially an incremental improvement on that existing framework rather than a novel conceptual contribution.
   - The techniques being combined are all borrowed from prior work: multi-layer ensembling, attention entropy metrics, and SAE-guided features each come from different papers. While applying them together to correctability hasn't been done before, the individual components aren't novel.
   - The three-way gating mechanism with abstention is a reasonable addition but not particularly innovative - CoRefine already implements three-way routing, and probe-based gating appears in several existing papers.

4. **Trivial Alternative Check**:
   - CoRefine already achieves 92.6% halt precision using just a simple output-level confidence controller, so the proposal needs to demonstrate that hidden-state probes actually provide meaningful advantages over this simpler baseline.
   - Simple confidence thresholding approaches like Reflective Confidence already work well, though the proposal does include these as baselines for comparison.

5. **Significance**:
   - The core question about predicting correctable errors is practically important for real-world LLM deployment, but the actual impact hinges on whether the probe improvements are substantial enough to justify the added complexity.

6. **Concerns**:
   - This reads like a research agenda rather than a focused paper - it's overly elaborate and tries to do too much at once.
   - The "robust to negative results" framing suggests some uncertainty about whether the main claims will hold up.
   - The venue choice is fundamentally misaligned. CoRL explicitly rejects submissions without robotics focus, and this proposal has nothing to do with robotics.

The venue mismatch is actually a fatal flaw - this would have essentially zero acceptance probability at CoRL regardless of idea quality. That said, evaluating the idea on its own merits for an appropriate venue like NeurIPS or ICML, I should focus on the core claim's logical strength, the genuine novelty, and the importance of the research question itself, setting aside execution-level concerns about experimental design and feasibility.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03b4742a-9440-45fa-ad73-969c7fe974e7",
  "isSidechain": false,
  "requestId": "req_011CbCSRpKwdUPEF1Er711AQ",
  "type": "assistant",
  "uuid": "74886ba0-bcc6-488e-aaf7-4768ab2dea89",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T4h8QBPwpEoy7pqpoJZTGN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 991,
      "cache_read_input_tokens": 30259,
      "output_tokens": 4875,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 991,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4875,
          "cache_read_input_tokens": 30259,
          "cache_creation_input_tokens": 991,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 991
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

_source line 33 · 2026-05-19T18:59:29.313Z_

Now I have enough information. Let me compile my assessment.

---

```
【阶段】: Triage

⚠️ 【致命前置问题：投稿会议不匹配】
CoRL (Conference on Robot Learning) 2026 官网明确声明：
"Submissions without a robotics focus will be returned without review."
本 proposal 的内容（LLM 内部表征探针、自我纠错门控、SAE 特征分解）100% 是纯 NLP/ML 机制研究，
与机器人学习完全无关。无论 idea 质量如何，投稿 CoRL 将被直接 desk reject，概率为 0%。
适合的会议：NeurIPS / ICML / ICLR / ACL / EMNLP。
以下评估基于假设投稿到合适的 ML/NLP 主会（如 NeurIPS 2026），以评价 idea 本身的质量。

【领域调研】:
- [arXiv:2604.22271] "How LLMs Detect and Correct Their Own Errors" (2026):
  建立了 PANL (Post-Answer NewLine) correctability 信号的概念，单层线性探针在 own-generated errors 上达到 0.614 AUROC。
  这是本 proposal 最直接的前序工作——本 proposal 本质上是在这篇论文的基础上做"探针方法升级"。

- [arXiv:2604.13386] "Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling" (2026):
  多层集成探针在欺骗检测上将 AUROC 从 0.510 提升到 0.910（+78%）。
  但该结果特定于 deception detection，是否可迁移到 correctability 是未验证假设。

- [arXiv:2604.19974] "Are LLM Uncertainty and Correctness Encoded by the Same Features?" (2026):
  用 SAE 分解出 pure uncertainty / pure incorrectness / confounded 三类特征，发现 68% 的 pure incorrectness 特征因果无效。
  proposal 将其引入 correctability 分析是合理的延伸，但属于"应用已有框架到新场景"。

- [arXiv:2602.08948] "CoRefine" (2026):
  已实现三路路由（halt/rethink/alternative），用 211K 参数 Conv1D 控制器在 output-level confidence 上运作，92.6% halt precision。
  proposal 的核心差异化点是用 hidden-state 探针替代 output-level confidence + 加入 genuine abstention。

- [arXiv:2512.20578] "Gnosis" (2025):
  多信号融合在 correctness prediction 上达到 0.80–0.95 AUROC。
  proposal 的多信号探针设计（多层+多 token+attention 熵）与 Gnosis 的方法论高度相似，只是目标从 correctness 切换到 correctability。

- [arXiv:2504.05419] "Reasoning Models Know When They're Right" (2025):
  用 hidden-state 探针做 early exit，AUROC 0.77–0.91（针对 correctness）。

- [arXiv:2602.08159] "The Confidence Manifold" (2026):
  correctness 仅需 3-8 维、25 个样本即可线性分离。Proposal 想测试 correctability 是否也有类似结构。

- 调研总结: correctability prediction 作为一个 distinct target（区分于 correctness/error detection）是由 PANL 论文刚刚建立的概念（2026年4月）。
  本 proposal 的定位是"用更强的探针方法论提升 correctability AUROC + 将其用于三路门控"。
  核心方法论组件（多层集成、多 token、attention 熵、SAE 引导）均来自已有工作，proposal 的贡献主要在于"组合 + 应用到新目标"。

【Trivial Alternative 检验】:
存在明显的 trivial alternative 威胁：
1. CoRefine 的 output-level confidence 已经实现了 92.6% halt precision 的三路路由。
   Proposal 需要证明 hidden-state 探针比 output-level confidence 好多少——如果提升有限（如 2-3 个 AUROC 点），
   那付出的额外复杂度（多层提取、SAE 训练、探针训练）是否值得？
2. 简单的 confidence thresholding（如 Reflective Confidence 的 logprob 阈值方法）在 AIME 2025 上达到 83.3%。
3. 核心问题：如果 correctability 作为一个内部信号本身就很弱（PANL 论文显示只有 0.614），
   那更好的探针可能只是从 0.614 提升到 0.70-0.75——这个增量是否足以让 probe-gated correction 真正优于简单 confidence baseline？
   Proposal 自己也承认 "whether similar gains transfer... is an open empirical question"。

增量价值在于：如果能证明 hidden-state probes 确实能可靠区分 correctable vs. uncorrectable errors（而 output-level confidence 不能），
这在理论上有意义。但这个 "如果" 本身就是最大的不确定性。

【前提假设检验】:
核心 claim 的逻辑链中有几个未验证的关键假设：

1. **"correctability 是可被探针捕获的信号"假设**：PANL 论文的 0.614 AUROC 仅略高于随机（0.5）。
   这可能意味着 correctability 根本就不是一个在 hidden states 中有强编码的属性——
   也许模型内部根本没有"我能纠正这个错误"的稳定表征。
   Proposal 假设 0.614 是因为探针方法太弱，但另一个同样合理的解释是：信号本身就很弱。

2. **"多层集成从 deception 迁移到 correctability"假设**：deception detection 和 correctability 是根本不同的任务。
   Deception 有明确的"模型知道真相但选择说谎"的编码模式；
   correctability 则取决于模型的知识覆盖、推理路径可达性等更复杂的因素。
   Proposal 用 Phase 0 测试这个假设是好的实验设计，但如果结果是 negative，
   整个 Phase 1 的方法论基础就塌了。

3. **"confounded features 是 correctability 的有效基底"假设**：
   arXiv:2604.19974 的 confounded features 发现是关于 uncertainty × correctness 的关系，
   而 correctability 是一个更高阶的概念（涉及纠错机制的可达性）。
   从"uncertainty-correctness confounded features"到"correctability prediction"的跳跃缺乏理论支撑。

4. **"genuine abstention 优于 CoRefine 的 ALTERNATIVE"假设**：
   在实际应用中，"尝试另一种方法"（CoRefine 的 ALTERNATIVE）可能比"直接放弃"（abstention）更有价值。
   Proposal 预设 abstention 是更好的策略，但这取决于具体应用场景。

【3 维度打分】:

1. Novelty: 弱-中 —
   - 核心概念"correctability as distinct from correctness"已由 PANL 论文（2604.22271）建立
   - 探针方法论的每个组件都是从已有工作借鉴：多层集成（2604.13386）、attention 熵（2602.13699）、SAE 引导（2604.19974）、多 token（PANL 论文自己的 causal analysis）
   - 三路门控已由 CoRefine（2602.08948）实现，差异在于信号源（hidden-state vs. output-level）和 abstention
   - 真正的 novelty delta 在于"组合这些技术应用于 correctability + SAE 分解分析 correctability 的表征结构"——这是一个有效但较薄的 novelty
   - Phase 3b 的 representational geometry 分析如果做好可以是不错的贡献，但本质上仍然是"将已有分析框架应用到新目标"

2. Significance: 中 —
   - 研究问题本身有意义：理解哪些错误可以被自我纠正是 LLM 部署中的真实需求
   - 但实际影响力受限于：(a) 如果信号本身就弱，实际可部署性很低；(b) 需要多层 hidden state 提取的方案在实际推理中成本很高；(c) 纯 confidence-based 方法已经相当有效
   - Phase 3b 的表征分析可能有较好的科学贡献（理解 second-order properties 的编码方式），但其影响力取决于发现是否 surprising
   - 如果核心发现是 "correctability 需要更高维度/非线性边界"，审稿人可能会说 "I would have guessed this"——因为更高阶的属性需要更复杂的表征是直觉上预期的

3. Related Work: 强 —
   - 相关工作覆盖非常全面，差异化定位清晰
   - 与 CoRefine 的三重区分（信号源、abstention、correctability-aware）描述准确
   - 对每篇引用工作的局限性分析到位（如 Gnosis 的 ablation 仅在 Qwen3-1.7B 上、多层集成的 deception-specific 性质）
   - 唯一的小问题：对四篇 concurrent probe-gating 论文的总结有点快速，可以更深入地分析与本工作的区别

【概率估计】: [15% - 30%] 中位 22%
（注意：此概率是假设投稿到 NeurIPS/ICML 等合适会议。投稿 CoRL 的概率为 ~0%，会被 desk reject。）

【估计理由】:
- Novelty 维度限制了上界：核心是"已有探针技术的组合应用于一个刚被提出的新目标"，审稿人可能会评价为 incremental combination
- Significance 处于中等：研究问题有价值，但核心发现（无论 positive 还是 negative）不太可能是 surprising。如果探针提升到 0.75 AUROC，审稿人可能说 "expected improvement from better probing"；如果 plateau 在 0.65，Phase 3b 的表征分析虽有趣但 impact 有限
- Related Work 是该 proposal 最强的维度，但好的 related work 覆盖不能弥补 novelty 的不足
- Proposal 过于 kitchen-sink：4 个 phase + 6 种探针变体 + 8 个 baseline + SAE 分析 + 表征几何 + error depth，试图在一篇论文中做太多事情，这本身可能被审稿人视为缺乏聚焦
- "Robust to negative results" 设计虽然是好的学术实践，但也暗示作者自己对核心 claim 的信心不足

【主要风险】:
1. **信号天花板风险**：correctability 可能在 hidden states 中根本就没有强编码——0.614 AUROC 可能不是探针方法的问题，而是信号本身的问题。如果增强探针只能把 AUROC 提到 0.68-0.72，整个 gating 框架的实用价值存疑，论文会变成"我们用了很多技术但提升有限"的 negative result + 分析论文
2. **Novelty 薄弱风险**：审稿人可能认为这是"将一堆已有的探针改进技术套用到一个新定义的预测目标上"——方法层面无新意，目标层面由 PANL 论文已经定义，组合本身不构成充分的 novelty

⚠️ 再次强调：如果目标确实是 CoRL 2026，请立即更换投稿会议。这个 proposal 与 robot learning 完全无关，会被 desk reject。
```

Sources:
- [How LLMs Detect and Correct Their Own Errors (arXiv:2604.22271)](https://arxiv.org/html/2604.22271v1)
- [Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling (arXiv:2604.13386)](https://arxiv.org/abs/2604.13386)
- [Are LLM Uncertainty and Correctness Encoded by the Same Features? (arXiv:2604.19974)](https://arxiv.org/abs/2604.19974)
- [CoRefine: Confidence-Guided Self-Refinement (arXiv:2602.08948)](https://arxiv.org/abs/2602.08948)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [Reasoning Models Know When They're Right (arXiv:2504.05419)](https://arxiv.org/html/2504.05419v1)
- [Can LLMs Predict Their Own Failures? Gnosis (arXiv:2512.20578)](https://arxiv.org/pdf/2512.20578)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74886ba0-bcc6-488e-aaf7-4768ab2dea89",
  "isSidechain": false,
  "requestId": "req_011CbCSRpKwdUPEF1Er711AQ",
  "type": "assistant",
  "uuid": "1c069373-2380-46ad-b4de-edc83a895e47",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T4h8QBPwpEoy7pqpoJZTGN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 991,
      "cache_read_input_tokens": 30259,
      "output_tokens": 4875,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 991,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4875,
          "cache_read_input_tokens": 30259,
          "cache_creation_input_tokens": 991,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 991
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "1c069373-2380-46ad-b4de-edc83a895e47",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Predict LLM error correctability with enhanced probes",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "1c069373-2380-46ad-b4de-edc83a895e47",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Predict LLM error correctability with enhanced probes",
  "sessionId": "b45d5360-28f0-406a-af8b-d7e8e5f62908"
}
```

---
