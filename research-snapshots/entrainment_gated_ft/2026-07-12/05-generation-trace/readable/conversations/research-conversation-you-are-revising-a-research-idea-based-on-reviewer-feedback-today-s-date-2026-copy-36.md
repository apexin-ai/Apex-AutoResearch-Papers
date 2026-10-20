# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-10 (UTC).** ## Original idea { "tit

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/5510b0f6-9c67-4418-9360-5f12db91350f.jsonl`
- **Structured JSON:** [`f2944fc9e8e5313e1638.json`](../../sessions/f2/f2944fc9e8e5313e1638.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T20:10:16.340Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T20:10:16.340Z",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-10 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Variance-Bounded Head-Adaptive Decomposition for Self-Speculative Reasoning Decoding\",\n  \"core_problem\": \"Self-speculative decoding methods (SparseSpec, SpecAttn) select critical tokens for sparse draft attention by reusing verification-stage attention scores as a free oracle, but these scores become stale over γ draft steps. The attention prediction landscape has responded to this staleness problem in multiple ways—SFI (2026) reuses a fixed sparse support set and refreshes at semantic boundaries, GVR (2026) uses the previous step's Top-K as a temporal predictor, Expected Attention (2025) predicts future attention via Gaussian moment-generating functions—but ALL existing approaches treat attention heads uniformly during prediction. Ada-KV (NeurIPS 2025) proved via an L1 eviction loss upper bound (Theorem 3.3) that uniform head budget allocation is suboptimal, and HeadKV (ICLR 2025) demonstrated that per-head differential KV cache treatment can retain 1.5% of cache at 97% performance. Yet both operate on runtime cache retention budgets, not on the prediction strategy itself. Meanwhile, Urrutia et al. (2025) proved that positional and symbolic attention behaviors are mutually exclusive per head, and TriAttention (2026) showed ~85% of GQA heads have MRL R_h > 0.95 (concentrated query directions), meaning their attention scores are analytically predictable from RoPE structure alone. The remaining ~15% of content-dependent heads have high residual variance and require explicit tracking. No existing method provides per-head prediction error bounds that connect MRL concentration to attention score staleness, nor differentiates heads by their intrinsic predictability for self-speculative scoring. Furthermore, the residual dynamics for content-dependent heads are poorly modeled: SparseSpec and EvoSparse assume temporally smooth degradation, but 'Beyond Exponential Decay' (2026) demonstrates that in LLM generation, errors concentrate at sparse decision points (~5-10% of tokens) rather than accumulating gradually—suggesting the commonly assumed exponential decay model is wrong.\",\n  \"opportunity\": \"We identify a theoretical gap that unifies and improves upon the fragmented attention prediction landscape. The key insight: TriAttention's MRL concentration metric directly bounds the per-head prediction error of any structural-only estimator, AND the tolerable prediction error depends on each head's Top-K attention gap—making the optimal head classification per-head adaptive, not a global threshold. Specifically, for head h with MRL R_h, the structural estimator Ŝ_struct(k,Δ) = E[q_f]^T R(Δ) k has mean-squared error bounded by O((1-R_h²)·σ²_q·||k||²/d). This bound, combined with a rank-swap analysis connecting MSE to Top-K selection quality via the per-head attention gap Δ_K(h), yields three consequences: (1) For structural heads where the bound is small relative to their attention gap, prediction is reliable at any draft distance—no staleness concern. (2) For content-dependent heads where the bound exceeds their attention gap tolerance, explicit residual tracking is necessary. (3) The per-head threshold θ_h emerges from an error-budget criterion that jointly considers MRL and attention gap, producing genuinely different classifications than a naive MRL percentile cutoff. This last point is critical: a peaked-attention head with moderate MRL (R=0.94, large Δ_K) may be reliably predicted structurally, while a flat-attention head with high MRL (R=0.96, small Δ_K) may require residual tracking. A naive global θ=0.95 misclassifies both. Ada-KV (NeurIPS 2025) proved uniform allocation is suboptimal but optimizes runtime cache budgets; our contribution operates upstream, optimizing which prediction strategy to deploy per head. HeadKV (ICLR 2025) differentiates heads via offline probe scores; our classification derives from architectural properties with a theoretical error bound. Combined with SFI's empirical finding that attention support is temporally stable within semantic segments, we can replace the unjustified exponential decay model with a segment-aware piecewise residual model that correctly captures the sparse, boundary-concentrated dynamics of content-dependent heads. No prior work connects MRL concentration to per-head attention prediction error bounds with gap-adaptive thresholds, nor exploits the resulting head-adaptive decomposition for self-speculative draft scoring.\",\n  \"landscape\": \"SparseSpec (Dec 2025, arXiv:2512.01278) achieves 2.13× throughput via PillarAttn self-speculation, reusing verification attention scores with k=8 stride; evaluated on Qwen3-1.7B/8B/14B (proof-of-concept codebase, not tested beyond 14B) with AIME/OlympiadBench/LiveCodeBench; code at github.com/sspec-project/SparseSpec. SpecAttn (Feb 2026, arXiv:2602.07223) improves to 2.81× with verification-guided sparse attention co-design. Both inherit the γ-staleness limitation, applying uniform stale scores across all heads. Slow-Fast Inference (SFI, March 2026, arXiv:2603.12038) exploits temporal stability of attention support within semantic segments, achieving 14.4× throughput via event-driven sparse/dense alternation with Tmax=64 refresh budget; evaluated on Qwen3-0.6B/4B/30B/235B; treats all heads uniformly with no per-head error guarantees. Guess-Verify-Refine (GVR, April 2026, arXiv:2604.22312) uses previous step's Top-K as temporal prediction signal for Blackwell hardware, achieving 1.88× speedup in sparse Top-K selection; targets DeepSeek-V3 at 100K context; again, uniform across heads. Expected Attention (Oct 2025, arXiv:2510.00636, under review ICLR 2026) predicts future attention via Gaussian moment-generating function over query distributions, with per-head adaptive compression; targets KV cache pruning, not self-speculative scoring; evaluated on Llama3.1-8B/Qwen3-8B with LongBench/RULER. AttentionPredictor (Feb 2025, arXiv:2502.04077, NeurIPS 2025) learns a lightweight convolution model for next-token attention prediction, achieving 13× KV compression; requires training, unlike our analytical approach. HeadKV (ICLR 2025, arXiv:2410.19258) performs head-level KV cache compression using offline probe-based importance scores (needle-in-a-haystack tests) for retrieval vs. reasoning heads, retaining 1.5% of KV cache at 97% performance on Llama-3-8B/Mistral-7B; key precedent for per-head differential treatment. Difference from ours: HeadKV uses task-specific probe scores fixed across inputs targeting KV retention budgets; DecompSpec uses architecture-intrinsic MRL classification with theoretical error bounds targeting scoring strategy selection. Ada-KV (NeurIPS 2025, arXiv:2407.11550) proves via L1 eviction loss upper bound (Theorem 3.3) that uniform head budget allocation is suboptimal, proposing global Top-B adaptive allocation; evaluated across 29 datasets (Ruler, LongBench). Ada-KV directly supports our premise that per-head treatment is necessary, but optimizes runtime eviction budgets, not prediction strategy. TriAttention (April 2026, arXiv:2604.04921) provides position-aware structural scoring via trigonometric series using fixed Q centers, achieving 2.5× throughput for KV compression; reports 84.7% of GQA heads and 96.6% of MLA heads have R>0.95; uses continuous concentration-based weighting (no hard classification threshold); evaluated on Qwen3-8B, Qwen2.5, Llama3; code at github.com/WeianMao/triattention. DuoAttention (ICLR 2025) pioneered retrieval/streaming head taxonomy for KV cache compression. LycheeDecode (ICLR 2026, arXiv:2602.04541) extends with HardKuma-based learned binary classification, 2.7× speedup at 128K. SeerAttention-R (2026, arXiv:2506.08889) uses learned gating for GQA-aligned sparse attention in reasoning, achieving near-lossless accuracy at 90% sparsity with 4K token budget; GQA alignment via linear projection is relevant to our GQA-aware classification. Self-Indexing KVCache (March 2026, arXiv:2603.14224, AAAI 2026) unifies compression and sparse retrieval via sign-based 1-bit VQ; treats prediction and compression jointly but uniformly across heads. Urrutia et al. (Nov 2025, arXiv:2511.11579) formally proved positional/symbolic mutual exclusivity per head. Beyond Exponential Decay (May 2026, arXiv:2505.24187) challenges exponential error accumulation—showing errors concentrate at sparse key tokens (~5-10%), motivating our segment-aware residual model. Gibson (Oct 2025, arXiv:2510.03315) decomposes attention into structural/content components on GPT2-Small. Flux Attention (April 2026, arXiv:2604.07394) identifies load imbalance from per-head dynamic sparsity—inapplicable to our setting where per-head routing is confined to the lightweight scoring phase. Component-Aware Self-Speculative Decoding (May 2026, arXiv:2605.01106) exploits SSM/attention heterogeneity. SpecKV (May 2026, arXiv:2605.02888) adaptively selects γ using confidence signals. EvoSparse (ACL 2026) addresses evolving token importance via cross-step accumulation. Linear Predictability of Attention Heads (March 2026, arXiv:2603.13314) shows inter-head QKV linear structure enables cache compression. No existing work provides per-head prediction error bounds connecting MRL to attention score staleness with gap-adaptive thresholds, nor applies head-adaptive decomposition with segment-aware residual tracking specifically for self-speculative draft token selection.\",\n  \"approach\": \"We propose DecompSpec, which provides variance-bounded head-adaptive attention prediction for self-speculative decoding, with four contributions:\\n\\n**Phase 0: Oracle Ceiling Analysis (Gating Experiment, ~3h on 1× H100).** Before the full experimental pipeline, we quantify the maximum possible improvement from head-selective decomposition. We run full-attention generation on 50 AIME25 problems with Qwen3-32B BF16, recording oracle attention scores at each step. Retrospectively, we compute Top-K (K=256) token selection under three scoring approaches: (a) uniform structural scoring (TriAttention for all heads), (b) head-selective oracle (structural for R_h>0.95 heads, oracle attention for the rest), and (c) SparseSpec stale reuse at γ=16. We measure Jaccard similarity with oracle Top-K, stratified by reasoning step boundaries vs. stable regions. The ceiling = Jaccard(b) − Jaccard(a) quantifies the maximum gain from decomposition. Decision gate: if ceiling > 3% Jaccard improvement, proceed to full implementation; if < 2%, reconsider scope. Additionally, we measure what fraction of token selection errors under uniform-structural scoring are attributable to the ~15% content-dependent heads—if these heads account for a disproportionate share (e.g., >40%) of selection errors, the decomposition targets the right bottleneck.\\n\\n**Contribution 1: Per-Head Adaptive Variance Bound.** We prove that for any attention head h with MRL R_h (computed from pre-RoPE query concentration per TriAttention), the structural-only estimator Ŝ_struct(k,Δ) = E[q_f]^T R(Δ) k achieves mean-squared prediction error: MSE_h ≤ (1 - R_h²) · σ²_q · ||k||² / d, where σ²_q is the expected query norm. The reviewer correctly notes this follows from the circular variance identity (Mardia & Jupp 1999). The practical contribution lies not in the bound itself but in connecting it to Top-K selection quality via rank-swap analysis: the probability that the structural predictor produces a rank swap at the Top-K boundary for head h is bounded by P(swap) ≤ exp(−Δ_K(h)² / (4·MSE_h)), where Δ_K(h) is the typical attention score gap at the K-th boundary for head h. Solving for the classification threshold: θ_h = sqrt(1 − Δ_K(h)² / (4·|ln(ε)|·σ²_q·||k||²/d)), where ε controls the tolerable Jaccard degradation. This makes θ_h per-head adaptive—it depends on both MRL and the attention gap landscape. Crucially, this produces materially different classifications than a naive MRL cutoff: a peaked-attention head (Δ_K=0.5) with R=0.94 gets θ_h≈0.93 → classified as structural (correctly: large gap means prediction errors don't affect Top-K); a flat-attention head (Δ_K=0.1) with R=0.96 gets θ_h≈0.997 → classified as content-dependent (correctly: small gap means even small errors cause rank swaps). A naive θ=0.95 misclassifies both. During offline calibration (~100 forward passes), we estimate both R_h and Δ_K(h) per head, producing the adaptive threshold map. The θ sensitivity ablation directly compares: (a) per-head adaptive θ_h from the error-budget criterion, (b) naive global θ=0.95, (c) naive θ at MRL 90th percentile—if (a) and (b)/(c) give the same classification for >95% of heads, the bound's contribution is overstated and we will report this honestly.\\n\\n**Contribution 2: Segment-Aware Residual Model.** We replace the unjustified exponential decay exp(-j/τ_h)·R(k) with a segment-aware piecewise-constant model motivated by two findings: (a) SFI's demonstration that attention support is temporally stable within semantic segments, and (b) 'Beyond Exponential Decay's finding that errors concentrate at sparse decision points (~5-10% of tokens). Within a semantic segment (between reasoning step boundaries), the content residual R(k) is held constant. At segment boundaries—detected via token-level triggers ({., ?, !, \\\\n, step markers}) plus a staleness budget T_max=32—a lightweight refresh re-scores only the content-dependent heads (~15% of heads) using the actual query. This model correctly captures non-monotonic dynamics at reasoning boundaries while being computationally cheaper than per-step refresh. We ablate: piecewise-constant vs. exponential vs. linear vs. learned piecewise decay.\\n\\n**Contribution 3: GQA-Aware Head Classification.** For GQA models (Qwen3-32B: 64Q/8KV; Llama 3.3 70B: 64Q/8KV), MRL and Δ_K are computed per-query-head via TriAttention's precomputed E[q_f] centers, then aggregated to per-KV-head classification using min-MRL and min-Δ_K across the GQA group (conservative: classify as content-dependent if ANY query head in the group has θ_h above its R_h). This is validated during calibration by comparing min vs. mean aggregation strategies. SeerAttention-R (2026) uses a learned linear projection for GQA-aligned sparsity; our analytical approach avoids training but may be less flexible—we compare the two classification strategies in ablation.\\n\\n**Concrete Method:**\\n(0) Offline head classification: Compute per-query-head MRL R_h using TriAttention's precomputed E[q_f] centers (available for Qwen3; we compute for Llama 3.3 70B FP8 using ~100 forward passes, ~4h on 2× H100). Additionally compute per-head Top-K attention gap statistics Δ_K(h) from the same calibration set. Compute per-head adaptive threshold θ_h. Aggregate via conservative min-rule per GQA group. Validate that MRL and Δ_K distributions are preserved under FP8 quantization. (1) During verification at position t: For all heads, compute full attention scores S_full(k) (free byproduct). For content-dependent heads only, compute S_struct(k, Δ_t) and store semantic residual R(k) = S_full(k) - S_struct(k, Δ_t). Storage: ~15% of heads × KV length. (2) During draft step j (position t+j): Structural heads: S_draft(k,j) = S_struct(k, Δ_{t+j}) via trigonometric rotation (O(n)). Content-dependent heads: if within current segment, S_draft(k,j) = S_struct(k, Δ_{t+j}) + R(k); if at segment boundary (trigger detected or j > T_max), refresh R(k) via lightweight re-scoring of content-dependent heads only. (3) Per-step trigonometric validation: Since TriAttention uses batch updates every 128 tokens while we apply per-token updates, we explicitly validate numerical precision at this granularity. (4) Token selection: Top-K union across all heads' S_draft scores, producing a single unified sparse token set for the attention kernel (same as SparseSpec's PillarAttn, preserving hardware efficiency—per-head routing is confined to the scoring phase, addressing Flux Attention's load imbalance concern).\\n\\n**Integration Plan:** Build on SparseSpec's open-source codebase, replacing PillarAttn's uniform stale-score reuse with head-adaptive decomposed scoring. SparseSpec was tested only up to Qwen3-14B; scaling to Qwen3-32B (2.3× larger) may require kernel modifications—we allocate 10h of the 20h buffer explicitly for SWIFT integration (github.com/hemingkx/SWIFT, ICLR 2025) as contingency if SparseSpec fails at 32B scale. The SWIFT integration path uses the same head-adaptive scoring module (framework-independent) with SWIFT's self-speculative infrastructure.\\n\\n**Memory Management:** Qwen3-32B BF16 weights occupy ~65GB on 1× H100-80GB, leaving ~15GB. KV cache at 16K context ≈ 4GB (64 layers × 8 KV heads × 128 dim × 2 × 2 bytes × 16K), leaving ~11GB for activations and framework overhead—workable for batch-size-1 but tight. For long-context benchmarks (LongBench, RULER), we restrict to ≤16K sequences in BF16 mode, or alternatively use FP8 quantization for Qwen3-32B (weights ~33GB, leaving ~47GB for KV+activations, comfortable up to 64K context). Llama 3.3 70B uses FP8 quantization (weights ~70GB on 2× H100-80GB = 160GB total, leaving ~90GB), restricted to short-context benchmarks. FP8 MRL validation is a gating experiment (~2h per model): we compare BF16 vs. FP8 head MRL and Δ_K distributions; if FP8 significantly distorts either, we fall back to BF16-only configurations.\\n\\n**Evaluation:**\\nPhase 0 (gating): Oracle ceiling analysis on 50 AIME25 problems (~3h, 1× H100). FP8 MRL/Δ_K validation (~2h per model, 6 GPU-h total).\\n\\nModels: Qwen3-32B (1× H100-80GB, primary) and Llama 3.3 70B (2× H100-80GB FP8, secondary).\\n\\nQwen3-32B benchmarks (9 total): AIME25, MATH500, HumanEval, MMLU, MT-Bench (BF16); LongBench (≤16K), RULER (≤16K) (BF16 or FP8); WikiText-103, C4 (BF16). Draft lengths γ ∈ {4, 8, 12, 16}.\\n\\nLlama 3.3 70B FP8 benchmarks (4 short-context): MMLU, HumanEval, MT-Bench, WikiText-103. Draft lengths γ ∈ {4, 8, 16}.\\n\\nMethods compared (6): DecompSpec-adaptive (ours, main: per-head adaptive θ_h + segment-aware residual), DecompSpec-naive (ours, ablation: global θ=0.95 + segment-aware residual), SparseSpec (uniform stale reuse), TriAttention structural-only (all heads treated as structural), DecompSpec-exp (exponential decay ablation), full attention (oracle upper bound).\\n\\nMetrics: throughput (tokens/sec), token acceptance rate, downstream task accuracy, selection agreement (Jaccard) with oracle scores, Kendall-τ rank correlation of predicted vs. actual importance.\\n\\nKey ablations on Qwen3-32B: (a) per-head adaptive θ_h vs. naive θ=0.95 vs. MRL-percentile cutoff—if adaptive and naive agree on >95% of heads, we report the bound's contribution as primarily theoretical; (b) piecewise-constant vs. exponential vs. linear vs. learned piecewise decay at γ=16; (c) GQA aggregation: min-MRL vs. mean-MRL; (d) selection agreement at reasoning step boundaries vs. stable regions; (e) per-step trigonometric numerical precision; (f) FP8 vs. BF16 MRL/Δ_K distribution comparison; (g) overhead breakdown vs. throughput gain; (h) T_max ∈ {16, 32, 64}; (i) oracle ceiling decomposition: fraction of selection errors attributable to content-dependent heads; (j) comparison with HeadKV-style probe-based classification (using TriAttention's available per-head scores as proxy).\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~195h H100-80GB active + 20h buffer (Phase 0 oracle ceiling ~3h, FP8 MRL validation ~2h [4 GPU-h on 2× H100], MRL+Δ_K calibration for Llama FP8 ~4h [8 GPU-h], integration ~25h, baseline reproduction ~15h, Qwen3-32B: 9 benchmarks × 4 γ × 6 methods × 0.35h ≈ 76h [1× H100], Llama 3.3 70B FP8: 4 benchmarks × 3 γ × 6 methods × 0.35h ≈ 25h wall [50 GPU-h, 2× H100], ablations ~30h on Qwen3-32B; total active ≈ 195 GPU-h). SWIFT contingency: 10h of the 20h buffer explicitly reserved.\",\n      \"gpu_utilization\": \"~30-35% — GPU idles while human writes integration code and debugs\",\n      \"timeline\": \"6-8 weeks (1 day Phase 0 gating, 2 weeks integration + calibration, 2-3 weeks experiments, 2 weeks analysis/writing)\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"$585 (195h × $3.00/hr H100)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~210h H100-80GB (agent explores more θ configurations including per-head adaptive vs. naive comparison, boundary detection strategies, GQA aggregation variants, T_max sweep, and HeadKV-style baseline)\",\n      \"gpu_utilization\": \"~60-65% — agent queues experiments, human reviews daily\",\n      \"timeline\": \"16-20 days (1 day Phase 0 gating + FP8 validation, 3-4 days integration + calibration, 8-9 days experiments, 4-5 days analysis/writing)\",\n      \"team\": \"1 researcher, ~30min/day oversight\",\n      \"claude_api_cost\": \"$80-130\",\n      \"estimated_gpu_cost\": \"$630 (210h × $3.00/hr)\",\n      \"risk_note\": \"SparseSpec codebase was tested only up to Qwen3-14B; scaling to 32B may require kernel modifications. SWIFT contingency: 10h explicitly budgeted. FP8 MRL/Δ_K validation is a gating experiment (~2h per model)—run first to confirm distributions are preserved. Oracle ceiling analysis (Phase 0) gates the entire pipeline: if ceiling < 2%, project scope should be reconsidered.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~220h H100-80GB (comprehensive sweep: per-head adaptive θ across ε ∈ {0.05, 0.1, 0.2, 0.3}, T_max ∈ {8, 16, 32, 64, 128}, per-head/per-layer/global residual tracking, min/mean/median GQA aggregation, extended to Qwen3-8B for direct SparseSpec comparison, HeadKV-style baseline reproduction)\",\n      \"gpu_utilization\": \"~85-90% — continuous experiment pipeline\",\n      \"timeline\": \"16-19 days with 2× H100 (Phase 0 gating: 1 day, FP8 validation: 0.5 day, integration + calibration: 3-4 days, experiments: 8-10 days, paper: 3-4 days)\",\n      \"team\": \"0 (2h initial setup)\",\n      \"claude_api_cost\": \"$200-300\",\n      \"estimated_gpu_cost\": \"$660 (220h × $3.00/hr)\",\n      \"speed_bottleneck\": \"Llama 3.3 70B FP8 requires 2× H100-80GB. Gating dependencies: (1) Phase 0 oracle ceiling must show >3% Jaccard improvement, (2) FP8 MRL validation must pass, before committing to full pipeline.\",\n      \"risk_note\": \"If FP8 significantly distorts MRL/Δ_K distributions, fall back to Qwen3-32B-only evaluation with BF16 short-context and FP8 long-context. If SparseSpec fails at 32B, 10h SWIFT contingency activated. If oracle ceiling is <2%, pivot to studying the gap-adaptive threshold contribution in isolation (still publishable as an analysis paper). The ~15% content-dependent head fraction may vary between dense (Llama) and MoE-distilled (Qwen3) architectures—the per-head adaptive θ naturally handles this variation.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026, commitment deadline August 2, 2026)\"\n  ],\n  \"level\": \"solid-to-strong\",\n  \"key_references\": [\n    \"Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning (HeadKV, ICLR 2025, arXiv:2410.19258)\",\n    \"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference (NeurIPS 2025, arXiv:2407.11550)\",\n    \"Decoupling Positional and Symbolic Attention Behavior in Transformers (Urrutia et al., arXiv Nov 2025, 2511.11579)\",\n    \"TriAttention: Efficient Long Reasoning with Trigonometric KV Compression (arXiv April 2026, 2604.04921)\",\n    \"Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding (SparseSpec, arXiv Dec 2025, 2512.01278)\",\n    \"SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding (arXiv Feb 2026, 2602.07223)\",\n    \"Slow-Fast Inference: Training-Free Inference Acceleration via Within-Sentence Support Stability (SFI, arXiv March 2026, 2603.12038)\",\n    \"Guess-Verify-Refine: Data-Aware Top-K for Sparse-Attention Decoding on Blackwell via Temporal Correlation (GVR, arXiv April 2026, 2604.22312)\",\n    \"Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution (arXiv Oct 2025, 2510.00636, under review ICLR 2026)\",\n    \"AttentionPredictor: Temporal Patterns Matter for KV Cache Compression (arXiv Feb 2025, 2502.04077, NeurIPS 2025)\",\n    \"Beyond Exponential Decay: Rethinking Error Accumulation in Large Language Models (arXiv May 2026, 2505.24187)\",\n    \"LycheeDecode: Accelerating Long-Context LLM Inference via Hybrid-Head Sparse Decoding (ICLR 2026, arXiv:2602.04541)\",\n    \"DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads (ICLR 2025, arXiv:2410.10819)\",\n    \"SeerAttention-R: Sparse Attention Adaptation for Long Reasoning (arXiv 2026, 2506.08889)\",\n    \"Decomposing Attention To Find Context-Sensitive Neurons (Gibson, arXiv Oct 2025, 2510.03315)\",\n    \"Flux Attention: Context-Aware Hybrid Attention for Efficient LLMs Inference (arXiv April 2026, 2604.07394)\",\n    \"Component-Aware Self-Speculative Decoding in Hybrid Language Models (arXiv May 2026, 2605.01106)\",\n    \"SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection (arXiv May 2026, 2605.02888)\",\n    \"Linear Predictability of Attention Heads in Large Language Models (arXiv March 2026, 2603.13314)\",\n    \"Evolving Sparsity: Leveraging Token Importance Dynamics for Efficient LLM Decoding with Sparse Attention (EvoSparse, ACL 2026)\",\n    \"SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acceleration (ICLR 2025)\",\n    \"SpecGuard: From Tokens to Steps — Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning (arXiv April 2026, 2604.15244)\",\n    \"Self-Indexing KVCache: Predicting Sparse Attention from Compressed Keys (AAAI 2026, arXiv:2603.14224)\",\n    \"Directional Statistics (Mardia & Jupp, 1999)\"\n  ],\n  \"description\": \"Self-speculative decoding methods (SparseSpec 2.13×, SpecAttn 2.81×) reuse verification-stage attention scores for draft-phase token selection, but these scores grow stale over γ draft steps. Recent approaches address temporal prediction uniformly: SFI (2026) reuses fixed sparse support with periodic refresh (14.4×), GVR (2026) exploits previous-step Top-K as temporal predictor, Expected Attention (2025) predicts via Gaussian MGF. However, none provides per-head prediction error guarantees or exploits the head-level heterogeneity proved by Urrutia et al. (2025) and empirically supported by Ada-KV's theorem (NeurIPS 2025) that uniform head allocation is suboptimal. We propose DecompSpec with four contributions. (0) Oracle Ceiling Analysis: A gating experiment quantifying the maximum gain from head-selective decomposition by comparing uniform-structural vs. head-selective-oracle scoring against full-attention Top-K selection on AIME25, measuring what fraction of selection errors are attributable to the ~15% content-dependent heads. (1) Per-Head Adaptive Variance Bound: We prove MSE_h ≤ (1−R_h²)·σ²_q·||k||²/d for the structural-only estimator, then connect this to Top-K selection quality via rank-swap analysis: the per-head threshold θ_h = f(R_h, Δ_K(h), ε) jointly considers MRL and the head's Top-K attention gap, producing materially different classifications than a naive MRL percentile cutoff. A peaked-attention head with moderate MRL may be reliably structural, while a flat-attention head with high MRL may need residual tracking—a global threshold misclassifies both. We explicitly ablate adaptive θ_h vs. naive cutoffs and commit to reporting honestly if they converge. (2) Segment-Aware Residual Model: Motivated by SFI's temporal stability finding and 'Beyond Exponential Decay's demonstration that errors concentrate at sparse decision points, we replace exponential decay with piecewise-constant residual tracking within semantic segments, refreshing only the ~15% content-dependent heads at reasoning step boundaries. (3) GQA-Aware Classification via conservative min-MRL/min-Δ_K aggregation across query heads per KV group. Structural heads receive analytically exact trigonometric updates at any draft distance (O(n)); content-dependent heads receive segment-aware residual tracking with boundary-triggered refresh. Per-head routing is confined to the lightweight scoring phase, and the sparse attention kernel operates on a unified Top-K token set (same as SparseSpec's PillarAttn, addressing Flux Attention's load imbalance concern). We differentiate from HeadKV (ICLR 2025), which uses offline probe-based importance for KV retention, by providing architecture-intrinsic MRL classification with theoretical error bounds targeting scoring strategy selection. Memory management: Qwen3-32B BF16 weights ≈65GB on 1× H100-80GB, leaving ~15GB; long-context experiments (LongBench, RULER) restricted to ≤16K in BF16 or use FP8 (weights ~33GB, ample headroom). Llama 3.3 70B FP8 on 2× H100, short-context only. FP8 MRL/Δ_K validation is a gating experiment. SparseSpec codebase (tested up to Qwen3-14B) is primary integration target; 10h SWIFT contingency explicitly budgeted if scaling to 32B fails. We evaluate on Qwen3-32B (9 benchmarks, γ ∈ {4,8,12,16}) and Llama 3.3 70B FP8 (4 short-context benchmarks, γ ∈ {4,8,16}), with ablations comparing: adaptive vs. naive threshold, residual models (piecewise vs. exponential vs. linear), GQA aggregation, HeadKV-style baseline, and per-step trigonometric precision. Key empirical questions: (1) does the oracle ceiling analysis show >3% Jaccard improvement from head-selective decomposition? (2) does the per-head adaptive threshold materially differ from naive cutoffs? (3) does segment-aware residual tracking capture reasoning boundary dynamics better than exponential decay? (4) is FP8 quantization compatible with MRL/Δ_K-based head classification?\",\n  \"project_name\": \"decomp_spec_decode\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 6)\nIssues: [\"BUDGET VIOLATION — All three resource modes exceed the user's hard constraint of ≤200 H100-hours total. Manual: 195h active + 20h buffer = 215h (7.5% over). HIL: 210h (5% over). Auto: 220h (10% over). The Llama 3.3 70B experiments on 2× H100 count as 2 GPU-hours per wall-clock hour; the 25h wall-clock for Llama benchmarks = 50 GPU-hours, and this is correctly counted but pushes the total over budget. The 20h buffer is partly contingency (10h SWIFT), but even the base experiments appear to sum above 200h.\", \"Missing relevant citation: 'A Mathematical Theory of Top-k Sparse Attention via Total Variation Distance' (arXiv 2512.07647, Dec 2025, NeurIPS 2025) provides rigorous per-head gap-based certificates for Top-K attention truncation error — including the key insight that the boundary gap between the K-th and (K+1)-th logits controls the approximation error bound. This is directly relevant to Contribution 1's rank-swap analysis connecting MSE to Top-K selection quality via the per-head attention gap Δ_K(h). While the two papers address complementary problems (truncation error given exact scores vs. prediction error given structural estimates), the mathematical framework (gap-based per-head certificates → Top-K quality guarantees) overlaps significantly and must be cited and differentiated.\", \"Missing relevant citation: DeltaAttention (arXiv 2505.11254, NeurIPS 2025) proposes distributional correction for sparse attention outputs, showing that sparse computation induces distributional shift that can be corrected with minimal overhead (~1.5% of full attention cost). While DeltaAttention corrects distributional shift from Top-K truncation rather than from stale prediction, the concept of 'correcting sparse attention errors via a residual/delta term' is closely related to DecompSpec's residual tracking for content-dependent heads.\", \"Date errors for two cited papers: 'Beyond Exponential Decay' (arXiv:2505.24187) was first posted May 30, 2025, not 'May 2026' as claimed — the arXiv ID 2505.xxxxx confirms May 2025 (v2 revised May 2026). SeerAttention-R (arXiv:2506.08889) was posted June 10, 2025, not '2026' as claimed. These are minor attribution errors but should be corrected.\", \"TriAttention already handles low-MRL heads adaptively: TriAttention's norm-based component is scaled by (1−R_f), meaning 'when R_f is low, the full norm contribution is preserved' while trigonometric scoring becomes less dominant. This is a continuous adaptive weighting mechanism for heterogeneous heads. DecompSpec's binary classification (structural vs. content-dependent) followed by different scoring strategies is a design alternative, not a clear improvement — the proposal should explicitly compare against TriAttention's existing continuous head weighting as a baseline and explain why binary classification with residual tracking is superior.\", \"TriAttention's evaluation on Qwen3-32B is limited: TriAttention's main experiments cover Qwen3-8B, DeepSeek-R1-Distill variants, GPT-OSS-20B, and GLM-4.7-Flash. Qwen3-32B appears only in a deployment appendix (AWQ INT4 on RTX 4090). The proposal assumes TriAttention's MRL statistics (84.7% of GQA heads with R>0.95) transfer to Qwen3-32B, but this hasn't been validated at scale — larger models may have different head concentration distributions.\", \"Impact ceiling remains uncertain despite oracle analysis design: Even with the well-designed Phase 0 gating experiment, the practical speedup is bounded by the fraction of token selection errors attributable to content-dependent heads. If structural scoring already achieves 95%+ Jaccard with oracle Top-K for reasoning tasks, the marginal improvement from residual tracking adds complexity (per-head routing, residual storage, boundary detection) for potentially modest throughput gains. The proposal should provide a back-of-envelope calculation of expected end-to-end throughput improvement given different oracle ceiling scenarios.\"]\nFeedback: The proposal has matured significantly across 6 rounds — the technical framing is honest, references are mostly verified, and the experimental design (especially gating experiments) shows strong research maturity. Three categories of issues remain:\n\n**Must fix (blocking):**\n\n1. **Trim budget to strictly ≤200 H100-hours**: Drop one γ value for Llama 3.3 70B (use γ ∈ {4, 16} instead of {4, 8, 16}), reduce from 6 to 5 comparison methods on Llama (drop one ablation variant), and reduce the buffer from 20h to 15h. Target: ≤195h total with 5h contingency = 200h. Alternatively, drop Llama 3.3 70B entirely and run Qwen3-32B only — this eliminates the 2× H100 cost multiplier and all FP8 validation overhead.\n\n2. **Cite 'A Mathematical Theory of Top-k Sparse Attention' (arXiv 2512.07647)**: Position DecompSpec as complementary — that paper bounds truncation error given exact scores; DecompSpec bounds prediction error given structural estimates. Note that both use boundary gap analysis, establishing a theoretical connection. This actually strengthens the proposal by situating the rank-swap analysis within an existing mathematical framework.\n\n3. **Fix date errors**: Beyond Exponential Decay → May 2025 (not 2026). SeerAttention-R → June 2025 (not 2026).\n\n**Should fix (to reach EMNLP Main quality):**\n\n4. **Add TriAttention's continuous weighting as an explicit baseline**: Since TriAttention already handles low-MRL heads via (1−R_f) continuous weighting, add a comparison method: 'TriAttention continuous-weighted scoring' alongside DecompSpec's binary classification + residual tracking. If DecompSpec doesn't significantly outperform this simpler approach, the binary classification's value is limited to theoretical interpretability. This comparison would make the empirical contribution much stronger.\n\n5. **Provide back-of-envelope throughput ceiling estimates**: E.g., 'If content-dependent heads (~15%) cause 40% of selection errors, and correcting these improves Jaccard by 5%, this translates to ~X% higher acceptance rate → ~Y% throughput improvement over SparseSpec.' Present this as a range (optimistic/pessimistic) to set expectations before Phase 0.\n\n6. **Cite DeltaAttention (arXiv 2505.11254, NeurIPS 2025)**: Related as a 'correction for sparse attention errors' approach. Differentiate: DeltaAttention corrects distributional shift from truncation; DecompSpec tracks semantic residuals from structural prediction. Both are correction mechanisms but target different error sources.\n\n**The path to passing**: The average score is 3.5, needing 4.0. The most actionable improvements are: (a) strict budget compliance, (b) the TriAttention continuous-weighting baseline comparison (if DecompSpec clearly wins, novelty and impact both rise), and (c) back-of-envelope throughput ceiling to clarify expected practical gains. If the oracle ceiling analysis in the proposal is compelling and the adaptive θ demonstrably outperforms both naive MRL cutoffs AND TriAttention's continuous weighting, this would reach EMNLP Main quality.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 6 轮修订，近 3 轮的平均分从 3.2 到 3.5，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-10T20:10:16.345Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T20:10:16.345Z",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f"
}
```

---

## Round 1

23 recorded events

### User

_source line 3 · 2026-05-10T20:10:16.369Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-10 (UTC).**

## Original idea
{
  "title": "Variance-Bounded Head-Adaptive Decomposition for Self-Speculative Reasoning Decoding",
  "core_problem": "Self-speculative decoding methods (SparseSpec, SpecAttn) select critical tokens for sparse draft attention by reusing verification-stage attention scores as a free oracle, but these scores become stale over γ draft steps. The attention prediction landscape has responded to this staleness problem in multiple ways—SFI (2026) reuses a fixed sparse support set and refreshes at semantic boundaries, GVR (2026) uses the previous step's Top-K as a temporal predictor, Expected Attention (2025) predicts future attention via Gaussian moment-generating functions—but ALL existing approaches treat attention heads uniformly during prediction. Ada-KV (NeurIPS 2025) proved via an L1 eviction loss upper bound (Theorem 3.3) that uniform head budget allocation is suboptimal, and HeadKV (ICLR 2025) demonstrated that per-head differential KV cache treatment can retain 1.5% of cache at 97% performance. Yet both operate on runtime cache retention budgets, not on the prediction strategy itself. Meanwhile, Urrutia et al. (2025) proved that positional and symbolic attention behaviors are mutually exclusive per head, and TriAttention (2026) showed ~85% of GQA heads have MRL R_h > 0.95 (concentrated query directions), meaning their attention scores are analytically predictable from RoPE structure alone. The remaining ~15% of content-dependent heads have high residual variance and require explicit tracking. No existing method provides per-head prediction error bounds that connect MRL concentration to attention score staleness, nor differentiates heads by their intrinsic predictability for self-speculative scoring. Furthermore, the residual dynamics for content-dependent heads are poorly modeled: SparseSpec and EvoSparse assume temporally smooth degradation, but 'Beyond Exponential Decay' (2026) demonstrates that in LLM generation, errors concentrate at sparse decision points (~5-10% of tokens) rather than accumulating gradually—suggesting the commonly assumed exponential decay model is wrong.",
  "opportunity": "We identify a theoretical gap that unifies and improves upon the fragmented attention prediction landscape. The key insight: TriAttention's MRL concentration metric directly bounds the per-head prediction error of any structural-only estimator, AND the tolerable prediction error depends on each head's Top-K attention gap—making the optimal head classification per-head adaptive, not a global threshold. Specifically, for head h with MRL R_h, the structural estimator Ŝ_struct(k,Δ) = E[q_f]^T R(Δ) k has mean-squared error bounded by O((1-R_h²)·σ²_q·||k||²/d). This bound, combined with a rank-swap analysis connecting MSE to Top-K selection quality via the per-head attention gap Δ_K(h), yields three consequences: (1) For structural heads where the bound is small relative to their attention gap, prediction is reliable at any draft distance—no staleness concern. (2) For content-dependent heads where the bound exceeds their attention gap tolerance, explicit residual tracking is necessary. (3) The per-head threshold θ_h emerges from an error-budget criterion that jointly considers MRL and attention gap, producing genuinely different classifications than a naive MRL percentile cutoff. This last point is critical: a peaked-attention head with moderate MRL (R=0.94, large Δ_K) may be reliably predicted structurally, while a flat-attention head with high MRL (R=0.96, small Δ_K) may require residual tracking. A naive global θ=0.95 misclassifies both. Ada-KV (NeurIPS 2025) proved uniform allocation is suboptimal but optimizes runtime cache budgets; our contribution operates upstream, optimizing which prediction strategy to deploy per head. HeadKV (ICLR 2025) differentiates heads via offline probe scores; our classification derives from architectural properties with a theoretical error bound. Combined with SFI's empirical finding that attention support is temporally stable within semantic segments, we can replace the unjustified exponential decay model with a segment-aware piecewise residual model that correctly captures the sparse, boundary-concentrated dynamics of content-dependent heads. No prior work connects MRL concentration to per-head attention prediction error bounds with gap-adaptive thresholds, nor exploits the resulting head-adaptive decomposition for self-speculative draft scoring.",
  "landscape": "SparseSpec (Dec 2025, arXiv:2512.01278) achieves 2.13× throughput via PillarAttn self-speculation, reusing verification attention scores with k=8 stride; evaluated on Qwen3-1.7B/8B/14B (proof-of-concept codebase, not tested beyond 14B) with AIME/OlympiadBench/LiveCodeBench; code at github.com/sspec-project/SparseSpec. SpecAttn (Feb 2026, arXiv:2602.07223) improves to 2.81× with verification-guided sparse attention co-design. Both inherit the γ-staleness limitation, applying uniform stale scores across all heads. Slow-Fast Inference (SFI, March 2026, arXiv:2603.12038) exploits temporal stability of attention support within semantic segments, achieving 14.4× throughput via event-driven sparse/dense alternation with Tmax=64 refresh budget; evaluated on Qwen3-0.6B/4B/30B/235B; treats all heads uniformly with no per-head error guarantees. Guess-Verify-Refine (GVR, April 2026, arXiv:2604.22312) uses previous step's Top-K as temporal prediction signal for Blackwell hardware, achieving 1.88× speedup in sparse Top-K selection; targets DeepSeek-V3 at 100K context; again, uniform across heads. Expected Attention (Oct 2025, arXiv:2510.00636, under review ICLR 2026) predicts future attention via Gaussian moment-generating function over query distributions, with per-head adaptive compression; targets KV cache pruning, not self-speculative scoring; evaluated on Llama3.1-8B/Qwen3-8B with LongBench/RULER. AttentionPredictor (Feb 2025, arXiv:2502.04077, NeurIPS 2025) learns a lightweight convolution model for next-token attention prediction, achieving 13× KV compression; requires training, unlike our analytical approach. HeadKV (ICLR 2025, arXiv:2410.19258) performs head-level KV cache compression using offline probe-based importance scores (needle-in-a-haystack tests) for retrieval vs. reasoning heads, retaining 1.5% of KV cache at 97% performance on Llama-3-8B/Mistral-7B; key precedent for per-head differential treatment. Difference from ours: HeadKV uses task-specific probe scores fixed across inputs targeting KV retention budgets; DecompSpec uses architecture-intrinsic MRL classification with theoretical error bounds targeting scoring strategy selection. Ada-KV (NeurIPS 2025, arXiv:2407.11550) proves via L1 eviction loss upper bound (Theorem 3.3) that uniform head budget allocation is suboptimal, proposing global Top-B adaptive allocation; evaluated across 29 datasets (Ruler, LongBench). Ada-KV directly supports our premise that per-head treatment is necessary, but optimizes runtime eviction budgets, not prediction strategy. TriAttention (April 2026, arXiv:2604.04921) provides position-aware structural scoring via trigonometric series using fixed Q centers, achieving 2.5× throughput for KV compression; reports 84.7% of GQA heads and 96.6% of MLA heads have R>0.95; uses continuous concentration-based weighting (no hard classification threshold); evaluated on Qwen3-8B, Qwen2.5, Llama3; code at github.com/WeianMao/triattention. DuoAttention (ICLR 2025) pioneered retrieval/streaming head taxonomy for KV cache compression. LycheeDecode (ICLR 2026, arXiv:2602.04541) extends with HardKuma-based learned binary classification, 2.7× speedup at 128K. SeerAttention-R (2026, arXiv:2506.08889) uses learned gating for GQA-aligned sparse attention in reasoning, achieving near-lossless accuracy at 90% sparsity with 4K token budget; GQA alignment via linear projection is relevant to our GQA-aware classification. Self-Indexing KVCache (March 2026, arXiv:2603.14224, AAAI 2026) unifies compression and sparse retrieval via sign-based 1-bit VQ; treats prediction and compression jointly but uniformly across heads. Urrutia et al. (Nov 2025, arXiv:2511.11579) formally proved positional/symbolic mutual exclusivity per head. Beyond Exponential Decay (May 2026, arXiv:2505.24187) challenges exponential error accumulation—showing errors concentrate at sparse key tokens (~5-10%), motivating our segment-aware residual model. Gibson (Oct 2025, arXiv:2510.03315) decomposes attention into structural/content components on GPT2-Small. Flux Attention (April 2026, arXiv:2604.07394) identifies load imbalance from per-head dynamic sparsity—inapplicable to our setting where per-head routing is confined to the lightweight scoring phase. Component-Aware Self-Speculative Decoding (May 2026, arXiv:2605.01106) exploits SSM/attention heterogeneity. SpecKV (May 2026, arXiv:2605.02888) adaptively selects γ using confidence signals. EvoSparse (ACL 2026) addresses evolving token importance via cross-step accumulation. Linear Predictability of Attention Heads (March 2026, arXiv:2603.13314) shows inter-head QKV linear structure enables cache compression. No existing work provides per-head prediction error bounds connecting MRL to attention score staleness with gap-adaptive thresholds, nor applies head-adaptive decomposition with segment-aware residual tracking specifically for self-speculative draft token selection.",
  "approach": "We propose DecompSpec, which provides variance-bounded head-adaptive attention prediction for self-speculative decoding, with four contributions:\n\n**Phase 0: Oracle Ceiling Analysis (Gating Experiment, ~3h on 1× H100).** Before the full experimental pipeline, we quantify the maximum possible improvement from head-selective decomposition. We run full-attention generation on 50 AIME25 problems with Qwen3-32B BF16, recording oracle attention scores at each step. Retrospectively, we compute Top-K (K=256) token selection under three scoring approaches: (a) uniform structural scoring (TriAttention for all heads), (b) head-selective oracle (structural for R_h>0.95 heads, oracle attention for the rest), and (c) SparseSpec stale reuse at γ=16. We measure Jaccard similarity with oracle Top-K, stratified by reasoning step boundaries vs. stable regions. The ceiling = Jaccard(b) − Jaccard(a) quantifies the maximum gain from decomposition. Decision gate: if ceiling > 3% Jaccard improvement, proceed to full implementation; if < 2%, reconsider scope. Additionally, we measure what fraction of token selection errors under uniform-structural scoring are attributable to the ~15% content-dependent heads—if these heads account for a disproportionate share (e.g., >40%) of selection errors, the decomposition targets the right bottleneck.\n\n**Contribution 1: Per-Head Adaptive Variance Bound.** We prove that for any attention head h with MRL R_h (computed from pre-RoPE query concentration per TriAttention), the structural-only estimator Ŝ_struct(k,Δ) = E[q_f]^T R(Δ) k achieves mean-squared prediction error: MSE_h ≤ (1 - R_h²) · σ²_q · ||k||² / d, where σ²_q is the expected query norm. The reviewer correctly notes this follows from the circular variance identity (Mardia & Jupp 1999). The practical contribution lies not in the bound itself but in connecting it to Top-K selection quality via rank-swap analysis: the probability that the structural predictor produces a rank swap at the Top-K boundary for head h is bounded by P(swap) ≤ exp(−Δ_K(h)² / (4·MSE_h)), where Δ_K(h) is the typical attention score gap at the K-th boundary for head h. Solving for the classification threshold: θ_h = sqrt(1 − Δ_K(h)² / (4·|ln(ε)|·σ²_q·||k||²/d)), where ε controls the tolerable Jaccard degradation. This makes θ_h per-head adaptive—it depends on both MRL and the attention gap landscape. Crucially, this produces materially different classifications than a naive MRL cutoff: a peaked-attention head (Δ_K=0.5) with R=0.94 gets θ_h≈0.93 → classified as structural (correctly: large gap means prediction errors don't affect Top-K); a flat-attention head (Δ_K=0.1) with R=0.96 gets θ_h≈0.997 → classified as content-dependent (correctly: small gap means even small errors cause rank swaps). A naive θ=0.95 misclassifies both. During offline calibration (~100 forward passes), we estimate both R_h and Δ_K(h) per head, producing the adaptive threshold map. The θ sensitivity ablation directly compares: (a) per-head adaptive θ_h from the error-budget criterion, (b) naive global θ=0.95, (c) naive θ at MRL 90th percentile—if (a) and (b)/(c) give the same classification for >95% of heads, the bound's contribution is overstated and we will report this honestly.\n\n**Contribution 2: Segment-Aware Residual Model.** We replace the unjustified exponential decay exp(-j/τ_h)·R(k) with a segment-aware piecewise-constant model motivated by two findings: (a) SFI's demonstration that attention support is temporally stable within semantic segments, and (b) 'Beyond Exponential Decay's finding that errors concentrate at sparse decision points (~5-10% of tokens). Within a semantic segment (between reasoning step boundaries), the content residual R(k) is held constant. At segment boundaries—detected via token-level triggers ({., ?, !, \\n, step markers}) plus a staleness budget T_max=32—a lightweight refresh re-scores only the content-dependent heads (~15% of heads) using the actual query. This model correctly captures non-monotonic dynamics at reasoning boundaries while being computationally cheaper than per-step refresh. We ablate: piecewise-constant vs. exponential vs. linear vs. learned piecewise decay.\n\n**Contribution 3: GQA-Aware Head Classification.** For GQA models (Qwen3-32B: 64Q/8KV; Llama 3.3 70B: 64Q/8KV), MRL and Δ_K are computed per-query-head via TriAttention's precomputed E[q_f] centers, then aggregated to per-KV-head classification using min-MRL and min-Δ_K across the GQA group (conservative: classify as content-dependent if ANY query head in the group has θ_h above its R_h). This is validated during calibration by comparing min vs. mean aggregation strategies. SeerAttention-R (2026) uses a learned linear projection for GQA-aligned sparsity; our analytical approach avoids training but may be less flexible—we compare the two classification strategies in ablation.\n\n**Concrete Method:**\n(0) Offline head classification: Compute per-query-head MRL R_h using TriAttention's precomputed E[q_f] centers (available for Qwen3; we compute for Llama 3.3 70B FP8 using ~100 forward passes, ~4h on 2× H100). Additionally compute per-head Top-K attention gap statistics Δ_K(h) from the same calibration set. Compute per-head adaptive threshold θ_h. Aggregate via conservative min-rule per GQA group. Validate that MRL and Δ_K distributions are preserved under FP8 quantization. (1) During verification at position t: For all heads, compute full attention scores S_full(k) (free byproduct). For content-dependent heads only, compute S_struct(k, Δ_t) and store semantic residual R(k) = S_full(k) - S_struct(k, Δ_t). Storage: ~15% of heads × KV length. (2) During draft step j (position t+j): Structural heads: S_draft(k,j) = S_struct(k, Δ_{t+j}) via trigonometric rotation (O(n)). Content-dependent heads: if within current segment, S_draft(k,j) = S_struct(k, Δ_{t+j}) + R(k); if at segment boundary (trigger detected or j > T_max), refresh R(k) via lightweight re-scoring of content-dependent heads only. (3) Per-step trigonometric validation: Since TriAttention uses batch updates every 128 tokens while we apply per-token updates, we explicitly validate numerical precision at this granularity. (4) Token selection: Top-K union across all heads' S_draft scores, producing a single unified sparse token set for the attention kernel (same as SparseSpec's PillarAttn, preserving hardware efficiency—per-head routing is confined to the scoring phase, addressing Flux Attention's load imbalance concern).\n\n**Integration Plan:** Build on SparseSpec's open-source codebase, replacing PillarAttn's uniform stale-score reuse with head-adaptive decomposed scoring. SparseSpec was tested only up to Qwen3-14B; scaling to Qwen3-32B (2.3× larger) may require kernel modifications—we allocate 10h of the 20h buffer explicitly for SWIFT integration (github.com/hemingkx/SWIFT, ICLR 2025) as contingency if SparseSpec fails at 32B scale. The SWIFT integration path uses the same head-adaptive scoring module (framework-independent) with SWIFT's self-speculative infrastructure.\n\n**Memory Management:** Qwen3-32B BF16 weights occupy ~65GB on 1× H100-80GB, leaving ~15GB. KV cache at 16K context ≈ 4GB (64 layers × 8 KV heads × 128 dim × 2 × 2 bytes × 16K), leaving ~11GB for activations and framework overhead—workable for batch-size-1 but tight. For long-context benchmarks (LongBench, RULER), we restrict to ≤16K sequences in BF16 mode, or alternatively use FP8 quantization for Qwen3-32B (weights ~33GB, leaving ~47GB for KV+activations, comfortable up to 64K context). Llama 3.3 70B uses FP8 quantization (weights ~70GB on 2× H100-80GB = 160GB total, leaving ~90GB), restricted to short-context benchmarks. FP8 MRL validation is a gating experiment (~2h per model): we compare BF16 vs. FP8 head MRL and Δ_K distributions; if FP8 significantly distorts either, we fall back to BF16-only configurations.\n\n**Evaluation:**\nPhase 0 (gating): Oracle ceiling analysis on 50 AIME25 problems (~3h, 1× H100). FP8 MRL/Δ_K validation (~2h per model, 6 GPU-h total).\n\nModels: Qwen3-32B (1× H100-80GB, primary) and Llama 3.3 70B (2× H100-80GB FP8, secondary).\n\nQwen3-32B benchmarks (9 total): AIME25, MATH500, HumanEval, MMLU, MT-Bench (BF16); LongBench (≤16K), RULER (≤16K) (BF16 or FP8); WikiText-103, C4 (BF16). Draft lengths γ ∈ {4, 8, 12, 16}.\n\nLlama 3.3 70B FP8 benchmarks (4 short-context): MMLU, HumanEval, MT-Bench, WikiText-103. Draft lengths γ ∈ {4, 8, 16}.\n\nMethods compared (6): DecompSpec-adaptive (ours, main: per-head adaptive θ_h + segment-aware residual), DecompSpec-naive (ours, ablation: global θ=0.95 + segment-aware residual), SparseSpec (uniform stale reuse), TriAttention structural-only (all heads treated as structural), DecompSpec-exp (exponential decay ablation), full attention (oracle upper bound).\n\nMetrics: throughput (tokens/sec), token acceptance rate, downstream task accuracy, selection agreement (Jaccard) with oracle scores, Kendall-τ rank correlation of predicted vs. actual importance.\n\nKey ablations on Qwen3-32B: (a) per-head adaptive θ_h vs. naive θ=0.95 vs. MRL-percentile cutoff—if adaptive and naive agree on >95% of heads, we report the bound's contribution as primarily theoretical; (b) piecewise-constant vs. exponential vs. linear vs. learned piecewise decay at γ=16; (c) GQA aggregation: min-MRL vs. mean-MRL; (d) selection agreement at reasoning step boundaries vs. stable regions; (e) per-step trigonometric numerical precision; (f) FP8 vs. BF16 MRL/Δ_K distribution comparison; (g) overhead breakdown vs. throughput gain; (h) T_max ∈ {16, 32, 64}; (i) oracle ceiling decomposition: fraction of selection errors attributable to content-dependent heads; (j) comparison with HeadKV-style probe-based classification (using TriAttention's available per-head scores as proxy).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~195h H100-80GB active + 20h buffer (Phase 0 oracle ceiling ~3h, FP8 MRL validation ~2h [4 GPU-h on 2× H100], MRL+Δ_K calibration for Llama FP8 ~4h [8 GPU-h], integration ~25h, baseline reproduction ~15h, Qwen3-32B: 9 benchmarks × 4 γ × 6 methods × 0.35h ≈ 76h [1× H100], Llama 3.3 70B FP8: 4 benchmarks × 3 γ × 6 methods × 0.35h ≈ 25h wall [50 GPU-h, 2× H100], ablations ~30h on Qwen3-32B; total active ≈ 195 GPU-h). SWIFT contingency: 10h of the 20h buffer explicitly reserved.",
      "gpu_utilization": "~30-35% — GPU idles while human writes integration code and debugs",
      "timeline": "6-8 weeks (1 day Phase 0 gating, 2 weeks integration + calibration, 2-3 weeks experiments, 2 weeks analysis/writing)",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "$585 (195h × $3.00/hr H100)"
    },
    "human_in_loop": {
      "gpu_hours": "~210h H100-80GB (agent explores more θ configurations including per-head adaptive vs. naive comparison, boundary detection strategies, GQA aggregation variants, T_max sweep, and HeadKV-style baseline)",
      "gpu_utilization": "~60-65% — agent queues experiments, human reviews daily",
      "timeline": "16-20 days (1 day Phase 0 gating + FP8 validation, 3-4 days integration + calibration, 8-9 days experiments, 4-5 days analysis/writing)",
      "team": "1 researcher, ~30min/day oversight",
      "claude_api_cost": "$80-130",
      "estimated_gpu_cost": "$630 (210h × $3.00/hr)",
      "risk_note": "SparseSpec codebase was tested only up to Qwen3-14B; scaling to 32B may require kernel modifications. SWIFT contingency: 10h explicitly budgeted. FP8 MRL/Δ_K validation is a gating experiment (~2h per model)—run first to confirm distributions are preserved. Oracle ceiling analysis (Phase 0) gates the entire pipeline: if ceiling < 2%, project scope should be reconsidered."
    },
    "auto_research": {
      "gpu_hours": "~220h H100-80GB (comprehensive sweep: per-head adaptive θ across ε ∈ {0.05, 0.1, 0.2, 0.3}, T_max ∈ {8, 16, 32, 64, 128}, per-head/per-layer/global residual tracking, min/mean/median GQA aggregation, extended to Qwen3-8B for direct SparseSpec comparison, HeadKV-style baseline reproduction)",
      "gpu_utilization": "~85-90% — continuous experiment pipeline",
      "timeline": "16-19 days with 2× H100 (Phase 0 gating: 1 day, FP8 validation: 0.5 day, integration + calibration: 3-4 days, experiments: 8-10 days, paper: 3-4 days)",
      "team": "0 (2h initial setup)",
      "claude_api_cost": "$200-300",
      "estimated_gpu_cost": "$660 (220h × $3.00/hr)",
      "speed_bottleneck": "Llama 3.3 70B FP8 requires 2× H100-80GB. Gating dependencies: (1) Phase 0 oracle ceiling must show >3% Jaccard improvement, (2) FP8 MRL validation must pass, before committing to full pipeline.",
      "risk_note": "If FP8 significantly distorts MRL/Δ_K distributions, fall back to Qwen3-32B-only evaluation with BF16 short-context and FP8 long-context. If SparseSpec fails at 32B, 10h SWIFT contingency activated. If oracle ceiling is <2%, pivot to studying the gap-adaptive threshold contribution in isolation (still publishable as an analysis paper). The ~15% content-dependent head fraction may vary between dense (Llama) and MoE-distilled (Qwen3) architectures—the per-head adaptive θ naturally handles this variation."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026, commitment deadline August 2, 2026)"
  ],
  "level": "solid-to-strong",
  "key_references": [
    "Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning (HeadKV, ICLR 2025, arXiv:2410.19258)",
    "Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference (NeurIPS 2025, arXiv:2407.11550)",
    "Decoupling Positional and Symbolic Attention Behavior in Transformers (Urrutia et al., arXiv Nov 2025, 2511.11579)",
    "TriAttention: Efficient Long Reasoning with Trigonometric KV Compression (arXiv April 2026, 2604.04921)",
    "Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding (SparseSpec, arXiv Dec 2025, 2512.01278)",
    "SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding (arXiv Feb 2026, 2602.07223)",
    "Slow-Fast Inference: Training-Free Inference Acceleration via Within-Sentence Support Stability (SFI, arXiv March 2026, 2603.12038)",
    "Guess-Verify-Refine: Data-Aware Top-K for Sparse-Attention Decoding on Blackwell via Temporal Correlation (GVR, arXiv April 2026, 2604.22312)",
    "Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution (arXiv Oct 2025, 2510.00636, under review ICLR 2026)",
    "AttentionPredictor: Temporal Patterns Matter for KV Cache Compression (arXiv Feb 2025, 2502.04077, NeurIPS 2025)",
    "Beyond Exponential Decay: Rethinking Error Accumulation in Large Language Models (arXiv May 2026, 2505.24187)",
    "LycheeDecode: Accelerating Long-Context LLM Inference via Hybrid-Head Sparse Decoding (ICLR 2026, arXiv:2602.04541)",
    "DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads (ICLR 2025, arXiv:2410.10819)",
    "SeerAttention-R: Sparse Attention Adaptation for Long Reasoning (arXiv 2026, 2506.08889)",
    "Decomposing Attention To Find Context-Sensitive Neurons (Gibson, arXiv Oct 2025, 2510.03315)",
    "Flux Attention: Context-Aware Hybrid Attention for Efficient LLMs Inference (arXiv April 2026, 2604.07394)",
    "Component-Aware Self-Speculative Decoding in Hybrid Language Models (arXiv May 2026, 2605.01106)",
    "SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection (arXiv May 2026, 2605.02888)",
    "Linear Predictability of Attention Heads in Large Language Models (arXiv March 2026, 2603.13314)",
    "Evolving Sparsity: Leveraging Token Importance Dynamics for Efficient LLM Decoding with Sparse Attention (EvoSparse, ACL 2026)",
    "SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acceleration (ICLR 2025)",
    "SpecGuard: From Tokens to Steps — Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning (arXiv April 2026, 2604.15244)",
    "Self-Indexing KVCache: Predicting Sparse Attention from Compressed Keys (AAAI 2026, arXiv:2603.14224)",
    "Directional Statistics (Mardia & Jupp, 1999)"
  ],
  "description": "Self-speculative decoding methods (SparseSpec 2.13×, SpecAttn 2.81×) reuse verification-stage attention scores for draft-phase token selection, but these scores grow stale over γ draft steps. Recent approaches address temporal prediction uniformly: SFI (2026) reuses fixed sparse support with periodic refresh (14.4×), GVR (2026) exploits previous-step Top-K as temporal predictor, Expected Attention (2025) predicts via Gaussian MGF. However, none provides per-head prediction error guarantees or exploits the head-level heterogeneity proved by Urrutia et al. (2025) and empirically supported by Ada-KV's theorem (NeurIPS 2025) that uniform head allocation is suboptimal. We propose DecompSpec with four contributions. (0) Oracle Ceiling Analysis: A gating experiment quantifying the maximum gain from head-selective decomposition by comparing uniform-structural vs. head-selective-oracle scoring against full-attention Top-K selection on AIME25, measuring what fraction of selection errors are attributable to the ~15% content-dependent heads. (1) Per-Head Adaptive Variance Bound: We prove MSE_h ≤ (1−R_h²)·σ²_q·||k||²/d for the structural-only estimator, then connect this to Top-K selection quality via rank-swap analysis: the per-head threshold θ_h = f(R_h, Δ_K(h), ε) jointly considers MRL and the head's Top-K attention gap, producing materially different classifications than a naive MRL percentile cutoff. A peaked-attention head with moderate MRL may be reliably structural, while a flat-attention head with high MRL may need residual tracking—a global threshold misclassifies both. We explicitly ablate adaptive θ_h vs. naive cutoffs and commit to reporting honestly if they converge. (2) Segment-Aware Residual Model: Motivated by SFI's temporal stability finding and 'Beyond Exponential Decay's demonstration that errors concentrate at sparse decision points, we replace exponential decay with piecewise-constant residual tracking within semantic segments, refreshing only the ~15% content-dependent heads at reasoning step boundaries. (3) GQA-Aware Classification via conservative min-MRL/min-Δ_K aggregation across query heads per KV group. Structural heads receive analytically exact trigonometric updates at any draft distance (O(n)); content-dependent heads receive segment-aware residual tracking with boundary-triggered refresh. Per-head routing is confined to the lightweight scoring phase, and the sparse attention kernel operates on a unified Top-K token set (same as SparseSpec's PillarAttn, addressing Flux Attention's load imbalance concern). We differentiate from HeadKV (ICLR 2025), which uses offline probe-based importance for KV retention, by providing architecture-intrinsic MRL classification with theoretical error bounds targeting scoring strategy selection. Memory management: Qwen3-32B BF16 weights ≈65GB on 1× H100-80GB, leaving ~15GB; long-context experiments (LongBench, RULER) restricted to ≤16K in BF16 or use FP8 (weights ~33GB, ample headroom). Llama 3.3 70B FP8 on 2× H100, short-context only. FP8 MRL/Δ_K validation is a gating experiment. SparseSpec codebase (tested up to Qwen3-14B) is primary integration target; 10h SWIFT contingency explicitly budgeted if scaling to 32B fails. We evaluate on Qwen3-32B (9 benchmarks, γ ∈ {4,8,12,16}) and Llama 3.3 70B FP8 (4 short-context benchmarks, γ ∈ {4,8,16}), with ablations comparing: adaptive vs. naive threshold, residual models (piecewise vs. exponential vs. linear), GQA aggregation, HeadKV-style baseline, and per-step trigonometric precision. Key empirical questions: (1) does the oracle ceiling analysis show >3% Jaccard improvement from head-selective decomposition? (2) does the per-head adaptive threshold materially differ from naive cutoffs? (3) does segment-aware residual tracking capture reasoning boundary dynamics better than exponential decay? (4) is FP8 quantization compatible with MRL/Δ_K-based head classification?",
  "project_name": "decomp_spec_decode",
  "source": "web_research"
}

## Reviewer feedback (round 6)
Issues: ["BUDGET VIOLATION — All three resource modes exceed the user's hard constraint of ≤200 H100-hours total. Manual: 195h active + 20h buffer = 215h (7.5% over). HIL: 210h (5% over). Auto: 220h (10% over). The Llama 3.3 70B experiments on 2× H100 count as 2 GPU-hours per wall-clock hour; the 25h wall-clock for Llama benchmarks = 50 GPU-hours, and this is correctly counted but pushes the total over budget. The 20h buffer is partly contingency (10h SWIFT), but even the base experiments appear to sum above 200h.", "Missing relevant citation: 'A Mathematical Theory of Top-k Sparse Attention via Total Variation Distance' (arXiv 2512.07647, Dec 2025, NeurIPS 2025) provides rigorous per-head gap-based certificates for Top-K attention truncation error — including the key insight that the boundary gap between the K-th and (K+1)-th logits controls the approximation error bound. This is directly relevant to Contribution 1's rank-swap analysis connecting MSE to Top-K selection quality via the per-head attention gap Δ_K(h). While the two papers address complementary problems (truncation error given exact scores vs. prediction error given structural estimates), the mathematical framework (gap-based per-head certificates → Top-K quality guarantees) overlaps significantly and must be cited and differentiated.", "Missing relevant citation: DeltaAttention (arXiv 2505.11254, NeurIPS 2025) proposes distributional correction for sparse attention outputs, showing that sparse computation induces distributional shift that can be corrected with minimal overhead (~1.5% of full attention cost). While DeltaAttention corrects distributional shift from Top-K truncation rather than from stale prediction, the concept of 'correcting sparse attention errors via a residual/delta term' is closely related to DecompSpec's residual tracking for content-dependent heads.", "Date errors for two cited papers: 'Beyond Exponential Decay' (arXiv:2505.24187) was first posted May 30, 2025, not 'May 2026' as claimed — the arXiv ID 2505.xxxxx confirms May 2025 (v2 revised May 2026). SeerAttention-R (arXiv:2506.08889) was posted June 10, 2025, not '2026' as claimed. These are minor attribution errors but should be corrected.", "TriAttention already handles low-MRL heads adaptively: TriAttention's norm-based component is scaled by (1−R_f), meaning 'when R_f is low, the full norm contribution is preserved' while trigonometric scoring becomes less dominant. This is a continuous adaptive weighting mechanism for heterogeneous heads. DecompSpec's binary classification (structural vs. content-dependent) followed by different scoring strategies is a design alternative, not a clear improvement — the proposal should explicitly compare against TriAttention's existing continuous head weighting as a baseline and explain why binary classification with residual tracking is superior.", "TriAttention's evaluation on Qwen3-32B is limited: TriAttention's main experiments cover Qwen3-8B, DeepSeek-R1-Distill variants, GPT-OSS-20B, and GLM-4.7-Flash. Qwen3-32B appears only in a deployment appendix (AWQ INT4 on RTX 4090). The proposal assumes TriAttention's MRL statistics (84.7% of GQA heads with R>0.95) transfer to Qwen3-32B, but this hasn't been validated at scale — larger models may have different head concentration distributions.", "Impact ceiling remains uncertain despite oracle analysis design: Even with the well-designed Phase 0 gating experiment, the practical speedup is bounded by the fraction of token selection errors attributable to content-dependent heads. If structural scoring already achieves 95%+ Jaccard with oracle Top-K for reasoning tasks, the marginal improvement from residual tracking adds complexity (per-head routing, residual storage, boundary detection) for potentially modest throughput gains. The proposal should provide a back-of-envelope calculation of expected end-to-end throughput improvement given different oracle ceiling scenarios."]
Feedback: The proposal has matured significantly across 6 rounds — the technical framing is honest, references are mostly verified, and the experimental design (especially gating experiments) shows strong research maturity. Three categories of issues remain:

**Must fix (blocking):**

1. **Trim budget to strictly ≤200 H100-hours**: Drop one γ value for Llama 3.3 70B (use γ ∈ {4, 16} instead of {4, 8, 16}), reduce from 6 to 5 comparison methods on Llama (drop one ablation variant), and reduce the buffer from 20h to 15h. Target: ≤195h total with 5h contingency = 200h. Alternatively, drop Llama 3.3 70B entirely and run Qwen3-32B only — this eliminates the 2× H100 cost multiplier and all FP8 validation overhead.

2. **Cite 'A Mathematical Theory of Top-k Sparse Attention' (arXiv 2512.07647)**: Position DecompSpec as complementary — that paper bounds truncation error given exact scores; DecompSpec bounds prediction error given structural estimates. Note that both use boundary gap analysis, establishing a theoretical connection. This actually strengthens the proposal by situating the rank-swap analysis within an existing mathematical framework.

3. **Fix date errors**: Beyond Exponential Decay → May 2025 (not 2026). SeerAttention-R → June 2025 (not 2026).

**Should fix (to reach EMNLP Main quality):**

4. **Add TriAttention's continuous weighting as an explicit baseline**: Since TriAttention already handles low-MRL heads via (1−R_f) continuous weighting, add a comparison method: 'TriAttention continuous-weighted scoring' alongside DecompSpec's binary classification + residual tracking. If DecompSpec doesn't significantly outperform this simpler approach, the binary classification's value is limited to theoretical interpretability. This comparison would make the empirical contribution much stronger.

5. **Provide back-of-envelope throughput ceiling estimates**: E.g., 'If content-dependent heads (~15%) cause 40% of selection errors, and correcting these improves Jaccard by 5%, this translates to ~X% higher acceptance rate → ~Y% throughput improvement over SparseSpec.' Present this as a range (optimistic/pessimistic) to set expectations before Phase 0.

6. **Cite DeltaAttention (arXiv 2505.11254, NeurIPS 2025)**: Related as a 'correction for sparse attention errors' approach. Differentiate: DeltaAttention corrects distributional shift from truncation; DecompSpec tracks semantic residuals from structural prediction. Both are correction mechanisms but target different error sources.

**The path to passing**: The average score is 3.5, needing 4.0. The most actionable improvements are: (a) strict budget compliance, (b) the TriAttention continuous-weighting baseline comparison (if DecompSpec clearly wins, novelty and impact both rise), and (c) back-of-envelope throughput ceiling to clarify expected practical gains. If the oracle ceiling analysis in the proposal is compelling and the adaptive θ demonstrably outperforms both naive MRL cutoffs AND TriAttention's continuous weighting, this would reach EMNLP Main quality.

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
这个 idea 已经经过 6 轮修订，近 3 轮的平均分从 3.2 到 3.5，没有明显改善。

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
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "type": "user",
  "uuid": "0e9f179c-924e-4c50-aed8-5ff255026328",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T20:10:16.366Z_

```json
{
  "parentUuid": "0e9f179c-924e-4c50-aed8-5ff255026328",
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
  "uuid": "3adbcce6-2c70-4dc3-b2f1-e11dcc40b96c",
  "timestamp": "2026-05-10T20:10:16.366Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T20:10:16.366Z_

```json
{
  "parentUuid": "3adbcce6-2c70-4dc3-b2f1-e11dcc40b96c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5fc6116a-4fc1-4679-9d5b-d1475cde776b",
  "timestamp": "2026-05-10T20:10:16.366Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Variance-Bounded Head-Adaptive Decomposition for Self-Speculative Reas…",
  "leafUuid": "5fc6116a-4fc1-4679-9d5b-d1475cde776b",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Self-speculative decoding with head-adaptive sparse attention",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f"
}
```

---

### Assistant

_source line 8 · 2026-05-10T20:10:37.547Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the reviewer feedback and think deeply about whether this idea needs minor fixes, major revision, or a pivot.

The reviewer feedback covers:
1. Budget violation (≤200 H100-hours) - must fix
2. Missing citation: "A Mathematical Theory of Top-k Sparse Attention" (arXiv 2512.07647) - must fix
3. Date errors for Beyond Exponential Decay and SeerAttention-R - must fix
4. TriAttention already handles low-MRL heads adaptively via continuous weighting - should fix
5. TriAttention's Qwen3-32B evaluation is limited - should fix


6. Missing citation: DeltaAttention (arXiv 2505.11254) - should fix
7. Impact ceiling uncertainty - should fix with back-of-envelope calculation

The stagnation warning is important - 6 rounds, score stuck at 3.5. I need to assess whether the fundamental approach is sound or if this requires more than surface-level fixes. The core novelty hinges on binary head classification with different prediction strategies, but TriAttention already achieves adaptive weighting through continuous mechanisms. I'm uncertain whether the binary approach offers genuine advantages, and if structural scoring already hits 95%+ Jaccard, the marginal gains might be too small to justify the added complexity.

The budget keeps creeping past 200 hours, which is a real constraint. To reach 4.0, I need to address the reviewer's substantive points: TriAttention's continuous weighting already handles head heterogeneity, so DecompSpec's contribution narrows to the theoretical bound (which follows straightforwardly from circular variance) and segment-aware residual tracking—that's insufficient for a main venue. A back-of-envelope calculation might confirm the improvement ceiling is modest. But I think this is still salvageable if I make TriAttention's continuous weighting an explicit baseline and demonstrate that binary classification plus residual tracking outperforms it, while keeping the budget strictly controlled.

Now I need to track down the missing citations, verify the dates, and nail down the throughput ceiling estimates before committing to the approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fc6116a-4fc1-4679-9d5b-d1475cde776b",
  "isSidechain": false,
  "requestId": "req_011CauVh9HvB2nW6H2JxQ5Nf",
  "type": "assistant",
  "uuid": "7376d5d8-97e4-4bce-9e2b-e8834f52af29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LA2SjHLA2JacNfH9F53mzF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17280,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1698,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17280,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1698,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 17280,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17280
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

_source line 9 · 2026-05-10T20:10:37.873Z_

I'll start by researching the specific papers and claims flagged by the reviewer, then assess whether this needs minor fixes, major revision, or a pivot.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7376d5d8-97e4-4bce-9e2b-e8834f52af29",
  "isSidechain": false,
  "requestId": "req_011CauVh9HvB2nW6H2JxQ5Nf",
  "type": "assistant",
  "uuid": "8de4f178-40c6-4060-814e-017d9f559876",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LA2SjHLA2JacNfH9F53mzF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17280,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1698,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17280,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1698,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 17280,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17280
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

_source line 10 · 2026-05-10T20:10:42.316Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01WLPv7aA5w4FzBmyc4w3AGd`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for Top-k sparse attention paper",
  "prompt": "Search for and read the paper \"A Mathematical Theory of Top-k Sparse Attention via Total Variation Distance\" (arXiv 2512.07647). I need to understand:\n1. What exactly does this paper prove about Top-K attention truncation error?\n2. How does the boundary gap between K-th and (K+1)-th logits factor into their bounds?\n3. Is this NeurIPS 2025 as claimed?\n4. What are the key theorems?\n\nUse WebSearch to find it, then use WebFetch to read the abstract and key results from the arXiv page. Report the key findings concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8de4f178-40c6-4060-814e-017d9f559876",
  "isSidechain": false,
  "requestId": "req_011CauVh9HvB2nW6H2JxQ5Nf",
  "type": "assistant",
  "uuid": "2eabe406-4531-4ed3-ad45-36ef90725871",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LA2SjHLA2JacNfH9F53mzF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17280,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1698,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17280,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1698,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 17280,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17280
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

_source line 11 · 2026-05-10T20:10:44.721Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01UwfJdrucDHv7EPmVwi6osm`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for DeltaAttention paper",
  "prompt": "Search for and read the paper \"DeltaAttention\" (arXiv 2505.11254). I need to understand:\n1. What is the core idea of distributional correction for sparse attention?\n2. How does it correct distributional shift from Top-K truncation?\n3. What is the overhead (~1.5% of full attention cost)?\n4. Is it NeurIPS 2025 as claimed?\n\nUse WebSearch to find it, then use WebFetch to read the abstract and method from the arXiv page. Report the key findings concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2eabe406-4531-4ed3-ad45-36ef90725871",
  "isSidechain": false,
  "requestId": "req_011CauVh9HvB2nW6H2JxQ5Nf",
  "type": "assistant",
  "uuid": "d836ffe7-13fa-429a-a578-a7d1ab3b63f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LA2SjHLA2JacNfH9F53mzF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17280,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1698,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17280,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1698,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 17280,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17280
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

_source line 12 · 2026-05-10T20:10:50.037Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Nh7ZLD1gpn9Abf8rHYN7EL`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify dates and TriAttention details",
  "prompt": "I need to verify several claims about papers:\n\n1. \"Beyond Exponential Decay\" (arXiv:2505.24187) - verify the actual posting date. The arXiv ID 2505.xxxxx suggests May 2025. Check if this is May 2025 or May 2026.\n\n2. \"SeerAttention-R\" (arXiv:2506.08889) - verify the actual posting date. The arXiv ID 2506.xxxxx suggests June 2025. Check if this is June 2025 or June 2026.\n\n3. TriAttention (arXiv:2604.04921) - I need to understand how TriAttention handles low-MRL heads. Specifically:\n   - How does the (1-R_f) norm-based component work as continuous adaptive weighting?\n   - Does TriAttention evaluate on Qwen3-32B in main experiments or only in appendix?\n   - What models are in the main evaluation?\n\nUse WebSearch and WebFetch to read the actual arXiv pages. Report findings concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d836ffe7-13fa-429a-a578-a7d1ab3b63f2",
  "isSidechain": false,
  "requestId": "req_011CauVh9HvB2nW6H2JxQ5Nf",
  "type": "assistant",
  "uuid": "9d97d9af-4e63-4f09-a804-a1b45af610ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LA2SjHLA2JacNfH9F53mzF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17280,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1698,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17280,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1698,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 17280,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17280
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

_source line 13 · 2026-05-10T20:10:57.021Z_

<details open><summary>🔧 Tool call — Agent · `toolu_017fht9B4JXrFWd8UYfjXnGJ`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search latest self-speculative decoding work",
  "prompt": "Search for the latest developments (2025-2026) in self-speculative decoding and sparse attention for LLM inference acceleration. I'm looking for:\n\n1. Any new papers (May-June 2026) that combine per-head adaptive attention with speculative decoding\n2. Any papers that do head-level classification/decomposition for attention prediction (not just KV cache compression)\n3. Current SOTA throughput numbers for self-speculative decoding on reasoning tasks\n4. Any work that challenges or extends TriAttention's MRL-based head classification\n\nUse WebSearch with multiple query variations:\n- \"self-speculative decoding head adaptive 2026\"\n- \"per-head attention prediction speculative decoding\"\n- \"MRL head classification attention\"\n- \"sparse attention head decomposition LLM\"\n\nReport findings concisely, focusing on anything that might affect the novelty or framing of a paper about head-adaptive decomposition for self-speculative decoding."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d97d9af-4e63-4f09-a804-a1b45af610ae",
  "isSidechain": false,
  "requestId": "req_011CauVh9HvB2nW6H2JxQ5Nf",
  "type": "assistant",
  "uuid": "5ad8f8b0-0678-4c6b-8391-d170e6a827a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LA2SjHLA2JacNfH9F53mzF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17280,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1698,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17280,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1698,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 17280,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17280
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

_source line 14 · 2026-05-10T20:11:43.918Z_

<details><summary>↩ Tool result · `toolu_01Nh7ZLD1gpn9Abf8rHYN7EL`</summary>

```text
I now have all the information needed. Here are the findings:

---

## 1. "Beyond Exponential Decay" (arXiv:2505.24187) -- Date Verification

- **Original submission date: May 30, 2025** (v1)
- Latest revision (v2): May 6, 2026
- The arXiv ID prefix `2505` correctly indicates May 2025. The paper was first posted in **May 2025**, not May 2026.

---

## 2. "SeerAttention-R" (arXiv:2506.08889) -- Date Verification

- **Submission date: June 10, 2025** (v1, the only version)
- The arXiv ID prefix `2506` correctly indicates June 2025. The paper was posted in **June 2025**, not June 2026.

---

## 3. TriAttention (arXiv:2604.04921) -- Technical Details

**Posting date:** April 6, 2026 (the `2604` prefix = April 2026).

### How (1-R_f) norm-based weighting works

The norm-based score is defined as:

**S_norm(k) = sum_f (1 - R_f) * E[||q_f||] * ||k_f||**

- R_f is the Mean Resultant Length for frequency f, measuring how concentrated the Q/K vectors are around their center.
- When R_f is high (strong concentration), (1 - R_f) approaches zero, so S_norm contributes minimally and the trigonometric series score dominates.
- When R_f is low (dispersed/low-concentration heads), (1 - R_f) is large, activating the full norm-based contribution.
- The authors show this rewrites as **sum_f (E[||q_f||] - ||E[q_f]||) * ||k_f||**, capturing the expected magnitude variance around the center -- exactly the signal needed for low-concentration heads.

This is a **continuous** weighting, not a binary gate: every head gets a blend of trigonometric and norm-based scoring proportional to its concentration level.

### Models in main evaluation

Four models appear in the primary experiment tables (Tables 1-5):
- **Qwen3-8B**
- **DeepSeek-R1-Distill-Llama-8B**
- **DeepSeek-R1-Distill-Qwen-7B**
- **GPT-OSS-20B**

### Qwen3-32B placement

Qwen3-32B appears **only in Appendix J** ("Real-World Deployment: Agentic Task on a Single GPU"), **not** in the main experiment tables. The main evaluation uses Qwen3-8B as the Qwen representative.

---

Sources:
- [Beyond Exponential Decay - arXiv](https://arxiv.org/abs/2505.24187)
- [SeerAttention-R - arXiv](https://arxiv.org/abs/2506.08889)
- [TriAttention - arXiv](https://arxiv.org/abs/2604.04921)
- [TriAttention HTML paper](https://arxiv.org/html/2604.04921)
- [TriAttention - MarkTechPost](https://www.marktechpost.com/2026/04/11/researchers-from-mit-nvidia-and-zhejiang-university-propose-triattention-a-kv-cache-compression-method-that-matches-full-attention-at-2-5x-higher-throughput/)
- [TriAttention - GitHub](https://github.com/WeianMao/triattention)

agentId: a409fc06e40d4196c (use SendMessage with to: 'a409fc06e40d4196c' to continue this agent)
&lt;usage>total_tokens: 14762
tool_uses: 6
duration_ms: 53878&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d97d9af-4e63-4f09-a804-a1b45af610ae",
  "isSidechain": false,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "type": "user",
  "uuid": "6317c53f-da5c-4920-968d-c458c160bc18",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify several claims about papers:\n\n1. \"Beyond Exponential Decay\" (arXiv:2505.24187) - verify the actual posting date. The arXiv ID 2505.xxxxx suggests May 2025. Check if this is May 2025 or May 2026.\n\n2. \"SeerAttention-R\" (arXiv:2506.08889) - verify the actual posting date. The arXiv ID 2506.xxxxx suggests June 2025. Check if this is June 2025 or June 2026.\n\n3. TriAttention (arXiv:2604.04921) - I need to understand how TriAttention handles low-MRL heads. Specifically:\n   - How does the (1-R_f) norm-based component work as continuous adaptive weighting?\n   - Does TriAttention evaluate on Qwen3-32B in main experiments or only in appendix?\n   - What models are in the main evaluation?\n\nUse WebSearch and WebFetch to read the actual arXiv pages. Report findings concisely.",
    "agentId": "a409fc06e40d4196c",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have all the information needed. Here are the findings:\n\n---\n\n## 1. \"Beyond Exponential Decay\" (arXiv:2505.24187) -- Date Verification\n\n- **Original submission date: May 30, 2025** (v1)\n- Latest revision (v2): May 6, 2026\n- The arXiv ID prefix `2505` correctly indicates May 2025. The paper was first posted in **May 2025**, not May 2026.\n\n---\n\n## 2. \"SeerAttention-R\" (arXiv:2506.08889) -- Date Verification\n\n- **Submission date: June 10, 2025** (v1, the only version)\n- The arXiv ID prefix `2506` correctly indicates June 2025. The paper was posted in **June 2025**, not June 2026.\n\n---\n\n## 3. TriAttention (arXiv:2604.04921) -- Technical Details\n\n**Posting date:** April 6, 2026 (the `2604` prefix = April 2026).\n\n### How (1-R_f) norm-based weighting works\n\nThe norm-based score is defined as:\n\n**S_norm(k) = sum_f (1 - R_f) * E[||q_f||] * ||k_f||**\n\n- R_f is the Mean Resultant Length for frequency f, measuring how concentrated the Q/K vectors are around their center.\n- When R_f is high (strong concentration), (1 - R_f) approaches zero, so S_norm contributes minimally and the trigonometric series score dominates.\n- When R_f is low (dispersed/low-concentration heads), (1 - R_f) is large, activating the full norm-based contribution.\n- The authors show this rewrites as **sum_f (E[||q_f||] - ||E[q_f]||) * ||k_f||**, capturing the expected magnitude variance around the center -- exactly the signal needed for low-concentration heads.\n\nThis is a **continuous** weighting, not a binary gate: every head gets a blend of trigonometric and norm-based scoring proportional to its concentration level.\n\n### Models in main evaluation\n\nFour models appear in the primary experiment tables (Tables 1-5):\n- **Qwen3-8B**\n- **DeepSeek-R1-Distill-Llama-8B**\n- **DeepSeek-R1-Distill-Qwen-7B**\n- **GPT-OSS-20B**\n\n### Qwen3-32B placement\n\nQwen3-32B appears **only in Appendix J** (\"Real-World Deployment: Agentic Task on a Single GPU\"), **not** in the main experiment tables. The main evaluation uses Qwen3-8B as the Qwen representative.\n\n---\n\nSources:\n- [Beyond Exponential Decay - arXiv](https://arxiv.org/abs/2505.24187)\n- [SeerAttention-R - arXiv](https://arxiv.org/abs/2506.08889)\n- [TriAttention - arXiv](https://arxiv.org/abs/2604.04921)\n- [TriAttention HTML paper](https://arxiv.org/html/2604.04921)\n- [TriAttention - MarkTechPost](https://www.marktechpost.com/2026/04/11/researchers-from-mit-nvidia-and-zhejiang-university-propose-triattention-a-kv-cache-compression-method-that-matches-full-attention-at-2-5x-higher-throughput/)\n- [TriAttention - GitHub](https://github.com/WeianMao/triattention)"
      }
    ],
    "totalDurationMs": 53878,
    "totalTokens": 14762,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 11945,
      "output_tokens": 906,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1910
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 906,
          "cache_read_input_tokens": 11945,
          "cache_creation_input_tokens": 1910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1910,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 6
    }
  },
  "sourceToolAssistantUUID": "9d97d9af-4e63-4f09-a804-a1b45af610ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T20:11:46.698Z_

<details><summary>↩ Tool result · `toolu_01WLPv7aA5w4FzBmyc4w3AGd`</summary>

```text
Here are the key findings from the paper.

---

**Paper:** "A Mathematical Theory of Top-k Sparse Attention via Total Variation Distance" (arXiv:2512.07647)
**Authors:** Georgios Tzachristas, Lei Deng, Ioannis Tzachristas, Gong Zhang, Renhai Chen
**Submitted:** December 8, 2025

---

### 1. What the paper proves about Top-K attention truncation error

The paper establishes an **exact identity** (not just a bound) between the total-variation distance of the full softmax distribution P and its Top-k truncation P-hat, and the discarded tail mass:

- **Lemma 4.1:** TV(P, P-hat) = sum of p_i for i > k (the tail mass tau). The TV distance *is* exactly the probability mass you throw away.
- **Theorem 4.3 (Exact TV-KL Identity):** KL(P-hat || P) = log(Z / Z_k), and TV(P, P-hat) = 1 - exp(-KL(P-hat || P)). This is a sharp equality, not an inequality, specific to the Top-k truncation structure.
- **Theorem 5.2 (Exact Head-Tail Decomposition):** The output-level error factorizes as:
  `||Attn(q,K,V) - Attn_k(q,K,V)||_2 = tau * ||mu_tail - mu_head||_2`
  where tau is the tail mass, and mu_head / mu_tail are the conditional means of value vectors over retained vs. discarded indices. This cleanly separates the **score-side error** (tau) from the **value-side geometry** (how different the discarded values are from the kept ones).

### 2. How the boundary gap factors into the bounds

The **boundary gap** Delta_k = s_k - s_{k+1} (the difference between the K-th and (K+1)-th largest logits) appears in **Theorem 4.5 (Deterministic Gap Bound)**:

`TV(P, P-hat) <= 1 / (1 + (k / (n-k)) * exp(Delta_k))`

The exponential dependence on Delta_k is the critical insight: even a **modest gap** (e.g., Delta_k around 15) exponentially suppresses the tail mass, making truncation highly accurate. The bound is tight when all top-k scores equal s_k and all remaining scores equal s_{k+1}. This gives practitioners a simple, checkable certificate: if the gap at the truncation boundary is large, the approximation is provably good. The paper also extends this to **multi-gap bounds** (Lemma 4.7) that examine sequences of adjacent gaps, and block-level generalizations.

### 3. Is this NeurIPS 2025?

**No.** The paper is an **arXiv preprint** (arXiv:2512.07647v1, submitted December 2025). There is **no indication** of NeurIPS 2025 acceptance anywhere on the arXiv page. If someone claimed it was a NeurIPS 2025 paper, that claim is not supported by the available metadata.

### 4. Key theorems summary

| Result | Statement |
|---|---|
| **Lemma 4.1** | TV(P, P-hat) = tau (tail mass) -- exact identity |
| **Theorem 4.3** | TV = 1 - exp(-KL), with KL = log(Z/Z_k) -- exact TV-KL relationship |
| **Theorem 4.5** | TV <= 1 / (1 + (k/(n-k)) exp(Delta_k)) -- deterministic gap bound |
| **Theorem 5.2** | Output error = tau * ||mu_tail - mu_head||_2 -- exact factorization |
| **Proposition 5.3** | Output error <= tau * diam_{H,T} -- geometric diameter bound |
| **Asymptotic scaling** | k_epsilon ~ n * Phi_c(sigma + Phi^{-1}(epsilon)) under Gaussian scores -- minimal k scales linearly in n, exponentially in score variance sigma |

The practical upshot: the framework lets you predict how many keys to keep (k) for a given error budget epsilon, and this prediction scales predictably with context length. Experiments show 2-4x reduction in scored keys while maintaining prescribed error budgets, validated to within 0.1% relative error for sigma <= 3.

Sources:
- [arXiv abstract page](https://arxiv.org/abs/2512.07647)
- [arXiv HTML full paper](https://arxiv.org/html/2512.07647)

agentId: a14a6f063bfdf7d5b (use SendMessage with to: 'a14a6f063bfdf7d5b' to continue this agent)
&lt;usage>total_tokens: 14388
tool_uses: 4
duration_ms: 64375&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2eabe406-4531-4ed3-ad45-36ef90725871",
  "isSidechain": false,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "type": "user",
  "uuid": "886d97f2-e9f9-46c0-82bc-f6fbd39ca741",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for and read the paper \"A Mathematical Theory of Top-k Sparse Attention via Total Variation Distance\" (arXiv 2512.07647). I need to understand:\n1. What exactly does this paper prove about Top-K attention truncation error?\n2. How does the boundary gap between K-th and (K+1)-th logits factor into their bounds?\n3. Is this NeurIPS 2025 as claimed?\n4. What are the key theorems?\n\nUse WebSearch to find it, then use WebFetch to read the abstract and key results from the arXiv page. Report the key findings concisely.",
    "agentId": "a14a6f063bfdf7d5b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the key findings from the paper.\n\n---\n\n**Paper:** \"A Mathematical Theory of Top-k Sparse Attention via Total Variation Distance\" (arXiv:2512.07647)\n**Authors:** Georgios Tzachristas, Lei Deng, Ioannis Tzachristas, Gong Zhang, Renhai Chen\n**Submitted:** December 8, 2025\n\n---\n\n### 1. What the paper proves about Top-K attention truncation error\n\nThe paper establishes an **exact identity** (not just a bound) between the total-variation distance of the full softmax distribution P and its Top-k truncation P-hat, and the discarded tail mass:\n\n- **Lemma 4.1:** TV(P, P-hat) = sum of p_i for i > k (the tail mass tau). The TV distance *is* exactly the probability mass you throw away.\n- **Theorem 4.3 (Exact TV-KL Identity):** KL(P-hat || P) = log(Z / Z_k), and TV(P, P-hat) = 1 - exp(-KL(P-hat || P)). This is a sharp equality, not an inequality, specific to the Top-k truncation structure.\n- **Theorem 5.2 (Exact Head-Tail Decomposition):** The output-level error factorizes as:\n  `||Attn(q,K,V) - Attn_k(q,K,V)||_2 = tau * ||mu_tail - mu_head||_2`\n  where tau is the tail mass, and mu_head / mu_tail are the conditional means of value vectors over retained vs. discarded indices. This cleanly separates the **score-side error** (tau) from the **value-side geometry** (how different the discarded values are from the kept ones).\n\n### 2. How the boundary gap factors into the bounds\n\nThe **boundary gap** Delta_k = s_k - s_{k+1} (the difference between the K-th and (K+1)-th largest logits) appears in **Theorem 4.5 (Deterministic Gap Bound)**:\n\n`TV(P, P-hat) <= 1 / (1 + (k / (n-k)) * exp(Delta_k))`\n\nThe exponential dependence on Delta_k is the critical insight: even a **modest gap** (e.g., Delta_k around 15) exponentially suppresses the tail mass, making truncation highly accurate. The bound is tight when all top-k scores equal s_k and all remaining scores equal s_{k+1}. This gives practitioners a simple, checkable certificate: if the gap at the truncation boundary is large, the approximation is provably good. The paper also extends this to **multi-gap bounds** (Lemma 4.7) that examine sequences of adjacent gaps, and block-level generalizations.\n\n### 3. Is this NeurIPS 2025?\n\n**No.** The paper is an **arXiv preprint** (arXiv:2512.07647v1, submitted December 2025). There is **no indication** of NeurIPS 2025 acceptance anywhere on the arXiv page. If someone claimed it was a NeurIPS 2025 paper, that claim is not supported by the available metadata.\n\n### 4. Key theorems summary\n\n| Result | Statement |\n|---|---|\n| **Lemma 4.1** | TV(P, P-hat) = tau (tail mass) -- exact identity |\n| **Theorem 4.3** | TV = 1 - exp(-KL), with KL = log(Z/Z_k) -- exact TV-KL relationship |\n| **Theorem 4.5** | TV <= 1 / (1 + (k/(n-k)) exp(Delta_k)) -- deterministic gap bound |\n| **Theorem 5.2** | Output error = tau * ||mu_tail - mu_head||_2 -- exact factorization |\n| **Proposition 5.3** | Output error <= tau * diam_{H,T} -- geometric diameter bound |\n| **Asymptotic scaling** | k_epsilon ~ n * Phi_c(sigma + Phi^{-1}(epsilon)) under Gaussian scores -- minimal k scales linearly in n, exponentially in score variance sigma |\n\nThe practical upshot: the framework lets you predict how many keys to keep (k) for a given error budget epsilon, and this prediction scales predictably with context length. Experiments show 2-4x reduction in scored keys while maintaining prescribed error budgets, validated to within 0.1% relative error for sigma <= 3.\n\nSources:\n- [arXiv abstract page](https://arxiv.org/abs/2512.07647)\n- [arXiv HTML full paper](https://arxiv.org/html/2512.07647)"
      }
    ],
    "totalDurationMs": 64375,
    "totalTokens": 14388,
    "totalToolUseCount": 4,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1371,
      "cache_read_input_tokens": 11864,
      "output_tokens": 1152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1371
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1152,
          "cache_read_input_tokens": 11864,
          "cache_creation_input_tokens": 1371,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1371,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 4
    }
  },
  "sourceToolAssistantUUID": "2eabe406-4531-4ed3-ad45-36ef90725871",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Variance-Bounded Head-Adaptive Decomposition for Self-Speculative Reas…",
  "leafUuid": "886d97f2-e9f9-46c0-82bc-f6fbd39ca741",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Self-speculative decoding with head-adaptive sparse attention",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f"
}
```

---

### Tool result

_source line 18 · 2026-05-10T20:11:53.718Z_

<details><summary>↩ Tool result · `toolu_01UwfJdrucDHv7EPmVwi6osm`</summary>

```text
Here are the key findings from the paper.

---

**Paper:** *Delta Attention: Fast and Accurate Sparse Attention Inference by Delta Correction* (arXiv 2505.11254)
**Authors:** Jeffrey Willette, Heejun Lee, Sung Ju Hwang

---

### 1. Core Idea of Distributional Correction for Sparse Attention

Sparse attention methods (Top-K, sliding window, etc.) prune away most attention scores to save computation. However, this pruning changes the softmax normalization constant. Full attention normalizes over all N keys (Z = H + T, where H is the sum over pruned/"head" entries and T is the sum over kept/"tail" entries), but sparse attention normalizes only over the kept entries (using T alone). This mismatch means the sparse attention output distribution diverges from that of full quadratic attention, causing decoding-time queries to misalign with the appropriate keys from prefill. Delta Attention corrects this by computing a cheap correction term that brings the sparse output distribution back toward the full-attention distribution.

### 2. How the Delta Correction Works (Step by Step)

The method is elegantly simple:

1. **Compute sparse attention** for all queries as usual: A*V (the standard sparse output).
2. **Sample every gamma-th query** (default gamma = 64) and compute **full dense attention** for just those sampled queries: tilde{A}V.
3. **Compute the delta** = (dense output - sparse output) for each sampled query. This difference captures the contribution of the pruned attention entries.
4. **Broadcast the delta** to all gamma neighbors: for query i, the corrected output is:

   `(corrected output)_i = (A*V)_i + [dense_output_{floor(i/gamma)} - sparse_output_{floor(i/gamma)}]`

The key insight is that the difference between dense and sparse outputs at a sampled query approximates the missing attention contribution from pruned regions, and this difference varies slowly across nearby queries, so broadcasting it across a window of gamma queries is a good approximation.

The approximation error is bounded (Lemma 1): `|delta - sum of pruned contributions| <= [H/(H+T)] * max|v_i|`, which is tight when sparsity is good (T >> H).

### 3. The ~1.5% Overhead

The overhead comes from recomputing dense attention for every 64th query (gamma = 64). At 131K context length:

- Each sampled query attends to the full context (rather than just the sparse window of ~2048 tokens).
- The additional cost per sampled row is roughly C/(2*gamma) = 131072 / 128 = 1024 extra tokens of attention.
- As a fraction of full quadratic attention: 1024 / 65536 ~ **1.5%**.

The operations contributing: (a) selecting the query subset (negligible), (b) dense attention for those queries (the 1.5%), (c) computing the difference and broadcasting (trivial). So the method maintains ~98.5% sparsity over full quadratic attention.

### 4. NeurIPS 2025 Status: Confirmed

Yes, the paper was **accepted at NeurIPS 2025** as a **poster presentation** (Thursday, December 4, 2025, San Diego). This is confirmed by the NeurIPS virtual site listing (poster #118545).

---

### Bottom Line

Delta Attention is a plug-in post-processing correction applicable to any sparse attention method. On the 131K RULER benchmark, it recovers an average of 36 percentage points of performance (reaching 88% of full quadratic attention accuracy) when applied on top of sliding window + sink tokens, at only ~1.5% additional cost. At 1M token prefills, this yields a 32x speedup over FlashAttention-2.

Sources:
- [arXiv Abstract Page](https://arxiv.org/abs/2505.11254)
- [arXiv HTML Full Paper](https://arxiv.org/html/2505.11254)
- [NeurIPS 2025 Poster Page](https://neurips.cc/virtual/2025/poster/118545)
- [HuggingFace Paper Page](https://huggingface.co/papers/2505.11254)

agentId: a5d5e8078d2e31eff (use SendMessage with to: 'a5d5e8078d2e31eff' to continue this agent)
&lt;usage>total_tokens: 14631
tool_uses: 5
duration_ms: 68995&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d836ffe7-13fa-429a-a578-a7d1ab3b63f2",
  "isSidechain": false,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "type": "user",
  "uuid": "28df4846-7137-46c5-be3e-2f1275857c24",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for and read the paper \"DeltaAttention\" (arXiv 2505.11254). I need to understand:\n1. What is the core idea of distributional correction for sparse attention?\n2. How does it correct distributional shift from Top-K truncation?\n3. What is the overhead (~1.5% of full attention cost)?\n4. Is it NeurIPS 2025 as claimed?\n\nUse WebSearch to find it, then use WebFetch to read the abstract and method from the arXiv page. Report the key findings concisely.",
    "agentId": "a5d5e8078d2e31eff",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the key findings from the paper.\n\n---\n\n**Paper:** *Delta Attention: Fast and Accurate Sparse Attention Inference by Delta Correction* (arXiv 2505.11254)\n**Authors:** Jeffrey Willette, Heejun Lee, Sung Ju Hwang\n\n---\n\n### 1. Core Idea of Distributional Correction for Sparse Attention\n\nSparse attention methods (Top-K, sliding window, etc.) prune away most attention scores to save computation. However, this pruning changes the softmax normalization constant. Full attention normalizes over all N keys (Z = H + T, where H is the sum over pruned/\"head\" entries and T is the sum over kept/\"tail\" entries), but sparse attention normalizes only over the kept entries (using T alone). This mismatch means the sparse attention output distribution diverges from that of full quadratic attention, causing decoding-time queries to misalign with the appropriate keys from prefill. Delta Attention corrects this by computing a cheap correction term that brings the sparse output distribution back toward the full-attention distribution.\n\n### 2. How the Delta Correction Works (Step by Step)\n\nThe method is elegantly simple:\n\n1. **Compute sparse attention** for all queries as usual: A*V (the standard sparse output).\n2. **Sample every gamma-th query** (default gamma = 64) and compute **full dense attention** for just those sampled queries: tilde{A}V.\n3. **Compute the delta** = (dense output - sparse output) for each sampled query. This difference captures the contribution of the pruned attention entries.\n4. **Broadcast the delta** to all gamma neighbors: for query i, the corrected output is:\n\n   `(corrected output)_i = (A*V)_i + [dense_output_{floor(i/gamma)} - sparse_output_{floor(i/gamma)}]`\n\nThe key insight is that the difference between dense and sparse outputs at a sampled query approximates the missing attention contribution from pruned regions, and this difference varies slowly across nearby queries, so broadcasting it across a window of gamma queries is a good approximation.\n\nThe approximation error is bounded (Lemma 1): `|delta - sum of pruned contributions| <= [H/(H+T)] * max|v_i|`, which is tight when sparsity is good (T >> H).\n\n### 3. The ~1.5% Overhead\n\nThe overhead comes from recomputing dense attention for every 64th query (gamma = 64). At 131K context length:\n\n- Each sampled query attends to the full context (rather than just the sparse window of ~2048 tokens).\n- The additional cost per sampled row is roughly C/(2*gamma) = 131072 / 128 = 1024 extra tokens of attention.\n- As a fraction of full quadratic attention: 1024 / 65536 ~ **1.5%**.\n\nThe operations contributing: (a) selecting the query subset (negligible), (b) dense attention for those queries (the 1.5%), (c) computing the difference and broadcasting (trivial). So the method maintains ~98.5% sparsity over full quadratic attention.\n\n### 4. NeurIPS 2025 Status: Confirmed\n\nYes, the paper was **accepted at NeurIPS 2025** as a **poster presentation** (Thursday, December 4, 2025, San Diego). This is confirmed by the NeurIPS virtual site listing (poster #118545).\n\n---\n\n### Bottom Line\n\nDelta Attention is a plug-in post-processing correction applicable to any sparse attention method. On the 131K RULER benchmark, it recovers an average of 36 percentage points of performance (reaching 88% of full quadratic attention accuracy) when applied on top of sliding window + sink tokens, at only ~1.5% additional cost. At 1M token prefills, this yields a 32x speedup over FlashAttention-2.\n\nSources:\n- [arXiv Abstract Page](https://arxiv.org/abs/2505.11254)\n- [arXiv HTML Full Paper](https://arxiv.org/html/2505.11254)\n- [NeurIPS 2025 Poster Page](https://neurips.cc/virtual/2025/poster/118545)\n- [HuggingFace Paper Page](https://huggingface.co/papers/2505.11254)"
      }
    ],
    "totalDurationMs": 68995,
    "totalTokens": 14631,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 296,
      "cache_read_input_tokens": 13308,
      "output_tokens": 1026,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 296
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1026,
          "cache_read_input_tokens": 13308,
          "cache_creation_input_tokens": 296,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 296,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 5
    }
  },
  "sourceToolAssistantUUID": "d836ffe7-13fa-429a-a578-a7d1ab3b63f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T20:12:52.616Z_

<details><summary>↩ Tool result · `toolu_017fht9B4JXrFWd8UYfjXnGJ`</summary>

```text
Here is a consolidated report of findings across all searches.

---

## 1. Papers Combining Per-Head Adaptive Attention with Speculative Decoding (May-June 2026)

**No paper found that explicitly combines per-head adaptive attention classification with speculative decoding in the May-June 2026 window.** The closest recent work is:

- **Component-Aware Self-Speculative Decoding in Hybrid Language Models** (arXiv:2605.01106, May 1 2026) -- by Hector Borobia et al. This exploits the architectural heterogeneity of hybrid models (e.g., Mamba-2 + attention in Falcon-H1) by isolating the SSM/linear-attention subgraph as a zero-cost internal draft. It operates at the *component* level (attention vs. SSM blocks), not at the *individual head* level. Parallel hybrids achieve acceptance rate alpha=0.68 at k=2, while sequential hybrids yield only alpha=0.038.

- **SpecKV** (arXiv:2605.02888, May 2026) -- a lightweight adaptive controller that selects the speculation length gamma per step using signals from the draft model. Achieves 56% improvement in expected tokens per speculation step. This is adaptive at the *step* level, not the head level.

**Key takeaway:** No one has published head-level adaptive decomposition for self-speculative decoding as of these searches. This appears to be an open niche.

---

## 2. Head-Level Classification/Decomposition for Attention Prediction

Several papers address head-level analysis but none frame it as a decomposition strategy for draft model construction in speculative decoding:

- **Linear Predictability of Attention Heads in Large Language Models** (arXiv:2603.13314, March 2026) -- The most directly relevant paper. Shows that Q, K, V activations of individual heads are linearly predictable from 2-5 "reference" peer heads (mean R^2 ~ 0.76 for keys on C4, frequently > 0.85 on GSM8K). This is a *learned* property, absent at initialization. Applied to KV cache compression (store only reference heads, reconstruct others on-the-fly), but **not connected to speculative decoding**. This paper is a potential threat to novelty if your approach also classifies heads as predictable vs. unpredictable, though the application domain differs.

- **Attention Head Entropy of LLMs** -- Uses entropy of attention patterns to predict correctness of model outputs. Classifies heads by entropy behavior but not for inference acceleration.

- **Safety Head ImPortant Score (Ships)** -- Classifies heads by safety contribution. Not relevant to inference.

- **SpecAttn (arXiv:2510.27641, Oct 2025) and SpecAttn v2 (arXiv:2602.07223, Feb 2026)** -- These are the closest to combining sparse attention with speculative decoding, but they operate at the *token* level (pruning KV cache entries), not at the *head* level. SpecAttn v2 achieves 2.81x throughput over vanilla AR decoding and 1.29x over SOTA sparsity-based self-speculative methods. Importantly, the Speculative Verification paper notes that "mapping attention heads between draft and target models does not provide useful signals for speculation accuracy" -- a finding your paper would need to address or refute if you're claiming head-level decomposition helps.

---

## 3. Current SOTA Throughput for Self-Speculative Decoding on Reasoning Tasks

| Method | Model | Throughput | Speedup |
|--------|-------|-----------|---------|
| **SparseSpec + PillarAttn** | Qwen3-8B | 1460 tok/s (from 690 baseline) | **2.13x** |
| **SpecAttn v2** (Feb 2026) | Various | -- | **2.81x** over AR, 1.29x over prior SOTA |
| **CAS-Spec** (NeurIPS 2025) | Various LLMs | -- | **1.1-2.3x** over AR |
| **SWIFT** (ICLR 2025) | Various | -- | **1.3-1.5x** over AR |

SparseSpec's PillarAttn and SpecAttn v2 represent the current throughput frontier for self-speculative approaches. PillarAttn is notable for reasoning tasks specifically (designed for long-chain reasoning with selective token loading). The absolute throughput of 1460 tok/s on Qwen3-8B is the most concrete number available.

---

## 4. Work Challenging or Extending TriAttention's MRL-Based Head Classification

**No papers were found that reference "TriAttention" or apply Matryoshka Representation Learning (MRL) to attention head classification.** The MRL search results returned only the original MRL embedding work (NeurIPS 2022) and downstream embedding applications. If "TriAttention" is your own unpublished framework, there is no known prior or concurrent work that uses MRL for head-level classification in the attention/inference acceleration space.

However, the **Linear Predictability of Attention Heads** paper (March 2026) implicitly provides an alternative head classification scheme (reference heads vs. predictable heads based on linear regression R^2) that could be seen as a competing framework for head decomposition, even though it doesn't use MRL.

---

## Implications for Novelty of a Head-Adaptive Decomposition Paper

**Strengths of the gap:**
- No existing work combines head-level classification with self-speculative decoding draft construction
- Existing self-speculative methods operate at layer level (LayerSkip, SWIFT, CLaSp), component level (Component-Aware), or token level (SparseSpec, SpecAttn) -- head level is unexplored
- MRL-based head classification has no precedent in this space

**Risks to address:**
1. The Linear Predictability paper (March 2026) establishes that heads have exploitable structure -- you should cite and differentiate
2. The Speculative Verification paper's finding that "head mapping between draft and target does not provide useful signals" needs to be carefully addressed -- your approach would need to show why per-head decomposition *within* the same model (self-speculation) works even if cross-model head mapping doesn't
3. SpecAttn v2's 2.81x speedup sets a high bar for throughput claims
4. Component-Aware Self-Speculative Decoding (May 2026) is the most thematically adjacent concurrent work and should be discussed

---

Sources:
- [Component-Aware Self-Speculative Decoding in Hybrid Language Models](https://arxiv.org/abs/2605.01106)
- [SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection](https://arxiv.org/html/2605.02888)
- [Linear Predictability of Attention Heads in Large Language Models](https://arxiv.org/abs/2603.13314)
- [SpecAttn: Speculating Sparse Attention (v1)](https://arxiv.org/abs/2510.27641)
- [SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding (v2)](https://arxiv.org/abs/2602.07223)
- [SparseSpec: Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding](https://arxiv.org/abs/2512.01278)
- [CAS-Spec: Cascade Adaptive Self-Speculative Decoding](https://arxiv.org/abs/2510.26843)
- [SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acceleration](https://arxiv.org/abs/2410.06916)
- [Speculative Speculative Decoding (ICLR 2026)](https://openreview.net/forum?id=aL1Wnml9Ef)
- [CLaSp: In-Context Layer Skip for Self-Speculative Decoding](https://arxiv.org/html/2505.24196v1)
- [Speculative Verification](https://arxiv.org/html/2509.24328v1)
- [A Benchmark of Speculative Decoding for Efficient LLM Test-Time Scaling](https://www.arxiv.org/pdf/2509.04474)

agentId: a8ae7e4a12f261c81 (use SendMessage with to: 'a8ae7e4a12f261c81' to continue this agent)
&lt;usage>total_tokens: 27311
tool_uses: 16
duration_ms: 115590&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ad8f8b0-0678-4c6b-8391-d170e6a827a9",
  "isSidechain": false,
  "promptId": "871e370c-0079-4344-90e2-68659d98cd6c",
  "type": "user",
  "uuid": "31da14b6-d8d3-4138-b358-8a28f182d181",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for the latest developments (2025-2026) in self-speculative decoding and sparse attention for LLM inference acceleration. I'm looking for:\n\n1. Any new papers (May-June 2026) that combine per-head adaptive attention with speculative decoding\n2. Any papers that do head-level classification/decomposition for attention prediction (not just KV cache compression)\n3. Current SOTA throughput numbers for self-speculative decoding on reasoning tasks\n4. Any work that challenges or extends TriAttention's MRL-based head classification\n\nUse WebSearch with multiple query variations:\n- \"self-speculative decoding head adaptive 2026\"\n- \"per-head attention prediction speculative decoding\"\n- \"MRL head classification attention\"\n- \"sparse attention head decomposition LLM\"\n\nReport findings concisely, focusing on anything that might affect the novelty or framing of a paper about head-adaptive decomposition for self-speculative decoding.",
    "agentId": "a8ae7e4a12f261c81",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is a consolidated report of findings across all searches.\n\n---\n\n## 1. Papers Combining Per-Head Adaptive Attention with Speculative Decoding (May-June 2026)\n\n**No paper found that explicitly combines per-head adaptive attention classification with speculative decoding in the May-June 2026 window.** The closest recent work is:\n\n- **Component-Aware Self-Speculative Decoding in Hybrid Language Models** (arXiv:2605.01106, May 1 2026) -- by Hector Borobia et al. This exploits the architectural heterogeneity of hybrid models (e.g., Mamba-2 + attention in Falcon-H1) by isolating the SSM/linear-attention subgraph as a zero-cost internal draft. It operates at the *component* level (attention vs. SSM blocks), not at the *individual head* level. Parallel hybrids achieve acceptance rate alpha=0.68 at k=2, while sequential hybrids yield only alpha=0.038.\n\n- **SpecKV** (arXiv:2605.02888, May 2026) -- a lightweight adaptive controller that selects the speculation length gamma per step using signals from the draft model. Achieves 56% improvement in expected tokens per speculation step. This is adaptive at the *step* level, not the head level.\n\n**Key takeaway:** No one has published head-level adaptive decomposition for self-speculative decoding as of these searches. This appears to be an open niche.\n\n---\n\n## 2. Head-Level Classification/Decomposition for Attention Prediction\n\nSeveral papers address head-level analysis but none frame it as a decomposition strategy for draft model construction in speculative decoding:\n\n- **Linear Predictability of Attention Heads in Large Language Models** (arXiv:2603.13314, March 2026) -- The most directly relevant paper. Shows that Q, K, V activations of individual heads are linearly predictable from 2-5 \"reference\" peer heads (mean R^2 ~ 0.76 for keys on C4, frequently > 0.85 on GSM8K). This is a *learned* property, absent at initialization. Applied to KV cache compression (store only reference heads, reconstruct others on-the-fly), but **not connected to speculative decoding**. This paper is a potential threat to novelty if your approach also classifies heads as predictable vs. unpredictable, though the application domain differs.\n\n- **Attention Head Entropy of LLMs** -- Uses entropy of attention patterns to predict correctness of model outputs. Classifies heads by entropy behavior but not for inference acceleration.\n\n- **Safety Head ImPortant Score (Ships)** -- Classifies heads by safety contribution. Not relevant to inference.\n\n- **SpecAttn (arXiv:2510.27641, Oct 2025) and SpecAttn v2 (arXiv:2602.07223, Feb 2026)** -- These are the closest to combining sparse attention with speculative decoding, but they operate at the *token* level (pruning KV cache entries), not at the *head* level. SpecAttn v2 achieves 2.81x throughput over vanilla AR decoding and 1.29x over SOTA sparsity-based self-speculative methods. Importantly, the Speculative Verification paper notes that \"mapping attention heads between draft and target models does not provide useful signals for speculation accuracy\" -- a finding your paper would need to address or refute if you're claiming head-level decomposition helps.\n\n---\n\n## 3. Current SOTA Throughput for Self-Speculative Decoding on Reasoning Tasks\n\n| Method | Model | Throughput | Speedup |\n|--------|-------|-----------|---------|\n| **SparseSpec + PillarAttn** | Qwen3-8B | 1460 tok/s (from 690 baseline) | **2.13x** |\n| **SpecAttn v2** (Feb 2026) | Various | -- | **2.81x** over AR, 1.29x over prior SOTA |\n| **CAS-Spec** (NeurIPS 2025) | Various LLMs | -- | **1.1-2.3x** over AR |\n| **SWIFT** (ICLR 2025) | Various | -- | **1.3-1.5x** over AR |\n\nSparseSpec's PillarAttn and SpecAttn v2 represent the current throughput frontier for self-speculative approaches. PillarAttn is notable for reasoning tasks specifically (designed for long-chain reasoning with selective token loading). The absolute throughput of 1460 tok/s on Qwen3-8B is the most concrete number available.\n\n---\n\n## 4. Work Challenging or Extending TriAttention's MRL-Based Head Classification\n\n**No papers were found that reference \"TriAttention\" or apply Matryoshka Representation Learning (MRL) to attention head classification.** The MRL search results returned only the original MRL embedding work (NeurIPS 2022) and downstream embedding applications. If \"TriAttention\" is your own unpublished framework, there is no known prior or concurrent work that uses MRL for head-level classification in the attention/inference acceleration space.\n\nHowever, the **Linear Predictability of Attention Heads** paper (March 2026) implicitly provides an alternative head classification scheme (reference heads vs. predictable heads based on linear regression R^2) that could be seen as a competing framework for head decomposition, even though it doesn't use MRL.\n\n---\n\n## Implications for Novelty of a Head-Adaptive Decomposition Paper\n\n**Strengths of the gap:**\n- No existing work combines head-level classification with self-speculative decoding draft construction\n- Existing self-speculative methods operate at layer level (LayerSkip, SWIFT, CLaSp), component level (Component-Aware), or token level (SparseSpec, SpecAttn) -- head level is unexplored\n- MRL-based head classification has no precedent in this space\n\n**Risks to address:**\n1. The Linear Predictability paper (March 2026) establishes that heads have exploitable structure -- you should cite and differentiate\n2. The Speculative Verification paper's finding that \"head mapping between draft and target does not provide useful signals\" needs to be carefully addressed -- your approach would need to show why per-head decomposition *within* the same model (self-speculation) works even if cross-model head mapping doesn't\n3. SpecAttn v2's 2.81x speedup sets a high bar for throughput claims\n4. Component-Aware Self-Speculative Decoding (May 2026) is the most thematically adjacent concurrent work and should be discussed\n\n---\n\nSources:\n- [Component-Aware Self-Speculative Decoding in Hybrid Language Models](https://arxiv.org/abs/2605.01106)\n- [SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection](https://arxiv.org/html/2605.02888)\n- [Linear Predictability of Attention Heads in Large Language Models](https://arxiv.org/abs/2603.13314)\n- [SpecAttn: Speculating Sparse Attention (v1)](https://arxiv.org/abs/2510.27641)\n- [SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding (v2)](https://arxiv.org/abs/2602.07223)\n- [SparseSpec: Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding](https://arxiv.org/abs/2512.01278)\n- [CAS-Spec: Cascade Adaptive Self-Speculative Decoding](https://arxiv.org/abs/2510.26843)\n- [SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acceleration](https://arxiv.org/abs/2410.06916)\n- [Speculative Speculative Decoding (ICLR 2026)](https://openreview.net/forum?id=aL1Wnml9Ef)\n- [CLaSp: In-Context Layer Skip for Self-Speculative Decoding](https://arxiv.org/html/2505.24196v1)\n- [Speculative Verification](https://arxiv.org/html/2509.24328v1)\n- [A Benchmark of Speculative Decoding for Efficient LLM Test-Time Scaling](https://www.arxiv.org/pdf/2509.04474)"
      }
    ],
    "totalDurationMs": 115590,
    "totalTokens": 27311,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 926,
      "cache_creation_input_tokens": 2089,
      "cache_read_input_tokens": 22240,
      "output_tokens": 2056,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2089
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 926,
          "output_tokens": 2056,
          "cache_read_input_tokens": 22240,
          "cache_creation_input_tokens": 2089,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2089,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 16
    }
  },
  "sourceToolAssistantUUID": "5ad8f8b0-0678-4c6b-8391-d170e6a827a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-10T20:15:29.294Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me synthesize what I've learned from the research:

### Key findings:

1. **"A Mathematical Theory of Top-k Sparse Attention" (arXiv 2512.07647)**: 
   - NOT NeurIPS 2025 (just arXiv preprint, Dec 2025)
   - Provides exact identity for TV distance = tail mass, and deterministic gap bound: TV ≤ 1/(1 + (k/(n-k))·exp(Δ_k))
   - The boundary gap Δ_k = s_k - s_{k+1} is exactly what DecompSpec's Δ_K(h) measures
   - This is the foundational work I need to cite—it gives me the mathematical rigor for gap-based Top-K quality guarantees

2. **DeltaAttention (arXiv 2505.11254)**: 
   - Confirmed NeurIPS 2025 (poster)
   - Corrects distributional shift from sparse attention by computing dense attention for every γ-th query and broadcasting the delta
   - Related concept of "correction term for sparse attention errors"

3. **Date corrections confirmed**:
   - Beyond Exponential Decay: May 2025 (not 2026)
   - SeerAttention-R: June 2025 (not 2026)

4. **TriAttention's continuous weighting scheme** uses a formula that computes normalized scores across heads based on their redundancy and norm characteristics—this is already a form of adaptive weighting for heterogeneous heads. The main evaluations were on Qwen3-8B and DeepSeek-R1-Distill variants, with Qwen3-32B only appearing in the appendix as a deployment demo.

5. **On novelty**: No prior work actually combines head-level classification with self-speculative decoding, which is where my contribution sits. The Linear Predictability paper shows heads have exploitable structure, and Component-Aware works at the component level, but neither applies this to speculative decoding.

The real concern is whether this idea can actually move forward. TriAttention already does continuous adaptive weighting, so the binary classification approach doesn't feel fundamentally new in spirit. The theoretical bound is straightforward, and it's unclear what the practical ceiling actually is. To get this past a 3.5 score, I'd need either minor fixes addressing all reviewer concerns, or a major revision that positions the binary classification plus residual tracking as capturing temporal dynamics that continuous weighting misses—and that second path is the stronger move.

The key distinction I need to sharpen: TriAttention's continuous weighting is spatial, scoring keys at a single timestep, while DecompSpec's binary classification enables temporal residual tracking across draft steps. Since the query changes at each step, the real question becomes which heads can be predicted structurally versus which need explicit tracking. That's genuinely different from what TriAttention does, and it's worth emphasizing that distinction as the core contribution.

Now looking at the budget constraints, I'm over across all categories—Manual by 15h, HIL by 10h, Auto by 20h. Dropping Llama 3.3 70B entirely would save too much (~62 GPU-hours), so instead I should keep it but trim the parameter sweep significantly.

I'm adjusting the approach: reduce the gamma values from three options to two, cut one method from the comparison set, and lower the contingency buffer from 20h to 12h. This gets me about 22 GPU-hours of savings on Llama while preserving the core experimental design. Let me recalculate the full budget with these constraints in place, starting with the calibration and baseline phases, then working through each model's evaluation costs. ) × 0.35h ≈ 88h

Wait, adding TriAttention continuous as a 7th method would increase costs. Let me reconsider.

Actually, the reviewer said to add TriAttention continuous weighting as a baseline. That's a 7th comparison method. Let me think about how to fit this within budget.

Options:
1. Drop one of the existing ablation variants to make room
2. Run TriAttention continuous only on a subset of benchmarks

Looking at my current 6 methods, I could replace TriAttention structural-only with TriAttention continuous-weighted since the continuous version is more informative. They test different aspects—structural-only applies trigonometric scoring to all heads while continuous-weighted uses the weighted combination of trigonometric and norm scoring—but for budget constraints, the stronger baseline makes more sense.

For Llama, that keeps me at 4 benchmarks × 2 γ × 5 methods × 0.35h = 14h wall time, or 28h total.

Now I'm recalculating the full GPU-hour budget across all phases. Phase 0 takes 3 GPU-hours on a single H100. For FP8 validation, Qwen3-32B needs 2 GPU-hours on one H100 while Llama needs 4 GPU-hours across two H100s. Calibration for Llama FP8 adds another 8 GPU-hours, integration work is 25 GPU-hours, and baseline reproduction is 15 GPU-hours. I'm working through the Qwen3-32B experiment costs now.

For the Qwen experiments across 9 benchmarks with 4 gamma values and 6 methods, that's roughly 75.6 GPU-hours. The Llama experiments are more modest at 28 GPU-hours total. Ablations on Qwen3-32B come to about 25 GPU-hours, and I'm adding a 12-hour buffer. Adding this all up gives me 197.6 GPU-hours, which fits under the 200 limit. Let me verify these numbers more carefully by breaking down each resource allocation mode.

For the manual mode, I've got 3 hours for phase 0, 6 hours for FP8 validation, 8 hours for calibration on the Llama FP8 setup, 25 hours for integration work, and 12 hours for baseline reproduction. The main experiments consume 75.6 hours for Qwen3-32B and 28 GPU-hours for Llama, with 25 hours for ablations and 12 hours as a safety buffer—totaling 194.6 hours.

For the HIL and Auto modes, I'm targeting around 200 GPU-hours for each, with Auto having a strict cap. Now I'm thinking through the throughput gains more carefully. SparseSpec achieves a 2.13× speedup on Qwen3-8B, and the draft phase involves sparse attention scoring with stale scores, selecting the top-K tokens, computing sparse attention, and then verifying the results. The scoring phase itself is relatively small, but if the content-dependent heads—which make up about 15% of the total—cause disproportionate selection errors, that could impact the overall efficiency.

Fixing those errors would improve the acceptance rate, which directly reduces wasted verification compute. Looking at the math, if acceptance rate improves from 0.85 to 0.88, the throughput gain is modest, but the real impact shows up at reasoning boundaries where acceptance drops to 0.7—improving that to 0.8 has much more leverage. The realistic picture is that DecompSpec probably gives us 5-15% throughput improvement over SparseSpec, not a 2× jump, but the value lies in better handling of those critical reasoning points.

The contribution actually holds up for EMNLP if I frame it around maintaining accuracy at longer draft lengths and understanding when stale scores work. Now I need to verify that citation the reviewer mentioned—they said "A Mathematical Theory of Top-k" is NeurIPS 2025, but my search shows it's just an arXiv preprint from December 2025, and NeurIPS 2025 was held in December, so the timing doesn't quite line up for acceptance.

I'll cite it accurately as an arXiv preprint and move forward with the revisions: tightening the budget to strictly under 200 hours, adding the missing citations properly differentiated, fixing the date errors, swapping in TriAttention with continuous weighting as an explicit baseline, and completing the remaining changes to the approach.

But I'm second-guessing whether this is truly a minor revision—the reviewer's point about TriAttention's continuous weighting actually challenges a core claim about existing methods not adapting to head heterogeneity. Let me reconsider whether this requires a more substantial rethinking of the contribution.

TriAttention uses continuous weighting to score keys at a single timestep, blending trigonometric and norm components. The crucial distinction is that DecompSpec operates across draft steps—structural heads can analytically update their trigonometric estimates as position changes, while content-dependent heads need residual tracking because their content component shifts unpredictably. Even if TriAttention's weighting is applied at each draft step, the norm components remain stale, especially for low-MRL heads. The real insight is that TriAttention improves spatial scoring across keys at one position, but doesn't address the temporal staleness problem that emerges during speculative decoding.

I should add TriAttention as a baseline in the speculative setting to empirically validate this distinction. Now I'm working through the back-of-envelope calculation to estimate the throughput ceiling. The chain starts with SparseSpec's reported 2.13× throughput at γ=8 on Qwen3-8B, then factors in that content-dependent heads comprise roughly 15% of total heads and likely account for 40-50% of selection errors. If correcting these errors yields a 3-7% Jaccard improvement, that should translate into measurable acceptance rate gains.

The key insight is that while a 5% Jaccard improvement might only yield 2-3% higher acceptance rates, the real value emerges at larger draft lengths—DecompSpec could maintain γ=8 acceptance rates even at γ=12-16, where SparseSpec's acceptance rate drops significantly due to staleness. This suggests a pessimistic scenario of ~5% throughput gain over SparseSpec, but optimistically could reach 20% at γ=16, with the primary benefit being the ability to extend viable draft lengths.

Now I'm factoring in the overhead costs: per-head routing is negligible since it's computed offline, residual storage takes about 0.6GB at 16K context, and refreshing residuals at boundaries adds roughly 0.5% per-step overhead. After accounting for these costs, the net throughput gain drops to around 4-19%, with the largest wins at γ=16 for long reasoning chains where I'd expect 15-20% improvement over SparseSpec, but minimal gains below 5% at shorter sequences with γ=4.

For the paper to be convincing, I need to show that the benefits at higher γ values are actually meaningful and that the overhead stays minimal when draft lengths are short. I'm also realizing I need to be careful about how I cite the sparse attention paper—the reviewer called it NeurIPS 2025, but I can't confirm that venue, so I should cite it as an arXiv preprint from December 2025 instead.

Now I'm working through the key revisions: updating all resource estimates to stay under 200 GPU-hours total, swapping out the structural-only TriAttention baseline for a continuous-weighted version, adding throughput estimates, fixing the dates, incorporating the two new citations properly, and acknowledging TriAttention's limited evaluation on Qwen3-32B while adding calibration for MRL validation. I also need to reconsider my comparison methods—currently I have six baselines, but I should think about whether that's the right set.

For the TriAttention baseline specifically, the reviewer wants continuous-weighted included. I could replace the structural-only version with it to stay within budget, but I'm realizing they actually test different things: structural-only isolates whether pure trigonometric scoring works without any norm component, while continuous-weighted tests whether continuous adaptation to head heterogeneity is sufficient on its own. The continuous-weighted approach is strictly more informative since it subsumes structural-only as a special case, so that's probably the better choice to keep.

My final six methods are now the main DecompSpec variant with per-head adaptive parameters and segment-aware residuals, a naive ablation using global parameters, SparseSpec as a uniform baseline, TriAttention with continuous weighting but no temporal residual tracking, an exponential decay ablation, and full attention as the oracle. This setup directly answers whether binary classification plus residual tracking outperforms continuous weighting without that temporal component. For Llama I'll drop the exponential decay variant and run the remaining five with the appropriate gamma settings.

Now I'm working through the precise GPU budget calculations across different experimental phases—starting with the oracle ceiling and FP8 validation, then moving through calibration, integration, and baseline reproduction before tackling the full experimental runs across both models. All three modes stay within the 200h GPU budget. Now I'm drafting the full revision, being careful about venue accuracy for that sparse attention paper—my research suggests it's an arXiv preprint from December 2025 rather than a NeurIPS 2025 paper, so I'll cite it that way to be precise. I'm also double-checking the timeline since the paper was posted December 8th and NeurIPS ran December 9-15. I'm realizing the arXiv ID pattern confirms my suspicion—a December 2025 posting (2512.xxxx) is too late for the main NeurIPS 2025 conference, which would've had acceptances in September. It could be a workshop paper, but I'll just cite it conservatively as "arXiv Dec 2025" to avoid making claims I can't verify. Now I need to format the revised JSON with all the key changes: tightening the budget to 200 hours with reduced hyperparameter sweeps for Llama, adding the two new citations, and fixing the timeline details. I'm seeing the reviewer's core concerns: strict budget compliance, whether TriAttention should be a baseline if DecompSpec clearly outperforms it, and back-of-envelope throughput estimates. The MRL validation gap for Qwen3-32B is also critical—I need to explicitly acknowledge that the 84.7% success rate might not hold there, and make sure the Phase 0 calibration step includes MRL distribution validation for that model specifically. The oracle ceiling analysis will help validate whether those MRL assumptions transfer. Now I'm ready to finalize the revision with these points addressed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31da14b6-d8d3-4138-b358-8a28f182d181",
  "isSidechain": false,
  "requestId": "req_011CauVtfApd2o69PLkNrwci",
  "type": "assistant",
  "uuid": "fd1d2d9d-1161-4e45-b8b0-6080c292dca7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017z9oHavLXHBgq4V1zS8xsV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7238,
      "cache_read_input_tokens": 29084,
      "output_tokens": 16718,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7238,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16718,
          "cache_read_input_tokens": 29084,
          "cache_creation_input_tokens": 7238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7238
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

_source line 21 · 2026-05-10T20:19:22.663Z_

Now let me synthesize the research findings before drafting the revision.

**Research summary:**
- **"A Mathematical Theory of Top-k Sparse Attention" (arXiv 2512.07647)**: arXiv preprint Dec 2025 (NOT confirmed NeurIPS 2025). Provides exact TV-distance identity and deterministic gap bound: TV ≤ 1/(1 + (k/(n-k))·exp(Δ_k)). Directly relevant to our rank-swap analysis via the boundary gap.
- **DeltaAttention (arXiv 2505.11254)**: Confirmed NeurIPS 2025 poster. Corrects sparse attention distributional shift by computing dense attention for every γ-th query and broadcasting the delta. ~1.5% overhead.
- **Date corrections confirmed**: Beyond Exponential Decay = May 2025, SeerAttention-R = June 2025.
- **TriAttention continuous weighting**: S_norm(k) = Σ_f (1-R_f)·E[||q_f||]·||k_f|| provides continuous adaptation to head heterogeneity at a single timestep. But this is *spatial* adaptation (across keys), not *temporal* (across draft steps). Main eval uses Qwen3-8B, not 32B.
- **Novelty check**: No existing work combines head-level classification with self-speculative decoding. The gap remains genuine.

The critical distinction to sharpen: TriAttention's continuous weighting improves *single-step* scoring quality, but doesn't solve *temporal staleness* across draft steps. DecompSpec's contribution is fundamentally about temporal prediction — which heads' scores can be analytically evolved across positions vs. which need explicit tracking. This makes the approaches complementary, not competing.

This is a **minor** revision — the core approach is sound, but needs budget compliance, missing citations, date fixes, TriAttention continuous baseline, and throughput ceiling estimates.

Let me now produce the complete revised JSON.

```json
{
  "title": "Variance-Bounded Head-Adaptive Decomposition for Self-Speculative Reasoning Decoding",
  "change_type": "minor",
  "core_problem": "Self-speculative decoding methods (SparseSpec, SpecAttn) select critical tokens for sparse draft attention by reusing verification-stage attention scores as a free oracle, but these scores become stale over γ draft steps. The attention prediction landscape has responded to this staleness problem in multiple ways—SFI (2026) reuses a fixed sparse support set and refreshes at semantic boundaries, GVR (2026) uses the previous step's Top-K as a temporal predictor, Expected Attention (2025) predicts future attention via Gaussian moment-generating functions—but ALL existing approaches treat attention heads uniformly during temporal prediction. Ada-KV (NeurIPS 2025) proved via an L1 eviction loss upper bound (Theorem 3.3) that uniform head budget allocation is suboptimal, and HeadKV (ICLR 2025) demonstrated that per-head differential KV cache treatment can retain 1.5% of cache at 97% performance. Yet both operate on runtime cache retention budgets, not on the temporal prediction strategy itself. TriAttention (April 2026) provides continuous spatial adaptation via (1−R_f)-weighted norm scoring—when a head has low MRL R_f, the norm component S_norm(k) = Σ_f (1−R_f)·E[||q_f||]·||k_f|| contributes more, effectively adapting scoring quality per head at a single timestep. However, this spatial adaptation does not address temporal staleness: when reusing scores across γ draft steps, the norm component itself becomes stale because it depends on the current query's magnitude properties, which change at each position. Meanwhile, Tzachristas et al. (Dec 2025) established a rigorous mathematical framework showing that the boundary gap Δ_k = s_k − s_{k+1} exponentially controls Top-K truncation quality (TV ≤ 1/(1 + (k/(n−k))·exp(Δ_k))), but this analysis assumes exact scores and does not account for prediction error. Urrutia et al. (2025) proved that positional and symbolic attention behaviors are mutually exclusive per head, and TriAttention showed ~85% of GQA heads have MRL R_h > 0.95 (concentrated query directions), meaning their attention scores are analytically predictable from RoPE structure alone. The remaining ~15% of content-dependent heads have high residual variance and require explicit tracking. No existing method provides per-head temporal prediction error bounds that connect MRL concentration to attention score staleness across draft steps, nor differentiates heads by their intrinsic temporal predictability for self-speculative scoring. Furthermore, 'Beyond Exponential Decay' (May 2025) demonstrates that in LLM generation, errors concentrate at sparse decision points (~5-10% of tokens) rather than accumulating gradually—suggesting the commonly assumed exponential decay model is wrong.",
  "opportunity": "We identify a theoretical gap that unifies and improves upon the fragmented attention prediction landscape. The key insight: the temporal prediction problem (how well can stale scores predict future attention?) decomposes per-head in a way that spatial adaptation alone cannot capture. TriAttention's (1−R_f) continuous weighting adapts the scoring formula at each timestep but does not model how scores evolve across draft positions—its norm component E[||q_f||]·||k_f|| is itself stale when reused from a previous step. DecompSpec addresses the complementary temporal dimension: for structural heads with high MRL, the trigonometric component S_struct(k,Δ) = E[q_f]^T R(Δ) k can be analytically evolved to any future position Δ via rotation matrix updates (exact, not approximate), while for content-dependent heads, explicit residual tracking is necessary. Specifically, for head h with MRL R_h, the structural estimator has mean-squared temporal prediction error bounded by MSE_h ≤ (1 − R_h²)·σ²_q·||k||²/d. Building on Tzachristas et al.'s gap-based Top-K quality framework—which proves that exact-score Top-K quality depends exponentially on the boundary gap—we extend this to the prediction setting: the probability that the structural predictor produces a rank swap at the Top-K boundary for head h is bounded by P(swap) ≤ exp(−Δ_K(h)²/(4·MSE_h)). This connects MRL concentration to Top-K selection quality via the per-head attention gap Δ_K(h), yielding a per-head adaptive threshold θ_h that jointly considers temporal predictability (MRL) and error tolerance (attention gap). Three consequences: (1) For structural heads where the bound is small relative to their attention gap, temporal prediction is reliable at any draft distance. (2) For content-dependent heads where the bound exceeds their attention gap tolerance, explicit residual tracking is necessary. (3) The per-head threshold θ_h produces genuinely different classifications than a naive MRL cutoff: a peaked-attention head (Δ_K=0.5) with R=0.94 gets θ_h≈0.93 → classified as structural; a flat-attention head (Δ_K=0.1) with R=0.96 gets θ_h≈0.997 → classified as content-dependent. A naive global θ=0.95 misclassifies both. This operates upstream of Ada-KV (which optimizes runtime eviction budgets) and is complementary to TriAttention's spatial adaptation (which improves single-step scoring quality). Combined with SFI's finding that attention support is temporally stable within semantic segments, we replace the unjustified exponential decay model with a segment-aware piecewise residual model. DeltaAttention (NeurIPS 2025) showed that sparse attention errors can be efficiently corrected via lightweight delta terms, validating the residual correction paradigm; DecompSpec applies this paradigm selectively to the ~15% content-dependent heads during temporal prediction, rather than uniformly across all attention computation.",
  "landscape": "SparseSpec (Dec 2025, arXiv:2512.01278) achieves 2.13× throughput via PillarAttn self-speculation, reusing verification attention scores with k=8 stride; evaluated on Qwen3-1.7B/8B/14B; code at github.com/sspec-project/SparseSpec. SpecAttn (Feb 2026, arXiv:2602.07223) improves to 2.81× with verification-guided sparse attention co-design. Both inherit the γ-staleness limitation, applying uniform stale scores across all heads. Slow-Fast Inference (SFI, March 2026, arXiv:2603.12038) exploits temporal stability of attention support within semantic segments, achieving 14.4× throughput via event-driven sparse/dense alternation with Tmax=64 refresh budget; evaluated on Qwen3-0.6B/4B/30B/235B; treats all heads uniformly. Guess-Verify-Refine (GVR, April 2026, arXiv:2604.22312) uses previous step's Top-K as temporal prediction signal for Blackwell hardware, 1.88× speedup; targets DeepSeek-V3 at 100K context; uniform across heads. Expected Attention (Oct 2025, arXiv:2510.00636, under review ICLR 2026) predicts future attention via Gaussian MGF with per-head adaptive compression; targets KV cache pruning, not self-speculative scoring. AttentionPredictor (Feb 2025, arXiv:2502.04077, NeurIPS 2025) learns a lightweight convolution model for attention prediction, 13× KV compression; requires training. HeadKV (ICLR 2025, arXiv:2410.19258) performs head-level KV cache compression via offline probe-based importance scores, retaining 1.5% of KV cache at 97% performance; key precedent for per-head treatment but uses task-specific probes for KV retention, not architecture-intrinsic classification for temporal prediction strategy. Ada-KV (NeurIPS 2025, arXiv:2407.11550) proves uniform head budget allocation is suboptimal (Theorem 3.3), proposing global Top-B adaptive allocation for eviction budgets. TriAttention (April 2026, arXiv:2604.04921) provides position-aware structural scoring via trigonometric series, achieving 2.5× throughput for KV compression; reports 84.7% of GQA heads and 96.6% of MLA heads have R>0.95; critically, provides continuous head-adaptive weighting via (1−R_f)-scaled norm component S_norm, adapting scoring quality per head at each timestep. Main evaluation covers Qwen3-8B, DeepSeek-R1-Distill variants, GPT-OSS-20B (Qwen3-32B appears only in deployment appendix)—the ~85% structural head fraction has not been validated on larger models; code at github.com/WeianMao/triattention. Distinction from DecompSpec: TriAttention's continuous weighting is spatial (adapts across keys at one position); DecompSpec's binary classification enables temporal residual tracking (across positions during drafting). Tzachristas et al. (Dec 2025, arXiv:2512.07647) establishes rigorous mathematical theory of Top-K sparse attention via total variation distance, proving TV = tail mass (exact identity) and the deterministic gap bound TV ≤ 1/(1 + (k/(n−k))·exp(Δ_k)). This provides the mathematical foundation for gap-based Top-K quality certificates with exact scores; DecompSpec extends this framework to the prediction setting, bounding rank-swap probability under structural estimation error. DeltaAttention (May 2025, arXiv:2505.11254, NeurIPS 2025) corrects distributional shift from sparse attention truncation via lightweight delta terms computed from periodic dense attention samples (~1.5% overhead); validates the residual correction paradigm. DecompSpec applies selective residual correction to content-dependent heads during temporal prediction rather than uniform correction across all attention. DuoAttention (ICLR 2025) pioneered retrieval/streaming head taxonomy. LycheeDecode (ICLR 2026, arXiv:2602.04541) extends with HardKuma-based learned binary classification, 2.7× speedup at 128K. SeerAttention-R (June 2025, arXiv:2506.08889) uses learned gating for GQA-aligned sparse attention in reasoning, near-lossless accuracy at 90% sparsity. Self-Indexing KVCache (March 2026, arXiv:2603.14224, AAAI 2026) unifies compression and sparse retrieval via sign-based 1-bit VQ. Urrutia et al. (Nov 2025, arXiv:2511.11579) proved positional/symbolic mutual exclusivity per head. Beyond Exponential Decay (May 2025, arXiv:2505.24187) challenges exponential error accumulation—showing errors concentrate at sparse key tokens (~5-10%). Gibson (Oct 2025, arXiv:2510.03315) decomposes attention into structural/content components on GPT2-Small. Flux Attention (April 2026, arXiv:2604.07394) identifies load imbalance from per-head dynamic sparsity. Component-Aware Self-Speculative Decoding (May 2026, arXiv:2605.01106) exploits SSM/attention heterogeneity at component level, not head level. SpecKV (May 2026, arXiv:2605.02888) adaptively selects γ using confidence signals. EvoSparse (ACL 2026) addresses evolving token importance. Linear Predictability of Attention Heads (March 2026, arXiv:2603.13314) shows inter-head QKV linear structure. No existing work provides per-head temporal prediction error bounds connecting MRL to attention score staleness with gap-adaptive thresholds, nor applies head-adaptive temporal decomposition with segment-aware residual tracking specifically for self-speculative draft token selection.",
  "approach": "We propose DecompSpec, which provides variance-bounded head-adaptive temporal attention prediction for self-speculative decoding, with four contributions:\n\n**Phase 0: Oracle Ceiling Analysis + MRL Validation (Gating Experiment, ~5h on 1× H100).** Before the full pipeline, we quantify (a) the maximum possible improvement from head-selective decomposition and (b) whether TriAttention's MRL statistics transfer to Qwen3-32B (since TriAttention's main experiments cover only Qwen3-8B and similar-scale models). We run full-attention generation on 50 AIME25 problems with Qwen3-32B BF16, recording oracle attention scores and computing per-head MRL R_h and attention gap Δ_K(h) statistics. Retrospectively, we compare Top-K (K=256) token selection under four scoring approaches: (a) SparseSpec stale reuse at γ=16, (b) TriAttention continuous-weighted scoring (trigonometric + (1−R_f)·norm, reused from verification step—tests whether spatial adaptation alone addresses staleness), (c) head-selective oracle (structural for high-R_h heads, oracle attention for the rest), (d) full oracle. The ceiling = Jaccard(c) − max(Jaccard(a), Jaccard(b)) quantifies the maximum gain from temporal decomposition beyond what spatial adaptation provides. Decision gate: if ceiling > 3% Jaccard improvement, proceed; if < 2%, reconsider scope. Additionally, we measure what fraction of selection errors under approaches (a) and (b) are attributable to content-dependent heads.\n\n**Back-of-envelope throughput ceiling:** SparseSpec achieves 2.13× at γ=8. At γ=16, acceptance rates drop due to staleness. If content-dependent heads (~15% of heads) cause ~40-50% of selection errors: (Pessimistic) 3% Jaccard improvement → ~1-2% higher acceptance rate → ~5-8% throughput gain over SparseSpec at γ=16, primarily from enabling longer viable draft lengths. (Moderate) 5% Jaccard improvement → ~3% higher acceptance rate → ~10-15% throughput gain at γ=16. (Optimistic) 7% Jaccard improvement → ~4-5% higher acceptance rate → ~15-20% throughput gain at γ=16, with the largest gains at reasoning step boundaries where staleness is worst. The scoring overhead (residual storage ~0.6GB at 16K, boundary refresh ~0.5% compute per step) is small relative to the acceptance rate gains in moderate/optimistic scenarios. The primary value is extending viable draft length γ: if DecompSpec maintains γ=8 acceptance rates at γ=12-16, the throughput gain compounds with the longer draft window.\n\n**Contribution 1: Per-Head Adaptive Variance Bound.** We prove that for head h with MRL R_h, the structural-only estimator Ŝ_struct(k,Δ) = E[q_f]^T R(Δ) k achieves MSE_h ≤ (1 − R_h²)·σ²_q·||k||²/d (from circular variance identity, Mardia & Jupp 1999). The practical contribution extends Tzachristas et al.'s gap-based Top-K quality framework from the exact-score setting to the prediction setting: the probability that structural prediction produces a rank swap at the Top-K boundary is P(swap) ≤ exp(−Δ_K(h)²/(4·MSE_h)). This connects their deterministic gap bound (which assumes exact scores) to our setting of estimated scores with bounded prediction error. The per-head threshold θ_h = sqrt(1 − Δ_K(h)²/(4·|ln(ε)|·σ²_q·||k||²/d)) produces materially different classifications than a naive MRL cutoff, as described previously. During offline calibration (~100 forward passes), we estimate R_h, Δ_K(h), and the adaptive threshold map. Sensitivity ablation: (a) per-head adaptive θ_h, (b) naive global θ=0.95, (c) MRL-percentile cutoff—if (a) and (b)/(c) agree on >95% of heads, we report honestly that the bound's contribution is primarily theoretical.\n\n**Contribution 2: Segment-Aware Residual Model.** We replace exponential decay with piecewise-constant residual tracking within semantic segments, motivated by SFI's temporal stability finding and Beyond Exponential Decay's demonstration that errors concentrate at sparse decision points. Within a semantic segment, the content residual R(k) is held constant. At segment boundaries—detected via token-level triggers ({., ?, !, \\n, step markers}) plus staleness budget T_max=32—a lightweight refresh re-scores only content-dependent heads (~15% of heads). This is conceptually related to DeltaAttention's periodic dense-attention sampling for distributional correction, but applies selectively to content-dependent heads during temporal prediction rather than uniformly for truncation correction. We ablate: piecewise-constant vs. exponential vs. linear vs. learned piecewise decay.\n\n**Contribution 3: GQA-Aware Head Classification.** For GQA models (Qwen3-32B: 64Q/8KV; Llama 3.3 70B: 64Q/8KV), MRL and Δ_K are computed per-query-head then aggregated to per-KV-head classification using min-MRL and min-Δ_K across the GQA group (conservative: classify as content-dependent if ANY query head in the group has θ_h above its R_h). Validated by comparing min vs. mean aggregation.\n\n**Concrete Method:**\n(0) Offline head classification: Compute per-query-head MRL R_h (for Qwen3-32B, validate that MRL statistics are consistent with TriAttention's 8B findings—since TriAttention did not evaluate 32B in main experiments; for Llama 3.3 70B FP8, compute from ~100 forward passes). Additionally compute per-head Δ_K(h) and adaptive thresholds θ_h. Aggregate via conservative min-rule per GQA group. Validate MRL/Δ_K distributions under FP8. (1) During verification at position t: For all heads, compute full attention S_full(k). For content-dependent heads only, store residual R(k) = S_full(k) − S_struct(k, Δ_t). Storage: ~15% of heads × KV length. (2) During draft step j (position t+j): Structural heads: S_draft(k,j) = S_struct(k, Δ_{t+j}) via trigonometric rotation (O(n), exact). Content-dependent heads: if within current segment, S_draft(k,j) = S_struct(k, Δ_{t+j}) + R(k); if at segment boundary, refresh R(k) via lightweight re-scoring. (3) Per-step trigonometric validation at per-token granularity (TriAttention uses batch updates every 128 tokens). (4) Token selection: Top-K union across all heads, producing unified sparse token set for PillarAttn (same hardware-efficient pattern as SparseSpec).\n\n**Integration Plan:** Build on SparseSpec's codebase, replacing PillarAttn's uniform stale-score reuse with head-adaptive decomposed scoring. SparseSpec tested only up to Qwen3-14B; we allocate 10h of the 12h buffer for SWIFT integration (ICLR 2025) as contingency if SparseSpec fails at 32B scale.\n\n**Memory Management:** Qwen3-32B BF16 ≈65GB on 1× H100-80GB, leaving ~15GB. KV cache at 16K ≈ 4GB, leaving ~11GB—workable for batch-1. Long-context benchmarks restricted to ≤16K in BF16 or use FP8 (weights ~33GB, ample headroom). Llama 3.3 70B FP8 on 2× H100-80GB (weights ~70GB, leaving ~90GB), short-context only. FP8 MRL/Δ_K validation is a gating experiment.\n\n**Evaluation:**\nPhase 0 (gating): Oracle ceiling + MRL validation on 50 AIME25 problems (~5h total, 1× H100). FP8 MRL/Δ_K validation (~2h per model).\n\nModels: Qwen3-32B (1× H100-80GB, primary) and Llama 3.3 70B (2× H100-80GB FP8, secondary).\n\nQwen3-32B benchmarks (9 total): AIME25, MATH500, HumanEval, MMLU, MT-Bench (BF16); LongBench (≤16K), RULER (≤16K) (BF16 or FP8); WikiText-103, C4 (BF16). Draft lengths γ ∈ {4, 8, 12, 16}.\n\nLlama 3.3 70B FP8 benchmarks (4 short-context): MMLU, HumanEval, MT-Bench, WikiText-103. Draft lengths γ ∈ {4, 16}.\n\nMethods compared on Qwen3-32B (6): DecompSpec-adaptive (main: per-head adaptive θ_h + segment-aware residual), DecompSpec-naive (ablation: global θ=0.95 + segment-aware residual), SparseSpec (uniform stale reuse), TriAttention continuous-weighted (continuous (1−R_f) spatial adaptation, stale reuse across draft steps—directly tests whether spatial head adaptation alone addresses temporal staleness), DecompSpec-exp (exponential decay ablation), full attention (oracle upper bound).\n\nMethods compared on Llama 3.3 70B (5): DecompSpec-adaptive, DecompSpec-naive, SparseSpec, TriAttention continuous-weighted, full attention.\n\nMetrics: throughput (tokens/sec), token acceptance rate, downstream task accuracy, Jaccard with oracle Top-K, Kendall-τ rank correlation.\n\nKey ablations on Qwen3-32B: (a) per-head adaptive θ_h vs. naive θ=0.95 vs. MRL-percentile cutoff; (b) piecewise-constant vs. exponential vs. linear vs. learned piecewise decay at γ=16; (c) GQA aggregation: min-MRL vs. mean-MRL; (d) selection agreement at reasoning boundaries vs. stable regions; (e) per-step trigonometric precision; (f) FP8 vs. BF16 MRL/Δ_K distribution comparison; (g) overhead breakdown vs. throughput gain; (h) T_max ∈ {16, 32, 64}; (i) oracle ceiling decomposition: error attribution to content-dependent heads; (j) DecompSpec-adaptive vs. TriAttention continuous-weighted: does binary classification + temporal residual tracking outperform continuous spatial adaptation with stale reuse? (This is the critical novelty-establishing comparison.)",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~188h H100-80GB active + 12h buffer = 200h total (Phase 0 oracle ceiling + MRL validation ~5h, FP8 validation ~4h [2h Qwen + 2h×2GPU Llama], MRL+Δ_K calibration for Llama FP8 ~8h [4h wall × 2 GPU], integration ~25h, baseline reproduction ~12h, Qwen3-32B: 9 benchmarks × 4 γ × 6 methods × 0.35h ≈ 76h [1× H100], Llama 3.3 70B FP8: 4 benchmarks × 2 γ × 5 methods × 0.35h = 14h wall ≈ 28 GPU-h [2× H100], ablations ~25h on Qwen3-32B, buffer 12h [10h SWIFT contingency + 2h misc]). Strictly ≤200 GPU-h.",
      "gpu_utilization": "~30-35% — GPU idles while human writes integration code and debugs",
      "timeline": "6-8 weeks (1 day Phase 0 gating, 2 weeks integration + calibration, 2-3 weeks experiments, 2 weeks analysis/writing)",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "$600 (200h × $3.00/hr H100)"
    },
    "human_in_loop": {
      "gpu_hours": "~200h H100-80GB strictly (agent explores more θ configurations including per-head adaptive vs. naive comparison, boundary detection strategies, GQA aggregation variants, T_max sweep, HeadKV-style baseline, TriAttention continuous-weighted comparison across benchmarks)",
      "gpu_utilization": "~60-65% — agent queues experiments, human reviews daily",
      "timeline": "16-20 days (1 day Phase 0 gating + FP8 validation, 3-4 days integration + calibration, 8-9 days experiments, 4-5 days analysis/writing)",
      "team": "1 researcher, ~30min/day oversight",
      "claude_api_cost": "$80-130",
      "estimated_gpu_cost": "$600 (200h × $3.00/hr)",
      "risk_note": "SparseSpec codebase tested only up to Qwen3-14B; scaling to 32B may require kernel modifications. SWIFT contingency: 10h explicitly budgeted within the 12h buffer. FP8 MRL/Δ_K validation gates Llama experiments. Oracle ceiling analysis gates the entire pipeline."
    },
    "auto_research": {
      "gpu_hours": "~200h H100-80GB strictly (comprehensive sweep: per-head adaptive θ across ε ∈ {0.05, 0.1, 0.2, 0.3}, T_max ∈ {16, 32, 64}, GQA aggregation variants, extended to Qwen3-8B for direct SparseSpec comparison on 2 key benchmarks, HeadKV-style baseline; budget achieved by restricting Llama to 4 benchmarks × 2 γ × 4 methods)",
      "gpu_utilization": "~85-90% — continuous experiment pipeline",
      "timeline": "16-19 days with 2× H100 (Phase 0 gating: 1 day, FP8 validation: 0.5 day, integration + calibration: 3-4 days, experiments: 8-10 days, paper: 3-4 days)",
      "team": "0 (2h initial setup)",
      "claude_api_cost": "$200-300",
      "estimated_gpu_cost": "$600 (200h × $3.00/hr)",
      "speed_bottleneck": "Llama 3.3 70B FP8 requires 2× H100-80GB. Gating dependencies: (1) Phase 0 oracle ceiling must show >3% Jaccard improvement beyond TriAttention continuous-weighted, (2) FP8 MRL validation must pass, before committing to full pipeline.",
      "risk_note": "If FP8 distorts MRL/Δ_K distributions, fall back to Qwen3-32B-only with BF16 short-context and FP8 long-context. If SparseSpec fails at 32B, 10h SWIFT contingency activated. If oracle ceiling <2%, pivot to analysis paper studying gap-adaptive threshold contribution in isolation."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026, commitment deadline August 2, 2026)"
  ],
  "level": "solid-to-strong",
  "key_references": [
    "Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning (HeadKV, ICLR 2025, arXiv:2410.19258)",
    "Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference (NeurIPS 2025, arXiv:2407.11550)",
    "Decoupling Positional and Symbolic Attention Behavior in Transformers (Urrutia et al., arXiv Nov 2025, 2511.11579)",
    "TriAttention: Efficient Long Reasoning with Trigonometric KV Compression (arXiv April 2026, 2604.04921)",
    "Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding (SparseSpec, arXiv Dec 2025, 2512.01278)",
    "SpecAttn: Co-Designing Sparse Attention with Self-Speculative Decoding (arXiv Feb 2026, 2602.07223)",
    "Slow-Fast Inference: Training-Free Inference Acceleration via Within-Sentence Support Stability (SFI, arXiv March 2026, 2603.12038)",
    "Guess-Verify-Refine: Data-Aware Top-K for Sparse-Attention Decoding on Blackwell via Temporal Correlation (GVR, arXiv April 2026, 2604.22312)",
    "Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution (arXiv Oct 2025, 2510.00636, under review ICLR 2026)",
    "AttentionPredictor: Temporal Patterns Matter for KV Cache Compression (arXiv Feb 2025, 2502.04077, NeurIPS 2025)",
    "A Mathematical Theory of Top-k Sparse Attention via Total Variation Distance (arXiv Dec 2025, 2512.07647)",
    "DeltaAttention: Fast and Accurate Sparse Attention Inference by Delta Correction (NeurIPS 2025, arXiv:2505.11254)",
    "Beyond Exponential Decay: Rethinking Error Accumulation in Large Language Models (arXiv May 2025, 2505.24187)",
    "LycheeDecode: Accelerating Long-Context LLM Inference via Hybrid-Head Sparse Decoding (ICLR 2026, arXiv:2602.04541)",
    "DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads (ICLR 2025, arXiv:2410.10819)",
    "SeerAttention-R: Sparse Attention Adaptation for Long Reasoning (arXiv June 2025, 2506.08889)",
    "Decomposing Attention To Find Context-Sensitive Neurons (Gibson, arXiv Oct 2025, 2510.03315)",
    "Flux Attention: Context-Aware Hybrid Attention for Efficient LLMs Inference (arXiv April 2026, 2604.07394)",
    "Component-Aware Self-Speculative Decoding in Hybrid Language Models (arXiv May 2026, 2605.01106)",
    "SpecKV: Adaptive Speculative Decoding with Compression-Aware Gamma Selection (arXiv May 2026, 2605.02888)",
    "Linear Predictability of Attention Heads in Large Language Models (arXiv March 2026, 2603.13314)",
    "Evolving Sparsity: Leveraging Token Importance Dynamics for Efficient LLM Decoding with Sparse Attention (EvoSparse, ACL 2026)",
    "SWIFT: On-the-Fly Self-Speculative Decoding for LLM Inference Acceleration (ICLR 2025)",
    "SpecGuard: From Tokens to Steps — Verification-Aware Speculative Decoding for Efficient Multi-Step Reasoning (arXiv April 2026, 2604.15244)",
    "Self-Indexing KVCache: Predicting Sparse Attention from Compressed Keys (AAAI 2026, arXiv:2603.14224)",
    "Directional Statistics (Mardia & Jupp, 1999)"
  ],
  "description": "Self-speculative decoding methods (SparseSpec 2.13×, SpecAttn 2.81×) reuse verification-stage attention scores for draft-phase token selection, but these scores grow stale over γ draft steps. Recent approaches address temporal prediction uniformly: SFI (2026) reuses fixed sparse support with periodic refresh, GVR (2026) exploits previous-step Top-K as temporal predictor, Expected Attention (2025) predicts via Gaussian MGF. TriAttention (2026) provides continuous spatial head adaptation via (1−R_f)-weighted norm scoring, adapting quality per head at each timestep—but this spatial adaptation does not solve temporal staleness, as the norm component itself becomes stale when reused across draft steps. Tzachristas et al. (2025) established rigorous gap-based Top-K quality certificates (TV ≤ 1/(1 + (k/(n−k))·exp(Δ_k))) but for exact scores, not predicted scores. No method provides per-head temporal prediction error bounds or exploits the spatial-temporal decomposition for self-speculative scoring. We propose DecompSpec with four contributions. (0) Oracle Ceiling Analysis + MRL Validation: A gating experiment on Qwen3-32B (whose MRL statistics have not been validated—TriAttention's main experiments cover only ≤20B models) comparing uniform stale reuse, TriAttention continuous-weighted reuse, and head-selective oracle scoring against full-attention Top-K, quantifying the maximum gain from temporal decomposition beyond spatial adaptation. Back-of-envelope throughput ceiling: pessimistic 5-8% gain over SparseSpec at γ=16 (3% Jaccard improvement), moderate 10-15% (5% Jaccard), optimistic 15-20% (7% Jaccard), with scoring overhead ~0.5% compute per step. (1) Per-Head Adaptive Variance Bound: MSE_h ≤ (1−R_h²)·σ²_q·||k||²/d for temporal prediction error, extended to rank-swap probability P(swap) ≤ exp(−Δ_K(h)²/(4·MSE_h)) by connecting to Tzachristas et al.'s gap-based framework. The per-head threshold θ_h = f(R_h, Δ_K(h), ε) produces materially different classifications than naive MRL cutoffs—peaked-attention heads with moderate MRL may be reliably structural, while flat-attention heads with high MRL may need residual tracking. We explicitly ablate adaptive θ_h vs. naive cutoffs and commit to reporting honestly if they converge. (2) Segment-Aware Residual Model: Motivated by SFI's temporal stability finding and Beyond Exponential Decay (May 2025)'s demonstration that errors concentrate at sparse decision points, we replace exponential decay with piecewise-constant residual tracking, refreshing only ~15% content-dependent heads at reasoning boundaries. Related to DeltaAttention's (NeurIPS 2025) residual correction paradigm but applied selectively during temporal prediction rather than uniformly for truncation correction. (3) GQA-Aware Classification via conservative min-MRL/min-Δ_K aggregation. Structural heads receive exact trigonometric updates at any draft distance; content-dependent heads receive segment-aware residual tracking. Per-head routing is confined to the scoring phase; the attention kernel operates on a unified Top-K set (same as SparseSpec's PillarAttn). We differentiate from HeadKV (offline probes for KV retention), Ada-KV (runtime eviction budgets), and TriAttention (spatial continuous weighting) by providing architecture-intrinsic temporal classification with theoretical error bounds. Evaluation: Qwen3-32B (9 benchmarks, γ ∈ {4,8,12,16}, 6 methods including TriAttention continuous-weighted baseline) and Llama 3.3 70B FP8 (4 benchmarks, γ ∈ {4,16}, 5 methods). Critical comparison: DecompSpec (binary temporal classification + residual tracking) vs. TriAttention continuous-weighted (continuous spatial adaptation, stale reuse). All resource modes strictly ≤200 GPU-hours.",
  "project_name": "decomp_spec_decode",
  "source": "web_research"
}
```

**Summary of changes (minor revision):**

1. **Budget strictly ≤200 GPU-h**: Llama trimmed to γ ∈ {4,16} (from {4,8,16}) and 5 methods (from 6); baseline reproduction reduced from 15h to 12h; buffer reduced from 20h to 12h (retaining 10h SWIFT contingency). All three modes now exactly ≤200h.

2. **Two new citations added with differentiation**:
   - *Tzachristas et al. (arXiv 2512.07647)*: Their gap-based Top-K certificates assume exact scores; DecompSpec extends to the prediction setting with bounded estimation error. Strengthens the rank-swap analysis by grounding it in an established framework.
   - *DeltaAttention (NeurIPS 2025)*: Validates the residual correction paradigm; DecompSpec applies it selectively to ~15% content-dependent heads during temporal prediction, not uniformly for truncation correction.

3. **Date errors fixed**: Beyond Exponential Decay → May 2025; SeerAttention-R → June 2025.

4. **TriAttention continuous-weighted replaces structural-only as baseline**: The key distinction is sharpened throughout: TriAttention's (1−R_f) weighting is *spatial* adaptation (across keys at one step); DecompSpec is *temporal* (across draft steps). The continuous-weighted baseline directly tests whether spatial adaptation alone addresses temporal staleness — the critical novelty-establishing comparison.

5. **Back-of-envelope throughput ceiling added**: Pessimistic 5-8%, moderate 10-15%, optimistic 15-20% gain over SparseSpec at γ=16, with ~0.5% scoring overhead.

6. **Acknowledged TriAttention's limited Qwen3-32B evaluation**: MRL validation for Qwen3-32B explicitly added to Phase 0 gating.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd1d2d9d-1161-4e45-b8b0-6080c292dca7",
  "isSidechain": false,
  "requestId": "req_011CauVtfApd2o69PLkNrwci",
  "type": "assistant",
  "uuid": "4d156d06-d532-4011-88ef-f586441032e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017z9oHavLXHBgq4V1zS8xsV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7238,
      "cache_read_input_tokens": 29084,
      "output_tokens": 16718,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7238,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16718,
          "cache_read_input_tokens": 29084,
          "cache_creation_input_tokens": 7238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7238
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

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Variance-Bounded Head-Adaptive Decomposition for Self-Speculative Reas…",
  "leafUuid": "4d156d06-d532-4011-88ef-f586441032e4",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Self-speculative decoding with head-adaptive sparse attention",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Variance-Bounded Head-Adaptive Decomposition for Self-Speculative Reas…",
  "leafUuid": "4d156d06-d532-4011-88ef-f586441032e4",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Self-speculative decoding with head-adaptive sparse attention",
  "sessionId": "5510b0f6-9c67-4418-9360-5f12db91350f"
}
```

---
