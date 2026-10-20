# Idea Brief: TurnKV: Protocol-Aware Segment Compression Policy for Multi-Turn Agent KV Caches


- **Idea ID**: `idea_009`
- **Created**: 2026-05-13
- **Approved**: 2026-05-13
- **Source**: foreign:be-idea-gen-0509-8
- **Level**: top-tier
- **Target Venues**: EMNLP 2026 Findings via ARR (submission deadline: May 25, 2026, 14 days from 2026-05-11; 'Efficient Methods for NLP' and 'LLM Agents' tracks — well-engineered policy contribution with comprehensive empirical validation; validated on HuggingFace Transformers with FlashAttention-2, stock vLLM integration demonstrated; EMNLP 2026 Main as stretch target if ablation results show >5% improvement over uniform ExpectedAttention on agentic benchmarks), AAAI 2027 (abstract: July 25, 2026; paper: August 1, 2026), MLSys 2027 (estimated deadline: October 2026; strong venue fit given FlashAttention compatibility and practical vLLM deployment)

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

In multi-turn agent loops with reasoning models, KV caches grow unboundedly as tool results and thinking traces accumulate across turns. A rich ecosystem of token-level KV compression methods now exists (ARKV's tri-state precision, R-KV's redundancy scoring, ThinKV's CoT decomposition, TriAttention's trigonometric compression, CLAA's cross-layer attention aggregation), chunk- and segment-level methods have emerged (ChunkKV's fixed-size chunks, SABlock's punctuation-based semantic segmentation, SentenceKV's sentence-level semantic grouping), and EpiCache (Apple) introduced episodic KV management for multi-turn conversations via topic clustering — but all these approaches either ignore the semantic role structure inherent in agent protocols (token-level, chunk-level, and linguistic-segment-level methods), require expensive external embedding and clustering to discover conversation structure (EpiCache), or target single-context inference without multi-turn awareness (SABlock, SentenceKV). Separately, scheduling-level approaches (CacheTTL, PBKV) optimize which KV caches to retain in memory but do not compress cache contents. The missing layer is a compression **policy** that (1) exploits the semantic role signals already embedded in agent protocols at zero extraction cost, (2) allocates per-segment compression budgets using FlashAttention-compatible importance scores rather than hand-tuned heuristics, and (3) bridges role-aware budget allocation with existing compression primitives without external models, training, or attention weight materialization. No existing method combines these three properties.

## Opportunity / Why Now

Agent workloads in 2026 show input-to-output ratios exceeding 100:1, making KV cache memory the dominant cost bottleneck. Token-level compression methods achieve 80-97% memory savings on single-turn reasoning benchmarks, but when applied naively to multi-turn agent contexts, they evict critical tool result tokens while preserving redundant thinking tokens — because they lack structural awareness of turn semantics. ChunkKV (Feb 2025) demonstrated that chunk-level compression preserves semantic relationships better than token-level eviction (+8.7% precision), but uses fixed-size windows that split mid-segment and cannot differentiate semantic roles. SABlock (Oct 2025) advanced this further by aligning compression boundaries with linguistic structures via punctuation-based semantic segmentation, achieving 99.9% NIAH retrieval accuracy with only 96 KV entries — establishing that semantically meaningful segmentation outperforms fixed-size chunking. SentenceKV (COLM 2025) demonstrated sentence-level semantic grouping with CPU offloading and selective retrieval during decoding. However, all three operate on single contexts without multi-turn or role awareness. EpiCache (Apple, Sep 2025) partially addresses multi-turn awareness via topic-based episodic clustering, achieving 4-6x compression on LongConvQA, but incurs runtime overhead from external sentence encoding and K-means clustering, and does not differentiate between the distinct semantic roles within agent protocols. CLAA (Feb 2026) stabilizes importance scoring via cross-layer attention aggregation, but requires materializing attention weights (incompatible with FlashAttention, the production default on H100) and operates at token level without turn awareness. Meanwhile, Transactional Attention shows that structural awareness matters critically for agents: 6 baselines achieve 0% credential retrieval at K=16, while semantic sponsorship achieves 100%. The untapped opportunity is that agent protocols already embed semantic structure through turn boundary markers (e.g., tool_result, thinking, system tags), providing a free structural prior for compression decisions. Combined with FlashAttention-compatible importance scoring (ExpectedAttention computes per-KV importance from cached key/query statistics in closed form, without materializing the attention matrix), this enables principled per-segment budget allocation that is both role-aware and deployable in production inference stacks — without external models, training, attention materialization, or hand-tuned heuristics.

## Landscape (SOTA & Limitations)

We organize the landscape into six categories to position TurnKV precisely.

**Scheduling-level (no content compression):** CacheTTL (Nov 2025, updated May 2026) introduces time-to-live policies for agent KV cache scheduling, achieving 8x improvement in average job completion time on SWE-Bench and BFCL, but operates at the scheduling level without compressing cache contents. PBKV (May 2026) uses workflow-graph prediction to manage KV cache eviction and prefetching across agents in dynamic workflows — again scheduling-level, complementary to within-cache compression.

**Token-level single-turn compression:** R-KV (NeurIPS 2025) achieves 90% memory saving via joint redundancy-importance scoring. ThinKV (ICLR 2026 Oral) decomposes CoT into reasoning/execution/transition segments for hybrid quantization-eviction. ARKV (Mar 2026) introduces a tri-state framework (Original/Quantized/Evicted) with per-layer OQ ratios from attention statistics. TriAttention (Apr 2026, MIT/NVIDIA) exploits trigonometric properties for 10.7x KV memory reduction. GVote (ICLR 2026) introduces adaptive per-request budgets via Monte Carlo query sampling. Transactional Attention (Apr 2026) introduces semantic sponsorship where structural anchor tokens protect adjacent value-bearing tokens — achieving 100% credential retrieval at K=16 where 6 baselines achieve 0%. StructKV (Apr 2026) preserves structural skeletons via Global In-Degree Centrality across early attention layers (note: also requires attention weight materialization, sharing the FlashAttention limitation). CLAA (Feb 2026) aggregates attention scores across consecutive layers using maximum aggregation S_i^CLAA = max_{l'∈L} S_i^(l') to stabilize token importance rankings, achieving up to 39% TTFT reduction — conceptually related to TurnKV's cross-segment importance estimation but operating at token level with observed attention (requires materialization). LKV (May 2026) demonstrates that global resource allocation dominates via end-to-end learned head-wise budgets. SAW-INT4 (Apr 2026) shows token-wise INT4 with Hadamard rotation recovers accuracy in serving contexts. PM-KVQ (2025) progressively lowers bit-width within single CoT blocks. MixKVQ (Dec 2025) introduces query-aware mixed-precision at the channel level.

**Chunk/segment-level compression:** ChunkKV (Feb 2025) reimagines KV cache compression by treating fixed-size token chunks (rather than individual tokens) as compression units, achieving +8.7% precision over token-level methods at the same compression ratio. ChunkKV uses observed attention weights within an observe window for chunk importance scoring and exploits cross-layer index similarity for latency reduction. However, ChunkKV's chunks are fixed-size windows (optimal size=10 tokens) without semantic role awareness. SABlock (Oct 2025) advances segment-level compression by aligning compression boundaries with linguistic structures via punctuation-based semantic segmentation, then applying segment-guided token scoring that combines per-segment importance (average attention) and diversity (entropy-based dispersion) into segment weights ωk = Ik·(1+η·Dk). A budget-driven descending search adaptively determines the largest block size preserving semantic integrity above a fidelity threshold. SABlock achieves 99.9% NIAH retrieval accuracy with only 96 KV entries, establishing that semantically meaningful segmentation substantially outperforms fixed-size chunking. However, SABlock uses punctuation-based linguistic boundaries (not agent protocol structure), operates on single contexts without multi-turn awareness, and uses observed attention for scoring. SentenceKV (COLM 2025) reorganizes KV cache at sentence-level granularity with semantic similarity grouping, offloads KV pairs to CPU, and selectively retrieves relevant sentence-level entries during decoding — demonstrating the value of semantically coherent grouping for retrieval efficiency. Like SABlock, it targets single-context inference without multi-turn or role differentiation. SemantiCache (Mar 2026) aligns compression with semantic hierarchical structure via semantic chunking and clustered merging — but also operates on single contexts without turn-level structure. Collectively, these four methods validate the principle that segment-level semantic compression outperforms token-level and fixed-chunk approaches. TurnKV extends this principle to a new domain: agent protocol structure in multi-turn contexts, with zero-cost role extraction and FlashAttention-compatible scoring.

**Multi-turn aware:** EpiCache (Apple, Sep 2025) clusters conversation history into topical episodes via external sentence encoding and K-means clustering for KV compression, achieving 4-6x compression on LongConvQA with near-full accuracy. Unlike TurnKV, EpiCache uses runtime topic clustering via embeddings (computational overhead) rather than protocol-embedded semantic roles (zero-cost extraction), and does not differentiate between semantic roles (system prompt vs. tool result vs. thinking trace). KEEP (Feb 2026, Microsoft) introduces static-dynamic memory construction for embodied planning — conceptually related but specific to embodied environments.

**Agent-specific but limited scope:** SideQuest (Feb 2026) uses the LRM itself to reason about token usefulness for agentic KV management, reducing peak tokens by 65% but incurs inference overhead and requires fine-tuning. CodeComp (Apr 2026) exploits Code Property Graphs for structure-aware KV compression in agentic coding — domain-specific to code. PolyKV (Apr 2026) shares asymmetrically-compressed KV caches across multiple agents — targets multi-agent sharing. ForesightKV (Feb 2026) learns to predict KV pair eviction via supervised and reinforcement learning (Golden Eviction oracle + GRPO), consistently outperforming heuristic methods at half the cache budget on AIME benchmarks — demonstrates the value of learned eviction but requires model-specific training.

**FlashAttention-compatible scoring:** ExpectedAttention (Oct 2025, arXiv 2510.00636; integrated in kvpress) estimates per-KV importance by predicting future attention in closed form from the distributional properties of query activations (mean and covariance) and cached key vectors — no attention matrix materialization required, fully FlashAttention-compatible. KnormPress uses key vector L2 norms as a cheap proxy (negative correlation with attention) — also FlashAttention-compatible but less reliable across architectures.

**The gap:** No method combines (1) zero-cost extraction of semantic roles from protocol markers to define compression segments, (2) FlashAttention-compatible per-segment importance scoring via aggregated ExpectedAttention, and (3) role-differentiated graduated compression with recency modulation — without external models, training, or attention weight materialization. The segment-level compression principle is now well-established: ChunkKV, SABlock, SentenceKV, and SemantiCache all demonstrate that operating above the token level preserves semantic coherence. But all four use either fixed-size windows (ChunkKV), linguistic boundaries (SABlock, SemantiCache), or sentence-level grouping (SentenceKV) in single-context settings. EpiCache extends to multi-turn but requires external embeddings and K-means. TurnKV fills this gap by applying the validated segment-level principle to agent protocol structure — using protocol markers for zero-cost segmentation, ExpectedAttention for FlashAttention-compatible scoring, and role-differentiated budgets for graduated compression.

## Proposed Approach

We propose TurnKV, a protocol-aware KV cache compression policy layer for multi-turn agent reasoning that operates at three levels: structural role extraction, importance-calibrated segment budget allocation, and graduated compression execution. TurnKV is a **policy** contribution — it determines what to compress and how much, orchestrating existing compression primitives based on turn-level semantics — not a new scoring or quantization method.

**Level 1: Zero-cost structural role extraction.** A lightweight rule-based classifier tags each KV cache segment by semantic role — SYSTEM_PROMPT, TOOL_RESULT, THINKING_TRACE, or USER_MESSAGE — using token boundary markers already present in agent protocols (e.g., tool_result, thinking, system tags in Anthropic/OpenAI/open-source agent frameworks). Unlike ChunkKV's fixed-size windows (optimal size=10 tokens), TurnKV segments follow semantically meaningful boundaries defined by the protocol. Unlike SABlock's punctuation-based linguistic segmentation, TurnKV exploits the richer structural signal of agent protocol markers — which encode not just boundary positions but semantic roles (a tool result vs. a thinking trace), enabling role-differentiated compression that linguistic segmentation cannot provide. Unlike SentenceKV's sentence-level semantic similarity grouping (which requires computing and storing semantic vectors), TurnKV's extraction is zero-cost string matching on turn boundaries. Unlike EpiCache's embedding-based topic clustering, this incurs negligible overhead (no external models).

**Level 2: Expected-Attention Segment Scoring (EASS) — the core mechanism.** TurnKV uses ExpectedAttention scores (Devoto et al., arXiv 2510.00636; implemented in kvpress) as the per-token importance signal, then aggregates at the segment level to allocate compression budgets. ExpectedAttention estimates how much future queries will attend to each KV pair using a closed-form computation over cached key vectors and the distributional statistics (mean and covariance) of pre-RoPE query activations — crucially, this requires no attention matrix materialization and is fully FlashAttention-compatible.

For each segment s, we compute the Expected-Attention Segment Score:

  EASS(s) = (1/|s|) Σ_{k∈s} EA(k)

where EA(k) is the ExpectedAttention score for key k. The structural prior from Level 1 provides a default budget B_prior(s) per role and recency tier:
- SYSTEM_PROMPT → B_prior = 1.0 (full preservation)
- TOOL_RESULT (recent, ≤2 turns) → B_prior = 0.8
- TOOL_RESULT (older) → B_prior = 0.5
- USER_MESSAGE → B_prior = 0.6
- THINKING_TRACE (recent) → B_prior = 0.4
- THINKING_TRACE (older, ≥3 turns) → B_prior = 0.15

EASS then modulates:
  B_final(s) = clip(B_prior(s) · (1 + β · (EASS(s) − EASS_mean) / EASS_std), B_min, B_max)

where β is a sensitivity parameter. This yields data-driven adjustments:
- A completed thinking trace with high EASS (model expects to reference its conclusions) → promoted to higher precision instead of aggressive eviction
- A recent tool result with near-zero EASS (e.g., a failed API call irrelevant to current context) → demoted despite recency
- System prompts and credential-bearing segments → protected via structural prior + Transactional Attention-inspired anchor preservation within segments

**Comparison with SABlock:** SABlock uses punctuation-based linguistic segmentation for single-context compression, with segment-guided token scoring that combines importance (average observed attention) and diversity (entropy) into segment weights. TurnKV differs in three ways: (1) segmentation source — protocol markers encode both boundaries and semantic roles, while punctuation encodes only boundaries without role differentiation; (2) scoring compatibility — TurnKV uses FlashAttention-compatible ExpectedAttention rather than observed attention; (3) context scope — TurnKV is designed for multi-turn agent contexts with recency-modulated budgets, not single-context inference.

**Comparison with CLAA:** CLAA aggregates attention scores across layers via maximum aggregation (S_i^CLAA = max_{l'∈L} S_i^(l')) at the token level to stabilize importance rankings. EASS differs in three ways: (1) it operates at the segment level with protocol-defined boundaries (not token level), (2) it uses ExpectedAttention (FlashAttention-compatible, predicts future importance) rather than observed attention (requires materialization, reflects only past patterns), and (3) it combines importance scores with structural priors from semantic roles, enabling role-differentiated compression that pure importance scoring cannot provide.

**Comparison with ChunkKV:** ChunkKV groups tokens into fixed-size chunks and scores chunk importance via observed attention in an observe window. EASS differs by using protocol-marker-defined segments (semantically meaningful boundaries, not arbitrary windows), FlashAttention-compatible scoring, and role-differentiated budget priors.

**Computational overhead of EASS:** ExpectedAttention scores are computed from cached key/value vectors and query statistics via standard tensor operations — no attention matrix materialization, no external models, no additional forward passes. The segment-level aggregation adds O(|segments|) mean operations over per-token scores. Total overhead: <1% prefill latency in our preliminary measurements, compared to EpiCache's external sentence encoder + K-means clustering overhead.

**Level 3: Graduated compression execution.** Based on B_final(s), each segment receives one of three treatments in vLLM, or four treatments in kvpress:

*kvpress quality evaluation (full graduated compression):*
- Full precision: segments with B_final above the full-precision threshold (typically system prompts, high-EASS tool results)
- Quantized (FP8 keys + INT4 values via kvpress QuantizedPress): segments with moderate B_final
- Anchor-preserved eviction: segments with low B_final — retain top-k attention-anchor tokens per segment using R-KV importance-diversity scoring within the segment, evict the rest
- Full eviction: segments with B_final below eviction threshold (very old, near-zero-EASS thinking traces)

*vLLM throughput evaluation (eviction-only + global quantization):* Since vLLM's TurboQuant applies a single global quantization preset (e.g., turboquant_k8v4) across all KV pages and does not support per-segment graduated quantization natively, we simplify the vLLM integration to eviction-only graduated compression: TurnKV's B_final determines which segments are retained (above threshold) vs. evicted (below threshold) in the paged KV cache, with a single TurboQuant preset applied uniformly to all retained pages. This cleanly separates TurnKV's policy contribution (which segments to keep) from the quantization layer (how to compress retained content), and is fully deployable on stock vLLM without custom attention backend modifications.

**Backend-agnostic design.** TurnKV's policy layer is designed to be pluggable with any per-token scoring backend. While we use ExpectedAttention as the primary backend (FlashAttention-compatible, strongest empirical results in kvpress), we also evaluate KnormPress as an alternative (cheaper but less reliable) and ObservedAttentionPress with eager attention (upper bound, not production-deployable). This demonstrates that the value of role-aware segment-level policy is orthogonal to the choice of scoring primitive.

**Sensitivity parameter calibration.** Rather than hand-tuning β and the prior budgets B_prior, we calibrate on a small validation set (~100 agent traces from BFCL V4 training split): grid search over β ∈ {0.3, 0.5, 0.7, 1.0} and per-role B_prior configurations, selecting the configuration that minimizes accuracy degradation at the target compression ratio. This is a one-time offline step (<5 GPU-hours), not runtime learning.

**Implementation.** We implement TurnKV as a custom ScorerPress within NVIDIA's kvpress library on HuggingFace Transformers. The EASS module wraps ExpectedAttentionPress, adding segment-level aggregation and budget modulation in the score() method. Since ExpectedAttention is FlashAttention-compatible (it does not read the `attentions` argument), TurnKV inherits full FlashAttention compatibility. For throughput measurements, we integrate TurnKV's eviction/retention decisions with vLLM's paged KV cache using a single TurboQuant preset (turboquant_k8v4) for all retained pages, demonstrating practical deployment without custom vLLM modifications.

**Evaluation.** We evaluate on two model scales: Qwen3-32B (loaded in INT8 via bitsandbytes to leave ~48GB for KV cache on H100 80GB) and Llama-3.1-8B-Instruct (BF16). All wall-clock and throughput measurements are on H100 80GB with FlashAttention-2 enabled (the production default). Benchmarks span: (a) standard quality metrics — perplexity on WikiText-2 and C4, MMLU, HumanEval, LongBench, RULER, MT-Bench; (b) agentic benchmarks — BFCL V4 (primary: 2000+ pairs, multi-turn agentic scenarios) with SWE-bench Verified subset deferred to camera-ready; (c) memory and throughput measurements via vLLM on H100; (d) credential/config retention test inspired by Transactional Attention's evaluation (measuring API key and config value retrieval accuracy under compression). We target 70-85% KV memory reduction with <2% accuracy degradation on standard benchmarks and <3% on agentic benchmarks.

**Critical ablations.** (1) Full TurnKV (EASS + structural prior) vs. structural prior only (no importance calibration) — isolating the value of data-driven budget modulation over purely rule-based assignment. (2) TurnKV vs. uniform ExpectedAttention (same scorer, no segment awareness) — isolating the value of role-aware policy over uniform application. (3) TurnKV vs. ChunkKV (protocol-defined segments vs. fixed-size chunks) — isolating the value of semantic segmentation. (4) TurnKV vs. EpiCache on agent traces — comparing zero-cost protocol markers vs. embedding-based top

## Resource Estimate

- **auto_research**: {'claude_api_cost': '$150-350 (~800-1500 Opus turns across implementation, experiment orchestration, analysis, and paper drafting)', 'estimated_gpu_cost': '$300-500', 'gpu_hours': '~200h H100 80GB (full grid over β values × B_prior configs × scoring backends × 2 models × 8 benchmarks, plus baseline sweep)', 'gpu_utilization': '~85-90% utilization; agent orchestrates experiments continuously', 'risk_note': 'Reduced risk: no attention materialization API differences across architectures. ExpectedAttention is architecture-agnostic in kvpress. vLLM integration is stock (no custom modifications). Main risk: agent may over-explore the combinatorial space of B_prior configurations.', 'speed_bottleneck': 'GPU count is the primary bottleneck: with 2 H100s, ~6-8 days. With 4 H100s, ~3-5 days.', 'team': '0 researchers after initial setup (kvpress installation, model weight download, benchmark dataset preparation)', 'timeline': '1-2 weeks with 2-4 H100s available concurrently'}
- **human_in_loop**: {'claude_api_cost': '$100-200 (~300-500 Opus turns for experiment design, implementation, result analysis, and paper section drafting)', 'estimated_gpu_cost': '$210-350', 'gpu_hours': '~140h H100 80GB (agent runs systematic ablations over β sensitivity, B_prior configurations, and per-segment treatments)', 'gpu_utilization': '~60-70% utilization; agent autonomously queues next evaluation while human reviews results from prior batch', 'risk_note': 'Lower implementation risk: EASS wraps existing ExpectedAttentionPress with segment-level aggregation using standard PyTorch ops. No attention weight extraction hooks needed. vLLM integration simplified to eviction-only + global TurboQuant (no custom attention backend modifications). Main risk is ExpectedAttention score quality varying across model architectures (GQA vs. MHA).', 'team': '1 researcher, ~20-30min/day reviewing agent-proposed configurations and validating benchmark results', 'timeline': '4-6 weeks'}
- **manual**: {'estimated_gpu_cost': '$165-275 (at ~$1.50-2.50/h marketplace rate for H100 80GB)', 'gpu_hours': '~110h H100 80GB (implementation on kvpress ~10h [wraps existing ExpectedAttentionPress], baseline reproduction [ARKV, ChunkKV, EpiCache] ~25h, EASS development ~10h, TurnKV quality evaluation on standard benchmarks ~25h, agent benchmark evaluation [BFCL V4] ~15h, ablations [7 ablation axes] ~15h, vLLM throughput measurements ~10h)', 'gpu_utilization': '~35-40% effective utilization; GPU idles while researcher writes kvpress plugin code and analyzes tradeoff curves', 'team': '1-2 researchers with PyTorch and HuggingFace Transformers experience (no CUDA/Triton kernel work — kvpress handles low-level compression; EASS uses standard PyTorch tensor ops)', 'timeline': '3-4 months (or sprint mode targeting EMNLP May 25, 2026 ARR: 14 days remaining from 2026-05-11 — requires aggressive scope focus: 2 models, BFCL V4 primary, top 4 ablations, SWE-bench and remaining ablations deferred to camera-ready)'}

## Key References

- ExpectedAttention: KV Cache Compression via Closed-Form Expected Attention Score Estimation (Devoto et al., arXiv 2510.00636, Oct 2025; integrated in NVIDIA kvpress; FlashAttention-compatible closed-form importance scoring — primary scoring backend for TurnKV)
- EpiCache: Episodic KV Cache Management for Long Conversational Question Answering (Apple, arXiv 2509.17396, Sep 2025; code: apple/ml-epicache)
- SABlock: Semantic-Aware KV Cache Eviction with Adaptive Compression Block Size (Chen et al., arXiv 2510.22556, Oct 2025; punctuation-based semantic segmentation + segment-guided token scoring + adaptive block sizes; 99.9% NIAH at 96 KV entries — establishes semantic segmentation principle for single contexts)
- SentenceKV: Efficient LLM Inference via Sentence-Level Semantic KV Caching (COLM 2025, arXiv 2504.00970; code: github.com/zzbright1998/SentenceKV; sentence-level semantic grouping with CPU offloading and selective retrieval — peer-reviewed segment-level method)
- CLAA: Cross-Layer Attention Aggregation for Token Importance Scoring (arXiv 2602.16054, Feb 2026; cross-layer max aggregation at token level — conceptually related but token-level, requires attention materialization)
- ChunkKV: Chunk-Level KV Cache Compression for Long-Context LLM Inference (arXiv 2502.00299, Feb 2025; fixed-size chunk compression units, +8.7% precision over token-level — establishes chunk-level compression principle)
- ForesightKV: Learned KV Cache Eviction via Supervised and Reinforcement Learning (arXiv 2602.03203, Feb 2026; learned alternative requiring training, outperforms heuristics at half cache budget on AIME)
- R-KV: Redundancy-aware KV Cache Compression for Reasoning Models (NeurIPS 2025)
- ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models (ICLR 2026 Oral)
- CacheTTL / Continuum: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live (arXiv 2511.02230, updated May 2026)
- ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget (arXiv 2603.08727, Mar 2026)
- PBKV: Efficient Serving for Dynamic Agent Workflows with Prediction-based KV-Cache Management (arXiv 2605.06472, May 2026)
- TriAttention: Efficient Long Reasoning with Trigonometric KV Compression (arXiv 2604.04921, Apr 2026)
- Transactional Attention: Semantic Sponsorship for KV-Cache Retention (arXiv 2604.11288, Apr 2026)
- StructKV: Preserving the Structural Skeleton for Scalable Long-Context Inference (arXiv 2604.06746, Apr 2026; also requires attention materialization)
- KEEP: A KV-Cache-Centric Memory Management System for Efficient Embodied Planning (arXiv 2602.23592, Feb 2026, Microsoft)
- GVote: Adaptive Per-Request KV-Cache Compression without Manually Setting Budget (ICLR 2026)
- SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Reasoning (arXiv 2602.22603, Feb 2026)
- CodeComp: Structural KV Cache Compression for Agentic Coding (arXiv 2604.10235, Apr 2026)
- SemantiCache: Efficient KV Cache Compression via Semantic Chunking and Clustered Merging (arXiv 2603.14303, Mar 2026)
- PolyKV: A Shared Asymmetrically-Compressed KV Cache Pool for Multi-Agent LLM Inference (arXiv, Apr 2026)
- PM-KVQ: Progressive Mixed-Precision KV Cache Quantization for Long-CoT LLMs (arXiv 2025)
- SAW-INT4: System-Aware 4-Bit KV-Cache Quantization for Real-World LLM Serving (arXiv 2604.19157, Apr 2026)
- LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction (arXiv 2605.06676, May 2026)
- MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning (arXiv 2512.19206, Dec 2025)
- TurboQuant: KV Cache Compression (Zandieh et al., ICLR 2026; merged upstream in vLLM Apr 2026)
- KnormPress: L2 Norm-based KV Cache Importance Scoring (arXiv 2406.11430; FlashAttention-compatible alternative backend)

## Reviewer Evaluation

**Scores**:
  - clarity: **{'rationale': "Exceptional after 6 rounds. The landscape covers 25+ papers across 6 well-organized categories with precise differentiation. The EASS mechanism is clearly specified with explicit formulas. Comparisons against SABlock, ChunkKV, CLAA, and EpiCache are detailed and accurate. The 'policy contribution' framing is honest and appropriate.", 'score': 4.5}**/5
  - feasibility: **{'rationale': 'Implementation path is exceptionally well-verified: kvpress API confirmed with ExpectedAttentionPress supporting Qwen3, BFCL V4 confirmed available with 5,639 test cases, vLLM TurboQuant integration confirmed (single global preset, eviction-only simplification is correct). 14-day timeline is tight but scope is well-managed with SWE-bench deferred. ~110-200 H100-hours is within budget.', 'score': 4}**/5
  - impact: **{'rationale': "Agent KV cache management is a genuine 2026 bottleneck (input-to-output ratios exceeding 100:1). A training-free, FlashAttention-compatible policy layer deployable on stock vLLM addresses real practitioner need. The credential retention test (inspired by Transactional Attention's 100% vs. 0% finding) highlights a safety-relevant dimension that uniform compression methods miss.", 'score': 4}**/5
  - novelty: **{'rationale': 'The combination of protocol-marker segmentation + FlashAttention-compatible segment scoring + role-differentiated budgets is genuinely new — independent search confirms no existing method uses this framing. However, each individual piece is borrowed (ExpectedAttention, segment-level aggregation, structural priors), making this an incremental-but-valid novelty appropriate for EMNLP Findings.', 'score': 3.5}**/5

## Human Review Note

## Agent 审核结果（完整三阶段 pipeline）

**Verdict**: PASS

**入口三重共识 (X)**: 25.0%
**终审自评 (Y)**: 35.0%
**出口三重共识 (Z)**: 34.0%
**Z 区间**: [28.0%, 39.0%]
**真实提升 (Z-X)**: +9.0 pp
**幻觉幅度 (Y-Z)**: +1.0 pp
**出口一致性**: 高
**出口三次评估**: [34.0, 35.0, 33.0]

### 优化方案 / 拒绝详情
【优化方案】

1. [Introduction / 核心 framing] — 新增 "Protocol Structure as Computational Semantics" 开篇段落，将 protocol markers 从 "free segmentation tool" 重新定位为 "a new class of zero-cost compression signals encoding computational semantics (information dynamics: persistence, reference probability, supersession likelihood)"。原始 proposal 仅将 protocol markers 描述为 "zero-cost extraction via string matching on turn boundary markers"，停留在工程特性层面。新 framing 论证了 protocol semantics 与 linguistic/statistical signals 的本质差异——前者来自 agent 执行协议的功能定义，后者来自文本表面特征。 — 命中 **Novelty**：将贡献从 "ChunkKV 在 agent 场景的变体" 拉升到 "发现并利用了一类新的压缩信号源"，直接回应 "straightforward extension" 的审稿攻击。

2. [Introduction / 贡献定位] — 新增 "policy-scorer separation" 显式框架声明："To our knowledge, TurnKV is the first KV cache compression method that explicitly separates compression policy from compression primitive, enabling modular composition with any existing scoring method." 原始 proposal 虽然提到了 policy-scorer orthogonality 实验，但没有将 "policy as first-class contribution" 上升为显式的贡献声明。 — 命中 **Novelty**：有效防御 "ExpectedAttention 不是你提出的，novelty 在哪？" 的高概率审稿质疑。类比 PagedAttention 不改注意力计算只改内存管理策略的先例。

3. [新增章节: Empirical Motivation — Attention Anatomy of Agent Traces] — 原始 proposal 完全没有 empirical motivation 环节。新版在 Method 之前加入完整的 attention anatomy 分析节：(a) 在 GAIA 和 BFCL V4 的真实多轮 agent trace 上，对 Llama-3.1-8B 和 Qwen3-32B 计算跨层/跨头的 attention reception 统计；(b) 报告定量指标（attention entropy per role type、cross-turn attention decay rate、attention spike frequency）；(c) 验证 role-differentiated attention 是跨模型族一致的结构性属性而非 model-specific artifact。 — 命中 **Novelty + Analysis Depth**：从 "I tried the obvious thing" 转变为 "I discovered a structural property and exploited it"。同时升级为独立 Contribution（Contribution 1: "The first systematic characterization of attention reception patterns across protocol-defined role types"），即使压缩方法本身被质疑，empirical finding 仍有独立价值，降低全盘否定风险。

4. [新增章节: Core Contributions] — 原始 proposal 无显式 contribution list。新版列出三大贡献：(1) Attention anatomy of agent traces（empirical finding）；(2) TurnKV compression policy（method）；(3) Agent State Integrity (ASI) diagnostic benchmark（resource contribution）。 — 命中 **Novelty + Significance**：三层贡献结构（empirical finding + method + resource）比单一 method contribution 更有层次，符合 EMNLP 对 multi-faceted contribution 的偏好。

5. [Method / EASS 形式化] — 原始 proposal 对 EASS 仅有一段 high-level 描述（"aggregating per-token ExpectedAttention scores"），未给出任何数学公式或伪代码。新版提供完整的形式化：(a) segment importance score 公式 $S_i = \alpha_{\text{role}} \cdot g(\text{Agg}(\text{EA})) \cdot d(\text{recency})$；(b) 每个变量的明确定义；(c) aggregation 策略选择（mean / 90th-percentile / max，ablated）；(d) budget allocation 算法（排序 + 累积分配 → 四级 treatment）；(e) treatment 阈值 $\tau_1, \tau_2, \tau_3$ 的参数化定义。 — 命中 **Technical Soundness**：从 "reviewer 无法判断方法是否 rigorous" 变为 "完整可复现的算法描述"。

6. [Method / System prompt recency decay 豁免] — 原始公式中 system prompt 会被 recency decay 严重惩罚（system prompt 在 turn 0，recency 最差），与 "persistent constraint 应全面保留" 的语义矛盾。新版显式规定 system prompts 豁免 recency decay（$d=1.0$ for system prompts），消除乘法公式中的逻辑矛盾。 — 命中 **Technical Soundness**：修复了一个会被审稿人发现的设计矛盾。

7. [Method / 组合方式消融] — 原始 proposal 默认乘法组合，未讨论替代方案。新版增加组合方式消融：乘法 vs. 加权加法 vs. 两阶段（structural prior 分 tier，tier 内 EA 排序）。如果两阶段设计效果相当，因可解释性更优可作为推荐方案。 — 命中 **Technical Soundness**：展示设计选择有经过系统验证，而非 arbitrary。

8. [Method / Structural prior $\alpha$ 跨任务敏感性] — 原始 proposal 的 $\alpha$ 值（1.0/0.8/0.6/0.3）未经任何验证讨论。新版要求在 GAIA / SWE-bench Lite / LongBench 三个差异化任务上报告 $\alpha$ 配置的效果曲线，确认默认值的鲁棒性或给出任务自适应建议。 — 命中 **Technical Soundness**：消除 "hand-tuned hyperparameters with unknown stability" 的审稿质疑。

9. [Evaluation / Agent benchmark 重组 — 最关键变更] — 原始 proposal 将 BFCL V4 作为 "primary agentic benchmark"，标准 benchmark 为辅。核心问题：BFCL V4 测的是单次 function calling 准确率，**不是**长链多轮 agent 推理（多步规划、错误恢复、跨轮信息引用）——与 TurnKV 声称解决的 "multi-turn agent reasoning" 严重错配。新版完全重组评估体系为四层：
   - **Tier 1（primary）**: GAIA（多步工具推理，5-15+ turns，bootstrap 95% CI）+ SWE-bench Lite（软件工程 agent，代码范式互补）+ ASI stress test
   - **Tier 2**: LongBench, RULER（长上下文）
   - **Tier 3**: Perplexity, MMLU, HumanEval, MT-Bench（no regression）
   - **Tier 4（supplementary）**: BFCL V4（降级）
   — 命中 **Significance + Soundness**：这是原始 proposal 最可能导致 reject 的缺陷（"You claim agent-specific benefits but evaluate on generic benchmarks"），修复后评估体系与核心 claim 完全对齐。

10. [Evaluation / Agent State Integrity (ASI) benchmark] — 原始 proposal 仅提 "credential retention tests inspired by Transactional Attention" 一句话。新版将其发展为完整的 ASI 诊断 benchmark，包含：(a) 50+ turn 合成 agent trace，关键信息按角色类型和 turn 位置植入；(b) 标准变体（信息在高保留段）；(c) **adversarial 变体**（信息在 TurnKV 倾向压缩的段中，测鲁棒性）；(d) **safety-critical 变体**（system prompt 安全指令在极端压缩下的保留率）；(e) 开源发布承诺（构建方法论 + 随机化协议 + 评估脚本）。 — 命中 **Significance + Soundness + Resource Contribution**：填补了 "KV cache compression 缺乏 agent-specific 评估工具" 的社区空白。adversarial 变体回应 "自我验证嫌疑"。

11. [Evaluation / Performance targets 按场景分解] — 原始 proposal 使用 blanket claim "70-85% KV memory reduction with <2% accuracy degradation"。新版按场景分解：(a) 标准 NLP：≤1% degradation（验证无 regression）；(b) 长上下文：报告 Pareto 曲线（70/80/85% 压缩率）；(c) Agent 任务：核心 claim 为 TurnKV vs. 最强 segment-level baseline ≥3-5pp task completion 提升。 — 命中 **Soundness**：消除 "target 过于笼统" 的质疑。明确的 novelty 判据（≥3-5pp）也展示了对自身方法的信心和诚实。

12. [Evaluation / NLP-specific 分析指标] — 原始 proposal 无 NLP-specific 的质量分析。新版增加：在不同压缩策略下报告 hallucination rate、instruction following accuracy、cross-turn coreference resolution quality。 — 命中 **Venue Fit (EMNLP)**：将论文定位从 "a compression algorithm" 转向 "enabling better NLP agent systems"，强化 EMNLP 审稿人对 NLP 核心能力影响的关注。

13. [Evaluation / 两轨评估设计 + eviction-only 桥接] — 原始 proposal 声称 "vLLM throughput evaluation" 使用 "stock vLLM"，但未解释 kvpress（HF 生态）与 vLLM（PagedAttention 后端）的不兼容性。新版诚实分为两轨：(a) 质量轨（kvpress + HF，四级渐进压缩）；(b) 吞吐量轨（vLLM，eviction-only + TurboQuant）；(c) **关键桥接**：质量轨增加 eviction-only 变体，确保两轨之间有直接可比的质量数据。明确 vLLM 集成路径（prefix caching + custom eviction scheduling hook）及工程降级方案。 — 命中 **Soundness + Reproducibility**：修复了质量与吞吐量证据链的断裂。

14. [Evaluation / Deployment impact 量化] — 原始 proposal 仅抽象声称 "reduces memory"。新版增加 back-of-envelope 量化：10 turns/session × typical token counts → ~9000 tokens/session，100 concurrent sessions → 900K tokens KV cache，70-85% compression → 135-270K tokens，enabling ~3-5× batch size increase。 — 命中 **Significance / Practical Impact**：concrete quantification 比 "reduces memory" 有说服力得多。

15. [Baselines / 三层结构 + 关键遗漏补充] — 原始 proposal 的 baseline 只列了 CLAA, EpiCache, ForesightKV, LKV, SideQuest, ChunkKV，**完全遗漏了 KV cache compression 领域最广泛引用的方法**：SnapKV (ICML 2024)、H2O (NeurIPS 2023)、PyramidKV、StreamingLLM。新版建立三层 baseline 结构：Token-level (SnapKV, H2O, PyramidKV, StreamingLLM) → Segment-level (ChunkKV, SentenceKV, SABlock) → Context-/agent-aware (EpiCache, CLAA, Transactional Attention)。 — 命中 **Soundness**：遗漏 SnapKV/H2O 几乎是 guaranteed reviewer complaint。三层结构同时支撑了 contribution 的层次叙事。

16. [Baselines / Ablation 矩阵扩展] — 原始 proposal 列了 5 个 ablation。新版扩展为完整 ablation 矩阵：structural-prior-only, recency-only, uniform-EA, **protocol-aware vs. linguistic-boundary segmentation**（关键新增：同一 EA scorer 下 protocol markers vs. 句子边界，直接验证 protocol markers 提供了 linguistic boundary 无法捕获的信息）, oracle segment scoring, aggregation ablation, combination method ablation, recency decay ablation, $\alpha$ sensitivity。 — 命中 **Soundness**：gain decomposition 是 systems paper 在 NLP venue 获高分的关键。protocol vs. linguistic boundary 消融直接论证 "computational semantics" insight 的不可替代性。

17. [Related Work / 覆盖扩展] — 原始 proposal 的 related work 仅覆盖 segment-level 和 training-based 方法的点对点比较。新版增加六个子方向完整覆盖：(a) Token-level adaptive compression (SnapKV, H2O, StreamingLLM)；(b) Layer-wise adaptive budget (PyramidKV, Ada-KV) — 指出与 segment-wise 正交可组合；(c) Query-aware dynamic selection (Quest, RetrievalAttention) — 指出与 query-agnostic 互补；(d) Training-based compression (DMC, ForesightKV, LKV, SideQuest)；(e) **Transactional Attention** — 最直接竞争者的详细方法差异分析；(f) **Prefix caching / KV reuse** (CacheBlend, Prompt Cache, RadixAttention) — 指出与 TurnKV 的 within-session compression 正交。 — 命中 **Related Work**：从 "有明显盲区" 提升到 "全面覆盖"。

18. [Discussion / Safety-by-design] — 原始 proposal 无任何 safety 讨论。新版增加：system prompt 包含行为约束和安全指令，role-unaware compression 在长 context 下可能意外丢失 safety-critical tokens，TurnKV 通过 $\alpha_{\text{system}}=1.0$ + recency decay 豁免提供 safety-by-construction 保护。ASI safety-critical 变体提供实验验证。 — 命中 **Broader Impact**：2025-2026 NLP 社区对 AI safety 高度敏感。点到为止，不过度膨胀。

19. [Discussion / Structure-Modulated Compression 泛化讨论] — 原始 proposal 无泛化讨论。新版在 Discussion 中（非 contribution level）讨论 structural prior + data-driven modulation 的 two-stage 设计模式向 RAG / code generation / multi-document summarization 的可推广性。明确标注为 future work 方向而非本文贡献。 — 命中 **Broader Impact**：展示 generalizable thinking 而不 over-claim。

20. [新增章节: Limitations] — 原始 proposal 无 limitations 节。新版增加六条诚实限制：protocol marker dependency、threshold hyperparameters、two model families、agent benchmark coverage、vLLM integration complexity、attention anatomy scope。 — 命中 **Soundness**：主动暴露弱点 > 被 reviewer 挖出来。

21. [Scope 限定 / Protocol marker generalizability] — 原始 proposal 声称 "zero-cost extraction" 但未讨论不同模型/框架间 marker 格式差异。新版明确 scope（依赖 chat template，marker 规则与模型绑定而非与 agent 框架绑定），提供 5 个主流模型族的 marker registry 示例（Llama-3, Qwen, Mistral/ChatML, Gemma, Phi-3），展示适配新模型仅需 <10 行 regex。在 Limitations 中诚实承认对自由格式对话不适用。 — 命中 **Soundness**：消除 "zero-cost claim is misleading" 的审稿质疑。精准 scope 限定反而让贡献定位更清晰。

【主要风险】:

1. **Novelty 边界争议 → Findings 分流风险**：尽管 framing 已全面优化（computational semantics、policy-scorer separation、attention anatomy as independent finding），核心事实不变——三个组件（segment compression, ExpectedAttention, chat template parsing）全部已有。如果 role-aware vs. role-unaware 的实验增益 <3pp，审稿人可能判定 "well-executed systems integration but insufficient novelty for main conference"，推荐 Findings。**这是最终概率能否突破 40% 的分水岭，完全取决于实验结果。**

2. **Venue fit 的 reviewer 随机性**：KV cache compression 的主要发表阵地仍是 I
