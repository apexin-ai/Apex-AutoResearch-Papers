# Paper Framing — redundancy-compound-sparsity

> Last updated: 2026-05-12 | Trigger: D005 (MLA misidentification)

> **⚠️ SUSPENDED**: D005 发现 DeepSeek-R1-Distill-Qwen-7B 是 Qwen2 GQA (4 KV heads)，不是 MLA。
> 下文所有 "MLA" 叙述（Claim 2, Section 5, Fig 1 等）**无事实基础**。
> 等 confound-ctrl-001 (DeepSeek-R1-Distill-Llama-8B) 结果后重写。
> 核心 confound: 推理模型 (长 CoT, 1353-3588 tok) vs 指令模型 (短回答, 623 tok)。

## Working Title
"When Does KV Redundancy Predict MLP Sparsity? Architecture Dependence of Cross-Axis Signals in Reasoning Inference"

## Target Venue
EMNLP 2026 ARR (DDL: 2026-05-25), Track: Efficient Methods for NLP

## Core Insight
The cross-axis redundancy hypothesis — that a single KV-similarity signal can drive both KV eviction and MLP sparsity — is NOT universally true or false. It is **architecture-dependent**: the hypothesis holds on standard GQA attention (Llama-3.1-8B: r=0.47, Δpert=+7%) but fails on Multi-head Latent Attention (DeepSeek-R1-7B: r=0.15, Δpert=-2%). MLA's latent compression destroys semantic fidelity in the KV space, breaking the information-content signal that links KV redundancy to MLP sparsity tolerance.

## Narrative Arc
1. **Setup**: Reasoning models generate redundant thinking traces. Multiple efficiency axes exist (KV eviction, MLP sparsity). Can one signal drive both? (Token Filtering + CLADA + Deja Vu motivate the question)
2. **Hypothesis**: EMA-based KV similarity predicts MLP sparsity tolerance via the chain: high KV similarity → low surprisal → high sparsity tolerance
3. **First result (unexpected negative)**: On DeepSeek-R1-7B (MLA), the hypothesis fails decisively. r=0.15, Δpert=-2.2% (inverted).
4. **Second result (unexpected positive)**: On Llama-3.1-8B (GQA), the hypothesis holds. r=0.47, Δpert=+6.6% (correct direction). Per-problem consistency: all 20 problems show r∈[0.42, 0.49].
5. **Resolution**: The difference is the attention architecture. MLA compresses KV into a low-rank latent space → cosine similarity in latent space no longer reflects token-level semantic redundancy. GQA preserves full-dimensional KV projections → cosine similarity retains semantic meaning.
6. **Per-layer analysis**: Cross-arch comparison of per-layer r and Δpert reveals where the signal breaks in MLA vs where it holds in GQA.
7. **Practical contribution**: (a) O(1) cross-axis coordination is viable for GQA-family models. (b) O(1) KV eviction works as standalone for all architectures.
8. **Design guideline**: Multi-axis efficiency systems must account for attention architecture; latent-compressed attention spaces are not suitable for semantic similarity-based signals.

## Core Claims
1. **Claim 1 (Primary)**: Cross-axis redundancy coordination (KV similarity → MLP sparsity) is architecture-dependent: it works on GQA but fails on MLA.
2. **Claim 2 (Mechanistic)**: MLA's latent compression destroys the semantic content of KV cosine similarity, breaking the information-content chain (KV sim → surprisal → sparsity tolerance).
3. **Claim 3 (Empirical depth)**: The architecture dependence manifests in both correlation strength (r: 0.15 vs 0.47) AND perturbation direction (Δpert: -2% vs +7%), with per-layer analysis revealing where the signal breaks.
4. **Claim 4 (Practical)**: EMA anchor similarity provides O(1) KV eviction competitive with O(n) methods, independent of attention architecture.

## Anticipated Reviewer Concerns & Responses
1. "Only two architectures — how generalizable?"
   → We test the two dominant attention paradigms (GQA: Llama family; MLA: DeepSeek family). Adding Mistral-7B (also GQA) would strengthen. The mechanism (latent compression) is specific to MLA, so the GQA finding should generalize.
2. "Δpert=+6.6% on Llama is modest"
   → The direction flip from -2.2% to +6.6% across architectures is the primary evidence. We also test higher sparsity levels (60-70%) where the gap may widen.
3. "Is this just a KV head count effect (4 vs 8)?"
   → We analyze per-head contributions. Even normalized per head, GQA shows stronger per-head signal.
4. "MLA explanation is speculative"
   → We provide: (a) per-layer r comparison showing WHERE signal degrades in MLA, (b) latent dimension analysis showing compressed representations lose angular structure.
5. "KV eviction contribution is incremental"
   → Same as before — standalone O(1) eviction is a practical bonus, not the core contribution.
6. "Why not just use surprisal directly?"
   → EMA similarity is O(1) from already-materialized projections; surprisal needs full vocab logit computation. The point is efficiency.

## Paper Structure
- Abstract
- 1. Introduction
- 2. Background (Token Filtering, CLADA, GQA vs MLA architectures)
- 3. Cross-Axis Hypothesis: Definition and Test Protocol
  - 3.1 EMA Anchor Signal Definition
  - 3.2 Validation Metrics (r, Δpert, K-S test)
  - 3.3 Pass/Fail Criteria
- 4. Results: Architecture Dependence
  - 4.1 GQA (Llama-3.1-8B): Hypothesis Holds (r=0.47, Δpert=+7%)
  - 4.2 MLA (DeepSeek-R1-7B): Hypothesis Fails (r=0.15, Δpert=-2%)
  - 4.3 Cross-Architecture Comparison
  - 4.4 Per-Layer Decomposition
  - 4.5 Per-Problem Consistency
  - 4.6 Sparsity Level Sweep (if Δpert pushed higher)
- 5. Why Does MLA Break the Signal?
  - 5.1 Latent Compression and Semantic Fidelity
  - 5.2 Per-Head Analysis
- 6. O(1) KV Eviction (Standalone Contribution)
  - 6.1 Method
  - 6.2 Benchmarks
- 7. Related Work
- 8. Discussion (Design Guidelines for Multi-Axis Efficiency)
- 9. Conclusion

## Key Figures (Planned)
- Fig 1: Architecture comparison diagram (GQA full-dim KV vs MLA latent KV) + r/Δpert summary
- Fig 2: Per-layer r heatmap — Llama vs DeepSeek side-by-side
- Fig 3: Per-layer Δpert comparison
- Fig 4: Per-problem r scatter (Llama vs DeepSeek)
- Fig 5: Sparsity sweep curves (Llama: Δpert vs sparsity level)
- Fig 6: KV eviction benchmark results
