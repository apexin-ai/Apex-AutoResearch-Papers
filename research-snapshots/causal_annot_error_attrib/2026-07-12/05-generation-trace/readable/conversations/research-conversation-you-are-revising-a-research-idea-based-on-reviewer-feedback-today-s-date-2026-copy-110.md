# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-19 (UTC).** ## Original idea { "tit

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 90
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-2/4f29d1ac-c145-4ad7-a4cf-bff927c1d340.jsonl`
- **Structured JSON:** [`f29006fb4968a299f649.json`](../../sessions/f2/f29006fb4968a299f649.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T12:59:05.093Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T12:59:05.093Z",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-19 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Disentangling Competing Calibration Biases via Geometry-Aware Activation Steering\",\n  \"core_problem\": \"LLM miscalibration arises from at least two competing biases — choice-supportive bias (inflating confidence in initial answers) and contradictory-evidence overweighting (causing excessive confidence revision under criticism) — that require opposing corrections. Existing calibration methods apply uniform corrections that cannot simultaneously address biases pulling confidence in opposite directions. Can we identify per-instance which bias dominates and apply targeted, manifold-preserving corrections?\",\n  \"opportunity\": \"Kumaran et al. (Nature Machine Intelligence, 2026; arXiv 2507.03120) identified that LLM miscalibration results from two mechanistically distinct behavioral biases in Gemma 3, GPT-4o, and o1-preview: choice-supportive bias inflates confidence in selected answers, while contradictory-advice overweighting causes models to over-react to opposing evidence. Miao & Ungar (arXiv 2603.25052, 2026) independently showed that calibration and verbalized confidence signals are encoded linearly but orthogonally in the residual stream across three 7-8B models, establishing that confidence-related constructs have accessible geometric structure. Chhikara (TMLR 2025) showed distractor prompts reduce ECE by up to 90% but found RLHF models remain paradoxically miscalibrated on easy queries — precisely where CSB and CEO may trade dominance. The 'Wired for Overconfidence' circuit analysis (2604.01457) achieved up to 96.9% ECE reduction via monolithic activation steering on 3B models, but treats overconfidence as a single phenomenon. Crucially, Spherical Steering (ICML 2026) now provides a norm-preserving rotation primitive that avoids the off-manifold artifacts of additive steering. The convergence of (a) identified competing biases, (b) evidence for linear confidence encoding, and (c) geometry-aware steering methods creates an opportunity for bias-specific, manifold-preserving calibration correction.\",\n  \"landscape\": \"Kumaran et al. (Nature MI, 2026) identified competing biases (CSB and CEO) via behavioral experiments on Gemma 3, GPT-4o, and o1-preview but proposed no correction framework and provided no mechanistic (activation-level) evidence. Miao & Ungar (arXiv 2603.25052, 2026) demonstrated that calibration accuracy and verbalized confidence are linearly encoded but orthogonal in 7-8B models (cosine similarity <0.04 across layers), and introduced adaptive steering achieving 4-7× ECE improvement — but they target the confidence-accuracy misalignment gap, not the competing bias structure. Tsujimura & Tagade (arXiv 2508.17182, Aug 2025) decomposed LLM assertiveness into emotional and logical sub-components via unsupervised clustering on Llama-3.2-1B-Instruct (645 samples), finding two clusters in high-assertive representations — methodologically adjacent but critically different: their decomposition is descriptive (post-hoc ChatGPT-labeled clusters of communication style) rather than causally grounded in identified cognitive biases, uses a single 1B model, reports no calibration metrics, and addresses assertiveness rather than calibration. The 'Wired for Overconfidence' paper (2604.01457, April 2026) identifies overconfidence circuits in Qwen2.5-3B and Llama-3.2-3B, achieving 96.9% ECE reduction on PopQA via monolithic activation steering, but only tests 3B models and treats overconfidence as a single phenomenon. Ji et al. (EMNLP 2025) modulates a single Verbal Uncertainty Feature direction, reducing hallucinations by ~30%, capturing only the net effect of competing biases. Joshi et al. (EMNLP 2025) found a single calibration direction but did not decompose it. CORAL (arXiv 2602.06022, Feb 2026) achieves 49% ECE improvement via correctness-subspace probing on 7B models but uses a single MLP probe direction. Wang & Stengel-Eskin (ICLR 2026) introduced DINCO to normalize suggestibility bias via self-generated distractors at the output level. Zhuang et al. (arXiv 2025) proposed RDG to alleviate choice-supportive bias through fine-tuning but did not address CEO. CCPS (arXiv 2025) achieves ~55% ECE reduction via representation stability probing on MMLU. 'Breaking the Mirror' (arXiv 2509.03647) found that self-preference bias 'spans multiple or nonlinear directions,' achieving 97% unjustified bias reduction but with instability on legitimate cases — a direct warning that some biases may not be linearly separable. On the steering side, 'Steered LLM Activations are Non-Surjective' (2604.09839, April 2026) formally proved that additive steering pushes activations off the natural prompt-reachable manifold; 'A Sober Look at Steering Vectors' (NeurIPS 2024) showed many behaviors are unsteerable. However, Spherical Steering (arXiv 2602.08169, ICML 2026) resolves this by performing norm-preserving geodesic rotation rather than additive shifts, outperforming addition-based baselines by +10% on TruthfulQA while maintaining generation quality. No existing method separately identifies CSB vs. CEO activation signatures and applies bias-specific, manifold-preserving corrections — yet their opposing effects on calibration mean uniform correction is fundamentally suboptimal.\",\n  \"inspired_by\": \"Gap: Competing biases create non-uniform miscalibration patterns that single-direction methods cannot fix (Kumaran et al. 2026), while Miao & Ungar (2026) show confidence constructs are linearly encoded but orthogonal — suggesting decomposition is geometrically feasible. Pattern: Theory-driven contrastive activation probing (Ji et al. 2025, Miao & Ungar 2026) combined with manifold-preserving steering (Spherical Steering, ICML 2026). Untried combination: Cognitive-bias-grounded contrastive stimuli → per-instance bias diagnosis → geometry-aware targeted rotation, with explicit assumption validation and SAE-based fallback.\",\n  \"approach\": \"We design DBS-v2 (Disentangled Bias Steering) in three phases.\\n\\n**Phase 1 — Assumption Validation (Weeks 1-4):** Before building the full pipeline, we empirically test the core assumption that CSB and CEO produce distinguishable activation signatures. We construct two contrastive stimulus sets: for CSB, we compare hidden states when the model reviews its own prior answer vs. a fresh unattributed answer (eliciting choice-supportive inflation); for CEO, we compare states when contradictory expert advice is present vs. absent (eliciting evidence overweighting). Using difference-in-means on these contrastive pairs, we extract candidate bias directions in the residual stream. We then validate separability via: (a) cosine similarity between candidate directions (testing orthogonality), (b) principal angle analysis between CSB and CEO subspaces using the methodology of Miao & Ungar (2026), (c) PCA to assess whether 2 directions capture sufficient variance vs. requiring higher-dimensional subspaces, (d) ICA to test whether statistically independent (not just orthogonal) components emerge, and (e) cross-prediction ablations to confirm removing one bias subspace does not collapse the other. If CSB and CEO directions show cosine similarity >0.3 or shared variance >15%, we activate the fallback: extracting a multi-direction bias subspace via SAE-derived features (following the superposition hypothesis) and training a subspace projection classifier rather than relying on two orthogonal directions.\\n\\n**Phase 2 — Per-Instance Bias Diagnosis (Weeks 3-7):** A lightweight logistic probe (or, in the fallback case, a small MLP) trained on per-instance projection magnitudes onto each bias direction classifies which bias dominates for a given query. We stratify by difficulty: on easy questions where models are already confident, CSB likely dominates; on hard questions under criticism, CEO likely dominates. The probe output also provides a continuous dominance score enabling graded intervention.\\n\\n**Phase 3 — Geometry-Aware Targeted Steering (Weeks 5-12):** Instead of additive activation steering (which the non-surjectivity result of Mishra et al., 2604.09839, shows pushes activations off-manifold), we adopt Spherical Steering (You et al., ICML 2026) as the primary intervention: rotating activations along a geodesic away from the dominant bias direction while preserving activation norms. When CSB dominates, we rotate away from the CSB direction (reducing unwarranted confidence inflation); when CEO dominates, we rotate away from the CEO direction (preventing excessive confidence deflation). A confidence gate modulates rotation magnitude based on the probe's dominance score. We include additive steering as an ablation baseline to quantify the benefit of norm preservation.\\n\\nWe evaluate on TriviaQA, MMLU, PopQA, and NQ-Open across Gemma 4 31B (Dense), Qwen3-8B, and Llama-3.1-8B-Instruct. We additionally include Qwen2.5-3B and Llama-3.2-3B as supplementary models to enable fair comparison with 'Wired for Overconfidence' results at the same scale. Metrics: ECE, Brier score, AUROC, and difficulty-stratified ECE (easy/medium/hard partitions). Baselines: temperature scaling, CCPS, VUF intervention, DINCO, CORAL, Miao & Ungar adaptive steering, monolithic circuit ablation (Wired for Overconfidence replication at 3B scale), and monolithic Spherical Steering (single direction, no bias decomposition).\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"600-850 H100\",\n      \"timeline\": \"14-18 weeks\",\n      \"estimated_gpu_cost\": \"$1,500-$2,125 (H100 @ ~$2.50/hr mid-tier provider)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"500-700 H100\",\n      \"timeline\": \"10-13 weeks\",\n      \"claude_api_cost\": \"$250-$500 (Sonnet 4.6 for contrastive dataset generation, probing code, assumption validation scripts, analysis)\",\n      \"estimated_gpu_cost\": \"$1,250-$1,750\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"800-1100 H100\",\n      \"timeline\": \"5-8 weeks\",\n      \"claude_api_cost\": \"$700-$1,200 (Opus 4.7 for experiment orchestration, assumption validation analysis, hyperparameter sweeps, ablation design)\",\n      \"estimated_gpu_cost\": \"$2,000-$2,750\",\n      \"speed_bottleneck\": \"Phase 1 assumption validation is inherently sequential — results determine whether Phase 2-3 use orthogonal directions or SAE-based fallback. Contrastive dataset quality validation requires expert judgment. Steering coefficient search across 5 models × 4 datasets is parallelizable but generates large evaluation matrices. Fair replication of 'Wired for Overconfidence' baselines on 3B models adds overhead.\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — primary target with full timeline for assumption validation)\",\n    \"ARR August 2026 cycle (Aug 3, 2026 — targets EMNLP 2027 or future *CL venues)\",\n    \"NeurIPS 2026 Workshops (~Aug 29, 2026 — workshop paper track for preliminary Phase 1 results)\",\n    \"AACL-IJCNLP 2026 (ARR May 25 commitment deadline Aug 26, 2026 — if Phase 1 completes early)\",\n    \"ICLR 2027 (expected Oct 2026 deadline — full paper with all phases complete)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Competing Biases underlie Overconfidence and Underconfidence in LLMs (Kumaran et al., Nature Machine Intelligence 2026; arXiv 2507.03120)\",\n    \"Closing the Confidence-Faithfulness Gap in Large Language Models (Miao & Ungar, arXiv 2603.25052, 2026) — orthogonal calibration/confidence encoding, adaptive steering\",\n    \"LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components (Tsujimura & Tagade, arXiv 2508.17182, 2025) — closest methodological precedent\",\n    \"Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs (arXiv 2604.01457, 2026)\",\n    \"Spherical Steering: Geometry-Aware Activation Rotation for Language Models (You et al., ICML 2026; arXiv 2602.08169)\",\n    \"Steered LLM Activations are Non-Surjective (Mishra et al., arXiv 2604.09839, 2026)\",\n    \"A Sober Look at Steering Vectors for LLMs (Tan et al., NeurIPS 2024)\",\n    \"Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators (arXiv 2509.03647, 2025) — nonlinear bias warning\",\n    \"CORAL: Correctness-Optimized Residual Activation Lens (arXiv 2602.06022, 2026) — calibration-aware steering baseline\",\n    \"Mind the Confidence Gap: Overconfidence, Calibration, and Distractor Effects in Large Language Models (Chhikara, TMLR 2025)\",\n    \"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025)\",\n    \"Calibrating Verbalized Confidence with Self-Generated Distractors (Wang & Stengel-Eskin, ICLR 2026)\",\n    \"Calibration Across Layers: Understanding Calibration Evolution in LLMs (Joshi et al., EMNLP 2025)\",\n    \"Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation (Zhuang et al., arXiv 2512.03082, 2025)\",\n    \"Calibrating LLM Confidence by Probing Perturbed Representation Stability (arXiv 2505.21772, 2025)\",\n    \"Know When You're Wrong: Aligning Confidence with Correctness for LLM Error Detection (arXiv 2603.06604, 2026)\"\n  ],\n  \"description\": \"We propose DBS-v2 (Disentangled Bias Steering), a method that separately identifies and corrects two competing sources of LLM miscalibration identified by Kumaran et al. (2026): choice-supportive bias (CSB, inflating confidence in selected answers) and contradictory-evidence overweighting (CEO, causing excessive confidence revision under criticism). Unlike Tsujimura & Tagade (2025), who descriptively decomposed assertiveness into emotion/logic clusters via unsupervised methods on a 1B model without calibration evaluation, DBS-v2 is grounded in causally-identified cognitive biases with theory-driven contrastive stimuli and directly targets calibration metrics.\\n\\nThe method proceeds in three phases. Phase 1 (Assumption Validation) explicitly tests whether CSB and CEO produce distinguishable, linearly separable activation signatures — the key empirical assumption the original proposal left untested. Using contrastive activation probing, we extract candidate bias directions and validate separability via cosine similarity, principal angle analysis, PCA/ICA dimensionality assessment, and cross-prediction ablation (following the subspace methodology of Miao & Ungar, 2026). If directions are not cleanly orthogonal, we activate a fallback: extracting a multi-direction bias subspace via SAE-derived features. Phase 2 trains a lightweight per-instance bias dominance classifier. Phase 3 applies targeted corrections using Spherical Steering (You et al., ICML 2026) — norm-preserving geodesic rotation rather than additive steering — directly addressing the formal non-surjectivity concern (Mishra et al., 2604.09839) that additive interventions push activations off the natural manifold.\\n\\nWe evaluate on TriviaQA, MMLU, PopQA, and NQ-Open across five models: Gemma 4 31B (Dense), Qwen3-8B, and Llama-3.1-8B-Instruct as primary targets, plus Qwen2.5-3B and Llama-3.2-3B for fair comparison with 'Wired for Overconfidence' baselines. We compare against temperature scaling, CCPS, VUF intervention, DINCO, CORAL, Miao & Ungar adaptive steering, and monolithic Spherical Steering (without bias decomposition). Rather than claiming to outperform the 96.9% ECE reduction achieved by monolithic steering at 3B scale on PopQA, we frame DBS-v2's contribution around three axes: (1) interpretable, bias-specific corrections that reveal which bias source drives miscalibration per-instance, (2) difficulty-stratified improvement where competing biases dominate differently, and (3) robustness via manifold-preserving intervention. Phase 1 results constitute an independent contribution regardless of Phase 2-3 outcomes: the first mechanistic test of whether behaviorally-identified competing biases have distinguishable activation signatures.\",\n  \"project_name\": \"bias_disentangle_calib\",\n  \"source\": \"web_research\",\n  \"revision_notes\": {\n    \"issue_1_missing_competitor\": \"Tsujimura & Tagade (2508.17182) now cited as closest methodological precedent. Differentiated on four axes: (a) DBS-v2 uses theory-driven contrastive stimuli grounded in identified cognitive biases (CSB/CEO) vs. their post-hoc unsupervised clustering labeled by ChatGPT; (b) DBS-v2 targets calibration (ECE, Brier, AUROC) while they measure assertiveness (MSE) with no calibration evaluation; (c) DBS-v2 tests 5 models at 3B-31B scale vs. their single Llama-3.2-1B with 645 samples; (d) DBS-v2 includes causal steering interventions while they only perform descriptive vector removal.\",\n    \"issue_2_model_names\": \"Fixed: 'Gemma 4 27B' → Gemma 4 31B (Dense); 'Llama-3.3-8B-Instruct' → Llama-3.1-8B-Instruct. Qwen3-8B confirmed as valid model name (dense, 8.2B parameters, Apache 2.0).\",\n    \"issue_3_untested_assumption\": \"Added explicit Phase 1 (Assumption Validation) with 5 separability tests: cosine similarity, principal angle analysis, PCA dimensionality, ICA independence, and cross-prediction ablation. Specified quantitative decision criteria (cosine >0.3 or shared variance >15% triggers fallback). Phase 1 results are framed as an independent contribution.\",\n    \"issue_4_steering_reliability\": \"Adopted Spherical Steering (ICML 2026) as primary intervention — norm-preserving geodesic rotation that avoids off-manifold artifacts. Additive steering retained as ablation baseline. This directly addresses the non-surjectivity formal proof (2604.09839) and the empirical concerns from 'A Sober Look'. Additionally noted that DBS-v2's targeted dampening of specific bias directions (small, focused rotations) is inherently more conservative than general behavioral steering.\",\n    \"issue_5_baseline_comparison\": \"Reframed contribution: no longer claiming to 'beat' 96.9% ECE from 3B-scale monolithic steering. Added Qwen2.5-3B and Llama-3.2-3B as supplementary models for fair same-scale comparison. Primary contribution reframed around interpretability, difficulty-stratified improvement, and manifold-preserving robustness. Added CORAL and Miao & Ungar adaptive steering as new baselines.\",\n    \"issue_6_behavioral_mechanistic_leap\": \"Phase 1 explicitly tests this assumption before building the full pipeline. Cited Miao & Ungar (2026) as evidence that confidence-related constructs ARE linearly encoded (cosine <0.04 between calibration/confidence directions). Cited 'Breaking the Mirror' as a warning that some biases span nonlinear directions. SAE-based fallback handles the case where linear separability fails. Paper explicitly frames Phase 1 as testing whether Kumaran et al.'s behavioral taxonomy has clean mechanistic correlates.\"\n  }\n}\n\n## Reviewer feedback (round 2)\nIssues: [\"CRITICAL MISSING COMPETITOR: 'Decodable but Not Corrected by Fixed Residual-Stream Linear Steering' (arXiv 2605.05715, May 2026) demonstrates a classification-correction gap where linearly decodable directions (71.6% balanced accuracy) yield Δ≈0 under steering because the failure directions have 85-88% overlap with task-critical computation (specificity ratio ≤0.152). This directly threatens DBS-v2's Phase 3: even if CSB/CEO are decodable (Phase 1 succeeds), steering may fail due to entanglement. The paper proposes specificity ratio as a pre-intervention diagnostic — DBS-v2 must incorporate this.\", \"SEPARABILITY ≠ STEERABILITY GAP: Phase 1 validates whether CSB and CEO are separable (cosine similarity, PCA/ICA, cross-prediction ablation) but does NOT test whether identified directions are steerable without collateral damage. The 'Decodable but Not Corrected' paper shows these are empirically distinct questions. Phase 1 needs a steerability diagnostic: compute the specificity ratio (shared vs. mode-specific variance) of CSB/CEO directions relative to the overall correct-vs-incorrect subspace.\", \"MINOR MISSING REFERENCES: (a) 'Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection' (arXiv 2601.19375, Jan 2026) — another norm-preserving rotation method predating Spherical Steering, with discriminative layer selection. (b) 'Minimizing Collateral Damage in Activation Steering' (arXiv 2605.01167, May 2026) — formalizes collateral damage from steering interventions and proposes minimum-damage solutions, directly relevant to the manifold-preservation rationale.\", \"NO NON-LINEAR STEERING FALLBACK: The proposal's fallback (SAE-based features) addresses the case where CSB/CEO are not linearly separable, but not the case where they are separable but not linearly steerable. The 'Decodable but Not Corrected' paper shows a learned non-linear residual MLP achieves Δ=+2.8pp where all linear methods yield Δ≈0. Phase 3 should include a non-linear steering fallback (e.g., learned MLP correction) alongside Spherical Steering.\"]\nFeedback: The revision from round 1 is excellent — all prior issues were addressed thoroughly and honestly. The main new concern is a very recent paper (2605.05715, this month) that identifies a 'classification-correction gap': failure directions can be linearly decodable but not steerable because they overlap heavily with task-critical computation. This is distinct from the off-manifold concern already addressed via Spherical Steering. Concrete fixes: (1) Add a 'steerability diagnostic' to Phase 1 — after extracting CSB/CEO directions, compute their specificity ratio (proportion of mode-specific vs. shared variance with the correct/incorrect subspace). If specificity is low (<0.2), flag high entanglement risk. (2) Add a non-linear steering fallback in Phase 3: when specificity is low, use a learned non-linear residual correction (small MLP) instead of fixed-direction rotation. (3) Cite Selective Steering and Minimizing Collateral Damage as part of the geometry-aware steering landscape. (4) Explicitly discuss the separation between 'decodable' and 'steerable' in the approach section — this strengthens the paper's contribution by showing awareness of a subtle and important distinction.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.\n- Address each issue specifically.\n\n## 深度调研要求\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。\n3. **深度思考**：\n   - 核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach？\n4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。\n\n## 针对 Review 意见的定向搜索\n\n1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点\n2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline\n3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现\n4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot\n\n- You have full freedom: minor fix, major revision, or pivot.\n- Include a \"change_type\" field: \"minor\", \"major\", or \"pivot\".\n- Output a COMPLETE JSON object with ALL fields."
}
```

---

### Runtime record

_source line 2 · 2026-05-19T12:59:05.097Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T12:59:05.097Z",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340"
}
```

---

## Round 1

88 recorded events

### User

_source line 3 · 2026-05-19T12:59:05.109Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-19 (UTC).**

## Original idea
{
  "title": "Disentangling Competing Calibration Biases via Geometry-Aware Activation Steering",
  "core_problem": "LLM miscalibration arises from at least two competing biases — choice-supportive bias (inflating confidence in initial answers) and contradictory-evidence overweighting (causing excessive confidence revision under criticism) — that require opposing corrections. Existing calibration methods apply uniform corrections that cannot simultaneously address biases pulling confidence in opposite directions. Can we identify per-instance which bias dominates and apply targeted, manifold-preserving corrections?",
  "opportunity": "Kumaran et al. (Nature Machine Intelligence, 2026; arXiv 2507.03120) identified that LLM miscalibration results from two mechanistically distinct behavioral biases in Gemma 3, GPT-4o, and o1-preview: choice-supportive bias inflates confidence in selected answers, while contradictory-advice overweighting causes models to over-react to opposing evidence. Miao & Ungar (arXiv 2603.25052, 2026) independently showed that calibration and verbalized confidence signals are encoded linearly but orthogonally in the residual stream across three 7-8B models, establishing that confidence-related constructs have accessible geometric structure. Chhikara (TMLR 2025) showed distractor prompts reduce ECE by up to 90% but found RLHF models remain paradoxically miscalibrated on easy queries — precisely where CSB and CEO may trade dominance. The 'Wired for Overconfidence' circuit analysis (2604.01457) achieved up to 96.9% ECE reduction via monolithic activation steering on 3B models, but treats overconfidence as a single phenomenon. Crucially, Spherical Steering (ICML 2026) now provides a norm-preserving rotation primitive that avoids the off-manifold artifacts of additive steering. The convergence of (a) identified competing biases, (b) evidence for linear confidence encoding, and (c) geometry-aware steering methods creates an opportunity for bias-specific, manifold-preserving calibration correction.",
  "landscape": "Kumaran et al. (Nature MI, 2026) identified competing biases (CSB and CEO) via behavioral experiments on Gemma 3, GPT-4o, and o1-preview but proposed no correction framework and provided no mechanistic (activation-level) evidence. Miao & Ungar (arXiv 2603.25052, 2026) demonstrated that calibration accuracy and verbalized confidence are linearly encoded but orthogonal in 7-8B models (cosine similarity <0.04 across layers), and introduced adaptive steering achieving 4-7× ECE improvement — but they target the confidence-accuracy misalignment gap, not the competing bias structure. Tsujimura & Tagade (arXiv 2508.17182, Aug 2025) decomposed LLM assertiveness into emotional and logical sub-components via unsupervised clustering on Llama-3.2-1B-Instruct (645 samples), finding two clusters in high-assertive representations — methodologically adjacent but critically different: their decomposition is descriptive (post-hoc ChatGPT-labeled clusters of communication style) rather than causally grounded in identified cognitive biases, uses a single 1B model, reports no calibration metrics, and addresses assertiveness rather than calibration. The 'Wired for Overconfidence' paper (2604.01457, April 2026) identifies overconfidence circuits in Qwen2.5-3B and Llama-3.2-3B, achieving 96.9% ECE reduction on PopQA via monolithic activation steering, but only tests 3B models and treats overconfidence as a single phenomenon. Ji et al. (EMNLP 2025) modulates a single Verbal Uncertainty Feature direction, reducing hallucinations by ~30%, capturing only the net effect of competing biases. Joshi et al. (EMNLP 2025) found a single calibration direction but did not decompose it. CORAL (arXiv 2602.06022, Feb 2026) achieves 49% ECE improvement via correctness-subspace probing on 7B models but uses a single MLP probe direction. Wang & Stengel-Eskin (ICLR 2026) introduced DINCO to normalize suggestibility bias via self-generated distractors at the output level. Zhuang et al. (arXiv 2025) proposed RDG to alleviate choice-supportive bias through fine-tuning but did not address CEO. CCPS (arXiv 2025) achieves ~55% ECE reduction via representation stability probing on MMLU. 'Breaking the Mirror' (arXiv 2509.03647) found that self-preference bias 'spans multiple or nonlinear directions,' achieving 97% unjustified bias reduction but with instability on legitimate cases — a direct warning that some biases may not be linearly separable. On the steering side, 'Steered LLM Activations are Non-Surjective' (2604.09839, April 2026) formally proved that additive steering pushes activations off the natural prompt-reachable manifold; 'A Sober Look at Steering Vectors' (NeurIPS 2024) showed many behaviors are unsteerable. However, Spherical Steering (arXiv 2602.08169, ICML 2026) resolves this by performing norm-preserving geodesic rotation rather than additive shifts, outperforming addition-based baselines by +10% on TruthfulQA while maintaining generation quality. No existing method separately identifies CSB vs. CEO activation signatures and applies bias-specific, manifold-preserving corrections — yet their opposing effects on calibration mean uniform correction is fundamentally suboptimal.",
  "inspired_by": "Gap: Competing biases create non-uniform miscalibration patterns that single-direction methods cannot fix (Kumaran et al. 2026), while Miao & Ungar (2026) show confidence constructs are linearly encoded but orthogonal — suggesting decomposition is geometrically feasible. Pattern: Theory-driven contrastive activation probing (Ji et al. 2025, Miao & Ungar 2026) combined with manifold-preserving steering (Spherical Steering, ICML 2026). Untried combination: Cognitive-bias-grounded contrastive stimuli → per-instance bias diagnosis → geometry-aware targeted rotation, with explicit assumption validation and SAE-based fallback.",
  "approach": "We design DBS-v2 (Disentangled Bias Steering) in three phases.\n\n**Phase 1 — Assumption Validation (Weeks 1-4):** Before building the full pipeline, we empirically test the core assumption that CSB and CEO produce distinguishable activation signatures. We construct two contrastive stimulus sets: for CSB, we compare hidden states when the model reviews its own prior answer vs. a fresh unattributed answer (eliciting choice-supportive inflation); for CEO, we compare states when contradictory expert advice is present vs. absent (eliciting evidence overweighting). Using difference-in-means on these contrastive pairs, we extract candidate bias directions in the residual stream. We then validate separability via: (a) cosine similarity between candidate directions (testing orthogonality), (b) principal angle analysis between CSB and CEO subspaces using the methodology of Miao & Ungar (2026), (c) PCA to assess whether 2 directions capture sufficient variance vs. requiring higher-dimensional subspaces, (d) ICA to test whether statistically independent (not just orthogonal) components emerge, and (e) cross-prediction ablations to confirm removing one bias subspace does not collapse the other. If CSB and CEO directions show cosine similarity >0.3 or shared variance >15%, we activate the fallback: extracting a multi-direction bias subspace via SAE-derived features (following the superposition hypothesis) and training a subspace projection classifier rather than relying on two orthogonal directions.\n\n**Phase 2 — Per-Instance Bias Diagnosis (Weeks 3-7):** A lightweight logistic probe (or, in the fallback case, a small MLP) trained on per-instance projection magnitudes onto each bias direction classifies which bias dominates for a given query. We stratify by difficulty: on easy questions where models are already confident, CSB likely dominates; on hard questions under criticism, CEO likely dominates. The probe output also provides a continuous dominance score enabling graded intervention.\n\n**Phase 3 — Geometry-Aware Targeted Steering (Weeks 5-12):** Instead of additive activation steering (which the non-surjectivity result of Mishra et al., 2604.09839, shows pushes activations off-manifold), we adopt Spherical Steering (You et al., ICML 2026) as the primary intervention: rotating activations along a geodesic away from the dominant bias direction while preserving activation norms. When CSB dominates, we rotate away from the CSB direction (reducing unwarranted confidence inflation); when CEO dominates, we rotate away from the CEO direction (preventing excessive confidence deflation). A confidence gate modulates rotation magnitude based on the probe's dominance score. We include additive steering as an ablation baseline to quantify the benefit of norm preservation.\n\nWe evaluate on TriviaQA, MMLU, PopQA, and NQ-Open across Gemma 4 31B (Dense), Qwen3-8B, and Llama-3.1-8B-Instruct. We additionally include Qwen2.5-3B and Llama-3.2-3B as supplementary models to enable fair comparison with 'Wired for Overconfidence' results at the same scale. Metrics: ECE, Brier score, AUROC, and difficulty-stratified ECE (easy/medium/hard partitions). Baselines: temperature scaling, CCPS, VUF intervention, DINCO, CORAL, Miao & Ungar adaptive steering, monolithic circuit ablation (Wired for Overconfidence replication at 3B scale), and monolithic Spherical Steering (single direction, no bias decomposition).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "600-850 H100",
      "timeline": "14-18 weeks",
      "estimated_gpu_cost": "$1,500-$2,125 (H100 @ ~$2.50/hr mid-tier provider)"
    },
    "human_in_loop": {
      "gpu_hours": "500-700 H100",
      "timeline": "10-13 weeks",
      "claude_api_cost": "$250-$500 (Sonnet 4.6 for contrastive dataset generation, probing code, assumption validation scripts, analysis)",
      "estimated_gpu_cost": "$1,250-$1,750"
    },
    "auto_research": {
      "gpu_hours": "800-1100 H100",
      "timeline": "5-8 weeks",
      "claude_api_cost": "$700-$1,200 (Opus 4.7 for experiment orchestration, assumption validation analysis, hyperparameter sweeps, ablation design)",
      "estimated_gpu_cost": "$2,000-$2,750",
      "speed_bottleneck": "Phase 1 assumption validation is inherently sequential — results determine whether Phase 2-3 use orthogonal directions or SAE-based fallback. Contrastive dataset quality validation requires expert judgment. Steering coefficient search across 5 models × 4 datasets is parallelizable but generates large evaluation matrices. Fair replication of 'Wired for Overconfidence' baselines on 3B models adds overhead."
    }
  },
  "target_venues": [
    "AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — primary target with full timeline for assumption validation)",
    "ARR August 2026 cycle (Aug 3, 2026 — targets EMNLP 2027 or future *CL venues)",
    "NeurIPS 2026 Workshops (~Aug 29, 2026 — workshop paper track for preliminary Phase 1 results)",
    "AACL-IJCNLP 2026 (ARR May 25 commitment deadline Aug 26, 2026 — if Phase 1 completes early)",
    "ICLR 2027 (expected Oct 2026 deadline — full paper with all phases complete)"
  ],
  "level": "top-tier",
  "key_references": [
    "Competing Biases underlie Overconfidence and Underconfidence in LLMs (Kumaran et al., Nature Machine Intelligence 2026; arXiv 2507.03120)",
    "Closing the Confidence-Faithfulness Gap in Large Language Models (Miao & Ungar, arXiv 2603.25052, 2026) — orthogonal calibration/confidence encoding, adaptive steering",
    "LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components (Tsujimura & Tagade, arXiv 2508.17182, 2025) — closest methodological precedent",
    "Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs (arXiv 2604.01457, 2026)",
    "Spherical Steering: Geometry-Aware Activation Rotation for Language Models (You et al., ICML 2026; arXiv 2602.08169)",
    "Steered LLM Activations are Non-Surjective (Mishra et al., arXiv 2604.09839, 2026)",
    "A Sober Look at Steering Vectors for LLMs (Tan et al., NeurIPS 2024)",
    "Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators (arXiv 2509.03647, 2025) — nonlinear bias warning",
    "CORAL: Correctness-Optimized Residual Activation Lens (arXiv 2602.06022, 2026) — calibration-aware steering baseline",
    "Mind the Confidence Gap: Overconfidence, Calibration, and Distractor Effects in Large Language Models (Chhikara, TMLR 2025)",
    "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025)",
    "Calibrating Verbalized Confidence with Self-Generated Distractors (Wang & Stengel-Eskin, ICLR 2026)",
    "Calibration Across Layers: Understanding Calibration Evolution in LLMs (Joshi et al., EMNLP 2025)",
    "Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation (Zhuang et al., arXiv 2512.03082, 2025)",
    "Calibrating LLM Confidence by Probing Perturbed Representation Stability (arXiv 2505.21772, 2025)",
    "Know When You're Wrong: Aligning Confidence with Correctness for LLM Error Detection (arXiv 2603.06604, 2026)"
  ],
  "description": "We propose DBS-v2 (Disentangled Bias Steering), a method that separately identifies and corrects two competing sources of LLM miscalibration identified by Kumaran et al. (2026): choice-supportive bias (CSB, inflating confidence in selected answers) and contradictory-evidence overweighting (CEO, causing excessive confidence revision under criticism). Unlike Tsujimura & Tagade (2025), who descriptively decomposed assertiveness into emotion/logic clusters via unsupervised methods on a 1B model without calibration evaluation, DBS-v2 is grounded in causally-identified cognitive biases with theory-driven contrastive stimuli and directly targets calibration metrics.\n\nThe method proceeds in three phases. Phase 1 (Assumption Validation) explicitly tests whether CSB and CEO produce distinguishable, linearly separable activation signatures — the key empirical assumption the original proposal left untested. Using contrastive activation probing, we extract candidate bias directions and validate separability via cosine similarity, principal angle analysis, PCA/ICA dimensionality assessment, and cross-prediction ablation (following the subspace methodology of Miao & Ungar, 2026). If directions are not cleanly orthogonal, we activate a fallback: extracting a multi-direction bias subspace via SAE-derived features. Phase 2 trains a lightweight per-instance bias dominance classifier. Phase 3 applies targeted corrections using Spherical Steering (You et al., ICML 2026) — norm-preserving geodesic rotation rather than additive steering — directly addressing the formal non-surjectivity concern (Mishra et al., 2604.09839) that additive interventions push activations off the natural manifold.\n\nWe evaluate on TriviaQA, MMLU, PopQA, and NQ-Open across five models: Gemma 4 31B (Dense), Qwen3-8B, and Llama-3.1-8B-Instruct as primary targets, plus Qwen2.5-3B and Llama-3.2-3B for fair comparison with 'Wired for Overconfidence' baselines. We compare against temperature scaling, CCPS, VUF intervention, DINCO, CORAL, Miao & Ungar adaptive steering, and monolithic Spherical Steering (without bias decomposition). Rather than claiming to outperform the 96.9% ECE reduction achieved by monolithic steering at 3B scale on PopQA, we frame DBS-v2's contribution around three axes: (1) interpretable, bias-specific corrections that reveal which bias source drives miscalibration per-instance, (2) difficulty-stratified improvement where competing biases dominate differently, and (3) robustness via manifold-preserving intervention. Phase 1 results constitute an independent contribution regardless of Phase 2-3 outcomes: the first mechanistic test of whether behaviorally-identified competing biases have distinguishable activation signatures.",
  "project_name": "bias_disentangle_calib",
  "source": "web_research",
  "revision_notes": {
    "issue_1_missing_competitor": "Tsujimura & Tagade (2508.17182) now cited as closest methodological precedent. Differentiated on four axes: (a) DBS-v2 uses theory-driven contrastive stimuli grounded in identified cognitive biases (CSB/CEO) vs. their post-hoc unsupervised clustering labeled by ChatGPT; (b) DBS-v2 targets calibration (ECE, Brier, AUROC) while they measure assertiveness (MSE) with no calibration evaluation; (c) DBS-v2 tests 5 models at 3B-31B scale vs. their single Llama-3.2-1B with 645 samples; (d) DBS-v2 includes causal steering interventions while they only perform descriptive vector removal.",
    "issue_2_model_names": "Fixed: 'Gemma 4 27B' → Gemma 4 31B (Dense); 'Llama-3.3-8B-Instruct' → Llama-3.1-8B-Instruct. Qwen3-8B confirmed as valid model name (dense, 8.2B parameters, Apache 2.0).",
    "issue_3_untested_assumption": "Added explicit Phase 1 (Assumption Validation) with 5 separability tests: cosine similarity, principal angle analysis, PCA dimensionality, ICA independence, and cross-prediction ablation. Specified quantitative decision criteria (cosine >0.3 or shared variance >15% triggers fallback). Phase 1 results are framed as an independent contribution.",
    "issue_4_steering_reliability": "Adopted Spherical Steering (ICML 2026) as primary intervention — norm-preserving geodesic rotation that avoids off-manifold artifacts. Additive steering retained as ablation baseline. This directly addresses the non-surjectivity formal proof (2604.09839) and the empirical concerns from 'A Sober Look'. Additionally noted that DBS-v2's targeted dampening of specific bias directions (small, focused rotations) is inherently more conservative than general behavioral steering.",
    "issue_5_baseline_comparison": "Reframed contribution: no longer claiming to 'beat' 96.9% ECE from 3B-scale monolithic steering. Added Qwen2.5-3B and Llama-3.2-3B as supplementary models for fair same-scale comparison. Primary contribution reframed around interpretability, difficulty-stratified improvement, and manifold-preserving robustness. Added CORAL and Miao & Ungar adaptive steering as new baselines.",
    "issue_6_behavioral_mechanistic_leap": "Phase 1 explicitly tests this assumption before building the full pipeline. Cited Miao & Ungar (2026) as evidence that confidence-related constructs ARE linearly encoded (cosine <0.04 between calibration/confidence directions). Cited 'Breaking the Mirror' as a warning that some biases span nonlinear directions. SAE-based fallback handles the case where linear separability fails. Paper explicitly frames Phase 1 as testing whether Kumaran et al.'s behavioral taxonomy has clean mechanistic correlates."
  }
}

## Reviewer feedback (round 2)
Issues: ["CRITICAL MISSING COMPETITOR: 'Decodable but Not Corrected by Fixed Residual-Stream Linear Steering' (arXiv 2605.05715, May 2026) demonstrates a classification-correction gap where linearly decodable directions (71.6% balanced accuracy) yield Δ≈0 under steering because the failure directions have 85-88% overlap with task-critical computation (specificity ratio ≤0.152). This directly threatens DBS-v2's Phase 3: even if CSB/CEO are decodable (Phase 1 succeeds), steering may fail due to entanglement. The paper proposes specificity ratio as a pre-intervention diagnostic — DBS-v2 must incorporate this.", "SEPARABILITY ≠ STEERABILITY GAP: Phase 1 validates whether CSB and CEO are separable (cosine similarity, PCA/ICA, cross-prediction ablation) but does NOT test whether identified directions are steerable without collateral damage. The 'Decodable but Not Corrected' paper shows these are empirically distinct questions. Phase 1 needs a steerability diagnostic: compute the specificity ratio (shared vs. mode-specific variance) of CSB/CEO directions relative to the overall correct-vs-incorrect subspace.", "MINOR MISSING REFERENCES: (a) 'Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection' (arXiv 2601.19375, Jan 2026) — another norm-preserving rotation method predating Spherical Steering, with discriminative layer selection. (b) 'Minimizing Collateral Damage in Activation Steering' (arXiv 2605.01167, May 2026) — formalizes collateral damage from steering interventions and proposes minimum-damage solutions, directly relevant to the manifold-preservation rationale.", "NO NON-LINEAR STEERING FALLBACK: The proposal's fallback (SAE-based features) addresses the case where CSB/CEO are not linearly separable, but not the case where they are separable but not linearly steerable. The 'Decodable but Not Corrected' paper shows a learned non-linear residual MLP achieves Δ=+2.8pp where all linear methods yield Δ≈0. Phase 3 should include a non-linear steering fallback (e.g., learned MLP correction) alongside Spherical Steering."]
Feedback: The revision from round 1 is excellent — all prior issues were addressed thoroughly and honestly. The main new concern is a very recent paper (2605.05715, this month) that identifies a 'classification-correction gap': failure directions can be linearly decodable but not steerable because they overlap heavily with task-critical computation. This is distinct from the off-manifold concern already addressed via Spherical Steering. Concrete fixes: (1) Add a 'steerability diagnostic' to Phase 1 — after extracting CSB/CEO directions, compute their specificity ratio (proportion of mode-specific vs. shared variance with the correct/incorrect subspace). If specificity is low (<0.2), flag high entanglement risk. (2) Add a non-linear steering fallback in Phase 3: when specificity is low, use a learned non-linear residual correction (small MLP) instead of fixed-direction rotation. (3) Cite Selective Steering and Minimizing Collateral Damage as part of the geometry-aware steering landscape. (4) Explicitly discuss the separation between 'decodable' and 'steerable' in the approach section — this strengthens the paper's contribution by showing awareness of a subtle and important distinction.

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
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "8b702768-0e8c-4ff9-b26a-89ccd4ca503c",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T12:59:05.108Z_

```json
{
  "parentUuid": "8b702768-0e8c-4ff9-b26a-89ccd4ca503c",
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
  "uuid": "0ffdc893-b01f-4ce0-a5fc-d166c8e46fca",
  "timestamp": "2026-05-19T12:59:05.108Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T12:59:05.108Z_

```json
{
  "parentUuid": "0ffdc893-b01f-4ce0-a5fc-d166c8e46fca",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4af88d61-378f-4424-864d-bf1866156e58",
  "timestamp": "2026-05-19T12:59:05.108Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"Disentangling Competing Calibration Biases via Geometry-Aware Activati…",
  "leafUuid": "4af88d61-378f-4424-864d-bf1866156e58",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise calibration bias steering with steerability diagnostics",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340"
}
```

---

### Assistant

_source line 8 · 2026-05-19T12:59:11.358Z_

<details><summary>Logged reasoning block</summary>

```text
The reviewer feedback in round 2 raises important concerns about a new paper (arXiv 2605.05715) that identifies a "classification-correction gap" - where linearly decodable directions may not be steerable due to entanglement with task-critical computation. Let me research these papers thoroughly before revising.

Let me search for:
1. "Decodable but Not Corrected by Fixed Residual-Stream Linear Steering" (arXiv 2605.05715)
2. "Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection" (arXiv 2601.19375)


3. "Minimizing Collateral Damage in Activation Steering" (arXiv 2605.01167)

I need to understand how these papers relate to the classification-correction gap and what implications this has for the DBS-v2 approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4af88d61-378f-4424-864d-bf1866156e58",
  "isSidechain": false,
  "requestId": "req_011CbBy6JVuDLmEw5WQQt4WX",
  "type": "assistant",
  "uuid": "6cc93d9e-44cf-46a5-9c12-43153bb893cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QFqLrRVJEgk9PYZKZc4Pcp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7920,
      "cache_read_input_tokens": 11374,
      "output_tokens": 322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7920,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 322,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 7920,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7920
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

_source line 9 · 2026-05-19T12:59:11.369Z_

I'll start by deeply researching the papers and concepts raised by the reviewer. Let me search for all the key references mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cc93d9e-44cf-46a5-9c12-43153bb893cd",
  "isSidechain": false,
  "requestId": "req_011CbBy6JVuDLmEw5WQQt4WX",
  "type": "assistant",
  "uuid": "64b7130e-371a-4b02-baa0-ec85bf130aee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QFqLrRVJEgk9PYZKZc4Pcp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7920,
      "cache_read_input_tokens": 11374,
      "output_tokens": 322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7920,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 322,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 7920,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7920
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

_source line 10 · 2026-05-19T12:59:11.524Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TuKf7uFf2TKoddZNaMy3pQ`</summary>

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
  "parentUuid": "64b7130e-371a-4b02-baa0-ec85bf130aee",
  "isSidechain": false,
  "requestId": "req_011CbBy6JVuDLmEw5WQQt4WX",
  "type": "assistant",
  "uuid": "c86160b7-8bd5-4d5f-8d4b-0499de297daa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QFqLrRVJEgk9PYZKZc4Pcp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7920,
      "cache_read_input_tokens": 11374,
      "output_tokens": 322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7920,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 322,
          "cache_read_input_tokens": 11374,
          "cache_creation_input_tokens": 7920,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7920
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

_source line 11 · 2026-05-19T12:59:11.531Z_

<details><summary>↩ Tool result · `toolu_01TuKf7uFf2TKoddZNaMy3pQ`</summary>

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
  "parentUuid": "c86160b7-8bd5-4d5f-8d4b-0499de297daa",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "fc03674a-2d63-4d28-b065-b16b18ba4e43",
  "toolUseResult": {
    "matches": [
      "WebFetch",
      "WebSearch"
    ],
    "query": "select:WebFetch,WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "c86160b7-8bd5-4d5f-8d4b-0499de297daa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-19T12:59:13.971Z_

Now let me search for all the key papers mentioned by the reviewer in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc03674a-2d63-4d28-b065-b16b18ba4e43",
  "isSidechain": false,
  "requestId": "req_011CbBy6n8ZNNrtU7XhhJSMp",
  "type": "assistant",
  "uuid": "d67bb397-20ac-45b9-8dc8-d29a60004915",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kksscxc8HaW78UVUJkhqLJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1341,
      "cache_read_input_tokens": 19294,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1341,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 99,
          "cache_read_input_tokens": 19294,
          "cache_creation_input_tokens": 1341,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1341
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

_source line 13 · 2026-05-19T12:59:14.615Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CVJtSyF4dDVdoSBK67iz6F`</summary>

```json
{
  "query": "arXiv 2605.05715 \"Decodable but Not Corrected\" residual stream linear steering classification-correction gap"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d67bb397-20ac-45b9-8dc8-d29a60004915",
  "isSidechain": false,
  "requestId": "req_011CbBy6n8ZNNrtU7XhhJSMp",
  "type": "assistant",
  "uuid": "30c5d660-0c31-4372-bae2-33a84aedbc2c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kksscxc8HaW78UVUJkhqLJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1341,
      "cache_read_input_tokens": 19294,
      "output_tokens": 99,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1341,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 99,
          "cache_read_input_tokens": 19294,
          "cache_creation_input_tokens": 1341,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1341
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

_source line 14 · 2026-05-19T12:59:22.850Z_

<details><summary>↩ Tool result · `toolu_01CVJtSyF4dDVdoSBK67iz6F`</summary>

```text
Web search results for query: "arXiv 2605.05715 "Decodable but Not Corrected" residual stream linear steering classification-correction gap"

Links: [{"title":"[2605.05715] Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes","url":"https://arxiv.org/abs/2605.05715"},{"title":"Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes","url":"https://arxiv.org/html/2605.05715"},{"title":"Analysing the Residual Stream of Language Models Under Knowledge   Conflicts","url":"https://arxiv.org/pdf/2410.16090"},{"title":"Activation Transport Operators","url":"https://arxiv.org/pdf/2508.17540"},{"title":"Error Correction for Message Streams","url":"https://arxiv.org/html/2307.07087"},{"title":"Tight bounds for stream decodable error-correcting codes","url":"https://www.arxiv.org/pdf/2407.06446"},{"title":"An Adversarial Example for Direct Logit Attribution: Memory Management   in GELU-4L","url":"https://arxiv.org/pdf/2310.07325"}]

Based on the search results, I found the paper you're looking for:

**arXiv:2605.05715** titled "Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes" by Ming Liu.

## Paper Overview

The paper addresses the question: "Can linearly decodable failure signals in LLM hidden states be leveraged to correct those failures?"

## Key Findings

The paper investigates the **classification-correction gap** through a specific failure mode called **Overthinking (OT)**. OT is a stable behavioral regime (Jaccard >= 0.81, 94% inter-annotator agreement) in medical QA where models answer correctly under resampling yet fail in extended chain-of-thought.

The core finding reveals a paradox: OT is linearly decodable at 71.6% balanced accuracy (p < 10^{-16}), yet five families of fixed linear steering (29 configurations, n=1,273) all yield Delta approximately 0, with identical null results cross-architecture (Qwen2.5-7B) and cross-domain (MMLU-STEM).

## Underlying Mechanism

Three convergent lines of evidence suggest representational entanglement: the OT direction has 85-88% overlap with task-critical computation (specificity ratio <= 0.152), indicating that the decodable failure signal is too intertwined with essential task computation to be corrected through simple linear steering.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30c5d660-0c31-4372-bae2-33a84aedbc2c",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "975fb00d-8c2c-4323-908a-0572076e7963",
  "toolUseResult": {
    "query": "arXiv 2605.05715 \"Decodable but Not Corrected\" residual stream linear steering classification-correction gap",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LLcMQoQfne8GFSkXFSEpDd",
        "content": [
          {
            "title": "[2605.05715] Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes",
            "url": "https://arxiv.org/abs/2605.05715"
          },
          {
            "title": "Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes",
            "url": "https://arxiv.org/html/2605.05715"
          },
          {
            "title": "Analysing the Residual Stream of Language Models Under Knowledge   Conflicts",
            "url": "https://arxiv.org/pdf/2410.16090"
          },
          {
            "title": "Activation Transport Operators",
            "url": "https://arxiv.org/pdf/2508.17540"
          },
          {
            "title": "Error Correction for Message Streams",
            "url": "https://arxiv.org/html/2307.07087"
          },
          {
            "title": "Tight bounds for stream decodable error-correcting codes",
            "url": "https://www.arxiv.org/pdf/2407.06446"
          },
          {
            "title": "An Adversarial Example for Direct Logit Attribution: Memory Management   in GELU-4L",
            "url": "https://arxiv.org/pdf/2310.07325"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**arXiv:2605.05715** titled \"Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes\" by Ming Liu.\n\n## Paper Overview\n\nThe paper addresses the question: \"Can linearly decodable failure signals in LLM hidden states be leveraged to correct those failures?\"\n\n## Key Findings\n\nThe paper investigates the **classification-correction gap** through a specific failure mode called **Overthinking (OT)**. OT is a stable behavioral regime (Jaccard >= 0.81, 94% inter-annotator agreement) in medical QA where models answer correctly under resampling yet fail in extended chain-of-thought.\n\nThe core finding reveals a paradox: OT is linearly decodable at 71.6% balanced accuracy (p < 10^{-16}), yet five families of fixed linear steering (29 configurations, n=1,273) all yield Delta approximately 0, with identical null results cross-architecture (Qwen2.5-7B) and cross-domain (MMLU-STEM).\n\n## Underlying Mechanism\n\nThree convergent lines of evidence suggest representational entanglement: the OT direction has 85-88% overlap with task-critical computation (specificity ratio <= 0.152), indicating that the decodable failure signal is too intertwined with essential task computation to be corrected through simple linear steering."
    ],
    "durationSeconds": 8.227355157999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "30c5d660-0c31-4372-bae2-33a84aedbc2c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T12:59:25.307Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017N4kyNwFMW61RZKLTVyFgZ`</summary>

```json
{
  "query": "arXiv 2601.19375 \"Selective Steering\" norm-preserving discriminative layer selection activation steering 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "975fb00d-8c2c-4323-908a-0572076e7963",
  "isSidechain": false,
  "requestId": "req_011CbBy7cGmFJgejbngqnAzG",
  "type": "assistant",
  "uuid": "544e1bc7-daa4-48d1-a98d-e6d0862faa78",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V2svem3RCsqnKYTuqEAmfi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 20635,
      "output_tokens": 80,
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
          "output_tokens": 80,
          "cache_read_input_tokens": 20635,
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

_source line 16 · 2026-05-19T12:59:33.551Z_

<details><summary>↩ Tool result · `toolu_017N4kyNwFMW61RZKLTVyFgZ`</summary>

```text
Web search results for query: "arXiv 2601.19375 "Selective Steering" norm-preserving discriminative layer selection activation steering 2026"

Links: [{"title":"[2601.19375] Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection","url":"https://arxiv.org/abs/2601.19375"},{"title":"GitHub - knoveleng/steering: Official repo for the paper: \"Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection\"","url":"https://github.com/knoveleng/steering"},{"title":"Selective Steering: Norm-Preserving Control Through Discriminative","url":"https://arxiv.org/pdf/2601.19375"},{"title":"Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection","url":"https://arxiv.org/html/2601.19375v1"},{"title":"Where to Steer: Input-Dependent Layer Selection for Steering Improves LLM Alignment","url":"https://arxiv.org/pdf/2604.03867"},{"title":"Understanding Unreliability of Steering Vectors in Language Models: Geometric Predictors and the Limits of Linear Approximations","url":"https://arxiv.org/pdf/2602.17881"}]

I found the paper you're looking for. Here are the key details about arXiv paper 2601.19375:

## Overview

The paper is titled "Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection" and was submitted on January 27, 2026 by authors Quy-Anh Dang and Chris Ngo.

## Problem Statement

The paper addresses the fact that large language models (LLMs) remain vulnerable to adversarial attacks that elicit harmful behaviors. Existing activation steering methods have critical limitations: activation addition requires careful coefficient tuning, directional ablation provides only binary control, and recent Angular Steering violates norm preservation, causing distribution shift and generation collapse in models below 7B parameters.

## Proposed Solution

Selective Steering addresses these limitations through two key innovations: (1) a mathematically rigorous norm-preserving rotation formulation that maintains activation distribution integrity, and (2) discriminative layer selection that applies steering only where feature representations exhibit opposite-signed class alignment.

## Results

The authors prove that Selective Steering guarantees activation norm preservation while standard Angular Steering violates this property. Comprehensive experiments on 8 models across 3 families (Llama, Qwen, Gemma) demonstrate that SS achieves zero perplexity threshold violations across all models and angles.

The official code repository is available on GitHub at https://github.com/knoveleng/steering.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "544e1bc7-daa4-48d1-a98d-e6d0862faa78",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "5d8219a3-1971-460d-8e20-2acd1684ccd6",
  "toolUseResult": {
    "query": "arXiv 2601.19375 \"Selective Steering\" norm-preserving discriminative layer selection activation steering 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YFN9Y2qwyo9xZaDdxrKVjE",
        "content": [
          {
            "title": "[2601.19375] Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection",
            "url": "https://arxiv.org/abs/2601.19375"
          },
          {
            "title": "GitHub - knoveleng/steering: Official repo for the paper: \"Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection\"",
            "url": "https://github.com/knoveleng/steering"
          },
          {
            "title": "Selective Steering: Norm-Preserving Control Through Discriminative",
            "url": "https://arxiv.org/pdf/2601.19375"
          },
          {
            "title": "Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection",
            "url": "https://arxiv.org/html/2601.19375v1"
          },
          {
            "title": "Where to Steer: Input-Dependent Layer Selection for Steering Improves LLM Alignment",
            "url": "https://arxiv.org/pdf/2604.03867"
          },
          {
            "title": "Understanding Unreliability of Steering Vectors in Language Models: Geometric Predictors and the Limits of Linear Approximations",
            "url": "https://arxiv.org/pdf/2602.17881"
          }
        ]
      },
      "I found the paper you're looking for. Here are the key details about arXiv paper 2601.19375:\n\n## Overview\n\nThe paper is titled \"Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection\" and was submitted on January 27, 2026 by authors Quy-Anh Dang and Chris Ngo.\n\n## Problem Statement\n\nThe paper addresses the fact that large language models (LLMs) remain vulnerable to adversarial attacks that elicit harmful behaviors. Existing activation steering methods have critical limitations: activation addition requires careful coefficient tuning, directional ablation provides only binary control, and recent Angular Steering violates norm preservation, causing distribution shift and generation collapse in models below 7B parameters.\n\n## Proposed Solution\n\nSelective Steering addresses these limitations through two key innovations: (1) a mathematically rigorous norm-preserving rotation formulation that maintains activation distribution integrity, and (2) discriminative layer selection that applies steering only where feature representations exhibit opposite-signed class alignment.\n\n## Results\n\nThe authors prove that Selective Steering guarantees activation norm preservation while standard Angular Steering violates this property. Comprehensive experiments on 8 models across 3 families (Llama, Qwen, Gemma) demonstrate that SS achieves zero perplexity threshold violations across all models and angles.\n\nThe official code repository is available on GitHub at https://github.com/knoveleng/steering."
    ],
    "durationSeconds": 8.239164359000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "544e1bc7-daa4-48d1-a98d-e6d0862faa78",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T12:59:35.923Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VEX4eEK3s9mEao3MKec9mu`</summary>

```json
{
  "query": "arXiv 2605.01167 \"Minimizing Collateral Damage\" activation steering 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d8219a3-1971-460d-8e20-2acd1684ccd6",
  "isSidechain": false,
  "requestId": "req_011CbBy8Q2LWyjNaEuiXoDLE",
  "type": "assistant",
  "uuid": "d6ffcda2-448b-4329-882c-8b3d5f410315",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BW2752uP36ZJhZywogKBPH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 748,
      "cache_read_input_tokens": 21436,
      "output_tokens": 76,
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
          "output_tokens": 76,
          "cache_read_input_tokens": 21436,
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

### Tool result

_source line 18 · 2026-05-19T12:59:41.916Z_

<details><summary>↩ Tool result · `toolu_01VEX4eEK3s9mEao3MKec9mu`</summary>

```text
Web search results for query: "arXiv 2605.01167 "Minimizing Collateral Damage" activation steering 2026"

Links: [{"title":"Minimizing Collateral Damage in Activation Steering","url":"https://arxiv.org/html/2605.01167v1"},{"title":"[2605.01167] Minimizing Collateral Damage in Activation Steering","url":"https://arxiv.org/abs/2605.01167"},{"title":"Minimizing Collateral Damage in Activation Steering","url":"https://www.researchgate.net/publication/404427927_Minimizing_Collateral_Damage_in_Activation_Steering"},{"title":"Mitigating Memorization in LLMs using Activation Steering","url":"https://arxiv.org/pdf/2503.06040"},{"title":"Extending Activation Steering to Broad Skills and Multiple Behaviours","url":"https://arxiv.org/pdf/2403.05767"},{"title":"Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/pdf/2602.04428"},{"title":"Improving Activation Steering in Language Models with Mean-Centring","url":"https://arxiv.org/pdf/2312.03813"},{"title":"Analysing the Safety Pitfalls of Steering Vectors","url":"https://arxiv.org/pdf/2603.24543"}]

I found the paper! Here's what I found about arXiv 2605.01167:

## "Minimizing Collateral Damage in Activation Steering"

**Authors:** Tam Nguyen, Tu Anh Nguyen, Sina Alemohammad, Richard G. Baraniuk

**Publication Date:** May 1, 2026

**Core Concept:**

Activation steering is a method for controlling Large Language Model (LLM) behavior by intervening in its internal representations to increase the alignment with a specific target feature direction. However, standard interventions, such as vector addition, often cause "collateral damage", defined as unintended changes in the alignment of activations along other non-target feature directions.

**The Problem Being Addressed:**

This damage occurs because standard methods implicitly assume the isotropy of non-target features.

**Proposed Solution:**

The work provides a mathematical formalization of collateral damage and introduces a principled framework that models steering as a constrained optimization problem. Their method finds a new activation that minimizes the expected squared collateral change weighted by the empirical second-moment matrix of activations.

The paper addresses a key challenge in using activation steering for LLM control—ensuring that efforts to steer a model toward desired behaviors don't inadvertently harm other aspects of the model's functioning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6ffcda2-448b-4329-882c-8b3d5f410315",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "9e3662f8-c46d-4228-ac0a-d3e9b3c08653",
  "toolUseResult": {
    "query": "arXiv 2605.01167 \"Minimizing Collateral Damage\" activation steering 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01H8FWisY2ZHFUUGRhVMTuUh",
        "content": [
          {
            "title": "Minimizing Collateral Damage in Activation Steering",
            "url": "https://arxiv.org/html/2605.01167v1"
          },
          {
            "title": "[2605.01167] Minimizing Collateral Damage in Activation Steering",
            "url": "https://arxiv.org/abs/2605.01167"
          },
          {
            "title": "Minimizing Collateral Damage in Activation Steering",
            "url": "https://www.researchgate.net/publication/404427927_Minimizing_Collateral_Damage_in_Activation_Steering"
          },
          {
            "title": "Mitigating Memorization in LLMs using Activation Steering",
            "url": "https://arxiv.org/pdf/2503.06040"
          },
          {
            "title": "Extending Activation Steering to Broad Skills and Multiple Behaviours",
            "url": "https://arxiv.org/pdf/2403.05767"
          },
          {
            "title": "Fine-Grained Activation Steering: Steering Less, Achieving More",
            "url": "https://arxiv.org/pdf/2602.04428"
          },
          {
            "title": "Improving Activation Steering in Language Models with Mean-Centring",
            "url": "https://arxiv.org/pdf/2312.03813"
          },
          {
            "title": "Analysing the Safety Pitfalls of Steering Vectors",
            "url": "https://arxiv.org/pdf/2603.24543"
          }
        ]
      },
      "I found the paper! Here's what I found about arXiv 2605.01167:\n\n## \"Minimizing Collateral Damage in Activation Steering\"\n\n**Authors:** Tam Nguyen, Tu Anh Nguyen, Sina Alemohammad, Richard G. Baraniuk\n\n**Publication Date:** May 1, 2026\n\n**Core Concept:**\n\nActivation steering is a method for controlling Large Language Model (LLM) behavior by intervening in its internal representations to increase the alignment with a specific target feature direction. However, standard interventions, such as vector addition, often cause \"collateral damage\", defined as unintended changes in the alignment of activations along other non-target feature directions.\n\n**The Problem Being Addressed:**\n\nThis damage occurs because standard methods implicitly assume the isotropy of non-target features.\n\n**Proposed Solution:**\n\nThe work provides a mathematical formalization of collateral damage and introduces a principled framework that models steering as a constrained optimization problem. Their method finds a new activation that minimizes the expected squared collateral change weighted by the empirical second-moment matrix of activations.\n\nThe paper addresses a key challenge in using activation steering for LLM control—ensuring that efforts to steer a model toward desired behaviors don't inadvertently harm other aspects of the model's functioning."
    ],
    "durationSeconds": 5.988758522,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d6ffcda2-448b-4329-882c-8b3d5f410315",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-19T12:59:44.684Z_

Now let me fetch the full details of the critical paper (2605.05715) and the other two references:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e3662f8-c46d-4228-ac0a-d3e9b3c08653",
  "isSidechain": false,
  "requestId": "req_011CbBy91mQwL8JU8evkBKEj",
  "type": "assistant",
  "uuid": "c37641e0-0962-4646-85b1-edca3a2e3e12",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8owMgXEZ76YfTpXW2EHoh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 22184,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 754,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 184,
          "cache_read_input_tokens": 22184,
          "cache_creation_input_tokens": 754,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 754
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

_source line 20 · 2026-05-19T12:59:47.764Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0196VBn6LwMXjkJhB6CavKmP`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.05715",
  "prompt": "Extract the full abstract, all key findings, methodology details, specificity ratio definition and formula, the classification-correction gap explanation, all quantitative results (balanced accuracy, delta values, overlap percentages), the non-linear MLP results (delta=+2.8pp), all models tested, and the paper's recommendations for when linear steering fails. Include author names and date."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c37641e0-0962-4646-85b1-edca3a2e3e12",
  "isSidechain": false,
  "requestId": "req_011CbBy91mQwL8JU8evkBKEj",
  "type": "assistant",
  "uuid": "c80ae8b3-0874-4154-9bee-9e6e1a9d5b56",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8owMgXEZ76YfTpXW2EHoh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 754,
      "cache_read_input_tokens": 22184,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 754,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 184,
          "cache_read_input_tokens": 22184,
          "cache_creation_input_tokens": 754,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 754
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

_source line 21 · 2026-05-19T12:59:55.866Z_

<details><summary>↩ Tool result · `toolu_0196VBn6LwMXjkJhB6CavKmP`</summary>

```text
# Research Summary: Medical LLM Failure Detection

**Author & Date:** Ming Liu, submitted May 7, 2026

## Full Abstract
"Can linearly decodable failure signals in LLM hidden states be leveraged to correct those failures? We investigate this classification-correction gap via Overthinking (OT)--a stable behavioral regime (Jaccard >= 0.81, 94% inter-annotator agreement) in medical QA where models answer correctly under resampling yet fail in extended chain-of-thought."

## Key Findings

**The Core Paradox:** The researchers identified a phenomenon where problematic patterns are mathematically detectable in the model's internal representations at 71.6% balanced accuracy, yet cannot be fixed using standard steering techniques.

**Primary Quantitative Results:**
- Decodability: 71.6% balanced accuracy (p < 10⁻¹⁶)
- Steering impact: Delta ≈ 0 across 29 configurations
- Representational overlap: 85-88% with task-critical computation
- Specificity ratio: ≤ 0.152
- Non-targeted steering damage: -12.1 percentage points accuracy loss
- LEACE erasure impact: -3.6pp (p=0.01)
- Probe-steering correlation: r=-0.002 (p=0.97)

**Note:** The provided content does not include non-linear MLP results or delta=+2.8pp data.

## Methodology

Researchers tested 29 steering configurations across five linear families on medical question-answering tasks, examining internal model states (residual streams) to identify failure indicators.

## Positive Application

The decodable structure enabled selective abstention achieving held-out AUROC of 0.610, outperforming five uncertainty baselines (p=0.009).

## Recommendation

When linear steering fails despite decodability, leverage the detected signals for reliability estimation rather than direct correction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c80ae8b3-0874-4154-9bee-9e6e1a9d5b56",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "7eeed673-106b-460d-8140-a7956744bf5d",
  "toolUseResult": {
    "bytes": 46810,
    "code": 200,
    "codeText": "OK",
    "result": "# Research Summary: Medical LLM Failure Detection\n\n**Author & Date:** Ming Liu, submitted May 7, 2026\n\n## Full Abstract\n\"Can linearly decodable failure signals in LLM hidden states be leveraged to correct those failures? We investigate this classification-correction gap via Overthinking (OT)--a stable behavioral regime (Jaccard >= 0.81, 94% inter-annotator agreement) in medical QA where models answer correctly under resampling yet fail in extended chain-of-thought.\"\n\n## Key Findings\n\n**The Core Paradox:** The researchers identified a phenomenon where problematic patterns are mathematically detectable in the model's internal representations at 71.6% balanced accuracy, yet cannot be fixed using standard steering techniques.\n\n**Primary Quantitative Results:**\n- Decodability: 71.6% balanced accuracy (p < 10⁻¹⁶)\n- Steering impact: Delta ≈ 0 across 29 configurations\n- Representational overlap: 85-88% with task-critical computation\n- Specificity ratio: ≤ 0.152\n- Non-targeted steering damage: -12.1 percentage points accuracy loss\n- LEACE erasure impact: -3.6pp (p=0.01)\n- Probe-steering correlation: r=-0.002 (p=0.97)\n\n**Note:** The provided content does not include non-linear MLP results or delta=+2.8pp data.\n\n## Methodology\n\nResearchers tested 29 steering configurations across five linear families on medical question-answering tasks, examining internal model states (residual streams) to identify failure indicators.\n\n## Positive Application\n\nThe decodable structure enabled selective abstention achieving held-out AUROC of 0.610, outperforming five uncertainty baselines (p=0.009).\n\n## Recommendation\n\nWhen linear steering fails despite decodability, leverage the detected signals for reliability estimation rather than direct correction.",
    "durationMs": 8098,
    "url": "https://arxiv.org/abs/2605.05715"
  },
  "sourceToolAssistantUUID": "c80ae8b3-0874-4154-9bee-9e6e1a9d5b56",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"Disentangling Competing Calibration Biases via Geometry-Aware Activati…",
  "leafUuid": "7eeed673-106b-460d-8140-a7956744bf5d",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise calibration bias steering with steerability diagnostics",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340"
}
```

---

### Tool call

_source line 24 · 2026-05-19T13:00:01.551Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DsWBCyEWMzYmMF8Muyx3We`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.05715",
  "prompt": "Extract ALL details about: (1) the specificity ratio - exact definition, formula, how it's computed, what thresholds they recommend; (2) the non-linear residual MLP - architecture, results (especially the +2.8pp delta mentioned), how it compares to linear methods; (3) all models tested (names, sizes); (4) all datasets used; (5) the five families of linear steering tested; (6) the three convergent lines of evidence for representational entanglement; (7) any recommendations for practitioners about when to use non-linear vs linear steering; (8) the selective abstention results. Be extremely detailed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7eeed673-106b-460d-8140-a7956744bf5d",
  "isSidechain": false,
  "requestId": "req_011CbByA3UP5Ar48mwN1VX6P",
  "type": "assistant",
  "uuid": "2f7898e2-85bb-488e-98f3-08d1c69e02be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WirEWTsuET1XoA3Cz9xDf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 642,
      "cache_read_input_tokens": 22938,
      "output_tokens": 222,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 642,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 222,
          "cache_read_input_tokens": 22938,
          "cache_creation_input_tokens": 642,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 642
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

_source line 25 · 2026-05-19T13:00:27.945Z_

<details><summary>↩ Tool result · `toolu_01DsWBCyEWMzYmMF8Muyx3We`</summary>

```text
# Detailed Extraction: Medical LLM Steering Study

## (1) Specificity Ratio

**Definition & Formula:**
The specificity ratio measures how much of a failure-mode direction is unique versus shared with task-critical computation. Computed via shared-specific decomposition:

- Average specificity ratio for OT: **0.119** (Llama-3.1-8B), meaning 88% of the signal overlaps with correctness computation
- For Qwen2.5-7B OT-specific: **0.152** (comparable entanglement despite different overall geometry)
- Refusal control: **0.999** (nearly all variance mode-specific)

**Threshold Recommendation:**
The authors suggest a **4.7× specificity gap** as predictive. Directions with specificity ≥0.99 are steerable (refusal); those ≤0.21 are not. They note "a concrete quantitative threshold for future work" but emphasize this derives from a two-point comparison and requires validation.

**Permutation Test:**
Random null mean = 0.370; observed OT = 0.119 is significantly *below* all 10,000 permuted values (p<0.0001), confirming anomalously high shared-axis alignment.

---

## (2) Non-Linear Residual MLP

**Architecture:**
- 4096 → 64 → 4096 bottleneck residual adapter
- Trained on correct/OT supervision pairs
- Learned via standard supervised learning on classification task

**Results:**
- **Δ = +2.8pp** (p=0.025, McNemar; n=1,273)
- 140 corrections, 104 damages
- Reduces centroid distance by 50.6%

**Comparison to Linear:**
Authors conclude the MLP achieves "only modest behavioral gain—modest relative to the 50.6% centroid-distance reduction, consistent with only partial disentanglement." The high damage rate (8.2%) suggests the entanglement remains partially resistant even to non-linear transforms.

**Interpretation:**
"Non-linear learned interventions can partially close the gap" but don't fully resolve the issue, indicating the entanglement is "partial rather than absolute."

---

## (3) All Models Tested

| Model | Size | Architecture | Use |
|-------|------|--------------|-----|
| Llama-3.1-8B-Instruct | 8B | Llama | Primary steering experiments (29 configs) |
| Qwen2.5-7B-Instruct | 7B | Qwen | Cross-architecture validation (9 configs) |

Both open-weight models evaluated on MedQA test set (n=1,273 questions).

---

## (4) All Datasets Used

1. **MedQA** (primary)
   - 10,178 questions with 10 traces each = 101,780 total traces
   - Annotation: 34,532 traces from Llama (71.6% decodability, binary OT-vs-non-OT)
   - Test set: 1,273 questions for steering evaluation

2. **MMLU-STEM** (cross-domain validation)
   - 300 questions, 18 subjects
   - 10 traces each; 33.7% OT prevalence
   - Steering: n=300 (mode-specific Δ=0.0pp, uniform Δ=-7.0pp, multi-layer Δ=-6.7pp)

---

## (5) Five Families of Linear Steering

1. **Contrastive Steering**
   - Mode-specific or uniform shared component vectors
   - α ∈ [0.5, 3.0]
   - Confidence-gated variants

2. **Probe-Guided Steering**
   - Used probe weight vectors instead of contrastive vectors
   - n=1,175 questions with valid outputs
   - α ∈ [0.5, 1.0]

3. **Multi-Layer Steering**
   - Applied 1, 3, or 5 layers centered on peak layer
   - Tested simultaneous multi-layer interventions

4. **Rank-k Subspace Steering**
   - SVD-based rank-k bases (k ∈ {1,3,5})
   - Tested whether rank-1 restriction limited effectiveness
   - Probe and combined direction matrices

5. **Prompt-End Steering**
   - Vectors extracted from pre-generation hidden states (causally independent)
   - Near-orthogonal to last-token vectors (cosine ≤0.17)
   - Mode-specific, uniform, and composite variants

**Overall Result:** All 29 configurations yielded Δ≈0, with only uniform/shared steering causing harm (Δ=-12.1pp).

---

## (6) Three Convergent Lines of Evidence for Representational Entanglement

1. **Low Specificity**
   - OT direction: 85–88% overlap with task-critical computation
   - Specificity ratio ≤0.152 (Qwen), ≤0.119 (Llama)
   - Within-class variance exceeds inter-centroid gap by 2–4×

2. **Non-Targeted Shared-Direction Steering Damages Accuracy**
   - Uniform steering of shared component: Δ=-12.1pp (p<.001)
   - Consistent with failure-mode direction co-occurring with task computation
   - At Qwen: Δ=+0.5pp (null effect)

3. **LEACE Concept Erasure Damages Accuracy**
   - Mean-difference concept erasure: Δ=-3.6pp (p=0.01)
   - Direction-specific damage (131 corrections vs. 177 damages)
   - 10 random erasures: Δ=+0.3pp (σ=1.8pp)
   - Confirms OT signal is causally entangled, not merely correlational

---

## (7) Practitioner Recommendations

The paper provides **four pre-intervention diagnostics** (noted as hypothesis-generating, not validated predictors):

1. **Specificity ratio check** – Directions ≥0.99 steerable; ≤0.21 are not
2. **Within-class variance analysis** – Compare to inter-centroid gap
3. **Cross-architecture stability** – Consistent signal across models
4. **Cross-domain subspace alignment at intervention layer** – Should not degrade at steering layers

**When Non-Linear Steering May Help:**
- Authors note "instance-adaptive methods (K-CAST, DAS, ReFT) could succeed by learning to disentangle shared directions"
- Learned non-linear approaches show promise but face high damage rates (8.2%)
- Use when linear methods fail *and* you have supervision pairs; untested methods remain open

**Clear Guidance:**
"Reading representations has operational value even when linear writing to them does not—probing success, even when robust and cross-domain transferable, does not imply steerability."

---

## (8) Selective Abstention Results

**Performance on Training Data (Balanced 50/50):**
- Probe AUROC = 0.716 (layer 21, selected via held-out scan)
- 5-fold CV: 0.721 ± 0.005
- At 60% coverage: +14.0pp accuracy gain (vs. 50% balanced baseline)
- At 70% coverage: +5.7pp gain

**Test Set Performance:**
- Held-out AUROC = 0.610 (95% CI: [0.577, 0.642])
- Generalization gap (0.716→0.610) primarily temperature-driven (cross-temperature vector cosine = 0.41)
- At 60% coverage: +5.5pp accuracy (72.3%)
- At 70% coverage: +5.7pp accuracy

**Superiority Over Baselines:**
- Exceeds all five single-forward-pass uncertainty baselines (Δ=0.041 AUROC, p=0.009)
- Best baseline: 0.569 AUROC
- Competes with best-of-NN probe selection (BoN@3 vs. MV@3: +1.4pp at identical cost)
- Self-consistency achieves higher AUROC (0.804) but at 10× cost

**Key Insight:**
"Decodable failure structure supports post-generation reliability estimation even when the fixed linear steering family cannot exploit it for correction."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f7898e2-85bb-488e-98f3-08d1c69e02be",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "bb28e57a-5ef7-4db2-9266-b0472d6f2d6b",
  "toolUseResult": {
    "bytes": 462213,
    "code": 200,
    "codeText": "OK",
    "result": "# Detailed Extraction: Medical LLM Steering Study\n\n## (1) Specificity Ratio\n\n**Definition & Formula:**\nThe specificity ratio measures how much of a failure-mode direction is unique versus shared with task-critical computation. Computed via shared-specific decomposition:\n\n- Average specificity ratio for OT: **0.119** (Llama-3.1-8B), meaning 88% of the signal overlaps with correctness computation\n- For Qwen2.5-7B OT-specific: **0.152** (comparable entanglement despite different overall geometry)\n- Refusal control: **0.999** (nearly all variance mode-specific)\n\n**Threshold Recommendation:**\nThe authors suggest a **4.7× specificity gap** as predictive. Directions with specificity ≥0.99 are steerable (refusal); those ≤0.21 are not. They note \"a concrete quantitative threshold for future work\" but emphasize this derives from a two-point comparison and requires validation.\n\n**Permutation Test:**\nRandom null mean = 0.370; observed OT = 0.119 is significantly *below* all 10,000 permuted values (p<0.0001), confirming anomalously high shared-axis alignment.\n\n---\n\n## (2) Non-Linear Residual MLP\n\n**Architecture:**\n- 4096 → 64 → 4096 bottleneck residual adapter\n- Trained on correct/OT supervision pairs\n- Learned via standard supervised learning on classification task\n\n**Results:**\n- **Δ = +2.8pp** (p=0.025, McNemar; n=1,273)\n- 140 corrections, 104 damages\n- Reduces centroid distance by 50.6%\n\n**Comparison to Linear:**\nAuthors conclude the MLP achieves \"only modest behavioral gain—modest relative to the 50.6% centroid-distance reduction, consistent with only partial disentanglement.\" The high damage rate (8.2%) suggests the entanglement remains partially resistant even to non-linear transforms.\n\n**Interpretation:**\n\"Non-linear learned interventions can partially close the gap\" but don't fully resolve the issue, indicating the entanglement is \"partial rather than absolute.\"\n\n---\n\n## (3) All Models Tested\n\n| Model | Size | Architecture | Use |\n|-------|------|--------------|-----|\n| Llama-3.1-8B-Instruct | 8B | Llama | Primary steering experiments (29 configs) |\n| Qwen2.5-7B-Instruct | 7B | Qwen | Cross-architecture validation (9 configs) |\n\nBoth open-weight models evaluated on MedQA test set (n=1,273 questions).\n\n---\n\n## (4) All Datasets Used\n\n1. **MedQA** (primary)\n   - 10,178 questions with 10 traces each = 101,780 total traces\n   - Annotation: 34,532 traces from Llama (71.6% decodability, binary OT-vs-non-OT)\n   - Test set: 1,273 questions for steering evaluation\n\n2. **MMLU-STEM** (cross-domain validation)\n   - 300 questions, 18 subjects\n   - 10 traces each; 33.7% OT prevalence\n   - Steering: n=300 (mode-specific Δ=0.0pp, uniform Δ=-7.0pp, multi-layer Δ=-6.7pp)\n\n---\n\n## (5) Five Families of Linear Steering\n\n1. **Contrastive Steering**\n   - Mode-specific or uniform shared component vectors\n   - α ∈ [0.5, 3.0]\n   - Confidence-gated variants\n\n2. **Probe-Guided Steering**\n   - Used probe weight vectors instead of contrastive vectors\n   - n=1,175 questions with valid outputs\n   - α ∈ [0.5, 1.0]\n\n3. **Multi-Layer Steering**\n   - Applied 1, 3, or 5 layers centered on peak layer\n   - Tested simultaneous multi-layer interventions\n\n4. **Rank-k Subspace Steering**\n   - SVD-based rank-k bases (k ∈ {1,3,5})\n   - Tested whether rank-1 restriction limited effectiveness\n   - Probe and combined direction matrices\n\n5. **Prompt-End Steering**\n   - Vectors extracted from pre-generation hidden states (causally independent)\n   - Near-orthogonal to last-token vectors (cosine ≤0.17)\n   - Mode-specific, uniform, and composite variants\n\n**Overall Result:** All 29 configurations yielded Δ≈0, with only uniform/shared steering causing harm (Δ=-12.1pp).\n\n---\n\n## (6) Three Convergent Lines of Evidence for Representational Entanglement\n\n1. **Low Specificity**\n   - OT direction: 85–88% overlap with task-critical computation\n   - Specificity ratio ≤0.152 (Qwen), ≤0.119 (Llama)\n   - Within-class variance exceeds inter-centroid gap by 2–4×\n\n2. **Non-Targeted Shared-Direction Steering Damages Accuracy**\n   - Uniform steering of shared component: Δ=-12.1pp (p<.001)\n   - Consistent with failure-mode direction co-occurring with task computation\n   - At Qwen: Δ=+0.5pp (null effect)\n\n3. **LEACE Concept Erasure Damages Accuracy**\n   - Mean-difference concept erasure: Δ=-3.6pp (p=0.01)\n   - Direction-specific damage (131 corrections vs. 177 damages)\n   - 10 random erasures: Δ=+0.3pp (σ=1.8pp)\n   - Confirms OT signal is causally entangled, not merely correlational\n\n---\n\n## (7) Practitioner Recommendations\n\nThe paper provides **four pre-intervention diagnostics** (noted as hypothesis-generating, not validated predictors):\n\n1. **Specificity ratio check** – Directions ≥0.99 steerable; ≤0.21 are not\n2. **Within-class variance analysis** – Compare to inter-centroid gap\n3. **Cross-architecture stability** – Consistent signal across models\n4. **Cross-domain subspace alignment at intervention layer** – Should not degrade at steering layers\n\n**When Non-Linear Steering May Help:**\n- Authors note \"instance-adaptive methods (K-CAST, DAS, ReFT) could succeed by learning to disentangle shared directions\"\n- Learned non-linear approaches show promise but face high damage rates (8.2%)\n- Use when linear methods fail *and* you have supervision pairs; untested methods remain open\n\n**Clear Guidance:**\n\"Reading representations has operational value even when linear writing to them does not—probing success, even when robust and cross-domain transferable, does not imply steerability.\"\n\n---\n\n## (8) Selective Abstention Results\n\n**Performance on Training Data (Balanced 50/50):**\n- Probe AUROC = 0.716 (layer 21, selected via held-out scan)\n- 5-fold CV: 0.721 ± 0.005\n- At 60% coverage: +14.0pp accuracy gain (vs. 50% balanced baseline)\n- At 70% coverage: +5.7pp gain\n\n**Test Set Performance:**\n- Held-out AUROC = 0.610 (95% CI: [0.577, 0.642])\n- Generalization gap (0.716→0.610) primarily temperature-driven (cross-temperature vector cosine = 0.41)\n- At 60% coverage: +5.5pp accuracy (72.3%)\n- At 70% coverage: +5.7pp accuracy\n\n**Superiority Over Baselines:**\n- Exceeds all five single-forward-pass uncertainty baselines (Δ=0.041 AUROC, p=0.009)\n- Best baseline: 0.569 AUROC\n- Competes with best-of-NN probe selection (BoN@3 vs. MV@3: +1.4pp at identical cost)\n- Self-consistency achieves higher AUROC (0.804) but at 10× cost\n\n**Key Insight:**\n\"Decodable failure structure supports post-generation reliability estimation even when the fixed linear steering family cannot exploit it for correction.\"",
    "durationMs": 26386,
    "url": "https://arxiv.org/html/2605.05715"
  },
  "sourceToolAssistantUUID": "2f7898e2-85bb-488e-98f3-08d1c69e02be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-19T13:00:31.753Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BTermeNer9BcrHkjcEtBkm`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.19375",
  "prompt": "Extract full abstract, key methodology details about norm-preserving rotation formulation, discriminative layer selection method, all models tested, all quantitative results, comparison with Angular Steering and other baselines, and key findings about when/which layers to steer. Include author names and date."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb28e57a-5ef7-4db2-9266-b0472d6f2d6b",
  "isSidechain": false,
  "requestId": "req_011CbByCQcfzmS6WSefAANZP",
  "type": "assistant",
  "uuid": "8226d876-420a-49ab-a8b1-d4bcbe89622a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UfrbZjo9spkaR6qXTGaPZ8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2285,
      "cache_read_input_tokens": 23580,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 23580,
          "cache_creation_input_tokens": 2285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2285
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

_source line 27 · 2026-05-19T13:00:37.255Z_

<details><summary>↩ Tool result · `toolu_01BTermeNer9BcrHkjcEtBkm`</summary>

```text
# Selective Steering: Research Summary

**Authors & Date:** Quy-Anh Dang and Chris Ngo (submitted January 27, 2026)

## Abstract
The paper addresses vulnerabilities in large language models to adversarial attacks through activation steering. The authors identify limitations in existing methods: activation addition requires coefficient tuning and is sensitive to norm variations, while directional ablation offers only binary control. They note that Angular Steering's practical implementation violates norm preservation, causing distribution shift.

## Key Methodology

**Norm-Preserving Rotation Formulation:**
The approach uses "a mathematically rigorous norm-preserving rotation formulation that maintains activation distribution integrity," enabling continuous control while preventing distribution collapse.

**Discriminative Layer Selection:**
The method "applies steering only where feature representations exhibit opposite-signed class alignment," selecting layers where steering is most effective rather than applying it uniformly across the model.

## Models & Results
The research tested nine models, demonstrating that Selective Steering achieves "5.5x higher attack success rates than prior methods while maintaining zero perplexity violations and approximately 100% capability retention on standard benchmarks."

## Key Findings
The method proves particularly valuable for smaller models (below 7B parameters), where previous approaches caused generation collapse. The discriminative selection ensures efficient, targeted intervention without compromising model functionality.

**Code:** Available on GitHub (https://github.com/knoveleng/steering)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8226d876-420a-49ab-a8b1-d4bcbe89622a",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "5dea3fb3-002a-4003-9dbd-f1cceb122349",
  "toolUseResult": {
    "bytes": 47414,
    "code": 200,
    "codeText": "OK",
    "result": "# Selective Steering: Research Summary\n\n**Authors & Date:** Quy-Anh Dang and Chris Ngo (submitted January 27, 2026)\n\n## Abstract\nThe paper addresses vulnerabilities in large language models to adversarial attacks through activation steering. The authors identify limitations in existing methods: activation addition requires coefficient tuning and is sensitive to norm variations, while directional ablation offers only binary control. They note that Angular Steering's practical implementation violates norm preservation, causing distribution shift.\n\n## Key Methodology\n\n**Norm-Preserving Rotation Formulation:**\nThe approach uses \"a mathematically rigorous norm-preserving rotation formulation that maintains activation distribution integrity,\" enabling continuous control while preventing distribution collapse.\n\n**Discriminative Layer Selection:**\nThe method \"applies steering only where feature representations exhibit opposite-signed class alignment,\" selecting layers where steering is most effective rather than applying it uniformly across the model.\n\n## Models & Results\nThe research tested nine models, demonstrating that Selective Steering achieves \"5.5x higher attack success rates than prior methods while maintaining zero perplexity violations and approximately 100% capability retention on standard benchmarks.\"\n\n## Key Findings\nThe method proves particularly valuable for smaller models (below 7B parameters), where previous approaches caused generation collapse. The discriminative selection ensures efficient, targeted intervention without compromising model functionality.\n\n**Code:** Available on GitHub (https://github.com/knoveleng/steering)",
    "durationMs": 5498,
    "url": "https://arxiv.org/abs/2601.19375"
  },
  "sourceToolAssistantUUID": "8226d876-420a-49ab-a8b1-d4bcbe89622a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28 · 2026-05-19T13:00:37.259Z_

```json
{
  "parentUuid": "5dea3fb3-002a-4003-9dbd-f1cceb122349",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "c65acca1-3cf1-431d-baef-94e674b36774",
  "timestamp": "2026-05-19T13:00:37.259Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 29 · 2026-05-19T13:00:40.725Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017ZrwLBFsik2vobWDu7ZvrC`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.01167",
  "prompt": "Extract full abstract, the mathematical formalization of collateral damage, the constrained optimization formulation, the second-moment matrix approach, all models tested, all quantitative results showing improvement over standard steering, key findings about isotropy assumptions, and practical recommendations. Include author names and date."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c65acca1-3cf1-431d-baef-94e674b36774",
  "isSidechain": false,
  "requestId": "req_011CbByD6Qa9uEfTACyMTpog",
  "type": "assistant",
  "uuid": "e311f2ba-9c5b-44ab-896e-f5368a237e82",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DGxGDVwWbUbLWu1qHbxcX6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 568,
      "cache_read_input_tokens": 25865,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 568,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 25865,
          "cache_creation_input_tokens": 568,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 568
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

_source line 30 · 2026-05-19T13:00:46.114Z_

<details><summary>↩ Tool result · `toolu_017ZrwLBFsik2vobWDu7ZvrC`</summary>

```text
# Paper Summary: Minimizing Collateral Damage in Activation Steering

**Authors & Date:**
Tam Nguyen, Tu Anh Nguyen, Sina Alemohammad, Richard G. Baraniuk
Submitted: May 1, 2026

**Full Abstract:**
"Activation steering is a method for controlling Large Language Model (LLM) behavior by intervening in its internal representations to increase the alignment with a specific target feature direction. However, standard interventions, such as vector addition, often cause 'collateral damage', defined as unintended changes in the alignment of activations along other non-target feature directions."

The authors note that standard methods fail because they "implicitly assume the isotropy of non-target features."

---

## Key Contributions

**Mathematical Formalization:**
The paper establishes collateral damage as unintended activation changes across non-target feature directions, distinguishing this from the isotropy assumption that treats all directions uniformly.

**Constrained Optimization Framework:**
The method formulates steering as a constrained optimization problem designed to minimize expected squared collateral change.

**Second-Moment Matrix Approach:**
Rather than uniform penalization, the solution uses the "empirical second-moment matrix of activations" to encode "nonuniform cost of the perturbation in different feature directions."

---

## Results & Key Findings

The abstract emphasizes that their approach achieves "more precise control while reducing the degradation of model performance on unrelated tasks"—addressing the isotropy problem that undermines standard steering methods.

**Note:** The page excerpt provided lacks detailed quantitative results, specific model names tested, and practical recommendations beyond the core methodological contribution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e311f2ba-9c5b-44ab-896e-f5368a237e82",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "8bfc0e48-cfe1-4cb8-a1e7-c1687d28e1d9",
  "toolUseResult": {
    "bytes": 46600,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary: Minimizing Collateral Damage in Activation Steering\n\n**Authors & Date:**\nTam Nguyen, Tu Anh Nguyen, Sina Alemohammad, Richard G. Baraniuk\nSubmitted: May 1, 2026\n\n**Full Abstract:**\n\"Activation steering is a method for controlling Large Language Model (LLM) behavior by intervening in its internal representations to increase the alignment with a specific target feature direction. However, standard interventions, such as vector addition, often cause 'collateral damage', defined as unintended changes in the alignment of activations along other non-target feature directions.\"\n\nThe authors note that standard methods fail because they \"implicitly assume the isotropy of non-target features.\"\n\n---\n\n## Key Contributions\n\n**Mathematical Formalization:**\nThe paper establishes collateral damage as unintended activation changes across non-target feature directions, distinguishing this from the isotropy assumption that treats all directions uniformly.\n\n**Constrained Optimization Framework:**\nThe method formulates steering as a constrained optimization problem designed to minimize expected squared collateral change.\n\n**Second-Moment Matrix Approach:**\nRather than uniform penalization, the solution uses the \"empirical second-moment matrix of activations\" to encode \"nonuniform cost of the perturbation in different feature directions.\"\n\n---\n\n## Results & Key Findings\n\nThe abstract emphasizes that their approach achieves \"more precise control while reducing the degradation of model performance on unrelated tasks\"—addressing the isotropy problem that undermines standard steering methods.\n\n**Note:** The page excerpt provided lacks detailed quantitative results, specific model names tested, and practical recommendations beyond the core methodological contribution.",
    "durationMs": 5385,
    "url": "https://arxiv.org/abs/2605.01167"
  },
  "sourceToolAssistantUUID": "e311f2ba-9c5b-44ab-896e-f5368a237e82",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-19T13:00:48.975Z_

Now let me search for more details on the collateral damage paper and also look for additional related work on the classification-correction gap:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bfc0e48-cfe1-4cb8-a1e7-c1687d28e1d9",
  "isSidechain": false,
  "requestId": "req_011CbByDkGPqhpqSYhoL7ZLh",
  "type": "assistant",
  "uuid": "61341dcf-b10e-423e-841d-28c30ceef759",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018jbF3Q9nWFdRgMcK4bTCUx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 26433,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 523,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 26433,
          "cache_creation_input_tokens": 523,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 523
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

_source line 32 · 2026-05-19T13:00:50.692Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Sg2yjiRYtW1LSJrdoiW17V`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.01167v1",
  "prompt": "Extract ALL quantitative results: models tested (names, sizes), datasets used, metrics reported, comparison with standard steering baselines, specific numbers showing collateral damage reduction, the closed-form solution details, and any ablation studies. Focus on concrete numbers and formulas."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61341dcf-b10e-423e-841d-28c30ceef759",
  "isSidechain": false,
  "requestId": "req_011CbByDkGPqhpqSYhoL7ZLh",
  "type": "assistant",
  "uuid": "5ccc7266-d2ec-4981-86f4-6f9873717df8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018jbF3Q9nWFdRgMcK4bTCUx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 26433,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 523,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 166,
          "cache_read_input_tokens": 26433,
          "cache_creation_input_tokens": 523,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 523
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

_source line 33 · 2026-05-19T13:01:02.112Z_

<details><summary>↩ Tool result · `toolu_01Sg2yjiRYtW1LSJrdoiW17V`</summary>

```text
# COAST: Quantitative Results Summary

## Models Tested
- Llama-3.2-3B-Instruct
- Llama-3.1-8B-Instruct
- Qwen2.5-14B-Instruct
- Gemma-2-9B-IT

## Datasets & Evaluation Metrics

**Steering Effectiveness:** Attack Success Rate (ASR) measuring "fraction of harmful instructions for which the steered model successfully produces a jailbreak completion"

**Performance Preservation:** tinyBenchmarks suite including:
- ARC, MMLU, Winogrande, GSM8K, TruthfulQA, HellaSwag (100 examples each)
- Perplexity (PPL) and Task Accuracy measurements

## Key Quantitative Results

**Trade-off Improvements (Figure 3):**
- COAST achieves up to 30% improvement in ASR over Angular Steering
- 20% accuracy advantage over ActAdd at equivalent ASR levels
- Maintains task performance comparable to unsteered baselines

**COAST vs. Slerp Comparison (Table 1):**

| Model | Metric | COAST | Slerp |
|-------|--------|-------|-------|
| Llama-3.1-8B | Avg ASR | 52.13% | 51.67% |
| Llama-3.2-3B | Avg ASR | 54.76% | 52.68% |
| Gemma-2-9B | Avg ASR | 19.48% | 19.28% |

**Collateral Damage Validation (Figure 1):**
Strong negative Pearson correlation (r < -0.9) across all six benchmarks between average collateral damage and model accuracy, validating the collateral damage metric as performance predictor

**Computational Efficiency:**
- 0.9%-4.0% overhead compared to unsteered baseline
- <1.5% slower than Slerp baseline

## Mathematical Formulation

**Collateral Damage Objective:**
The method minimizes: J(x) = (x−h)^T Σ(x−h) subject to norm preservation (‖x‖=1) and alignment budget (d^T x = α)

**Feasible Set Geometry:**
The constraint manifold M forms a (p−2)-sphere with center αd and radius r = √(1−α²)

**Closed-form Solutions (Isotropic Cases):**
When features are orthogonal to target direction d, the optimal solution reduces to: x* = αd + r(h − (d^T h)d)/‖h − (d^T h)d‖, which equals Slerp steering

## Theoretical Guarantees

**Convergence (Theorem 1):** The continuous-time Riemannian gradient flow converges to global minimum with proper initialization at the Euclidean projection of h onto M

**Step-size Bounds (Proposition 1):** η ≤ 1/L where L = 2‖Π_{d⊥}ΣΠ_{d⊥}‖₂, guaranteeing descent inequality: J(x_{t+1}) ≤ J(x_t) − (η/2)‖grad J(x_t)‖²

## Collateral Matrix Construction

The method uses empirical second moment: Σ_{h_ref} = E[h_ref h_ref^T], which naturally captures both individual feature moments and co-activation terms, avoiding the independence assumption of dictionary-based approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ccc7266-d2ec-4981-86f4-6f9873717df8",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "cf5a2321-b9af-4590-9fa5-c3e691cf3aad",
  "toolUseResult": {
    "bytes": 645295,
    "code": 200,
    "codeText": "OK",
    "result": "# COAST: Quantitative Results Summary\n\n## Models Tested\n- Llama-3.2-3B-Instruct\n- Llama-3.1-8B-Instruct\n- Qwen2.5-14B-Instruct\n- Gemma-2-9B-IT\n\n## Datasets & Evaluation Metrics\n\n**Steering Effectiveness:** Attack Success Rate (ASR) measuring \"fraction of harmful instructions for which the steered model successfully produces a jailbreak completion\"\n\n**Performance Preservation:** tinyBenchmarks suite including:\n- ARC, MMLU, Winogrande, GSM8K, TruthfulQA, HellaSwag (100 examples each)\n- Perplexity (PPL) and Task Accuracy measurements\n\n## Key Quantitative Results\n\n**Trade-off Improvements (Figure 3):**\n- COAST achieves up to 30% improvement in ASR over Angular Steering\n- 20% accuracy advantage over ActAdd at equivalent ASR levels\n- Maintains task performance comparable to unsteered baselines\n\n**COAST vs. Slerp Comparison (Table 1):**\n\n| Model | Metric | COAST | Slerp |\n|-------|--------|-------|-------|\n| Llama-3.1-8B | Avg ASR | 52.13% | 51.67% |\n| Llama-3.2-3B | Avg ASR | 54.76% | 52.68% |\n| Gemma-2-9B | Avg ASR | 19.48% | 19.28% |\n\n**Collateral Damage Validation (Figure 1):**\nStrong negative Pearson correlation (r < -0.9) across all six benchmarks between average collateral damage and model accuracy, validating the collateral damage metric as performance predictor\n\n**Computational Efficiency:**\n- 0.9%-4.0% overhead compared to unsteered baseline\n- <1.5% slower than Slerp baseline\n\n## Mathematical Formulation\n\n**Collateral Damage Objective:**\nThe method minimizes: J(x) = (x−h)^T Σ(x−h) subject to norm preservation (‖x‖=1) and alignment budget (d^T x = α)\n\n**Feasible Set Geometry:**\nThe constraint manifold M forms a (p−2)-sphere with center αd and radius r = √(1−α²)\n\n**Closed-form Solutions (Isotropic Cases):**\nWhen features are orthogonal to target direction d, the optimal solution reduces to: x* = αd + r(h − (d^T h)d)/‖h − (d^T h)d‖, which equals Slerp steering\n\n## Theoretical Guarantees\n\n**Convergence (Theorem 1):** The continuous-time Riemannian gradient flow converges to global minimum with proper initialization at the Euclidean projection of h onto M\n\n**Step-size Bounds (Proposition 1):** η ≤ 1/L where L = 2‖Π_{d⊥}ΣΠ_{d⊥}‖₂, guaranteeing descent inequality: J(x_{t+1}) ≤ J(x_t) − (η/2)‖grad J(x_t)‖²\n\n## Collateral Matrix Construction\n\nThe method uses empirical second moment: Σ_{h_ref} = E[h_ref h_ref^T], which naturally captures both individual feature moments and co-activation terms, avoiding the independence assumption of dictionary-based approaches.",
    "durationMs": 11417,
    "url": "https://arxiv.org/html/2605.01167v1"
  },
  "sourceToolAssistantUUID": "5ccc7266-d2ec-4981-86f4-6f9873717df8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"Disentangling Competing Calibration Biases via Geometry-Aware Activati…",
  "leafUuid": "cf5a2321-b9af-4590-9fa5-c3e691cf3aad",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise calibration bias steering with steerability diagnostics",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340"
}
```

---

### Tool call

_source line 36 · 2026-05-19T13:01:06.406Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KN1o8hZCyTcYXXMXsZt3JB`</summary>

```json
{
  "query": "specificity ratio activation steering decodable steerable gap entanglement task-critical directions LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf5a2321-b9af-4590-9fa5-c3e691cf3aad",
  "isSidechain": false,
  "requestId": "req_011CbByEvmSd21zuWuvr6MYX",
  "type": "assistant",
  "uuid": "faf6579b-1d46-4475-ac96-027a2ba1187e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MrCwhamNJNGyDVpMzYsZAk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1033,
      "cache_read_input_tokens": 26956,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1033,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 26956,
          "cache_creation_input_tokens": 1033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1033
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

_source line 37 · 2026-05-19T13:01:14.936Z_

<details><summary>↩ Tool result · `toolu_01KN1o8hZCyTcYXXMXsZt3JB`</summary>

```text
Web search results for query: "specificity ratio activation steering decodable steerable gap entanglement task-critical directions LLM 2026"

Links: [{"title":"Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes","url":"https://arxiv.org/html/2605.05715"},{"title":"[2605.05715] Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes","url":"https://arxiv.org/abs/2605.05715"},{"title":"SteeringSafety: A Systematic Safety Evaluation Framework of Representation Steering in LLMs","url":"https://arxiv.org/html/2509.13450"},{"title":"Activation Steering in LLMs","url":"https://www.emergentmind.com/topics/activation-steering-method"},{"title":"SteeringControl: Holistic Evaluation of Alignment Steering in LLMs","url":"https://arxiv.org/html/2509.13450v1"},{"title":"Latent Steering Vectors in Deep Models","url":"https://www.emergentmind.com/topics/latent-steering-vectors"},{"title":"Steerable but Not Decodable: Function Vectors Operate Beyond the Logit Lens","url":"https://arxiv.org/pdf/2604.02608"}]

Based on the search results, I found highly relevant recent research on these topics from 2026 and late 2025:

## Key Findings

The specificity ratio is a metric where the OT (Overthinking) direction has 85-88% overlap with task-critical computation (specificity ratio <= 0.152). When the OT-specific specificity ratio is only 0.119, it means 88% of the signal is shared with task-relevant directions, and concept erasure damages accuracy, providing causal evidence that the decodable signal is entangled with task computation.

## Classification-Correction Gap

Research on the classification-correction gap examines whether linearly decodable failure signals in LLM hidden states can be leveraged to correct failures. OT is linearly decodable at 71.6% balanced accuracy, yet five families of fixed linear steering with 29 configurations all yield near-zero results.

## Representational Entanglement

Three convergent lines of evidence suggest representational entanglement: the OT direction has 85-88% overlap with task-critical computation; non-targeted shared-direction steering damages accuracy; and LEACE concept erasure damages accuracy.

## Broader Context on Steering

All steering methods exhibit substantial entanglement, with social behaviors showing highest vulnerability reaching degradation as high as 76%, jailbreaking often compromising normative judgment, and hallucination steering unpredictably shifting political views.

These results suggest fundamental challenges in activation steering due to the entanglement of decodable directions with task-critical computation in LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "faf6579b-1d46-4475-ac96-027a2ba1187e",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "f2bcfb12-6faa-4f40-9268-44f347a82aa5",
  "toolUseResult": {
    "query": "specificity ratio activation steering decodable steerable gap entanglement task-critical directions LLM 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012bLEVofhHrrMdXaLNiW1cD",
        "content": [
          {
            "title": "Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes",
            "url": "https://arxiv.org/html/2605.05715"
          },
          {
            "title": "[2605.05715] Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes",
            "url": "https://arxiv.org/abs/2605.05715"
          },
          {
            "title": "SteeringSafety: A Systematic Safety Evaluation Framework of Representation Steering in LLMs",
            "url": "https://arxiv.org/html/2509.13450"
          },
          {
            "title": "Activation Steering in LLMs",
            "url": "https://www.emergentmind.com/topics/activation-steering-method"
          },
          {
            "title": "SteeringControl: Holistic Evaluation of Alignment Steering in LLMs",
            "url": "https://arxiv.org/html/2509.13450v1"
          },
          {
            "title": "Latent Steering Vectors in Deep Models",
            "url": "https://www.emergentmind.com/topics/latent-steering-vectors"
          },
          {
            "title": "Steerable but Not Decodable: Function Vectors Operate Beyond the Logit Lens",
            "url": "https://arxiv.org/pdf/2604.02608"
          }
        ]
      },
      "Based on the search results, I found highly relevant recent research on these topics from 2026 and late 2025:\n\n## Key Findings\n\nThe specificity ratio is a metric where the OT (Overthinking) direction has 85-88% overlap with task-critical computation (specificity ratio <= 0.152). When the OT-specific specificity ratio is only 0.119, it means 88% of the signal is shared with task-relevant directions, and concept erasure damages accuracy, providing causal evidence that the decodable signal is entangled with task computation.\n\n## Classification-Correction Gap\n\nResearch on the classification-correction gap examines whether linearly decodable failure signals in LLM hidden states can be leveraged to correct failures. OT is linearly decodable at 71.6% balanced accuracy, yet five families of fixed linear steering with 29 configurations all yield near-zero results.\n\n## Representational Entanglement\n\nThree convergent lines of evidence suggest representational entanglement: the OT direction has 85-88% overlap with task-critical computation; non-targeted shared-direction steering damages accuracy; and LEACE concept erasure damages accuracy.\n\n## Broader Context on Steering\n\nAll steering methods exhibit substantial entanglement, with social behaviors showing highest vulnerability reaching degradation as high as 76%, jailbreaking often compromising normative judgment, and hallucination steering unpredictably shifting political views.\n\nThese results suggest fundamental challenges in activation steering due to the entanglement of decodable directions with task-critical computation in LLMs."
    ],
    "durationSeconds": 8.52427913200001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "faf6579b-1d46-4475-ac96-027a2ba1187e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-19T13:01:18.070Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019NQjcGHTvVDY8nh9hh6BAa`</summary>

```json
{
  "query": "\"classification-correction gap\" OR \"decodable but not steerable\" activation steering nonlinear correction MLP residual 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2bcfb12-6faa-4f40-9268-44f347a82aa5",
  "isSidechain": false,
  "requestId": "req_011CbByFsVmdYPQEUMRdsPzX",
  "type": "assistant",
  "uuid": "a8d8ec1f-9c65-4cfa-ba1a-b58c21357141",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016sfWxXuLeNHj3WpRh6SAnn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 804,
      "cache_read_input_tokens": 27989,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 804,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 27989,
          "cache_creation_input_tokens": 804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 804
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

_source line 39 · 2026-05-19T13:01:30.799Z_

<details><summary>↩ Tool result · `toolu_019NQjcGHTvVDY8nh9hh6BAa`</summary>

```text
Web search results for query: ""classification-correction gap" OR "decodable but not steerable" activation steering nonlinear correction MLP residual 2025 2026"

Links: [{"title":"Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes","url":"https://arxiv.org/html/2605.05715"},{"title":"No Training Wheels: Steering Vectors for Bias Correction at Inference Time","url":"https://arxiv.org/html/2506.18598v1"},{"title":"Steerable but Not Decodable: Function Vectors Operate Beyond the Logit Lens","url":"https://arxiv.org/html/2604.02608v1"},{"title":"Activation Steering for Masked Diffusion Language Models","url":"https://arxiv.org/html/2512.24143v1"},{"title":"[2605.05715] Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes","url":"https://arxiv.org/abs/2605.05715"},{"title":"No Training Wheels: Steering Vectors for Bias Correction at Inference Time","url":"https://arxiv.org/pdf/2506.18598"},{"title":"Steerable but Not Decodable: Function Vectors Operate Beyond the Logit Lens","url":"https://arxiv.org/pdf/2604.02608"}]

I found highly relevant research on these topics. Here are the key papers:

## Primary Result: "Decodable but Not Corrected" Paper

The most directly relevant paper investigates the classification-correction gap via Overthinking (OT)—a behavioral regime in medical QA where models answer correctly under resampling yet fail in extended chain-of-thought. OT is linearly decodable at 71.6% balanced accuracy, yet five families of fixed linear steering (29 configurations) all yield negligible correction, with identical null results cross-architecture and cross-domain.

Three convergent lines of evidence suggest representational entanglement: the OT direction has 85–88% overlap with task-critical computation. Importantly for your query, a learned non-linear residual MLP produces modest behavioral gain—consistent with partial but incomplete disentanglement of the shared subspace.

## Related Finding: Inverse Gap

Interestingly, there's a complementary dissociation: FV steering succeeds even when the logit lens cannot decode the correct answer at any layer, across 4,032 pairs across 12 tasks and 6 models. Even highly effective FVs project to incoherent token distributions, suggesting FVs encode computational instructions that the model's nonlinear processing executes through pathways invisible to the unembedding.

These papers from 2025-2026 directly address the phenomena you're searching for.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8d8ec1f-9c65-4cfa-ba1a-b58c21357141",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "b79ee93a-8c50-4cb7-9f92-c32a658b3732",
  "toolUseResult": {
    "query": "\"classification-correction gap\" OR \"decodable but not steerable\" activation steering nonlinear correction MLP residual 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018tgvSRKiGbgVVmwWEN6YHG",
        "content": [
          {
            "title": "Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes",
            "url": "https://arxiv.org/html/2605.05715"
          },
          {
            "title": "No Training Wheels: Steering Vectors for Bias Correction at Inference Time",
            "url": "https://arxiv.org/html/2506.18598v1"
          },
          {
            "title": "Steerable but Not Decodable: Function Vectors Operate Beyond the Logit Lens",
            "url": "https://arxiv.org/html/2604.02608v1"
          },
          {
            "title": "Activation Steering for Masked Diffusion Language Models",
            "url": "https://arxiv.org/html/2512.24143v1"
          },
          {
            "title": "[2605.05715] Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes",
            "url": "https://arxiv.org/abs/2605.05715"
          },
          {
            "title": "No Training Wheels: Steering Vectors for Bias Correction at Inference Time",
            "url": "https://arxiv.org/pdf/2506.18598"
          },
          {
            "title": "Steerable but Not Decodable: Function Vectors Operate Beyond the Logit Lens",
            "url": "https://arxiv.org/pdf/2604.02608"
          }
        ]
      },
      "I found highly relevant research on these topics. Here are the key papers:\n\n## Primary Result: \"Decodable but Not Corrected\" Paper\n\nThe most directly relevant paper investigates the classification-correction gap via Overthinking (OT)—a behavioral regime in medical QA where models answer correctly under resampling yet fail in extended chain-of-thought. OT is linearly decodable at 71.6% balanced accuracy, yet five families of fixed linear steering (29 configurations) all yield negligible correction, with identical null results cross-architecture and cross-domain.\n\nThree convergent lines of evidence suggest representational entanglement: the OT direction has 85–88% overlap with task-critical computation. Importantly for your query, a learned non-linear residual MLP produces modest behavioral gain—consistent with partial but incomplete disentanglement of the shared subspace.\n\n## Related Finding: Inverse Gap\n\nInterestingly, there's a complementary dissociation: FV steering succeeds even when the logit lens cannot decode the correct answer at any layer, across 4,032 pairs across 12 tasks and 6 models. Even highly effective FVs project to incoherent token distributions, suggesting FVs encode computational instructions that the model's nonlinear processing executes through pathways invisible to the unembedding.\n\nThese papers from 2025-2026 directly address the phenomena you're searching for."
    ],
    "durationSeconds": 12.701442444999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a8d8ec1f-9c65-4cfa-ba1a-b58c21357141",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-19T13:01:33.695Z_

Let me also check for additional related work on learned non-linear steering methods and instance-adaptive steering:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b79ee93a-8c50-4cb7-9f92-c32a658b3732",
  "isSidechain": false,
  "requestId": "req_011CbByH3LPRtQDgVu9sbEe2",
  "type": "assistant",
  "uuid": "fa69777b-96a6-4046-b768-bd08d744c0ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FaRZ9hhNUWGHb24SQ8MrBa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 791,
      "cache_read_input_tokens": 28793,
      "output_tokens": 101,
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
          "output_tokens": 101,
          "cache_read_input_tokens": 28793,
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

### Tool call

_source line 41 · 2026-05-19T13:01:34.352Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VpXn4WD9pyW1ZWg8wuab6L`</summary>

```json
{
  "query": "K-CAST DAS ReFT instance-adaptive activation steering learned nonlinear intervention LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa69777b-96a6-4046-b768-bd08d744c0ac",
  "isSidechain": false,
  "requestId": "req_011CbByH3LPRtQDgVu9sbEe2",
  "type": "assistant",
  "uuid": "18cc98ed-941c-4784-a692-14d324acb997",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FaRZ9hhNUWGHb24SQ8MrBa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 791,
      "cache_read_input_tokens": 28793,
      "output_tokens": 101,
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
          "output_tokens": 101,
          "cache_read_input_tokens": 28793,
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

_source line 42 · 2026-05-19T13:01:40.548Z_

<details><summary>↩ Tool result · `toolu_01VpXn4WD9pyW1ZWg8wuab6L`</summary>

```text
Web search results for query: "K-CAST DAS ReFT instance-adaptive activation steering learned nonlinear intervention LLM 2025 2026"

Links: [{"title":"Contrastive Activation Steering","url":"https://www.emergentmind.com/topics/contrastive-activation-steering"},{"title":"Activation Steering in LLMs","url":"https://www.emergentmind.com/topics/activation-steering-method"},{"title":"Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs","url":"https://arxiv.org/pdf/2505.20309"},{"title":"Steering smarter. Why K-Steering is reshaping LLM… | by Thoughtworks | Medium","url":"https://thoughtworks.medium.com/steering-smarter-4fbfbdb58803"},{"title":"Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method for Diverse Hallucinations Categories","url":"https://arxiv.org/html/2406.00034v1"},{"title":"Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement   Method for Diverse Hallucinations Categories","url":"https://arxiv.org/pdf/2406.00034"}]

Based on the search results, I found relevant information about K-CAST and related activation steering methods for LLMs:

K-CAST (Conditional/kNN-based conditional steering) provides per-instance fine-grained control, improving formal reasoning performance by up to 15% and reducing content confounds in LLM deductive tasks.

The search results also show that K-CAST is part of a broader landscape of instance-adaptive activation steering approaches for LLMs. Conditional Activation Steering (CAST) leverages distinct activation patterns elicited by different prompt categories to apply steering conditionally, enforcing rules such as refusing harmful requests while answering normal prompts.

Additionally, there are related methods like Flexible Activation Steering with Backtracking (FASB), which determines the necessity and strength of intervention on-the-fly based on classifiers probing activation states, incorporating a backtracking mechanism to correct previously deviated token predictions.

These techniques represent recent advances (2025-2026) in using learned nonlinear interventions to steer LLM behavior through activation steering, allowing for fine-grained, instance-adaptive control over model outputs without retraining.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18cc98ed-941c-4784-a692-14d324acb997",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "db4d9c49-bd13-47bb-b83e-a026584e5fe3",
  "toolUseResult": {
    "query": "K-CAST DAS ReFT instance-adaptive activation steering learned nonlinear intervention LLM 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NUgVaWUeVtR5jWdQ9cpRtz",
        "content": [
          {
            "title": "Contrastive Activation Steering",
            "url": "https://www.emergentmind.com/topics/contrastive-activation-steering"
          },
          {
            "title": "Activation Steering in LLMs",
            "url": "https://www.emergentmind.com/topics/activation-steering-method"
          },
          {
            "title": "Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs",
            "url": "https://arxiv.org/pdf/2505.20309"
          },
          {
            "title": "Steering smarter. Why K-Steering is reshaping LLM… | by Thoughtworks | Medium",
            "url": "https://thoughtworks.medium.com/steering-smarter-4fbfbdb58803"
          },
          {
            "title": "Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method for Diverse Hallucinations Categories",
            "url": "https://arxiv.org/html/2406.00034v1"
          },
          {
            "title": "Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement   Method for Diverse Hallucinations Categories",
            "url": "https://arxiv.org/pdf/2406.00034"
          }
        ]
      },
      "Based on the search results, I found relevant information about K-CAST and related activation steering methods for LLMs:\n\nK-CAST (Conditional/kNN-based conditional steering) provides per-instance fine-grained control, improving formal reasoning performance by up to 15% and reducing content confounds in LLM deductive tasks.\n\nThe search results also show that K-CAST is part of a broader landscape of instance-adaptive activation steering approaches for LLMs. Conditional Activation Steering (CAST) leverages distinct activation patterns elicited by different prompt categories to apply steering conditionally, enforcing rules such as refusing harmful requests while answering normal prompts.\n\nAdditionally, there are related methods like Flexible Activation Steering with Backtracking (FASB), which determines the necessity and strength of intervention on-the-fly based on classifiers probing activation states, incorporating a backtracking mechanism to correct previously deviated token predictions.\n\nThese techniques represent recent advances (2025-2026) in using learned nonlinear interventions to steer LLM behavior through activation steering, allowing for fine-grained, instance-adaptive control over model outputs without retraining."
    ],
    "durationSeconds": 6.190939870000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "18cc98ed-941c-4784-a692-14d324acb997",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T13:01:45.982Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KmSLRKuWpyBEHsUbZK7QaN`</summary>

```json
{
  "query": "learned nonlinear residual adapter steering correction bottleneck MLP activation intervention calibration LLM arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db4d9c49-bd13-47bb-b83e-a026584e5fe3",
  "isSidechain": false,
  "requestId": "req_011CbByHm2tja29UjuGVbumb",
  "type": "assistant",
  "uuid": "22f491b3-6183-4a2e-baeb-8fd6ceaaade0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UzVFBYqDKSU7JkWFaPJrAp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 698,
      "cache_read_input_tokens": 29584,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 698,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 29584,
          "cache_creation_input_tokens": 698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 698
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

_source line 44 · 2026-05-19T13:01:52.269Z_

<details><summary>↩ Tool result · `toolu_01KmSLRKuWpyBEHsUbZK7QaN`</summary>

```text
Web search results for query: "learned nonlinear residual adapter steering correction bottleneck MLP activation intervention calibration LLM arXiv 2026"

Links: [{"title":"Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes","url":"https://arxiv.org/html/2605.05715"},{"title":"Contextual Linear Activation Steering of Language Models","url":"https://arxiv.org/html/2604.24693"},{"title":"Steered LLM Activations are Non-Surjective","url":"https://arxiv.org/html/2604.09839v1"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/pdf/2602.06022"},{"title":"The Rogue Scalpel: Activation Steering Compromises LLM Safety","url":"https://arxiv.org/html/2509.22067v2"}]

Based on the search results, I found several relevant papers from 2026 that discuss related concepts:

The most directly relevant result is a paper discussing a learned non-linear residual MLP that reduces centroid distance by 50.6% yet produces only modest behavioral gain, consistent with partial but incomplete disentanglement of the shared subspace. This suggests that non-linear transforms can partially navigate around task-critical directions that linear perturbations inevitably disrupt.

Additionally, CORAL (Correctness-Optimized Residual Activation Lens) is a regularized inference-time steering method that captures distributed correctness signals from model internal activations using weight-decay MLP probes, and it consistently improves accuracy by 10% and expected calibration error (ECE) by 50% on average, with gains transferring to held-out benchmarks.

These papers explore advanced techniques for activation steering and intervention in large language models, including the use of learned nonlinear adapters and calibration-aware approaches, which aligns with the topics in your search query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22f491b3-6183-4a2e-baeb-8fd6ceaaade0",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "1df52b26-a79c-4660-ab60-cbef38b93c72",
  "toolUseResult": {
    "query": "learned nonlinear residual adapter steering correction bottleneck MLP activation intervention calibration LLM arXiv 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DVbVZm4eg79rwqN2zgeNkg",
        "content": [
          {
            "title": "Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes",
            "url": "https://arxiv.org/html/2605.05715"
          },
          {
            "title": "Contextual Linear Activation Steering of Language Models",
            "url": "https://arxiv.org/html/2604.24693"
          },
          {
            "title": "Steered LLM Activations are Non-Surjective",
            "url": "https://arxiv.org/html/2604.09839v1"
          },
          {
            "title": "Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "https://arxiv.org/pdf/2602.06022"
          },
          {
            "title": "The Rogue Scalpel: Activation Steering Compromises LLM Safety",
            "url": "https://arxiv.org/html/2509.22067v2"
          }
        ]
      },
      "Based on the search results, I found several relevant papers from 2026 that discuss related concepts:\n\nThe most directly relevant result is a paper discussing a learned non-linear residual MLP that reduces centroid distance by 50.6% yet produces only modest behavioral gain, consistent with partial but incomplete disentanglement of the shared subspace. This suggests that non-linear transforms can partially navigate around task-critical directions that linear perturbations inevitably disrupt.\n\nAdditionally, CORAL (Correctness-Optimized Residual Activation Lens) is a regularized inference-time steering method that captures distributed correctness signals from model internal activations using weight-decay MLP probes, and it consistently improves accuracy by 10% and expected calibration error (ECE) by 50% on average, with gains transferring to held-out benchmarks.\n\nThese papers explore advanced techniques for activation steering and intervention in large language models, including the use of learned nonlinear adapters and calibration-aware approaches, which aligns with the topics in your search query."
    ],
    "durationSeconds": 6.282334591999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "22f491b3-6183-4a2e-baeb-8fd6ceaaade0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T13:01:54.984Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VFSK98MNRaPTNZVaiW8rd1`</summary>

```json
{
  "query": "Contextual Linear Activation Steering arXiv 2604.24693 instance-adaptive steering 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1df52b26-a79c-4660-ab60-cbef38b93c72",
  "isSidechain": false,
  "requestId": "req_011CbByJd7RBibdynttonAxj",
  "type": "assistant",
  "uuid": "795c2e78-9288-4ab0-af61-85374bbc5c7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HMyru2942xeU5jgqLZZTUP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 30282,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 602,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 30282,
          "cache_creation_input_tokens": 602,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 602
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

_source line 46 · 2026-05-19T13:02:00.722Z_

<details><summary>↩ Tool result · `toolu_01VFSK98MNRaPTNZVaiW8rd1`</summary>

```text
Web search results for query: "Contextual Linear Activation Steering arXiv 2604.24693 instance-adaptive steering 2026"

Links: [{"title":"Contextual Linear Activation Steering of Language Models","url":"https://arxiv.org/html/2604.24693"},{"title":"[2604.24693] Contextual Linear Activation Steering of Language Models","url":"https://arxiv.org/abs/2604.24693"},{"title":"GitHub - bhdsc/CLAS: Official implementation of Contextual Linear Activation Steering of Language Models (CLAS) · GitHub","url":"https://github.com/bhdsc/CLAS"},{"title":"COLD-Steer: Steering Large Language Models via In-Context One-step Learning Dynamics","url":"https://arxiv.org/pdf/2603.06495"},{"title":"LinEAS: End-to-end Learning of Activation Steering with a Distributional Loss","url":"https://arxiv.org/pdf/2503.10679"},{"title":"Improving Activation Steering in Language Models with Mean-Centring","url":"https://arxiv.org/pdf/2312.03813"},{"title":"Activation Steering for Aligned Open-ended Generation without Sacrificing Coherence","url":"https://arxiv.org/html/2604.08169v1"},{"title":"Steering Language Models With Activation Engineering","url":"https://arxiv.org/pdf/2308.10248"},{"title":"Activation Steering for Aligned Open-ended Generation without Sacrificing Coherence","url":"https://arxiv.org/pdf/2604.08169"}]

Based on the search results, I found detailed information about the paper you're interested in:

Contextual Linear Activation Steering (CLAS) is a method that dynamically adapts linear activation steering to context-dependent steering strengths. The paper was submitted to arXiv on April 27, 2026 by Brandon Hsu, Daniel Beaglehole, Adityanarayanan Radhakrishnan, and Mikhail Belkin from UC San Diego, MIT, and the Broad Institute of MIT and Harvard.

The key problem CLAS addresses is that existing linear activation steering methods often apply a fixed steering strength to all tokens, resulting in inconsistent steering quality across diverse input prompts. Across eleven steering benchmarks and four model families, CLAS consistently outperforms standard linear activation steering and matches or exceeds the performance of ReFT and LoRA in settings with limited labeled data.

The official implementation of CLAS is available on GitHub at https://github.com/bhdsc/CLAS, and the full paper can be accessed at https://arxiv.org/abs/2604.24693.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "795c2e78-9288-4ab0-af61-85374bbc5c7d",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "f9b8ff3a-7cba-42cc-be49-a519e7a579d6",
  "toolUseResult": {
    "query": "Contextual Linear Activation Steering arXiv 2604.24693 instance-adaptive steering 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VDPDmfRZrdjGzhe8S5TxfM",
        "content": [
          {
            "title": "Contextual Linear Activation Steering of Language Models",
            "url": "https://arxiv.org/html/2604.24693"
          },
          {
            "title": "[2604.24693] Contextual Linear Activation Steering of Language Models",
            "url": "https://arxiv.org/abs/2604.24693"
          },
          {
            "title": "GitHub - bhdsc/CLAS: Official implementation of Contextual Linear Activation Steering of Language Models (CLAS) · GitHub",
            "url": "https://github.com/bhdsc/CLAS"
          },
          {
            "title": "COLD-Steer: Steering Large Language Models via In-Context One-step Learning Dynamics",
            "url": "https://arxiv.org/pdf/2603.06495"
          },
          {
            "title": "LinEAS: End-to-end Learning of Activation Steering with a Distributional Loss",
            "url": "https://arxiv.org/pdf/2503.10679"
          },
          {
            "title": "Improving Activation Steering in Language Models with Mean-Centring",
            "url": "https://arxiv.org/pdf/2312.03813"
          },
          {
            "title": "Activation Steering for Aligned Open-ended Generation without Sacrificing Coherence",
            "url": "https://arxiv.org/html/2604.08169v1"
          },
          {
            "title": "Steering Language Models With Activation Engineering",
            "url": "https://arxiv.org/pdf/2308.10248"
          },
          {
            "title": "Activation Steering for Aligned Open-ended Generation without Sacrificing Coherence",
            "url": "https://arxiv.org/pdf/2604.08169"
          }
        ]
      },
      "Based on the search results, I found detailed information about the paper you're interested in:\n\nContextual Linear Activation Steering (CLAS) is a method that dynamically adapts linear activation steering to context-dependent steering strengths. The paper was submitted to arXiv on April 27, 2026 by Brandon Hsu, Daniel Beaglehole, Adityanarayanan Radhakrishnan, and Mikhail Belkin from UC San Diego, MIT, and the Broad Institute of MIT and Harvard.\n\nThe key problem CLAS addresses is that existing linear activation steering methods often apply a fixed steering strength to all tokens, resulting in inconsistent steering quality across diverse input prompts. Across eleven steering benchmarks and four model families, CLAS consistently outperforms standard linear activation steering and matches or exceeds the performance of ReFT and LoRA in settings with limited labeled data.\n\nThe official implementation of CLAS is available on GitHub at https://github.com/bhdsc/CLAS, and the full paper can be accessed at https://arxiv.org/abs/2604.24693."
    ],
    "durationSeconds": 5.733212879999977,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "795c2e78-9288-4ab0-af61-85374bbc5c7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"Disentangling Competing Calibration Biases via Geometry-Aware Activati…",
  "leafUuid": "f9b8ff3a-7cba-42cc-be49-a519e7a579d6",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise calibration bias steering with steerability diagnostics",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340"
}
```

---

### Tool call

_source line 49 · 2026-05-19T13:02:03.590Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F9EFjrtQfDkymhBAtNCmAM`</summary>

```json
{
  "query": "\"Fine-Grained Activation Steering\" arXiv 2602.04428 \"steering less achieving more\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9b8ff3a-7cba-42cc-be49-a519e7a579d6",
  "isSidechain": false,
  "requestId": "req_011CbByKFFJYCy85u7mdsK3M",
  "type": "assistant",
  "uuid": "05ced130-0a67-44d4-b532-e0bfd2414e51",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JU1Q6jpHSt2RqfxwcHbDmi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 749,
      "cache_read_input_tokens": 30884,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 749,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 30884,
          "cache_creation_input_tokens": 749,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 749
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

_source line 50 · 2026-05-19T13:02:09.362Z_

<details><summary>↩ Tool result · `toolu_01F9EFjrtQfDkymhBAtNCmAM`</summary>

```text
Web search results for query: ""Fine-Grained Activation Steering" arXiv 2602.04428 "steering less achieving more" 2026"

Links: [{"title":"[2602.04428] Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/abs/2602.04428"},{"title":"Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/pdf/2602.04428"},{"title":"Fine-Grained Activation Steering: Steering Less, Achieving More | OpenReview","url":"https://openreview.net/forum?id=guSVafqhrB"},{"title":"Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/html/2602.04428"},{"title":"FINE-GRAINED ACTIVATION STEERING","url":"https://openreview.net/pdf/a9cada056ebe41df04f02a22bc25b2fe3d125857.pdf"}]

I found the paper! Here are the results for your search:

The paper "Fine-Grained Activation Steering: Steering Less, Achieving More" (arXiv 2602.04428) discusses activation steering as a cost-effective paradigm for modifying large language model behaviors, noting that existing methods typically intervene at the block level, steering bundled activations of selected attention heads, feedforward networks, or residual streams.

The authors reveal that block-level activations are inherently heterogeneous, entangling beneficial, irrelevant, and harmful features, rendering block-level steering coarse, inefficient, and intrusive. They decompose block activations into fine-grained atomic unit (AU)-level activations, where each AU-level activation corresponds to a single dimension of the block activation.

The paper proposes AUSteer, a method that operates at the AU level, first identifying discriminative AUs globally by computing activation momenta on contrastive samples, then assigning adaptive steering strengths tailored to diverse inputs and selected AU activations. Comprehensive experiments show that AUSteer consistently surpasses advanced baselines while steering considerably fewer activations.

The paper was submitted on February 4, 2026, and demonstrates that more precise, fine-grained steering can achieve better results with fewer interventions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05ced130-0a67-44d4-b532-e0bfd2414e51",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "883b17f1-6801-49eb-92c8-d0978f3a1add",
  "toolUseResult": {
    "query": "\"Fine-Grained Activation Steering\" arXiv 2602.04428 \"steering less achieving more\" 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ARU7ZZNFCBSA7iPfM52DPR",
        "content": [
          {
            "title": "[2602.04428] Fine-Grained Activation Steering: Steering Less, Achieving More",
            "url": "https://arxiv.org/abs/2602.04428"
          },
          {
            "title": "Fine-Grained Activation Steering: Steering Less, Achieving More",
            "url": "https://arxiv.org/pdf/2602.04428"
          },
          {
            "title": "Fine-Grained Activation Steering: Steering Less, Achieving More | OpenReview",
            "url": "https://openreview.net/forum?id=guSVafqhrB"
          },
          {
            "title": "Fine-Grained Activation Steering: Steering Less, Achieving More",
            "url": "https://arxiv.org/html/2602.04428"
          },
          {
            "title": "FINE-GRAINED ACTIVATION STEERING",
            "url": "https://openreview.net/pdf/a9cada056ebe41df04f02a22bc25b2fe3d125857.pdf"
          }
        ]
      },
      "I found the paper! Here are the results for your search:\n\nThe paper \"Fine-Grained Activation Steering: Steering Less, Achieving More\" (arXiv 2602.04428) discusses activation steering as a cost-effective paradigm for modifying large language model behaviors, noting that existing methods typically intervene at the block level, steering bundled activations of selected attention heads, feedforward networks, or residual streams.\n\nThe authors reveal that block-level activations are inherently heterogeneous, entangling beneficial, irrelevant, and harmful features, rendering block-level steering coarse, inefficient, and intrusive. They decompose block activations into fine-grained atomic unit (AU)-level activations, where each AU-level activation corresponds to a single dimension of the block activation.\n\nThe paper proposes AUSteer, a method that operates at the AU level, first identifying discriminative AUs globally by computing activation momenta on contrastive samples, then assigning adaptive steering strengths tailored to diverse inputs and selected AU activations. Comprehensive experiments show that AUSteer consistently surpasses advanced baselines while steering considerably fewer activations.\n\nThe paper was submitted on February 4, 2026, and demonstrates that more precise, fine-grained steering can achieve better results with fewer interventions."
    ],
    "durationSeconds": 5.768464938999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "05ced130-0a67-44d4-b532-e0bfd2414e51",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 51 · 2026-05-19T13:02:09.369Z_

```json
{
  "parentUuid": "883b17f1-6801-49eb-92c8-d0978f3a1add",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "489b8ebd-6326-4f4d-b032-0352deb4583e",
  "timestamp": "2026-05-19T13:02:09.369Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 52 · 2026-05-19T13:02:12.785Z_

Now let me search for the Spherical Steering paper to ensure I have the latest details and understand how it compares to Selective Steering and COAST:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "489b8ebd-6326-4f4d-b032-0352deb4583e",
  "isSidechain": false,
  "requestId": "req_011CbByKtEXrcZRLk7nVN7P8",
  "type": "assistant",
  "uuid": "12cb18bd-0959-44c5-bf46-c05831c2f1fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LNHkq1pdvw4QjqV5SPrg12",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 763,
      "cache_read_input_tokens": 31633,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 763,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 118,
          "cache_read_input_tokens": 31633,
          "cache_creation_input_tokens": 763,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 763
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

_source line 53 · 2026-05-19T13:02:13.327Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017iDnSi2kXEt3Xr6rHmAEQT`</summary>

```json
{
  "query": "Spherical Steering ICML 2026 arXiv 2602.08169 geodesic rotation norm-preserving activation steering"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12cb18bd-0959-44c5-bf46-c05831c2f1fc",
  "isSidechain": false,
  "requestId": "req_011CbByKtEXrcZRLk7nVN7P8",
  "type": "assistant",
  "uuid": "359ffd4e-164d-4015-9195-fd69ddb6c23e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LNHkq1pdvw4QjqV5SPrg12",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 763,
      "cache_read_input_tokens": 31633,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 763,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 118,
          "cache_read_input_tokens": 31633,
          "cache_creation_input_tokens": 763,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 763
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

_source line 54 · 2026-05-19T13:02:20.191Z_

<details><summary>↩ Tool result · `toolu_017iDnSi2kXEt3Xr6rHmAEQT`</summary>

```text
Web search results for query: "Spherical Steering ICML 2026 arXiv 2602.08169 geodesic rotation norm-preserving activation steering"

Links: [{"title":"GitHub - chili-lab/Spherical-Steering: [ICML 2026] Spherical Steering: Geometry-Aware Activation Rotation for Language Models · GitHub","url":"https://github.com/chili-lab/Spherical-Steering"},{"title":"[2602.08169] Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/abs/2602.08169"},{"title":"Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/pdf/2602.08169"},{"title":"(PDF) Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://www.researchgate.net/publication/400605038_Spherical_Steering_Geometry-Aware_Activation_Rotation_for_Language_Models"},{"title":"Spherical Steering is highly complementary to few-shot prompting.... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Spherical-Steering-is-highly-complementary-to-few-shot-prompting-Performance-on_fig3_400605038"},{"title":"On the Non-Identifiability of Steering Vectors in Large Language Models","url":"https://arxiv.org/html/2602.06801v4"},{"title":"Radio controlled vehicle within a sphere","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4541814"},{"title":"Vehicle with spherical-shaped wheels for steering and speed control purposes","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4785899"}]

Based on the search results, I found information about your query:

The paper titled "Spherical Steering: Geometry-Aware Activation Rotation for Language Models" (arXiv:2602.08169) was submitted on February 9, 2026 by authors Zejia You, Chunyuan Deng, and Hanjie Chen.

The paper addresses inference-time steering as a promising paradigm for controlling language models without retraining. Standard approaches typically rely on activation addition, which inevitably alters the magnitude of hidden representations.

Spherical Steering is a training-free method that resolves this trade-off through activation rotation, where activations are rotated along a geodesic toward a target direction, guiding the activation toward the target concept while preserving the integrity of representations.

Unlike additive baselines, Spherical Steering delivers norm-preserving rotation that operates orthogonally to prompt-based adaptation.

You can access the full paper on arXiv at: https://arxiv.org/abs/2602.08169


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "359ffd4e-164d-4015-9195-fd69ddb6c23e",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "a5bd975b-0833-4cbb-9218-5fd2805a5c82",
  "toolUseResult": {
    "query": "Spherical Steering ICML 2026 arXiv 2602.08169 geodesic rotation norm-preserving activation steering",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VqUYhMmU48dviof9AHkUEk",
        "content": [
          {
            "title": "GitHub - chili-lab/Spherical-Steering: [ICML 2026] Spherical Steering: Geometry-Aware Activation Rotation for Language Models · GitHub",
            "url": "https://github.com/chili-lab/Spherical-Steering"
          },
          {
            "title": "[2602.08169] Spherical Steering: Geometry-Aware Activation Rotation for Language Models",
            "url": "https://arxiv.org/abs/2602.08169"
          },
          {
            "title": "Spherical Steering: Geometry-Aware Activation Rotation for Language Models",
            "url": "https://arxiv.org/pdf/2602.08169"
          },
          {
            "title": "(PDF) Spherical Steering: Geometry-Aware Activation Rotation for Language Models",
            "url": "https://www.researchgate.net/publication/400605038_Spherical_Steering_Geometry-Aware_Activation_Rotation_for_Language_Models"
          },
          {
            "title": "Spherical Steering is highly complementary to few-shot prompting.... | Download Scientific Diagram",
            "url": "https://www.researchgate.net/figure/Spherical-Steering-is-highly-complementary-to-few-shot-prompting-Performance-on_fig3_400605038"
          },
          {
            "title": "On the Non-Identifiability of Steering Vectors in Large Language Models",
            "url": "https://arxiv.org/html/2602.06801v4"
          },
          {
            "title": "Radio controlled vehicle within a sphere",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4541814"
          },
          {
            "title": "Vehicle with spherical-shaped wheels for steering and speed control purposes",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4785899"
          }
        ]
      },
      "Based on the search results, I found information about your query:\n\nThe paper titled \"Spherical Steering: Geometry-Aware Activation Rotation for Language Models\" (arXiv:2602.08169) was submitted on February 9, 2026 by authors Zejia You, Chunyuan Deng, and Hanjie Chen.\n\nThe paper addresses inference-time steering as a promising paradigm for controlling language models without retraining. Standard approaches typically rely on activation addition, which inevitably alters the magnitude of hidden representations.\n\nSpherical Steering is a training-free method that resolves this trade-off through activation rotation, where activations are rotated along a geodesic toward a target direction, guiding the activation toward the target concept while preserving the integrity of representations.\n\nUnlike additive baselines, Spherical Steering delivers norm-preserving rotation that operates orthogonally to prompt-based adaptation.\n\nYou can access the full paper on arXiv at: https://arxiv.org/abs/2602.08169"
    ],
    "durationSeconds": 6.859423454999982,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "359ffd4e-164d-4015-9195-fd69ddb6c23e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-19T13:02:23.724Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VRabC6qW5eYUraaPLRBiNK`</summary>

```json
{
  "query": "activation steering collateral damage entanglement task-critical features specificity calibration confidence LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5bd975b-0833-4cbb-9218-5fd2805a5c82",
  "isSidechain": false,
  "requestId": "req_011CbByLgUdQzYmkr8s1SMpC",
  "type": "assistant",
  "uuid": "dedb8c71-bfd0-4656-843d-5efb95d650bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SA9eBTXXNKi86rMoEf2v5o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 848,
      "cache_read_input_tokens": 32396,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 848,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 32396,
          "cache_creation_input_tokens": 848,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 848
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

_source line 56 · 2026-05-19T13:02:31.405Z_

<details><summary>↩ Tool result · `toolu_01VRabC6qW5eYUraaPLRBiNK`</summary>

```text
Web search results for query: "activation steering collateral damage entanglement task-critical features specificity calibration confidence LLM 2025 2026"

Links: [{"title":"Minimizing Collateral Damage in Activation Steering","url":"https://arxiv.org/html/2605.01167"},{"title":"[2605.01167] Minimizing Collateral Damage in Activation Steering","url":"https://arxiv.org/abs/2605.01167"},{"title":"Activation Steering in LLMs","url":"https://www.emergentmind.com/topics/activation-steering-method"},{"title":"Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"},{"title":"Identifying and Transferring Reasoning-Critical Neurons: Improving LLM Inference Reliability via Activation Steering","url":"https://arxiv.org/pdf/2601.19847"},{"title":"Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/pdf/2602.04428"},{"title":"The Rogue Scalpel: Activation Steering Compromises LLM Safety","url":"https://arxiv.org/html/2509.22067v2"}]

I found several relevant research papers and resources on activation steering in LLMs from 2025-2026. Here are the key findings:

## Core Research on Collateral Damage

Activation steering is a method for controlling LLM behavior by intervening in internal representations, though standard interventions like vector addition often cause "collateral damage"—unintended changes in alignment along other non-target feature directions. This steering/performance trade-off arises because steering the model to exhibit one feature can alter the alignment of activations with other features.

## Understanding Feature Entanglement

The geometry of LLM representations is anisotropic, with features being non-uniform such that some directions are more coupled to others, and when features are entangled with the steering direction, ignoring this geometry can unintentionally disturb them. Multi-property steering via simultaneous injection of separate steering vectors at distinct layers enables robust control over several behaviors without detrimental interference, unlike direct vector composition, which often fails due to feature entanglement.

## Mathematical Framework and Solutions

A principled framework models steering as a constrained optimization problem, finding a new activation that minimizes the expected squared collateral change weighted by the empirical second-moment matrix of activations.

## Recent Methodological Advances (2025-2026)

Flexible Activation Steering with Backtracking (FASB) determines the necessity and strength of intervention on-the-fly based on classifiers probing activation states, incorporating a backtracking mechanism to correct previously deviated token predictions. Fine-grained activation steering addresses the limitation of block-level intervention by accounting for heterogeneity within block activations, which often span hundreds or thousands of dimensions, each indicating a different feature.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dedb8c71-bfd0-4656-843d-5efb95d650bb",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "04942e58-d501-43e7-889c-95a0e5c2e041",
  "toolUseResult": {
    "query": "activation steering collateral damage entanglement task-critical features specificity calibration confidence LLM 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01P9S3cvmTSajSzGJvocYFfm",
        "content": [
          {
            "title": "Minimizing Collateral Damage in Activation Steering",
            "url": "https://arxiv.org/html/2605.01167"
          },
          {
            "title": "[2605.01167] Minimizing Collateral Damage in Activation Steering",
            "url": "https://arxiv.org/abs/2605.01167"
          },
          {
            "title": "Activation Steering in LLMs",
            "url": "https://www.emergentmind.com/topics/activation-steering-method"
          },
          {
            "title": "Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra",
            "url": "https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"
          },
          {
            "title": "Identifying and Transferring Reasoning-Critical Neurons: Improving LLM Inference Reliability via Activation Steering",
            "url": "https://arxiv.org/pdf/2601.19847"
          },
          {
            "title": "Fine-Grained Activation Steering: Steering Less, Achieving More",
            "url": "https://arxiv.org/pdf/2602.04428"
          },
          {
            "title": "The Rogue Scalpel: Activation Steering Compromises LLM Safety",
            "url": "https://arxiv.org/html/2509.22067v2"
          }
        ]
      },
      "I found several relevant research papers and resources on activation steering in LLMs from 2025-2026. Here are the key findings:\n\n## Core Research on Collateral Damage\n\nActivation steering is a method for controlling LLM behavior by intervening in internal representations, though standard interventions like vector addition often cause \"collateral damage\"—unintended changes in alignment along other non-target feature directions. This steering/performance trade-off arises because steering the model to exhibit one feature can alter the alignment of activations with other features.\n\n## Understanding Feature Entanglement\n\nThe geometry of LLM representations is anisotropic, with features being non-uniform such that some directions are more coupled to others, and when features are entangled with the steering direction, ignoring this geometry can unintentionally disturb them. Multi-property steering via simultaneous injection of separate steering vectors at distinct layers enables robust control over several behaviors without detrimental interference, unlike direct vector composition, which often fails due to feature entanglement.\n\n## Mathematical Framework and Solutions\n\nA principled framework models steering as a constrained optimization problem, finding a new activation that minimizes the expected squared collateral change weighted by the empirical second-moment matrix of activations.\n\n## Recent Methodological Advances (2025-2026)\n\nFlexible Activation Steering with Backtracking (FASB) determines the necessity and strength of intervention on-the-fly based on classifiers probing activation states, incorporating a backtracking mechanism to correct previously deviated token predictions. Fine-grained activation steering addresses the limitation of block-level intervention by accounting for heterogeneity within block activations, which often span hundreds or thousands of dimensions, each indicating a different feature."
    ],
    "durationSeconds": 7.677135355999984,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "dedb8c71-bfd0-4656-843d-5efb95d650bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-19T13:02:36.245Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DL66bHzCiYGBQgAcsdZakN`</summary>

```json
{
  "url": "https://subhadipmitra.com/blog/2026/activation-steering-field-guide/",
  "prompt": "Extract all key papers and methods mentioned in this field guide. Especially focus on: (1) any discussion of the classification-correction gap or decodable-but-not-steerable phenomenon, (2) norm-preserving methods (Spherical Steering, Selective Steering, COAST), (3) collateral damage minimization approaches, (4) nonlinear steering methods, (5) instance-adaptive methods. List all paper citations with arXiv IDs where available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04942e58-d501-43e7-889c-95a0e5c2e041",
  "isSidechain": false,
  "requestId": "req_011CbByMWV92xrJ1pAfbhipL",
  "type": "assistant",
  "uuid": "83665067-41cc-4199-ba4a-7472b5bde880",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D9AoajSNFxxzVeKtK4siQB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 816,
      "cache_read_input_tokens": 33244,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 816,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 33244,
          "cache_creation_input_tokens": 816,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 816
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-19T13:02:46.812Z_

<details><summary>↩ Tool result · `toolu_01DL66bHzCiYGBQgAcsdZakN`</summary>

```text
# Key Papers and Methods in Activation Steering (2026)

## Papers Explicitly Cited

Based on the guide's references section, here are the primary papers mentioned:

**Core Steering Theory:**
- Turner et al. (2024). "Activation Addition: Steering Language Models Without Optimization" [arXiv:2308.10248]
- Tan et al. (2024). "Analysing the Generalisation and Reliability of Steering Vectors" - NeurIPS 2024 [arXiv:2407.12404]
- Taimeskhanov et al. (2026). "Towards Understanding Steering Strength" [arXiv:2602.02712]

**Advanced Steering Methods:**
- Li et al. (2026). "Steering Vector Fields for Context-Aware Inference-Time Control in LLMs" [arXiv:2602.01654]
- Fang et al. (2026). "Controllable LLM Reasoning via Sparse Autoencoder-Based Steering" [arXiv:2601.03595]
- Cho et al. (2026). "Control Reinforcement Learning: Interpretable Token-Level Steering via SAE Features" [arXiv:2602.10437]
- YaPO (2026). "Learnable Sparse Activation Steering Vectors for Domain Adaptation" [arXiv:2601.08441]
- AUSteer (2026). "Fine-Grained Activation Steering" [arXiv:2602.04428]

**Safety & Robustness:**
- Goyal & Daumé (2026). "Steering Safely or Off a Cliff? Rethinking Specificity and Robustness" [arXiv:2602.06256]
- Venkatesh & Kurapath (2026). "On the Identifiability of Steering Vectors" [arXiv:2602.06801]

**Unified Theory:**
- (2026). "Why Steering Works: Toward a Unified View" [arXiv:2602.02343]

**Additional Methods:**
- Postmus et al. (2024). "From Steering Vectors to Conceptors: Compositional Affine Activation Steering"
- Weij et al. (2024). "Multi-property steering via simultaneous injection"
- Nguyen et al. (2025). "PID-based Activation Steering for LLMs"
- ARGUS system [arXiv:2501.09661]

## Notable Gaps

**Not Found in This Guide:**
- No explicit discussion of the "classification-correction gap" or "decodable-but-not-steerable phenomenon"
- No mention of norm-preserving methods (Spherical Steering, Selective Steering, COAST)
- No dedicated section on collateral damage minimization
- Nonlinear steering methods not detailed
- Instance-adaptive steering approaches mentioned tangentially but not systematically covered

The guide focuses primarily on linear activation vectors and empirical practice rather than theoretical foundations of these advanced methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83665067-41cc-4199-ba4a-7472b5bde880",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "a79e4456-84b5-4202-8d04-ed7f74f2cd10",
  "toolUseResult": {
    "bytes": 80503,
    "code": 200,
    "codeText": "OK",
    "result": "# Key Papers and Methods in Activation Steering (2026)\n\n## Papers Explicitly Cited\n\nBased on the guide's references section, here are the primary papers mentioned:\n\n**Core Steering Theory:**\n- Turner et al. (2024). \"Activation Addition: Steering Language Models Without Optimization\" [arXiv:2308.10248]\n- Tan et al. (2024). \"Analysing the Generalisation and Reliability of Steering Vectors\" - NeurIPS 2024 [arXiv:2407.12404]\n- Taimeskhanov et al. (2026). \"Towards Understanding Steering Strength\" [arXiv:2602.02712]\n\n**Advanced Steering Methods:**\n- Li et al. (2026). \"Steering Vector Fields for Context-Aware Inference-Time Control in LLMs\" [arXiv:2602.01654]\n- Fang et al. (2026). \"Controllable LLM Reasoning via Sparse Autoencoder-Based Steering\" [arXiv:2601.03595]\n- Cho et al. (2026). \"Control Reinforcement Learning: Interpretable Token-Level Steering via SAE Features\" [arXiv:2602.10437]\n- YaPO (2026). \"Learnable Sparse Activation Steering Vectors for Domain Adaptation\" [arXiv:2601.08441]\n- AUSteer (2026). \"Fine-Grained Activation Steering\" [arXiv:2602.04428]\n\n**Safety & Robustness:**\n- Goyal & Daumé (2026). \"Steering Safely or Off a Cliff? Rethinking Specificity and Robustness\" [arXiv:2602.06256]\n- Venkatesh & Kurapath (2026). \"On the Identifiability of Steering Vectors\" [arXiv:2602.06801]\n\n**Unified Theory:**\n- (2026). \"Why Steering Works: Toward a Unified View\" [arXiv:2602.02343]\n\n**Additional Methods:**\n- Postmus et al. (2024). \"From Steering Vectors to Conceptors: Compositional Affine Activation Steering\"\n- Weij et al. (2024). \"Multi-property steering via simultaneous injection\"\n- Nguyen et al. (2025). \"PID-based Activation Steering for LLMs\"\n- ARGUS system [arXiv:2501.09661]\n\n## Notable Gaps\n\n**Not Found in This Guide:**\n- No explicit discussion of the \"classification-correction gap\" or \"decodable-but-not-steerable phenomenon\"\n- No mention of norm-preserving methods (Spherical Steering, Selective Steering, COAST)\n- No dedicated section on collateral damage minimization\n- Nonlinear steering methods not detailed\n- Instance-adaptive steering approaches mentioned tangentially but not systematically covered\n\nThe guide focuses primarily on linear activation vectors and empirical practice rather than theoretical foundations of these advanced methods.",
    "durationMs": 10561,
    "url": "https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"
  },
  "sourceToolAssistantUUID": "83665067-41cc-4199-ba4a-7472b5bde880",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-19T13:02:49.887Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BQuFJNsRf6UhCXP8fMhP2c`</summary>

```json
{
  "query": "ReFT representation finetuning low-rank linear subspace intervention ICLR 2025 activation steering learned"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a79e4456-84b5-4202-8d04-ed7f74f2cd10",
  "isSidechain": false,
  "requestId": "req_011CbByNeMwTMjBGy9FGp2nS",
  "type": "assistant",
  "uuid": "87976600-3d56-4779-be9d-6d2a5fc2e3fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y84LEFhbj31CVQtVF1AiPk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1744,
      "cache_read_input_tokens": 33244,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1744,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 33244,
          "cache_creation_input_tokens": 1744,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1744
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-19T13:02:57.026Z_

<details><summary>↩ Tool result · `toolu_01BQuFJNsRf6UhCXP8fMhP2c`</summary>

```text
Web search results for query: "ReFT representation finetuning low-rank linear subspace intervention ICLR 2025 activation steering learned"

Links: [{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/dcf88cbc8d01ce7309b83d0ebaeb9d29-Paper-Conference.pdf"},{"title":"[Literature Review] ReFT: Representation Finetuning for Language Models","url":"https://www.themoonlight.io/en/review/reft-representation-finetuning-for-language-models"},{"title":"ReFT: Representation Finetuning for Language Models","url":"https://nlp.stanford.edu/~wuzhengx/reft/index.html"},{"title":"ReFT: Representation Finetuning for Language Models","url":"https://www.linkedin.com/pulse/reft-representation-finetuning-language-models-vlad-bogolin-ea9ce"},{"title":"ReFT: Representation Finetuning for Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/reft-representation-finetuning-language-models"},{"title":"[PDF] ReFT: Representation Finetuning for Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ReFT:-Representation-Finetuning-for-Language-Models-Wu-Arora/1bda8efbbf4abae6c8c1da97d6137396807b1e09"},{"title":"[2404.03592] ReFT: Representation Finetuning for Language Models","url":"https://arxiv.org/abs/2404.03592"},{"title":"ReFT: Representation Finetuning for Language Models Zhengxuan Wu∗†","url":"https://arxiv.org/pdf/2404.03592"},{"title":"ReFT: Representation Finetuning for Language Models","url":"https://ssawant.github.io/posts/ReFT/ReFT.html"},{"title":"ReFT: Representation Finetuning for Language Models | OpenReview","url":"https://openreview.net/forum?id=fykjplMc0V"}]

Based on the search results, here's information about ReFT and representation finetuning:

## Overview

ReFT is a family of Representation Finetuning methods that operate on a frozen base model and learn task-specific interventions on hidden representations. Rather than traditional parameter-efficient finetuning (PEFT) that updates a small number of weights, ReFT was developed because prior interpretability work has shown that representations encode rich semantic information, suggesting that editing representations might be a more powerful alternative.

## Low-rank Linear Subspace ReFT (LoReFT)

A strong instance of the ReFT family is Low-rank Linear Subspace ReFT (LoReFT), with an ablation of this method that trades some performance for increased efficiency. ReFT introduces intervention-based representation editing, steering partial representations of Transformers-based layers via a low-rank projection matrix with orthonormal rows and a linear projector.

In LoReFT, the intervention edits the representation in a low-dimensional linear subspace to take on values obtained from a learned linear projection.

## Performance

Compared to LoRA, LoReFT uses 15×–65× times fewer parameters while achieving state-of-the-art performance on commonsense reasoning, instruction-following, and natural language understanding against the strongest PEFTs.

The search results indicate that ReFT papers exist in the academic literature, though the original ReFT work appears to predate ICLR 2025 (with arxiv version from April 2024). The first search result appears to be from an ICLR 2025 paper that builds upon or extends ReFT methodology to multimodal settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87976600-3d56-4779-be9d-6d2a5fc2e3fc",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "c362c326-3108-4ef8-9fac-b15e29b70e3d",
  "toolUseResult": {
    "query": "ReFT representation finetuning low-rank linear subspace intervention ICLR 2025 activation steering learned",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PQoE1tCa4wGMR29JYDm7Aq",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/dcf88cbc8d01ce7309b83d0ebaeb9d29-Paper-Conference.pdf"
          },
          {
            "title": "[Literature Review] ReFT: Representation Finetuning for Language Models",
            "url": "https://www.themoonlight.io/en/review/reft-representation-finetuning-for-language-models"
          },
          {
            "title": "ReFT: Representation Finetuning for Language Models",
            "url": "https://nlp.stanford.edu/~wuzhengx/reft/index.html"
          },
          {
            "title": "ReFT: Representation Finetuning for Language Models",
            "url": "https://www.linkedin.com/pulse/reft-representation-finetuning-language-models-vlad-bogolin-ea9ce"
          },
          {
            "title": "ReFT: Representation Finetuning for Language Models | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/reft-representation-finetuning-language-models"
          },
          {
            "title": "[PDF] ReFT: Representation Finetuning for Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/ReFT:-Representation-Finetuning-for-Language-Models-Wu-Arora/1bda8efbbf4abae6c8c1da97d6137396807b1e09"
          },
          {
            "title": "[2404.03592] ReFT: Representation Finetuning for Language Models",
            "url": "https://arxiv.org/abs/2404.03592"
          },
          {
            "title": "ReFT: Representation Finetuning for Language Models Zhengxuan Wu∗†",
            "url": "https://arxiv.org/pdf/2404.03592"
          },
          {
            "title": "ReFT: Representation Finetuning for Language Models",
            "url": "https://ssawant.github.io/posts/ReFT/ReFT.html"
          },
          {
            "title": "ReFT: Representation Finetuning for Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=fykjplMc0V"
          }
        ]
      },
      "Based on the search results, here's information about ReFT and representation finetuning:\n\n## Overview\n\nReFT is a family of Representation Finetuning methods that operate on a frozen base model and learn task-specific interventions on hidden representations. Rather than traditional parameter-efficient finetuning (PEFT) that updates a small number of weights, ReFT was developed because prior interpretability work has shown that representations encode rich semantic information, suggesting that editing representations might be a more powerful alternative.\n\n## Low-rank Linear Subspace ReFT (LoReFT)\n\nA strong instance of the ReFT family is Low-rank Linear Subspace ReFT (LoReFT), with an ablation of this method that trades some performance for increased efficiency. ReFT introduces intervention-based representation editing, steering partial representations of Transformers-based layers via a low-rank projection matrix with orthonormal rows and a linear projector.\n\nIn LoReFT, the intervention edits the representation in a low-dimensional linear subspace to take on values obtained from a learned linear projection.\n\n## Performance\n\nCompared to LoRA, LoReFT uses 15×–65× times fewer parameters while achieving state-of-the-art performance on commonsense reasoning, instruction-following, and natural language understanding against the strongest PEFTs.\n\nThe search results indicate that ReFT papers exist in the academic literature, though the original ReFT work appears to predate ICLR 2025 (with arxiv version from April 2024). The first search result appears to be from an ICLR 2025 paper that builds upon or extends ReFT methodology to multimodal settings."
    ],
    "durationSeconds": 7.129466849999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "87976600-3d56-4779-be9d-6d2a5fc2e3fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 61_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"Disentangling Competing Calibration Biases via Geometry-Aware Activati…",
  "leafUuid": "c362c326-3108-4ef8-9fac-b15e29b70e3d",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340"
}
```

---

### Runtime record

_source line 62_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise calibration bias steering with steerability diagnostics",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340"
}
```

---

### Assistant

_source line 63 · 2026-05-19T13:04:06.502Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of all the papers and concepts. Let me synthesize my findings and craft the revision.

Key insights from my research:

1. **"Decodable but Not Corrected" (2605.05715)** - This is a critical paper. The classification-correction gap is real and well-documented:
   - OT is decodable at 71.6% balanced accuracy but Δ≈0 under 29 linear steering configs
   - Specificity ratio ≤0.152 (85-88% overlap with task-critical computation)
   - Non-linear MLP (4096→64→4096 bottleneck): Δ=+2.8pp but with 8.2% damage rate
   - The key finding is that representations can be read with operational value even when linear interventions fail, suggesting specificity ratio as a useful diagnostic before attempting steering. They validated this across Llama-3.1-8B and Qwen2.5-7B on MedQA.

2. **Selective Steering (2601.19375)** - Norm-preserving rotation with discriminative layer selection. Predates Spherical Steering (Jan 2026 vs Feb 2026). 5.5× higher ASR with zero perplexity violations. Code available.

3. **COAST / Minimizing Collateral Damage (2**

605.01167)** - Formalizes collateral damage from steering using empirical second-moment matrices and constrained optimization. Tested across multiple models including Llama-3.2-3B, Llama-3.1-8B, Qwen2.5-14B, and Gemma-2-9B, achieving up to 30% ASR improvement over Angular Steering.

4. **CLAS (2604.24693)** - Context-dependent adaptive steering strengths with instance-level adaptation.

5. **AUSteer (2602.04428)** - Fine-grained AU-level steering that decomposes block activations.

Now I'm noticing a critical gap: there's a paper (2605.05715) showing that linear decodability doesn't guarantee steerability. With specificity ratios around 0.152, there's 85-88% overlap with the task representation, which is a major competitor I need to account for.

The threat to DBS-v2's Phase 3 is real, but I should contextualize it carefully. The paper focuses on "Overthinking" in medical QA—a specific failure mode distinct from what I'm targeting with CSB and CEO. The specificity ratio itself is context-dependent, and prior work on calibration and confidence suggests some directions might have higher specificity. The non-linear MLP achieving +2.8pp improvement indicates partial disentanglement is feasible. Still, the core warning stands: I can't assume decodability implies steerability.

This means Phase 1 needs a steerability diagnostic built in, and the specificity ratio is the right metric to use for validation.

I'm also noticing gaps in my references—I should cite Selective Steering, Minimizing Collateral Damage, CLAS, and AUSteer to properly situate this work. And I need a non-linear MLP fallback for cases where specificity is low.

But stepping back, this decodable-but-not-correctable gap might actually strengthen the intellectual contribution if I frame it right. The real question is whether CSB and CEO directions have higher or lower specificity than generic overconfidence directions—that's where the hypothesis lies.

Since these are competing biases, they might have different steerability profiles, which would explain why monolithic steering sometimes succeeds and sometimes fails. The specificity ratio then becomes diagnostic and methodological at once: it reveals not just what's happening but why certain calibration improvements are possible while others aren't.

This reframes the whole approach—instead of treating biases as a monolith, DBS-v2 validates separability and uses the specificity diagnostic to route different interventions per bias, making the method fundamentally about assumption validation and per-instance steering decisions.

The core contribution shifts from manifold-preserving steering to adaptive intervention routing informed by steerability diagnostics. I'm weighing the resource costs of adding a non-linear fallback—it requires labeled supervision pairs and extra compute, though the MLP itself is lightweight. The reviewer's feedback is specific and actionable, so I should incorporate this revision carefully.

This restructuring isn't a pivot but a major revision that strengthens the core idea. I'm adding steerability diagnostics to Phase 1, introducing adaptive routing in Phase 3 with a non-linear fallback, and reframing the key insight around decodability versus steerability. The disentangled bias steering concept remains intact but now has better theoretical grounding.

Restructuring the approach now... I'm pulling together the landscape of related work—there are several key papers on decodable-but-uncorrected gaps, selective steering with layer selection, collateral damage minimization, and context-adaptive steering strengths that I should reference. Let me compile the citations and write this up thoroughly, though I want to double-check that non-linear MLP result the reviewer flagged since it showed a +2.8 percentage point improvement.

Looking at the numbers more carefully, the paper reports 140 corrections against 104 damages, which translates to an 8.2% damage rate—fairly modest gains. I should be candid about this: the non-linear fallback won't be a silver bullet, but it's still a meaningful improvement over nothing. The paper also demonstrates selective abstention via AUROC of 0.610 that beats five baselines, which is worth incorporating into DBS-v2 as a mechanism for flagging cases where neither linear nor non-linear steering is likely to help.

For the resource budget, adding non-linear MLP training does increase compute requirements, so I need to account for that. The specificity ratio itself comes from decomposing shared versus specific variance between the bias direction and the correct-versus-incorrect subspace, which is the foundation for how I'll extract and apply the correct-steering-bias direction in the updated approach.

I'm now distinguishing between two separate problems: non-surjectivity (where additive steering pushes activations off the learned manifold, solved by norm-preserving rotation) and entanglement (where even norm-preserving rotation along the bias direction can still interfere with task-critical computation if there's heavy overlap). Both need addressing—norm-preservation keeps us on-manifold while the specificity ratio ensures we're not damaging task-critical directions.

The specificity threshold creates a natural hierarchy: when it's high, Spherical Steering alone works well; when it's low, even norm-preserving approaches cause collateral damage and we'd need either a non-linear method or to abstain. I could also layer in COAST's second-moment weighting to identify lower-damage rotation directions, though that might be overcomplicating things for now—better as a future direction.

So the simplified approach is: use Spherical Steering for high specificity cases, fall back to a non-linear residual MLP when that fails, and use selective abstention as a last resort with the bias probe for confidence estimation. Now I'm thinking through the timeline impact of adding the steerability phase and non-linear fallback—that's roughly 3-5 weeks of additional work between data labeling, computing specificity ratios, and training the MLP.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c362c326-3108-4ef8-9fac-b15e29b70e3d",
  "isSidechain": false,
  "requestId": "req_011CbByPPxnnFXzq4BJGBhjU",
  "type": "assistant",
  "uuid": "762eb3a3-b2dc-48c6-9cfe-8525f052bbca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JCAPmDWUvQVpzfoxeugMoh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1069,
      "cache_read_input_tokens": 34988,
      "output_tokens": 3035,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1069,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3035,
          "cache_read_input_tokens": 34988,
          "cache_creation_input_tokens": 1069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1069
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

_source line 64 · 2026-05-19T13:04:06.919Z_

Now I have thorough understanding of all the papers. Let me do one more targeted search to ensure I haven't missed anything about the relationship between specificity ratio and calibration-specific steering:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "762eb3a3-b2dc-48c6-9cfe-8525f052bbca",
  "isSidechain": false,
  "requestId": "req_011CbByPPxnnFXzq4BJGBhjU",
  "type": "assistant",
  "uuid": "2c4aaaed-ce03-4b8f-a9c7-64bf4a243aec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JCAPmDWUvQVpzfoxeugMoh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1069,
      "cache_read_input_tokens": 34988,
      "output_tokens": 3035,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1069,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3035,
          "cache_read_input_tokens": 34988,
          "cache_creation_input_tokens": 1069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1069
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

_source line 65 · 2026-05-19T13:04:07.238Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MHPDn1tPiZGRnHKJc3AaFE`</summary>

```json
{
  "query": "calibration confidence steering entanglement correctness subspace overlap specificity LLM activation probing 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c4aaaed-ce03-4b8f-a9c7-64bf4a243aec",
  "isSidechain": false,
  "requestId": "req_011CbByPPxnnFXzq4BJGBhjU",
  "type": "assistant",
  "uuid": "45db3ab5-3360-4bc5-a68a-012e2194134f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JCAPmDWUvQVpzfoxeugMoh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1069,
      "cache_read_input_tokens": 34988,
      "output_tokens": 3035,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1069,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3035,
          "cache_read_input_tokens": 34988,
          "cache_creation_input_tokens": 1069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1069
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

_source line 66 · 2026-05-19T13:04:18.011Z_

<details><summary>↩ Tool result · `toolu_01MHPDn1tPiZGRnHKJc3AaFE`</summary>

```text
Web search results for query: "calibration confidence steering entanglement correctness subspace overlap specificity LLM activation probing 2026"

Links: [{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/html/2602.06022v1"},{"title":"Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/html/2511.00280v1"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/pdf/2505.21772"},{"title":"Calibrating LLM Confidence with Semantic Steering: A Multi-Prompt Aggregation Framework","url":"https://arxiv.org/html/2503.02863v1"},{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/pdf/2602.08159"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/html/2505.21772v1"}]

I found several highly relevant research papers and resources related to your search query. Here's what the web search revealed:

## Key Research Papers (2026)

**1. Correctness-Optimized Residual Activation Lens (CORAL)**
This recent work on mechanistic interpretability suggests that confidence and correctness signals are distributed, and regularized probes extract correctness signals that sparse methods miss. The research provides evidence that probes capture a general-purpose correctness subspace rather than task-specific patterns.

**2. The Confidence Manifold Study**
Internal probes achieve 0.80-0.97 AUC for detecting correctness, while output-based methods only achieve 0.44-0.64 AUC, indicating the correctness signal exists internally but is not expressed in outputs. The learned direction produces 10.9 percentage point changes in error rates through activation steering.

**3. Calibration Across Layers**
LLMs undergo a clear confidence correction phase in their later layers, where confidence is actively adjusted even after prediction accuracy has stabilized, with a low-dimensional direction in the residual stream consistently aligned with changes in model confidence.

**4. CCPS Method**
This approach applies targeted adversarial perturbations to final hidden states, extracts features reflecting the model's response, and uses a lightweight classifier to predict answer correctness.

**5. Practical Field Guide**
There's also a 2026 practitioner's guide discussing limitations of steering—the result of attempting to add truthfulness directions is usually that the model becomes more confident rather than more correct.

These resources cover the intersection of activation probing, calibration, correctness detection, and steering in LLMs—all central to your search query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45db3ab5-3360-4bc5-a68a-012e2194134f",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "2c3ea683-8af3-4c7f-90c9-5a4c1b6ef0d0",
  "toolUseResult": {
    "query": "calibration confidence steering entanglement correctness subspace overlap specificity LLM activation probing 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YMsEPtgubbbdiAKfXkawqG",
        "content": [
          {
            "title": "Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "https://arxiv.org/html/2602.06022v1"
          },
          {
            "title": "Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra",
            "url": "https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"
          },
          {
            "title": "Calibration Across Layers: Understanding Calibration Evolution in LLMs",
            "url": "https://arxiv.org/html/2511.00280v1"
          },
          {
            "title": "Calibrating LLM Confidence by Probing Perturbed Representation Stability",
            "url": "https://arxiv.org/pdf/2505.21772"
          },
          {
            "title": "Calibrating LLM Confidence with Semantic Steering: A Multi-Prompt Aggregation Framework",
            "url": "https://arxiv.org/html/2503.02863v1"
          },
          {
            "title": "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models",
            "url": "https://arxiv.org/pdf/2602.08159"
          },
          {
            "title": "Calibrating LLM Confidence by Probing Perturbed Representation Stability",
            "url": "https://arxiv.org/html/2505.21772v1"
          }
        ]
      },
      "I found several highly relevant research papers and resources related to your search query. Here's what the web search revealed:\n\n## Key Research Papers (2026)\n\n**1. Correctness-Optimized Residual Activation Lens (CORAL)**\nThis recent work on mechanistic interpretability suggests that confidence and correctness signals are distributed, and regularized probes extract correctness signals that sparse methods miss. The research provides evidence that probes capture a general-purpose correctness subspace rather than task-specific patterns.\n\n**2. The Confidence Manifold Study**\nInternal probes achieve 0.80-0.97 AUC for detecting correctness, while output-based methods only achieve 0.44-0.64 AUC, indicating the correctness signal exists internally but is not expressed in outputs. The learned direction produces 10.9 percentage point changes in error rates through activation steering.\n\n**3. Calibration Across Layers**\nLLMs undergo a clear confidence correction phase in their later layers, where confidence is actively adjusted even after prediction accuracy has stabilized, with a low-dimensional direction in the residual stream consistently aligned with changes in model confidence.\n\n**4. CCPS Method**\nThis approach applies targeted adversarial perturbations to final hidden states, extracts features reflecting the model's response, and uses a lightweight classifier to predict answer correctness.\n\n**5. Practical Field Guide**\nThere's also a 2026 practitioner's guide discussing limitations of steering—the result of attempting to add truthfulness directions is usually that the model becomes more confident rather than more correct.\n\nThese resources cover the intersection of activation probing, calibration, correctness detection, and steering in LLMs—all central to your search query."
    ],
    "durationSeconds": 10.764951959999976,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "45db3ab5-3360-4bc5-a68a-012e2194134f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 67_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"Disentangling Competing Calibration Biases via Geometry-Aware Activati…",
  "leafUuid": "2c3ea683-8af3-4c7f-90c9-5a4c1b6ef0d0",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340"
}
```

---

### Runtime record

_source line 68_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise calibration bias steering with steerability diagnostics",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340"
}
```

---

### Tool call

_source line 69 · 2026-05-19T13:04:21.636Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012mkRsDpBRKKGGQv1gWZKB2`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.08159",
  "prompt": "Extract the full abstract, key findings about the geometric structure of correctness representations, relationship between confidence and correctness subspaces, any results about orthogonality or entanglement of these subspaces, all quantitative results, and models tested. This is about the \"Confidence Manifold\" paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c3ea683-8af3-4c7f-90c9-5a4c1b6ef0d0",
  "isSidechain": false,
  "requestId": "req_011CbByVNHk9P3tRkVGzNLtV",
  "type": "assistant",
  "uuid": "c4a077f1-c098-48ab-916d-c31128818406",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUEJQBv3ai8fbtb4trW4E7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3802,
      "cache_read_input_tokens": 36057,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3802,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 36057,
          "cache_creation_input_tokens": 3802,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3802
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

_source line 70 · 2026-05-19T13:04:28.604Z_

<details><summary>↩ Tool result · `toolu_012mkRsDpBRKKGGQv1gWZKB2`</summary>

```text
# The Confidence Manifold: Key Findings

## Full Abstract
"When a language model asserts that 'the capital of Australia is Sydney,' does it know this is wrong? We characterize the geometry of correctness representations across 9 models from 5 architecture families. The structure is simple: the discriminative signal occupies 3-8 dimensions, performance degrades with additional dimensions, and no nonlinear classifier improves over linear separation. Centroid distance in the low-dimensional subspace matches trained probe performance (0.90 AUC), enabling few-shot detection: on GPT-2, 25 labeled examples achieve 89% of full-data accuracy. We validate causally through activation steering: the learned direction produces 10.9 percentage point changes in error rates while random directions show no effect. Internal probes achieve 0.80-0.97 AUC; output-based methods (P(True), semantic entropy) achieve only 0.44-0.64 AUC. The correctness signal exists internally but is not expressed in outputs. That centroid distance matches probe performance indicates class separation is a mean shift, making detection geometric rather than learned."

## Key Geometric Findings

- **Dimensionality**: The correctness signal occupies 3-8 dimensions across tested models
- **Linear Separability**: Linear classification matches nonlinear approaches; no advantage from complexity
- **Class Structure**: "class separation is a mean shift," suggesting simple geometric organization
- **Internal vs. Output**: Strong internal signal (0.80-0.97 AUC) versus weak output-based detection (0.44-0.64 AUC)

## Quantitative Results

- Centroid distance probe achieves 0.90 AUC
- GPT-2 few-shot detection: 25 examples reach 89% of full-data accuracy
- Activation steering produces 10.9 percentage point error rate changes
- Random directions show no effect

## Models Tested

9 models across 5 architecture families (specific identities not detailed in abstract)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4a077f1-c098-48ab-916d-c31128818406",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "9d5fe78f-aa34-43ad-88d8-a7b033955b64",
  "toolUseResult": {
    "bytes": 46880,
    "code": 200,
    "codeText": "OK",
    "result": "# The Confidence Manifold: Key Findings\n\n## Full Abstract\n\"When a language model asserts that 'the capital of Australia is Sydney,' does it know this is wrong? We characterize the geometry of correctness representations across 9 models from 5 architecture families. The structure is simple: the discriminative signal occupies 3-8 dimensions, performance degrades with additional dimensions, and no nonlinear classifier improves over linear separation. Centroid distance in the low-dimensional subspace matches trained probe performance (0.90 AUC), enabling few-shot detection: on GPT-2, 25 labeled examples achieve 89% of full-data accuracy. We validate causally through activation steering: the learned direction produces 10.9 percentage point changes in error rates while random directions show no effect. Internal probes achieve 0.80-0.97 AUC; output-based methods (P(True), semantic entropy) achieve only 0.44-0.64 AUC. The correctness signal exists internally but is not expressed in outputs. That centroid distance matches probe performance indicates class separation is a mean shift, making detection geometric rather than learned.\"\n\n## Key Geometric Findings\n\n- **Dimensionality**: The correctness signal occupies 3-8 dimensions across tested models\n- **Linear Separability**: Linear classification matches nonlinear approaches; no advantage from complexity\n- **Class Structure**: \"class separation is a mean shift,\" suggesting simple geometric organization\n- **Internal vs. Output**: Strong internal signal (0.80-0.97 AUC) versus weak output-based detection (0.44-0.64 AUC)\n\n## Quantitative Results\n\n- Centroid distance probe achieves 0.90 AUC\n- GPT-2 few-shot detection: 25 examples reach 89% of full-data accuracy\n- Activation steering produces 10.9 percentage point error rate changes\n- Random directions show no effect\n\n## Models Tested\n\n9 models across 5 architecture families (specific identities not detailed in abstract)",
    "durationMs": 6964,
    "url": "https://arxiv.org/abs/2602.08159"
  },
  "sourceToolAssistantUUID": "c4a077f1-c098-48ab-916d-c31128818406",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-19T13:04:31.482Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QFAyvcy1nouE1bwseVhMwH`</summary>

```json
{
  "query": "\"Guiding Giants\" lightweight controllers weighted activation steering arXiv 2505.20309 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d5fe78f-aa34-43ad-88d8-a7b033955b64",
  "isSidechain": false,
  "requestId": "req_011CbByW9VqKjzwgCCkFsQ34",
  "type": "assistant",
  "uuid": "7f9a6ce5-7f49-45f4-b2fe-87d4393cc47f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013FM8ZDfXgk5XZ7zgbhxTYU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 620,
      "cache_read_input_tokens": 39859,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 620,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 39859,
          "cache_creation_input_tokens": 620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 620
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

_source line 72 · 2026-05-19T13:04:38.154Z_

<details><summary>↩ Tool result · `toolu_01QFAyvcy1nouE1bwseVhMwH`</summary>

```text
Web search results for query: ""Guiding Giants" lightweight controllers weighted activation steering arXiv 2505.20309 2025"

Links: [{"title":"[2505.20309] Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs","url":"https://arxiv.org/abs/2505.20309"},{"title":"Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs","url":"https://arxiv.org/pdf/2505.20309"},{"title":"Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs","url":"https://arxiv.org/html/2505.20309"},{"title":"Computer Science May 2025","url":"https://www.arxiv.org/list/cs/2025-05?skip=10425&show=500"},{"title":"Machine Learning May 2025","url":"https://www.arxiv.org/list/cs.LG/2025-05?skip=4325&show=50"},{"title":"Computation and Language May 2025","url":"https://arxiv.org/list/cs.CL/2025-05?skip=1475&show=250"},{"title":"The Anatomy of Alignment: Decomposing Preference Optimization by Steering Sparse Features","url":"https://arxiv.org/html/2509.12934v1"},{"title":"MASteer: Multi-Agent Adaptive Steer Strategy for End-to-End LLM Trustworthiness Repair","url":"https://arxiv.org/html/2508.06963v1"}]

I found the paper! Here's what I discovered:

**"Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs"** (arXiv:2505.20309)

The paper addresses controlling undesirable Large Language Model behaviors, such as the generation of unsafe content or failing to adhere to safety guidelines, often relying on costly fine-tuning.

The authors introduce a novel approach using a lightweight, trainable controller network integrated during inference that observes specific intermediate LLM activations and predicts both a global scaling factor and layer-specific weights. The predicted global scaling factor and layer-specific weights then dynamically modulate the intensity of a steering patch, derived from a pre-computed "refusal direction" vector, applied across the LLM's layers during generation.

Trained on activations from both harmful and benign prompts, the controller learns to discriminatively apply nuanced, layer-aware interventions, activating steering primarily for harmful inputs.

The paper was submitted on May 22, 2025, with a revised version (v2) on October 7, 2025, and the authors are Amr Hegazy, Mostafa Elhoushi, and Amr Alanwar. The work focuses on safety-oriented inference-time control of LLMs without the overhead of fine-tuning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f9a6ce5-7f49-45f4-b2fe-87d4393cc47f",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "d7ffee42-4e5a-46f0-bf83-b395180f4d45",
  "toolUseResult": {
    "query": "\"Guiding Giants\" lightweight controllers weighted activation steering arXiv 2505.20309 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KQEf3XLT1mK4fVzXFuGaGe",
        "content": [
          {
            "title": "[2505.20309] Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs",
            "url": "https://arxiv.org/abs/2505.20309"
          },
          {
            "title": "Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs",
            "url": "https://arxiv.org/pdf/2505.20309"
          },
          {
            "title": "Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs",
            "url": "https://arxiv.org/html/2505.20309"
          },
          {
            "title": "Computer Science May 2025",
            "url": "https://www.arxiv.org/list/cs/2025-05?skip=10425&show=500"
          },
          {
            "title": "Machine Learning May 2025",
            "url": "https://www.arxiv.org/list/cs.LG/2025-05?skip=4325&show=50"
          },
          {
            "title": "Computation and Language May 2025",
            "url": "https://arxiv.org/list/cs.CL/2025-05?skip=1475&show=250"
          },
          {
            "title": "The Anatomy of Alignment: Decomposing Preference Optimization by Steering Sparse Features",
            "url": "https://arxiv.org/html/2509.12934v1"
          },
          {
            "title": "MASteer: Multi-Agent Adaptive Steer Strategy for End-to-End LLM Trustworthiness Repair",
            "url": "https://arxiv.org/html/2508.06963v1"
          }
        ]
      },
      "I found the paper! Here's what I discovered:\n\n**\"Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs\"** (arXiv:2505.20309)\n\nThe paper addresses controlling undesirable Large Language Model behaviors, such as the generation of unsafe content or failing to adhere to safety guidelines, often relying on costly fine-tuning.\n\nThe authors introduce a novel approach using a lightweight, trainable controller network integrated during inference that observes specific intermediate LLM activations and predicts both a global scaling factor and layer-specific weights. The predicted global scaling factor and layer-specific weights then dynamically modulate the intensity of a steering patch, derived from a pre-computed \"refusal direction\" vector, applied across the LLM's layers during generation.\n\nTrained on activations from both harmful and benign prompts, the controller learns to discriminatively apply nuanced, layer-aware interventions, activating steering primarily for harmful inputs.\n\nThe paper was submitted on May 22, 2025, with a revised version (v2) on October 7, 2025, and the authors are Amr Hegazy, Mostafa Elhoushi, and Amr Alanwar. The work focuses on safety-oriented inference-time control of LLMs without the overhead of fine-tuning."
    ],
    "durationSeconds": 6.668643772999989,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7f9a6ce5-7f49-45f4-b2fe-87d4393cc47f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 73 · 2026-05-19T13:04:51.809Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the landscape. Let me draft the complete revised JSON.

Key revisions needed:

1. **CRITICAL: Address the classification-correction gap (2605.05715)**
   - Add specificity ratio as a diagnostic in Phase 1
   - Distinguish between "decodable" and "steerable"
   - This changes the core problem framing slightly

2. **SEPARABILITY ≠ STEERABILITY**
   - Phase 1 needs a "steerability diagnostic" 
   - Compute specificity ratio for CSB and CEO directions relative to correct/incorrect subspace
   
3. **MISSING REFERENCES**
   - Selective Steering (2601.19375), Minimizing Collateral Damage (2605.01167), CLAS (2604.24693), AUSteer (2602.04428), Confidence Manifold (2602.08159)

4. **NON-LINEAR STEERING FALLBACK**
   - Add learned non-linear residual MLP for low-specificity directions
   - Add selective abstention as ultimate fallback

The classification-correction gap actually strengthens the paper's contribution—it raises a fundamental question about whether CSB and CEO exhibit different specificity ratios, which could reshape how we think about steering effectiveness.

This reframing makes DBS-v2's core contribution clearer: testing whether these biases have distinct steerability profiles, routing interventions adaptively based on specificity, and providing interpretable diagnostics about which calibration issues are actually correctable. That's a more compelling narrative than just applying bias-specific rotations. The change warrants a "major" classification since it updates the core framing around decodability versus steerability, expands Phase 1 into a proper steerability diagnostic, restructures Phase 3 with adaptive routing and non-linear fallbacks, integrates new references, and requires updated resource estimates.

Writing the full JSON now...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7ffee42-4e5a-46f0-bf83-b395180f4d45",
  "isSidechain": false,
  "requestId": "req_011CbByWrJkdKtPS8T1rxXyr",
  "type": "assistant",
  "uuid": "190dae31-df41-496a-ba09-d4dfbc49a776",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XfGbKniXRZadHitBnFJZLK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 40479,
      "output_tokens": 9087,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 784,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9087,
          "cache_read_input_tokens": 40479,
          "cache_creation_input_tokens": 784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 784
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

_source line 74 · 2026-05-19T13:04:51.819Z_

Now I have deep understanding of all the relevant papers. Let me synthesize everything and produce the complete revised research idea.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "190dae31-df41-496a-ba09-d4dfbc49a776",
  "isSidechain": false,
  "requestId": "req_011CbByWrJkdKtPS8T1rxXyr",
  "type": "assistant",
  "uuid": "1b3d318b-89e5-40f8-9295-ad24d1badfd7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XfGbKniXRZadHitBnFJZLK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 40479,
      "output_tokens": 9087,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 784,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9087,
          "cache_read_input_tokens": 40479,
          "cache_creation_input_tokens": 784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 784
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

_source line 75 · 2026-05-19T13:08:04.769Z_

<details open><summary>🔧 Tool call — Write · `toolu_015KwYoPUQmbJQiYx9KFuZnZ`</summary>

```json
{
  "file_path": "/tmp/revised_idea_r2.json",
  "content": "{\n  \"title\": \"Disentangling Competing Calibration Biases via Geometry-Aware Activation Steering\",\n  \"change_type\": \"major\",\n  \"core_problem\": \"LLM miscalibration arises from at least two competing biases — choice-supportive bias (inflating confidence in initial answers) and contradictory-evidence overweighting (causing excessive confidence revision under criticism) — that require opposing corrections. Existing calibration methods apply uniform corrections that cannot simultaneously address biases pulling confidence in opposite directions. Recent work (Liu, 2605.05715) further reveals a classification-correction gap: failure-mode directions that are linearly decodable may not be linearly steerable due to entanglement with task-critical computation (specificity ratio ≤0.152). This means even if competing biases can be identified in activations, correcting them requires knowing not just WHICH bias dominates but WHETHER each bias direction is steerable — and routing to appropriate interventions (linear rotation, non-linear correction, or selective abstention) accordingly. Can we jointly diagnose per-instance bias dominance AND steerability to apply targeted, manifold-preserving corrections where possible and graceful degradation where not?\",\n  \"opportunity\": \"Kumaran et al. (Nature Machine Intelligence, 2026; arXiv 2507.03120) identified that LLM miscalibration results from two mechanistically distinct behavioral biases in Gemma 3, GPT-4o, and o1-preview: choice-supportive bias inflates confidence in selected answers, while contradictory-advice overweighting causes models to over-react to opposing evidence. Miao & Ungar (arXiv 2603.25052, 2026) independently showed that calibration and verbalized confidence signals are encoded linearly but orthogonally in the residual stream across three 7-8B models, establishing that confidence-related constructs have accessible geometric structure. Liu (arXiv 2605.05715, May 2026) demonstrated a critical classification-correction gap: linearly decodable failure directions (71.6% balanced accuracy) yield Δ≈0 under 29 steering configurations because the failure directions have 85-88% overlap with task-critical computation (specificity ratio ≤0.152) — but crucially, the paper also shows that (a) a learned non-linear residual MLP achieves Δ=+2.8pp where all linear methods fail, and (b) the decodable signal still supports selective abstention (AUROC 0.610, outperforming 5 uncertainty baselines). The 'Confidence Manifold' study (arXiv 2602.08159) found correctness signals occupy only 3-8 dimensions with simple mean-shift geometry across 9 models, suggesting that for calibration-related directions, the geometric structure may be more favorable than for the medical overthinking phenomenon Liu studied. The convergence of (a) identified competing biases, (b) linear confidence encoding evidence, (c) the decodable-steerable distinction with quantitative diagnostics, and (d) both norm-preserving rotation (Spherical Steering, ICML 2026) and collateral-damage-aware optimization (COAST, 2605.01167) creates an opportunity for a principled pipeline: diagnose bias identity, assess steerability, and route to the appropriate intervention.\",\n  \"landscape\": \"Kumaran et al. (Nature MI, 2026) identified competing biases (CSB and CEO) via behavioral experiments on Gemma 3, GPT-4o, and o1-preview but proposed no correction framework and provided no mechanistic (activation-level) evidence. Miao & Ungar (arXiv 2603.25052, 2026) demonstrated that calibration accuracy and verbalized confidence are linearly encoded but orthogonal in 7-8B models (cosine similarity <0.04 across layers), and introduced adaptive steering achieving 4-7× ECE improvement — but they target the confidence-accuracy misalignment gap, not the competing bias structure. Tsujimura & Tagade (arXiv 2508.17182, Aug 2025) decomposed LLM assertiveness into emotional and logical sub-components via unsupervised clustering on Llama-3.2-1B-Instruct (645 samples), finding two clusters in high-assertive representations — methodologically adjacent but critically different: their decomposition is descriptive (post-hoc ChatGPT-labeled clusters of communication style) rather than causally grounded in identified cognitive biases, uses a single 1B model, reports no calibration metrics, and addresses assertiveness rather than calibration. The 'Wired for Overconfidence' paper (2604.01457, April 2026) identifies overconfidence circuits in Qwen2.5-3B and Llama-3.2-3B, achieving 96.9% ECE reduction on PopQA via monolithic activation steering, but only tests 3B models and treats overconfidence as a single phenomenon. Liu (arXiv 2605.05715, May 2026) is the most directly relevant recent advance: the paper demonstrates a classification-correction gap where linearly decodable failure directions (71.6% balanced accuracy on Llama-3.1-8B) yield Δ≈0 across five families of linear steering (29 configurations) because the failure direction has 85-88% overlap with task-critical computation (specificity ratio ≤0.152). Three convergent evidence lines confirm entanglement: low specificity, shared-direction steering damages accuracy (-12.1pp), and LEACE concept erasure damages accuracy (-3.6pp). Crucially, a learned non-linear bottleneck MLP (4096→64→4096) achieves Δ=+2.8pp (p=0.025) where linear methods fail, though with 8.2% damage rate — demonstrating that partial disentanglement is possible via non-linear transforms. The paper proposes the specificity ratio as a pre-intervention diagnostic and recommends selective abstention (AUROC 0.610) when steering fails. However, this was studied for medical overthinking, a single failure mode; whether calibration biases (CSB/CEO) exhibit similar or different entanglement profiles is an open question. Ji et al. (EMNLP 2025) modulates a single Verbal Uncertainty Feature direction, reducing hallucinations by ~30%, capturing only the net effect of competing biases. Joshi et al. (EMNLP 2025) found a single calibration direction but did not decompose it. CORAL (arXiv 2602.06022, Feb 2026) achieves 49% ECE improvement via correctness-subspace probing on 7B models but uses a single MLP probe direction. The 'Confidence Manifold' study (arXiv 2602.08159, Feb 2026) found correctness signals occupy 3-8 dimensions with simple mean-shift geometry across 9 models from 5 families, and causally validated via steering (10.9pp error rate change) — importantly, the low dimensionality and linear separability of correctness signals contrasts with Liu's high-entanglement finding for overthinking, suggesting calibration-related directions may have more favorable specificity profiles. Wang & Stengel-Eskin (ICLR 2026) introduced DINCO to normalize suggestibility bias via self-generated distractors at the output level. Zhuang et al. (arXiv 2025) proposed RDG to alleviate choice-supportive bias through fine-tuning but did not address CEO. CCPS (arXiv 2025) achieves ~55% ECE reduction via representation stability probing on MMLU. 'Breaking the Mirror' (arXiv 2509.03647) found that self-preference bias 'spans multiple or nonlinear directions,' achieving 97% unjustified bias reduction but with instability on legitimate cases — a direct warning that some biases may not be linearly separable. On the steering methodology side, the landscape has rapidly matured: Spherical Steering (arXiv 2602.08169, ICML 2026) performs norm-preserving geodesic rotation, outperforming addition-based baselines by +10% on TruthfulQA while maintaining generation quality. Selective Steering (Dang & Ngo, arXiv 2601.19375, Jan 2026) independently developed norm-preserving rotation with discriminative layer selection — applying steering only where feature representations exhibit opposite-signed class alignment, achieving 5.5× higher attack success rates with zero perplexity violations across 8 models. COAST (Nguyen et al., arXiv 2605.01167, May 2026) formalizes collateral damage from steering interventions as unintended alignment changes along non-target feature directions, and solves a constrained optimization that minimizes expected squared collateral change weighted by the empirical second-moment matrix — achieving up to 30% improvement over Angular Steering while reducing Pearson r<-0.9 correlation between collateral damage and accuracy loss. AUSteer (arXiv 2602.04428, Feb 2026) decomposes block activations into fine-grained atomic units, steering fewer activations more precisely. CLAS (arXiv 2604.24693, Apr 2026) adapts steering strengths per-context, outperforming ReFT and LoRA with limited labeled data. 'Steered LLM Activations are Non-Surjective' (2604.09839, April 2026) formally proved that additive steering pushes activations off-manifold; 'A Sober Look at Steering Vectors' (NeurIPS 2024) showed many behaviors are unsteerable. No existing method jointly diagnoses which calibration bias dominates, assesses the steerability of each bias direction (via specificity ratio or equivalent), and routes to bias-specific interventions that range from manifold-preserving rotation to learned non-linear correction — yet the competing effects of CSB and CEO on calibration, combined with the now-established decodable-steerable gap, mean that both uniform correction AND uniform intervention strategy are fundamentally suboptimal.\",\n  \"inspired_by\": \"Gap: Competing biases create non-uniform miscalibration patterns that single-direction methods cannot fix (Kumaran et al. 2026), while the classification-correction gap (Liu, 2605.05715) shows that decodable directions are not necessarily steerable — meaning Phase 1's separability validation is necessary but insufficient. Pattern: Theory-driven contrastive probing (Miao & Ungar 2026) + steerability diagnostics (specificity ratio, Liu 2026) + adaptive intervention routing (geometry-aware rotation for steerable directions, learned non-linear correction for entangled directions). Untried combination: Cognitive-bias-grounded contrastive stimuli → per-instance bias diagnosis → specificity-informed intervention routing (Spherical Steering / non-linear MLP / selective abstention), with the hypothesis that CSB and CEO may have asymmetric steerability profiles — which would explain why monolithic steering sometimes succeeds and sometimes fails at calibration correction.\",\n  \"approach\": \"We design DBS-v2 (Disentangled Bias Steering) in three phases, now incorporating the critical distinction between decodability and steerability identified by Liu (2605.05715).\\n\\n**Phase 1 — Assumption Validation & Steerability Assessment (Weeks 1-5):** This phase tests TWO assumptions, not one: (A) that CSB and CEO produce distinguishable activation signatures, and (B) that identified directions are steerable without catastrophic collateral damage.\\n\\n*Phase 1A — Separability (Weeks 1-3):* We construct two contrastive stimulus sets: for CSB, we compare hidden states when the model reviews its own prior answer vs. a fresh unattributed answer (eliciting choice-supportive inflation); for CEO, we compare states when contradictory expert advice is present vs. absent (eliciting evidence overweighting). Using difference-in-means on these contrastive pairs, we extract candidate bias directions in the residual stream. We validate separability via: (a) cosine similarity between candidate directions, (b) principal angle analysis between CSB and CEO subspaces using the methodology of Miao & Ungar (2026), (c) PCA to assess whether 2 directions capture sufficient variance vs. requiring higher-dimensional subspaces, (d) ICA to test whether statistically independent (not just orthogonal) components emerge, and (e) cross-prediction ablations to confirm removing one bias subspace does not collapse the other. If CSB and CEO directions show cosine similarity >0.3 or shared variance >15%, we activate the separability fallback: extracting a multi-direction bias subspace via SAE-derived features and training a subspace projection classifier.\\n\\n*Phase 1B — Steerability Diagnostics (Weeks 3-5):* This is a critical addition motivated by Liu (2605.05715). Even if CSB and CEO are separable (Phase 1A succeeds), steering along identified directions may fail if those directions are entangled with task-critical computation. For each identified bias direction, we compute: (a) the **specificity ratio** — the proportion of mode-specific variance vs. shared variance with the correct-vs-incorrect subspace, following Liu's shared-specific decomposition methodology. Concretely, we extract the correctness subspace (correct vs. incorrect answer centroids), then decompose each bias direction into a component within this subspace (shared) and a component orthogonal to it (mode-specific). The specificity ratio = ||mode-specific||² / ||total||². (b) **Within-class variance analysis** — comparing within-class variance to inter-centroid gap for each bias direction (Liu's second diagnostic). (c) **LEACE concept erasure test** — applying concept erasure to each bias direction and measuring accuracy damage as causal evidence of entanglement. (d) **Cross-architecture stability** — verifying specificity ratios are consistent across model families.\\n\\nWe establish quantitative thresholds informed by Liu's findings: specificity ratio ≥0.5 → HIGH steerability (linear rotation expected to work); 0.2-0.5 → MEDIUM (rotation may partially work, monitor collateral damage); <0.2 → LOW (linear steering unlikely to succeed, route to non-linear intervention). These thresholds are calibrated against Liu's findings where specificity ≤0.152 yielded Δ≈0 for linear steering but ≤0.999 succeeded for refusal steering. Crucially, we hypothesize that CSB and CEO may have ASYMMETRIC specificity profiles — one may be more steerable than the other — which would provide a mechanistic explanation for why monolithic calibration steering sometimes succeeds partially.\\n\\nPhase 1 results constitute an independent contribution: the first joint separability-and-steerability assessment of behaviorally-identified competing biases, providing the field's first specificity ratio measurements for calibration-related bias directions.\\n\\n**Phase 2 — Per-Instance Bias Diagnosis (Weeks 4-8):** A lightweight logistic probe (or, in the fallback case, a small MLP) trained on per-instance projection magnitudes onto each bias direction classifies which bias dominates for a given query. We stratify by difficulty: on easy questions where models are already confident, CSB likely dominates; on hard questions under criticism, CEO likely dominates. The probe output provides a continuous dominance score. NEW: The Phase 1B steerability assessment informs a per-direction intervention routing table, so the probe's output determines not only which bias is active but which intervention to apply.\\n\\n**Phase 3 — Adaptive Geometry-Aware Intervention (Weeks 6-14):** Instead of a single intervention strategy, Phase 3 now implements an adaptive routing pipeline informed by Phase 1B's steerability diagnostics:\\n\\n*Route A — Spherical Steering (for HIGH-specificity directions):* When a bias direction has specificity ratio ≥0.5, we adopt Spherical Steering (You et al., ICML 2026) as the primary intervention: rotating activations along a geodesic away from the dominant bias direction while preserving activation norms. This addresses the off-manifold concern (Mishra et al., 2604.09839) while the high specificity ensures minimal collateral damage to task-critical computation. A confidence gate modulates rotation magnitude based on the probe's dominance score. We note that Selective Steering (Dang & Ngo, 2601.19375) provides an alternative norm-preserving formulation with discriminative layer selection; we ablate both to determine which is more effective for calibration-specific interventions.\\n\\n*Route B — Learned Non-Linear Residual Correction (for LOW-specificity directions):* When a bias direction has specificity ratio <0.2, linear steering of any kind (additive, rotational, or projected) is expected to fail due to entanglement with task-critical computation (Liu, 2605.05715). Following Liu's finding that a bottleneck residual MLP (d→64→d) achieves Δ=+2.8pp where all 29 linear configurations yield Δ≈0, we train a small non-linear residual adapter per bias type. The adapter takes the hidden state as input and outputs a residual correction, trained via supervision on (biased state, corrected state) pairs extracted from the contrastive dataset. We incorporate the COAST framework (Nguyen et al., 2605.01167) by weighting the training loss by the empirical second-moment matrix to minimize expected collateral damage along non-target feature directions. The adapter's bottleneck architecture (d→64→d, <0.1% of model parameters) keeps the intervention lightweight and inference-efficient.\\n\\n*Route C — Selective Abstention (for UNSTEERABLE directions):* When Phase 1B indicates low specificity AND Phase 3 ablations confirm that neither Route A nor Route B improves calibration without excessive damage (>5% accuracy degradation), we leverage the decodable signal for selective abstention: the bias probe flags instances where the dominant bias has high activation but low steerability, outputting a reliability score. Following Liu's demonstration that decodable signals support post-generation reliability estimation (AUROC 0.610) even when correction fails, this provides a graceful degradation path. In practice, this means DBS-v2 can still improve system-level calibration by selectively expressing lower confidence (or abstaining) on instances where bias correction is not safely possible.\\n\\n*Route D — Medium-Specificity Hybrid (for intermediate cases):* For directions with specificity 0.2-0.5, we apply Spherical Steering with conservative rotation magnitude (capped at 50% of the high-specificity coefficient) and monitor collateral damage via the COAST second-moment diagnostic. If per-instance collateral damage exceeds a threshold, we fall back to Route B for that instance.\\n\\nWe evaluate on TriviaQA, MMLU, PopQA, and NQ-Open across Gemma 4 31B (Dense), Qwen3-8B, and Llama-3.1-8B-Instruct. We additionally include Qwen2.5-3B and Llama-3.2-3B as supplementary models to enable fair comparison with 'Wired for Overconfidence' results at the same scale. Metrics: ECE, Brier score, AUROC, difficulty-stratified ECE (easy/medium/hard partitions), AND NEW: per-direction specificity ratios, collateral damage measurements (accuracy on non-target tasks before/after steering), and route-distribution analysis (what fraction of instances are routed to each intervention). Baselines: temperature scaling, CCPS, VUF intervention, DINCO, CORAL, Miao & Ungar adaptive steering, monolithic circuit ablation (Wired for Overconfidence replication at 3B scale), monolithic Spherical Steering (single direction, no bias decomposition), and NEW: monolithic non-linear residual MLP (single direction, no bias decomposition) to isolate the contribution of bias decomposition from the contribution of non-linear correction.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"750-1050 H100\",\n      \"timeline\": \"16-20 weeks\",\n      \"estimated_gpu_cost\": \"$1,875-$2,625 (H100 @ ~$2.50/hr mid-tier provider)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"650-900 H100\",\n      \"timeline\": \"12-15 weeks\",\n      \"claude_api_cost\": \"$350-$600 (Sonnet 4.6 for contrastive dataset generation, probing code, specificity ratio computation scripts, non-linear adapter training, analysis)\",\n      \"estimated_gpu_cost\": \"$1,625-$2,250\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"1000-1400 H100\",\n      \"timeline\": \"6-10 weeks\",\n      \"claude_api_cost\": \"$800-$1,400 (Opus 4.7 for experiment orchestration, assumption validation analysis, steerability diagnostics, adapter training sweeps, ablation design)\",\n      \"estimated_gpu_cost\": \"$2,500-$3,500\",\n      \"speed_bottleneck\": \"Phase 1A→1B is inherently sequential (separability must be established before steerability diagnostics are meaningful). Phase 1B requires extracting the correctness subspace and computing specificity ratios per-direction per-model, which is parallelizable across models but adds ~2 weeks over original timeline. Route B adapter training requires supervision pairs from Phase 1 contrastive data. Steering coefficient search across 5 models × 4 datasets × 3-4 intervention routes generates large evaluation matrices. Fair replication of 'Wired for Overconfidence' baselines on 3B models adds overhead.\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — primary target, tight but feasible with aggressive Phase 1 timeline)\",\n    \"ARR August 2026 cycle (Aug 3, 2026 — targets EMNLP 2027 or future *CL venues)\",\n    \"NeurIPS 2026 Workshops (~Aug 29, 2026 — workshop paper track for Phase 1 separability + steerability results)\",\n    \"AACL-IJCNLP 2026 (ARR May 25 commitment deadline Aug 26, 2026 — if Phase 1 completes early)\",\n    \"ICLR 2027 (expected Oct 2026 deadline — full paper with all phases and routes complete)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Competing Biases underlie Overconfidence and Underconfidence in LLMs (Kumaran et al., Nature Machine Intelligence 2026; arXiv 2507.03120)\",\n    \"Closing the Confidence-Faithfulness Gap in Large Language Models (Miao & Ungar, arXiv 2603.25052, 2026) — orthogonal calibration/confidence encoding, adaptive steering\",\n    \"LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components (Tsujimura & Tagade, arXiv 2508.17182, 2025) — closest methodological precedent\",\n    \"Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes (Liu, arXiv 2605.05715, May 2026) — classification-correction gap, specificity ratio diagnostic\",\n    \"Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs (arXiv 2604.01457, 2026)\",\n    \"Spherical Steering: Geometry-Aware Activation Rotation for Language Models (You et al., ICML 2026; arXiv 2602.08169)\",\n    \"Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection (Dang & Ngo, arXiv 2601.19375, Jan 2026) — independent norm-preserving rotation with discriminative layer selection\",\n    \"Minimizing Collateral Damage in Activation Steering (Nguyen et al., arXiv 2605.01167, May 2026) — COAST framework, collateral damage formalization, second-moment optimization\",\n    \"Steered LLM Activations are Non-Surjective (Mishra et al., arXiv 2604.09839, 2026)\",\n    \"A Sober Look at Steering Vectors for LLMs (Tan et al., NeurIPS 2024)\",\n    \"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models (arXiv 2602.08159, 2026) — 3-8 dimensional correctness signals, linear separability across 9 models\",\n    \"Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators (arXiv 2509.03647, 2025) — nonlinear bias warning\",\n    \"CORAL: Correctness-Optimized Residual Activation Lens (arXiv 2602.06022, 2026) — calibration-aware steering baseline\",\n    \"Mind the Confidence Gap: Overconfidence, Calibration, and Distractor Effects in Large Language Models (Chhikara, TMLR 2025)\",\n    \"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025)\",\n    \"Calibrating Verbalized Confidence with Self-Generated Distractors (Wang & Stengel-Eskin, ICLR 2026)\",\n    \"Calibration Across Layers: Understanding Calibration Evolution in LLMs (Joshi et al., EMNLP 2025)\",\n    \"Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation (Zhuang et al., arXiv 2512.03082, 2025)\",\n    \"Calibrating LLM Confidence by Probing Perturbed Representation Stability (arXiv 2505.21772, 2025)\",\n    \"Know When You're Wrong: Aligning Confidence with Correctness for LLM Error Detection (arXiv 2603.06604, 2026)\",\n    \"Fine-Grained Activation Steering: Steering Less, Achieving More (arXiv 2602.04428, 2026) — atomic-unit-level steering\",\n    \"Contextual Linear Activation Steering of Language Models (arXiv 2604.24693, 2026) — context-adaptive steering strengths\"\n  ],\n  \"description\": \"We propose DBS-v2 (Disentangled Bias Steering), a method that separately identifies, assesses the steerability of, and adaptively corrects two competing sources of LLM miscalibration identified by Kumaran et al. (2026): choice-supportive bias (CSB, inflating confidence in selected answers) and contradictory-evidence overweighting (CEO, causing excessive confidence revision under criticism). Unlike Tsujimura & Tagade (2025), who descriptively decomposed assertiveness into emotion/logic clusters via unsupervised methods on a 1B model without calibration evaluation, DBS-v2 is grounded in causally-identified cognitive biases with theory-driven contrastive stimuli and directly targets calibration metrics.\\n\\nA critical insight motivating this revision is the classification-correction gap demonstrated by Liu (2605.05715): linearly decodable failure directions (71.6% balanced accuracy) can yield Δ≈0 under steering because they overlap 85-88% with task-critical computation. This means that separability (Phase 1A) is necessary but insufficient — we must also assess steerability before committing to an intervention strategy.\\n\\nThe method proceeds in three phases. Phase 1A (Separability Validation) tests whether CSB and CEO produce distinguishable activation signatures using contrastive activation probing, validated via cosine similarity, principal angle analysis, PCA/ICA dimensionality assessment, and cross-prediction ablation (following Miao & Ungar, 2026). Phase 1B (Steerability Assessment) — the key new addition — computes the specificity ratio (mode-specific vs. shared variance with the correct/incorrect subspace) for each identified bias direction, following Liu's shared-specific decomposition methodology. This diagnostic distinguishes between directions that are decodable-and-steerable vs. decodable-but-entangled. We hypothesize that CSB and CEO may have asymmetric specificity profiles, which would explain why monolithic calibration steering yields inconsistent results across settings. The Confidence Manifold study (2602.08159) provides encouraging evidence that correctness-related signals occupy only 3-8 dimensions with simple mean-shift geometry, suggesting calibration-related directions may have more favorable specificity than the medical overthinking phenomenon Liu studied.\\n\\nPhase 2 trains a lightweight per-instance bias dominance classifier whose output determines both which bias is active and which intervention route to apply. Phase 3 implements adaptive routing: (Route A) Spherical Steering for high-specificity directions (≥0.5), with Selective Steering (Dang & Ngo, 2601.19375) as an ablation alternative providing discriminative layer selection; (Route B) a learned non-linear bottleneck residual MLP (d→64→d) for low-specificity directions (<0.2), trained with COAST-informed (Nguyen et al., 2605.01167) collateral-damage-aware loss weighting; (Route C) selective abstention leveraging the decodable signal for reliability estimation when neither linear nor non-linear correction is safe; and (Route D) conservative hybrid steering for intermediate specificity (0.2-0.5).\\n\\nWe evaluate on TriviaQA, MMLU, PopQA, and NQ-Open across five models: Gemma 4 31B (Dense), Qwen3-8B, and Llama-3.1-8B-Instruct as primary targets, plus Qwen2.5-3B and Llama-3.2-3B for fair comparison with 'Wired for Overconfidence' baselines. We compare against temperature scaling, CCPS, VUF intervention, DINCO, CORAL, Miao & Ungar adaptive steering, monolithic Spherical Steering (without bias decomposition), and monolithic non-linear MLP (without bias decomposition). The primary contributions are: (1) the first joint separability-and-steerability assessment of competing calibration biases, providing specificity ratio measurements that the field currently lacks; (2) interpretable, bias-specific diagnostics revealing which bias source drives miscalibration per-instance AND whether it is correctable; (3) adaptive intervention routing that gracefully degrades from manifold-preserving rotation to non-linear correction to selective abstention based on measured entanglement; and (4) the hypothesis that CSB and CEO have asymmetric steerability profiles, offering a mechanistic explanation for inconsistent monolithic steering results. Phase 1 results constitute an independent contribution regardless of Phase 2-3 outcomes.\",\n  \"project_name\": \"bias_disentangle_calib\",\n  \"source\": \"web_research\",\n  \"revision_notes\": {\n    \"round1_issue_1_missing_competitor\": \"Tsujimura & Tagade (2508.17182) cited as closest methodological precedent, differentiated on four axes (theory-driven vs. post-hoc, calibration vs. assertiveness, 5 models vs. 1, causal intervention vs. descriptive). [Carried from R1]\",\n    \"round1_issue_2_model_names\": \"Fixed model names (Gemma 4 31B Dense, Llama-3.1-8B-Instruct, Qwen3-8B). [Carried from R1]\",\n    \"round1_issue_3_untested_assumption\": \"Phase 1A retains all 5 separability tests with quantitative thresholds. [Carried from R1, now labeled Phase 1A]\",\n    \"round1_issue_4_steering_reliability\": \"Spherical Steering retained as primary Route A intervention; now augmented with Route B non-linear fallback and Route C abstention for when even rotation fails. [Extended from R1]\",\n    \"round1_issue_5_baseline_comparison\": \"Contribution framing around interpretability, difficulty-stratification, and robustness retained. Added monolithic non-linear MLP as new baseline. [Extended from R1]\",\n    \"round1_issue_6_behavioral_mechanistic_leap\": \"Phase 1A tests separability; Phase 1B now ALSO tests steerability. [Extended from R1]\",\n    \"round2_issue_1_critical_missing_competitor\": \"Liu (2605.05715) now thoroughly integrated as a foundational reference rather than treated as merely a competitor. The classification-correction gap is incorporated into the core problem framing, opportunity statement, and landscape. The specificity ratio is adopted as a pre-intervention diagnostic in Phase 1B. The non-linear MLP finding (Δ=+2.8pp) motivates Route B. The selective abstention finding (AUROC 0.610) motivates Route C. We differentiate from Liu by (a) studying calibration biases rather than medical overthinking, (b) testing multiple competing directions rather than a single failure mode, (c) hypothesizing asymmetric steerability profiles, and (d) providing the Confidence Manifold evidence (2602.08159) that calibration-related directions may have more favorable geometry.\",\n    \"round2_issue_2_separability_steerability_gap\": \"Phase 1 now has two explicit sub-phases: 1A (separability, carried from R1) and 1B (steerability, NEW). Phase 1B computes specificity ratio, within-class variance analysis, LEACE concept erasure, and cross-architecture stability for each bias direction. Quantitative thresholds established: ≥0.5 HIGH, 0.2-0.5 MEDIUM, <0.2 LOW. The separability≠steerability distinction is elevated to a core theme of the paper, discussed in the core_problem, opportunity, and approach.\",\n    \"round2_issue_3_minor_missing_references\": \"Selective Steering (Dang & Ngo, 2601.19375) now cited in landscape and used as Route A ablation alternative. COAST (Nguyen et al., 2605.01167) cited in landscape and used for collateral-damage-aware training in Route B. Additionally cited: Confidence Manifold (2602.08159), AUSteer (2602.04428), CLAS (2604.24693) in landscape for completeness.\",\n    \"round2_issue_4_nonlinear_steering_fallback\": \"Route B (learned non-linear residual MLP) added as Phase 3 intervention for low-specificity directions, directly motivated by Liu's finding that a 4096→64→4096 bottleneck achieves Δ=+2.8pp where 29 linear methods fail. Route C (selective abstention) added as ultimate fallback. Route D (conservative hybrid) added for intermediate specificity. This creates a principled four-tier intervention hierarchy that degrades gracefully based on measured entanglement rather than assuming all directions are equally steerable.\"\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b3d318b-89e5-40f8-9295-ad24d1badfd7",
  "isSidechain": false,
  "requestId": "req_011CbByWrJkdKtPS8T1rxXyr",
  "type": "assistant",
  "uuid": "85548d4a-56b8-4138-9e13-49e49c6233b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XfGbKniXRZadHitBnFJZLK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 784,
      "cache_read_input_tokens": 40479,
      "output_tokens": 9087,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 784,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9087,
          "cache_read_input_tokens": 40479,
          "cache_creation_input_tokens": 784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 784
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

_source line 76 · 2026-05-19T13:08:04.790Z_

<details><summary>↩ Tool result · reported error · `toolu_015KwYoPUQmbJQiYx9KFuZnZ`</summary>

```text
Claude requested permissions to write to /tmp/revised_idea_r2.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85548d4a-56b8-4138-9e13-49e49c6233b0",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "3c58f375-f461-4dd6-bb79-028f951fc97a",
  "toolUseResult": "Error: Claude requested permissions to write to /tmp/revised_idea_r2.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "85548d4a-56b8-4138-9e13-49e49c6233b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 77 · 2026-05-19T13:08:04.863Z_

```json
{
  "parentUuid": "3c58f375-f461-4dd6-bb79-028f951fc97a",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ce26aebf-5e90-429e-bfcf-7e867d8b63ad",
  "timestamp": "2026-05-19T13:08:04.863Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 78_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"Disentangling Competing Calibration Biases via Geometry-Aware Activati…",
  "leafUuid": "ce26aebf-5e90-429e-bfcf-7e867d8b63ad",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340"
}
```

---

### Runtime record

_source line 79_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise calibration bias steering with steerability diagnostics",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340"
}
```

---

### Tool call

_source line 80 · 2026-05-19T13:10:57.425Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Cv6c1iLWn1U4Yjb7KRy8D3`</summary>

```json
{
  "file_path": "/tmp/revised_idea_r2.json",
  "content": "{\n  \"title\": \"Disentangling Competing Calibration Biases via Geometry-Aware Activation Steering\",\n  \"change_type\": \"major\",\n  \"core_problem\": \"LLM miscalibration arises from at least two competing biases — choice-supportive bias (inflating confidence in initial answers) and contradictory-evidence overweighting (causing excessive confidence revision under criticism) — that require opposing corrections. Existing calibration methods apply uniform corrections that cannot simultaneously address biases pulling confidence in opposite directions. Recent work (Liu, 2605.05715) further reveals a classification-correction gap: failure-mode directions that are linearly decodable may not be linearly steerable due to entanglement with task-critical computation (specificity ratio ≤0.152). This means even if competing biases can be identified in activations, correcting them requires knowing not just WHICH bias dominates but WHETHER each bias direction is steerable — and routing to appropriate interventions (linear rotation, non-linear correction, or selective abstention) accordingly. Can we jointly diagnose per-instance bias dominance AND steerability to apply targeted, manifold-preserving corrections where possible and graceful degradation where not?\",\n  \"opportunity\": \"Kumaran et al. (Nature Machine Intelligence, 2026; arXiv 2507.03120) identified that LLM miscalibration results from two mechanistically distinct behavioral biases in Gemma 3, GPT-4o, and o1-preview: choice-supportive bias inflates confidence in selected answers, while contradictory-advice overweighting causes models to over-react to opposing evidence. Miao & Ungar (arXiv 2603.25052, 2026) independently showed that calibration and verbalized confidence signals are encoded linearly but orthogonally in the residual stream across three 7-8B models, establishing that confidence-related constructs have accessible geometric structure. Liu (arXiv 2605.05715, May 2026) demonstrated a critical classification-correction gap: linearly decodable failure directions (71.6% balanced accuracy) yield Δ≈0 under 29 steering configurations because the failure directions have 85-88% overlap with task-critical computation (specificity ratio ≤0.152) — but crucially, the paper also shows that (a) a learned non-linear residual MLP achieves Δ=+2.8pp where all linear methods fail, and (b) the decodable signal still supports selective abstention (AUROC 0.610, outperforming 5 uncertainty baselines). The 'Confidence Manifold' study (arXiv 2602.08159) found correctness signals occupy only 3-8 dimensions with simple mean-shift geometry across 9 models, suggesting that for calibration-related directions, the geometric structure may be more favorable than for the medical overthinking phenomenon Liu studied. The convergence of (a) identified competing biases, (b) linear confidence encoding evidence, (c) the decodable-steerable distinction with quantitative diagnostics, and (d) both norm-preserving rotation (Spherical Steering, ICML 2026) and collateral-damage-aware optimization (COAST, 2605.01167) creates an opportunity for a principled pipeline: diagnose bias identity, assess steerability, and route to the appropriate intervention.\",\n  \"landscape\": \"Kumaran et al. (Nature MI, 2026) identified competing biases (CSB and CEO) via behavioral experiments on Gemma 3, GPT-4o, and o1-preview but proposed no correction framework and provided no mechanistic (activation-level) evidence. Miao & Ungar (arXiv 2603.25052, 2026) demonstrated that calibration accuracy and verbalized confidence are linearly encoded but orthogonal in 7-8B models (cosine similarity <0.04 across layers), and introduced adaptive steering achieving 4-7× ECE improvement — but they target the confidence-accuracy misalignment gap, not the competing bias structure. Tsujimura & Tagade (arXiv 2508.17182, Aug 2025) decomposed LLM assertiveness into emotional and logical sub-components via unsupervised clustering on Llama-3.2-1B-Instruct (645 samples), finding two clusters in high-assertive representations — methodologically adjacent but critically different: their decomposition is descriptive (post-hoc ChatGPT-labeled clusters of communication style) rather than causally grounded in identified cognitive biases, uses a single 1B model, reports no calibration metrics, and addresses assertiveness rather than calibration. The 'Wired for Overconfidence' paper (2604.01457, April 2026) identifies overconfidence circuits in Qwen2.5-3B and Llama-3.2-3B, achieving 96.9% ECE reduction on PopQA via monolithic activation steering, but only tests 3B models and treats overconfidence as a single phenomenon. Liu (arXiv 2605.05715, May 2026) is the most directly relevant recent advance: the paper demonstrates a classification-correction gap where linearly decodable failure directions (71.6% balanced accuracy on Llama-3.1-8B) yield Δ≈0 across five families of linear steering (29 configurations) because the failure direction has 85-88% overlap with task-critical computation (specificity ratio ≤0.152). Three convergent evidence lines confirm entanglement: low specificity, shared-direction steering damages accuracy (-12.1pp), and LEACE concept erasure damages accuracy (-3.6pp). Crucially, a learned non-linear bottleneck MLP (4096→64→4096) achieves Δ=+2.8pp (p=0.025) where linear methods fail, though with 8.2% damage rate — demonstrating that partial disentanglement is possible via non-linear transforms. The paper proposes the specificity ratio as a pre-intervention diagnostic and recommends selective abstention (AUROC 0.610) when steering fails. However, this was studied for medical overthinking, a single failure mode; whether calibration biases (CSB/CEO) exhibit similar or different entanglement profiles is an open question. Ji et al. (EMNLP 2025) modulates a single Verbal Uncertainty Feature direction, reducing hallucinations by ~30%, capturing only the net effect of competing biases. Joshi et al. (EMNLP 2025) found a single calibration direction but did not decompose it. CORAL (arXiv 2602.06022, Feb 2026) achieves 49% ECE improvement via correctness-subspace probing on 7B models but uses a single MLP probe direction. The 'Confidence Manifold' study (arXiv 2602.08159, Feb 2026) found correctness signals occupy 3-8 dimensions with simple mean-shift geometry across 9 models from 5 families, and causally validated via steering (10.9pp error rate change) — importantly, the low dimensionality and linear separability of correctness signals contrasts with Liu's high-entanglement finding for overthinking, suggesting calibration-related directions may have more favorable specificity profiles. Wang & Stengel-Eskin (ICLR 2026) introduced DINCO to normalize suggestibility bias via self-generated distractors at the output level. Zhuang et al. (arXiv 2025) proposed RDG to alleviate choice-supportive bias through fine-tuning but did not address CEO. CCPS (arXiv 2025) achieves ~55% ECE reduction via representation stability probing on MMLU. 'Breaking the Mirror' (arXiv 2509.03647) found that self-preference bias 'spans multiple or nonlinear directions,' achieving 97% unjustified bias reduction but with instability on legitimate cases — a direct warning that some biases may not be linearly separable. On the steering methodology side, the landscape has rapidly matured: Spherical Steering (arXiv 2602.08169, ICML 2026) performs norm-preserving geodesic rotation, outperforming addition-based baselines by +10% on TruthfulQA while maintaining generation quality. Selective Steering (Dang & Ngo, arXiv 2601.19375, Jan 2026) independently developed norm-preserving rotation with discriminative layer selection — applying steering only where feature representations exhibit opposite-signed class alignment, achieving 5.5× higher attack success rates with zero perplexity violations across 8 models from 3 families (Llama, Qwen, Gemma). COAST (Nguyen et al., arXiv 2605.01167, May 2026) formalizes collateral damage from steering interventions as unintended alignment changes along non-target feature directions, models steering as a constrained optimization minimizing expected squared collateral change weighted by the empirical second-moment matrix of activations, achieving up to 30% improvement over Angular Steering with strong negative correlation (r<-0.9) between collateral damage and accuracy loss across six benchmarks. AUSteer (arXiv 2602.04428, Feb 2026) decomposes block activations into fine-grained atomic units, steering fewer activations more precisely. CLAS (arXiv 2604.24693, Apr 2026) dynamically adapts steering strengths per-context across 11 benchmarks and 4 model families. 'Steered LLM Activations are Non-Surjective' (2604.09839, April 2026) formally proved that additive steering pushes activations off-manifold; 'A Sober Look at Steering Vectors' (NeurIPS 2024) showed many behaviors are unsteerable. No existing method jointly diagnoses which calibration bias dominates, assesses the steerability of each bias direction (via specificity ratio or equivalent), and routes to bias-specific interventions that range from manifold-preserving rotation to learned non-linear correction to selective abstention — yet the competing effects of CSB and CEO on calibration, combined with the now-established decodable-steerable gap, mean that both uniform correction AND uniform intervention strategy are fundamentally suboptimal.\",\n  \"inspired_by\": \"Gap: Competing biases create non-uniform miscalibration patterns that single-direction methods cannot fix (Kumaran et al. 2026), while the classification-correction gap (Liu, 2605.05715) shows that decodable directions are not necessarily steerable — meaning Phase 1's separability validation is necessary but insufficient. Pattern: Theory-driven contrastive probing (Miao & Ungar 2026) + steerability diagnostics (specificity ratio, Liu 2026) + adaptive intervention routing (geometry-aware rotation for steerable directions, learned non-linear correction for entangled directions). Untried combination: Cognitive-bias-grounded contrastive stimuli → per-instance bias diagnosis → specificity-informed intervention routing (Spherical Steering / non-linear MLP / selective abstention), with the hypothesis that CSB and CEO may have asymmetric steerability profiles — which would explain why monolithic steering sometimes succeeds and sometimes fails at calibration correction.\",\n  \"approach\": \"We design DBS-v2 (Disentangled Bias Steering) in three phases, now incorporating the critical distinction between decodability and steerability identified by Liu (2605.05715).\\n\\n**Phase 1 — Assumption Validation & Steerability Assessment (Weeks 1-5):** This phase tests TWO assumptions, not one: (A) that CSB and CEO produce distinguishable activation signatures, and (B) that identified directions are steerable without catastrophic collateral damage.\\n\\n*Phase 1A — Separability (Weeks 1-3):* We construct two contrastive stimulus sets: for CSB, we compare hidden states when the model reviews its own prior answer vs. a fresh unattributed answer (eliciting choice-supportive inflation); for CEO, we compare states when contradictory expert advice is present vs. absent (eliciting evidence overweighting). Using difference-in-means on these contrastive pairs, we extract candidate bias directions in the residual stream. We validate separability via: (a) cosine similarity between candidate directions, (b) principal angle analysis between CSB and CEO subspaces using the methodology of Miao & Ungar (2026), (c) PCA to assess whether 2 directions capture sufficient variance vs. requiring higher-dimensional subspaces, (d) ICA to test whether statistically independent (not just orthogonal) components emerge, and (e) cross-prediction ablations to confirm removing one bias subspace does not collapse the other. If CSB and CEO directions show cosine similarity >0.3 or shared variance >15%, we activate the separability fallback: extracting a multi-direction bias subspace via SAE-derived features and training a subspace projection classifier.\\n\\n*Phase 1B — Steerability Diagnostics (Weeks 3-5):* This is a critical addition motivated by Liu (2605.05715). Even if CSB and CEO are separable (Phase 1A succeeds), steering along identified directions may fail if those directions are entangled with task-critical computation. For each identified bias direction, we compute: (a) the **specificity ratio** — the proportion of mode-specific variance vs. shared variance with the correct-vs-incorrect subspace, following Liu's shared-specific decomposition methodology. Concretely, we extract the correctness subspace (correct vs. incorrect answer centroids), then decompose each bias direction into a component within this subspace (shared) and a component orthogonal to it (mode-specific). The specificity ratio = ||mode-specific||² / ||total||². (b) **Within-class variance analysis** — comparing within-class variance to inter-centroid gap for each bias direction (Liu's second diagnostic). (c) **LEACE concept erasure test** — applying concept erasure to each bias direction and measuring accuracy damage as causal evidence of entanglement. (d) **Cross-architecture stability** — verifying specificity ratios are consistent across model families.\\n\\nWe establish quantitative thresholds informed by Liu's findings: specificity ratio ≥0.5 → HIGH steerability (linear rotation expected to work); 0.2-0.5 → MEDIUM (rotation may partially work, monitor collateral damage); <0.2 → LOW (linear steering unlikely to succeed, route to non-linear intervention). These thresholds are calibrated against Liu's findings where specificity ≤0.152 yielded Δ≈0 for linear steering while ≥0.999 succeeded for refusal steering. Crucially, we hypothesize that CSB and CEO may have ASYMMETRIC specificity profiles — one may be more steerable than the other — which would provide a mechanistic explanation for why monolithic calibration steering sometimes succeeds partially.\\n\\nPhase 1 results constitute an independent contribution: the first joint separability-and-steerability assessment of behaviorally-identified competing biases, providing the field's first specificity ratio measurements for calibration-related bias directions.\\n\\n**Phase 2 — Per-Instance Bias Diagnosis (Weeks 4-8):** A lightweight logistic probe (or, in the fallback case, a small MLP) trained on per-instance projection magnitudes onto each bias direction classifies which bias dominates for a given query. We stratify by difficulty: on easy questions where models are already confident, CSB likely dominates; on hard questions under criticism, CEO likely dominates. The probe output provides a continuous dominance score. NEW: The Phase 1B steerability assessment informs a per-direction intervention routing table, so the probe's output determines not only which bias is active but which intervention to apply.\\n\\n**Phase 3 — Adaptive Geometry-Aware Intervention (Weeks 6-14):** Instead of a single intervention strategy, Phase 3 now implements an adaptive routing pipeline informed by Phase 1B's steerability diagnostics:\\n\\n*Route A — Spherical Steering (for HIGH-specificity directions):* When a bias direction has specificity ratio ≥0.5, we adopt Spherical Steering (You et al., ICML 2026) as the primary intervention: rotating activations along a geodesic away from the dominant bias direction while preserving activation norms. This addresses the off-manifold concern (Mishra et al., 2604.09839) while the high specificity ensures minimal collateral damage to task-critical computation. A confidence gate modulates rotation magnitude based on the probe's dominance score. We note that Selective Steering (Dang & Ngo, 2601.19375) provides an alternative norm-preserving formulation with discriminative layer selection; we ablate both to determine which is more effective for calibration-specific interventions.\\n\\n*Route B — Learned Non-Linear Residual Correction (for LOW-specificity directions):* When a bias direction has specificity ratio <0.2, linear steering of any kind (additive, rotational, or projected) is expected to fail due to entanglement with task-critical computation (Liu, 2605.05715). Following Liu's finding that a bottleneck residual MLP (d→64→d) achieves Δ=+2.8pp where all 29 linear configurations yield Δ≈0, we train a small non-linear residual adapter per bias type. The adapter takes the hidden state as input and outputs a residual correction, trained via supervision on (biased state, corrected state) pairs extracted from the contrastive dataset. We incorporate the COAST framework (Nguyen et al., 2605.01167) by weighting the training loss by the empirical second-moment matrix to minimize expected collateral damage along non-target feature directions. The adapter's bottleneck architecture (d→64→d, <0.1% of model parameters) keeps the intervention lightweight and inference-efficient.\\n\\n*Route C — Selective Abstention (for UNSTEERABLE directions):* When Phase 1B indicates low specificity AND Phase 3 ablations confirm that neither Route A nor Route B improves calibration without excessive damage (>5% accuracy degradation), we leverage the decodable signal for selective abstention: the bias probe flags instances where the dominant bias has high activation but low steerability, outputting a reliability score. Following Liu's demonstration that decodable signals support post-generation reliability estimation (AUROC 0.610) even when correction fails, this provides a graceful degradation path.\\n\\n*Route D — Medium-Specificity Hybrid (for intermediate cases):* For directions with specificity 0.2-0.5, we apply Spherical Steering with conservative rotation magnitude (capped at 50% of the high-specificity coefficient) and monitor collateral damage via the COAST second-moment diagnostic. If per-instance collateral damage exceeds a threshold, we fall back to Route B for that instance.\\n\\nWe evaluate on TriviaQA, MMLU, PopQA, and NQ-Open across Gemma 4 31B (Dense), Qwen3-8B, and Llama-3.1-8B-Instruct. We additionally include Qwen2.5-3B and Llama-3.2-3B as supplementary models to enable fair comparison with 'Wired for Overconfidence' results at the same scale. Metrics: ECE, Brier score, AUROC, difficulty-stratified ECE (easy/medium/hard partitions), AND NEW: per-direction specificity ratios, collateral damage measurements (accuracy on non-target tasks before/after steering), and route-distribution analysis (what fraction of instances are routed to each intervention). Baselines: temperature scaling, CCPS, VUF intervention, DINCO, CORAL, Miao & Ungar adaptive steering, monolithic circuit ablation (Wired for Overconfidence replication at 3B scale), monolithic Spherical Steering (single direction, no bias decomposition), and NEW: monolithic non-linear residual MLP (single direction, no bias decomposition) to isolate the contribution of bias decomposition from the contribution of non-linear correction.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"750-1050 H100\",\n      \"timeline\": \"16-20 weeks\",\n      \"estimated_gpu_cost\": \"$1,875-$2,625 (H100 @ ~$2.50/hr mid-tier provider)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"650-900 H100\",\n      \"timeline\": \"12-15 weeks\",\n      \"claude_api_cost\": \"$350-$600 (Sonnet 4.6 for contrastive dataset generation, probing code, specificity ratio computation scripts, non-linear adapter training, analysis)\",\n      \"estimated_gpu_cost\": \"$1,625-$2,250\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"1000-1400 H100\",\n      \"timeline\": \"6-10 weeks\",\n      \"claude_api_cost\": \"$800-$1,400 (Opus 4.7 for experiment orchestration, assumption validation analysis, steerability diagnostics, adapter training sweeps, ablation design)\",\n      \"estimated_gpu_cost\": \"$2,500-$3,500\",\n      \"speed_bottleneck\": \"Phase 1A→1B is inherently sequential (separability must be established before steerability diagnostics are meaningful). Phase 1B requires extracting the correctness subspace and computing specificity ratios per-direction per-model, which is parallelizable across models but adds ~2 weeks over original timeline. Route B adapter training requires supervision pairs from Phase 1 contrastive data. Steering coefficient search across 5 models × 4 datasets × 3-4 intervention routes generates large evaluation matrices. Fair replication of 'Wired for Overconfidence' baselines on 3B models adds overhead.\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — primary target, tight but feasible with aggressive Phase 1 timeline)\",\n    \"ARR August 2026 cycle (Aug 3, 2026 — targets EMNLP 2027 or future *CL venues)\",\n    \"NeurIPS 2026 Workshops (~Aug 29, 2026 — workshop paper track for Phase 1 separability + steerability results)\",\n    \"AACL-IJCNLP 2026 (ARR May 25 commitment deadline Aug 26, 2026 — if Phase 1 completes early)\",\n    \"ICLR 2027 (expected Oct 2026 deadline — full paper with all phases and routes complete)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Competing Biases underlie Overconfidence and Underconfidence in LLMs (Kumaran et al., Nature Machine Intelligence 2026; arXiv 2507.03120)\",\n    \"Closing the Confidence-Faithfulness Gap in Large Language Models (Miao & Ungar, arXiv 2603.25052, 2026) — orthogonal calibration/confidence encoding, adaptive steering\",\n    \"LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components (Tsujimura & Tagade, arXiv 2508.17182, 2025) — closest methodological precedent\",\n    \"Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes (Liu, arXiv 2605.05715, May 2026) — classification-correction gap, specificity ratio diagnostic\",\n    \"Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs (arXiv 2604.01457, 2026)\",\n    \"Spherical Steering: Geometry-Aware Activation Rotation for Language Models (You et al., ICML 2026; arXiv 2602.08169)\",\n    \"Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection (Dang & Ngo, arXiv 2601.19375, Jan 2026) — independent norm-preserving rotation with discriminative layer selection\",\n    \"Minimizing Collateral Damage in Activation Steering (Nguyen et al., arXiv 2605.01167, May 2026) — COAST framework, collateral damage formalization, second-moment optimization\",\n    \"Steered LLM Activations are Non-Surjective (Mishra et al., arXiv 2604.09839, 2026)\",\n    \"A Sober Look at Steering Vectors for LLMs (Tan et al., NeurIPS 2024)\",\n    \"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models (arXiv 2602.08159, 2026) — 3-8 dimensional correctness signals, linear separability across 9 models\",\n    \"Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators (arXiv 2509.03647, 2025) — nonlinear bias warning\",\n    \"CORAL: Correctness-Optimized Residual Activation Lens (arXiv 2602.06022, 2026) — calibration-aware steering baseline\",\n    \"Mind the Confidence Gap: Overconfidence, Calibration, and Distractor Effects in Large Language Models (Chhikara, TMLR 2025)\",\n    \"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025)\",\n    \"Calibrating Verbalized Confidence with Self-Generated Distractors (Wang & Stengel-Eskin, ICLR 2026)\",\n    \"Calibration Across Layers: Understanding Calibration Evolution in LLMs (Joshi et al., EMNLP 2025)\",\n    \"Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation (Zhuang et al., arXiv 2512.03082, 2025)\",\n    \"Calibrating LLM Confidence by Probing Perturbed Representation Stability (arXiv 2505.21772, 2025)\",\n    \"Know When You're Wrong: Aligning Confidence with Correctness for LLM Error Detection (arXiv 2603.06604, 2026)\",\n    \"Fine-Grained Activation Steering: Steering Less, Achieving More (arXiv 2602.04428, 2026) — atomic-unit-level steering\",\n    \"Contextual Linear Activation Steering of Language Models (arXiv 2604.24693, 2026) — context-adaptive steering strengths\"\n  ],\n  \"description\": \"We propose DBS-v2 (Disentangled Bias Steering), a method that separately identifies, assesses the steerability of, and adaptively corrects two competing sources of LLM miscalibration identified by Kumaran et al. (2026): choice-supportive bias (CSB, inflating confidence in selected answers) and contradictory-evidence overweighting (CEO, causing excessive confidence revision under criticism). Unlike Tsujimura & Tagade (2025), who descriptively decomposed assertiveness into emotion/logic clusters via unsupervised methods on a 1B model without calibration evaluation, DBS-v2 is grounded in causally-identified cognitive biases with theory-driven contrastive stimuli and directly targets calibration metrics.\\n\\nA critical insight motivating this revision is the classification-correction gap demonstrated by Liu (2605.05715): linearly decodable failure directions (71.6% balanced accuracy) can yield Δ≈0 under steering because they overlap 85-88% with task-critical computation. This means that separability (Phase 1A) is necessary but insufficient — we must also assess steerability before committing to an intervention strategy.\\n\\nThe method proceeds in three phases. Phase 1A (Separability Validation) tests whether CSB and CEO produce distinguishable activation signatures using contrastive activation probing, validated via cosine similarity, principal angle analysis, PCA/ICA dimensionality assessment, and cross-prediction ablation (following Miao & Ungar, 2026). Phase 1B (Steerability Assessment) — the key new addition — computes the specificity ratio (mode-specific vs. shared variance with the correct/incorrect subspace) for each identified bias direction, following Liu's shared-specific decomposition methodology. This diagnostic distinguishes between directions that are decodable-and-steerable vs. decodable-but-entangled. We hypothesize that CSB and CEO may have asymmetric specificity profiles, which would explain why monolithic calibration steering yields inconsistent results across settings. The Confidence Manifold study (2602.08159) provides encouraging evidence that correctness-related signals occupy only 3-8 dimensions with simple mean-shift geometry, suggesting calibration-related directions may have more favorable specificity than the medical overthinking phenomenon Liu studied.\\n\\nPhase 2 trains a lightweight per-instance bias dominance classifier whose output determines both which bias is active and which intervention route to apply. Phase 3 implements adaptive routing: (Route A) Spherical Steering for high-specificity directions (≥0.5), with Selective Steering (Dang & Ngo, 2601.19375) as an ablation alternative providing discriminative layer selection; (Route B) a learned non-linear bottleneck residual MLP (d→64→d) for low-specificity directions (<0.2), trained with COAST-informed (Nguyen et al., 2605.01167) collateral-damage-aware loss weighting; (Route C) selective abstention leveraging the decodable signal for reliability estimation when neither linear nor non-linear correction is safe; and (Route D) conservative hybrid steering for intermediate specificity (0.2-0.5).\\n\\nWe evaluate on TriviaQA, MMLU, PopQA, and NQ-Open across five models: Gemma 4 31B (Dense), Qwen3-8B, and Llama-3.1-8B-Instruct as primary targets, plus Qwen2.5-3B and Llama-3.2-3B for fair comparison with 'Wired for Overconfidence' baselines. We compare against temperature scaling, CCPS, VUF intervention, DINCO, CORAL, Miao & Ungar adaptive steering, monolithic Spherical Steering (without bias decomposition), and monolithic non-linear MLP (without bias decomposition). The primary contributions are: (1) the first joint separability-and-steerability assessment of competing calibration biases, providing specificity ratio measurements that the field currently lacks; (2) interpretable, bias-specific diagnostics revealing which bias source drives miscalibration per-instance AND whether it is correctable; (3) adaptive intervention routing that gracefully degrades from manifold-preserving rotation to non-linear correction to selective abstention based on measured entanglement; and (4) the hypothesis that CSB and CEO have asymmetric steerability profiles, offering a mechanistic explanation for inconsistent monolithic steering results. Phase 1 results constitute an independent contribution regardless of Phase 2-3 outcomes.\",\n  \"project_name\": \"bias_disentangle_calib\",\n  \"source\": \"web_research\",\n  \"revision_notes\": {\n    \"round1_issue_1_missing_competitor\": \"Tsujimura & Tagade (2508.17182) cited as closest methodological precedent, differentiated on four axes (theory-driven vs. post-hoc, calibration vs. assertiveness, 5 models vs. 1, causal intervention vs. descriptive). [Carried from R1]\",\n    \"round1_issue_2_model_names\": \"Fixed model names (Gemma 4 31B Dense, Llama-3.1-8B-Instruct, Qwen3-8B). [Carried from R1]\",\n    \"round1_issue_3_untested_assumption\": \"Phase 1A retains all 5 separability tests with quantitative thresholds. [Carried from R1, now labeled Phase 1A]\",\n    \"round1_issue_4_steering_reliability\": \"Spherical Steering retained as primary Route A intervention; now augmented with Route B non-linear fallback and Route C abstention for when even rotation fails. [Extended from R1]\",\n    \"round1_issue_5_baseline_comparison\": \"Contribution framing around interpretability, difficulty-stratification, and robustness retained. Added monolithic non-linear MLP as new baseline. [Extended from R1]\",\n    \"round1_issue_6_behavioral_mechanistic_leap\": \"Phase 1A tests separability; Phase 1B now ALSO tests steerability. [Extended from R1]\",\n    \"round2_issue_1_critical_missing_competitor\": \"Liu (2605.05715) now thoroughly integrated as a foundational reference rather than treated as merely a competitor. The classification-correction gap is incorporated into the core problem framing, opportunity statement, and landscape. The specificity ratio is adopted as a pre-intervention diagnostic in Phase 1B. The non-linear MLP finding (Δ=+2.8pp) motivates Route B. The selective abstention finding (AUROC 0.610) motivates Route C. We differentiate from Liu by (a) studying calibration biases rather than medical overthinking, (b) testing multiple competing directions rather than a single failure mode, (c) hypothesizing asymmetric steerability profiles, and (d) providing the Confidence Manifold evidence (2602.08159) that calibration-related directions may have more favorable geometry.\",\n    \"round2_issue_2_separability_steerability_gap\": \"Phase 1 now has two explicit sub-phases: 1A (separability, carried from R1) and 1B (steerability, NEW). Phase 1B computes specificity ratio, within-class variance analysis, LEACE concept erasure, and cross-architecture stability for each bias direction. Quantitative thresholds established: ≥0.5 HIGH, 0.2-0.5 MEDIUM, <0.2 LOW. The separability≠steerability distinction is elevated to a core theme of the paper, discussed in the core_problem, opportunity, and approach.\",\n    \"round2_issue_3_minor_missing_references\": \"Selective Steering (Dang & Ngo, 2601.19375) now cited in landscape and used as Route A ablation alternative. COAST (Nguyen et al., 2605.01167) cited in landscape and used for collateral-damage-aware training in Route B. Additionally cited: Confidence Manifold (2602.08159), AUSteer (2602.04428), CLAS (2604.24693) in landscape for completeness.\",\n    \"round2_issue_4_nonlinear_steering_fallback\": \"Route B (learned non-linear residual MLP) added as Phase 3 intervention for low-specificity directions, directly motivated by Liu's finding that a 4096→64→4096 bottleneck achieves Δ=+2.8pp where 29 linear methods fail. Route C (selective abstention) added as ultimate fallback. Route D (conservative hybrid) added for intermediate specificity. This creates a principled four-tier intervention hierarchy that degrades gracefully based on measured entanglement rather than assuming all directions are equally steerable.\"\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce26aebf-5e90-429e-bfcf-7e867d8b63ad",
  "isSidechain": false,
  "requestId": "req_011CbBynAu7mvbmooEZCKGss",
  "type": "assistant",
  "uuid": "86e60690-8bc0-459a-941e-a2052f9b17cb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SuBCyYTZiUX1GinGHcAJnS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9228,
      "cache_read_input_tokens": 41263,
      "output_tokens": 8532,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9228,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8532,
          "cache_read_input_tokens": 41263,
          "cache_creation_input_tokens": 9228,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9228
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

_source line 81 · 2026-05-19T13:10:57.431Z_

<details><summary>↩ Tool result · reported error · `toolu_01Cv6c1iLWn1U4Yjb7KRy8D3`</summary>

```text
Claude requested permissions to write to /tmp/revised_idea_r2.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86e60690-8bc0-459a-941e-a2052f9b17cb",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "e6d94068-85bc-4f5d-87f9-d62809a8d401",
  "toolUseResult": "Error: Claude requested permissions to write to /tmp/revised_idea_r2.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "86e60690-8bc0-459a-941e-a2052f9b17cb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 82_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"Disentangling Competing Calibration Biases via Geometry-Aware Activati…",
  "leafUuid": "e6d94068-85bc-4f5d-87f9-d62809a8d401",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340"
}
```

---

### Runtime record

_source line 83_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise calibration bias steering with steerability diagnostics",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340"
}
```

---

### Tool call

_source line 84 · 2026-05-19T13:11:00.689Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Fk8S3ecVoEn2cHNL452ULU`</summary>

```json
{
  "command": "echo \"ready\"",
  "description": "Test shell access"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6d94068-85bc-4f5d-87f9-d62809a8d401",
  "isSidechain": false,
  "requestId": "req_011CbByzpAoKmwBwVxfE28KD",
  "type": "assistant",
  "uuid": "2d925e07-d0de-4493-bfee-3e4dbad00fb0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Tnzrw4gpZm73H4XKsrTDw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8577,
      "cache_read_input_tokens": 50491,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8577,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 50491,
          "cache_creation_input_tokens": 8577,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8577
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

_source line 85 · 2026-05-19T13:11:00.845Z_

<details><summary>↩ Tool result · `toolu_01Fk8S3ecVoEn2cHNL452ULU`</summary>

```text
ready
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d925e07-d0de-4493-bfee-3e4dbad00fb0",
  "isSidechain": false,
  "promptId": "972ef96b-c48f-4d58-9168-768f94b90152",
  "type": "user",
  "uuid": "05fedddc-ec7a-487e-86bc-2ad37455d8af",
  "toolUseResult": {
    "stdout": "ready",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "2d925e07-d0de-4493-bfee-3e4dbad00fb0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 86 · 2026-05-19T13:14:06.373Z_

Here is the complete revised research idea JSON:

```json
{
  "title": "Disentangling Competing Calibration Biases via Geometry-Aware Activation Steering",
  "change_type": "major",
  "core_problem": "LLM miscalibration arises from at least two competing biases — choice-supportive bias (inflating confidence in initial answers) and contradictory-evidence overweighting (causing excessive confidence revision under criticism) — that require opposing corrections. Existing calibration methods apply uniform corrections that cannot simultaneously address biases pulling confidence in opposite directions. Recent work (Liu, 2605.05715) further reveals a classification-correction gap: failure-mode directions that are linearly decodable may not be linearly steerable due to entanglement with task-critical computation (specificity ratio ≤0.152). This means even if competing biases can be identified in activations, correcting them requires knowing not just WHICH bias dominates but WHETHER each bias direction is steerable — and routing to appropriate interventions (linear rotation, non-linear correction, or selective abstention) accordingly. Can we jointly diagnose per-instance bias dominance AND steerability to apply targeted, manifold-preserving corrections where possible and graceful degradation where not?",
  "opportunity": "Kumaran et al. (Nature Machine Intelligence, 2026; arXiv 2507.03120) identified that LLM miscalibration results from two mechanistically distinct behavioral biases in Gemma 3, GPT-4o, and o1-preview: choice-supportive bias inflates confidence in selected answers, while contradictory-advice overweighting causes models to over-react to opposing evidence. Miao & Ungar (arXiv 2603.25052, 2026) independently showed that calibration and verbalized confidence signals are encoded linearly but orthogonally in the residual stream across three 7-8B models, establishing that confidence-related constructs have accessible geometric structure. Liu (arXiv 2605.05715, May 2026) demonstrated a critical classification-correction gap: linearly decodable failure directions (71.6% balanced accuracy) yield Δ≈0 under 29 steering configurations because the failure directions have 85-88% overlap with task-critical computation (specificity ratio ≤0.152) — but crucially, the paper also shows that (a) a learned non-linear residual MLP achieves Δ=+2.8pp where all linear methods fail, and (b) the decodable signal still supports selective abstention (AUROC 0.610, outperforming 5 uncertainty baselines). The 'Confidence Manifold' study (arXiv 2602.08159) found correctness signals occupy only 3-8 dimensions with simple mean-shift geometry across 9 models, suggesting that for calibration-related directions, the geometric structure may be more favorable than for the medical overthinking phenomenon Liu studied. The convergence of (a) identified competing biases, (b) linear confidence encoding evidence, (c) the decodable-steerable distinction with quantitative diagnostics, and (d) both norm-preserving rotation (Spherical Steering, ICML 2026) and collateral-damage-aware optimization (COAST, 2605.01167) creates an opportunity for a principled pipeline: diagnose bias identity, assess steerability, and route to the appropriate intervention.",
  "landscape": "Kumaran et al. (Nature MI, 2026) identified competing biases (CSB and CEO) via behavioral experiments on Gemma 3, GPT-4o, and o1-preview but proposed no correction framework and provided no mechanistic (activation-level) evidence. Miao & Ungar (arXiv 2603.25052, 2026) demonstrated that calibration accuracy and verbalized confidence are linearly encoded but orthogonal in 7-8B models (cosine similarity <0.04 across layers), and introduced adaptive steering achieving 4-7× ECE improvement — but they target the confidence-accuracy misalignment gap, not the competing bias structure. Tsujimura & Tagade (arXiv 2508.17182, Aug 2025) decomposed LLM assertiveness into emotional and logical sub-components via unsupervised clustering on Llama-3.2-1B-Instruct (645 samples), finding two clusters in high-assertive representations — methodologically adjacent but critically different: their decomposition is descriptive (post-hoc ChatGPT-labeled clusters of communication style) rather than causally grounded in identified cognitive biases, uses a single 1B model, reports no calibration metrics, and addresses assertiveness rather than calibration. The 'Wired for Overconfidence' paper (2604.01457, April 2026) identifies overconfidence circuits in Qwen2.5-3B and Llama-3.2-3B, achieving 96.9% ECE reduction on PopQA via monolithic activation steering, but only tests 3B models and treats overconfidence as a single phenomenon. Liu (arXiv 2605.05715, May 2026) is the most directly relevant recent advance: the paper demonstrates a classification-correction gap where linearly decodable failure directions (71.6% balanced accuracy on Llama-3.1-8B) yield Δ≈0 across five families of linear steering (29 configurations) because the failure direction has 85-88% overlap with task-critical computation (specificity ratio ≤0.152). Three convergent evidence lines confirm entanglement: low specificity, shared-direction steering damages accuracy (-12.1pp), and LEACE concept erasure damages accuracy (-3.6pp). Crucially, a learned non-linear bottleneck MLP (4096→64→4096) achieves Δ=+2.8pp (p=0.025) where linear methods fail, though with 8.2% damage rate — demonstrating that partial disentanglement is possible via non-linear transforms. The paper proposes the specificity ratio as a pre-intervention diagnostic and recommends selective abstention (AUROC 0.610) when steering fails. However, this was studied for medical overthinking, a single failure mode; whether calibration biases (CSB/CEO) exhibit similar or different entanglement profiles is an open question. Ji et al. (EMNLP 2025) modulates a single Verbal Uncertainty Feature direction, reducing hallucinations by ~30%, capturing only the net effect of competing biases. Joshi et al. (EMNLP 2025) found a single calibration direction but did not decompose it. CORAL (arXiv 2602.06022, Feb 2026) achieves 49% ECE improvement via correctness-subspace probing on 7B models but uses a single MLP probe direction. The 'Confidence Manifold' study (arXiv 2602.08159, Feb 2026) found correctness signals occupy 3-8 dimensions with simple mean-shift geometry across 9 models from 5 families, and causally validated via steering (10.9pp error rate change) — importantly, the low dimensionality and linear separability of correctness signals contrasts with Liu's high-entanglement finding for overthinking, suggesting calibration-related directions may have more favorable specificity profiles. Wang & Stengel-Eskin (ICLR 2026) introduced DINCO to normalize suggestibility bias via self-generated distractors at the output level. Zhuang et al. (arXiv 2025) proposed RDG to alleviate choice-supportive bias through fine-tuning but did not address CEO. CCPS (arXiv 2025) achieves ~55% ECE reduction via representation stability probing on MMLU. 'Breaking the Mirror' (arXiv 2509.03647) found that self-preference bias 'spans multiple or nonlinear directions,' achieving 97% unjustified bias reduction but with instability on legitimate cases — a direct warning that some biases may not be linearly separable. On the steering methodology side, the landscape has rapidly matured: Spherical Steering (arXiv 2602.08169, ICML 2026) performs norm-preserving geodesic rotation, outperforming addition-based baselines by +10% on TruthfulQA while maintaining generation quality. Selective Steering (Dang & Ngo, arXiv 2601.19375, Jan 2026) independently developed norm-preserving rotation with discriminative layer selection — applying steering only where feature representations exhibit opposite-signed class alignment, achieving 5.5× higher attack success rates with zero perplexity violations across 8 models from 3 families (Llama, Qwen, Gemma). COAST (Nguyen et al., arXiv 2605.01167, May 2026) formalizes collateral damage from steering interventions as unintended alignment changes along non-target feature directions, models steering as a constrained optimization minimizing expected squared collateral change weighted by the empirical second-moment matrix of activations, achieving up to 30% improvement over Angular Steering with strong negative correlation (r<-0.9) between collateral damage and accuracy loss across six benchmarks. AUSteer (arXiv 2602.04428, Feb 2026) decomposes block activations into fine-grained atomic units, steering fewer activations more precisely. CLAS (arXiv 2604.24693, Apr 2026) dynamically adapts steering strengths per-context across 11 benchmarks and 4 model families. 'Steered LLM Activations are Non-Surjective' (2604.09839, April 2026) formally proved that additive steering pushes activations off-manifold; 'A Sober Look at Steering Vectors' (NeurIPS 2024) showed many behaviors are unsteerable. No existing method jointly diagnoses which calibration bias dominates, assesses the steerability of each bias direction (via specificity ratio or equivalent), and routes to bias-specific interventions that range from manifold-preserving rotation to learned non-linear correction to selective abstention — yet the competing effects of CSB and CEO on calibration, combined with the now-established decodable-steerable gap, mean that both uniform correction AND uniform intervention strategy are fundamentally suboptimal.",
  "inspired_by": "Gap: Competing biases create non-uniform miscalibration patterns that single-direction methods cannot fix (Kumaran et al. 2026), while the classification-correction gap (Liu, 2605.05715) shows that decodable directions are not necessarily steerable — meaning Phase 1's separability validation is necessary but insufficient. Pattern: Theory-driven contrastive probing (Miao & Ungar 2026) + steerability diagnostics (specificity ratio, Liu 2026) + adaptive intervention routing (geometry-aware rotation for steerable directions, learned non-linear correction for entangled directions). Untried combination: Cognitive-bias-grounded contrastive stimuli → per-instance bias diagnosis → specificity-informed intervention routing (Spherical Steering / non-linear MLP / selective abstention), with the hypothesis that CSB and CEO may have asymmetric steerability profiles — which would explain why monolithic steering sometimes succeeds and sometimes fails at calibration correction.",
  "approach": "We design DBS-v2 (Disentangled Bias Steering) in three phases, now incorporating the critical distinction between decodability and steerability identified by Liu (2605.05715).\n\n**Phase 1 — Assumption Validation & Steerability Assessment (Weeks 1-5):** This phase tests TWO assumptions, not one: (A) that CSB and CEO produce distinguishable activation signatures, and (B) that identified directions are steerable without catastrophic collateral damage.\n\n*Phase 1A — Separability (Weeks 1-3):* We construct two contrastive stimulus sets: for CSB, we compare hidden states when the model reviews its own prior answer vs. a fresh unattributed answer (eliciting choice-supportive inflation); for CEO, we compare states when contradictory expert advice is present vs. absent (eliciting evidence overweighting). Using difference-in-means on these contrastive pairs, we extract candidate bias directions in the residual stream. We validate separability via: (a) cosine similarity between candidate directions, (b) principal angle analysis between CSB and CEO subspaces using the methodology of Miao & Ungar (2026), (c) PCA to assess whether 2 directions capture sufficient variance vs. requiring higher-dimensional subspaces, (d) ICA to test whether statistically independent (not just orthogonal) components emerge, and (e) cross-prediction ablations to confirm removing one bias subspace does not collapse the other. If CSB and CEO directions show cosine similarity >0.3 or shared variance >15%, we activate the separability fallback: extracting a multi-direction bias subspace via SAE-derived features and training a subspace projection classifier.\n\n*Phase 1B — Steerability Diagnostics (Weeks 3-5):* This is a critical addition motivated by Liu (2605.05715). Even if CSB and CEO are separable (Phase 1A succeeds), steering along identified directions may fail if those directions are entangled with task-critical computation. For each identified bias direction, we compute: (a) the **specificity ratio** — the proportion of mode-specific variance vs. shared variance with the correct-vs-incorrect subspace, following Liu's shared-specific decomposition methodology. Concretely, we extract the correctness subspace (correct vs. incorrect answer centroids), then decompose each bias direction into a component within this subspace (shared) and a component orthogonal to it (mode-specific). The specificity ratio = ||mode-specific||² / ||total||². (b) **Within-class variance analysis** — comparing within-class variance to inter-centroid gap for each bias direction (Liu's second diagnostic). (c) **LEACE concept erasure test** — applying concept erasure to each bias direction and measuring accuracy damage as causal evidence of entanglement. (d) **Cross-architecture stability** — verifying specificity ratios are consistent across model families.\n\nWe establish quantitative thresholds informed by Liu's findings: specificity ratio ≥0.5 → HIGH steerability (linear rotation expected to work); 0.2-0.5 → MEDIUM (rotation may partially work, monitor collateral damage); <0.2 → LOW (linear steering unlikely to succeed, route to non-linear intervention). These thresholds are calibrated against Liu's findings where specificity ≤0.152 yielded Δ≈0 for linear steering while ≥0.999 succeeded for refusal steering. Crucially, we hypothesize that CSB and CEO may have ASYMMETRIC specificity profiles — one may be more steerable than the other — which would provide a mechanistic explanation for why monolithic calibration steering sometimes succeeds partially.\n\nPhase 1 results constitute an independent contribution: the first joint separability-and-steerability assessment of behaviorally-identified competing biases, providing the field's first specificity ratio measurements for calibration-related bias directions.\n\n**Phase 2 — Per-Instance Bias Diagnosis (Weeks 4-8):** A lightweight logistic probe (or, in the fallback case, a small MLP) trained on per-instance projection magnitudes onto each bias direction classifies which bias dominates for a given query. We stratify by difficulty: on easy questions where models are already confident, CSB likely dominates; on hard questions under criticism, CEO likely dominates. The probe output provides a continuous dominance score. NEW: The Phase 1B steerability assessment informs a per-direction intervention routing table, so the probe's output determines not only which bias is active but which intervention to apply.\n\n**Phase 3 — Adaptive Geometry-Aware Intervention (Weeks 6-14):** Instead of a single intervention strategy, Phase 3 now implements an adaptive routing pipeline informed by Phase 1B's steerability diagnostics:\n\n*Route A — Spherical Steering (for HIGH-specificity directions):* When a bias direction has specificity ratio ≥0.5, we adopt Spherical Steering (You et al., ICML 2026) as the primary intervention: rotating activations along a geodesic away from the dominant bias direction while preserving activation norms. This addresses the off-manifold concern (Mishra et al., 2604.09839) while the high specificity ensures minimal collateral damage to task-critical computation. A confidence gate modulates rotation magnitude based on the probe's dominance score. We note that Selective Steering (Dang & Ngo, 2601.19375) provides an alternative norm-preserving formulation with discriminative layer selection; we ablate both to determine which is more effective for calibration-specific interventions.\n\n*Route B — Learned Non-Linear Residual Correction (for LOW-specificity directions):* When a bias direction has specificity ratio <0.2, linear steering of any kind (additive, rotational, or projected) is expected to fail due to entanglement with task-critical computation (Liu, 2605.05715). Following Liu's finding that a bottleneck residual MLP (d→64→d) achieves Δ=+2.8pp where all 29 linear configurations yield Δ≈0, we train a small non-linear residual adapter per bias type. The adapter takes the hidden state as input and outputs a residual correction, trained via supervision on (biased state, corrected state) pairs extracted from the contrastive dataset. We incorporate the COAST framework (Nguyen et al., 2605.01167) by weighting the training loss by the empirical second-moment matrix to minimize expected collateral damage along non-target feature directions. The adapter's bottleneck architecture (d→64→d, <0.1% of model parameters) keeps the intervention lightweight and inference-efficient.\n\n*Route C — Selective Abstention (for UNSTEERABLE directions):* When Phase 1B indicates low specificity AND Phase 3 ablations confirm that neither Route A nor Route B improves calibration without excessive damage (>5% accuracy degradation), we leverage the decodable signal for selective abstention: the bias probe flags instances where the dominant bias has high activation but low steerability, outputting a reliability score. Following Liu's demonstration that decodable signals support post-generation reliability estimation (AUROC 0.610) even when correction fails, this provides a graceful degradation path.\n\n*Route D — Medium-Specificity Hybrid (for intermediate cases):* For directions with specificity 0.2-0.5, we apply Spherical Steering with conservative rotation magnitude (capped at 50% of the high-specificity coefficient) and monitor collateral damage via the COAST second-moment diagnostic. If per-instance collateral damage exceeds a threshold, we fall back to Route B for that instance.\n\nWe evaluate on TriviaQA, MMLU, PopQA, and NQ-Open across Gemma 4 31B (Dense), Qwen3-8B, and Llama-3.1-8B-Instruct. We additionally include Qwen2.5-3B and Llama-3.2-3B as supplementary models to enable fair comparison with 'Wired for Overconfidence' results at the same scale. Metrics: ECE, Brier score, AUROC, difficulty-stratified ECE (easy/medium/hard partitions), AND NEW: per-direction specificity ratios, collateral damage measurements (accuracy on non-target tasks before/after steering), and route-distribution analysis (what fraction of instances are routed to each intervention). Baselines: temperature scaling, CCPS, VUF intervention, DINCO, CORAL, Miao & Ungar adaptive steering, monolithic circuit ablation (Wired for Overconfidence replication at 3B scale), monolithic Spherical Steering (single direction, no bias decomposition), and NEW: monolithic non-linear residual MLP (single direction, no bias decomposition) to isolate the contribution of bias decomposition from the contribution of non-linear correction.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "750-1050 H100",
      "timeline": "16-20 weeks",
      "estimated_gpu_cost": "$1,875-$2,625 (H100 @ ~$2.50/hr mid-tier provider)"
    },
    "human_in_loop": {
      "gpu_hours": "650-900 H100",
      "timeline": "12-15 weeks",
      "claude_api_cost": "$350-$600 (Sonnet 4.6 for contrastive dataset generation, probing code, specificity ratio computation scripts, non-linear adapter training, analysis)",
      "estimated_gpu_cost": "$1,625-$2,250"
    },
    "auto_research": {
      "gpu_hours": "1000-1400 H100",
      "timeline": "6-10 weeks",
      "claude_api_cost": "$800-$1,400 (Opus 4.7 for experiment orchestration, assumption validation analysis, steerability diagnostics, adapter training sweeps, ablation design)",
      "estimated_gpu_cost": "$2,500-$3,500",
      "speed_bottleneck": "Phase 1A→1B is inherently sequential (separability must be established before steerability diagnostics are meaningful). Phase 1B requires extracting the correctness subspace and computing specificity ratios per-direction per-model, which is parallelizable across models but adds ~2 weeks over original timeline. Route B adapter training requires supervision pairs from Phase 1 contrastive data. Steering coefficient search across 5 models × 4 datasets × 3-4 intervention routes generates large evaluation matrices. Fair replication of 'Wired for Overconfidence' baselines on 3B models adds overhead."
    }
  },
  "target_venues": [
    "AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — primary target, tight but feasible with aggressive Phase 1 timeline)",
    "ARR August 2026 cycle (Aug 3, 2026 — targets EMNLP 2027 or future *CL venues)",
    "NeurIPS 2026 Workshops (~Aug 29, 2026 — workshop paper track for Phase 1 separability + steerability results)",
    "AACL-IJCNLP 2026 (ARR May 25 commitment deadline Aug 26, 2026 — if Phase 1 completes early)",
    "ICLR 2027 (expected Oct 2026 deadline — full paper with all phases and routes complete)"
  ],
  "level": "top-tier",
  "key_references": [
    "Competing Biases underlie Overconfidence and Underconfidence in LLMs (Kumaran et al., Nature Machine Intelligence 2026; arXiv 2507.03120)",
    "Closing the Confidence-Faithfulness Gap in Large Language Models (Miao & Ungar, arXiv 2603.25052, 2026) — orthogonal calibration/confidence encoding, adaptive steering",
    "LLM Assertiveness can be Mechanistically Decomposed into Emotional and Logical Components (Tsujimura & Tagade, arXiv 2508.17182, 2025) — closest methodological precedent",
    "Decodable but Not Corrected by Fixed Residual-Stream Linear Steering: Evidence from Medical LLM Failure Regimes (Liu, arXiv 2605.05715, May 2026) — classification-correction gap, specificity ratio diagnostic",
    "Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs (arXiv 2604.01457, 2026)",
    "Spherical Steering: Geometry-Aware Activation Rotation for Language Models (You et al., ICML 2026; arXiv 2602.08169)",
    "Selective Steering: Norm-Preserving Control Through Discriminative Layer Selection (Dang & Ngo, arXiv 2601.19375, Jan 2026) — independent norm-preserving rotation with discriminative layer selection",
    "Minimizing Collateral Damage in Activation Steering (Nguyen et al., arXiv 2605.01167, May 2026) — COAST framework, collateral damage formalization, second-moment optimization",
    "Steered LLM Activations are Non-Surjective (Mishra et al., arXiv 2604.09839, 2026)",
    "A Sober Look at Steering Vectors for LLMs (Tan et al., NeurIPS 2024)",
    "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models (arXiv 2602.08159, 2026) — 3-8 dimensional correctness signals, linear separability across 9 models",
    "Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators (arXiv 2509.03647, 2025) — nonlinear bias warning",
    "CORAL: Correctness-Optimized Residual Activation Lens (arXiv 2602.06022, 2026) — calibration-aware steering baseline",
    "Mind the Confidence Gap: Overconfidence, Calibration, and Distractor Effects in Large Language Models (Chhikara, TMLR 2025)",
    "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025)",
    "Calibrating Verbalized Confidence with Self-Generated Distractors (Wang & Stengel-Eskin, ICLR 2026)",
    "Calibration Across Layers: Understanding Calibration Evolution in LLMs (Joshi et al., EMNLP 2025)",
    "Alleviating Choice Supportive Bias in LLM with Reasoning Dependency Generation (Zhuang et al., arXiv 2512.03082, 2025)",
    "Calibrating LLM Confidence by Probing Perturbed Representation Stability (arXiv 2505.21772, 2025)",
    "Know When You're Wrong: Aligning Confidence with Correctness for LLM Error Detection (arXiv 2603.06604, 2026)",
    "Fine-Grained Activation Steering: Steering Less, Achieving More (arXiv 2602.04428, 2026) — atomic-unit-level steering",
    "Contextual Linear Activation Steering of Language Models (arXiv 2604.24693, 2026) — context-adaptive steering strengths"
  ],
  "description": "We propose DBS-v2 (Disentangled Bias Steering), a method that separately identifies, assesses the steerability of, and adaptively corrects two competing sources of LLM miscalibration identified by Kumaran et al. (2026): choice-supportive bias (CSB, inflating confidence in selected answers) and contradictory-evidence overweighting (CEO, causing excessive confidence revision under criticism). Unlike Tsujimura & Tagade (2025), who descriptively decomposed assertiveness into emotion/logic clusters via unsupervised methods on a 1B model without calibration evaluation, DBS-v2 is grounded in causally-identified cognitive biases with theory-driven contrastive stimuli and directly targets calibration metrics.\n\nA critical insight motivating this revision is the classification-correction gap demonstrated by Liu (2605.05715): linearly decodable failure directions (71.6% balanced accuracy) can yield Δ≈0 under steering because they overlap 85-88% with task-critical computation. This means that separability (Phase 1A) is necessary but insufficient — we must also assess steerability before committing to an intervention strategy.\n\nThe method proceeds in three phases. Phase 1A (Separability Validation) tests whether CSB and CEO produce distinguishable activation signatures using contrastive activation probing, validated via cosine similarity, principal angle analysis, PCA/ICA dimensionality assessment, and cross-prediction ablation (following Miao & Ungar, 2026). Phase 1B (Steerability Assessment) — the key new addition — computes the specificity ratio (mode-specific vs. shared variance with the correct/incorrect subspace) for each identified bias direction, following Liu's shared-specific decomposition methodology. This diagnostic distinguishes between directions that are decodable-and-steerable vs. decodable-but-entangled. We hypothesize that CSB and CEO may have asymmetric specificity profiles, which would explain why monolithic calibration steering yields inconsistent results across settings. The Confidence Manifold study (2602.08159) provides encouraging evidence that correctness-related signals occupy only 3-8 dimensions with simple mean-shift geometry, suggesting calibration-related directions may have more favorable specificity than the medical overthinking phenomenon Liu studied.\n\nPhase 2 trains a lightweight per-instance bias dominance classifier whose output determines both which bias is active and which intervention route to apply. Phase 3 implements adaptive routing: (Route A) Spherical Steering for high-specificity directions (≥0.5), with Selective Steering (Dang & Ngo, 2601.19375) as an ablation alternative providing discriminative layer selection; (Route B) a learned non-linear bottleneck residual MLP (d→64→d) for low-specificity directions (<0.2), trained with COAST-informed (Nguyen et al., 2605.01167) collateral-damage-aware loss weighting; (Route C) selective abstention leveraging the decodable signal for reliability estimation when neither linear nor non-linear correction is safe; and (Route D) conservative hybrid steering for intermediate specificity (0.2-0.5).\n\nWe evaluate on TriviaQA, MMLU, PopQA, and NQ-Open across five models: Gemma 4 31B (Dense), Qwen3-8B, and Llama-3.1-8B-Instruct as primary targets, plus Qwen2.5-3B and Llama-3.2-3B for fair comparison with 'Wired for Overconfidence' baselines. We compare against temperature scaling, CCPS, VUF intervention, DINCO, CORAL, Miao & Ungar adaptive steering, monolithic Spherical Steering (without bias decomposition), and monolithic non-linear MLP (without bias decomposition). The primary contributions are: (1) the first joint separability-and-steerability assessment of competing calibration biases, providing specificity ratio measurements that the field currently lacks; (2) interpretable, bias-specific diagnostics revealing which bias source drives miscalibration per-instance AND whether it is correctable; (3) adaptive intervention routing that gracefully degrades from manifold-preserving rotation to non-linear correction to selective abstention based on measured entanglement; and (4) the hypothesis that CSB and CEO have asymmetric steerability profiles, offering a mechanistic explanation for inconsistent monolithic steering results. Phase 1 results constitute an independent contribution regardless of Phase 2-3 outcomes.",
  "project_name": "bias_disentangle_calib",
  "source": "web_research",
  "revision_notes": {
    "round1_issue_1_missing_competitor": "Tsujimura & Tagade (2508.17182) cited as closest methodological precedent, differentiated on four axes (theory-driven vs. post-hoc, calibration vs. assertiveness, 5 models vs. 1, causal intervention vs. descriptive). [Carried from R1]",
    "round1_issue_2_model_names": "Fixed model names (Gemma 4 31B Dense, Llama-3.1-8B-Instruct, Qwen3-8B). [Carried from R1]",
    "round1_issue_3_untested_assumption": "Phase 1A retains all 5 separability tests with quantitative thresholds. [Carried from R1, now labeled Phase 1A]",
    "round1_issue_4_steering_reliability": "Spherical Steering retained as primary Route A intervention; now augmented with Route B non-linear fallback and Route C abstention for when even rotation fails. [Extended from R1]",
    "round1_issue_5_baseline_comparison": "Contribution framing around interpretability, difficulty-stratification, and robustness retained. Added monolithic non-linear MLP as new baseline. [Extended from R1]",
    "round1_issue_6_behavioral_mechanistic_leap": "Phase 1A tests separability; Phase 1B now ALSO tests steerability. [Extended from R1]",
    "round2_issue_1_critical_missing_competitor": "Liu (2605.05715) now thoroughly integrated as a foundational reference rather than treated as merely a competitor. The classification-correction gap is incorporated into the core problem framing, opportunity statement, and landscape. The specificity ratio is adopted as a pre-intervention diagnostic in Phase 1B. The non-linear MLP finding (Δ=+2.8pp) motivates Route B. The selective abstention finding (AUROC 0.610) motivates Route C. We differentiate from Liu by (a) studying calibration biases rather than medical overthinking, (b) testing multiple competing directions rather than a single failure mode, (c) hypothesizing asymmetric steerability profiles, and (d) providing the Confidence Manifold evidence (2602.08159) that calibration-related directions may have more favorable geometry.",
    "round2_issue_2_separability_steerability_gap": "Phase 1 now has two explicit sub-phases: 1A (separability, carried from R1) and 1B (steerability, NEW). Phase 1B computes specificity ratio, within-class variance analysis, LEACE concept erasure, and cross-architecture stability for each bias direction. Quantitative thresholds established: ≥0.5 HIGH, 0.2-0.5 MEDIUM, <0.2 LOW. The separability≠steerability distinction is elevated to a core theme of the paper, discussed in the core_problem, opportunity, and approach.",
    "round2_issue_3_minor_missing_references": "Selective Steering (Dang & Ngo, 2601.19375) now cited in landscape and used as Route A ablation alternative. COAST (Nguyen et al., 2605.01167) cited in landscape and used for collateral-damage-aware training in Route B. Additionally cited: Confidence Manifold (2602.08159), AUSteer (2602.04428), CLAS (2604.24693) in landscape for completeness.",
    "round2_issue_4_nonlinear_steering_fallback": "Route B (learned non-linear residual MLP) added as Phase 3 intervention for low-specificity directions, directly motivated by Liu's finding that a 4096→64→4096 bottleneck achieves Δ=+2.8pp where 29 linear methods fail. Route C (selective abstention) added as ultimate fallback. Route D (conservative hybrid) added for intermediate specificity. This creates a principled four-tier intervention hierarchy that degrades gracefully based on measured entanglement rather than assuming all directions are equally steerable."
  }
}
```

---

## Summary of Changes (Round 2 → Round 3)

**Change type: MAJOR.** This revision goes beyond patching — it reconceptualizes the relationship between diagnosis and intervention.

### Deep Analysis of Reviewer Concerns

The reviewer's central insight is profound: **decodability ≠ steerability**. Liu (2605.05715) showed that on Llama-3.1-8B and Qwen2.5-7B, a failure mode (medical overthinking) was linearly decodable at 71.6% balanced accuracy, yet ALL 29 linear steering configurations across 5 families yielded Δ≈0. The root cause is representational entanglement: the failure direction overlaps 85-88% with task-critical computation (specificity ratio ≤0.152).

This doesn't kill the project — it actually **strengthens** it by adding a new dimension. Here's why:

### Key Reconceptualization

1. **The classification-correction gap becomes a core feature, not a bug.** Rather than assuming all identified bias directions are steerable, we now explicitly test steerability and route to appropriate interventions. This makes DBS-v2 more principled than any competing method.

2. **The asymmetric steerability hypothesis is novel and testable.** CSB and CEO are mechanistically different biases. It's plausible (and interesting) that one has high specificity (steerable via rotation) while the other has low specificity (requires non-linear correction). This would explain the inconsistent results from monolithic calibration steering in the literature.

3. **The Confidence Manifold evidence (2602.08159) provides reasonable optimism.** Correctness signals occupy only 3-8 dimensions with simple mean-shift geometry — suggesting calibration-related directions may have better specificity profiles than the medical overthinking case Liu studied.

4. **Four-tier adaptive routing is principled.** Route A (Spherical Steering) → Route B (non-linear MLP) → Route C (selective abstention) → Route D (conservative hybrid) provides graceful degradation based on measured entanglement rather than assuming one-size-fits-all.

### Structural Changes
- **Core problem**: Now explicitly names the decodable-steerable gap
- **Phase 1**: Split into 1A (separability) and 1B (steerability diagnostics with specificity ratio)
- **Phase 3**: Restructured from single-strategy to 4-route adaptive routing
- **Landscape**: 6 new papers integrated (Liu 2605.05715, Selective Steering, COAST, Confidence Manifold, AUSteer, CLAS)
- **References**: Expanded from 16 to 22
- **Resources**: +20-25% compute increase for steerability diagnostics and non-linear adapter training

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05fedddc-ec7a-487e-86bc-2ad37455d8af",
  "isSidechain": false,
  "requestId": "req_011CbBz14WVzgwMWTJ1ssG9A",
  "type": "assistant",
  "uuid": "ebe1433b-2e1f-40f8-8f4f-20000177fb47",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RN4GPSnoa6TPAwAfnMWVkb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 87,
      "cache_read_input_tokens": 59068,
      "output_tokens": 9124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 87,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9124,
          "cache_read_input_tokens": 59068,
          "cache_creation_input_tokens": 87,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 87
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

_source line 87_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"Disentangling Competing Calibration Biases via Geometry-Aware Activati…",
  "leafUuid": "ebe1433b-2e1f-40f8-8f4f-20000177fb47",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340"
}
```

---

### Runtime record

_source line 88_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise calibration bias steering with steerability diagnostics",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340"
}
```

---

### Runtime record

_source line 89_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-19 (UTC).**  ## Original idea {   \"title\": \"Disentangling Competing Calibration Biases via Geometry-Aware Activati…",
  "leafUuid": "ebe1433b-2e1f-40f8-8f4f-20000177fb47",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340"
}
```

---

### Runtime record

_source line 90_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise calibration bias steering with steerability diagnostics",
  "sessionId": "4f29d1ac-c145-4ad7-a4cf-bff927c1d340"
}
```

---
