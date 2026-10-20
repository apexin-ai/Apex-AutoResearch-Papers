# Research conversation: I need you to help me compose a very large JSON object for a revised research proposal. I'll provide all the content — I

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 4
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a57e08d2da4cfab3d.jsonl`
- **Structured JSON:** [`acb70259b756ed643fc4.json`](../../sessions/ac/acb70259b756ed643fc4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

4 recorded events

### User

_source line 1 · 2026-05-19T13:35:44.344Z_

I need you to help me compose a very large JSON object for a revised research proposal. I'll provide all the content — I need you to output it as a single, valid, complete JSON object. Please output ONLY the JSON, nothing else.

Here is the complete content for each field. Please assemble into valid JSON:

{
  "change_type": "major",
  "title": "Disentangling Competing Calibration Biases via Geometry-Aware Activation Steering",
  
  "core_problem": "LLM miscalibration arises from at least two competing biases — choice-supportive bias (CSB, inflating confidence in initial answers) and contradictory-evidence overweighting (CEO, causing excessive confidence revision under criticism) — that require opposing corrections. Existing calibration methods apply uniform corrections that cannot simultaneously address biases pulling confidence in opposite directions. Recent work reveals two deeper obstacles. First, a classification-correction gap (Liu, 2605.05715): failure-mode directions that are linearly decodable may not be linearly steerable due to entanglement with task-critical computation (specificity ratio ≤0.152), meaning that even if competing biases can be identified in activations, correcting them requires knowing not just WHICH bias dominates but WHETHER each bias direction is steerable. Second, even principled adaptive frameworks like MERA (Hedström et al., ICML 2025) that optimize intervention strength and abstain when correction is unsafe still treat errors monolithically — they cannot decompose miscalibration into opposing sources or route different bias types to different intervention strategies. The rapidly maturing nonlinear steering landscape (ODESteer, ICLR 2026; Curveball Steering, 2026; FLAS, 2026) provides powerful general-purpose alternatives to linear steering, yet none address the diagnosis problem: which competing bias dominates per-instance, and what is its steerability profile? Can we jointly diagnose per-instance bias dominance AND steerability to apply targeted, manifold-preserving corrections where possible and graceful degradation where not?",

  "opportunity": "Kumaran et al. (Nature Machine Intelligence, 2026; arXiv 2507.03120) identified that LLM miscalibration results from two mechanistically distinct behavioral biases in Gemma 3, GPT-4o, and o1-preview: choice-supportive bias inflates confidence in selected answers, while contradictory-advice overweighting causes models to over-react to opposing evidence. Miao & Ungar (arXiv 2603.25052, 2026) independently showed that calibration and verbalized confidence signals are encoded linearly but orthogonally in the residual stream across three 7-8B models, establishing that confidence-related constructs have accessible geometric structure. Liu (arXiv 2605.05715, May 2026) demonstrated a critical classification-correction gap: linearly decodable failure directions (71.6% balanced accuracy) yield Δ≈0 under 29 steering configurations because the failure directions have 85-88% overlap with task-critical computation — but crucially, a learned non-linear residual MLP achieves Δ=+2.8pp where all linear methods fail, and the decodable signal still supports selective abstention (AUROC 0.610). Hedström et al. (MERA, ICML 2025; arXiv 2510.13290) established that steering benefits from principled adaptive strength calibration and provable non-degradation guarantees via constrained optimization (min ‖v‖² s.t. p̂(h+v) ≤ α) — but MERA's monolithic error probe cannot distinguish between calibration errors arising from opposing bias sources. Meanwhile, the nonlinear steering landscape has rapidly matured: ODESteer (Chen et al., ICLR 2026; arXiv 2602.17560) unified existing methods under a barrier-function ODE framework with multi-step adaptive steering; Curveball Steering (Raval et al., arXiv 2603.09313, Mar 2026) introduced polynomial kernel PCA to respect curved activation geometry; and FLAS (arXiv 2605.05892, May 2026) learned concept-conditioned velocity fields that first outperformed prompting on AxBench. The 'Confidence Manifold' study (arXiv 2602.08159) found correctness signals occupy only 3-8 dimensions with simple mean-shift geometry across 9 models, suggesting that calibration-related directions may have more favorable specificity profiles than entangled failure modes. The convergence of (a) identified competing biases, (b) linear confidence encoding evidence, (c) the decodable-steerable distinction with quantitative diagnostics, (d) both norm-preserving rotation (Spherical Steering, ICML 2026) and adaptive frameworks (MERA), (e) nonlinear steering alternatives for when linear methods fail, and (f) collateral-damage-aware optimization (COAST, 2605.01167) creates an opportunity for a principled pipeline: decompose calibration error into competing biases, assess per-direction steerability, and route to the appropriate intervention — extending MERA's adaptive principle from monolithic to bias-specific.",

  "landscape": "Kumaran et al. (Nature MI, 2026) identified competing biases (CSB and CEO) via behavioral experiments on Gemma 3, GPT-4o, and o1-preview but proposed no correction framework and provided no mechanistic (activation-level) evidence. Miao & Ungar (arXiv 2603.25052, 2026) demonstrated that calibration accuracy and verbalized confidence are linearly encoded but orthogonal in 7-8B models (cosine similarity <0.04 across layers), and introduced adaptive steering achieving 4-7× ECE improvement — but they target the confidence-accuracy misalignment gap, not the competing bias structure. Tsujimura & Tagade (arXiv 2508.17182, Aug 2025) decomposed LLM assertiveness into emotional and logical sub-components via unsupervised clustering on Llama-3.2-1B-Instruct (645 samples), finding two clusters in high-assertive representations — methodologically adjacent but critically different: their decomposition is descriptive (post-hoc ChatGPT-labeled clusters) rather than causally grounded in identified cognitive biases, uses a single 1B model, reports no calibration metrics, and addresses assertiveness rather than calibration. The 'Wired for Overconfidence' paper (2604.01457, April 2026) identifies overconfidence circuits in Qwen2.5-3B and Llama-3.2-3B, achieving 96.9% ECE reduction on PopQA via monolithic activation steering, but only tests 3B models and treats overconfidence as a single phenomenon.\n\nLiu (arXiv 2605.05715, May 2026) is the most directly relevant advance on the decodable-steerable gap: linearly decodable failure directions (71.6% balanced accuracy on Llama-3.1-8B) yield Δ≈0 across five families of linear steering (29 configurations) because the failure direction has 85-88% overlap with task-critical computation (specificity ratio ≤0.152). Three convergent evidence lines confirm entanglement: low specificity, shared-direction steering damages accuracy (-12.1pp), and LEACE concept erasure damages accuracy (-3.6pp). A learned non-linear bottleneck MLP (4096→64→4096) achieves Δ=+2.8pp (p=0.025) where linear methods fail, and selective abstention outperforms 5 uncertainty baselines (AUROC 0.610). However, this was studied for medical overthinking, a single failure mode.\n\nHedström et al. (MERA, ICML 2025; arXiv 2510.13290) established the most principled framework for selective steering to date: MERA solves a constrained optimization problem (min ‖v‖² s.t. p̂(h+v) ≤ α) to derive per-instance adaptive steering strength, and calibrates the intervention threshold α* with provable non-degradation guarantees via Hoeffding bounds with Bonferroni correction — either finding a statistically significant improvement or abstaining. MERA can be applied on top of existing steering methods. However, MERA operates with a single monolithic error probe and a single linear steering direction; it cannot decompose calibration errors into opposing sources (CSB vs. CEO) or route to different intervention types based on per-direction steerability assessment. MERA also acknowledges its inherently linear intervention as a limitation.\n\nThe nonlinear steering landscape has matured rapidly. ODESteer (Chen et al., ICLR 2026; arXiv 2602.17560) formulated a unified ODE-based framework where identifying a steering direction is equivalent to designing a barrier function from control theory, enabling multi-step adaptive steering via numerical ODE solvers — achieving consistent improvements on TruthfulQA, UltraFeedback, and RealToxicityPrompts across Falcon-7B, Mistral-7B, LLaMA3.1-8B, and Qwen2.5-7B. Curveball Steering (Raval et al., arXiv 2603.09313, Mar 2026) used polynomial kernel PCA to perform interventions in a curved feature space rather than globally linear directions, demonstrating up to +47% improvement over linear steering in high-curvature regimes (κ>8) on Llama-3.2-1B and Phi-3.5-mini — but is tested only on behavioral attributes (power-seeking, corrigibility), not calibration. FLAS (arXiv 2605.05892, May 2026) learned a concept-conditioned velocity field via flow matching, becoming the first steering method to consistently outperform prompting on AxBench (harmonic mean 1.015-1.113), with a 97.6-255M parameter FlowBlock — a powerful but heavy general-purpose approach. These nonlinear methods address the geometric limitations of linear steering but do not provide bias decomposition or steerability-based routing.\n\nJi et al. (EMNLP 2025) modulates a single Verbal Uncertainty Feature direction, reducing hallucinations by ~30%, capturing only the net effect of competing biases. Joshi et al. (EMNLP 2025) found a single calibration direction but did not decompose it. CORAL (arXiv 2602.06022, Feb 2026) achieves 49% ECE improvement via correctness-subspace probing on 7B models but uses a single MLP probe direction. The 'Confidence Manifold' study (arXiv 2602.08159, Feb 2026) found correctness signals occupy 3-8 dimensions with simple mean-shift geometry across 9 models from 5 families, and causally validated via steering (10.9pp error rate change) — the low dimensionality and linear separability contrasts with Liu's high-entanglement finding for overthinking, suggesting calibration-related directions may have more favorable specificity profiles. Wang & Stengel-Eskin (ICLR 2026) introduced DINCO to normalize suggestibility bias via self-generated distractors at the output level. Zhuang et al. (arXiv 2025) proposed RDG to alleviate choice-supportive bias through fine-tuning but did not address CEO. 'Breaking the Mirror' (arXiv 2509.03647) found that self-preference bias 'spans multiple or nonlinear directions,' achieving 97% unjustified bias reduction but with instability on legitimate cases.\n\nOn the steering methodology side: Spherical Steering (arXiv 2602.08169, ICML 2026) performs norm-preserving geodesic rotation, outperforming addition-based baselines by +10% on TruthfulQA. Selective Steering (Dang & Ngo, arXiv 2601.19375, Jan 2026) independently developed norm-preserving rotation with discriminative layer selection, achieving 5.5× higher attack success rates with zero perplexity violations across 8 models. COAST (Nguyen et al., arXiv 2605.01167, May 2026) formalizes collateral damage from steering as unintended alignment changes along non-target feature directions, achieving up to 30% improvement over Angular Steering. AUSteer (arXiv 2602.04428) decomposes block activations into fine-grained atomic units. CLAS (arXiv 2604.24693) dynamically adapts steering strengths per-context. 'Steered LLM Activations are Non-Surjective' (2604.09839) formally proved that additive steering pushes activations off-manifold.\n\nNo existing method jointly decomposes calibration error into competing biases, assesses the steerability of each bias direction, and routes to bias-specific interventions. MERA provides adaptive strength and abstention but is monolithic and linear; the nonlinear methods (ODESteer, Curveball, FLAS) provide powerful alternatives to linear steering but lack bias decomposition and steerability diagnosis. DBS-v2 fills this gap by combining bias-grounded decomposition with steerability-aware routing, using MERA's adaptive framework as a building block for steerable directions and Liu's nonlinear MLP for entangled ones.",

  "inspired_by": "Gap: Competing biases create non-uniform miscalibration patterns that even adaptive monolithic methods like MERA cannot optimally correct (Kumaran et al. 2026), while the classification-correction gap (Liu, 2605.05715) shows that decodable directions are not necessarily steerable. Pattern: Theory-driven contrastive probing (Miao & Ungar 2026) + steerability diagnostics (specificity ratio, Liu 2026) + adaptive intervention with non-degradation guarantees (MERA, ICML 2025) + nonlinear fallback when linear fails (Liu's MLP finding, supported by the broader nonlinear landscape of ODESteer/Curveball/FLAS). Untried combination: Cognitive-bias-grounded contrastive stimuli → per-instance bias diagnosis → specificity-informed intervention routing (MERA-wrapped Spherical Steering for steerable directions / lightweight nonlinear MLP for entangled directions / statistical abstention), with the hypothesis that CSB and CEO may have asymmetric steerability profiles.",

  "approach": "We design DBS-v2 (Disentangled Bias Steering) in three phases, incorporating the critical decodable-steerable distinction (Liu, 2605.05715) and streamlined to a focused experimental matrix of 3 models × 3 datasets × 3 intervention routes.\n\n**Phase 1 — Assumption Validation & Steerability Assessment (Weeks 1-5):**\n\n*Phase 1A — Separability (Weeks 1-3):* We construct two contrastive stimulus sets: for CSB, we compare hidden states when the model reviews its own prior answer vs. a fresh unattributed answer (eliciting choice-supportive inflation); for CEO, we compare states when contradictory expert advice is present vs. absent (eliciting evidence overweighting). Using difference-in-means on these contrastive pairs, we extract candidate bias directions in the residual stream. We validate separability via: (a) cosine similarity between candidate directions, (b) principal angle analysis between CSB and CEO subspaces using the methodology of Miao & Ungar (2026), (c) PCA to assess whether 2 directions capture sufficient variance vs. requiring higher-dimensional subspaces, and (d) cross-prediction ablations to confirm removing one bias subspace does not collapse the other. If CSB and CEO directions show cosine similarity >0.3 or shared variance >15%, we activate the separability fallback: extracting a multi-direction bias subspace via SAE-derived features and training a subspace projection classifier.\n\n*Phase 1B — Steerability Diagnostics (Weeks 3-5):* Even if CSB and CEO are separable, steering along identified directions may fail if those directions are entangled with task-critical computation. For each identified bias direction, we compute: (a) the **specificity ratio** — the proportion of mode-specific variance vs. shared variance with the correct-vs-incorrect subspace, following Liu's shared-specific decomposition methodology; (b) **LEACE concept erasure test** — applying concept erasure to each bias direction and measuring accuracy damage as causal evidence of entanglement; (c) **pilot linear steering test** — applying small-magnitude Spherical Steering along each direction and measuring both calibration improvement and accuracy impact.\n\nCritically, we do NOT pre-commit to fixed routing thresholds. The specificity ratio boundaries proposed by Liu (≤0.152 for overthinking where linear fails; ~0.999 for refusal where linear succeeds) provide initial reference points, but the actual relationship between specificity and steering effectiveness for calibration biases is an open empirical question. We instead LEARN the routing thresholds by sweeping specificity cutoffs on a held-out validation set and reporting the full specificity-vs-effectiveness curve as a primary empirical contribution. We hypothesize that CSB and CEO may have asymmetric specificity profiles — one may be more steerable than the other — which would provide a mechanistic explanation for why monolithic calibration steering sometimes succeeds partially.\n\nPhase 1 results constitute an independent contribution: the first joint separability-and-steerability assessment of behaviorally-identified competing biases, providing the field's first specificity ratio measurements for calibration-related bias directions.\n\n**Phase 2 — Per-Instance Bias Diagnosis (Weeks 4-7):** A lightweight logistic probe (or, in the fallback case, a small MLP) trained on per-instance projection magnitudes onto each bias direction classifies which bias dominates for a given query. We stratify by difficulty: on easy questions where models are already confident, CSB likely dominates; on hard questions under criticism, CEO likely dominates. The probe output provides a continuous dominance score. The Phase 1B steerability assessment informs a per-direction intervention routing table, so the probe determines both which bias is active and which intervention to apply.\n\n**Phase 3 — Adaptive Intervention (Weeks 6-12):** Instead of a single intervention strategy, Phase 3 implements three intervention routes informed by Phase 1B's learned steerability thresholds:\n\n*Route A — Adaptive Spherical Steering (for steerable directions):* When a bias direction has specificity above the learned threshold for effective linear intervention, we apply Spherical Steering (You et al., ICML 2026) with MERA-inspired adaptive strength: for each instance, the rotation magnitude is optimized to minimize ‖v‖² subject to the bias probe's predicted error falling below a calibrated threshold α*, following MERA's constrained optimization framework (Hedström et al., ICML 2025). This combines Spherical Steering's norm-preservation (addressing the off-manifold concern of Mishra et al., 2604.09839) with MERA's adaptive strength calibration and non-degradation guarantees. Unlike MERA applied monolithically, our adaptation operates per-bias-direction, allowing different strengths for CSB vs. CEO corrections.\n\n*Route B — Learned Non-Linear Residual Correction (for entangled directions):* When a bias direction has specificity below the learned threshold, linear steering is expected to fail. Following Liu's finding that a bottleneck residual MLP (d→64→d) achieves Δ=+2.8pp where 29 linear configurations yield Δ≈0, we train a small non-linear residual adapter per bias type. We choose this lightweight architecture (< 0.1% of model parameters) over heavier nonlinear alternatives — Curveball Steering requires kernel PCA with pre-image reconstruction, FLAS requires a 97-255M parameter FlowBlock, ODESteer requires ODE solver iterations — because Liu's calibration-specific evidence directly validates the bottleneck MLP for the regime we target (entangled failure directions), and the minimal parameter footprint preserves inference efficiency. We incorporate COAST-informed training (Nguyen et al., 2605.01167) by weighting the loss by the empirical second-moment matrix to minimize expected collateral damage along non-target feature directions.\n\n*Route C — Selective Abstention (for uncorrectable instances):* When neither Route A nor Route B improves calibration without excessive accuracy damage (> 3% degradation on validation), we leverage the decodable signal for selective abstention. Following MERA's statistical framework, we apply Hoeffding-based confidence bounds to determine whether any intervention yields statistically significant improvement; if not, we abstain and output a reliability score. This provides graceful degradation backed by MERA's provable non-degradation guarantees, extended to our bias-decomposed setting.\n\nFor intermediate-specificity directions, Route A is applied with a conservative strength cap (rotation magnitude ≤ 50% of high-specificity coefficient), falling back to Route C per-instance if collateral damage exceeds the threshold.\n\nWe evaluate on TriviaQA, MMLU, and PopQA across Gemma 4 31B (Dense), Qwen3-8B, and Llama-3.1-8B-Instruct. Metrics: ECE, Brier score, AUROC, difficulty-stratified ECE (easy/medium/hard partitions), per-direction specificity ratios, collateral damage measurements, and route-distribution analysis. Core baselines: (1) temperature scaling, (2) CORAL, (3) Miao & Ungar adaptive steering, (4) MERA applied monolithically (to isolate the contribution of bias decomposition over MERA's adaptive framework), (5) monolithic Spherical Steering (single direction, no bias decomposition), (6) monolithic non-linear residual MLP (single direction, no bias decomposition). Extended baselines in supplementary: CCPS, VUF intervention, DINCO, 'Wired for Overconfidence' replication at 3B scale.",

  "resource_estimate": {
    "manual": {
      "gpu_hours": "500-750 H100",
      "timeline": "12-16 weeks",
      "estimated_gpu_cost": "$1,250-$1,875 (H100 @ ~$2.50/hr mid-tier provider)"
    },
    "human_in_loop": {
      "gpu_hours": "400-600 H100",
      "timeline": "9-12 weeks",
      "claude_api_cost": "$250-$450 (Sonnet 4.6 for contrastive dataset generation, probing code, specificity ratio computation, adapter training, analysis)",
      "estimated_gpu_cost": "$1,000-$1,500"
    },
    "auto_research": {
      "gpu_hours": "700-1000 H100",
      "timeline": "5-8 weeks",
      "claude_api_cost": "$600-$1,000 (Opus 4.7 for experiment orchestration, validation analysis, steerability diagnostics, adapter training sweeps, ablation design)",
      "estimated_gpu_cost": "$1,750-$2,500",
      "speed_bottleneck": "Phase 1A→1B is inherently sequential (separability must be established before steerability diagnostics are meaningful). Route B adapter training requires supervision pairs from Phase 1 contrastive data. Evaluation across 3 models × 3 datasets × 3 routes + 6 baselines is parallelizable across models."
    }
  },

  "target_venues": [
    "ICLR 2027 (abstract Sep 19, full paper Sep 24, 2026 — primary target, 18 weeks; streamlined scope makes human-in-loop timeline of 9-12 weeks feasible with 6-9 weeks for writing)",
    "NeurIPS 2026 Workshops (~Aug 29, 2026 — Phase 1 separability + steerability results as standalone contribution)",
    "ARR October 2026 cycle (~Oct 15, 2026 — backup full paper targeting NAACL 2027 or EACL 2027)"
  ],

  "level": "top-tier",

  "key_references": [
    "Competing Biases underlie Overconfidence and Underconfidence in LLMs (Kumaran et al., Nature Machine Intelligence 2026; arXiv 2507.03120)",
    "Closing the Confidence-Faithfulness Gap in Large Language Models (Miao & Ungar, arXiv 2603.25052, 2026) — orthogonal calibration/confidence encoding, adaptive steering",
    "LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components (Tsujimura & Tagade, arXiv 2508.17182, 2025) — closest methodological precedent",
    "Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes (Liu, arXiv 2605.05715, May 2026) — classification-correction gap, specificity ratio diagnostic",
    "To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models (Hedström et al., ICML 2025; arXiv 2510.13290) — MERA: adaptive strength, provable non-degradation, selective abstention",
    "ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment (Chen et al., ICLR 2026; arXiv 2602.17560) — barrier-function ODE framework, multi-step adaptive steering",
    "Curveball Steering: The Right Direction To Steer Isn't Always Linear (Raval et al., arXiv 2603.09313, Mar 2026) — polynomial kernel PCA nonlinear steering",
    "Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention (arXiv 2605.05892, May 2026) — FLAS: concept-conditioned velocity fields, first method to outperform prompting on AxBench",
    "Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs (arXiv 2604.01457, 2026)",
    "Spherical Steering: Geometry-Aware Activation Rotation for Language Models (You et al., ICML 2026; arXiv 2602.08169)",
    "Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection (Dang & Ngo, arXiv 2601.19375, Jan 2026)",
    "Minimizing Collateral Damage in Activation Steering (Nguyen et al., arXiv 2605.01167, May 2026) — COAST framework",
    "Steered LLM Activations are Non-Surjective (Mishra et al., arXiv 2604.09839, 2026)",
    "A Sober Look at Steering Vectors for LLMs (Tan et al., NeurIPS 2024)",
    "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models (arXiv 2602.08159, 2026)",
    "Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators (arXiv 2509.03647, 2025)",
    "CORAL: Correctness-Optimized Residual Activation Lens (arXiv 2602.06022, 2026)",
    "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025)",
    "Calibrating Verbalized Confidence with Self-Generated Distractors (Wang & Stengel-Eskin, ICLR 2026)",
    "Calibration Across Layers: Understanding Calibration Evolution in LLMs (Joshi et al., EMNLP 2025)",
    "Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation (Zhuang et al., arXiv 2512.03082, 2025)",
    "Calibrating LLM Confidence by Probing Perturbed Representation Stability (arXiv 2505.21772, 2025)",
    "Fine-Grained Activation Steering: Steering Less, Achieving More (arXiv 2602.04428, 2026)",
    "Contextual Linear Activation Steering of Language Models (arXiv 2604.24693, 2026)"
  ],

  "description": "We propose DBS-v2 (Disentangled Bias Steering), a method that separately identifies, assesses the steerability of, and adaptively corrects two competing sources of LLM miscalibration identified by Kumaran et al. (2026): choice-supportive bias (CSB) and contradictory-evidence overweighting (CEO).\n\nA critical insight motivating this revision is that both monolithic steering (which cannot decompose competing biases) and uniform intervention strategies (which ignore the classification-correction gap) are fundamentally suboptimal. MERA (Hedström et al., ICML 2025) demonstrated that adaptive steering strength with abstention outperforms fixed steering — but MERA's single error probe cannot distinguish between opposing calibration biases. The nonlinear steering landscape (ODESteer, Curveball, FLAS) provides powerful geometry-aware alternatives — but none diagnose which bias dominates per-instance or assess per-direction steerability.\n\nThe method proceeds in three phases. Phase 1A (Separability Validation) tests whether CSB and CEO produce distinguishable activation signatures using contrastive activation probing, validated via cosine similarity, principal angle analysis, PCA dimensionality assessment, and cross-prediction ablation. Phase 1B (Steerability Assessment) computes the specificity ratio for each bias direction following Liu's (2605.05715) methodology, supplemented with LEACE concept erasure tests and pilot steering experiments. Rather than pre-committing to fixed routing thresholds (which would rest on only two empirical data points from Liu), we LEARN optimal thresholds via validation-set sweeps and report the full specificity-vs-effectiveness curve as a primary contribution. We hypothesize that CSB and CEO have asymmetric specificity profiles, explaining inconsistent monolithic steering results.\n\nPhase 2 trains a lightweight per-instance bias dominance classifier. Phase 3 implements adaptive routing: (Route A) Spherical Steering with MERA-inspired adaptive strength optimization for steerable directions — combining norm-preservation with per-instance strength calibration and non-degradation guarantees, applied per-bias rather than monolithically; (Route B) a lightweight bottleneck residual MLP (d→64→d, <0.1% parameters) for entangled directions, chosen over heavier nonlinear alternatives (Curveball/FLAS/ODESteer) based on Liu's calibration-specific validation, trained with COAST-informed collateral-damage-aware loss; (Route C) selective abstention via MERA's statistical framework when neither route safely improves calibration.\n\nWe evaluate on TriviaQA, MMLU, and PopQA across Gemma 4 31B Dense, Qwen3-8B, and Llama-3.1-8B-Instruct. Core baselines: temperature scaling, CORAL, Miao & Ungar adaptive steering, MERA (monolithic), monolithic Spherical Steering, and monolithic nonlinear MLP — isolating the contribution of bias decomposition from both the adaptive framework (vs. MERA) and the steering methodology (vs. monolithic variants). The primary contributions are: (1) the first joint separability-and-steerability assessment of competing calibration biases, with empirically-learned routing thresholds; (2) the hypothesis and test of asymmetric steerability profiles for CSB vs. CEO; (3) adaptive bias-specific intervention routing that extends MERA's monolithic adaptive framework to the multi-bias setting; and (4) principled graceful degradation from geometry-preserving rotation to nonlinear correction to abstention based on measured entanglement.",

  "project_name": "bias_disentangle_calib",
  "source": "web_research",

  "revision_notes": {
    "round1_issue_1_missing_competitor": "Tsujimura & Tagade (2508.17182) cited as closest methodological precedent, differentiated on four axes. [Carried from R1]",
    "round1_issue_2_model_names": "Fixed model names. [Carried from R1]",
    "round1_issue_3_untested_assumption": "Phase 1A retains separability tests with quantitative thresholds. [Carried from R1]",
    "round1_issue_4_steering_reliability": "Spherical Steering retained as primary Route A; augmented with MERA-inspired adaptive strength. [Extended from R1]",
    "round1_issue_5_baseline_comparison": "Contribution framing retained. MERA now added as critical baseline. [Extended from R1]",
    "round1_issue_6_behavioral_mechanistic_leap": "Phase 1A + 1B retained. [Carried from R1]",
    "round2_issue_1_critical_missing_competitor": "Liu (2605.05715) thoroughly integrated. [Carried from R2]",
    "round2_issue_2_separability_steerability_gap": "Phase 1A + 1B retained. [Carried from R2]",
    "round2_issue_3_minor_missing_references": "Selective Steering, COAST, Confidence Manifold, AUSteer, CLAS retained. [Carried from R2]",
    "round2_issue_4_nonlinear_steering_fallback": "Routes A/B/C retained with streamlined structure. [Carried from R2, simplified]",
    "round3_issue_1_MERA_baseline": "MERA (Hedström et al., ICML 2025; arXiv 2510.13290) now thoroughly integrated as BOTH a key baseline AND a building block. As baseline: MERA applied monolithically isolates the contribution of bias decomposition. As building block: Route A uses MERA-inspired constrained optimization for per-instance adaptive steering strength with non-degradation guarantees; Route C adopts MERA's Hoeffding-based statistical abstention framework. Key distinction: DBS-v2 decomposes biases (MERA treats errors monolithically), routes between intervention types based on steerability (MERA uses a single linear intervention), and operates per-bias-direction (MERA operates on a single error probe). MERA's acknowledged limitation of inherent linearity motivates Route B.",
    "round3_issue_2_nonlinear_steering_competitors": "Three nonlinear steering methods added to landscape: (a) ODESteer (Chen et al., ICLR 2026; arXiv 2602.17560) — barrier-function ODE framework unifying existing methods, multi-step adaptive steering on 4 × 7B models; (b) Curveball Steering (Raval et al., arXiv 2603.09313, Mar 2026) — polynomial kernel PCA respecting curved activation geometry, up to +47% over linear in high-curvature regimes on 1-4B models; (c) FLAS (arXiv 2605.05892, May 2026) — flow-based concept-conditioned velocity fields, first method to outperform prompting on AxBench, 97-255M parameter FlowBlock. Route B's lightweight bottleneck MLP is explicitly positioned against these: chosen for calibration-specific validation (Liu's direct evidence), minimal parameter footprint (<0.1% vs. these methods' 97M+ parameters), and inference efficiency. ODESteer/Curveball/FLAS are acknowledged as powerful general-purpose alternatives but none provide bias decomposition or steerability-based routing.",
    "round3_issue_3_venue_targeting": "AAAI 2027 dropped as primary target (July 28 deadline = ~10 weeks, infeasible). Revised: ICLR 2027 (Sep 24 full paper, ~18 weeks) as primary target — feasible with streamlined scope and human-in-loop timeline of 9-12 weeks. NeurIPS 2026 workshop (Aug 29) for Phase 1 results. ARR October 2026 as backup. ARR August (Aug 3, too tight) and AACL-IJCNLP dropped.",
    "round3_issue_4_specificity_thresholds": "Specificity ratio routing thresholds (previously ≥0.5 HIGH, 0.2-0.5 MEDIUM, <0.2 LOW) are now explicitly framed as HYPOTHESES to be empirically refined, not as calibrated boundaries. The approach now LEARNS thresholds via validation-set sweeps over specificity cutoffs and reports the full specificity-vs-effectiveness curve as a primary empirical contribution. Liu's two data points (≤0.152 for overthinking, ~0.999 for refusal) are cited as reference points only. This reframing converts a weakness (arbitrary thresholds) into a strength (the empirical threshold curve is itself a novel finding).",
    "round3_issue_5_overcomplexity": "MAJOR streamlining: (a) Models reduced from 5 to 3 (dropped Qwen2.5-3B, Llama-3.2-3B supplementary models — 'Wired for Overconfidence' comparison moved to supplementary); (b) Datasets reduced from 4 to 3 (dropped NQ-Open); (c) Routes reduced from 4 to 3 (Route D medium-specificity hybrid absorbed into Route A with conservative strength cap); (d) Core baselines reduced from 10+ to 6 (CCPS, VUF, DINCO, 'Wired for Overconfidence' replication moved to supplementary); (e) Phase 1A diagnostics reduced from 5 to 4 (dropped ICA); (f) Phase 1B diagnostics reduced from 4 to 3 (dropped within-class variance analysis, replaced cross-architecture stability with pilot steering test). Estimated GPU hours reduced ~30% (500-750 from 750-1050 manual). The streamlined matrix (3×3×3 + 6 baselines) is focused and executable within ICLR 2027 timeline."
  }
}

Please output this as a single valid JSON. Make sure all the newline characters within strings are properly escaped as \n. Output ONLY the JSON object.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f193b0a6-df13-47f8-a94f-8964b1333fc2",
  "agentId": "a57e08d2da4cfab3d",
  "type": "user",
  "uuid": "0a27125f-728d-4975-82cf-6ea279e7ecc6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "1e795d8c-c874-44f7-aace-83a8b0668b24",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T13:35:44.354Z_

```json
{
  "parentUuid": "0a27125f-728d-4975-82cf-6ea279e7ecc6",
  "isSidechain": true,
  "agentId": "a57e08d2da4cfab3d",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "cf059853-a0c0-40b1-b91a-318746991c17",
  "timestamp": "2026-05-19T13:35:44.354Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "1e795d8c-c874-44f7-aace-83a8b0668b24",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T13:35:44.355Z_

```json
{
  "parentUuid": "cf059853-a0c0-40b1-b91a-318746991c17",
  "isSidechain": true,
  "agentId": "a57e08d2da4cfab3d",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f6808b2f-168c-4f17-a8e1-91190a5559d8",
  "timestamp": "2026-05-19T13:35:44.355Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "1e795d8c-c874-44f7-aace-83a8b0668b24",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T13:39:00.834Z_



```json
{
  "change_type": "major",
  "title": "Disentangling Competing Calibration Biases via Geometry-Aware Activation Steering",
  "core_problem": "LLM miscalibration arises from at least two competing biases — choice-supportive bias (CSB, inflating confidence in initial answers) and contradictory-evidence overweighting (CEO, causing excessive confidence revision under criticism) — that require opposing corrections. Existing calibration methods apply uniform corrections that cannot simultaneously address biases pulling confidence in opposite directions. Recent work reveals two deeper obstacles. First, a classification-correction gap (Liu, 2605.05715): failure-mode directions that are linearly decodable may not be linearly steerable due to entanglement with task-critical computation (specificity ratio ≤0.152), meaning that even if competing biases can be identified in activations, correcting them requires knowing not just WHICH bias dominates but WHETHER each bias direction is steerable. Second, even principled adaptive frameworks like MERA (Hedström et al., ICML 2025) that optimize intervention strength and abstain when correction is unsafe still treat errors monolithically — they cannot decompose miscalibration into opposing sources or route different bias types to different intervention strategies. The rapidly maturing nonlinear steering landscape (ODESteer, ICLR 2026; Curveball Steering, 2026; FLAS, 2026) provides powerful general-purpose alternatives to linear steering, yet none address the diagnosis problem: which competing bias dominates per-instance, and what is its steerability profile? Can we jointly diagnose per-instance bias dominance AND steerability to apply targeted, manifold-preserving corrections where possible and graceful degradation where not?",
  "opportunity": "Kumaran et al. (Nature Machine Intelligence, 2026; arXiv 2507.03120) identified that LLM miscalibration results from two mechanistically distinct behavioral biases in Gemma 3, GPT-4o, and o1-preview: choice-supportive bias inflates confidence in selected answers, while contradictory-advice overweighting causes models to over-react to opposing evidence. Miao & Ungar (arXiv 2603.25052, 2026) independently showed that calibration and verbalized confidence signals are encoded linearly but orthogonally in the residual stream across three 7-8B models, establishing that confidence-related constructs have accessible geometric structure. Liu (arXiv 2605.05715, May 2026) demonstrated a critical classification-correction gap: linearly decodable failure directions (71.6% balanced accuracy) yield Δ≈0 under 29 steering configurations because the failure directions have 85-88% overlap with task-critical computation — but crucially, a learned non-linear residual MLP achieves Δ=+2.8pp where all linear methods fail, and the decodable signal still supports selective abstention (AUROC 0.610). Hedström et al. (MERA, ICML 2025; arXiv 2510.13290) established that steering benefits from principled adaptive strength calibration and provable non-degradation guarantees via constrained optimization (min ‖v‖² s.t. p̂(h+v) ≤ α) — but MERA's monolithic error probe cannot distinguish between calibration errors arising from opposing bias sources. Meanwhile, the nonlinear steering landscape has rapidly matured: ODESteer (Chen et al., ICLR 2026; arXiv 2602.17560) unified existing methods under a barrier-function ODE framework with multi-step adaptive steering; Curveball Steering (Raval et al., arXiv 2603.09313, Mar 2026) introduced polynomial kernel PCA to respect curved activation geometry; and FLAS (arXiv 2605.05892, May 2026) learned concept-conditioned velocity fields that first outperformed prompting on AxBench. The 'Confidence Manifold' study (arXiv 2602.08159) found correctness signals occupy only 3-8 dimensions with simple mean-shift geometry across 9 models, suggesting that calibration-related directions may have more favorable specificity profiles than entangled failure modes. The convergence of (a) identified competing biases, (b) linear confidence encoding evidence, (c) the decodable-steerable distinction with quantitative diagnostics, (d) both norm-preserving rotation (Spherical Steering, ICML 2026) and adaptive frameworks (MERA), (e) nonlinear steering alternatives for when linear methods fail, and (f) collateral-damage-aware optimization (COAST, 2605.01167) creates an opportunity for a principled pipeline: decompose calibration error into competing biases, assess per-direction steerability, and route to the appropriate intervention — extending MERA's adaptive principle from monolithic to bias-specific.",
  "landscape": "Kumaran et al. (Nature MI, 2026) identified competing biases (CSB and CEO) via behavioral experiments on Gemma 3, GPT-4o, and o1-preview but proposed no correction framework and provided no mechanistic (activation-level) evidence. Miao & Ungar (arXiv 2603.25052, 2026) demonstrated that calibration accuracy and verbalized confidence are linearly encoded but orthogonal in 7-8B models (cosine similarity <0.04 across layers), and introduced adaptive steering achieving 4-7× ECE improvement — but they target the confidence-accuracy misalignment gap, not the competing bias structure. Tsujimura & Tagade (arXiv 2508.17182, Aug 2025) decomposed LLM assertiveness into emotional and logical sub-components via unsupervised clustering on Llama-3.2-1B-Instruct (645 samples), finding two clusters in high-assertive representations — methodologically adjacent but critically different: their decomposition is descriptive (post-hoc ChatGPT-labeled clusters) rather than causally grounded in identified cognitive biases, uses a single 1B model, reports no calibration metrics, and addresses assertiveness rather than calibration. The 'Wired for Overconfidence' paper (2604.01457, April 2026) identifies overconfidence circuits in Qwen2.5-3B and Llama-3.2-3B, achieving 96.9% ECE reduction on PopQA via monolithic activation steering, but only tests 3B models and treats overconfidence as a single phenomenon.\n\nLiu (arXiv 2605.05715, May 2026) is the most directly relevant advance on the decodable-steerable gap: linearly decodable failure directions (71.6% balanced accuracy on Llama-3.1-8B) yield Δ≈0 across five families of linear steering (29 configurations) because the failure direction has 85-88% overlap with task-critical computation (specificity ratio ≤0.152). Three convergent evidence lines confirm entanglement: low specificity, shared-direction steering damages accuracy (-12.1pp), and LEACE concept erasure damages accuracy (-3.6pp). A learned non-linear bottleneck MLP (4096→64→4096) achieves Δ=+2.8pp (p=0.025) where linear methods fail, and selective abstention outperforms 5 uncertainty baselines (AUROC 0.610). However, this was studied for medical overthinking, a single failure mode.\n\nHedström et al. (MERA, ICML 2025; arXiv 2510.13290) established the most principled framework for selective steering to date: MERA solves a constrained optimization problem (min ‖v‖² s.t. p̂(h+v) ≤ α) to derive per-instance adaptive steering strength, and calibrates the intervention threshold α* with provable non-degradation guarantees via Hoeffding bounds with Bonferroni correction — either finding a statistically significant improvement or abstaining. MERA can be applied on top of existing steering methods. However, MERA operates with a single monolithic error probe and a single linear steering direction; it cannot decompose calibration errors into opposing sources (CSB vs. CEO) or route to different intervention types based on per-direction steerability assessment. MERA also acknowledges its inherently linear intervention as a limitation.\n\nThe nonlinear steering landscape has matured rapidly. ODESteer (Chen et al., ICLR 2026; arXiv 2602.17560) formulated a unified ODE-based framework where identifying a steering direction is equivalent to designing a barrier function from control theory, enabling multi-step adaptive steering via numerical ODE solvers — achieving consistent improvements on TruthfulQA, UltraFeedback, and RealToxicityPrompts across Falcon-7B, Mistral-7B, LLaMA3.1-8B, and Qwen2.5-7B. Curveball Steering (Raval et al., arXiv 2603.09313, Mar 2026) used polynomial kernel PCA to perform interventions in a curved feature space rather than globally linear directions, demonstrating up to +47% improvement over linear steering in high-curvature regimes (κ>8) on Llama-3.2-1B and Phi-3.5-mini — but is tested only on behavioral attributes (power-seeking, corrigibility), not calibration. FLAS (arXiv 2605.05892, May 2026) learned a concept-conditioned velocity field via flow matching, becoming the first steering method to consistently outperform prompting on AxBench (harmonic mean 1.015-1.113), with a 97.6-255M parameter FlowBlock — a powerful but heavy general-purpose approach. These nonlinear methods address the geometric limitations of linear steering but do not provide bias decomposition or steerability-based routing.\n\nJi et al. (EMNLP 2025) modulates a single Verbal Uncertainty Feature direction, reducing hallucinations by ~30%, capturing only the net effect of competing biases. Joshi et al. (EMNLP 2025) found a single calibration direction but did not decompose it. CORAL (arXiv 2602.06022, Feb 2026) achieves 49% ECE improvement via correctness-subspace probing on 7B models but uses a single MLP probe direction. The 'Confidence Manifold' study (arXiv 2602.08159, Feb 2026) found correctness signals occupy 3-8 dimensions with simple mean-shift geometry across 9 models from 5 families, and causally validated via steering (10.9pp error rate change) — the low dimensionality and linear separability contrasts with Liu's high-entanglement finding for overthinking, suggesting calibration-related directions may have more favorable specificity profiles. Wang & Stengel-Eskin (ICLR 2026) introduced DINCO to normalize suggestibility bias via self-generated distractors at the output level. Zhuang et al. (arXiv 2025) proposed RDG to alleviate choice-supportive bias through fine-tuning but did not address CEO. 'Breaking the Mirror' (arXiv 2509.03647) found that self-preference bias 'spans multiple or nonlinear directions,' achieving 97% unjustified bias reduction but with instability on legitimate cases.\n\nOn the steering methodology side: Spherical Steering (arXiv 2602.08169, ICML 2026) performs norm-preserving geodesic rotation, outperforming addition-based baselines by +10% on TruthfulQA. Selective Steering (Dang & Ngo, arXiv 2601.19375, Jan 2026) independently developed norm-preserving rotation with discriminative layer selection, achieving 5.5× higher attack success rates with zero perplexity violations across 8 models. COAST (Nguyen et al., arXiv 2605.01167, May 2026) formalizes collateral damage from steering as unintended alignment changes along non-target feature directions, achieving up to 30% improvement over Angular Steering. AUSteer (arXiv 2602.04428) decomposes block activations into fine-grained atomic units. CLAS (arXiv 2604.24693) dynamically adapts steering strengths per-context. 'Steered LLM Activations are Non-Surjective' (2604.09839) formally proved that additive steering pushes activations off-manifold.\n\nNo existing method jointly decomposes calibration error into competing biases, assesses the steerability of each bias direction, and routes to bias-specific interventions. MERA provides adaptive strength and abstention but is monolithic and linear; the nonlinear methods (ODESteer, Curveball, FLAS) provide powerful alternatives to linear steering but lack bias decomposition and steerability diagnosis. DBS-v2 fills this gap by combining bias-grounded decomposition with steerability-aware routing, using MERA's adaptive framework as a building block for steerable directions and Liu's nonlinear MLP for entangled ones.",
  "inspired_by": "Gap: Competing biases create non-uniform miscalibration patterns that even adaptive monolithic methods like MERA cannot optimally correct (Kumaran et al. 2026), while the classification-correction gap (Liu, 2605.05715) shows that decodable directions are not necessarily steerable. Pattern: Theory-driven contrastive probing (Miao & Ungar 2026) + steerability diagnostics (specificity ratio, Liu 2026) + adaptive intervention with non-degradation guarantees (MERA, ICML 2025) + nonlinear fallback when linear fails (Liu's MLP finding, supported by the broader nonlinear landscape of ODESteer/Curveball/FLAS). Untried combination: Cognitive-bias-grounded contrastive stimuli → per-instance bias diagnosis → specificity-informed intervention routing (MERA-wrapped Spherical Steering for steerable directions / lightweight nonlinear MLP for entangled directions / statistical abstention), with the hypothesis that CSB and CEO may have asymmetric steerability profiles.",
  "approach": "We design DBS-v2 (Disentangled Bias Steering) in three phases, incorporating the critical decodable-steerable distinction (Liu, 2605.05715) and streamlined to a focused experimental matrix of 3 models × 3 datasets × 3 intervention routes.\n\n**Phase 1 — Assumption Validation & Steerability Assessment (Weeks 1-5):**\n\n*Phase 1A — Separability (Weeks 1-3):* We construct two contrastive stimulus sets: for CSB, we compare hidden states when the model reviews its own prior answer vs. a fresh unattributed answer (eliciting choice-supportive inflation); for CEO, we compare states when contradictory expert advice is present vs. absent (eliciting evidence overweighting). Using difference-in-means on these contrastive pairs, we extract candidate bias directions in the residual stream. We validate separability via: (a) cosine similarity between candidate directions, (b) principal angle analysis between CSB and CEO subspaces using the methodology of Miao & Ungar (2026), (c) PCA to assess whether 2 directions capture sufficient variance vs. requiring higher-dimensional subspaces, and (d) cross-prediction ablations to confirm removing one bias subspace does not collapse the other. If CSB and CEO directions show cosine similarity >0.3 or shared variance >15%, we activate the separability fallback: extracting a multi-direction bias subspace via SAE-derived features and training a subspace projection classifier.\n\n*Phase 1B — Steerability Diagnostics (Weeks 3-5):* Even if CSB and CEO are separable, steering along identified directions may fail if those directions are entangled with task-critical computation. For each identified bias direction, we compute: (a) the **specificity ratio** — the proportion of mode-specific variance vs. shared variance with the correct-vs-incorrect subspace, following Liu's shared-specific decomposition methodology; (b) **LEACE concept erasure test** — applying concept erasure to each bias direction and measuring accuracy damage as causal evidence of entanglement; (c) **pilot linear steering test** — applying small-magnitude Spherical Steering along each direction and measuring both calibration improvement and accuracy impact.\n\nCritically, we do NOT pre-commit to fixed routing thresholds. The specificity ratio boundaries proposed by Liu (≤0.152 for overthinking where linear fails; ~0.999 for refusal where linear succeeds) provide initial reference points, but the actual relationship between specificity and steering effectiveness for calibration biases is an open empirical question. We instead LEARN the routing thresholds by sweeping specificity cutoffs on a held-out validation set and reporting the full specificity-vs-effectiveness curve as a primary empirical contribution. We hypothesize that CSB and CEO may have asymmetric specificity profiles — one may be more steerable than the other — which would provide a mechanistic explanation for why monolithic calibration steering sometimes succeeds partially.\n\nPhase 1 results constitute an independent contribution: the first joint separability-and-steerability assessment of behaviorally-identified competing biases, providing the field's first specificity ratio measurements for calibration-related bias directions.\n\n**Phase 2 — Per-Instance Bias Diagnosis (Weeks 4-7):** A lightweight logistic probe (or, in the fallback case, a small MLP) trained on per-instance projection magnitudes onto each bias direction classifies which bias dominates for a given query. We stratify by difficulty: on easy questions where models are already confident, CSB likely dominates; on hard questions under criticism, CEO likely dominates. The probe output provides a continuous dominance score. The Phase 1B steerability assessment informs a per-direction intervention routing table, so the probe determines both which bias is active and which intervention to apply.\n\n**Phase 3 — Adaptive Intervention (Weeks 6-12):** Instead of a single intervention strategy, Phase 3 implements three intervention routes informed by Phase 1B's learned steerability thresholds:\n\n*Route A — Adaptive Spherical Steering (for steerable directions):* When a bias direction has specificity above the learned threshold for effective linear intervention, we apply Spherical Steering (You et al., ICML 2026) with MERA-inspired adaptive strength: for each instance, the rotation magnitude is optimized to minimize ‖v‖² subject to the bias probe's predicted error falling below a calibrated threshold α*, following MERA's constrained optimization framework (Hedström et al., ICML 2025). This combines Spherical Steering's norm-preservation (addressing the off-manifold concern of Mishra et al., 2604.09839) with MERA's adaptive strength calibration and non-degradation guarantees. Unlike MERA applied monolithically, our adaptation operates per-bias-direction, allowing different strengths for CSB vs. CEO corrections.\n\n*Route B — Learned Non-Linear Residual Correction (for entangled directions):* When a bias direction has specificity below the learned threshold, linear steering is expected to fail. Following Liu's finding that a bottleneck residual MLP (d→64→d) achieves Δ=+2.8pp where 29 linear configurations yield Δ≈0, we train a small non-linear residual adapter per bias type. We choose this lightweight architecture (< 0.1% of model parameters) over heavier nonlinear alternatives — Curveball Steering requires kernel PCA with pre-image reconstruction, FLAS requires a 97-255M parameter FlowBlock, ODESteer requires ODE solver iterations — because Liu's calibration-specific evidence directly validates the bottleneck MLP for the regime we target (entangled failure directions), and the minimal parameter footprint preserves inference efficiency. We incorporate COAST-informed training (Nguyen et al., 2605.01167) by weighting the loss by the empirical second-moment matrix to minimize expected collateral damage along non-target feature directions.\n\n*Route C — Selective Abstention (for uncorrectable instances):* When neither Route A nor Route B improves calibration without excessive accuracy damage (> 3% degradation on validation), we leverage the decodable signal for selective abstention. Following MERA's statistical framework, we apply Hoeffding-based confidence bounds to determine whether any intervention yields statistically significant improvement; if not, we abstain and output a reliability score. This provides graceful degradation backed by MERA's provable non-degradation guarantees, extended to our bias-decomposed setting.\n\nFor intermediate-specificity directions, Route A is applied with a conservative strength cap (rotation magnitude ≤ 50% of high-specificity coefficient), falling back to Route C per-instance if collateral damage exceeds the threshold.\n\nWe evaluate on TriviaQA, MMLU, and PopQA across Gemma 4 31B (Dense), Qwen3-8B, and Llama-3.1-8B-Instruct. Metrics: ECE, Brier score, AUROC, difficulty-stratified ECE (easy/medium/hard partitions), per-direction specificity ratios, collateral damage measurements, and route-distribution analysis. Core baselines: (1) temperature scaling, (2) CORAL, (3) Miao & Ungar adaptive steering, (4) MERA applied monolithically (to isolate the contribution of bias decomposition over MERA's adaptive framework), (5) monolithic Spherical Steering (single direction, no bias decomposition), (6) monolithic non-linear residual MLP (single direction, no bias decomposition). Extended baselines in supplementary: CCPS, VUF intervention, DINCO, 'Wired for Overconfidence' replication at 3B scale.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "500-750 H100",
      "timeline": "12-16 weeks",
      "estimated_gpu_cost": "$1,250-$1,875 (H100 @ ~$2.50/hr mid-tier provider)"
    },
    "human_in_loop": {
      "gpu_hours": "400-600 H100",
      "timeline": "9-12 weeks",
      "claude_api_cost": "$250-$450 (Sonnet 4.6 for contrastive dataset generation, probing code, specificity ratio computation, adapter training, analysis)",
      "estimated_gpu_cost": "$1,000-$1,500"
    },
    "auto_research": {
      "gpu_hours": "700-1000 H100",
      "timeline": "5-8 weeks",
      "claude_api_cost": "$600-$1,000 (Opus 4.7 for experiment orchestration, validation analysis, steerability diagnostics, adapter training sweeps, ablation design)",
      "estimated_gpu_cost": "$1,750-$2,500",
      "speed_bottleneck": "Phase 1A→1B is inherently sequential (separability must be established before steerability diagnostics are meaningful). Route B adapter training requires supervision pairs from Phase 1 contrastive data. Evaluation across 3 models × 3 datasets × 3 routes + 6 baselines is parallelizable across models."
    }
  },
  "target_venues": [
    "ICLR 2027 (abstract Sep 19, full paper Sep 24, 2026 — primary target, 18 weeks; streamlined scope makes human-in-loop timeline of 9-12 weeks feasible with 6-9 weeks for writing)",
    "NeurIPS 2026 Workshops (~Aug 29, 2026 — Phase 1 separability + steerability results as standalone contribution)",
    "ARR October 2026 cycle (~Oct 15, 2026 — backup full paper targeting NAACL 2027 or EACL 2027)"
  ],
  "level": "top-tier",
  "key_references": [
    "Competing Biases underlie Overconfidence and Underconfidence in LLMs (Kumaran et al., Nature Machine Intelligence 2026; arXiv 2507.03120)",
    "Closing the Confidence-Faithfulness Gap in Large Language Models (Miao & Ungar, arXiv 2603.25052, 2026) — orthogonal calibration/confidence encoding, adaptive steering",
    "LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components (Tsujimura & Tagade, arXiv 2508.17182, 2025) — closest methodological precedent",
    "Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes (Liu, arXiv 2605.05715, May 2026) — classification-correction gap, specificity ratio diagnostic",
    "To Steer or Not to Steer? Mechanistic Error Reduction with Abstention for Language Models (Hedström et al., ICML 2025; arXiv 2510.13290) — MERA: adaptive strength, provable non-degradation, selective abstention",
    "ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment (Chen et al., ICLR 2026; arXiv 2602.17560) — barrier-function ODE framework, multi-step adaptive steering",
    "Curveball Steering: The Right Direction To Steer Isn't Always Linear (Raval et al., arXiv 2603.09313, Mar 2026) — polynomial kernel PCA nonlinear steering",
    "Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention (arXiv 2605.05892, May 2026) — FLAS: concept-conditioned velocity fields, first method to outperform prompting on AxBench",
    "Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs (arXiv 2604.01457, 2026)",
    "Spherical Steering: Geometry-Aware Activation Rotation for Language Models (You et al., ICML 2026; arXiv 2602.08169)",
    "Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection (Dang & Ngo, arXiv 2601.19375, Jan 2026)",
    "Minimizing Collateral Damage in Activation Steering (Nguyen et al., arXiv 2605.01167, May 2026) — COAST framework",
    "Steered LLM Activations are Non-Surjective (Mishra et al., arXiv 2604.09839, 2026)",
    "A Sober Look at Steering Vectors for LLMs (Tan et al., NeurIPS 2024)",
    "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models (arXiv 2602.08159, 2026)",
    "Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators (arXiv 2509.03647, 2025)",
    "CORAL: Correctness-Optimized Residual Activation Lens (arXiv 2602.06022, 2026)",
    "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025)",
    "Calibrating Verbalized Confidence with Self-Generated Distractors (Wang & Stengel-Eskin, ICLR 2026)",
    "Calibration Across Layers: Understanding Calibration Evolution in LLMs (Joshi et al., EMNLP 2025)",
    "Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation (Zhuang et al., arXiv 2512.03082, 2025)",
    "Calibrating LLM Confidence by Probing Perturbed Representation Stability (arXiv 2505.21772, 2025)",
    "Fine-Grained Activation Steering: Steering Less, Achieving More (arXiv 2602.04428, 2026)",
    "Contextual Linear Activation Steering of Language Models (arXiv 2604.24693, 2026)"
  ],
  "description": "We propose DBS-v2 (Disentangled Bias Steering), a method that separately identifies, assesses the steerability of, and adaptively corrects two competing sources of LLM miscalibration identified by Kumaran et al. (2026): choice-supportive bias (CSB) and contradictory-evidence overweighting (CEO).\n\nA critical insight motivating this revision is that both monolithic steering (which cannot decompose competing biases) and uniform intervention strategies (which ignore the classification-correction gap) are fundamentally suboptimal. MERA (Hedström et al., ICML 2025) demonstrated that adaptive steering strength with abstention outperforms fixed steering — but MERA's single error probe cannot distinguish between opposing calibration biases. The nonlinear steering landscape (ODESteer, Curveball, FLAS) provides powerful geometry-aware alternatives — but none diagnose which bias dominates per-instance or assess per-direction steerability.\n\nThe method proceeds in three phases. Phase 1A (Separability Validation) tests whether CSB and CEO produce distinguishable activation signatures using contrastive activation probing, validated via cosine similarity, principal angle analysis, PCA dimensionality assessment, and cross-prediction ablation. Phase 1B (Steerability Assessment) computes the specificity ratio for each bias direction following Liu's (2605.05715) methodology, supplemented with LEACE concept erasure tests and pilot steering experiments. Rather than pre-committing to fixed routing thresholds (which would rest on only two empirical data points from Liu), we LEARN optimal thresholds via validation-set sweeps and report the full specificity-vs-effectiveness curve as a primary contribution. We hypothesize that CSB and CEO have asymmetric specificity profiles, explaining inconsistent monolithic steering results.\n\nPhase 2 trains a lightweight per-instance bias dominance classifier. Phase 3 implements adaptive routing: (Route A) Spherical Steering with MERA-inspired adaptive strength optimization for steerable directions — combining norm-preservation with per-instance strength calibration and non-degradation guarantees, applied per-bias rather than monolithically; (Route B) a lightweight bottleneck residual MLP (d→64→d, <0.1% parameters) for entangled directions, chosen over heavier nonlinear alternatives (Curveball/FLAS/ODESteer) based on Liu's calibration-specific validation, trained with COAST-informed collateral-damage-aware loss; (Route C) selective abstention via MERA's statistical framework when neither route safely improves calibration.\n\nWe evaluate on TriviaQA, MMLU, and PopQA across Gemma 4 31B Dense, Qwen3-8B, and Llama-3.1-8B-Instruct. Core baselines: temperature scaling, CORAL, Miao & Ungar adaptive steering, MERA (monolithic), monolithic Spherical Steering, and monolithic nonlinear MLP — isolating the contribution of bias decomposition from both the adaptive framework (vs. MERA) and the steering methodology (vs. monolithic variants). The primary contributions are: (1) the first joint separability-and-steerability assessment of competing calibration biases, with empirically-learned routing thresholds; (2) the hypothesis and test of asymmetric steerability profiles for CSB vs. CEO; (3) adaptive bias-specific intervention routing that extends MERA's monolithic adaptive framework to the multi-bias setting; and (4) principled graceful degradation from geometry-preserving rotation to nonlinear correction to abstention based on measured entanglement.",
  "project_name": "bias_disentangle_calib",
  "source": "web_research",
  "revision_notes": {
    "round1_issue_1_missing_competitor": "Tsujimura & Tagade (2508.17182) cited as closest methodological precedent, differentiated on four axes. [Carried from R1]",
    "round1_issue_2_model_names": "Fixed model names. [Carried from R1]",
    "round1_issue_3_untested_assumption": "Phase 1A retains separability tests with quantitative thresholds. [Carried from R1]",
    "round1_issue_4_steering_reliability": "Spherical Steering retained as primary Route A; augmented with MERA-inspired adaptive strength. [Extended from R1]",
    "round1_issue_5_baseline_comparison": "Contribution framing retained. MERA now added as critical baseline. [Extended from R1]",
    "round1_issue_6_behavioral_mechanistic_leap": "Phase 1A + 1B retained. [Carried from R1]",
    "round2_issue_1_critical_missing_competitor": "Liu (2605.05715) thoroughly integrated. [Carried from R2]",
    "round2_issue_2_separability_steerability_gap": "Phase 1A + 1B retained. [Carried from R2]",
    "round2_issue_3_minor_missing_references": "Selective Steering, COAST, Confidence Manifold, AUSteer, CLAS retained. [Carried from R2]",
    "round2_issue_4_nonlinear_steering_fallback": "Routes A/B/C retained with streamlined structure. [Carried from R2, simplified]",
    "round3_issue_1_MERA_baseline": "MERA (Hedström et al., ICML 2025; arXiv 2510.13290) now thoroughly integrated as BOTH a key baseline AND a building block. As baseline: MERA applied monolithically isolates the contribution of bias decomposition. As building block: Route A uses MERA-inspired constrained optimization for per-instance adaptive steering strength with non-degradation guarantees; Route C adopts MERA's Hoeffding-based statistical abstention framework. Key distinction: DBS-v2 decomposes biases (MERA treats errors monolithically), routes between intervention types based on steerability (MERA uses a single linear intervention), and operates per-bias-direction (MERA operates on a single error probe). MERA's acknowledged limitation of inherent linearity motivates Route B.",
    "round3_issue_2_nonlinear_steering_competitors": "Three nonlinear steering methods added to landscape: (a) ODESteer (Chen et al., ICLR 2026; arXiv 2602.17560) — barrier-function ODE framework unifying existing methods, multi-step adaptive steering on 4 × 7B models; (b) Curveball Steering (Raval et al., arXiv 2603.09313, Mar 2026) — polynomial kernel PCA respecting curved activation geometry, up to +47% over linear in high-curvature regimes on 1-4B models; (c) FLAS (arXiv 2605.05892, May 2026) — flow-based concept-conditioned velocity fields, first method to outperform prompting on AxBench, 97-255M parameter FlowBlock. Route B's lightweight bottleneck MLP is explicitly positioned against these: chosen for calibration-specific validation (Liu's direct evidence), minimal parameter footprint (<0.1% vs. these methods' 97M+ parameters), and inference efficiency. ODESteer/Curveball/FLAS are acknowledged as powerful general-purpose alternatives but none provide bias decomposition or steerability-based routing.",
    "round3_issue_3_venue_targeting": "AAAI 2027 dropped as primary target (July 28 deadline = ~10 weeks, infeasible). Revised: ICLR 2027 (Sep 24 full paper, ~18 weeks) as primary target — feasible with streamlined scope and human-in-loop timeline of 9-12 weeks. NeurIPS 2026 workshop (Aug 29) for Phase 1 results. ARR October 2026 as backup. ARR August (Aug 3, too tight) and AACL-IJCNLP dropped.",
    "round3_issue_4_specificity_thresholds": "Specificity ratio routing thresholds (previously ≥0.5 HIGH, 0.2-0.5 MEDIUM, <0.2 LOW) are now explicitly framed as HYPOTHESES to be empirically refined, not as calibrated boundaries. The approach now LEARNS thresholds via validation-set sweeps over specificity cutoffs and reports the full specificity-vs-effectiveness curve as a primary empirical contribution. Liu's two data points (≤0.152 for overthinking, ~0.999 for refusal) are cited as reference points only. This reframing converts a weakness (arbitrary thresholds) into a strength (the empirical threshold curve is itself a novel finding).",
    "round3_issue_5_overcomplexity": "MAJOR streamlining: (a) Models reduced from 5 to 3 (dropped Qwen2.5-3B, Llama-3.2-3B supplementary models — 'Wired for Overconfidence' comparison moved to supplementary); (b) Datasets reduced from 4 to 3 (dropped NQ-Open); (c) Routes reduced from 4 to 3 (Route D medium-specificity hybrid absorbed into Route A with conservative strength cap); (d) Core baselines reduced from 10+ to 6 (CCPS, VUF, DINCO, 'Wired for Overconfidence' replication moved to supplementary); (e) Phase 1A diagnostics reduced from 5 to 4 (dropped ICA); (f) Phase 1B diagnostics reduced from 4 to 3 (dropped within-class variance analysis, replaced cross-architecture stability with pilot steering test). Estimated GPU hours reduced ~30% (500-750 from 750-1050 manual). The streamlined matrix (3×3×3 + 6 baselines) is focused and executable within ICLR 2027 timeline."
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6808b2f-168c-4f17-a8e1-91190a5559d8",
  "isSidechain": true,
  "agentId": "a57e08d2da4cfab3d",
  "requestId": "req_011CbC1tR9WvvNcNwSYkMCzF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17131387-e6eb-4727-90b1-bdc62d65ef33",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "1e795d8c-c874-44f7-aace-83a8b0668b24",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P7a1M7oigWCudUjCJBZZ8f",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18462,
      "cache_read_input_tokens": 0,
      "output_tokens": 9260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18462
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 9260,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 18462,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18462,
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
