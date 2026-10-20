# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-16 (UTC).** ## Original idea { "tit

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-1/05d199d5-3d58-4072-a284-85726a2303cb.jsonl`
- **Structured JSON:** [`c5e51cea773da0c88c0f.json`](../../sessions/c5/c5e51cea773da0c88c0f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T08:40:42.867Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T08:40:42.867Z",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-16 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Geometry-Triggered Sentence-Level Activation Steering for Factual Hallucination Suppression\",\n  \"core_problem\": \"Recent work (Attractor Geometry of Transformer Memory, May 2026) demonstrates that factual hallucination corresponds to 'basin absence'—the hidden state drifts freely when no memorized attractor basin exists—and that geometric margin cleanly separates correct recall from hallucination (AUROC 0.993–1.000, vs. entropy's 0.622). Yet this remains analysis-only: no method translates geometric margin into targeted activation interventions. Meanwhile, Hallucination Basins (April 2026) proposes geometry-aware steering but operates at per-sequence granularity with a single scalar controller—applying uniform corrections across all claims in a response, causing unnecessary utility loss on correct sub-claims. Existing steering methods (ACT, ODESteer, Verbal Uncertainty Feature Calibration) either apply corpus-averaged corrections uniformly, are input-oblivious, or calibrate confidence expression without actually redirecting toward factual representations.\",\n  \"opportunity\": \"The critical gap is between detection granularity and intervention granularity. Hallucination Basins demonstrates that geometry-aware steering works but is limited by its sequence-level all-or-nothing decision: if one claim in a multi-sentence response triggers intervention, all claims get steered—including correct ones. PCNet operates at token level but hallucination is fundamentally a claim-level phenomenon (one incorrect token contaminates an entire factual assertion). The unexploited sweet spot is sentence-level intervention: sentences are the natural unit of factual claims (the granularity FActScore evaluates, the granularity humans judge, and the granularity at which 'Think in Sentences' (2604.10135) shows LLMs perform context integration → next-step planning). The combination of (1) PCA-regularized Mahalanobis margin as trigger (capturing directional covariance, unlike Hallucination Basins' isotropic Euclidean distance), (2) sentence-level gating enabling within-sequence selectivity, and (3) per-layer MLP controller (vs. Hallucination Basins' single logistic-regression scalar) bridges the detection-to-intervention gap with principled granularity.\",\n  \"landscape\": \"Attractor Geometry of Transformer Memory (arxiv 2605.05686, May 2026) demonstrates hallucination = basin absence with geometric margin achieving AUROC 0.993–1.000 for hallucination detection on factoid tasks, but is analysis-only with no intervention. Hallucination Basins (arxiv 2604.04743, April 2026) is the most direct competitor: proposes Adaptive Geometry-Aware Steering using centroid-difference vectors (μ_fact−μ_hall), Euclidean distance to basin center as trigger, and a learned scalar controller mapping Φ(x)∈ℝ² (local contraction ratio + min distance) to steering intensity via logistic regression, at per-sequence granularity on 1B–3B models (Llama-3.2-1B/3B, Qwen-2.5-1.5B, Gemma-2-2B). GTS advances beyond Hallucination Basins in three specific ways: (a) sentence-level gating enables within-sequence selectivity—selectively steering uncertain claims while preserving confident ones, avoiding the all-or-nothing sequence-level decision that causes utility loss when only one claim in a multi-sentence response is problematic; (b) PCA-regularized Mahalanobis distance accounts for directional covariance in representation space, providing tighter decision boundaries than isotropic Euclidean distance (matching findings from OOD detection literature, Lee et al. 2018); (c) per-layer MLP controller learns which layers matter for different types of factual errors, vs. a single scalar that applies uniform intensity across layers. Calibrating Verbal Uncertainty as a Linear Feature (Ji et al., EMNLP 2025 Outstanding Paper, arxiv 2503.14477) achieves ~31.9% reduction in confident hallucinations via inference-time linear-feature intervention on Llama3.1-8B/Mistral-7B/Qwen2.5-7B. However, it calibrates verbal uncertainty expression rather than redirecting toward factual representations—it makes the model hedge when uncertain but does not correct the underlying generation. GTS detects knowledge absence (basin absence), while verbal uncertainty detects expressed hesitation—these are complementary signals. GTS specifically catches confident hallucinations where the model shows no verbal uncertainty (high decisiveness + wrong answer), which is the failure mode verbal uncertainty misses. HELIX/Tethered Reasoning (arxiv 2602.17691, Feb 2026) uses Mahalanobis distance + graduated steering but targets structural coherence in quantized models—a 'syntax tether' not factual accuracy. ACT (WWW 2025) achieves TruthfulQA improvement via K-means clustered steering but uses corpus-averaged vectors. ODESteer (ICLR 2026) achieves 5.7% over ACT via ODE-based multi-step steering but remains input-oblivious. PCNet (May 2026, arxiv 2605.05953) detects hallucinations as geometric anomalies and applies contrastive decoding at token level—but token-level intervention fragments the semantic unit of factual claims and incurs per-token computational overhead. Where Does Reasoning Break? (arxiv 2605.13772, May 2026) detects step-level hallucination via transport geometry but proposes no intervention. DRIFT (arxiv 2601.14210, Jan 2026) detects representational instability from intermediate layers at <0.1% overhead but is detection-only. Guiding Giants/WAS (arxiv 2505.20309, May 2025) trains lightweight controllers for instance-specific, layer-aware weighted activation steering but does not condition on geometric trajectory signals. SADI (arxiv 2410.12299, 2024) constructs input-specific dynamic steering vectors but does not use geometric margin or sentence-level gating. Hallucination as Trajectory Commitment (arxiv 2604.15400, April 2026) provides causal evidence for early commitment with asymmetric attractor dynamics, supporting the idea that intervention at sentence boundaries (before commitment propagates) is timely. Think in Sentences (arxiv 2604.10135, April 2026) demonstrates that sentence boundary tokens serve as 'inference anchors' triggering context integration → next-step planning cycles, providing theoretical support for why geometric margin at these positions may be predictive of subsequent sentence quality.\",\n  \"approach\": \"We propose Geometry-Triggered Steering (GTS), operating in three stages with explicit specification of each computational component:\\n\\n**Stage 1: TRIGGER (PCA-Regularized Geometric Margin)**\\nDuring generation, at each sentence boundary (detected via period/newline tokens), extract hidden-state activations at the boundary token across layers using nnsight intervention hooks. Compute the geometric margin using class-conditional PCA-regularized Mahalanobis distance:\\n(a) Offline: From a calibration set (~2K examples from TruthfulQA + FELM correct-answer forward passes), collect hidden states at factual completion positions. Apply PCA to project from full hidden dimension (d=4096 for Llama-3.1-8B, d=4096 for Qwen3-8B) to the top-k principal components (k=256), reducing covariance estimation to a well-conditioned 256×256 matrix from ~2K samples.\\n(b) Online: Project the boundary token's activation into the PCA subspace, compute Mahalanobis distance to the nearest factual cluster centroid in reduced space: δ(x) = √((h_pca - μ_pca)ᵀ Σ_pca⁻¹ (h_pca - μ_pca)).\\n(c) When δ exceeds a calibrated threshold (set via precision-recall analysis on validation split), flag the upcoming sentence for intervention.\\nWe ablate k∈{64, 128, 256, 512} and include a diagonal-covariance baseline and a pure Euclidean baseline (matching Hallucination Basins' approach) to quantify the benefit of directional covariance.\\n\\n**Stage 2: DIRECTION (Centroid-Directed Steering Vector)**\\nCompute the steering direction as the unit vector from the current activation toward the factual cluster centroid at each layer in the PCA subspace, then project back to full space: v_steer = (μ_pca - h_pca) / ||μ_pca - h_pca||, lifted back to full dimensionality via PCA inverse transform. This yields an input-specific correction direction toward regions of successful fact recall.\\n\\n**Stage 3: INTENSITY (Per-Layer MLP Controller)**\\nA lightweight 2-layer MLP controller (hidden dim 64, inspired by Guiding Giants/WAS) takes [geometric_margin, layer_index/L, margin_velocity] as input (3D feature vector) and predicts per-layer steering weight λ_ℓ. The controller is trained on a calibration set (~2K examples) via a combined objective: maximize FActScore on steered outputs while minimizing perplexity increase on outputs where margin is below threshold (i.e., correct outputs). Steering is applied: h_steered(ℓ) = h(ℓ) + λ_ℓ · v_steer(ℓ) at the residual stream of layers where λ_ℓ > ε.\\n\\n**Timing Hypothesis Validation:**\\nWe explicitly frame the following as a testable hypothesis: geometric margin at sentence boundary N is predictive of factual accuracy in sentence N+1. Validation protocol: (1) Generate 500 multi-sentence responses on LongFact/FActScore prompts. (2) Compute margin at every sentence boundary. (3) Annotate each subsequent sentence with FActScore. (4) Measure Spearman correlation between boundary margin and next-sentence factuality. If correlation ρ < 0.3, we fall back to a look-ahead variant: extract margin from the first 3 generated tokens of the new sentence (before committing the full sentence via speculative-style buffering), which still allows early intervention before the full sentence is decoded.\\n\\n**Ablation Design (addressing Hallucination Basins comparison):**\\n- GTS-full vs. GTS-sequence (ablate sentence gating: apply single decision per sequence, matching Hallucination Basins)\\n- GTS-full vs. GTS-Euclidean (replace Mahalanobis with Euclidean distance)\\n- GTS-full vs. GTS-scalar (replace per-layer MLP with single scalar logistic regression, matching Hallucination Basins' controller)\\n- GTS-full vs. Verbal-Uncertainty-Feature (Ji et al. baseline)\\nThese ablations isolate the contribution of each design choice.\\n\\nImplementation uses nnsight 0.6 on Qwen3-8B and Llama-3.1-8B-Instruct (8B scale, vs. Hallucination Basins' 1B–3B). Evaluation on TruthfulQA, HaluEval, FaithBench, FActScore, FELM, SimpleQA, LongFact, MT-Bench, MMLU, plus ECE/Brier calibration metrics.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~180h H100 80GB\",\n      \"gpu_utilization\": \"Low (~15-20%). GPU idles during code/debug/analysis cycles.\",\n      \"timeline\": \"3-4 months\",\n      \"team\": \"1-2 researchers with mechanistic interpretability + geometric ML experience\",\n      \"estimated_gpu_cost\": \"$540-630 (H100 at ~$3/hr spot)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~210h H100 80GB\",\n      \"gpu_utilization\": \"Moderate (45-55%). Agent queues batches but blocks on geometric design decisions and timing validation analysis.\",\n      \"timeline\": \"3-4 weeks\",\n      \"team\": \"1 researcher, ~30min/day reviewing agent proposals\",\n      \"claude_api_cost\": \"$200-350\",\n      \"estimated_gpu_cost\": \"$630-735\",\n      \"risk_note\": \"Timing hypothesis validation and PCA dimensionality selection benefit from human intuition about precision-recall tradeoffs.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~220-250h H100 80GB (expanded: PCA-k ablations, Mahalanobis vs. Euclidean comparison, timing validation experiment, Hallucination Basins ablations, layer weight ablations, two-model validation, 10 benchmarks)\",\n      \"gpu_utilization\": \"High (~85-90%). Well-defined pipeline with clear ablation structure.\",\n      \"timeline\": \"9-12 days with 2-4 H100 GPUs running in parallel\",\n      \"team\": \"0 (initial setup: provision GPUs, configure nnsight, define eval harness)\",\n      \"claude_api_cost\": \"$350-550 (est. 5000-7000 turns)\",\n      \"estimated_gpu_cost\": \"$660-750\",\n      \"speed_bottleneck\": \"GPU count for parallel ablation sweeps (each model requires full H100 for forward passes with intervention hooks). Secondary: FActScore evaluation requires GPT-4 API calls.\",\n      \"risk_note\": \"Primary risk: timing hypothesis may not hold for multi-sentence generation (validated Attractor Geometry insight was on factoid completion). Mitigation: look-ahead variant as fallback. Secondary risk: Mahalanobis may not significantly outperform Euclidean (Hallucination Basins uses Euclidean successfully)—in that case, the contribution shifts to sentence-level gating + per-layer controller as primary novelty.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination (arXiv 2605.05686, May 2026)\",\n    \"Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations (arXiv 2604.04743, April 2026)\",\n    \"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025 Outstanding Paper, arXiv 2503.14477)\",\n    \"Tethered Reasoning (HELIX): Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering (arXiv 2602.17691, Feb 2026)\",\n    \"Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method (ACT, WWW 2025)\",\n    \"ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment (ICLR 2026, arXiv 2602.17560)\",\n    \"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (arXiv 2605.13772, May 2026)\",\n    \"DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness (arXiv 2601.14210, Jan 2026)\",\n    \"Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs (arXiv 2505.20309, May 2025)\",\n    \"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits (PCNet, arXiv 2605.05953, May 2026)\",\n    \"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics (arXiv 2604.15400, April 2026)\",\n    \"Think in Sentences: Explicit Sentence Boundaries Enhance Language Model's Capabilities (arXiv 2604.10135, April 2026)\",\n    \"A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks (Lee et al., NeurIPS 2018)\",\n    \"Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors (SADI, arXiv 2410.12299, 2024)\",\n    \"Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models (ICLR 2026)\",\n    \"Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation (ACL Findings 2025)\"\n  ],\n  \"description\": \"We propose Geometry-Triggered Steering (GTS), a method that bridges the detection-to-intervention gap by translating geometric hallucination theory into practical, sentence-gated activation steering. Building on the insight that factual hallucination corresponds to 'basin absence' in hidden-state attractor geometry (Liang et al., May 2026), GTS monitors PCA-regularized Mahalanobis distance from residual stream activations to factual cluster centroids at sentence boundaries during generation. When geometric margin indicates basin absence, GTS computes an input-specific steering vector directed toward the factual centroid and applies it with per-layer weights predicted by a lightweight learned controller.\\n\\nGTS addresses specific limitations of the most direct prior work: (1) vs. Hallucination Basins (2604.04743), which applies geometry-aware steering at per-sequence granularity with a single scalar controller on 1B–3B models, GTS introduces sentence-level gating that enables within-sequence selectivity (steering only uncertain claims while preserving correct ones), PCA-regularized Mahalanobis distance (capturing directional covariance vs. isotropic Euclidean), and a per-layer MLP controller at 8B scale; (2) vs. Verbal Uncertainty Feature Calibration (Ji et al., EMNLP 2025), which calibrates confidence expression without correcting the underlying generation, GTS detects knowledge absence and actively redirects toward factual representations—catching the critical failure mode of confident hallucinations that show no verbal uncertainty; (3) vs. PCNet's token-level contrastive decoding, GTS operates at sentence granularity—the natural unit of factual claims—avoiding per-token overhead while matching the abstraction level at which hallucination manifests semantically.\\n\\nWe explicitly validate the timing hypothesis (margin at boundary N predicts factuality of sentence N+1) with a correlation study, provide a look-ahead fallback, and include ablations isolating each design choice against Hallucination Basins' approach. Implementation uses nnsight 0.6 on Qwen3-8B and Llama-3.1-8B-Instruct, evaluating on TruthfulQA, HaluEval, FaithBench, FActScore, FELM, SimpleQA, LongFact, MT-Bench, MMLU, plus ECE/Brier calibration metrics.\",\n  \"project_name\": \"geometry_triggered_steering\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 3)\nIssues: [\"MISSING CRITICAL COMPETITOR: Spherical Steering (arXiv 2602.08169, ICML 2026) proposes geometry-aware activation rotation with a 'confidence gate that dynamically modulates steering strength based on input uncertainty' — this is conceptually very close to GTS's trigger-then-steer paradigm but uses rotation instead of addition, achieving +10% on TruthfulQA while preserving generation quality. This paper is NOT cited and must be discussed as a baseline.\", \"MISSING COMPETITOR: 'Minimizing Collateral Damage in Activation Steering' (arXiv 2605.01167, May 2026) directly addresses the utility-preservation problem that GTS claims sentence-level gating solves, but via a constrained optimization framework. This is an alternative solution to the same problem that should be compared.\", \"MISSING COMPETITOR: FLAS (Flow-based Activation Steering, arXiv 2605.05892, May 2026) learns a concept-conditioned velocity field that transports activations, claiming to outperform existing steering methods including those on TruthfulQA. This represents another geometry-aware steering approach not discussed.\", \"CHERRY-PICKED AUROC CLAIM: The description implies geometric margin achieves 'AUROC 0.993–1.000' but this is on synthetic factoid tasks. On TruthfulQA, the actual AUROC is 0.858 — a 14-point gap that significantly weakens the trigger reliability argument. The proposal must report the TruthfulQA AUROC and discuss implications for trigger precision/recall.\", \"TIMING HYPOTHESIS REMAINS HIGH-RISK: The Attractor Geometry paper tests ONLY first-token factoid completion on synthetic and controlled tasks. Extrapolating to 'margin at sentence boundary N predicts sentence N+1 factuality' during multi-sentence open-ended generation is a substantial leap. The look-ahead fallback (extracting margin from first 3 tokens) is reasonable but introduces latency and complexity not accounted for in the resource estimate.\", \"OVER-INTERPRETATION OF 'Think in Sentences': The proposal claims this paper provides 'theoretical support for why geometric margin at these positions may be predictive of subsequent sentence quality.' However, the paper is a prompting strategy paper that shows attention concentration at delimiters — it does NOT analyze hidden-state geometry at sentence boundaries and provides no evidence about geometric margin predictiveness.\", \"MAHALANOBIS vs EUCLIDEAN: The proposal positions PCA-regularized Mahalanobis as an advantage over Hallucination Basins' Euclidean, citing OOD detection literature (Lee et al. 2018). However, (1) Hallucination Basins works successfully with Euclidean, (2) the Attractor Geometry paper also uses Euclidean and achieves strong results, and (3) the benefit of Mahalanobis in THIS setting (high-dim LLM residual streams with limited calibration data) is undemonstrated. The ablation is planned but this is a risk to the primary novelty claim if Mahalanobis doesn't significantly outperform Euclidean.\", \"RESOURCE ESTIMATE CONCERN: Running FActScore evaluation on multi-model outputs requires significant GPT-4 API costs (not included in the estimate). FActScore evaluates ~130-205 entailment checks per biography and takes ~100 seconds per response. With 2 models × multiple conditions × hundreds of examples, API costs could be $200-500+ on top of GPU costs.\", \"SCALE COMPARISON WEAKNESS: GTS claims to operate at '8B scale, vs. Hallucination Basins' 1B-3B' as an advance. But the Attractor Geometry paper also tested on models up to 14B and Hallucination Basins tested basin detection on Llama-3.1-8B. Scale alone is not a contribution.\"]\nFeedback: The idea has improved substantially from rounds 1-2 and now has a clear, well-articulated pipeline. The core concept of sentence-level selective steering is sound. However, three critical issues remain:\n\n1. **Cite and compare against Spherical Steering (ICML 2026, arXiv 2602.08169)**: This paper's confidence gate + geometry-aware rotation is the closest competitor to GTS's trigger + steer paradigm. You MUST position against it. Key differentiation: Spherical Steering uses rotation (preserving norm) with a general confidence gate, while GTS uses centroid-directed addition with a geometry-specific Mahalanobis trigger. Argue that GTS's trigger is more principled (basin-distance-based) and its sentence-level granularity enables within-sequence selectivity that Spherical Steering lacks (it applies uniformly). Also cite 'Minimizing Collateral Damage' (2605.01167) as an alternative approach to utility preservation.\n\n2. **Fix the AUROC reporting**: Currently the 0.993-1.000 AUROC is prominently featured but comes from synthetic factoid tasks. The TruthfulQA AUROC is 0.858 — still useful as a trigger but with much higher false-positive/negative rates. Be honest about this: 'Geometric margin achieves AUROC 0.858 on TruthfulQA (vs. entropy's 0.622), sufficient for selective intervention with appropriate thresholding, though precision-recall tradeoffs require careful calibration.' This honesty actually strengthens the paper because it motivates the ablation study.\n\n3. **De-emphasize 'Think in Sentences' as geometric evidence**: This paper shows attention concentration, not hidden-state geometry. Cite it as motivating the sentence-as-unit-of-planning hypothesis, not as providing geometric evidence. The timing hypothesis must stand on its own empirical validation (which the proposal already plans).\n\nMinor improvements: (a) Add FActScore API costs to the resource estimate (~$200-400). (b) Acknowledge that if Mahalanobis doesn't significantly outperform Euclidean, the novelty shifts primarily to sentence-level gating + per-layer controller. (c) Drop the 'AUROC 0.993-1.000' framing and lead with the TruthfulQA number instead.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\")."
}
```

---

### Runtime record

_source line 2 · 2026-05-16T08:40:42.872Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T08:40:42.872Z",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb"
}
```

---

## Round 1

55 recorded events

### User

_source line 3 · 2026-05-16T08:40:42.900Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-16 (UTC).**

## Original idea
{
  "title": "Geometry-Triggered Sentence-Level Activation Steering for Factual Hallucination Suppression",
  "core_problem": "Recent work (Attractor Geometry of Transformer Memory, May 2026) demonstrates that factual hallucination corresponds to 'basin absence'—the hidden state drifts freely when no memorized attractor basin exists—and that geometric margin cleanly separates correct recall from hallucination (AUROC 0.993–1.000, vs. entropy's 0.622). Yet this remains analysis-only: no method translates geometric margin into targeted activation interventions. Meanwhile, Hallucination Basins (April 2026) proposes geometry-aware steering but operates at per-sequence granularity with a single scalar controller—applying uniform corrections across all claims in a response, causing unnecessary utility loss on correct sub-claims. Existing steering methods (ACT, ODESteer, Verbal Uncertainty Feature Calibration) either apply corpus-averaged corrections uniformly, are input-oblivious, or calibrate confidence expression without actually redirecting toward factual representations.",
  "opportunity": "The critical gap is between detection granularity and intervention granularity. Hallucination Basins demonstrates that geometry-aware steering works but is limited by its sequence-level all-or-nothing decision: if one claim in a multi-sentence response triggers intervention, all claims get steered—including correct ones. PCNet operates at token level but hallucination is fundamentally a claim-level phenomenon (one incorrect token contaminates an entire factual assertion). The unexploited sweet spot is sentence-level intervention: sentences are the natural unit of factual claims (the granularity FActScore evaluates, the granularity humans judge, and the granularity at which 'Think in Sentences' (2604.10135) shows LLMs perform context integration → next-step planning). The combination of (1) PCA-regularized Mahalanobis margin as trigger (capturing directional covariance, unlike Hallucination Basins' isotropic Euclidean distance), (2) sentence-level gating enabling within-sequence selectivity, and (3) per-layer MLP controller (vs. Hallucination Basins' single logistic-regression scalar) bridges the detection-to-intervention gap with principled granularity.",
  "landscape": "Attractor Geometry of Transformer Memory (arxiv 2605.05686, May 2026) demonstrates hallucination = basin absence with geometric margin achieving AUROC 0.993–1.000 for hallucination detection on factoid tasks, but is analysis-only with no intervention. Hallucination Basins (arxiv 2604.04743, April 2026) is the most direct competitor: proposes Adaptive Geometry-Aware Steering using centroid-difference vectors (μ_fact−μ_hall), Euclidean distance to basin center as trigger, and a learned scalar controller mapping Φ(x)∈ℝ² (local contraction ratio + min distance) to steering intensity via logistic regression, at per-sequence granularity on 1B–3B models (Llama-3.2-1B/3B, Qwen-2.5-1.5B, Gemma-2-2B). GTS advances beyond Hallucination Basins in three specific ways: (a) sentence-level gating enables within-sequence selectivity—selectively steering uncertain claims while preserving confident ones, avoiding the all-or-nothing sequence-level decision that causes utility loss when only one claim in a multi-sentence response is problematic; (b) PCA-regularized Mahalanobis distance accounts for directional covariance in representation space, providing tighter decision boundaries than isotropic Euclidean distance (matching findings from OOD detection literature, Lee et al. 2018); (c) per-layer MLP controller learns which layers matter for different types of factual errors, vs. a single scalar that applies uniform intensity across layers. Calibrating Verbal Uncertainty as a Linear Feature (Ji et al., EMNLP 2025 Outstanding Paper, arxiv 2503.14477) achieves ~31.9% reduction in confident hallucinations via inference-time linear-feature intervention on Llama3.1-8B/Mistral-7B/Qwen2.5-7B. However, it calibrates verbal uncertainty expression rather than redirecting toward factual representations—it makes the model hedge when uncertain but does not correct the underlying generation. GTS detects knowledge absence (basin absence), while verbal uncertainty detects expressed hesitation—these are complementary signals. GTS specifically catches confident hallucinations where the model shows no verbal uncertainty (high decisiveness + wrong answer), which is the failure mode verbal uncertainty misses. HELIX/Tethered Reasoning (arxiv 2602.17691, Feb 2026) uses Mahalanobis distance + graduated steering but targets structural coherence in quantized models—a 'syntax tether' not factual accuracy. ACT (WWW 2025) achieves TruthfulQA improvement via K-means clustered steering but uses corpus-averaged vectors. ODESteer (ICLR 2026) achieves 5.7% over ACT via ODE-based multi-step steering but remains input-oblivious. PCNet (May 2026, arxiv 2605.05953) detects hallucinations as geometric anomalies and applies contrastive decoding at token level—but token-level intervention fragments the semantic unit of factual claims and incurs per-token computational overhead. Where Does Reasoning Break? (arxiv 2605.13772, May 2026) detects step-level hallucination via transport geometry but proposes no intervention. DRIFT (arxiv 2601.14210, Jan 2026) detects representational instability from intermediate layers at <0.1% overhead but is detection-only. Guiding Giants/WAS (arxiv 2505.20309, May 2025) trains lightweight controllers for instance-specific, layer-aware weighted activation steering but does not condition on geometric trajectory signals. SADI (arxiv 2410.12299, 2024) constructs input-specific dynamic steering vectors but does not use geometric margin or sentence-level gating. Hallucination as Trajectory Commitment (arxiv 2604.15400, April 2026) provides causal evidence for early commitment with asymmetric attractor dynamics, supporting the idea that intervention at sentence boundaries (before commitment propagates) is timely. Think in Sentences (arxiv 2604.10135, April 2026) demonstrates that sentence boundary tokens serve as 'inference anchors' triggering context integration → next-step planning cycles, providing theoretical support for why geometric margin at these positions may be predictive of subsequent sentence quality.",
  "approach": "We propose Geometry-Triggered Steering (GTS), operating in three stages with explicit specification of each computational component:\n\n**Stage 1: TRIGGER (PCA-Regularized Geometric Margin)**\nDuring generation, at each sentence boundary (detected via period/newline tokens), extract hidden-state activations at the boundary token across layers using nnsight intervention hooks. Compute the geometric margin using class-conditional PCA-regularized Mahalanobis distance:\n(a) Offline: From a calibration set (~2K examples from TruthfulQA + FELM correct-answer forward passes), collect hidden states at factual completion positions. Apply PCA to project from full hidden dimension (d=4096 for Llama-3.1-8B, d=4096 for Qwen3-8B) to the top-k principal components (k=256), reducing covariance estimation to a well-conditioned 256×256 matrix from ~2K samples.\n(b) Online: Project the boundary token's activation into the PCA subspace, compute Mahalanobis distance to the nearest factual cluster centroid in reduced space: δ(x) = √((h_pca - μ_pca)ᵀ Σ_pca⁻¹ (h_pca - μ_pca)).\n(c) When δ exceeds a calibrated threshold (set via precision-recall analysis on validation split), flag the upcoming sentence for intervention.\nWe ablate k∈{64, 128, 256, 512} and include a diagonal-covariance baseline and a pure Euclidean baseline (matching Hallucination Basins' approach) to quantify the benefit of directional covariance.\n\n**Stage 2: DIRECTION (Centroid-Directed Steering Vector)**\nCompute the steering direction as the unit vector from the current activation toward the factual cluster centroid at each layer in the PCA subspace, then project back to full space: v_steer = (μ_pca - h_pca) / ||μ_pca - h_pca||, lifted back to full dimensionality via PCA inverse transform. This yields an input-specific correction direction toward regions of successful fact recall.\n\n**Stage 3: INTENSITY (Per-Layer MLP Controller)**\nA lightweight 2-layer MLP controller (hidden dim 64, inspired by Guiding Giants/WAS) takes [geometric_margin, layer_index/L, margin_velocity] as input (3D feature vector) and predicts per-layer steering weight λ_ℓ. The controller is trained on a calibration set (~2K examples) via a combined objective: maximize FActScore on steered outputs while minimizing perplexity increase on outputs where margin is below threshold (i.e., correct outputs). Steering is applied: h_steered(ℓ) = h(ℓ) + λ_ℓ · v_steer(ℓ) at the residual stream of layers where λ_ℓ > ε.\n\n**Timing Hypothesis Validation:**\nWe explicitly frame the following as a testable hypothesis: geometric margin at sentence boundary N is predictive of factual accuracy in sentence N+1. Validation protocol: (1) Generate 500 multi-sentence responses on LongFact/FActScore prompts. (2) Compute margin at every sentence boundary. (3) Annotate each subsequent sentence with FActScore. (4) Measure Spearman correlation between boundary margin and next-sentence factuality. If correlation ρ < 0.3, we fall back to a look-ahead variant: extract margin from the first 3 generated tokens of the new sentence (before committing the full sentence via speculative-style buffering), which still allows early intervention before the full sentence is decoded.\n\n**Ablation Design (addressing Hallucination Basins comparison):**\n- GTS-full vs. GTS-sequence (ablate sentence gating: apply single decision per sequence, matching Hallucination Basins)\n- GTS-full vs. GTS-Euclidean (replace Mahalanobis with Euclidean distance)\n- GTS-full vs. GTS-scalar (replace per-layer MLP with single scalar logistic regression, matching Hallucination Basins' controller)\n- GTS-full vs. Verbal-Uncertainty-Feature (Ji et al. baseline)\nThese ablations isolate the contribution of each design choice.\n\nImplementation uses nnsight 0.6 on Qwen3-8B and Llama-3.1-8B-Instruct (8B scale, vs. Hallucination Basins' 1B–3B). Evaluation on TruthfulQA, HaluEval, FaithBench, FActScore, FELM, SimpleQA, LongFact, MT-Bench, MMLU, plus ECE/Brier calibration metrics.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~180h H100 80GB",
      "gpu_utilization": "Low (~15-20%). GPU idles during code/debug/analysis cycles.",
      "timeline": "3-4 months",
      "team": "1-2 researchers with mechanistic interpretability + geometric ML experience",
      "estimated_gpu_cost": "$540-630 (H100 at ~$3/hr spot)"
    },
    "human_in_loop": {
      "gpu_hours": "~210h H100 80GB",
      "gpu_utilization": "Moderate (45-55%). Agent queues batches but blocks on geometric design decisions and timing validation analysis.",
      "timeline": "3-4 weeks",
      "team": "1 researcher, ~30min/day reviewing agent proposals",
      "claude_api_cost": "$200-350",
      "estimated_gpu_cost": "$630-735",
      "risk_note": "Timing hypothesis validation and PCA dimensionality selection benefit from human intuition about precision-recall tradeoffs."
    },
    "auto_research": {
      "gpu_hours": "~220-250h H100 80GB (expanded: PCA-k ablations, Mahalanobis vs. Euclidean comparison, timing validation experiment, Hallucination Basins ablations, layer weight ablations, two-model validation, 10 benchmarks)",
      "gpu_utilization": "High (~85-90%). Well-defined pipeline with clear ablation structure.",
      "timeline": "9-12 days with 2-4 H100 GPUs running in parallel",
      "team": "0 (initial setup: provision GPUs, configure nnsight, define eval harness)",
      "claude_api_cost": "$350-550 (est. 5000-7000 turns)",
      "estimated_gpu_cost": "$660-750",
      "speed_bottleneck": "GPU count for parallel ablation sweeps (each model requires full H100 for forward passes with intervention hooks). Secondary: FActScore evaluation requires GPT-4 API calls.",
      "risk_note": "Primary risk: timing hypothesis may not hold for multi-sentence generation (validated Attractor Geometry insight was on factoid completion). Mitigation: look-ahead variant as fallback. Secondary risk: Mahalanobis may not significantly outperform Euclidean (Hallucination Basins uses Euclidean successfully)—in that case, the contribution shifts to sentence-level gating + per-layer controller as primary novelty."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026)"
  ],
  "level": "top-tier",
  "key_references": [
    "Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination (arXiv 2605.05686, May 2026)",
    "Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations (arXiv 2604.04743, April 2026)",
    "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025 Outstanding Paper, arXiv 2503.14477)",
    "Tethered Reasoning (HELIX): Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering (arXiv 2602.17691, Feb 2026)",
    "Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method (ACT, WWW 2025)",
    "ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment (ICLR 2026, arXiv 2602.17560)",
    "Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (arXiv 2605.13772, May 2026)",
    "DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness (arXiv 2601.14210, Jan 2026)",
    "Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs (arXiv 2505.20309, May 2025)",
    "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits (PCNet, arXiv 2605.05953, May 2026)",
    "Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics (arXiv 2604.15400, April 2026)",
    "Think in Sentences: Explicit Sentence Boundaries Enhance Language Model's Capabilities (arXiv 2604.10135, April 2026)",
    "A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks (Lee et al., NeurIPS 2018)",
    "Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors (SADI, arXiv 2410.12299, 2024)",
    "Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models (ICLR 2026)",
    "Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation (ACL Findings 2025)"
  ],
  "description": "We propose Geometry-Triggered Steering (GTS), a method that bridges the detection-to-intervention gap by translating geometric hallucination theory into practical, sentence-gated activation steering. Building on the insight that factual hallucination corresponds to 'basin absence' in hidden-state attractor geometry (Liang et al., May 2026), GTS monitors PCA-regularized Mahalanobis distance from residual stream activations to factual cluster centroids at sentence boundaries during generation. When geometric margin indicates basin absence, GTS computes an input-specific steering vector directed toward the factual centroid and applies it with per-layer weights predicted by a lightweight learned controller.\n\nGTS addresses specific limitations of the most direct prior work: (1) vs. Hallucination Basins (2604.04743), which applies geometry-aware steering at per-sequence granularity with a single scalar controller on 1B–3B models, GTS introduces sentence-level gating that enables within-sequence selectivity (steering only uncertain claims while preserving correct ones), PCA-regularized Mahalanobis distance (capturing directional covariance vs. isotropic Euclidean), and a per-layer MLP controller at 8B scale; (2) vs. Verbal Uncertainty Feature Calibration (Ji et al., EMNLP 2025), which calibrates confidence expression without correcting the underlying generation, GTS detects knowledge absence and actively redirects toward factual representations—catching the critical failure mode of confident hallucinations that show no verbal uncertainty; (3) vs. PCNet's token-level contrastive decoding, GTS operates at sentence granularity—the natural unit of factual claims—avoiding per-token overhead while matching the abstraction level at which hallucination manifests semantically.\n\nWe explicitly validate the timing hypothesis (margin at boundary N predicts factuality of sentence N+1) with a correlation study, provide a look-ahead fallback, and include ablations isolating each design choice against Hallucination Basins' approach. Implementation uses nnsight 0.6 on Qwen3-8B and Llama-3.1-8B-Instruct, evaluating on TruthfulQA, HaluEval, FaithBench, FActScore, FELM, SimpleQA, LongFact, MT-Bench, MMLU, plus ECE/Brier calibration metrics.",
  "project_name": "geometry_triggered_steering",
  "source": "web_research"
}

## Reviewer feedback (round 3)
Issues: ["MISSING CRITICAL COMPETITOR: Spherical Steering (arXiv 2602.08169, ICML 2026) proposes geometry-aware activation rotation with a 'confidence gate that dynamically modulates steering strength based on input uncertainty' — this is conceptually very close to GTS's trigger-then-steer paradigm but uses rotation instead of addition, achieving +10% on TruthfulQA while preserving generation quality. This paper is NOT cited and must be discussed as a baseline.", "MISSING COMPETITOR: 'Minimizing Collateral Damage in Activation Steering' (arXiv 2605.01167, May 2026) directly addresses the utility-preservation problem that GTS claims sentence-level gating solves, but via a constrained optimization framework. This is an alternative solution to the same problem that should be compared.", "MISSING COMPETITOR: FLAS (Flow-based Activation Steering, arXiv 2605.05892, May 2026) learns a concept-conditioned velocity field that transports activations, claiming to outperform existing steering methods including those on TruthfulQA. This represents another geometry-aware steering approach not discussed.", "CHERRY-PICKED AUROC CLAIM: The description implies geometric margin achieves 'AUROC 0.993–1.000' but this is on synthetic factoid tasks. On TruthfulQA, the actual AUROC is 0.858 — a 14-point gap that significantly weakens the trigger reliability argument. The proposal must report the TruthfulQA AUROC and discuss implications for trigger precision/recall.", "TIMING HYPOTHESIS REMAINS HIGH-RISK: The Attractor Geometry paper tests ONLY first-token factoid completion on synthetic and controlled tasks. Extrapolating to 'margin at sentence boundary N predicts sentence N+1 factuality' during multi-sentence open-ended generation is a substantial leap. The look-ahead fallback (extracting margin from first 3 tokens) is reasonable but introduces latency and complexity not accounted for in the resource estimate.", "OVER-INTERPRETATION OF 'Think in Sentences': The proposal claims this paper provides 'theoretical support for why geometric margin at these positions may be predictive of subsequent sentence quality.' However, the paper is a prompting strategy paper that shows attention concentration at delimiters — it does NOT analyze hidden-state geometry at sentence boundaries and provides no evidence about geometric margin predictiveness.", "MAHALANOBIS vs EUCLIDEAN: The proposal positions PCA-regularized Mahalanobis as an advantage over Hallucination Basins' Euclidean, citing OOD detection literature (Lee et al. 2018). However, (1) Hallucination Basins works successfully with Euclidean, (2) the Attractor Geometry paper also uses Euclidean and achieves strong results, and (3) the benefit of Mahalanobis in THIS setting (high-dim LLM residual streams with limited calibration data) is undemonstrated. The ablation is planned but this is a risk to the primary novelty claim if Mahalanobis doesn't significantly outperform Euclidean.", "RESOURCE ESTIMATE CONCERN: Running FActScore evaluation on multi-model outputs requires significant GPT-4 API costs (not included in the estimate). FActScore evaluates ~130-205 entailment checks per biography and takes ~100 seconds per response. With 2 models × multiple conditions × hundreds of examples, API costs could be $200-500+ on top of GPU costs.", "SCALE COMPARISON WEAKNESS: GTS claims to operate at '8B scale, vs. Hallucination Basins' 1B-3B' as an advance. But the Attractor Geometry paper also tested on models up to 14B and Hallucination Basins tested basin detection on Llama-3.1-8B. Scale alone is not a contribution."]
Feedback: The idea has improved substantially from rounds 1-2 and now has a clear, well-articulated pipeline. The core concept of sentence-level selective steering is sound. However, three critical issues remain:

1. **Cite and compare against Spherical Steering (ICML 2026, arXiv 2602.08169)**: This paper's confidence gate + geometry-aware rotation is the closest competitor to GTS's trigger + steer paradigm. You MUST position against it. Key differentiation: Spherical Steering uses rotation (preserving norm) with a general confidence gate, while GTS uses centroid-directed addition with a geometry-specific Mahalanobis trigger. Argue that GTS's trigger is more principled (basin-distance-based) and its sentence-level granularity enables within-sequence selectivity that Spherical Steering lacks (it applies uniformly). Also cite 'Minimizing Collateral Damage' (2605.01167) as an alternative approach to utility preservation.

2. **Fix the AUROC reporting**: Currently the 0.993-1.000 AUROC is prominently featured but comes from synthetic factoid tasks. The TruthfulQA AUROC is 0.858 — still useful as a trigger but with much higher false-positive/negative rates. Be honest about this: 'Geometric margin achieves AUROC 0.858 on TruthfulQA (vs. entropy's 0.622), sufficient for selective intervention with appropriate thresholding, though precision-recall tradeoffs require careful calibration.' This honesty actually strengthens the paper because it motivates the ablation study.

3. **De-emphasize 'Think in Sentences' as geometric evidence**: This paper shows attention concentration, not hidden-state geometry. Cite it as motivating the sentence-as-unit-of-planning hypothesis, not as providing geometric evidence. The timing hypothesis must stand on its own empirical validation (which the proposal already plans).

Minor improvements: (a) Add FActScore API costs to the resource estimate (~$200-400). (b) Acknowledge that if Mahalanobis doesn't significantly outperform Euclidean, the novelty shifts primarily to sentence-level gating + per-layer controller. (c) Drop the 'AUROC 0.993-1.000' framing and lead with the TruthfulQA number instead.

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.
- Address each issue specifically.

## 深度调研要求（每一轮修订都必须执行）

不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。
   - 搜索最新的相关论文（arXiv, conference proceedings）
   - 搜索 benchmark/leaderboard 确认当前 SOTA
   - 搜索可能遗漏的相关工作和 concurrent work

2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，
   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。

3. **深度思考**：在修订之前，先独立思考以下问题：
   - 这个 idea 的核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach 来解决同一个核心问题？
   - 修订后的 idea 相比上一版有什么本质性的改进？

4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，
   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。

## 针对 Review 意见的定向搜索

对 reviewer 指出的每个问题，执行以下搜索流程：

1. **如果 reviewer 说'已有类似工作'**：
   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读
   - 搜索该论文的 cited-by，找到后续跟进工作
   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot

2. **如果 reviewer 说'SOTA 过时'**：
   - 用 Papers With Code 查看当前排行榜
   - 搜索过去 6 个月的最新方法
   - 更新你的 landscape 和 baseline

3. **如果 reviewer 说'可行性有问题'**：
   - 搜索类似规模实验的实际成本和时间线
   - 搜索 GitHub 上是否有可复用的实现
   - 搜索相关数据集/模型的可获取性

4. **如果 reviewer 说'novelty 不足'**：
   - 对核心方法尽量做 3-5 种不同关键词组合的搜索
   - 搜索相邻领域是否有类似思路
   - 如果确实 novelty 不足，考虑 major revision 或 pivot

- Use WebSearch to find updated information if the reviewer flagged outdated claims.
- You have full freedom in how much to change:
  - Minor fix: if only specific details are wrong, correct them and keep everything else.
  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.
  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.
- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.
- In the output JSON, include a "change_type" field with one of: "minor", "major", or "pivot" to indicate the scope of your changes.
- Output the revised idea as a COMPLETE JSON object (same schema as original, plus "change_type").

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "43455a43-f601-4f83-8fa7-df33f42d6c19",
  "type": "user",
  "uuid": "34bbb9bd-4d72-42ae-ba30-794af2d90b20",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T08:40:42.898Z_

```json
{
  "parentUuid": "34bbb9bd-4d72-42ae-ba30-794af2d90b20",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "37bbd065-8e76-4087-a18b-e0fec9b0ad1c",
  "timestamp": "2026-05-16T08:40:42.898Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T08:40:42.898Z_

```json
{
  "parentUuid": "37bbd065-8e76-4087-a18b-e0fec9b0ad1c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "468b2e3f-a6a4-4bc9-8d33-e9f003332e60",
  "timestamp": "2026-05-16T08:40:42.898Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-16 (UTC).**  ## Original idea {   \"title\": \"Geometry-Triggered Sentence-Level Activation Steering for Factual Hall…",
  "leafUuid": "468b2e3f-a6a4-4bc9-8d33-e9f003332e60",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising geometry-triggered steering with competitor analysis",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb"
}
```

---

### Assistant

_source line 8 · 2026-05-16T08:40:51.211Z_

<details><summary>Logged reasoning block</summary>

```text
The reviewer has raised several important issues in round 3. Let me analyze them:

1. **Missing critical competitor: Spherical Steering (arXiv 2602.08169, ICML 2026)** - Need to search for this paper and understand its approach
2. **Missing competitor: 'Minimizing Collateral Damage in Activation Steering' (arXiv 2605.01167)** - Need to find and understand this
3. **Missing competitor: FLAS (Flow-based Activation Steering, arXiv 2605.05892)** - Need to find and understand this


4. **Cherry-picked AUROC claim** - Need to fix reporting to be honest about TruthfulQA AUROC of 0.858
5. **Timing hypothesis risk** - Need to better acknowledge this
6. **Over-interpretation of 'Think in Sentences'** - Need to de-emphasize
7. **Mahalanobis vs Euclidean risk** - Need to acknowledge
8. **Resource estimate missing FActScore API costs** - Need to add
9. **Scale comparison weakness** - Need to de-emphasize scale as contribution

I need to search for these key papers the reviewer mentioned to properly understand their approaches before revising the manuscript.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "468b2e3f-a6a4-4bc9-8d33-e9f003332e60",
  "isSidechain": false,
  "requestId": "req_011Cb5wxqLgbDWNoH87MSjup",
  "type": "assistant",
  "uuid": "1750c25c-59b5-449b-9988-8cc50d54af19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3wH3z9isgeY4C7FrcYtg9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12442,
      "cache_read_input_tokens": 11841,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12442,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 404,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12442,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12442
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

_source line 9 · 2026-05-16T08:40:51.213Z_

I'll research the missing competitors and key claims flagged by the reviewer before revising the idea.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1750c25c-59b5-449b-9988-8cc50d54af19",
  "isSidechain": false,
  "requestId": "req_011Cb5wxqLgbDWNoH87MSjup",
  "type": "assistant",
  "uuid": "61927316-d964-4d58-a12d-9742f27148e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3wH3z9isgeY4C7FrcYtg9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12442,
      "cache_read_input_tokens": 11841,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12442,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 404,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12442,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12442
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

_source line 10 · 2026-05-16T08:40:51.237Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TmywcFVJu8SZEXedhKSHJT`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61927316-d964-4d58-a12d-9742f27148e2",
  "isSidechain": false,
  "requestId": "req_011Cb5wxqLgbDWNoH87MSjup",
  "type": "assistant",
  "uuid": "bb96418a-850c-4dea-b619-92295727e8cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3wH3z9isgeY4C7FrcYtg9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12442,
      "cache_read_input_tokens": 11841,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12442,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 404,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12442,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12442
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

_source line 11 · 2026-05-16T08:40:51.243Z_

<details><summary>↩ Tool result · `toolu_01TmywcFVJu8SZEXedhKSHJT`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb96418a-850c-4dea-b619-92295727e8cc",
  "isSidechain": false,
  "promptId": "43455a43-f601-4f83-8fa7-df33f42d6c19",
  "type": "user",
  "uuid": "4c95f80e-434c-483e-97e5-8d7d1745dcaf",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "bb96418a-850c-4dea-b619-92295727e8cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-16T08:40:54.562Z_

<details><summary>Logged reasoning block</summary>

```text
Let me search for the three missing competitors and verify the AUROC claims. I'll do multiple searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c95f80e-434c-483e-97e5-8d7d1745dcaf",
  "isSidechain": false,
  "requestId": "req_011Cb5wySJcwiT4Nr2tWYuzS",
  "type": "assistant",
  "uuid": "8eb5b40d-96c9-411d-9da5-8adeb88d6c15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqEURuuA6FYTk8xHtLJ7wv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1423,
      "cache_read_input_tokens": 24283,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1423,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 316,
          "cache_read_input_tokens": 24283,
          "cache_creation_input_tokens": 1423,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1423
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

_source line 13 · 2026-05-16T08:40:55.078Z_

Let me research the missing competitors and verify key claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8eb5b40d-96c9-411d-9da5-8adeb88d6c15",
  "isSidechain": false,
  "requestId": "req_011Cb5wySJcwiT4Nr2tWYuzS",
  "type": "assistant",
  "uuid": "56ce7789-d31b-400d-906b-f700f098a792",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqEURuuA6FYTk8xHtLJ7wv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1423,
      "cache_read_input_tokens": 24283,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1423,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 316,
          "cache_read_input_tokens": 24283,
          "cache_creation_input_tokens": 1423,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1423
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

_source line 14 · 2026-05-16T08:40:55.738Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AQyd2wNyF6JfmFsMrxxMbD`</summary>

```json
{
  "query": "Spherical Steering arXiv 2602.08169 ICML 2026 geometry-aware activation rotation confidence gate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56ce7789-d31b-400d-906b-f700f098a792",
  "isSidechain": false,
  "requestId": "req_011Cb5wySJcwiT4Nr2tWYuzS",
  "type": "assistant",
  "uuid": "36ff0cd7-e7b3-4235-89fb-5fdee4b141f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqEURuuA6FYTk8xHtLJ7wv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1423,
      "cache_read_input_tokens": 24283,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1423,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 316,
          "cache_read_input_tokens": 24283,
          "cache_creation_input_tokens": 1423,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1423
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

_source line 15 · 2026-05-16T08:40:56.689Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011jqJELEsuFS6yH5NQqczNw`</summary>

```json
{
  "query": "\"Minimizing Collateral Damage\" activation steering arXiv 2605.01167 2026 constrained optimization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36ff0cd7-e7b3-4235-89fb-5fdee4b141f7",
  "isSidechain": false,
  "requestId": "req_011Cb5wySJcwiT4Nr2tWYuzS",
  "type": "assistant",
  "uuid": "2ab20f97-8526-49a0-9aff-ff9f6980b16b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqEURuuA6FYTk8xHtLJ7wv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1423,
      "cache_read_input_tokens": 24283,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1423,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 316,
          "cache_read_input_tokens": 24283,
          "cache_creation_input_tokens": 1423,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1423
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

_source line 16 · 2026-05-16T08:40:57.220Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ARutKXZeVq4mkGWDctDzjv`</summary>

```json
{
  "query": "FLAS flow-based activation steering arXiv 2605.05892 concept-conditioned velocity field 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ab20f97-8526-49a0-9aff-ff9f6980b16b",
  "isSidechain": false,
  "requestId": "req_011Cb5wySJcwiT4Nr2tWYuzS",
  "type": "assistant",
  "uuid": "31186a6b-7e52-413a-afaf-52e77585afbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqEURuuA6FYTk8xHtLJ7wv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1423,
      "cache_read_input_tokens": 24283,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1423,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 316,
          "cache_read_input_tokens": 24283,
          "cache_creation_input_tokens": 1423,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1423
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

_source line 17 · 2026-05-16T08:40:57.826Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CJeGbyEDWXCWt5VjEBFakV`</summary>

```json
{
  "query": "Attractor Geometry Transformer Memory arXiv 2605.05686 TruthfulQA AUROC results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31186a6b-7e52-413a-afaf-52e77585afbf",
  "isSidechain": false,
  "requestId": "req_011Cb5wySJcwiT4Nr2tWYuzS",
  "type": "assistant",
  "uuid": "288aa0c0-ea5f-4766-b54b-12660d90b134",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqEURuuA6FYTk8xHtLJ7wv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1423,
      "cache_read_input_tokens": 24283,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1423,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 316,
          "cache_read_input_tokens": 24283,
          "cache_creation_input_tokens": 1423,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1423
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

_source line 18 · 2026-05-16T08:41:02.979Z_

<details><summary>↩ Tool result · `toolu_01AQyd2wNyF6JfmFsMrxxMbD`</summary>

```text
Web search results for query: "Spherical Steering arXiv 2602.08169 ICML 2026 geometry-aware activation rotation confidence gate"

Links: [{"title":"[2602.08169] Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/abs/2602.08169"},{"title":"Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/pdf/2602.08169"},{"title":"GitHub - chili-lab/Spherical-Steering: [ICML 2026] Spherical Steering: Geometry-Aware Activation Rotation for Language Models · GitHub","url":"https://github.com/chili-lab/Spherical-Steering"},{"title":"(PDF) Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://www.researchgate.net/publication/400605038_Spherical_Steering_Geometry-Aware_Activation_Rotation_for_Language_Models"},{"title":"Steer2Edit: From Activation Steering to Component-Level Editing","url":"https://arxiv.org/html/2602.09870"},{"title":"On the Non-Identifiability of Steering Vectors in Large Language Models","url":"https://arxiv.org/html/2602.06801v4"},{"title":"Identifiable Steering via Sparse Autoencoding of Multi-Concept Shifts","url":"https://arxiv.org/html/2502.12179v1"},{"title":"Reliable Control-Point Selection for Steering Reasoning in ...","url":"https://arxiv.org/pdf/2604.02113"},{"title":"Curveball Steering: The Right Direction To Steer Isn’t Always Linear","url":"https://arxiv.org/html/2603.09313v1"},{"title":"(PDF) Steering LLMs via Scalable Interactive Oversight","url":"https://www.researchgate.net/publication/400459769_Steering_LLMs_via_Scalable_Interactive_Oversight"}]

Based on the search results, I found comprehensive information about the paper you're looking for:

## Spherical Steering: Geometry-Aware Activation Rotation for Language Models

**arXiv:2602.08169** was submitted on February 9, 2026, by authors Zejia You, Chunyuan Deng, and Hanjie Chen, and the paper has been accepted to ICML 2026.

### Core Concept

The paper addresses inference-time steering of language models without retraining. Standard approaches rely on activation addition, which inevitably alters the magnitude of hidden representations, raising concerns about representation collapse and degradation of open-ended generation capabilities.

### Solution Approach

Spherical Steering is a training-free primitive that resolves this trade-off through activation rotation. Rather than shifting activations with a fixed vector, the method rotates them along a geodesic toward a target direction, guiding the activation toward the target concept while preserving the integrity of the representation.

### Implementation Details

The paper compares the proposed method against several baselines including ITI (In-context Influence), CAA (Contrastive Activation Addition), SADI-HEAD, and ICL (In-context Learning) approaches, as shown in experimental evaluations comparing multiple choice accuracy versus generation quality.

You can access the full paper at the arXiv link: https://arxiv.org/abs/2602.08169, and the code is available on GitHub at https://github.com/chili-lab/Spherical-Steering.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36ff0cd7-e7b3-4235-89fb-5fdee4b141f7",
  "isSidechain": false,
  "promptId": "43455a43-f601-4f83-8fa7-df33f42d6c19",
  "type": "user",
  "uuid": "f908847f-f8ba-4180-a387-b17f63ee0683",
  "toolUseResult": {
    "query": "Spherical Steering arXiv 2602.08169 ICML 2026 geometry-aware activation rotation confidence gate",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WModuvxcn4rj9mjxViSPbR",
        "content": [
          {
            "title": "[2602.08169] Spherical Steering: Geometry-Aware Activation Rotation for Language Models",
            "url": "https://arxiv.org/abs/2602.08169"
          },
          {
            "title": "Spherical Steering: Geometry-Aware Activation Rotation for Language Models",
            "url": "https://arxiv.org/pdf/2602.08169"
          },
          {
            "title": "GitHub - chili-lab/Spherical-Steering: [ICML 2026] Spherical Steering: Geometry-Aware Activation Rotation for Language Models · GitHub",
            "url": "https://github.com/chili-lab/Spherical-Steering"
          },
          {
            "title": "(PDF) Spherical Steering: Geometry-Aware Activation Rotation for Language Models",
            "url": "https://www.researchgate.net/publication/400605038_Spherical_Steering_Geometry-Aware_Activation_Rotation_for_Language_Models"
          },
          {
            "title": "Steer2Edit: From Activation Steering to Component-Level Editing",
            "url": "https://arxiv.org/html/2602.09870"
          },
          {
            "title": "On the Non-Identifiability of Steering Vectors in Large Language Models",
            "url": "https://arxiv.org/html/2602.06801v4"
          },
          {
            "title": "Identifiable Steering via Sparse Autoencoding of Multi-Concept Shifts",
            "url": "https://arxiv.org/html/2502.12179v1"
          },
          {
            "title": "Reliable Control-Point Selection for Steering Reasoning in ...",
            "url": "https://arxiv.org/pdf/2604.02113"
          },
          {
            "title": "Curveball Steering: The Right Direction To Steer Isn’t Always Linear",
            "url": "https://arxiv.org/html/2603.09313v1"
          },
          {
            "title": "(PDF) Steering LLMs via Scalable Interactive Oversight",
            "url": "https://www.researchgate.net/publication/400459769_Steering_LLMs_via_Scalable_Interactive_Oversight"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about the paper you're looking for:\n\n## Spherical Steering: Geometry-Aware Activation Rotation for Language Models\n\n**arXiv:2602.08169** was submitted on February 9, 2026, by authors Zejia You, Chunyuan Deng, and Hanjie Chen, and the paper has been accepted to ICML 2026.\n\n### Core Concept\n\nThe paper addresses inference-time steering of language models without retraining. Standard approaches rely on activation addition, which inevitably alters the magnitude of hidden representations, raising concerns about representation collapse and degradation of open-ended generation capabilities.\n\n### Solution Approach\n\nSpherical Steering is a training-free primitive that resolves this trade-off through activation rotation. Rather than shifting activations with a fixed vector, the method rotates them along a geodesic toward a target direction, guiding the activation toward the target concept while preserving the integrity of the representation.\n\n### Implementation Details\n\nThe paper compares the proposed method against several baselines including ITI (In-context Influence), CAA (Contrastive Activation Addition), SADI-HEAD, and ICL (In-context Learning) approaches, as shown in experimental evaluations comparing multiple choice accuracy versus generation quality.\n\nYou can access the full paper at the arXiv link: https://arxiv.org/abs/2602.08169, and the code is available on GitHub at https://github.com/chili-lab/Spherical-Steering."
    ],
    "durationSeconds": 7.236002260999999
  },
  "sourceToolAssistantUUID": "36ff0cd7-e7b3-4235-89fb-5fdee4b141f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-16T08:41:03.777Z_

<details><summary>↩ Tool result · `toolu_01ARutKXZeVq4mkGWDctDzjv`</summary>

```text
Web search results for query: "FLAS flow-based activation steering arXiv 2605.05892 concept-conditioned velocity field 2026"

Links: [{"title":"[2605.05892] Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention","url":"https://arxiv.org/abs/2605.05892"},{"title":"Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention","url":"https://arxiv.org/html/2605.05892"},{"title":"[2605.06342] Don't Lose Focus: Activation Steering via Key-Orthogonal Projections","url":"https://arxiv.org/abs/2605.06342"},{"title":"[2605.03907v1] Steer Like the LLM: Activation Steering that Mimics Prompting","url":"https://arxiv.org/abs/2605.03907v1"},{"title":"Steering Large Reasoning Models towards Concise Reasoning via Flow Matching","url":"https://arxiv.org/html/2602.05539"},{"title":"STEERING LANGUAGE MODELS WITH ACTIVATION EN","url":"https://openreview.net/pdf?id=2XBPdPIcFK"},{"title":"Steering Large Reasoning Models towards Concise Reason","url":"https://www.arxiv.org/pdf/2602.05539"},{"title":"[2605.03907] Steer Like the LLM: Activation Steering that Mimics Prompting","url":"https://arxiv.org/abs/2605.03907"},{"title":"Steer Like the LLM: Activation Steering that Mimics Prompting","url":"https://arxiv.org/html/2605.03907v1"},{"title":"[2308.10248] Steering Language Models With Activation Engineering","url":"https://arxiv.org/abs/2308.10248"}]

Based on the search results, I found information about the paper you're looking for:

FLAS (Flow-based Activation Steering) learns a general, concept-conditioned velocity field that transports unsteered activations to steered ones without relying on simplifying assumptions.

The paper was published on May 7, 2026, by researchers from Georgia Institute of Technology including Zehao Jin, Ruixuan Deng, Junran Wang, Xinjie Shen, and Chao Zhang.

The key innovation of FLAS addresses limitations in existing activation steering methods. Existing steering methods are often outperformed by simple in-context prompting and generalize poorly to unseen concepts due to unvalidated simplifying assumptions that restrict steering interventions to fixed, single-step, position-invariant transforms.

FLAS replaces a fixed one-step intervention with a learned, time-conditioned velocity field where the velocity depends on the current activation state, allowing the intervention to adapt as the activation evolves and follow curved trajectories through activation space when integrated over multiple steps. The method trains on positive examples under a standard language-modeling objective without requiring contrastive pairs.

FLAS is the first learned steering method to consistently outperform prompting on AxBench and generalizes to held-out concepts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31186a6b-7e52-413a-afaf-52e77585afbf",
  "isSidechain": false,
  "promptId": "43455a43-f601-4f83-8fa7-df33f42d6c19",
  "type": "user",
  "uuid": "4dfbab43-c8d6-49a7-b221-ea9b82baaf9d",
  "toolUseResult": {
    "query": "FLAS flow-based activation steering arXiv 2605.05892 concept-conditioned velocity field 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XvvGpiJk2nbAZuoacXbpje",
        "content": [
          {
            "title": "[2605.05892] Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention",
            "url": "https://arxiv.org/abs/2605.05892"
          },
          {
            "title": "Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention",
            "url": "https://arxiv.org/html/2605.05892"
          },
          {
            "title": "[2605.06342] Don't Lose Focus: Activation Steering via Key-Orthogonal Projections",
            "url": "https://arxiv.org/abs/2605.06342"
          },
          {
            "title": "[2605.03907v1] Steer Like the LLM: Activation Steering that Mimics Prompting",
            "url": "https://arxiv.org/abs/2605.03907v1"
          },
          {
            "title": "Steering Large Reasoning Models towards Concise Reasoning via Flow Matching",
            "url": "https://arxiv.org/html/2602.05539"
          },
          {
            "title": "STEERING LANGUAGE MODELS WITH ACTIVATION EN",
            "url": "https://openreview.net/pdf?id=2XBPdPIcFK"
          },
          {
            "title": "Steering Large Reasoning Models towards Concise Reason",
            "url": "https://www.arxiv.org/pdf/2602.05539"
          },
          {
            "title": "[2605.03907] Steer Like the LLM: Activation Steering that Mimics Prompting",
            "url": "https://arxiv.org/abs/2605.03907"
          },
          {
            "title": "Steer Like the LLM: Activation Steering that Mimics Prompting",
            "url": "https://arxiv.org/html/2605.03907v1"
          },
          {
            "title": "[2308.10248] Steering Language Models With Activation Engineering",
            "url": "https://arxiv.org/abs/2308.10248"
          }
        ]
      },
      "Based on the search results, I found information about the paper you're looking for:\n\nFLAS (Flow-based Activation Steering) learns a general, concept-conditioned velocity field that transports unsteered activations to steered ones without relying on simplifying assumptions.\n\nThe paper was published on May 7, 2026, by researchers from Georgia Institute of Technology including Zehao Jin, Ruixuan Deng, Junran Wang, Xinjie Shen, and Chao Zhang.\n\nThe key innovation of FLAS addresses limitations in existing activation steering methods. Existing steering methods are often outperformed by simple in-context prompting and generalize poorly to unseen concepts due to unvalidated simplifying assumptions that restrict steering interventions to fixed, single-step, position-invariant transforms.\n\nFLAS replaces a fixed one-step intervention with a learned, time-conditioned velocity field where the velocity depends on the current activation state, allowing the intervention to adapt as the activation evolves and follow curved trajectories through activation space when integrated over multiple steps. The method trains on positive examples under a standard language-modeling objective without requiring contrastive pairs.\n\nFLAS is the first learned steering method to consistently outperform prompting on AxBench and generalizes to held-out concepts."
    ],
    "durationSeconds": 6.553973851
  },
  "sourceToolAssistantUUID": "31186a6b-7e52-413a-afaf-52e77585afbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T08:41:03.781Z_

<details><summary>↩ Tool result · `toolu_01CJeGbyEDWXCWt5VjEBFakV`</summary>

```text
Web search results for query: "Attractor Geometry Transformer Memory arXiv 2605.05686 TruthfulQA AUROC results"

Links: [{"title":"[2605.05686] Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination","url":"https://arxiv.org/abs/2605.05686"},{"title":"Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination","url":"https://arxiv.org/html/2605.05686"},{"title":"The Geometry of Truth: Layer-wise Semantic Dynamics for Hallucination Detection in Large Language Models","url":"https://arxiv.org/html/2510.04933v1"},{"title":"Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations","url":"https://arxiv.org/html/2604.04743"},{"title":"A Geometric Taxonomy of Hallucinations in LLMs","url":"https://arxiv.org/html/2602.13224"},{"title":"[2605.12466] Solve the Loop: Attractor Models for Language and Reasoning","url":"https://arxiv.org/abs/2605.12466"},{"title":"Self-attention as an attractor network: transient memories without backpropagation M. N. acknowledges the support of PNRR MUR Project No. PE0000013-FAIR.","url":"https://arxiv.org/html/2409.16112v1"},{"title":"The Bayesian Geometry of Transformer Attention","url":"https://arxiv.org/html/2512.22471v3"},{"title":"Understanding and controlling the geometry of memory organization in RNNs","url":"https://arxiv.org/html/2502.07256"},{"title":"Memory-Augmented Transformers: A Systematic Review from Neuroscience Principles to Technical Solutions","url":"https://arxiv.org/html/2508.10824v1"}]

Based on the search results, I found the arXiv paper 2605.05686 titled "Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination," but the search results do not contain specific TruthfulQA AUROC results from this paper.

The abstract and content from the paper discusses learned facts forming attractor basins in the hidden-state space, with conflict being basin competition where working memory disrupts convergence to the correct basin without raising output entropy, and hallucination being basin absence where the hidden state drifts freely when no memorized basin exists.

The paper introduces geometric margin—the hidden state's distance to the nearest memorized basin—which separates correct recall from hallucination far more cleanly than output entropy, with zero false refusals where entropy-based detection cannot avoid rejecting the vast majority of correct outputs.

However, the search results do not provide the specific TruthfulQA AUROC numerical results from paper 2605.05686. To find those specific metrics, you would need to access the full paper directly on arXiv at https://arxiv.org/abs/2605.05686.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "288aa0c0-ea5f-4766-b54b-12660d90b134",
  "isSidechain": false,
  "promptId": "43455a43-f601-4f83-8fa7-df33f42d6c19",
  "type": "user",
  "uuid": "b0a1975d-53c5-4081-9ce0-9931c08bd708",
  "toolUseResult": {
    "query": "Attractor Geometry Transformer Memory arXiv 2605.05686 TruthfulQA AUROC results",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XnWNJd1gsLUswnjmbkAsx3",
        "content": [
          {
            "title": "[2605.05686] Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination",
            "url": "https://arxiv.org/abs/2605.05686"
          },
          {
            "title": "Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination",
            "url": "https://arxiv.org/html/2605.05686"
          },
          {
            "title": "The Geometry of Truth: Layer-wise Semantic Dynamics for Hallucination Detection in Large Language Models",
            "url": "https://arxiv.org/html/2510.04933v1"
          },
          {
            "title": "Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations",
            "url": "https://arxiv.org/html/2604.04743"
          },
          {
            "title": "A Geometric Taxonomy of Hallucinations in LLMs",
            "url": "https://arxiv.org/html/2602.13224"
          },
          {
            "title": "[2605.12466] Solve the Loop: Attractor Models for Language and Reasoning",
            "url": "https://arxiv.org/abs/2605.12466"
          },
          {
            "title": "Self-attention as an attractor network: transient memories without backpropagation M. N. acknowledges the support of PNRR MUR Project No. PE0000013-FAIR.",
            "url": "https://arxiv.org/html/2409.16112v1"
          },
          {
            "title": "The Bayesian Geometry of Transformer Attention",
            "url": "https://arxiv.org/html/2512.22471v3"
          },
          {
            "title": "Understanding and controlling the geometry of memory organization in RNNs",
            "url": "https://arxiv.org/html/2502.07256"
          },
          {
            "title": "Memory-Augmented Transformers: A Systematic Review from Neuroscience Principles to Technical Solutions",
            "url": "https://arxiv.org/html/2508.10824v1"
          }
        ]
      },
      "Based on the search results, I found the arXiv paper 2605.05686 titled \"Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination,\" but the search results do not contain specific TruthfulQA AUROC results from this paper.\n\nThe abstract and content from the paper discusses learned facts forming attractor basins in the hidden-state space, with conflict being basin competition where working memory disrupts convergence to the correct basin without raising output entropy, and hallucination being basin absence where the hidden state drifts freely when no memorized basin exists.\n\nThe paper introduces geometric margin—the hidden state's distance to the nearest memorized basin—which separates correct recall from hallucination far more cleanly than output entropy, with zero false refusals where entropy-based detection cannot avoid rejecting the vast majority of correct outputs.\n\nHowever, the search results do not provide the specific TruthfulQA AUROC numerical results from paper 2605.05686. To find those specific metrics, you would need to access the full paper directly on arXiv at https://arxiv.org/abs/2605.05686."
    ],
    "durationSeconds": 5.929878873999998
  },
  "sourceToolAssistantUUID": "288aa0c0-ea5f-4766-b54b-12660d90b134",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-16 (UTC).**  ## Original idea {   \"title\": \"Geometry-Triggered Sentence-Level Activation Steering for Factual Hall…",
  "leafUuid": "b0a1975d-53c5-4081-9ce0-9931c08bd708",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising geometry-triggered steering with competitor analysis",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb"
}
```

---

### Tool result

_source line 23 · 2026-05-16T08:41:04.388Z_

<details><summary>↩ Tool result · `toolu_011jqJELEsuFS6yH5NQqczNw`</summary>

```text
Web search results for query: ""Minimizing Collateral Damage" activation steering arXiv 2605.01167 2026 constrained optimization"

Links: [{"title":"[2605.01167] Minimizing Collateral Damage in Activation Steering","url":"https://arxiv.org/abs/2605.01167"},{"title":"Minimizing Collateral Damage in Activation Steering","url":"https://arxiv.org/html/2605.01167v1"},{"title":"Minimizing Collateral Damage in Activation Steering","url":"https://www.researchgate.net/publication/404427927_Minimizing_Collateral_Damage_in_Activation_Steering"},{"title":"[2605.06342] Don't Lose Focus: Activation Steering via Key-Orthogonal Projections","url":"https://arxiv.org/abs/2605.06342"},{"title":"[2605.10664] Prompt-Activation Duality: Improving Activation Steering via Attention-Level Interventions","url":"https://arxiv.org/abs/2605.10664"},{"title":"[2605.03907v1] Steer Like the LLM: Activation Steering that Mimics Prompting","url":"https://arxiv.org/abs/2605.03907v1"},{"title":"Trojan Activation Attack: Red-Teaming Large Language ...","url":"https://dl.acm.org/doi/pdf/10.1145/3627673.3679821"},{"title":"[2605.05892] Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention","url":"https://arxiv.org/abs/2605.05892"},{"title":"[2605.03907] Steer Like the LLM: Activation Steering that Mimics Prompting","url":"https://arxiv.org/abs/2605.03907"},{"title":"Don’t Lose Focus: Activation Steering via Key-Orthogonal Projections","url":"https://arxiv.org/html/2605.06342"}]

I found the paper you're looking for! Here's what I found:

Activation steering is a method for controlling Large Language Model (LLM) behavior by intervening in its internal representations to increase the alignment with a specific target feature direction. However, standard interventions, such as vector addition, often cause "collateral damage", defined as unintended changes in the alignment of activations along other non-target feature directions.

The paper provides a mathematical formalization of collateral damage and introduces a principled framework that models steering as a constrained optimization problem. The method finds a new activation that minimizes the expected squared collateral change weighted by the empirical second-moment matrix of activations.

The paper was submitted on May 1, 2026 (arXiv:2605.01167) by Tam Nguyen, Tu Anh Nguyen, Sina Alemohammad, and Richard G. Baraniuk. You can access it directly at https://arxiv.org/abs/2605.01167.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ab20f97-8526-49a0-9aff-ff9f6980b16b",
  "isSidechain": false,
  "promptId": "43455a43-f601-4f83-8fa7-df33f42d6c19",
  "type": "user",
  "uuid": "1ce88f75-3bd3-4ba4-bec5-24b07985c0e3",
  "toolUseResult": {
    "query": "\"Minimizing Collateral Damage\" activation steering arXiv 2605.01167 2026 constrained optimization",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XYzAfqjT8FkTPcEVhUoe6P",
        "content": [
          {
            "title": "[2605.01167] Minimizing Collateral Damage in Activation Steering",
            "url": "https://arxiv.org/abs/2605.01167"
          },
          {
            "title": "Minimizing Collateral Damage in Activation Steering",
            "url": "https://arxiv.org/html/2605.01167v1"
          },
          {
            "title": "Minimizing Collateral Damage in Activation Steering",
            "url": "https://www.researchgate.net/publication/404427927_Minimizing_Collateral_Damage_in_Activation_Steering"
          },
          {
            "title": "[2605.06342] Don't Lose Focus: Activation Steering via Key-Orthogonal Projections",
            "url": "https://arxiv.org/abs/2605.06342"
          },
          {
            "title": "[2605.10664] Prompt-Activation Duality: Improving Activation Steering via Attention-Level Interventions",
            "url": "https://arxiv.org/abs/2605.10664"
          },
          {
            "title": "[2605.03907v1] Steer Like the LLM: Activation Steering that Mimics Prompting",
            "url": "https://arxiv.org/abs/2605.03907v1"
          },
          {
            "title": "Trojan Activation Attack: Red-Teaming Large Language ...",
            "url": "https://dl.acm.org/doi/pdf/10.1145/3627673.3679821"
          },
          {
            "title": "[2605.05892] Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention",
            "url": "https://arxiv.org/abs/2605.05892"
          },
          {
            "title": "[2605.03907] Steer Like the LLM: Activation Steering that Mimics Prompting",
            "url": "https://arxiv.org/abs/2605.03907"
          },
          {
            "title": "Don’t Lose Focus: Activation Steering via Key-Orthogonal Projections",
            "url": "https://arxiv.org/html/2605.06342"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I found:\n\nActivation steering is a method for controlling Large Language Model (LLM) behavior by intervening in its internal representations to increase the alignment with a specific target feature direction. However, standard interventions, such as vector addition, often cause \"collateral damage\", defined as unintended changes in the alignment of activations along other non-target feature directions.\n\nThe paper provides a mathematical formalization of collateral damage and introduces a principled framework that models steering as a constrained optimization problem. The method finds a new activation that minimizes the expected squared collateral change weighted by the empirical second-moment matrix of activations.\n\nThe paper was submitted on May 1, 2026 (arXiv:2605.01167) by Tam Nguyen, Tu Anh Nguyen, Sina Alemohammad, and Richard G. Baraniuk. You can access it directly at https://arxiv.org/abs/2605.01167."
    ],
    "durationSeconds": 7.696506566
  },
  "sourceToolAssistantUUID": "2ab20f97-8526-49a0-9aff-ff9f6980b16b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-16T08:41:08.040Z_

Now let me fetch the actual paper contents to understand the details better.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ce88f75-3bd3-4ba4-bec5-24b07985c0e3",
  "isSidechain": false,
  "requestId": "req_011Cb5wzQKqXcihMdook3QRV",
  "type": "assistant",
  "uuid": "313bd098-a818-4322-aa5b-56ef8aa51db8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JbcQEcXr2srhQP6iebZwJN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1594,
      "cache_creation_input_tokens": 2000,
      "cache_read_input_tokens": 25706,
      "output_tokens": 544,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2000,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1594,
          "output_tokens": 544,
          "cache_read_input_tokens": 25706,
          "cache_creation_input_tokens": 2000,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2000
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

_source line 25 · 2026-05-16T08:41:10.418Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FMEmmsgN64FvdJd6PWtEsv`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.08169",
  "prompt": "Extract the full abstract, key method details (how the confidence gate works, what geometry-aware rotation means, how steering strength is modulated), main results on TruthfulQA and other benchmarks, and any limitations. What granularity does it operate at (token, sentence, sequence)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "313bd098-a818-4322-aa5b-56ef8aa51db8",
  "isSidechain": false,
  "requestId": "req_011Cb5wzQKqXcihMdook3QRV",
  "type": "assistant",
  "uuid": "950d8610-f34b-49af-9289-52edba7f3f52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JbcQEcXr2srhQP6iebZwJN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1594,
      "cache_creation_input_tokens": 2000,
      "cache_read_input_tokens": 25706,
      "output_tokens": 544,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2000,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1594,
          "output_tokens": 544,
          "cache_read_input_tokens": 25706,
          "cache_creation_input_tokens": 2000,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2000
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

_source line 26 · 2026-05-16T08:41:11.844Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Uo4SazE177ySvPyUYuo8io`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.01167",
  "prompt": "Extract the full abstract, key method details (how collateral damage is formalized, what the constrained optimization framework looks like, how it preserves utility), main results, and what granularity it operates at. Does it address sentence-level vs sequence-level intervention?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "950d8610-f34b-49af-9289-52edba7f3f52",
  "isSidechain": false,
  "requestId": "req_011Cb5wzQKqXcihMdook3QRV",
  "type": "assistant",
  "uuid": "0a9efb73-3326-476d-bd90-3214c1ceb01b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JbcQEcXr2srhQP6iebZwJN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1594,
      "cache_creation_input_tokens": 2000,
      "cache_read_input_tokens": 25706,
      "output_tokens": 544,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2000,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1594,
          "output_tokens": 544,
          "cache_read_input_tokens": 25706,
          "cache_creation_input_tokens": 2000,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2000
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

_source line 27 · 2026-05-16T08:41:13.265Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HpVRw34TErwvxUxhJuhvU8`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.05892",
  "prompt": "Extract the full abstract, key method details (how the flow-based velocity field works, what concept-conditioning means, how it differs from linear steering), main results especially on TruthfulQA, and limitations. Does it use any geometric trigger or sentence-level gating?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a9efb73-3326-476d-bd90-3214c1ceb01b",
  "isSidechain": false,
  "requestId": "req_011Cb5wzQKqXcihMdook3QRV",
  "type": "assistant",
  "uuid": "26f6ffac-b770-4d4a-a486-35f939326639",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JbcQEcXr2srhQP6iebZwJN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1594,
      "cache_creation_input_tokens": 2000,
      "cache_read_input_tokens": 25706,
      "output_tokens": 544,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2000,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1594,
          "output_tokens": 544,
          "cache_read_input_tokens": 25706,
          "cache_creation_input_tokens": 2000,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2000
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

_source line 28 · 2026-05-16T08:41:15.281Z_

<details><summary>↩ Tool result · `toolu_01FMEmmsgN64FvdJd6PWtEsv`</summary>

```text
# Spherical Steering: Summary

## Full Abstract
"Inference-time steering has emerged as a promising paradigm for controlling language models (LMs) without the cost of retraining. However, standard approaches typically rely on activation addition, a geometric operation that inevitably alters the magnitude of hidden representations."

The approach uses activation rotation along geodesics instead of vector addition, incorporating "a confidence gate that dynamically modulates steering strength based on input uncertainty."

## Key Method Details

**Geometry-Aware Rotation:** Rather than shifting activations with fixed vectors, the technique rotates them toward target directions while preserving signal magnitude—addressing representation collapse issues.

**Confidence Gate:** The mechanism dynamically adjusts steering intensity according to input uncertainty, enabling adaptive control without requiring retraining.

**Steering Modulation:** Strength is controlled through the confidence gate, which evaluates input conditions to determine appropriate intervention levels.

**Operational Granularity:** The abstract does not specify whether steering operates at token, sentence, or sequence levels.

## Main Results

Performance improvements include "+10% on TruthfulQA, COPA, and Storycloze" compared to addition-based methods, while maintaining "the model's general open-ended generation quality."

## Limitations

The document provided contains only the abstract and metadata. Specific limitations, detailed experimental conditions, failure cases, or boundary conditions are not discussed in this excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "950d8610-f34b-49af-9289-52edba7f3f52",
  "isSidechain": false,
  "promptId": "43455a43-f601-4f83-8fa7-df33f42d6c19",
  "type": "user",
  "uuid": "5e2f664a-e2bc-4371-a2d4-9f517054431c",
  "toolUseResult": {
    "bytes": 47357,
    "code": 200,
    "codeText": "OK",
    "result": "# Spherical Steering: Summary\n\n## Full Abstract\n\"Inference-time steering has emerged as a promising paradigm for controlling language models (LMs) without the cost of retraining. However, standard approaches typically rely on activation addition, a geometric operation that inevitably alters the magnitude of hidden representations.\"\n\nThe approach uses activation rotation along geodesics instead of vector addition, incorporating \"a confidence gate that dynamically modulates steering strength based on input uncertainty.\"\n\n## Key Method Details\n\n**Geometry-Aware Rotation:** Rather than shifting activations with fixed vectors, the technique rotates them toward target directions while preserving signal magnitude—addressing representation collapse issues.\n\n**Confidence Gate:** The mechanism dynamically adjusts steering intensity according to input uncertainty, enabling adaptive control without requiring retraining.\n\n**Steering Modulation:** Strength is controlled through the confidence gate, which evaluates input conditions to determine appropriate intervention levels.\n\n**Operational Granularity:** The abstract does not specify whether steering operates at token, sentence, or sequence levels.\n\n## Main Results\n\nPerformance improvements include \"+10% on TruthfulQA, COPA, and Storycloze\" compared to addition-based methods, while maintaining \"the model's general open-ended generation quality.\"\n\n## Limitations\n\nThe document provided contains only the abstract and metadata. Specific limitations, detailed experimental conditions, failure cases, or boundary conditions are not discussed in this excerpt.",
    "durationMs": 4859,
    "url": "https://arxiv.org/abs/2602.08169"
  },
  "sourceToolAssistantUUID": "950d8610-f34b-49af-9289-52edba7f3f52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T08:41:15.889Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01L57A2JEXStfJubvryANSZC`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.05686",
  "prompt": "Find the specific AUROC results for TruthfulQA vs synthetic factoid tasks. What was the AUROC on TruthfulQA? What was the AUROC on synthetic/controlled tasks? What tasks were tested? What models were tested? Is there any discussion of limitations when extrapolating from factoid tasks to open-ended generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e2f664a-e2bc-4371-a2d4-9f517054431c",
  "isSidechain": false,
  "requestId": "req_011Cb5wzQKqXcihMdook3QRV",
  "type": "assistant",
  "uuid": "a56608eb-15bd-40f4-82aa-862165784855",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JbcQEcXr2srhQP6iebZwJN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1594,
      "cache_creation_input_tokens": 2000,
      "cache_read_input_tokens": 25706,
      "output_tokens": 544,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2000,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1594,
          "output_tokens": 544,
          "cache_read_input_tokens": 25706,
          "cache_creation_input_tokens": 2000,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2000
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

_source line 30 · 2026-05-16T08:41:17.466Z_

<details><summary>↩ Tool result · `toolu_01Uo4SazE177ySvPyUYuo8io`</summary>

```text
# Analysis of "Minimizing Collateral Damage in Activation Steering"

## Full Abstract
The paper defines "collateral damage" as unintended changes in activation alignment along non-target feature directions during steering interventions. It proposes a constrained optimization framework that minimizes expected squared collateral change weighted by the empirical second-moment matrix of activations, accounting for nonuniform perturbation costs across feature directions.

## Formalization of Collateral Damage
The work provides mathematical formalization showing that standard methods like vector addition cause unintended shifts. The key insight is that traditional approaches "implicitly assume the isotropy of non-target features," treating all directions uniformly.

## Constrained Optimization Framework
The method models steering as a constrained optimization problem. Rather than using isotropic penalties, it weights perturbations by the empirical second-moment matrix of activations, encoding variable costs across different feature directions.

## Utility Preservation
The approach achieves "more precise control while reducing the degradation of model performance on unrelated tasks" by accounting for the empirical second-moment structure.

## Granularity Level
The document does not explicitly address whether interventions operate at sentence-level versus sequence-level. The abstract discusses internal representations and activation interventions without specifying the granularity of application.

## Main Results
The paper demonstrates that accounting for activation second-moment statistics enables better LLM behavior control with reduced collateral performance degradation on unrelated tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a9efb73-3326-476d-bd90-3214c1ceb01b",
  "isSidechain": false,
  "promptId": "43455a43-f601-4f83-8fa7-df33f42d6c19",
  "type": "user",
  "uuid": "c6bb2e68-0bc4-4fe8-8f19-293f15407724",
  "toolUseResult": {
    "bytes": 46600,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of \"Minimizing Collateral Damage in Activation Steering\"\n\n## Full Abstract\nThe paper defines \"collateral damage\" as unintended changes in activation alignment along non-target feature directions during steering interventions. It proposes a constrained optimization framework that minimizes expected squared collateral change weighted by the empirical second-moment matrix of activations, accounting for nonuniform perturbation costs across feature directions.\n\n## Formalization of Collateral Damage\nThe work provides mathematical formalization showing that standard methods like vector addition cause unintended shifts. The key insight is that traditional approaches \"implicitly assume the isotropy of non-target features,\" treating all directions uniformly.\n\n## Constrained Optimization Framework\nThe method models steering as a constrained optimization problem. Rather than using isotropic penalties, it weights perturbations by the empirical second-moment matrix of activations, encoding variable costs across different feature directions.\n\n## Utility Preservation\nThe approach achieves \"more precise control while reducing the degradation of model performance on unrelated tasks\" by accounting for the empirical second-moment structure.\n\n## Granularity Level\nThe document does not explicitly address whether interventions operate at sentence-level versus sequence-level. The abstract discusses internal representations and activation interventions without specifying the granularity of application.\n\n## Main Results\nThe paper demonstrates that accounting for activation second-moment statistics enables better LLM behavior control with reduced collateral performance degradation on unrelated tasks.",
    "durationMs": 5619,
    "url": "https://arxiv.org/abs/2605.01167"
  },
  "sourceToolAssistantUUID": "0a9efb73-3326-476d-bd90-3214c1ceb01b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-16T08:41:19.302Z_

<details><summary>↩ Tool result · `toolu_01HpVRw34TErwvxUxhJuhvU8`</summary>

```text
# FLAS: Flow-based Activation Steering - Key Details

## Full Abstract
The paper proposes FLAS, which learns a general, concept-conditioned velocity field that transports unsteered activations to steered ones. The method represents a departure from prior steering approaches by rejecting restrictive assumptions about fixed, single-step, position-invariant transformations.

## Method Details

**Velocity Field Mechanism:**
The core innovation involves learning "a general, concept-conditioned velocity field $v_t(h,t,c)$ that transports unsteered activations to steered ones without relying on these assumptions." This means the method learns continuous trajectories rather than applying static offsets.

**Concept-Conditioning:**
Rather than using fixed steering vectors, the approach conditions the transformation on specific concepts, enabling more flexible and generalizable interventions across different behavioral targets.

**Distinction from Linear Steering:**
Unlike traditional steering vectors that apply constant corrections, FLAS enables "curved, multi-step, token-varying trajectories," suggesting activation space modifications vary across tokens and require multiple transformation steps.

## Main Results
On AxBench benchmarks, FLAS achieved harmonic means of 1.015 (Gemma-2-2B-IT) and 1.113 (Gemma-2-9B-IT), becoming "the first learned method to consistently outperform prompting" without requiring per-concept tuning.

## Limitations & Gaps
The abstract does not mention TruthfulQA results, geometric triggers, or sentence-level gating mechanisms, so these cannot be confirmed from the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26f6ffac-b770-4d4a-a486-35f939326639",
  "isSidechain": false,
  "promptId": "43455a43-f601-4f83-8fa7-df33f42d6c19",
  "type": "user",
  "uuid": "8c75d05c-0ca7-4152-ad52-dab08c916093",
  "toolUseResult": {
    "bytes": 46297,
    "code": 200,
    "codeText": "OK",
    "result": "# FLAS: Flow-based Activation Steering - Key Details\n\n## Full Abstract\nThe paper proposes FLAS, which learns a general, concept-conditioned velocity field that transports unsteered activations to steered ones. The method represents a departure from prior steering approaches by rejecting restrictive assumptions about fixed, single-step, position-invariant transformations.\n\n## Method Details\n\n**Velocity Field Mechanism:**\nThe core innovation involves learning \"a general, concept-conditioned velocity field $v_t(h,t,c)$ that transports unsteered activations to steered ones without relying on these assumptions.\" This means the method learns continuous trajectories rather than applying static offsets.\n\n**Concept-Conditioning:**\nRather than using fixed steering vectors, the approach conditions the transformation on specific concepts, enabling more flexible and generalizable interventions across different behavioral targets.\n\n**Distinction from Linear Steering:**\nUnlike traditional steering vectors that apply constant corrections, FLAS enables \"curved, multi-step, token-varying trajectories,\" suggesting activation space modifications vary across tokens and require multiple transformation steps.\n\n## Main Results\nOn AxBench benchmarks, FLAS achieved harmonic means of 1.015 (Gemma-2-2B-IT) and 1.113 (Gemma-2-9B-IT), becoming \"the first learned method to consistently outperform prompting\" without requiring per-concept tuning.\n\n## Limitations & Gaps\nThe abstract does not mention TruthfulQA results, geometric triggers, or sentence-level gating mechanisms, so these cannot be confirmed from the provided content.",
    "durationMs": 6034,
    "url": "https://arxiv.org/abs/2605.05892"
  },
  "sourceToolAssistantUUID": "26f6ffac-b770-4d4a-a486-35f939326639",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T08:41:21.177Z_

<details><summary>↩ Tool result · `toolu_01L57A2JEXStfJubvryANSZC`</summary>

```text
# AUROC Results: TruthfulQA vs. Synthetic Tasks

## TruthfulQA Performance
The paper reports that on TruthfulQA, geometric margin achieved "AUROC = 0.858" compared to entropy's 0.656. This represents a meaningful but notably lower performance than the controlled synthetic setting.

## Synthetic Task Performance
In contrast, the controlled entity-code mapping task demonstrated substantially higher discrimination: margin achieved "AUROC = 0.993" versus entropy's 0.968, with the framework achieving "perfect separation with zero false refusals."

## Task Comparison
The synthetic experiments used 1,600 entities mapped to unique five-digit codes with carefully controlled parametric and working memory conditions. The TruthfulQA evaluation represented natural-language factual queries without adapter modifications.

## Model Coverage
Testing spanned 12 instruction-tuned models across 0.36B–14B parameters in scaling analyses, though specific TruthfulQA model details aren't extensively elaborated.

## Acknowledged Limitations
The authors explicitly note that margin "degrades on adversarial reasoning probes where no memorized basin exists" and state that "transfer to open-domain settings requires further study," acknowledging that their framework's theoretical elegance doesn't fully transfer to naturally-occurring hallucinations beyond memorization failures.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a56608eb-15bd-40f4-82aa-862165784855",
  "isSidechain": false,
  "promptId": "43455a43-f601-4f83-8fa7-df33f42d6c19",
  "type": "user",
  "uuid": "806795f9-807e-44b7-958c-69860a462db9",
  "toolUseResult": {
    "bytes": 632050,
    "code": 200,
    "codeText": "OK",
    "result": "# AUROC Results: TruthfulQA vs. Synthetic Tasks\n\n## TruthfulQA Performance\nThe paper reports that on TruthfulQA, geometric margin achieved \"AUROC = 0.858\" compared to entropy's 0.656. This represents a meaningful but notably lower performance than the controlled synthetic setting.\n\n## Synthetic Task Performance\nIn contrast, the controlled entity-code mapping task demonstrated substantially higher discrimination: margin achieved \"AUROC = 0.993\" versus entropy's 0.968, with the framework achieving \"perfect separation with zero false refusals.\"\n\n## Task Comparison\nThe synthetic experiments used 1,600 entities mapped to unique five-digit codes with carefully controlled parametric and working memory conditions. The TruthfulQA evaluation represented natural-language factual queries without adapter modifications.\n\n## Model Coverage\nTesting spanned 12 instruction-tuned models across 0.36B–14B parameters in scaling analyses, though specific TruthfulQA model details aren't extensively elaborated.\n\n## Acknowledged Limitations\nThe authors explicitly note that margin \"degrades on adversarial reasoning probes where no memorized basin exists\" and state that \"transfer to open-domain settings requires further study,\" acknowledging that their framework's theoretical elegance doesn't fully transfer to naturally-occurring hallucinations beyond memorization failures.",
    "durationMs": 5286,
    "url": "https://arxiv.org/html/2605.05686"
  },
  "sourceToolAssistantUUID": "a56608eb-15bd-40f4-82aa-862165784855",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-16T08:41:21.180Z_

```json
{
  "parentUuid": "806795f9-807e-44b7-958c-69860a462db9",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1582ee18-3529-4a5d-a258-104e176ca35c",
  "timestamp": "2026-05-16T08:41:21.180Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 34 · 2026-05-16T08:41:24.673Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent! Now I have key details. Let me also fetch the full HTML versions of the Spherical Steering paper and FLAS paper to get more details on their methods, especially granularity of operation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1582ee18-3529-4a5d-a258-104e176ca35c",
  "isSidechain": false,
  "requestId": "req_011Cb5x1e8aDhwMd6v7Tr5td",
  "type": "assistant",
  "uuid": "aa636278-f036-4083-a344-092e8c1edbc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FwLV7EdhyWNS4cEwjrFtgZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3636,
      "cache_read_input_tokens": 27706,
      "output_tokens": 441,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3636,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 441,
          "cache_read_input_tokens": 27706,
          "cache_creation_input_tokens": 3636,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3636
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

_source line 35 · 2026-05-16T08:41:25.640Z_

Good, I now have the key details. Let me get more specifics on Spherical Steering's confidence gate mechanism and FLAS's TruthfulQA results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa636278-f036-4083-a344-092e8c1edbc0",
  "isSidechain": false,
  "requestId": "req_011Cb5x1e8aDhwMd6v7Tr5td",
  "type": "assistant",
  "uuid": "94148a13-43b9-432b-a810-b703e135f6be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FwLV7EdhyWNS4cEwjrFtgZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3636,
      "cache_read_input_tokens": 27706,
      "output_tokens": 441,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3636,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 441,
          "cache_read_input_tokens": 27706,
          "cache_creation_input_tokens": 3636,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3636
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

_source line 36 · 2026-05-16T08:41:27.704Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012Fr5HPnJf31TsddCPkoSnC`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.05892",
  "prompt": "Find TruthfulQA results if any. What benchmarks are used? What are the specific numerical results? Does FLAS operate at token-level, sentence-level, or sequence-level? How does it compare to ACT, ODESteer, and other steering baselines? What are its computational costs?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94148a13-43b9-432b-a810-b703e135f6be",
  "isSidechain": false,
  "requestId": "req_011Cb5x1e8aDhwMd6v7Tr5td",
  "type": "assistant",
  "uuid": "29740bad-e374-46a5-a775-2932f3e83648",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FwLV7EdhyWNS4cEwjrFtgZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3636,
      "cache_read_input_tokens": 27706,
      "output_tokens": 441,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3636,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 441,
          "cache_read_input_tokens": 27706,
          "cache_creation_input_tokens": 3636,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3636
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

_source line 37 · 2026-05-16T08:41:30.540Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012GpNEBJvQhY4KP33ips33e`</summary>

```json
{
  "url": "https://github.com/chili-lab/Spherical-Steering",
  "prompt": "Find details about the confidence gate mechanism. How does it determine input uncertainty? What granularity does steering apply at (per-token, per-sentence, per-sequence)? What models were tested? What are the specific TruthfulQA numbers? Any details about how rotation differs from addition in practice?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29740bad-e374-46a5-a775-2932f3e83648",
  "isSidechain": false,
  "requestId": "req_011Cb5x1e8aDhwMd6v7Tr5td",
  "type": "assistant",
  "uuid": "998dcec4-2105-4158-a4d4-48a1cc05c151",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FwLV7EdhyWNS4cEwjrFtgZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3636,
      "cache_read_input_tokens": 27706,
      "output_tokens": 441,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3636,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 441,
          "cache_read_input_tokens": 27706,
          "cache_creation_input_tokens": 3636,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3636
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

_source line 38 · 2026-05-16T08:41:30.918Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017veVS6DRgngHNd1xUir9ad`</summary>

```json
{
  "query": "Spherical Steering confidence gate mechanism per-token sentence granularity TruthfulQA results Llama"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "998dcec4-2105-4158-a4d4-48a1cc05c151",
  "isSidechain": false,
  "requestId": "req_011Cb5x1e8aDhwMd6v7Tr5td",
  "type": "assistant",
  "uuid": "af484b5f-105f-4118-9c56-f6cf0f140758",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FwLV7EdhyWNS4cEwjrFtgZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3636,
      "cache_read_input_tokens": 27706,
      "output_tokens": 441,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3636,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 441,
          "cache_read_input_tokens": 27706,
          "cache_creation_input_tokens": 3636,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3636
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

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-16 (UTC).**  ## Original idea {   \"title\": \"Geometry-Triggered Sentence-Level Activation Steering for Factual Hall…",
  "leafUuid": "af484b5f-105f-4118-9c56-f6cf0f140758",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising geometry-triggered steering with competitor analysis",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb"
}
```

---

### Tool result

_source line 41 · 2026-05-16T08:41:35.404Z_

<details><summary>↩ Tool result · `toolu_012GpNEBJvQhY4KP33ips33e`</summary>

```text
# Analysis of Spherical Steering Documentation

Based on the provided GitHub repository content, I cannot find details addressing most of your questions:

**Missing Information:**
- **Confidence gate mechanism**: Not mentioned in the repository overview
- **Input uncertainty determination**: No discussion provided
- **Steering granularity**: The documentation doesn't specify whether steering operates at token, sentence, or sequence level
- **Specific TruthfulQA metrics**: While the repo uses TruthfulQA for evaluation, actual numerical results aren't included in this page

**Available Details:**

The repository confirms testing on two language models:
- Llama 3.1-8B-Instruct
- Qwen2.5-7B-Instruct

Regarding rotation versus addition, the abstract explains that Spherical Steering "performs a rotation: it treats steering as a directional update in representation space and rotates hidden activations along a geodesic toward a target direction, while keeping activation magnitudes intact"—contrasting with standard addition methods.

**Recommendation:** The actual paper (arxiv.org/abs/2602.08169) would contain the comprehensive technical details you're seeking, including confidence mechanisms, granularity specifications, and quantitative TruthfulQA results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "998dcec4-2105-4158-a4d4-48a1cc05c151",
  "isSidechain": false,
  "promptId": "43455a43-f601-4f83-8fa7-df33f42d6c19",
  "type": "user",
  "uuid": "6d8ae8d2-0fb8-4bb9-8f0f-9f2ea5f63cfa",
  "toolUseResult": {
    "bytes": 303560,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of Spherical Steering Documentation\n\nBased on the provided GitHub repository content, I cannot find details addressing most of your questions:\n\n**Missing Information:**\n- **Confidence gate mechanism**: Not mentioned in the repository overview\n- **Input uncertainty determination**: No discussion provided\n- **Steering granularity**: The documentation doesn't specify whether steering operates at token, sentence, or sequence level\n- **Specific TruthfulQA metrics**: While the repo uses TruthfulQA for evaluation, actual numerical results aren't included in this page\n\n**Available Details:**\n\nThe repository confirms testing on two language models:\n- Llama 3.1-8B-Instruct\n- Qwen2.5-7B-Instruct\n\nRegarding rotation versus addition, the abstract explains that Spherical Steering \"performs a rotation: it treats steering as a directional update in representation space and rotates hidden activations along a geodesic toward a target direction, while keeping activation magnitudes intact\"—contrasting with standard addition methods.\n\n**Recommendation:** The actual paper (arxiv.org/abs/2602.08169) would contain the comprehensive technical details you're seeking, including confidence mechanisms, granularity specifications, and quantitative TruthfulQA results.",
    "durationMs": 4860,
    "url": "https://github.com/chili-lab/Spherical-Steering"
  },
  "sourceToolAssistantUUID": "998dcec4-2105-4158-a4d4-48a1cc05c151",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T08:41:35.597Z_

<details><summary>↩ Tool result · `toolu_012Fr5HPnJf31TsddCPkoSnC`</summary>

```text
# FLAS: Flow-based Activation Steering - Key Technical Details

## Benchmarks and Results

FLAS is evaluated exclusively on **AxBench**, which the paper describes as providing "large-scale natural-language concepts" for testing zero-shot generalization. **No TruthfulQA results are reported** in this paper.

**Primary Results (AxBench, held-out evaluation):**
- Gemma-2-2B-IT: HMean of 1.015 (vs. prompting baseline 0.762)
- Gemma-2-9B-IT: HMean of 1.113 (vs. prompting baseline 1.091)

The paper also reports cross-model testing on Qwen3-4B with a held-out HMean of 0.960.

## Operational Level

FLAS operates at the **token level**. The velocity field is "computed per token position," and analysis reveals that "per-token steering is far from uniform" with average pairwise cosine similarity of only 0.294 across positions—far below uniform methods.

## Comparisons to Other Methods

The paper directly compares against:
- **AcT** (Activation Transport): FLAS significantly outperforms, particularly on held-out concepts
- **ODESteer**: Not directly compared in main results, but listed in related work
- **ReFT-r1, DiffMean**: All three baselines shown to "collapse at higher strengths, while FLAS steadily improves"

Table 2 shows FLAS achieving substantially higher scores than HyperSteer (0.608 vs. 1.015 on 2B held-out).

## Computational Costs

The paper acknowledges that FLAS "introduces acceptable additional inference cost because it accepts arbitrary text concepts, which requires concept encoding and cross attention during steering." Detailed quantification is deferred to Appendix H, which evaluates latency overhead. The method uses 97.6M trainable parameters (2B model) and 255M parameters (9B model).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29740bad-e374-46a5-a775-2932f3e83648",
  "isSidechain": false,
  "promptId": "43455a43-f601-4f83-8fa7-df33f42d6c19",
  "type": "user",
  "uuid": "17ba13c5-f592-40d7-8357-a482c7c273c7",
  "toolUseResult": {
    "bytes": 534683,
    "code": 200,
    "codeText": "OK",
    "result": "# FLAS: Flow-based Activation Steering - Key Technical Details\n\n## Benchmarks and Results\n\nFLAS is evaluated exclusively on **AxBench**, which the paper describes as providing \"large-scale natural-language concepts\" for testing zero-shot generalization. **No TruthfulQA results are reported** in this paper.\n\n**Primary Results (AxBench, held-out evaluation):**\n- Gemma-2-2B-IT: HMean of 1.015 (vs. prompting baseline 0.762)\n- Gemma-2-9B-IT: HMean of 1.113 (vs. prompting baseline 1.091)\n\nThe paper also reports cross-model testing on Qwen3-4B with a held-out HMean of 0.960.\n\n## Operational Level\n\nFLAS operates at the **token level**. The velocity field is \"computed per token position,\" and analysis reveals that \"per-token steering is far from uniform\" with average pairwise cosine similarity of only 0.294 across positions—far below uniform methods.\n\n## Comparisons to Other Methods\n\nThe paper directly compares against:\n- **AcT** (Activation Transport): FLAS significantly outperforms, particularly on held-out concepts\n- **ODESteer**: Not directly compared in main results, but listed in related work\n- **ReFT-r1, DiffMean**: All three baselines shown to \"collapse at higher strengths, while FLAS steadily improves\"\n\nTable 2 shows FLAS achieving substantially higher scores than HyperSteer (0.608 vs. 1.015 on 2B held-out).\n\n## Computational Costs\n\nThe paper acknowledges that FLAS \"introduces acceptable additional inference cost because it accepts arbitrary text concepts, which requires concept encoding and cross attention during steering.\" Detailed quantification is deferred to Appendix H, which evaluates latency overhead. The method uses 97.6M trainable parameters (2B model) and 255M parameters (9B model).",
    "durationMs": 7887,
    "url": "https://arxiv.org/html/2605.05892"
  },
  "sourceToolAssistantUUID": "29740bad-e374-46a5-a775-2932f3e83648",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-16T08:41:38.710Z_

<details><summary>↩ Tool result · `toolu_017veVS6DRgngHNd1xUir9ad`</summary>

```text
Web search results for query: "Spherical Steering confidence gate mechanism per-token sentence granularity TruthfulQA results Llama"

Links: [{"title":"Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/html/2602.08169v1"},{"title":"(PDF) Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://www.researchgate.net/publication/400605038_Spherical_Steering_Geometry-Aware_Activation_Rotation_for_Language_Models"},{"title":"[2602.08169] Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/abs/2602.08169"},{"title":"SteerConf: Steering LLMs for Confidence Elicitation","url":"https://arxiv.org/html/2503.02863v2"},{"title":"Compositional Steering of Large Language Models with Steering Tokens","url":"https://arxiv.org/html/2601.05062v1"},{"title":"Steering Llama 2 via Contrastive Activation Addition","url":"https://arxiv.org/html/2312.06681v2"},{"title":"Scaling laws for activation steering with Llama 2 models and refusal mechanisms","url":"https://arxiv.org/pdf/2507.11771"},{"title":"Activation Addition: Steering Language Models Without Optimization","url":"https://arxiv.org/html/2308.10248v4"},{"title":"Dialogue Action Tokens: Steering Language Models in ...","url":"https://arxiv.org/pdf/2406.11978"},{"title":"[2312.06681] Steering Llama 2 via Contrastive Activation Addition","url":"https://arxiv.org/abs/2312.06681"}]

Based on the search results, I found comprehensive information about Spherical Steering with a confidence gate mechanism and its TruthfulQA results on Llama models.

## Spherical Steering: Key Findings

Spherical Steering is a training-free method that resolves the trade-off between accuracy and generation quality through activation rotation, rotating activations along a geodesic toward a target direction while preserving signal integrity.

### Confidence Gate Mechanism

The method incorporates a confidence gate that dynamically modulates steering strength based on input uncertainty. More specifically, a von Mises-Fisher (vMF)-based confidence gate is used to set input-adaptive steering strength.

### TruthfulQA Results on Llama

Spherical Steering dominates all baselines in multiple-choice performance across both model families, achieving MC average improvements of +11.09% on LLaMA and +5.31% on Qwen over the best baseline.

More specifically, Spherical Steering significantly outperforms addition-based baselines with notably +10% on TruthfulQA, COPA, and Storycloze, while simultaneously maintaining the model's general open-ended generation quality.

### Key Performance Advantage

Spherical Steering achieves the best multiple-choice performance while simultaneously maintaining or improving generation quality—a Pareto improvement over all baselines. This is particularly important because these accuracy gains do not come at the expense of generation quality, with the method achieving the highest TRUE × INFO scores (+3.45% and +0.90% respectively).

The research demonstrates that geometry-aware activation rotation with adaptive confidence gating provides a more effective approach to steering language models compared to additive baselines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af484b5f-105f-4118-9c56-f6cf0f140758",
  "isSidechain": false,
  "promptId": "43455a43-f601-4f83-8fa7-df33f42d6c19",
  "type": "user",
  "uuid": "88ac4704-8a2b-4266-ab60-f31a53102744",
  "toolUseResult": {
    "query": "Spherical Steering confidence gate mechanism per-token sentence granularity TruthfulQA results Llama",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HwbQeAqbALUdVRBBF4gB5h",
        "content": [
          {
            "title": "Spherical Steering: Geometry-Aware Activation Rotation for Language Models",
            "url": "https://arxiv.org/html/2602.08169v1"
          },
          {
            "title": "(PDF) Spherical Steering: Geometry-Aware Activation Rotation for Language Models",
            "url": "https://www.researchgate.net/publication/400605038_Spherical_Steering_Geometry-Aware_Activation_Rotation_for_Language_Models"
          },
          {
            "title": "[2602.08169] Spherical Steering: Geometry-Aware Activation Rotation for Language Models",
            "url": "https://arxiv.org/abs/2602.08169"
          },
          {
            "title": "SteerConf: Steering LLMs for Confidence Elicitation",
            "url": "https://arxiv.org/html/2503.02863v2"
          },
          {
            "title": "Compositional Steering of Large Language Models with Steering Tokens",
            "url": "https://arxiv.org/html/2601.05062v1"
          },
          {
            "title": "Steering Llama 2 via Contrastive Activation Addition",
            "url": "https://arxiv.org/html/2312.06681v2"
          },
          {
            "title": "Scaling laws for activation steering with Llama 2 models and refusal mechanisms",
            "url": "https://arxiv.org/pdf/2507.11771"
          },
          {
            "title": "Activation Addition: Steering Language Models Without Optimization",
            "url": "https://arxiv.org/html/2308.10248v4"
          },
          {
            "title": "Dialogue Action Tokens: Steering Language Models in ...",
            "url": "https://arxiv.org/pdf/2406.11978"
          },
          {
            "title": "[2312.06681] Steering Llama 2 via Contrastive Activation Addition",
            "url": "https://arxiv.org/abs/2312.06681"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about Spherical Steering with a confidence gate mechanism and its TruthfulQA results on Llama models.\n\n## Spherical Steering: Key Findings\n\nSpherical Steering is a training-free method that resolves the trade-off between accuracy and generation quality through activation rotation, rotating activations along a geodesic toward a target direction while preserving signal integrity.\n\n### Confidence Gate Mechanism\n\nThe method incorporates a confidence gate that dynamically modulates steering strength based on input uncertainty. More specifically, a von Mises-Fisher (vMF)-based confidence gate is used to set input-adaptive steering strength.\n\n### TruthfulQA Results on Llama\n\nSpherical Steering dominates all baselines in multiple-choice performance across both model families, achieving MC average improvements of +11.09% on LLaMA and +5.31% on Qwen over the best baseline.\n\nMore specifically, Spherical Steering significantly outperforms addition-based baselines with notably +10% on TruthfulQA, COPA, and Storycloze, while simultaneously maintaining the model's general open-ended generation quality.\n\n### Key Performance Advantage\n\nSpherical Steering achieves the best multiple-choice performance while simultaneously maintaining or improving generation quality—a Pareto improvement over all baselines. This is particularly important because these accuracy gains do not come at the expense of generation quality, with the method achieving the highest TRUE × INFO scores (+3.45% and +0.90% respectively).\n\nThe research demonstrates that geometry-aware activation rotation with adaptive confidence gating provides a more effective approach to steering language models compared to additive baselines."
    ],
    "durationSeconds": 7.788940004000004
  },
  "sourceToolAssistantUUID": "af484b5f-105f-4118-9c56-f6cf0f140758",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-16T08:41:42.312Z_

<details><summary>Logged reasoning block</summary>

```text
Let me get more details on Spherical Steering's confidence gate and operational granularity.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88ac4704-8a2b-4266-ab60-f31a53102744",
  "isSidechain": false,
  "requestId": "req_011Cb5x2yRTtKx49mS8qq82x",
  "type": "assistant",
  "uuid": "a11a429d-7c60-468b-8c15-ea4592715d9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ghy7FXWiaYTyuaW7SjRGL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2135,
      "cache_read_input_tokens": 31342,
      "output_tokens": 336,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2135,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 336,
          "cache_read_input_tokens": 31342,
          "cache_creation_input_tokens": 2135,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2135
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

_source line 45 · 2026-05-16T08:41:43.262Z_

Let me fetch the full HTML of the Spherical Steering paper for more technical details on the confidence gate and granularity.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a11a429d-7c60-468b-8c15-ea4592715d9c",
  "isSidechain": false,
  "requestId": "req_011Cb5x2yRTtKx49mS8qq82x",
  "type": "assistant",
  "uuid": "e32c11c5-9536-4cda-9622-aebe051ea454",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ghy7FXWiaYTyuaW7SjRGL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2135,
      "cache_read_input_tokens": 31342,
      "output_tokens": 336,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2135,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 336,
          "cache_read_input_tokens": 31342,
          "cache_creation_input_tokens": 2135,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2135
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

_source line 46 · 2026-05-16T08:41:46.204Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019Wmh2amTPPBqF3VHAjz35e`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.08169v1",
  "prompt": "Find details about: 1) The von Mises-Fisher (vMF) confidence gate - how exactly does it work? What inputs does it take? 2) What granularity does steering operate at - per-token, per-sentence, or per-sequence? 3) What are the exact TruthfulQA numbers (MC1, MC2, TRUE*INFO)? 4) How is the steering direction determined? 5) What layers are targeted? 6) How does it compare to CAA (Contrastive Activation Addition)? 7) What are the limitations?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e32c11c5-9536-4cda-9622-aebe051ea454",
  "isSidechain": false,
  "requestId": "req_011Cb5x2yRTtKx49mS8qq82x",
  "type": "assistant",
  "uuid": "9d5a13bf-95de-432e-96f0-8a72663db7ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ghy7FXWiaYTyuaW7SjRGL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2135,
      "cache_read_input_tokens": 31342,
      "output_tokens": 336,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2135,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 336,
          "cache_read_input_tokens": 31342,
          "cache_creation_input_tokens": 2135,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2135
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

_source line 47 · 2026-05-16T08:41:46.531Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RdavGAQLKyvsvg5sHeRRNE`</summary>

```json
{
  "query": "\"Minimizing Collateral Damage\" activation steering second-moment matrix results benchmarks utility preservation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d5a13bf-95de-432e-96f0-8a72663db7ec",
  "isSidechain": false,
  "requestId": "req_011Cb5x2yRTtKx49mS8qq82x",
  "type": "assistant",
  "uuid": "4f95ea59-bb3b-48b5-b6a0-3545e5ac3b7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ghy7FXWiaYTyuaW7SjRGL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2135,
      "cache_read_input_tokens": 31342,
      "output_tokens": 336,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2135,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 336,
          "cache_read_input_tokens": 31342,
          "cache_creation_input_tokens": 2135,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2135
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

_source line 48 · 2026-05-16T08:41:56.126Z_

<details><summary>↩ Tool result · `toolu_019Wmh2amTPPBqF3VHAjz35e`</summary>

```text
# Spherical Steering: Key Technical Details

## 1) vMF Confidence Gate Mechanism

The von Mises-Fisher confidence gate operates by measuring alignment to truthful/hallucinated directions. It takes the current normalized activation and computes cosine similarities to both directions, then applies an exponential weighting scheme inspired by the vMF distribution. The gate outputs a steering strength *t* ∈ [0,1] via: "t={0 if δ≤β, else clip(α·(δ-β)/(1-β), 0, 1)}" where δ represents the probability difference between hallucinated and truthful alignments. This enables input-adaptive intervention that reduces steering when the model is already confident.

## 2) Steering Granularity

Steering operates **per-token during autoregressive generation**. At each decoding step, the method extracts the current token's activation, normalizes it, computes alignment scores, applies the vMF gate to determine strength, then rotates via spherical linear interpolation (Slerp). This allows token-by-token adaptivity rather than sequence-level control.

## 3) TruthfulQA Performance Numbers

On LLaMA-3.1-8B-Instruct: MC1=49.95% (+15.80% vs baseline), MC2=68.51% (+15.39%), TRUE×INFO=54.63% (+6.39%). On Qwen-2.5-7B-Instruct: MC1=48.71% (+12.84%), MC2=66.90% (+11.95%), TRUE×INFO=77.84% (+3.44%).

## 4) Steering Direction Determination

The method constructs a "truthfulness axis" from contrastive training data. It extracts last-token activations from positive/negative answer pairs, computes mean representations for each, takes their difference, then normalizes: "μ = Δ/‖Δ‖" where Δ = m₊ - m₋.

## 5) Layer Targeting

The paper tests single-layer intervention at layer 24 for LLaMA-3.1-8B. Multi-layer experiments (Table 3) reveal asymmetric effects: K=2-3 layers boost informativeness (+29.78%) with minimal accuracy gains (+2.21%). The method doesn't specify automatic layer selection; practitioners must tune this.

## 6) Comparison to CAA

Unlike Contrastive Activation Addition which applies "h' = h + λμ" causing uncontrolled magnitude distortion, Spherical Steering performs norm-preserving rotation on the hypersphere. The paper shows this achieves 8-10% higher multiple-choice accuracy at matched representation collapse levels while maintaining generation quality—a fundamental collapse-efficiency advantage.

## 7) Limitations

The paper acknowledges: (i) lacks "principled multi-layer layer selection"; (ii) involves multiple hyperparameters (α, β, κ) requiring tuning; (iii) the single-layer analysis shows κ's reduced sensitivity but doesn't fully characterize layer interactions; (iv) evaluation focuses on truthfulness—generalization to other behaviors unclear.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d5a13bf-95de-432e-96f0-8a72663db7ec",
  "isSidechain": false,
  "promptId": "43455a43-f601-4f83-8fa7-df33f42d6c19",
  "type": "user",
  "uuid": "61e36754-27f7-42bd-9a73-0acc56ba3dbb",
  "toolUseResult": {
    "bytes": 390719,
    "code": 200,
    "codeText": "OK",
    "result": "# Spherical Steering: Key Technical Details\n\n## 1) vMF Confidence Gate Mechanism\n\nThe von Mises-Fisher confidence gate operates by measuring alignment to truthful/hallucinated directions. It takes the current normalized activation and computes cosine similarities to both directions, then applies an exponential weighting scheme inspired by the vMF distribution. The gate outputs a steering strength *t* ∈ [0,1] via: \"t={0 if δ≤β, else clip(α·(δ-β)/(1-β), 0, 1)}\" where δ represents the probability difference between hallucinated and truthful alignments. This enables input-adaptive intervention that reduces steering when the model is already confident.\n\n## 2) Steering Granularity\n\nSteering operates **per-token during autoregressive generation**. At each decoding step, the method extracts the current token's activation, normalizes it, computes alignment scores, applies the vMF gate to determine strength, then rotates via spherical linear interpolation (Slerp). This allows token-by-token adaptivity rather than sequence-level control.\n\n## 3) TruthfulQA Performance Numbers\n\nOn LLaMA-3.1-8B-Instruct: MC1=49.95% (+15.80% vs baseline), MC2=68.51% (+15.39%), TRUE×INFO=54.63% (+6.39%). On Qwen-2.5-7B-Instruct: MC1=48.71% (+12.84%), MC2=66.90% (+11.95%), TRUE×INFO=77.84% (+3.44%).\n\n## 4) Steering Direction Determination\n\nThe method constructs a \"truthfulness axis\" from contrastive training data. It extracts last-token activations from positive/negative answer pairs, computes mean representations for each, takes their difference, then normalizes: \"μ = Δ/‖Δ‖\" where Δ = m₊ - m₋.\n\n## 5) Layer Targeting\n\nThe paper tests single-layer intervention at layer 24 for LLaMA-3.1-8B. Multi-layer experiments (Table 3) reveal asymmetric effects: K=2-3 layers boost informativeness (+29.78%) with minimal accuracy gains (+2.21%). The method doesn't specify automatic layer selection; practitioners must tune this.\n\n## 6) Comparison to CAA\n\nUnlike Contrastive Activation Addition which applies \"h' = h + λμ\" causing uncontrolled magnitude distortion, Spherical Steering performs norm-preserving rotation on the hypersphere. The paper shows this achieves 8-10% higher multiple-choice accuracy at matched representation collapse levels while maintaining generation quality—a fundamental collapse-efficiency advantage.\n\n## 7) Limitations\n\nThe paper acknowledges: (i) lacks \"principled multi-layer layer selection\"; (ii) involves multiple hyperparameters (α, β, κ) requiring tuning; (iii) the single-layer analysis shows κ's reduced sensitivity but doesn't fully characterize layer interactions; (iv) evaluation focuses on truthfulness—generalization to other behaviors unclear.",
    "durationMs": 9918,
    "url": "https://arxiv.org/html/2602.08169v1"
  },
  "sourceToolAssistantUUID": "9d5a13bf-95de-432e-96f0-8a72663db7ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-16T08:41:57.774Z_

<details><summary>↩ Tool result · `toolu_01RdavGAQLKyvsvg5sHeRRNE`</summary>

```text
Web search results for query: ""Minimizing Collateral Damage" activation steering second-moment matrix results benchmarks utility preservation 2026"

Links: [{"title":"Minimizing Collateral Damage in Activation Steering","url":"https://arxiv.org/html/2605.01167v1"},{"title":"[2605.01167] Minimizing Collateral Damage in Activation Steering","url":"https://arxiv.org/abs/2605.01167"},{"title":"Minimizing Collateral Damage in Activation Steering","url":"https://www.researchgate.net/publication/404427927_Minimizing_Collateral_Damage_in_Activation_Steering"},{"title":"Machine Learning Mar 2025","url":"https://www.arxiv.org/list/cs.LG/2025-03?skip=500&show=2000"},{"title":"Industry Benchmarks 2026: Critical Response Insights","url":"https://cybersecuritytime.com/industry-benchmarks-2026-detection-response/"},{"title":"Learning-Based Safe Control for Robot and Autonomous ...","url":"https://ieeexplore.ieee.org/iel7/8784355/9999144/10138462.pdf"},{"title":"Ecolab Pest Control & Eco Pest: Top 2026 Spray Rig Trends","url":"https://farmonaut.com/precision-farming/ecolab-pest-control-eco-pest-top-2026-spray-rig-trends"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/new?skip=300&show=1000"},{"title":"[2502.02716] A Unified Understanding and Evaluation of Steering Methods","url":"https://arxiv.org/abs/2502.02716"},{"title":"Machine Learning May 2025","url":"https://arxiv.org/list/cs.LG/2025-05?skip=3050&show=2000"}]

I found relevant results for your search query. Here's what the research shows:

## "Minimizing Collateral Damage in Activation Steering"

The work provides a mathematical formalization of collateral damage and introduces a principled framework that models steering as a constrained optimization problem, with a method that finds a new activation minimizing the expected squared collateral change weighted by the empirical second-moment matrix of activations.

### Key Methodology

This weighting encodes the nonuniform cost of the perturbation in different feature directions, in contrast to isotropic approaches that penalize changes uniformly in all feature directions. By accounting for the empirical second-moment of activations, the approach achieves more precise control while reducing the degradation of model performance on unrelated tasks.

### Results and Benchmarks

To evaluate performance preservation, the research reports task accuracy on the tinyBenchmarks suite of tasks, including 100 examples of ARC, MMLU, Winogrande, GSM8K, TruthfulQA, and HellaSwag. 

The method (COAST) achieves high-quality steering without degrading performance, yielding up to a 30% improvement in Attack Success Rate (ASR) over Angular Steering and improving up to 20% in accuracy compared to ActAdd at the same ASR, and outperforms SLERP in steering success while preserving the model's performance.

The paper appears to be recent (arxiv 2605.01167), posted in May 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f95ea59-bb3b-48b5-b6a0-3545e5ac3b7f",
  "isSidechain": false,
  "promptId": "43455a43-f601-4f83-8fa7-df33f42d6c19",
  "type": "user",
  "uuid": "628ba54a-eea0-4592-93b3-6df2fbe72039",
  "toolUseResult": {
    "query": "\"Minimizing Collateral Damage\" activation steering second-moment matrix results benchmarks utility preservation 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_015nhy2SGJCwHctGGeAs8QzQ",
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
            "title": "Machine Learning Mar 2025",
            "url": "https://www.arxiv.org/list/cs.LG/2025-03?skip=500&show=2000"
          },
          {
            "title": "Industry Benchmarks 2026: Critical Response Insights",
            "url": "https://cybersecuritytime.com/industry-benchmarks-2026-detection-response/"
          },
          {
            "title": "Learning-Based Safe Control for Robot and Autonomous ...",
            "url": "https://ieeexplore.ieee.org/iel7/8784355/9999144/10138462.pdf"
          },
          {
            "title": "Ecolab Pest Control & Eco Pest: Top 2026 Spray Rig Trends",
            "url": "https://farmonaut.com/precision-farming/ecolab-pest-control-eco-pest-top-2026-spray-rig-trends"
          },
          {
            "title": "Computer Science",
            "url": "https://arxiv.org/list/cs/new?skip=300&show=1000"
          },
          {
            "title": "[2502.02716] A Unified Understanding and Evaluation of Steering Methods",
            "url": "https://arxiv.org/abs/2502.02716"
          },
          {
            "title": "Machine Learning May 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-05?skip=3050&show=2000"
          }
        ]
      },
      "I found relevant results for your search query. Here's what the research shows:\n\n## \"Minimizing Collateral Damage in Activation Steering\"\n\nThe work provides a mathematical formalization of collateral damage and introduces a principled framework that models steering as a constrained optimization problem, with a method that finds a new activation minimizing the expected squared collateral change weighted by the empirical second-moment matrix of activations.\n\n### Key Methodology\n\nThis weighting encodes the nonuniform cost of the perturbation in different feature directions, in contrast to isotropic approaches that penalize changes uniformly in all feature directions. By accounting for the empirical second-moment of activations, the approach achieves more precise control while reducing the degradation of model performance on unrelated tasks.\n\n### Results and Benchmarks\n\nTo evaluate performance preservation, the research reports task accuracy on the tinyBenchmarks suite of tasks, including 100 examples of ARC, MMLU, Winogrande, GSM8K, TruthfulQA, and HellaSwag. \n\nThe method (COAST) achieves high-quality steering without degrading performance, yielding up to a 30% improvement in Attack Success Rate (ASR) over Angular Steering and improving up to 20% in accuracy compared to ActAdd at the same ASR, and outperforms SLERP in steering success while preserving the model's performance.\n\nThe paper appears to be recent (arxiv 2605.01167), posted in May 2026."
    ],
    "durationSeconds": 11.239521697000004
  },
  "sourceToolAssistantUUID": "4f95ea59-bb3b-48b5-b6a0-3545e5ac3b7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 50_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-16 (UTC).**  ## Original idea {   \"title\": \"Geometry-Triggered Sentence-Level Activation Steering for Factual Hall…",
  "leafUuid": "628ba54a-eea0-4592-93b3-6df2fbe72039",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising geometry-triggered steering with competitor analysis",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb"
}
```

---

### Assistant

_source line 52 · 2026-05-16T08:42:33.947Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information. Let me also quickly look at how "Minimizing Collateral Damage" compares to the sentence-level approach, and check if there's anything I'm missing about the FLAS paper's relevance to hallucination.

Let me summarize what I've learned:

1. **Spherical Steering (arXiv 2602.08169, ICML 2026)**:
   - Uses activation rotation (Slerp on hypersphere) instead of addition
   - Has a vMF-based confidence gate that determines steering strength per-token based on alignment to truthful/hallucinated directions
   - Operates at the token level during generation, achieving 10-15% improvements on TruthfulQA across Llama-3.1-8B and Qwen-2.5-7B
   - Differs from GTS through per-token granularity rather than sentence-level gating, rotation mechanics instead of centroid-directed addition, and a directional alignment confidence gate instead of Mahalanobis distance triggers
   - Main constraint is limited multi-layer support without a systematic approach to layer selection

2. **Minimizing Collateral Damage** /

COAST addresses unintended feature changes through constrained optimization with second-moment weighting, delivering 30% ASR improvement over Angular Steering and 20% accuracy gains over ActAdd. While GTS uses selective gating to preserve utility, COAST refines steering vectors through optimization—complementary strategies that tackle the same problem differently.

3. **FLAS** learns a concept-conditioned velocity field to transport token-level activations through curved multi-step paths.
   - Evaluated on AxBench rather than TruthfulQA
   - Requires 97.6M-255M trainable parameters
   - Unlike GTS's hallucination-specific design, FLAS functions as a general-purpose steering framework using learned flow dynamics

4. **Attractor Geometry AUROC**:
   - TruthfulQA achieves 0.858 versus entropy's 0.656
   - Synthetic data reaches 0.993 versus entropy's 0.968
   - The authors acknowledge that generalizing to open-domain settings needs more investigation
   - Performance degrades on adversarial reasoning tasks where no memorized basin exists

Now examining what these comparisons reveal about the positioning...

GTS operates at the sentence level with binary gating decisions, whereas Spherical Steering modulates per-token intensity through its vMF gate without making claim-level keep/steer choices—though I should acknowledge that Spherical Steering's +15% improvement on TruthfulQA MC1 sets a strong baseline. The AUROC of 0.858 on TruthfulQA is honest reporting, not the synthetic 0.993, which means the trigger still has meaningful false positive and negative rates that need careful handling. Rather than framing this as geometric evidence, I should focus on the sentence-as-planning-unit motivation. There's also the Mahalanobis versus Euclidean distance question to address directly.

FLAS and COAST represent alternative solutions to steering quality—learned flows versus constrained optimization—while GTS's contribution is selective application only where needed. I need to factor in FActScore API costs for the resource estimate and avoid overstating scale as a standalone contribution. The core hypothesis still holds: sentence-level selective steering should outperform uniform approaches because Spherical Steering steers every token with varying intensity, Hallucination Basins steers entire sequences, and GTS steers only at sentence boundaries when the geometric margin indicates the model isn't in a hallucination basin. That timing insight is the strongest part of the argument.

The main risk is whether margin at a sentence boundary actually predicts factuality of the next sentence—the Attractor Geometry paper only validates this on first-token factoid completion, so the leap is non-trivial. But using the first three tokens of the next sentence as a look-ahead fallback is a reasonable hedge. I should lead with the TruthfulQA AUROC of 0.858 and be honest about it, position GTS against Spherical Steering as the primary per-token baseline, and frame the advantages as sentence-level selectivity enabling claim-by-claim decisions within a sequence, the Mahalanobis trigger specifically measuring basin distance rather than directional alignment, and the per-layer MLP controller. COAST is worth acknowledging as complementary—potentially combinable with GTS's steering step—while FLAS is less directly relevant.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "628ba54a-eea0-4592-93b3-6df2fbe72039",
  "isSidechain": false,
  "requestId": "req_011Cb5x4LbxPUF5abKLasTMa",
  "type": "assistant",
  "uuid": "9fb9732f-6f75-48ed-9b49-e3700ed46b3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VvFs7q7jaAcq8CtL8xCxRS",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1962,
      "cache_read_input_tokens": 33477,
      "output_tokens": 7812,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1962,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7812,
          "cache_read_input_tokens": 33477,
          "cache_creation_input_tokens": 1962,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1962
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

_source line 53 · 2026-05-16T08:44:58.974Z_

Now I have all the information needed. Let me synthesize:

**Key findings:**
- Spherical Steering uses per-token vMF confidence gate + geodesic rotation, achieves +15% MC1 on TruthfulQA. Operates per-token, not sentence-level.
- COAST (Minimizing Collateral Damage) uses constrained optimization with second-moment weighting. Complementary approach to utility preservation.
- FLAS uses learned flow fields, evaluated on AxBench (not TruthfulQA). General concept steering, not hallucination-specific.
- Attractor Geometry: TruthfulQA AUROC = 0.858 (not 0.993-1.000). Authors explicitly note "transfer to open-domain settings requires further study."

The core idea remains sound — sentence-level selective steering is genuinely differentiated from Spherical Steering's per-token approach and Hallucination Basins' per-sequence approach. This is a minor revision with honest framing corrections. Let me produce the revised JSON.

```json
{
  "title": "Geometry-Triggered Sentence-Level Activation Steering for Factual Hallucination Suppression",
  "change_type": "minor",
  "core_problem": "Recent work (Attractor Geometry of Transformer Memory, May 2026) demonstrates that factual hallucination corresponds to 'basin absence'—the hidden state drifts freely when no memorized attractor basin exists—and that geometric margin separates correct recall from hallucination substantially better than entropy (AUROC 0.858 vs. 0.656 on TruthfulQA; up to 0.993 on controlled factoid tasks). Yet translating geometric margin into targeted activation interventions remains unsolved at the right granularity. Hallucination Basins (April 2026) proposes geometry-aware steering but operates at per-sequence granularity—applying uniform corrections across all claims in a response. Spherical Steering (ICML 2026) introduces geometry-aware rotation with an input-adaptive vMF confidence gate, achieving strong TruthfulQA gains, but applies steering per-token without claim-level selectivity: every token gets steered with some intensity, even in correct sub-claims, causing subtle quality degradation on already-accurate content. COAST (May 2026) addresses utility preservation via constrained optimization of the steering vector itself but does not address when to steer. Existing methods either steer everything (Spherical Steering, FLAS, ODESteer), steer the whole sequence (Hallucination Basins), or refine how to steer (COAST)—none selectively gate intervention at the natural unit of factual claims.",
  "opportunity": "The critical gap is between detection granularity and intervention granularity. Current geometry-aware steering methods couple 'where to steer' with 'how to steer' at mismatched granularities: Spherical Steering's per-token vMF gate modulates intensity continuously but cannot make a binary 'this claim needs correction / this claim is fine' decision; Hallucination Basins' per-sequence decision cannot distinguish correct from incorrect claims within a response; COAST optimizes the steering vector but applies it uniformly. The unexploited sweet spot is sentence-level gating: sentences are the natural unit of factual claims (the granularity FActScore evaluates, the granularity humans judge, and the granularity at which LLMs perform context integration before next-sentence planning). The combination of (1) Mahalanobis-distance-based basin absence detection as a binary trigger at sentence boundaries, (2) sentence-level gating enabling within-sequence selectivity (steer only flagged claims), and (3) per-layer MLP controller provides a principled 'when + where + how much' framework that is complementary to advances in 'how to steer' (rotation, flow, constrained optimization). Importantly, the trigger mechanism uses basin distance (measuring knowledge absence) rather than directional alignment to a pre-computed truthfulness axis (as in Spherical Steering's vMF gate), providing a more principled signal for detecting hallucination-prone states.",
  "landscape": "**Geometry-aware steering (closest competitors):** Spherical Steering (arXiv 2602.08169, ICML 2026) uses geodesic rotation with a von Mises-Fisher confidence gate that dynamically modulates per-token steering strength based on cosine alignment to truthful/hallucinated directions. Achieves MC1 +15.80% on TruthfulQA (Llama-3.1-8B) while preserving generation quality. Operates per-token with a single-layer intervention (layer 24). GTS differs in three ways: (a) sentence-level binary gating vs. per-token continuous modulation—enabling selective skip of entire correct claims rather than low-intensity steering through them; (b) Mahalanobis basin-distance trigger (measuring knowledge absence from attractor geometry) vs. vMF directional alignment to a fixed truthfulness axis (measuring surface-level direction); (c) per-layer MLP controller vs. single-layer intervention. Hallucination Basins (arXiv 2604.04743, April 2026) proposes Adaptive Geometry-Aware Steering using centroid-difference vectors, Euclidean distance trigger, and scalar logistic-regression controller at per-sequence granularity on 1B–3B models. GTS advances beyond it via sentence-level gating, Mahalanobis distance, and per-layer controller.\n\n**Utility-preservation approaches:** Minimizing Collateral Damage / COAST (arXiv 2605.01167, May 2026) formalizes collateral damage as unintended feature-direction shifts and solves steering as constrained optimization weighted by the empirical second-moment matrix. Achieves 30% ASR improvement over Angular Steering with preserved benchmarks. COAST is complementary to GTS: it optimizes the steering vector, while GTS optimizes when to apply it. These could be combined (sentence-gated COAST steering). FLAS (arXiv 2605.05892, May 2026) learns a concept-conditioned velocity field for multi-step token-level activation transport, first learned method to outperform prompting on AxBench. Operates per-token with 97.6M–255M trainable parameters. Not hallucination-specific and does not use geometric triggers.\n\n**Hallucination detection (analysis-only):** Attractor Geometry of Transformer Memory (arXiv 2605.05686, May 2026) demonstrates hallucination = basin absence with geometric margin achieving AUROC 0.858 on TruthfulQA (vs. entropy 0.656), and AUROC 0.993 on controlled factoid tasks. Authors note 'transfer to open-domain settings requires further study' and margin 'degrades on adversarial reasoning probes.' PCNet (arXiv 2605.05953, May 2026) detects hallucinations as geometric anomalies and applies contrastive decoding at token level. Where Does Reasoning Break? (arXiv 2605.13772, May 2026) detects step-level hallucination via transport geometry but proposes no intervention. DRIFT (arXiv 2601.14210, Jan 2026) detects representational instability at <0.1% overhead.\n\n**Calibration/expression approaches:** Calibrating Verbal Uncertainty as a Linear Feature (Ji et al., EMNLP 2025 Outstanding Paper, arXiv 2503.14477) achieves ~31.9% reduction in confident hallucinations via linear-feature intervention on Llama3.1-8B/Mistral-7B/Qwen2.5-7B. Calibrates uncertainty expression without correcting underlying generation—complementary to GTS which detects knowledge absence and redirects toward factual representations.\n\n**Other steering methods:** ACT (WWW 2025) uses K-means clustered corpus-averaged vectors. ODESteer (ICLR 2026) achieves 5.7% over ACT via ODE-based multi-step steering but remains input-oblivious. Guiding Giants/WAS (arXiv 2505.20309, May 2025) trains lightweight controllers for layer-aware weighted activation steering. SADI (arXiv 2410.12299, 2024) constructs input-specific dynamic steering vectors. HELIX/Tethered Reasoning (arXiv 2602.17691, Feb 2026) uses Mahalanobis distance + graduated steering for structural coherence in quantized models.\n\n**Supporting evidence:** Hallucination as Trajectory Commitment (arXiv 2604.15400, April 2026) provides causal evidence for early commitment with asymmetric attractor dynamics, supporting timely intervention at sentence boundaries before commitment propagates. Think in Sentences (arXiv 2604.10135, April 2026) demonstrates that sentence boundary tokens show attention concentration patterns consistent with context integration cycles, motivating the sentence-as-planning-unit hypothesis (though it does not analyze hidden-state geometry directly).",
  "approach": "We propose Geometry-Triggered Steering (GTS), a method that bridges the detection-to-intervention gap by introducing sentence-level selective gating to geometry-aware activation steering. The key insight is that the 'when to steer' decision should operate at claim granularity (sentences), even if the 'how to steer' step operates at token/layer granularity.\n\n**Stage 1: TRIGGER (PCA-Regularized Geometric Margin at Sentence Boundaries)**\nDuring generation, at each sentence boundary (detected via period/newline tokens), extract hidden-state activations at the boundary token across layers using nnsight intervention hooks. Compute geometric margin using class-conditional PCA-regularized Mahalanobis distance:\n(a) Offline: From a calibration set (~2K examples from TruthfulQA + FELM correct-answer forward passes), collect hidden states at factual completion positions. Apply PCA to project from full hidden dimension (d=4096) to top-k principal components (k=256), reducing covariance estimation to a well-conditioned 256×256 matrix.\n(b) Online: Project the boundary token's activation into the PCA subspace, compute Mahalanobis distance to nearest factual cluster centroid: δ(x) = √((h_pca - μ_pca)ᵀ Σ_pca⁻¹ (h_pca - μ_pca)).\n(c) When δ exceeds a calibrated threshold (set via precision-recall analysis on validation split targeting high precision to minimize false interventions), flag the upcoming sentence for intervention.\n\n**Trigger reliability note:** Geometric margin achieves AUROC 0.858 on TruthfulQA (vs. entropy 0.656)—sufficient for selective intervention with appropriate thresholding, though far from the 0.993 achieved on synthetic factoid tasks. This motivates operating at high-precision thresholds (accepting lower recall) so that when GTS intervenes, it is likely correct. The precision-recall tradeoff is explicitly studied in ablations.\n\n**Stage 2: DIRECTION (Centroid-Directed Steering Vector)**\nCompute the steering direction as the unit vector from the current activation toward the factual cluster centroid at each layer in the PCA subspace, then project back to full space: v_steer = (μ_pca - h_pca) / ||μ_pca - h_pca||, lifted back to full dimensionality via PCA inverse transform. This yields an input-specific correction direction toward regions of successful fact recall. We additionally experiment with a COAST-style constrained refinement of this vector to minimize collateral damage.\n\n**Stage 3: INTENSITY (Per-Layer MLP Controller)**\nA lightweight 2-layer MLP controller (hidden dim 64, inspired by Guiding Giants/WAS) takes [geometric_margin, layer_index/L, margin_velocity] as input (3D feature vector) and predicts per-layer steering weight λ_ℓ. The controller is trained on a calibration set (~2K examples) via a combined objective: maximize FActScore on steered outputs while minimizing perplexity increase on outputs where margin is below threshold. Steering is applied: h_steered(ℓ) = h(ℓ) + λ_ℓ · v_steer(ℓ) at the residual stream of layers where λ_ℓ > ε.\n\n**Timing Hypothesis Validation:**\nWe explicitly frame the following as a testable hypothesis: geometric margin at sentence boundary N is predictive of factual accuracy in sentence N+1. This is a non-trivial extrapolation from the Attractor Geometry results (which validated margin on first-token factoid completion only). Validation protocol: (1) Generate 500 multi-sentence responses on LongFact/FActScore prompts. (2) Compute margin at every sentence boundary. (3) Annotate each subsequent sentence with FActScore. (4) Measure Spearman correlation between boundary margin and next-sentence factuality. If correlation ρ < 0.3, we fall back to a look-ahead variant: extract margin from the first 3 generated tokens of the new sentence (before committing via speculative-style buffering). The look-ahead variant adds ~15% latency overhead (3 extra forward passes per sentence boundary with rollback capability), which is accounted for in the resource estimate.\n\n**Ablation Design (isolating each contribution):**\n- GTS-full vs. GTS-sequence (ablate sentence gating: single decision per sequence, matching Hallucination Basins)\n- GTS-full vs. GTS-Euclidean (replace Mahalanobis with Euclidean, matching Hallucination Basins and Attractor Geometry)\n- GTS-full vs. GTS-scalar (replace per-layer MLP with single scalar, matching Hallucination Basins' controller)\n- GTS-full vs. GTS-pertoken (apply continuous steering every token, matching Spherical Steering's granularity but with our trigger signal)\n- GTS-full vs. Spherical Steering (direct comparison using their released code)\n- GTS-full vs. Verbal-Uncertainty-Feature (Ji et al. baseline)\n- GTS-full + COAST refinement (combining selective gating with constrained optimization)\n\n**Novelty acknowledgment:** If Mahalanobis does not significantly outperform Euclidean in ablations (a known risk given that both Attractor Geometry and Hallucination Basins succeed with Euclidean), the primary novelty contribution shifts to sentence-level gating + per-layer controller as the mechanism enabling within-sequence selectivity—which remains differentiated from all baselines.\n\nImplementation uses nnsight 0.6 on Qwen3-8B and Llama-3.1-8B-Instruct. Evaluation on TruthfulQA, HaluEval, FaithBench, FActScore, FELM, SimpleQA, LongFact, MT-Bench, MMLU, plus ECE/Brier calibration metrics. Spherical Steering (released code) serves as primary baseline on identical benchmarks.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~200h H100 80GB",
      "gpu_utilization": "Low (~15-20%). GPU idles during code/debug/analysis cycles.",
      "timeline": "3-4 months",
      "team": "1-2 researchers with mechanistic interpretability + geometric ML experience",
      "estimated_gpu_cost": "$600-700 (H100 at ~$3/hr spot)",
      "factScore_api_cost": "$200-400 (GPT-4 entailment checks: ~150 checks/biography × 2 models × ~8 conditions × 200 examples)"
    },
    "human_in_loop": {
      "gpu_hours": "~230h H100 80GB",
      "gpu_utilization": "Moderate (45-55%). Agent queues batches but blocks on geometric design decisions and timing validation analysis.",
      "timeline": "3-4 weeks",
      "team": "1 researcher, ~30min/day reviewing agent proposals",
      "claude_api_cost": "$200-350",
      "estimated_gpu_cost": "$690-800",
      "factScore_api_cost": "$200-400",
      "risk_note": "Timing hypothesis validation and precision-recall threshold calibration benefit from human intuition. If timing hypothesis fails (ρ < 0.3), implementing look-ahead fallback adds ~1 week."
    },
    "auto_research": {
      "gpu_hours": "~240-270h H100 80GB (expanded: PCA-k ablations, Mahalanobis vs. Euclidean, timing validation, Spherical Steering comparison, Hallucination Basins ablations, per-token vs sentence-level ablation, COAST combination, layer weight ablations, two-model validation, 10 benchmarks)",
      "gpu_utilization": "High (~85-90%). Well-defined pipeline with clear ablation structure.",
      "timeline": "10-14 days with 2-4 H100 GPUs running in parallel",
      "team": "0 (initial setup: provision GPUs, configure nnsight, define eval harness, clone Spherical Steering repo)",
      "claude_api_cost": "$350-550 (est. 5000-7000 turns)",
      "estimated_gpu_cost": "$720-810",
      "factScore_api_cost": "$300-500 (higher due to more ablation conditions)",
      "speed_bottleneck": "GPU count for parallel ablation sweeps. Secondary: FActScore GPT-4 API calls (~100s per response). Spherical Steering baseline reproduction requires their codebase setup.",
      "risk_note": "Primary risk: timing hypothesis may fail for multi-sentence generation (Attractor Geometry validated only on factoid completion, authors note 'transfer to open-domain settings requires further study'). Mitigation: look-ahead variant. Secondary risk: Mahalanobis may not beat Euclidean—novelty then rests on sentence-level gating + per-layer controller. Tertiary risk: Spherical Steering's per-token vMF gate may approximate sentence-level selectivity well enough that the explicit gating advantage is marginal."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026)"
  ],
  "level": "top-tier",
  "key_references": [
    "Spherical Steering: Geometry-Aware Activation Rotation for Language Models (arXiv 2602.08169, ICML 2026)",
    "Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination (arXiv 2605.05686, May 2026)",
    "Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations (arXiv 2604.04743, April 2026)",
    "Minimizing Collateral Damage in Activation Steering (arXiv 2605.01167, May 2026)",
    "Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention (FLAS, arXiv 2605.05892, May 2026)",
    "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025 Outstanding Paper, arXiv 2503.14477)",
    "Tethered Reasoning (HELIX): Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering (arXiv 2602.17691, Feb 2026)",
    "Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method (ACT, WWW 2025)",
    "ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment (ICLR 2026, arXiv 2602.17560)",
    "Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (arXiv 2605.13772, May 2026)",
    "DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness (arXiv 2601.14210, Jan 2026)",
    "Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs (arXiv 2505.20309, May 2025)",
    "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits (PCNet, arXiv 2605.05953, May 2026)",
    "Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics (arXiv 2604.15400, April 2026)",
    "Think in Sentences: Explicit Sentence Boundaries Enhance Language Model's Capabilities (arXiv 2604.10135, April 2026)",
    "A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks (Lee et al., NeurIPS 2018)",
    "Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors (SADI, arXiv 2410.12299, 2024)",
    "Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models (ICLR 2026)",
    "Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation (ACL Findings 2025)"
  ],
  "description": "We propose Geometry-Triggered Steering (GTS), a method that introduces sentence-level selective gating to geometry-aware activation steering for factual hallucination suppression. The key insight is that the 'when to steer' decision should operate at claim granularity (sentences), even when 'how to steer' operates at token/layer granularity.\n\nBuilding on the finding that geometric margin separates correct recall from hallucination (AUROC 0.858 on TruthfulQA vs. entropy's 0.656; Liang et al., May 2026), GTS monitors PCA-regularized Mahalanobis distance from residual stream activations to factual cluster centroids at sentence boundaries during generation. When geometric margin indicates basin absence—suggesting the model lacks a memorized attractor for the upcoming content—GTS computes an input-specific steering vector directed toward the factual centroid and applies it with per-layer weights predicted by a lightweight MLP controller. Crucially, sentences where the model is within a factual basin are left untouched.\n\nGTS addresses the granularity mismatch in prior work: (1) vs. Spherical Steering (ICML 2026), which applies per-token rotation with continuous vMF-gated intensity (achieving +15% TruthfulQA MC1), GTS makes binary claim-level steer/skip decisions—enabling complete preservation of correct sub-claims within multi-sentence responses, rather than applying low-intensity steering through all tokens including correct ones. The trigger signals also differ fundamentally: Spherical Steering's vMF gate measures alignment to a fixed truthfulness axis, while GTS's Mahalanobis trigger measures distance from factual attractor basins (knowledge absence vs. directional alignment). (2) vs. Hallucination Basins (April 2026), which uses per-sequence Euclidean distance with a scalar controller on 1B–3B models, GTS introduces within-sequence selectivity, directional covariance, and per-layer control. (3) vs. COAST (May 2026), which optimizes the steering vector via constrained optimization to minimize collateral damage, GTS is complementary—it optimizes when to steer rather than how to steer, and we include a GTS+COAST combination experiment.\n\nWe explicitly validate the timing hypothesis (margin at boundary N predicts factuality of sentence N+1)—a non-trivial extrapolation from factoid completion settings—with a correlation study and provide a look-ahead fallback if the hypothesis fails. Ablations isolate each design choice against matched baselines (sentence-gating ablated, Euclidean substituted, scalar controller substituted, per-token granularity substituted, direct Spherical Steering comparison). We acknowledge that if Mahalanobis does not significantly outperform Euclidean, the primary novelty shifts to sentence-level gating + per-layer controller.\n\nImplementation uses nnsight 0.6 on Qwen3-8B and Llama-3.1-8B-Instruct with Spherical Steering's released code as primary baseline. Evaluation on TruthfulQA, HaluEval, FaithBench, FActScore, FELM, SimpleQA, LongFact, MT-Bench, MMLU, plus ECE/Brier calibration metrics.",
  "project_name": "geometry_triggered_steering",
  "source": "web_research"
}
```

**Summary of changes (minor revision):**

1. **Added Spherical Steering as primary competitor** — positioned as closest baseline with clear differentiation (per-token continuous vMF gate vs. sentence-level binary gating; directional alignment vs. basin distance).
2. **Added COAST and FLAS** — COAST framed as complementary (optimizes how vs. when), FLAS as general-purpose per-token method.
3. **Fixed AUROC reporting** — now leads with TruthfulQA 0.858 (honest), explains synthetic 0.993 is controlled setting only, motivates high-precision thresholding.
4. **De-emphasized "Think in Sentences"** — now cited only as motivating sentence-as-planning-unit hypothesis, explicitly noting it does not analyze hidden-state geometry.
5. **Acknowledged Mahalanobis risk** — explicit statement that if it doesn't outperform Euclidean, novelty shifts to gating + controller.
6. **Added FActScore API costs** — $200-500 depending on condition count.
7. **Removed scale-as-contribution framing** — no longer claims 8B vs 1-3B as an advance.
8. **Added Spherical Steering ablation** — direct comparison using their released code.
9. **Added timing hypothesis risk acknowledgment** — explicitly notes the extrapolation from factoid to open-ended, includes look-ahead latency overhead.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fb9732f-6f75-48ed-9b49-e3700ed46b3a",
  "isSidechain": false,
  "requestId": "req_011Cb5x4LbxPUF5abKLasTMa",
  "type": "assistant",
  "uuid": "c4870f9d-9ce2-49f7-8a8f-cb62a76e150c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VvFs7q7jaAcq8CtL8xCxRS",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1962,
      "cache_read_input_tokens": 33477,
      "output_tokens": 7812,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1962,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7812,
          "cache_read_input_tokens": 33477,
          "cache_creation_input_tokens": 1962,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1962
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-16 (UTC).**  ## Original idea {   \"title\": \"Geometry-Triggered Sentence-Level Activation Steering for Factual Hall…",
  "leafUuid": "c4870f9d-9ce2-49f7-8a8f-cb62a76e150c",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising geometry-triggered steering with competitor analysis",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-16 (UTC).**  ## Original idea {   \"title\": \"Geometry-Triggered Sentence-Level Activation Steering for Factual Hall…",
  "leafUuid": "c4870f9d-9ce2-49f7-8a8f-cb62a76e150c",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising geometry-triggered steering with competitor analysis",
  "sessionId": "05d199d5-3d58-4072-a284-85726a2303cb"
}
```

---
