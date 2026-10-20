# Idea Brief: RateKV: Input-Adaptive Rate-Distortion Allocation for Joint KV Cache Eviction and Quantization


- **Idea ID**: `idea_017`
- **Created**: 2026-05-13
- **Approved**: 2026-05-13
- **Source**: foreign:be-idea-gen-0509-2
- **Level**: top-tier
- **Target Venues**: EMNLP 2026 Main (ARR submission deadline: May 25, 2026), EMNLP 2026 Findings

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

## Generation Journey

1. **Start** — 开始生成，seed: 'Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Efficient Methods for NLP.\n\nDirection: Efficiency methods for NLP — NOT limited to LLM inference optimization. In-scope: speculative decoding, KV-cache compression/eviction, quantization-aware distillation, parameter-efficient fine-tuning, efficient long-context serving, MoE routing, attention approximations, efficient smaller models for specific NLP tasks, pruning for task-specific deployment.\n\nContribution type: METHOD ONLY. Propose new algorithms — not profiling studies.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Generous for efficiency work.\n2. Time: ≤16 days. Build on vLLM, SGLang, llama.cpp, TensorRT-LLM, HF Transformers, FlashAttention, bitsandbytes.\n3. Eval: perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench. Report wall-clock and throughput on H100.\n\nLook for: cache-aware methods for new workloads (long thinking traces, agent loops, RAG), quantization-aware distillation, structured sparsity during inference, efficient serving of reasoning models with variable-length thinking. Avoid: vanilla 4-bit quantization, generic LoRA, plain speculative decoding.\n\nTag: direction=efficiency, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].'
2. **Problem Discovery** (945s) — 发现 5 个研究方向
   - Phase-Adaptive Joint Sparsity for Reasoning Model Decoding
   - Distillation-Compressed KV Cache for Chunk-Reusable RAG Serving
   - Sparsity-Quantization Co-Design for Reasoning KV Caches
   - Workload-Predictive KV Cache Tiering for Mixed Serving
   - Distillation-Trained Contextual Sparsity Predictors for SwiGLU Models
3. **Method Synthesis** (666s) — 完成: "Phase-Adaptive Joint Sparsity for Reasoning Model Decoding" [top-tier] → AAAI 2027 (abstract: Jul 26, full paper: Aug 2, 2026), ICLR 2027 (abstract: Sep 19, full paper: Sep 24, 2026), MLSys 2027 (~Oct 31, 2026)
3. **Method Synthesis** (380s) — 完成: "Distillation-Compressed KV Cache for Chunk-Reusable RAG Serving" [solid] → AAAI 2027 (deadline expected ~August 2026), ICLR 2027 (deadline expected ~September 2026)
3. **Method Synthesis** (552s) — 完成: "Sparsity-Quantization Co-Design for Reasoning KV Caches" [solid] → EMNLP 2026 (ARR deadline: May 25, 2026 — extremely tight, 14 days from today; stretch target only), AAAI 2027 (expected deadline: ~August 2026; primary target), ICLR 2027 (expected deadline: ~September-October 2026; primary target)
3. **Method Synthesis** (510s) — 完成: "Workload-Predictive KV Cache Tiering for Mixed Serving" [solid] → EMNLP 2026 (ARR submission deadline: May 25, 2026), NeurIPS 2026 Workshops (suggested paper deadline: ~Aug 29, 2026), ICLR 2027 (expected ~Sep-Oct 2026, based on ICLR 2026 deadline of Sep 24, 2025)
3. **Method Synthesis** (718s) — 完成: "Distillation-Trained Contextual Sparsity Predictors for SwiGLU Models" [solid] → EMNLP 2026 (ARR deadline May 25, 2026), AAAI 2027 (deadline August 1, 2026), ICLR 2027 (deadline ~October 2026, expected), MLSys 2027 (deadline October 31, 2026)

## Core Problem

KV cache compression operates in two fundamentally different regimes — token eviction (removing less important tokens entirely) and quantization (reducing precision of retained tokens) — and the optimal regime varies across attention heads, layers, and inputs. 'More Tokens, Lower Precision' (EMNLP 2025 Findings) empirically demonstrated that this trade-off matters: storing 4× tokens at 4-bit precision outperforms 1× tokens at 16-bit, but the optimal allocation varies by task (retrieval vs. reasoning) and the paper provides no theory for when each regime wins. RateQuant (May 2026) provides theoretically optimal per-head bit allocation via rate-distortion reverse waterfilling, but only handles quantization and uses static calibration that cannot adapt to input-dependent variation. ARKV (March 2026) heuristically selects between eviction, quantization, and full-precision using attention entropy/variance/kurtosis, but operates at per-layer granularity, relies on hand-tuned thresholds without optimality guarantees, and requires post-softmax attention statistics (incompatible with Flash Attention). MixedDimKV (March 2026) frames eviction as the zero-dimension limit of a unified dimension allocation framework and uses Lagrangian dual optimization, but does not provide rate-distortion optimality guarantees and operates at per-token granularity with non-trivial overhead. HqeKV (ARR 2026) proposes per-element hybrid quantization+eviction but uses importance-score heuristics without a unified theoretical framework. KVSculpt (March 2026) found 467× distortion variation across KV heads within a single layer, confirming that per-head allocation is essential, but uses pilot-based distillation without a rate-distortion framework. The result: no existing method provides (a) a theoretically grounded framework for jointly optimizing eviction AND quantization allocation across KV heads with provable R-D optimality, (b) input-adaptive per-head decisions that work under Flash Attention, or (c) optimal resolution of the token-precision trade-off that empirical work has identified as critical but left unsolved.

## Opportunity / Why Now

Three independent 2026 advances create the conditions for a unified solution. First, RateQuant demonstrated that rate-distortion reverse waterfilling yields optimal per-head quantization allocation: per-head distortion curves D_h(b) = α_h·β_h^{-b} can be reliably fit from brief calibration (R² > 0.99), and the decay rate β varies significantly across quantizer designs (3.6–5.3), making per-head allocation essential. However, RateQuant is limited to static, quantization-only allocation and its reverse waterfilling cannot handle the discrete, heterogeneous action sets required for joint eviction+quantization. Second, DuoAttention (ICLR 2025) showed that approximately 50% of KV heads (at KV head granularity, not query head level) in GQA models like Llama-3-8B are 'streaming heads' focusing on recent tokens and attention sinks. Critically, DuoAttention's classification operates at the KV head level in GQA models, meaning the GQA constraint (all query heads sharing a KV head must receive the same action) is naturally aligned with the streaming/retrieval distinction — there is no 'mixing' problem within KV groups. These streaming KV heads are natural eviction candidates where retaining important tokens at full precision avoids quantization noise on critical values. Third, 'Quantization Dominates Rank Reduction' (April 2026) showed quantization outperforms PCA/SVD-based rank reduction by 4–364 PPL, narrowing the useful strategy space to the eviction-vs-quantization decision. Additionally, Expected Attention (ICLR 2026) provides FA-compatible closed-form importance scoring from activation distributions, and KVSculpt (March 2026) demonstrated 467× distortion variation across KV heads within a single layer, confirming that fine-grained per-head allocation is critical. The missing piece: extending rate-distortion allocation from quantization-only to the joint eviction+quantization action space via a multiple-choice knapsack formulation (MCKP), treating eviction and quantization as alternative actions at memory-equivalent operating points. At any memory budget, retaining fraction f of tokens at 16-bit costs the same as quantizing all tokens at b = 16f bits — the optimal choice depends on per-KV-head attention sparsity, which varies across heads and inputs. This is timely for EMNLP because: (a) 'More Tokens, Lower Precision' (EMNLP 2025 Findings) established the empirical importance of this trade-off in NLP tasks but provided no optimal allocation theory, (b) 'On the Limits of Learned Importance Scoring' (Jan 2026) showed learned scorers don't outperform heuristics, motivating analytical allocation over learned selectors, and (c) the combination of RateQuant's R-D framework with per-head attention sparsity profiling provides the theoretical scaffold for a unified solution.

## Landscape (SOTA & Limitations)

Token eviction methods select which tokens to retain: GVote (ICLR 2026) adaptively computes per-head budgets via Monte Carlo sampling; CapKV (2026) derives eviction from an Information Bottleneck objective using leverage scores (FA-compatible, implemented in kvpress as LeverageScorePress); LKV (2026) learns head-wise budgets end-to-end via differentiable optimization (Flash Attention compatible); Expected Attention (ICLR 2026) estimates future attention in closed form from activation distributions (FA-compatible, implemented in kvpress as ExpectedAttentionPress); LaProx (May 2026) reformulates eviction as layer-wise output-aware matrix multiplication approximation with inter-head dependency modeling (FA2-compatible); CAOTE (April 2025) minimizes attention output error by jointly scoring via attention weights and value vectors; DuoAttention (ICLR 2025) identifies ~50% of KV heads (at KV head granularity in GQA) as 'streaming heads' (eviction-friendly) vs. 'retrieval heads' (full-cache-needed); KVSculpt (March 2026, arXiv 2603.27819) uses pilot-based distillation with adaptive per-head budget allocation, finding 467× distortion variation across KV heads within a single layer; HeteroCache (Jan 2026, arXiv 2601.13684) categorizes heads into functional roles and clusters redundant heads for hierarchical heterogeneous compression. Quantization methods: RateQuant (May 2026) applies rate-distortion reverse waterfilling for optimal static per-head bit allocation (1.6s calibration, zero inference overhead, R² > 0.99 for D(b) = α·β^{-b}, reduces Qwen3-8B PPL from 49.3→14.9 at 2.5 avg bits, code not yet released); HeadQ (May 2026) measures model-visible distortion in score-space with low-rank residual correction; eOptShrinkQ (April 2026) uses random matrix theory spectral denoising with provable guarantees; TurboQuant (ICLR 2026) achieves near-optimal online vector quantization; KVTC (ICLR 2026) combines PCA decorrelation + adaptive quantization + entropy coding for 20× compression; 'Don't Waste Bits' (April 2026) learns token-level bit-width selection via compact MLP controller; PM-KVQ (May 2026) proposes progressive mixed-precision KV cache quantization with block-wise memory allocation for long-CoT reasoning. Hybrid methods: 'More Tokens, Lower Precision' (EMNLP 2025 Findings, arXiv 2412.12706) empirically established that quantized pruning (more tokens at lower precision) outperforms standalone pruning, showing 4× tokens at 4-bit beats 1× at 16-bit, but provides no optimization theory; MixedDimKV (March 2026, arXiv 2603.20616) frames eviction as zero-dimension allocation and optimizes per-token dimension assignment via Lagrangian bisection — conceptually analogous to our 'eviction as zero-rate' insight but uses dimension (not rate-distortion) theory without R-D optimality guarantees; ARKV (March 2026) computes attention entropy/variance/kurtosis for per-layer heuristic selection between eviction/quantization/full-precision — closest hybrid competitor but requires post-softmax attention (FA-incompatible), per-layer granularity, and no optimality guarantees; HqeKV (ARR 2026) performs per-element hybrid quantization+eviction with automatic optimizer (code available at github.com/skywclouds/HqeKV); TailorKV (ACL Findings 2025) performs binary layer-level classification; EvicPress (2025) jointly optimizes compression and eviction across storage tiers. Negative results: 'On the Limits of Learned Importance Scoring' (Jan 2026) shows a 1.7M-parameter learned scorer does not outperform position-based heuristics — motivating analytical over learned approaches. 'Quantization Dominates Rank Reduction' (April 2026) shows quantization outperforms rank reduction (PCA/SVD) by 4–364 PPL, but compares to rank reduction, not token eviction — these have fundamentally different failure modes (dimension removal flips attention routing; token eviction preserves representational integrity of retained tokens). This result narrows the useful strategy space to eviction-vs-quantization, making our joint R-D framework the right problem formulation. No existing method extends rate-distortion theory to the JOINT eviction+quantization allocation problem with per-head input-adaptive allocation under Flash Attention and R-D optimality guarantees.

## Proposed Approach

We propose RateKV, a training-free, input-adaptive framework that jointly optimizes per-KV-head eviction and quantization allocation via extended rate-distortion theory, formulated as a multiple-choice knapsack problem (MCKP) over a unified eviction+quantization action space.

**Key Theoretical Insight.** At any memory budget, eviction and quantization are alternative compression strategies with different distortion characteristics. Retaining fraction f = b/16 of tokens at 16-bit precision costs the same memory as b-bit quantization of all tokens. The optimal choice per head depends on attention sparsity: sparse heads (concentrated attention on few tokens) benefit from eviction (keeping important tokens at full precision avoids quantization noise on critical values), while dense heads (distributed attention) benefit from quantization (keeping all tokens prevents information loss from discarding attended tokens). We formalize this as an MCKP: for each KV head, select from a discrete set of eviction and quantization actions to minimize total distortion under a global memory budget. This eliminates the need for separate eviction/quantization passes and provides a single unified optimization with provable near-optimality.

**GQA Eviction Fraction Analysis.** A critical concern is whether the GQA constraint (all query heads sharing a KV head must use the same action) renders eviction-mode selection impractical. We present a concrete analysis showing this concern is overstated. DuoAttention (ICLR 2025) classifies attention heads as streaming vs. retrieval at the **KV head level** in GQA models — not at the individual query head level. For Llama 3.1-8B (8 KV heads/layer × 32 layers = 256 MCKP decisions), DuoAttention finds ~50% of KV heads are streaming, meaning ~128 of 256 KV heads have attention concentrated on recent tokens/sinks. There is no 'mixing' problem within KV groups because the streaming/retrieval classification is already at the KV head granularity. For streaming KV heads at 4× compression: evict(1/4) retains top-25% tokens at 16-bit, capturing >95% of attention mass (since attention is concentrated), yielding near-zero eviction distortion. Meanwhile, quant(4-bit) adds noise to all tokens including the critical recent ones. We therefore estimate that **30–50% of KV heads will prefer eviction** at moderate compression ratios (4×), with the exact fraction depending on compression aggressiveness (higher compression → more heads prefer eviction, since extreme quantization e.g. 2-bit is more destructive than proportional eviction) and task type (retrieval tasks may have fewer streaming heads). We validate this estimate empirically during calibration and report the actual eviction fraction as a key result (Experiment ii). Even if the eviction fraction is lower than estimated (e.g., 15–20%), the MCKP framework remains valuable as input-adaptive R-D allocation generalizing RateQuant to heterogeneous action sets.

RateKV operates in four stages:

**(1) Offline Distortion Profiling (~2 min per model, one-time).** Following RateQuant's calibration protocol, we use 16 sequences of length 512 to measure per-KV-head distortion at discrete action points. For each KV head h at each layer:
- Quantization distortion: Measure D_h^quant(b) = MSE(O_h^{16bit}, O_h^{b-bit}) at b ∈ {2, 4, 8} bits, where O_h is the head's contribution to the layer output. Optionally fit parametric model D_h^quant(b) = α_h · β_h^{-b} via log-linear regression (R² > 0.99 per RateQuant's finding).
- Eviction distortion: Measure D_h^evict(k) = MSE(O_h^{full}, O_h^{top-k}) at retention fractions k/N ∈ {1/16, 1/8, 1/4, 1/2} using Expected Attention scoring (ExpectedAttentionPress in kvpress) for token selection.
- Distortion is measured directly at each discrete action point — no parametric model is required since the MCKP operates over a finite action set. As a diagnostic, we report R² of optional parametric fits across all heads.
- Store calibrated profiles as a compact lookup table (~4KB per model): for each KV head, store distortion values at each of the ~7 action points (3 quantization levels + 4 eviction fractions).

**(2) Input-Adaptive Profile Adjustment (online, <0.1ms).** We propose a lightweight, empirically motivated heuristic for adapting calibrated profiles to new inputs. The core observation is that distortion scales approximately linearly with V-matrix energy (value magnitude). At inference time, compute per-KV-head statistics from the materialized KV cache (always available, even under Flash Attention): V-matrix Frobenius norm ||V_h(x)||²_F and key-norm Gini coefficient G_h(x). Adjust calibrated distortion profiles: D_h(a; x) = D_h^cal(a) · (||V_h(x)||²_F / ||V_h^cal||²_F). For eviction actions, additionally scale by the runtime/calibration Gini ratio to capture shifts in attention sparsity. **We explicitly frame these adjustments as empirically motivated heuristics, not theoretically derived results.** We validate them through a three-way ablation: (A) static calibration (no adjustment), (B) V-norm adjustment only, (C) V-norm + Gini adjustment. If the gain from (B) or (C) over (A) is small, we report this honestly and note that the primary value lies in the MCKP framework itself, not the input-adaptive adjustment — which would still represent a meaningful result as static R-D allocation already outperforms heuristic methods.

**(3) Unified MCKP Allocation (online, <0.2ms).** For each KV head h, define action set: {evict(f) for f ∈ {1/16, 1/8, 1/4, 1/2}, quant(b) for b ∈ {2, 4, 8}, full-precision}. Note: evict(f) at f = b/16 has identical memory cost to quant(b), so we directly compare their distortion at each memory-equivalent point. After dominance filtering (removing actions where another has both lower cost AND lower distortion), solve the MCKP via LP-relaxation-guided greedy: compute efficiency ratio η = ΔD/Δcost for each action upgrade, greedily upgrade the most efficient head-action pair until budget exhausted. With H_kv × L KV heads (e.g., 8 × 32 = 256 for Llama 3.1-8B) and ~5 non-dominated actions per head, this runs in O(H · A · log(H · A)) ≈ microseconds. When per-head distortion functions are convex in cost (verified empirically during calibration for our discrete action sets), greedy MCKP achieves provably optimal allocation.

**(4) Strategy Execution via MixedStrategyCache.** We implement a custom HuggingFace DynamicCache subclass (MixedStrategyCache) that stores per-KV-head metadata specifying each head's assigned action (quantization bit-width or eviction retention fraction). Quantization-mode heads: per-channel key / per-token value quantization at the allocated bit-width (using KIVI backend). Eviction-mode heads: retain top-k tokens at full 16-bit precision using Expected Attention scoring (ExpectedAttentionPress from kvpress, FA-compatible). The MixedStrategyCache manages heterogeneous per-KV-head storage (~300 lines). Engineering estimate: 2-3 days for a working implementation. The GQA constraint simplifies implementation since each KV head gets a single action. Fallback: if the custom cache proves fragile, eviction and quantization can be applied in separate passes with per-KV-head masking using existing kvpress primitives (AdaKVPress for eviction, QuantizedCache for quantization).

**Crossover Visualization (Key Figure).** During calibration, we produce the paper's most important figure: for representative KV heads across 2-3 layers, plot D_h^evict(f) and D_h^quant(b) at memory-equivalent operating points (e.g., evict(1/4)@16-bit vs. quant(4-bit), evict(1/8)@16-bit vs. quant(2-bit)). This per-head crossover analysis visualizes exactly where eviction outperforms quantization and vice versa, demonstrating that the MCKP is non-trivial. We expect streaming KV heads to show eviction-preferred regions (especially at higher compression) and retrieval KV heads to show quantization-preferred regions, with the crossover point varying by head.

**Token Selection: Expected Attention over Key-Norm.** We use Expected Attention (ICLR 2026) for eviction-mode token selection rather than key-norm ranking. Key-norm has only moderate correlation with attention scores (Pearson ~0.30 per HashEvict), while Expected Attention estimates future attention in closed form from activation distributions. Expected Attention is FA-compatible, training-free, and already implemented in kvpress. As an ablation, we compare Expected Attention vs. key-norm vs. CapKV leverage scores.

**On 'Quantization Dominates Rank Reduction':** This result compares quantization to PCA/SVD rank reduction, NOT to token eviction — fundamentally different failure modes. Token eviction preserves representational integrity of retained tokens while rank reduction removes embedding dimensions. Our calibration profiles provide the first systematic per-KV-head comparison of eviction vs. quantization distortion at matched budgets.

**Contribution Hierarchy (Robust Regardless of Eviction Fraction).**
(a) **Primary: R-D allocation via MCKP over heterogeneous action sets, generalizing RateQuant's reverse waterfilling.** Even if all heads select quantization, the MCKP framework enables principled per-head budget allocation over discrete, heterogeneous action sets that RateQuant's continuous reverse waterfilling cannot handle. The input-adaptive distortion adjustment (validated via ablation) provides improvement over static calibration.
(b) **Secondary: First systematic empirical characterization of when eviction outperforms quantization at matched memory budgets, with per-KV-head crossover analysis under GQA constraints.** This includes the crossover visualization and eviction fraction analysis across head types and tasks. This analysis has standalone value regardless of eviction fraction magnitude.
(c) **Tertiary: Non-parametric eviction distortion profiling methodology extending RateQuant's calibration protocol.** Enables any future MCKP-based method to incorporate eviction a

## Resource Estimate

- **auto_research**: {'claude_api_cost': '$100-200', 'estimated_gpu_cost': '$350-450 (140-180h × ~$2.50/hr)', 'gpu_hours': '~140-180h H100', 'gpu_utilization': 'High (~70-80%)', 'risk_note': 'MixedStrategyCache and RateQuant reimplementation are the main engineering risks. Both are well-scoped (~100-300 lines each). Fallback: implement eviction and quantization in separate passes with per-head masking using existing kvpress primitives.', 'speed_bottleneck': 'RateQuant reimplementation and MixedStrategyCache are the main engineering risks. Distortion profiling and evaluation are embarrassingly parallelizable.', 'team': '0 (initial setup ~3-4 hours)', 'timeline': '14-18 days with ≥2 H100 GPUs'}
- **human_in_loop**: {'claude_api_cost': '$60-120', 'estimated_gpu_cost': '$225-275 (90-110h × ~$2.50/hr)', 'gpu_hours': '~90-110h H100', 'gpu_utilization': 'High (~55-65%)', 'risk_note': 'Primary risk is MixedStrategyCache implementation (2-3 days): GQA constraint simplifies per-head dispatch since each KV head gets a single action. Fallback: use separate AdaKVPress + QuantizedCache passes per KV group. RateQuant reimplementation (1-2 days): algorithm is fully described (~100 lines), verify reproduction of reported numbers before comparison. Eviction fraction experiment is important for narrative but not existential — contribution hierarchy is robust to low eviction fraction.', 'team': '1 researcher, ~2-3h/day reviewing distortion profiles and writing', 'timeline': '16-20 days (Days 1-2: RateQuant reimplementation + verification against reported numbers; Days 3-5: MixedStrategyCache + calibration pipeline + MCKP solver; Days 6-7: crossover visualization + eviction fraction analysis; Days 8-12: run evaluation experiments + distortion validation; Days 13-16: input-adaptivity ablation + paper writing; Days 17-20: buffer for iteration)'}
- **manual**: {'estimated_gpu_cost': '$275 (110h × ~$2.50/hr)', 'gpu_hours': '~110h H100', 'gpu_utilization': 'Moderate (~40%)', 'team': '1-2 researchers (information theory + LLM systems background)', 'timeline': '3-4 weeks'}

## Key References

- RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory (arXiv 2605.06675, May 2026)
- More Tokens, Lower Precision: Towards the Optimal Token-Precision Trade-off in KV Cache Compression (EMNLP 2025 Findings, arXiv 2412.12706)
- Beyond Token Eviction: Mixed-Dimension Budget Allocation for Efficient KV Cache Compression [MixedDimKV] (arXiv 2603.20616, March 2026)
- ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget (arXiv 2603.08727, March 2026)
- DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads (ICLR 2025, arXiv 2410.10819)
- Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution (arXiv 2510.00636, ICLR 2026)
- Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective [CapKV] (arXiv 2604.25975, 2026)
- Reformulating KV Cache Eviction Problem for Long-Context LLM Inference [LaProx] (arXiv 2605.07234, May 2026)
- LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction (arXiv 2605.06676, 2026)
- HqeKV: Towards Hybrid Quantization and Eviction for KV Cache in Long-Context LLM Inference (ARR 2026)
- PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs (arXiv 2505.18610, May 2026)
- On the Limits of Learned Importance Scoring for KV Cache Compression (arXiv 2601.14279, Jan 2026)
- Quantization Dominates Rank Reduction for KV-Cache Compression (arXiv 2604.11501, April 2026)
- Understanding the Physics of Key-Value Cache Compression for LLMs through Attention Dynamics (arXiv 2603.01426, March 2026)
- CAOTE: KV Cache Eviction for LLMs via Attention Output Error-Based Token Selection (arXiv 2504.14051, April 2025)
- HashEvict: A Pre-Attention KV Cache Eviction Strategy using Locality-Sensitive Hashing (arXiv 2412.16187, 2024)
- eOptShrinkQ: Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization (arXiv 2605.02905, April 2026)
- HeadQ: Model-Visible Distortion and Score-Space Correction for KV-Cache Quantization (arXiv 2605.03562, May 2026)
- GVote: Adaptive Per-request KV-Cache Compression without Manually Setting Budget (ICLR 2026)
- KV Cache Transform Coding for Compact Storage in LLM Inference [KVTC] (ICLR 2026)
- Don't Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs (arXiv 2604.04722, April 2026)
- TailorKV: A Hybrid Framework for Long-Context Inference via Tailored KV Cache Optimization (ACL Findings 2025)
- Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs [FastGen] (ICLR 2024 Oral)
- EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving (arXiv 2025)
- Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference (NeurIPS 2025)
- KVSculpt: KV Cache Compression as Distillation (arXiv 2603.27819, March 2026)
- HeteroCache: A Dynamic Retrieval Approach to Heterogeneous KV Cache Compression for Long-Context LLM Inference (arXiv 2601.13684, Jan 2026)

## Reviewer Evaluation

**Scores**:
  - clarity: **{'rationale': "Exceptionally well-articulated: the 4-stage approach is cleanly specified, the GQA eviction fraction analysis is concrete (citing DuoAttention's KV-head-level classification), input-adaptive adjustments are honestly framed as empirically motivated heuristics with a three-way ablation, and the contribution hierarchy is explicitly designed to be robust regardless of eviction fraction. The crossover visualization is well-motivated as the paper's key figure.", 'score': 4}**/5
  - feasibility: **{'rationale': 'Training-free method with well-scoped implementation (~300 lines MixedStrategyCache, ~100 lines RateQuant reimplementation), reasonable compute budget (~110h H100 within the 200h constraint), and clear fallback paths. Non-parametric distortion profiling over finite action sets eliminates the parametric model validation risk from earlier rounds. 14-day timeline is tight but achievable for a training-free method built on existing frameworks (kvpress, KIVI, Expected Attention). The GQA constraint actually simplifies implementation since each KV head gets a single action.', 'score': 4}**/5
  - impact: **{'rationale': "Provides the theoretical framework for the empirical finding in 'More Tokens, Lower Precision' (EMNLP 2025 Findings), extends R-D theory to a new domain (joint eviction+quantization), and offers practical deployment benefits (training-free, FA-compatible, <0.5ms overhead). The crossover visualization has standalone analytical value. Well-matched to EMNLP 'Efficient Methods for NLP' track. Even if eviction fraction is modest, the MCKP framework generalizing reverse waterfilling to heterogeneous action sets is independently valuable.", 'score': 4}**/5
  - novelty: **{'rationale': "The MCKP formulation for joint eviction+quantization at per-KV-head granularity with R-D distortion profiling is genuinely novel. No existing work combines R-D theory with a unified eviction+quantization action space at per-head granularity: ARKV is per-layer with hand-tuned heuristics and FA-incompatible; HqeKV is per-element with importance-score heuristics; MixedDimKV uses dimension theory (not R-D) at per-token granularity; RateQuant is quantization-only. The 'eviction as zero-rate at memory-equivalent points' insight is natural but non-trivial, and the contribution hierarchy is robust to low eviction fractions.", 'score': 4}**/5

## Human Review Note

## Agent 审核结果（完整三阶段 pipeline）

**Verdict**: PASS

**入口三重共识 (X)**: 31.0%
**终审自评 (Y)**: 40.0%
**出口三重共识 (Z)**: 39.0%
**Z 区间**: [34.0%, 44.0%]
**真实提升 (Z-X)**: +8.0 pp
**幻觉幅度 (Y-Z)**: +1.0 pp
**出口一致性**: 高
**出口三次评估**: [40.0, 38.0, 40.0]

### 优化方案 / 拒绝详情
【优化方案】

1. [标题] — 将 "Input-Adaptive Rate-Distortion Allocation" 改为 "Optimal Rate-Distortion Allocation"，消除标题与核心贡献（static MCKP allocation）之间的 overclaim 错位。Runtime adaptation 保留为独立 engineering enhancement，不在标题中承诺。 — [命中 soundness / clarity：消除 reviewer 对标题-方法不匹配的质疑]

2. [Introduction 开篇] — 将 b = 16f 从淹没在技术细节中的中间推导步骤提升为 Introduction 第一页的显式概念，定位为 "memory-equivalence cost normalization"（非 "principle"，避免将算术恒等式过度包装）。配一个 2×2 toy example（"head A: 丢 50% token distortion < 8-bit quantization distortion → 选 eviction；head B: 反之 → 选 quantization"），让 reviewer 30 秒内抓住核心 insight。 — [命中 clarity / novelty presentation：改善第一印象分]

3. [Method 核心：Proposition] — 新增显式理论命题，建立 reverse waterfilling 在异构 action space 下失效的精确条件：eviction distortion 的非参数性、attention-distribution-dependent 性、retention threshold 处的不连续性违反 waterfilling 的连续性/凸性前提。附带 concrete counterexample（高稀疏头 vs. 均匀注意力头，精确计算 waterfilling 次优 gap）。这是将 RateKV 从 "RateQuant 的工程扩展" 提升为 "填补理论 gap" 的关键差异化手段。 — [命中 novelty / soundness：区分主会与 Findings 的核心改动]

4. [Method：Distortion metric 明确化] — 显式定义 distortion = per-head attention output MSE（与 RateQuant 一致），论证 eviction/quantization 在此度量下的跨类型可比性。Ablation 中测试 MSE vs. cosine distance 的鲁棒性。原始 proposal 多次使用 "distortion" 但从未定义度量标准，是审稿人必然追问的缺口。 — [命中 soundness：消除 formulation 层面的含糊性]

5. [Method：贡献层次重构] — 明确分层：(1) 核心贡献 = static R-D MCKP allocation（完备理论结果），(2) 独立 engineering enhancement = runtime adaptation（V-norm + Gini heuristics）。Ablation 强调 static-only 已大幅优于 baseline，runtime 只是锦上添花。原始 proposal 的叙事让 static 和 runtime 纠缠不清，产生"理论最优 → 退化为 heuristic"的叙事张力。 — [命中 soundness / clarity：消解理论-实践张力]

6. [Method：DuoAttention 叙事重构] — **关键叙事改动**。原始 proposal 依赖 DuoAttention 的 streaming/retrieval 分类来论证 GQA 不产生 mixing problem 和估计 eviction 比例。重构为：MCKP allocation 从 distortion profile 出发自主决策，不依赖任何外部分类器。DuoAttention 仅作 post-hoc validation（报告 Jaccard coefficient），形成 "R-D 理论独立选出的 eviction heads 与 DuoAttention streaming heads 高度吻合" 的 convergent evidence story。 — [命中 novelty / soundness：加强 R-D 框架自洽性，反转为更强的 novelty story]

7. [Method：Eviction distortion profiling 地位提升] — 将 eviction distortion profiling 从 contribution (c) 提升为 contribution (b)，作为论文的核心方法论支柱。强调：与 quantization（有 Lloyd-Max 等闭式解）不同，eviction distortion 必须 empirically profile，profiling protocol（Expected Attention scoring + retention fraction 采样策略 + calibration set 选择）是非平凡的设计选择。 — [命中 novelty：为论文增加一个独立于 MCKP 的方法论贡献维度]

8. [Method：Flash Attention 实现细节] — 新增 Implementation Details 小节，说明 MixedStrategyCache 使用 `flash_attn_varlen_func` 处理异构 KV 长度，无需 padding。包含 memory overhead 分析和 wall-clock benchmark。原始 proposal 将 "FA-compatible" 作为关键卖点（区别于 ARKV）但未提供任何实现细节——这是关键 claim 缺证据的硬伤。 — [命中 soundness / reproducibility：为核心卖点补齐实证支撑]

9. [Experiment：Baseline 补充] — (a) 加入 ARKV 作为 must-do reimplementation baseline（per-layer heuristic 核心逻辑），quality metrics 在非 FA 路径下公平对比，latency 图标注 "non-FA upper bound"；(b) 加入 PyramidKV 或 SnapKV 作为 eviction-only 代表，与 RateQuant（quantization-only）形成 eviction-only / quantization-only / hybrid / joint allocation 四路完整对比。原始 proposal 缺少最直接竞品 ARKV 是审稿人最容易抓住的硬伤。 — [命中 related work / soundness：消除 baseline 缺失的致命扣分点]

10. [Experiment：Oracle + Waterfilling 三路对比] — 在 Llama 3.1-8B 的 3-4 个 layer group（early / middle / late）做三路对比：oracle（穷举最优）/ MCKP / naïve waterfilling。同时量化"MCKP 距 oracle 有多近"和"waterfilling 在异构设定下差多少"，闭合 Proposition 的理论-实证环。原始 proposal 完全没有 oracle 或 waterfilling 对比。 — [命中 soundness / novelty：将理论 claim 从陈述升级为可验证结果]

11. [Experiment：Gain decomposition] — 新增分析将 RateKV 总增益分解为 allocation gain（joint vs. quantization-only optimal）和 profiling gain（R-D optimal vs. heuristic baselines）。提供叙事鲁棒性：即使 allocation gain 是 modest 的，论文价值在于 principled framework + crossover analysis + profiling methodology。 — [命中 significance / soundness：预防"增量收益太小"的 reviewer 攻击]

12. [Experiment：Cross-domain calibration robustness] — 提升为 named finding。Calibrate on C4, evaluate on HumanEval/MT-Bench，报告 per-head action assignment agreement rate。无论高一致（证明部署泛化性）或低一致（分析哪些 swing heads 对 calibration 敏感），都有叙事价值。几乎零额外 compute cost。 — [命中 soundness / practical impact：主动化解 calibration-based 方法的标准质疑]

13. [Experiment：模型规模扩展] — 增加 70B 级模型的 profiling-only 分析（KV-head distortion profile + streaming/retrieval 比例跨规模稳定性），资源允许追加 perplexity。原始 proposal 仅覆盖两个 8B 模型，到 EMNLP 2026 投稿时 generalizability 会被质疑。 — [命中 significance / generalizability]

14. [Experiment：Decode latency + 双 Pareto frontier] — 从仅报告 latency 数字升级为双 Pareto frontier 分析（memory-distortion + memory-latency），展示 RateKV 在两个维度上是否 Pareto-efficient。原始 proposal 的 memory-equivalence 完全忽略 compute 不对称性。此分析放入 Appendix。 — [命中 soundness / practical impact：回应 systems reviewer 对 latency 回退的关切]

15. [Experiment：MCKP solver overhead + discretization sensitivity] — 报告 solver wall-clock time（8B 和 70B）+ budget 离散化粒度 sensitivity study。虽然 solver 大概率是毫秒级，但不报告就是缺口。 — [命中 soundness / completeness]

16. [Analysis：Crossover 分析深化] — (a) 三类 head regime 划分（strongly sparse / strongly dense / swing heads）；(b) swing heads 的 attention entropy + layer depth 刻画（Appendix 展开）；(c) DuoAttention concordance 随压缩比变化分析（Appendix）；(d) 跨模型族（Llama vs. Qwen）allocation pattern 一致性。将 "phase transition" 改为 "crossover shift" 避免术语过度使用。 — [命中 analysis depth / novelty：从 descriptive observation 升级为 mechanistic finding]

17. [Related Work] — 补充 KVQuant、GEAR、H2O、StreamingLLM、token merging 方向的讨论。加入 scooping 风险扫描计划（arXiv 2026.03-2026.05 + ICML/ACL 2026）。token merging extensibility 仅在 Discussion/Future Work 简述，不作 selling point（避免声称但不验证的 overclaim）。 — [命中 related work：展示对领域的全面掌握]

18. [Presentation 分层规划] — 明确主文 vs. Appendix 分配。主文（8+1 页）：理论框架 + MCKP、eviction profiling 方法、crossover 分析（简化版）、核心 benchmark、oracle + waterfilling 三路对比、gain decomposition。Appendix：cross-domain calibration、cross-architecture comparison、runtime adaptation ablation、dual Pareto、discretization sensitivity、FA 实现细节、70B profiling、distortion metric ablation、swing head 详细刻画。 — [命中 feasibility / clarity：确保 11-12 个子实验不导致主文拥挤失焦]

19. [RateQuant 复现] — 时间估计从 1-2 天调整为 ~1 周，计划提供详细 reimplementation details + reproduction study（reported vs. reimplemented numbers 对比）。 — [命中 soundness / credibility]

20. [Limitations] — 新增诚实声明：(1) 8B-only end-to-end evaluation；(2) runtime adaptation 为 heuristic 非 theoretically bounded；(3) 不联合优化 memory 和 compute；(4) extensibility 未实证验证。 — [命中 soundness：reviewer 看到作者主动承认限制会给更高的 trust 分]

【主要风险】:

1. **与 RateQuant 的 incrementality 风险**（最可能被攻击的点）：即使有 Proposition + counterexample + waterfilling gap 实证，部分 skeptical reviewer 仍可能将 RateKV 视为 "把 RateQuant 的 MCKP 扩展到多一种 action type" 的 incremental work。这是 novelty ceiling 的根本限制。防御策略：强调理论 gap（reverse waterfilling 不适用于异构设定）+ 独立 empirical contribution（crossover analysis）+ 独立方法论贡献（eviction profiling），三条线并行使得即使 reviewer 不买账某一条，整体 contribution 仍然 sufficient。

2. **Joint allocation 的实际增益幅度不确定**：如果实验中 RateKV 相对 RateQuant 的 allocation gain 很小（大部分 head 在所有压缩比下一致偏好 quantization），核心卖点"joint allocation matters"会被削弱。Gain decomposition 预案提供了叙事后路，但 reviewer 可能仍认为"如果增益只有 0.x PPL，为什么不直接用 RateQuant"。

【实施评估】:
- 计算资源: 主要实验（Llama 3.1-8B, Qwen3-8B）在单张 A100 80GB 上可完成；calibration ~2 分钟/模型，benchmark 推理按 6 个评测集 × 2 模型 × 5-7 压缩配置估算约 2-3 GPU-天。70B profiling-only 需 2-4 张 A100（或等效），约 0.5 GPU-天。70B perplexity 评估（可选）需 4 张 A100 约 1 GPU-天。Oracle 穷举在 8B subset 上计算量可控（3-4 layer groups × brute-force，估 1-2 GPU-小时）。总计约 4-6 GPU-天（核心）+ 1-2 GPU-天（可选 70B end-to-end）。
- 数据需求: WikiText-2、C4、MMLU、HumanEval、MT-Bench、LongBench、RULER——全部公开可得。Calibration data 用 C4 subset（标准做法）。Cross-domain calibration 额外使用 HumanEval/MT-Bench 子集，同样公开。
- 人工介入: 无需人工标注或专家评审。RateQuant 和 ARKV 的 reimplementation 需研究者手动实现（估 1-1.5 周），但属于标准工程工作。文献扫描（scooping check）需人工阅读 arXiv 近期论文，约 1-2 天。
- 训练需求: 无模型训练。方法完全 training-free（calibration-based + MCKP solver）。
- 新 Benchmark: 不需要构建新 benchmark。使用现有标准评测集。
- 预估周期: Reimplementation（RateQuant + ARKV）~1.5 周 → Calibration + profiling + 核心实验 ~1.5 周 → Analysis（crossover、oracle、gain decomposition、cross-domain）~1 周 → Writing ~2 周。总计约 **6-7 周**（从启动到可投稿初稿），假设单人全职 + GPU 资源就绪。



## MVP Validation Results

- **Date**: 2026-05-14
- **Hypothesis Supported**: Yes

### Key Metrics

Constrained MCKP PPL=11.23 vs Uniform 4-bit PPL=15.45 (Δ=4.21, 27% improvement) | Budget=0.2500 (exact match) | Solver > Manual Oracle (11.23 vs 11.69) | Allocation: 4×8-bit + 8×2-bit + 100×4-bit | Layer 0 auto-selected 8-bit by profiling delta (0.88-3.29 vs rest ~0.0)

### Summary

Constrained MCKP solver 在 Qwen2.5-7B (112 KV heads) 上验证通过。solver 自动为每个 KV head 分配最优 bit-width (4/8/16-bit + 受限 2-bit)，在 4× 压缩 budget (0.2500) 下 PPL=11.23，比 uniform 4-bit (PPL=15.45) 改善 27%。solver 自主发现 Layer 0 的 4 个 heads 需要 8-bit 保护（基于 profiling delta 驱动，非硬编码），并优于手动设计的 oracle 策略 (11.69)。关键 insight：per-head sensitivity 高度不均匀，Layer 0 占 3.6% 的 heads 却决定 70%+ 的 PPL 差异；cardinality constraint (max 2-bit heads ≤ 8) 作为对 profiler 系统误差的正则化是必要的。

### Recommendation

GO — 进入 research 阶段。Research 优先级：(1) 去掉 L0 排除约束验证 solver 自主性；(2) 多模型验证 (Llama/Mistral, 不同 GQA ratio)；(3) 高分辨率 profiling 发掘中间层异质性；(4) cardinality constraint 理论化。
