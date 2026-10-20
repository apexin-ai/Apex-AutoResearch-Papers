# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-16 (UTC).** ## Original idea { "tit

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 74
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-1/50176f91-6e24-4baa-8fdc-ff59abed166c.jsonl`
- **Structured JSON:** [`b85939ef60765cf162d0.json`](../../sessions/b8/b85939ef60765cf162d0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T09:07:23.570Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T09:07:23.570Z",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-16 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Geometry-Triggered Sentence-Level Activation Steering for Factual Hallucination Suppression\",\n  \"core_problem\": \"Recent work (Attractor Geometry of Transformer Memory, May 2026) demonstrates that factual hallucination corresponds to 'basin absence'—the hidden state drifts freely when no memorized attractor basin exists—and that geometric margin separates correct recall from hallucination substantially better than entropy (AUROC 0.858 vs. 0.656 on TruthfulQA; up to 0.993 on controlled factoid tasks). Yet translating geometric margin into targeted activation interventions remains unsolved at the right granularity. Existing methods address 'when to steer' at mismatched granularities: FASB (NeurIPS 2025) introduces token-level probe-based detection with backtracking—the closest prior work on selective steering—but operates reactively (detect deviation, then rollback 10 tokens and regenerate), wasting compute and partially disrupting correct content mid-claim. Hallucination Basins (April 2026) proposes geometry-aware steering but operates at per-sequence granularity—applying uniform corrections across all claims in a response. Spherical Steering (ICML 2026) introduces geometry-aware rotation with an input-adaptive vMF confidence gate, achieving strong TruthfulQA gains, but applies steering per-token without claim-level selectivity. Steering Vector Fields (Feb 2026) learns context-dependent steering directions but always steers at every K-step without gating. COAST (May 2026) addresses utility preservation via constrained optimization of the steering vector itself but does not address when to steer. The gap is a pre-emptive, claim-granular gating mechanism that decides whether to steer before generating each factual unit—avoiding both FASB's corrective overhead and per-token methods' indiscriminate intervention.\",\n  \"opportunity\": \"The critical gap is between detection granularity and intervention granularity, with an additional temporal mismatch (pre-emptive vs. corrective). FASB (NeurIPS 2025) is the closest work addressing 'when to steer,' using linear probes on attention heads with token-level monitoring and backtracking. However, FASB has three structural limitations that create opportunity: (1) It is corrective rather than pre-emptive—it detects deviation after tokens are generated, then rolls back s=10 tokens and regenerates, wasting compute proportional to intervention frequency and partially disrupting coherent sub-claims. (2) Its linear probe measures directional alignment to a learned truthful/hallucinated axis rather than measuring knowledge absence geometrically—a surface-level feature that may not generalize across domains. (3) It operates at token granularity, meaning interventions cut across claim boundaries (a backtrack may split a correct clause from an incorrect one). The unexploited sweet spot is pre-emptive sentence-level gating: sentences are the natural unit of factual claims (the granularity FActScore evaluates, the granularity humans judge, and the granularity at which LLMs perform context integration before next-sentence planning). A system that (1) detects basin absence at sentence boundaries before generating the next claim, (2) makes binary steer/skip decisions at claim granularity (preserving entire correct sentences untouched), and (3) uses per-layer intensity control provides a 'when + where + how much' framework that is pre-emptive (no wasted tokens), atomic (entire claims preserved or steered), and geometrically principled (Mahalanobis distance measuring knowledge absence rather than directional alignment).\",\n  \"landscape\": \"**Selective steering (closest competitors):** FASB (arXiv 2508.17621, NeurIPS 2025) is the most direct competitor, addressing 'when to steer' via linear probes trained on attention head activations. It monitors the concatenated question-and-generated-content states, triggers intervention when deviation is detected, and backtracks s=10 tokens to regenerate with steering. Achieves MC1 48.71% on TruthfulQA (LLaMA-2-7B-Chat, up from 33.41% baseline). Operates at token-level with top-24 attention heads. GTS differs in three fundamental ways: (a) pre-emptive gating at sentence boundaries (no wasted tokens, no rollback) vs. FASB's corrective backtracking (regenerates 10 tokens per intervention); (b) Mahalanobis basin-distance trigger measuring knowledge absence from factual attractor geometry vs. FASB's linear probe measuring learned directional alignment on attention heads; (c) atomic claim-level decisions (entire sentences preserved or steered) vs. FASB's token-level cuts that may split coherent claims. FASB's backtracking overhead scales linearly with intervention frequency—for hallucination-dense passages, this means significant wasted compute.\\n\\n**Geometry-aware steering:** Spherical Steering (arXiv 2602.08169, ICML 2026) uses geodesic rotation with a von Mises-Fisher confidence gate that dynamically modulates per-token steering strength based on cosine alignment to truthful/hallucinated directions. Achieves MC1 +15.80% on TruthfulQA (Llama-3.1-8B) while preserving generation quality. Operates per-token with single-layer intervention (layer 24). GTS differs via sentence-level binary gating (skip entire correct claims), Mahalanobis basin-distance trigger (knowledge absence vs. directional alignment), and per-layer MLP controller. Hallucination Basins (arXiv 2604.04743, April 2026) proposes Adaptive Geometry-Aware Steering using centroid-difference vectors, Euclidean distance trigger (dbasin = ||h − μ||₂), and a learned scalar map trained via logistic regression on geometric features (minimum basin distance + mean contraction ratio) at per-sequence granularity. Tested on Llama-3.2-1B/3B, Qwen-2.5-1.5B, Gemma-2-2B, Llama-3.1-8B, and Mistral-7B. GTS advances beyond it via sentence-level within-sequence selectivity, Mahalanobis distance (covariance-aware), and per-layer controller.\\n\\n**Context-dependent steering directions:** Steering Vector Fields (SVF, arXiv 2602.01654, Feb 2026) learns a differentiable concept scoring MLP whose gradient defines context-aware steering directions, refreshed every K steps during generation. Tested on Llama-2-7b and Qwen3-14b. SVF addresses 'how to steer' (varying directions) but always steers—no gating mechanism. GTS is complementary: it addresses 'whether to steer' (binary gating) while SVF addresses 'in which direction.' These could be combined (sentence-gated SVF directions).\\n\\n**Nonlinear geometry-aware approaches:** Curveball Steering (arXiv 2603.09313, March 2026) demonstrates substantial geometric distortion in activation spaces (measured via geodesic/Euclidean distance ratios) and proposes nonlinear polynomial kernel PCA for steering, outperforming linear PCA-based steering. Relevant as evidence that activation geometry is non-trivially curved—supporting the use of Mahalanobis (covariance-aware) over Euclidean distance.\\n\\n**Utility-preservation approaches:** COAST (arXiv 2605.01167, May 2026) formalizes collateral damage as unintended feature-direction shifts and solves steering as constrained optimization. Complementary to GTS: COAST optimizes the steering vector, GTS optimizes when to apply it. FLAS (arXiv 2605.05892, May 2026) learns a concept-conditioned velocity field for multi-step token-level activation transport. Not hallucination-specific and does not use geometric triggers.\\n\\n**Hallucination detection (analysis-only):** Attractor Geometry of Transformer Memory (arXiv 2605.05686, May 2026) demonstrates hallucination = basin absence with geometric margin AUROC 0.858 on TruthfulQA (vs. entropy 0.656), 0.993 on controlled factoid tasks. PCNet (arXiv 2605.05953, May 2026) detects hallucinations as geometric anomalies and applies contrastive decoding at token level. Where Does Reasoning Break? (arXiv 2605.13772, May 2026) detects step-level hallucination via transport geometry but proposes no intervention. DRIFT (arXiv 2601.14210, Jan 2026) detects representational instability.\\n\\n**Calibration/expression:** Calibrating Verbal Uncertainty as a Linear Feature (Ji et al., EMNLP 2025 Outstanding Paper) achieves ~31.9% reduction in confident hallucinations via linear-feature intervention. Calibrates uncertainty expression without correcting underlying generation—complementary.\\n\\n**Other steering methods:** ACT (WWW 2025) uses K-means clustered corpus-averaged vectors. ODESteer (ICLR 2026) achieves 5.7% over ACT via ODE-based multi-step steering but remains input-oblivious. Guiding Giants/WAS (arXiv 2505.20309) trains lightweight controllers for layer-aware weighted activation steering. SADI (arXiv 2410.12299) constructs input-specific dynamic steering vectors. HELIX/Tethered Reasoning (arXiv 2602.17691) uses Mahalanobis distance + graduated steering for structural coherence in quantized models.\\n\\n**Supporting evidence:** Hallucination as Trajectory Commitment (arXiv 2604.15400, April 2026) provides causal evidence for early commitment with asymmetric attractor dynamics, supporting timely intervention before commitment propagates. Think in Sentences (arXiv 2604.10135, April 2026) demonstrates sentence boundary attention concentration patterns consistent with context integration cycles.\",\n  \"approach\": \"We propose Geometry-Triggered Steering (GTS), a method that bridges the detection-to-intervention gap by introducing pre-emptive sentence-level selective gating to geometry-aware activation steering. The key insight is that the 'when to steer' decision should be (a) pre-emptive (decided before generating the next claim, not corrective after deviation), (b) atomic at claim granularity (entire sentences preserved or steered, not partially disrupted), and (c) geometrically principled (measuring knowledge absence rather than learned directional features).\\n\\n**Stage 1: TRIGGER (PCA-Regularized Geometric Margin at Sentence Boundaries)**\\nDuring generation, at each sentence boundary (detected via period/newline tokens), extract hidden-state activations at the boundary token across layers using nnsight intervention hooks. Compute geometric margin using class-conditional PCA-regularized Mahalanobis distance:\\n(a) Offline: From a calibration set (~2K examples from TruthfulQA + FELM correct-answer forward passes), collect hidden states at factual completion positions. Apply PCA to project from full hidden dimension (d=4096) to top-k principal components (k=256), reducing covariance estimation to a well-conditioned 256×256 matrix.\\n(b) Online: Project the boundary token's activation into the PCA subspace, compute Mahalanobis distance to nearest factual cluster centroid: δ(x) = √((h_pca - μ_pca)ᵀ Σ_pca⁻¹ (h_pca - μ_pca)).\\n(c) When δ exceeds a calibrated threshold (set via precision-recall analysis on validation split targeting high precision to minimize false interventions), flag the upcoming sentence for intervention.\\n\\n**Trigger reliability note:** Geometric margin achieves AUROC 0.858 on TruthfulQA (vs. entropy 0.656)—sufficient for selective intervention with appropriate thresholding, though far from the 0.993 achieved on synthetic factoid tasks. This motivates operating at high-precision thresholds (accepting lower recall) so that when GTS intervenes, it is likely correct.\\n\\n**Comparison to FASB's trigger:** FASB trains a linear probe p(x) = sigmoid(⟨θ, x⟩) on attention head activations to detect deviation from desired behavior. This measures directional alignment—a learned surface feature that requires the model to have already begun deviating. GTS's Mahalanobis trigger measures geometric distance from factual attractor basins—detecting knowledge absence before the model commits to hallucination. This is pre-emptive rather than corrective, and grounded in attractor geometry rather than learned classification boundaries.\\n\\n**Stage 2: DIRECTION (Centroid-Directed Steering Vector)**\\nCompute the steering direction as the unit vector from the current activation toward the factual cluster centroid at each layer in the PCA subspace, then project back to full space: v_steer = (μ_pca - h_pca) / ||μ_pca - h_pca||, lifted back to full dimensionality via PCA inverse transform. This yields an input-specific correction direction toward regions of successful fact recall. We additionally experiment with a COAST-style constrained refinement of this vector to minimize collateral damage.\\n\\n**Stage 3: INTENSITY (Per-Layer MLP Controller)**\\nA lightweight 2-layer MLP controller (hidden dim 64, inspired by Guiding Giants/WAS) takes [geometric_margin, layer_index/L, margin_velocity] as input (3D feature vector) and predicts per-layer steering weight λ_ℓ. The controller is trained on a calibration set (~2K examples) via a combined objective: maximize FActScore on steered outputs while minimizing perplexity increase on outputs where margin is below threshold. Steering is applied: h_steered(ℓ) = h(ℓ) + λ_ℓ · v_steer(ℓ) at the residual stream of layers where λ_ℓ > ε.\\n\\n**Timing Hypothesis Validation:**\\nWe explicitly frame the following as a testable hypothesis: geometric margin at sentence boundary N is predictive of factual accuracy in sentence N+1. Validation protocol: (1) Generate 500 multi-sentence responses on LongFact/FActScore prompts. (2) Compute margin at every sentence boundary. (3) Annotate each subsequent sentence with FActScore. (4) Measure Spearman correlation between boundary margin and next-sentence factuality. If correlation ρ < 0.3, we fall back to a look-ahead variant: extract margin from the first 3 generated tokens of the new sentence (before committing via speculative-style buffering). The look-ahead variant adds ~15% latency overhead.\\n\\n**Ablation Design (isolating each contribution):**\\n- GTS-full vs. GTS-sequence (ablate sentence gating: single decision per sequence, matching Hallucination Basins)\\n- GTS-full vs. GTS-Euclidean (replace Mahalanobis with Euclidean, matching Hallucination Basins' trigger)\\n- GTS-full vs. GTS-scalar (replace per-layer MLP with single scalar map, matching Hallucination Basins' controller)\\n- GTS-full vs. GTS-pertoken (apply continuous steering every token, matching Spherical Steering's granularity with our trigger signal)\\n- GTS-full vs. GTS-FASB-trigger (replace Mahalanobis trigger with FASB-style linear probe on attention heads, isolating the trigger mechanism contribution)\\n- GTS-full vs. Spherical Steering (direct comparison using their released code)\\n- GTS-full vs. FASB (direct comparison using their released code, github.com/gjw185/FASB)\\n- GTS-full + COAST refinement (combining selective gating with constrained optimization)\\n\\n**Novelty acknowledgment:** If Mahalanobis does not significantly outperform Euclidean in ablations, the primary novelty contribution rests on pre-emptive sentence-level gating + per-layer controller as the mechanism enabling within-sequence selectivity without backtracking—which remains differentiated from all baselines including FASB.\\n\\nImplementation uses nnsight 0.6 on Qwen3-8B and Llama-3.1-8B-Instruct. Evaluation on TruthfulQA, HaluEval, FaithBench, FActScore, SimpleQA, LongFact, MT-Bench (7 primary benchmarks), plus ECE/Brier calibration metrics. Spherical Steering (released code) and FASB (released code) serve as primary baselines.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~180h H100 80GB\",\n      \"gpu_utilization\": \"Low (~15-20%). GPU idles during code/debug/analysis cycles.\",\n      \"timeline\": \"3-4 months\",\n      \"team\": \"1-2 researchers with mechanistic interpretability + geometric ML experience\",\n      \"estimated_gpu_cost\": \"$540-600 (H100 at ~$3/hr spot)\",\n      \"factScore_api_cost\": \"$150-300 (GPT-4 entailment checks: ~150 checks/biography × 2 models × ~6 conditions × 150 examples)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~195h H100 80GB\",\n      \"gpu_utilization\": \"Moderate (45-55%). Agent queues batches but blocks on geometric design decisions and timing validation analysis.\",\n      \"timeline\": \"3-4 weeks\",\n      \"team\": \"1 researcher, ~30min/day reviewing agent proposals\",\n      \"claude_api_cost\": \"$200-350\",\n      \"estimated_gpu_cost\": \"$585-650\",\n      \"factScore_api_cost\": \"$150-300\",\n      \"risk_note\": \"Timing hypothesis validation and precision-recall threshold calibration benefit from human intuition. If timing hypothesis fails (ρ < 0.3), implementing look-ahead fallback adds ~1 week.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~195-200h H100 80GB\",\n      \"gpu_utilization\": \"High (~85-90%). Well-defined pipeline with clear ablation structure.\",\n      \"timeline\": \"10-12 days with 2-4 H100 GPUs running in parallel\",\n      \"team\": \"0 (initial setup: provision GPUs, configure nnsight, define eval harness, clone Spherical Steering + FASB repos)\",\n      \"claude_api_cost\": \"$350-500 (est. 4500-6000 turns)\",\n      \"estimated_gpu_cost\": \"$585-600\",\n      \"factScore_api_cost\": \"$200-350 (higher due to more ablation conditions)\",\n      \"speed_bottleneck\": \"GPU count for parallel ablation sweeps. Secondary: FActScore GPT-4 API calls.\",\n      \"resource_optimization\": \"Budget achieved via: (1) full 7-benchmark evaluation only on GTS-full, Spherical Steering, FASB, and GTS+COAST (4 conditions); (2) 4-benchmark core set (TruthfulQA, FActScore, SimpleQA, MT-Bench) for ablation variants (4 conditions); (3) Mahalanobis-vs-Euclidean and scalar-vs-MLP ablations combined into a 2×2 grid rather than separate sweeps; (4) single model (Llama-3.1-8B) for ablations, both models for final results only.\",\n      \"risk_note\": \"Primary risk: timing hypothesis may fail for multi-sentence generation (Attractor Geometry validated only on factoid completion). Mitigation: look-ahead variant (~10h additional if needed). Secondary risk: Mahalanobis may not beat Euclidean—novelty then rests on pre-emptive sentence-level gating + per-layer controller. Tertiary risk: FASB's simpler probe mechanism may achieve comparable selective-steering quality on short-form QA benchmarks—GTS's advantage is expected to be strongest on long-form generation (FActScore, LongFact) where multiple claims coexist.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Steering When Necessary: Flexible Steering Large Language Models with Backtracking (FASB, arXiv 2508.17621, NeurIPS 2025)\",\n    \"Spherical Steering: Geometry-Aware Activation Rotation for Language Models (arXiv 2602.08169, ICML 2026)\",\n    \"Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination (arXiv 2605.05686, May 2026)\",\n    \"Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations (arXiv 2604.04743, April 2026)\",\n    \"Steering Vector Fields for Context-Aware Inference-Time Control in Large Language Models (SVF, arXiv 2602.01654, Feb 2026)\",\n    \"Curveball Steering: The Right Direction To Steer Isn't Always Linear (arXiv 2603.09313, March 2026)\",\n    \"Minimizing Collateral Damage in Activation Steering (COAST, arXiv 2605.01167, May 2026)\",\n    \"Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention (FLAS, arXiv 2605.05892, May 2026)\",\n    \"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025 Outstanding Paper, arXiv 2503.14477)\",\n    \"Tethered Reasoning (HELIX): Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering (arXiv 2602.17691, Feb 2026)\",\n    \"Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method (ACT, WWW 2025)\",\n    \"ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment (ICLR 2026, arXiv 2602.17560)\",\n    \"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (arXiv 2605.13772, May 2026)\",\n    \"DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness (arXiv 2601.14210, Jan 2026)\",\n    \"Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs (arXiv 2505.20309, May 2025)\",\n    \"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits (PCNet, arXiv 2605.05953, May 2026)\",\n    \"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics (arXiv 2604.15400, April 2026)\",\n    \"Think in Sentences: Explicit Sentence Boundaries Enhance Language Model's Capabilities (arXiv 2604.10135, April 2026)\",\n    \"A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks (Lee et al., NeurIPS 2018)\",\n    \"Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors (SADI, arXiv 2410.12299, 2024)\",\n    \"Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models (ICLR 2026)\"\n  ],\n  \"description\": \"We propose Geometry-Triggered Steering (GTS), a method that introduces pre-emptive sentence-level selective gating to geometry-aware activation steering for factual hallucination suppression. The key insight is that the 'when to steer' decision should be pre-emptive (decided before generating), atomic at claim granularity (sentences), and geometrically principled (measuring knowledge absence).\\n\\nBuilding on the finding that geometric margin separates correct recall from hallucination (AUROC 0.858 on TruthfulQA; Liang et al., May 2026), GTS monitors PCA-regularized Mahalanobis distance from residual stream activations to factual cluster centroids at sentence boundaries during generation. When geometric margin indicates basin absence—suggesting the model lacks a memorized attractor for the upcoming content—GTS computes an input-specific steering vector directed toward the factual centroid and applies it with per-layer weights predicted by a lightweight MLP controller. Sentences where the model is within a factual basin are left entirely untouched.\\n\\nGTS addresses limitations in the most direct prior work on selective steering: (1) vs. FASB (NeurIPS 2025), which achieves MC1 48.71% on TruthfulQA via token-level probe monitoring + 10-token backtracking, GTS is pre-emptive rather than corrective—it gates before generating rather than detecting deviation and rolling back. This eliminates wasted compute from backtracking (which scales with intervention frequency) and preserves claim coherence (no mid-sentence rollbacks). GTS's Mahalanobis trigger measures geometric knowledge absence from attractor basins, while FASB's linear probe measures learned directional alignment on attention heads—a surface feature that requires deviation to have already begun. (2) vs. Spherical Steering (ICML 2026, +15% TruthfulQA MC1), which applies per-token rotation with continuous vMF-gated intensity, GTS makes binary claim-level steer/skip decisions—enabling complete preservation of correct sub-claims. The trigger signals differ: vMF gate measures alignment to a fixed truthfulness axis; Mahalanobis measures distance from factual attractor basins. (3) vs. Steering Vector Fields (Feb 2026), which learns context-dependent steering directions refreshed every K steps but always steers, GTS decides whether to steer at all—complementary approaches that could be combined. (4) vs. Hallucination Basins (April 2026), which uses per-sequence Euclidean distance with a logistic-regression scalar map on 1B–8B models, GTS introduces within-sequence selectivity, covariance-aware distance, and per-layer control. (5) vs. COAST (May 2026), which optimizes the steering vector, GTS optimizes when to apply it—the combination (sentence-gated COAST) is included as an experiment.\\n\\nWe explicitly validate the timing hypothesis (margin at boundary N predicts factuality of sentence N+1) with a correlation study and provide a look-ahead fallback if it fails. Ablations isolate each design choice including a direct comparison with FASB's probe-based trigger mechanism (using their released code) to quantify the value of geometric vs. directional triggers. We hypothesize GTS's advantage over FASB will be strongest on long-form generation benchmarks (FActScore, LongFact) where multiple claims coexist and backtracking overhead compounds.\\n\\nImplementation uses nnsight 0.6 on Qwen3-8B and Llama-3.1-8B-Instruct. Resource-optimized evaluation: full 7-benchmark suite (TruthfulQA, HaluEval, FaithBench, FActScore, SimpleQA, LongFact, MT-Bench) on GTS-full and primary baselines; 4-benchmark core set for ablation variants. Total budget: ≤200 H100-hours.\",\n  \"project_name\": \"geometry_triggered_steering\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 5)\nIssues: [\"INSUFFICIENT PCNet DIFFERENTIATION: PCNet (arXiv 2605.05953, May 2026) is conceptually very close to GTS—both detect geometric anomaly from factual manifold and selectively intervene only at deviant positions during decoding. PCNet uses NLL via probabilistic circuits as gate + contrastive decoding; GTS uses Mahalanobis as gate + activation addition. The proposal mentions PCNet in one sentence ('detects hallucinations as geometric anomalies and applies contrastive decoding at token level') but does NOT provide explicit differentiation paragraphs like it does for FASB and Spherical Steering. Since PCNet is a May 2026 concurrent work with the same 'selective geometric gating' paradigm, it needs head-to-head comparison or at minimum a clear argument for why sentence-level activation addition is preferable to token-level contrastive decoding.\", \"FOUNDATIONAL AUROC USES EUCLIDEAN, NOT MAHALANOBIS: The 0.858 AUROC on TruthfulQA that motivates GTS's trigger comes from the Attractor Geometry paper, which explicitly uses Euclidean distance: δ(x) = min_i ||h(x) − m_i||₂. The proposal builds on this result to argue for a Mahalanobis trigger—but this is an unvalidated modification, not a validated foundation. The framing 'Building on the finding that geometric margin separates correct recall from hallucination (AUROC 0.858)' + then proposing Mahalanobis distance could mislead reviewers into thinking Mahalanobis achieves 0.858. The proposal should clarify: 'The Attractor Geometry paper demonstrates Euclidean geometric margin achieves AUROC 0.858; we hypothesize that Mahalanobis distance (covariance-aware) can improve this by accounting for directional anisotropy in representation space, and ablate this choice.'\", \"TIMELINE HAS NO BUFFER: Auto estimate is 10-12 days for an 11-day budget (May 14→May 25). With 2 days already elapsed (today is May 16), only 9 days remain. The proposal should define a 'minimum viable paper' scope that fits in 8 days (leaving 1 day for writing/formatting), e.g., dropping the COAST combination experiment and reducing ablation conditions to a 2×2 grid (Euclidean vs. Mahalanobis × sentence vs. token) + FASB baseline + Spherical Steering baseline.\", \"TIMING HYPOTHESIS VALIDATION LACKING SUPPORTING EVIDENCE: The Attractor Geometry paper explicitly states all experiments measure signals 'at the first-digit position, before autoregressive dynamics compound' and 'transfer to open-domain settings requires further study.' The proposal's hypothesis that margin at sentence boundary N predicts factuality of sentence N+1 during multi-sentence open-ended generation is a substantial extrapolation. While the fallback (look-ahead variant) is specified, the proposal should note that the Attractor Geometry paper's disclaimer makes this extrapolation less certain than the 0.858 AUROC suggests.\"]\nFeedback: The proposal has matured substantially over 5 rounds and the competitive landscape is now comprehensive. Three targeted changes would strengthen it for the next round:\n\n1. **Add explicit PCNet differentiation paragraph**: 'PCNet (2605.05953) detects hallucination via NLL anomaly from a probabilistic circuit and applies contrastive decoding selectively at token level—the same paradigm as GTS (detect geometric anomaly → selectively intervene). GTS differs in: (a) granularity: sentence-level binary decisions preserve entire correct claims and avoid token-level overhead (PCNet evaluates NLL at every token position); (b) intervention mechanism: activation steering preserves the model's own generation distribution shifted toward factual attractors, while contrastive decoding requires maintaining two forward passes (original + modified logits); (c) trigger interpretability: Mahalanobis distance has a clear geometric interpretation (distance from factual cluster in PCA subspace) while NLL from a trained probabilistic circuit is less transparent. We include PCNet as an ablation baseline if their code is available.'\n\n2. **Clarify the Euclidean→Mahalanobis extrapolation**: Add a sentence: 'Note: the 0.858 AUROC was achieved with Euclidean distance; our use of Mahalanobis distance is a hypothesized improvement motivated by OOD detection literature (Lee et al., NeurIPS 2018), which we validate via ablation. If Mahalanobis does not significantly outperform Euclidean, the primary novelty rests on pre-emptive sentence-level gating.'\n\n3. **Define minimum viable scope for 9 remaining days**: Propose a reduced-scope plan: (a) Core experiments on Llama-3.1-8B only (Qwen3-8B as secondary if time permits); (b) 4-benchmark core evaluation (TruthfulQA, FActScore, SimpleQA, MT-Bench) for all conditions; (c) Full 7-benchmark suite only on GTS-full vs. Spherical Steering vs. FASB; (d) Timing hypothesis validation as first milestone (day 1-2)—if it fails immediately, pivot to look-ahead variant rather than spending time on other experiments first.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 5 轮修订，近 3 轮的平均分从 3.2 到 3.5，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T09:07:23.576Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T09:07:23.576Z",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c"
}
```

---

## Round 1

72 recorded events

### User

_source line 3 · 2026-05-16T09:07:23.609Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-16 (UTC).**

## Original idea
{
  "title": "Geometry-Triggered Sentence-Level Activation Steering for Factual Hallucination Suppression",
  "core_problem": "Recent work (Attractor Geometry of Transformer Memory, May 2026) demonstrates that factual hallucination corresponds to 'basin absence'—the hidden state drifts freely when no memorized attractor basin exists—and that geometric margin separates correct recall from hallucination substantially better than entropy (AUROC 0.858 vs. 0.656 on TruthfulQA; up to 0.993 on controlled factoid tasks). Yet translating geometric margin into targeted activation interventions remains unsolved at the right granularity. Existing methods address 'when to steer' at mismatched granularities: FASB (NeurIPS 2025) introduces token-level probe-based detection with backtracking—the closest prior work on selective steering—but operates reactively (detect deviation, then rollback 10 tokens and regenerate), wasting compute and partially disrupting correct content mid-claim. Hallucination Basins (April 2026) proposes geometry-aware steering but operates at per-sequence granularity—applying uniform corrections across all claims in a response. Spherical Steering (ICML 2026) introduces geometry-aware rotation with an input-adaptive vMF confidence gate, achieving strong TruthfulQA gains, but applies steering per-token without claim-level selectivity. Steering Vector Fields (Feb 2026) learns context-dependent steering directions but always steers at every K-step without gating. COAST (May 2026) addresses utility preservation via constrained optimization of the steering vector itself but does not address when to steer. The gap is a pre-emptive, claim-granular gating mechanism that decides whether to steer before generating each factual unit—avoiding both FASB's corrective overhead and per-token methods' indiscriminate intervention.",
  "opportunity": "The critical gap is between detection granularity and intervention granularity, with an additional temporal mismatch (pre-emptive vs. corrective). FASB (NeurIPS 2025) is the closest work addressing 'when to steer,' using linear probes on attention heads with token-level monitoring and backtracking. However, FASB has three structural limitations that create opportunity: (1) It is corrective rather than pre-emptive—it detects deviation after tokens are generated, then rolls back s=10 tokens and regenerates, wasting compute proportional to intervention frequency and partially disrupting coherent sub-claims. (2) Its linear probe measures directional alignment to a learned truthful/hallucinated axis rather than measuring knowledge absence geometrically—a surface-level feature that may not generalize across domains. (3) It operates at token granularity, meaning interventions cut across claim boundaries (a backtrack may split a correct clause from an incorrect one). The unexploited sweet spot is pre-emptive sentence-level gating: sentences are the natural unit of factual claims (the granularity FActScore evaluates, the granularity humans judge, and the granularity at which LLMs perform context integration before next-sentence planning). A system that (1) detects basin absence at sentence boundaries before generating the next claim, (2) makes binary steer/skip decisions at claim granularity (preserving entire correct sentences untouched), and (3) uses per-layer intensity control provides a 'when + where + how much' framework that is pre-emptive (no wasted tokens), atomic (entire claims preserved or steered), and geometrically principled (Mahalanobis distance measuring knowledge absence rather than directional alignment).",
  "landscape": "**Selective steering (closest competitors):** FASB (arXiv 2508.17621, NeurIPS 2025) is the most direct competitor, addressing 'when to steer' via linear probes trained on attention head activations. It monitors the concatenated question-and-generated-content states, triggers intervention when deviation is detected, and backtracks s=10 tokens to regenerate with steering. Achieves MC1 48.71% on TruthfulQA (LLaMA-2-7B-Chat, up from 33.41% baseline). Operates at token-level with top-24 attention heads. GTS differs in three fundamental ways: (a) pre-emptive gating at sentence boundaries (no wasted tokens, no rollback) vs. FASB's corrective backtracking (regenerates 10 tokens per intervention); (b) Mahalanobis basin-distance trigger measuring knowledge absence from factual attractor geometry vs. FASB's linear probe measuring learned directional alignment on attention heads; (c) atomic claim-level decisions (entire sentences preserved or steered) vs. FASB's token-level cuts that may split coherent claims. FASB's backtracking overhead scales linearly with intervention frequency—for hallucination-dense passages, this means significant wasted compute.\n\n**Geometry-aware steering:** Spherical Steering (arXiv 2602.08169, ICML 2026) uses geodesic rotation with a von Mises-Fisher confidence gate that dynamically modulates per-token steering strength based on cosine alignment to truthful/hallucinated directions. Achieves MC1 +15.80% on TruthfulQA (Llama-3.1-8B) while preserving generation quality. Operates per-token with single-layer intervention (layer 24). GTS differs via sentence-level binary gating (skip entire correct claims), Mahalanobis basin-distance trigger (knowledge absence vs. directional alignment), and per-layer MLP controller. Hallucination Basins (arXiv 2604.04743, April 2026) proposes Adaptive Geometry-Aware Steering using centroid-difference vectors, Euclidean distance trigger (dbasin = ||h − μ||₂), and a learned scalar map trained via logistic regression on geometric features (minimum basin distance + mean contraction ratio) at per-sequence granularity. Tested on Llama-3.2-1B/3B, Qwen-2.5-1.5B, Gemma-2-2B, Llama-3.1-8B, and Mistral-7B. GTS advances beyond it via sentence-level within-sequence selectivity, Mahalanobis distance (covariance-aware), and per-layer controller.\n\n**Context-dependent steering directions:** Steering Vector Fields (SVF, arXiv 2602.01654, Feb 2026) learns a differentiable concept scoring MLP whose gradient defines context-aware steering directions, refreshed every K steps during generation. Tested on Llama-2-7b and Qwen3-14b. SVF addresses 'how to steer' (varying directions) but always steers—no gating mechanism. GTS is complementary: it addresses 'whether to steer' (binary gating) while SVF addresses 'in which direction.' These could be combined (sentence-gated SVF directions).\n\n**Nonlinear geometry-aware approaches:** Curveball Steering (arXiv 2603.09313, March 2026) demonstrates substantial geometric distortion in activation spaces (measured via geodesic/Euclidean distance ratios) and proposes nonlinear polynomial kernel PCA for steering, outperforming linear PCA-based steering. Relevant as evidence that activation geometry is non-trivially curved—supporting the use of Mahalanobis (covariance-aware) over Euclidean distance.\n\n**Utility-preservation approaches:** COAST (arXiv 2605.01167, May 2026) formalizes collateral damage as unintended feature-direction shifts and solves steering as constrained optimization. Complementary to GTS: COAST optimizes the steering vector, GTS optimizes when to apply it. FLAS (arXiv 2605.05892, May 2026) learns a concept-conditioned velocity field for multi-step token-level activation transport. Not hallucination-specific and does not use geometric triggers.\n\n**Hallucination detection (analysis-only):** Attractor Geometry of Transformer Memory (arXiv 2605.05686, May 2026) demonstrates hallucination = basin absence with geometric margin AUROC 0.858 on TruthfulQA (vs. entropy 0.656), 0.993 on controlled factoid tasks. PCNet (arXiv 2605.05953, May 2026) detects hallucinations as geometric anomalies and applies contrastive decoding at token level. Where Does Reasoning Break? (arXiv 2605.13772, May 2026) detects step-level hallucination via transport geometry but proposes no intervention. DRIFT (arXiv 2601.14210, Jan 2026) detects representational instability.\n\n**Calibration/expression:** Calibrating Verbal Uncertainty as a Linear Feature (Ji et al., EMNLP 2025 Outstanding Paper) achieves ~31.9% reduction in confident hallucinations via linear-feature intervention. Calibrates uncertainty expression without correcting underlying generation—complementary.\n\n**Other steering methods:** ACT (WWW 2025) uses K-means clustered corpus-averaged vectors. ODESteer (ICLR 2026) achieves 5.7% over ACT via ODE-based multi-step steering but remains input-oblivious. Guiding Giants/WAS (arXiv 2505.20309) trains lightweight controllers for layer-aware weighted activation steering. SADI (arXiv 2410.12299) constructs input-specific dynamic steering vectors. HELIX/Tethered Reasoning (arXiv 2602.17691) uses Mahalanobis distance + graduated steering for structural coherence in quantized models.\n\n**Supporting evidence:** Hallucination as Trajectory Commitment (arXiv 2604.15400, April 2026) provides causal evidence for early commitment with asymmetric attractor dynamics, supporting timely intervention before commitment propagates. Think in Sentences (arXiv 2604.10135, April 2026) demonstrates sentence boundary attention concentration patterns consistent with context integration cycles.",
  "approach": "We propose Geometry-Triggered Steering (GTS), a method that bridges the detection-to-intervention gap by introducing pre-emptive sentence-level selective gating to geometry-aware activation steering. The key insight is that the 'when to steer' decision should be (a) pre-emptive (decided before generating the next claim, not corrective after deviation), (b) atomic at claim granularity (entire sentences preserved or steered, not partially disrupted), and (c) geometrically principled (measuring knowledge absence rather than learned directional features).\n\n**Stage 1: TRIGGER (PCA-Regularized Geometric Margin at Sentence Boundaries)**\nDuring generation, at each sentence boundary (detected via period/newline tokens), extract hidden-state activations at the boundary token across layers using nnsight intervention hooks. Compute geometric margin using class-conditional PCA-regularized Mahalanobis distance:\n(a) Offline: From a calibration set (~2K examples from TruthfulQA + FELM correct-answer forward passes), collect hidden states at factual completion positions. Apply PCA to project from full hidden dimension (d=4096) to top-k principal components (k=256), reducing covariance estimation to a well-conditioned 256×256 matrix.\n(b) Online: Project the boundary token's activation into the PCA subspace, compute Mahalanobis distance to nearest factual cluster centroid: δ(x) = √((h_pca - μ_pca)ᵀ Σ_pca⁻¹ (h_pca - μ_pca)).\n(c) When δ exceeds a calibrated threshold (set via precision-recall analysis on validation split targeting high precision to minimize false interventions), flag the upcoming sentence for intervention.\n\n**Trigger reliability note:** Geometric margin achieves AUROC 0.858 on TruthfulQA (vs. entropy 0.656)—sufficient for selective intervention with appropriate thresholding, though far from the 0.993 achieved on synthetic factoid tasks. This motivates operating at high-precision thresholds (accepting lower recall) so that when GTS intervenes, it is likely correct.\n\n**Comparison to FASB's trigger:** FASB trains a linear probe p(x) = sigmoid(⟨θ, x⟩) on attention head activations to detect deviation from desired behavior. This measures directional alignment—a learned surface feature that requires the model to have already begun deviating. GTS's Mahalanobis trigger measures geometric distance from factual attractor basins—detecting knowledge absence before the model commits to hallucination. This is pre-emptive rather than corrective, and grounded in attractor geometry rather than learned classification boundaries.\n\n**Stage 2: DIRECTION (Centroid-Directed Steering Vector)**\nCompute the steering direction as the unit vector from the current activation toward the factual cluster centroid at each layer in the PCA subspace, then project back to full space: v_steer = (μ_pca - h_pca) / ||μ_pca - h_pca||, lifted back to full dimensionality via PCA inverse transform. This yields an input-specific correction direction toward regions of successful fact recall. We additionally experiment with a COAST-style constrained refinement of this vector to minimize collateral damage.\n\n**Stage 3: INTENSITY (Per-Layer MLP Controller)**\nA lightweight 2-layer MLP controller (hidden dim 64, inspired by Guiding Giants/WAS) takes [geometric_margin, layer_index/L, margin_velocity] as input (3D feature vector) and predicts per-layer steering weight λ_ℓ. The controller is trained on a calibration set (~2K examples) via a combined objective: maximize FActScore on steered outputs while minimizing perplexity increase on outputs where margin is below threshold. Steering is applied: h_steered(ℓ) = h(ℓ) + λ_ℓ · v_steer(ℓ) at the residual stream of layers where λ_ℓ > ε.\n\n**Timing Hypothesis Validation:**\nWe explicitly frame the following as a testable hypothesis: geometric margin at sentence boundary N is predictive of factual accuracy in sentence N+1. Validation protocol: (1) Generate 500 multi-sentence responses on LongFact/FActScore prompts. (2) Compute margin at every sentence boundary. (3) Annotate each subsequent sentence with FActScore. (4) Measure Spearman correlation between boundary margin and next-sentence factuality. If correlation ρ < 0.3, we fall back to a look-ahead variant: extract margin from the first 3 generated tokens of the new sentence (before committing via speculative-style buffering). The look-ahead variant adds ~15% latency overhead.\n\n**Ablation Design (isolating each contribution):**\n- GTS-full vs. GTS-sequence (ablate sentence gating: single decision per sequence, matching Hallucination Basins)\n- GTS-full vs. GTS-Euclidean (replace Mahalanobis with Euclidean, matching Hallucination Basins' trigger)\n- GTS-full vs. GTS-scalar (replace per-layer MLP with single scalar map, matching Hallucination Basins' controller)\n- GTS-full vs. GTS-pertoken (apply continuous steering every token, matching Spherical Steering's granularity with our trigger signal)\n- GTS-full vs. GTS-FASB-trigger (replace Mahalanobis trigger with FASB-style linear probe on attention heads, isolating the trigger mechanism contribution)\n- GTS-full vs. Spherical Steering (direct comparison using their released code)\n- GTS-full vs. FASB (direct comparison using their released code, github.com/gjw185/FASB)\n- GTS-full + COAST refinement (combining selective gating with constrained optimization)\n\n**Novelty acknowledgment:** If Mahalanobis does not significantly outperform Euclidean in ablations, the primary novelty contribution rests on pre-emptive sentence-level gating + per-layer controller as the mechanism enabling within-sequence selectivity without backtracking—which remains differentiated from all baselines including FASB.\n\nImplementation uses nnsight 0.6 on Qwen3-8B and Llama-3.1-8B-Instruct. Evaluation on TruthfulQA, HaluEval, FaithBench, FActScore, SimpleQA, LongFact, MT-Bench (7 primary benchmarks), plus ECE/Brier calibration metrics. Spherical Steering (released code) and FASB (released code) serve as primary baselines.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~180h H100 80GB",
      "gpu_utilization": "Low (~15-20%). GPU idles during code/debug/analysis cycles.",
      "timeline": "3-4 months",
      "team": "1-2 researchers with mechanistic interpretability + geometric ML experience",
      "estimated_gpu_cost": "$540-600 (H100 at ~$3/hr spot)",
      "factScore_api_cost": "$150-300 (GPT-4 entailment checks: ~150 checks/biography × 2 models × ~6 conditions × 150 examples)"
    },
    "human_in_loop": {
      "gpu_hours": "~195h H100 80GB",
      "gpu_utilization": "Moderate (45-55%). Agent queues batches but blocks on geometric design decisions and timing validation analysis.",
      "timeline": "3-4 weeks",
      "team": "1 researcher, ~30min/day reviewing agent proposals",
      "claude_api_cost": "$200-350",
      "estimated_gpu_cost": "$585-650",
      "factScore_api_cost": "$150-300",
      "risk_note": "Timing hypothesis validation and precision-recall threshold calibration benefit from human intuition. If timing hypothesis fails (ρ < 0.3), implementing look-ahead fallback adds ~1 week."
    },
    "auto_research": {
      "gpu_hours": "~195-200h H100 80GB",
      "gpu_utilization": "High (~85-90%). Well-defined pipeline with clear ablation structure.",
      "timeline": "10-12 days with 2-4 H100 GPUs running in parallel",
      "team": "0 (initial setup: provision GPUs, configure nnsight, define eval harness, clone Spherical Steering + FASB repos)",
      "claude_api_cost": "$350-500 (est. 4500-6000 turns)",
      "estimated_gpu_cost": "$585-600",
      "factScore_api_cost": "$200-350 (higher due to more ablation conditions)",
      "speed_bottleneck": "GPU count for parallel ablation sweeps. Secondary: FActScore GPT-4 API calls.",
      "resource_optimization": "Budget achieved via: (1) full 7-benchmark evaluation only on GTS-full, Spherical Steering, FASB, and GTS+COAST (4 conditions); (2) 4-benchmark core set (TruthfulQA, FActScore, SimpleQA, MT-Bench) for ablation variants (4 conditions); (3) Mahalanobis-vs-Euclidean and scalar-vs-MLP ablations combined into a 2×2 grid rather than separate sweeps; (4) single model (Llama-3.1-8B) for ablations, both models for final results only.",
      "risk_note": "Primary risk: timing hypothesis may fail for multi-sentence generation (Attractor Geometry validated only on factoid completion). Mitigation: look-ahead variant (~10h additional if needed). Secondary risk: Mahalanobis may not beat Euclidean—novelty then rests on pre-emptive sentence-level gating + per-layer controller. Tertiary risk: FASB's simpler probe mechanism may achieve comparable selective-steering quality on short-form QA benchmarks—GTS's advantage is expected to be strongest on long-form generation (FActScore, LongFact) where multiple claims coexist."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026)"
  ],
  "level": "top-tier",
  "key_references": [
    "Steering When Necessary: Flexible Steering Large Language Models with Backtracking (FASB, arXiv 2508.17621, NeurIPS 2025)",
    "Spherical Steering: Geometry-Aware Activation Rotation for Language Models (arXiv 2602.08169, ICML 2026)",
    "Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination (arXiv 2605.05686, May 2026)",
    "Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations (arXiv 2604.04743, April 2026)",
    "Steering Vector Fields for Context-Aware Inference-Time Control in Large Language Models (SVF, arXiv 2602.01654, Feb 2026)",
    "Curveball Steering: The Right Direction To Steer Isn't Always Linear (arXiv 2603.09313, March 2026)",
    "Minimizing Collateral Damage in Activation Steering (COAST, arXiv 2605.01167, May 2026)",
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
    "Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models (ICLR 2026)"
  ],
  "description": "We propose Geometry-Triggered Steering (GTS), a method that introduces pre-emptive sentence-level selective gating to geometry-aware activation steering for factual hallucination suppression. The key insight is that the 'when to steer' decision should be pre-emptive (decided before generating), atomic at claim granularity (sentences), and geometrically principled (measuring knowledge absence).\n\nBuilding on the finding that geometric margin separates correct recall from hallucination (AUROC 0.858 on TruthfulQA; Liang et al., May 2026), GTS monitors PCA-regularized Mahalanobis distance from residual stream activations to factual cluster centroids at sentence boundaries during generation. When geometric margin indicates basin absence—suggesting the model lacks a memorized attractor for the upcoming content—GTS computes an input-specific steering vector directed toward the factual centroid and applies it with per-layer weights predicted by a lightweight MLP controller. Sentences where the model is within a factual basin are left entirely untouched.\n\nGTS addresses limitations in the most direct prior work on selective steering: (1) vs. FASB (NeurIPS 2025), which achieves MC1 48.71% on TruthfulQA via token-level probe monitoring + 10-token backtracking, GTS is pre-emptive rather than corrective—it gates before generating rather than detecting deviation and rolling back. This eliminates wasted compute from backtracking (which scales with intervention frequency) and preserves claim coherence (no mid-sentence rollbacks). GTS's Mahalanobis trigger measures geometric knowledge absence from attractor basins, while FASB's linear probe measures learned directional alignment on attention heads—a surface feature that requires deviation to have already begun. (2) vs. Spherical Steering (ICML 2026, +15% TruthfulQA MC1), which applies per-token rotation with continuous vMF-gated intensity, GTS makes binary claim-level steer/skip decisions—enabling complete preservation of correct sub-claims. The trigger signals differ: vMF gate measures alignment to a fixed truthfulness axis; Mahalanobis measures distance from factual attractor basins. (3) vs. Steering Vector Fields (Feb 2026), which learns context-dependent steering directions refreshed every K steps but always steers, GTS decides whether to steer at all—complementary approaches that could be combined. (4) vs. Hallucination Basins (April 2026), which uses per-sequence Euclidean distance with a logistic-regression scalar map on 1B–8B models, GTS introduces within-sequence selectivity, covariance-aware distance, and per-layer control. (5) vs. COAST (May 2026), which optimizes the steering vector, GTS optimizes when to apply it—the combination (sentence-gated COAST) is included as an experiment.\n\nWe explicitly validate the timing hypothesis (margin at boundary N predicts factuality of sentence N+1) with a correlation study and provide a look-ahead fallback if it fails. Ablations isolate each design choice including a direct comparison with FASB's probe-based trigger mechanism (using their released code) to quantify the value of geometric vs. directional triggers. We hypothesize GTS's advantage over FASB will be strongest on long-form generation benchmarks (FActScore, LongFact) where multiple claims coexist and backtracking overhead compounds.\n\nImplementation uses nnsight 0.6 on Qwen3-8B and Llama-3.1-8B-Instruct. Resource-optimized evaluation: full 7-benchmark suite (TruthfulQA, HaluEval, FaithBench, FActScore, SimpleQA, LongFact, MT-Bench) on GTS-full and primary baselines; 4-benchmark core set for ablation variants. Total budget: ≤200 H100-hours.",
  "project_name": "geometry_triggered_steering",
  "source": "web_research"
}

## Reviewer feedback (round 5)
Issues: ["INSUFFICIENT PCNet DIFFERENTIATION: PCNet (arXiv 2605.05953, May 2026) is conceptually very close to GTS—both detect geometric anomaly from factual manifold and selectively intervene only at deviant positions during decoding. PCNet uses NLL via probabilistic circuits as gate + contrastive decoding; GTS uses Mahalanobis as gate + activation addition. The proposal mentions PCNet in one sentence ('detects hallucinations as geometric anomalies and applies contrastive decoding at token level') but does NOT provide explicit differentiation paragraphs like it does for FASB and Spherical Steering. Since PCNet is a May 2026 concurrent work with the same 'selective geometric gating' paradigm, it needs head-to-head comparison or at minimum a clear argument for why sentence-level activation addition is preferable to token-level contrastive decoding.", "FOUNDATIONAL AUROC USES EUCLIDEAN, NOT MAHALANOBIS: The 0.858 AUROC on TruthfulQA that motivates GTS's trigger comes from the Attractor Geometry paper, which explicitly uses Euclidean distance: δ(x) = min_i ||h(x) − m_i||₂. The proposal builds on this result to argue for a Mahalanobis trigger—but this is an unvalidated modification, not a validated foundation. The framing 'Building on the finding that geometric margin separates correct recall from hallucination (AUROC 0.858)' + then proposing Mahalanobis distance could mislead reviewers into thinking Mahalanobis achieves 0.858. The proposal should clarify: 'The Attractor Geometry paper demonstrates Euclidean geometric margin achieves AUROC 0.858; we hypothesize that Mahalanobis distance (covariance-aware) can improve this by accounting for directional anisotropy in representation space, and ablate this choice.'", "TIMELINE HAS NO BUFFER: Auto estimate is 10-12 days for an 11-day budget (May 14→May 25). With 2 days already elapsed (today is May 16), only 9 days remain. The proposal should define a 'minimum viable paper' scope that fits in 8 days (leaving 1 day for writing/formatting), e.g., dropping the COAST combination experiment and reducing ablation conditions to a 2×2 grid (Euclidean vs. Mahalanobis × sentence vs. token) + FASB baseline + Spherical Steering baseline.", "TIMING HYPOTHESIS VALIDATION LACKING SUPPORTING EVIDENCE: The Attractor Geometry paper explicitly states all experiments measure signals 'at the first-digit position, before autoregressive dynamics compound' and 'transfer to open-domain settings requires further study.' The proposal's hypothesis that margin at sentence boundary N predicts factuality of sentence N+1 during multi-sentence open-ended generation is a substantial extrapolation. While the fallback (look-ahead variant) is specified, the proposal should note that the Attractor Geometry paper's disclaimer makes this extrapolation less certain than the 0.858 AUROC suggests."]
Feedback: The proposal has matured substantially over 5 rounds and the competitive landscape is now comprehensive. Three targeted changes would strengthen it for the next round:

1. **Add explicit PCNet differentiation paragraph**: 'PCNet (2605.05953) detects hallucination via NLL anomaly from a probabilistic circuit and applies contrastive decoding selectively at token level—the same paradigm as GTS (detect geometric anomaly → selectively intervene). GTS differs in: (a) granularity: sentence-level binary decisions preserve entire correct claims and avoid token-level overhead (PCNet evaluates NLL at every token position); (b) intervention mechanism: activation steering preserves the model's own generation distribution shifted toward factual attractors, while contrastive decoding requires maintaining two forward passes (original + modified logits); (c) trigger interpretability: Mahalanobis distance has a clear geometric interpretation (distance from factual cluster in PCA subspace) while NLL from a trained probabilistic circuit is less transparent. We include PCNet as an ablation baseline if their code is available.'

2. **Clarify the Euclidean→Mahalanobis extrapolation**: Add a sentence: 'Note: the 0.858 AUROC was achieved with Euclidean distance; our use of Mahalanobis distance is a hypothesized improvement motivated by OOD detection literature (Lee et al., NeurIPS 2018), which we validate via ablation. If Mahalanobis does not significantly outperform Euclidean, the primary novelty rests on pre-emptive sentence-level gating.'

3. **Define minimum viable scope for 9 remaining days**: Propose a reduced-scope plan: (a) Core experiments on Llama-3.1-8B only (Qwen3-8B as secondary if time permits); (b) 4-benchmark core evaluation (TruthfulQA, FActScore, SimpleQA, MT-Bench) for all conditions; (c) Full 7-benchmark suite only on GTS-full vs. Spherical Steering vs. FASB; (d) Timing hypothesis validation as first milestone (day 1-2)—if it fails immediately, pivot to look-ahead variant rather than spending time on other experiments first.

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

## 停滞提醒
这个 idea 已经经过 5 轮修订，近 3 轮的平均分从 3.2 到 3.5，没有明显改善。

请认真思考：
- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？
- 如果你认为问题出在 approach 而非 framing，可以做 major revision。
- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。
- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。

最终由你判断——做你认为最能提升 idea 质量的选择。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "6c31b04f-5b26-44ca-b486-31fab11de0b0",
  "type": "user",
  "uuid": "9a9f52bc-30e3-4c9d-8751-97dc78621c20",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T09:07:23.607Z_

```json
{
  "parentUuid": "9a9f52bc-30e3-4c9d-8751-97dc78621c20",
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
  "uuid": "58956f5d-1edd-4b72-b179-f3725b2e6d79",
  "timestamp": "2026-05-16T09:07:23.607Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T09:07:23.607Z_

```json
{
  "parentUuid": "58956f5d-1edd-4b72-b179-f3725b2e6d79",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "89344571-28ce-47c9-bab3-3db9628d13b5",
  "timestamp": "2026-05-16T09:07:23.607Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
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
  "leafUuid": "89344571-28ce-47c9-bab3-3db9628d13b5",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise GTS with PCNet differentiation and realistic timeline",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c"
}
```

---

### Assistant

_source line 8 · 2026-05-16T09:07:40.334Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the reviewer feedback and the current state of this research idea before deciding on the best course of action.

The idea has been through 5 rounds with scores hovering around 3.2-3.5 without clear improvement. Let me think about whether the fundamental approach is sound or if we need a more significant change.

**Key issues from this round:**

1. **PCNet differentiation** - PCNet is a concurrent work doing the same "detect geometric anomaly → selectively intervene" paradigm. This is a significant novelty threat.


2. **Euclidean vs Mahalanobis foundation** - The motivating AUROC (0.858) was achieved with Euclidean, not Mahalanobis. This undermines the framing.
3. **Timeline crisis** - Only 9 days remain for the ARR deadline. The proposal is overscoped.
4. **Timing hypothesis weakness** - The foundational paper explicitly disclaims transfer to open-domain settings.

The core idea of GTS is "pre-emptive sentence-level gating for activation steering," but the fundamental problem is that PCNet already covers selective geometric gating, which removes the novelty claim.

I'm realizing the sentence-level granularity is genuinely differentiated from existing work—no one else operates at the claim or sentence boundary level. Rather than abandon the project, I should do a major revision: ground the approach in the Euclidean results that actually work, add a direct comparison to PCNet to clarify what's different, and be upfront about the Mahalanobis extrapolation being speculative. The timeline is brutal, but the core insight is salvageable if I tighten the scope and focus on what's actually novel.

I need to dig into PCNet's specifics to understand exactly where the methods diverge.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89344571-28ce-47c9-bab3-3db9628d13b5",
  "isSidechain": false,
  "requestId": "req_011Cb5yzqnWa7wRpzfvWCBUD",
  "type": "assistant",
  "uuid": "efb4603f-5c5e-492b-80e7-82ba66522065",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RciAqUinvLuWRS2mYRQk6L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14584,
      "cache_read_input_tokens": 11841,
      "output_tokens": 663,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14584,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 663,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14584
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

_source line 9 · 2026-05-16T09:07:40.549Z_

I'll start by researching the specific issues raised by reviewers, particularly PCNet's methodology and any recent concurrent work that could affect differentiation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efb4603f-5c5e-492b-80e7-82ba66522065",
  "isSidechain": false,
  "requestId": "req_011Cb5yzqnWa7wRpzfvWCBUD",
  "type": "assistant",
  "uuid": "f59969ea-504c-4919-8601-3ea16f0f8b50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RciAqUinvLuWRS2mYRQk6L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14584,
      "cache_read_input_tokens": 11841,
      "output_tokens": 663,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14584,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 663,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14584
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

_source line 10 · 2026-05-16T09:07:40.657Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014fgM2iMj9avosNmNRwWu6L`</summary>

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
  "parentUuid": "f59969ea-504c-4919-8601-3ea16f0f8b50",
  "isSidechain": false,
  "requestId": "req_011Cb5yzqnWa7wRpzfvWCBUD",
  "type": "assistant",
  "uuid": "3d26ca39-dbe8-46c6-84f2-96e2fda7dd97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RciAqUinvLuWRS2mYRQk6L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14584,
      "cache_read_input_tokens": 11841,
      "output_tokens": 663,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14584,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 663,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14584
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

_source line 11 · 2026-05-16T09:07:40.664Z_

<details><summary>↩ Tool result · `toolu_014fgM2iMj9avosNmNRwWu6L`</summary>

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
  "parentUuid": "3d26ca39-dbe8-46c6-84f2-96e2fda7dd97",
  "isSidechain": false,
  "promptId": "6c31b04f-5b26-44ca-b486-31fab11de0b0",
  "type": "user",
  "uuid": "a5b0fd38-c832-4ee3-95b0-2de7c86dc8f6",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "3d26ca39-dbe8-46c6-84f2-96e2fda7dd97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-16T09:07:43.810Z_

Let me research the key issues raised by reviewers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5b0fd38-c832-4ee3-95b0-2de7c86dc8f6",
  "isSidechain": false,
  "requestId": "req_011Cb5z25Pqt75gGzfeDK7qE",
  "type": "assistant",
  "uuid": "588c5e0a-22d8-488f-bbd0-1b2a73369103",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLsT24L6q5aBAMUUDnifZR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1683,
      "cache_read_input_tokens": 26425,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1683,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 93,
          "cache_read_input_tokens": 26425,
          "cache_creation_input_tokens": 1683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1683
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

_source line 13 · 2026-05-16T09:07:44.336Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FAPp4FBuAC79fNEduHaGEX`</summary>

```json
{
  "query": "PCNet hallucination anomaly probabilistic circuits contrastive decoding arXiv 2605.05953 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "588c5e0a-22d8-488f-bbd0-1b2a73369103",
  "isSidechain": false,
  "requestId": "req_011Cb5z25Pqt75gGzfeDK7qE",
  "type": "assistant",
  "uuid": "b7d3d7de-4ee5-427a-816b-8593c530c2ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLsT24L6q5aBAMUUDnifZR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1683,
      "cache_read_input_tokens": 26425,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1683,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 93,
          "cache_read_input_tokens": 26425,
          "cache_creation_input_tokens": 1683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1683
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

_source line 14 · 2026-05-16T09:07:50.364Z_

<details><summary>↩ Tool result · `toolu_01FAPp4FBuAC79fNEduHaGEX`</summary>

```text
Web search results for query: "PCNet hallucination anomaly probabilistic circuits contrastive decoding arXiv 2605.05953 2026"

Links: [{"title":"[2605.05953] Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/abs/2605.05953"},{"title":"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/html/2605.05953"},{"title":"Computer Science Apr 2025","url":"https://www.arxiv.org/list/cs/2025-04?skip=5650&show=25"},{"title":"Efficient Contrastive Decoding with Probabilistic Hallucination Detection - Mitigating Hallucinations in Large Vision Language Models -","url":"https://arxiv.org/html/2504.12137v1"},{"title":"[2504.12137] Efficient Contrastive Decoding with Probabilistic Hallucination Detection - Mitigating Hallucinations in Large Vision Language Models -","url":"https://arxiv.org/abs/2504.12137"},{"title":"Computer Science Apr 2025","url":"https://arxiv.org/list/cs/2025-04?skip=5650&show=2000"},{"title":"Do We Really Need External Tools to Mitigate Hallucinations? Sira: Shared-Prefix Internal Reconstruction of Attribution","url":"https://arxiv.org/html/2605.14621"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=18875&show=25"},{"title":"Decoupling Contrastive Decoding: Robust Hallucination Mitigation in Multimodal Large Language Models","url":"https://arxiv.org/html/2504.08809v2"},{"title":"Artificial Intelligence Apr 2025","url":"https://arxiv.org/list/cs.AI/2025-04?skip=1850&show=50"}]

I found the paper you're looking for! Here are the key details about arXiv paper 2605.05953:

**Title:** Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits

**Main Contribution:** The paper proposes PCNET, a Probabilistic Circuit trained as a tractable density estimator over the LLM residual stream.

**Approach:** The method detects hallucinations as geometric anomalies on the factual manifold, which is done via exact Negative Log-Likelihood computation, hence without the need for sampling, external verifiers, or weight modifications, as in existing techniques.

**Key Innovation:** PC-LDCD (Probabilistic Circuit Latent Density Contrastive Decoding), only when the latent geometry deviates from factual regions, while leaving correct generations untouched. This addresses a key limitation in existing approaches: they apply corrections indiscriminately to every token, corrupting also the originally correct generations.

The paper was posted about one week ago on arXiv and combines probabilistic circuits with contrastive decoding to selectively intervene only when hallucinations are detected, rather than applying blanket corrections to all tokens.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7d3d7de-4ee5-427a-816b-8593c530c2ed",
  "isSidechain": false,
  "promptId": "6c31b04f-5b26-44ca-b486-31fab11de0b0",
  "type": "user",
  "uuid": "3a9396e7-28c4-4b75-b016-ca68c8096bc5",
  "toolUseResult": {
    "query": "PCNet hallucination anomaly probabilistic circuits contrastive decoding arXiv 2605.05953 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Q6cxGh8eqLPRu4wWLXzK6h",
        "content": [
          {
            "title": "[2605.05953] Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits",
            "url": "https://arxiv.org/abs/2605.05953"
          },
          {
            "title": "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits",
            "url": "https://arxiv.org/html/2605.05953"
          },
          {
            "title": "Computer Science Apr 2025",
            "url": "https://www.arxiv.org/list/cs/2025-04?skip=5650&show=25"
          },
          {
            "title": "Efficient Contrastive Decoding with Probabilistic Hallucination Detection - Mitigating Hallucinations in Large Vision Language Models -",
            "url": "https://arxiv.org/html/2504.12137v1"
          },
          {
            "title": "[2504.12137] Efficient Contrastive Decoding with Probabilistic Hallucination Detection - Mitigating Hallucinations in Large Vision Language Models -",
            "url": "https://arxiv.org/abs/2504.12137"
          },
          {
            "title": "Computer Science Apr 2025",
            "url": "https://arxiv.org/list/cs/2025-04?skip=5650&show=2000"
          },
          {
            "title": "Do We Really Need External Tools to Mitigate Hallucinations? Sira: Shared-Prefix Internal Reconstruction of Attribution",
            "url": "https://arxiv.org/html/2605.14621"
          },
          {
            "title": "Computation and Language 2025",
            "url": "https://arxiv.org/list/cs.CL/2025?skip=18875&show=25"
          },
          {
            "title": "Decoupling Contrastive Decoding: Robust Hallucination Mitigation in Multimodal Large Language Models",
            "url": "https://arxiv.org/html/2504.08809v2"
          },
          {
            "title": "Artificial Intelligence Apr 2025",
            "url": "https://arxiv.org/list/cs.AI/2025-04?skip=1850&show=50"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details about arXiv paper 2605.05953:\n\n**Title:** Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits\n\n**Main Contribution:** The paper proposes PCNET, a Probabilistic Circuit trained as a tractable density estimator over the LLM residual stream.\n\n**Approach:** The method detects hallucinations as geometric anomalies on the factual manifold, which is done via exact Negative Log-Likelihood computation, hence without the need for sampling, external verifiers, or weight modifications, as in existing techniques.\n\n**Key Innovation:** PC-LDCD (Probabilistic Circuit Latent Density Contrastive Decoding), only when the latent geometry deviates from factual regions, while leaving correct generations untouched. This addresses a key limitation in existing approaches: they apply corrections indiscriminately to every token, corrupting also the originally correct generations.\n\nThe paper was posted about one week ago on arXiv and combines probabilistic circuits with contrastive decoding to selectively intervene only when hallucinations are detected, rather than applying blanket corrections to all tokens."
    ],
    "durationSeconds": 6.02338263
  },
  "sourceToolAssistantUUID": "b7d3d7de-4ee5-427a-816b-8593c530c2ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T09:07:54.861Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019eynTqjAqrF7WLggVRmbkm`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.05953",
  "prompt": "Extract the full abstract and key details: 1) What is the exact detection mechanism (how does the probabilistic circuit detect anomalies)? 2) At what granularity does it intervene (token-level, sentence-level)? 3) What is the intervention mechanism (contrastive decoding details)? 4) What benchmarks and results are reported? 5) What models are tested? 6) How does it compare to activation steering methods? 7) What are the claimed limitations?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a9396e7-28c4-4b75-b016-ca68c8096bc5",
  "isSidechain": false,
  "requestId": "req_011Cb5z2ncZgiTnexCL6PkUn",
  "type": "assistant",
  "uuid": "eb84a9b2-30b1-4b1e-bf34-c0c80189e6fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012NBsZfM162w8P5V9tBh4wf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 898,
      "cache_read_input_tokens": 28108,
      "output_tokens": 191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 898,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 191,
          "cache_read_input_tokens": 28108,
          "cache_creation_input_tokens": 898,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 898
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

_source line 16 · 2026-05-16T09:08:02.125Z_

<details><summary>↩ Tool result · `toolu_019eynTqjAqrF7WLggVRmbkm`</summary>

```text
# PCNET: Hallucination Detection via Probabilistic Circuits

## Full Abstract
"One of the most critical challenges in Large Language Models is their tendency to hallucinate, i.e., produce factually incorrect responses. Existing approaches show promising results in terms of hallucination correction, but still suffer from a main limitation: they apply corrections indiscriminately to every token, corrupting also the originally correct generations. To overcome this drawback, we propose PCNET, a Probabilistic Circuit trained as a tractable density estimator over the LLM residual stream. The method detects hallucinations as geometric anomalies on the factual manifold, which is done via exact Negative Log-Likelihood computation, hence without the need for sampling, external verifiers, or weight modifications, as in existing techniques. To demonstrate its effectiveness, we exploit PCNET as a dynamic gate that distinguishes hallucinated from factual hidden states at each decoding step. This triggers our second main contribution, PC-LDCD (Probabilistic Circuit Latent Density Contrastive Decoding), only when the latent geometry deviates from factual regions, while leaving correct generations untouched."

## Key Details

**1) Detection Mechanism:** The system identifies hallucinations through "exact Negative Log-Likelihood computation" on the LLM's residual stream, treating hallucinations as "geometric anomalies on the factual manifold."

**2) Intervention Granularity:** Token-level—the method operates "at each decoding step," making decisions per-token.

**3) Intervention Mechanism:** PC-LDCD (Probabilistic Circuit Latent Density Contrastive Decoding) activates "only when the latent geometry deviates from factual regions, while leaving correct generations untouched."

**4) Benchmarks & Results:**
- CoQA, SQuAD v2.0, TriviaQA (near-perfect detection, AUROC up to 99%)
- TruthfulQA (highest True+Info, MC2, MC3 scores in 3/4 models)
- Corruption rate: 53.7%, preservation rate: 79.3%

**5) Models Tested:** 1B to 8B parameter models

**6) Comparison to Activation Steering:** Not addressed in the abstract

**7) Limitations:** Not explicitly stated in the abstract provided
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb84a9b2-30b1-4b1e-bf34-c0c80189e6fa",
  "isSidechain": false,
  "promptId": "6c31b04f-5b26-44ca-b486-31fab11de0b0",
  "type": "user",
  "uuid": "e85df4a7-c565-40cf-bd1b-9f5c7ea7704a",
  "toolUseResult": {
    "bytes": 47725,
    "code": 200,
    "codeText": "OK",
    "result": "# PCNET: Hallucination Detection via Probabilistic Circuits\n\n## Full Abstract\n\"One of the most critical challenges in Large Language Models is their tendency to hallucinate, i.e., produce factually incorrect responses. Existing approaches show promising results in terms of hallucination correction, but still suffer from a main limitation: they apply corrections indiscriminately to every token, corrupting also the originally correct generations. To overcome this drawback, we propose PCNET, a Probabilistic Circuit trained as a tractable density estimator over the LLM residual stream. The method detects hallucinations as geometric anomalies on the factual manifold, which is done via exact Negative Log-Likelihood computation, hence without the need for sampling, external verifiers, or weight modifications, as in existing techniques. To demonstrate its effectiveness, we exploit PCNET as a dynamic gate that distinguishes hallucinated from factual hidden states at each decoding step. This triggers our second main contribution, PC-LDCD (Probabilistic Circuit Latent Density Contrastive Decoding), only when the latent geometry deviates from factual regions, while leaving correct generations untouched.\"\n\n## Key Details\n\n**1) Detection Mechanism:** The system identifies hallucinations through \"exact Negative Log-Likelihood computation\" on the LLM's residual stream, treating hallucinations as \"geometric anomalies on the factual manifold.\"\n\n**2) Intervention Granularity:** Token-level—the method operates \"at each decoding step,\" making decisions per-token.\n\n**3) Intervention Mechanism:** PC-LDCD (Probabilistic Circuit Latent Density Contrastive Decoding) activates \"only when the latent geometry deviates from factual regions, while leaving correct generations untouched.\"\n\n**4) Benchmarks & Results:**\n- CoQA, SQuAD v2.0, TriviaQA (near-perfect detection, AUROC up to 99%)\n- TruthfulQA (highest True+Info, MC2, MC3 scores in 3/4 models)\n- Corruption rate: 53.7%, preservation rate: 79.3%\n\n**5) Models Tested:** 1B to 8B parameter models\n\n**6) Comparison to Activation Steering:** Not addressed in the abstract\n\n**7) Limitations:** Not explicitly stated in the abstract provided",
    "durationMs": 7258,
    "url": "https://arxiv.org/abs/2605.05953"
  },
  "sourceToolAssistantUUID": "eb84a9b2-30b1-4b1e-bf34-c0c80189e6fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T09:08:05.264Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T8cP5dc5t1PwwtFVtXsqd9`</summary>

```json
{
  "query": "PCNet probabilistic circuit hallucination detection selective intervention token-level vs sentence-level comparison 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e85df4a7-c565-40cf-bd1b-9f5c7ea7704a",
  "isSidechain": false,
  "requestId": "req_011Cb5z3etztsNDJE9m32SwA",
  "type": "assistant",
  "uuid": "5316c25d-0f8a-4a48-bcfc-7d007d05729b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Sh9bokFuidcva14rD4HFY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 29006,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 29006,
          "cache_creation_input_tokens": 746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 746
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

_source line 18 · 2026-05-16T09:08:13.883Z_

<details><summary>↩ Tool result · `toolu_01T8cP5dc5t1PwwtFVtXsqd9`</summary>

```text
Web search results for query: "PCNet probabilistic circuit hallucination detection selective intervention token-level vs sentence-level comparison 2026"

Links: [{"title":"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/html/2605.05953"},{"title":"[2605.05953] Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/abs/2605.05953"},{"title":"Token-Level Self-Consistency for Hallucination Detection","url":"https://aclanthology.org/2025.semeval-1.38.pdf"},{"title":"Mitigating Hallucination via Evaluating the Factuality of ...","url":"https://aclanthology.org/2025.findings-acl.752.pdf"},{"title":"A Probabilistic Framework for LLM Hallucination Detection ...","url":"https://aclanthology.org/2025.naacl-long.158.pdf"},{"title":"[2503.03106] Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation","url":"https://arxiv.org/abs/2503.03106"},{"title":"Hallucination Detection and Mitigation in Large Language ...","url":"https://arxiv.org/pdf/2601.09929"},{"title":"Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection | OpenReview","url":"https://openreview.net/forum?id=yzWGQNTbHQ"},{"title":"GPTZero uncovers 50+ Hallucinations in ICLR 2026","url":"https://gptzero.me/news/iclr-2026/"},{"title":"A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202510.0540/v1"}]

Based on the web search results, I found relevant research on PCNet (Probabilistic Circuit hallucination detection). Here are the key findings:

## PCNet Overview

PCNet is a Probabilistic Circuit trained as a tractable density estimator over the LLM residual stream. The method detects hallucinations as geometric anomalies on the factual manifold, which is done via exact Negative Log-Likelihood computation, hence without the need for sampling, external verifiers, or weight modifications, as in existing techniques.

## Selective Intervention Mechanism

PCNet is used as a dynamic gate that distinguishes hallucinated from factual hidden states at each decoding step. PC-LDCD (Probabilistic Circuit Latent Density Contrastive Decoding) triggers only when the latent geometry deviates from factual regions, while leaving correct generations untouched.

## Token-Level Intervention

The approach operates at the token level during generation. PCNet triggers an intervention at a fraction of decoding steps, measured by the Instance Gating Rate (IGR), alongside metrics assessing the Corruption rate (fraction of originally correct generations degraded by intervention) and the Preservation rate (fraction of correct generations successfully protected by gating).

## Performance Results

Across four LLMs (1B to 8B models) and four benchmarks, PCNet achieves near-perfect hallucination detection across CoQA, SQuAD v2.0, and TriviaQA, with AUROC reaching up to 99%. Moreover, PC-LDCD obtains the highest True+Info, MC2, and MC3 scores on TruthfulQA in three out of four models, while reducing the mean corruption rate to 53.7% and achieving a preservation rate of 79.3%.

This research was published in May 2026 on arXiv and represents a significant advancement in selective, intervention-based hallucination mitigation during language model generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5316c25d-0f8a-4a48-bcfc-7d007d05729b",
  "isSidechain": false,
  "promptId": "6c31b04f-5b26-44ca-b486-31fab11de0b0",
  "type": "user",
  "uuid": "c9a6160d-dff9-451e-b869-f628abbcccf8",
  "toolUseResult": {
    "query": "PCNet probabilistic circuit hallucination detection selective intervention token-level vs sentence-level comparison 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ud8Yc8sJafQSo9A5LVp1JU",
        "content": [
          {
            "title": "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits",
            "url": "https://arxiv.org/html/2605.05953"
          },
          {
            "title": "[2605.05953] Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits",
            "url": "https://arxiv.org/abs/2605.05953"
          },
          {
            "title": "Token-Level Self-Consistency for Hallucination Detection",
            "url": "https://aclanthology.org/2025.semeval-1.38.pdf"
          },
          {
            "title": "Mitigating Hallucination via Evaluating the Factuality of ...",
            "url": "https://aclanthology.org/2025.findings-acl.752.pdf"
          },
          {
            "title": "A Probabilistic Framework for LLM Hallucination Detection ...",
            "url": "https://aclanthology.org/2025.naacl-long.158.pdf"
          },
          {
            "title": "[2503.03106] Monitoring Decoding: Mitigating Hallucination via Evaluating the Factuality of Partial Response during Generation",
            "url": "https://arxiv.org/abs/2503.03106"
          },
          {
            "title": "Hallucination Detection and Mitigation in Large Language ...",
            "url": "https://arxiv.org/pdf/2601.09929"
          },
          {
            "title": "Next-Token Gradient Sensitivity Probing for LLM Hallucination Detection | OpenReview",
            "url": "https://openreview.net/forum?id=yzWGQNTbHQ"
          },
          {
            "title": "GPTZero uncovers 50+ Hallucinations in ICLR 2026",
            "url": "https://gptzero.me/news/iclr-2026/"
          },
          {
            "title": "A Survey on Hallucination in Large Language Models: Definitions, Detection, and Mitigation[v1] | Preprints.org",
            "url": "https://www.preprints.org/manuscript/202510.0540/v1"
          }
        ]
      },
      "Based on the web search results, I found relevant research on PCNet (Probabilistic Circuit hallucination detection). Here are the key findings:\n\n## PCNet Overview\n\nPCNet is a Probabilistic Circuit trained as a tractable density estimator over the LLM residual stream. The method detects hallucinations as geometric anomalies on the factual manifold, which is done via exact Negative Log-Likelihood computation, hence without the need for sampling, external verifiers, or weight modifications, as in existing techniques.\n\n## Selective Intervention Mechanism\n\nPCNet is used as a dynamic gate that distinguishes hallucinated from factual hidden states at each decoding step. PC-LDCD (Probabilistic Circuit Latent Density Contrastive Decoding) triggers only when the latent geometry deviates from factual regions, while leaving correct generations untouched.\n\n## Token-Level Intervention\n\nThe approach operates at the token level during generation. PCNet triggers an intervention at a fraction of decoding steps, measured by the Instance Gating Rate (IGR), alongside metrics assessing the Corruption rate (fraction of originally correct generations degraded by intervention) and the Preservation rate (fraction of correct generations successfully protected by gating).\n\n## Performance Results\n\nAcross four LLMs (1B to 8B models) and four benchmarks, PCNet achieves near-perfect hallucination detection across CoQA, SQuAD v2.0, and TriviaQA, with AUROC reaching up to 99%. Moreover, PC-LDCD obtains the highest True+Info, MC2, and MC3 scores on TruthfulQA in three out of four models, while reducing the mean corruption rate to 53.7% and achieving a preservation rate of 79.3%.\n\nThis research was published in May 2026 on arXiv and represents a significant advancement in selective, intervention-based hallucination mitigation during language model generation."
    ],
    "durationSeconds": 8.614343145000007
  },
  "sourceToolAssistantUUID": "5316c25d-0f8a-4a48-bcfc-7d007d05729b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-16 (UTC).**  ## Original idea {   \"title\": \"Geometry-Triggered Sentence-Level Activation Steering for Factual Hall…",
  "leafUuid": "c9a6160d-dff9-451e-b869-f628abbcccf8",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise GTS with PCNet differentiation and realistic timeline",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c"
}
```

---

### Tool call

_source line 21 · 2026-05-16T09:08:20.172Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012yc25SRkXdUq7SttPb2hgo`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.05953",
  "prompt": "Extract the detailed methodology: 1) How exactly is the Probabilistic Circuit (PC) trained? What is the input representation? 2) How is NLL computed and what threshold is used for gating? 3) How does PC-LDCD contrastive decoding work mechanically—what are the two distributions being contrasted? 4) What is the corruption rate and preservation rate in detail? 5) What are the TruthfulQA MC1/MC2 results for each model? 6) What are the specific limitations the authors acknowledge? 7) Does the paper compare against activation steering methods like ITI, Spherical Steering, or FASB? 8) What is the computational overhead of running the PC at every token?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9a6160d-dff9-451e-b869-f628abbcccf8",
  "isSidechain": false,
  "requestId": "req_011Cb5z4XBgFBdE3FPWzo2eb",
  "type": "assistant",
  "uuid": "8ced33b1-e7cc-4990-b91e-89924d964249",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CmDnmX4mdvfL2R4FNzL8RE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1038,
      "cache_read_input_tokens": 29752,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1038,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 245,
          "cache_read_input_tokens": 29752,
          "cache_creation_input_tokens": 1038,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1038
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

_source line 22 · 2026-05-16T09:08:36.024Z_

<details><summary>↩ Tool result · `toolu_012yc25SRkXdUq7SttPb2hgo`</summary>

```text
# Detailed Methodology Analysis

## 1) Probabilistic Circuit Training

**Input Representation:**
The PC operates on compressed latent states: raw hidden states (D_LLM=4096) are projected through a 2-layer MLP bottleneck into z ∈ ℝ^128. This projection "filters out syntactic artifacts while preserving the core semantic and factual geometries."

**Training Process:**
PCNet uses a contrastive objective combining generative and discriminative losses:
- **Generative term**: minimizes negative log-likelihood on factual states
- **Contrastive term**: enforces margin γ=5.0 between factual and hallucinated projections

The architecture consists of heterogeneous leaf nodes (mixture of Gaussian, Laplace, Student-T distributions), product nodes (context-specific independence), and sum nodes (modeling latent sub-populations). Training uses 500 paired samples (250 factual/250 hallucinated) across 50 epochs with Adam optimizer (lr=10^-3).

## 2) NLL Computation & Gating Threshold

**NLL Calculation:**
Exact Negative Log-Likelihood is computed in a single forward pass: S_NLL(z) = -log C_root(z), where C_root is the circuit's root node. This guarantees "exact and efficient marginal and conditional inference."

**Threshold Selection:**
The anomaly threshold τ is calibrated per model using "the precision-recall curve against ground truth labels," selecting the value maximizing F1 score on validation data. The gating strength β_t uses sigmoid scaling: β_t = σ(S_NLL(z_t) - τ).

## 3) PC-LDCD Contrastive Decoding Mechanics

**The Two Distributions:**
PC-LDCD contrasts:
1. **LM log-probability**: log P_LM(c_i | x_<t)
2. **Manifold density penalty**: β_t · S_NLL(f_φ(h_t+1^(c_i)))

**Scoring Formula:**
Score_LDCD(c_i) = log P_LM(c_i | x_<t) - β_t · S_NLL(...), applied to top-k candidates from raw logits. Unlike prior "contrastive methods" using amateur proxy models, this uses "exact log-density score under the learned manifold model."

## 4) Corruption & Preservation Rates

**Definitions:**
- **Corruption rate**: fraction of originally correct generations degraded by un-gated intervention (56.5% average across methods)
- **Preservation rate**: percentage of correct generations protected by PCNet gating (78.0% average)

**Key Finding:**
Un-gated methods (applying corrections at every token) corrupt 26-90% of factual text depending on model. PC-LDCD achieves the lowest corruption (53.7%) and highest preservation (79.3%).

## 5) TruthfulQA MC Results by Model

| Model | T+I | MC1 | MC2 | MC3 |
|-------|-----|-----|-----|-----|
| Llama-3.2-1B | 0.50 | 0.36 | 0.51 | 0.14 |
| Qwen3-4B | 0.78 | 0.51 | 0.68 | 0.23 |
| Mistral-7B | 0.72 | 0.54 | 0.72 | 0.29 |
| Llama-3.1-8B | 0.69 | 0.51 | 0.65 | 0.25 |

PC-LDCD leads on MC2/MC3 but underperforms on MC1 because "MC1 rewards aggressive logit re-ranking toward a single correct answer."

## 6) Acknowledged Limitations

The authors explicitly state:
- "PCNet requires a small calibration set of labeled factual and hallucinated hidden states, which may be costly in new domains"
- Evaluation "limited to models up to 8B parameters, leaving open whether geometric separation holds in larger models"
- "PC-LDCD gains are stronger on generative benchmarks than on exact-match tasks"

## 7) Comparison Against Activation Steering

**Methods Compared:**
- ITI (inference-time intervention with linear probes)
- AdaSteer (adaptive context-conditioned intervention)
- SADI (semantics-adaptive activation intervention)

All three are evaluated. ITI frequently fails (e.g., SQuAD EM 0.50±0.01), while adaptive methods (AdaSteer/SADI) match baselines but still suffer from "un-gated correction" degrading factual text.

## 8) Computational Overhead

Per-token cost breakdown:
- MLP encoder: O(D_LLM · D_PC) = O(4096 · 128)
- PC forward pass: O(|N|) where |N| ≈ 10^3 nodes
- Lookahead (anomalies only): IGR · k · d_block

**Total:** PC scoring overhead is "below 2% of one full transformer-layer forward pass." Lookahead dominates, scaling with Intervention Gating Rate (IGR ∈ [0.41, 0.78]) × k=8 candidates. This means 3.3-6.2 additional block evaluations per generated token when anomalies are detected.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ced33b1-e7cc-4990-b91e-89924d964249",
  "isSidechain": false,
  "promptId": "6c31b04f-5b26-44ca-b486-31fab11de0b0",
  "type": "user",
  "uuid": "774acfef-789c-4447-860b-ecb725fe80e8",
  "toolUseResult": {
    "bytes": 667871,
    "code": 200,
    "codeText": "OK",
    "result": "# Detailed Methodology Analysis\n\n## 1) Probabilistic Circuit Training\n\n**Input Representation:**\nThe PC operates on compressed latent states: raw hidden states (D_LLM=4096) are projected through a 2-layer MLP bottleneck into z ∈ ℝ^128. This projection \"filters out syntactic artifacts while preserving the core semantic and factual geometries.\"\n\n**Training Process:**\nPCNet uses a contrastive objective combining generative and discriminative losses:\n- **Generative term**: minimizes negative log-likelihood on factual states\n- **Contrastive term**: enforces margin γ=5.0 between factual and hallucinated projections\n\nThe architecture consists of heterogeneous leaf nodes (mixture of Gaussian, Laplace, Student-T distributions), product nodes (context-specific independence), and sum nodes (modeling latent sub-populations). Training uses 500 paired samples (250 factual/250 hallucinated) across 50 epochs with Adam optimizer (lr=10^-3).\n\n## 2) NLL Computation & Gating Threshold\n\n**NLL Calculation:**\nExact Negative Log-Likelihood is computed in a single forward pass: S_NLL(z) = -log C_root(z), where C_root is the circuit's root node. This guarantees \"exact and efficient marginal and conditional inference.\"\n\n**Threshold Selection:**\nThe anomaly threshold τ is calibrated per model using \"the precision-recall curve against ground truth labels,\" selecting the value maximizing F1 score on validation data. The gating strength β_t uses sigmoid scaling: β_t = σ(S_NLL(z_t) - τ).\n\n## 3) PC-LDCD Contrastive Decoding Mechanics\n\n**The Two Distributions:**\nPC-LDCD contrasts:\n1. **LM log-probability**: log P_LM(c_i | x_<t)\n2. **Manifold density penalty**: β_t · S_NLL(f_φ(h_t+1^(c_i)))\n\n**Scoring Formula:**\nScore_LDCD(c_i) = log P_LM(c_i | x_<t) - β_t · S_NLL(...), applied to top-k candidates from raw logits. Unlike prior \"contrastive methods\" using amateur proxy models, this uses \"exact log-density score under the learned manifold model.\"\n\n## 4) Corruption & Preservation Rates\n\n**Definitions:**\n- **Corruption rate**: fraction of originally correct generations degraded by un-gated intervention (56.5% average across methods)\n- **Preservation rate**: percentage of correct generations protected by PCNet gating (78.0% average)\n\n**Key Finding:**\nUn-gated methods (applying corrections at every token) corrupt 26-90% of factual text depending on model. PC-LDCD achieves the lowest corruption (53.7%) and highest preservation (79.3%).\n\n## 5) TruthfulQA MC Results by Model\n\n| Model | T+I | MC1 | MC2 | MC3 |\n|-------|-----|-----|-----|-----|\n| Llama-3.2-1B | 0.50 | 0.36 | 0.51 | 0.14 |\n| Qwen3-4B | 0.78 | 0.51 | 0.68 | 0.23 |\n| Mistral-7B | 0.72 | 0.54 | 0.72 | 0.29 |\n| Llama-3.1-8B | 0.69 | 0.51 | 0.65 | 0.25 |\n\nPC-LDCD leads on MC2/MC3 but underperforms on MC1 because \"MC1 rewards aggressive logit re-ranking toward a single correct answer.\"\n\n## 6) Acknowledged Limitations\n\nThe authors explicitly state:\n- \"PCNet requires a small calibration set of labeled factual and hallucinated hidden states, which may be costly in new domains\"\n- Evaluation \"limited to models up to 8B parameters, leaving open whether geometric separation holds in larger models\"\n- \"PC-LDCD gains are stronger on generative benchmarks than on exact-match tasks\"\n\n## 7) Comparison Against Activation Steering\n\n**Methods Compared:**\n- ITI (inference-time intervention with linear probes)\n- AdaSteer (adaptive context-conditioned intervention)\n- SADI (semantics-adaptive activation intervention)\n\nAll three are evaluated. ITI frequently fails (e.g., SQuAD EM 0.50±0.01), while adaptive methods (AdaSteer/SADI) match baselines but still suffer from \"un-gated correction\" degrading factual text.\n\n## 8) Computational Overhead\n\nPer-token cost breakdown:\n- MLP encoder: O(D_LLM · D_PC) = O(4096 · 128)\n- PC forward pass: O(|N|) where |N| ≈ 10^3 nodes\n- Lookahead (anomalies only): IGR · k · d_block\n\n**Total:** PC scoring overhead is \"below 2% of one full transformer-layer forward pass.\" Lookahead dominates, scaling with Intervention Gating Rate (IGR ∈ [0.41, 0.78]) × k=8 candidates. This means 3.3-6.2 additional block evaluations per generated token when anomalies are detected.",
    "durationMs": 15845,
    "url": "https://arxiv.org/html/2605.05953"
  },
  "sourceToolAssistantUUID": "8ced33b1-e7cc-4990-b91e-89924d964249",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-16T09:08:39.228Z_

Now let me search for the Attractor Geometry paper to confirm the Euclidean vs Mahalanobis issue, and also search for any very recent work on sentence-level hallucination intervention.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "774acfef-789c-4447-860b-ecb725fe80e8",
  "isSidechain": false,
  "requestId": "req_011Cb5z69o7pbVcN2CbpKrPy",
  "type": "assistant",
  "uuid": "9f8ddec0-5f5d-40fb-94ff-500b33ac9a9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVDY9KJf2YyVRHHhwz3RJS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1568,
      "cache_read_input_tokens": 30790,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1568,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 232,
          "cache_read_input_tokens": 30790,
          "cache_creation_input_tokens": 1568,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1568
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

_source line 24 · 2026-05-16T09:08:42.104Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013ev6QEdJdsqTNYkDqK34kq`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.05686",
  "prompt": "Extract: 1) The exact distance metric used for geometric margin (Euclidean or Mahalanobis or both?). 2) The exact AUROC numbers and what benchmarks they were measured on. 3) Any disclaimers about generalization to open-domain or multi-sentence generation. 4) Whether the paper proposes any intervention mechanism or is detection-only. 5) The exact experimental setup—what models, what tasks, what positions are measurements taken at."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f8ddec0-5f5d-40fb-94ff-500b33ac9a9b",
  "isSidechain": false,
  "requestId": "req_011Cb5z69o7pbVcN2CbpKrPy",
  "type": "assistant",
  "uuid": "bede162a-5f6d-45a9-8b0d-7f8a5aad696e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVDY9KJf2YyVRHHhwz3RJS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1568,
      "cache_read_input_tokens": 30790,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1568,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 232,
          "cache_read_input_tokens": 30790,
          "cache_creation_input_tokens": 1568,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1568
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

_source line 25 · 2026-05-16T09:08:46.536Z_

<details><summary>↩ Tool result · `toolu_013ev6QEdJdsqTNYkDqK34kq`</summary>

```text
# Response Based on Available Content

I cannot provide complete answers to all five questions based on the webpage content provided, as it contains only the abstract and metadata from an arXiv paper, not the full paper itself.

## What I can extract:

**1) Distance metric:** Not specified in the abstract.

**2) AUROC numbers:** Not provided in available content.

**3) Generalization disclaimers:** The abstract mentions "natural-language factual queries from the pretrained model" but does not discuss limitations regarding open-domain or multi-sentence generation.

**4) Intervention mechanism:** The work appears to be "detection-only." The abstract states that "geometric margin...separates correct recall from hallucination" but proposes no corrective intervention.

**5) Experimental setup:** Partially described—the abstract mentions: "controlled synthetic task-entity identifiers mapped to unique codes with PM installed via LoRA adapters" and verification "on natural-language factual queries from the pretrained model with no adaptation." However, specific model names, task details, and measurement positions are not detailed in this excerpt.

## Limitation

To answer questions 1-2 comprehensively, you would need to access the full PDF or HTML version of the paper using the links provided on the arXiv page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bede162a-5f6d-45a9-8b0d-7f8a5aad696e",
  "isSidechain": false,
  "promptId": "6c31b04f-5b26-44ca-b486-31fab11de0b0",
  "type": "user",
  "uuid": "f7cf4760-954c-4755-8514-76790fbb7c75",
  "toolUseResult": {
    "bytes": 48434,
    "code": 200,
    "codeText": "OK",
    "result": "# Response Based on Available Content\n\nI cannot provide complete answers to all five questions based on the webpage content provided, as it contains only the abstract and metadata from an arXiv paper, not the full paper itself.\n\n## What I can extract:\n\n**1) Distance metric:** Not specified in the abstract.\n\n**2) AUROC numbers:** Not provided in available content.\n\n**3) Generalization disclaimers:** The abstract mentions \"natural-language factual queries from the pretrained model\" but does not discuss limitations regarding open-domain or multi-sentence generation.\n\n**4) Intervention mechanism:** The work appears to be \"detection-only.\" The abstract states that \"geometric margin...separates correct recall from hallucination\" but proposes no corrective intervention.\n\n**5) Experimental setup:** Partially described—the abstract mentions: \"controlled synthetic task-entity identifiers mapped to unique codes with PM installed via LoRA adapters\" and verification \"on natural-language factual queries from the pretrained model with no adaptation.\" However, specific model names, task details, and measurement positions are not detailed in this excerpt.\n\n## Limitation\n\nTo answer questions 1-2 comprehensively, you would need to access the full PDF or HTML version of the paper using the links provided on the arXiv page.",
    "durationMs": 4428,
    "url": "https://arxiv.org/abs/2605.05686"
  },
  "sourceToolAssistantUUID": "bede162a-5f6d-45a9-8b0d-7f8a5aad696e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-16T09:08:51.914Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012g9xuPxvJJepbXT6Jekmya`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.05686",
  "prompt": "Extract the following specific details: 1) What exact distance metric is used for geometric margin—Euclidean distance, Mahalanobis distance, or something else? Quote the formula if possible. 2) The exact AUROC numbers (0.858 on TruthfulQA, 0.993 on controlled tasks, etc.) and what distance metric produced them. 3) Any disclaimers about transfer to open-domain settings or multi-sentence generation. 4) At what token position are measurements taken (first digit, last token, sentence boundary)? 5) Is the paper detection-only or does it propose intervention?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7cf4760-954c-4755-8514-76790fbb7c75",
  "isSidechain": false,
  "requestId": "req_011Cb5z6vhbYK61dub98MTDx",
  "type": "assistant",
  "uuid": "79bb289b-75c1-4446-b25a-73ad1d3b9521",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TQoyotk2vqLBx7MLEefyHX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 524,
      "cache_read_input_tokens": 32358,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 524,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 221,
          "cache_read_input_tokens": 32358,
          "cache_creation_input_tokens": 524,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 524
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

_source line 27 · 2026-05-16T09:08:58.192Z_

<details><summary>↩ Tool result · `toolu_012g9xuPxvJJepbXT6Jekmya`</summary>

```text
# Analysis of Geometric Margin Methodology

## 1) Distance Metric

The paper uses **Euclidean distance** (L2 norm). The formula is explicitly stated:

> "δ(x)=min_i ‖h(x)−m_i‖₂"

This measures the distance from the hidden state to the nearest basin center.

## 2) AUROC Numbers and Metrics

- **Controlled synthetic task**: AUROC = 0.993 for margin vs. 0.968 for entropy
- **Pretrained knowledge (196 factual queries, no adapter)**: AUROC = 1.000 for margin vs. 0.622 for entropy
- **TruthfulQA**: AUROC = 0.858 for margin vs. 0.656 for entropy

All use the same L2-distance margin metric described above.

## 3) Transfer Limitations

The authors acknowledge significant constraints:

> "Margin reaches TruthfulQA AUROC=0.858...but degrades on adversarial reasoning probes where no memorized basin exists"

They note that "transfer to open-domain settings requires further study" and the approach is primarily validated on controlled entity-mapping and factual-recall tasks.

## 4) Token Position

Measurements are taken at **the first-digit position** before autoregressive generation compounds:

> "All signals are computed at the first-digit position, before autoregressive dynamics compound."

## 5) Detection vs. Intervention

The paper is **detection-only**. It proposes no interventions to modify model behavior, only methods to identify failures. The authors suggest future work on retraining the output head or creating auxiliary epistemic readout mechanisms, but do not implement these.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79bb289b-75c1-4446-b25a-73ad1d3b9521",
  "isSidechain": false,
  "promptId": "6c31b04f-5b26-44ca-b486-31fab11de0b0",
  "type": "user",
  "uuid": "8b9f8759-30d6-4479-9c36-4b129a022039",
  "toolUseResult": {
    "bytes": 632050,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of Geometric Margin Methodology\n\n## 1) Distance Metric\n\nThe paper uses **Euclidean distance** (L2 norm). The formula is explicitly stated:\n\n> \"δ(x)=min_i ‖h(x)−m_i‖₂\"\n\nThis measures the distance from the hidden state to the nearest basin center.\n\n## 2) AUROC Numbers and Metrics\n\n- **Controlled synthetic task**: AUROC = 0.993 for margin vs. 0.968 for entropy\n- **Pretrained knowledge (196 factual queries, no adapter)**: AUROC = 1.000 for margin vs. 0.622 for entropy\n- **TruthfulQA**: AUROC = 0.858 for margin vs. 0.656 for entropy\n\nAll use the same L2-distance margin metric described above.\n\n## 3) Transfer Limitations\n\nThe authors acknowledge significant constraints:\n\n> \"Margin reaches TruthfulQA AUROC=0.858...but degrades on adversarial reasoning probes where no memorized basin exists\"\n\nThey note that \"transfer to open-domain settings requires further study\" and the approach is primarily validated on controlled entity-mapping and factual-recall tasks.\n\n## 4) Token Position\n\nMeasurements are taken at **the first-digit position** before autoregressive generation compounds:\n\n> \"All signals are computed at the first-digit position, before autoregressive dynamics compound.\"\n\n## 5) Detection vs. Intervention\n\nThe paper is **detection-only**. It proposes no interventions to modify model behavior, only methods to identify failures. The authors suggest future work on retraining the output head or creating auxiliary epistemic readout mechanisms, but do not implement these.",
    "durationMs": 6275,
    "url": "https://arxiv.org/html/2605.05686"
  },
  "sourceToolAssistantUUID": "79bb289b-75c1-4446-b25a-73ad1d3b9521",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28 · 2026-05-16T09:08:58.199Z_

```json
{
  "parentUuid": "8b9f8759-30d6-4479-9c36-4b129a022039",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "cce8bb1a-0857-4d88-8112-d5be652a523d",
  "timestamp": "2026-05-16T09:08:58.199Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 29 · 2026-05-16T09:09:00.924Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J9r7kJtCCqcizf1TxKMCZs`</summary>

```json
{
  "query": "sentence-level hallucination detection intervention activation steering claim-level granularity 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cce8bb1a-0857-4d88-8112-d5be652a523d",
  "isSidechain": false,
  "requestId": "req_011Cb5z7nbxpgUUc6bnbu7wi",
  "type": "assistant",
  "uuid": "76bd327d-20a1-4ce5-8537-5cdaf03f386d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8GFfaWPXJSAgGKRMwhoAP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 32882,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 737,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 32882,
          "cache_creation_input_tokens": 737,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 737
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

_source line 30 · 2026-05-16T09:09:08.852Z_

<details><summary>↩ Tool result · `toolu_01J9r7kJtCCqcizf1TxKMCZs`</summary>

```text
Web search results for query: "sentence-level hallucination detection intervention activation steering claim-level granularity 2026"

Links: [{"title":"Reducing hallucinations of large language models via hierarchical semantic piece | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-01833-9"},{"title":"A Survey of Multimodal Hallucination Evaluation and Detection","url":"https://arxiv.org/html/2507.19024v2"},{"title":"Dynamic Multimodal Activation Steering for Hallucination ...","url":"https://arxiv.org/pdf/2602.21704"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/html/2509.03531v1"},{"title":"Constructing Benchmarks and Interventions for Combating Hallucinations in LLMs","url":"https://arxiv.org/pdf/2404.09971"},{"title":"Activation Steering Decoding: Mitigating Hallucination in ...","url":"https://aclanthology.org/2025.acl-long.634.pdf"},{"title":"Activation Steering Decoding: Mitigating Hallucination in Large Vision-Language Models through Bidirectional Hidden State Intervention - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.634/"},{"title":"From Illusion to Insight: A Taxonomic Survey of Hallucination Mitigation Techniques in LLMs","url":"https://www.mdpi.com/2673-2688/6/10/260"},{"title":"Mitigating Object Hallucinations via Sentence-Level Early Intervention","url":"https://arxiv.org/pdf/2507.12455"},{"title":"A Comprehensive Survey of Hallucination in Large Language Models: Causes, Detection, and Mitigation","url":"https://arxiv.org/html/2510.06265v1"}]

I found several relevant research papers and studies related to your search query. Here are the key findings:

## Hallucination Detection with Multi-Level Granularity

A hierarchical semantic piece (HSP) method extracts multi-granularity semantic pieces from reference and generated text, with sentence-level semantic pieces encapsulating global semantic information and entity-level semantic pieces handling local semantic information. This approach verifies consistency between generated and reference text at corresponding granularities to enhance hallucination detection and mitigation.

## Activation Steering for Hallucination Mitigation

Dynamic multimodal activation steering (DMAS) is a method that extracts truthfulness steering vectors by contrasting attention activations between factual and hallucination-prone samples, stores these vectors with cluster embeddings in a database, calculates perception steering vectors from activation differences, and during inference dynamically retrieves the most semantically relevant steering vector to apply to attention heads with the largest activation differences.

## Entity-Level vs. Claim-Level Granularity

Recent work targets entity-level hallucinations—such as fabricated names, dates, and citations—rather than claim-level hallucinations. For more granular analysis, FAVA was proposed as a retrieval-augmented model trained on synthetic data to detect hallucination using span-level identification, outperforming baseline models including GPT-4 in both span-level and binary hallucination detection tasks.

## Intervention Approaches

Steering vectors can be used to mitigate hallucinations by adding a vector to a hidden state to steer away from hallucinations, with detection targeting before hallucination onset to steer generation away from hallucination before it materializes in surface tokens.

These papers represent the latest research in 2025-2026 on combining sentence-level granularity with activation steering and intervention techniques for hallucination detection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76bd327d-20a1-4ce5-8537-5cdaf03f386d",
  "isSidechain": false,
  "promptId": "6c31b04f-5b26-44ca-b486-31fab11de0b0",
  "type": "user",
  "uuid": "2e937d10-22b1-4118-8ca6-22eefee9e07c",
  "toolUseResult": {
    "query": "sentence-level hallucination detection intervention activation steering claim-level granularity 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WiawG7VzC7Ei2sQCApRjvo",
        "content": [
          {
            "title": "Reducing hallucinations of large language models via hierarchical semantic piece | Complex & Intelligent Systems | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s40747-025-01833-9"
          },
          {
            "title": "A Survey of Multimodal Hallucination Evaluation and Detection",
            "url": "https://arxiv.org/html/2507.19024v2"
          },
          {
            "title": "Dynamic Multimodal Activation Steering for Hallucination ...",
            "url": "https://arxiv.org/pdf/2602.21704"
          },
          {
            "title": "Real-Time Detection of Hallucinated Entities in Long-Form Generation",
            "url": "https://arxiv.org/html/2509.03531v1"
          },
          {
            "title": "Constructing Benchmarks and Interventions for Combating Hallucinations in LLMs",
            "url": "https://arxiv.org/pdf/2404.09971"
          },
          {
            "title": "Activation Steering Decoding: Mitigating Hallucination in ...",
            "url": "https://aclanthology.org/2025.acl-long.634.pdf"
          },
          {
            "title": "Activation Steering Decoding: Mitigating Hallucination in Large Vision-Language Models through Bidirectional Hidden State Intervention - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.634/"
          },
          {
            "title": "From Illusion to Insight: A Taxonomic Survey of Hallucination Mitigation Techniques in LLMs",
            "url": "https://www.mdpi.com/2673-2688/6/10/260"
          },
          {
            "title": "Mitigating Object Hallucinations via Sentence-Level Early Intervention",
            "url": "https://arxiv.org/pdf/2507.12455"
          },
          {
            "title": "A Comprehensive Survey of Hallucination in Large Language Models: Causes, Detection, and Mitigation",
            "url": "https://arxiv.org/html/2510.06265v1"
          }
        ]
      },
      "I found several relevant research papers and studies related to your search query. Here are the key findings:\n\n## Hallucination Detection with Multi-Level Granularity\n\nA hierarchical semantic piece (HSP) method extracts multi-granularity semantic pieces from reference and generated text, with sentence-level semantic pieces encapsulating global semantic information and entity-level semantic pieces handling local semantic information. This approach verifies consistency between generated and reference text at corresponding granularities to enhance hallucination detection and mitigation.\n\n## Activation Steering for Hallucination Mitigation\n\nDynamic multimodal activation steering (DMAS) is a method that extracts truthfulness steering vectors by contrasting attention activations between factual and hallucination-prone samples, stores these vectors with cluster embeddings in a database, calculates perception steering vectors from activation differences, and during inference dynamically retrieves the most semantically relevant steering vector to apply to attention heads with the largest activation differences.\n\n## Entity-Level vs. Claim-Level Granularity\n\nRecent work targets entity-level hallucinations—such as fabricated names, dates, and citations—rather than claim-level hallucinations. For more granular analysis, FAVA was proposed as a retrieval-augmented model trained on synthetic data to detect hallucination using span-level identification, outperforming baseline models including GPT-4 in both span-level and binary hallucination detection tasks.\n\n## Intervention Approaches\n\nSteering vectors can be used to mitigate hallucinations by adding a vector to a hidden state to steer away from hallucinations, with detection targeting before hallucination onset to steer generation away from hallucination before it materializes in surface tokens.\n\nThese papers represent the latest research in 2025-2026 on combining sentence-level granularity with activation steering and intervention techniques for hallucination detection."
    ],
    "durationSeconds": 7.923285769000009
  },
  "sourceToolAssistantUUID": "76bd327d-20a1-4ce5-8537-5cdaf03f386d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-16 (UTC).**  ## Original idea {   \"title\": \"Geometry-Triggered Sentence-Level Activation Steering for Factual Hall…",
  "leafUuid": "2e937d10-22b1-4118-8ca6-22eefee9e07c",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise GTS with PCNet differentiation and realistic timeline",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c"
}
```

---

### Tool call

_source line 33 · 2026-05-16T09:09:11.749Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015WZ5GuZ9pnA37PHbRArau3`</summary>

```json
{
  "query": "\"sentence-level\" OR \"claim-level\" hallucination intervention steering preemptive gating arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e937d10-22b1-4118-8ca6-22eefee9e07c",
  "isSidechain": false,
  "requestId": "req_011Cb5z8aB8EigCsh9sxcZ4x",
  "type": "assistant",
  "uuid": "e53d5cb7-0bf7-4cb2-934e-3e644fd5f339",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBaVy8qt5dnEYUhXgLC3cF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1003,
      "cache_read_input_tokens": 33619,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1003,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 33619,
          "cache_creation_input_tokens": 1003,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1003
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

_source line 34 · 2026-05-16T09:09:21.219Z_

<details><summary>↩ Tool result · `toolu_015WZ5GuZ9pnA37PHbRArau3`</summary>

```text
Web search results for query: ""sentence-level" OR "claim-level" hallucination intervention steering preemptive gating arXiv 2026"

Links: [{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/html/2509.03531v1"},{"title":"[2507.12455] Mitigating Object Hallucinations via Sentence-Level Early Intervention","url":"https://arxiv.org/abs/2507.12455"},{"title":"(PDF) Mitigating Object Hallucinations via Sentence-Level Early Intervention","url":"https://www.researchgate.net/publication/393771584_Mitigating_Object_Hallucinations_via_Sentence-Level_Early_Intervention"},{"title":"[2404.14233] Detecting and Mitigating Hallucination in Large Vision Language Models via Fine-Grained AI Feedback","url":"https://arxiv.org/abs/2404.14233"}]

I found several relevant papers on hallucination mitigation in language models. Here are the key results:

1. **SENTINEL** - A framework called SENTINEL (Sentence-level Early iNtervention Through IN-domain prEference Learning) that eliminates dependency on human annotations. The key insight is that hallucinations predominantly emerge at the early stages of text generation and propagate through subsequent outputs.

2. **Sentence-level detection approach** - One approach generates a sentence-level hallucination annotation dataset, training a hallucination detection model to perform sentence-level detection, covering primary hallucination types (object, attribute, and relationship).

3. **Entity-level focus** - Some work targets entity-level hallucinations (fabricated names, dates, citations) rather than claim-level, naturally mapping to token-level labels and enabling streaming detection.

The search results show active research on early intervention strategies and sentence-level approaches to detecting and mitigating hallucinations in both multimodal and text-based language models, with papers from mid-2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e53d5cb7-0bf7-4cb2-934e-3e644fd5f339",
  "isSidechain": false,
  "promptId": "6c31b04f-5b26-44ca-b486-31fab11de0b0",
  "type": "user",
  "uuid": "8621c34e-2ab7-47d5-ab66-2e93a476cf6d",
  "toolUseResult": {
    "query": "\"sentence-level\" OR \"claim-level\" hallucination intervention steering preemptive gating arXiv 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Uo7FNznJfkWMyuWHGyBAMp",
        "content": [
          {
            "title": "Real-Time Detection of Hallucinated Entities in Long-Form Generation",
            "url": "https://arxiv.org/html/2509.03531v1"
          },
          {
            "title": "[2507.12455] Mitigating Object Hallucinations via Sentence-Level Early Intervention",
            "url": "https://arxiv.org/abs/2507.12455"
          },
          {
            "title": "(PDF) Mitigating Object Hallucinations via Sentence-Level Early Intervention",
            "url": "https://www.researchgate.net/publication/393771584_Mitigating_Object_Hallucinations_via_Sentence-Level_Early_Intervention"
          },
          {
            "title": "[2404.14233] Detecting and Mitigating Hallucination in Large Vision Language Models via Fine-Grained AI Feedback",
            "url": "https://arxiv.org/abs/2404.14233"
          }
        ]
      },
      "I found several relevant papers on hallucination mitigation in language models. Here are the key results:\n\n1. **SENTINEL** - A framework called SENTINEL (Sentence-level Early iNtervention Through IN-domain prEference Learning) that eliminates dependency on human annotations. The key insight is that hallucinations predominantly emerge at the early stages of text generation and propagate through subsequent outputs.\n\n2. **Sentence-level detection approach** - One approach generates a sentence-level hallucination annotation dataset, training a hallucination detection model to perform sentence-level detection, covering primary hallucination types (object, attribute, and relationship).\n\n3. **Entity-level focus** - Some work targets entity-level hallucinations (fabricated names, dates, citations) rather than claim-level, naturally mapping to token-level labels and enabling streaming detection.\n\nThe search results show active research on early intervention strategies and sentence-level approaches to detecting and mitigating hallucinations in both multimodal and text-based language models, with papers from mid-2025."
    ],
    "durationSeconds": 9.465830180000005
  },
  "sourceToolAssistantUUID": "e53d5cb7-0bf7-4cb2-934e-3e644fd5f339",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T09:09:25.665Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0187Sjxf94A1Exg5f9Zysqxp`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.12455",
  "prompt": "Extract: 1) What is SENTINEL's exact approach—how does sentence-level early intervention work? 2) Does it use activation steering or some other intervention? 3) What is the detection mechanism? 4) What benchmarks and results? 5) Is this about LLMs or vision-language models? 6) How does it differ from token-level approaches?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8621c34e-2ab7-47d5-ab66-2e93a476cf6d",
  "isSidechain": false,
  "requestId": "req_011Cb5z9V3apu1buJ7Gtihs8",
  "type": "assistant",
  "uuid": "df180dbf-be41-4b3c-8254-40cdfbb0daca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EzzGvPNScBtFM8RanuBduJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 34622,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 586,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 163,
          "cache_read_input_tokens": 34622,
          "cache_creation_input_tokens": 586,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 586
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

_source line 36 · 2026-05-16T09:09:30.011Z_

<details><summary>↩ Tool result · `toolu_0187Sjxf94A1Exg5f9Zysqxp`</summary>

```text
# SENTINEL: Object Hallucination Mitigation Analysis

**1) Sentence-Level Early Intervention Approach:**
The method operates at sentence granularity rather than token-level. It works by identifying that "hallucinations predominantly emerge at the early stages of text generation" and constructs context-aware preference learning to address this.

**2) Intervention Mechanism:**
This isn't activation steering. Instead, SENTINEL uses preference learning through a "context-aware preference loss (C-DPO)" that emphasizes "discriminative learning at the sentence level where hallucinations initially manifest."

**3) Detection Mechanism:**
The framework employs "cross-checking with two open-vocabulary detectors" to validate whether mentioned objects actually appear in images. This automated validation bootstraps training data without human annotation.

**4) Benchmarks & Results:**
SENTINEL achieves a "90% reduction in hallucinations compared to the original model" and "outperforms the previous state-of-the-art method on both hallucination benchmarks and general capabilities benchmarks."

**5) Model Type:**
This addresses Multimodal Large Language Models (MLLMs), specifically vision-language systems that process both images and text.

**6) Differentiation from Token-Level Approaches:**
Unlike token-level methods, SENTINEL operates at the sentence boundary, building "context-coherent positive samples and hallucinated negative samples" to create sentence-level preference pairs for more targeted intervention.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df180dbf-be41-4b3c-8254-40cdfbb0daca",
  "isSidechain": false,
  "promptId": "6c31b04f-5b26-44ca-b486-31fab11de0b0",
  "type": "user",
  "uuid": "943c5438-24c5-457f-9962-d96b630a442b",
  "toolUseResult": {
    "bytes": 47598,
    "code": 200,
    "codeText": "OK",
    "result": "# SENTINEL: Object Hallucination Mitigation Analysis\n\n**1) Sentence-Level Early Intervention Approach:**\nThe method operates at sentence granularity rather than token-level. It works by identifying that \"hallucinations predominantly emerge at the early stages of text generation\" and constructs context-aware preference learning to address this.\n\n**2) Intervention Mechanism:**\nThis isn't activation steering. Instead, SENTINEL uses preference learning through a \"context-aware preference loss (C-DPO)\" that emphasizes \"discriminative learning at the sentence level where hallucinations initially manifest.\"\n\n**3) Detection Mechanism:**\nThe framework employs \"cross-checking with two open-vocabulary detectors\" to validate whether mentioned objects actually appear in images. This automated validation bootstraps training data without human annotation.\n\n**4) Benchmarks & Results:**\nSENTINEL achieves a \"90% reduction in hallucinations compared to the original model\" and \"outperforms the previous state-of-the-art method on both hallucination benchmarks and general capabilities benchmarks.\"\n\n**5) Model Type:**\nThis addresses Multimodal Large Language Models (MLLMs), specifically vision-language systems that process both images and text.\n\n**6) Differentiation from Token-Level Approaches:**\nUnlike token-level methods, SENTINEL operates at the sentence boundary, building \"context-coherent positive samples and hallucinated negative samples\" to create sentence-level preference pairs for more targeted intervention.",
    "durationMs": 4342,
    "url": "https://arxiv.org/abs/2507.12455"
  },
  "sourceToolAssistantUUID": "df180dbf-be41-4b3c-8254-40cdfbb0daca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T09:09:33.085Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013NGCqsyz9mByzrcqFe9UYM`</summary>

```json
{
  "query": "Mahalanobis distance out-of-distribution detection LLM hidden states hallucination 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "943c5438-24c5-457f-9962-d96b630a442b",
  "isSidechain": false,
  "requestId": "req_011Cb5zA9AH1nf36oM5bSm9w",
  "type": "assistant",
  "uuid": "f7c6a672-35bb-4ae3-b146-1d096e8cb99e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vz2m4v2zYztx7XiNiRX8rH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 496,
      "cache_read_input_tokens": 35208,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 496,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 35208,
          "cache_creation_input_tokens": 496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 496
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

_source line 38 · 2026-05-16T09:09:41.548Z_

<details><summary>↩ Tool result · `toolu_013NGCqsyz9mByzrcqFe9UYM`</summary>

```text
Web search results for query: "Mahalanobis distance out-of-distribution detection LLM hidden states hallucination 2025 2026"

Links: [{"title":"Revisiting Mahalanobis Distance for Transformer-Based Out-of-Domain Detection | Request PDF","url":"https://www.researchgate.net/publication/363393389_Revisiting_Mahalanobis_Distance_for_Transformer-Based_Out-of-Domain_Detection"},{"title":"Simple Factuality Probes Detect Hallucinations in Long- ...","url":"https://aclanthology.org/2025.findings-emnlp.880.pdf"},{"title":"Mahalanobis++: Improving OOD Detection via Feature Normalization","url":"https://arxiv.org/html/2505.18032v1"},{"title":"Detection of Hallucinations Based on the Internal States of Large Language Models | Automatic Documentation and Mathematical Linguistics | Springer Nature Link","url":"https://link.springer.com/article/10.3103/S0005105525701456"},{"title":"A Geometric Taxonomy of Hallucination in LLMs","url":"https://arxiv.org/html/2602.13224v3"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"AggTruth: Contextual Hallucination Detection using ...","url":"https://arxiv.org/pdf/2506.18628"},{"title":"HalluMatDetector: Modular LLM Hallucination Detector","url":"https://www.emergentmind.com/topics/hallumatdetector"},{"title":"arXiv:2506.09886v1 [cs.CL] 11 Jun 2025","url":"https://arxiv.org/pdf/2506.09886"},{"title":"HADEMIF: HALLUCINATION DETECTION AND MITI","url":"https://openreview.net/pdf?id=VwOYxPScxB"}]

I've performed a web search on Mahalanobis distance out-of-distribution detection in LLMs with focus on hidden states and hallucination detection from 2025-2026. Here's a summary of the key findings:

## Recent Research on OOD Detection and Hallucination in LLMs (2025-2026)

### Mahalanobis Distance Applications

Distance-based methods using Mahalanobis distance for distinguishing between in-distribution (ID) and out-of-distribution (OOD) samples have shown promising results when combined with transformers. Mahalanobis distance applied to pre-logit features is among the most effective for ImageNet-scale OOD detection, though performance varies significantly across models.

A recent advancement is Mahalanobis++, which improves OOD detection by projecting features onto the unit sphere before estimating the Mahalanobis distance, significantly reducing class-dependent feature variability.

### Hidden States for Hallucination Detection

Several 2025-2026 papers focus on using LLM hidden states to detect hallucinations:

- Factuality probes obtain hidden states for each claim and apply lightweight probes on hidden states to estimate claim-level factuality, providing fine-grained confidence reporting in long-form generations.

- Research using the Flan-T5 model analyzes differences in the model's internal states when generating hallucinations versus correct responses, proposing approaches leveraging attention maps and hidden states for hallucination detection.

- A recent framework (BAFH) trains a feedforward classifier on hidden states to determine belief states and classify hallucination types, evaluated across eight LLMs including Gemma-2, Llama-3.1, and Mistral.

### OOD Detection in LLMs

The rapid proliferation of LLMs has stimulated researchers to seek effective approaches to deal with LLM hallucinations and low-quality outputs, with uncertainty quantification being a key element.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7c6a672-35bb-4ae3-b146-1d096e8cb99e",
  "isSidechain": false,
  "promptId": "6c31b04f-5b26-44ca-b486-31fab11de0b0",
  "type": "user",
  "uuid": "73b6a865-e759-43ac-b20f-078e8086020c",
  "toolUseResult": {
    "query": "Mahalanobis distance out-of-distribution detection LLM hidden states hallucination 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018g8yfiPunvRRuThgoYwRiZ",
        "content": [
          {
            "title": "Revisiting Mahalanobis Distance for Transformer-Based Out-of-Domain Detection | Request PDF",
            "url": "https://www.researchgate.net/publication/363393389_Revisiting_Mahalanobis_Distance_for_Transformer-Based_Out-of-Domain_Detection"
          },
          {
            "title": "Simple Factuality Probes Detect Hallucinations in Long- ...",
            "url": "https://aclanthology.org/2025.findings-emnlp.880.pdf"
          },
          {
            "title": "Mahalanobis++: Improving OOD Detection via Feature Normalization",
            "url": "https://arxiv.org/html/2505.18032v1"
          },
          {
            "title": "Detection of Hallucinations Based on the Internal States of Large Language Models | Automatic Documentation and Mathematical Linguistics | Springer Nature Link",
            "url": "https://link.springer.com/article/10.3103/S0005105525701456"
          },
          {
            "title": "A Geometric Taxonomy of Hallucination in LLMs",
            "url": "https://arxiv.org/html/2602.13224v3"
          },
          {
            "title": "GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub",
            "url": "https://github.com/EdinburghNLP/awesome-hallucination-detection"
          },
          {
            "title": "AggTruth: Contextual Hallucination Detection using ...",
            "url": "https://arxiv.org/pdf/2506.18628"
          },
          {
            "title": "HalluMatDetector: Modular LLM Hallucination Detector",
            "url": "https://www.emergentmind.com/topics/hallumatdetector"
          },
          {
            "title": "arXiv:2506.09886v1 [cs.CL] 11 Jun 2025",
            "url": "https://arxiv.org/pdf/2506.09886"
          },
          {
            "title": "HADEMIF: HALLUCINATION DETECTION AND MITI",
            "url": "https://openreview.net/pdf?id=VwOYxPScxB"
          }
        ]
      },
      "I've performed a web search on Mahalanobis distance out-of-distribution detection in LLMs with focus on hidden states and hallucination detection from 2025-2026. Here's a summary of the key findings:\n\n## Recent Research on OOD Detection and Hallucination in LLMs (2025-2026)\n\n### Mahalanobis Distance Applications\n\nDistance-based methods using Mahalanobis distance for distinguishing between in-distribution (ID) and out-of-distribution (OOD) samples have shown promising results when combined with transformers. Mahalanobis distance applied to pre-logit features is among the most effective for ImageNet-scale OOD detection, though performance varies significantly across models.\n\nA recent advancement is Mahalanobis++, which improves OOD detection by projecting features onto the unit sphere before estimating the Mahalanobis distance, significantly reducing class-dependent feature variability.\n\n### Hidden States for Hallucination Detection\n\nSeveral 2025-2026 papers focus on using LLM hidden states to detect hallucinations:\n\n- Factuality probes obtain hidden states for each claim and apply lightweight probes on hidden states to estimate claim-level factuality, providing fine-grained confidence reporting in long-form generations.\n\n- Research using the Flan-T5 model analyzes differences in the model's internal states when generating hallucinations versus correct responses, proposing approaches leveraging attention maps and hidden states for hallucination detection.\n\n- A recent framework (BAFH) trains a feedforward classifier on hidden states to determine belief states and classify hallucination types, evaluated across eight LLMs including Gemma-2, Llama-3.1, and Mistral.\n\n### OOD Detection in LLMs\n\nThe rapid proliferation of LLMs has stimulated researchers to seek effective approaches to deal with LLM hallucinations and low-quality outputs, with uncertainty quantification being a key element."
    ],
    "durationSeconds": 8.459667944000001
  },
  "sourceToolAssistantUUID": "f7c6a672-35bb-4ae3-b146-1d096e8cb99e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T09:09:44.228Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011YoUu7iQJ3v49avq2nn3iG`</summary>

```json
{
  "query": "contrastive decoding vs activation steering hallucination comparison advantages disadvantages 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73b6a865-e759-43ac-b20f-078e8086020c",
  "isSidechain": false,
  "requestId": "req_011Cb5zAyzu2VQwvd8EyTRrk",
  "type": "assistant",
  "uuid": "e4b5240b-c57d-4c0a-b76e-4467ccf8ebb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GDUmzQFaRsNReLYN2Ppe2F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1083,
      "cache_read_input_tokens": 35704,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1083,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 35704,
          "cache_creation_input_tokens": 1083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1083
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

_source line 40 · 2026-05-16T09:09:53.250Z_

<details><summary>↩ Tool result · `toolu_011YoUu7iQJ3v49avq2nn3iG`</summary>

```text
Web search results for query: "contrastive decoding vs activation steering hallucination comparison advantages disadvantages 2025 2026"

Links: [{"title":"Dynamic Multimodal Activation Steering for Hallucination ...","url":"https://arxiv.org/pdf/2602.21704"},{"title":"Activation Steering Decoding: Mitigating Hallucination in Large Vision-Language Models through Bidirectional Hidden State Intervention - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.634/"},{"title":"Mitigating Entangled Steering in Large Vision-Language Models for Hallucination Reduction | Request PDF","url":"https://www.researchgate.net/publication/403683244_Mitigating_Entangled_Steering_in_Large_Vision-Language_Models_for_Hallucination_Reduction"},{"title":"Activation Steering Decoding: Mitigating Hallucination in Large Vision-Language Models through Bidirectional Hidden State Intervention | Request PDF","url":"https://www.researchgate.net/publication/394298568_Activation_Steering_Decoding_Mitigating_Hallucination_in_Large_Vision-Language_Models_through_Bidirectional_Hidden_State_Intervention"},{"title":"Activation Steering Decoding: Mitigating Hallucination in Large Vision-Language Models through Bidirectional Hidden State Intervention","url":"https://chatpaper.com/paper/176030"},{"title":"Mitigating Hallucinations in Large Vision-Language Models via Dual Contrastive Decoding | Proceedings of the 7th ACM International Conference on Multimedia in Asia","url":"https://dl.acm.org/doi/10.1145/3743093.3770933"},{"title":"Activation Steering Decoding: Mitigating Hallucination in ...","url":"https://aclanthology.org/2025.acl-long.634.pdf"},{"title":"Active Layer-Contrastive Decoding Reduces Hallucination in Large","url":"https://arxiv.org/pdf/2505.23657"},{"title":"ASCD: Attention-Steerable Contrastive Decoding for Reducing Hallucination in","url":"https://ojs.aaai.org/index.php/AAAI/article/download/38000/41962"},{"title":"Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering | OpenReview","url":"https://openreview.net/forum?id=LBl7Hez0fF"}]

Based on the search results, here's a comparison of **contrastive decoding** and **activation steering** for hallucination mitigation in large vision-language models (LVLMs), with recent developments from 2025-2026:

## **Key Approaches**

### Contrastive Decoding
Contrastive decoding is a training-free method where Visual Contrastive Decoding (VCD) perturbs input images to generate a negative logit branch that is subtracted from original predictions, while other approaches employ negative prompts to steer outputs away from hallucinated content.

### Activation Steering
Activation Steering Decoding (ASD) identifies directional patterns of hallucination in the activation space using a small calibration set, then employs a contrast decoding mechanism that computes the difference between positive and negative steering predictions, effectively suppressing hallucination patterns while preserving the model's general capabilities.

More recently, methods dynamically retrieve semantically relevant truthfulness steering vectors and apply both truthfulness and visual perception vectors to top-K attention heads with the largest activation differences, with this dual intervention effectively reducing hallucinations.

## **Advantages and Disadvantages**

### Contrastive Decoding - Advantages
- Training-free means to mitigate hallucinations
- Works at the decoding level without model modifications

### Contrastive Decoding - Disadvantages
Decoding-based methods modify the decoding strategies of LVLMs, but while these methods avoid the need for training, they often compromise the quality of the generated content.

### Activation Steering - Advantages
- Requires no model re-training or architectural modifications, making it readily applicable to existing deployed models.
- Reduces latency by up to 2x compared to prior contrastive decoding methods that require multiple forward passes.
- Introduces only 10–20% additional inference latency due to parallel processing of the two steering branches, making it practical for real-world deployment.

## **Recent 2025-2026 Developments**

The field has evolved to combine both approaches: activation steering now employs contrast decoding mechanisms that compute differences between positive and negative steering predictions. This hybrid approach appears to be the emerging standard for effective hallucination mitigation while maintaining practical efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4b5240b-c57d-4c0a-b76e-4467ccf8ebb9",
  "isSidechain": false,
  "promptId": "6c31b04f-5b26-44ca-b486-31fab11de0b0",
  "type": "user",
  "uuid": "993c0239-9133-48da-9145-b8085f84171a",
  "toolUseResult": {
    "query": "contrastive decoding vs activation steering hallucination comparison advantages disadvantages 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NgNoRyaNrbzm64P5AWmtE9",
        "content": [
          {
            "title": "Dynamic Multimodal Activation Steering for Hallucination ...",
            "url": "https://arxiv.org/pdf/2602.21704"
          },
          {
            "title": "Activation Steering Decoding: Mitigating Hallucination in Large Vision-Language Models through Bidirectional Hidden State Intervention - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.634/"
          },
          {
            "title": "Mitigating Entangled Steering in Large Vision-Language Models for Hallucination Reduction | Request PDF",
            "url": "https://www.researchgate.net/publication/403683244_Mitigating_Entangled_Steering_in_Large_Vision-Language_Models_for_Hallucination_Reduction"
          },
          {
            "title": "Activation Steering Decoding: Mitigating Hallucination in Large Vision-Language Models through Bidirectional Hidden State Intervention | Request PDF",
            "url": "https://www.researchgate.net/publication/394298568_Activation_Steering_Decoding_Mitigating_Hallucination_in_Large_Vision-Language_Models_through_Bidirectional_Hidden_State_Intervention"
          },
          {
            "title": "Activation Steering Decoding: Mitigating Hallucination in Large Vision-Language Models through Bidirectional Hidden State Intervention",
            "url": "https://chatpaper.com/paper/176030"
          },
          {
            "title": "Mitigating Hallucinations in Large Vision-Language Models via Dual Contrastive Decoding | Proceedings of the 7th ACM International Conference on Multimedia in Asia",
            "url": "https://dl.acm.org/doi/10.1145/3743093.3770933"
          },
          {
            "title": "Activation Steering Decoding: Mitigating Hallucination in ...",
            "url": "https://aclanthology.org/2025.acl-long.634.pdf"
          },
          {
            "title": "Active Layer-Contrastive Decoding Reduces Hallucination in Large",
            "url": "https://arxiv.org/pdf/2505.23657"
          },
          {
            "title": "ASCD: Attention-Steerable Contrastive Decoding for Reducing Hallucination in",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/download/38000/41962"
          },
          {
            "title": "Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering | OpenReview",
            "url": "https://openreview.net/forum?id=LBl7Hez0fF"
          }
        ]
      },
      "Based on the search results, here's a comparison of **contrastive decoding** and **activation steering** for hallucination mitigation in large vision-language models (LVLMs), with recent developments from 2025-2026:\n\n## **Key Approaches**\n\n### Contrastive Decoding\nContrastive decoding is a training-free method where Visual Contrastive Decoding (VCD) perturbs input images to generate a negative logit branch that is subtracted from original predictions, while other approaches employ negative prompts to steer outputs away from hallucinated content.\n\n### Activation Steering\nActivation Steering Decoding (ASD) identifies directional patterns of hallucination in the activation space using a small calibration set, then employs a contrast decoding mechanism that computes the difference between positive and negative steering predictions, effectively suppressing hallucination patterns while preserving the model's general capabilities.\n\nMore recently, methods dynamically retrieve semantically relevant truthfulness steering vectors and apply both truthfulness and visual perception vectors to top-K attention heads with the largest activation differences, with this dual intervention effectively reducing hallucinations.\n\n## **Advantages and Disadvantages**\n\n### Contrastive Decoding - Advantages\n- Training-free means to mitigate hallucinations\n- Works at the decoding level without model modifications\n\n### Contrastive Decoding - Disadvantages\nDecoding-based methods modify the decoding strategies of LVLMs, but while these methods avoid the need for training, they often compromise the quality of the generated content.\n\n### Activation Steering - Advantages\n- Requires no model re-training or architectural modifications, making it readily applicable to existing deployed models.\n- Reduces latency by up to 2x compared to prior contrastive decoding methods that require multiple forward passes.\n- Introduces only 10–20% additional inference latency due to parallel processing of the two steering branches, making it practical for real-world deployment.\n\n## **Recent 2025-2026 Developments**\n\nThe field has evolved to combine both approaches: activation steering now employs contrast decoding mechanisms that compute differences between positive and negative steering predictions. This hybrid approach appears to be the emerging standard for effective hallucination mitigation while maintaining practical efficiency."
    ],
    "durationSeconds": 9.017694396999985
  },
  "sourceToolAssistantUUID": "e4b5240b-c57d-4c0a-b76e-4467ccf8ebb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T09:10:01.667Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XsMrenp95DBn55nW4uiHYp`</summary>

```json
{
  "query": "FASB steering backtracking NeurIPS 2025 TruthfulQA MC1 results FActScore long-form generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "993c0239-9133-48da-9145-b8085f84171a",
  "isSidechain": false,
  "requestId": "req_011Cb5zBrNnS4E5KAvPepA7R",
  "type": "assistant",
  "uuid": "291f8523-0884-490e-aa99-74e1cef5c552",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NBzkgVUxGECSPPiQzSbVLg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1240,
      "cache_read_input_tokens": 36787,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1240,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 36787,
          "cache_creation_input_tokens": 1240,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1240
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

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-16 (UTC).**  ## Original idea {   \"title\": \"Geometry-Triggered Sentence-Level Activation Steering for Factual Hall…",
  "leafUuid": "291f8523-0884-490e-aa99-74e1cef5c552",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise GTS with PCNet differentiation and realistic timeline",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c"
}
```

---

### Tool result

_source line 44 · 2026-05-16T09:10:09.004Z_

<details><summary>↩ Tool result · `toolu_01XsMrenp95DBn55nW4uiHYp`</summary>

```text
Web search results for query: "FASB steering backtracking NeurIPS 2025 TruthfulQA MC1 results FActScore long-form generation"

Links: [{"title":"Steering When Necessary: Flexible Steering Large Language Models with Backtracking","url":"https://arxiv.org/html/2508.17621"},{"title":"NeurIPS Poster Steering When Necessary: Flexible Steering Large Language Models with Backtracking","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/116311"},{"title":"Steering When Necessary: Flexible Steering Large Language Models with Backtracking | OpenReview","url":"https://openreview.net/forum?id=l75RyRcevf"},{"title":"[2508.17621] Steering When Necessary: Flexible Steering Large Language Models with Backtracking","url":"https://arxiv.org/abs/2508.17621"},{"title":"Spectral Editing of Activations for Large Language Model Alignment","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf"},{"title":"FLAME : Factuality-Aware Alignment for Large Language Models","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/d16152d53088ad779ffa634e7bf66166-Paper-Conference.pdf"},{"title":"GitHub - sylinrl/TruthfulQA: TruthfulQA: Measuring How Models Imitate Human Falsehoods · GitHub","url":"https://github.com/sylinrl/TruthfulQA"},{"title":"LOFIT: Localized Fine-tuning on LLM Representations Fangcong Yin","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"},{"title":"Large Language Model Evaluation in 2025: Smarter Metrics That ...","url":"https://www.techrxiv.org/users/927947/articles/1304989/master/file/data/Large%20Language%20Model%20Evaluation%20in%202025-Smarter%20Metrics%20That%20Separate%20Hype%20from%20Trust/Large%20Language%20Model%20Evaluation%20in%202025-Smarter%20Metrics%20That%20Separate%20Hype%20from%20Trust.pdf"}]

Based on the search results, I found relevant information about FASB (Flexible Activation Steering with Backtracking) at NeurIPS 2025:

## FASB: Flexible Activation Steering with Backtracking at NeurIPS 2025

The Flexible Activation Steering with Backtracking (FASB) framework dynamically determines both the necessity and strength of intervention by tracking the internal states of the LLMs during generation, considering both the question and the generated content.

### Key Results on TruthfulQA MC1

The method yields significant improvements of 24.61 in MC1 on Qwen2.5-7B. More broadly, compared with the ITI method, the FASB method achieves better performance on all 6 LLMs, with an improvement of 23.50 on the MC1 for Qwen2.5-7B, and it outperforms the ITI method in terms of performance across different LLMs.

### Backtracking Mechanism

Since intervening after detecting a deviation from the desired behavior is often too late, the backtracking mechanism was proposed to correct the deviated tokens and steer the LLMs toward the desired behavior.

### Evaluation Scope

Extensive experiments on the TruthfulQA dataset and six multiple-choice datasets demonstrate that the method outperforms baselines. However, the search results provided do not contain specific details about FActScore results on long-form generation tasks from this paper.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "291f8523-0884-490e-aa99-74e1cef5c552",
  "isSidechain": false,
  "promptId": "6c31b04f-5b26-44ca-b486-31fab11de0b0",
  "type": "user",
  "uuid": "692bcdcf-0803-4f2f-b2ce-d78e197b6c11",
  "toolUseResult": {
    "query": "FASB steering backtracking NeurIPS 2025 TruthfulQA MC1 results FActScore long-form generation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Nz9kFAyDLchk9qHYFxLiq8",
        "content": [
          {
            "title": "Steering When Necessary: Flexible Steering Large Language Models with Backtracking",
            "url": "https://arxiv.org/html/2508.17621"
          },
          {
            "title": "NeurIPS Poster Steering When Necessary: Flexible Steering Large Language Models with Backtracking",
            "url": "https://neurips.cc/virtual/2025/loc/san-diego/poster/116311"
          },
          {
            "title": "Steering When Necessary: Flexible Steering Large Language Models with Backtracking | OpenReview",
            "url": "https://openreview.net/forum?id=l75RyRcevf"
          },
          {
            "title": "[2508.17621] Steering When Necessary: Flexible Steering Large Language Models with Backtracking",
            "url": "https://arxiv.org/abs/2508.17621"
          },
          {
            "title": "Spectral Editing of Activations for Large Language Model Alignment",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/684c59d614fe6ae74a3be8c3ef07e061-Paper-Conference.pdf"
          },
          {
            "title": "FLAME : Factuality-Aware Alignment for Large Language Models",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/d16152d53088ad779ffa634e7bf66166-Paper-Conference.pdf"
          },
          {
            "title": "GitHub - sylinrl/TruthfulQA: TruthfulQA: Measuring How Models Imitate Human Falsehoods · GitHub",
            "url": "https://github.com/sylinrl/TruthfulQA"
          },
          {
            "title": "LOFIT: Localized Fine-tuning on LLM Representations Fangcong Yin",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf"
          },
          {
            "title": "GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub",
            "url": "https://github.com/EdinburghNLP/awesome-hallucination-detection"
          },
          {
            "title": "Large Language Model Evaluation in 2025: Smarter Metrics That ...",
            "url": "https://www.techrxiv.org/users/927947/articles/1304989/master/file/data/Large%20Language%20Model%20Evaluation%20in%202025-Smarter%20Metrics%20That%20Separate%20Hype%20from%20Trust/Large%20Language%20Model%20Evaluation%20in%202025-Smarter%20Metrics%20That%20Separate%20Hype%20from%20Trust.pdf"
          }
        ]
      },
      "Based on the search results, I found relevant information about FASB (Flexible Activation Steering with Backtracking) at NeurIPS 2025:\n\n## FASB: Flexible Activation Steering with Backtracking at NeurIPS 2025\n\nThe Flexible Activation Steering with Backtracking (FASB) framework dynamically determines both the necessity and strength of intervention by tracking the internal states of the LLMs during generation, considering both the question and the generated content.\n\n### Key Results on TruthfulQA MC1\n\nThe method yields significant improvements of 24.61 in MC1 on Qwen2.5-7B. More broadly, compared with the ITI method, the FASB method achieves better performance on all 6 LLMs, with an improvement of 23.50 on the MC1 for Qwen2.5-7B, and it outperforms the ITI method in terms of performance across different LLMs.\n\n### Backtracking Mechanism\n\nSince intervening after detecting a deviation from the desired behavior is often too late, the backtracking mechanism was proposed to correct the deviated tokens and steer the LLMs toward the desired behavior.\n\n### Evaluation Scope\n\nExtensive experiments on the TruthfulQA dataset and six multiple-choice datasets demonstrate that the method outperforms baselines. However, the search results provided do not contain specific details about FActScore results on long-form generation tasks from this paper."
    ],
    "durationSeconds": 7.332321129999997
  },
  "sourceToolAssistantUUID": "291f8523-0884-490e-aa99-74e1cef5c552",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T09:10:12.209Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UkTUYiPK8uWTHCwqnA3sB4`</summary>

```json
{
  "query": "selective hallucination gating activation steering concurrent work May 2026 arXiv geometry-aware"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "692bcdcf-0803-4f2f-b2ce-d78e197b6c11",
  "isSidechain": false,
  "requestId": "req_011Cb5zD1MoqzjhX1NtxL1KH",
  "type": "assistant",
  "uuid": "aae3f1ce-752e-4658-8522-09b837ca2d32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjcfTZQRsWTmq3PZVBPKEC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1145,
      "cache_read_input_tokens": 38027,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1145,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 38027,
          "cache_creation_input_tokens": 1145,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1145
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

_source line 46 · 2026-05-16T09:10:19.070Z_

<details><summary>↩ Tool result · `toolu_01UkTUYiPK8uWTHCwqnA3sB4`</summary>

```text
Web search results for query: "selective hallucination gating activation steering concurrent work May 2026 arXiv geometry-aware"

Links: [{"title":"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/html/2604.15400v1"},{"title":"Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/pdf/2602.08169"},{"title":"Dynamic Multimodal Activation Steering for Hallucination ...","url":"https://arxiv.org/pdf/2602.21704"},{"title":"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits","url":"https://arxiv.org/html/2605.05953"},{"title":"Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models","url":"https://arxiv.org/html/2602.21704v1"},{"title":"Hallucination as Output-Boundary Misclassification: A Composite Abstention Architecture for Language Models","url":"https://arxiv.org/html/2604.06195"},{"title":"Steering to Say No: Configurable Refusal via Activation Steering in Vision Language Models","url":"https://arxiv.org/html/2602.07013v1"},{"title":"[2605.04641] CAST: Mitigating Object Hallucination in Large Vision-Language Models via Caption-Guided Visual Attention Steering","url":"https://arxiv.org/abs/2605.04641"},{"title":"[2602.21704] Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models","url":"https://arxiv.org/abs/2602.21704"},{"title":"[2410.15778] Reducing Hallucinations in Vision-Language Models via Latent Space Steering","url":"https://arxiv.org/abs/2410.15778"}]

Based on the search results, I found several highly relevant papers from arXiv related to your query about hallucination, activation steering, gating, and geometry-aware approaches from May 2026:

## Key Findings:

**Concurrent Work on Geometry-Aware Steering:**

The concurrent work of Cherukuri & Varshney frames hallucination through basin geometry and proposes geometry-aware steering. This appears in a paper titled "Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation."

**Spherical Steering (Geometry-Aware Activation Rotation):**

Contrastive pairs define a truthfulness axis, and steering is done by a norm-preserving geodesic rotation of hidden activations toward truthfulness, with a von Mises-Fisher confidence gate to selectively intervene. The overall intervention is primarily controlled by β, which sets the selection boundary, and α, which determines the magnitude of rotation once the gate is triggered.

**Recent May 2026 Work:**

CAST: Mitigating Object Hallucination in Large Vision-Language Models via Caption-Guided Visual Attention Steering was submitted on May 6, 2026. CAST is a training-free, plug-and-play hallucination mitigation method that leverages the attention activation pattern corresponding to caption queries to enhance LVLMs' visual perception capability.

These papers represent cutting-edge concurrent research on selective gating mechanisms combined with geometry-aware activation steering for hallucination mitigation in language and vision-language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aae3f1ce-752e-4658-8522-09b837ca2d32",
  "isSidechain": false,
  "promptId": "6c31b04f-5b26-44ca-b486-31fab11de0b0",
  "type": "user",
  "uuid": "0079ef69-3512-49c3-b394-f12adf97a0a7",
  "toolUseResult": {
    "query": "selective hallucination gating activation steering concurrent work May 2026 arXiv geometry-aware",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PA9kYhhN9y1g3JVg7SpEjg",
        "content": [
          {
            "title": "Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation",
            "url": "https://arxiv.org/html/2604.15400v1"
          },
          {
            "title": "Spherical Steering: Geometry-Aware Activation Rotation for Language Models",
            "url": "https://arxiv.org/pdf/2602.08169"
          },
          {
            "title": "Dynamic Multimodal Activation Steering for Hallucination ...",
            "url": "https://arxiv.org/pdf/2602.21704"
          },
          {
            "title": "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits",
            "url": "https://arxiv.org/html/2605.05953"
          },
          {
            "title": "Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models",
            "url": "https://arxiv.org/html/2602.21704v1"
          },
          {
            "title": "Hallucination as Output-Boundary Misclassification: A Composite Abstention Architecture for Language Models",
            "url": "https://arxiv.org/html/2604.06195"
          },
          {
            "title": "Steering to Say No: Configurable Refusal via Activation Steering in Vision Language Models",
            "url": "https://arxiv.org/html/2602.07013v1"
          },
          {
            "title": "[2605.04641] CAST: Mitigating Object Hallucination in Large Vision-Language Models via Caption-Guided Visual Attention Steering",
            "url": "https://arxiv.org/abs/2605.04641"
          },
          {
            "title": "[2602.21704] Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models",
            "url": "https://arxiv.org/abs/2602.21704"
          },
          {
            "title": "[2410.15778] Reducing Hallucinations in Vision-Language Models via Latent Space Steering",
            "url": "https://arxiv.org/abs/2410.15778"
          }
        ]
      },
      "Based on the search results, I found several highly relevant papers from arXiv related to your query about hallucination, activation steering, gating, and geometry-aware approaches from May 2026:\n\n## Key Findings:\n\n**Concurrent Work on Geometry-Aware Steering:**\n\nThe concurrent work of Cherukuri & Varshney frames hallucination through basin geometry and proposes geometry-aware steering. This appears in a paper titled \"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation.\"\n\n**Spherical Steering (Geometry-Aware Activation Rotation):**\n\nContrastive pairs define a truthfulness axis, and steering is done by a norm-preserving geodesic rotation of hidden activations toward truthfulness, with a von Mises-Fisher confidence gate to selectively intervene. The overall intervention is primarily controlled by β, which sets the selection boundary, and α, which determines the magnitude of rotation once the gate is triggered.\n\n**Recent May 2026 Work:**\n\nCAST: Mitigating Object Hallucination in Large Vision-Language Models via Caption-Guided Visual Attention Steering was submitted on May 6, 2026. CAST is a training-free, plug-and-play hallucination mitigation method that leverages the attention activation pattern corresponding to caption queries to enhance LVLMs' visual perception capability.\n\nThese papers represent cutting-edge concurrent research on selective gating mechanisms combined with geometry-aware activation steering for hallucination mitigation in language and vision-language models."
    ],
    "durationSeconds": 6.855817494999996
  },
  "sourceToolAssistantUUID": "aae3f1ce-752e-4658-8522-09b837ca2d32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T09:10:22.055Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NPzon8Ggg8RxtYYwkNDtqa`</summary>

```json
{
  "query": "PCNet PC-LDCD TruthfulQA MC1 results Llama-3.1-8B comparison activation steering ITI 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0079ef69-3512-49c3-b394-f12adf97a0a7",
  "isSidechain": false,
  "requestId": "req_011Cb5zDkPBBWJk6KCtQ6T6d",
  "type": "assistant",
  "uuid": "2b6e265c-914e-4645-9cc8-a094b0bddf7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gGTX5Kqa5ierSmDeYwZgZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 947,
      "cache_read_input_tokens": 39172,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 947,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 86,
          "cache_read_input_tokens": 39172,
          "cache_creation_input_tokens": 947,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 947
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

_source line 48 · 2026-05-16T09:10:29.196Z_

<details><summary>↩ Tool result · `toolu_01NPzon8Ggg8RxtYYwkNDtqa`</summary>

```text
Web search results for query: "PCNet PC-LDCD TruthfulQA MC1 results Llama-3.1-8B comparison activation steering ITI 2026"

Links: [{"title":"GitHub - duykhuongnguyen/MAT-Steer · GitHub","url":"https://github.com/duykhuongnguyen/MAT-Steer"},{"title":"[2308.10248] Activation Addition: Steering Language Models Without Optimization","url":"https://ar5iv.labs.arxiv.org/html/2308.10248"},{"title":"The Development of Activation Steering","url":"https://sidn.baulab.info/steering/"},{"title":"Steering Llama 2 via Contrastive Activation Addition","url":"https://arxiv.org/html/2312.06681v2"},{"title":"GitHub - likenneth/honest_llama: Inference-Time Intervention: Eliciting Truthful Answers from a Language Model · GitHub","url":"https://github.com/likenneth/honest_llama"},{"title":"Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method for Diverse Hallucinations Categories","url":"https://arxiv.org/html/2406.00034v1"},{"title":"NL-ITI: Optimizing Probing and Intervention for Improvement of ITI Method","url":"https://arxiv.org/html/2403.18680v1"},{"title":"meta-llama/Llama-3.1-8B-Instruct · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct"},{"title":"Inference-Time Intervention: Eliciting Truthful Answers from a Language Model | OpenReview","url":"https://openreview.net/forum?id=aLLuYpn83y"},{"title":"RedHatAI/Meta-Llama-3.1-8B-Instruct-FP8 · Hugging Face","url":"https://huggingface.co/RedHatAI/Meta-Llama-3.1-8B-Instruct-FP8"}]

Based on my search results, I found relevant information about activation steering, ITI (Inference-Time Intervention), and TruthfulQA MC1 results, though the search did not return specific results about "PCNet" or "PC-LDCD" by those exact names.

Here's what I found regarding related topics:

**Activation Steering and ITI with TruthfulQA:**

Inference-Time Intervention (ITI) is a technique designed to enhance the truthfulness of large language models by shifting model activations during inference following a set of directions across a limited number of attention heads, significantly improving the performance of LLaMA models on the TruthfulQA benchmark.

NL-ITI outperforms ITI on 4 major benchmarks, including TruthfulQA, reporting around 14% MC1 metric improvement (up to 50.19).

**Llama-3.1-8B Context:**

Recent work has involved extracting last-token activations at specified layers (such as layer 14) from Llama-3.1-8B on the TruthfulQA dataset for steering applications.

**MC1 Metric:**

MC1 (Single-true) involves selecting the only correct answer from 4-5 answer choices based on the highest log-probability assigned to the answer choice.

However, I did not find specific papers or results about "PCNet PC-LDCD" in these search results. If you're looking for a specific recent paper or benchmark comparing these methods, you may want to search for the full paper title or check recent preprints on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b6e265c-914e-4645-9cc8-a094b0bddf7e",
  "isSidechain": false,
  "promptId": "6c31b04f-5b26-44ca-b486-31fab11de0b0",
  "type": "user",
  "uuid": "bbd06cdc-f941-4864-b999-de51f4afdcf5",
  "toolUseResult": {
    "query": "PCNet PC-LDCD TruthfulQA MC1 results Llama-3.1-8B comparison activation steering ITI 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SnX6UG2pjVt1RN1WNCTiY4",
        "content": [
          {
            "title": "GitHub - duykhuongnguyen/MAT-Steer · GitHub",
            "url": "https://github.com/duykhuongnguyen/MAT-Steer"
          },
          {
            "title": "[2308.10248] Activation Addition: Steering Language Models Without Optimization",
            "url": "https://ar5iv.labs.arxiv.org/html/2308.10248"
          },
          {
            "title": "The Development of Activation Steering",
            "url": "https://sidn.baulab.info/steering/"
          },
          {
            "title": "Steering Llama 2 via Contrastive Activation Addition",
            "url": "https://arxiv.org/html/2312.06681v2"
          },
          {
            "title": "GitHub - likenneth/honest_llama: Inference-Time Intervention: Eliciting Truthful Answers from a Language Model · GitHub",
            "url": "https://github.com/likenneth/honest_llama"
          },
          {
            "title": "Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method for Diverse Hallucinations Categories",
            "url": "https://arxiv.org/html/2406.00034v1"
          },
          {
            "title": "NL-ITI: Optimizing Probing and Intervention for Improvement of ITI Method",
            "url": "https://arxiv.org/html/2403.18680v1"
          },
          {
            "title": "meta-llama/Llama-3.1-8B-Instruct · Hugging Face",
            "url": "https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct"
          },
          {
            "title": "Inference-Time Intervention: Eliciting Truthful Answers from a Language Model | OpenReview",
            "url": "https://openreview.net/forum?id=aLLuYpn83y"
          },
          {
            "title": "RedHatAI/Meta-Llama-3.1-8B-Instruct-FP8 · Hugging Face",
            "url": "https://huggingface.co/RedHatAI/Meta-Llama-3.1-8B-Instruct-FP8"
          }
        ]
      },
      "Based on my search results, I found relevant information about activation steering, ITI (Inference-Time Intervention), and TruthfulQA MC1 results, though the search did not return specific results about \"PCNet\" or \"PC-LDCD\" by those exact names.\n\nHere's what I found regarding related topics:\n\n**Activation Steering and ITI with TruthfulQA:**\n\nInference-Time Intervention (ITI) is a technique designed to enhance the truthfulness of large language models by shifting model activations during inference following a set of directions across a limited number of attention heads, significantly improving the performance of LLaMA models on the TruthfulQA benchmark.\n\nNL-ITI outperforms ITI on 4 major benchmarks, including TruthfulQA, reporting around 14% MC1 metric improvement (up to 50.19).\n\n**Llama-3.1-8B Context:**\n\nRecent work has involved extracting last-token activations at specified layers (such as layer 14) from Llama-3.1-8B on the TruthfulQA dataset for steering applications.\n\n**MC1 Metric:**\n\nMC1 (Single-true) involves selecting the only correct answer from 4-5 answer choices based on the highest log-probability assigned to the answer choice.\n\nHowever, I did not find specific papers or results about \"PCNet PC-LDCD\" in these search results. If you're looking for a specific recent paper or benchmark comparing these methods, you may want to search for the full paper title or check recent preprints on arXiv."
    ],
    "durationSeconds": 7.137595396000019
  },
  "sourceToolAssistantUUID": "2b6e265c-914e-4645-9cc8-a094b0bddf7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-16T09:10:31.943Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H3mK3F9DQ8uj7PZq5pe69U`</summary>

```json
{
  "query": "nnsight library activation steering sentence boundary detection implementation feasibility 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbd06cdc-f941-4864-b999-de51f4afdcf5",
  "isSidechain": false,
  "requestId": "req_011Cb5zEVewDytLEjzgpfpHm",
  "type": "assistant",
  "uuid": "7068f03f-851c-4326-8b9d-a0f4ee183050",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AvUapDMV6YnRQLh6hWzTEU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1024,
      "cache_read_input_tokens": 40119,
      "output_tokens": 66,
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
          "output_tokens": 66,
          "cache_read_input_tokens": 40119,
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

_source line 50 · 2026-05-16T09:10:39.268Z_

<details><summary>↩ Tool result · `toolu_01H3mK3F9DQ8uj7PZq5pe69U`</summary>

```text
Web search results for query: "nnsight library activation steering sentence boundary detection implementation feasibility 2026"

Links: [{"title":"nnsight/NNsight.md at main · ndif-team/nnsight","url":"https://github.com/ndif-team/nnsight/blob/main/NNsight.md"},{"title":"Introducing NNsight 0.6 - nnsight","url":"https://nnsight.net/blog/2026/02/26/introducing-nnsight-06/"},{"title":"2026 - nnsight","url":"https://nnsight.net/blog/archive/2026/"},{"title":"nnsight","url":"https://nnsight.net/"},{"title":"nnsight · PyPI","url":"https://pypi.org/project/nnsight/"},{"title":"GitHub - ndif-team/nnsight: The nnsight package enables interpreting and manipulating the internals of deep learned models. · GitHub","url":"https://github.com/ndif-team/nnsight"},{"title":"GitHub - jkminder/nnpatch: A library for activation patching based on nnsight. · GitHub","url":"https://github.com/jkminder/nnpatch"},{"title":"NNsight and NDIF: Democratizing Access to Foundation Model Internals","url":"https://arxiv.org/html/2407.14561v1"},{"title":"NNsight Walkthrough — nnsight","url":"https://nnsight.net/notebooks/tutorials/get_started/walkthrough/"},{"title":"Main Tutorials — nnsight","url":"https://nnsight.net/walkthroughs/"}]

Based on the search results, here's what I found about nnsight and related implementations:

## Overview of NNsight

The nnsight package enables interpreting and manipulating the internals of deep learned models. The pattern includes activation patching, causal tracing, steering, probing, and other techniques that require the ability to observe and modify the internal computations of a neural network during inference.

## Activation Steering Capabilities

NNsight 0.6 supports steering interventions that apply on every forward pass during generation, with recent versions enabling async mode for streaming output while still applying interventions. Gradient-based steering is supported as one of the gradient-based interpretability methods.

## Current Implementation Status (May 2026)

The library appears to be actively maintained, with version 0.7.0 released on May 5, 2026.

## Limitations

Regarding implementation feasibility, the search results note that interventions are limited to module boundaries; you cannot hook into arbitrary operations within a module's forward pass. This means sentence boundary detection using activation steering would be constrained to operations at module-level boundaries rather than at arbitrary points within operations.

The search results do not contain specific information about sentence boundary detection implementation feasibility or dedicated tutorials/documentation for that particular use case in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7068f03f-851c-4326-8b9d-a0f4ee183050",
  "isSidechain": false,
  "promptId": "6c31b04f-5b26-44ca-b486-31fab11de0b0",
  "type": "user",
  "uuid": "b7b87ca8-cdd8-4e35-bb61-c5f3e074779b",
  "toolUseResult": {
    "query": "nnsight library activation steering sentence boundary detection implementation feasibility 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_017EAWGf4STbikwAR1UriHyf",
        "content": [
          {
            "title": "nnsight/NNsight.md at main · ndif-team/nnsight",
            "url": "https://github.com/ndif-team/nnsight/blob/main/NNsight.md"
          },
          {
            "title": "Introducing NNsight 0.6 - nnsight",
            "url": "https://nnsight.net/blog/2026/02/26/introducing-nnsight-06/"
          },
          {
            "title": "2026 - nnsight",
            "url": "https://nnsight.net/blog/archive/2026/"
          },
          {
            "title": "nnsight",
            "url": "https://nnsight.net/"
          },
          {
            "title": "nnsight · PyPI",
            "url": "https://pypi.org/project/nnsight/"
          },
          {
            "title": "GitHub - ndif-team/nnsight: The nnsight package enables interpreting and manipulating the internals of deep learned models. · GitHub",
            "url": "https://github.com/ndif-team/nnsight"
          },
          {
            "title": "GitHub - jkminder/nnpatch: A library for activation patching based on nnsight. · GitHub",
            "url": "https://github.com/jkminder/nnpatch"
          },
          {
            "title": "NNsight and NDIF: Democratizing Access to Foundation Model Internals",
            "url": "https://arxiv.org/html/2407.14561v1"
          },
          {
            "title": "NNsight Walkthrough — nnsight",
            "url": "https://nnsight.net/notebooks/tutorials/get_started/walkthrough/"
          },
          {
            "title": "Main Tutorials — nnsight",
            "url": "https://nnsight.net/walkthroughs/"
          }
        ]
      },
      "Based on the search results, here's what I found about nnsight and related implementations:\n\n## Overview of NNsight\n\nThe nnsight package enables interpreting and manipulating the internals of deep learned models. The pattern includes activation patching, causal tracing, steering, probing, and other techniques that require the ability to observe and modify the internal computations of a neural network during inference.\n\n## Activation Steering Capabilities\n\nNNsight 0.6 supports steering interventions that apply on every forward pass during generation, with recent versions enabling async mode for streaming output while still applying interventions. Gradient-based steering is supported as one of the gradient-based interpretability methods.\n\n## Current Implementation Status (May 2026)\n\nThe library appears to be actively maintained, with version 0.7.0 released on May 5, 2026.\n\n## Limitations\n\nRegarding implementation feasibility, the search results note that interventions are limited to module boundaries; you cannot hook into arbitrary operations within a module's forward pass. This means sentence boundary detection using activation steering would be constrained to operations at module-level boundaries rather than at arbitrary points within operations.\n\nThe search results do not contain specific information about sentence boundary detection implementation feasibility or dedicated tutorials/documentation for that particular use case in 2026."
    ],
    "durationSeconds": 7.320665122000006
  },
  "sourceToolAssistantUUID": "7068f03f-851c-4326-8b9d-a0f4ee183050",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-16T09:10:42.237Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015UYTuCz6xXjC1UEzzF1Atu`</summary>

```json
{
  "query": "ARR May 2026 submission deadline EMNLP 2026 exact date requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7b87ca8-cdd8-4e35-bb61-c5f3e074779b",
  "isSidechain": false,
  "requestId": "req_011Cb5zFEkGujBYSDXuh5MCK",
  "type": "assistant",
  "uuid": "74236033-4eb5-4a67-aead-e6434212fcb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ApijFUGTkPY1n6AuwdbJxk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 790,
      "cache_read_input_tokens": 41143,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 41143,
          "cache_creation_input_tokens": 790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 790
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

_source line 52_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-16 (UTC).**  ## Original idea {   \"title\": \"Geometry-Triggered Sentence-Level Activation Steering for Factual Hall…",
  "leafUuid": "74236033-4eb5-4a67-aead-e6434212fcb4",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c"
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise GTS with PCNet differentiation and realistic timeline",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c"
}
```

---

### Tool result

_source line 54 · 2026-05-16T09:10:50.887Z_

<details><summary>↩ Tool result · `toolu_015UYTuCz6xXjC1UEzzF1Atu`</summary>

```text
Web search results for query: "ARR May 2026 submission deadline EMNLP 2026 exact date requirements"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"The updated ARR schedule has now been posted! As per the call for papers, the submission deadline for EMNLP 2025 will be May 19th https://t.co/kvTZ8LPxam #EMNLP2025\" / X","url":"https://x.com/emnlpmeeting/status/1892259536137785419"}]

Based on the search results, here are the key details for the ARR May 2026 submission deadline for EMNLP 2026:

## Exact Submission Deadline

The ARR submission deadline is May 25, 2026. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

## Key Requirements

**Venue Selection**: Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors must explicitly declare which conference they intend to commit to at submission time, and this choice is binding for EMNLP 2026.

**Author Registration**: After submission, all authors must complete the author registration form by May 27, 2026 EoD AoE.

**Mandatory Reviewing**: All authors are expected to sign up to review, or serve as an Area Chair or Senior Area Chair, with assignments subsequently based on qualifications.

**Dual Submissions**: Dual submissions are not allowed.

## Related Timeline

- Author response and author-reviewer discussion: July 7 - July 13, 2026
- Meta review released: July 30, 2026
- EMNLP commitment deadline: August 2, 2026
- Notification of acceptance: August 20, 2026


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74236033-4eb5-4a67-aead-e6434212fcb4",
  "isSidechain": false,
  "promptId": "6c31b04f-5b26-44ca-b486-31fab11de0b0",
  "type": "user",
  "uuid": "150de4c6-523a-4d19-976b-d98bddd1353a",
  "toolUseResult": {
    "query": "ARR May 2026 submission deadline EMNLP 2026 exact date requirements",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RCCPAGbhcHcAVoB5zchqXN",
        "content": [
          {
            "title": "Call for Main Conference Papers - EMNLP 2026",
            "url": "https://2026.emnlp.org/calls/main_conference_papers/"
          },
          {
            "title": "EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X",
            "url": "https://x.com/emnlpmeeting/status/2029508292637061462"
          },
          {
            "title": "Dates and Venues",
            "url": "http://aclrollingreview.org/dates"
          },
          {
            "title": "LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)",
            "url": "https://linguistlist.org/issues/37/972/"
          },
          {
            "title": "EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X",
            "url": "https://x.com/emnlpmeeting/status/2047754845919031450"
          },
          {
            "title": "AI Conference Deadlines",
            "url": "https://mlciv.com/ai-deadlines/"
          },
          {
            "title": "Call for Main Conference Papers -",
            "url": "https://2026.eacl.org/calls/papers/"
          },
          {
            "title": "EMNLP 2026 : The 2026 Conference on Empirical Methods in N",
            "url": "https://callforpaper.org/call-for-papers-emnlp-2026"
          },
          {
            "title": "emnlp 2026 - AI Conference Deadlines",
            "url": "https://mlciv.com/ai-deadlines/conference/?id=emnlp26"
          },
          {
            "title": "EMNLP 2026 on X: \"The updated ARR schedule has now been posted! As per the call for papers, the submission deadline for EMNLP 2025 will be May 19th https://t.co/kvTZ8LPxam #EMNLP2025\" / X",
            "url": "https://x.com/emnlpmeeting/status/1892259536137785419"
          }
        ]
      },
      "Based on the search results, here are the key details for the ARR May 2026 submission deadline for EMNLP 2026:\n\n## Exact Submission Deadline\n\nThe ARR submission deadline is May 25, 2026. All deadlines are 11:59PM UTC-12:00 (\"anywhere on Earth\").\n\n## Key Requirements\n\n**Venue Selection**: Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors must explicitly declare which conference they intend to commit to at submission time, and this choice is binding for EMNLP 2026.\n\n**Author Registration**: After submission, all authors must complete the author registration form by May 27, 2026 EoD AoE.\n\n**Mandatory Reviewing**: All authors are expected to sign up to review, or serve as an Area Chair or Senior Area Chair, with assignments subsequently based on qualifications.\n\n**Dual Submissions**: Dual submissions are not allowed.\n\n## Related Timeline\n\n- Author response and author-reviewer discussion: July 7 - July 13, 2026\n- Meta review released: July 30, 2026\n- EMNLP commitment deadline: August 2, 2026\n- Notification of acceptance: August 20, 2026"
    ],
    "durationSeconds": 8.645038774999994
  },
  "sourceToolAssistantUUID": "74236033-4eb5-4a67-aead-e6434212fcb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 55 · 2026-05-16T09:10:50.889Z_

```json
{
  "parentUuid": "150de4c6-523a-4d19-976b-d98bddd1353a",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3944e5e8-99a2-496b-8878-8a356ea86c82",
  "timestamp": "2026-05-16T09:10:50.889Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 56 · 2026-05-16T09:10:53.719Z_

Now let me do one more search for any very recent work that might have appeared in May 2026 that could further impact novelty.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3944e5e8-99a2-496b-8878-8a356ea86c82",
  "isSidechain": false,
  "requestId": "req_011Cb5zG6RjofTuYckcPKio8",
  "type": "assistant",
  "uuid": "cf9cdb15-810f-418d-b261-c82271696bba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017TrrX5iQHchUDEqxpQWoyg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1178,
      "cache_read_input_tokens": 41933,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1178,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 41933,
          "cache_creation_input_tokens": 1178,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1178
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

_source line 57 · 2026-05-16T09:10:54.487Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HH2wZUP3hYGNNHy8QSac2i`</summary>

```json
{
  "query": "preemptive hallucination prevention activation steering before generation claim-level 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf9cdb15-810f-418d-b261-c82271696bba",
  "isSidechain": false,
  "requestId": "req_011Cb5zG6RjofTuYckcPKio8",
  "type": "assistant",
  "uuid": "e325b725-9caa-43f1-a68d-0470b2fec2a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017TrrX5iQHchUDEqxpQWoyg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1178,
      "cache_read_input_tokens": 41933,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1178,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 41933,
          "cache_creation_input_tokens": 1178,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1178
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

_source line 58 · 2026-05-16T09:11:02.745Z_

<details><summary>↩ Tool result · `toolu_01HH2wZUP3hYGNNHy8QSac2i`</summary>

```text
Web search results for query: "preemptive hallucination prevention activation steering before generation claim-level 2026 arXiv"

Links: [{"title":"Dynamic Multimodal Activation Steering for Hallucination ...","url":"https://arxiv.org/pdf/2602.21704"},{"title":"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation","url":"https://arxiv.org/html/2604.15400v1"},{"title":"Preemptive Hallucination Reduction: An Input-Level Approach for Multimodal Language Model","url":"https://arxiv.org/html/2505.24007"},{"title":"[2602.21704] Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models","url":"https://arxiv.org/abs/2602.21704"},{"title":"Constructing Benchmarks and Interventions for Combating Hallucinations in LLMs","url":"https://arxiv.org/html/2404.09971"},{"title":"Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models","url":"https://arxiv.org/html/2602.21704v1"},{"title":"arXiv:2410.02899v2 [cs.CL] 24 Jun 2025","url":"https://arxiv.org/pdf/2410.02899"},{"title":"Hallucination Detection and Mitigation in Large Language ...","url":"https://arxiv.org/pdf/2601.09929"},{"title":"Real-Time Detection of Hallucinated Entities in Long-Form Generation","url":"https://arxiv.org/html/2509.03531v1"},{"title":"Activation Steering Decoding: Mitigating Hallucination in ...","url":"https://aclanthology.org/2025.acl-long.634.pdf"}]

Based on the search results, I found several relevant papers from 2026 and related work on hallucination prevention using activation steering and preemptive approaches:

## Key Papers Found

**1. Dynamic Multimodal Activation Steering (DMAS)**
A training-free approach that proposes Dynamic Multimodal Activation Steering for hallucination mitigation in Large Vision-Language Models, which constructs a semantic-based truthfulness steering vector database and computes visual perception steering vectors, enabling context-aware interventions during inference. This paper was submitted on February 25, 2026.

**2. Preemptive Hallucination Reduction**
An input-level approach that dynamically selects the most appropriate image representation based on the posed question, achieving a 44.3% reduction in hallucination rates on the HaloQuest dataset.

**3. Hallucination as Trajectory Commitment**
Research showing that linear probes can detect hallucination in hidden states, but linear steering and direct activation steering along hallucination directions have not reliably prevented hallucinations.

**4. Preemptive Detection and Steering Before Generation**
Work that targets detection before hallucination onset, intending to steer generation away from hallucination before it is materialized in surface tokens, unlike prior work which detected and created steering vectors for hallucinations after they were generated.

These papers represent the current research frontier in preventing hallucinations through activation steering and preemptive approaches before generation occurs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e325b725-9caa-43f1-a68d-0470b2fec2a4",
  "isSidechain": false,
  "promptId": "6c31b04f-5b26-44ca-b486-31fab11de0b0",
  "type": "user",
  "uuid": "65dd5562-e2a2-49db-9888-4f170a93bda1",
  "toolUseResult": {
    "query": "preemptive hallucination prevention activation steering before generation claim-level 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_0164TLp8QHdvsbEEo4yV5m4n",
        "content": [
          {
            "title": "Dynamic Multimodal Activation Steering for Hallucination ...",
            "url": "https://arxiv.org/pdf/2602.21704"
          },
          {
            "title": "Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics in Transformer Generation",
            "url": "https://arxiv.org/html/2604.15400v1"
          },
          {
            "title": "Preemptive Hallucination Reduction: An Input-Level Approach for Multimodal Language Model",
            "url": "https://arxiv.org/html/2505.24007"
          },
          {
            "title": "[2602.21704] Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models",
            "url": "https://arxiv.org/abs/2602.21704"
          },
          {
            "title": "Constructing Benchmarks and Interventions for Combating Hallucinations in LLMs",
            "url": "https://arxiv.org/html/2404.09971"
          },
          {
            "title": "Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models",
            "url": "https://arxiv.org/html/2602.21704v1"
          },
          {
            "title": "arXiv:2410.02899v2 [cs.CL] 24 Jun 2025",
            "url": "https://arxiv.org/pdf/2410.02899"
          },
          {
            "title": "Hallucination Detection and Mitigation in Large Language ...",
            "url": "https://arxiv.org/pdf/2601.09929"
          },
          {
            "title": "Real-Time Detection of Hallucinated Entities in Long-Form Generation",
            "url": "https://arxiv.org/html/2509.03531v1"
          },
          {
            "title": "Activation Steering Decoding: Mitigating Hallucination in ...",
            "url": "https://aclanthology.org/2025.acl-long.634.pdf"
          }
        ]
      },
      "Based on the search results, I found several relevant papers from 2026 and related work on hallucination prevention using activation steering and preemptive approaches:\n\n## Key Papers Found\n\n**1. Dynamic Multimodal Activation Steering (DMAS)**\nA training-free approach that proposes Dynamic Multimodal Activation Steering for hallucination mitigation in Large Vision-Language Models, which constructs a semantic-based truthfulness steering vector database and computes visual perception steering vectors, enabling context-aware interventions during inference. This paper was submitted on February 25, 2026.\n\n**2. Preemptive Hallucination Reduction**\nAn input-level approach that dynamically selects the most appropriate image representation based on the posed question, achieving a 44.3% reduction in hallucination rates on the HaloQuest dataset.\n\n**3. Hallucination as Trajectory Commitment**\nResearch showing that linear probes can detect hallucination in hidden states, but linear steering and direct activation steering along hallucination directions have not reliably prevented hallucinations.\n\n**4. Preemptive Detection and Steering Before Generation**\nWork that targets detection before hallucination onset, intending to steer generation away from hallucination before it is materialized in surface tokens, unlike prior work which detected and created steering vectors for hallucinations after they were generated.\n\nThese papers represent the current research frontier in preventing hallucinations through activation steering and preemptive approaches before generation occurs."
    ],
    "durationSeconds": 8.255076681999984
  },
  "sourceToolAssistantUUID": "e325b725-9caa-43f1-a68d-0470b2fec2a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-16T09:11:06.075Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GPLxgaEF4babGnakvQgKFM`</summary>

```json
{
  "query": "Spherical Steering ICML 2026 MC1 TruthfulQA Llama-3.1-8B results released code github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65dd5562-e2a2-49db-9888-4f170a93bda1",
  "isSidechain": false,
  "requestId": "req_011Cb5zGy7yp7qBrYVZa8L5G",
  "type": "assistant",
  "uuid": "e1ea3c51-94d7-4b95-8fd6-2bb020195bee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016rKHYPkc3FEjQJpQthv8Yo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 940,
      "cache_read_input_tokens": 43111,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 940,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 86,
          "cache_read_input_tokens": 43111,
          "cache_creation_input_tokens": 940,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 940
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

_source line 60 · 2026-05-16T09:11:13.373Z_

<details><summary>↩ Tool result · `toolu_01GPLxgaEF4babGnakvQgKFM`</summary>

```text
Web search results for query: "Spherical Steering ICML 2026 MC1 TruthfulQA Llama-3.1-8B results released code github"

Links: [{"title":"GitHub - chili-lab/Spherical-Steering: [ICML 2026] Spherical Steering: Geometry-Aware Activation Rotation for Language Models · GitHub","url":"https://github.com/chili-lab/Spherical-Steering"},{"title":"Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/pdf/2602.08169"},{"title":"(PDF) Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://www.researchgate.net/publication/400605038_Spherical_Steering_Geometry-Aware_Activation_Rotation_for_Language_Models"},{"title":"Spherical Steering is highly complementary to few-shot prompting.... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Spherical-Steering-is-highly-complementary-to-few-shot-prompting-Performance-on_fig3_400605038"},{"title":"[2602.08169] Spherical Steering: Geometry-Aware Activation Rotation for Language Models","url":"https://arxiv.org/abs/2602.08169"},{"title":"GitHub - sylinrl/TruthfulQA: TruthfulQA: Measuring How Models Imitate Human Falsehoods · GitHub","url":"https://github.com/sylinrl/TruthfulQA"},{"title":"Activation Addition: Steering Language Models Without Optimization","url":"https://arxiv.org/html/2308.10248v4"},{"title":"Depth-Wise Activation Steering for Honest Language Models Gracjan Góral∗","url":"https://www.arxiv.org/pdf/2512.07667"},{"title":"SteeringControl: Holistic Evaluation of Alignment Steering in LLMs","url":"https://arxiv.org/pdf/2509.13450"},{"title":"2026 Conference","url":"https://icml.cc/"}]

Based on the web search results, I found information about Spherical Steering, an ICML 2026 paper with results on TruthfulQA MC1 using Llama-3.1-8B.

## Key Findings:

**Paper Details:**
The paper is titled "Spherical Steering: Geometry-Aware Activation Rotation for Language Models" by Zejia You, Chunyuan Deng, and Hanjie Chen (2026).

**GitHub Repository:**
The code and results are available at https://github.com/chili-lab/Spherical-Steering, with MC evaluation using TruthfulQA.csv.

**Results on Llama-3.1-8B:**
The method achieves substantial gains across all multiple-choice metrics (MC1/MC2/MC3) while maintaining strong open-ended generation quality (TRUE×INFO). Spherical Steering significantly outperforms addition-based baselines by notably +10% on TruthfulQA, COPA, and Storycloze, while simultaneously maintaining the model's general open-ended generation quality.

**Key Technical Details:**
Rather than shifting activations with a fixed vector, the method rotates them along a geodesic toward a target direction, and incorporates a confidence gate that dynamically modulates steering strength based on input uncertainty.

**Paper Citation:**
arxiv preprint arXiv:2602.08169

You can find the full paper at https://arxiv.org/abs/2602.08169 and the code at https://github.com/chili-lab/Spherical-Steering.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1ea3c51-94d7-4b95-8fd6-2bb020195bee",
  "isSidechain": false,
  "promptId": "6c31b04f-5b26-44ca-b486-31fab11de0b0",
  "type": "user",
  "uuid": "0437114e-6078-431f-905b-f9bb77af3527",
  "toolUseResult": {
    "query": "Spherical Steering ICML 2026 MC1 TruthfulQA Llama-3.1-8B results released code github",
    "results": [
      {
        "tool_use_id": "srvtoolu_0122Vn3vZtN1Y1riM9cMr7rF",
        "content": [
          {
            "title": "GitHub - chili-lab/Spherical-Steering: [ICML 2026] Spherical Steering: Geometry-Aware Activation Rotation for Language Models · GitHub",
            "url": "https://github.com/chili-lab/Spherical-Steering"
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
            "title": "[2602.08169] Spherical Steering: Geometry-Aware Activation Rotation for Language Models",
            "url": "https://arxiv.org/abs/2602.08169"
          },
          {
            "title": "GitHub - sylinrl/TruthfulQA: TruthfulQA: Measuring How Models Imitate Human Falsehoods · GitHub",
            "url": "https://github.com/sylinrl/TruthfulQA"
          },
          {
            "title": "Activation Addition: Steering Language Models Without Optimization",
            "url": "https://arxiv.org/html/2308.10248v4"
          },
          {
            "title": "Depth-Wise Activation Steering for Honest Language Models Gracjan Góral∗",
            "url": "https://www.arxiv.org/pdf/2512.07667"
          },
          {
            "title": "SteeringControl: Holistic Evaluation of Alignment Steering in LLMs",
            "url": "https://arxiv.org/pdf/2509.13450"
          },
          {
            "title": "2026 Conference",
            "url": "https://icml.cc/"
          }
        ]
      },
      "Based on the web search results, I found information about Spherical Steering, an ICML 2026 paper with results on TruthfulQA MC1 using Llama-3.1-8B.\n\n## Key Findings:\n\n**Paper Details:**\nThe paper is titled \"Spherical Steering: Geometry-Aware Activation Rotation for Language Models\" by Zejia You, Chunyuan Deng, and Hanjie Chen (2026).\n\n**GitHub Repository:**\nThe code and results are available at https://github.com/chili-lab/Spherical-Steering, with MC evaluation using TruthfulQA.csv.\n\n**Results on Llama-3.1-8B:**\nThe method achieves substantial gains across all multiple-choice metrics (MC1/MC2/MC3) while maintaining strong open-ended generation quality (TRUE×INFO). Spherical Steering significantly outperforms addition-based baselines by notably +10% on TruthfulQA, COPA, and Storycloze, while simultaneously maintaining the model's general open-ended generation quality.\n\n**Key Technical Details:**\nRather than shifting activations with a fixed vector, the method rotates them along a geodesic toward a target direction, and incorporates a confidence gate that dynamically modulates steering strength based on input uncertainty.\n\n**Paper Citation:**\narxiv preprint arXiv:2602.08169\n\nYou can find the full paper at https://arxiv.org/abs/2602.08169 and the code at https://github.com/chili-lab/Spherical-Steering."
    ],
    "durationSeconds": 7.295073076
  },
  "sourceToolAssistantUUID": "e1ea3c51-94d7-4b95-8fd6-2bb020195bee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-16T09:12:16.897Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the landscape. Let me synthesize my findings before writing the revision:

**Key findings from research:**

1. **PCNet (2605.05953)** is indeed a very close competitor:
   - Token-level gating using NLL from probabilistic circuits
   - Contrastive decoding (not activation steering) as intervention
   - TruthfulQA results: MC1 0.51 (Llama-3.1-8B), MC2 0.65
   - Corruption rate: 53.7%, Preservation rate: 79.3%
   - Overhead is minimal for the probabilistic circuit scoring itself, though the lookahead mechanism requires evaluating several additional blocks per anomalous token
   - Trained on just 500 paired samples, which is notably efficient
   - Benchmarked against other activation steering approaches like ITI, AdaSteer, and SADI

2. **Attractor Geometry (2605.05686)** confirmed:
   - Uses **Euclidean distance** explicitly: δ(x) = min_i ||h(x) − m_i||₂
   - AUROC 0.858 on TruthfulQA with L2 distance
   - Measurements taken at the first layer position before autoregressive dynamics compound errors
   - Explicitly states "transfer to open-domain settings requires further study"
   - Detection-only, no intervention

3. **Timeline**: ARR deadline is May 25, 2026. Today is May 16. That's 9 days remaining.

4. **SENTINEL (2507.12455)**: sentence-level early intervention but for vision-language models using preference learning, not activation steering. Different enough.

5. **Spherical Steering**: Code available at github.com/chili-lab/Spherical-Steering

**Deep thinking about the idea's viability:**

The stagnation at 3.2-3.5 across 3 rounds suggests something deeper is wrong. Let me think about this:

**Fundamental issues:**
1. The Mahalanobis motivation is built on an Euclidean result — this is an honest extrapolation, not a validated improvement
2. The timing hypothesis (sentence boundary N → factuality of sentence N+1) is a substantial extrapolation from a paper that explicitly disclaims this
3. PCNet is doing something very similar (selective geometric gating → intervention) but at token level with a different intervention mechanism
4. The 9-day timeline is extremely tight

**What's genuinely novel about GTS?**
- Sentence-level (claim-level) granularity for gating — no one else does this
- Pre-emptive rather than corrective — genuine advantage over FASB
- Combining geometry-aware detection with activation steering (vs PCNet's contrastive decoding)

**Should I pivot?**

Looking at PCNet's results more carefully, it still corrupts over half of originally correct generations when it intervenes, with a 79.3% preservation rate meaning roughly 21% of correct generations are still degraded. PCNet operates at the token level, which is a different approach than what I'm attempting.

The sentence-level approach could genuinely outperform PCNet on preservation since it avoids touching entire correct sentences, and it's more natural for long-form generation where claim-level decisions align better with how humans evaluate factuality. But this needs a major revision — the framing around Euclidean versus Mahalanobis needs to be honest, PCNet should be positioned as a primary competitor rather than a passing mention, the timeline needs to be realistic with a clearly defined minimum viable paper, and the timing hypothesis disclaimer needs prominence.

Actually, the core insight here is strong: sentence-level granularity is the right unit for selective steering. FActScore evaluates at sentence level, humans judge claims, and there's a real mismatch between token-level interventions and how factuality actually works.

The weak point is the specific mechanism — using Mahalanobis distance at sentence boundaries doesn't have solid grounding since the attractor geometry work used Euclidean distance on factoid completion, not sentence boundaries in open-ended generation. So the right move is a major revision that frames the Euclidean-to-sentence-boundary extrapolation as the central hypothesis to test, elevates PCNet to primary competitor status with detailed differentiation, defines a tight minimum viable scope for the remaining time, and simplifies the approach slightly for the MVP.

But with 9 days until the May 25 deadline and already at day 2+ still revising the idea itself, I need to map out what's actually achievable. The realistic path is: finalize the idea and set up the codebase in the next couple days, validate the timing hypothesis as the critical path, implement the core GTS method with evaluations on TruthfulQA and SimpleQA, run baselines and key ablations comparing Euclidean versus Mahalanobis and sentence versus token boundaries, then dedicate the final days to writing and formatting.

This is only feasible if I scope down significantly—stick with Llama-3.1-8B as the single model, focus on 4 core benchmarks, keep ablations to a minimal 2×2 grid, and drop the COAST combination and Qwen3-8B entirely. Now I'm revising the paper to make several critical clarifications: properly differentiate PCNet as a primary competitor with a full comparison, honestly state that the 0.858 result is Euclidean while Mahalanobis is a hypothesized improvement, define the 8-day execution plan with a 1-day buffer, add a disclaimer about the attractor geometry paper's limitations, and update resource estimates to reflect the 9 remaining days.

But I'm concerned about the reviewer feedback—scores went from 3.2 to 3.5 with no obvious improvement, which suggests they find the core idea marginal. The real question is whether sentence-level granularity actually justifies a paper when existing methods like Spherical Steering and FASB are already achieving substantial token-level improvements. I think it does matter for long-form generation where multiple claims need coordinated intervention, but I need to make that case much more convincingly.

The key insight is that token-level methods either intervene everywhere and degrade quality, or they miss claims entirely—and FActScore evaluation naturally operates at sentence level anyway. So the paper should position long-form generation as the primary use case, not short-form QA where the distinction barely matters.

For the framing, I need to move away from the technical jargon and focus on what actually matters: selective intervention at the right granularity for realistic generation tasks. Let me think about how to position the core contribution more compellingly. Now I'm mapping out the concrete changes needed: reframing the core problem around granularity mismatch with PCNet's corruption rate as evidence, repositioning Mahalanobis as an ablation rather than the main contribution, and elevating PCNet to a primary competitor alongside FASB and Spherical Steering. I'm also clarifying that the 0.858 AUROC uses Euclidean distance, simplifying the MVP scope to a single model with 4 benchmarks, and compressing the timeline to 9 days total. Let me compose the revised JSON now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0437114e-6078-431f-905b-f9bb77af3527",
  "isSidechain": false,
  "requestId": "req_011Cb5zHkXUWvNtHkMyki1i2",
  "type": "assistant",
  "uuid": "037e469b-822d-463f-a634-171b25a1bf8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MvjhNCA9we25w95Cg6PT8T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1023,
      "cache_read_input_tokens": 44051,
      "output_tokens": 10169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1023,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10169,
          "cache_read_input_tokens": 44051,
          "cache_creation_input_tokens": 1023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1023
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

_source line 62 · 2026-05-16T09:12:20.587Z_

Now I have a thorough understanding of the key issues. Let me synthesize my findings:

**Key research findings:**
1. **PCNet** is indeed very close to GTS — token-level NLL gating + contrastive decoding, corruption rate still 53.7%, preservation 79.3%. MC1 0.51 on Llama-3.1-8B. Tested against ITI/AdaSteer/SADI.
2. **Attractor Geometry** confirmed: uses Euclidean L2 distance explicitly (`δ(x)=min_i ||h(x)−m_i||₂`), measurements at "first-digit position before autoregressive dynamics compound," explicitly disclaims open-domain transfer.
3. **ARR deadline** confirmed May 25, 2026 — exactly 9 days remain.
4. **SENTINEL** does sentence-level intervention but for VLMs via preference learning, not activation steering.

The stagnation at 3.2-3.5 suggests the framing needs a deeper rethink, not just patches. I'll do a **major revision** that recenters the contribution on the granularity mismatch (token-level intervention vs claim-level evaluation), honestly positions the Euclidean foundation, elevates PCNet as a primary competitor, and defines a feasible 9-day scope.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "037e469b-822d-463f-a634-171b25a1bf8c",
  "isSidechain": false,
  "requestId": "req_011Cb5zHkXUWvNtHkMyki1i2",
  "type": "assistant",
  "uuid": "5e4a8888-8d7b-44a7-8e11-6c773319d4be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MvjhNCA9we25w95Cg6PT8T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1023,
      "cache_read_input_tokens": 44051,
      "output_tokens": 10169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1023,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10169,
          "cache_read_input_tokens": 44051,
          "cache_creation_input_tokens": 1023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1023
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

_source line 63 · 2026-05-16T09:15:03.971Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01VjiYqXq5Di3QQ88aP3x3qF`</summary>

````json
{
  "description": "Compose revised research idea JSON",
  "prompt": "You are helping revise a research idea based on detailed reviewer feedback and new research findings. I need you to compose a complete revised JSON object. I'll provide the structure, key changes, and content for each field. Your job is to assemble it into a clean, complete JSON.\n\n**Context**: This is round 6 of revision for a paper on \"Geometry-Triggered Steering\" (GTS) — selective activation steering for hallucination suppression. The idea has stagnated at scores 3.2-3.5 across 3 rounds. Today is May 16, 2026. ARR deadline is May 25 (9 days remain).\n\n**Key changes for this major revision:**\n\n1. **Reframe the core contribution** around the GRANULARITY MISMATCH between token-level intervention and claim-level evaluation, rather than centering on Mahalanobis distance. PCNet's 53.7% corruption rate is concrete evidence that token-level gating still damages correct text.\n\n2. **Elevate PCNet to primary competitor** with full differentiation paragraph.\n\n3. **Honestly position Euclidean→Mahalanobis** as a hypothesized improvement to ablate, not the core contribution.\n\n4. **Add timing hypothesis disclaimer** noting Attractor Geometry paper's explicit limitation.\n\n5. **Define realistic 9-day minimum viable scope.**\n\nHere is the complete JSON to output. Output ONLY the JSON, no other text:\n\n```json\n{\n  \"change_type\": \"major\",\n  \"title\": \"Claim-Level Selective Activation Steering for Factual Hallucination Suppression in Long-Form Generation\",\n  \"core_problem\": \"Factual hallucination in LLMs has spurred a proliferation of geometry-aware detection and activation steering methods, yet a fundamental granularity mismatch persists: detection and intervention operate at token level, while factual evaluation operates at claim/sentence level. PCNet (May 2026) exemplifies this—its probabilistic-circuit gating achieves near-perfect detection AUROC yet still corrupts 53.7% of originally correct generations when intervening at every deviant token, because token-level decisions cannot distinguish 'this token is anomalous within an otherwise correct claim' from 'this claim is genuinely hallucinated.' FASB (NeurIPS 2025) addresses selective steering but operates correctively—detecting deviation after tokens are generated, then backtracking 10 tokens—which wastes compute and splits coherent claims. Spherical Steering (ICML 2026) applies per-token rotation with continuous vMF-gated intensity, achieving strong TruthfulQA gains but intervening indiscriminately across all claims. The Attractor Geometry paper (May 2026) demonstrates that Euclidean geometric margin separates correct recall from hallucination (AUROC 0.858 on TruthfulQA vs. entropy 0.656), but this result is detection-only and measured at first-digit positions on factoid completion—translation into targeted intervention at appropriate granularity during multi-sentence generation remains the open challenge.\",\n  \"opportunity\": \"The unexploited sweet spot is pre-emptive claim-level gating: sentences are the natural unit of factual claims—the granularity FActScore evaluates, the granularity humans judge, and the granularity at which LLMs integrate context before next-sentence planning (supported by 'Think in Sentences,' April 2026). The key evidence that this granularity matters comes from PCNet's results: despite near-perfect token-level detection (AUROC up to 99% on extractive QA), its token-level intervention still corrupts 53.7% of correct generations and preserves only 79.3%. This is because anomaly at individual token positions does not reliably indicate that the entire claim is hallucinated—a high-NLL token may be stylistically unusual but factually correct, or may be part of a partially correct claim that token-level correction damages. A system that makes binary steer/skip decisions at sentence boundaries—preserving entire correct claims untouched while steering only claims where the model lacks factual grounding—can achieve higher preservation rates by avoiding sub-claim intervention entirely. The three-part framework (when: sentence boundaries; whether: geometric distance trigger; how much: per-layer intensity) addresses limitations in all current methods: PCNet's token-level corruption, FASB's corrective backtracking overhead, Spherical Steering's indiscriminate application, and Hallucination Basins' per-sequence uniformity.\",\n  \"landscape\": \"**Selective geometric gating (primary competitors):**\\n\\n*PCNet (arXiv 2605.05953, May 2026)* is the closest concurrent work sharing the 'detect geometric anomaly → selectively intervene' paradigm. PCNet trains a Probabilistic Circuit as a density estimator over MLP-compressed residual stream states (4096→128 dims), computes exact NLL as anomaly score, and triggers PC-LDCD (contrastive decoding) only at deviant tokens. Results: TruthfulQA MC1 0.51 / MC2 0.65 on Llama-3.1-8B; near-perfect detection AUROC on extractive QA; corruption rate 53.7%, preservation rate 79.3%. Overhead: <2% for PC scoring, but 3.3–6.2 additional block evaluations per anomalous token for lookahead. GTS differs in three fundamental ways: (a) Granularity: sentence-level binary decisions preserve entire correct claims and avoid sub-claim corruption. PCNet evaluates NLL at every token, meaning intervention can damage partially correct claims—evidenced by its 53.7% corruption rate despite near-perfect detection. GTS's claim-level atomicity should achieve substantially lower corruption. (b) Intervention mechanism: activation steering shifts the model's own generation distribution toward factual attractors in a single forward pass, while contrastive decoding requires maintaining lookahead evaluations for top-k candidates at every anomalous position (PCNet's IGR ranges 0.41–0.78, meaning lookahead triggers at 41–78% of tokens). On long-form generation where many tokens are flagged, GTS's steering-only approach avoids this per-token lookahead cost. (c) Trigger interpretability: Euclidean/Mahalanobis distance from factual cluster centroids has a clear geometric interpretation (distance in representation space), while NLL from a trained probabilistic circuit is a learned density estimate whose failure modes are less transparent.\\n\\n*FASB (arXiv 2508.17621, NeurIPS 2025)* is the most direct prior work on 'when to steer,' using linear probes trained on attention head activations. It monitors concatenated question-and-generated-content states, triggers intervention when deviation is detected, and backtracks s=10 tokens to regenerate with steering. MC1 48.71% on TruthfulQA (LLaMA-2-7B-Chat). GTS differs in: (a) pre-emptive gating at sentence boundaries (no wasted tokens, no rollback) vs. FASB's corrective backtracking; (b) geometric distance trigger measuring knowledge absence vs. learned directional alignment on attention heads; (c) atomic claim-level decisions vs. token-level cuts that may split coherent claims. FASB's backtracking overhead scales linearly with intervention frequency—compounding on hallucination-dense long-form passages.\\n\\n**Geometry-aware steering (per-token):** Spherical Steering (arXiv 2602.08169, ICML 2026) uses geodesic rotation with a von Mises-Fisher confidence gate, achieving MC1 +15.80% on TruthfulQA (Llama-3.1-8B) with single-layer intervention (layer 24). Code released at github.com/chili-lab/Spherical-Steering. Per-token with continuous intensity—no claim-level selectivity. Hallucination Basins (arXiv 2604.04743, April 2026) proposes Adaptive Geometry-Aware Steering using Euclidean distance triggers and logistic-regression scalar maps at per-sequence granularity (uniform across all claims). Tested on 1B–8B models. GTS advances beyond both via within-sequence sentence-level selectivity.\\n\\n**Context-dependent directions:** Steering Vector Fields (SVF, arXiv 2602.01654, Feb 2026) learns differentiable concept-scoring MLPs for context-aware steering directions refreshed every K steps. Always steers—no gating. Complementary to GTS (GTS decides whether; SVF decides in which direction).\\n\\n**Utility preservation:** COAST (arXiv 2605.01167, May 2026) formalizes collateral damage as unintended feature-direction shifts and optimizes the steering vector via constrained optimization. Complementary to GTS (COAST optimizes the vector; GTS optimizes when to apply it).\\n\\n**Nonlinear geometry:** Curveball Steering (arXiv 2603.09313, March 2026) demonstrates substantial geometric distortion in activation spaces, supporting covariance-aware (Mahalanobis) over Euclidean distance.\\n\\n**Detection-only:** Attractor Geometry of Transformer Memory (arXiv 2605.05686, May 2026) demonstrates hallucination = basin absence with Euclidean geometric margin AUROC 0.858 on TruthfulQA (vs. entropy 0.656), 0.993 on controlled factoid tasks. All measurements at first-digit positions before autoregressive dynamics compound; the paper explicitly states 'transfer to open-domain settings requires further study.' Where Does Reasoning Break? (arXiv 2605.13772, May 2026) detects step-level hallucination via transport geometry. DRIFT (arXiv 2601.14210, Jan 2026) detects representational instability.\\n\\n**Calibration:** Calibrating Verbal Uncertainty (Ji et al., EMNLP 2025 Outstanding Paper) achieves ~31.9% reduction in confident hallucinations via linear-feature intervention—calibrates expression, does not correct generation.\\n\\n**Other steering:** ACT (WWW 2025), ODESteer (ICLR 2026, +5.7% over ACT), Guiding Giants/WAS (arXiv 2505.20309), SADI (arXiv 2410.12299), HELIX/Tethered Reasoning (arXiv 2602.17691). FLAS (arXiv 2605.05892, May 2026) learns concept-conditioned velocity fields for multi-step activation transport.\\n\\n**Supporting evidence:** Hallucination as Trajectory Commitment (arXiv 2604.15400, April 2026) provides causal evidence for early commitment with asymmetric attractor dynamics—supporting timely intervention before commitment propagates. Think in Sentences (arXiv 2604.10135, April 2026) demonstrates sentence boundary attention concentration patterns.\",\n  \"approach\": \"We propose Claim-Level Selective Activation Steering (CLSAS), a method that bridges the granularity gap between token-level detection/intervention and claim-level factual evaluation. The central insight is that intervention granularity should match evaluation granularity: since factuality is assessed per-claim (FActScore, human judgment), steering decisions should be made per-claim—preserving entire correct sentences untouched while steering only sentences where the model lacks factual grounding.\\n\\n**Stage 1: TRIGGER (Geometric Distance at Sentence Boundaries)**\\nDuring generation, at each sentence boundary (period/newline tokens), extract hidden-state activations at the boundary token across layers using nnsight intervention hooks. Compute geometric distance from factual cluster centroids:\\n(a) Offline: From a calibration set (~2K examples from TruthfulQA + FELM correct-answer forward passes), collect hidden states at factual completion positions. Apply PCA to project from full hidden dimension (d=4096) to top-k principal components (k=256), yielding a well-conditioned 256×256 covariance matrix.\\n(b) Online: Project the boundary token's activation into the PCA subspace. Compute distance to nearest factual centroid. We evaluate two distance metrics: (i) Euclidean distance δ_E(x) = ||h_pca − μ_pca||₂, matching the Attractor Geometry paper's validated metric (AUROC 0.858 on TruthfulQA); (ii) Mahalanobis distance δ_M(x) = √((h_pca − μ_pca)ᵀ Σ_pca⁻¹ (h_pca − μ_pca)), a hypothesized improvement motivated by OOD detection literature (Lee et al., NeurIPS 2018) that accounts for directional anisotropy in representation space.\\n(c) When distance exceeds a calibrated threshold (set via precision-recall analysis targeting high precision ≥0.85 to minimize false interventions), flag the upcoming sentence for steering.\\n\\n**Critical clarification:** The 0.858 AUROC motivating this trigger was achieved with Euclidean distance on first-digit positions during factoid completion (Attractor Geometry, May 2026). Our application to sentence boundaries during multi-sentence open-ended generation is an extrapolation that we explicitly validate as Milestone 1. The Attractor Geometry authors note 'transfer to open-domain settings requires further study.' If Mahalanobis does not significantly outperform Euclidean in our ablation, the primary novelty contribution rests on claim-level selective gating itself—which remains differentiated from all baselines regardless of distance metric.\\n\\n**Timing Hypothesis Validation (Milestone 1, Days 1-2):**\\nWe explicitly frame the following as a testable hypothesis: geometric distance at sentence boundary N is predictive of factual accuracy in sentence N+1. Validation protocol: (1) Generate 500 multi-sentence responses on LongFact/FActScore prompts using Llama-3.1-8B-Instruct. (2) Compute both Euclidean and Mahalanobis distance at every sentence boundary. (3) Annotate each subsequent sentence with FActScore. (4) Measure Spearman correlation between boundary distance and next-sentence factuality, and AUROC for binary classification. If AUROC < 0.70, we implement a look-ahead variant: extract distance from the first 3 generated tokens of the new sentence (before committing via speculative-style buffering). The look-ahead variant adds ~15% latency overhead but operates before the sentence is visible to the user. If look-ahead also fails (AUROC < 0.65), we fall back to a sliding-window approach using the mean distance over the last 5 tokens before the boundary.\\n\\n**Comparison to PCNet's trigger:** PCNet uses NLL from a trained probabilistic circuit as its anomaly score, evaluated at every token. This achieves near-perfect detection on extractive QA but still yields 53.7% corruption on correct generations. We hypothesize this is because token-level anomaly conflates stylistic deviation with factual error. Our sentence-level trigger aggregates geometric information at natural claim boundaries, making a single binary decision per claim—either the model has factual grounding for this claim (skip) or it doesn't (steer). This avoids sub-claim intervention entirely.\\n\\n**Stage 2: DIRECTION (Centroid-Directed Steering Vector)**\\nCompute the steering direction as the unit vector from the current activation toward the factual cluster centroid at each layer in the PCA subspace, then project back to full space: v_steer = (μ_pca − h_pca) / ||μ_pca − h_pca||, lifted back to full dimensionality via PCA inverse transform. This yields an input-specific correction direction toward regions of successful fact recall.\\n\\n**Stage 3: INTENSITY (Per-Layer Weighted Steering)**\\nA lightweight 2-layer MLP controller (hidden dim 64, inspired by Guiding Giants/WAS) takes [geometric_distance, layer_index/L, distance_velocity] as input (3D feature vector) and predicts per-layer steering weight λ_ℓ. Trained on a calibration set (~2K examples) to maximize FActScore on steered outputs while minimizing perplexity increase on non-flagged outputs. Steering: h_steered(ℓ) = h(ℓ) + λ_ℓ · v_steer(ℓ) at layers where λ_ℓ > ε.\\n\\n**Minimum Viable Scope (9 days, May 16–25):**\\n- Days 1-2 (May 16-17): Timing hypothesis validation on Llama-3.1-8B-Instruct. This is the critical-path milestone—if it fails, immediately implement look-ahead variant.\\n- Days 3-4 (May 18-19): Core CLSAS implementation + calibration. Run TruthfulQA and SimpleQA.\\n- Days 5-6 (May 20-21): Run baselines (Spherical Steering from released code, FASB from released code). Run FActScore and MT-Bench on CLSAS.\\n- Days 7-8 (May 22-23): Key ablations: 2×2 grid (Euclidean vs Mahalanobis × sentence-level vs token-level gating) on 4-benchmark core set. PCNet comparison if code is available; otherwise use reported numbers with matched model.\\n- Day 9 (May 24): Writing, formatting, submission buffer.\\n- Dropped from scope: COAST combination experiment, Qwen3-8B (secondary model), full 7-benchmark suite for ablations, GTS-FASB-trigger ablation.\\n\\n**Ablation Design (MVP):**\\n- CLSAS-full vs. CLSAS-Euclidean (isolate Mahalanobis contribution)\\n- CLSAS-full vs. CLSAS-pertoken (apply continuous per-token gating with our distance metric, matching PCNet/Spherical Steering's granularity—isolates the claim-level contribution)\\n- CLSAS-full vs. CLSAS-sequence (single decision per sequence, matching Hallucination Basins' granularity)\\n- CLSAS-full vs. CLSAS-scalar (replace per-layer MLP with single scalar, isolating controller contribution)\\n- Direct comparison: CLSAS-full vs. Spherical Steering vs. FASB vs. PCNet (reported numbers if code unavailable)\\n\\n**Primary evaluation metrics:**\\n- Corruption rate and preservation rate (matching PCNet's protocol): fraction of correct claims degraded / preserved by intervention\\n- FActScore on long-form biographies (primary benchmark where claim-level advantage should be largest)\\n- TruthfulQA MC1/MC2, SimpleQA accuracy, MT-Bench score\\n- Intervention rate: fraction of sentences steered (lower is better for comparable factuality gains)\\n- Latency overhead vs. baselines\\n\\nImplementation uses nnsight 0.7 on Llama-3.1-8B-Instruct. Qwen3-8B included only if time permits after MVP completion.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~120h H100 80GB\",\n      \"gpu_utilization\": \"Low (~15-20%)\",\n      \"timeline\": \"3-4 months\",\n      \"team\": \"1-2 researchers with mechanistic interpretability + geometric ML experience\",\n      \"estimated_gpu_cost\": \"$360-400\",\n      \"factScore_api_cost\": \"$100-200\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~130h H100 80GB\",\n      \"gpu_utilization\": \"Moderate (45-55%)\",\n      \"timeline\": \"2-3 weeks\",\n      \"team\": \"1 researcher, ~30min/day reviewing proposals\",\n      \"claude_api_cost\": \"$150-250\",\n      \"estimated_gpu_cost\": \"$390-430\",\n      \"factScore_api_cost\": \"$100-200\",\n      \"risk_note\": \"Timing hypothesis validation is critical-path. If it fails (AUROC < 0.70), look-ahead fallback adds ~3 days.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~140h H100 80GB\",\n      \"gpu_utilization\": \"High (~85-90%)\",\n      \"timeline\": \"9 days (May 16-25) with 2 H100 GPUs. Minimum viable paper scope: single model (Llama-3.1-8B), 4-benchmark core set for ablations, full baselines on FActScore+TruthfulQA+SimpleQA+MT-Bench.\",\n      \"team\": \"0 (initial setup: provision GPUs, configure nnsight 0.7, clone Spherical Steering + FASB repos)\",\n      \"claude_api_cost\": \"$250-350 (est. 3000-4000 turns)\",\n      \"estimated_gpu_cost\": \"$420-450\",\n      \"factScore_api_cost\": \"$100-200\",\n      \"speed_bottleneck\": \"Timing hypothesis validation (days 1-2) is critical path. If it fails, look-ahead variant must be implemented immediately. Secondary: FActScore GPT-4 API calls.\",\n      \"resource_optimization\": \"Budget achieved via: (1) single model (Llama-3.1-8B) for all experiments; (2) 4-benchmark core set (TruthfulQA, FActScore, SimpleQA, MT-Bench); (3) 2×2 ablation grid (distance metric × gating granularity) instead of separate sweeps; (4) use Spherical Steering and FASB released code directly; (5) PCNet comparison using reported numbers if code unavailable.\",\n      \"minimum_viable_paper\": \"If timing hypothesis fails AND look-ahead also fails: pivot to a detection-only contribution (sentence-level geometric detection benchmark) comparing Euclidean/Mahalanobis at sentence boundaries vs. PCNet's token-level NLL. This is publishable as a shorter paper (findings track).\",\n      \"risk_note\": \"Primary risk: timing hypothesis may fail (Attractor Geometry paper validated only on factoid completion at first-digit positions, explicitly disclaiming open-domain transfer). Mitigation: look-ahead variant, then sliding-window fallback. Secondary risk: claim-level gating may not outperform PCNet's token-level gating on short-form QA—advantage expected primarily on long-form generation (FActScore, LongFact). Tertiary risk: 9-day timeline leaves zero buffer for unexpected implementation issues.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits (PCNet, arXiv 2605.05953, May 2026)\",\n    \"Steering When Necessary: Flexible Steering Large Language Models with Backtracking (FASB, arXiv 2508.17621, NeurIPS 2025)\",\n    \"Spherical Steering: Geometry-Aware Activation Rotation for Language Models (arXiv 2602.08169, ICML 2026)\",\n    \"Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination (arXiv 2605.05686, May 2026)\",\n    \"Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations (arXiv 2604.04743, April 2026)\",\n    \"Steering Vector Fields for Context-Aware Inference-Time Control in Large Language Models (SVF, arXiv 2602.01654, Feb 2026)\",\n    \"Curveball Steering: The Right Direction To Steer Isn't Always Linear (arXiv 2603.09313, March 2026)\",\n    \"Minimizing Collateral Damage in Activation Steering (COAST, arXiv 2605.01167, May 2026)\",\n    \"Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention (FLAS, arXiv 2605.05892, May 2026)\",\n    \"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025 Outstanding Paper, arXiv 2503.14477)\",\n    \"Tethered Reasoning (HELIX): Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering (arXiv 2602.17691, Feb 2026)\",\n    \"Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method (ACT, WWW 2025)\",\n    \"ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment (ICLR 2026, arXiv 2602.17560)\",\n    \"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (arXiv 2605.13772, May 2026)\",\n    \"DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness (arXiv 2601.14210, Jan 2026)\",\n    \"Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs (arXiv 2505.20309, May 2025)\",\n    \"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics (arXiv 2604.15400, April 2026)\",\n    \"Think in Sentences: Explicit Sentence Boundaries Enhance Language Model's Capabilities (arXiv 2604.10135, April 2026)\",\n    \"A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks (Lee et al., NeurIPS 2018)\",\n    \"Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors (SADI, arXiv 2410.12299, 2024)\",\n    \"Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models (ICLR 2026)\"\n  ],\n  \"description\": \"We propose Claim-Level Selective Activation Steering (CLSAS), a method that bridges the granularity gap between token-level hallucination detection/intervention and claim-level factual evaluation. The central insight is that intervention granularity should match evaluation granularity: since factuality is assessed per-claim (FActScore, human judgment), steering decisions should be per-claim—preserving entire correct sentences untouched while steering only claims where the model lacks factual grounding.\\n\\nThe motivation is concrete: PCNet (May 2026), the state-of-the-art in selective geometric gating, achieves near-perfect token-level hallucination detection (AUROC up to 99% on extractive QA) yet still corrupts 53.7% of originally correct generations when intervening token-by-token via contrastive decoding. We hypothesize this corruption stems from the granularity mismatch—token-level anomaly conflates stylistic deviation with factual error, and sub-claim interventions damage partially correct claims.\\n\\nCLSAS monitors geometric distance from residual stream activations to factual cluster centroids at sentence boundaries during generation. Building on the finding that Euclidean geometric margin separates correct recall from hallucination (AUROC 0.858 on TruthfulQA; Attractor Geometry, May 2026), we evaluate both Euclidean and Mahalanobis distance triggers—the latter a hypothesized improvement motivated by OOD detection literature (Lee et al., NeurIPS 2018) that we validate via ablation. When distance indicates basin absence, CLSAS computes an input-specific steering vector toward the factual centroid and applies it with per-layer weights from a lightweight MLP controller. Sentences within a factual basin are left entirely untouched.\\n\\nCLSAS addresses limitations in the closest concurrent work: (1) vs. PCNet (May 2026, MC1 0.51 on Llama-3.1-8B), CLSAS makes sentence-level binary decisions that avoid sub-claim corruption. PCNet's token-level NLL gating triggers at 41-78% of tokens (IGR), requiring costly lookahead evaluations at each; CLSAS intervenes only at sentence boundaries. (2) vs. FASB (NeurIPS 2025, MC1 48.71% on LLaMA-2-7B-Chat), CLSAS is pre-emptive—gating before generation rather than detecting deviation and rolling back 10 tokens. (3) vs. Spherical Steering (ICML 2026, +15% MC1), CLSAS makes binary claim-level steer/skip decisions rather than continuous per-token rotation, enabling complete preservation of correct claims. (4) vs. Hallucination Basins (April 2026), CLSAS provides within-sequence selectivity rather than uniform per-sequence correction.\\n\\nWe explicitly validate the timing hypothesis (distance at boundary N predicts factuality of sentence N+1) as Milestone 1 with a correlation study, noting the Attractor Geometry paper's disclaimer that results were measured at first-digit positions and 'transfer to open-domain settings requires further study.' A look-ahead fallback is specified if correlation is insufficient. We hypothesize CLSAS's advantage over token-level methods will be strongest on long-form generation (FActScore) where multiple claims coexist and token-level corruption compounds.\\n\\nMinimum viable scope for 9 remaining days: single model (Llama-3.1-8B-Instruct), 4-benchmark evaluation (TruthfulQA, FActScore, SimpleQA, MT-Bench), 2×2 ablation grid (distance metric × gating granularity), direct comparison with Spherical Steering and FASB using released code. Total budget: ≤140 H100-hours.\",\n  \"project_name\": \"claim_level_selective_steering\",\n  \"source\": \"web_research\"\n}\n```\n\nPlease output this JSON exactly as provided, ensuring it is valid JSON. Do not add any text before or after the JSON.\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e4a8888-8d7b-44a7-8e11-6c773319d4be",
  "isSidechain": false,
  "requestId": "req_011Cb5zHkXUWvNtHkMyki1i2",
  "type": "assistant",
  "uuid": "88e4fe58-55d5-4874-847a-61b3e11849a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MvjhNCA9we25w95Cg6PT8T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1023,
      "cache_read_input_tokens": 44051,
      "output_tokens": 10169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1023,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10169,
          "cache_read_input_tokens": 44051,
          "cache_creation_input_tokens": 1023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1023
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

_source line 64_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-16 (UTC).**  ## Original idea {   \"title\": \"Geometry-Triggered Sentence-Level Activation Steering for Factual Hall…",
  "leafUuid": "88e4fe58-55d5-4874-847a-61b3e11849a1",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c"
}
```

---

### Runtime record

_source line 65_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise GTS with PCNet differentiation and realistic timeline",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c"
}
```

---

### Tool result

_source line 66 · 2026-05-16T09:16:50.739Z_

<details><summary>↩ Tool result · `toolu_01VjiYqXq5Di3QQ88aP3x3qF`</summary>

````text


```json
{
  "change_type": "major",
  "title": "Claim-Level Selective Activation Steering for Factual Hallucination Suppression in Long-Form Generation",
  "core_problem": "Factual hallucination in LLMs has spurred a proliferation of geometry-aware detection and activation steering methods, yet a fundamental granularity mismatch persists: detection and intervention operate at token level, while factual evaluation operates at claim/sentence level. PCNet (May 2026) exemplifies this—its probabilistic-circuit gating achieves near-perfect detection AUROC yet still corrupts 53.7% of originally correct generations when intervening at every deviant token, because token-level decisions cannot distinguish 'this token is anomalous within an otherwise correct claim' from 'this claim is genuinely hallucinated.' FASB (NeurIPS 2025) addresses selective steering but operates correctively—detecting deviation after tokens are generated, then backtracking 10 tokens—which wastes compute and splits coherent claims. Spherical Steering (ICML 2026) applies per-token rotation with continuous vMF-gated intensity, achieving strong TruthfulQA gains but intervening indiscriminately across all claims. The Attractor Geometry paper (May 2026) demonstrates that Euclidean geometric margin separates correct recall from hallucination (AUROC 0.858 on TruthfulQA vs. entropy 0.656), but this result is detection-only and measured at first-digit positions on factoid completion—translation into targeted intervention at appropriate granularity during multi-sentence generation remains the open challenge.",
  "opportunity": "The unexploited sweet spot is pre-emptive claim-level gating: sentences are the natural unit of factual claims—the granularity FActScore evaluates, the granularity humans judge, and the granularity at which LLMs integrate context before next-sentence planning (supported by 'Think in Sentences,' April 2026). The key evidence that this granularity matters comes from PCNet's results: despite near-perfect token-level detection (AUROC up to 99% on extractive QA), its token-level intervention still corrupts 53.7% of correct generations and preserves only 79.3%. This is because anomaly at individual token positions does not reliably indicate that the entire claim is hallucinated—a high-NLL token may be stylistically unusual but factually correct, or may be part of a partially correct claim that token-level correction damages. A system that makes binary steer/skip decisions at sentence boundaries—preserving entire correct claims untouched while steering only claims where the model lacks factual grounding—can achieve higher preservation rates by avoiding sub-claim intervention entirely. The three-part framework (when: sentence boundaries; whether: geometric distance trigger; how much: per-layer intensity) addresses limitations in all current methods: PCNet's token-level corruption, FASB's corrective backtracking overhead, Spherical Steering's indiscriminate application, and Hallucination Basins' per-sequence uniformity.",
  "landscape": "**Selective geometric gating (primary competitors):**\n\n*PCNet (arXiv 2605.05953, May 2026)* is the closest concurrent work sharing the 'detect geometric anomaly → selectively intervene' paradigm. PCNet trains a Probabilistic Circuit as a density estimator over MLP-compressed residual stream states (4096→128 dims), computes exact NLL as anomaly score, and triggers PC-LDCD (contrastive decoding) only at deviant tokens. Results: TruthfulQA MC1 0.51 / MC2 0.65 on Llama-3.1-8B; near-perfect detection AUROC on extractive QA; corruption rate 53.7%, preservation rate 79.3%. Overhead: <2% for PC scoring, but 3.3–6.2 additional block evaluations per anomalous token for lookahead. GTS differs in three fundamental ways: (a) Granularity: sentence-level binary decisions preserve entire correct claims and avoid sub-claim corruption. PCNet evaluates NLL at every token, meaning intervention can damage partially correct claims—evidenced by its 53.7% corruption rate despite near-perfect detection. GTS's claim-level atomicity should achieve substantially lower corruption. (b) Intervention mechanism: activation steering shifts the model's own generation distribution toward factual attractors in a single forward pass, while contrastive decoding requires maintaining lookahead evaluations for top-k candidates at every anomalous position (PCNet's IGR ranges 0.41–0.78, meaning lookahead triggers at 41–78% of tokens). On long-form generation where many tokens are flagged, GTS's steering-only approach avoids this per-token lookahead cost. (c) Trigger interpretability: Euclidean/Mahalanobis distance from factual cluster centroids has a clear geometric interpretation (distance in representation space), while NLL from a trained probabilistic circuit is a learned density estimate whose failure modes are less transparent.\n\n*FASB (arXiv 2508.17621, NeurIPS 2025)* is the most direct prior work on 'when to steer,' using linear probes trained on attention head activations. It monitors concatenated question-and-generated-content states, triggers intervention when deviation is detected, and backtracks s=10 tokens to regenerate with steering. MC1 48.71% on TruthfulQA (LLaMA-2-7B-Chat). GTS differs in: (a) pre-emptive gating at sentence boundaries (no wasted tokens, no rollback) vs. FASB's corrective backtracking; (b) geometric distance trigger measuring knowledge absence vs. learned directional alignment on attention heads; (c) atomic claim-level decisions vs. token-level cuts that may split coherent claims. FASB's backtracking overhead scales linearly with intervention frequency—compounding on hallucination-dense long-form passages.\n\n**Geometry-aware steering (per-token):** Spherical Steering (arXiv 2602.08169, ICML 2026) uses geodesic rotation with a von Mises-Fisher confidence gate, achieving MC1 +15.80% on TruthfulQA (Llama-3.1-8B) with single-layer intervention (layer 24). Code released at github.com/chili-lab/Spherical-Steering. Per-token with continuous intensity—no claim-level selectivity. Hallucination Basins (arXiv 2604.04743, April 2026) proposes Adaptive Geometry-Aware Steering using Euclidean distance triggers and logistic-regression scalar maps at per-sequence granularity (uniform across all claims). Tested on 1B–8B models. GTS advances beyond both via within-sequence sentence-level selectivity.\n\n**Context-dependent directions:** Steering Vector Fields (SVF, arXiv 2602.01654, Feb 2026) learns differentiable concept-scoring MLPs for context-aware steering directions refreshed every K steps. Always steers—no gating. Complementary to GTS (GTS decides whether; SVF decides in which direction).\n\n**Utility preservation:** COAST (arXiv 2605.01167, May 2026) formalizes collateral damage as unintended feature-direction shifts and optimizes the steering vector via constrained optimization. Complementary to GTS (COAST optimizes the vector; GTS optimizes when to apply it).\n\n**Nonlinear geometry:** Curveball Steering (arXiv 2603.09313, March 2026) demonstrates substantial geometric distortion in activation spaces, supporting covariance-aware (Mahalanobis) over Euclidean distance.\n\n**Detection-only:** Attractor Geometry of Transformer Memory (arXiv 2605.05686, May 2026) demonstrates hallucination = basin absence with Euclidean geometric margin AUROC 0.858 on TruthfulQA (vs. entropy 0.656), 0.993 on controlled factoid tasks. All measurements at first-digit positions before autoregressive dynamics compound; the paper explicitly states 'transfer to open-domain settings requires further study.' Where Does Reasoning Break? (arXiv 2605.13772, May 2026) detects step-level hallucination via transport geometry. DRIFT (arXiv 2601.14210, Jan 2026) detects representational instability.\n\n**Calibration:** Calibrating Verbal Uncertainty (Ji et al., EMNLP 2025 Outstanding Paper) achieves ~31.9% reduction in confident hallucinations via linear-feature intervention—calibrates expression, does not correct generation.\n\n**Other steering:** ACT (WWW 2025), ODESteer (ICLR 2026, +5.7% over ACT), Guiding Giants/WAS (arXiv 2505.20309), SADI (arXiv 2410.12299), HELIX/Tethered Reasoning (arXiv 2602.17691). FLAS (arXiv 2605.05892, May 2026) learns concept-conditioned velocity fields for multi-step activation transport.\n\n**Supporting evidence:** Hallucination as Trajectory Commitment (arXiv 2604.15400, April 2026) provides causal evidence for early commitment with asymmetric attractor dynamics—supporting timely intervention before commitment propagates. Think in Sentences (arXiv 2604.10135, April 2026) demonstrates sentence boundary attention concentration patterns.",
  "approach": "We propose Claim-Level Selective Activation Steering (CLSAS), a method that bridges the granularity gap between token-level detection/intervention and claim-level factual evaluation. The central insight is that intervention granularity should match evaluation granularity: since factuality is assessed per-claim (FActScore, human judgment), steering decisions should be made per-claim—preserving entire correct sentences untouched while steering only sentences where the model lacks factual grounding.\n\n**Stage 1: TRIGGER (Geometric Distance at Sentence Boundaries)**\nDuring generation, at each sentence boundary (period/newline tokens), extract hidden-state activations at the boundary token across layers using nnsight intervention hooks. Compute geometric distance from factual cluster centroids:\n(a) Offline: From a calibration set (~2K examples from TruthfulQA + FELM correct-answer forward passes), collect hidden states at factual completion positions. Apply PCA to project from full hidden dimension (d=4096) to top-k principal components (k=256), yielding a well-conditioned 256×256 covariance matrix.\n(b) Online: Project the boundary token's activation into the PCA subspace. Compute distance to nearest factual centroid. We evaluate two distance metrics: (i) Euclidean distance δ_E(x) = ||h_pca − μ_pca||₂, matching the Attractor Geometry paper's validated metric (AUROC 0.858 on TruthfulQA); (ii) Mahalanobis distance δ_M(x) = √((h_pca − μ_pca)ᵀ Σ_pca⁻¹ (h_pca − μ_pca)), a hypothesized improvement motivated by OOD detection literature (Lee et al., NeurIPS 2018) that accounts for directional anisotropy in representation space.\n(c) When distance exceeds a calibrated threshold (set via precision-recall analysis targeting high precision ≥0.85 to minimize false interventions), flag the upcoming sentence for steering.\n\n**Critical clarification:** The 0.858 AUROC motivating this trigger was achieved with Euclidean distance on first-digit positions during factoid completion (Attractor Geometry, May 2026). Our application to sentence boundaries during multi-sentence open-ended generation is an extrapolation that we explicitly validate as Milestone 1. The Attractor Geometry authors note 'transfer to open-domain settings requires further study.' If Mahalanobis does not significantly outperform Euclidean in our ablation, the primary novelty contribution rests on claim-level selective gating itself—which remains differentiated from all baselines regardless of distance metric.\n\n**Timing Hypothesis Validation (Milestone 1, Days 1-2):**\nWe explicitly frame the following as a testable hypothesis: geometric distance at sentence boundary N is predictive of factual accuracy in sentence N+1. Validation protocol: (1) Generate 500 multi-sentence responses on LongFact/FActScore prompts using Llama-3.1-8B-Instruct. (2) Compute both Euclidean and Mahalanobis distance at every sentence boundary. (3) Annotate each subsequent sentence with FActScore. (4) Measure Spearman correlation between boundary distance and next-sentence factuality, and AUROC for binary classification. If AUROC < 0.70, we implement a look-ahead variant: extract distance from the first 3 generated tokens of the new sentence (before committing via speculative-style buffering). The look-ahead variant adds ~15% latency overhead but operates before the sentence is visible to the user. If look-ahead also fails (AUROC < 0.65), we fall back to a sliding-window approach using the mean distance over the last 5 tokens before the boundary.\n\n**Comparison to PCNet's trigger:** PCNet uses NLL from a trained probabilistic circuit as its anomaly score, evaluated at every token. This achieves near-perfect detection on extractive QA but still yields 53.7% corruption on correct generations. We hypothesize this is because token-level anomaly conflates stylistic deviation with factual error. Our sentence-level trigger aggregates geometric information at natural claim boundaries, making a single binary decision per claim—either the model has factual grounding for this claim (skip) or it doesn't (steer). This avoids sub-claim intervention entirely.\n\n**Stage 2: DIRECTION (Centroid-Directed Steering Vector)**\nCompute the steering direction as the unit vector from the current activation toward the factual cluster centroid at each layer in the PCA subspace, then project back to full space: v_steer = (μ_pca − h_pca) / ||μ_pca − h_pca||, lifted back to full dimensionality via PCA inverse transform. This yields an input-specific correction direction toward regions of successful fact recall.\n\n**Stage 3: INTENSITY (Per-Layer Weighted Steering)**\nA lightweight 2-layer MLP controller (hidden dim 64, inspired by Guiding Giants/WAS) takes [geometric_distance, layer_index/L, distance_velocity] as input (3D feature vector) and predicts per-layer steering weight λ_ℓ. Trained on a calibration set (~2K examples) to maximize FActScore on steered outputs while minimizing perplexity increase on non-flagged outputs. Steering: h_steered(ℓ) = h(ℓ) + λ_ℓ · v_steer(ℓ) at layers where λ_ℓ > ε.\n\n**Minimum Viable Scope (9 days, May 16–25):**\n- Days 1-2 (May 16-17): Timing hypothesis validation on Llama-3.1-8B-Instruct. This is the critical-path milestone—if it fails, immediately implement look-ahead variant.\n- Days 3-4 (May 18-19): Core CLSAS implementation + calibration. Run TruthfulQA and SimpleQA.\n- Days 5-6 (May 20-21): Run baselines (Spherical Steering from released code, FASB from released code). Run FActScore and MT-Bench on CLSAS.\n- Days 7-8 (May 22-23): Key ablations: 2×2 grid (Euclidean vs Mahalanobis × sentence-level vs token-level gating) on 4-benchmark core set. PCNet comparison if code is available; otherwise use reported numbers with matched model.\n- Day 9 (May 24): Writing, formatting, submission buffer.\n- Dropped from scope: COAST combination experiment, Qwen3-8B (secondary model), full 7-benchmark suite for ablations, GTS-FASB-trigger ablation.\n\n**Ablation Design (MVP):**\n- CLSAS-full vs. CLSAS-Euclidean (isolate Mahalanobis contribution)\n- CLSAS-full vs. CLSAS-pertoken (apply continuous per-token gating with our distance metric, matching PCNet/Spherical Steering's granularity—isolates the claim-level contribution)\n- CLSAS-full vs. CLSAS-sequence (single decision per sequence, matching Hallucination Basins' granularity)\n- CLSAS-full vs. CLSAS-scalar (replace per-layer MLP with single scalar, isolating controller contribution)\n- Direct comparison: CLSAS-full vs. Spherical Steering vs. FASB vs. PCNet (reported numbers if code unavailable)\n\n**Primary evaluation metrics:**\n- Corruption rate and preservation rate (matching PCNet's protocol): fraction of correct claims degraded / preserved by intervention\n- FActScore on long-form biographies (primary benchmark where claim-level advantage should be largest)\n- TruthfulQA MC1/MC2, SimpleQA accuracy, MT-Bench score\n- Intervention rate: fraction of sentences steered (lower is better for comparable factuality gains)\n- Latency overhead vs. baselines\n\nImplementation uses nnsight 0.7 on Llama-3.1-8B-Instruct. Qwen3-8B included only if time permits after MVP completion.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~120h H100 80GB",
      "gpu_utilization": "Low (~15-20%)",
      "timeline": "3-4 months",
      "team": "1-2 researchers with mechanistic interpretability + geometric ML experience",
      "estimated_gpu_cost": "$360-400",
      "factScore_api_cost": "$100-200"
    },
    "human_in_loop": {
      "gpu_hours": "~130h H100 80GB",
      "gpu_utilization": "Moderate (45-55%)",
      "timeline": "2-3 weeks",
      "team": "1 researcher, ~30min/day reviewing proposals",
      "claude_api_cost": "$150-250",
      "estimated_gpu_cost": "$390-430",
      "factScore_api_cost": "$100-200",
      "risk_note": "Timing hypothesis validation is critical-path. If it fails (AUROC < 0.70), look-ahead fallback adds ~3 days."
    },
    "auto_research": {
      "gpu_hours": "~140h H100 80GB",
      "gpu_utilization": "High (~85-90%)",
      "timeline": "9 days (May 16-25) with 2 H100 GPUs. Minimum viable paper scope: single model (Llama-3.1-8B), 4-benchmark core set for ablations, full baselines on FActScore+TruthfulQA+SimpleQA+MT-Bench.",
      "team": "0 (initial setup: provision GPUs, configure nnsight 0.7, clone Spherical Steering + FASB repos)",
      "claude_api_cost": "$250-350 (est. 3000-4000 turns)",
      "estimated_gpu_cost": "$420-450",
      "factScore_api_cost": "$100-200",
      "speed_bottleneck": "Timing hypothesis validation (days 1-2) is critical path. If it fails, look-ahead variant must be implemented immediately. Secondary: FActScore GPT-4 API calls.",
      "resource_optimization": "Budget achieved via: (1) single model (Llama-3.1-8B) for all experiments; (2) 4-benchmark core set (TruthfulQA, FActScore, SimpleQA, MT-Bench); (3) 2×2 ablation grid (distance metric × gating granularity) instead of separate sweeps; (4) use Spherical Steering and FASB released code directly; (5) PCNet comparison using reported numbers if code unavailable.",
      "minimum_viable_paper": "If timing hypothesis fails AND look-ahead also fails: pivot to a detection-only contribution (sentence-level geometric detection benchmark) comparing Euclidean/Mahalanobis at sentence boundaries vs. PCNet's token-level NLL. This is publishable as a shorter paper (findings track).",
      "risk_note": "Primary risk: timing hypothesis may fail (Attractor Geometry paper validated only on factoid completion at first-digit positions, explicitly disclaiming open-domain transfer). Mitigation: look-ahead variant, then sliding-window fallback. Secondary risk: claim-level gating may not outperform PCNet's token-level gating on short-form QA—advantage expected primarily on long-form generation (FActScore, LongFact). Tertiary risk: 9-day timeline leaves zero buffer for unexpected implementation issues."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026)"
  ],
  "level": "top-tier",
  "key_references": [
    "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits (PCNet, arXiv 2605.05953, May 2026)",
    "Steering When Necessary: Flexible Steering Large Language Models with Backtracking (FASB, arXiv 2508.17621, NeurIPS 2025)",
    "Spherical Steering: Geometry-Aware Activation Rotation for Language Models (arXiv 2602.08169, ICML 2026)",
    "Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination (arXiv 2605.05686, May 2026)",
    "Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations (arXiv 2604.04743, April 2026)",
    "Steering Vector Fields for Context-Aware Inference-Time Control in Large Language Models (SVF, arXiv 2602.01654, Feb 2026)",
    "Curveball Steering: The Right Direction To Steer Isn't Always Linear (arXiv 2603.09313, March 2026)",
    "Minimizing Collateral Damage in Activation Steering (COAST, arXiv 2605.01167, May 2026)",
    "Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention (FLAS, arXiv 2605.05892, May 2026)",
    "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025 Outstanding Paper, arXiv 2503.14477)",
    "Tethered Reasoning (HELIX): Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering (arXiv 2602.17691, Feb 2026)",
    "Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method (ACT, WWW 2025)",
    "ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment (ICLR 2026, arXiv 2602.17560)",
    "Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (arXiv 2605.13772, May 2026)",
    "DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness (arXiv 2601.14210, Jan 2026)",
    "Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs (arXiv 2505.20309, May 2025)",
    "Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics (arXiv 2604.15400, April 2026)",
    "Think in Sentences: Explicit Sentence Boundaries Enhance Language Model's Capabilities (arXiv 2604.10135, April 2026)",
    "A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks (Lee et al., NeurIPS 2018)",
    "Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors (SADI, arXiv 2410.12299, 2024)",
    "Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models (ICLR 2026)"
  ],
  "description": "We propose Claim-Level Selective Activation Steering (CLSAS), a method that bridges the granularity gap between token-level hallucination detection/intervention and claim-level factual evaluation. The central insight is that intervention granularity should match evaluation granularity: since factuality is assessed per-claim (FActScore, human judgment), steering decisions should be per-claim—preserving entire correct sentences untouched while steering only claims where the model lacks factual grounding.\n\nThe motivation is concrete: PCNet (May 2026), the state-of-the-art in selective geometric gating, achieves near-perfect token-level hallucination detection (AUROC up to 99% on extractive QA) yet still corrupts 53.7% of originally correct generations when intervening token-by-token via contrastive decoding. We hypothesize this corruption stems from the granularity mismatch—token-level anomaly conflates stylistic deviation with factual error, and sub-claim interventions damage partially correct claims.\n\nCLSAS monitors geometric distance from residual stream activations to factual cluster centroids at sentence boundaries during generation. Building on the finding that Euclidean geometric margin separates correct recall from hallucination (AUROC 0.858 on TruthfulQA; Attractor Geometry, May 2026), we evaluate both Euclidean and Mahalanobis distance triggers—the latter a hypothesized improvement motivated by OOD detection literature (Lee et al., NeurIPS 2018) that we validate via ablation. When distance indicates basin absence, CLSAS computes an input-specific steering vector toward the factual centroid and applies it with per-layer weights from a lightweight MLP controller. Sentences within a factual basin are left entirely untouched.\n\nCLSAS addresses limitations in the closest concurrent work: (1) vs. PCNet (May 2026, MC1 0.51 on Llama-3.1-8B), CLSAS makes sentence-level binary decisions that avoid sub-claim corruption. PCNet's token-level NLL gating triggers at 41-78% of tokens (IGR), requiring costly lookahead evaluations at each; CLSAS intervenes only at sentence boundaries. (2) vs. FASB (NeurIPS 2025, MC1 48.71% on LLaMA-2-7B-Chat), CLSAS is pre-emptive—gating before generation rather than detecting deviation and rolling back 10 tokens. (3) vs. Spherical Steering (ICML 2026, +15% MC1), CLSAS makes binary claim-level steer/skip decisions rather than continuous per-token rotation, enabling complete preservation of correct claims. (4) vs. Hallucination Basins (April 2026), CLSAS provides within-sequence selectivity rather than uniform per-sequence correction.\n\nWe explicitly validate the timing hypothesis (distance at boundary N predicts factuality of sentence N+1) as Milestone 1 with a correlation study, noting the Attractor Geometry paper's disclaimer that results were measured at first-digit positions and 'transfer to open-domain settings requires further study.' A look-ahead fallback is specified if correlation is insufficient. We hypothesize CLSAS's advantage over token-level methods will be strongest on long-form generation (FActScore) where multiple claims coexist and token-level corruption compounds.\n\nMinimum viable scope for 9 remaining days: single model (Llama-3.1-8B-Instruct), 4-benchmark evaluation (TruthfulQA, FActScore, SimpleQA, MT-Bench), 2×2 ablation grid (distance metric × gating granularity), direct comparison with Spherical Steering and FASB using released code. Total budget: ≤140 H100-hours.",
  "project_name": "claim_level_selective_steering",
  "source": "web_research"
}
```

agentId: ace13499b3290f5f7 (use SendMessage with to: 'ace13499b3290f5f7' to continue this agent)
&lt;usage>total_tokens: 23101
tool_uses: 0
duration_ms: 106759&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "88e4fe58-55d5-4874-847a-61b3e11849a1",
  "isSidechain": false,
  "promptId": "6c31b04f-5b26-44ca-b486-31fab11de0b0",
  "type": "user",
  "uuid": "88b641a8-8e77-476f-a24b-694dd7fc4a91",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping revise a research idea based on detailed reviewer feedback and new research findings. I need you to compose a complete revised JSON object. I'll provide the structure, key changes, and content for each field. Your job is to assemble it into a clean, complete JSON.\n\n**Context**: This is round 6 of revision for a paper on \"Geometry-Triggered Steering\" (GTS) — selective activation steering for hallucination suppression. The idea has stagnated at scores 3.2-3.5 across 3 rounds. Today is May 16, 2026. ARR deadline is May 25 (9 days remain).\n\n**Key changes for this major revision:**\n\n1. **Reframe the core contribution** around the GRANULARITY MISMATCH between token-level intervention and claim-level evaluation, rather than centering on Mahalanobis distance. PCNet's 53.7% corruption rate is concrete evidence that token-level gating still damages correct text.\n\n2. **Elevate PCNet to primary competitor** with full differentiation paragraph.\n\n3. **Honestly position Euclidean→Mahalanobis** as a hypothesized improvement to ablate, not the core contribution.\n\n4. **Add timing hypothesis disclaimer** noting Attractor Geometry paper's explicit limitation.\n\n5. **Define realistic 9-day minimum viable scope.**\n\nHere is the complete JSON to output. Output ONLY the JSON, no other text:\n\n```json\n{\n  \"change_type\": \"major\",\n  \"title\": \"Claim-Level Selective Activation Steering for Factual Hallucination Suppression in Long-Form Generation\",\n  \"core_problem\": \"Factual hallucination in LLMs has spurred a proliferation of geometry-aware detection and activation steering methods, yet a fundamental granularity mismatch persists: detection and intervention operate at token level, while factual evaluation operates at claim/sentence level. PCNet (May 2026) exemplifies this—its probabilistic-circuit gating achieves near-perfect detection AUROC yet still corrupts 53.7% of originally correct generations when intervening at every deviant token, because token-level decisions cannot distinguish 'this token is anomalous within an otherwise correct claim' from 'this claim is genuinely hallucinated.' FASB (NeurIPS 2025) addresses selective steering but operates correctively—detecting deviation after tokens are generated, then backtracking 10 tokens—which wastes compute and splits coherent claims. Spherical Steering (ICML 2026) applies per-token rotation with continuous vMF-gated intensity, achieving strong TruthfulQA gains but intervening indiscriminately across all claims. The Attractor Geometry paper (May 2026) demonstrates that Euclidean geometric margin separates correct recall from hallucination (AUROC 0.858 on TruthfulQA vs. entropy 0.656), but this result is detection-only and measured at first-digit positions on factoid completion—translation into targeted intervention at appropriate granularity during multi-sentence generation remains the open challenge.\",\n  \"opportunity\": \"The unexploited sweet spot is pre-emptive claim-level gating: sentences are the natural unit of factual claims—the granularity FActScore evaluates, the granularity humans judge, and the granularity at which LLMs integrate context before next-sentence planning (supported by 'Think in Sentences,' April 2026). The key evidence that this granularity matters comes from PCNet's results: despite near-perfect token-level detection (AUROC up to 99% on extractive QA), its token-level intervention still corrupts 53.7% of correct generations and preserves only 79.3%. This is because anomaly at individual token positions does not reliably indicate that the entire claim is hallucinated—a high-NLL token may be stylistically unusual but factually correct, or may be part of a partially correct claim that token-level correction damages. A system that makes binary steer/skip decisions at sentence boundaries—preserving entire correct claims untouched while steering only claims where the model lacks factual grounding—can achieve higher preservation rates by avoiding sub-claim intervention entirely. The three-part framework (when: sentence boundaries; whether: geometric distance trigger; how much: per-layer intensity) addresses limitations in all current methods: PCNet's token-level corruption, FASB's corrective backtracking overhead, Spherical Steering's indiscriminate application, and Hallucination Basins' per-sequence uniformity.\",\n  \"landscape\": \"**Selective geometric gating (primary competitors):**\\n\\n*PCNet (arXiv 2605.05953, May 2026)* is the closest concurrent work sharing the 'detect geometric anomaly → selectively intervene' paradigm. PCNet trains a Probabilistic Circuit as a density estimator over MLP-compressed residual stream states (4096→128 dims), computes exact NLL as anomaly score, and triggers PC-LDCD (contrastive decoding) only at deviant tokens. Results: TruthfulQA MC1 0.51 / MC2 0.65 on Llama-3.1-8B; near-perfect detection AUROC on extractive QA; corruption rate 53.7%, preservation rate 79.3%. Overhead: <2% for PC scoring, but 3.3–6.2 additional block evaluations per anomalous token for lookahead. GTS differs in three fundamental ways: (a) Granularity: sentence-level binary decisions preserve entire correct claims and avoid sub-claim corruption. PCNet evaluates NLL at every token, meaning intervention can damage partially correct claims—evidenced by its 53.7% corruption rate despite near-perfect detection. GTS's claim-level atomicity should achieve substantially lower corruption. (b) Intervention mechanism: activation steering shifts the model's own generation distribution toward factual attractors in a single forward pass, while contrastive decoding requires maintaining lookahead evaluations for top-k candidates at every anomalous position (PCNet's IGR ranges 0.41–0.78, meaning lookahead triggers at 41–78% of tokens). On long-form generation where many tokens are flagged, GTS's steering-only approach avoids this per-token lookahead cost. (c) Trigger interpretability: Euclidean/Mahalanobis distance from factual cluster centroids has a clear geometric interpretation (distance in representation space), while NLL from a trained probabilistic circuit is a learned density estimate whose failure modes are less transparent.\\n\\n*FASB (arXiv 2508.17621, NeurIPS 2025)* is the most direct prior work on 'when to steer,' using linear probes trained on attention head activations. It monitors concatenated question-and-generated-content states, triggers intervention when deviation is detected, and backtracks s=10 tokens to regenerate with steering. MC1 48.71% on TruthfulQA (LLaMA-2-7B-Chat). GTS differs in: (a) pre-emptive gating at sentence boundaries (no wasted tokens, no rollback) vs. FASB's corrective backtracking; (b) geometric distance trigger measuring knowledge absence vs. learned directional alignment on attention heads; (c) atomic claim-level decisions vs. token-level cuts that may split coherent claims. FASB's backtracking overhead scales linearly with intervention frequency—compounding on hallucination-dense long-form passages.\\n\\n**Geometry-aware steering (per-token):** Spherical Steering (arXiv 2602.08169, ICML 2026) uses geodesic rotation with a von Mises-Fisher confidence gate, achieving MC1 +15.80% on TruthfulQA (Llama-3.1-8B) with single-layer intervention (layer 24). Code released at github.com/chili-lab/Spherical-Steering. Per-token with continuous intensity—no claim-level selectivity. Hallucination Basins (arXiv 2604.04743, April 2026) proposes Adaptive Geometry-Aware Steering using Euclidean distance triggers and logistic-regression scalar maps at per-sequence granularity (uniform across all claims). Tested on 1B–8B models. GTS advances beyond both via within-sequence sentence-level selectivity.\\n\\n**Context-dependent directions:** Steering Vector Fields (SVF, arXiv 2602.01654, Feb 2026) learns differentiable concept-scoring MLPs for context-aware steering directions refreshed every K steps. Always steers—no gating. Complementary to GTS (GTS decides whether; SVF decides in which direction).\\n\\n**Utility preservation:** COAST (arXiv 2605.01167, May 2026) formalizes collateral damage as unintended feature-direction shifts and optimizes the steering vector via constrained optimization. Complementary to GTS (COAST optimizes the vector; GTS optimizes when to apply it).\\n\\n**Nonlinear geometry:** Curveball Steering (arXiv 2603.09313, March 2026) demonstrates substantial geometric distortion in activation spaces, supporting covariance-aware (Mahalanobis) over Euclidean distance.\\n\\n**Detection-only:** Attractor Geometry of Transformer Memory (arXiv 2605.05686, May 2026) demonstrates hallucination = basin absence with Euclidean geometric margin AUROC 0.858 on TruthfulQA (vs. entropy 0.656), 0.993 on controlled factoid tasks. All measurements at first-digit positions before autoregressive dynamics compound; the paper explicitly states 'transfer to open-domain settings requires further study.' Where Does Reasoning Break? (arXiv 2605.13772, May 2026) detects step-level hallucination via transport geometry. DRIFT (arXiv 2601.14210, Jan 2026) detects representational instability.\\n\\n**Calibration:** Calibrating Verbal Uncertainty (Ji et al., EMNLP 2025 Outstanding Paper) achieves ~31.9% reduction in confident hallucinations via linear-feature intervention—calibrates expression, does not correct generation.\\n\\n**Other steering:** ACT (WWW 2025), ODESteer (ICLR 2026, +5.7% over ACT), Guiding Giants/WAS (arXiv 2505.20309), SADI (arXiv 2410.12299), HELIX/Tethered Reasoning (arXiv 2602.17691). FLAS (arXiv 2605.05892, May 2026) learns concept-conditioned velocity fields for multi-step activation transport.\\n\\n**Supporting evidence:** Hallucination as Trajectory Commitment (arXiv 2604.15400, April 2026) provides causal evidence for early commitment with asymmetric attractor dynamics—supporting timely intervention before commitment propagates. Think in Sentences (arXiv 2604.10135, April 2026) demonstrates sentence boundary attention concentration patterns.\",\n  \"approach\": \"We propose Claim-Level Selective Activation Steering (CLSAS), a method that bridges the granularity gap between token-level detection/intervention and claim-level factual evaluation. The central insight is that intervention granularity should match evaluation granularity: since factuality is assessed per-claim (FActScore, human judgment), steering decisions should be made per-claim—preserving entire correct sentences untouched while steering only sentences where the model lacks factual grounding.\\n\\n**Stage 1: TRIGGER (Geometric Distance at Sentence Boundaries)**\\nDuring generation, at each sentence boundary (period/newline tokens), extract hidden-state activations at the boundary token across layers using nnsight intervention hooks. Compute geometric distance from factual cluster centroids:\\n(a) Offline: From a calibration set (~2K examples from TruthfulQA + FELM correct-answer forward passes), collect hidden states at factual completion positions. Apply PCA to project from full hidden dimension (d=4096) to top-k principal components (k=256), yielding a well-conditioned 256×256 covariance matrix.\\n(b) Online: Project the boundary token's activation into the PCA subspace. Compute distance to nearest factual centroid. We evaluate two distance metrics: (i) Euclidean distance δ_E(x) = ||h_pca − μ_pca||₂, matching the Attractor Geometry paper's validated metric (AUROC 0.858 on TruthfulQA); (ii) Mahalanobis distance δ_M(x) = √((h_pca − μ_pca)ᵀ Σ_pca⁻¹ (h_pca − μ_pca)), a hypothesized improvement motivated by OOD detection literature (Lee et al., NeurIPS 2018) that accounts for directional anisotropy in representation space.\\n(c) When distance exceeds a calibrated threshold (set via precision-recall analysis targeting high precision ≥0.85 to minimize false interventions), flag the upcoming sentence for steering.\\n\\n**Critical clarification:** The 0.858 AUROC motivating this trigger was achieved with Euclidean distance on first-digit positions during factoid completion (Attractor Geometry, May 2026). Our application to sentence boundaries during multi-sentence open-ended generation is an extrapolation that we explicitly validate as Milestone 1. The Attractor Geometry authors note 'transfer to open-domain settings requires further study.' If Mahalanobis does not significantly outperform Euclidean in our ablation, the primary novelty contribution rests on claim-level selective gating itself—which remains differentiated from all baselines regardless of distance metric.\\n\\n**Timing Hypothesis Validation (Milestone 1, Days 1-2):**\\nWe explicitly frame the following as a testable hypothesis: geometric distance at sentence boundary N is predictive of factual accuracy in sentence N+1. Validation protocol: (1) Generate 500 multi-sentence responses on LongFact/FActScore prompts using Llama-3.1-8B-Instruct. (2) Compute both Euclidean and Mahalanobis distance at every sentence boundary. (3) Annotate each subsequent sentence with FActScore. (4) Measure Spearman correlation between boundary distance and next-sentence factuality, and AUROC for binary classification. If AUROC < 0.70, we implement a look-ahead variant: extract distance from the first 3 generated tokens of the new sentence (before committing via speculative-style buffering). The look-ahead variant adds ~15% latency overhead but operates before the sentence is visible to the user. If look-ahead also fails (AUROC < 0.65), we fall back to a sliding-window approach using the mean distance over the last 5 tokens before the boundary.\\n\\n**Comparison to PCNet's trigger:** PCNet uses NLL from a trained probabilistic circuit as its anomaly score, evaluated at every token. This achieves near-perfect detection on extractive QA but still yields 53.7% corruption on correct generations. We hypothesize this is because token-level anomaly conflates stylistic deviation with factual error. Our sentence-level trigger aggregates geometric information at natural claim boundaries, making a single binary decision per claim—either the model has factual grounding for this claim (skip) or it doesn't (steer). This avoids sub-claim intervention entirely.\\n\\n**Stage 2: DIRECTION (Centroid-Directed Steering Vector)**\\nCompute the steering direction as the unit vector from the current activation toward the factual cluster centroid at each layer in the PCA subspace, then project back to full space: v_steer = (μ_pca − h_pca) / ||μ_pca − h_pca||, lifted back to full dimensionality via PCA inverse transform. This yields an input-specific correction direction toward regions of successful fact recall.\\n\\n**Stage 3: INTENSITY (Per-Layer Weighted Steering)**\\nA lightweight 2-layer MLP controller (hidden dim 64, inspired by Guiding Giants/WAS) takes [geometric_distance, layer_index/L, distance_velocity] as input (3D feature vector) and predicts per-layer steering weight λ_ℓ. Trained on a calibration set (~2K examples) to maximize FActScore on steered outputs while minimizing perplexity increase on non-flagged outputs. Steering: h_steered(ℓ) = h(ℓ) + λ_ℓ · v_steer(ℓ) at layers where λ_ℓ > ε.\\n\\n**Minimum Viable Scope (9 days, May 16–25):**\\n- Days 1-2 (May 16-17): Timing hypothesis validation on Llama-3.1-8B-Instruct. This is the critical-path milestone—if it fails, immediately implement look-ahead variant.\\n- Days 3-4 (May 18-19): Core CLSAS implementation + calibration. Run TruthfulQA and SimpleQA.\\n- Days 5-6 (May 20-21): Run baselines (Spherical Steering from released code, FASB from released code). Run FActScore and MT-Bench on CLSAS.\\n- Days 7-8 (May 22-23): Key ablations: 2×2 grid (Euclidean vs Mahalanobis × sentence-level vs token-level gating) on 4-benchmark core set. PCNet comparison if code is available; otherwise use reported numbers with matched model.\\n- Day 9 (May 24): Writing, formatting, submission buffer.\\n- Dropped from scope: COAST combination experiment, Qwen3-8B (secondary model), full 7-benchmark suite for ablations, GTS-FASB-trigger ablation.\\n\\n**Ablation Design (MVP):**\\n- CLSAS-full vs. CLSAS-Euclidean (isolate Mahalanobis contribution)\\n- CLSAS-full vs. CLSAS-pertoken (apply continuous per-token gating with our distance metric, matching PCNet/Spherical Steering's granularity—isolates the claim-level contribution)\\n- CLSAS-full vs. CLSAS-sequence (single decision per sequence, matching Hallucination Basins' granularity)\\n- CLSAS-full vs. CLSAS-scalar (replace per-layer MLP with single scalar, isolating controller contribution)\\n- Direct comparison: CLSAS-full vs. Spherical Steering vs. FASB vs. PCNet (reported numbers if code unavailable)\\n\\n**Primary evaluation metrics:**\\n- Corruption rate and preservation rate (matching PCNet's protocol): fraction of correct claims degraded / preserved by intervention\\n- FActScore on long-form biographies (primary benchmark where claim-level advantage should be largest)\\n- TruthfulQA MC1/MC2, SimpleQA accuracy, MT-Bench score\\n- Intervention rate: fraction of sentences steered (lower is better for comparable factuality gains)\\n- Latency overhead vs. baselines\\n\\nImplementation uses nnsight 0.7 on Llama-3.1-8B-Instruct. Qwen3-8B included only if time permits after MVP completion.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~120h H100 80GB\",\n      \"gpu_utilization\": \"Low (~15-20%)\",\n      \"timeline\": \"3-4 months\",\n      \"team\": \"1-2 researchers with mechanistic interpretability + geometric ML experience\",\n      \"estimated_gpu_cost\": \"$360-400\",\n      \"factScore_api_cost\": \"$100-200\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~130h H100 80GB\",\n      \"gpu_utilization\": \"Moderate (45-55%)\",\n      \"timeline\": \"2-3 weeks\",\n      \"team\": \"1 researcher, ~30min/day reviewing proposals\",\n      \"claude_api_cost\": \"$150-250\",\n      \"estimated_gpu_cost\": \"$390-430\",\n      \"factScore_api_cost\": \"$100-200\",\n      \"risk_note\": \"Timing hypothesis validation is critical-path. If it fails (AUROC < 0.70), look-ahead fallback adds ~3 days.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~140h H100 80GB\",\n      \"gpu_utilization\": \"High (~85-90%)\",\n      \"timeline\": \"9 days (May 16-25) with 2 H100 GPUs. Minimum viable paper scope: single model (Llama-3.1-8B), 4-benchmark core set for ablations, full baselines on FActScore+TruthfulQA+SimpleQA+MT-Bench.\",\n      \"team\": \"0 (initial setup: provision GPUs, configure nnsight 0.7, clone Spherical Steering + FASB repos)\",\n      \"claude_api_cost\": \"$250-350 (est. 3000-4000 turns)\",\n      \"estimated_gpu_cost\": \"$420-450\",\n      \"factScore_api_cost\": \"$100-200\",\n      \"speed_bottleneck\": \"Timing hypothesis validation (days 1-2) is critical path. If it fails, look-ahead variant must be implemented immediately. Secondary: FActScore GPT-4 API calls.\",\n      \"resource_optimization\": \"Budget achieved via: (1) single model (Llama-3.1-8B) for all experiments; (2) 4-benchmark core set (TruthfulQA, FActScore, SimpleQA, MT-Bench); (3) 2×2 ablation grid (distance metric × gating granularity) instead of separate sweeps; (4) use Spherical Steering and FASB released code directly; (5) PCNet comparison using reported numbers if code unavailable.\",\n      \"minimum_viable_paper\": \"If timing hypothesis fails AND look-ahead also fails: pivot to a detection-only contribution (sentence-level geometric detection benchmark) comparing Euclidean/Mahalanobis at sentence boundaries vs. PCNet's token-level NLL. This is publishable as a shorter paper (findings track).\",\n      \"risk_note\": \"Primary risk: timing hypothesis may fail (Attractor Geometry paper validated only on factoid completion at first-digit positions, explicitly disclaiming open-domain transfer). Mitigation: look-ahead variant, then sliding-window fallback. Secondary risk: claim-level gating may not outperform PCNet's token-level gating on short-form QA—advantage expected primarily on long-form generation (FActScore, LongFact). Tertiary risk: 9-day timeline leaves zero buffer for unexpected implementation issues.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits (PCNet, arXiv 2605.05953, May 2026)\",\n    \"Steering When Necessary: Flexible Steering Large Language Models with Backtracking (FASB, arXiv 2508.17621, NeurIPS 2025)\",\n    \"Spherical Steering: Geometry-Aware Activation Rotation for Language Models (arXiv 2602.08169, ICML 2026)\",\n    \"Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination (arXiv 2605.05686, May 2026)\",\n    \"Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations (arXiv 2604.04743, April 2026)\",\n    \"Steering Vector Fields for Context-Aware Inference-Time Control in Large Language Models (SVF, arXiv 2602.01654, Feb 2026)\",\n    \"Curveball Steering: The Right Direction To Steer Isn't Always Linear (arXiv 2603.09313, March 2026)\",\n    \"Minimizing Collateral Damage in Activation Steering (COAST, arXiv 2605.01167, May 2026)\",\n    \"Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention (FLAS, arXiv 2605.05892, May 2026)\",\n    \"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025 Outstanding Paper, arXiv 2503.14477)\",\n    \"Tethered Reasoning (HELIX): Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering (arXiv 2602.17691, Feb 2026)\",\n    \"Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method (ACT, WWW 2025)\",\n    \"ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment (ICLR 2026, arXiv 2602.17560)\",\n    \"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (arXiv 2605.13772, May 2026)\",\n    \"DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness (arXiv 2601.14210, Jan 2026)\",\n    \"Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs (arXiv 2505.20309, May 2025)\",\n    \"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics (arXiv 2604.15400, April 2026)\",\n    \"Think in Sentences: Explicit Sentence Boundaries Enhance Language Model's Capabilities (arXiv 2604.10135, April 2026)\",\n    \"A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks (Lee et al., NeurIPS 2018)\",\n    \"Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors (SADI, arXiv 2410.12299, 2024)\",\n    \"Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models (ICLR 2026)\"\n  ],\n  \"description\": \"We propose Claim-Level Selective Activation Steering (CLSAS), a method that bridges the granularity gap between token-level hallucination detection/intervention and claim-level factual evaluation. The central insight is that intervention granularity should match evaluation granularity: since factuality is assessed per-claim (FActScore, human judgment), steering decisions should be per-claim—preserving entire correct sentences untouched while steering only claims where the model lacks factual grounding.\\n\\nThe motivation is concrete: PCNet (May 2026), the state-of-the-art in selective geometric gating, achieves near-perfect token-level hallucination detection (AUROC up to 99% on extractive QA) yet still corrupts 53.7% of originally correct generations when intervening token-by-token via contrastive decoding. We hypothesize this corruption stems from the granularity mismatch—token-level anomaly conflates stylistic deviation with factual error, and sub-claim interventions damage partially correct claims.\\n\\nCLSAS monitors geometric distance from residual stream activations to factual cluster centroids at sentence boundaries during generation. Building on the finding that Euclidean geometric margin separates correct recall from hallucination (AUROC 0.858 on TruthfulQA; Attractor Geometry, May 2026), we evaluate both Euclidean and Mahalanobis distance triggers—the latter a hypothesized improvement motivated by OOD detection literature (Lee et al., NeurIPS 2018) that we validate via ablation. When distance indicates basin absence, CLSAS computes an input-specific steering vector toward the factual centroid and applies it with per-layer weights from a lightweight MLP controller. Sentences within a factual basin are left entirely untouched.\\n\\nCLSAS addresses limitations in the closest concurrent work: (1) vs. PCNet (May 2026, MC1 0.51 on Llama-3.1-8B), CLSAS makes sentence-level binary decisions that avoid sub-claim corruption. PCNet's token-level NLL gating triggers at 41-78% of tokens (IGR), requiring costly lookahead evaluations at each; CLSAS intervenes only at sentence boundaries. (2) vs. FASB (NeurIPS 2025, MC1 48.71% on LLaMA-2-7B-Chat), CLSAS is pre-emptive—gating before generation rather than detecting deviation and rolling back 10 tokens. (3) vs. Spherical Steering (ICML 2026, +15% MC1), CLSAS makes binary claim-level steer/skip decisions rather than continuous per-token rotation, enabling complete preservation of correct claims. (4) vs. Hallucination Basins (April 2026), CLSAS provides within-sequence selectivity rather than uniform per-sequence correction.\\n\\nWe explicitly validate the timing hypothesis (distance at boundary N predicts factuality of sentence N+1) as Milestone 1 with a correlation study, noting the Attractor Geometry paper's disclaimer that results were measured at first-digit positions and 'transfer to open-domain settings requires further study.' A look-ahead fallback is specified if correlation is insufficient. We hypothesize CLSAS's advantage over token-level methods will be strongest on long-form generation (FActScore) where multiple claims coexist and token-level corruption compounds.\\n\\nMinimum viable scope for 9 remaining days: single model (Llama-3.1-8B-Instruct), 4-benchmark evaluation (TruthfulQA, FActScore, SimpleQA, MT-Bench), 2×2 ablation grid (distance metric × gating granularity), direct comparison with Spherical Steering and FASB using released code. Total budget: ≤140 H100-hours.\",\n  \"project_name\": \"claim_level_selective_steering\",\n  \"source\": \"web_research\"\n}\n```\n\nPlease output this JSON exactly as provided, ensuring it is valid JSON. Do not add any text before or after the JSON.\n",
    "agentId": "ace13499b3290f5f7",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "\n\n```json\n{\n  \"change_type\": \"major\",\n  \"title\": \"Claim-Level Selective Activation Steering for Factual Hallucination Suppression in Long-Form Generation\",\n  \"core_problem\": \"Factual hallucination in LLMs has spurred a proliferation of geometry-aware detection and activation steering methods, yet a fundamental granularity mismatch persists: detection and intervention operate at token level, while factual evaluation operates at claim/sentence level. PCNet (May 2026) exemplifies this—its probabilistic-circuit gating achieves near-perfect detection AUROC yet still corrupts 53.7% of originally correct generations when intervening at every deviant token, because token-level decisions cannot distinguish 'this token is anomalous within an otherwise correct claim' from 'this claim is genuinely hallucinated.' FASB (NeurIPS 2025) addresses selective steering but operates correctively—detecting deviation after tokens are generated, then backtracking 10 tokens—which wastes compute and splits coherent claims. Spherical Steering (ICML 2026) applies per-token rotation with continuous vMF-gated intensity, achieving strong TruthfulQA gains but intervening indiscriminately across all claims. The Attractor Geometry paper (May 2026) demonstrates that Euclidean geometric margin separates correct recall from hallucination (AUROC 0.858 on TruthfulQA vs. entropy 0.656), but this result is detection-only and measured at first-digit positions on factoid completion—translation into targeted intervention at appropriate granularity during multi-sentence generation remains the open challenge.\",\n  \"opportunity\": \"The unexploited sweet spot is pre-emptive claim-level gating: sentences are the natural unit of factual claims—the granularity FActScore evaluates, the granularity humans judge, and the granularity at which LLMs integrate context before next-sentence planning (supported by 'Think in Sentences,' April 2026). The key evidence that this granularity matters comes from PCNet's results: despite near-perfect token-level detection (AUROC up to 99% on extractive QA), its token-level intervention still corrupts 53.7% of correct generations and preserves only 79.3%. This is because anomaly at individual token positions does not reliably indicate that the entire claim is hallucinated—a high-NLL token may be stylistically unusual but factually correct, or may be part of a partially correct claim that token-level correction damages. A system that makes binary steer/skip decisions at sentence boundaries—preserving entire correct claims untouched while steering only claims where the model lacks factual grounding—can achieve higher preservation rates by avoiding sub-claim intervention entirely. The three-part framework (when: sentence boundaries; whether: geometric distance trigger; how much: per-layer intensity) addresses limitations in all current methods: PCNet's token-level corruption, FASB's corrective backtracking overhead, Spherical Steering's indiscriminate application, and Hallucination Basins' per-sequence uniformity.\",\n  \"landscape\": \"**Selective geometric gating (primary competitors):**\\n\\n*PCNet (arXiv 2605.05953, May 2026)* is the closest concurrent work sharing the 'detect geometric anomaly → selectively intervene' paradigm. PCNet trains a Probabilistic Circuit as a density estimator over MLP-compressed residual stream states (4096→128 dims), computes exact NLL as anomaly score, and triggers PC-LDCD (contrastive decoding) only at deviant tokens. Results: TruthfulQA MC1 0.51 / MC2 0.65 on Llama-3.1-8B; near-perfect detection AUROC on extractive QA; corruption rate 53.7%, preservation rate 79.3%. Overhead: <2% for PC scoring, but 3.3–6.2 additional block evaluations per anomalous token for lookahead. GTS differs in three fundamental ways: (a) Granularity: sentence-level binary decisions preserve entire correct claims and avoid sub-claim corruption. PCNet evaluates NLL at every token, meaning intervention can damage partially correct claims—evidenced by its 53.7% corruption rate despite near-perfect detection. GTS's claim-level atomicity should achieve substantially lower corruption. (b) Intervention mechanism: activation steering shifts the model's own generation distribution toward factual attractors in a single forward pass, while contrastive decoding requires maintaining lookahead evaluations for top-k candidates at every anomalous position (PCNet's IGR ranges 0.41–0.78, meaning lookahead triggers at 41–78% of tokens). On long-form generation where many tokens are flagged, GTS's steering-only approach avoids this per-token lookahead cost. (c) Trigger interpretability: Euclidean/Mahalanobis distance from factual cluster centroids has a clear geometric interpretation (distance in representation space), while NLL from a trained probabilistic circuit is a learned density estimate whose failure modes are less transparent.\\n\\n*FASB (arXiv 2508.17621, NeurIPS 2025)* is the most direct prior work on 'when to steer,' using linear probes trained on attention head activations. It monitors concatenated question-and-generated-content states, triggers intervention when deviation is detected, and backtracks s=10 tokens to regenerate with steering. MC1 48.71% on TruthfulQA (LLaMA-2-7B-Chat). GTS differs in: (a) pre-emptive gating at sentence boundaries (no wasted tokens, no rollback) vs. FASB's corrective backtracking; (b) geometric distance trigger measuring knowledge absence vs. learned directional alignment on attention heads; (c) atomic claim-level decisions vs. token-level cuts that may split coherent claims. FASB's backtracking overhead scales linearly with intervention frequency—compounding on hallucination-dense long-form passages.\\n\\n**Geometry-aware steering (per-token):** Spherical Steering (arXiv 2602.08169, ICML 2026) uses geodesic rotation with a von Mises-Fisher confidence gate, achieving MC1 +15.80% on TruthfulQA (Llama-3.1-8B) with single-layer intervention (layer 24). Code released at github.com/chili-lab/Spherical-Steering. Per-token with continuous intensity—no claim-level selectivity. Hallucination Basins (arXiv 2604.04743, April 2026) proposes Adaptive Geometry-Aware Steering using Euclidean distance triggers and logistic-regression scalar maps at per-sequence granularity (uniform across all claims). Tested on 1B–8B models. GTS advances beyond both via within-sequence sentence-level selectivity.\\n\\n**Context-dependent directions:** Steering Vector Fields (SVF, arXiv 2602.01654, Feb 2026) learns differentiable concept-scoring MLPs for context-aware steering directions refreshed every K steps. Always steers—no gating. Complementary to GTS (GTS decides whether; SVF decides in which direction).\\n\\n**Utility preservation:** COAST (arXiv 2605.01167, May 2026) formalizes collateral damage as unintended feature-direction shifts and optimizes the steering vector via constrained optimization. Complementary to GTS (COAST optimizes the vector; GTS optimizes when to apply it).\\n\\n**Nonlinear geometry:** Curveball Steering (arXiv 2603.09313, March 2026) demonstrates substantial geometric distortion in activation spaces, supporting covariance-aware (Mahalanobis) over Euclidean distance.\\n\\n**Detection-only:** Attractor Geometry of Transformer Memory (arXiv 2605.05686, May 2026) demonstrates hallucination = basin absence with Euclidean geometric margin AUROC 0.858 on TruthfulQA (vs. entropy 0.656), 0.993 on controlled factoid tasks. All measurements at first-digit positions before autoregressive dynamics compound; the paper explicitly states 'transfer to open-domain settings requires further study.' Where Does Reasoning Break? (arXiv 2605.13772, May 2026) detects step-level hallucination via transport geometry. DRIFT (arXiv 2601.14210, Jan 2026) detects representational instability.\\n\\n**Calibration:** Calibrating Verbal Uncertainty (Ji et al., EMNLP 2025 Outstanding Paper) achieves ~31.9% reduction in confident hallucinations via linear-feature intervention—calibrates expression, does not correct generation.\\n\\n**Other steering:** ACT (WWW 2025), ODESteer (ICLR 2026, +5.7% over ACT), Guiding Giants/WAS (arXiv 2505.20309), SADI (arXiv 2410.12299), HELIX/Tethered Reasoning (arXiv 2602.17691). FLAS (arXiv 2605.05892, May 2026) learns concept-conditioned velocity fields for multi-step activation transport.\\n\\n**Supporting evidence:** Hallucination as Trajectory Commitment (arXiv 2604.15400, April 2026) provides causal evidence for early commitment with asymmetric attractor dynamics—supporting timely intervention before commitment propagates. Think in Sentences (arXiv 2604.10135, April 2026) demonstrates sentence boundary attention concentration patterns.\",\n  \"approach\": \"We propose Claim-Level Selective Activation Steering (CLSAS), a method that bridges the granularity gap between token-level detection/intervention and claim-level factual evaluation. The central insight is that intervention granularity should match evaluation granularity: since factuality is assessed per-claim (FActScore, human judgment), steering decisions should be made per-claim—preserving entire correct sentences untouched while steering only sentences where the model lacks factual grounding.\\n\\n**Stage 1: TRIGGER (Geometric Distance at Sentence Boundaries)**\\nDuring generation, at each sentence boundary (period/newline tokens), extract hidden-state activations at the boundary token across layers using nnsight intervention hooks. Compute geometric distance from factual cluster centroids:\\n(a) Offline: From a calibration set (~2K examples from TruthfulQA + FELM correct-answer forward passes), collect hidden states at factual completion positions. Apply PCA to project from full hidden dimension (d=4096) to top-k principal components (k=256), yielding a well-conditioned 256×256 covariance matrix.\\n(b) Online: Project the boundary token's activation into the PCA subspace. Compute distance to nearest factual centroid. We evaluate two distance metrics: (i) Euclidean distance δ_E(x) = ||h_pca − μ_pca||₂, matching the Attractor Geometry paper's validated metric (AUROC 0.858 on TruthfulQA); (ii) Mahalanobis distance δ_M(x) = √((h_pca − μ_pca)ᵀ Σ_pca⁻¹ (h_pca − μ_pca)), a hypothesized improvement motivated by OOD detection literature (Lee et al., NeurIPS 2018) that accounts for directional anisotropy in representation space.\\n(c) When distance exceeds a calibrated threshold (set via precision-recall analysis targeting high precision ≥0.85 to minimize false interventions), flag the upcoming sentence for steering.\\n\\n**Critical clarification:** The 0.858 AUROC motivating this trigger was achieved with Euclidean distance on first-digit positions during factoid completion (Attractor Geometry, May 2026). Our application to sentence boundaries during multi-sentence open-ended generation is an extrapolation that we explicitly validate as Milestone 1. The Attractor Geometry authors note 'transfer to open-domain settings requires further study.' If Mahalanobis does not significantly outperform Euclidean in our ablation, the primary novelty contribution rests on claim-level selective gating itself—which remains differentiated from all baselines regardless of distance metric.\\n\\n**Timing Hypothesis Validation (Milestone 1, Days 1-2):**\\nWe explicitly frame the following as a testable hypothesis: geometric distance at sentence boundary N is predictive of factual accuracy in sentence N+1. Validation protocol: (1) Generate 500 multi-sentence responses on LongFact/FActScore prompts using Llama-3.1-8B-Instruct. (2) Compute both Euclidean and Mahalanobis distance at every sentence boundary. (3) Annotate each subsequent sentence with FActScore. (4) Measure Spearman correlation between boundary distance and next-sentence factuality, and AUROC for binary classification. If AUROC < 0.70, we implement a look-ahead variant: extract distance from the first 3 generated tokens of the new sentence (before committing via speculative-style buffering). The look-ahead variant adds ~15% latency overhead but operates before the sentence is visible to the user. If look-ahead also fails (AUROC < 0.65), we fall back to a sliding-window approach using the mean distance over the last 5 tokens before the boundary.\\n\\n**Comparison to PCNet's trigger:** PCNet uses NLL from a trained probabilistic circuit as its anomaly score, evaluated at every token. This achieves near-perfect detection on extractive QA but still yields 53.7% corruption on correct generations. We hypothesize this is because token-level anomaly conflates stylistic deviation with factual error. Our sentence-level trigger aggregates geometric information at natural claim boundaries, making a single binary decision per claim—either the model has factual grounding for this claim (skip) or it doesn't (steer). This avoids sub-claim intervention entirely.\\n\\n**Stage 2: DIRECTION (Centroid-Directed Steering Vector)**\\nCompute the steering direction as the unit vector from the current activation toward the factual cluster centroid at each layer in the PCA subspace, then project back to full space: v_steer = (μ_pca − h_pca) / ||μ_pca − h_pca||, lifted back to full dimensionality via PCA inverse transform. This yields an input-specific correction direction toward regions of successful fact recall.\\n\\n**Stage 3: INTENSITY (Per-Layer Weighted Steering)**\\nA lightweight 2-layer MLP controller (hidden dim 64, inspired by Guiding Giants/WAS) takes [geometric_distance, layer_index/L, distance_velocity] as input (3D feature vector) and predicts per-layer steering weight λ_ℓ. Trained on a calibration set (~2K examples) to maximize FActScore on steered outputs while minimizing perplexity increase on non-flagged outputs. Steering: h_steered(ℓ) = h(ℓ) + λ_ℓ · v_steer(ℓ) at layers where λ_ℓ > ε.\\n\\n**Minimum Viable Scope (9 days, May 16–25):**\\n- Days 1-2 (May 16-17): Timing hypothesis validation on Llama-3.1-8B-Instruct. This is the critical-path milestone—if it fails, immediately implement look-ahead variant.\\n- Days 3-4 (May 18-19): Core CLSAS implementation + calibration. Run TruthfulQA and SimpleQA.\\n- Days 5-6 (May 20-21): Run baselines (Spherical Steering from released code, FASB from released code). Run FActScore and MT-Bench on CLSAS.\\n- Days 7-8 (May 22-23): Key ablations: 2×2 grid (Euclidean vs Mahalanobis × sentence-level vs token-level gating) on 4-benchmark core set. PCNet comparison if code is available; otherwise use reported numbers with matched model.\\n- Day 9 (May 24): Writing, formatting, submission buffer.\\n- Dropped from scope: COAST combination experiment, Qwen3-8B (secondary model), full 7-benchmark suite for ablations, GTS-FASB-trigger ablation.\\n\\n**Ablation Design (MVP):**\\n- CLSAS-full vs. CLSAS-Euclidean (isolate Mahalanobis contribution)\\n- CLSAS-full vs. CLSAS-pertoken (apply continuous per-token gating with our distance metric, matching PCNet/Spherical Steering's granularity—isolates the claim-level contribution)\\n- CLSAS-full vs. CLSAS-sequence (single decision per sequence, matching Hallucination Basins' granularity)\\n- CLSAS-full vs. CLSAS-scalar (replace per-layer MLP with single scalar, isolating controller contribution)\\n- Direct comparison: CLSAS-full vs. Spherical Steering vs. FASB vs. PCNet (reported numbers if code unavailable)\\n\\n**Primary evaluation metrics:**\\n- Corruption rate and preservation rate (matching PCNet's protocol): fraction of correct claims degraded / preserved by intervention\\n- FActScore on long-form biographies (primary benchmark where claim-level advantage should be largest)\\n- TruthfulQA MC1/MC2, SimpleQA accuracy, MT-Bench score\\n- Intervention rate: fraction of sentences steered (lower is better for comparable factuality gains)\\n- Latency overhead vs. baselines\\n\\nImplementation uses nnsight 0.7 on Llama-3.1-8B-Instruct. Qwen3-8B included only if time permits after MVP completion.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~120h H100 80GB\",\n      \"gpu_utilization\": \"Low (~15-20%)\",\n      \"timeline\": \"3-4 months\",\n      \"team\": \"1-2 researchers with mechanistic interpretability + geometric ML experience\",\n      \"estimated_gpu_cost\": \"$360-400\",\n      \"factScore_api_cost\": \"$100-200\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~130h H100 80GB\",\n      \"gpu_utilization\": \"Moderate (45-55%)\",\n      \"timeline\": \"2-3 weeks\",\n      \"team\": \"1 researcher, ~30min/day reviewing proposals\",\n      \"claude_api_cost\": \"$150-250\",\n      \"estimated_gpu_cost\": \"$390-430\",\n      \"factScore_api_cost\": \"$100-200\",\n      \"risk_note\": \"Timing hypothesis validation is critical-path. If it fails (AUROC < 0.70), look-ahead fallback adds ~3 days.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~140h H100 80GB\",\n      \"gpu_utilization\": \"High (~85-90%)\",\n      \"timeline\": \"9 days (May 16-25) with 2 H100 GPUs. Minimum viable paper scope: single model (Llama-3.1-8B), 4-benchmark core set for ablations, full baselines on FActScore+TruthfulQA+SimpleQA+MT-Bench.\",\n      \"team\": \"0 (initial setup: provision GPUs, configure nnsight 0.7, clone Spherical Steering + FASB repos)\",\n      \"claude_api_cost\": \"$250-350 (est. 3000-4000 turns)\",\n      \"estimated_gpu_cost\": \"$420-450\",\n      \"factScore_api_cost\": \"$100-200\",\n      \"speed_bottleneck\": \"Timing hypothesis validation (days 1-2) is critical path. If it fails, look-ahead variant must be implemented immediately. Secondary: FActScore GPT-4 API calls.\",\n      \"resource_optimization\": \"Budget achieved via: (1) single model (Llama-3.1-8B) for all experiments; (2) 4-benchmark core set (TruthfulQA, FActScore, SimpleQA, MT-Bench); (3) 2×2 ablation grid (distance metric × gating granularity) instead of separate sweeps; (4) use Spherical Steering and FASB released code directly; (5) PCNet comparison using reported numbers if code unavailable.\",\n      \"minimum_viable_paper\": \"If timing hypothesis fails AND look-ahead also fails: pivot to a detection-only contribution (sentence-level geometric detection benchmark) comparing Euclidean/Mahalanobis at sentence boundaries vs. PCNet's token-level NLL. This is publishable as a shorter paper (findings track).\",\n      \"risk_note\": \"Primary risk: timing hypothesis may fail (Attractor Geometry paper validated only on factoid completion at first-digit positions, explicitly disclaiming open-domain transfer). Mitigation: look-ahead variant, then sliding-window fallback. Secondary risk: claim-level gating may not outperform PCNet's token-level gating on short-form QA—advantage expected primarily on long-form generation (FActScore, LongFact). Tertiary risk: 9-day timeline leaves zero buffer for unexpected implementation issues.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits (PCNet, arXiv 2605.05953, May 2026)\",\n    \"Steering When Necessary: Flexible Steering Large Language Models with Backtracking (FASB, arXiv 2508.17621, NeurIPS 2025)\",\n    \"Spherical Steering: Geometry-Aware Activation Rotation for Language Models (arXiv 2602.08169, ICML 2026)\",\n    \"Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination (arXiv 2605.05686, May 2026)\",\n    \"Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations (arXiv 2604.04743, April 2026)\",\n    \"Steering Vector Fields for Context-Aware Inference-Time Control in Large Language Models (SVF, arXiv 2602.01654, Feb 2026)\",\n    \"Curveball Steering: The Right Direction To Steer Isn't Always Linear (arXiv 2603.09313, March 2026)\",\n    \"Minimizing Collateral Damage in Activation Steering (COAST, arXiv 2605.01167, May 2026)\",\n    \"Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention (FLAS, arXiv 2605.05892, May 2026)\",\n    \"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025 Outstanding Paper, arXiv 2503.14477)\",\n    \"Tethered Reasoning (HELIX): Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering (arXiv 2602.17691, Feb 2026)\",\n    \"Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method (ACT, WWW 2025)\",\n    \"ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment (ICLR 2026, arXiv 2602.17560)\",\n    \"Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (arXiv 2605.13772, May 2026)\",\n    \"DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness (arXiv 2601.14210, Jan 2026)\",\n    \"Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs (arXiv 2505.20309, May 2025)\",\n    \"Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics (arXiv 2604.15400, April 2026)\",\n    \"Think in Sentences: Explicit Sentence Boundaries Enhance Language Model's Capabilities (arXiv 2604.10135, April 2026)\",\n    \"A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks (Lee et al., NeurIPS 2018)\",\n    \"Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors (SADI, arXiv 2410.12299, 2024)\",\n    \"Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models (ICLR 2026)\"\n  ],\n  \"description\": \"We propose Claim-Level Selective Activation Steering (CLSAS), a method that bridges the granularity gap between token-level hallucination detection/intervention and claim-level factual evaluation. The central insight is that intervention granularity should match evaluation granularity: since factuality is assessed per-claim (FActScore, human judgment), steering decisions should be per-claim—preserving entire correct sentences untouched while steering only claims where the model lacks factual grounding.\\n\\nThe motivation is concrete: PCNet (May 2026), the state-of-the-art in selective geometric gating, achieves near-perfect token-level hallucination detection (AUROC up to 99% on extractive QA) yet still corrupts 53.7% of originally correct generations when intervening token-by-token via contrastive decoding. We hypothesize this corruption stems from the granularity mismatch—token-level anomaly conflates stylistic deviation with factual error, and sub-claim interventions damage partially correct claims.\\n\\nCLSAS monitors geometric distance from residual stream activations to factual cluster centroids at sentence boundaries during generation. Building on the finding that Euclidean geometric margin separates correct recall from hallucination (AUROC 0.858 on TruthfulQA; Attractor Geometry, May 2026), we evaluate both Euclidean and Mahalanobis distance triggers—the latter a hypothesized improvement motivated by OOD detection literature (Lee et al., NeurIPS 2018) that we validate via ablation. When distance indicates basin absence, CLSAS computes an input-specific steering vector toward the factual centroid and applies it with per-layer weights from a lightweight MLP controller. Sentences within a factual basin are left entirely untouched.\\n\\nCLSAS addresses limitations in the closest concurrent work: (1) vs. PCNet (May 2026, MC1 0.51 on Llama-3.1-8B), CLSAS makes sentence-level binary decisions that avoid sub-claim corruption. PCNet's token-level NLL gating triggers at 41-78% of tokens (IGR), requiring costly lookahead evaluations at each; CLSAS intervenes only at sentence boundaries. (2) vs. FASB (NeurIPS 2025, MC1 48.71% on LLaMA-2-7B-Chat), CLSAS is pre-emptive—gating before generation rather than detecting deviation and rolling back 10 tokens. (3) vs. Spherical Steering (ICML 2026, +15% MC1), CLSAS makes binary claim-level steer/skip decisions rather than continuous per-token rotation, enabling complete preservation of correct claims. (4) vs. Hallucination Basins (April 2026), CLSAS provides within-sequence selectivity rather than uniform per-sequence correction.\\n\\nWe explicitly validate the timing hypothesis (distance at boundary N predicts factuality of sentence N+1) as Milestone 1 with a correlation study, noting the Attractor Geometry paper's disclaimer that results were measured at first-digit positions and 'transfer to open-domain settings requires further study.' A look-ahead fallback is specified if correlation is insufficient. We hypothesize CLSAS's advantage over token-level methods will be strongest on long-form generation (FActScore) where multiple claims coexist and token-level corruption compounds.\\n\\nMinimum viable scope for 9 remaining days: single model (Llama-3.1-8B-Instruct), 4-benchmark evaluation (TruthfulQA, FActScore, SimpleQA, MT-Bench), 2×2 ablation grid (distance metric × gating granularity), direct comparison with Spherical Steering and FASB using released code. Total budget: ≤140 H100-hours.\",\n  \"project_name\": \"claim_level_selective_steering\",\n  \"source\": \"web_research\"\n}\n```"
      }
    ],
    "totalDurationMs": 106759,
    "totalTokens": 23101,
    "totalToolUseCount": 0,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16112,
      "cache_read_input_tokens": 0,
      "output_tokens": 6987,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16112
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 6987,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16112,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  },
  "sourceToolAssistantUUID": "88e4fe58-55d5-4874-847a-61b3e11849a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 67_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-16 (UTC).**  ## Original idea {   \"title\": \"Geometry-Triggered Sentence-Level Activation Steering for Factual Hall…",
  "leafUuid": "88b641a8-8e77-476f-a24b-694dd7fc4a91",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c"
}
```

---

### Runtime record

_source line 68_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise GTS with PCNet differentiation and realistic timeline",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c"
}
```

---

### Assistant

_source line 69 · 2026-05-16T09:17:02.590Z_

<details><summary>Logged reasoning block</summary>

```text
The agent has output the complete JSON. Let me verify it looks correct and complete, then present the final revised idea to the user. Let me also do a final quality check to make sure all reviewer issues are addressed:

1. **PCNet differentiation**: ✅ Full paragraph in landscape as primary competitor, with 3-way differentiation (granularity, intervention mechanism, trigger interpretability). Also referenced in core_problem, opportunity, and approach.

2. **Euclidean→Mahalanobis clarification**: ✅ Clear statement that 0.858 AUROC was Euclidean, Mahalanobis is hypothesized improvement. 

3. **Timeline/minimum viable scope**: ✅ 9-day plan with specific daily milestones. Dropped COAST, Qwen3-8B, full 7-benchmark suite. Defined minimum viable paper fallback if timing hypothesis fails.

4. **Timing hypothesis disclaimer**: ✅ Explicitly notes Attractor Geometry paper's limitations ("first-digit positions," "transfer to open-domain settings requires further study"). Validation as Milestone 1 with multiple fallbacks.

Now I'm adding the critical clarification section in the approach that explicitly lays out the ablation study comparing the full CLSAS method against the Euclidean baseline to validate the Mahalanobis improvement hypothesis.

The core contribution is reframed from focusing on Mahalanobis distance at sentence boundaries to highlighting the granularity mismatch between token-level interventions and claim-level evaluation — this is a much cleaner framing that doesn't hinge on any single distance metric. The JSON structure looks solid, so I'm ready to present this.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88b641a8-8e77-476f-a24b-694dd7fc4a91",
  "isSidechain": false,
  "requestId": "req_011Cb5zicxkSg95NRYxePkmT",
  "type": "assistant",
  "uuid": "6a712db9-273a-4022-8001-c73cf6d1f604",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014LKAHFzrYX3bau6SuNsEtY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17228,
      "cache_read_input_tokens": 45074,
      "output_tokens": 8134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17228,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8134,
          "cache_read_input_tokens": 45074,
          "cache_creation_input_tokens": 17228,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17228
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

_source line 70 · 2026-05-16T09:19:08.428Z_

Here is the revised research idea. This is a **major revision** that reframes the core contribution around the granularity mismatch (token-level intervention vs. claim-level evaluation) rather than centering on Mahalanobis distance.

**Summary of key changes addressing each reviewer issue:**

1. **PCNet differentiation**: Elevated to primary competitor with a full differentiation paragraph (granularity, intervention mechanism, trigger interpretability). PCNet's 53.7% corruption rate is now the central motivating evidence for why claim-level gating matters.

2. **Euclidean→Mahalanobis clarification**: The 0.858 AUROC is now explicitly attributed to Euclidean distance. Mahalanobis is presented as a "hypothesized improvement motivated by OOD detection literature" with a dedicated ablation (CLSAS-full vs. CLSAS-Euclidean). A "Critical clarification" section makes this transparent.

3. **Minimum viable scope**: Defined a concrete 9-day plan (Days 1-2: timing validation, Days 3-4: core implementation, Days 5-6: baselines, Days 7-8: 2x2 ablation grid, Day 9: writing). Dropped: COAST combination, Qwen3-8B, full 7-benchmark suite for ablations, FASB-trigger ablation. Added fallback: if timing hypothesis fails entirely, pivot to findings-track detection paper.

4. **Timing hypothesis disclaimer**: Explicitly notes the Attractor Geometry paper measured at "first-digit positions before autoregressive dynamics compound" and states "transfer to open-domain settings requires further study." Three-tier fallback: sentence boundary → look-ahead (first 3 tokens) → sliding window (last 5 tokens).

**Deeper reframing**: The method is renamed from GTS to CLSAS (Claim-Level Selective Activation Steering) to center the contribution on the granularity insight rather than the geometry. The core argument is now: "intervention granularity should match evaluation granularity" — supported by PCNet's concrete evidence that token-level gating still corrupts >50% of correct text.

```json
{
  "change_type": "major",
  "title": "Claim-Level Selective Activation Steering for Factual Hallucination Suppression in Long-Form Generation",
  "core_problem": "Factual hallucination in LLMs has spurred a proliferation of geometry-aware detection and activation steering methods, yet a fundamental granularity mismatch persists: detection and intervention operate at token level, while factual evaluation operates at claim/sentence level. PCNet (May 2026) exemplifies this—its probabilistic-circuit gating achieves near-perfect detection AUROC yet still corrupts 53.7% of originally correct generations when intervening at every deviant token, because token-level decisions cannot distinguish 'this token is anomalous within an otherwise correct claim' from 'this claim is genuinely hallucinated.' FASB (NeurIPS 2025) addresses selective steering but operates correctively—detecting deviation after tokens are generated, then backtracking 10 tokens—which wastes compute and splits coherent claims. Spherical Steering (ICML 2026) applies per-token rotation with continuous vMF-gated intensity, achieving strong TruthfulQA gains but intervening indiscriminately across all claims. The Attractor Geometry paper (May 2026) demonstrates that Euclidean geometric margin separates correct recall from hallucination (AUROC 0.858 on TruthfulQA vs. entropy 0.656), but this result is detection-only and measured at first-digit positions on factoid completion—translation into targeted intervention at appropriate granularity during multi-sentence generation remains the open challenge.",
  "opportunity": "The unexploited sweet spot is pre-emptive claim-level gating: sentences are the natural unit of factual claims—the granularity FActScore evaluates, the granularity humans judge, and the granularity at which LLMs integrate context before next-sentence planning (supported by 'Think in Sentences,' April 2026). The key evidence that this granularity matters comes from PCNet's results: despite near-perfect token-level detection (AUROC up to 99% on extractive QA), its token-level intervention still corrupts 53.7% of correct generations and preserves only 79.3%. This is because anomaly at individual token positions does not reliably indicate that the entire claim is hallucinated—a high-NLL token may be stylistically unusual but factually correct, or may be part of a partially correct claim that token-level correction damages. A system that makes binary steer/skip decisions at sentence boundaries—preserving entire correct claims untouched while steering only claims where the model lacks factual grounding—can achieve higher preservation rates by avoiding sub-claim intervention entirely. The three-part framework (when: sentence boundaries; whether: geometric distance trigger; how much: per-layer intensity) addresses limitations in all current methods: PCNet's token-level corruption, FASB's corrective backtracking overhead, Spherical Steering's indiscriminate application, and Hallucination Basins' per-sequence uniformity.",
  "landscape": "**Selective geometric gating (primary competitors):**\n\n*PCNet (arXiv 2605.05953, May 2026)* is the closest concurrent work sharing the 'detect geometric anomaly → selectively intervene' paradigm. PCNet trains a Probabilistic Circuit as a density estimator over MLP-compressed residual stream states (4096→128 dims), computes exact NLL as anomaly score, and triggers PC-LDCD (contrastive decoding) only at deviant tokens. Results: TruthfulQA MC1 0.51 / MC2 0.65 on Llama-3.1-8B; near-perfect detection AUROC on extractive QA; corruption rate 53.7%, preservation rate 79.3%. Overhead: <2% for PC scoring, but 3.3–6.2 additional block evaluations per anomalous token for lookahead. CLSAS differs in three fundamental ways: (a) Granularity: sentence-level binary decisions preserve entire correct claims and avoid sub-claim corruption. PCNet evaluates NLL at every token, meaning intervention can damage partially correct claims—evidenced by its 53.7% corruption rate despite near-perfect detection. CLSAS's claim-level atomicity should achieve substantially lower corruption. (b) Intervention mechanism: activation steering shifts the model's own generation distribution toward factual attractors in a single forward pass, while contrastive decoding requires maintaining lookahead evaluations for top-k candidates at every anomalous position (PCNet's IGR ranges 0.41–0.78, meaning lookahead triggers at 41–78% of tokens). On long-form generation where many tokens are flagged, CLSAS's steering-only approach avoids this per-token lookahead cost. (c) Trigger interpretability: Euclidean/Mahalanobis distance from factual cluster centroids has a clear geometric interpretation (distance in representation space), while NLL from a trained probabilistic circuit is a learned density estimate whose failure modes are less transparent.\n\n*FASB (arXiv 2508.17621, NeurIPS 2025)* is the most direct prior work on 'when to steer,' using linear probes trained on attention head activations. It monitors concatenated question-and-generated-content states, triggers intervention when deviation is detected, and backtracks s=10 tokens to regenerate with steering. MC1 48.71% on TruthfulQA (LLaMA-2-7B-Chat). CLSAS differs in: (a) pre-emptive gating at sentence boundaries (no wasted tokens, no rollback) vs. FASB's corrective backtracking; (b) geometric distance trigger measuring knowledge absence vs. learned directional alignment on attention heads; (c) atomic claim-level decisions vs. token-level cuts that may split coherent claims. FASB's backtracking overhead scales linearly with intervention frequency—compounding on hallucination-dense long-form passages.\n\n**Geometry-aware steering (per-token):** Spherical Steering (arXiv 2602.08169, ICML 2026) uses geodesic rotation with a von Mises-Fisher confidence gate, achieving MC1 +15.80% on TruthfulQA (Llama-3.1-8B) with single-layer intervention (layer 24). Code released at github.com/chili-lab/Spherical-Steering. Per-token with continuous intensity—no claim-level selectivity. Hallucination Basins (arXiv 2604.04743, April 2026) proposes Adaptive Geometry-Aware Steering using Euclidean distance triggers and logistic-regression scalar maps at per-sequence granularity (uniform across all claims). Tested on 1B–8B models. CLSAS advances beyond both via within-sequence sentence-level selectivity.\n\n**Context-dependent directions:** Steering Vector Fields (SVF, arXiv 2602.01654, Feb 2026) learns differentiable concept-scoring MLPs for context-aware steering directions refreshed every K steps. Always steers—no gating. Complementary to CLSAS (CLSAS decides whether; SVF decides in which direction).\n\n**Utility preservation:** COAST (arXiv 2605.01167, May 2026) formalizes collateral damage as unintended feature-direction shifts and optimizes the steering vector via constrained optimization. Complementary to CLSAS (COAST optimizes the vector; CLSAS optimizes when to apply it).\n\n**Nonlinear geometry:** Curveball Steering (arXiv 2603.09313, March 2026) demonstrates substantial geometric distortion in activation spaces, supporting covariance-aware (Mahalanobis) over Euclidean distance.\n\n**Detection-only:** Attractor Geometry of Transformer Memory (arXiv 2605.05686, May 2026) demonstrates hallucination = basin absence with Euclidean geometric margin AUROC 0.858 on TruthfulQA (vs. entropy 0.656), 0.993 on controlled factoid tasks. All measurements at first-digit positions before autoregressive dynamics compound; the paper explicitly states 'transfer to open-domain settings requires further study.' Where Does Reasoning Break? (arXiv 2605.13772, May 2026) detects step-level hallucination via transport geometry. DRIFT (arXiv 2601.14210, Jan 2026) detects representational instability.\n\n**Calibration:** Calibrating Verbal Uncertainty (Ji et al., EMNLP 2025 Outstanding Paper) achieves ~31.9% reduction in confident hallucinations via linear-feature intervention—calibrates expression, does not correct generation.\n\n**Other steering:** ACT (WWW 2025), ODESteer (ICLR 2026, +5.7% over ACT), Guiding Giants/WAS (arXiv 2505.20309), SADI (arXiv 2410.12299), HELIX/Tethered Reasoning (arXiv 2602.17691). FLAS (arXiv 2605.05892, May 2026) learns concept-conditioned velocity fields for multi-step activation transport.\n\n**Supporting evidence:** Hallucination as Trajectory Commitment (arXiv 2604.15400, April 2026) provides causal evidence for early commitment with asymmetric attractor dynamics—supporting timely intervention before commitment propagates. Think in Sentences (arXiv 2604.10135, April 2026) demonstrates sentence boundary attention concentration patterns.",
  "approach": "We propose Claim-Level Selective Activation Steering (CLSAS), a method that bridges the granularity gap between token-level detection/intervention and claim-level factual evaluation. The central insight is that intervention granularity should match evaluation granularity: since factuality is assessed per-claim (FActScore, human judgment), steering decisions should be made per-claim—preserving entire correct sentences untouched while steering only sentences where the model lacks factual grounding.\n\n**Stage 1: TRIGGER (Geometric Distance at Sentence Boundaries)**\nDuring generation, at each sentence boundary (period/newline tokens), extract hidden-state activations at the boundary token across layers using nnsight intervention hooks. Compute geometric distance from factual cluster centroids:\n(a) Offline: From a calibration set (~2K examples from TruthfulQA + FELM correct-answer forward passes), collect hidden states at factual completion positions. Apply PCA to project from full hidden dimension (d=4096) to top-k principal components (k=256), yielding a well-conditioned 256×256 covariance matrix.\n(b) Online: Project the boundary token's activation into the PCA subspace. Compute distance to nearest factual centroid. We evaluate two distance metrics: (i) Euclidean distance δ_E(x) = ||h_pca − μ_pca||₂, matching the Attractor Geometry paper's validated metric (AUROC 0.858 on TruthfulQA); (ii) Mahalanobis distance δ_M(x) = √((h_pca − μ_pca)ᵀ Σ_pca⁻¹ (h_pca − μ_pca)), a hypothesized improvement motivated by OOD detection literature (Lee et al., NeurIPS 2018) that accounts for directional anisotropy in representation space.\n(c) When distance exceeds a calibrated threshold (set via precision-recall analysis targeting high precision ≥0.85 to minimize false interventions), flag the upcoming sentence for steering.\n\n**Critical clarification:** The 0.858 AUROC motivating this trigger was achieved with Euclidean distance on first-digit positions during factoid completion (Attractor Geometry, May 2026). Our application to sentence boundaries during multi-sentence open-ended generation is an extrapolation that we explicitly validate as Milestone 1. The Attractor Geometry authors note 'transfer to open-domain settings requires further study.' If Mahalanobis does not significantly outperform Euclidean in our ablation, the primary novelty contribution rests on claim-level selective gating itself—which remains differentiated from all baselines regardless of distance metric.\n\n**Timing Hypothesis Validation (Milestone 1, Days 1-2):**\nWe explicitly frame the following as a testable hypothesis: geometric distance at sentence boundary N is predictive of factual accuracy in sentence N+1. Validation protocol: (1) Generate 500 multi-sentence responses on LongFact/FActScore prompts using Llama-3.1-8B-Instruct. (2) Compute both Euclidean and Mahalanobis distance at every sentence boundary. (3) Annotate each subsequent sentence with FActScore. (4) Measure Spearman correlation between boundary distance and next-sentence factuality, and AUROC for binary classification. If AUROC < 0.70, we implement a look-ahead variant: extract distance from the first 3 generated tokens of the new sentence (before committing via speculative-style buffering). The look-ahead variant adds ~15% latency overhead but operates before the sentence is visible to the user. If look-ahead also fails (AUROC < 0.65), we fall back to a sliding-window approach using the mean distance over the last 5 tokens before the boundary.\n\n**Comparison to PCNet's trigger:** PCNet uses NLL from a trained probabilistic circuit as its anomaly score, evaluated at every token. This achieves near-perfect detection on extractive QA but still yields 53.7% corruption on correct generations. We hypothesize this is because token-level anomaly conflates stylistic deviation with factual error. Our sentence-level trigger aggregates geometric information at natural claim boundaries, making a single binary decision per claim—either the model has factual grounding for this claim (skip) or it doesn't (steer). This avoids sub-claim intervention entirely.\n\n**Stage 2: DIRECTION (Centroid-Directed Steering Vector)**\nCompute the steering direction as the unit vector from the current activation toward the factual cluster centroid at each layer in the PCA subspace, then project back to full space: v_steer = (μ_pca − h_pca) / ||μ_pca − h_pca||, lifted back to full dimensionality via PCA inverse transform. This yields an input-specific correction direction toward regions of successful fact recall.\n\n**Stage 3: INTENSITY (Per-Layer Weighted Steering)**\nA lightweight 2-layer MLP controller (hidden dim 64, inspired by Guiding Giants/WAS) takes [geometric_distance, layer_index/L, distance_velocity] as input (3D feature vector) and predicts per-layer steering weight λ_ℓ. Trained on a calibration set (~2K examples) to maximize FActScore on steered outputs while minimizing perplexity increase on non-flagged outputs. Steering: h_steered(ℓ) = h(ℓ) + λ_ℓ · v_steer(ℓ) at layers where λ_ℓ > ε.\n\n**Minimum Viable Scope (9 days, May 16–25):**\n- Days 1-2 (May 16-17): Timing hypothesis validation on Llama-3.1-8B-Instruct. This is the critical-path milestone—if it fails, immediately implement look-ahead variant.\n- Days 3-4 (May 18-19): Core CLSAS implementation + calibration. Run TruthfulQA and SimpleQA.\n- Days 5-6 (May 20-21): Run baselines (Spherical Steering from released code, FASB from released code). Run FActScore and MT-Bench on CLSAS.\n- Days 7-8 (May 22-23): Key ablations: 2×2 grid (Euclidean vs Mahalanobis × sentence-level vs token-level gating) on 4-benchmark core set. PCNet comparison if code is available; otherwise use reported numbers with matched model.\n- Day 9 (May 24): Writing, formatting, submission buffer.\n- Dropped from scope: COAST combination experiment, Qwen3-8B (secondary model), full 7-benchmark suite for ablations, GTS-FASB-trigger ablation.\n\n**Ablation Design (MVP):**\n- CLSAS-full vs. CLSAS-Euclidean (isolate Mahalanobis contribution)\n- CLSAS-full vs. CLSAS-pertoken (apply continuous per-token gating with our distance metric, matching PCNet/Spherical Steering's granularity—isolates the claim-level contribution)\n- CLSAS-full vs. CLSAS-sequence (single decision per sequence, matching Hallucination Basins' granularity)\n- CLSAS-full vs. CLSAS-scalar (replace per-layer MLP with single scalar, isolating controller contribution)\n- Direct comparison: CLSAS-full vs. Spherical Steering vs. FASB vs. PCNet (reported numbers if code unavailable)\n\n**Primary evaluation metrics:**\n- Corruption rate and preservation rate (matching PCNet's protocol): fraction of correct claims degraded / preserved by intervention\n- FActScore on long-form biographies (primary benchmark where claim-level advantage should be largest)\n- TruthfulQA MC1/MC2, SimpleQA accuracy, MT-Bench score\n- Intervention rate: fraction of sentences steered (lower is better for comparable factuality gains)\n- Latency overhead vs. baselines\n\nImplementation uses nnsight 0.7 on Llama-3.1-8B-Instruct. Qwen3-8B included only if time permits after MVP completion.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~120h H100 80GB",
      "gpu_utilization": "Low (~15-20%)",
      "timeline": "3-4 months",
      "team": "1-2 researchers with mechanistic interpretability + geometric ML experience",
      "estimated_gpu_cost": "$360-400",
      "factScore_api_cost": "$100-200"
    },
    "human_in_loop": {
      "gpu_hours": "~130h H100 80GB",
      "gpu_utilization": "Moderate (45-55%)",
      "timeline": "2-3 weeks",
      "team": "1 researcher, ~30min/day reviewing proposals",
      "claude_api_cost": "$150-250",
      "estimated_gpu_cost": "$390-430",
      "factScore_api_cost": "$100-200",
      "risk_note": "Timing hypothesis validation is critical-path. If it fails (AUROC < 0.70), look-ahead fallback adds ~3 days."
    },
    "auto_research": {
      "gpu_hours": "~140h H100 80GB",
      "gpu_utilization": "High (~85-90%)",
      "timeline": "9 days (May 16-25) with 2 H100 GPUs. Minimum viable paper scope: single model (Llama-3.1-8B), 4-benchmark core set for ablations, full baselines on FActScore+TruthfulQA+SimpleQA+MT-Bench.",
      "team": "0 (initial setup: provision GPUs, configure nnsight 0.7, clone Spherical Steering + FASB repos)",
      "claude_api_cost": "$250-350 (est. 3000-4000 turns)",
      "estimated_gpu_cost": "$420-450",
      "factScore_api_cost": "$100-200",
      "speed_bottleneck": "Timing hypothesis validation (days 1-2) is critical path. If it fails, look-ahead variant must be implemented immediately. Secondary: FActScore GPT-4 API calls.",
      "resource_optimization": "Budget achieved via: (1) single model (Llama-3.1-8B) for all experiments; (2) 4-benchmark core set (TruthfulQA, FActScore, SimpleQA, MT-Bench); (3) 2×2 ablation grid (distance metric × gating granularity) instead of separate sweeps; (4) use Spherical Steering and FASB released code directly; (5) PCNet comparison using reported numbers if code unavailable.",
      "minimum_viable_paper": "If timing hypothesis fails AND look-ahead also fails: pivot to a detection-only contribution (sentence-level geometric detection benchmark) comparing Euclidean/Mahalanobis at sentence boundaries vs. PCNet's token-level NLL. This is publishable as a shorter paper (findings track).",
      "risk_note": "Primary risk: timing hypothesis may fail (Attractor Geometry paper validated only on factoid completion at first-digit positions, explicitly disclaiming open-domain transfer). Mitigation: look-ahead variant, then sliding-window fallback. Secondary risk: claim-level gating may not outperform PCNet's token-level gating on short-form QA—advantage expected primarily on long-form generation (FActScore, LongFact). Tertiary risk: 9-day timeline leaves zero buffer for unexpected implementation issues."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026)"
  ],
  "level": "top-tier",
  "key_references": [
    "Hallucination as an Anomaly: Dynamic Intervention via Probabilistic Circuits (PCNet, arXiv 2605.05953, May 2026)",
    "Steering When Necessary: Flexible Steering Large Language Models with Backtracking (FASB, arXiv 2508.17621, NeurIPS 2025)",
    "Spherical Steering: Geometry-Aware Activation Rotation for Language Models (arXiv 2602.08169, ICML 2026)",
    "Attractor Geometry of Transformer Memory: From Conflict Arbitration to Confident Hallucination (arXiv 2605.05686, May 2026)",
    "Hallucination Basins: A Dynamic Framework for Understanding and Controlling LLM Hallucinations (arXiv 2604.04743, April 2026)",
    "Steering Vector Fields for Context-Aware Inference-Time Control in Large Language Models (SVF, arXiv 2602.01654, Feb 2026)",
    "Curveball Steering: The Right Direction To Steer Isn't Always Linear (arXiv 2603.09313, March 2026)",
    "Minimizing Collateral Damage in Activation Steering (COAST, arXiv 2605.01167, May 2026)",
    "Beyond Steering Vector: Flow-based Activation Steering for Inference-Time Intervention (FLAS, arXiv 2605.05892, May 2026)",
    "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations (Ji et al., EMNLP 2025 Outstanding Paper, arXiv 2503.14477)",
    "Tethered Reasoning (HELIX): Decoupling Entropy from Hallucination in Quantized LLMs via Manifold Steering (arXiv 2602.17691, Feb 2026)",
    "Adaptive Activation Steering: A Tuning-Free LLM Truthfulness Improvement Method (ACT, WWW 2025)",
    "ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment (ICLR 2026, arXiv 2602.17560)",
    "Where Does Reasoning Break? Step-Level Hallucination Detection via Hidden-State Transport Geometry (arXiv 2605.13772, May 2026)",
    "DRIFT: Detecting Representational Inconsistencies for Factual Truthfulness (arXiv 2601.14210, Jan 2026)",
    "Guiding Giants: Lightweight Controllers for Weighted Activation Steering in LLMs (arXiv 2505.20309, May 2025)",
    "Hallucination as Trajectory Commitment: Causal Evidence for Asymmetric Attractor Dynamics (arXiv 2604.15400, April 2026)",
    "Think in Sentences: Explicit Sentence Boundaries Enhance Language Model's Capabilities (arXiv 2604.10135, April 2026)",
    "A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks (Lee et al., NeurIPS 2018)",
    "Semantics-Adaptive Activation Intervention for LLMs via Dynamic Steering Vectors (SADI, arXiv 2410.12299, 2024)",
    "Dynamic Multimodal Activation Steering for Hallucination Mitigation in Large Vision-Language Models (ICLR 2026)"
  ],
  "description": "We propose Claim-Level Selective Activation Steering (CLSAS), a method that bridges the granularity gap between token-level hallucination detection/intervention and claim-level factual evaluation. The central insight is that intervention granularity should match evaluation granularity: since factuality is assessed per-claim (FActScore, human judgment), steering decisions should be per-claim—preserving entire correct sentences untouched while steering only claims where the model lacks factual grounding.\n\nThe motivation is concrete: PCNet (May 2026), the state-of-the-art in selective geometric gating, achieves near-perfect token-level hallucination detection (AUROC up to 99% on extractive QA) yet still corrupts 53.7% of originally correct generations when intervening token-by-token via contrastive decoding. We hypothesize this corruption stems from the granularity mismatch—token-level anomaly conflates stylistic deviation with factual error, and sub-claim interventions damage partially correct claims.\n\nCLSAS monitors geometric distance from residual stream activations to factual cluster centroids at sentence boundaries during generation. Building on the finding that Euclidean geometric margin separates correct recall from hallucination (AUROC 0.858 on TruthfulQA; Attractor Geometry, May 2026), we evaluate both Euclidean and Mahalanobis distance triggers—the latter a hypothesized improvement motivated by OOD detection literature (Lee et al., NeurIPS 2018) that we validate via ablation. When distance indicates basin absence, CLSAS computes an input-specific steering vector toward the factual centroid and applies it with per-layer weights from a lightweight MLP controller. Sentences within a factual basin are left entirely untouched.\n\nCLSAS addresses limitations in the closest concurrent work: (1) vs. PCNet (May 2026, MC1 0.51 on Llama-3.1-8B), CLSAS makes sentence-level binary decisions that avoid sub-claim corruption. PCNet's token-level NLL gating triggers at 41-78% of tokens (IGR), requiring costly lookahead evaluations at each; CLSAS intervenes only at sentence boundaries. (2) vs. FASB (NeurIPS 2025, MC1 48.71% on LLaMA-2-7B-Chat), CLSAS is pre-emptive—gating before generation rather than detecting deviation and rolling back 10 tokens. (3) vs. Spherical Steering (ICML 2026, +15% MC1), CLSAS makes binary claim-level steer/skip decisions rather than continuous per-token rotation, enabling complete preservation of correct claims. (4) vs. Hallucination Basins (April 2026), CLSAS provides within-sequence selectivity rather than uniform per-sequence correction.\n\nWe explicitly validate the timing hypothesis (distance at boundary N predicts factuality of sentence N+1) as Milestone 1 with a correlation study, noting the Attractor Geometry paper's disclaimer that results were measured at first-digit positions and 'transfer to open-domain settings requires further study.' A look-ahead fallback is specified if correlation is insufficient. We hypothesize CLSAS's advantage over token-level methods will be strongest on long-form generation (FActScore) where multiple claims coexist and token-level corruption compounds.\n\nMinimum viable scope for 9 remaining days: single model (Llama-3.1-8B-Instruct), 4-benchmark evaluation (TruthfulQA, FActScore, SimpleQA, MT-Bench), 2×2 ablation grid (distance metric × gating granularity), direct comparison with Spherical Steering and FASB using released code. Total budget: ≤140 H100-hours.",
  "project_name": "claim_level_selective_steering",
  "source": "web_research"
}
```

Sources:
- [PCNet: Hallucination as an Anomaly](https://arxiv.org/abs/2605.05953)
- [PCNet HTML (detailed methodology)](https://arxiv.org/html/2605.05953)
- [Attractor Geometry of Transformer Memory](https://arxiv.org/abs/2605.05686)
- [Spherical Steering (ICML 2026)](https://arxiv.org/abs/2602.08169)
- [Spherical Steering GitHub](https://github.com/chili-lab/Spherical-Steering)
- [FASB: Steering When Necessary (NeurIPS 2025)](https://arxiv.org/abs/2508.17621)
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [SENTINEL: Sentence-Level Early Intervention](https://arxiv.org/abs/2507.12455)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a712db9-273a-4022-8001-c73cf6d1f604",
  "isSidechain": false,
  "requestId": "req_011Cb5zicxkSg95NRYxePkmT",
  "type": "assistant",
  "uuid": "5559b4de-5b26-48b0-8584-c87cef8a9331",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014LKAHFzrYX3bau6SuNsEtY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17228,
      "cache_read_input_tokens": 45074,
      "output_tokens": 8134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17228,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8134,
          "cache_read_input_tokens": 45074,
          "cache_creation_input_tokens": 17228,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17228
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

_source line 71_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-16 (UTC).**  ## Original idea {   \"title\": \"Geometry-Triggered Sentence-Level Activation Steering for Factual Hall…",
  "leafUuid": "5559b4de-5b26-48b0-8584-c87cef8a9331",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c"
}
```

---

### Runtime record

_source line 72_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise GTS with PCNet differentiation and realistic timeline",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c"
}
```

---

### Runtime record

_source line 73_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-16 (UTC).**  ## Original idea {   \"title\": \"Geometry-Triggered Sentence-Level Activation Steering for Factual Hall…",
  "leafUuid": "5559b4de-5b26-48b0-8584-c87cef8a9331",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c"
}
```

---

### Runtime record

_source line 74_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise GTS with PCNet differentiation and realistic timeline",
  "sessionId": "50176f91-6e24-4baa-8fdc-ff59abed166c"
}
```

---
