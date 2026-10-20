# Paper Framing — ratekv

## Target Venue
- Primary: EMNLP 2026 Main (ARR submission)
- Deadline: ARR May 25, 2026 (11 days from today 2026-05-14)
- Track: Efficient Methods for NLP

## Core Insight

Per-head independent distortion profiling systematically underestimates joint degradation at extreme quantization levels due to compounding effects. A constrained MCKP formulation bridges this gap: cardinality constraints on extreme bit-widths act as principled regularization for profiler systematic errors, enabling automatic near-optimal per-head bit-width allocation for KV cache quantization.

## Core Claims (3 条)

1. **Head sensitivity heterogeneity**: Per-KV-head quantization sensitivity in modern LLMs is extremely non-uniform — Layer 0 heads exhibit 100× higher profiling delta than average, and 3.6% of heads determine 70%+ of total PPL degradation under uniform quantization.

2. **Constrained MCKP outperforms uniform and manual allocation**: A constrained MCKP solver over discrete bit-width action space {2,4,8,16}-bit with cardinality constraints achieves 27% PPL improvement over uniform 4-bit at matched 4× compression budget (11.23 vs 15.45), and outperforms hand-designed oracle strategies (11.23 vs 11.69).

3. **Cardinality constraints as profiler error regularization**: Unconstrained solvers that trust per-head independent profiling produce catastrophic allocations (PPL 36.92) because additive distortion models fail when many heads are simultaneously assigned extreme quantization. Cardinality constraints (≤k heads at 2-bit) regularize this non-additivity, and the optimal k can be determined by a small-scale compounding effect test.

## Story Spine

- **Problem**: KV cache quantization typically applies uniform bit-width across all heads, wasting budget on insensitive heads while under-protecting critical ones. Per-head mixed-precision allocation promises better quality-compression tradeoffs, but existing approaches (RateQuant's reverse waterfilling) assume continuous bit-width and additive distortion — both assumptions break in practice.

- **Existing approaches & gaps**: RateQuant (May 2026) provides R-D optimal per-head allocation via reverse waterfilling, but only for continuous bit-width selection and cannot handle discrete action sets or non-additive compounding effects. ARKV (March 2026) does per-layer heuristic selection but lacks per-head granularity and optimality guarantees. No existing method addresses the fundamental gap between independent per-head profiling and joint quantization effects.

- **Our framing**: We formulate per-head bit-width allocation as a constrained MCKP over discrete bit-widths. The key insight is that cardinality constraints on extreme quantization levels (2-bit) serve as principled regularization for profiler systematic errors — specifically, the non-additivity of extreme quantization that independent profiling cannot capture. This makes the solver robust to imperfect distortion estimates while preserving near-optimality.

- **Headline result template**: "On Qwen2.5-7B, constrained MCKP allocation achieves PPL 11.23 at 4× KV cache compression, a 27% improvement over uniform 4-bit (PPL 15.45) and better than hand-designed oracle strategies (PPL 11.69), with the solver automatically discovering that Layer 0 heads require 8-bit protection."

## Differentiation from RateQuant

| Aspect | RateQuant | Ours |
|--------|-----------|------|
| Bit-width selection | Continuous (reverse waterfilling) | Discrete MCKP ({2,4,8,16}-bit) |
| Distortion model | Additive, parametric D(b)=α·β^{-b} | Additive + cardinality regularization |
| Compounding effects | Not addressed | Explicitly handled via constraints |
| Action space | Homogeneous (quantization only) | Heterogeneous (multiple discrete bit-widths) |
| Optimality | Under additive assumption | Near-optimal with regularized profiling |

## Venue Fit Risks

- **Incrementality over RateQuant**: Strongest reviewer attack. Defense: (a) discrete MCKP is fundamentally different from continuous waterfilling, (b) compounding effect discovery and constraint-based regularization are novel contributions, (c) RateQuant's additive assumption demonstrably fails (PPL 36.92 vs 11.23).
- **Single-domain evaluation**: KV cache quantization only. Mitigate by testing across model families (Qwen, Llama, Mistral) with different GQA ratios.
- **No eviction arm**: Original idea proposed joint eviction+quantization. Eviction was abandoned after MVP (attention MSE fails as distortion proxy for eviction). Mention as negative finding in paper; the MCKP framework itself extends naturally to include eviction once better eviction distortion metrics are developed.

## Anticipated Reviewer Concerns

1. **"This is just RateQuant with MCKP instead of waterfilling"** → Show waterfilling fails on discrete action sets (counterexample); show unconstrained MCKP also fails (PPL 36.92); our contribution is the constraint-regularized formulation.
2. **"Only tested on one model"** → Multi-model experiments (Llama, Mistral) are P0.
3. **"Cardinality constraint is just a heuristic"** → Show it has principled motivation (compounding effect non-additivity); characterize the compounding threshold empirically; show constraint value k can be determined systematically.
4. **"How does this work at different compression ratios?"** → Budget sweep across 2×, 4×, 8× compression.
5. **"Profiler resolution is too low for mid-layer differentiation"** → High-res profiling experiment (64 seq × 2048 tokens) to explore.
