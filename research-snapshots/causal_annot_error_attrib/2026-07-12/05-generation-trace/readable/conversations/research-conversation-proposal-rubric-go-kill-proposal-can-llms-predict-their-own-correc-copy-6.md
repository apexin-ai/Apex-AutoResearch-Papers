# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Can LLMs Predict Their Own Correc

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/c850925d-dde6-4896-9e34-cafecb7b59ba.jsonl`
- **Structured JSON:** [`01cb08a338ba40670213.json`](../../sessions/01/01cb08a338ba40670213.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T21:12:35.709Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T21:12:35.709Z",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction\n\n## Description\nWe investigate whether LLMs' internal representations can predict which of their errors are self-correctable, and whether this prediction enables selective correction that outperforms both ungated correction, the trivial 'Wait' baseline, and confidence-based routing. Prior work shows a faint correctability signal at the post-answer newline token (PANL) achieving only 0.614 AUROC with a single-layer linear probe — insufficient for reliable gating. We develop Enhanced Correctability Probes (ECP) that combine multi-layer ensemble stacking, multi-token features (PANL + last-answer-token + reasoning tokens), attention-entropy features, pre-Wait hidden-state features (informed by crosscoder analysis of Wait-token mechanisms, arXiv:2510.04128), and SAE-guided feature selection targeting the confounded feature intersection that bridges uncertainty and correctness (motivated by the functional dissociation finding of arXiv:2604.19974, where 68% of pure incorrectness features are causally inert). We begin with a Phase 0 pilot that directly tests whether multi-layer ensembling — which improved deception detection AUROC by up to 78% (arXiv:2604.13386, specifically on Harm-Pressure Knowledge in Llama-70B) — transfers to the fundamentally different task of correctability prediction. These probes gate a three-way decision: retain the original answer (likely correct), attempt correction including probe-selective Wait insertion (error detected, high correctability), or abstain (error detected, low correctability). This framework is distinguished from CoRefine's (arXiv:2602.08948) three-way routing — which uses output-level confidence, lacks genuine abstention, and is not correctability-aware — by using hidden-state probes, providing a genuine abstention option for unfixable errors, and explicitly predicting error fixability rather than confidence. Critically, we provide the first evaluation of the 'Wait' baseline on correct answers, measuring its previously-unknown overcorrection cost. We also conduct the first representational geometry and SAE feature decomposition analysis of correctability vs. correctness, testing whether correctability — a second-order property that depends not just on whether the model is wrong but on whether correction mechanisms can reach the right answer — shares the low-dimensional, linearly-separable structure that correctness exhibits (arXiv:2602.08159), requires higher dimensionality or non-linear boundaries, or depends disproportionately on the narrow confounded feature population identified by arXiv:2604.19974. This analysis, combined with error depth characterization (arXiv:2601.00828) and threshold analysis mapping probe quality to gating utility, ensures publishable contributions even if probe AUROC plateaus at marginal levels. We evaluate across Gemma-3-27B, Qwen-2.5-7B-Instruct, and Mistral-Small-3.2-24B on TriviaQA, MMLU, and GSM8K, comparing against eight baselines including ungated correction, Wait (universal and probe-selective), confidence-based routing (CoRefine-style and Reflective Confidence-style), PAG, and oracle gating. Our contributions are: (1) operationalizing correctability as a prediction target distinct from correctness, (2) the first pilot testing whether multi-layer ensembling transfers from deception to correctability, (3) the first hidden-state probe-based gating with genuine abstention for correctability-aware self-correction — distinguished from CoRefine's confidence-based routing by signal source, abstention capability, and correctability specificity, (4) the first representational geometry and SAE feature decomposition comparison of correctability vs. correctness, testing whether second-order properties have a different confounded-feature signature than first-order properties, and (5) establishing the conditions — including minimum probe quality thresholds — under which probe-gated correction outperforms simpler alternatives including confidence-based controllers.\n\n## Core Problem\nLLMs attempt correction on all detected errors equally, but ~64.5% of self-generated errors are uncorrectable. Recent work reveals a faint internal 'correctability' signal at the post-answer newline token (PANL), but it achieves only 0.614 AUROC on own-generated errors using a single-layer linear probe — barely actionable for reliable gating. Meanwhile, trivial interventions like appending 'Wait' reduce blind spots by 89.3% on known errors, but their overcorrection rate on correct answers is completely untested. Confidence-based controllers like CoRefine (arXiv:2602.08948) achieve efficient three-way routing (halt/rethink/explore-alternative) using output-level logprobs, but they do not distinguish between correctable and uncorrectable errors — treating all detected issues as potentially fixable. Critically, correctability is a second-order property — it depends not just on whether the model is wrong, but on whether the model's correction mechanism can reach the right answer — and recent SAE analysis (arXiv:2604.19974) reveals that uncertainty and correctness are encoded by functionally distinct feature populations, with only rare 'confounded' features bridging both signals. It is unknown whether correctability — which inherently requires engaging both axes — shares the favorable geometric properties (low dimensionality, linear separability) that correctness exhibits, or whether it requires targeting the narrow confounded feature intersection. Can enhanced multi-signal probes substantially improve correctability prediction, what is the representational relationship between correctability, correctness, and uncertainty at the feature level, and under what conditions does probe-gated correction with genuine abstention outperform both ungated correction and simpler confidence-based alternatives?\n\n## Opportunity\nThree converging findings create a clear research opportunity: (1) The PANL paper (arXiv:2604.22271) establishes that correctability is partially encoded in internal representations, but their single-layer, single-token linear probe barely exceeds chance (0.614 AUROC) on own-generated errors — leaving substantial room for improvement. For correctness prediction on adjacent tasks, Gnosis-style multi-signal fusion (arXiv:2512.20578) achieves 0.78–0.92 AUROC on hidden states alone (with the lower end on MMLU-Pro; ablation on Qwen3-1.7B only) and 0.80–0.95 with attention fusion, while attention-head entropy probes (arXiv:2602.13699) achieve +0.06 AUROC absolute improvement in OOD settings (0.70→0.76 average, 8.5% relative vs. Lookback Lens). Multi-layer probe ensembling (arXiv:2604.13386) has dramatically improved deception detection AUROC (0.510→0.910 on Harm-Pressure Knowledge in Llama-70B), though whether similar gains transfer to correctability — a fundamentally different property — is an open empirical question that motivates our pilot experiment. (2) The 'Wait' baseline from Self-Correction Bench (arXiv:2507.02778) is powerful but fundamentally non-selective: it was tested only on known errors, never on correct answers, so its overcorrection cost is unknown. QwQ-32B naturally generates 'Wait' as its first correction token 37.7–76.8% of the time depending on benchmark (SCLI5 to PRM800K-SC), but this behavior varies widely across models and is near-zero for non-reasoning models. Recent mechanistic work shows that internal states before Wait tokens causally modulate distinct reasoning patterns — restarting, recalling, uncertainty expression, and double-checking (arXiv:2510.04128, EMNLP 2025 Findings) — and that Wait token probabilities correlate with reasoning correctness in ways that vary by training strategy (arXiv:2601.17421). These findings suggest Wait's effectiveness is not uniform but depends on which reasoning pattern it triggers, creating an opportunity for probe-selective application. Reflective Confidence (arXiv:2512.18605) demonstrates a related approach, transforming low-confidence output signals into reflection triggers rather than stopping, achieving 83.3% accuracy on AIME 2025 vs. 70.0% for Self-Consistency — but uses only output-level logprobs, not internal representations. (3) Existing gating approaches occupy adjacent niches but leave a clear gap. CoRefine (arXiv:2602.08948) implements three-way routing (halt/rethink/alternative) via a 211K-parameter Conv1D controller on output-level confidence, achieving 92.6% halt precision — but its decisions are confidence-based rather than correctability-aware, and its ALTERNATIVE option explores different approaches rather than genuinely abstaining when errors are likely unfixable. Four concurrent probe-gating papers address correctness, early exit, abstention, or reflection control — but none probe for correctability (whether a specific error is fixable), and none combine hidden-state probes with genuine abstention in a correctability-aware framework. Moreover, the SAE dissociation paper (arXiv:2604.19974) reveals that uncertainty and correctness are encoded by functionally distinct feature populations — with 68% of pure incorrectness features being causally inert and only rare confounded features (102 out of 1,057 in Llama-3.1-8B) bridging both signals to achieve 0.79 AUROC with just 3 features. This finding directly challenges naive linear probing over broad activations and suggests correctability prediction may need to target the narrow confounded feature intersection, motivating our SAE-guided probe design and representational analysis.\n\n## Related Work / Landscape\nThe PANL paper (arXiv:2604.22271) establishes correctability prediction as a distinct task from error detection, achieving 0.986 AUROC for detection but only 0.614 for correctability on own-generated errors using single-layer logistic regression at one token position. This gap — high detectability but low correctability prediction — is the central technical challenge. Gnosis (arXiv:2512.20578) achieves 0.80–0.95 AUROC for correctness prediction by fusing final-layer hidden states with attention-map features via a ~5M-parameter architecture; notably, the hidden-state stream alone achieves 0.78–0.92 AUROC (with the lower end on MMLU-Pro; ablation only reported for Qwen3-1.7B), with attention fusion adding 0–3 points depending on the task. The multi-layer ensembling paper (arXiv:2604.13386) shows that logistic stacking across complementary layers can dramatically improve probe performance — achieving 0.510→0.910 AUROC on the hardest deception detection task (Harm-Pressure Knowledge, Llama-70B) — because informative directions rotate across layers and double-fault analysis reveals complementary error patterns between early and late layers. However, this result is specific to deception detection, which has different layer-wise encoding properties than correctness or correctability; whether analogous gains transfer is an empirical hypothesis we test via a Phase 0 pilot. For correctness prediction specifically, multi-signal approaches show more modest but consistent gains: attention-head entropy probes (arXiv:2602.13699) improve OOD AUROC by +0.06 absolute (0.70→0.76 average across 5 models, an 8.5% relative improvement over Lookback Lens), and perturbation-stability probes (arXiv:2505.21772) add +6 AUROC points via targeted adversarial perturbations to hidden states. SWIFT (arXiv:2505.12225) concatenates all-layer hidden states with learned gating weights to extract token-level quality signals.\n\nThe Self-Correction Bench (arXiv:2507.02778) documents the 64.5% blind spot and shows 'Wait' reduces it by 89.3%. QwQ-32B naturally generates 'Wait' as its first correction token at rates varying by benchmark (37.7% on SCLI5, 72.5% on GSM8K-SC, 76.8% on PRM800K-SC), but this behavior is model-specific — other reasoning models show different patterns and non-reasoning models rarely generate Wait spontaneously. The Wait baseline was never tested on correct answers, leaving the overcorrection cost unknown. Two recent papers provide mechanistic understanding of Wait tokens: arXiv:2510.04128 (EMNLP 2025 Findings) trains crosscoders on DeepSeek-R1-Distill-Llama-8B to identify features that promote or suppress Wait tokens, discovering causal features for distinct reasoning patterns (restarting, recalling, uncertainty expression, double-checking) via activation steering at layer 15; arXiv:2601.17421 systematically analyzes Wait and other discourse tokens across model scales and training strategies, finding that Wait token probabilities correlate with reasoning correctness but that models exploit this signal only partially. Reflective Confidence (arXiv:2512.18605) proposes a related approach, transforming low-confidence output-level logprob signals into reflection triggers rather than early stopping, achieving 83.3% accuracy on AIME 2025 (vs. 70.0% Self-Consistency, K=32) on Qwen3-8B — demonstrating that selective confidence-gated correction can significantly outperform non-selective baselines, though it uses output-level signals rather than internal representations and does not model correctability.\n\nCoRefine (arXiv:2602.08948) is the closest existing system to our three-way gating, implementing halt/rethink/alternative decisions via a 211K-parameter Conv1D controller that consumes output-level confidence traces from the frozen LLM. It achieves 92.6% halt precision, averages 2.7 refinement steps per problem, and reduces tokens ~190× relative to 512-sample baselines on mathematical reasoning benchmarks. However, CoRefine differs from our proposal in three fundamental ways: (a) it uses output-level logprobs rather than hidden-state probes, missing the richer internal signal that PANL demonstrates exists; (b) its HALT decision accepts the current answer — it never genuinely abstains or flags for external intervention when errors are likely unfixable; (c) its routing is confidence-based, not correctability-aware — it cannot distinguish correctable from uncorrectable errors, treating all low-confidence outputs as potentially improvable. Four concurrent probe-gating papers occupy adjacent niches: arXiv:2507.12379 probes for arithmetic errors and selectively re-prompts (only 6–12% of detected errors actually get corrected); arXiv:2504.05419 uses probes for early exit from reasoning chains (AUROC 0.77–0.91 for correctness, not correctability); arXiv:2604.18419 trains value-function probes for dynamic mid-generation abstention; arXiv:2506.12217 uses activation steering to modulate self-reflection frequency. None of these probe for correctability specifically, and none combine hidden-state probes with genuine abstention in a correctability-aware framework.\n\nA critical finding for our probing approach comes from arXiv:2604.19974, which uses sparse autoencoders to decompose LLM representations into functionally distinct feature populations. In Llama-3.1-8B, they identify 700 pure uncertainty features, 255 pure incorrectness features, and only 102 confounded features encoding both signals. The key insight is a functional dissociation: 68% of pure incorrectness features are causally inert (mean accuracy delta of -0.03% when suppressed), while pure uncertainty features are essential for model performance, and only confounded features bridging both axes are causally effective for correctness prediction — with just 3 confounded features from layer 18 achieving 0.79 AUROC. This has direct implications for correctability probing: correctability is inherently a joint uncertainty+correctness concept (the model must be wrong AND the correction mechanism must be able to reach the right answer), so probes targeting broad activation spaces risk relying on functionally inert incorrectness features. This motivates our SAE-guided feature analysis in Phase 3b and suggests that the confounded feature intersection — not the full activation space — may be the effective substrate for correctability prediction, potentially explaining why the single-layer PANL probe achieves only 0.614 AUROC.\n\nThe Confidence Manifold (arXiv:2602.08159) shows correctness occupies only 3–8 dimensions in activation space and is linearly separable with as few as 25 labeled examples. However, correctability is a second-order property: it depends not just on whether the model is wrong, but on whether the model's correction mechanism can reach the right answer given the model's knowledge state and reasoning pathways. The Interpretability-without-Actionability paper (arXiv:2603.18353) provides indirect evidence that this second-order property may be harder to capture: even with 98.2% detection AUROC, activation steering corrected only 20–24% of errors (concept-bottleneck steering) or 0% (SAE feature steering), revealing a 53-percentage-point knowledge-action gap. This suggests correctability may occupy a different — possibly higher-dimensional or non-linear — representational subspace than correctness, and the SAE dissociation finding (arXiv:2604.19974) provides a mechanistic explanation: correctability may require engaging the narrow confounded feature population rather than the broader (but functionally inert) incorrectness features. The Truth-as-a-Trajectory framework (arXiv:2603.01326) proposes that cross-layer displacement vectors capture properties that static single-layer probes miss, potentially relevant to second-order properties like correctability. The Accuracy-Correction Paradox (arXiv:2601.00828) shows weaker models achieve 1.6× higher correction rates and proposes the Error Depth Hypothesis — that stronger models make fewer but deeper errors that resist self-correction — providing a taxonomy of error correctable characteristics. The information-theoretic analysis of correlated errors (Preprints.org 202601.0892) formalizes bounds on self-correction when generator and evaluator share failure modes, motivating external probe-based gating as a mechanism to break the correlation. LLMs also encode problem difficulty as a linearly decodable property (arXiv:2510.18147, ρ ≈ 0.88), suggesting that related meta-cognitive properties may be extractable, though correctability's second-order nature makes direct analogy uncertain.\n\n## Approach\nWe propose a four-phase study of correctability prediction and selective self-correction, including an explicit pilot to validate the multi-layer ensemble transfer hypothesis, SAE-guided feature analysis informed by the uncertainty-correctness dissociation (arXiv:2604.19974), and a contribution plan that is robust to negative results.\n\n**Phase 0: Pilot Feasibility Study.** Before committing to the full experimental pipeline, we run a targeted pilot on the PANL paper's existing correctability labels (Gemma-3-27B, TriviaQA subset). We train independent logistic regression probes at each of the ~42 layers, identify complementary layers via double-fault analysis (following arXiv:2604.13386's methodology), and build a 3–5 layer stacked ensemble. This pilot directly tests whether the multi-layer ensembling technique that improved deception detection AUROC by up to 78% transfers to correctability prediction. Success criterion: if the ensemble achieves ≥0.70 AUROC (meaningful improvement over the 0.614 single-layer baseline), we proceed to Phase 1. If the ensemble plateaus below 0.70, we shift emphasis to the representational geometry and SAE feature analysis (Phase 3b), which remains a publishable contribution. Estimated cost: ~15 H100-hours (single model, single dataset, multi-layer extraction only).\n\n**Phase 1: Enhanced Correctability Probes (ECP).** We move beyond the PANL paper's single-layer, single-token linear probe by developing multi-signal correctability probes. (a) Multi-layer ensemble: train independent logistic regression probes at each layer, select 3–5 complementary layers via double-fault analysis, combine via logistic stacking (following arXiv:2604.13386, but with the explicit caveat that this technique was validated on deception detection — our Phase 0 tests transfer to correctability). (b) Multi-token features: concatenate hidden states from the post-answer newline token (PANL), the last answer token (LAT), and the last 2 reasoning tokens — the PANL paper's own causal analysis shows LAT carries complementary information at different layers. (c) Attention-based features: extract per-head entropy statistics across semantic sections (question, reasoning, answer), following the methodology of arXiv:2602.13699 which achieves +0.06 AUROC absolute improvement over Lookback Lens in OOD correctness prediction. (d) Wait-token features: inspired by the crosscoder analysis of arXiv:2510.04128, extract hidden-state features at the position immediately preceding natural Wait tokens (when present), capturing the causal features that modulate reasoning patterns (restarting, recalling, uncertainty expression, double-checking). The insight from arXiv:2601.17421 that Wait token probabilities correlate with reasoning correctness suggests these features encode meta-cognitive state relevant to correctability. (e) SAE-guided feature selection: motivated by arXiv:2604.19974's finding that only confounded features (encoding both uncertainty and correctness) are causally effective while pure incorrectness features are functionally inert, we train SAEs on our target models and identify confounded features relevant to correctability. We then compare probes trained on (i) full activation spaces, (ii) SAE-reconstructed activations from confounded features only, and (iii) SAE-reconstructed activations excluding pure incorrectness features. This tests whether the narrow confounded feature intersection — rather than broad activations — is the effective substrate for correctability prediction, and whether filtering out causally inert features improves probe AUROC. (f) Non-linear probe ablation: compare linear probes, 2-layer MLPs (hidden dim 16/32), and SWIFT-style all-layer gated aggregation — motivated by the possibility that correctability, as a second-order property, may require non-linear boundaries even if correctness is linearly separable in 3–8 dimensions (arXiv:2602.08159). All probes are trained on on-policy correctability labels generated by running the model's actual self-correction pipeline (multiple correction attempts per error to get calibrated fixability scores), avoiding the distribution mismatch of synthetic error injection documented in SCoRe (arXiv:2409.12917).\n\n**Phase 2: Three-Way Gated Self-Correction.** Use the ECP to implement a three-way decision at inference time: (i) if the error detection probe indicates the answer is likely correct, retain the original answer; (ii) if the error is detected AND the correctability probe predicts high fixability (above a calibrated threshold), attempt correction — either prompting-based correction or probe-selective Wait insertion (applying Wait only when the probe detects both an error and high correctability, leveraging the mechanistic finding from arXiv:2510.04128 that Wait triggers different reasoning patterns depending on internal state); (iii) if the error is detected but correctability is predicted as low, abstain or flag for external intervention. This design is distinguished from CoRefine's (arXiv:2602.08948) three-way routing in three key ways: we use hidden-state probes rather than output-level confidence, our third option is genuine abstention (declining to answer) rather than exploring alternative approaches, and our gating is explicitly correctability-aware — routing based on predicted fixability rather than confidence level. Where CoRefine optimizes compute efficiency (achieving ~190× token reduction), our framework optimizes decision quality by preventing wasted correction attempts on unfixable errors and avoiding overcorrection of correct answers.\n\n**Phase 3: Comprehensive Evaluation.** Evaluate across three dense models where probing is well-understood: Gemma-3-27B (same as PANL paper, validates signal transfer), Qwen-2.5-7B-Instruct (same as PANL paper, smaller scale), and Mistral-Small-3.2-24B (different architecture family, tests generalization). Use three benchmarks (TriviaQA, MMLU, GSM8K) with 10K+ questions each. Compare gated correction against eight baselines: (1) no correction, (2) ungated prompting-based correction, (3) Wait-appended correction applied to all answers — measuring the previously-untested overcorrection rate, (4) Wait-appended correction applied only to probe-detected errors, (5) confidence-threshold gating using log-probabilities (following Reflective Confidence's approach, arXiv:2512.18605), (6) CoRefine-style output-confidence routing (arXiv:2602.08948) — retrained on our models/benchmarks for fair comparison, (7) PAG-style generative verification (arXiv:2506.10406), (8) oracle gating (upper bound). Conduct ablations on: probe architecture (linear vs. MLP vs. ensemble vs. SAE-guided), feature sources (PANL-only vs. multi-token vs. +attention vs. +Wait-features vs. +SAE-confounded), layer selection, cross-task transferability, and threshold sensitivity analysis showing at what AUROC level gating begins to outperform ungated correction.\n\n**Phase 3b: Representational Geometry and Feature Decomposition of Correctability (Robust to Negative Probe Results).** Regardless of probe performance, we conduct a dedicated analysis of the representational relationship between correctability, correctness, and uncertainty at the feature population level. (a) Subspace comparison: compute the principal components of correctness and correctability representations separately (following arXiv:2602.08159's methodology) and measure subspace alignment via principal angle analysis — testing whether correctability occupies the same 3–8 dimensional subspace as correctness or requires distinct dimensions. (b) Dimensionality analysis: determine how many dimensions encode correctability vs. correctness at each layer, and whether correctability requires higher dimensionality (consistent with its second-order nature). (c) Non-linearity characterization: compare linear vs. non-linear probe AUROC gaps for correctability vs. correctness — a larger gap for correctability would indicate it occupies a more complex geometric region. (d) SAE feature decomposition: train SAEs on our target models and decompose correctability-predictive features into pure uncertainty, pure incorrectness, and confounded populations (following arXiv:2604.19974's 2×2 framework). Test whether confounded features are disproportionately important for correctability prediction compared to correctness prediction — which would provide mechanistic evidence that correctability requires simultaneously engaging both uncertainty and correctness axes. Measure the causal efficacy of each population via suppression experiments: if suppressing pure incorrectness features has minimal effect on correctability prediction (paralleling the functional inertness finding for correctness), this confirms the narrow confounded intersection hypothesis and explains the representational ceiling for broad-activation linear probes. (e) Error depth analysis: using the Error Depth Hypothesis framework (arXiv:2601.00828), characterize what makes errors correctable vs. uncorrectable — surface-level errors (calculation mistakes, recall failures) vs. deep errors (fundamental misunderstanding, missing knowledge) — and test whether this taxonomy is reflected in representational distance and SAE feature activation patterns. (f) Cross-layer trajectory analysis: inspired by Truth-as-a-Trajectory (arXiv:2603.01326), examine whether correctability is better captured by cross-layer displacement vectors than by static single-layer activations, which would explain why single-layer probes struggle. This phase yields publishable insights regardless of whether the ECP achieves high AUROC, providing the first empirical characterization of how correctability is (or is not) represented in LLM internal states and the first application of the SAE uncertainty-correctness dissociation framework to a second-order property.\n\n## Inspiration\nThe gap between 0.614 AUROC (single-layer PANL probe) and the consistently higher performance of multi-signal probes on correctness prediction (Gnosis hidden-only: 0.78–0.92; attention entropy: +0.06 AUROC absolute in OOD) suggests correctability prediction has room for improvement with better probing methodology — though the magnitude of potential gains is uncertain given correctability's second-order nature. The dramatic improvement from multi-layer ensembling on deception detection (0.510→0.910; arXiv:2604.13386) demonstrates that multi-layer stacking can rescue failing single-layer probes, but transferability to correctability is a hypothesis to test, not a guaranteed outcome. The SAE dissociation finding (arXiv:2604.19974) — that only rare confounded features bridging uncertainty and correctness are causally effective — provides both a challenge and an opportunity: correctability probes may need to target this narrow feature intersection, but successfully doing so could yield more principled and interpretable predictions than broad-activation probing. The untested overcorrection cost of the 'Wait' baseline, combined with new mechanistic understanding of Wait tokens' causal role in triggering distinct reasoning patterns (arXiv:2510.04128, arXiv:2601.17421), creates a clear opportunity for probe-selective Wait application. CoRefine (arXiv:2602.08948) demonstrates the viability of learned three-way routing for self-correction but uses output-level confidence without correctability awareness or genuine abstention — leaving a well-defined gap for hidden-state probe-based gating that distinguishes correctable from uncorrectable errors. Key untried combination: multi-signal enhanced probes for correctability prediction informed by SAE feature analysis + three-way gating with genuine abstention + comparison against Wait and confidence-based controllers, with explicit analysis of what makes correctability representationally distinct from correctness at the feature population level.\n\n## Key References\n- How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals (arXiv:2604.22271, 2026) — establishes PANL correctability signal, 0.614 AUROC baseline\n- Self-Correction Bench: Uncovering and Addressing the Self-Correction Blind Spot in LLMs (arXiv:2507.02778, NeurIPS 2025 Workshop) — 64.5% blind spot, Wait baseline achieving 89.3% reduction; QwQ-32B generates Wait first-token at 37.7–76.8% depending on benchmark\n- Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling (arXiv:2604.13386, 2026) — multi-layer stacking on deception detection: +29% on Insider Trading, +78% on Harm-Pressure Knowledge (0.510→0.910 in Llama-70B); transfer to correctability is a hypothesis we test\n- Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits — Gnosis (arXiv:2512.20578, 2025) — multi-signal fusion for correctness prediction: hidden-only 0.78–0.92 AUROC (ablation on Qwen3-1.7B), fusion 0.80–0.95 AUROC\n- Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders (arXiv:2604.19974, 2026) — SAE decomposition reveals functionally distinct feature populations: 68% of pure incorrectness features are causally inert; only rare confounded features (102/1,057 in Llama-3.1-8B) bridge uncertainty and correctness, achieving 0.79 AUROC with 3 features from layer 18; directly informs our probe design and Phase 3b analysis\n- CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute (arXiv:2602.08948, 2026) — three-way routing (halt/rethink/alternative) via 211K-parameter Conv1D controller on output-level confidence; 92.6% halt precision, ~190× token reduction; differs from our approach in signal source (output logprobs vs. hidden-state probes), decision type (no genuine abstention), and gating criterion (confidence vs. correctability)\n- Reflective Confidence: Correcting Reasoning Flaws via Online Self-Correction (arXiv:2512.18605, 2025) — transforms low-confidence output signals into reflection triggers; 83.3% on AIME 2025 vs. 70.0% Self-Consistency; uses output-level logprobs, no correctability modeling\n- Internal states before wait modulate reasoning patterns (arXiv:2510.04128, EMNLP 2025 Findings) — crosscoders identify causal features promoting/suppressing Wait tokens; distinct reasoning patterns (restarting, recalling, uncertainty expression, double-checking) triggered by pre-Wait internal states\n- Oops, Wait: Token-Level Signals as a Lens into LLM Reasoning (arXiv:2601.17421, Jan 2026) — Wait token probabilities correlate with reasoning correctness; models exploit Wait signals only partially; implications for token-level steering\n- Probing for Arithmetic Errors in Language Models (arXiv:2507.12379, 2025) — probe-guided selective re-prompting, 6–12% correction rate\n- Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification (arXiv:2504.05419, 2025) — probe-gated early exit, AUROC 0.77–0.91\n- Knowing When to Quit: A Principled Framework for Dynamic Abstention in LLM Reasoning (arXiv:2604.18419, 2026) — value-function probes for abstention gating\n- From Emergence to Control: Probing and Modulating Self-Reflection in Language Models (arXiv:2506.12217, 2025) — self-reflection vector steering\n- The Confidence Manifold (arXiv:2602.08159, 2026) — correctness in 3–8 dimensions, 25-example sufficiency, linearly separable\n- Attention Head Entropy of LLMs Predicts Answer Correctness (arXiv:2602.13699, 2026) — per-head 2-Rényi entropy achieves OOD AUROC 0.76 average (+0.06 absolute, 8.5% relative improvement over Lookback Lens)\n- PAG: Multi-Turn Reinforced LLM Self-Correction with Policy as Generative Verifier (arXiv:2506.10406, 2025)\n- Understanding the Dark Side of LLMs' Intrinsic Self-Correction (ACL 2025) — overcorrection and cognitive biases\n- Interpretability without Actionability (arXiv:2603.18353, 2026) — knowledge-action gap: 98.2% detection AUROC but only 20–24% correction via steering, 53-point gap\n- Mining Intrinsic Rewards from LLM Hidden States — SWIFT (arXiv:2505.12225, 2025) — all-layer gated aggregation\n- Between the Layers Lies the Truth (arXiv:2603.22299, 2026) — cross-layer agreement features\n- Truth as a Trajectory (arXiv:2603.01326, 2026) — cross-layer displacement vectors capture properties missed by static single-layer probes\n- Training Language Models to Self-Correct via Reinforcement Learning — SCoRe (arXiv:2409.12917, 2024) — on-policy training data importance\n- Large Language Models Cannot Self-Correct Reasoning Yet (ICLR 2024)\n- Decomposing LLM Self-Correction: The Accuracy-Correction Paradox (arXiv:2601.00828, 2026) — Error Depth Hypothesis: weaker models achieve 1.6× higher correction rates; deeper errors resist self-correction\n- No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes (arXiv:2509.10625, ICLR 2026 Workshop)\n- Calibrating LLM Confidence by Probing Perturbed Representation Stability (arXiv:2505.21772, 2025) — +6 AUROC points via adversarial perturbation stability\n- LLMs Encode How Difficult Problems Are (arXiv:2510.18147, 2025) — difficulty linearly decodable (ρ ≈ 0.88); meta-cognitive properties extractable but correctability's second-order nature makes transfer uncertain\n- Limits of Self-Correction in LLMs: An Information-Theoretic Analysis of Correlated Errors (Preprints.org 202601.0892, Feb 2026) — formalizes bounds on self-correction with correlated generator-evaluator errors\n\n## Resource Estimate\n- **manual**: {'gpu_hours': '220–280 H100-hours (Phase 0 pilot: ~15 hrs; inference for 3 models × ~30K questions × 3 passes [initial + Wait + correction] + multi-layer hidden state extraction across ~10 layers + attention feature extraction + Wait-feature extraction + SAE training and feature decomposition + probe training + representational geometry analysis + ablations)', 'timeline': '11–13 weeks (includes pilot, SAE analysis, full experiments, geometry analysis, paper writing)', 'estimated_gpu_cost': '$550–700 (at ~$2.50/H100-hr on cloud providers)'}\n- **human_in_loop**: {'gpu_hours': '220–280 H100-hours (same compute, faster iteration via AI-assisted code/analysis)', 'timeline': '8–10 weeks', 'claude_api_cost': '$150–210 (experiment orchestration, SAE analysis notebooks, geometry visualization, paper drafting via Sonnet 4.6)', 'estimated_gpu_cost': '$550–700'}\n- **auto_research**: {'gpu_hours': '300–360 H100-hours (overhead from automated probe architecture sweeps, SAE training and decomposition, threshold optimization, representational geometry grid, and broader ablation grid)', 'timeline': '2–3 weeks wall-clock', 'claude_api_cost': '$420–580 (full pipeline orchestration, code generation, debugging, SAE analysis, statistical analysis, visualization, paper drafting)', 'estimated_gpu_cost': '$750–900', 'speed_bottleneck': 'Sequential multi-layer hidden state extraction over ~90K forward passes (3 models × 30K questions); extraction requires full-precision activations at 5–10 layers per pass and cannot be batched as aggressively as standard inference; SAE training adds ~20–30 H100-hours per model'}\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-19T21:12:35.713Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T21:12:35.713Z",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba"
}
```

---

## Round 1

36 recorded events

### User

_source line 3 · 2026-05-19T21:12:35.727Z_

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
  "promptId": "157d3033-198f-4187-a348-8e3127be4a36",
  "type": "user",
  "uuid": "5f02251b-b079-4cd4-b58b-0c0bb05c9294",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T21:12:35.725Z_

```json
{
  "parentUuid": "5f02251b-b079-4cd4-b58b-0c0bb05c9294",
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
  "uuid": "88b6b40d-ab01-466b-bff9-56f5220ac785",
  "timestamp": "2026-05-19T21:12:35.725Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T21:12:35.725Z_

```json
{
  "parentUuid": "88b6b40d-ab01-466b-bff9-56f5220ac785",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4db860e9-3ffc-44d7-815a-92ebcd2bcd8c",
  "timestamp": "2026-05-19T21:12:35.725Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
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
  "leafUuid": "4db860e9-3ffc-44d7-815a-92ebcd2bcd8c",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM correctability prediction proposal",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba"
}
```

---

### Assistant

_source line 8 · 2026-05-19T21:12:53.776Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for CoRL 2026. Let me first carefully read the proposal, then conduct web searches to understand the field landscape before making my assessment.

Wait - CoRL is Conference on Robot Learning. This proposal is about LLM self-correction and probing internal representations. This seems more suited for NLP/ML venues like ACL, EMNLP, NeurIPS, ICML, ICLR rather than CoRL. Let me re-read the task description...

The user says "评估其投稿 CoRL 2026 主会的中稿潜力". So they're asking about CoRL 2026 specifically. 

There's a fundamental mismatch here - CoRL is specifically focused on robot learning, but this proposal deals entirely with LLM internal representations and self-correction mechanisms, which falls squarely in the NLP/ML domain. I should flag this venue misalignment as a critical issue in my evaluation, even as I assess the proposal's technical merit.

Before diving into the evaluation, I need to search for recent work on LLM self-correction capabilities, multi-layer probing techniques for understanding model internals, and sparse autoencoders applied to uncertainty detection in language models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4db860e9-3ffc-44d7-815a-92ebcd2bcd8c",
  "isSidechain": false,
  "requestId": "req_011CbCcj2jCx5M4qGgu56ncV",
  "type": "assistant",
  "uuid": "e5de3d20-89d1-4817-acbb-281f000a55fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158iUyovCcAFidMXEF98KUi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10635,
      "cache_read_input_tokens": 13985,
      "output_tokens": 651,
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
          "output_tokens": 651,
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

_source line 9 · 2026-05-19T21:12:53.781Z_

I'll start by conducting the required literature searches to ground my evaluation. Let me search for the key topics in this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5de3d20-89d1-4817-acbb-281f000a55fa",
  "isSidechain": false,
  "requestId": "req_011CbCcj2jCx5M4qGgu56ncV",
  "type": "assistant",
  "uuid": "73cbe399-aca0-4ebb-b81d-94ceeec6b868",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158iUyovCcAFidMXEF98KUi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10635,
      "cache_read_input_tokens": 13985,
      "output_tokens": 651,
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
          "output_tokens": 651,
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

_source line 10 · 2026-05-19T21:12:53.943Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VnLFeoGgznJu9Vo7v12nLo`</summary>

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
  "parentUuid": "73cbe399-aca0-4ebb-b81d-94ceeec6b868",
  "isSidechain": false,
  "requestId": "req_011CbCcj2jCx5M4qGgu56ncV",
  "type": "assistant",
  "uuid": "1ea5de10-89e3-4de5-aae4-0ac23ef563eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158iUyovCcAFidMXEF98KUi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10635,
      "cache_read_input_tokens": 13985,
      "output_tokens": 651,
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
          "output_tokens": 651,
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

_source line 11 · 2026-05-19T21:12:53.950Z_

<details><summary>↩ Tool result · `toolu_01VnLFeoGgznJu9Vo7v12nLo`</summary>

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
  "parentUuid": "1ea5de10-89e3-4de5-aae4-0ac23ef563eb",
  "isSidechain": false,
  "promptId": "157d3033-198f-4187-a348-8e3127be4a36",
  "type": "user",
  "uuid": "f1b23d83-ba2a-4e3c-b7c4-fb262e0f481d",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "1ea5de10-89e3-4de5-aae4-0ac23ef563eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T21:13:01.179Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me conduct the required searches. I'll do multiple searches in parallel to cover the key areas.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1b23d83-ba2a-4e3c-b7c4-fb262e0f481d",
  "isSidechain": false,
  "requestId": "req_011CbCckNgHbQR5EL1kQstZn",
  "type": "assistant",
  "uuid": "a00f337b-482b-4c67-8b88-39c9faa2bb8d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NEdXudRoLJqQSJpGC2X35k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1177,
      "cache_read_input_tokens": 24620,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1177,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 118,
          "cache_read_input_tokens": 24620,
          "cache_creation_input_tokens": 1177,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1177
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

_source line 13 · 2026-05-19T21:13:02.028Z_

Let me conduct the required literature searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a00f337b-482b-4c67-8b88-39c9faa2bb8d",
  "isSidechain": false,
  "requestId": "req_011CbCckNgHbQR5EL1kQstZn",
  "type": "assistant",
  "uuid": "326484c2-70df-482b-a619-c58384a32a48",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NEdXudRoLJqQSJpGC2X35k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1177,
      "cache_read_input_tokens": 24620,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1177,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 118,
          "cache_read_input_tokens": 24620,
          "cache_creation_input_tokens": 1177,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1177
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

_source line 14 · 2026-05-19T21:13:02.062Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0195fGbdtwB6osGnqooLtC29`</summary>

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
  "parentUuid": "326484c2-70df-482b-a619-c58384a32a48",
  "isSidechain": false,
  "requestId": "req_011CbCckNgHbQR5EL1kQstZn",
  "type": "assistant",
  "uuid": "902aeec6-8cdf-4dc8-832a-fe94ddc7a860",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NEdXudRoLJqQSJpGC2X35k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1177,
      "cache_read_input_tokens": 24620,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1177,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 118,
          "cache_read_input_tokens": 24620,
          "cache_creation_input_tokens": 1177,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1177
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

_source line 15 · 2026-05-19T21:13:12.661Z_

<details><summary>↩ Tool result · `toolu_0195fGbdtwB6osGnqooLtC29`</summary>

```text
Web search results for query: "LLM self-correction correctability prediction internal representations probing 2025 2026"

Links: [{"title":"Predicting LLM Answer Accuracy from Question-Only ...","url":"https://arxiv.org/pdf/2509.10625"},{"title":"Model-Agnostic Correctness Assessment for LLM-Generated Code via Dynamic Internal Representation Selection","url":"https://arxiv.org/pdf/2510.02934"},{"title":"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/pdf/2512.20578"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"},{"title":"Probing for Arithmetic Errors in Language Models","url":"https://arxiv.org/pdf/2507.12379"},{"title":"Internalized Self-Correction for Large Language Models","url":"https://arxiv.org/pdf/2412.16653"}]

I found several relevant research papers on LLM self-correction, correctability prediction, and internal representation probing from 2025-2026. Here are the key findings:

## Correctability Prediction from Internal Representations

Recent work investigates the structure of self-correctness representations in LLMs, with a focus on testing whether correctness can be predicted from internal activations. One approach introduces AUTOPROBE, a model-agnostic method that dynamically selects informative internal representations for code correctness assessment using attention-based mechanisms to learn importance scores for hidden states, then aggregates these weighted representations to predict code correctness across multiple dimensions including compilability, functionality, and security.

## LLM Self-Awareness and Failure Prediction

LLMs remain unreliable at assessing the correctness of their own outputs and frequently produce confident but incorrect answers, failing to detect reasoning errors or hallucinations. A fundamental open question is whether LLMs can anticipate their own failures by examining the internal dynamics that govern their generation process.

## Self-Correction Challenges

Research has demonstrated that LLMs cannot correct their own reasoning without external feedback, and that correction attempts can actually make things worse. Additionally, self-correction sometimes flips correct answers to incorrect ones through prompt bias and cognitive-like biases in the correction process.

## Arithmetic Error Detection

Arithmetic errors can be anticipated from internal activations alone, and simple probes offer a viable path toward lightweight model self-correction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "902aeec6-8cdf-4dc8-832a-fe94ddc7a860",
  "isSidechain": false,
  "promptId": "157d3033-198f-4187-a348-8e3127be4a36",
  "type": "user",
  "uuid": "c23a9025-f830-4ef5-b592-7ff131e77170",
  "toolUseResult": {
    "query": "LLM self-correction correctability prediction internal representations probing 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LMQ3WLmBFSzUBix2Cu9usN",
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
      "I found several relevant research papers on LLM self-correction, correctability prediction, and internal representation probing from 2025-2026. Here are the key findings:\n\n## Correctability Prediction from Internal Representations\n\nRecent work investigates the structure of self-correctness representations in LLMs, with a focus on testing whether correctness can be predicted from internal activations. One approach introduces AUTOPROBE, a model-agnostic method that dynamically selects informative internal representations for code correctness assessment using attention-based mechanisms to learn importance scores for hidden states, then aggregates these weighted representations to predict code correctness across multiple dimensions including compilability, functionality, and security.\n\n## LLM Self-Awareness and Failure Prediction\n\nLLMs remain unreliable at assessing the correctness of their own outputs and frequently produce confident but incorrect answers, failing to detect reasoning errors or hallucinations. A fundamental open question is whether LLMs can anticipate their own failures by examining the internal dynamics that govern their generation process.\n\n## Self-Correction Challenges\n\nResearch has demonstrated that LLMs cannot correct their own reasoning without external feedback, and that correction attempts can actually make things worse. Additionally, self-correction sometimes flips correct answers to incorrect ones through prompt bias and cognitive-like biases in the correction process.\n\n## Arithmetic Error Detection\n\nArithmetic errors can be anticipated from internal activations alone, and simple probes offer a viable path toward lightweight model self-correction."
    ],
    "durationSeconds": 10.59217192,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "902aeec6-8cdf-4dc8-832a-fe94ddc7a860",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T21:13:15.922Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WqetLA3ws4Xf6E6U33PFPG`</summary>

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
  "parentUuid": "c23a9025-f830-4ef5-b592-7ff131e77170",
  "isSidechain": false,
  "requestId": "req_011CbCcmkS1aU27Ras4Pb6Tv",
  "type": "assistant",
  "uuid": "da7c5608-2847-46d7-b623-8d6ae03800a0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SdE9fJLjxLqh2Xt9ksmiA5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 773,
      "cache_read_input_tokens": 25797,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 773,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 25797,
          "cache_creation_input_tokens": 773,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 773
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

_source line 17 · 2026-05-19T21:13:34.866Z_

<details><summary>↩ Tool result · `toolu_01WqetLA3ws4Xf6E6U33PFPG`</summary>

```text
Web search results for query: "arXiv 2604.22271 PANL correctability signal LLM internal confidence"

Links: [{"title":"How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals","url":"https://arxiv.org/html/2604.22271v1"},{"title":"On LLMs’ Internal Representation of Code Correctness","url":"https://arxiv.org/html/2512.07404"},{"title":"On LLMs' Internal Representation of Code Correctness","url":"https://arxiv.org/pdf/2512.07404"},{"title":"Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs","url":"https://arxiv.org/pdf/2604.01457"},{"title":"How do LLMs Compute Verbal Confidence?","url":"https://arxiv.org/html/2603.17839v1"},{"title":"Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders","url":"https://arxiv.org/html/2604.19974"},{"title":"InternalInspector $I^2$: Robust Confidence Estimation in LLMs through   Internal States","url":"https://arxiv.org/pdf/2406.12053"},{"title":"Towards Fully Exploiting LLM Internal States to Enhance Knowledge Boundary Perception","url":"https://arxiv.org/pdf/2502.11677"},{"title":"No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes","url":"https://arxiv.org/html/2509.10625v3"}]

Based on the search results, I found the paper arXiv 2604.22271. Here's what the research is about:

## Paper: "How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals"

The paper investigates how large language models can detect their own errors and sometimes correct them without external feedback. 

The researchers investigate this through the lens of second-order models of confidence from decision neuroscience. In first-order systems, confidence derives from the generation signal itself and is maximal for the chosen response, precluding error detection, while second-order models posit a partially independent evaluative signal that can disagree with the committed response, providing the basis for error detection.

### Key Findings on PANL and Correctability:

The research found that LLMs cache a confidence representation at a token immediately following the answer (post-answer newline: PANL)—that causally drives verbal confidence and dissociates from log-probabilities.

The main discovery is that PANL activations predict error detection beyond verbal confidence itself, and PANL predicts which errors the model can correct—where all behavioral signals fail. Additionally, causal interventions confirm that PANL signals rescue error detection behavior when answer information is corrupted.

The results reveal that LLMs naturally implement a second-order confidence architecture whose internal evaluative signal encodes not only whether an answer is likely wrong, but whether the model has the knowledge to fix it. All findings replicate across models (Gemma 3 27B and Qwen 2.5 7B) and tasks (TriviaQA and MNLI).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da7c5608-2847-46d7-b623-8d6ae03800a0",
  "isSidechain": false,
  "promptId": "157d3033-198f-4187-a348-8e3127be4a36",
  "type": "user",
  "uuid": "9ccb0cd1-f07f-40ff-91e9-1bc0286a52a1",
  "toolUseResult": {
    "query": "arXiv 2604.22271 PANL correctability signal LLM internal confidence",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YbvmeRenLY3v11Pm5HCbtJ",
        "content": [
          {
            "title": "How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals",
            "url": "https://arxiv.org/html/2604.22271v1"
          },
          {
            "title": "On LLMs’ Internal Representation of Code Correctness",
            "url": "https://arxiv.org/html/2512.07404"
          },
          {
            "title": "On LLMs' Internal Representation of Code Correctness",
            "url": "https://arxiv.org/pdf/2512.07404"
          },
          {
            "title": "Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs",
            "url": "https://arxiv.org/pdf/2604.01457"
          },
          {
            "title": "How do LLMs Compute Verbal Confidence?",
            "url": "https://arxiv.org/html/2603.17839v1"
          },
          {
            "title": "Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders",
            "url": "https://arxiv.org/html/2604.19974"
          },
          {
            "title": "InternalInspector $I^2$: Robust Confidence Estimation in LLMs through   Internal States",
            "url": "https://arxiv.org/pdf/2406.12053"
          },
          {
            "title": "Towards Fully Exploiting LLM Internal States to Enhance Knowledge Boundary Perception",
            "url": "https://arxiv.org/pdf/2502.11677"
          },
          {
            "title": "No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes",
            "url": "https://arxiv.org/html/2509.10625v3"
          }
        ]
      },
      "Based on the search results, I found the paper arXiv 2604.22271. Here's what the research is about:\n\n## Paper: \"How LLMs Detect and Correct Their Own Errors: The Role of Internal Confidence Signals\"\n\nThe paper investigates how large language models can detect their own errors and sometimes correct them without external feedback. \n\nThe researchers investigate this through the lens of second-order models of confidence from decision neuroscience. In first-order systems, confidence derives from the generation signal itself and is maximal for the chosen response, precluding error detection, while second-order models posit a partially independent evaluative signal that can disagree with the committed response, providing the basis for error detection.\n\n### Key Findings on PANL and Correctability:\n\nThe research found that LLMs cache a confidence representation at a token immediately following the answer (post-answer newline: PANL)—that causally drives verbal confidence and dissociates from log-probabilities.\n\nThe main discovery is that PANL activations predict error detection beyond verbal confidence itself, and PANL predicts which errors the model can correct—where all behavioral signals fail. Additionally, causal interventions confirm that PANL signals rescue error detection behavior when answer information is corrupted.\n\nThe results reveal that LLMs naturally implement a second-order confidence architecture whose internal evaluative signal encodes not only whether an answer is likely wrong, but whether the model has the knowledge to fix it. All findings replicate across models (Gemma 3 27B and Qwen 2.5 7B) and tasks (TriviaQA and MNLI)."
    ],
    "durationSeconds": 18.93670145,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "da7c5608-2847-46d7-b623-8d6ae03800a0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T21:13:37.429Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UCVXA1wBzWydDnCdk1RB5w`</summary>

```json
{
  "query": "arXiv 2604.13386 multi-layer probe ensembling deception detection linear probe accuracy scales"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ccb0cd1-f07f-40ff-91e9-1bc0286a52a1",
  "isSidechain": false,
  "requestId": "req_011CbCcoPLoySVNcTNWWnany",
  "type": "assistant",
  "uuid": "cf4ff367-6e0a-4b43-ac55-f7b527a0fd6a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H1NoRjuC5KUnpqx1gNXNM5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 884,
      "cache_read_input_tokens": 26570,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 884,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 26570,
          "cache_creation_input_tokens": 884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 884
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

_source line 19 · 2026-05-19T21:13:45.464Z_

<details><summary>↩ Tool result · `toolu_01UCVXA1wBzWydDnCdk1RB5w`</summary>

```text
Web search results for query: "arXiv 2604.13386 multi-layer probe ensembling deception detection linear probe accuracy scales"

Links: [{"title":"[2604.13386] Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling","url":"https://arxiv.org/abs/2604.13386"},{"title":"Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling","url":"https://arxiv.org/html/2604.13386v1"},{"title":"Building Better Deception Probes Using Targeted Instruction Pairs","url":"https://arxiv.org/html/2602.01425"},{"title":"Caught in the Act: a mechanistic approach to detecting deception","url":"https://arxiv.org/pdf/2508.19505"},{"title":"Multilayered deception for intrusion detection and prevention","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9392001"},{"title":"Multilayered deception for intrusion detection and prevention","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8739281"},{"title":"Detecting Strategic Deception Using Linear Probes","url":"https://arxiv.org/pdf/2502.03407"},{"title":"Improved semi-supervised autoencoder for deception detection","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6782094/"}]

Based on the search results, here's the information about arXiv paper 2604.13386:

The paper titled "Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling" shows that linear probes can detect when language models produce outputs they "know" are wrong, a capability relevant to both deception and reward hacking.

Key findings from the paper include:

1. **Multi-layer ensembling effectiveness**: Combining probes from multiple layers into an ensemble recovers strong performance even where single-layer probes fail, improving AUROC by +29% on Insider Trading and +78% on Harm-Pressure Knowledge.

2. **Scaling with model size**: Across 12 models (0.5B--176B parameters), probe accuracy improves with scale: ~5% AUROC per 10x parameters (R=0.81).

3. **Why single-layer probes fail**: Single-layer probes are fragile: the best layer varies across models and tasks, and probes fail entirely on some deception types.

4. **Geometric explanation**: Deception directions rotate gradually across layers rather than appearing at one location, explaining both why single-layer probes are brittle and why multi-layer ensembles succeed.

The paper was submitted on April 15, 2026, and was authored by Erik Nordby, Tasha Pais, and Aviel Parrack.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf4ff367-6e0a-4b43-ac55-f7b527a0fd6a",
  "isSidechain": false,
  "promptId": "157d3033-198f-4187-a348-8e3127be4a36",
  "type": "user",
  "uuid": "67f10577-0201-4fb9-988f-fd1f81b3138c",
  "toolUseResult": {
    "query": "arXiv 2604.13386 multi-layer probe ensembling deception detection linear probe accuracy scales",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EEbKH8k5wZKUA5vMuBxsPk",
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
      "Based on the search results, here's the information about arXiv paper 2604.13386:\n\nThe paper titled \"Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling\" shows that linear probes can detect when language models produce outputs they \"know\" are wrong, a capability relevant to both deception and reward hacking.\n\nKey findings from the paper include:\n\n1. **Multi-layer ensembling effectiveness**: Combining probes from multiple layers into an ensemble recovers strong performance even where single-layer probes fail, improving AUROC by +29% on Insider Trading and +78% on Harm-Pressure Knowledge.\n\n2. **Scaling with model size**: Across 12 models (0.5B--176B parameters), probe accuracy improves with scale: ~5% AUROC per 10x parameters (R=0.81).\n\n3. **Why single-layer probes fail**: Single-layer probes are fragile: the best layer varies across models and tasks, and probes fail entirely on some deception types.\n\n4. **Geometric explanation**: Deception directions rotate gradually across layers rather than appearing at one location, explaining both why single-layer probes are brittle and why multi-layer ensembles succeed.\n\nThe paper was submitted on April 15, 2026, and was authored by Erik Nordby, Tasha Pais, and Aviel Parrack."
    ],
    "durationSeconds": 8.030819285999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "cf4ff367-6e0a-4b43-ac55-f7b527a0fd6a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "67f10577-0201-4fb9-988f-fd1f81b3138c",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM correctability prediction proposal",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba"
}
```

---

### Tool call

_source line 22 · 2026-05-19T21:13:49.449Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CTWQk3cKMeCTGWK9ViXYwz`</summary>

```json
{
  "query": "CoRefine confidence-guided self-refinement arXiv 2602.08948 2026 three-way routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67f10577-0201-4fb9-988f-fd1f81b3138c",
  "isSidechain": false,
  "requestId": "req_011CbCcpAh5c1dBo7d1ZPmwG",
  "type": "assistant",
  "uuid": "e8fe061e-4737-48af-a80b-72e3e48a5cc4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VKwUJFuDy2f7bSTeNvcaBg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 796,
      "cache_read_input_tokens": 27454,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 796,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 27454,
          "cache_creation_input_tokens": 796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 796
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

_source line 23 · 2026-05-19T21:14:09.468Z_

<details><summary>↩ Tool result · `toolu_01CTWQk3cKMeCTGWK9ViXYwz`</summary>

```text
Web search results for query: "CoRefine confidence-guided self-refinement arXiv 2602.08948 2026 three-way routing"

Links: [{"title":"[2602.08948] CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute","url":"https://arxiv.org/abs/2602.08948"},{"title":"CoRefine: Confidence-Guided Self-Refinement for Adaptive Test-Time Compute","url":"https://arxiv.org/pdf/2602.08948"},{"title":"Confidence-aware Adversarial Learning for Self-supervised Semantic   Matching","url":"https://arxiv.org/pdf/2008.10902"},{"title":"Self-Refinement of Language Models from External Proxy Metrics Feedback","url":"https://arxiv.org/pdf/2403.00827"},{"title":"A Stitch in Time Saves Nine: Proactive Self-Refinement for Language Models","url":"https://arxiv.org/pdf/2508.12903"},{"title":"Toward More Reliable Artificial Intelligence: Reducing Hallucinations in Vision-Language Models","url":"https://arxiv.org/pdf/2512.07564"}]

Based on the search results, I found detailed information about the CoRefine paper:

CoRefine is a confidence-guided self-refinement method that achieves competitive accuracy using a fraction of the tokens via a lightweight 211k-parameter Conv1D controller atop a frozen LLM.

The controller consumes full-trace confidence to decide whether to halt, re-examine, or try a different approach, enabling targeted self-correction with an average of 2.7 refinement steps per problem and roughly 190-fold token reduction relative to 512-sample baselines.

The three routing/decision options that the controller makes are: HALT (accept current answer), RETHINK (verify reasoning), or ALTERNATIVE (explore new approach).

CoRefine consists of three components: (1) full-trace confidence extraction from the model's logprobs, (2) a lightweight neural controller (∼211K parameters) that maps confidence features to refinement decisions, and (3) targeted synthesis prompts that compact previous reasoning into high-signal context for self-correction.

The paper was submitted on February 9, 2026 to arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8fe061e-4737-48af-a80b-72e3e48a5cc4",
  "isSidechain": false,
  "promptId": "157d3033-198f-4187-a348-8e3127be4a36",
  "type": "user",
  "uuid": "2c9ef1f6-12e6-4d0f-86b3-4e5ae2400414",
  "toolUseResult": {
    "query": "CoRefine confidence-guided self-refinement arXiv 2602.08948 2026 three-way routing",
    "results": [
      {
        "tool_use_id": "srvtoolu_01G7ZxvG6CsDCwotqsWc7rAF",
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
      "Based on the search results, I found detailed information about the CoRefine paper:\n\nCoRefine is a confidence-guided self-refinement method that achieves competitive accuracy using a fraction of the tokens via a lightweight 211k-parameter Conv1D controller atop a frozen LLM.\n\nThe controller consumes full-trace confidence to decide whether to halt, re-examine, or try a different approach, enabling targeted self-correction with an average of 2.7 refinement steps per problem and roughly 190-fold token reduction relative to 512-sample baselines.\n\nThe three routing/decision options that the controller makes are: HALT (accept current answer), RETHINK (verify reasoning), or ALTERNATIVE (explore new approach).\n\nCoRefine consists of three components: (1) full-trace confidence extraction from the model's logprobs, (2) a lightweight neural controller (∼211K parameters) that maps confidence features to refinement decisions, and (3) targeted synthesis prompts that compact previous reasoning into high-signal context for self-correction.\n\nThe paper was submitted on February 9, 2026 to arXiv."
    ],
    "durationSeconds": 20.013124905000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e8fe061e-4737-48af-a80b-72e3e48a5cc4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T21:14:15.393Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Es9cTHACgeG4MK69gRuURH`</summary>

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
  "parentUuid": "2c9ef1f6-12e6-4d0f-86b3-4e5ae2400414",
  "isSidechain": false,
  "requestId": "req_011CbCcqwNwMEgf9HgQEMf8x",
  "type": "assistant",
  "uuid": "f0a03842-64fc-4bd8-9834-27b7f220133f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XZxDLvaHvVRR5FVPNhfFha",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 28250,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 652,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 28250,
          "cache_creation_input_tokens": 652,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 652
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

_source line 25 · 2026-05-19T21:14:25.702Z_

<details><summary>↩ Tool result · `toolu_01Es9cTHACgeG4MK69gRuURH`</summary>

```text
Web search results for query: "SAE sparse autoencoder uncertainty correctness dissociation LLM features arXiv 2604.19974"

Links: [{"title":"Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders","url":"https://arxiv.org/html/2604.19974"},{"title":"[2604.19974] Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders","url":"https://arxiv.org/abs/2604.19974"},{"title":"Sparse but Wrong: Incorrect L0 Leads to Incorrect Features in Sparse Autoencoders","url":"https://arxiv.org/pdf/2508.16560"},{"title":"Mechanistic Interpretability of Code Correctness in LLMs via Sparse Autoencoders","url":"https://arxiv.org/pdf/2510.02917"},{"title":"AdaptiveK Sparse Autoencoders: Dynamic Sparsity Allocation for Interpretable LLM Representations","url":"https://arxiv.org/pdf/2508.17320"}]

Based on the search results, I found the paper you're looking for. Here's what arXiv paper 2604.19974 is about:

The paper addresses whether output-level uncertainty and actual correctness in large language models are driven by the same internal mechanisms or by distinct feature populations. The authors introduce a 2x2 framework that partitions model predictions along correctness and confidence axes, and uses sparse autoencoders to identify features associated with each dimension independently.

Applying this to Llama-3.1-8B and Gemma-2-9B, they identify three feature populations that play fundamentally different functional roles. These consist of pure uncertainty features, pure incorrectness features, and confounded features associated with both signals.

The key findings are:
- Pure uncertainty features are functionally essential: suppressing them severely degrades accuracy.
- Pure incorrectness features are functionally inert: despite showing statistically significant activation differences between correct and incorrect predictions, the majority produce near-zero change in accuracy when suppressed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0a03842-64fc-4bd8-9834-27b7f220133f",
  "isSidechain": false,
  "promptId": "157d3033-198f-4187-a348-8e3127be4a36",
  "type": "user",
  "uuid": "edc8aa6a-52fb-4c40-b7ab-493cbc986468",
  "toolUseResult": {
    "query": "SAE sparse autoencoder uncertainty correctness dissociation LLM features arXiv 2604.19974",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KjoUxwMGuC3w612YcuJaRe",
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
      "Based on the search results, I found the paper you're looking for. Here's what arXiv paper 2604.19974 is about:\n\nThe paper addresses whether output-level uncertainty and actual correctness in large language models are driven by the same internal mechanisms or by distinct feature populations. The authors introduce a 2x2 framework that partitions model predictions along correctness and confidence axes, and uses sparse autoencoders to identify features associated with each dimension independently.\n\nApplying this to Llama-3.1-8B and Gemma-2-9B, they identify three feature populations that play fundamentally different functional roles. These consist of pure uncertainty features, pure incorrectness features, and confounded features associated with both signals.\n\nThe key findings are:\n- Pure uncertainty features are functionally essential: suppressing them severely degrades accuracy.\n- Pure incorrectness features are functionally inert: despite showing statistically significant activation differences between correct and incorrect predictions, the majority produce near-zero change in accuracy when suppressed."
    ],
    "durationSeconds": 10.303883688,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f0a03842-64fc-4bd8-9834-27b7f220133f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-19T21:14:28.382Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ae6uKHSkU1nTLkxgznUy1W`</summary>

```json
{
  "query": "\"self-correction\" LLM probe gating hidden state correctability 2026 selective"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edc8aa6a-52fb-4c40-b7ab-493cbc986468",
  "isSidechain": false,
  "requestId": "req_011CbCcs9GqNS9QnXNKxnovs",
  "type": "assistant",
  "uuid": "c3352430-7f37-4473-899e-4cc6868b442e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SEYqSQFcgWP4D2CL4ZjTSG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 28902,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 622,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 28902,
          "cache_creation_input_tokens": 622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 622
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

_source line 27 · 2026-05-19T21:14:35.819Z_

<details><summary>↩ Tool result · `toolu_01Ae6uKHSkU1nTLkxgznUy1W`</summary>

```text
Web search results for query: ""self-correction" LLM probe gating hidden state correctability 2026 selective"

Links: [{"title":"Probing for Arithmetic Errors in Language Models","url":"https://arxiv.org/pdf/2507.12379"},{"title":"Adaptation with Self-Evaluation to Improve Selective Prediction in LLMs","url":"https://arxiv.org/pdf/2310.11689"},{"title":"Temporal Predictors of Outcome in Reasoning Language Models","url":"https://arxiv.org/pdf/2511.14773"},{"title":"Intrinsic Self-correction for Enhanced Morality: An Analysis of Internal   Mechanisms and the Superficial Hypothesis","url":"https://arxiv.org/pdf/2407.15286"},{"title":"Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/pdf/2512.20578"},{"title":"Latent Space Chain-of-Embedding Enables Output-free LLM Self-Evaluation","url":"https://arxiv.org/pdf/2410.13640"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"}]

I found several relevant research papers on this topic. Here are the key results:

**Probing and Hidden State Analysis:**

Simple probes offer a viable path toward lightweight model self-correction, with arithmetic errors anticipated from internal activations alone. Additionally, probes can guide selective re-prompting of erroneous reasoning steps, improving task accuracy with minimal disruption to correct outputs.

**Correctability Detection:**

Research demonstrates predicting answer correctness directly from an LLM's hidden state while the chain-of-thought is being generated. Furthermore, hidden states from very short prefixes already contain linearly decodable information about eventual correctness, reaching AUCs up to 0.8+ on MATH-like data.

**Self-Awareness Mechanisms:**

Gnosis is a lightweight mechanism that enables frozen LLMs to predict the correctness of their own generations by decoding signals intrinsic to the inference process. Gnosis jointly models hidden-state evolution and attention-routing patterns through a compact architecture that extracts reliability cues with negligible inference overhead.

**Self-Evaluation Approaches:**

Recent research has revealed that the latent space of LLMs contains hidden state information that can largely reflect response correctness.

**Confidence Signals:**

LLMs cache a confidence representation at a token immediately following the answer—post-answer newline—that causally drives verbal confidence and dissociates from log-probabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3352430-7f37-4473-899e-4cc6868b442e",
  "isSidechain": false,
  "promptId": "157d3033-198f-4187-a348-8e3127be4a36",
  "type": "user",
  "uuid": "f9be9973-0e03-40fb-b878-63f246015dee",
  "toolUseResult": {
    "query": "\"self-correction\" LLM probe gating hidden state correctability 2026 selective",
    "results": [
      {
        "tool_use_id": "srvtoolu_0159F4WS9TGSasCx8kqKuZMP",
        "content": [
          {
            "title": "Probing for Arithmetic Errors in Language Models",
            "url": "https://arxiv.org/pdf/2507.12379"
          },
          {
            "title": "Adaptation with Self-Evaluation to Improve Selective Prediction in LLMs",
            "url": "https://arxiv.org/pdf/2310.11689"
          },
          {
            "title": "Temporal Predictors of Outcome in Reasoning Language Models",
            "url": "https://arxiv.org/pdf/2511.14773"
          },
          {
            "title": "Intrinsic Self-correction for Enhanced Morality: An Analysis of Internal   Mechanisms and the Superficial Hypothesis",
            "url": "https://arxiv.org/pdf/2407.15286"
          },
          {
            "title": "Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/pdf/2512.20578"
          },
          {
            "title": "Latent Space Chain-of-Embedding Enables Output-free LLM Self-Evaluation",
            "url": "https://arxiv.org/pdf/2410.13640"
          },
          {
            "title": "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs",
            "url": "https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"
          }
        ]
      },
      "I found several relevant research papers on this topic. Here are the key results:\n\n**Probing and Hidden State Analysis:**\n\nSimple probes offer a viable path toward lightweight model self-correction, with arithmetic errors anticipated from internal activations alone. Additionally, probes can guide selective re-prompting of erroneous reasoning steps, improving task accuracy with minimal disruption to correct outputs.\n\n**Correctability Detection:**\n\nResearch demonstrates predicting answer correctness directly from an LLM's hidden state while the chain-of-thought is being generated. Furthermore, hidden states from very short prefixes already contain linearly decodable information about eventual correctness, reaching AUCs up to 0.8+ on MATH-like data.\n\n**Self-Awareness Mechanisms:**\n\nGnosis is a lightweight mechanism that enables frozen LLMs to predict the correctness of their own generations by decoding signals intrinsic to the inference process. Gnosis jointly models hidden-state evolution and attention-routing patterns through a compact architecture that extracts reliability cues with negligible inference overhead.\n\n**Self-Evaluation Approaches:**\n\nRecent research has revealed that the latent space of LLMs contains hidden state information that can largely reflect response correctness.\n\n**Confidence Signals:**\n\nLLMs cache a confidence representation at a token immediately following the answer—post-answer newline—that causally drives verbal confidence and dissociates from log-probabilities."
    ],
    "durationSeconds": 7.432036273999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c3352430-7f37-4473-899e-4cc6868b442e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-19T21:14:38.230Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KC5xRL54DFxbgMHRnaka8k`</summary>

```json
{
  "query": "CoRL 2026 conference robot learning topics scope submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9be9973-0e03-40fb-b878-63f246015dee",
  "isSidechain": false,
  "requestId": "req_011CbCcssxNRkvxh21PXQKQr",
  "type": "assistant",
  "uuid": "35ba49f2-a1ca-4387-afb8-290e6e95ec2c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018oQaSo3r6UZ1bPfhemBpUm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 768,
      "cache_read_input_tokens": 29524,
      "output_tokens": 63,
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
          "output_tokens": 63,
          "cache_read_input_tokens": 29524,
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

### Tool result

_source line 29 · 2026-05-19T21:14:45.837Z_

<details><summary>↩ Tool result · `toolu_01KC5xRL54DFxbgMHRnaka8k`</summary>

```text
Web search results for query: "CoRL 2026 conference robot learning topics scope submission"

Links: [{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Conference on Robot Learning (CoRL) 2026: Everything You Need to Know - AI Expert Magazine - premier publication dedicated to AI","url":"https://www.aiexpertmagazine.com/conference-on-robot-learning-corl-2026-everything-you-need-to-know/"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Workshops","url":"https://www.corl.org/contributions/call-for-workshops"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"}]

Based on the search results, here's comprehensive information about CoRL 2026:

## Conference Overview

The Conference on Robot Learning (CoRL) is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics and its interaction with other areas of robotics.

## Topics and Scope

CoRL covers topics including imitation learning, reinforcement learning for robots, sim-to-real transfer, robot perception through learning, learned manipulation and locomotion, and learning-based planning.

CoRL welcomes papers in areas such as learning representations for robotic perception and control, learning robot foundation models or general-purpose knowledge systems for robotics, imitation learning for robotics (e.g., by behavioral cloning and/or inverse reinforcement learning), reinforcement learning for control of physical robots, and video models and latent world models for robot learning.

## Submission Requirements

The paper submission deadline is May 29, 2026. Papers are limited to 8 pages of content plus unlimited references.

Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.

## Conference Dates and Location

CoRL 2026 will be held at the JW Marriott Austin in Austin, TX (November 9–12, 2026), with a workshop day on November 9 and the main conference on November 10–12.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35ba49f2-a1ca-4387-afb8-290e6e95ec2c",
  "isSidechain": false,
  "promptId": "157d3033-198f-4187-a348-8e3127be4a36",
  "type": "user",
  "uuid": "b8194b5b-5482-4ae3-9ee1-471729d025a2",
  "toolUseResult": {
    "query": "CoRL 2026 conference robot learning topics scope submission",
    "results": [
      {
        "tool_use_id": "srvtoolu_011VV1SjrSLmSNwURyuyZ876",
        "content": [
          {
            "title": "CoRL LaTeX Template | Robot Learning Conference Format | Underleaf",
            "url": "https://www.underleaf.ai/templates/corl"
          },
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
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
            "title": "CoRL 2026 - Instruction for Authors",
            "url": "https://www.corl.org/contributions/instruction-for-authors"
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
            "title": "Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"
          }
        ]
      },
      "Based on the search results, here's comprehensive information about CoRL 2026:\n\n## Conference Overview\n\nThe Conference on Robot Learning (CoRL) is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics and its interaction with other areas of robotics.\n\n## Topics and Scope\n\nCoRL covers topics including imitation learning, reinforcement learning for robots, sim-to-real transfer, robot perception through learning, learned manipulation and locomotion, and learning-based planning.\n\nCoRL welcomes papers in areas such as learning representations for robotic perception and control, learning robot foundation models or general-purpose knowledge systems for robotics, imitation learning for robotics (e.g., by behavioral cloning and/or inverse reinforcement learning), reinforcement learning for control of physical robots, and video models and latent world models for robot learning.\n\n## Submission Requirements\n\nThe paper submission deadline is May 29, 2026. Papers are limited to 8 pages of content plus unlimited references.\n\nSubmissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.\n\n## Conference Dates and Location\n\nCoRL 2026 will be held at the JW Marriott Austin in Austin, TX (November 9–12, 2026), with a workshop day on November 9 and the main conference on November 10–12."
    ],
    "durationSeconds": 7.602089966999992,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "35ba49f2-a1ca-4387-afb8-290e6e95ec2c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-19T21:14:45.844Z_

```json
{
  "parentUuid": "b8194b5b-5482-4ae3-9ee1-471729d025a2",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "a96f659f-14ca-4e46-a4c7-df3d4b9edca2",
  "timestamp": "2026-05-19T21:14:45.844Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-19T21:14:50.418Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AdHGA7XDQ46CTvxKUKQcES`</summary>

```json
{
  "query": "LLM correctability prediction probe-gated self-correction abstention 2026 hidden state"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a96f659f-14ca-4e46-a4c7-df3d4b9edca2",
  "isSidechain": false,
  "requestId": "req_011CbCctcpZngnTGGS1QFCdc",
  "type": "assistant",
  "uuid": "03cb0a37-3d18-46e3-8a58-1f1eccf6138a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ak35UETk8CVmMe5PtpDWDs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 897,
      "cache_read_input_tokens": 30292,
      "output_tokens": 72,
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
          "output_tokens": 72,
          "cache_read_input_tokens": 30292,
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

_source line 32 · 2026-05-19T21:15:00.836Z_

<details><summary>↩ Tool result · `toolu_01AdHGA7XDQ46CTvxKUKQcES`</summary>

```text
Web search results for query: "LLM correctability prediction probe-gated self-correction abstention 2026 hidden state"

Links: [{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018.full.pdf"},{"title":"No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes","url":"https://arxiv.org/html/2509.10625v3"},{"title":"Temporal Predictors of Outcome in Reasoning Language Models","url":"https://arxiv.org/pdf/2511.14773"},{"title":"Latent Space Chain-of-Embedding Enables Output-free LLM Self-Evaluation","url":"https://arxiv.org/pdf/2410.13640"},{"title":"Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs","url":"https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"},{"title":"[2512.20578] Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits","url":"https://arxiv.org/abs/2512.20578"}]

Based on the search results, I found several relevant papers from 2026 addressing LLM correctability prediction using hidden states and related techniques:

## Key Research Findings:

**Correctability Prediction from Hidden States:**
Researchers train probes, small classifiers that take in hidden states and predict properties of interest, with probes on final-layer activations used to estimate hallucination risk with over 80% accuracy across hundreds of datasets.

**Question-Only Linear Probes (March 2026):**
Residual stream activations for all model layers are extracted at the last token of the question, prior to sampling. The research shows that for models that answer "I don't know" without being explicitly prompted, doing so correlates with the question's position along the in-advance correctness direction, suggesting this vector also captures an implicit confidence axis.

**Self-Correction and Abstention:**
Correctness can be predicted directly from an LLM's hidden state while the chain-of-thought is being generated, not only after initial question or the final answer. Additionally, internal signals enable early interventions such as switching to self-reflection or to an alternative decoding strategy as soon as the internal probe flags low confidence.

**Probe-Based Methods (January 2026):**
Gnosis is a lightweight self-awareness mechanism that enables frozen LLMs to perform intrinsic self-verification by decoding signals from hidden states and attention patterns.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03cb0a37-3d18-46e3-8a58-1f1eccf6138a",
  "isSidechain": false,
  "promptId": "157d3033-198f-4187-a348-8e3127be4a36",
  "type": "user",
  "uuid": "c34fb4be-0716-459d-a797-1910abedf6a3",
  "toolUseResult": {
    "query": "LLM correctability prediction probe-gated self-correction abstention 2026 hidden state",
    "results": [
      {
        "tool_use_id": "srvtoolu_017Ykdn7M2JP3yZocuNSNnTS",
        "content": [
          {
            "title": "Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs",
            "url": "https://www.medrxiv.org/content/10.1101/2025.09.17.25336018.full.pdf"
          },
          {
            "title": "No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes",
            "url": "https://arxiv.org/html/2509.10625v3"
          },
          {
            "title": "Temporal Predictors of Outcome in Reasoning Language Models",
            "url": "https://arxiv.org/pdf/2511.14773"
          },
          {
            "title": "Latent Space Chain-of-Embedding Enables Output-free LLM Self-Evaluation",
            "url": "https://arxiv.org/pdf/2410.13640"
          },
          {
            "title": "Probing Hidden States for Calibrated, Alignment-Resistant Predictions in LLMs",
            "url": "https://www.medrxiv.org/content/10.1101/2025.09.17.25336018v2.full.pdf"
          },
          {
            "title": "[2512.20578] Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits",
            "url": "https://arxiv.org/abs/2512.20578"
          }
        ]
      },
      "Based on the search results, I found several relevant papers from 2026 addressing LLM correctability prediction using hidden states and related techniques:\n\n## Key Research Findings:\n\n**Correctability Prediction from Hidden States:**\nResearchers train probes, small classifiers that take in hidden states and predict properties of interest, with probes on final-layer activations used to estimate hallucination risk with over 80% accuracy across hundreds of datasets.\n\n**Question-Only Linear Probes (March 2026):**\nResidual stream activations for all model layers are extracted at the last token of the question, prior to sampling. The research shows that for models that answer \"I don't know\" without being explicitly prompted, doing so correlates with the question's position along the in-advance correctness direction, suggesting this vector also captures an implicit confidence axis.\n\n**Self-Correction and Abstention:**\nCorrectness can be predicted directly from an LLM's hidden state while the chain-of-thought is being generated, not only after initial question or the final answer. Additionally, internal signals enable early interventions such as switching to self-reflection or to an alternative decoding strategy as soon as the internal probe flags low confidence.\n\n**Probe-Based Methods (January 2026):**\nGnosis is a lightweight self-awareness mechanism that enables frozen LLMs to perform intrinsic self-verification by decoding signals from hidden states and attention patterns."
    ],
    "durationSeconds": 10.414088754999975,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "03cb0a37-3d18-46e3-8a58-1f1eccf6138a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "c34fb4be-0716-459d-a797-1910abedf6a3",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM correctability prediction proposal",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba"
}
```

---

### Assistant

_source line 35 · 2026-05-19T21:15:24.875Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to make my assessment. Let me synthesize my findings:

1. **CoRL venue mismatch**: This is a critical issue. CoRL 2026 is specifically about robot learning - topics like imitation learning, reinforcement learning for robots, sim-to-real transfer, robot perception, etc. This proposal is purely about LLM internal representations and self-correction probing - it has ZERO robotics content. This is a fundamental venue mismatch that would result in a desk reject.

2. **Idea quality assessment**:
   - The proposal is about predicting which LLM errors are self-correctable using enhanced probes on internal representations
   - I've verified that the foundational papers are real: PANL establishes the 0.614 AUROC baseline for correctability prediction, multi-layer ensembling and SAE dissociation techniques have been validated in related work, and CoRefine demonstrates practical self-correction approaches
   - The core novelty hinges on combining the PANL correctability signal with multi-signal probing methods that have shown promise elsewhere, but this feels incremental rather than a significant conceptual advance
   - The three-way gating mechanism with abstention adds some originality compared to CoRefine, though the representational geometry analysis in Phase 3b is more of an analytical contribution than a methodological one
   - I'm questioning whether simpler baselines would suffice: CoRefine already achieves 92.6% halt precision with output-level confidence, and I could potentially just adjust the PANL probe threshold rather than building an elaborate multi-signal system

The core risk here is that the transfer hypothesis—applying multi-layer ensembling techniques from deception detection to correctability—is speculative and unvalidated. The proposal is methodologically dense but the actual novelty feels thin relative to its complexity. The "correctability as a second-order property" angle is conceptually interesting, though the claim that it demands fundamentally different probing approaches is still speculative.

There's also a critical venue mismatch: CoRL is a robotics conference, and this work has no connection to robotics whatsoever. This would face desk rejection regardless of quality. The paper belongs at ACL, EMNLP, NeurIPS, ICML, or ICLR instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c34fb4be-0716-459d-a797-1910abedf6a3",
  "isSidechain": false,
  "requestId": "req_011CbCcuivChFEmnxyLQUrTY",
  "type": "assistant",
  "uuid": "eac27492-b1b1-46d0-95c2-c400a6f4884e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQDcBCkVCDazbM2Tu5mmSN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 745,
      "cache_read_input_tokens": 31189,
      "output_tokens": 5072,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 745,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5072,
          "cache_read_input_tokens": 31189,
          "cache_creation_input_tokens": 745,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 745
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

_source line 36 · 2026-05-19T21:16:59.419Z_

Now I have sufficient information to make my assessment. Let me compile the evaluation.

---

```
【阶段】: Triage

【⚠️ 致命性前置问题：投稿场地严重不匹配】

CoRL (Conference on Robot Learning) 2026 的 scope 明确要求论文"focus on a core robotics problem"，
涵盖的主题包括 imitation learning、reinforcement learning for robots、sim-to-real transfer、
robot perception、learned manipulation and locomotion 等。

本 proposal 的主题是"LLM 内部表征的 correctability 预测 + probe-gated 自我纠错"——
**与机器人学习零关联**。不涉及任何物理系统、传感器、执行器、或 sim-to-real 问题。
按 CoRL 2026 CFP 的 scope，本文大概率在 desk reject 阶段即被淘汰。

适合的投稿场地：ACL / EMNLP / NeurIPS / ICML / ICLR。

如果投稿目标确实是 CoRL，以下评估中的概率应直接视为 ≈0%。
以下评估假设投稿目标改为合适的 NLP/ML 顶会（如 ACL/EMNLP 2026 或 NeurIPS 2026）。

---

【领域调研】:

- [How LLMs Detect and Correct Their Own Errors (arXiv:2604.22271)](https://arxiv.org/abs/2604.22271) (2026):
  建立 PANL correctability signal，correctability AUROC 0.614（own-generated errors），
  error detection AUROC 0.986。本 proposal 的直接前序工作和 baseline。

- [Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling (arXiv:2604.13386)](https://arxiv.org/abs/2604.13386) (2026):
  多层 ensemble stacking 在 deception detection 上 AUROC 0.510→0.910。
  本 proposal 的核心技术灵感来源，但该结果仅在 deception 任务上验证。

- [Are LLM Uncertainty and Correctness Encoded by the Same Features? (arXiv:2604.19974)](https://arxiv.org/abs/2604.19974) (2026):
  SAE 分解发现 uncertainty 和 correctness 由功能性不同的 feature population 编码，
  confounded features 仅 102/1057。本 proposal 的 SAE-guided probe 设计灵感来源。

- [CoRefine (arXiv:2602.08948)](https://arxiv.org/abs/2602.08948) (2026):
  output-level confidence 三路路由（halt/rethink/alternative），92.6% halt precision。
  最接近的 system-level 竞争工作。

- [Gnosis / Can LLMs Predict Their Own Failures? (arXiv:2512.20578)](https://arxiv.org/abs/2512.20578) (2025):
  多信号融合 correctness prediction，hidden-only 0.78–0.92 AUROC。
  证明 multi-signal 方法能显著提升 correctness 预测，但做的是 correctness 而非 correctability。

- [Attention Head Entropy (arXiv:2602.13699)](https://arxiv.org/abs/2602.13699) (2026):
  per-head entropy 在 OOD correctness prediction 上 +0.06 AUROC absolute。

- [Probing for Arithmetic Errors (arXiv:2507.12379)](https://arxiv.org/abs/2507.12379) (2025):
  probe-guided selective re-prompting，仅 6–12% 实际纠正率。
  展示了 probe-gated correction 的可行性但也暴露了其局限。

- [Knowing When to Quit (arXiv:2604.18419)](https://arxiv.org/abs/2604.18419) (2026):
  value-function probes for dynamic abstention。相邻工作，但不 probe correctability。

- [Interpretability without Actionability (arXiv:2603.18353)](https://arxiv.org/abs/2603.18353) (2026):
  98.2% detection AUROC 但仅 20–24% correction via steering，揭示 knowledge-action gap。

- 调研总结：该领域在 2025-2026 年极其活跃。correctness prediction from hidden states 已有
  多条成熟路线（Gnosis, attention entropy, confidence manifold）。"correctability"作为独立
  预测目标由 PANL 论文首次提出（2026.04），尚未有后续跟进工作发表。本 proposal 定位为
  PANL 的直接后续改进 + 系统化分析，时效性好但本质上是 incremental follow-up。

---

【Trivial Alternative 检验】:

存在明确的 trivial alternative 威胁：

1. **简单 MLP 替代**: PANL 论文用的是 single-layer logistic regression on single token。
   最 trivial 的 follow-up 是换成 2-layer MLP + 多 token 拼接——无需 SAE 分析、
   crosscoder features、attention entropy 等复杂组件。如果这个简单变体就能把 AUROC 
   从 0.614 提到 0.70+，那本 proposal 90% 的工程量（SAE-guided selection, Phase 3b 
   geometry analysis, Wait-feature extraction）就显得 over-engineered。

2. **Output-level 方法已很强**: CoRefine 用 output-level logprobs 实现三路路由，
   halt precision 92.6%。本 proposal 声称 hidden-state probes 应优于 output-level signals，
   但这个 claim 完全未经验证。如果 hidden-state probe 仅在 correctability AUROC 上
   略优于 output-level confidence threshold（比如 0.72 vs 0.70），那巨大的额外复杂度
   （多层提取、SAE训练、attention 计算）带来的增量价值极低。

**增量价值在哪？** 增量价值 *如果存在* 在于：(a) correctability 确实是一个需要 hidden-state
才能预测的 property，output-level signals 做不到；(b) SAE-guided feature selection 
确实显著优于 naive multi-layer probing。但这两个都是未验证的假设。

---

【前提假设检验】:

核心 claim 的逻辑链中，以下环节是未经验证的假设：

1. **"Multi-layer ensembling 从 deception 迁移到 correctability"**:
   这是 Phase 0 要测试的假设，但也是整个 proposal 的核心赌注。Deception detection 
   和 correctability prediction 是根本不同的任务——deception 有明确的 "model knows 
   the truth but says otherwise" 的对比结构，而 correctability 是 "model's correction 
   mechanism can reach the right answer" 的二阶属性。没有先验理由认为二者的层间编码
   特性相似。proposal 自身也承认这一点，但仍将其作为核心技术路线。

2. **"Correctability 需要 target confounded feature intersection"**:
   这是从 arXiv:2604.19974 外推的推测。该论文分析的是 correctness prediction，
   不是 correctability。从 "correctness 的 confounded features 很重要" 到 
   "correctability 的 confounded features 也很重要" 是一个类比跳跃，
   没有理论或实证支撑。

3. **"Hidden-state probes 优于 output-level signals for correctability"**:
   PANL 论文展示的是 hidden-state 可以 *detect* correctability（虽然 AUROC 低），
   但没有和 output-level alternatives 做对比。本 proposal 隐含假设 hidden-state 
   信号更丰富，但 CoRefine 用 output-level signals 已经很有效。这个假设可能不成立。

4. **"Correctability 作为 second-order property 有不同的 representational geometry"**:
   这是 Phase 3b 的核心假设。但 "second-order" 这个 framing 本身是作者自己提出的
   概念框架，目前没有理论依据证明 correctability 在表征空间中的几何性质必然不同于 
   correctness。如果实验发现二者几何性质类似，Phase 3b 的 narrative 就塌了。

---

【3 维度打分】:

1. **Novelty: 弱-中** — 
   核心贡献是将已有的 multi-signal probing 技术（multi-layer ensemble from 2604.13386,
   attention entropy from 2602.13699, SAE analysis from 2604.19974）应用到一个新的 
   prediction target（correctability）。这是典型的 "technique transfer" 工作：
   把在任务 A 上验证过的方法用到相关任务 B 上。PANL 论文（2604.22271）刚于 2026.04 
   发表，本 proposal 本质上是其直接 follow-up。"Correctability 作为独立预测目标"
   的 framing novelty 已被 PANL 论文占据。本 proposal 的独立新贡献是：
   (i) 测试 multi-layer ensemble 迁移性——这更像一个实验报告而非方法创新；
   (ii) SAE feature decomposition for correctability——有一定 analytical novelty，
   但本质是将 2604.19974 的框架换一个分析对象；
   (iii) 三路 gating with abstention——与 CoRefine 有差异但差异程度有限。
   proposal 通过堆叠大量 phases 和分析来制造"多贡献"的印象，但剥去表层后，
   核心 novelty delta 较薄。

2. **Significance: 中** — 
   研究问题本身重要且及时。LLM self-correction 是当前热门方向，
   区分 correctable vs. uncorrectable errors 是一个有实际价值的 framing。
   但影响力受限于以下因素：
   (a) 问题的 practical impact 取决于 probe 能否达到足够高的 AUROC（比如 0.85+），
   而 proposal 自身对此不乐观（Phase 0 success criterion 仅为 0.70）；
   (b) 如果 probe AUROC 仅从 0.614 提到 0.70-0.75，gating 的实际效用有限——
   比如 arXiv:2507.12379 显示 probe-guided re-prompting 仅 6-12% correction rate；
   (c) Phase 3b 的 representational analysis 有学术价值，但如果结论是 
   "correctability 和 correctness 几何性质差不多"，那 significance 大打折扣。
   总体而言，如果核心发现是 positive（比如 AUROC 0.85+），审稿人会说 "interesting 
   and useful"，但不会说 "surprising"——因为 multi-signal 优于 single-signal 
   是 expected。

3. **Related Work: 强** — 
   proposal 对 related work 的覆盖极其全面和细致。引用的关键论文（PANL, 
   multi-layer ensembling, SAE dissociation, CoRefine, Gnosis, Confidence Manifold 等）
   都真实存在且描述准确。与 CoRefine 的差异化定位清晰且诚实。
   对 concurrent work（arXiv:2507.12379, 2504.05419, 2604.18419, 2506.12217）
   的覆盖也很到位。唯一轻微的问题是：proposal 在 related work 中花太多篇幅
   为自己的方法做 motivation，读起来更像 introduction 而非中立的 landscape survey。

---

【概率估计】: [15% - 28%] 中位 20%

【估计理由】: 
Novelty 是限制上界的核心维度。这本质上是一个 technique-transfer + follow-up 工作：
将已在 deception/correctness 任务上验证过的 multi-signal probing 方法应用到 
correctability 这个新 target 上。核心 framing novelty（correctability 作为独立 target）
已被 PANL 论文占据。proposal 的独立贡献——multi-layer ensemble transfer 测试、
SAE feature decomposition、三路 gating——每一项单独看都不够撑一篇 top venue 论文，
组合在一起虽然构成了完整 story，但有"多个弱贡献拼凑"的风险。

如果核心结果是 positive（AUROC 大幅提升 + gating 显著优于 baselines），
可以靠 empirical strength 弥补 novelty 的不足，概率上界可达 28%。
如果核心结果 marginal（AUROC 仅小幅提升），则 Phase 3b 的 analysis contribution
也难以独立支撑，概率下限 15%。

Significance 中等，不构成加分也不构成硬伤。
Related work 覆盖强，是一个正面因素但不足以弥补 novelty 短板。

**重申：如果投 CoRL 2026，概率 ≈ 0%，因为完全不在 scope 内。**

【主要风险】:
1. **Novelty 不足 / "Incremental follow-up" 质疑**: 审稿人很可能指出本文是 PANL 论文
   的直接 engineering follow-up，核心创新不在于新 insight 而在于"多信号拼接"，
   这在 probing 文献中已是 well-trodden path（Gnosis, SWIFT, attention entropy 等
   都做过类似的 multi-signal fusion for correctness）。

2. **核心赌注失败风险**: 如果 multi-layer ensemble 在 correctability 上的提升远不如
   在 deception 上的提升（比如 0.614→0.66 而非 0.614→0.75+），则整个 proposal 
   的叙事基础崩塌。Phase 3b 虽然 robust to negative results，但一篇"我们发现 
   correctability 很难 probe"的 analysis paper 在 top venue 的接受门槛很高。
```

Sources:
- [How LLMs Detect and Correct Their Own Errors (PANL paper)](https://arxiv.org/abs/2604.22271)
- [Linear Probe Accuracy Scales with Model Size and Benefits from Multi-Layer Ensembling](https://arxiv.org/abs/2604.13386)
- [Are LLM Uncertainty and Correctness Encoded by the Same Features?](https://arxiv.org/abs/2604.19974)
- [CoRefine: Confidence-Guided Self-Refinement](https://arxiv.org/abs/2602.08948)
- [Gnosis: Can LLMs Predict Their Own Failures?](https://arxiv.org/abs/2512.20578)
- [Probing for Arithmetic Errors in Language Models](https://arxiv.org/abs/2507.12379)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eac27492-b1b1-46d0-95c2-c400a6f4884e",
  "isSidechain": false,
  "requestId": "req_011CbCcuivChFEmnxyLQUrTY",
  "type": "assistant",
  "uuid": "ce47e0ca-ed7b-4152-9b7e-8fd376595d9b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQDcBCkVCDazbM2Tu5mmSN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 745,
      "cache_read_input_tokens": 31189,
      "output_tokens": 5072,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 745,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5072,
          "cache_read_input_tokens": 31189,
          "cache_creation_input_tokens": 745,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 745
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Can LLMs Predict Their Own Correctability? Multi-Signal Probing for Selective Self-Correction  ## Description We…",
  "leafUuid": "ce47e0ca-ed7b-4152-9b7e-8fd376595d9b",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate LLM correctability prediction proposal",
  "sessionId": "c850925d-dde6-4896-9e34-cafecb7b59ba"
}
```

---
