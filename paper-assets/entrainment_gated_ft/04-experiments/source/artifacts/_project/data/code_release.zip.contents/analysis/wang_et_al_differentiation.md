# Wang et al. (2025) vs Our Work: Differentiation Analysis

## Paper Information

- **Title**: A Systematic Analysis of Hybrid Linear Attention
- **Authors**: Dustin Wang, Rui-Jie Zhu, Steven Abreu, Yong Shan, Taylor Kergan, Yuqi Pan, Yuhong Chou, Zheng Li, Ge Zhang, Wenhao Huang, Jason Eshraghian
- **arXiv**: 2507.06457
- **Date**: July 8, 2025
- **Scope**: Trains 72 models (6 linear attention variants × 5 hybridization ratios × 2 scales) to answer "which linear attention + what ratio is best for hybrid architectures"

## Summary

Wang et al. is a **practitioner's architecture selection guide** — it systematically benchmarks 72 hybrid models to answer "which linear attention + what ratio is best." Our work asks a fundamentally different question: **"why do different architectures become more similar when attention is added, and through what per-example mechanism?"** They observe that rankings change after hybridization; we quantify the convergence, decompose it by task type and scale, and reveal that aggregate similarity masks architecture-specific per-example divergence.

---

## Verbatim Extractions from Wang et al.

### On Rankings Changing After Hybridization
- **Section 4.1**: "The relative performance of different architectures changes substantially when linear and full attention mechanisms are combined, making standalone scores unreliable predictors of hybrid performance."
- **Section 4.1**: "GatedDeltaNet achieves the highest standalone accuracy. However, when hybridized, HGRN2 at a 6:1 linear-to-full attention ratio outperforms it, exceeding both the Transformer baseline and the standalone leader by 1.2 percentage points."
- **Section 4.1** (1.3B): "The same pattern emerges at 1.3B parameters: GatedDeltaNet leads in standalone evaluation but becomes comparable with HGRN2 after hybridization."
- **Section 4.5**: "Hybrid quality cannot be inferred from standalone performance."

### On Performance Stability Across Ratios
- **Section 4.2**: "Language modeling performance remains largely flat across all ratio configurations. Most architectures cluster around 0.55-0.57 average LM score, with minimal variation."
- **Section 4.2**: "All architectures show a clear upward trend as the proportion of full-attention layers increases [for recall]."
- **Section 4.2**: "Most architectures approach or exceed this baseline at the 3:1 ratio, with some like DeltaNet and Gated-DeltaNet achieving their peak recall performance at this configuration."
- **Section 4.2**: "recall capability benefits substantially from increased full-attention allocation, unlike language modeling performance."

### On Perplexity Plateau
- **Section 2 (Related Work)**: "Empirically, long-context quality rises steeply once a few full-attention blocks or heads are present, after which perplexity plateaus; thus the linear:full ratio primarily controls recall."

### On Architectural Mechanisms
- **Section 4.3**: "Selective gating prevents catastrophic overwriting... Architectures that expose their hidden state to a learned, token-wise gate—GatedDeltaNet and HGRN-2—consistently perform best in recall once hybridised, surpassing the Transformer baseline by 2–5 percentage points."
- **Section 4.3**: "Hierarchical recurrence supplies multi-timescale context... this hierarchy doubles recall."
- **Section 4.3**: "Controlled forgetting curbs state crowding."
- **Section 4.3**: "Architectures lacking either gated or delta-style forgetting never reach Transformer-level recall, regardless of ratio."

### On Task Differences
- **Section 4.2**: "Single-Key, Multi-key, and QA sub tasks are noticeably affected by a changing ratio... Common Word Extraction and Frequent Word Extraction does not seem to correlate with the hybrid ratio."
- **Section 4.5**: "Recall—not perplexity—determines the optimal linear:full mix." (with "24:1 to 3:1 shift nearly doubling RULER recall while shifting language-model loss by less than 1%")

### On Scale
- **Section 5 (Limitations)**: "The analysis is confined to models up to 1.3B parameters, a 2,048-token context window, and block-wise mixing ratios. Whether the observed trade-offs persist at the 10B+ scale... remains open."

### On Diminishing Returns
- **Section 1 (Introduction)**: "simply increasing the state size of linear attention models yields diminishing returns."

### Convergence (Only Non-Performance Usage)
- **Section 2 (Related Work)**: "production models at Character.ai and MiniMax that converge on a 6–7:1 ratio" — refers to industry convergence on ratio choice, **not** performance convergence between architectures.

### Practical Recommendations
- **Section 4.5**: "Employ a gated, hierarchical backbone (e.g., HGRN-2 or GatedDeltaNet) with one soft-max attention layer for every 3–6 linear layers."
- **Section 5**: "when equipped with gating, hierarchical recurrence, and controlled forgetting, linear backbones can match Transformer-level recall at a fraction of the KV-cache cost; a 3:1–6:1 (linear:full) ratio provides a practical balance between memory and quality."

---

## Wang et al. Key Numerical Results

### Table 2 — 340M LM Performance (selected)

| Model | ARC-c | ARC-e | HellaSwag | LAMBADA | OBQA | PIQA | Avg |
|-------|-------|-------|-----------|---------|------|------|-----|
| GatedDeltaNet pure | 0.291 | 0.602 | 0.415 | 0.348 | 0.338 | 0.661 | 0.442 |
| HGRN2 6:1 | 0.300 | 0.617 | 0.436 | 0.347 | 0.346 | 0.690 | 0.456 |
| RetNet 24:1 | 0.287 | 0.574 | 0.411 | 0.309 | 0.364 | 0.672 | 0.436 |
| Transformer | 0.276 | 0.612 | 0.424 | 0.353 | 0.330 | 0.670 | 0.444 |

### Table 3 — 1.3B LM Performance (selected)

| Model | ARC-c | ARC-e | HellaSwag | LAMBADA | OBQA | PIQA | Avg |
|-------|-------|-------|-----------|---------|------|------|-----|
| GatedDeltaNet 24:1 | 0.410 | 0.733 | 0.598 | 0.502 | 0.406 | 0.741 | 0.565 |
| HGRN2 6:1 | 0.404 | 0.729 | 0.604 | 0.500 | 0.420 | 0.733 | 0.565 |
| RetNet 6:1 | 0.380 | 0.718 | 0.584 | 0.475 | 0.400 | 0.727 | 0.547 |
| Transformer | 0.395 | 0.704 | 0.589 | 0.474 | 0.400 | 0.729 | 0.548 |

### Table 4 — LM Performance Averaged Across Scales by Ratio

| Ratio | DeltaNet | GDN | GLA | HGRN | HGRN2 | RetNet | Avg |
|-------|----------|-----|-----|------|-------|--------|-----|
| 24:1 | 0.472 | 0.468 | 0.470 | 0.488 | 0.488 | 0.472 | 0.476 |
| 12:1 | 0.476 | 0.478 | 0.474 | 0.482 | 0.488 | 0.472 | 0.478 |
| 6:1 | 0.478 | 0.481 | 0.471 | 0.486 | 0.494 | 0.472 | 0.480 |
| 3:1 | 0.475 | 0.478 | 0.478 | 0.483 | 0.489 | 0.468 | 0.479 |
| pure | 0.472 | 0.487 | 0.459 | 0.459 | 0.486 | 0.471 | 0.472 |

Note: Range across architectures at any given ratio is ~0.02-0.03. They report this but **never compute cross-architecture variance or track its change with ratio**.

### Statistical Methods Used

**None.** Wang et al. report point estimates only — no p-values, no confidence intervals, no significance tests, no error bars. All evaluation is zero-shot without task-specific fine-tuning.

### Analysis Granularity

**Aggregate metrics only.** No per-example analysis, no error analysis, no sample-level decomposition.

---

## 4-Point Differentiation Table (Detailed)

### 1. Cross-Architecture Convergence Quantification

**Wang et al.**: Observe qualitatively that "the relative performance of different architectures changes substantially when linear and full attention mechanisms are combined" (Section 4.1) and that LM performance "remains largely flat" with architectures clustering around 0.55–0.57 (Section 4.2). Their Table 4 shows LM performance averaged across both scales (range ~0.468–0.494 across architectures at any ratio), and Figure 3 shows individual architecture curves. However, they **never compute any cross-architecture variance metric**. They do not quantify the *spread* between architectures or how it changes with attention ratio. The word "convergence" appears only once, in the Related Work section referring to industry adoption of the 6–7:1 ratio, not performance convergence.

**Our work**: We compute cross-architecture standard deviation at each attention ratio across all benchmarks, then test monotonic decrease with Spearman rank correlation + exact permutation test (n=5 ratio levels). For LAMBADA at 1.3B: ρ = −1.0, p = 0.0167 (exact permutation test, two-tailed, n=5); std decreases monotonically from 0.024 (pure) to 0.005 (h3-1), a 79% reduction. ARC-Easy and MMLU show suggestive convergence (ρ = −0.7, p = 0.2333 (exact permutation test, two-tailed, n=5) each — underpowered at n=5). HellaSwag, ARC-Challenge, and Winogrande show no convergence (ρ ≥ 0.1).

**Gap**: Wang et al. make a qualitative observation ("rankings change"). We provide a **quantitative convergence framework** with Spearman correlation, exact permutation p-values, and effect sizes. This transforms an anecdotal observation into a testable, reproducible phenomenon. Their closest claim — that architectures "cluster" — describes static similarity at one point, not the *dynamic process* of convergence across ratio levels.

---

### 2. Scale-Dependent Analysis

**Wang et al.**: Train at 340M (20B tokens) and 1.3B (100B tokens). Their cross-scale comparison is limited to confirming the same ranking inversion: "The same pattern emerges at 1.3B parameters: GatedDeltaNet leads in standalone evaluation but becomes comparable with HGRN2 after hybridization" (Section 4.1). They **never compare convergence strength across scales**. Table 4 averages performance across both scales, collapsing scale information. Limitations section acknowledges: "Whether the observed trade-offs persist at the 10B+ scale... remains open" (Section 5).

**Our work**: We directly compare equalizer effect intensity across scales on LAMBADA:
- **1.3B**: std drops monotonically 0.024 → 0.005 (79% reduction), ρ = −1.0, p = 0.0167 (exact permutation test, two-tailed, n=5)
- **340M**: std drops 0.025 → 0.011 at attn=4 (56% reduction) but **rebounds** to 0.015 at attn=8 (non-monotonic)
- The 1.3B convergence is approximately 1.4× stronger than 340M, and critically, the non-monotonic rebound at 340M (capacity bottleneck at high attention ratio) disappears at 1.3B

**Gap**: Wang et al. make a binary statement ("same pattern, both scales"). We quantify **how much stronger** the convergence is at 1.3B, identify a **scale-dependent qualitative difference** (non-monotonic rebound at 340M vs monotonic convergence at 1.3B), and propose a mechanistic explanation (capacity bottleneck — at 340M, the model lacks capacity to simultaneously support attention overhead and maintain architecture-specific strengths).

---

### 3. Per-Example Mechanism

**Wang et al.**: All analysis is at the aggregate benchmark level. No per-example, per-sample, or instance-level analysis appears anywhere in the paper. Their Section 4.3 (Architectural Determinants of Hybrid Effectiveness) analyzes *why certain architectures benefit more from hybridization* at the architecture level (selective gating, hierarchical recurrence, controlled forgetting), but never at the individual sample level.

**Our work**: We extract per-example accuracy changes (via lm-eval --log_samples) and compute:
- **Helped/hurt sample sets** per architecture (which specific examples improve/degrade when attention is added)
- **Pairwise Jaccard overlap** between architectures' helped sets: ~0.04–0.07 for retrieval tasks (near-zero overlap)
- **Net effect asymmetry**: GDN shows net negative effect on LAMBADA (more samples hurt than helped) while HGRN2 shows net positive on *different* samples
- **Feature characterization**: helped/hurt samples distinguished by target token frequency, context length, last-sentence perplexity, with architecture-specific profiles

**Gap**: This is our most distinctive contribution. Wang et al. see the aggregate picture ("HGRN2 improves with attention"). We reveal that beneath aggregate convergence, **each architecture is helped and hurt on almost entirely different examples** (Jaccard ~0.04–0.07). This is the core divergence finding: architectures look more similar in aggregate precisely because attention compensates different weaknesses on different samples. This level of analysis is completely absent from Wang et al.

---

### 4. Task-Specificity Characterization

**Wang et al.**: Make a coarse-grained distinction: LM performance "remains largely flat across ratios" vs. recall "significantly improves with increased full attention layers" (Section 4.2). Their RULER subtask analysis (Table 6) shows "Single-Key, Multi-key, and QA sub tasks are noticeably affected by a changing ratio... Common Word Extraction and Frequent Word Extraction does not seem to correlate with the hybrid ratio" (Section 4.2). This is a **ratio-sensitivity** analysis (which tasks benefit from more attention), not a **convergence-pattern** analysis (do architectures become more similar on different tasks at different rates).

**Our work**: We measure convergence strength (Spearman ρ of cross-arch std vs attention ratio) per benchmark:
- **LAMBADA** (retrieval-dependent): ρ = −1.0, p = 0.0167 (exact permutation test, two-tailed, n=5) — strong, monotonic convergence
- **ARC-Easy, MMLU** (mixed): ρ = −0.7, p = 0.2333 (exact permutation test, two-tailed, n=5) — suggestive convergence, underpowered
- **HellaSwag** (reasoning): ρ = +0.3, p = 0.6833 (exact permutation test, two-tailed, n=5) — no convergence
- **ARC-Challenge** (reasoning): ρ = +0.6, p = 0.35 (exact permutation test, two-tailed, n=5) — no convergence
- **Winogrande** (mixed): ρ = +0.1, p = 0.95 (exact permutation test, two-tailed, n=5) — no convergence

This yields a continuous spectrum: tasks with higher retrieval demand show stronger convergence, consistent with the interpretation that attention compensates architecture-specific retrieval weaknesses but cannot bridge reasoning capacity gaps.

**Gap**: Wang et al. ask "which tasks benefit more from attention?" (answer: recall tasks). We ask "on which tasks does attention make architectures more *similar*?" (answer: retrieval-grounded tasks, not reasoning tasks). These are orthogonal questions. Their "flat across ratios" observation does not distinguish whether the *spread between architectures* changes — all architectures could shift equally (no convergence) or differentially (convergence). We show the latter occurs selectively by task type.

---

## Differentiation Summary Table

| Dimension | Wang et al. | Ours | Status |
|---|---|---|---|
| **Convergence quantification** | Qualitative ("rankings change", architectures "cluster") | Spearman ρ + exact permutation test across 5 ratios × 3 architectures; LAMBADA ρ=−1.0 (p=0.017, exact permutation, two-tailed, n=5), std 0.024→0.005 | **Fully novel** |
| **Scale dependency** | Binary ("same pattern both scales"); Table 4 averages across scales | 1.3B: 79% reduction (monotonic); 340M: 56% (non-monotonic rebound); qualitative scale-dependent difference | **Fully novel** |
| **Per-example mechanism** | Not performed (aggregate metrics only, zero per-sample analysis) | Jaccard ~0.04–0.07, architecture-specific helped/hurt profiles, net effect asymmetry (GDN net−, HGRN2 net+) | **Fully novel** |
| **Task-specificity of convergence** | Ratio-sensitivity by task type ("recall benefits from attention") | Convergence-strength by task type: retrieval ρ=−1.0 vs reasoning ρ≥+0.1 (continuous spectrum) | **Fully novel** |
| **Phenomenon framed** | "Standalone ≠ hybrid" (practical observation) | "Aggregate-individual decoupling" (aggregate convergence via architecture-specific, non-overlapping per-example effects — a characterization finding) | **Fully novel** |

---

## Conclusion

All four differentiation dimensions are **fully novel** — none are incremental extensions of Wang et al.'s analysis. The relationship is complementary:

1. **Wang et al. provides infrastructure**: 72 controlled models, systematic benchmarking, architecture taxonomy. They answer "what happens" — which architectures work best in hybrid configurations and at what ratio.
2. **We provide analysis**: convergence quantification, per-example decomposition, scale-dependent characterization, task-type spectrum. We answer "why it happens and through what mechanism" — the equalizer effect and its per-example divergence.

Wang et al.'s closest observation to our work — that "rankings change" and architectures become "comparable" after hybridization — is made in passing as a factual observation supporting their architecture recommendation. They never treat it as a *phenomenon to be explained*. We formalize it as the equalizer effect, quantify it, decompose it, and reveal the per-example divergence beneath it.

**Assessment**: These differences are sufficient to constitute an independent contribution. A reviewer familiar with both papers should see them as complementary: Wang et al. built the model zoo and asked the engineering question; we used their models and asked the science question.
