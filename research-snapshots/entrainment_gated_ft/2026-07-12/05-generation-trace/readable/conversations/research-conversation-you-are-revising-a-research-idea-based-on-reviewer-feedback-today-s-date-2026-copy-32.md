# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-11 (UTC).** ## Original idea { "tit

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-1/91be2f02-e30d-47e4-8888-aa49b5f1487c.jsonl`
- **Structured JSON:** [`6c90ca0eeda43f4672df.json`](../../sessions/6c/6c90ca0eeda43f4672df.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T00:03:29.729Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T00:03:29.729Z",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-11 (UTC).**\n\n## Original idea\n{\n  \"title\": \"CompressLink: Co-Optimizing Compression and Restoration for Position-Independent KV Cache Serving\",\n  \"core_problem\": \"Production RAG systems redundantly reprocess ~75% of retrieved chunks across queries (Cache-Craft, SIGMOD 2025). Position-independent caching (PIC) avoids this recomputation by storing chunk KVs without positional encodings for arbitrary-position reuse, and MEPIC (arXiv 2512.16822) further reduces HBM usage by 2x over EPIC via RoPE fusion and NoPE storage — yet cached KV states remain at full precision. A single Llama-3.1-8B instance caching 100K chunks at 512 tokens each requires ~3.2TB of KV storage. Meanwhile, KV compression methods like KVTC (ICLR 2026) achieve 8-20x storage reduction via PCA decorrelation + adaptive quantization + entropy coding. MEPIC explicitly identifies KV compression as an orthogonal direction 'that can be seamlessly combined with existing KV compression methods,' and KV Packet (arXiv:2604.13226) demonstrates compatibility of adapter-based PIC with eviction-based compression — but both treat compression and restoration as independent stages. This independence is suboptimal: compression degrades all tokens uniformly regardless of whether they will be restored, and restoration selects tokens based on query relevance or positional heuristics without accounting for which tokens suffered most from compression. No prior work jointly optimizes the compression-restoration pipeline for chunk KV caching.\",\n  \"opportunity\": \"MEPIC and KVTC share a structural element: both store KV without RoPE (NoPE format). MEPIC stores NoPE KVs for position-independent reuse with RoPE applied on-the-fly; KVTC removes RoPE before PCA compression. This alignment enables natural composition — KVTC compression applied to MEPIC's NoPE KV stores, with decompressed KVs fed into MEPIC's RoPE-fusion attention path. However, naive composition treats compression and restoration as independent stages, wasting compression bits on tokens that will be restored anyway and missing restoration opportunities on tokens with high compression error. We identify a bidirectional optimization opportunity: (1) At compression time, tokens in restorable positions (boundary tokens always recomputed by MEPIC, or tokens frequently selected by query-driven methods) can tolerate aggressive compression since they will be replaced with fresh KVs — reallocating their bits to persistent tokens improves overall quality. (2) At restoration time, per-token compression error (analytically computable from PCA residuals and quantization step sizes at decompression, requiring zero additional forward passes) provides an orthogonal signal to query relevance for selecting which tokens to recompute — prioritizing tokens that are both query-relevant AND high-compression-error yields better quality per recomputed token. Additionally, KVTC's PCA basis calibrated on full-sequence KVs is suboptimal for independently-encoded chunks due to distribution mismatch (local vs. global attention sinks, absent cross-chunk attention), motivating chunk-aware recalibration. KV Packet (arXiv:2604.13226, Section 4.4) demonstrates that adapter-based PIC is robust to eviction-based compression (CUR, KVzap, LeverageScore, TOVA) at 10-50% retention rates — but this tests token-pruning compression, not transform coding (PCA + quantization + entropy coding) at 8-20x rates, and does not optimize the compression-restoration interface. Our approach is the first to jointly optimize this interface.\",\n  \"landscape\": \"Position-independent KV caching: MEPIC (arXiv 2512.16822, Dec 2025) achieves 2x HBM reduction over EPIC via NoPE KV storage, block-level recomputation (first block per chunk is request-specific), and RoPE fusion in fused attention kernels; integrated into vLLM + LMCache serving stack; evaluated on Mistral-7B-Instruct-v0.3 across SQuAD, NewsQA, NarrativeQA, emrQA. EPIC (ICML 2025) recomputes k≤32 boundary tokens via LegoLink. ProphetKV (arXiv:2602.02579, Feb 2026) introduces user-query-driven selective recomputation, achieving 96-101% accuracy at 20% recomputation ratio; evaluated on Llama-3.1-8B, Qwen2.5-14B, Qwen-3-14B (per the paper's evaluation tables). InfoFlow KV (arXiv:2603.05353, March 2026) casts selective recomputation as an information flow problem using prompt-conditioned attention norms under inference-consistent RoPE geometry; does not consider compression. KVLink (NeurIPS 2025) adjusts RoPE positions with trainable link tokens. Cache-Craft (SIGMOD 2025) stores chunk KVs without RoPE. CacheSlide (FAST 2026) uses learned weights for cross-position-aware reuse. CacheBlend (EuroSys 2025) selectively recomputes tokens based on output deviation. KV Packet (arXiv:2604.13226, April 2026) uses trainable soft-token adapters for recomputation-free PIC; Section 4.4 tests compatibility with 5 eviction-based compression methods (CUR, KVzap, LeverageScore, TOVA, random pruning) at 10-50% retention, claiming PIC 'natively bypasses bottlenecks' of compression-impaired recomputation — but tests token eviction, not transform coding, and does not optimize the compression-restoration interface. FusionRAG (PACMMOD/SIGMOD 2026) embeds cross-chunk information offline. A systematic CLC study (arXiv 2603.20218, March 2026) compared 11 chunk-level caching strategies but did not examine compression. KV compression: KVTC (ICLR 2026) achieves 8-20x compression via PCA decorrelation + adaptive quantization + entropy coding, removing RoPE before PCA; maintains <1pp accuracy drop at 20x on most tasks; bit allocation via DP minimizes reconstruction MSE. RateQuant (arXiv:2605.06675, May 2026) applies rate-distortion theory for mixed-precision per-head quantization via reverse waterfilling, reducing KIVI's perplexity from 49.3 to 14.9 on Qwen3-8B at 2.5 bits with 1.6s calibration; principled bit allocation without PCA. eOptShrinkQ (arXiv:2605.02905, May 2026) achieves near-lossless compression via optimal spectral denoising + quantization, saving ~1 bit/entry. HeadQ (arXiv:2605.03562, May 2026) measures distortion in model-visible score space rather than storage space, achieving 94% excess perplexity removal at 2 bits. DynaKV (arXiv:2603.04411, March 2026) provides per-token adaptive PCA rank via learned gating — requires fine-tuning (128M tokens), operates on full-sequence KVs. 'Quantization Dominates Rank Reduction' (arXiv:2604.11501, April 2026) shows quantization outperforms dimension-discarding PCA projection but tests rank reduction, not decorrelation-before-quantization as KVTC uses. CacheGen (SIGCOMM 2024) achieves 3.5-4.3x via tensor encoders. KVzip (NeurIPS 2025 Oral) provides 3-4x eviction-based compression. Joint Encoding of KV-Cache Blocks (Jan 2026) fuses similar blocks achieving 4.38x. No prior work jointly optimizes KV compression bit allocation with selective restoration token selection in the chunk-caching setting — compression and restoration are universally treated as independent stages.\",\n  \"approach\": \"We propose CompressLink, a framework that co-optimizes KV compression and quality restoration for position-independent chunk caching, built on the shared NoPE representation of MEPIC and KVTC. CompressLink introduces two novel algorithms — Restoration-Aware Bit Allocation (RABA) and Compression-Error-Guided Restoration (CEGR) — that jointly optimize the compression-restoration pipeline, plus chunk-aware PCA calibration as a supporting technique. **Offline Compression Pipeline:** Each document chunk is independently encoded through the LLM; MEPIC stores the resulting KV caches in NoPE format. Before KVTC compression, PCA bases are calibrated on independently-encoded chunk KVs (matching inference-time distribution, addressing the calibration mismatch from full-sequence KVs). RABA then modifies KVTC's DP-based bit allocation: each token position is assigned a restoration probability p_r(t) based on positional priors — boundary tokens (first block per chunk, always recomputed by MEPIC) get p_r ≈ 1.0; tokens frequently selected across calibration queries by ProphetKV-style scoring get intermediate p_r; remaining tokens get p_r ≈ 0. The DP objective is modified from minimizing total reconstruction MSE to minimizing restoration-weighted MSE: sum over tokens t of (1 - p_r(t)) * MSE(t), so that bits are reallocated from high-restoration-probability tokens (whose compressed values will be overwritten) to persistent tokens (whose compressed values must survive). At 20% recomputation ratio, this effectively concentrates the full bit budget on 80% of tokens, improving quality where it matters. Compressed KVs (PCA transform → RABA-allocated quantization → entropy coding) are stored in LMCache's persistence layer. **Online Restoration Pipeline:** Retrieved chunks' compressed KVs are decompressed (entropy decode → dequantize → PCA inverse). CEGR computes per-token compression error estimates analytically from decompression: for each token, error_c(t) = sum over PCA components j of (Δ_j² / 12) where Δ_j is the quantization step size for component j at the allocated bit width — this requires zero additional forward passes, only the bit allocation metadata stored alongside compressed KVs. CEGR then combines this with a query relevance signal r_q(t) obtained from a lightweight attention probe (single-layer attention of the query against decompressed keys, following ProphetKV's first-pass scoring). The joint restoration score is: score(t) = r_q(t) * error_c(t)^β, where β controls the compression-error sensitivity. Tokens with highest joint scores are selected for recomputation within the budget. The key insight: a query-relevant token with low compression error needs no recomputation (compression preserved it); a high-error token irrelevant to the query wastes recomputation budget. Only tokens that are both query-relevant AND high-error benefit maximally from recomputation. MEPIC's fused RoPE-attention kernel applies positional encodings on-the-fly during final attention computation over the mix of recomputed and decompressed KVs. **Joint Optimization Loop:** RABA and CEGR share the restoration probability model — RABA's p_r(t) at compression time is calibrated to match CEGR's empirical restoration rate at inference time. During calibration, we run CEGR on calibration queries to estimate per-position restoration frequencies, then feed these back into RABA's DP allocation. This creates a consistent compression-restoration contract: positions that CEGR frequently restores are precisely those where RABA saves bits. **Contributions:** (1) RABA — a novel restoration-aware bit allocation algorithm that extends rate-distortion-optimal quantization (cf. RateQuant's reverse waterfilling, KVTC's DP) with position-dependent restoration weights, provably reducing effective MSE on persistent tokens at matched total bit budgets. Differentiation from RateQuant: RateQuant allocates across heads, RABA allocates across token positions within each head; RateQuant is restoration-unaware. Differentiation from DynaKV: DynaKV allocates per-token PCA rank via learned gating (requires fine-tuning), RABA allocates per-token bit budget via restoration probability (training-free, calibration only). (2) CEGR — a novel compression-error-guided restoration algorithm that augments query-relevance-based token selection with an analytically-derived compression error signal, available at zero additional compute cost from decompression metadata. Differentiation from ProphetKV: ProphetKV selects on query relevance alone; CEGR adds the compression error dimension. Differentiation from CacheBlend: CacheBlend uses output deviation (requires early-layer forward passes); CEGR uses analytical error estimates (zero forward passes). Differentiation from InfoFlow KV: InfoFlow KV uses attention-norm for information flow; CEGR uses compression error — orthogonal signals. (3) Chunk-aware PCA calibration — calibrating on independent chunk KVs to match inference-time distribution, a supporting technique that further improves the PCA basis quality for the chunk-caching setting. **Evaluation:** Primary model: Llama-3.1-8B-Instruct; secondary: Qwen2.5-7B-Instruct. RAG benchmarks: NaturalQuestions, HotpotQA, MuSiQue. Long-context: LongBench, RULER. General quality: WikiText perplexity, C4 perplexity, MT-Bench. Capability: MMLU, HumanEval. Key ablation axes: (a) compression ratio (4x, 8x, 16x via KVTC bit budget), (b) RABA vs. standard KVTC bit allocation (matched total bits), (c) CEGR vs. ProphetKV-only vs. CacheBlend-only restoration (matched recomputation budget), (d) RABA+CEGR joint vs. each alone, (e) chunk-aware vs. full-sequence PCA calibration, (f) pure quantization baselines (RateQuant with reverse waterfilling, INT4/FP4 without PCA), (g) recomputation ratio (3%, 10%, 20%), (h) chunk size (256, 512, 1024 tokens). Baselines: (i) uncompressed MEPIC, (ii) naive MEPIC+KVTC (independent stages, full-sequence PCA), (iii) MEPIC+RateQuant (principled pure quantization without PCA), (iv) MEPIC+KVTC with chunk-aware calibration but no RABA/CEGR. Targets: 8-16x storage reduction with <2% quality degradation vs. uncompressed MEPIC at 20% recomputation budget. Wall-clock throughput measured on H100.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~160h H100-80GB (PCA calibration + chunk-aware recalibration: ~4h; RABA implementation and DP modification: ~3h compute, ~1 day engineering; CEGR implementation and joint scoring: ~2h compute, ~1 day engineering; MEPIC baselines across all benchmarks: ~20h; RABA+CEGR pipeline across configs: ~45h; RateQuant pure quantization baseline: ~12h; RABA vs standard allocation ablation: ~15h; CEGR vs ProphetKV-only ablation: ~15h; joint optimization loop calibration: ~8h; additional benchmarks: ~18h; chunk size ablation: ~18h)\",\n      \"gpu_utilization\": \"~40-50% effective utilization; GPU idles during RABA DP modification, CEGR integration with ProphetKV scoring, and joint calibration loop engineering\",\n      \"timeline\": \"16 days (days 1-3: implement KVTC compression pipeline from paper description — PCA + adaptive DP quantization + DEFLATE via nvCOMP; integrate as LMCache storage hooks; days 4-5: implement chunk-aware PCA calibration, validate reconstruction error improvement; days 6-8: implement RABA — modify KVTC's DP to incorporate restoration probability weights, calibrate p_r(t) from MEPIC boundary positions; days 9-11: implement CEGR — analytical compression error estimation from bit allocation metadata, joint scoring with query relevance probe; days 12-13: joint optimization loop — run CEGR on calibration queries, feed restoration frequencies back to RABA; days 14-15: full evaluation + ablations; day 16: paper writing)\",\n      \"team\": \"1 researcher with systems/ML experience\",\n      \"estimated_gpu_cost\": \"$480 (160h × ~$3.00/hr H100-80GB)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~180h H100-80GB (agent handles benchmark scripting and ablation grids; human focuses on RABA DP formulation and CEGR scoring design)\",\n      \"gpu_utilization\": \"~60-70% effective utilization; agent runs experiments continuously while human reviews algorithm correctness and theoretical analysis\",\n      \"timeline\": \"12-16 days (days 1-3: human designs RABA DP modification and CEGR joint scoring; agent scaffolds KVTC compression from paper description + LMCache hooks; days 4-6: agent implements chunk-aware calibration + RABA; human validates DP correctness; days 7-9: agent implements CEGR + joint optimization loop; human reviews scoring function design; days 10-13: agent runs full evaluation grid; human analyzes results; days 14-16: paper writing with agent assistance)\",\n      \"team\": \"1 researcher, ~2h/day for algorithm design decisions and theoretical analysis\",\n      \"claude_api_cost\": \"$100-180 (~1000-1800 Opus turns for code integration, experiment scripting, and result analysis)\",\n      \"estimated_gpu_cost\": \"$540 (180h × ~$3.00/hr H100-80GB)\",\n      \"risk_note\": \"KVTC is implemented from the ICLR paper description (PCA + DP-based adaptive quantization + DEFLATE) rather than relying on the third-party OnlyTerp/kvtc repo (which achieves only 6-9x vs. paper's 20x). PCA and DP are standard algorithms; nvCOMP provides GPU-accelerated DEFLATE. The RABA DP modification is a straightforward extension (adding position-dependent weights to the MSE objective). CEGR's analytical error estimation is computable from stored bit allocation metadata. ProphetKV's query-guided token selection requires implementing its dual-stage attention scoring, which may add ~2 days engineering.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~300h H100-80GB (exhaustive grid over compression ratios × RABA vs standard × CEGR vs ProphetKV × joint vs individual × RateQuant baselines × two models × chunk sizes × recomputation ratios; near-zero idle)\",\n      \"gpu_utilization\": \"~85-90% effective utilization; agent pipelines experiments continuously\",\n      \"timeline\": \"8-12 days with 2 H100 GPUs (single GPU: 14-16 days)\",\n      \"team\": \"0 (initial setup: ~4h to implement KVTC pipeline from paper, integrate RABA DP modification, and set up CEGR scoring)\",\n      \"claude_api_cost\": \"$180-350 (~1800-3500 Opus turns for implementation, debugging, and experiment orchestration)\",\n      \"estimated_gpu_cost\": \"$900 (300h × ~$3.00/hr H100-80GB)\",\n      \"speed_bottleneck\": \"Implementing KVTC from the paper description (PCA decorrelation + DP bit allocation + nvCOMP entropy coding) and integrating RABA's restoration-weighted DP — agent can handle the standard components but may need human guidance on the DP cost function modification for restoration weights\",\n      \"risk_note\": \"RABA's DP modification is algorithmically straightforward (adding multiplicative weights to the MSE terms), and CEGR's analytical error estimation is a closed-form computation. The joint calibration loop (running CEGR on calibration queries to estimate per-position restoration frequencies for RABA) adds ~1 day of engineering but is conceptually simple. Fallback: if joint optimization is infeasible in the timeline, RABA and CEGR independently are each sufficient algorithmic contributions.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"MEPIC: Memory Efficient Position Independent Caching for LLM Serving (arXiv:2512.16822, Dec 2025)\",\n    \"EPIC: Efficient Position-Independent Caching for Serving Large Language Models (ICML 2025)\",\n    \"ProphetKV: User-Query-Driven Selective Recomputation for Efficient KV Cache Reuse in RAG (arXiv:2602.02579, Feb 2026)\",\n    \"KV Cache Transform Coding for Compact Storage in LLM Inference (KVTC, ICLR 2026)\",\n    \"KV Packet: Recomputation-Free Context-Independent KV Caching for LLMs (arXiv:2604.13226, April 2026)\",\n    \"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory (arXiv:2605.06675, May 2026)\",\n    \"eOptShrinkQ: Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization (arXiv:2605.02905, May 2026)\",\n    \"HeadQ: Model-Visible Distortion and Score-Space Correction for KV-Cache Quantization (arXiv:2605.03562, May 2026)\",\n    \"Quantization Dominates Rank Reduction for KV-Cache Compression (arXiv:2604.11501, Apr 2026)\",\n    \"InfoFlow KV: Information-Flow-Aware KV Recomputation for Long Context (arXiv:2603.05353, March 2026)\",\n    \"DynaKV: One Size Does Not Fit All — Token-Wise Adaptive Compression for KV Cache (arXiv:2603.04411, March 2026)\",\n    \"KVLink: Accelerating Large Language Models via Efficient KV Cache Reuse (NeurIPS 2025)\",\n    \"CacheGen: KV Cache Compression and Streaming for Fast Large Language Model Serving (SIGCOMM 2024)\",\n    \"Cache-Craft: Managing Chunk-Caches for Efficient Retrieval-Augmented Generation (SIGMOD 2025)\",\n    \"CacheBlend: Fast Large Language Model Serving for RAG with Cached Knowledge Fusion (EuroSys 2025)\",\n    \"KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction (NeurIPS 2025 Oral)\",\n    \"CacheSlide: Unlocking Cross Position-Aware KV Cache Reuse for Accelerating LLM Serving (FAST 2026)\",\n    \"From Prefix Cache to Fusion RAG Cache: Accelerating LLM Inference in Retrieval-Augmented Generation (FusionRAG, PACMMOD/SIGMOD 2026)\",\n    \"An Experimental Study of KV Cache Reuse Strategies in Chunk-Level Caching Systems (arXiv:2603.20218, March 2026)\",\n    \"TurboRAG: Accelerating Retrieval-Augmented Generation with Precomputed KV Caches for Chunked Text (EMNLP 2025)\",\n    \"Joint Encoding of KV-Cache Blocks for Scalable LLM Serving (arXiv, Jan 2026)\",\n    \"LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference (arXiv:2510.09665)\"\n  ],\n  \"description\": \"We propose CompressLink, a framework that co-optimizes KV compression and quality restoration for position-independent chunk caching in RAG serving. MEPIC (arXiv 2512.16822) stores chunk KVs in NoPE format for position-independent reuse and identifies compression as an orthogonal direction; KVTC (ICLR 2026) achieves 8-20x compression via PCA + adaptive quantization + entropy coding, also operating on NoPE KVs. While KV Packet (arXiv:2604.13226, Section 4.4) demonstrates that adapter-based PIC is compatible with eviction-based compression at 10-50% retention rates, no work jointly optimizes the compression-restoration interface — compression and restoration are universally treated as independent stages. We make three contributions: (1) Restoration-Aware Bit Allocation (RABA) — a novel algorithm that extends rate-distortion-optimal quantization with position-dependent restoration weights. RABA modifies KVTC's DP-based bit allocation so that tokens with high restoration probability (boundary tokens always recomputed by MEPIC, or frequently-restored tokens identified via calibration) receive fewer bits, and the saved budget is reallocated to persistent tokens. At 20% recomputation ratio, this concentrates the full bit budget on the 80% of tokens that must survive compression, reducing effective MSE on persistent tokens. Differentiated from RateQuant (arXiv:2605.06675), which allocates bits across heads but is restoration-unaware, and from DynaKV (arXiv:2603.04411), which allocates per-token PCA rank via learned gating requiring fine-tuning. (2) Compression-Error-Guided Restoration (CEGR) — a novel algorithm that augments query-relevance-based token selection with an analytically-derived compression error signal. Per-token compression error is estimated from decompression metadata (quantization step sizes and PCA basis), requiring zero additional forward passes. CEGR combines this with a query relevance probe via multiplicative joint scoring: score(t) = r_q(t) * error_c(t)^β. The key insight: recomputation budget should prioritize tokens that are both query-relevant AND high-compression-error; a query-relevant token with low error needs no recomputation, and a high-error token irrelevant to the query wastes budget. Differentiated from ProphetKV (query-only selection), CacheBlend (requires forward passes for deviation), and InfoFlow KV (attention-norm flow, compression-unaware). (3) A joint optimization loop where RABA and CEGR share a restoration probability model — CEGR's empirical restoration frequencies on calibration queries feed back to RABA's bit allocation weights, creating a consistent compression-restoration contract. Additionally, chunk-aware PCA calibration addresses the distribution mismatch between full-sequence and independently-encoded chunk KVs (a supporting technique, not a main contribution). Evaluated on Llama-3.1-8B-Instruct and Qwen2.5-7B-Instruct across NaturalQuestions, HotpotQA, MuSiQue, LongBench, RULER, WikiText perplexity, C4 perplexity, MT-Bench, MMLU, and HumanEval. Key baselines: uncompressed MEPIC, naive MEPIC+KVTC, MEPIC+RateQuant (principled pure quantization), and MEPIC+KVTC with chunk-aware calibration but without RABA/CEGR. KVTC is implemented from the ICLR paper description (PCA + DP quantization + nvCOMP DEFLATE) rather than third-party repos. Targets 8-16x storage reduction with <2% quality degradation vs. uncompressed MEPIC at 20% recomputation budget, with wall-clock throughput on H100.\",\n  \"project_name\": \"distill_kv_rag_cache\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 4)\nIssues: [\"MISSING REFERENCE — EVICPRESS (arXiv:2512.14946, Dec 2025, Microsoft Research): Jointly optimizes KV cache compression and eviction decisions via a unified utility function. While it operates at the system/storage-tier level (not bit-allocation level) and treats compression as a coarse per-cache decision, its framing as 'joint compression optimization' directly overlaps with CompressLink's positioning. It also applies 'conservative compression to contexts sensitive to compression errors,' which is a form of restoration-aware compression. MUST be cited and differentiated: EVICPRESS jointly decides *whether* to compress and *where* to place caches; CompressLink jointly decides *how many bits per token* during compression and *which tokens* to restore — algorithmic-level vs. system-level joint optimization.\", \"MISSING REFERENCE — QCFuse (arXiv:2604.08585, April 2026): Query-centric cache fusion for RAG that selectively recomputes query-related tokens using semantic summary anchors and attention distributions from the most critical transformer layer. Achieves 40% latency reduction over existing cache fusion baselines. This is a direct competitor for the restoration/recomputation side of CompressLink (alongside ProphetKV and InfoFlow KV) and should be included as a baseline or cited comparison. QCFuse explicitly criticizes ProphetKV's pipeline synchronization issues — relevant since CompressLink builds on ProphetKV-style scoring.\", \"MISSING REFERENCE — CacheFlow (arXiv:2604.25080, April 2026): Rethinks cache restoration as a 3D-parallel execution problem (tokens × layers × GPUs) with a batch-aware scheduler. Complementary to CompressLink (execution optimization vs. selection optimization) but should be cited as it addresses restoration scheduling, and CompressLink's restored tokens would benefit from CacheFlow's parallel execution.\", \"HeadQ CHALLENGE TO CEGR'S ERROR METRIC: HeadQ (arXiv:2605.03562, May 2026) demonstrates that Fisher/score-space error predicts attention KL 'far better than raw key MSE.' CEGR's compression error estimate (sum of Δ_j²/12 over PCA components) operates in storage/embedding space, not model-visible score space. This means CEGR's error ranking may be poorly calibrated — a token with high embedding-space MSE may have low attention-level impact (e.g., if the error falls in the query-null-space). The idea should either: (a) argue why relative ranking in embedding space is sufficient for the token selection task (even if absolute error is miscalibrated), or (b) propose using HeadQ-style score-space error as an enhanced variant of CEGR, or (c) include an ablation comparing embedding-space vs. score-space error for CEGR's signal.\", \"TIMELINE UNREALISM — MEPIC REIMPLEMENTATION: The timeline allocates zero days for MEPIC reimplementation despite MEPIC having no public code. While NoPE storage is conceptually simple (store keys before RoPE), the fused RoPE attention kernel and block-level recomputation logic are non-trivial. A functionally-correct but non-optimized implementation (apply RoPE to queries only, use standard attention) would take ~2 days. This must be budgeted, likely by compressing the evaluation grid or accepting that some ablation axes run post-submission as supplementary.\", \"KVTC IMPLEMENTATION GAP ACKNOWLEDGED BUT UNDERESTIMATED: The idea correctly notes the OnlyTerp/kvtc repo achieves only 6-9x vs. the paper's 20x. Reimplementing the full pipeline to match paper performance (especially the DP-based adaptive quantization at aggressive compression ratios with nvCOMP DEFLATE instead of CPU zlib) is a significant engineering effort. The risk note mentions this but the timeline (days 1-3) seems optimistic for achieving paper-level compression ratios from scratch.\"]\nFeedback: The idea has improved dramatically across rounds — it now proposes genuine METHOD contributions (RABA, CEGR) that address the Round 3 criticism, all references are verified as accurate, the landscape is thorough, and the gap is confirmed as real. You are close to passing. Here is what remains:\n\n1. **Add 3 missing references (must fix, low effort):** Cite EVICPRESS, QCFuse, and CacheFlow. EVICPRESS is the most important — differentiate by scope (system-level placement vs. algorithmic bit allocation). QCFuse goes in the restoration baselines alongside ProphetKV. CacheFlow is complementary.\n\n2. **Address HeadQ's challenge to CEGR (must fix, medium effort):** HeadQ shows storage-space MSE is a poor proxy for model-visible distortion. Your strongest defense: CEGR uses error for *relative ranking* of tokens within a chunk, not absolute error estimation. If MSE is monotonically related to score-space error within a head (plausible for moderate compression), rankings are preserved even if magnitudes are wrong. State this argument explicitly and include a score-space vs. embedding-space ablation in the evaluation plan.\n\n3. **Fix timeline realism (must fix):** Budget 2 days for MEPIC NoPE reimplementation (functional, not optimized). Compress evaluation: run full benchmarks on Llama-3.1-8B only; run Qwen2.5-7B on a subset (perplexity + 2 RAG benchmarks). Extend paper writing to 2-3 days by overlapping with late evaluation runs. Revised timeline: days 1-2 MEPIC NoPE + KVTC pipeline, days 3-4 chunk-aware PCA, days 5-7 RABA, days 8-10 CEGR, days 11-12 joint loop, days 13-15 evaluation (Llama full + Qwen subset), days 14-16 paper writing (overlapped).\n\n4. **Acknowledge KVTC implementation risk explicitly:** State that if paper-level 20x compression is not achievable in the timeline, you will evaluate at 4-8x (which the OnlyTerp code can achieve) and note higher ratios as future work. This is honest and reviewers will respect it.\n\nWith these fixes, the average score should reach 4.0. The core idea is strong — the joint optimization insight is verified as novel and the algorithms are well-designed.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 4 轮修订，近 3 轮的平均分从 3.5 到 3.8，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-12T00:03:29.737Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T00:03:29.737Z",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c"
}
```

---

## Round 1

50 recorded events

### User

_source line 3 · 2026-05-12T00:03:29.792Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-11 (UTC).**

## Original idea
{
  "title": "CompressLink: Co-Optimizing Compression and Restoration for Position-Independent KV Cache Serving",
  "core_problem": "Production RAG systems redundantly reprocess ~75% of retrieved chunks across queries (Cache-Craft, SIGMOD 2025). Position-independent caching (PIC) avoids this recomputation by storing chunk KVs without positional encodings for arbitrary-position reuse, and MEPIC (arXiv 2512.16822) further reduces HBM usage by 2x over EPIC via RoPE fusion and NoPE storage — yet cached KV states remain at full precision. A single Llama-3.1-8B instance caching 100K chunks at 512 tokens each requires ~3.2TB of KV storage. Meanwhile, KV compression methods like KVTC (ICLR 2026) achieve 8-20x storage reduction via PCA decorrelation + adaptive quantization + entropy coding. MEPIC explicitly identifies KV compression as an orthogonal direction 'that can be seamlessly combined with existing KV compression methods,' and KV Packet (arXiv:2604.13226) demonstrates compatibility of adapter-based PIC with eviction-based compression — but both treat compression and restoration as independent stages. This independence is suboptimal: compression degrades all tokens uniformly regardless of whether they will be restored, and restoration selects tokens based on query relevance or positional heuristics without accounting for which tokens suffered most from compression. No prior work jointly optimizes the compression-restoration pipeline for chunk KV caching.",
  "opportunity": "MEPIC and KVTC share a structural element: both store KV without RoPE (NoPE format). MEPIC stores NoPE KVs for position-independent reuse with RoPE applied on-the-fly; KVTC removes RoPE before PCA compression. This alignment enables natural composition — KVTC compression applied to MEPIC's NoPE KV stores, with decompressed KVs fed into MEPIC's RoPE-fusion attention path. However, naive composition treats compression and restoration as independent stages, wasting compression bits on tokens that will be restored anyway and missing restoration opportunities on tokens with high compression error. We identify a bidirectional optimization opportunity: (1) At compression time, tokens in restorable positions (boundary tokens always recomputed by MEPIC, or tokens frequently selected by query-driven methods) can tolerate aggressive compression since they will be replaced with fresh KVs — reallocating their bits to persistent tokens improves overall quality. (2) At restoration time, per-token compression error (analytically computable from PCA residuals and quantization step sizes at decompression, requiring zero additional forward passes) provides an orthogonal signal to query relevance for selecting which tokens to recompute — prioritizing tokens that are both query-relevant AND high-compression-error yields better quality per recomputed token. Additionally, KVTC's PCA basis calibrated on full-sequence KVs is suboptimal for independently-encoded chunks due to distribution mismatch (local vs. global attention sinks, absent cross-chunk attention), motivating chunk-aware recalibration. KV Packet (arXiv:2604.13226, Section 4.4) demonstrates that adapter-based PIC is robust to eviction-based compression (CUR, KVzap, LeverageScore, TOVA) at 10-50% retention rates — but this tests token-pruning compression, not transform coding (PCA + quantization + entropy coding) at 8-20x rates, and does not optimize the compression-restoration interface. Our approach is the first to jointly optimize this interface.",
  "landscape": "Position-independent KV caching: MEPIC (arXiv 2512.16822, Dec 2025) achieves 2x HBM reduction over EPIC via NoPE KV storage, block-level recomputation (first block per chunk is request-specific), and RoPE fusion in fused attention kernels; integrated into vLLM + LMCache serving stack; evaluated on Mistral-7B-Instruct-v0.3 across SQuAD, NewsQA, NarrativeQA, emrQA. EPIC (ICML 2025) recomputes k≤32 boundary tokens via LegoLink. ProphetKV (arXiv:2602.02579, Feb 2026) introduces user-query-driven selective recomputation, achieving 96-101% accuracy at 20% recomputation ratio; evaluated on Llama-3.1-8B, Qwen2.5-14B, Qwen-3-14B (per the paper's evaluation tables). InfoFlow KV (arXiv:2603.05353, March 2026) casts selective recomputation as an information flow problem using prompt-conditioned attention norms under inference-consistent RoPE geometry; does not consider compression. KVLink (NeurIPS 2025) adjusts RoPE positions with trainable link tokens. Cache-Craft (SIGMOD 2025) stores chunk KVs without RoPE. CacheSlide (FAST 2026) uses learned weights for cross-position-aware reuse. CacheBlend (EuroSys 2025) selectively recomputes tokens based on output deviation. KV Packet (arXiv:2604.13226, April 2026) uses trainable soft-token adapters for recomputation-free PIC; Section 4.4 tests compatibility with 5 eviction-based compression methods (CUR, KVzap, LeverageScore, TOVA, random pruning) at 10-50% retention, claiming PIC 'natively bypasses bottlenecks' of compression-impaired recomputation — but tests token eviction, not transform coding, and does not optimize the compression-restoration interface. FusionRAG (PACMMOD/SIGMOD 2026) embeds cross-chunk information offline. A systematic CLC study (arXiv 2603.20218, March 2026) compared 11 chunk-level caching strategies but did not examine compression. KV compression: KVTC (ICLR 2026) achieves 8-20x compression via PCA decorrelation + adaptive quantization + entropy coding, removing RoPE before PCA; maintains <1pp accuracy drop at 20x on most tasks; bit allocation via DP minimizes reconstruction MSE. RateQuant (arXiv:2605.06675, May 2026) applies rate-distortion theory for mixed-precision per-head quantization via reverse waterfilling, reducing KIVI's perplexity from 49.3 to 14.9 on Qwen3-8B at 2.5 bits with 1.6s calibration; principled bit allocation without PCA. eOptShrinkQ (arXiv:2605.02905, May 2026) achieves near-lossless compression via optimal spectral denoising + quantization, saving ~1 bit/entry. HeadQ (arXiv:2605.03562, May 2026) measures distortion in model-visible score space rather than storage space, achieving 94% excess perplexity removal at 2 bits. DynaKV (arXiv:2603.04411, March 2026) provides per-token adaptive PCA rank via learned gating — requires fine-tuning (128M tokens), operates on full-sequence KVs. 'Quantization Dominates Rank Reduction' (arXiv:2604.11501, April 2026) shows quantization outperforms dimension-discarding PCA projection but tests rank reduction, not decorrelation-before-quantization as KVTC uses. CacheGen (SIGCOMM 2024) achieves 3.5-4.3x via tensor encoders. KVzip (NeurIPS 2025 Oral) provides 3-4x eviction-based compression. Joint Encoding of KV-Cache Blocks (Jan 2026) fuses similar blocks achieving 4.38x. No prior work jointly optimizes KV compression bit allocation with selective restoration token selection in the chunk-caching setting — compression and restoration are universally treated as independent stages.",
  "approach": "We propose CompressLink, a framework that co-optimizes KV compression and quality restoration for position-independent chunk caching, built on the shared NoPE representation of MEPIC and KVTC. CompressLink introduces two novel algorithms — Restoration-Aware Bit Allocation (RABA) and Compression-Error-Guided Restoration (CEGR) — that jointly optimize the compression-restoration pipeline, plus chunk-aware PCA calibration as a supporting technique. **Offline Compression Pipeline:** Each document chunk is independently encoded through the LLM; MEPIC stores the resulting KV caches in NoPE format. Before KVTC compression, PCA bases are calibrated on independently-encoded chunk KVs (matching inference-time distribution, addressing the calibration mismatch from full-sequence KVs). RABA then modifies KVTC's DP-based bit allocation: each token position is assigned a restoration probability p_r(t) based on positional priors — boundary tokens (first block per chunk, always recomputed by MEPIC) get p_r ≈ 1.0; tokens frequently selected across calibration queries by ProphetKV-style scoring get intermediate p_r; remaining tokens get p_r ≈ 0. The DP objective is modified from minimizing total reconstruction MSE to minimizing restoration-weighted MSE: sum over tokens t of (1 - p_r(t)) * MSE(t), so that bits are reallocated from high-restoration-probability tokens (whose compressed values will be overwritten) to persistent tokens (whose compressed values must survive). At 20% recomputation ratio, this effectively concentrates the full bit budget on 80% of tokens, improving quality where it matters. Compressed KVs (PCA transform → RABA-allocated quantization → entropy coding) are stored in LMCache's persistence layer. **Online Restoration Pipeline:** Retrieved chunks' compressed KVs are decompressed (entropy decode → dequantize → PCA inverse). CEGR computes per-token compression error estimates analytically from decompression: for each token, error_c(t) = sum over PCA components j of (Δ_j² / 12) where Δ_j is the quantization step size for component j at the allocated bit width — this requires zero additional forward passes, only the bit allocation metadata stored alongside compressed KVs. CEGR then combines this with a query relevance signal r_q(t) obtained from a lightweight attention probe (single-layer attention of the query against decompressed keys, following ProphetKV's first-pass scoring). The joint restoration score is: score(t) = r_q(t) * error_c(t)^β, where β controls the compression-error sensitivity. Tokens with highest joint scores are selected for recomputation within the budget. The key insight: a query-relevant token with low compression error needs no recomputation (compression preserved it); a high-error token irrelevant to the query wastes recomputation budget. Only tokens that are both query-relevant AND high-error benefit maximally from recomputation. MEPIC's fused RoPE-attention kernel applies positional encodings on-the-fly during final attention computation over the mix of recomputed and decompressed KVs. **Joint Optimization Loop:** RABA and CEGR share the restoration probability model — RABA's p_r(t) at compression time is calibrated to match CEGR's empirical restoration rate at inference time. During calibration, we run CEGR on calibration queries to estimate per-position restoration frequencies, then feed these back into RABA's DP allocation. This creates a consistent compression-restoration contract: positions that CEGR frequently restores are precisely those where RABA saves bits. **Contributions:** (1) RABA — a novel restoration-aware bit allocation algorithm that extends rate-distortion-optimal quantization (cf. RateQuant's reverse waterfilling, KVTC's DP) with position-dependent restoration weights, provably reducing effective MSE on persistent tokens at matched total bit budgets. Differentiation from RateQuant: RateQuant allocates across heads, RABA allocates across token positions within each head; RateQuant is restoration-unaware. Differentiation from DynaKV: DynaKV allocates per-token PCA rank via learned gating (requires fine-tuning), RABA allocates per-token bit budget via restoration probability (training-free, calibration only). (2) CEGR — a novel compression-error-guided restoration algorithm that augments query-relevance-based token selection with an analytically-derived compression error signal, available at zero additional compute cost from decompression metadata. Differentiation from ProphetKV: ProphetKV selects on query relevance alone; CEGR adds the compression error dimension. Differentiation from CacheBlend: CacheBlend uses output deviation (requires early-layer forward passes); CEGR uses analytical error estimates (zero forward passes). Differentiation from InfoFlow KV: InfoFlow KV uses attention-norm for information flow; CEGR uses compression error — orthogonal signals. (3) Chunk-aware PCA calibration — calibrating on independent chunk KVs to match inference-time distribution, a supporting technique that further improves the PCA basis quality for the chunk-caching setting. **Evaluation:** Primary model: Llama-3.1-8B-Instruct; secondary: Qwen2.5-7B-Instruct. RAG benchmarks: NaturalQuestions, HotpotQA, MuSiQue. Long-context: LongBench, RULER. General quality: WikiText perplexity, C4 perplexity, MT-Bench. Capability: MMLU, HumanEval. Key ablation axes: (a) compression ratio (4x, 8x, 16x via KVTC bit budget), (b) RABA vs. standard KVTC bit allocation (matched total bits), (c) CEGR vs. ProphetKV-only vs. CacheBlend-only restoration (matched recomputation budget), (d) RABA+CEGR joint vs. each alone, (e) chunk-aware vs. full-sequence PCA calibration, (f) pure quantization baselines (RateQuant with reverse waterfilling, INT4/FP4 without PCA), (g) recomputation ratio (3%, 10%, 20%), (h) chunk size (256, 512, 1024 tokens). Baselines: (i) uncompressed MEPIC, (ii) naive MEPIC+KVTC (independent stages, full-sequence PCA), (iii) MEPIC+RateQuant (principled pure quantization without PCA), (iv) MEPIC+KVTC with chunk-aware calibration but no RABA/CEGR. Targets: 8-16x storage reduction with <2% quality degradation vs. uncompressed MEPIC at 20% recomputation budget. Wall-clock throughput measured on H100.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~160h H100-80GB (PCA calibration + chunk-aware recalibration: ~4h; RABA implementation and DP modification: ~3h compute, ~1 day engineering; CEGR implementation and joint scoring: ~2h compute, ~1 day engineering; MEPIC baselines across all benchmarks: ~20h; RABA+CEGR pipeline across configs: ~45h; RateQuant pure quantization baseline: ~12h; RABA vs standard allocation ablation: ~15h; CEGR vs ProphetKV-only ablation: ~15h; joint optimization loop calibration: ~8h; additional benchmarks: ~18h; chunk size ablation: ~18h)",
      "gpu_utilization": "~40-50% effective utilization; GPU idles during RABA DP modification, CEGR integration with ProphetKV scoring, and joint calibration loop engineering",
      "timeline": "16 days (days 1-3: implement KVTC compression pipeline from paper description — PCA + adaptive DP quantization + DEFLATE via nvCOMP; integrate as LMCache storage hooks; days 4-5: implement chunk-aware PCA calibration, validate reconstruction error improvement; days 6-8: implement RABA — modify KVTC's DP to incorporate restoration probability weights, calibrate p_r(t) from MEPIC boundary positions; days 9-11: implement CEGR — analytical compression error estimation from bit allocation metadata, joint scoring with query relevance probe; days 12-13: joint optimization loop — run CEGR on calibration queries, feed restoration frequencies back to RABA; days 14-15: full evaluation + ablations; day 16: paper writing)",
      "team": "1 researcher with systems/ML experience",
      "estimated_gpu_cost": "$480 (160h × ~$3.00/hr H100-80GB)"
    },
    "human_in_loop": {
      "gpu_hours": "~180h H100-80GB (agent handles benchmark scripting and ablation grids; human focuses on RABA DP formulation and CEGR scoring design)",
      "gpu_utilization": "~60-70% effective utilization; agent runs experiments continuously while human reviews algorithm correctness and theoretical analysis",
      "timeline": "12-16 days (days 1-3: human designs RABA DP modification and CEGR joint scoring; agent scaffolds KVTC compression from paper description + LMCache hooks; days 4-6: agent implements chunk-aware calibration + RABA; human validates DP correctness; days 7-9: agent implements CEGR + joint optimization loop; human reviews scoring function design; days 10-13: agent runs full evaluation grid; human analyzes results; days 14-16: paper writing with agent assistance)",
      "team": "1 researcher, ~2h/day for algorithm design decisions and theoretical analysis",
      "claude_api_cost": "$100-180 (~1000-1800 Opus turns for code integration, experiment scripting, and result analysis)",
      "estimated_gpu_cost": "$540 (180h × ~$3.00/hr H100-80GB)",
      "risk_note": "KVTC is implemented from the ICLR paper description (PCA + DP-based adaptive quantization + DEFLATE) rather than relying on the third-party OnlyTerp/kvtc repo (which achieves only 6-9x vs. paper's 20x). PCA and DP are standard algorithms; nvCOMP provides GPU-accelerated DEFLATE. The RABA DP modification is a straightforward extension (adding position-dependent weights to the MSE objective). CEGR's analytical error estimation is computable from stored bit allocation metadata. ProphetKV's query-guided token selection requires implementing its dual-stage attention scoring, which may add ~2 days engineering."
    },
    "auto_research": {
      "gpu_hours": "~300h H100-80GB (exhaustive grid over compression ratios × RABA vs standard × CEGR vs ProphetKV × joint vs individual × RateQuant baselines × two models × chunk sizes × recomputation ratios; near-zero idle)",
      "gpu_utilization": "~85-90% effective utilization; agent pipelines experiments continuously",
      "timeline": "8-12 days with 2 H100 GPUs (single GPU: 14-16 days)",
      "team": "0 (initial setup: ~4h to implement KVTC pipeline from paper, integrate RABA DP modification, and set up CEGR scoring)",
      "claude_api_cost": "$180-350 (~1800-3500 Opus turns for implementation, debugging, and experiment orchestration)",
      "estimated_gpu_cost": "$900 (300h × ~$3.00/hr H100-80GB)",
      "speed_bottleneck": "Implementing KVTC from the paper description (PCA decorrelation + DP bit allocation + nvCOMP entropy coding) and integrating RABA's restoration-weighted DP — agent can handle the standard components but may need human guidance on the DP cost function modification for restoration weights",
      "risk_note": "RABA's DP modification is algorithmically straightforward (adding multiplicative weights to the MSE terms), and CEGR's analytical error estimation is a closed-form computation. The joint calibration loop (running CEGR on calibration queries to estimate per-position restoration frequencies for RABA) adds ~1 day of engineering but is conceptually simple. Fallback: if joint optimization is infeasible in the timeline, RABA and CEGR independently are each sufficient algorithmic contributions."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026)"
  ],
  "level": "solid",
  "key_references": [
    "MEPIC: Memory Efficient Position Independent Caching for LLM Serving (arXiv:2512.16822, Dec 2025)",
    "EPIC: Efficient Position-Independent Caching for Serving Large Language Models (ICML 2025)",
    "ProphetKV: User-Query-Driven Selective Recomputation for Efficient KV Cache Reuse in RAG (arXiv:2602.02579, Feb 2026)",
    "KV Cache Transform Coding for Compact Storage in LLM Inference (KVTC, ICLR 2026)",
    "KV Packet: Recomputation-Free Context-Independent KV Caching for LLMs (arXiv:2604.13226, April 2026)",
    "RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory (arXiv:2605.06675, May 2026)",
    "eOptShrinkQ: Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization (arXiv:2605.02905, May 2026)",
    "HeadQ: Model-Visible Distortion and Score-Space Correction for KV-Cache Quantization (arXiv:2605.03562, May 2026)",
    "Quantization Dominates Rank Reduction for KV-Cache Compression (arXiv:2604.11501, Apr 2026)",
    "InfoFlow KV: Information-Flow-Aware KV Recomputation for Long Context (arXiv:2603.05353, March 2026)",
    "DynaKV: One Size Does Not Fit All — Token-Wise Adaptive Compression for KV Cache (arXiv:2603.04411, March 2026)",
    "KVLink: Accelerating Large Language Models via Efficient KV Cache Reuse (NeurIPS 2025)",
    "CacheGen: KV Cache Compression and Streaming for Fast Large Language Model Serving (SIGCOMM 2024)",
    "Cache-Craft: Managing Chunk-Caches for Efficient Retrieval-Augmented Generation (SIGMOD 2025)",
    "CacheBlend: Fast Large Language Model Serving for RAG with Cached Knowledge Fusion (EuroSys 2025)",
    "KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction (NeurIPS 2025 Oral)",
    "CacheSlide: Unlocking Cross Position-Aware KV Cache Reuse for Accelerating LLM Serving (FAST 2026)",
    "From Prefix Cache to Fusion RAG Cache: Accelerating LLM Inference in Retrieval-Augmented Generation (FusionRAG, PACMMOD/SIGMOD 2026)",
    "An Experimental Study of KV Cache Reuse Strategies in Chunk-Level Caching Systems (arXiv:2603.20218, March 2026)",
    "TurboRAG: Accelerating Retrieval-Augmented Generation with Precomputed KV Caches for Chunked Text (EMNLP 2025)",
    "Joint Encoding of KV-Cache Blocks for Scalable LLM Serving (arXiv, Jan 2026)",
    "LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference (arXiv:2510.09665)"
  ],
  "description": "We propose CompressLink, a framework that co-optimizes KV compression and quality restoration for position-independent chunk caching in RAG serving. MEPIC (arXiv 2512.16822) stores chunk KVs in NoPE format for position-independent reuse and identifies compression as an orthogonal direction; KVTC (ICLR 2026) achieves 8-20x compression via PCA + adaptive quantization + entropy coding, also operating on NoPE KVs. While KV Packet (arXiv:2604.13226, Section 4.4) demonstrates that adapter-based PIC is compatible with eviction-based compression at 10-50% retention rates, no work jointly optimizes the compression-restoration interface — compression and restoration are universally treated as independent stages. We make three contributions: (1) Restoration-Aware Bit Allocation (RABA) — a novel algorithm that extends rate-distortion-optimal quantization with position-dependent restoration weights. RABA modifies KVTC's DP-based bit allocation so that tokens with high restoration probability (boundary tokens always recomputed by MEPIC, or frequently-restored tokens identified via calibration) receive fewer bits, and the saved budget is reallocated to persistent tokens. At 20% recomputation ratio, this concentrates the full bit budget on the 80% of tokens that must survive compression, reducing effective MSE on persistent tokens. Differentiated from RateQuant (arXiv:2605.06675), which allocates bits across heads but is restoration-unaware, and from DynaKV (arXiv:2603.04411), which allocates per-token PCA rank via learned gating requiring fine-tuning. (2) Compression-Error-Guided Restoration (CEGR) — a novel algorithm that augments query-relevance-based token selection with an analytically-derived compression error signal. Per-token compression error is estimated from decompression metadata (quantization step sizes and PCA basis), requiring zero additional forward passes. CEGR combines this with a query relevance probe via multiplicative joint scoring: score(t) = r_q(t) * error_c(t)^β. The key insight: recomputation budget should prioritize tokens that are both query-relevant AND high-compression-error; a query-relevant token with low error needs no recomputation, and a high-error token irrelevant to the query wastes budget. Differentiated from ProphetKV (query-only selection), CacheBlend (requires forward passes for deviation), and InfoFlow KV (attention-norm flow, compression-unaware). (3) A joint optimization loop where RABA and CEGR share a restoration probability model — CEGR's empirical restoration frequencies on calibration queries feed back to RABA's bit allocation weights, creating a consistent compression-restoration contract. Additionally, chunk-aware PCA calibration addresses the distribution mismatch between full-sequence and independently-encoded chunk KVs (a supporting technique, not a main contribution). Evaluated on Llama-3.1-8B-Instruct and Qwen2.5-7B-Instruct across NaturalQuestions, HotpotQA, MuSiQue, LongBench, RULER, WikiText perplexity, C4 perplexity, MT-Bench, MMLU, and HumanEval. Key baselines: uncompressed MEPIC, naive MEPIC+KVTC, MEPIC+RateQuant (principled pure quantization), and MEPIC+KVTC with chunk-aware calibration but without RABA/CEGR. KVTC is implemented from the ICLR paper description (PCA + DP quantization + nvCOMP DEFLATE) rather than third-party repos. Targets 8-16x storage reduction with <2% quality degradation vs. uncompressed MEPIC at 20% recomputation budget, with wall-clock throughput on H100.",
  "project_name": "distill_kv_rag_cache",
  "source": "web_research"
}

## Reviewer feedback (round 4)
Issues: ["MISSING REFERENCE — EVICPRESS (arXiv:2512.14946, Dec 2025, Microsoft Research): Jointly optimizes KV cache compression and eviction decisions via a unified utility function. While it operates at the system/storage-tier level (not bit-allocation level) and treats compression as a coarse per-cache decision, its framing as 'joint compression optimization' directly overlaps with CompressLink's positioning. It also applies 'conservative compression to contexts sensitive to compression errors,' which is a form of restoration-aware compression. MUST be cited and differentiated: EVICPRESS jointly decides *whether* to compress and *where* to place caches; CompressLink jointly decides *how many bits per token* during compression and *which tokens* to restore — algorithmic-level vs. system-level joint optimization.", "MISSING REFERENCE — QCFuse (arXiv:2604.08585, April 2026): Query-centric cache fusion for RAG that selectively recomputes query-related tokens using semantic summary anchors and attention distributions from the most critical transformer layer. Achieves 40% latency reduction over existing cache fusion baselines. This is a direct competitor for the restoration/recomputation side of CompressLink (alongside ProphetKV and InfoFlow KV) and should be included as a baseline or cited comparison. QCFuse explicitly criticizes ProphetKV's pipeline synchronization issues — relevant since CompressLink builds on ProphetKV-style scoring.", "MISSING REFERENCE — CacheFlow (arXiv:2604.25080, April 2026): Rethinks cache restoration as a 3D-parallel execution problem (tokens × layers × GPUs) with a batch-aware scheduler. Complementary to CompressLink (execution optimization vs. selection optimization) but should be cited as it addresses restoration scheduling, and CompressLink's restored tokens would benefit from CacheFlow's parallel execution.", "HeadQ CHALLENGE TO CEGR'S ERROR METRIC: HeadQ (arXiv:2605.03562, May 2026) demonstrates that Fisher/score-space error predicts attention KL 'far better than raw key MSE.' CEGR's compression error estimate (sum of Δ_j²/12 over PCA components) operates in storage/embedding space, not model-visible score space. This means CEGR's error ranking may be poorly calibrated — a token with high embedding-space MSE may have low attention-level impact (e.g., if the error falls in the query-null-space). The idea should either: (a) argue why relative ranking in embedding space is sufficient for the token selection task (even if absolute error is miscalibrated), or (b) propose using HeadQ-style score-space error as an enhanced variant of CEGR, or (c) include an ablation comparing embedding-space vs. score-space error for CEGR's signal.", "TIMELINE UNREALISM — MEPIC REIMPLEMENTATION: The timeline allocates zero days for MEPIC reimplementation despite MEPIC having no public code. While NoPE storage is conceptually simple (store keys before RoPE), the fused RoPE attention kernel and block-level recomputation logic are non-trivial. A functionally-correct but non-optimized implementation (apply RoPE to queries only, use standard attention) would take ~2 days. This must be budgeted, likely by compressing the evaluation grid or accepting that some ablation axes run post-submission as supplementary.", "KVTC IMPLEMENTATION GAP ACKNOWLEDGED BUT UNDERESTIMATED: The idea correctly notes the OnlyTerp/kvtc repo achieves only 6-9x vs. the paper's 20x. Reimplementing the full pipeline to match paper performance (especially the DP-based adaptive quantization at aggressive compression ratios with nvCOMP DEFLATE instead of CPU zlib) is a significant engineering effort. The risk note mentions this but the timeline (days 1-3) seems optimistic for achieving paper-level compression ratios from scratch."]
Feedback: The idea has improved dramatically across rounds — it now proposes genuine METHOD contributions (RABA, CEGR) that address the Round 3 criticism, all references are verified as accurate, the landscape is thorough, and the gap is confirmed as real. You are close to passing. Here is what remains:

1. **Add 3 missing references (must fix, low effort):** Cite EVICPRESS, QCFuse, and CacheFlow. EVICPRESS is the most important — differentiate by scope (system-level placement vs. algorithmic bit allocation). QCFuse goes in the restoration baselines alongside ProphetKV. CacheFlow is complementary.

2. **Address HeadQ's challenge to CEGR (must fix, medium effort):** HeadQ shows storage-space MSE is a poor proxy for model-visible distortion. Your strongest defense: CEGR uses error for *relative ranking* of tokens within a chunk, not absolute error estimation. If MSE is monotonically related to score-space error within a head (plausible for moderate compression), rankings are preserved even if magnitudes are wrong. State this argument explicitly and include a score-space vs. embedding-space ablation in the evaluation plan.

3. **Fix timeline realism (must fix):** Budget 2 days for MEPIC NoPE reimplementation (functional, not optimized). Compress evaluation: run full benchmarks on Llama-3.1-8B only; run Qwen2.5-7B on a subset (perplexity + 2 RAG benchmarks). Extend paper writing to 2-3 days by overlapping with late evaluation runs. Revised timeline: days 1-2 MEPIC NoPE + KVTC pipeline, days 3-4 chunk-aware PCA, days 5-7 RABA, days 8-10 CEGR, days 11-12 joint loop, days 13-15 evaluation (Llama full + Qwen subset), days 14-16 paper writing (overlapped).

4. **Acknowledge KVTC implementation risk explicitly:** State that if paper-level 20x compression is not achievable in the timeline, you will evaluate at 4-8x (which the OnlyTerp code can achieve) and note higher ratios as future work. This is honest and reviewers will respect it.

With these fixes, the average score should reach 4.0. The core idea is strong — the joint optimization insight is verified as novel and the algorithms are well-designed.

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
这个 idea 已经经过 4 轮修订，近 3 轮的平均分从 3.5 到 3.8，没有明显改善。

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
  "promptId": "b368710b-e415-41f5-a2d9-b7e249a1c17c",
  "type": "user",
  "uuid": "2fe51a95-205c-4fd9-a2ad-9f4c37a0e685",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T00:03:29.790Z_

```json
{
  "parentUuid": "2fe51a95-205c-4fd9-a2ad-9f4c37a0e685",
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
  "uuid": "372dcc63-fd7d-4b05-95e8-b4c1016f8215",
  "timestamp": "2026-05-12T00:03:29.790Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T00:03:29.790Z_

```json
{
  "parentUuid": "372dcc63-fd7d-4b05-95e8-b4c1016f8215",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b8abd20f-4c65-4ab8-b54f-1835b1eb782d",
  "timestamp": "2026-05-12T00:03:29.790Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"CompressLink: Co-Optimizing Compression and Restoration for Position-I…",
  "leafUuid": "b8abd20f-4c65-4ab8-b54f-1835b1eb782d",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Co-optimize KV compression and restoration for RAG chunk caching",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c"
}
```

---

### Assistant

_source line 8 · 2026-05-12T00:03:38.803Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully before making changes. The feedback indicates this idea is close to passing (score ~3.8, target 4.0) and needs specific fixes:

1. Add 3 missing references (EVICPRESS, QCFuse, CacheFlow)
2. Address HeadQ's challenge to CEGR's error metric
3. Fix timeline realism
4. Acknowledge KVTC implementation risk

The reviewer explicitly says "the core idea is strong" and "you are close to passing." This suggests a minor fix is appropriate, not a major revision or pivot. Let me do the required research first.


Now I'm looking up those three missing references to understand what they contribute to the field and how they relate to my proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8abd20f-4c65-4ab8-b54f-1835b1eb782d",
  "isSidechain": false,
  "requestId": "req_011CawhHbhtRyJ6QRbJdDD1x",
  "type": "assistant",
  "uuid": "cc48506b-0f3d-4faa-87ad-812106e13e74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LRZzdC3JSBfsAdB1Wz3L11",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14907,
      "cache_read_input_tokens": 11841,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14907,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 282,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14907,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14907
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-12T00:03:38.855Z_

I'll research the three missing references and the HeadQ challenge before revising. Let me search for each one.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc48506b-0f3d-4faa-87ad-812106e13e74",
  "isSidechain": false,
  "requestId": "req_011CawhHbhtRyJ6QRbJdDD1x",
  "type": "assistant",
  "uuid": "18bbeefd-3476-4e87-830d-b0d894c34750",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LRZzdC3JSBfsAdB1Wz3L11",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14907,
      "cache_read_input_tokens": 11841,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14907,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 282,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14907,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14907
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-12T00:03:39.312Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015qjX3q3QJE31zS7zw2hYdu`</summary>

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
  "parentUuid": "18bbeefd-3476-4e87-830d-b0d894c34750",
  "isSidechain": false,
  "requestId": "req_011CawhHbhtRyJ6QRbJdDD1x",
  "type": "assistant",
  "uuid": "fb68a662-ea86-4ee0-b0c3-cffe62bd97a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LRZzdC3JSBfsAdB1Wz3L11",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14907,
      "cache_read_input_tokens": 11841,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14907,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 282,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14907,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14907
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-12T00:03:39.318Z_

<details><summary>↩ Tool result · `toolu_015qjX3q3QJE31zS7zw2hYdu`</summary>

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
  "parentUuid": "fb68a662-ea86-4ee0-b0c3-cffe62bd97a1",
  "isSidechain": false,
  "promptId": "b368710b-e415-41f5-a2d9-b7e249a1c17c",
  "type": "user",
  "uuid": "4f83ea7c-9943-441d-ac5d-6c4ce41001c0",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "fb68a662-ea86-4ee0-b0c3-cffe62bd97a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-12T00:03:42.409Z_

<details><summary>Logged reasoning block</summary>

```text
Let me search for all three missing references and HeadQ in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f83ea7c-9943-441d-ac5d-6c4ce41001c0",
  "isSidechain": false,
  "requestId": "req_011CawhJH8DdGMjRysza9nnP",
  "type": "assistant",
  "uuid": "071448e3-3fec-44a9-91f0-2d7f5f5c0767",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A4AixVYwA7XJMYmHXw8Czi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1302,
      "cache_read_input_tokens": 26748,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1302,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 121,
          "cache_read_input_tokens": 26748,
          "cache_creation_input_tokens": 1302,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1302
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-12T00:03:43.020Z_

Let me research all the missing references and the HeadQ challenge in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "071448e3-3fec-44a9-91f0-2d7f5f5c0767",
  "isSidechain": false,
  "requestId": "req_011CawhJH8DdGMjRysza9nnP",
  "type": "assistant",
  "uuid": "067f5e20-85c1-4035-94e6-31e542bb2c08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A4AixVYwA7XJMYmHXw8Czi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1302,
      "cache_read_input_tokens": 26748,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1302,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 121,
          "cache_read_input_tokens": 26748,
          "cache_creation_input_tokens": 1302,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1302
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-12T00:03:43.895Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SUm7t1XwL11CHQCjDcAssh`</summary>

```json
{
  "query": "EVICPRESS arXiv 2512.14946 KV cache compression eviction joint optimization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "067f5e20-85c1-4035-94e6-31e542bb2c08",
  "isSidechain": false,
  "requestId": "req_011CawhJH8DdGMjRysza9nnP",
  "type": "assistant",
  "uuid": "30a7289d-6146-4652-92c8-72f9cd1545a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A4AixVYwA7XJMYmHXw8Czi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1302,
      "cache_read_input_tokens": 26748,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1302,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 121,
          "cache_read_input_tokens": 26748,
          "cache_creation_input_tokens": 1302,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1302
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-12T00:03:50.639Z_

<details><summary>↩ Tool result · `toolu_01SUm7t1XwL11CHQCjDcAssh`</summary>

```text
Web search results for query: "EVICPRESS arXiv 2512.14946 KV cache compression eviction joint optimization"

Links: [{"title":"[2512.14946] EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving","url":"https://arxiv.org/abs/2512.14946"},{"title":"EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving","url":"https://arxiv.org/pdf/2512.14946"},{"title":"EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251214946F/abstract"},{"title":"(PDF) EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving","url":"https://www.researchgate.net/publication/398806282_EVICPRESS_Joint_KV-Cache_Compression_and_Eviction_for_Efficient_LLM_Serving"},{"title":"EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/evicpress-joint-kv-cache-compression-and-eviction-for-efficient-llm-serving/"},{"title":"Hold Onto That Thought: Assessing KV Cache Compression On Reasoning","url":"https://arxiv.org/html/2512.12008v1"},{"title":"[2512.05916] KQ-SVD: Compressing the KV Cache with Provable Guarantees on Attention Fidelity","url":"https://arxiv.org/abs/2512.05916"},{"title":"[2602.10238] Learning to Evict from Key-Value Cache","url":"https://arxiv.org/abs/2602.10238"},{"title":"[2603.20397] KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/abs/2603.20397"},{"title":"RETHINKING KEY-VALUE CACHE COMPRESSION TECHNIQUES FOR LARGE","url":"https://arxiv.org/pdf/2503.24000"}]

Based on the search results, here is information about EVICPRESS (arXiv 2512.14946):

## Overview

EVICPRESS is a KV-cache management system that applies lossy compression and adaptive eviction to KV cache across multiple storage tiers.

## Key Problem and Motivation

Prior work proposed either evicting KV cache to lower-tier storage devices or compressing KV cache so more can fit in fast memory, but missed the opportunity to jointly optimize the eviction and compression decisions across all KV caches to minimize average generation latency without hurting quality.

## Technical Approach

EVICPRESS proposes a unified utility function that quantifies the effect of quality and delay of lossy compression or eviction, with a profiling module that periodically updates utility function scores on all possible eviction-compression configurations and places KV caches using a fast heuristic to rearrange them across storage tiers, maximizing utility function scores on each tier.

## Results

Compared to baselines that evict or compress KV cache separately, EVICPRESS achieves higher KV-cache hit rates on fast devices (lower delay) while preserving high generation quality by applying conservative compression to contexts sensitive to compression errors. Evaluation on 12 datasets and 5 models demonstrates that EVICPRESS achieves up to 2.19x faster time-to-first-token (TTFT) at equivalent generation quality.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30a7289d-6146-4652-92c8-72f9cd1545a8",
  "isSidechain": false,
  "promptId": "b368710b-e415-41f5-a2d9-b7e249a1c17c",
  "type": "user",
  "uuid": "41773bde-063e-4f3a-8424-3bde30ef5a32",
  "toolUseResult": {
    "query": "EVICPRESS arXiv 2512.14946 KV cache compression eviction joint optimization",
    "results": [
      {
        "tool_use_id": "srvtoolu_015k5jpDRBxbGWaszSyYZyZA",
        "content": [
          {
            "title": "[2512.14946] EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving",
            "url": "https://arxiv.org/abs/2512.14946"
          },
          {
            "title": "EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving",
            "url": "https://arxiv.org/pdf/2512.14946"
          },
          {
            "title": "EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv251214946F/abstract"
          },
          {
            "title": "(PDF) EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving",
            "url": "https://www.researchgate.net/publication/398806282_EVICPRESS_Joint_KV-Cache_Compression_and_Eviction_for_Efficient_LLM_Serving"
          },
          {
            "title": "EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving - Microsoft Research",
            "url": "https://www.microsoft.com/en-us/research/publication/evicpress-joint-kv-cache-compression-and-eviction-for-efficient-llm-serving/"
          },
          {
            "title": "Hold Onto That Thought: Assessing KV Cache Compression On Reasoning",
            "url": "https://arxiv.org/html/2512.12008v1"
          },
          {
            "title": "[2512.05916] KQ-SVD: Compressing the KV Cache with Provable Guarantees on Attention Fidelity",
            "url": "https://arxiv.org/abs/2512.05916"
          },
          {
            "title": "[2602.10238] Learning to Evict from Key-Value Cache",
            "url": "https://arxiv.org/abs/2602.10238"
          },
          {
            "title": "[2603.20397] KV Cache Optimization Strategies for Scalable and Efficient LLM Inference",
            "url": "https://arxiv.org/abs/2603.20397"
          },
          {
            "title": "RETHINKING KEY-VALUE CACHE COMPRESSION TECHNIQUES FOR LARGE",
            "url": "https://arxiv.org/pdf/2503.24000"
          }
        ]
      },
      "Based on the search results, here is information about EVICPRESS (arXiv 2512.14946):\n\n## Overview\n\nEVICPRESS is a KV-cache management system that applies lossy compression and adaptive eviction to KV cache across multiple storage tiers.\n\n## Key Problem and Motivation\n\nPrior work proposed either evicting KV cache to lower-tier storage devices or compressing KV cache so more can fit in fast memory, but missed the opportunity to jointly optimize the eviction and compression decisions across all KV caches to minimize average generation latency without hurting quality.\n\n## Technical Approach\n\nEVICPRESS proposes a unified utility function that quantifies the effect of quality and delay of lossy compression or eviction, with a profiling module that periodically updates utility function scores on all possible eviction-compression configurations and places KV caches using a fast heuristic to rearrange them across storage tiers, maximizing utility function scores on each tier.\n\n## Results\n\nCompared to baselines that evict or compress KV cache separately, EVICPRESS achieves higher KV-cache hit rates on fast devices (lower delay) while preserving high generation quality by applying conservative compression to contexts sensitive to compression errors. Evaluation on 12 datasets and 5 models demonstrates that EVICPRESS achieves up to 2.19x faster time-to-first-token (TTFT) at equivalent generation quality."
    ],
    "durationSeconds": 6.737993752
  },
  "sourceToolAssistantUUID": "30a7289d-6146-4652-92c8-72f9cd1545a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-12T00:03:54.941Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018PdrvmhNZYC7HLN2pT3Faq`</summary>

```json
{
  "query": "QCFuse arXiv 2604.08585 query-centric cache fusion RAG recomputation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41773bde-063e-4f3a-8424-3bde30ef5a32",
  "isSidechain": false,
  "requestId": "req_011CawhK7MNnzacqcdBoWjU2",
  "type": "assistant",
  "uuid": "c3a73620-4619-40e1-a714-990985526a8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WjmRhNjwybckszNDyRAF26",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1036,
      "cache_read_input_tokens": 28050,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1036,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 28050,
          "cache_creation_input_tokens": 1036,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1036
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-12T00:04:03.136Z_

<details><summary>↩ Tool result · `toolu_018PdrvmhNZYC7HLN2pT3Faq`</summary>

```text
Web search results for query: "QCFuse arXiv 2604.08585 query-centric cache fusion RAG recomputation"

Links: [{"title":"[2604.08585] QCFuse: Query-Centric Cache Fusion for Efficient RAG Inference","url":"https://arxiv.org/abs/2604.08585"},{"title":"QCFuse: Query-Centric Cache Fusion for Efficient RAG Inference","url":"https://arxiv.org/html/2604.08585"},{"title":"From Prefix Cache to Fusion RAG Cache: Accelerating LLM Inference in Retrieval-Augmented Generation","url":"https://arxiv.org/html/2601.12904v1"},{"title":"𝐴³: Attention-Aware Accurate KV Cache Fusion for Fast Large Language Model Serving","url":"https://arxiv.org/html/2511.17560"},{"title":"[2601.12904] From Prefix Cache to Fusion RAG Cache: Accelerating LLM Inference in Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2601.12904"},{"title":"From Prefix Cache to Fusion RAG Cache: Accelerating LLM Inference in Retrieval-Augmented Generation | Proceedings of the ACM on Management of Data","url":"https://dl.acm.org/doi/abs/10.1145/3786655?af=R"},{"title":"CacheBlend: Fast Large Language Model Serving for RAG with","url":"https://www.cs.princeton.edu/~ravian/COS597_F24/papers/cacheblend.pdf"},{"title":"ProphetKV: User-Query-Driven Selective Recomputation for Efficient KV Cache Reuse in Retrieval-Augmented Generation","url":"https://arxiv.org/html/2602.02579"},{"title":"CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration","url":"https://arxiv.org/html/2604.25080"},{"title":"[2405.16444] CacheBlend: Fast Large Language Model Serving for RAG with Cached Knowledge Fusion","url":"https://arxiv.org/abs/2405.16444"}]

Based on the search results, here's what I found about QCFuse (arXiv 2604.08585):

## QCFuse: Query-Centric Cache Fusion for Efficient RAG Inference

QCFuse is an innovative KV cache fusion system centered on the user query that leverages semantic summary anchors to enhance query representations and selectively recomputes query-related tokens to improve accuracy.

### Problem It Addresses

Cache fusion accelerates generation process of LLMs equipped with RAG through KV caching and selective token recomputation, thereby reducing computational costs and improving efficiency. However, existing methods primarily rely on local perspectives for token selection and lack global awareness from the user query.

### Key Innovation

QCFuse leverages semantic summary anchors to enhance query representations and selectively recomputes query-related tokens to improve accuracy, updating tokens based on the attention distribution of the most critical Transformer layer to preserve the high efficiency of the pipeline structure.

### Implementation and Performance

QCFuse is an efficient query-centric cache fusion system implemented on SGLang with a high-performance sparse-attention Triton kernel for discrete token recomputation. Evaluations across multiple LLMs and multi-hop QA benchmarks demonstrate up to a 2× speedup of TTFT over full computation and a 40% latency reduction compared to existing cache fusion baselines, with matching or improved generation quality.

The source code is available at https://github.com/uYanJX/QCFuse-Demo.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3a73620-4619-40e1-a714-990985526a8b",
  "isSidechain": false,
  "promptId": "b368710b-e415-41f5-a2d9-b7e249a1c17c",
  "type": "user",
  "uuid": "1405f678-aaba-4b86-8623-19e2b2cda97c",
  "toolUseResult": {
    "query": "QCFuse arXiv 2604.08585 query-centric cache fusion RAG recomputation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GgaH38saHrbMPRpkeU2kSE",
        "content": [
          {
            "title": "[2604.08585] QCFuse: Query-Centric Cache Fusion for Efficient RAG Inference",
            "url": "https://arxiv.org/abs/2604.08585"
          },
          {
            "title": "QCFuse: Query-Centric Cache Fusion for Efficient RAG Inference",
            "url": "https://arxiv.org/html/2604.08585"
          },
          {
            "title": "From Prefix Cache to Fusion RAG Cache: Accelerating LLM Inference in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2601.12904v1"
          },
          {
            "title": "𝐴³: Attention-Aware Accurate KV Cache Fusion for Fast Large Language Model Serving",
            "url": "https://arxiv.org/html/2511.17560"
          },
          {
            "title": "[2601.12904] From Prefix Cache to Fusion RAG Cache: Accelerating LLM Inference in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/abs/2601.12904"
          },
          {
            "title": "From Prefix Cache to Fusion RAG Cache: Accelerating LLM Inference in Retrieval-Augmented Generation | Proceedings of the ACM on Management of Data",
            "url": "https://dl.acm.org/doi/abs/10.1145/3786655?af=R"
          },
          {
            "title": "CacheBlend: Fast Large Language Model Serving for RAG with",
            "url": "https://www.cs.princeton.edu/~ravian/COS597_F24/papers/cacheblend.pdf"
          },
          {
            "title": "ProphetKV: User-Query-Driven Selective Recomputation for Efficient KV Cache Reuse in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2602.02579"
          },
          {
            "title": "CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration",
            "url": "https://arxiv.org/html/2604.25080"
          },
          {
            "title": "[2405.16444] CacheBlend: Fast Large Language Model Serving for RAG with Cached Knowledge Fusion",
            "url": "https://arxiv.org/abs/2405.16444"
          }
        ]
      },
      "Based on the search results, here's what I found about QCFuse (arXiv 2604.08585):\n\n## QCFuse: Query-Centric Cache Fusion for Efficient RAG Inference\n\nQCFuse is an innovative KV cache fusion system centered on the user query that leverages semantic summary anchors to enhance query representations and selectively recomputes query-related tokens to improve accuracy.\n\n### Problem It Addresses\n\nCache fusion accelerates generation process of LLMs equipped with RAG through KV caching and selective token recomputation, thereby reducing computational costs and improving efficiency. However, existing methods primarily rely on local perspectives for token selection and lack global awareness from the user query.\n\n### Key Innovation\n\nQCFuse leverages semantic summary anchors to enhance query representations and selectively recomputes query-related tokens to improve accuracy, updating tokens based on the attention distribution of the most critical Transformer layer to preserve the high efficiency of the pipeline structure.\n\n### Implementation and Performance\n\nQCFuse is an efficient query-centric cache fusion system implemented on SGLang with a high-performance sparse-attention Triton kernel for discrete token recomputation. Evaluations across multiple LLMs and multi-hop QA benchmarks demonstrate up to a 2× speedup of TTFT over full computation and a 40% latency reduction compared to existing cache fusion baselines, with matching or improved generation quality.\n\nThe source code is available at https://github.com/uYanJX/QCFuse-Demo."
    ],
    "durationSeconds": 8.190540486000002
  },
  "sourceToolAssistantUUID": "c3a73620-4619-40e1-a714-990985526a8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-12T00:04:05.616Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019NmBUjmFFG42pLu5cY9G4w`</summary>

```json
{
  "query": "CacheFlow arXiv 2604.25080 3D parallel KV cache restoration scheduling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1405f678-aaba-4b86-8623-19e2b2cda97c",
  "isSidechain": false,
  "requestId": "req_011CawhL2jLztaU6PfnEu47t",
  "type": "assistant",
  "uuid": "a2be4195-fde0-4420-930f-0987c56c885a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VYdNepXRqjnE9aYwsHVY3m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 996,
      "cache_read_input_tokens": 29086,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 996,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 29086,
          "cache_creation_input_tokens": 996,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 996
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T00:04:12.007Z_

<details><summary>↩ Tool result · `toolu_019NmBUjmFFG42pLu5cY9G4w`</summary>

```text
Web search results for query: "CacheFlow arXiv 2604.25080 3D parallel KV cache restoration scheduling"

Links: [{"title":"[2604.25080] CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration","url":"https://arxiv.org/abs/2604.25080"},{"title":"CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration","url":"https://arxiv.org/html/2604.25080"},{"title":"Efficient LLM Serving with 3D-Parallel KV Cache Restoration","url":"https://arxiv.org/pdf/2604.25080"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=332&show=1000"},{"title":"Prefill-as-a-Service: KVCache of Next-Generation Models Could Go Cross-Datacenter","url":"https://arxiv.org/html/2604.15039v1"},{"title":"[2510.09665] LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference","url":"https://arxiv.org/abs/2510.09665"},{"title":"[2604.26968] Predictive Multi-Tier Memory Management for KV Cache in Large-Scale GPU Inference","url":"https://arxiv.org/abs/2604.26968"},{"title":"KVCache Cache in the Wild: Characterizing and Optimizing KVCache Cache at a Large Cloud Provider","url":"https://arxiv.org/html/2506.02634v1"},{"title":"CacheTTL: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live","url":"https://arxiv.org/html/2511.02230v4"},{"title":"KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows","url":"https://arxiv.org/html/2507.07400v1"}]

Based on the search results, here's information about CacheFlow (arXiv 2604.25080):

## CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration

KV cache restoration has emerged as a dominant bottleneck in serving long-context LLM workloads, including multi-turn conversations, retrieval-augmented generation, and agentic pipelines.

### Key Innovation

CacheFlow is a KV cache restoration framework that rethinks cache restoration as a multi-dimensional parallel execution problem. It introduces a unified 3D parallelism abstraction across tokens, layers, and GPUs, enabling fine-grained overlap of recomputation and I/O along the structural dependencies of transformer inference.

### Three Dimensions of Parallelism

The framework decomposes restoration into three complementary forms of parallelism: (i) Token-level parallelism: overlapping recomputation of earlier tokens with I/O transfer of later tokens; (ii) Layer-level parallelism: pipelining recomputation of lower layers with transfer of higher-layer KV cache; (iii) Multi-GPU parallelism: enabling concurrent restoration across GPUs.

### Scheduling Strategy

At the core of CacheFlow is a batch-aware two-pointer scheduler that jointly optimizes compute and I/O allocation across requests by prioritizing operations with the highest marginal reduction in recomputation cost.

### Performance Results

CacheFlow reduces Time-To-First-Token (TTFT) by 10%-62% over existing advances across diverse models, workloads, and hardware.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2be4195-fde0-4420-930f-0987c56c885a",
  "isSidechain": false,
  "promptId": "b368710b-e415-41f5-a2d9-b7e249a1c17c",
  "type": "user",
  "uuid": "0cd1ef81-05d8-41c8-8b6f-d410a0743f76",
  "toolUseResult": {
    "query": "CacheFlow arXiv 2604.25080 3D parallel KV cache restoration scheduling",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EyDsUuRXHaXGcGnvBDZQBS",
        "content": [
          {
            "title": "[2604.25080] CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration",
            "url": "https://arxiv.org/abs/2604.25080"
          },
          {
            "title": "CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration",
            "url": "https://arxiv.org/html/2604.25080"
          },
          {
            "title": "Efficient LLM Serving with 3D-Parallel KV Cache Restoration",
            "url": "https://arxiv.org/pdf/2604.25080"
          },
          {
            "title": "Computer Science",
            "url": "https://arxiv.org/list/cs/pastweek?skip=332&show=1000"
          },
          {
            "title": "Prefill-as-a-Service: KVCache of Next-Generation Models Could Go Cross-Datacenter",
            "url": "https://arxiv.org/html/2604.15039v1"
          },
          {
            "title": "[2510.09665] LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference",
            "url": "https://arxiv.org/abs/2510.09665"
          },
          {
            "title": "[2604.26968] Predictive Multi-Tier Memory Management for KV Cache in Large-Scale GPU Inference",
            "url": "https://arxiv.org/abs/2604.26968"
          },
          {
            "title": "KVCache Cache in the Wild: Characterizing and Optimizing KVCache Cache at a Large Cloud Provider",
            "url": "https://arxiv.org/html/2506.02634v1"
          },
          {
            "title": "CacheTTL: Efficient and Robust Multi-Turn LLM Agent Scheduling with KV Cache Time-to-Live",
            "url": "https://arxiv.org/html/2511.02230v4"
          },
          {
            "title": "KVFlow: Efficient Prefix Caching for Accelerating LLM-Based Multi-Agent Workflows",
            "url": "https://arxiv.org/html/2507.07400v1"
          }
        ]
      },
      "Based on the search results, here's information about CacheFlow (arXiv 2604.25080):\n\n## CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration\n\nKV cache restoration has emerged as a dominant bottleneck in serving long-context LLM workloads, including multi-turn conversations, retrieval-augmented generation, and agentic pipelines.\n\n### Key Innovation\n\nCacheFlow is a KV cache restoration framework that rethinks cache restoration as a multi-dimensional parallel execution problem. It introduces a unified 3D parallelism abstraction across tokens, layers, and GPUs, enabling fine-grained overlap of recomputation and I/O along the structural dependencies of transformer inference.\n\n### Three Dimensions of Parallelism\n\nThe framework decomposes restoration into three complementary forms of parallelism: (i) Token-level parallelism: overlapping recomputation of earlier tokens with I/O transfer of later tokens; (ii) Layer-level parallelism: pipelining recomputation of lower layers with transfer of higher-layer KV cache; (iii) Multi-GPU parallelism: enabling concurrent restoration across GPUs.\n\n### Scheduling Strategy\n\nAt the core of CacheFlow is a batch-aware two-pointer scheduler that jointly optimizes compute and I/O allocation across requests by prioritizing operations with the highest marginal reduction in recomputation cost.\n\n### Performance Results\n\nCacheFlow reduces Time-To-First-Token (TTFT) by 10%-62% over existing advances across diverse models, workloads, and hardware."
    ],
    "durationSeconds": 6.386749788000001
  },
  "sourceToolAssistantUUID": "a2be4195-fde0-4420-930f-0987c56c885a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"CompressLink: Co-Optimizing Compression and Restoration for Position-I…",
  "leafUuid": "0cd1ef81-05d8-41c8-8b6f-d410a0743f76",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Co-optimize KV compression and restoration for RAG chunk caching",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c"
}
```

---

### Tool call

_source line 22 · 2026-05-12T00:04:15.007Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QGgTdJ6RfmepqapbH2p6yF`</summary>

```json
{
  "query": "HeadQ arXiv 2605.03562 score-space distortion KV cache quantization Fisher information"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cd1ef81-05d8-41c8-8b6f-d410a0743f76",
  "isSidechain": false,
  "requestId": "req_011CawhLgetFUrDH1y4ZEPor",
  "type": "assistant",
  "uuid": "20907a25-607f-4157-a9d3-cf9f60e4a423",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xg4LDpHXWTHroYNXXeGpof",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 957,
      "cache_read_input_tokens": 30082,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 957,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 30082,
          "cache_creation_input_tokens": 957,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 957
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-12T00:04:22.522Z_

<details><summary>↩ Tool result · `toolu_01QGgTdJ6RfmepqapbH2p6yF`</summary>

```text
Web search results for query: "HeadQ arXiv 2605.03562 score-space distortion KV cache quantization Fisher information"

Links: [{"title":"HeadQ: Model-Visible Distortion and a Prototype KV Quantizer-Corrector Codec","url":"https://arxiv.org/html/2605.03562"},{"title":"[2605.03562] HeadQ: Model-Visible Distortion and Score-Space Correction for KV-Cache Quantization","url":"https://arxiv.org/abs/2605.03562"},{"title":"HeadQ: Model-Visible Distortion and Score-Space Correction for KV-Cache Quantization","url":"https://arxiv.org/html/2605.03562v1"},{"title":"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/html/2605.06675"},{"title":"[2605.06675] RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/abs/2605.06675"},{"title":"eOptShrinkQ: Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization","url":"https://arxiv.org/html/2605.02905"},{"title":"ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget for Long-Context Inference in LLMs","url":"https://arxiv.org/html/2603.08727"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution","url":"https://arxiv.org/html/2510.00636v1"},{"title":"[2605.02262] WindowQuant: Mixed-Precision KV Cache Quantization based on Window-Level Similarity for VLMs Inference Optimization","url":"https://arxiv.org/abs/2605.02262"},{"title":"[2406.03482] QJL: 1-Bit Quantized JL Transform for KV Cache Quantization with Zero Overhead","url":"https://arxiv.org/abs/2406.03482"}]

Based on the search results, here's what I found about HeadQ (arXiv 2605.03562):

## Overview

HeadQ addresses the issue that KV-cache quantizers usually optimize storage-space reconstruction, even though attention reads keys through logits and values through attention-weighted readout. The paper argues that persistent cache error should be measured in model-visible coordinates.

## Key Concepts

**Score-Space Distortion and Fisher Information:**

For keys, the visible object is score error modulo constant shifts; this yields HeadQ, a key-side method that stores a low-rank residual side code in a calibration-learned query basis and applies it as an additive logit correction.

For values, fixed-attention readout gives an A²-weighted token-distortion surrogate.

## Empirical Results

Across six models, Fisher/score-space error predicts attention KL far better than raw key MSE; same-budget counterexamples, null-space interventions, query-PCA controls, and wrong-sign HeadQ falsify storage-MSE alternatives.

## Implementation Details

The Fisher object is a derivation and diagnostic; the computational primitive is cheaper: compute score errors, remove the softmax-inert constant, and preserve the remaining score-visible coordinates.

The paper demonstrates that measuring quantization error in score-space (using Fisher information) rather than traditional MSE provides better predictions of actual model performance, offering a more principled approach to KV cache quantization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20907a25-607f-4157-a9d3-cf9f60e4a423",
  "isSidechain": false,
  "promptId": "b368710b-e415-41f5-a2d9-b7e249a1c17c",
  "type": "user",
  "uuid": "9b3598e6-7984-42ef-a3b0-d5cb24959ab7",
  "toolUseResult": {
    "query": "HeadQ arXiv 2605.03562 score-space distortion KV cache quantization Fisher information",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KbA6W2dVgJeor4CyEDEUze",
        "content": [
          {
            "title": "HeadQ: Model-Visible Distortion and a Prototype KV Quantizer-Corrector Codec",
            "url": "https://arxiv.org/html/2605.03562"
          },
          {
            "title": "[2605.03562] HeadQ: Model-Visible Distortion and Score-Space Correction for KV-Cache Quantization",
            "url": "https://arxiv.org/abs/2605.03562"
          },
          {
            "title": "HeadQ: Model-Visible Distortion and Score-Space Correction for KV-Cache Quantization",
            "url": "https://arxiv.org/html/2605.03562v1"
          },
          {
            "title": "RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory",
            "url": "https://arxiv.org/html/2605.06675"
          },
          {
            "title": "[2605.06675] RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory",
            "url": "https://arxiv.org/abs/2605.06675"
          },
          {
            "title": "eOptShrinkQ: Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization",
            "url": "https://arxiv.org/html/2605.02905"
          },
          {
            "title": "ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget for Long-Context Inference in LLMs",
            "url": "https://arxiv.org/html/2603.08727"
          },
          {
            "title": "Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution",
            "url": "https://arxiv.org/html/2510.00636v1"
          },
          {
            "title": "[2605.02262] WindowQuant: Mixed-Precision KV Cache Quantization based on Window-Level Similarity for VLMs Inference Optimization",
            "url": "https://arxiv.org/abs/2605.02262"
          },
          {
            "title": "[2406.03482] QJL: 1-Bit Quantized JL Transform for KV Cache Quantization with Zero Overhead",
            "url": "https://arxiv.org/abs/2406.03482"
          }
        ]
      },
      "Based on the search results, here's what I found about HeadQ (arXiv 2605.03562):\n\n## Overview\n\nHeadQ addresses the issue that KV-cache quantizers usually optimize storage-space reconstruction, even though attention reads keys through logits and values through attention-weighted readout. The paper argues that persistent cache error should be measured in model-visible coordinates.\n\n## Key Concepts\n\n**Score-Space Distortion and Fisher Information:**\n\nFor keys, the visible object is score error modulo constant shifts; this yields HeadQ, a key-side method that stores a low-rank residual side code in a calibration-learned query basis and applies it as an additive logit correction.\n\nFor values, fixed-attention readout gives an A²-weighted token-distortion surrogate.\n\n## Empirical Results\n\nAcross six models, Fisher/score-space error predicts attention KL far better than raw key MSE; same-budget counterexamples, null-space interventions, query-PCA controls, and wrong-sign HeadQ falsify storage-MSE alternatives.\n\n## Implementation Details\n\nThe Fisher object is a derivation and diagnostic; the computational primitive is cheaper: compute score errors, remove the softmax-inert constant, and preserve the remaining score-visible coordinates.\n\nThe paper demonstrates that measuring quantization error in score-space (using Fisher information) rather than traditional MSE provides better predictions of actual model performance, offering a more principled approach to KV cache quantization."
    ],
    "durationSeconds": 7.510926564000001
  },
  "sourceToolAssistantUUID": "20907a25-607f-4157-a9d3-cf9f60e4a423",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-12T00:04:24.700Z_

Now let me read the key papers in more detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b3598e6-7984-42ef-a3b0-d5cb24959ab7",
  "isSidechain": false,
  "requestId": "req_011CawhMTcqStZPd7cxkYRz8",
  "type": "assistant",
  "uuid": "e2351aff-517a-4b15-b4de-10475672bf2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017EqKLcQz9egFvKSyP9gLje",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 980,
      "cache_read_input_tokens": 31039,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 980,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 31039,
          "cache_creation_input_tokens": 980,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 980
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-12T00:04:27.127Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AjT7icbMt5G1kth4HRYBoU`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.14946",
  "prompt": "Extract the full abstract and key technical details: (1) How does the unified utility function work? (2) What does \"conservative compression to contexts sensitive to compression errors\" mean specifically? (3) How does it decide which KV caches to compress vs evict? (4) Does it operate at per-token granularity or per-cache/per-context granularity?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2351aff-517a-4b15-b4de-10475672bf2d",
  "isSidechain": false,
  "requestId": "req_011CawhMTcqStZPd7cxkYRz8",
  "type": "assistant",
  "uuid": "9f2be6b9-498a-41d7-ac5f-307580a79a98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017EqKLcQz9egFvKSyP9gLje",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 980,
      "cache_read_input_tokens": 31039,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 980,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 31039,
          "cache_creation_input_tokens": 980,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 980
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-12T00:04:32.729Z_

<details><summary>↩ Tool result · `toolu_01AjT7icbMt5G1kth4HRYBoU`</summary>

```text
# EVICPRESS: KV-Cache Management Analysis

## Full Abstract
The system addresses KV cache memory constraints by jointly optimizing lossy compression and adaptive eviction across storage tiers. It proposes a unified utility function that quantifies quality and latency effects, enabling placement decisions that maximize cache hit rates on fast devices while preserving generation quality.

## Technical Details

**1. Unified Utility Function**
The system employs a mechanism that "quantifies the effect of quality and delay of the lossy compression or eviction." The profiling module periodically updates utility scores for all possible eviction-compression configurations, allowing the system to balance speed improvements against quality degradation trade-offs.

**2. Conservative Compression Strategy**
The approach applies "conservative compression to contexts that are sensitive to compression errors." This means the system identifies which contexts degrade significantly under lossy compression and compresses them minimally, while more robust contexts receive aggressive compression.

**3. Compression vs. Eviction Decisions**
The system doesn't explicitly detail decision logic in the provided abstract. However, it indicates decisions occur through "a fast heuristic to rearrange KV caches on all storage tiers" based on utility scores, suggesting decisions optimize placement across the storage hierarchy rather than binary compression-or-evict choices.

**4. Operational Granularity**
The evidence points to **per-context or per-cache granularity**. The abstract references "each KV cache of a context" and evaluates effects "across all contexts as a whole," indicating context-level management rather than per-token decisions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f2be6b9-498a-41d7-ac5f-307580a79a98",
  "isSidechain": false,
  "promptId": "b368710b-e415-41f5-a2d9-b7e249a1c17c",
  "type": "user",
  "uuid": "378e1b04-566e-4155-b834-1026b9aaf338",
  "toolUseResult": {
    "bytes": 49512,
    "code": 200,
    "codeText": "OK",
    "result": "# EVICPRESS: KV-Cache Management Analysis\n\n## Full Abstract\nThe system addresses KV cache memory constraints by jointly optimizing lossy compression and adaptive eviction across storage tiers. It proposes a unified utility function that quantifies quality and latency effects, enabling placement decisions that maximize cache hit rates on fast devices while preserving generation quality.\n\n## Technical Details\n\n**1. Unified Utility Function**\nThe system employs a mechanism that \"quantifies the effect of quality and delay of the lossy compression or eviction.\" The profiling module periodically updates utility scores for all possible eviction-compression configurations, allowing the system to balance speed improvements against quality degradation trade-offs.\n\n**2. Conservative Compression Strategy**\nThe approach applies \"conservative compression to contexts that are sensitive to compression errors.\" This means the system identifies which contexts degrade significantly under lossy compression and compresses them minimally, while more robust contexts receive aggressive compression.\n\n**3. Compression vs. Eviction Decisions**\nThe system doesn't explicitly detail decision logic in the provided abstract. However, it indicates decisions occur through \"a fast heuristic to rearrange KV caches on all storage tiers\" based on utility scores, suggesting decisions optimize placement across the storage hierarchy rather than binary compression-or-evict choices.\n\n**4. Operational Granularity**\nThe evidence points to **per-context or per-cache granularity**. The abstract references \"each KV cache of a context\" and evaluates effects \"across all contexts as a whole,\" indicating context-level management rather than per-token decisions.",
    "durationMs": 5598,
    "url": "https://arxiv.org/abs/2512.14946"
  },
  "sourceToolAssistantUUID": "9f2be6b9-498a-41d7-ac5f-307580a79a98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-12T00:04:36.946Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M3ZjiDXSCSe479rFqd7y7E`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.08585",
  "prompt": "Extract: (1) Full abstract, (2) How does QCFuse select tokens for recomputation — what is the \"semantic summary anchor\" mechanism? (3) How does it determine the \"most critical Transformer layer\"? (4) What baselines does it compare against? (5) Does it consider compression at all? (6) What are the specific criticisms of ProphetKV mentioned in the paper?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "378e1b04-566e-4155-b834-1026b9aaf338",
  "isSidechain": false,
  "requestId": "req_011CawhNDGesYixSRuii5iri",
  "type": "assistant",
  "uuid": "923f7ffc-b3c7-4b35-a198-9e23a65da9ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HgyjzT4ow36WstSJazCeSE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 530,
      "cache_read_input_tokens": 32019,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 530,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 32019,
          "cache_creation_input_tokens": 530,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 530
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-12T00:04:42.431Z_

<details><summary>↩ Tool result · `toolu_01M3ZjiDXSCSe479rFqd7y7E`</summary>

```text
# QCFuse Paper Analysis

Based on the arXiv page provided, here's what can be extracted:

**(1) Full Abstract:**
"Cache fusion accelerates generation process of LLMs equipped with RAG through KV caching and selective token recomputation, thereby reducing computational costs and improving efficiency. However, existing methods primarily rely on local perspectives for token selection and lack global awareness from the user query. Utilizing this global awareness is challenging due to the high cost of obtaining context-aware query representations and the strict pipeline constraints required for efficient attention analysis. Thus, this demonstration introduces QCFuse, an innovative KV cache fusion system centered on the user query. QCFuse leverages semantic summary anchors to enhance query representations and selectively recomputes query-related tokens to improve accuracy, updating tokens based on the attention distribution of the most critical Transformer layer to preserve the high efficiency of the pipeline structure. Evaluations on real-world datasets demonstrate that QCFuse significantly improves the response efficiency of LLMs by 40% while maintaining equivalent accuracy compared to current methods. Additionally, in certain scenarios, QCFuse achieves an attention denoising effect that yields higher response accuracy, demonstrating substantial potential in the optimization of LLM inference."

**(2-6) Unavailable:**
The webpage excerpt provided contains only the abstract and metadata. Specific technical details about semantic summary anchor mechanisms, critical layer identification, baseline comparisons, compression considerations, and criticisms of ProphetKV are not included in this page content and would require access to the full paper PDF or HTML version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "923f7ffc-b3c7-4b35-a198-9e23a65da9ca",
  "isSidechain": false,
  "promptId": "b368710b-e415-41f5-a2d9-b7e249a1c17c",
  "type": "user",
  "uuid": "f246f2f9-5933-436d-8dc1-34700456d3d7",
  "toolUseResult": {
    "bytes": 46986,
    "code": 200,
    "codeText": "OK",
    "result": "# QCFuse Paper Analysis\n\nBased on the arXiv page provided, here's what can be extracted:\n\n**(1) Full Abstract:**\n\"Cache fusion accelerates generation process of LLMs equipped with RAG through KV caching and selective token recomputation, thereby reducing computational costs and improving efficiency. However, existing methods primarily rely on local perspectives for token selection and lack global awareness from the user query. Utilizing this global awareness is challenging due to the high cost of obtaining context-aware query representations and the strict pipeline constraints required for efficient attention analysis. Thus, this demonstration introduces QCFuse, an innovative KV cache fusion system centered on the user query. QCFuse leverages semantic summary anchors to enhance query representations and selectively recomputes query-related tokens to improve accuracy, updating tokens based on the attention distribution of the most critical Transformer layer to preserve the high efficiency of the pipeline structure. Evaluations on real-world datasets demonstrate that QCFuse significantly improves the response efficiency of LLMs by 40% while maintaining equivalent accuracy compared to current methods. Additionally, in certain scenarios, QCFuse achieves an attention denoising effect that yields higher response accuracy, demonstrating substantial potential in the optimization of LLM inference.\"\n\n**(2-6) Unavailable:**\nThe webpage excerpt provided contains only the abstract and metadata. Specific technical details about semantic summary anchor mechanisms, critical layer identification, baseline comparisons, compression considerations, and criticisms of ProphetKV are not included in this page content and would require access to the full paper PDF or HTML version.",
    "durationMs": 5482,
    "url": "https://arxiv.org/abs/2604.08585"
  },
  "sourceToolAssistantUUID": "923f7ffc-b3c7-4b35-a198-9e23a65da9ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-12T00:04:42.433Z_

```json
{
  "parentUuid": "f246f2f9-5933-436d-8dc1-34700456d3d7",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "9fb8690d-1549-44f8-b044-c7c1cd91d0bb",
  "timestamp": "2026-05-12T00:04:42.433Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-12T00:04:45.209Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012y4q9bmN5qES48MGrShdZw`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.08585",
  "prompt": "Extract: (1) How does QCFuse select tokens for recomputation — what is the \"semantic summary anchor\" mechanism? (2) How does it determine the \"most critical Transformer layer\"? (3) What baselines does it compare against? (4) Does it consider KV compression at all? (5) What are the specific criticisms of ProphetKV? (6) What recomputation ratios does it use?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fb8690d-1549-44f8-b044-c7c1cd91d0bb",
  "isSidechain": false,
  "requestId": "req_011CawhNvj217abvspztXP2K",
  "type": "assistant",
  "uuid": "01c33412-b5fc-489f-ab5c-fef7389c2599",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mMGqKMUrXuHhaBdZ3DunH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 626,
      "cache_read_input_tokens": 32549,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 626,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 32549,
          "cache_creation_input_tokens": 626,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 626
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-12T00:04:51.045Z_

<details><summary>↩ Tool result · `toolu_012y4q9bmN5qES48MGrShdZw`</summary>

```text
# QCFuse: Key Technical Details

**(1) Semantic Summary Anchor Mechanism**
QCFuse extracts anchor tokens by analyzing "token key-norm magnitudes" from precomputed context chunks. These high-magnitude tokens serve as "compressed semantic summaries" injected as "lightweight prefixes during query forwarding" to ground query representations without disrupting pipeline efficiency.

**(2) Critical Layer Selection**
Rather than analyzing all transformer layers, the system identifies "a single pipeline-friendly layer whose attention distribution serves as a reliable proxy for global token importance." The paper notes that "middle layers offer superior semantic localization," avoiding both cross-layer pipeline stalls and the incomplete semantic view of last-layer approaches.

**(3) Baseline Comparisons**
QCFuse compares against:
- CacheBlend (uses first-layer KV deviations)
- EPIC (static recomputation ratio)
- KVShare (scales KV deviation by attention weights)
- ProphetKV (emulated as "QCAll")
- FusionRAG (emulated as "QCLast")
- Full computation and full reuse baselines

**(4) KV Compression**
The paper does not discuss KV compression techniques. Its focus centers on selective token recomputation rather than compression.

**(5) ProphetKV Criticisms**
ProphetKV "evaluates all layers concurrently, ignoring stage-wise scheduling constraints," which disrupts pipelined execution efficiency.

**(6) Recomputation Ratios**
Evaluations test ratios from 0.1 to 0.5 (10–50%). At 40% recomputation, QCFuse "matches the accuracy of full computation."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01c33412-b5fc-489f-ab5c-fef7389c2599",
  "isSidechain": false,
  "promptId": "b368710b-e415-41f5-a2d9-b7e249a1c17c",
  "type": "user",
  "uuid": "d8312590-e91f-4feb-b2b2-88ec22884732",
  "toolUseResult": {
    "bytes": 106361,
    "code": 200,
    "codeText": "OK",
    "result": "# QCFuse: Key Technical Details\n\n**(1) Semantic Summary Anchor Mechanism**\nQCFuse extracts anchor tokens by analyzing \"token key-norm magnitudes\" from precomputed context chunks. These high-magnitude tokens serve as \"compressed semantic summaries\" injected as \"lightweight prefixes during query forwarding\" to ground query representations without disrupting pipeline efficiency.\n\n**(2) Critical Layer Selection**\nRather than analyzing all transformer layers, the system identifies \"a single pipeline-friendly layer whose attention distribution serves as a reliable proxy for global token importance.\" The paper notes that \"middle layers offer superior semantic localization,\" avoiding both cross-layer pipeline stalls and the incomplete semantic view of last-layer approaches.\n\n**(3) Baseline Comparisons**\nQCFuse compares against:\n- CacheBlend (uses first-layer KV deviations)\n- EPIC (static recomputation ratio)\n- KVShare (scales KV deviation by attention weights)\n- ProphetKV (emulated as \"QCAll\")\n- FusionRAG (emulated as \"QCLast\")\n- Full computation and full reuse baselines\n\n**(4) KV Compression**\nThe paper does not discuss KV compression techniques. Its focus centers on selective token recomputation rather than compression.\n\n**(5) ProphetKV Criticisms**\nProphetKV \"evaluates all layers concurrently, ignoring stage-wise scheduling constraints,\" which disrupts pipelined execution efficiency.\n\n**(6) Recomputation Ratios**\nEvaluations test ratios from 0.1 to 0.5 (10–50%). At 40% recomputation, QCFuse \"matches the accuracy of full computation.\"",
    "durationMs": 5834,
    "url": "https://arxiv.org/html/2604.08585"
  },
  "sourceToolAssistantUUID": "01c33412-b5fc-489f-ab5c-fef7389c2599",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-12T00:04:57.044Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BNCe5GU4mtJNtBw9uiEbs2`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.03562",
  "prompt": "Extract the key technical argument about why storage-space MSE is a poor proxy for model-visible distortion. Specifically: (1) What are the \"null-space interventions\" that show MSE can be misleading? (2) Is there evidence that MSE-based ranking is monotonically related to score-space error for moderate compression? (3) Does HeadQ address per-token error estimation or only per-head? (4) What is the computational cost of computing score-space error vs MSE?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8312590-e91f-4feb-b2b2-88ec22884732",
  "isSidechain": false,
  "requestId": "req_011CawhPZbJs4tCJQS75JQAm",
  "type": "assistant",
  "uuid": "5406a679-c222-4beb-947d-cefe587b81aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhXww3zZJc8vAFEUg5JaXs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 582,
      "cache_read_input_tokens": 33175,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 582,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 33175,
          "cache_creation_input_tokens": 582,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 582
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-12T00:05:05.322Z_

<details><summary>↩ Tool result · `toolu_01BNCe5GU4mtJNtBw9uiEbs2`</summary>

```text
# Key Technical Arguments on Storage MSE vs Model-Visible Distortion

## (1) Null-Space Interventions

The paper uses a token-shared mean restoration intervention (Eq. 23) to isolate MSE's failure mode. By adding back an attention-inert common key component α·1·k̄ᵀ while holding the residual fixed, the authors show that:

- Dense attention remains unchanged (softmax cancels the constant)
- Fixed-grid quantizers experience sharp Fisher damage increases
- Non-equivariant quantizers convert "invisible storage energy" into active score error

As stated: "a perturbation can have large storage error and zero attention damage, while a smaller perturbation in the active direction can change attention sharply."

## (2) MSE-Ranking Monotonicity

The evidence is **not** monotonic. Table 2 presents a direct counterexample: a centered TurboQuant-MSE baseline achieves *lower* key MSE than the Fisher-pullback baseline while producing *worse* Fisher error, attention KL, and output MSE. The paper notes this separates "Euclidean reconstruction" success from behavioral validity—storage coordinates don't order behavioral importance.

## (3) Per-Token vs Per-Head Scope

HeadQ operates at per-head granularity. The residual code Z ∈ ℝⁿ×ʳ has one coordinate per cached key position and per head, but the query basis Uₕ is "learned per-head" from calibration. Token-level variation is captured in the rank-r projection, not separate per-token estimation.

## (4) Computational Cost Comparison

The paper does not provide explicit computational benchmarks. It notes using "Python-side eager-attention hooks for calibration and evaluation rather than custom CUDA kernels," treating systems optimization as out-of-scope. Fisher computation (Eq. 6) requires only score variance calculation—"cheaper" than dense matrix operations—but no wall-clock comparison to MSE is given.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5406a679-c222-4beb-947d-cefe587b81aa",
  "isSidechain": false,
  "promptId": "b368710b-e415-41f5-a2d9-b7e249a1c17c",
  "type": "user",
  "uuid": "99b8d254-d5fb-41f6-9244-59297c3c1b12",
  "toolUseResult": {
    "bytes": 309940,
    "code": 200,
    "codeText": "OK",
    "result": "# Key Technical Arguments on Storage MSE vs Model-Visible Distortion\n\n## (1) Null-Space Interventions\n\nThe paper uses a token-shared mean restoration intervention (Eq. 23) to isolate MSE's failure mode. By adding back an attention-inert common key component α·1·k̄ᵀ while holding the residual fixed, the authors show that:\n\n- Dense attention remains unchanged (softmax cancels the constant)\n- Fixed-grid quantizers experience sharp Fisher damage increases\n- Non-equivariant quantizers convert \"invisible storage energy\" into active score error\n\nAs stated: \"a perturbation can have large storage error and zero attention damage, while a smaller perturbation in the active direction can change attention sharply.\"\n\n## (2) MSE-Ranking Monotonicity\n\nThe evidence is **not** monotonic. Table 2 presents a direct counterexample: a centered TurboQuant-MSE baseline achieves *lower* key MSE than the Fisher-pullback baseline while producing *worse* Fisher error, attention KL, and output MSE. The paper notes this separates \"Euclidean reconstruction\" success from behavioral validity—storage coordinates don't order behavioral importance.\n\n## (3) Per-Token vs Per-Head Scope\n\nHeadQ operates at per-head granularity. The residual code Z ∈ ℝⁿ×ʳ has one coordinate per cached key position and per head, but the query basis Uₕ is \"learned per-head\" from calibration. Token-level variation is captured in the rank-r projection, not separate per-token estimation.\n\n## (4) Computational Cost Comparison\n\nThe paper does not provide explicit computational benchmarks. It notes using \"Python-side eager-attention hooks for calibration and evaluation rather than custom CUDA kernels,\" treating systems optimization as out-of-scope. Fisher computation (Eq. 6) requires only score variance calculation—\"cheaper\" than dense matrix operations—but no wall-clock comparison to MSE is given.",
    "durationMs": 8273,
    "url": "https://arxiv.org/html/2605.03562"
  },
  "sourceToolAssistantUUID": "5406a679-c222-4beb-947d-cefe587b81aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"CompressLink: Co-Optimizing Compression and Restoration for Position-I…",
  "leafUuid": "99b8d254-d5fb-41f6-9244-59297c3c1b12",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Co-optimize KV compression and restoration for RAG chunk caching",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c"
}
```

---

### Assistant

_source line 36 · 2026-05-12T00:05:28.746Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have detailed information on all three missing references and a deep understanding of HeadQ's challenge. Let me also search for any additional recent work that might be relevant.

Key findings:
1. **EVICPRESS**: Per-context granularity, system-level decisions about whether to compress and where to place. CompressLink operates at per-token bit allocation granularity — clear differentiation.

2. **QCFuse**: A restoration competitor using semantic summary anchors and single-layer attention analysis. Doesn't consider compression. Criticizes ProphetKV's pipeline disruption. Should be added as a baseline/comparison for restoration.


3. **CacheFlow** is orthogonal to CompressLink's approach — it optimizes execution for restoration rather than the selection process itself, so restored tokens would actually benefit from its parallel execution capabilities.

4. For the HeadQ challenge, the core issue is that MSE ranking doesn't correlate monotonically with score-space error, which poses a problem for CEGR. But I can defend this by noting that CEGR uses compression error only for relative ranking among tokens already filtered as query-relevant, whereas HeadQ's counterexamples compare entirely different quantization schemes.  Within a single head and quantization scheme, the PCA residual energy should be more reliably monotonic with score-space error. I should still acknowledge this limitation and propose a score-space variant as an alternative, backed by ablation studies.

For the timeline, I'm mapping out a 16-day sprint: reimplementing MEPIC NoPE and starting the KVTC pipeline in the first two days, completing KVTC with chunk-aware PCA calibration by day four, then RABA implementation through day seven, CEGR through day ten, the joint optimization loop by day twelve, and evaluation across days thirteen through fifteen, with paper writing overlapping toward the end.

On the KVTC implementation risk, if I can't hit the 20x compression target, I'll evaluate at 4-8x instead and flag the higher ratios as future work. The reviewer's feedback suggests these are targeted fixes rather than fundamental issues—they mentioned I'm close to passing and that addressing these four points should push the average score to 4.0. Let me also check if there's any very recent work I should be aware of.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99b8d254-d5fb-41f6-9244-59297c3c1b12",
  "isSidechain": false,
  "requestId": "req_011CawhQcavLD3nB8bYBhMke",
  "type": "assistant",
  "uuid": "b8462f7b-3365-4466-b5c6-922214267010",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qcBiYJR4923nF8BHzbEjS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 667,
      "cache_read_input_tokens": 33757,
      "output_tokens": 745,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 667,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 745,
          "cache_read_input_tokens": 33757,
          "cache_creation_input_tokens": 667,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 667
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-12T00:05:28.749Z_

Let me also check for any very recent concurrent work that could affect the positioning.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8462f7b-3365-4466-b5c6-922214267010",
  "isSidechain": false,
  "requestId": "req_011CawhQcavLD3nB8bYBhMke",
  "type": "assistant",
  "uuid": "67efebf1-26ee-496f-a856-019986adb10a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qcBiYJR4923nF8BHzbEjS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 667,
      "cache_read_input_tokens": 33757,
      "output_tokens": 745,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 667,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 745,
          "cache_read_input_tokens": 33757,
          "cache_creation_input_tokens": 667,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 667
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-12T00:05:28.762Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0174sxM1e2NAuTD2KcRzcXAe`</summary>

```json
{
  "query": "joint compression restoration KV cache RAG chunk caching 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67efebf1-26ee-496f-a856-019986adb10a",
  "isSidechain": false,
  "requestId": "req_011CawhQcavLD3nB8bYBhMke",
  "type": "assistant",
  "uuid": "d40289d0-8ea3-4ca3-86ca-241de18d5419",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qcBiYJR4923nF8BHzbEjS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 667,
      "cache_read_input_tokens": 33757,
      "output_tokens": 745,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 667,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 745,
          "cache_read_input_tokens": 33757,
          "cache_creation_input_tokens": 667,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 667
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-12T00:05:36.392Z_

<details><summary>↩ Tool result · `toolu_0174sxM1e2NAuTD2KcRzcXAe`</summary>

```text
Web search results for query: "joint compression restoration KV cache RAG chunk caching 2026 arXiv"

Links: [{"title":"ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference","url":"https://arxiv.org/html/2502.00299v5"},{"title":"CacheClip: Accelerating RAG with Effective KV Cache Reuse","url":"https://arxiv.org/html/2510.10129v1"},{"title":"[2510.10129] CacheClip: Accelerating RAG with Effective KV Cache Reuse","url":"https://arxiv.org/abs/2510.10129"},{"title":"Beyond RAG: Task-Aware KV Cache Compression for Comprehensive Knowledge Reasoning","url":"https://arxiv.org/html/2503.04973v1"},{"title":"Caching and Reuse Optimizations","url":"https://www.aussieai.com/research/caching"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference | OpenReview","url":"https://openreview.net/forum?id=20JDhbJqn3"},{"title":"CacheGen: KV Cache Compression and Streaming for Fast Large","url":"https://arxiv.org/pdf/2310.07240"},{"title":"EvicPress: Joint KV-Cache Compression and Eviction for Efficient LLM Serving","url":"https://arxiv.org/html/2512.14946"},{"title":"An experimental study of KV cache reuse strategies in chunk-level caching systems","url":"https://arxiv.org/html/2603.20218"}]

Based on the search results, I found several relevant 2026 arXiv papers related to KV cache compression and RAG chunk caching. Here are the key findings:

## Main Papers Found:

**1. ChunkKV: Semantic-Preserving KV Cache Compression**
ChunkKV demonstrates that chunks of the original KV cache are more important than discrete tokens as inference scenarios become increasingly complex with dynamic KV cache compression methods. The approach groups tokens in a chunk as a basic compressing unit, which should be preserved or discarded as a whole, retaining the most informative semantic chunks from the original KV cache. The innovation includes a novel layer-wise index reuse technique that exploits higher cross-layer similarity of preserved indices, reducing computational overhead and improving throughput by 26.5%.

**2. CacheClip: Accelerating RAG with Effective KV Cache Reuse**
CacheClip integrates three techniques: auxiliary-LLM-guided selection of important tokens to restore inter-chunk dependencies with finetuned auxiliary models, a shared prefix to eliminate redundant attention sinks, and a grouping strategy to maintain local coherence when partially updating the KV cache.

**3. EvicPress: Joint KV-Cache Compression and Eviction**
EvicPress computes utility functions based on context-level rather than chunk-level or token-level, as context-level profiling has a global view of important token distribution considering the entire context.

**4. Chunk-level Caching Systems Study**
Chunk-level caching addresses limitations by computing the KV caches of individual chunks independently and pursuing position-independent reuse to avoid redundant computation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d40289d0-8ea3-4ca3-86ca-241de18d5419",
  "isSidechain": false,
  "promptId": "b368710b-e415-41f5-a2d9-b7e249a1c17c",
  "type": "user",
  "uuid": "46e6d17d-ab2b-4ad7-a5a0-121ebe0d0335",
  "toolUseResult": {
    "query": "joint compression restoration KV cache RAG chunk caching 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EgEVnkB4e5wpHW64CdeooL",
        "content": [
          {
            "title": "ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference",
            "url": "https://arxiv.org/html/2502.00299v5"
          },
          {
            "title": "CacheClip: Accelerating RAG with Effective KV Cache Reuse",
            "url": "https://arxiv.org/html/2510.10129v1"
          },
          {
            "title": "[2510.10129] CacheClip: Accelerating RAG with Effective KV Cache Reuse",
            "url": "https://arxiv.org/abs/2510.10129"
          },
          {
            "title": "Beyond RAG: Task-Aware KV Cache Compression for Comprehensive Knowledge Reasoning",
            "url": "https://arxiv.org/html/2503.04973v1"
          },
          {
            "title": "Caching and Reuse Optimizations",
            "url": "https://www.aussieai.com/research/caching"
          },
          {
            "title": "GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).",
            "url": "https://github.com/October2001/Awesome-KV-Cache-Compression"
          },
          {
            "title": "ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference | OpenReview",
            "url": "https://openreview.net/forum?id=20JDhbJqn3"
          },
          {
            "title": "CacheGen: KV Cache Compression and Streaming for Fast Large",
            "url": "https://arxiv.org/pdf/2310.07240"
          },
          {
            "title": "EvicPress: Joint KV-Cache Compression and Eviction for Efficient LLM Serving",
            "url": "https://arxiv.org/html/2512.14946"
          },
          {
            "title": "An experimental study of KV cache reuse strategies in chunk-level caching systems",
            "url": "https://arxiv.org/html/2603.20218"
          }
        ]
      },
      "Based on the search results, I found several relevant 2026 arXiv papers related to KV cache compression and RAG chunk caching. Here are the key findings:\n\n## Main Papers Found:\n\n**1. ChunkKV: Semantic-Preserving KV Cache Compression**\nChunkKV demonstrates that chunks of the original KV cache are more important than discrete tokens as inference scenarios become increasingly complex with dynamic KV cache compression methods. The approach groups tokens in a chunk as a basic compressing unit, which should be preserved or discarded as a whole, retaining the most informative semantic chunks from the original KV cache. The innovation includes a novel layer-wise index reuse technique that exploits higher cross-layer similarity of preserved indices, reducing computational overhead and improving throughput by 26.5%.\n\n**2. CacheClip: Accelerating RAG with Effective KV Cache Reuse**\nCacheClip integrates three techniques: auxiliary-LLM-guided selection of important tokens to restore inter-chunk dependencies with finetuned auxiliary models, a shared prefix to eliminate redundant attention sinks, and a grouping strategy to maintain local coherence when partially updating the KV cache.\n\n**3. EvicPress: Joint KV-Cache Compression and Eviction**\nEvicPress computes utility functions based on context-level rather than chunk-level or token-level, as context-level profiling has a global view of important token distribution considering the entire context.\n\n**4. Chunk-level Caching Systems Study**\nChunk-level caching addresses limitations by computing the KV caches of individual chunks independently and pursuing position-independent reuse to avoid redundant computation."
    ],
    "durationSeconds": 7.624569942999995
  },
  "sourceToolAssistantUUID": "d40289d0-8ea3-4ca3-86ca-241de18d5419",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-12T00:05:38.635Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015KKdYfFpjshR4dzr3ugbiu`</summary>

```json
{
  "query": "\"restoration-aware\" OR \"compression-aware restoration\" KV cache bit allocation token selection 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46e6d17d-ab2b-4ad7-a5a0-121ebe0d0335",
  "isSidechain": false,
  "requestId": "req_011CawhSuTEVuWpHxBJuWUUy",
  "type": "assistant",
  "uuid": "a98f9d24-6e9a-4939-b97c-e01599d25d97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtULXE4BHk4iGGkcan2qs1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1640,
      "cache_read_input_tokens": 34424,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1640,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 34424,
          "cache_creation_input_tokens": 1640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1640
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-12T00:05:46.399Z_

<details><summary>↩ Tool result · `toolu_015KKdYfFpjshR4dzr3ugbiu`</summary>

```text
Web search results for query: ""restoration-aware" OR "compression-aware restoration" KV cache bit allocation token selection 2025 2026"

Links: [{"title":"Beyond Token Eviction: Mixed-Dimension Budget Allocation for Efficient KV Cache Compression","url":"https://arxiv.org/html/2603.20616"},{"title":"Optimizing Key-Value Cache Compression in Long-context ...","url":"https://aclanthology.org/2025.acl-long.529.pdf"},{"title":"GitHub - TreeAI-Lab/Awesome-KV-Cache-Management: This repository serves as a comprehensive survey of LLM development, featuring numerous research papers along with their corresponding code links. · GitHub","url":"https://github.com/TreeAI-Lab/Awesome-KV-Cache-Management"},{"title":"Fast State Restoration in LLM Serving with HCache Shiwei Gao","url":"https://chenyoumin1993.github.io/papers/eurosys25-hcache.pdf"},{"title":"Caching and Reuse Optimizations","url":"https://www.aussieai.com/research/caching"},{"title":"Don’t Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs","url":"https://arxiv.org/html/2604.04722v1"},{"title":"© 2025 Akshat Sharma - IDEALS - University of Illinois","url":"https://www.ideals.illinois.edu/items/136217/bitstreams/445287/data.pdf"},{"title":"ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference | OpenReview","url":"https://openreview.net/forum?id=20JDhbJqn3"},{"title":"KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/html/2603.20397v1"},{"title":"Published as a conference paper at ICLR 2026 KV CACHE TRANSFORM CODING","url":"https://openreview.net/pdf/1cef9774f0f0cf7bb9e4b167882e3ad3ef8cde16.pdf"}]

Based on the web search results, I found several relevant papers and research on KV cache compression with bit allocation and token selection from 2025-2026:

## Key Research Findings

Recent work has explored KV cache compression through sparse attention approaches that store the entire KV cache but dynamically load a small portion during decoding. 

Quantization methods compress KV cache by reducing bit width, with examples including KVQuant (which achieves 3-bit quantization) and PolarQuant (which encodes KV caches with quantized radii and angles).

### Restoration-Aware and Compression-Aware Methods

Q-Hitter presents a sparsity-aware quantized design where tokens are selected based on both attention importance and quantization robustness, identifying tokens that are both semantically important and amenable to quantization.

The system computes two metrics: attention score (reflecting the token's importance for future predictions) and quantization error (showing information loss in low-bit representation), which are combined into a unified score.

### Bit Allocation Approaches

Recent work employs dynamic programming algorithms that produce optimal bit allocation for each principal component of KV cache representations.

### Mixed-Dimension Budget Allocation

One paper approaches token eviction as a special case of dimensionality reduction where each token is compressed to either 0 or full dimension, and raises the question of whether dimensions can be allocated to tokens at a more granular level to maximize information retention under a fixed budget.

The search results show active research in 2025-2026 on combining compression awareness with token selection strategies for efficient KV cache management.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a98f9d24-6e9a-4939-b97c-e01599d25d97",
  "isSidechain": false,
  "promptId": "b368710b-e415-41f5-a2d9-b7e249a1c17c",
  "type": "user",
  "uuid": "becd8057-dd6c-45c6-b5a7-19a4f8d6db4f",
  "toolUseResult": {
    "query": "\"restoration-aware\" OR \"compression-aware restoration\" KV cache bit allocation token selection 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SWKszkFUr8bF3vvUW6Meyr",
        "content": [
          {
            "title": "Beyond Token Eviction: Mixed-Dimension Budget Allocation for Efficient KV Cache Compression",
            "url": "https://arxiv.org/html/2603.20616"
          },
          {
            "title": "Optimizing Key-Value Cache Compression in Long-context ...",
            "url": "https://aclanthology.org/2025.acl-long.529.pdf"
          },
          {
            "title": "GitHub - TreeAI-Lab/Awesome-KV-Cache-Management: This repository serves as a comprehensive survey of LLM development, featuring numerous research papers along with their corresponding code links. · GitHub",
            "url": "https://github.com/TreeAI-Lab/Awesome-KV-Cache-Management"
          },
          {
            "title": "Fast State Restoration in LLM Serving with HCache Shiwei Gao",
            "url": "https://chenyoumin1993.github.io/papers/eurosys25-hcache.pdf"
          },
          {
            "title": "Caching and Reuse Optimizations",
            "url": "https://www.aussieai.com/research/caching"
          },
          {
            "title": "Don’t Waste Bits! Adaptive KV-Cache Quantization for Lightweight On-Device LLMs",
            "url": "https://arxiv.org/html/2604.04722v1"
          },
          {
            "title": "© 2025 Akshat Sharma - IDEALS - University of Illinois",
            "url": "https://www.ideals.illinois.edu/items/136217/bitstreams/445287/data.pdf"
          },
          {
            "title": "ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference | OpenReview",
            "url": "https://openreview.net/forum?id=20JDhbJqn3"
          },
          {
            "title": "KV Cache Optimization Strategies for Scalable and Efficient LLM Inference",
            "url": "https://arxiv.org/html/2603.20397v1"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 KV CACHE TRANSFORM CODING",
            "url": "https://openreview.net/pdf/1cef9774f0f0cf7bb9e4b167882e3ad3ef8cde16.pdf"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers and research on KV cache compression with bit allocation and token selection from 2025-2026:\n\n## Key Research Findings\n\nRecent work has explored KV cache compression through sparse attention approaches that store the entire KV cache but dynamically load a small portion during decoding. \n\nQuantization methods compress KV cache by reducing bit width, with examples including KVQuant (which achieves 3-bit quantization) and PolarQuant (which encodes KV caches with quantized radii and angles).\n\n### Restoration-Aware and Compression-Aware Methods\n\nQ-Hitter presents a sparsity-aware quantized design where tokens are selected based on both attention importance and quantization robustness, identifying tokens that are both semantically important and amenable to quantization.\n\nThe system computes two metrics: attention score (reflecting the token's importance for future predictions) and quantization error (showing information loss in low-bit representation), which are combined into a unified score.\n\n### Bit Allocation Approaches\n\nRecent work employs dynamic programming algorithms that produce optimal bit allocation for each principal component of KV cache representations.\n\n### Mixed-Dimension Budget Allocation\n\nOne paper approaches token eviction as a special case of dimensionality reduction where each token is compressed to either 0 or full dimension, and raises the question of whether dimensions can be allocated to tokens at a more granular level to maximize information retention under a fixed budget.\n\nThe search results show active research in 2025-2026 on combining compression awareness with token selection strategies for efficient KV cache management."
    ],
    "durationSeconds": 7.760306750999996
  },
  "sourceToolAssistantUUID": "a98f9d24-6e9a-4939-b97c-e01599d25d97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-12T00:05:52.395Z_

<details><summary>Logged reasoning block</summary>

```text
The search results didn't reveal any work that directly jointly optimizes bit allocation with restoration token selection in the chunk-caching setting. Good — the novelty claim holds.

Let me also check the Q-Hitter reference more carefully — it mentions combining attention score with quantization error for token selection, which could be somewhat related to CEGR.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "becd8057-dd6c-45c6-b5a7-19a4f8d6db4f",
  "isSidechain": false,
  "requestId": "req_011CawhTeMAgDfokYMD8d9Zu",
  "type": "assistant",
  "uuid": "a64f405c-c0a0-41f0-bb1f-9333d939e550",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018saT9J3VXxuizU8oMhpz3p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1006,
      "cache_read_input_tokens": 36064,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1006,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 36064,
          "cache_creation_input_tokens": 1006,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1006
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-12T00:05:52.810Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S5H4JcewKdrDdr5TRnEBSw`</summary>

```json
{
  "query": "Q-Hitter sparsity-aware quantization KV cache token selection attention quantization error"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a64f405c-c0a0-41f0-bb1f-9333d939e550",
  "isSidechain": false,
  "requestId": "req_011CawhTeMAgDfokYMD8d9Zu",
  "type": "assistant",
  "uuid": "a4d515fb-b173-49a4-a672-4cdd5c53079b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018saT9J3VXxuizU8oMhpz3p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1006,
      "cache_read_input_tokens": 36064,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1006,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 36064,
          "cache_creation_input_tokens": 1006,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1006
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-12T00:05:59.397Z_

<details><summary>↩ Tool result · `toolu_01S5H4JcewKdrDdr5TRnEBSw`</summary>

```text
Web search results for query: "Q-Hitter sparsity-aware quantization KV cache token selection attention quantization error"

Links: [{"title":"Q-Hitter: A Better Token Oracle for Efficient LLM Inference ...","url":"https://proceedings.mlsys.org/paper_files/paper/2024/file/bbb7506579431a85861a05fff048d3e1-Paper-Conference.pdf"},{"title":"KV Cache Optimization Strategies for Scalable and Efficient LLM Inference","url":"https://arxiv.org/html/2603.20397v1"},{"title":"Q-Hitter: A Better Token Oracle for Efficient LLM Inference via Sparse-Quantized KV Cache","url":"https://proceedings.mlsys.org/paper_files/paper/2024/hash/bbb7506579431a85861a05fff048d3e1-Abstract-Conference.html"},{"title":"FIER: Fine-Grained and Efficient KV Cache Retrieval for ...","url":"https://aclanthology.org/2025.findings-emnlp.515.pdf"},{"title":"1 Introduction","url":"https://arxiv.org/html/2411.18077v1"},{"title":"A Survey on Large Language Model Acceleration based on KV Cache Management","url":"https://arxiv.org/html/2412.19442v3"},{"title":"Towards 10 Million Context Length LLM Inference with KV ...","url":"https://www.stat.berkeley.edu/~mmahoney/pubs/neurips-2024-kvquant.pdf"},{"title":"LogQuant: Log-Distributed 2-Bit Quantization of KV Cache with Superior Accuracy Preservation","url":"https://arxiv.org/html/2503.19950v1"},{"title":"QuantSpec: Self-Speculative Decoding with Hierarchical Quantized KV Cache","url":"https://www.stat.berkeley.edu/~mmahoney/pubs/9485_QuantSpec_Self_Speculativ.pdf"},{"title":"Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost","url":"https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"}]

Based on the search results, here's what I found about Q-Hitter and its approach to sparsity-aware quantization for KV cache optimization:

## Q-Hitter Overview

Q-Hitter is a quantization-aware KV cache sparsification framework that simultaneously takes "quantization friendliness" and accumulated attention scores into account.

## Key Problem It Addresses

KV cache quantization results in significant accuracy degradation in the Heavy-Hitter selection process, and tokens identified by H2O (a prior method) do not consistently exhibit compatibility with quantization. A simplistic amalgamation of sparsification and quantization can yield sub-optimal performance.

## Token Selection Mechanism

Q-Hitter features a sparsity-aware quantized design where tokens are selected based on both attention importance and quantization robustness, identifying tokens that are both semantically important and amenable to quantization. Q-Hitter selects the top-K tokens according to their combined score and stores only their KV entries in quantized form, with lower-scoring tokens discarded.

## Performance Results

Q-Hitter is capable of preserving the performance of the full model while applying 4-bit quantization, resulting in an overall compression ratio ranging from 8× to 20× across various tasks. Q-Hitter achieves up to a 20× reduction in memory usage and up to 33× throughput improvements compared with various baselines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4d515fb-b173-49a4-a672-4cdd5c53079b",
  "isSidechain": false,
  "promptId": "b368710b-e415-41f5-a2d9-b7e249a1c17c",
  "type": "user",
  "uuid": "4149340d-4258-414a-a607-29662394dffd",
  "toolUseResult": {
    "query": "Q-Hitter sparsity-aware quantization KV cache token selection attention quantization error",
    "results": [
      {
        "tool_use_id": "srvtoolu_01H5uLxfWeS7m3UjU6N5ssos",
        "content": [
          {
            "title": "Q-Hitter: A Better Token Oracle for Efficient LLM Inference ...",
            "url": "https://proceedings.mlsys.org/paper_files/paper/2024/file/bbb7506579431a85861a05fff048d3e1-Paper-Conference.pdf"
          },
          {
            "title": "KV Cache Optimization Strategies for Scalable and Efficient LLM Inference",
            "url": "https://arxiv.org/html/2603.20397v1"
          },
          {
            "title": "Q-Hitter: A Better Token Oracle for Efficient LLM Inference via Sparse-Quantized KV Cache",
            "url": "https://proceedings.mlsys.org/paper_files/paper/2024/hash/bbb7506579431a85861a05fff048d3e1-Abstract-Conference.html"
          },
          {
            "title": "FIER: Fine-Grained and Efficient KV Cache Retrieval for ...",
            "url": "https://aclanthology.org/2025.findings-emnlp.515.pdf"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2411.18077v1"
          },
          {
            "title": "A Survey on Large Language Model Acceleration based on KV Cache Management",
            "url": "https://arxiv.org/html/2412.19442v3"
          },
          {
            "title": "Towards 10 Million Context Length LLM Inference with KV ...",
            "url": "https://www.stat.berkeley.edu/~mmahoney/pubs/neurips-2024-kvquant.pdf"
          },
          {
            "title": "LogQuant: Log-Distributed 2-Bit Quantization of KV Cache with Superior Accuracy Preservation",
            "url": "https://arxiv.org/html/2503.19950v1"
          },
          {
            "title": "QuantSpec: Self-Speculative Decoding with Hierarchical Quantized KV Cache",
            "url": "https://www.stat.berkeley.edu/~mmahoney/pubs/9485_QuantSpec_Self_Speculativ.pdf"
          },
          {
            "title": "Top 10 KV Cache Compression Techniques for LLM Inference: Reducing Memory Overhead Across Eviction, Quantization, and Low-Rank Methods - MarkTechPost",
            "url": "https://www.marktechpost.com/2026/04/29/top-10-kv-cache-compression-techniques-for-llm-inference-reducing-memory-overhead-across-eviction-quantization-and-low-rank-methods/"
          }
        ]
      },
      "Based on the search results, here's what I found about Q-Hitter and its approach to sparsity-aware quantization for KV cache optimization:\n\n## Q-Hitter Overview\n\nQ-Hitter is a quantization-aware KV cache sparsification framework that simultaneously takes \"quantization friendliness\" and accumulated attention scores into account.\n\n## Key Problem It Addresses\n\nKV cache quantization results in significant accuracy degradation in the Heavy-Hitter selection process, and tokens identified by H2O (a prior method) do not consistently exhibit compatibility with quantization. A simplistic amalgamation of sparsification and quantization can yield sub-optimal performance.\n\n## Token Selection Mechanism\n\nQ-Hitter features a sparsity-aware quantized design where tokens are selected based on both attention importance and quantization robustness, identifying tokens that are both semantically important and amenable to quantization. Q-Hitter selects the top-K tokens according to their combined score and stores only their KV entries in quantized form, with lower-scoring tokens discarded.\n\n## Performance Results\n\nQ-Hitter is capable of preserving the performance of the full model while applying 4-bit quantization, resulting in an overall compression ratio ranging from 8× to 20× across various tasks. Q-Hitter achieves up to a 20× reduction in memory usage and up to 33× throughput improvements compared with various baselines."
    ],
    "durationSeconds": 6.583272353999986
  },
  "sourceToolAssistantUUID": "a4d515fb-b173-49a4-a672-4cdd5c53079b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"CompressLink: Co-Optimizing Compression and Restoration for Position-I…",
  "leafUuid": "4149340d-4258-414a-a607-29662394dffd",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Co-optimize KV compression and restoration for RAG chunk caching",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c"
}
```

---

### Assistant

_source line 47 · 2026-05-12T00:06:27.033Z_

<details><summary>Logged reasoning block</summary>

```text
Q-Hitter is from MLSys 2024 — it combines sparsification (eviction) with quantization, selecting tokens based on both attention importance AND quantization friendliness. This is somewhat related to CEGR's idea of combining query relevance with compression error. However:

1. Q-Hitter selects tokens to *keep* (eviction), not tokens to *recompute* (restoration)
2. Q-Hitter uses "quantization friendliness" (how well a token can be quantized) to decide which tokens to keep, not "compression error" (how much a token was actually damaged by compression) to decide which to restore


3. Q-Hitter doesn't operate in the chunk-caching/PIC setting
4. Q-Hitter's goal is to find tokens that are both important AND easy to quantize (complementary signals for keeping), while CEGR's goal is to find tokens that are both query-relevant AND damaged by compression (complementary signals for restoring)

So Q-Hitter is related work that also considers the interaction between compression quality and token importance, but the key difference is directional: Q-Hitter optimizes *what to keep and quantize*, while CEGR optimizes *what to restore after compression*. I should mention it as related work and clearly differentiate these approaches.

Now I need to work through the revision checklist. First, I'll add EVICPRESS, QCFuse, and CacheFlow to the related work section and references. Then I need to address the HeadQ challenge more carefully — the core issue is that storage-space MSE might not perfectly correlate with score-space error, but within a single chunk using the same quantization scheme and head, that correlation should be much tighter than across different schemes. I can propose a score-space variant as an enhanced option and add an ablation comparing embedding-space versus score-space error metrics for CEGR. I also need to revise the timeline to allocate 2 days for MEPIC and compression evaluation while overlapping with paper writing. Finally, I should acknowledge the implementation risk with KVTC — if the 20x compression target isn't achievable, I have a fallback to 4-8x. with query null-spaces. So I need to explicitly state the relative ranking argument, propose a score-space variant using Fisher weighting on the PCA components derived from the query basis, and add an ablation comparing embedding-space versus score-space approaches. For the score-space variant, I'll weight each PCA component's quantization error by its Fisher information rather than treating all components equally, keeping the computation tractable.

Writing the revised JSON...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4149340d-4258-414a-a607-29662394dffd",
  "isSidechain": false,
  "requestId": "req_011CawhUbqdrgGmsvgfin174",
  "type": "assistant",
  "uuid": "e3d83b35-1578-4c66-a9dc-0148fb35ff9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WiAuK9qCKkYq2RE8QXpzvH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1127,
      "cache_read_input_tokens": 37070,
      "output_tokens": 10670,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1127,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10670,
          "cache_read_input_tokens": 37070,
          "cache_creation_input_tokens": 1127,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1127
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-12T00:10:26.497Z_

Now I have all the information needed. Let me synthesize and produce the revised idea.

Key findings from research:
- **EVICPRESS**: Per-context granularity system-level decisions; clear differentiation from CompressLink's per-token algorithmic optimization
- **QCFuse**: Restoration competitor using semantic summary anchors + single critical layer; doesn't consider compression; criticizes ProphetKV's pipeline issues
- **CacheFlow**: Complementary execution optimization (3D parallelism for restoration scheduling)
- **HeadQ**: Table 2 shows MSE ranking is NOT monotonic with score-space error across different quantization schemes — but CEGR ranks tokens within the same scheme/head, which is a different (and more favorable) setting
- **Q-Hitter** (MLSys 2024): Also combines quantization quality with token importance, but for eviction (what to keep) rather than restoration (what to recompute)

Here is the revised idea:

```json
{
  "title": "CompressLink: Co-Optimizing Compression and Restoration for Position-Independent KV Cache Serving",
  "change_type": "minor",
  "core_problem": "Production RAG systems redundantly reprocess ~75% of retrieved chunks across queries (Cache-Craft, SIGMOD 2025). Position-independent caching (PIC) avoids this recomputation by storing chunk KVs without positional encodings for arbitrary-position reuse, and MEPIC (arXiv 2512.16822) further reduces HBM usage by 2x over EPIC via RoPE fusion and NoPE storage — yet cached KV states remain at full precision. A single Llama-3.1-8B instance caching 100K chunks at 512 tokens each requires ~3.2TB of KV storage. Meanwhile, KV compression methods like KVTC (ICLR 2026) achieve 8-20x storage reduction via PCA decorrelation + adaptive quantization + entropy coding. MEPIC explicitly identifies KV compression as an orthogonal direction 'that can be seamlessly combined with existing KV compression methods,' and KV Packet (arXiv:2604.13226) demonstrates compatibility of adapter-based PIC with eviction-based compression — but both treat compression and restoration as independent stages. EVICPRESS (arXiv:2512.14946) jointly optimizes compression and eviction decisions at the system/storage-tier level via a unified utility function, applying conservative compression to compression-sensitive contexts — but operates at per-context granularity (which contexts to compress and where to place them), not at per-token algorithmic granularity (how many bits per token, which tokens to restore). No prior work jointly optimizes the per-token compression bit allocation with per-token restoration selection in the chunk-caching setting — compression and restoration are universally treated as independent stages at the algorithmic level.",
  "opportunity": "MEPIC and KVTC share a structural element: both store KV without RoPE (NoPE format). MEPIC stores NoPE KVs for position-independent reuse with RoPE applied on-the-fly; KVTC removes RoPE before PCA compression. This alignment enables natural composition — KVTC compression applied to MEPIC's NoPE KV stores, with decompressed KVs fed into MEPIC's RoPE-fusion attention path. However, naive composition treats compression and restoration as independent stages, wasting compression bits on tokens that will be restored anyway and missing restoration opportunities on tokens with high compression error. We identify a bidirectional optimization opportunity: (1) At compression time, tokens in restorable positions (boundary tokens always recomputed by MEPIC, or tokens frequently selected by query-driven methods like ProphetKV or QCFuse) can tolerate aggressive compression since they will be replaced with fresh KVs — reallocating their bits to persistent tokens improves overall quality. (2) At restoration time, per-token compression error provides an orthogonal signal to query relevance for selecting which tokens to recompute — prioritizing tokens that are both query-relevant AND high-compression-error yields better quality per recomputed token. Additionally, KVTC's PCA basis calibrated on full-sequence KVs is suboptimal for independently-encoded chunks due to distribution mismatch (local vs. global attention sinks, absent cross-chunk attention), motivating chunk-aware recalibration. KV Packet (arXiv:2604.13226, Section 4.4) demonstrates that adapter-based PIC is robust to eviction-based compression (CUR, KVzap, LeverageScore, TOVA) at 10-50% retention rates — but this tests token-pruning compression, not transform coding (PCA + quantization + entropy coding) at 8-20x rates, and does not optimize the compression-restoration interface. EVICPRESS (arXiv:2512.14946) jointly decides whether to compress and where to place KV caches across storage tiers, but treats each context as an atomic unit and does not modify per-token bit allocation or inform per-token restoration selection. Our approach is the first to jointly optimize this interface at the algorithmic level.",
  "landscape": "Position-independent KV caching: MEPIC (arXiv 2512.16822, Dec 2025) achieves 2x HBM reduction over EPIC via NoPE KV storage, block-level recomputation (first block per chunk is request-specific), and RoPE fusion in fused attention kernels; integrated into vLLM + LMCache serving stack; evaluated on Mistral-7B-Instruct-v0.3 across SQuAD, NewsQA, NarrativeQA, emrQA. EPIC (ICML 2025) recomputes k≤32 boundary tokens via LegoLink. ProphetKV (arXiv:2602.02579, Feb 2026) introduces user-query-driven selective recomputation, achieving 96-101% accuracy at 20% recomputation ratio; evaluated on Llama-3.1-8B, Qwen2.5-14B, Qwen-3-14B. QCFuse (arXiv:2604.08585, April 2026) uses semantic summary anchors to enhance query representations and selectively recomputes query-related tokens using attention distributions from the most critical transformer layer (middle layers); achieves 40% latency reduction over existing cache fusion baselines; implemented on SGLang with sparse-attention Triton kernel; criticizes ProphetKV's all-layer concurrent evaluation as disruptive to pipeline scheduling. InfoFlow KV (arXiv:2603.05353, March 2026) casts selective recomputation as an information flow problem using prompt-conditioned attention norms under inference-consistent RoPE geometry; does not consider compression. KVLink (NeurIPS 2025) adjusts RoPE positions with trainable link tokens. Cache-Craft (SIGMOD 2025) stores chunk KVs without RoPE. CacheSlide (FAST 2026) uses learned weights for cross-position-aware reuse. CacheBlend (EuroSys 2025) selectively recomputes tokens based on output deviation. KV Packet (arXiv:2604.13226, April 2026) uses trainable soft-token adapters for recomputation-free PIC; Section 4.4 tests compatibility with 5 eviction-based compression methods (CUR, KVzap, LeverageScore, TOVA, random pruning) at 10-50% retention, claiming PIC 'natively bypasses bottlenecks' of compression-impaired recomputation — but tests token eviction, not transform coding, and does not optimize the compression-restoration interface. CacheFlow (arXiv:2604.25080, April 2026) rethinks cache restoration as a 3D-parallel execution problem (tokens × layers × GPUs) with a batch-aware two-pointer scheduler; reduces TTFT by 10-62%; complementary to CompressLink (execution optimization vs. selection optimization) — CompressLink's restored tokens would benefit from CacheFlow's parallel execution. FusionRAG (PACMMOD/SIGMOD 2026) embeds cross-chunk information offline. A systematic CLC study (arXiv 2603.20218, March 2026) compared 11 chunk-level caching strategies but did not examine compression. KV compression: KVTC (ICLR 2026) achieves 8-20x compression via PCA decorrelation + adaptive quantization + entropy coding, removing RoPE before PCA; maintains <1pp accuracy drop at 20x on most tasks; bit allocation via DP minimizes reconstruction MSE. RateQuant (arXiv:2605.06675, May 2026) applies rate-distortion theory for mixed-precision per-head quantization via reverse waterfilling, reducing KIVI's perplexity from 49.3 to 14.9 on Qwen3-8B at 2.5 bits with 1.6s calibration; principled bit allocation without PCA. eOptShrinkQ (arXiv:2605.02905, May 2026) achieves near-lossless compression via optimal spectral denoising + quantization, saving ~1 bit/entry. HeadQ (arXiv:2605.03562, May 2026) demonstrates that Fisher/score-space error predicts attention KL far better than raw key MSE, using null-space interventions to show that storage-space MSE can be misleading — a perturbation can have large storage error and zero attention damage; operates at per-head granularity with learned query-basis residual codes. DynaKV (arXiv:2603.04411, March 2026) provides per-token adaptive PCA rank via learned gating — requires fine-tuning (128M tokens), operates on full-sequence KVs. 'Quantization Dominates Rank Reduction' (arXiv:2604.11501, April 2026) shows quantization outperforms dimension-discarding PCA projection but tests rank reduction, not decorrelation-before-quantization as KVTC uses. EVICPRESS (arXiv:2512.14946, Dec 2025, Microsoft Research) jointly optimizes KV cache compression and eviction via a unified utility function across storage tiers, applying conservative compression to compression-sensitive contexts — operates at per-context system-level granularity, not per-token bit allocation. Q-Hitter (MLSys 2024) combines quantization friendliness with attention importance for token selection in sparse-quantized KV cache, but optimizes what to keep (eviction), not what to restore (recomputation), and does not operate in the chunk-caching setting. CacheGen (SIGCOMM 2024) achieves 3.5-4.3x via tensor encoders. KVzip (NeurIPS 2025 Oral) provides 3-4x eviction-based compression. Joint Encoding of KV-Cache Blocks (Jan 2026) fuses similar blocks achieving 4.38x. No prior work jointly optimizes per-token KV compression bit allocation with per-token selective restoration token selection in the chunk-caching setting — compression and restoration are universally treated as independent stages at the algorithmic level.",
  "approach": "We propose CompressLink, a framework that co-optimizes KV compression and quality restoration for position-independent chunk caching, built on the shared NoPE representation of MEPIC and KVTC. CompressLink introduces two novel algorithms — Restoration-Aware Bit Allocation (RABA) and Compression-Error-Guided Restoration (CEGR) — that jointly optimize the compression-restoration pipeline, plus chunk-aware PCA calibration as a supporting technique. **Offline Compression Pipeline:** Each document chunk is independently encoded through the LLM; MEPIC stores the resulting KV caches in NoPE format. Before KVTC compression, PCA bases are calibrated on independently-encoded chunk KVs (matching inference-time distribution, addressing the calibration mismatch from full-sequence KVs). RABA then modifies KVTC's DP-based bit allocation: each token position is assigned a restoration probability p_r(t) based on positional priors — boundary tokens (first block per chunk, always recomputed by MEPIC) get p_r ≈ 1.0; tokens frequently selected across calibration queries by ProphetKV-style scoring get intermediate p_r; remaining tokens get p_r ≈ 0. The DP objective is modified from minimizing total reconstruction MSE to minimizing restoration-weighted MSE: sum over tokens t of (1 - p_r(t)) * MSE(t), so that bits are reallocated from high-restoration-probability tokens (whose compressed values will be overwritten) to persistent tokens (whose compressed values must survive). At 20% recomputation ratio, this effectively concentrates the full bit budget on 80% of tokens, improving quality where it matters. Compressed KVs (PCA transform → RABA-allocated quantization → entropy coding) are stored in LMCache's persistence layer. **Online Restoration Pipeline:** Retrieved chunks' compressed KVs are decompressed (entropy decode → dequantize → PCA inverse). CEGR computes per-token compression error estimates from decompression metadata. The default variant (CEGR-MSE) estimates error analytically in embedding space: for each token, error_c(t) = sum over PCA components j of (Δ_j² / 12) where Δ_j is the quantization step size for component j at the allocated bit width — this requires zero additional forward passes, only the bit allocation metadata stored alongside compressed KVs. We additionally propose an enhanced variant (CEGR-Score) motivated by HeadQ's finding that storage-space MSE is a poor proxy for model-visible distortion. CEGR-Score weights PCA components by their Fisher-information contribution to attention score space: error_c^score(t) = sum over components j of F_j * (Δ_j² / 12), where F_j is the Fisher weight of component j estimated during offline calibration from query-key score variance. This adds negligible cost (F_j is precomputed per-head and stored with the PCA basis). We note that HeadQ's counterexamples (Table 2) compare different quantization schemes; CEGR ranks tokens within the same head under the same quantization scheme, where embedding-space error ranking is more likely to correlate with score-space ranking — but CEGR-Score provides a principled hedge against null-space misalignment. CEGR then combines the compression error signal with a query relevance signal r_q(t) obtained from a lightweight attention probe (single-layer attention of the query against decompressed keys, following ProphetKV's first-pass scoring or QCFuse's critical-layer approach). The joint restoration score is: score(t) = r_q(t) * error_c(t)^β, where β controls the compression-error sensitivity. Tokens with highest joint scores are selected for recomputation within the budget. The key insight: a query-relevant token with low compression error needs no recomputation (compression preserved it); a high-error token irrelevant to the query wastes recomputation budget. Only tokens that are both query-relevant AND high-error benefit maximally from recomputation. MEPIC's fused RoPE-attention kernel applies positional encodings on-the-fly during final attention computation over the mix of recomputed and decompressed KVs. **Joint Optimization Loop:** RABA and CEGR share the restoration probability model — RABA's p_r(t) at compression time is calibrated to match CEGR's empirical restoration rate at inference time. During calibration, we run CEGR on calibration queries to estimate per-position restoration frequencies, then feed these back into RABA's DP allocation. This creates a consistent compression-restoration contract: positions that CEGR frequently restores are precisely those where RABA saves bits. **Contributions:** (1) RABA — a novel restoration-aware bit allocation algorithm that extends rate-distortion-optimal quantization (cf. RateQuant's reverse waterfilling, KVTC's DP) with position-dependent restoration weights, provably reducing effective MSE on persistent tokens at matched total bit budgets. Differentiation from RateQuant: RateQuant allocates across heads, RABA allocates across token positions within each head; RateQuant is restoration-unaware. Differentiation from DynaKV: DynaKV allocates per-token PCA rank via learned gating (requires fine-tuning), RABA allocates per-token bit budget via restoration probability (training-free, calibration only). Differentiation from EVICPRESS: EVICPRESS jointly optimizes compression and placement at per-context system-level granularity; RABA operates at per-token algorithmic-level granularity within the compression codec. (2) CEGR — a novel compression-error-guided restoration algorithm that augments query-relevance-based token selection with compression error, available at zero additional compute cost from decompression metadata. The CEGR-Score variant further aligns the error metric with model-visible score-space distortion via Fisher weighting, addressing HeadQ's critique of storage-space MSE. Differentiation from ProphetKV: ProphetKV selects on query relevance alone; CEGR adds the compression error dimension. Differentiation from QCFuse: QCFuse uses semantic summary anchors and critical-layer attention for query-centric selection but is compression-unaware; CEGR adds the compression error signal to any query-relevance method. Differentiation from CacheBlend: CacheBlend uses output deviation (requires early-layer forward passes); CEGR uses analytical error estimates (zero forward passes). Differentiation from InfoFlow KV: InfoFlow KV uses attention-norm for information flow; CEGR uses compression error — orthogonal signals. Differentiation from Q-Hitter: Q-Hitter combines quantization friendliness with attention importance for eviction (what to keep); CEGR combines compression error with query relevance for restoration (what to recompute after compression). (3) A joint optimization loop where RABA and CEGR share a restoration probability model — CEGR's empirical restoration frequencies on calibration queries feed back to RABA's bit allocation weights, creating a consistent compression-restoration contract. Additionally, chunk-aware PCA calibration addresses the distribution mismatch between full-sequence and independently-encoded chunk KVs (a supporting technique, not a main contribution). **Evaluation:** Primary model: Llama-3.1-8B-Instruct (full benchmark suite); secondary: Qwen2.5-7B-Instruct (perplexity + 2 RAG benchmarks subset). RAG benchmarks: NaturalQuestions, HotpotQA, MuSiQue. Long-context: LongBench, RULER. General quality: WikiText perplexity, C4 perplexity, MT-Bench. Capability: MMLU, HumanEval. Key ablation axes: (a) compression ratio (4x, 8x, 16x via KVTC bit budget; 20x included if achievable from reimplementation, otherwise noted as future work), (b) RABA vs. standard KVTC bit allocation (matched total bits), (c) CEGR-MSE vs. CEGR-Score vs. ProphetKV-only vs. QCFuse-only vs. CacheBlend-only restoration (matched recomputation budget), (d) RABA+CEGR joint vs. each alone, (e) chunk-aware vs. full-sequence PCA calibration, (f) pure quantization baselines (RateQuant with reverse waterfilling, INT4/FP4 without PCA), (g) recomputation ratio (3%, 10%, 20%), (h) chunk size (256, 512, 1024 tokens), (i) embedding-space vs. score-space compression error for CEGR (CEGR-MSE vs. CEGR-Score ablation). Baselines: (i) uncompressed MEPIC, (ii) naive MEPIC+KVTC (independent stages, full-sequence PCA), (iii) MEPIC+RateQuant (principled pure quantization without PCA), (iv) MEPIC+KVTC with chunk-aware calibration but no RABA/CEGR. Targets: 8-16x storage reduction with <2% quality degradation vs. uncompressed MEPIC at 20% recomputation budget. Wall-clock throughput measured on H100.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~180h H100-80GB (MEPIC functional reimplementation + NoPE storage: ~6h; PCA calibration + chunk-aware recalibration: ~4h; KVTC pipeline from paper (PCA + DP quantization + nvCOMP DEFLATE): ~8h; RABA implementation and DP modification: ~3h compute, ~1 day engineering; CEGR implementation (MSE + Score variants) and joint scoring: ~3h compute, ~1 day engineering; MEPIC baselines across all benchmarks: ~20h; RABA+CEGR pipeline across configs: ~45h; RateQuant pure quantization baseline: ~12h; RABA vs standard allocation ablation: ~15h; CEGR-MSE vs CEGR-Score vs ProphetKV-only ablation: ~18h; joint optimization loop calibration: ~8h; additional benchmarks (Qwen subset): ~10h; chunk size ablation: ~18h; buffer for debugging: ~10h)",
      "gpu_utilization": "~40-50% effective utilization; GPU idles during RABA DP modification, CEGR integration with ProphetKV scoring, and joint calibration loop engineering",
      "timeline": "18 days (days 1-2: implement MEPIC functional reimplementation — NoPE KV storage, RoPE-on-query-only attention, block-level recomputation logic; non-optimized but functionally correct; days 3-4: implement KVTC compression pipeline from paper description — PCA + adaptive DP quantization + DEFLATE via nvCOMP; integrate as LMCache storage hooks; validate compression ratios at 4-8x (see risk note on 20x); days 5-6: implement chunk-aware PCA calibration, validate reconstruction error improvement; days 7-9: implement RABA — modify KVTC's DP to incorporate restoration probability weights, calibrate p_r(t) from MEPIC boundary positions; days 10-12: implement CEGR — both MSE and Score variants; analytical compression error estimation from bit allocation metadata; Fisher-weighted variant using calibration query basis; joint scoring with query relevance probe; days 13-14: joint optimization loop — run CEGR on calibration queries, feed restoration frequencies back to RABA; days 15-16: full evaluation on Llama-3.1-8B + Qwen2.5-7B subset (perplexity + NQ + HotpotQA); days 15-18: paper writing overlapped with late evaluation runs)",
      "team": "1 researcher with systems/ML experience",
      "estimated_gpu_cost": "$540 (180h × ~$3.00/hr H100-80GB)"
    },
    "human_in_loop": {
      "gpu_hours": "~200h H100-80GB (agent handles benchmark scripting and ablation grids; human focuses on RABA DP formulation and CEGR scoring design)",
      "gpu_utilization": "~60-70% effective utilization; agent runs experiments continuously while human reviews algorithm correctness and theoretical analysis",
      "timeline": "16 days (days 1-2: human designs RABA DP modification and CEGR joint scoring (MSE + Score variants); agent scaffolds MEPIC functional reimplementation + KVTC compression from paper description + LMCache hooks; days 3-4: agent implements chunk-aware calibration; human validates PCA basis quality; days 5-7: agent implements RABA; human validates DP correctness; days 8-10: agent implements CEGR (both variants) + joint optimization loop; human reviews scoring function design and Fisher weighting; days 11-14: agent runs full evaluation grid (Llama full + Qwen subset); human analyzes results; days 13-16: paper writing with agent assistance, overlapped with late eval)",
      "team": "1 researcher, ~2h/day for algorithm design decisions and theoretical analysis",
      "claude_api_cost": "$100-180 (~1000-1800 Opus turns for code integration, experiment scripting, and result analysis)",
      "estimated_gpu_cost": "$600 (200h × ~$3.00/hr H100-80GB)",
      "risk_note": "KVTC is implemented from the ICLR paper description (PCA + DP-based adaptive quantization + DEFLATE) rather than relying on the third-party OnlyTerp/kvtc repo (which achieves only 6-9x vs. paper's 20x). If paper-level 20x compression is not achievable within the timeline, we will evaluate at 4-8x (achievable with standard PCA + uniform quantization + zlib, confirmed by the OnlyTerp implementation) and note higher compression ratios as future work contingent on a faithful reimplementation or official code release. PCA and DP are standard algorithms; nvCOMP provides GPU-accelerated DEFLATE. The RABA DP modification is a straightforward extension (adding position-dependent weights to the MSE objective). CEGR's analytical error estimation is computable from stored bit allocation metadata; the Fisher-weighted variant requires a one-time calibration pass to estimate per-component score-space weights. MEPIC reimplementation (functional, non-optimized) budgets 2 days for NoPE storage + RoPE-on-query attention + block-level recomputation — the fused attention kernel is not reimplemented; we use standard attention with explicit RoPE application, accepting ~20% slower attention but functionally equivalent output. ProphetKV's query-guided token selection requires implementing its dual-stage attention scoring, which may add ~2 days engineering."
    },
    "auto_research": {
      "gpu_hours": "~320h H100-80GB (exhaustive grid over compression ratios × RABA vs standard × CEGR-MSE vs CEGR-Score vs ProphetKV × joint vs individual × RateQuant baselines × two models × chunk sizes × recomputation ratios; near-zero idle)",
      "gpu_utilization": "~85-90% effective utilization; agent pipelines experiments continuously",
      "timeline": "10-14 days with 2 H100 GPUs (single GPU: 16-18 days)",
      "team": "0 (initial setup: ~6h to implement MEPIC functional reimplementation, KVTC pipeline from paper, integrate RABA DP modification, and set up CEGR scoring)",
      "claude_api_cost": "$180-350 (~1800-3500 Opus turns for implementation, debugging, and experiment orchestration)",
      "estimated_gpu_cost": "$960 (320h × ~$3.00/hr H100-80GB)",
      "speed_bottleneck": "Implementing KVTC from the paper description (PCA decorrelation + DP bit allocation + nvCOMP entropy coding) and integrating RABA's restoration-weighted DP — agent can handle the standard components but may need human guidance on the DP cost function modification for restoration weights. MEPIC functional reimplementation adds ~1 day to the critical path.",
      "risk_note": "RABA's DP modification is algorithmically straightforward (adding multiplicative weights to the MSE terms), and CEGR's analytical error estimation is a closed-form computation. The Fisher-weighted CEGR-Score variant adds minimal complexity (one calibration pass for F_j weights per head). If paper-level 20x KVTC compression is not achievable, evaluation proceeds at 4-8x with 20x noted as future work. The joint calibration loop (running CEGR on calibration queries to estimate per-position restoration frequencies for RABA) adds ~1 day of engineering but is conceptually simple. Fallback: if joint optimization is infeasible in the timeline, RABA and CEGR independently are each sufficient algorithmic contributions."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026)"
  ],
  "level": "solid",
  "key_references": [
    "MEPIC: Memory Efficient Position Independent Caching for LLM Serving (arXiv:2512.16822, Dec 2025)",
    "EPIC: Efficient Position-Independent Caching for Serving Large Language Models (ICML 2025)",
    "ProphetKV: User-Query-Driven Selective Recomputation for Efficient KV Cache Reuse in RAG (arXiv:2602.02579, Feb 2026)",
    "KV Cache Transform Coding for Compact Storage in LLM Inference (KVTC, ICLR 2026)",
    "KV Packet: Recomputation-Free Context-Independent KV Caching for LLMs (arXiv:2604.13226, April 2026)",
    "EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving (arXiv:2512.14946, Dec 2025)",
    "QCFuse: Query-Centric Cache Fusion for Efficient RAG Inference (arXiv:2604.08585, April 2026)",
    "CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration (arXiv:2604.25080, April 2026)",
    "RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory (arXiv:2605.06675, May 2026)",
    "eOptShrinkQ: Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization (arXiv:2605.02905, May 2026)",
    "HeadQ: Model-Visible Distortion and Score-Space Correction for KV-Cache Quantization (arXiv:2605.03562, May 2026)",
    "Quantization Dominates Rank Reduction for KV-Cache Compression (arXiv:2604.11501, Apr 2026)",
    "InfoFlow KV: Information-Flow-Aware KV Recomputation for Long Context (arXiv:2603.05353, March 2026)",
    "DynaKV: One Size Does Not Fit All — Token-Wise Adaptive Compression for KV Cache (arXiv:2603.04411, March 2026)",
    "Q-Hitter: A Better Token Oracle for Efficient LLM Inference via Sparse-Quantized KV Cache (MLSys 2024)",
    "KVLink: Accelerating Large Language Models via Efficient KV Cache Reuse (NeurIPS 2025)",
    "CacheGen: KV Cache Compression and Streaming for Fast Large Language Model Serving (SIGCOMM 2024)",
    "Cache-Craft: Managing Chunk-Caches for Efficient Retrieval-Augmented Generation (SIGMOD 2025)",
    "CacheBlend: Fast Large Language Model Serving for RAG with Cached Knowledge Fusion (EuroSys 2025)",
    "KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction (NeurIPS 2025 Oral)",
    "CacheSlide: Unlocking Cross Position-Aware KV Cache Reuse for Accelerating LLM Serving (FAST 2026)",
    "From Prefix Cache to Fusion RAG Cache: Accelerating LLM Inference in Retrieval-Augmented Generation (FusionRAG, PACMMOD/SIGMOD 2026)",
    "An Experimental Study of KV Cache Reuse Strategies in Chunk-Level Caching Systems (arXiv:2603.20218, March 2026)",
    "TurboRAG: Accelerating Retrieval-Augmented Generation with Precomputed KV Caches for Chunked Text (EMNLP 2025)",
    "Joint Encoding of KV-Cache Blocks for Scalable LLM Serving (arXiv, Jan 2026)",
    "LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference (arXiv:2510.09665)"
  ],
  "description": "We propose CompressLink, a framework that co-optimizes KV compression and quality restoration for position-independent chunk caching in RAG serving. MEPIC (arXiv 2512.16822) stores chunk KVs in NoPE format for position-independent reuse and identifies compression as an orthogonal direction; KVTC (ICLR 2026) achieves 8-20x compression via PCA + adaptive quantization + entropy coding, also operating on NoPE KVs. While KV Packet (arXiv:2604.13226, Section 4.4) demonstrates that adapter-based PIC is compatible with eviction-based compression at 10-50% retention rates, and EVICPRESS (arXiv:2512.14946) jointly optimizes compression and eviction at per-context system-level granularity, no work jointly optimizes the per-token compression-restoration interface — compression and restoration are universally treated as independent stages at the algorithmic level. We make three contributions: (1) Restoration-Aware Bit Allocation (RABA) — a novel algorithm that extends rate-distortion-optimal quantization with position-dependent restoration weights. RABA modifies KVTC's DP-based bit allocation so that tokens with high restoration probability (boundary tokens always recomputed by MEPIC, or frequently-restored tokens identified via calibration) receive fewer bits, and the saved budget is reallocated to persistent tokens. At 20% recomputation ratio, this concentrates the full bit budget on the 80% of tokens that must survive compression, reducing effective MSE on persistent tokens. Differentiated from RateQuant (arXiv:2605.06675), which allocates bits across heads but is restoration-unaware; from DynaKV (arXiv:2603.04411), which allocates per-token PCA rank via learned gating requiring fine-tuning; and from EVICPRESS, which operates at per-context system-level granularity rather than per-token bit allocation. (2) Compression-Error-Guided Restoration (CEGR) — a novel algorithm that augments query-relevance-based token selection with a compression error signal. The default variant (CEGR-MSE) estimates per-token error analytically from decompression metadata (quantization step sizes and PCA basis), requiring zero forward passes. An enhanced variant (CEGR-Score) weights PCA components by Fisher-information contributions to attention score space, addressing HeadQ's finding (arXiv:2605.03562) that storage-space MSE can mispredict model-visible distortion — though we note HeadQ's counterexamples compare across quantization schemes, while CEGR ranks tokens within the same scheme where embedding-space ranking is more likely to preserve score-space ordering. CEGR combines compression error with query relevance via multiplicative joint scoring: score(t) = r_q(t) * error_c(t)^β. The key insight: recomputation budget should prioritize tokens that are both query-relevant AND high-compression-error. Differentiated from ProphetKV (query-only selection), QCFuse (arXiv:2604.08585, semantic-anchor query-centric selection, compression-unaware), CacheBlend (requires forward passes for deviation), InfoFlow KV (attention-norm flow, compression-unaware), and Q-Hitter (MLSys 2024, combines quantization quality with importance for eviction, not restoration). (3) A joint optimization loop where RABA and CEGR share a restoration probability model — CEGR's empirical restoration frequencies on calibration queries feed back to RABA's bit allocation weights, creating a consistent compression-restoration contract. Additionally, chunk-aware PCA calibration addresses the distribution mismatch between full-sequence and independently-encoded chunk KVs (a supporting technique, not a main contribution). CacheFlow (arXiv:2604.25080) is complementary — its 3D-parallel restoration execution can accelerate CompressLink's recomputation phase. Evaluated on Llama-3.1-8B-Instruct (full suite) and Qwen2.5-7B-Instruct (subset) across NaturalQuestions, HotpotQA, MuSiQue, LongBench, RULER, WikiText perplexity, C4 perplexity, MT-Bench, MMLU, and HumanEval. Key ablations include CEGR-MSE vs. CEGR-Score (embedding-space vs. score-space error). Key baselines: uncompressed MEPIC, naive MEPIC+KVTC, MEPIC+RateQuant (principled pure quantization), and MEPIC+KVTC with chunk-aware calibration but without RABA/CEGR. KVTC is implemented from the ICLR paper description; if paper-level 20x compression is not achievable in the timeline, evaluation proceeds at 4-8x (confirmed achievable) with 20x noted as future work. Targets 8-16x storage reduction with <2% quality degradation vs. uncompressed MEPIC at 20% recomputation budget, with wall-clock throughput on H100.",
  "project_name": "distill_kv_rag_cache",
  "source": "web_research"
}
```

**Summary of changes (minor fix):**

1. **Added 3 missing references** — EVICPRESS, QCFuse, and CacheFlow are now cited and differentiated throughout core_problem, opportunity, landscape, approach, and description. EVICPRESS is differentiated as system-level per-context granularity vs. CompressLink's algorithmic per-token granularity. QCFuse is added as a restoration baseline/comparison alongside ProphetKV. CacheFlow is noted as complementary execution optimization. Also added Q-Hitter (MLSys 2024) as related work combining quantization quality with token importance for eviction.

2. **Addressed HeadQ challenge to CEGR** — Introduced two CEGR variants: CEGR-MSE (original embedding-space) and CEGR-Score (Fisher-weighted score-space). Explicitly stated the argument that HeadQ's counterexamples compare across quantization schemes while CEGR ranks within the same scheme/head. Added CEGR-MSE vs. CEGR-Score as an ablation axis (embedding-space vs. score-space error).

3. **Fixed timeline realism** — Budgeted 2 days for MEPIC functional reimplementation (non-optimized: NoPE storage + RoPE-on-query attention). Extended to 18 days (manual). Compressed evaluation: full benchmarks on Llama-3.1-8B only, Qwen2.5-7B on subset (perplexity + 2 RAG benchmarks). Paper writing overlapped with late evaluation (days 15-18).

4. **Acknowledged KVTC implementation risk explicitly** — Stated that if 20x compression is not achievable, evaluation proceeds at 4-8x (confirmed achievable by OnlyTerp code) with 20x noted as future work.

Sources:
- [EVICPRESS: Joint KV-Cache Compression and Eviction](https://arxiv.org/abs/2512.14946)
- [QCFuse: Query-Centric Cache Fusion for Efficient RAG Inference](https://arxiv.org/abs/2604.08585)
- [CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration](https://arxiv.org/abs/2604.25080)
- [HeadQ: Model-Visible Distortion and Score-Space Correction](https://arxiv.org/abs/2605.03562)
- [Q-Hitter: A Better Token Oracle for Efficient LLM Inference](https://proceedings.mlsys.org/paper_files/paper/2024/hash/bbb7506579431a85861a05fff048d3e1-Abstract-Conference.html)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3d83b35-1578-4c66-a9dc-0148fb35ff9d",
  "isSidechain": false,
  "requestId": "req_011CawhUbqdrgGmsvgfin174",
  "type": "assistant",
  "uuid": "088aea23-ff7e-46cc-91da-4c7831375fca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WiAuK9qCKkYq2RE8QXpzvH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1127,
      "cache_read_input_tokens": 37070,
      "output_tokens": 10670,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1127,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10670,
          "cache_read_input_tokens": 37070,
          "cache_creation_input_tokens": 1127,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1127
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Runtime record

_source line 49_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"CompressLink: Co-Optimizing Compression and Restoration for Position-I…",
  "leafUuid": "088aea23-ff7e-46cc-91da-4c7831375fca",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c"
}
```

---

### Runtime record

_source line 50_

```json
{
  "type": "ai-title",
  "aiTitle": "Co-optimize KV compression and restoration for RAG chunk caching",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"CompressLink: Co-Optimizing Compression and Restoration for Position-I…",
  "leafUuid": "088aea23-ff7e-46cc-91da-4c7831375fca",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "ai-title",
  "aiTitle": "Co-optimize KV compression and restoration for RAG chunk caching",
  "sessionId": "91be2f02-e30d-47e4-8888-aa49b5f1487c"
}
```

---
