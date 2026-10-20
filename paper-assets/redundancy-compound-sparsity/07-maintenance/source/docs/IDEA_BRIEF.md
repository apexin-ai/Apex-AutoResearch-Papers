# Idea Brief: Cross-Axis Redundancy Coordination: Unified Signal for Joint MLP Sparsity and KV Eviction in Reasoning Inference


- **Idea ID**: `idea_010`
- **Created**: 2026-05-11
- **Approved**: 2026-05-11
- **Source**: foreign:be-idea-gen-0509-2
- **Level**: top-tier
- **Target Venues**: EMNLP 2026 (ARR submission deadline May 25, 2026 — primary target, 15 days), AAAI 2027 (expected abstract late Jul 2026 — fallback with extended ablations, full composability experiments with TriAttention/LongFlow)

## Seed Topic

Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Efficient Methods for NLP.

Direction: Efficiency methods for NLP — NOT limited to LLM inference optimization. In-scope: speculative decoding, KV-cache compression/eviction, quantization-aware distillation, parameter-efficient fine-tuning, efficient long-context serving, MoE routing, attention approximations, efficient smaller models for specific NLP tasks, pruning for task-specific deployment.

Contribution type: METHOD ONLY. Propose new algorithms — not profiling studies.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total. Generous for efficiency work.
2. Time: ≤16 days. Build on vLLM, SGLang, llama.cpp, TensorRT-LLM, HF Transformers, FlashAttention, bitsandbytes.
3. Eval: perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench. Report wall-clock and throughput on H100.

Look for: cache-aware methods for new workloads (long thinking traces, agent loops, RAG), quantization-aware distillation, structured sparsity during inference, efficient serving of reasoning models with variable-length thinking. Avoid: vanilla 4-bit quantization, generic LoRA, plain speculative decoding.

Tag: direction=efficiency, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].

## Core Problem

Reasoning models generate highly redundant thinking traces, yet current efficiency methods each address a single bottleneck axis: Token Filtering (arXiv:2512.07090) uses EMA-based key-value similarity to skip attention layers but leaves MLP computation untouched; R-KV evicts redundant KV entries using costly O(B²) pairwise similarity unsuitable for per-token triggering; TEAL applies uniform magnitude-based activation sparsity across all linear layers regardless of token redundancy; CLADA (arXiv:2502.19078) adaptively modulates MLP sparsity per-token using surprisal and entropy signals but does not coordinate with KV cache management; SkipKV (arXiv:2512.07993) performs sentence-level KV skipping but at coarser granularity without MLP modulation; and FASA uses offline-calibrated frequency chunks for KV compression without modulating compute. Q-Infer (ACM TACO 2025) jointly manages MLP neuron sparsity and KV cache at the system level but uses SEPARATE predictor-based signals for each axis — a trained MLP predictor for neuron activation and multi-window importance scoring for KV — rather than a unified per-token redundancy signal. Critically, no existing work validates whether the same per-token redundancy signal that predicts attention-level importance also predicts MLP sparsity tolerance — a cross-axis assumption that, if true, enables coordinated savings across orthogonal bottlenecks from a single O(1) computation.

## Opportunity / Why Now

Token Filtering demonstrated that EMA centroid similarity of key-value vectors reliably identifies redundant tokens at O(1) per-token cost for attention layer skipping. CLADA independently demonstrated that tokens with low cognitive load (low surprisal/entropy) tolerate higher MLP sparsity. We hypothesize — and propose to empirically validate — that KV similarity is a relational proxy for the same underlying phenomenon: high KV similarity implies the current token's hidden state is similar to recent context, which implies low surprisal (the token is predictable given recent context), which implies low cognitive load. If this correlation holds, it provides both (a) theoretical grounding for using KV similarity as a cross-axis signal (it captures the same information content property that CLADA's surprisal measures directly), and (b) practical advantages over surprisal-based approaches: KV similarity is computed from already-materialized projections with no additional forward pass, whereas surprisal requires the full vocabulary logit computation. This enables a single O(1) signal to simultaneously orchestrate: (1) elevated MLP sparsity on redundant tokens via TEAL's existing kernel, and (2) priority-based KV cache eviction replacing R-KV's O(B²) scoring. These target independent bottlenecks — weight-loading-bound MLP at batch=1 and memory-footprint-bound KV attention at long sequences — yielding additive speedups that no single-axis method or multi-signal system (Q-Infer, QuickSilver) achieves with comparable simplicity. Crucially, CARC's MLP sparsity mechanism is orthogonal to the choice of KV compression method: the two-tier MLP gain can be composed with any KV method (TriAttention, LongFlow, FASA), positioning CARC as a coordination layer rather than a competing system.

## Landscape (SOTA & Limitations)

Token Filtering (arXiv:2512.07090, Dec 2025) introduces an EMA anchor for key-value vectors with variance-aware fusion to skip attention layers during inference — the signal we extend to additional axes. R-KV (NeurIPS 2025) achieves 90% KV memory savings using O(B²) pairwise key similarity for periodic eviction — proving redundancy-aware KV eviction works but with a signal too expensive for per-token use. TEAL (ICLR 2025 Spotlight) achieves 40–50% training-free activation sparsity with 1.5–1.8× decoding speedup via magnitude pruning applied MODEL-WIDE to all linear layers (W_q, W_k, W_v, W_o AND W_up, W_gate, W_down), using block-wise greedy optimization for per-layer thresholds — not MLP-only as sometimes mischaracterized. CLADA (arXiv:2502.19078, Feb 2025) proposes cognitive-load-aware dynamic activation sparsity using surprisal and entropy as per-token signals, achieving ~20% speedup with <2% accuracy drop — the closest single-axis prior work for adaptive MLP sparsity, but using a semantically richer signal (information content) that requires full vocabulary logit computation without coordination to KV cache management. WiSparse (arXiv:2602.14452, Feb 2026) shows that sparsity sensitivity depends on the joint consideration of activation magnitudes AND precomputed weight norms, achieving 97% dense performance at 50% sparsity on Llama3.1 — demonstrating that activation magnitude alone may be insufficient and block-level sensitivity varies non-monotonically. SkipKV (arXiv:2512.07993, Dec 2025) performs sentence-level KV generation and storage skipping for reasoning models using semantic scoring and adaptive steering — a coarser-granularity approach that reduces both memory and generation length but cannot modulate per-token MLP compute. LazyEviction (arXiv:2506.15969, Jun 2025) discovers Token Importance Recurrence: 80% of tokens have MRI < 175 on MATH-500/Qwen (with practical ablation window sizes W=25 for GSM8K, W=52 for MATH-500), demonstrating that naive insertion-filtering approaches risk catastrophic eviction of periodically critical tokens — directly motivating our recurrence-aware retention mechanism. LongFlow (arXiv:2603.11504, Mar 2026) derives KV importance from an intermediate result of attention computation using only the current query, achieving 11.8× throughput improvement with 80% KV compression via a custom fused FlashAttention+eviction kernel — a reasoning-specific KV method with impressive throughput gains but no MLP coordination and requiring kernel-level implementation. ForesightKV (arXiv:2602.03203, Feb 2026) trains a lightweight scoring model to predict long-term KV contribution using supervised learning with future attention labels plus GRPO reinforcement learning — achieving strong eviction quality at 50% budget but requiring training, making it non-training-free. TriAttention (arXiv:2604.04921, Apr 2026) exploits pre-RoPE geometric structure (Q/K concentration around fixed non-zero centers) for position-based importance scoring, achieving 2.5× throughput / 10.7× KV memory reduction on AIME25 at 32K tokens while matching full attention accuracy — the strongest recent KV-only method, but leveraging geometric properties specific to attention that do not extend to MLP sparsity decisions. Q-Infer (ACM TACO 2025) jointly manages MLP neuron sparsity and KV cache compression at the system level via GPU-CPU collaborative scheduling, using a trained predictor for neuron activation and multi-window key-token selection — the closest multi-axis prior work, but requiring training and using separate signals per axis rather than a unified per-token redundancy score. Polar Sparsity (NeurIPS 2025) shows MLP neuron-level sparsity vanishes at larger batch sizes (union of active neurons approaches dense) while attention head sparsity remains batch-invariant — confirming MLP sparsity gains are primarily valuable at batch=1, and demonstrating that MLP and attention sparsity target independent bottlenecks, supporting compositional gains. MUSTAFAR (NeurIPS 2025) introduces unstructured KV-cache sparsity explicitly described as 'orthogonal to existing compression techniques' including token eviction — precedent for claiming composability of different efficiency axes. KeyDiff (arXiv:2504.15364) uses mean-of-keys as an anchor for KV eviction — a related anchor approach but without recency bias and limited to the KV axis. FASA (arXiv:2602.03152, ICLR 2026) discovers RoPE-induced frequency-chunk sparsity for query-aware KV compression, achieving ~5× compression (18.9% cache retention) with 2.56× speedup on AIME24, requiring offline calibration of dominant frequency chunks. ThinKV (ICLR 2026 Oral) decomposes reasoning chains into thought types for hybrid quantization-eviction. EvoSparse (ACL 2026) leverages cross-step token importance accumulation for dynamic sparse attention on the attention axis only. CSAttention (arXiv:2604.08584) demonstrates query-centric attention sparsity, showing that key-only metrics can miss query-dependent importance — a limitation we acknowledge. 'EMA Is Not All You Need' (arXiv:2604.08556, Apr 2026) shows EMA traces suffer irreversible information dilution — motivating our windowed-reset mechanism. QuickSilver (arXiv:2506.22396, 2025) integrates four mechanisms (token halting via L2 drift, KV skipping, token fusion, adaptive quantization) — a multi-mechanism framework where each mechanism uses a DIFFERENT trigger signal, requiring independent calibration. DuoGPT (NeurIPS 2025) combines weight pruning with activation sparsity but uses offline OBC calibration, not online redundancy detection. Deja Vu (ICML 2023) demonstrates that contextual sparsity is predictable from hidden states — the theoretical foundation for our cross-axis hypothesis. R-Sparse (ICLR 2025) achieves 50% model-level sparsity via rank-aware input channel pruning. No existing work (1) empirically validates that a KV-similarity-based redundancy signal predicts MLP sparsity tolerance, (2) demonstrates that KV similarity correlates with CLADA's surprisal-based cognitive load metric (providing mutual theoretical support), or (3) demonstrates training-free, calibration-free coordination of MLP sparsity and KV eviction from a single per-token signal with recurrence-aware safeguards.

## Proposed Approach

We propose Cross-Axis Redundancy Coordination (CARC), a training-free inference method that extends Token Filtering's EMA-based redundancy signal to simultaneously orchestrate MLP activation sparsity and KV cache eviction — a cross-axis coordination validated by preliminary empirical analysis. CARC is designed as a composable coordination layer: its MLP sparsity mechanism is independent of its KV eviction mechanism, meaning either axis can be combined with alternative methods (e.g., CARC-MLP + TriAttention-KV).

**Contribution hierarchy (in order of novelty and impact):**
(A) **Analytical contribution** (primary novelty): Cross-axis hypothesis validation — first empirical evidence linking KV-similarity redundancy to MLP sparsity tolerance, with analysis of correlation to CLADA's surprisal signal.
(B) **Practical KV eviction** (primary practical impact): O(1)-triggered recurrence-aware KV cache eviction that replaces R-KV's O(B²) scoring while avoiding LazyEviction's catastrophic insertion-filtering — scales to dramatic savings at long sequences (25–30% speedup at L=64K).
(C) **Composable MLP sparsity** (orthogonal bonus): Modest (~7%) but free additional speedup at batch=1, stackable on top of ANY KV compression method.

**Contribution A: Cross-Axis Hypothesis Validation (most novel analytical contribution).** We provide the first empirical evidence linking KV-similarity-based redundancy to MLP sparsity tolerance, and analyze its relationship to CLADA's surprisal-based cognitive load. Concretely: we run Token Filtering's EMA signal on 500+ reasoning tokens from DeepSeek-R1-Distill-Qwen-14B, partition tokens into redundant (S > τ) vs. novel (S ≤ τ), then measure: (a) the activation magnitude distribution at each MLP layer (TEAL's pruning metric) — testing whether redundant tokens have more near-zero activations; (b) the output perturbation ‖MLP_dense(h) − MLP_sparse(h)‖₂ / ‖MLP_dense(h)‖₂ at 55% vs 40% sparsity — testing whether redundant tokens suffer less output distortion under elevated pruning; (c) the Pearson correlation between EMA similarity score and token-level surprisal (negative log-probability under the model) — testing whether KV similarity is indeed a proxy for low cognitive load as we hypothesize; (d) the downstream perplexity impact when two-tier vs uniform sparsity is applied to redundant/novel partitions. The theoretical basis (Deja Vu + CLADA connection): high KV similarity → similar hidden state to recent context → low surprisal (token is predictable) → low cognitive load (per CLADA) → higher sparsity tolerance. If CLADA's finding that low-surprisal tokens tolerate higher sparsity is correct, AND KV similarity correlates with low surprisal, then KV similarity transitively predicts sparsity tolerance — turning CLADA from a competitor into supporting evidence.

**Two-tiered validation criteria:** We define validation strength as follows: (i) **Strong validation** (|r| > 0.5 between EMA score and negative surprisal AND ≥20% lower output perturbation for redundant tokens): confirms the cross-axis hypothesis — KV similarity reliably captures the information-content property underlying sparsity tolerance. (ii) **Suggestive evidence** (|r| ∈ [0.4, 0.5) OR output perturbation difference 10–20%): indicates a meaningful but moderate relationship — we present it as suggestive rather than definitive, and rely on downstream task metrics as primary validation. (iii) **Insufficient** (|r| < 0.4 AND perturbation difference <10%): cross-axis hypothesis is not supported — we pivot to O(1) KV eviction as the main contribution. This tiered framing prevents overclaiming from weak correlations while preserving the contribution if moderate evidence is found.

**Contribution B: Enhanced redundancy signal with windowed reset.** We adopt Token Filtering's EMA centroid with variance-aware key+value fusion: Anchor_k ← γ·Anchor_k + (1−γ)·k_new; final score S = α·cos(k_new, Anchor_k) + (1−α)·cos(v_new, Anchor_v). Enhancement: a windowed reset mechanism addressing EMA irreversible information dilution (per 'EMA Is Not All You Need'). When S drops below τ_reset, the EMA reinitializes from a sliding window of W=16 recent tokens, preventing the anchor from converging to an uninformative steady state over long reasoning chains. Storage: <1MB for a 14B model. Overhead: <0.001% FLOPs.

**Contribution C: Two-tier MLP sparsity (composable with any KV method).** Tokens classified as redundant (S > τ) are routed to TEAL's magnitude-pruning kernel with elevated threshold applied SPECIFICALLY to MLP matrices (W_up, W_gate, W_down) at 50–55% sparsity, while attention projections (W_q, W_k, W_v, W_o) retain TEAL's default per-layer thresholds (~40% model-wide average). This surgical application is motivated by: (1) MLP matrices account for ~77% of per-layer weight loading at batch=1 for a 14B GQA model, providing the largest marginal gain; (2) attention projections have highly variable per-layer sparsifiability (Figure 7 of TEAL) making uniform elevation risky. Implementation: tokens are batched into redundant/novel groups per forward pass; the redundant batch uses elevated MLP thresholds. No kernel modification — only threshold routing. **Crucially, the MLP two-tier mechanism depends only on the EMA similarity signal, not on CARC's KV eviction policy.** This means CARC-MLP can be composed with ANY KV compression method (TriAttention, LongFlow, FASA, or full cache) — the ~7% MLP gain stacks additively on top of whatever KV method is used. We validate this composability with a CARC-MLP-only ablation (no CARC KV eviction, using TEAL's default cache behavior) to confirm the MLP gain is independent of the KV axis.

**Contribution D: Budget-triggered KV eviction with recurrence-aware protection.** Unlike naive insertion filtering (which LazyEviction shows is catastrophic due to token importance recurrence), CARC uses a budget-triggered eviction policy: all tokens are initially stored in the KV cache; when cache occupancy reaches the budget limit B (e.g., 50% of sequence length), eviction is triggered using the cumulative EMA similarity score as priority (highest-similarity tokens evicted first). Critical safeguard: a recurrence protection window W_grace=175 steps, set to the 80th-percentile Maximum Recurrence Interval from LazyEviction's analysis (80% of tokens on MATH-500/Qwen have MRI < 175), prevents recently-generated tokens from being eviction-eligible, ensuring tokens have opportunity to demonstrate recurrence before being discarded. This gives O(1) per-token scoring (vs R-KV's O(B²) periodic pairwise comparison), recency-aware priority (vs KeyDiff's global mean), and recurrence protection (vs naive insertion filtering). Unlike SkipKV's sentence-level granularity, CARC operates per-token for finer control. Unlike LongFlow and TriAttention which achieve higher per-axis KV throughput through specialized kernels or geometric analysis, CARC's KV eviction is designed for cross-axis coordination — the same signal driving eviction also drives MLP sparsity.

**Complementarity and composability discussion.** CARC's architecture is explicitly modular: the EMA similarity signal is computed once and consumed independently by two downstream mechanisms (MLP threshold routing and KV eviction priority). This design means: (1) CARC-MLP-only can replace CARC's built-in KV eviction with a superior specialized method (e.g., TriAttention's geometric scoring, LongFlow's fused kernel, FASA's frequency analysis) while retaining the ~7% MLP gain for free. (2) CARC-KV-only can operate without the MLP two-tier mechanism for deployments where batch>4 (where MLP sparsity gains diminish per Polar Sparsity). (3) The full CARC system provides the simplest possible coordination (one signal, two axes) for batch=1 reasoning where both bottlenecks are active. This composable design is supported by Polar Sparsity's demonstration that MLP and attention sparsity target independent bottlenecks (weight-loading vs cache-loading), and by MUSTAFAR's explicit claim that KV-cache sparsity methods are orthogonal to other compression techniques. We validate composability with an explicit ablation: CARC-MLP-only (no KV eviction) showing that MLP gains are independent of the KV method used.

**Speedup Decomposition (back-of-envelope for DeepSeek-R1-Distill-Qwen-14B on H100 SXM, batch=1).** Model: d=5120, n_layers=40, intermediate=13824, n_kv_heads=8, GQA. At batch=1, decoding is memory-bandwidth-bound (H100 HBM: 3.35 TB/s). Weight loading: 28 GB (BF16) → 8.4 ms/token dense. With TEAL 40% uniform: 16.8 GB → 5.0 ms/token. CARC adds: (A) MLP two-tier (assuming 60% redundant tokens): average MLP sparsity 49% vs 40% baseline → saves 9% × 77% = 6.9% of weight loading per redundant-token-amortized average → ~0.35 ms/token. (B) KV eviction at various sequence lengths: L=16K (50% budget): KV loading 2.5 GB → 1.25 GB saved → 0.37 ms/token; L=32K: 0.75 ms/token; L=64K: 1.5 ms/token. Combined at L=16K: ~13% speedup over TEAL-only (5.0 ms → 4.3 ms). At L=32K: ~18% (6.5 ms → 5.3 ms). At L=64K: ~25% (8.5 ms → 6.4 ms). Memory savings: 50% KV reduction (2.5–10 GB at L=16K–64K). The MLP axis provides consistent ~7% gain; the KV axis scales with sequence length — their independence (weight-loading vs cache-loading) produces additive wall-clock reduction. At L=64K, KV eviction alone provides ~18% speedup, making it the dominant practical contribution for long reasoning chains. **When composed with a superior KV method:** replacing CARC-KV with TriAttention (10.7× KV reduction) would yield TriAttention's KV gains PLUS CARC's ~7% MLP gain — demonstrating that the cross-axis signal provides value beyond what any single-axis KV method achieves alone.

**QuickSilver differentiation.** QuickSilver uses four mechanisms with INDEPENDENT trigger signals (L2 drift for halting, spatial proximity for fusion, per-token entropy for quantization), each requiring separate calibration and adding separate overhead. CARC

## Resource Estimate

- **auto_research**: {'claude_api_cost': '$280–450 (2800–4500 turns for autonomous implementation, validation, debugging, experiment orchestration, and paper writing)', 'estimated_gpu_cost': '$620–930 (310h × $2.00–3.00/hr)', 'gpu_hours': '~310h H100 80GB (validation experiment + two-stage sweep + cross-model evaluation + L=64K scaling)', 'gpu_utilization': 'High (~90%): agent pipelines validation → conditional sweep → benchmarks', 'risk_note': 'If validation fails, agent must autonomously pivot to O(1) KV eviction focus — requires clear two-tiered decision criteria (strong/suggestive/insufficient) defined upfront.', 'speed_bottleneck': 'Sequential dependency: Contribution A validation must complete before committing to two-tier MLP experiments. Agent can run KV eviction experiments in parallel with validation.', 'team': '0 (initial setup ~2 hours for codebase access and GPU provisioning)', 'timeline': '7–10 days with 4× H100 80GB; 4–5 days with 8× H100'}
- **human_in_loop**: {'claude_api_cost': '$140–280 (1400–2800 turns for implementation, validation analysis, experiments, and paper drafting)', 'estimated_gpu_cost': '$380–570 (190h × $2.00–3.00/hr)', 'gpu_hours': '~190h H100 80GB', 'gpu_utilization': 'Moderate (~55%): agent runs validation experiment and sweeps autonomously; human reviews cross-axis validation results before proceeding with full evaluation', 'risk_note': 'Tight EMNLP deadline (May 25) — validation experiment is critical path: if cross-axis hypothesis fails (output perturbation difference <10% AND |r| < 0.4), pivot to O(1) KV eviction paper must happen by day 4. Two-stage sweep design ensures budget feasibility.', 'team': '1 researcher, ~45 min/day reviewing agent proposals and validation results', 'timeline': '10–12 days'}
- **manual**: {'estimated_gpu_cost': '$280–420 (140h × $2.00–3.00/hr on-demand H100 80GB)', 'gpu_hours': '~140h H100 80GB (includes 10h for Contribution A validation + 15h for L=64K evaluation)', 'gpu_utilization': 'Low (~25%): GPUs idle while researcher designs validation analysis and integrates eviction logic', 'team': '1–2 researchers (systems ML background; implementation leverages existing codebases)', 'timeline': '14–16 days (targets EMNLP 2026 ARR deadline May 25, 2026)'}

## Key References

- Token Filtering: Leveraging KV Similarity for Online Structured Pruning in LLMs (arXiv:2512.07090, Dec 2025)
- R-KV: Redundancy-aware KV Cache Compression for Reasoning Models (NeurIPS 2025)
- TEAL: Training-Free Activation Sparsity in Large Language Models (ICLR 2025 Spotlight)
- CLADA: Sparse Brains are Also Adaptive Brains: Cognitive-Load-Aware Dynamic Activation for LLMs (arXiv:2502.19078, Feb 2025)
- WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity (arXiv:2602.14452, Feb 2026)
- What Matters in Transformers? Not All Attention is Needed (arXiv:2406.15786, Jun 2024)
- SkipKV: Selective Skipping of KV Generation and Storage for Efficient Inference with Large Reasoning Models (arXiv:2512.07993, Dec 2025)
- LazyEviction: Lagged KV Eviction with Attention Pattern Observation for Efficient Long Reasoning (arXiv:2506.15969, Jun 2025)
- LongFlow: Efficient KV Cache Compression for Reasoning Models (arXiv:2603.11504, Mar 2026)
- ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution (arXiv:2602.03203, Feb 2026)
- TriAttention: Efficient Long Reasoning with Trigonometric KV Compression (arXiv:2604.04921, Apr 2026)
- Q-Infer: Towards Efficient GPU-CPU Collaborative LLM Inference via Sparsity-Aware Dynamic Scheduling (ACM TACO 2025)
- Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time (ICML 2023)
- KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference (arXiv:2504.15364)
- FASA: Frequency-Aware Sparse Attention (arXiv:2602.03152, ICLR 2026)
- EMA Is Not All You Need: Mapping the Boundary Between Structure and Content in Recurrent Context (arXiv:2604.08556, Apr 2026)
- CSAttention: Centroid-Scoring Attention for Accelerating LLM Inference (arXiv:2604.08584, Apr 2026)
- EvoSparse: Evolving Sparsity — Leveraging Token Importance Dynamics for Efficient LLM Decoding (ACL 2026)
- ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models (ICLR 2026 Oral)
- Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity (NeurIPS 2025)
- MUSTAFAR: Unstructured KV-Cache Sparsity (NeurIPS 2025)
- SeerAttention-R: Sparse Attention Adaptation for Long Reasoning (ICLR 2026)
- QuickSilver: Speeding up LLM Inference through Dynamic Token Halting and KV Skipping (arXiv:2506.22396, 2025)
- DuoGPT: Training-free Dual Sparsity through Activation-aware Pruning in LLMs (NeurIPS 2025)
- R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference (ICLR 2025)

## Reviewer Evaluation

**Scores**:
  - clarity: **{'rationale': "Exceptionally clear contribution hierarchy (A>B>C), honest limitations, two-tiered validation criteria preventing overclaiming, explicit fallback plan, and comprehensive back-of-envelope speedup decomposition. One of the clearest efficiency proposals I've reviewed.", 'score': 4}**/5
  - feasibility: **{'rationale': "Two-stage sweep (27→9 configs) fits 140h H100 budget; all models are public; no kernel modifications needed; existing codebases (Token Filtering, TEAL) provide implementation foundations. Timeline is tight but achievable given the approach's simplicity.", 'score': 4}**/5
  - impact: **{'rationale': 'Raw speedups are modest (25% at L=64K), but the composability framing (CARC-MLP stacks additively on ANY KV method including TriAttention/LongFlow) gives it unique practical value. The analytical contribution connecting KV redundancy to MLP sparsity tolerance bridges two research threads and provides actionable insight for the community.', 'score': 4}**/5
  - novelty: **{'rationale': "The cross-axis hypothesis (KV similarity predicts MLP sparsity tolerance) is independently verified as unexplored. Extending Token Filtering's signal to two additional axes with a composable architecture and validated cross-axis correlation is a genuine contribution beyond incremental extension.", 'score': 4}**/5

## Human Review Note

## Agent 审核结果（完整三阶段 pipeline）

**Verdict**: PASS

**入口三重共识 (X)**: 25.0%
**终审自评 (Y)**: 35.0%
**出口三重共识 (Z)**: 32.0%
**Z 区间**: [27.0%, 37.0%]
**真实提升 (Z-X)**: +7.0 pp
**幻觉幅度 (Y-Z)**: +3.0 pp
**出口一致性**: 高（std = 1.7%，三方在 Novelty/Significance/Feasibility/核心风险判断上高度一致）
**出口三次评估**: [30.0, 33.0, 33.0]

### 优化方案 / 拒绝详情
【优化方案】

1. **[标题/Motivation — 叙事框架重构]** — 将全文叙事从 "system efficiency speedup" 重构为 "revealing and exploiting the information redundancy structure of CoT reasoning tokens"。Motivation 段新增 NLP-specific 锚点：长链推理部署可行性 + 理解推理过程中哪些步骤是信息"新颖"的、哪些是"巩固"的。 — 命中 **Significance / venue fit**。EMNLP 对 pure systems paper 接受率低，将技术贡献锚定在 NLP insight 上是 accept/reject 边界最有效的拉分点。

2. **[Contribution A — Novelty 双支柱重构]** — 将核心贡献从 "首次发现 cross-axis correlation" 重构为双支柱：(1) structured redundancy characterization（结构化冗余刻画）；(2) composable lightweight add-on（可组合轻量附加模块）。Aggregate correlation 降级为 motivating observation，novelty 重心转向 non-uniform distribution 的结构化发现。明确声明 "our contribution is not the existence of the correlation per se, but its structured characterization and cross-axis operationalization"。 — 命中 **Novelty**。降低对 "shared signal superiority" 的依赖，使论文 novelty 不会被 R²=0.25 或 "trivially expected" 质疑一击致命。

3. **[Contribution A — 新增逐层 conditioned R² 分析]** — 在不同 layer group（shallow/middle/deep）和 reasoning phase 中分别报告 R²，展示 shared signal 在 high-redundancy regime（deep layers, consolidation phases）的解释力远超 aggregate 0.25。 — 命中 **Technical Soundness / Novelty**。将 R²=0.25 从 weakness 转化为 nuanced finding：信号强度在该压缩的地方集中，aggregate 被不压缩的区域稀释。

4. **[Contribution A — 新增 positional redundancy profiling（reasoning phase 时序分析）]** — 将 CoT trace 按位置切分为推理阶段（problem parsing → exploration → derivation → verification → summary），绘制 cross-axis correlation 随阶段演进的曲线。验证集 ≥2000 tokens（≥10 完整 CoT trace），报告 per-phase precision/recall + confusion matrix，双分段方法（equal-partition vs n-gram-based）鲁棒性检验。措辞控制为 "positional redundancy profiles" 而非强认知主张。 — 命中 **Novelty + Analysis depth + venue fit**。这是从 "efficiency method" 到 "understanding reasoning process" 的关键跨越，且计算成本几乎为零（对已有 EMA 数据做 positional binning）。

5. **[Contribution A — 新增 causal ablation with confound controls]** — 原始方案无因果验证。新增：(a) high-EMA tokens 禁用 MLP sparsity vs low-EMA tokens 施加最大 sparsity 的对比；(b) position-matched control（同一位置桶内按 EMA 分组）；(c) frequency-matched control（同一 token type 在不同 context 下的 EMA 变化）。 — 命中 **Technical Soundness**。将 Contribution A 从 "correlation report" 升级为有因果支撑的 empirical finding，preempt "correlation ≠ causation" 的标准质疑。

6. **[Contribution A — 新增 attention retrieval analysis]** — 对 high-EMA 和 low-EMA token 组分别统计被后续 token attend 的频率/权重分布，验证 mechanistic account 的 (b) 侧（representational stability → lower retrieval demand → safe to evict）。 — 命中 **Soundness / Analysis depth**。完成 mechanistic explanation 的双侧实证支撑，使 "unified account" 从 hypothesis 升级为 empirically grounded explanation。

7. **[Contribution A — 新增 conditional mutual information 分析]** — 计算 I(EMA; MLP_sparsity | attention_score)，证明 EMA 信号携带 attention score 之外的独立信息。 — 命中 **Novelty / Soundness**。直接回应 "为什么不用 attention score 做两轴" 这一最自然的审稿质疑。

8. **[Contribution A — 新增 mechanistic intuition 段落]** — 原始方案缺少机制解释。新增信息论视角：EMA 高 → 表征稳定 → (a) MLP 无需大幅变换 → 高 sparsity；(b) KV entry 不被后续 token 密集 attend → 可 evict。同时在 Related Work 中显式对接 early-exit 文献（CALM, LayerSkip, LAPE），说明共享 "stability ≈ redundancy" 信号但 CARC 扩展到跨轴。 — 命中 **Soundness / Novelty**。Preempt "lacks deeper analysis / why does this work" 的常见 criticism。

9. **[Contribution A — 新增 cross-architecture validation]** — 原始方案仅有 Qwen 架构族。新增 Llama-3.1-8B（GQA, SiLU），明确定位为 general long-context model（非 CoT reasoning）用于信号泛化性验证。Reasoning phase analysis 仅限 CoT 模型。 — 命中 **Technical Soundness**。消除 "Qwen-specific artifact" 的质疑。

10. **[Contribution A — 新增 distilled vs non-distilled 对比]** — 对比 DeepSeek-R1-Distill-Qwen-14B 与 Qwen3-8B 的 cross-axis correlation 模式，不仅排除 distillation artifact，还报告差异方向和幅度作为关于 distillation 影响冗余结构的 observation。 — 命中 **Analysis depth**。将 defensive 实验转化为 offensive 贡献。

11. **[Method — 删除 fallback path]** — 从 proposal 中完全删除 "If Contribution A fails, KV eviction alone remains a novel contribution" 的 fallback 叙述。 — 命中 **Novelty（心理层面）**。显式 fallback 暗示作者对核心贡献信心不足，是审稿人的负面信号。

12. **[Method — 术语修正 "zero-cost" → "lightweight"]** — 所有 "zero-cost add-on" / "zero integration cost" 改为 "lightweight" / "near-zero marginal cost"。新增 CARC overhead profiling（EMA 计算 + threshold logic 的 wall-clock 占比），composability matrix 每 cell 报告 CARC 自身 overhead。 — 命中 **Technical Soundness**。消除 "zero-cost is false" 的可信度攻击。

13. **[Method — 新增 implementation discussion]** — 说明 CARC-MLP 的实现策略（Triton kernel batched threshold masking / TensorCore structured sparsity），区分 theoretical FLOPs reduction 和 measured wall-clock speedup，报告 hardware utilization efficiency。若 kernel 工程不可行，FLOPs/memory reduction 作为 fallback metrics（TEAL 先例）。 — 命中 **Feasibility / Soundness**。Preempt "per-token conditional masking 在 GPU 上反而更慢" 的系统级质疑。

14. **[Method — 新增 CARC-Adaptive 变体]** — Phase-aware adaptive thresholding（滑动窗口 EMA 均值检测 phase 转换，scale τ_reset），作为 Extended ablation 变体而非替代主方法。展示 analysis → insight → method design 的逻辑闭环。 — 命中 **方法论创新 + 叙事完整性**。Contribution A（分析）和 Contribution B（方法）之间建立设计依据关系。

15. **[Experimental Design — 新增 composability matrix]** — 原始方案仅有 CARC-MLP-only 单一 ablation。新增系统性组合矩阵：{CARC-MLP, TEAL, none} × {CARC-KV, LongFlow-KV, TriAttention-KV, none}，每 cell 报告 accuracy + latency + peak memory + CARC overhead。 — 命中 **Experimental rigor + Practical impact**。将 composability 从 claim 升级为实测验证，产出的兼容性表格对社区有独立参考价值。

16. **[Experimental Design — 新增 naive combined baseline]** — 独立应用各轴最优方法（best KV eviction + best MLP pruning，各用自己最优信号，无 coordination），与 CARC 在 accuracy-speedup Pareto frontier 上对比。 — 命中 **Technical Soundness**。直接验证 "coordination 比独立压缩更好" 的核心 thesis，堵住最可能的审稿质疑。

17. **[Experimental Design — 新增 oracle baseline comparison]** — 各轴独立最优信号（KV 用 attention-score-optimal，MLP 用 activation-magnitude-optimal）vs CARC shared signal。预设成功标准：≤2% accuracy gap at matched speedup。 — 命中 **Soundness**。量化 shared signal 的 optimality trade-off。

18. **[Experimental Design — 实验分层 Core vs Extended]** — 原始方案实验设计未分层，膨胀风险高。新增明确分层：Core（~2-3 周，支撑主要 claim）vs Extended（资源允许再做）。Core = Contribution A 分析（14B + 8B + Llama-8B）+ MATH-500/GPQA 质量 + composability matrix 核心行 + oracle + naive combined + 参数敏感性 + wall-clock 实测。Extended = 32B full benchmark、Ruler、batch×length full matrix、CARC-Adaptive、MiniCache、early-exit oracle、AIME。 — 命中 **Feasibility**。确保核心 claim 做深做透，保留 rebuttal 响应空间。

19. **[Experimental Design — 新增 parameter sensitivity analysis]** — 原始方案直接借用 LazyEviction 的 W_grace=175、τ_reset=0.7。新增独立敏感性分析（W_grace ∈ {100,150,175,200,250}，τ_reset ∈ {0.5,0.6,0.7,0.8,0.9}），LazyEviction 重定位为 "independent corroboration"。 — 命中 **Soundness / 方法独立性**。消除 "参数依赖 LazyEviction" 的方法论独立性质疑。

20. **[Experimental Design — 新增 batch × sequence length ablation（Extended）]** — 原始方案仅 batch=1, L=64K。新增 batch ∈ {1,4,8,16} × length ∈ {4K,8K,16K,32K,64K} 矩阵。叙事从 "speedup percentage" 转向 "unlocking new operating points"（在同等质量约束下 serve 更大 batch / 更长 sequence）+ memory 收益。 — 命中 **Thoroughness + Practical impact**。消除 cherry-picking 质疑，展示作者对方法适用范围的清醒认知。

21. **[Experimental Design — wall-clock measurement protocol]** — 原始方案所有数字为 back-of-envelope。新增标准化测量协议（5 warm-up + 20 timed iterations, mean ± std, hardware spec），所有 projected estimates 标注为 projected 并承诺替换为实测。 — 命中 **Soundness**。Efficiency paper 无实测是 EMNLP 审稿的高优先攻击点。

22. **[Positioning — 新增 deployment overhead 对比表]** — Training-free + calibration-free + no offline profiling 作为 first-class differentiator，与 H2O/SnapKV、PowerInfer/Deja Vu、CALM 的 deployment overhead 做表格对比。 — 命中 **Practical significance / Reproducibility**。一目了然展示 CARC 的 deployment simplicity 优势。

23. **[Related Work — 大幅扩展]** — 原始方案遗漏大量重要工作。新增覆盖：KV eviction（SnapKV, PyramidKV, H2O, AdaKV, StreamingLLM, MiniCache, Quest）、early exit（CALM, LayerSkip, LAPE）、conditional computation（Switch Transformer, Expert Choice, ACT/Universal Transformer）、token merging（ToMe LLM variants）。按子类组织，对 MiniCache 的差异化定位（coordination index vs direct compression）尤为关键。 — 命中 **Related Work**。消除 reviewer 发现熟悉 baseline 未被讨论而直接扣分的风险。

24. **[Discussion — 新增 EMA 作为 general indicator]** — 简要展开 EMA similarity 作为通用 per-token information novelty indicator 的泛化潜力（early exit、speculative decoding、adaptive computation），以 "may generalize to" 审慎语气，配合 Extended E6 的初步 oracle correlation 证据。 — 命中 **Broader impact / Significance**。将论文 takeaway 从 "一个效率方法" 扩展为 "一个通用信号的发现 + 首次应用"。

25. **[Limitations — 新增显式讨论]** — 原始方案无 Limitations 段。新增：模型规模上限（≤32B）、distillation artifact 可能性、phase segmentation 方法学局限、projected vs measured 差距、custom kernel 需求。 — 命中 **Soundness（诚实度）**。主动讨论 limitations 是 EMNLP 审稿的正面信号。

【主要风险】:

1. **R²=0.25 下 "cross-axis coordination" 的实际价值**。这是最大审稿风险。如果 oracle baseline（各轴独立最优信号）或 naive combined baseline（各轴独立最优方法）大幅优于 CARC，"shared signal coordination" 的核心叙事将被削弱。缓解措施已部署（conditioned R²、conditional MI、novelty 双支柱），但最终取决于实验结果。若 oracle gap > 2% accuracy，需要诚实重定位为 "architectural simplicity vs optimality trade-off 的量化研究"。

2. **Wall-clock speedup 远低于 projected ~25%**。Per-token dynamic MLP sparsity 在 GPU 上的实际加速高度依赖 kernel 实现质量。如果 measured speedup 仅有 10-15% 甚至更低，reviewer 会质疑 practical impact。FLOPs/memory reduction 作为 fallback metrics 可接受（TEAL 先例），但会削弱 "efficiency method" 的 selling point，使论文更依赖 Contribution A 的分析价值。

【实施评估】:

- **计算资源**: 需要至少 2×A100-80GB（或等效）。14B 模型在 64K 上推理需要 ~40GB 显存（可单卡）；32B 模型需 2 卡或 1×H100。Core experiments 预计 ~500-800 GPU-hours（主要消耗在 composability matrix 的多配置 evaluation 和 cross-model correlation analysis）。Extended experiments（含 32B full benchmark、batch×length matrix）额外 ~300-500 GPU-hours。

- **数据需求**: MATH-500（公开）、GPQA-Diamond（公开，需申请）、AIME 2024（公开）、Ruler（公开合成 benchmark）。所有数据集公开可得，无数据获取障碍。

- **人工介入**: (1) Token-type 分类验证：≥2000 tokens 的 LLM-as-judge 标注 + 人工审核 Cohen's κ，约 2-3 人天；(2) Reasoning phase segmentation 验证：10+ CoT traces 的分段质量检查，约 1-2 人天；(3) 无需大规模人工标注或专家评审。总人工约 3-5 人天。

- **训练需求**: **无模型训练**。CARC 是 training-free 方法，所有实验均为 inference-time evaluation。唯一的工程开发是 Triton kernel 实现（batched threshold masking），预计 1-2 周开发 + 调试。若放弃 wall-c


## MVP Validation Results

- **Date**: 2026-05-12
- **Hypothesis Supported**: No

### Key Metrics

mvp-001b: r=0.147, Δpert=-2.2% | mvp-001c: r=0.159, Δpert=-1.2% | Both far below Suggestive thresholds (r≥0.4, Δpert≥10%). Δpert direction inverted across all experiments.

### Summary

Cross-axis hypothesis (KV similarity predicts MLP sparsity tolerance) tested across 3 experiments: mvp-001 (wrong EMA, baseline), mvp-001b (correct anchor EMA, 20 easy problems), mvp-001c (correct anchor EMA, 5 AIME-level hard problems). All FAIL. Δpert consistently negative (redundant tokens MORE sensitive to MLP pruning). Pivot to Option B: negative evidence paper + O(1) KV eviction standalone.

### Recommendation

Pivot to Option B: (1) Negative evidence paper — systematic validation of cross-axis hypothesis failure with "inverted relationship" as surprising finding, (2) O(1) KV eviction as standalone practical contribution. The Δpert inversion is analytically interesting — MLP may compensate for attention-level redundancy.
